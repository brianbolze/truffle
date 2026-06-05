#!/usr/bin/env python3
"""build_db — project the markdown store into a derived SQLite lens for cross-company aggregation.

Markdown stays the source of truth; this is a **regenerable cache, never authoritative** — the architecture's
rung-3 "derived index" ([_design/2026-05-30-architecture.md]). It exists for two consumers of the *telehealth
cohort*: a human browsing/querying in a SQLite GUI (Beekeeper), and an agent running ad-hoc SQL. Rebuild it
whenever the markdown changes (`python scripts/build_db.py`); query `_out/store.db`.

Scoped + fenced so it can't hand back a confident wrong answer — the lessons the 2026-06-04 sqlite-aggregation
probe paid for ([experiments/2026-06-04-sqlite-aggregation/CAVEATS.md], folded into QUERYING.md):

  - **No molecule column.** Grouping is `LIKE` on `what` (page-attested free text); a stored `molecule` key
    fragments "testosterone" into ~30 buckets (OFFERINGS rule 4). So we don't store one — group at query time.
  - **No price magnitude.** Only `price_verbatim` — a first-`$` grab is *wrong, not lossy* (`$749` for a
    $166/mo SKU; first-month teasers sort below real prices). No sortable price number exists to mislead.
  - **A count is never naked.** `sku_count` rides beside `enumeration` (the capture-scope signal) and a
    `catalog_breadth` rendering that flags a floor — so a `lines-omitted` count can't be sorted as a census
    (the Ro.co lie: it sorted dead-last at 8 SKUs off a weight-loss-only run, actually carrying ~36).
  - **Telehealth-scoped.** SKU/price rows are the telehealth cohort only, so a cross-type aggregate
    (`AVG(price)` over $/mo + take-rate + per-night) is structurally impossible. `companies` carries all
    profiles for browsing, but has no magnitude to mis-aggregate.

Stdlib + PyYAML (sqlite3 is stdlib). The roster parser is imported from `offeringscheck` — one lint-tested
source of truth for the table shape, so the two can't drift. Run `--check` for the drift self-test.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sqlite3
import sys
from typing import Any

try:
    import yaml
except ImportError:
    sys.exit("PyYAML not importable — `pip install pyyaml`.")

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
if SCRIPTS not in sys.path:  # so the sibling import works library-side too, not just when run as a script
    sys.path.insert(0, SCRIPTS)
from offeringscheck import SPINE_PREFIXES, parse_roster  # noqa: E402 — after the sys.path insert above

ROOT = os.environ.get("WEB_RESEARCH_HOME") or os.path.dirname(SCRIPTS)
STORE = os.path.join(ROOT, "store")
OUT = os.path.join(SCRIPTS, "_out")

# The capture-scope completeness signal (offerings.md frontmatter, schema 1.2; designed 2026-06-04). A fact
# about the *capture*, not the company. Read defensively — anything off-list → `unknown`, so the lens never
# over-claims; the lint (offeringscheck) is what enforces the value in the file.
ENUMERATION_VALUES = {"indexed-complete", "lines-omitted", "unknown"}

# The 8 telehealth cohort cuts (TELEHEALTH.md), in pack order — the cuts that actually separate players within
# the cohort (the universal profile classification reads ~identical across it). Drift-guarded by --check.
TELEHEALTH_CUTS = [
    "value_chain_role",
    "pharmacy_model",
    "audience",
    "compounding_posture",
    "anchor_category",
    "modality",
    "access_model",
    "pay_model",
]

# The standard profile.md frontmatter, carried verbatim for browsing (lists/maps → JSON text so the column
# stays queryable with json_extract / LIKE). No magnitude here — classification only, safe to GROUP BY.
PROFILE_FIELDS = [
    "name",
    "domain",
    "aliases",
    "parent",
    "owns",
    "entity_type",
    "target_market",
    "offering_category",
    "portfolio_shape",
    "business_model",
    "primary_industry",
    "description",
    "logo_url",
    "brand_colors",
    "fonts",
    "color_scheme",
    "design_framework",
    "socials",
    "external",
    "logos",
    "key_pages",
    "site_notes",
    "unverified_fields",
    "capture_method",
    "schema_version",
    "captured_at",
]


# --- parse ----------------------------------------------------------------------------------------
def frontmatter(path: str) -> dict[str, Any]:
    """The QUERYING.md canonical reader: the YAML between the first two `---` fences."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    return yaml.safe_load(text.split("---", 2)[1]) if text.startswith("---") else {}


def slug_of(path: str) -> str:
    return os.path.basename(os.path.dirname(path))


def enumeration_of(fm: dict[str, Any], text: str) -> str:
    """The capture-scope value, frontmatter-first (its confirmed home) with a permissive body fallback for
    files the convention hasn't reached yet. Off-list / absent → `unknown` — the lens never over-claims trust.
    """
    raw = fm.get("enumeration")
    if raw is None:
        m = re.search(r"enumeration[\"'`:\s]+(indexed-complete|lines-omitted|unknown)", text, re.I)
        raw = m.group(1) if m else None
    val = str(raw).strip().strip("`").lower() if raw is not None else ""
    return val if val in ENUMERATION_VALUES else "unknown"


def roster_rows(text: str) -> list[dict[str, str]]:
    """The `## Roster` table → spine-keyed SKU dicts. Reuses offeringscheck's committed, lint-tested walker;
    maps header→canonical column by NAME (robust to project-local extra columns — eden adds Form/Category),
    cleaning markdown emphasis/backticks from each cell. The one genuinely error-prone parse, imported once.
    """
    header, raw = parse_roster(text)
    if not header:
        return []
    hdr = [h.lower() for h in header]
    col = {pref: next((i for i, h in enumerate(hdr) if h.startswith(pref)), None) for pref in SPINE_PREFIXES}

    def cell(cells: list[str], pref: str) -> str:
        i = col[pref]
        return re.sub(r"[*`]", "", cells[i]).strip() if i is not None and i < len(cells) else ""

    rows: list[dict[str, str]] = []
    for cells in raw:
        if not cell(cells, "offering"):
            continue
        rows.append(
            {
                "offering": cell(cells, "offering"),
                "kind": cell(cells, "kind"),
                "parent": cell(cells, "parent"),
                "sku_slug": cell(cells, "slug"),
                "price_verbatim": cell(cells, "price"),
                "visibility": cell(cells, "visibility"),
                "what": cell(cells, "what"),
            }
        )
    return rows


def cell_value(value: Any) -> str | None:
    """Normalize a frontmatter value to a TEXT cell: None stays None, list/dict → JSON, scalar → str."""
    if value is None:
        return None
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


# --- build ----------------------------------------------------------------------------------------
def build(conn: sqlite3.Connection) -> dict[str, int]:
    """Project the markdown into the lens. `companies` = every profile (browsable classification, no magnitude);
    `telehealth` / `offerings` = the cohort only, so price/SKU aggregation is intra-cohort by construction.
    """
    cur = conn.cursor()
    cur.executescript(
        "DROP VIEW IF EXISTS telehealth_full; DROP VIEW IF EXISTS offerings_stats;"
        "DROP TABLE IF EXISTS companies; DROP TABLE IF EXISTS telehealth; DROP TABLE IF EXISTS offerings;"
    )
    cur.execute("CREATE TABLE companies (slug TEXT PRIMARY KEY, " + ", ".join(f'"{f}" TEXT' for f in PROFILE_FIELDS) + ")")
    cur.executescript(
        """
        CREATE TABLE telehealth (
          slug TEXT PRIMARY KEY, domain TEXT, value_chain_role TEXT, pharmacy_model TEXT,
          audience TEXT, compounding_posture TEXT, anchor_category TEXT, modality TEXT,
          access_model TEXT, pay_model TEXT, captured_at TEXT
        );
        CREATE TABLE offerings (
          slug TEXT, domain TEXT, offering TEXT, kind TEXT, parent TEXT, sku_slug TEXT,
          price_verbatim TEXT, visibility TEXT, what TEXT,
          offerings_captured_at TEXT, enumeration TEXT
        );
        """
    )
    n = {"companies": 0, "telehealth": 0, "offerings": 0, "skus": 0}

    insert_company = "INSERT INTO companies VALUES (" + ",".join("?" * (1 + len(PROFILE_FIELDS))) + ")"
    for path in sorted(glob.glob(os.path.join(STORE, "*", "profile.md"))):
        fm, slug = frontmatter(path), slug_of(path)
        cur.execute(insert_company, (slug, *[cell_value(fm.get(f)) for f in PROFILE_FIELDS]))
        n["companies"] += 1

    telehealth_slugs: set[str] = set()
    for path in sorted(glob.glob(os.path.join(STORE, "*", "telehealth.md"))):
        fm, slug = frontmatter(path), slug_of(path)
        telehealth_slugs.add(slug)
        cur.execute(
            "INSERT INTO telehealth VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (slug, fm.get("domain"), *[fm.get(cut) for cut in TELEHEALTH_CUTS], str(fm.get("captured_at"))),
        )
        n["telehealth"] += 1

    # offerings: the telehealth cohort ONLY — the scope fence that makes a cross-type aggregate impossible.
    for path in sorted(glob.glob(os.path.join(STORE, "*", "offerings.md"))):
        slug = slug_of(path)
        if slug not in telehealth_slugs:
            continue
        fm = frontmatter(path)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        enum = enumeration_of(fm, text)
        cap = str(fm.get("captured_at")) if fm.get("captured_at") is not None else None
        n["offerings"] += 1
        for r in roster_rows(text):
            cur.execute(
                "INSERT INTO offerings VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (
                    slug,
                    fm.get("domain"),
                    r["offering"],
                    r["kind"],
                    r["parent"],
                    r["sku_slug"],
                    r["price_verbatim"],
                    r["visibility"],
                    r["what"],
                    cap,
                    enum,
                ),
            )
            n["skus"] += 1

    # per-company offerings aggregates — the HONEST ones only: counts + visibility posture + molecule presence
    # (LIKE-membership, never an adjudicated lane). enumeration / offerings_captured_at are file-level constants,
    # so MAX() over the group just carries them through. NO price magnitude (the wall — CAVEATS #2).
    cur.execute(
        """
        CREATE VIEW offerings_stats AS
        SELECT slug,
          MAX(enumeration)                                             AS enumeration,
          MAX(offerings_captured_at)                                  AS offerings_captured_at,
          SUM(kind LIKE '%buyable%')                                  AS sku_count,
          SUM(kind = 'family')                                        AS line_count,
          SUM(kind LIKE '%buyable%' AND visibility='published')       AS published_skus,
          SUM(kind LIKE '%buyable%' AND visibility='partial')         AS partial_skus,
          SUM(kind LIKE '%buyable%' AND visibility='on-request')      AS gated_skus,
          ROUND(100.0 * SUM(kind LIKE '%buyable%' AND visibility='published')
                / NULLIF(SUM(kind LIKE '%buyable%'), 0))              AS pct_published,
          SUM(kind LIKE '%buyable%' AND (what LIKE '%semaglutide%' OR what LIKE '%tirzepatide%')) AS glp1_skus
        FROM offerings GROUP BY slug
        """
    )

    # the joined surface: profile + 8 cohort cuts + offerings aggregates, keyed on slug. A VIEW, not a table —
    # regenerates with the build, never goes stale. enumeration + catalog_breadth sit BEFORE the raw sku_count
    # so a count is never read naked: a `lines-omitted` count renders `≥N (floor)`, an `unknown` one `N
    # (unverified)`, and only an `indexed-complete` count is a bare number safe to rank on.
    cur.execute(
        """
        CREATE VIEW telehealth_full AS
        SELECT c.*,
               t.value_chain_role, t.pharmacy_model, t.audience, t.compounding_posture,
               t.anchor_category, t.modality, t.access_model, t.pay_model,
               t.captured_at AS telehealth_captured_at,
               s.offerings_captured_at,
               s.enumeration,
               CASE
                 WHEN s.enumeration='lines-omitted'   THEN '≥' || s.sku_count || ' (floor)'
                 WHEN s.enumeration='indexed-complete' THEN CAST(s.sku_count AS TEXT)
                 ELSE COALESCE(CAST(s.sku_count AS TEXT), '?') || ' (unverified)'
               END                                                     AS catalog_breadth,
               s.sku_count, s.line_count, s.published_skus, s.partial_skus, s.gated_skus,
               s.pct_published, s.glp1_skus
        FROM companies c
        JOIN telehealth t ON c.slug = t.slug
        LEFT JOIN offerings_stats s ON s.slug = c.slug
        """
    )
    conn.commit()
    return n


# --- drift self-test (--check) --------------------------------------------------------------------
def check(conn: sqlite3.Connection) -> list[str]:
    """Assert the lens's structural invariants — a schema change (a renamed roster column or cohort cut, a
    re-added footgun column) fails here loudly instead of misbuilding quietly. The querycheck-style sentinel.
    """
    fails: list[str] = []
    q = conn.execute

    for table in ("companies", "telehealth", "offerings"):
        if q(f"SELECT COUNT(*) FROM {table}").fetchone()[0] == 0:
            fails.append(f"{table}: 0 rows — a glob or parse broke (or the store is empty).")

    # footgun columns must stay gone — a regression guard against re-adding the laundered price / fake key.
    ocols = {r[1] for r in q("PRAGMA table_info(offerings)").fetchall()}
    for forbidden in ("molecule", "price_num", "price_unit", "promo_first_month"):
        if forbidden in ocols:
            fails.append(f"offerings: footgun column '{forbidden}' is back — it launders a wrong answer (see the module docstring).")

    # scope fence: every SKU row is a telehealth company, so no cross-type aggregate is possible.
    stray = q("SELECT COUNT(*) FROM offerings WHERE slug NOT IN (SELECT slug FROM telehealth)").fetchone()[0]
    if stray:
        fails.append(f"offerings: {stray} row(s) outside the telehealth cohort — the scope fence leaked.")

    # join density: every telehealth pack that has an offerings.md on disk must have contributed rows
    # (a roster that silently failed to parse — e.g. a spine rename — drops out here).
    on_disk = {
        slug_of(p)
        for p in glob.glob(os.path.join(STORE, "*", "offerings.md"))
        if slug_of(p) in {r[0] for r in q("SELECT slug FROM telehealth").fetchall()}
    }
    in_db = {r[0] for r in q("SELECT DISTINCT slug FROM offerings").fetchall()}
    missing = on_disk - in_db
    if missing:
        fails.append(f"offerings: {sorted(missing)} have an offerings.md but produced no rows — a roster parse failed (spine rename?).")

    # the 8 cohort cuts are present as columns (a rename in TELEHEALTH.md would silently drop one).
    tcols = {r[1] for r in q("PRAGMA table_info(telehealth)").fetchall()}
    for cut in TELEHEALTH_CUTS:
        if cut not in tcols:
            fails.append(f"telehealth: cohort cut '{cut}' is not a column — renamed in TELEHEALTH.md?")

    # enumeration only ever holds closed-set values (the never-read-naked guard depends on it).
    vals = {r[0] for r in q("SELECT DISTINCT enumeration FROM offerings").fetchall()}
    bad = vals - ENUMERATION_VALUES
    if bad:
        fails.append(f"offerings: off-list enumeration value(s) {sorted(bad)} — not in {sorted(ENUMERATION_VALUES)}.")

    # the joined view resolves and is intra-cohort (one row per telehealth company).
    vfull = q("SELECT COUNT(*) FROM telehealth_full").fetchone()[0]
    nth = q("SELECT COUNT(*) FROM telehealth").fetchone()[0]
    if vfull != nth:
        fails.append(f"telehealth_full: {vfull} rows ≠ {nth} telehealth companies — the join changed cardinality.")

    return fails


# --- CLI ------------------------------------------------------------------------------------------
def _summary(conn: sqlite3.Connection, n: dict[str, int]) -> None:
    th_with_off = conn.execute("SELECT COUNT(DISTINCT t.slug) FROM telehealth t JOIN offerings o ON o.slug=t.slug").fetchone()[0]
    print(f"  companies:  {n['companies']}  (all profiles — browsable classification, no magnitude)")
    print(f"  telehealth: {n['telehealth']}")
    print(f"  offerings:  {n['offerings']} files (telehealth-scoped) → {n['skus']} SKU rows")
    print(f"  telehealth ∩ offerings (joinable): {th_with_off}/{n['telehealth']}")
    print("\n  telehealth_full sample — breadth reads through enumeration, never a naked count:")
    print(f"    {'breadth':>16}  {'enum':<16} {'%pub':>4} {'glp1':>4}  brand")
    for r in conn.execute(
        """SELECT catalog_breadth, enumeration, pct_published, glp1_skus, name
           FROM telehealth_full ORDER BY sku_count DESC NULLS LAST LIMIT 8"""
    ):
        print(f"    {str(r[0]):>16}  {str(r[1]):<16} {str(r[2]) + '%':>4} {r[3]:>4}  {r[4]}")


def main() -> None:
    ap = argparse.ArgumentParser(description="build the derived SQLite lens over the markdown store (telehealth cohort)")
    ap.add_argument("--check", action="store_true", help="drift self-test: build in-memory and assert invariants (exit nonzero on drift)")
    ap.add_argument("--db", default=os.path.join(OUT, "store.db"), help="output path (default: scripts/_out/store.db)")
    args = ap.parse_args()

    if args.check:
        conn = sqlite3.connect(":memory:")
        build(conn)
        fails = check(conn)
        conn.close()
        n = len(fails)
        if fails:
            for f in fails:
                print("FAIL:", f)
            sys.exit(f"\n{n} failure(s) — the lens drifted from the store contract.")
        print("build_db --check: OK — the lens's structural invariants hold.")
        return

    os.makedirs(OUT, exist_ok=True)
    if os.path.exists(args.db):
        os.remove(args.db)
    conn = sqlite3.connect(args.db)
    n = build(conn)
    print(f"built {args.db}")
    _summary(conn, n)
    conn.close()


if __name__ == "__main__":
    main()
