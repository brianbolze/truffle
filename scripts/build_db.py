#!/usr/bin/env python3
"""build_db — project the markdown store into a derived SQLite lens for cross-company aggregation.

Markdown stays the source of truth; this is a **regenerable cache, never authoritative** — the architecture's
rung-3 "derived index" ([_design/2026-05-30-architecture.md]). It exists for two consumers: a human
browsing/querying in a SQLite GUI (Beekeeper), and an agent running ad-hoc SQL. Rebuild it before reading
(`python scripts/build_db.py`); query `_out/store.db`.

Corpus-wide + fenced so it can't hand back a confident wrong answer — the lessons the 2026-06-04
sqlite-aggregation probe paid for ([experiments/2026-06-04-sqlite-aggregation/CAVEATS.md], folded into
QUERYING.md):

  - **No molecule column.** Grouping is `LIKE` on `what` (page-attested free text); a stored `molecule` key
    fragments "testosterone" into ~30 buckets (OFFERINGS rule 4). So we don't store one — group at query time.
  - **No price magnitude.** Only `price_verbatim` — a first-`$` grab is *wrong, not lossy* (`$749` for a
    $166/mo SKU; first-month teasers sort below real prices). No sortable price number exists to mislead.
  - **A count is never naked.** `sku_count` rides beside `enumeration` (the capture-scope signal) and a
    `catalog_breadth` rendering that flags a floor — so a `lines-omitted` count can't be sorted as a census
    (the Ro.co lie: it sorted dead-last at 8 SKUs off a weight-loss-only run, actually carrying ~36).
  - **Corpus-wide lookup, cohort-gated ranking.** `offerings` carries every roster so "who sells X" doesn't
    silently miss non-telehealth companies. Ranking/count surfaces stay inside cohort views like
    `telehealth_full`, so Ford and Hims don't land in the same league table.
  - **Freshness lives in the db.** `_meta` holds `built_at`, row counts, and caveat rows; `_meta_days_old`
    recomputes age on every open. `coverage` is the folder manifest with module presence and clocks.

Stdlib + PyYAML (sqlite3 is stdlib). The roster parser is imported from `offeringscheck` — one lint-tested
source of truth for the table shape, so the two can't drift. Run `--check` for the drift self-test.
"""

from __future__ import annotations

import argparse
import datetime as dt
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
OUT = os.path.join(ROOT, "_out")

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
    "legal_entity",
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


def captured_at(fm: dict[str, Any]) -> str | None:
    val = fm.get("captured_at")
    return str(val) if val is not None else None


def store_slugs() -> list[str]:
    return sorted(os.path.basename(d) for d in glob.glob(os.path.join(STORE, "*")) if os.path.isdir(d))


def write_meta(cur: sqlite3.Cursor, n: dict[str, int]) -> None:
    built_at = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    rows = [
        (10, "build", "built_at", built_at, built_at),
        (20, "count", "store_folders", str(n["folders"]), built_at),
        (30, "count", "companies", str(n["companies"]), built_at),
        (40, "count", "coverage_rows", str(n["coverage"]), built_at),
        (50, "count", "telehealth", str(n["telehealth"]), built_at),
        (60, "count", "offerings_files", str(n["offerings"]), built_at),
        (70, "count", "offering_rows", str(n["skus"]), built_at),
        (80, "caveat", "counts_are_floors", "counts are floors — read enumeration and catalog_breadth", built_at),
        (90, "caveat", "no_price_number", "no price number exists — price_verbatim only", built_at),
        (100, "caveat", "cohort_gated_ranking", "ranking surfaces live in <cohort>_full views", built_at),
        (110, "rule", "rebuild_before_read", "rebuild before you read; reconnect GUI clients after rebuild", built_at),
    ]
    cur.executemany("INSERT INTO _meta VALUES (?,?,?,?,?)", rows)


# --- build ----------------------------------------------------------------------------------------
def build(conn: sqlite3.Connection) -> dict[str, int]:
    """Project the markdown into the lens.

    `companies` = every profile (browsable classification, no magnitude).
    `coverage` = every store folder, including stubs and per-module clocks.
    `offerings` = every roster row in the corpus.
    `<cohort>_full` views = the only ranking surfaces.
    """
    cur = conn.cursor()
    cur.executescript(
        """
        DROP VIEW IF EXISTS _meta_days_old;
        DROP VIEW IF EXISTS telehealth_full;
        DROP VIEW IF EXISTS offerings_stats;
        DROP TABLE IF EXISTS _meta;
        DROP TABLE IF EXISTS coverage;
        DROP TABLE IF EXISTS companies;
        DROP TABLE IF EXISTS telehealth;
        DROP TABLE IF EXISTS offerings;
        """
    )
    cur.executescript(
        """
        CREATE TABLE _meta (
          sort_order INTEGER PRIMARY KEY, kind TEXT, item TEXT, value TEXT, built_at TEXT
        );
        CREATE TABLE coverage (
          slug TEXT PRIMARY KEY, domain TEXT,
          has_profile INTEGER NOT NULL, has_offerings INTEGER NOT NULL, has_telehealth INTEGER NOT NULL,
          profile_captured_at TEXT, offerings_captured_at TEXT, telehealth_captured_at TEXT,
          enumeration TEXT
        );
        """
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
    slugs = store_slugs()
    n = {"folders": len(slugs), "coverage": 0, "companies": 0, "telehealth": 0, "offerings": 0, "skus": 0}

    insert_company = "INSERT INTO companies VALUES (" + ",".join("?" * (1 + len(PROFILE_FIELDS))) + ")"
    for slug in slugs:
        slug_dir = os.path.join(STORE, slug)
        profile_path = os.path.join(slug_dir, "profile.md")
        telehealth_path = os.path.join(slug_dir, "telehealth.md")
        offerings_path = os.path.join(slug_dir, "offerings.md")

        profile_fm = frontmatter(profile_path) if os.path.exists(profile_path) else {}
        telehealth_fm = frontmatter(telehealth_path) if os.path.exists(telehealth_path) else {}
        offerings_fm: dict[str, Any] = {}
        offerings_text = ""
        enum = None

        if os.path.exists(profile_path):
            cur.execute(insert_company, (slug, *[cell_value(profile_fm.get(f)) for f in PROFILE_FIELDS]))
            n["companies"] += 1

        if os.path.exists(telehealth_path):
            cur.execute(
                "INSERT INTO telehealth VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (slug, telehealth_fm.get("domain"), *[telehealth_fm.get(cut) for cut in TELEHEALTH_CUTS], captured_at(telehealth_fm)),
            )
            n["telehealth"] += 1

        if os.path.exists(offerings_path):
            offerings_fm = frontmatter(offerings_path)
            with open(offerings_path, encoding="utf-8") as fh:
                offerings_text = fh.read()
            enum = enumeration_of(offerings_fm, offerings_text)
            cap = captured_at(offerings_fm)
            n["offerings"] += 1
            for r in roster_rows(offerings_text):
                cur.execute(
                    "INSERT INTO offerings VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        slug,
                        offerings_fm.get("domain"),
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

        domain = profile_fm.get("domain") or offerings_fm.get("domain") or telehealth_fm.get("domain")
        cur.execute(
            "INSERT INTO coverage VALUES (?,?,?,?,?,?,?,?,?)",
            (
                slug,
                domain,
                int(os.path.exists(profile_path)),
                int(os.path.exists(offerings_path)),
                int(os.path.exists(telehealth_path)),
                captured_at(profile_fm),
                captured_at(offerings_fm),
                captured_at(telehealth_fm),
                enum,
            ),
        )
        n["coverage"] += 1

    # Per-company offerings aggregates — the HONEST ones only: counts + visibility posture + molecule presence
    # (LIKE-membership, never an adjudicated lane). This is deliberately cohort-gated; the corpus table is for
    # membership/lookup, not cross-type league tables.
    cur.execute(
        """
        CREATE VIEW offerings_stats AS
        SELECT o.slug,
          MAX(o.enumeration)                                             AS enumeration,
          MAX(o.offerings_captured_at)                                  AS offerings_captured_at,
          SUM(o.kind LIKE '%buyable%')                                  AS sku_count,
          SUM(o.kind = 'family')                                        AS line_count,
          SUM(o.kind LIKE '%buyable%' AND o.visibility='published')     AS published_skus,
          SUM(o.kind LIKE '%buyable%' AND o.visibility='partial')       AS partial_skus,
          SUM(o.kind LIKE '%buyable%' AND o.visibility='on-request')    AS gated_skus,
          ROUND(100.0 * SUM(o.kind LIKE '%buyable%' AND o.visibility='published')
                / NULLIF(SUM(o.kind LIKE '%buyable%'), 0))              AS pct_published,
          SUM(o.kind LIKE '%buyable%' AND (o.what LIKE '%semaglutide%' OR o.what LIKE '%tirzepatide%')) AS glp1_skus
        FROM offerings o
        JOIN telehealth t ON t.slug = o.slug
        GROUP BY o.slug
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
    cur.execute(
        """
        CREATE VIEW _meta_days_old AS
        SELECT MIN(built_at) AS built_at,
               ROUND(julianday('now') - julianday(MIN(built_at)), 3) AS days_old
        FROM _meta
        """
    )
    write_meta(cur, n)
    conn.commit()
    return n


# --- drift self-test (--check) --------------------------------------------------------------------
def check(conn: sqlite3.Connection) -> list[str]:
    """Assert the lens's structural invariants — a schema change (a renamed roster column or cohort cut, a
    re-added footgun column) fails here loudly instead of misbuilding quietly. The querycheck-style sentinel.
    """
    fails: list[str] = []
    q = conn.execute

    for table in ("_meta", "coverage", "companies", "telehealth", "offerings"):
        if q(f"SELECT COUNT(*) FROM {table}").fetchone()[0] == 0:
            fails.append(f"{table}: 0 rows — a glob or parse broke (or the store is empty).")

    # Footgun columns must stay gone everywhere — a regression guard against re-adding the laundered price /
    # fake key. SQLite will happily coerce leading-digit TEXT in AVG(); the fence is that no numeric price
    # column exists in the lens.
    relations = q(
        "SELECT name, type FROM sqlite_master WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%'"
    ).fetchall()
    for name, _kind in relations:
        cols = q(f'PRAGMA table_info("{name}")').fetchall()
        for col in cols:
            cname = col[1].lower()
            ctype = (col[2] or "").upper()
            if cname == "molecule" or cname in {"price", "price_num", "price_numeric", "price_value", "price_unit", "promo_first_month"}:
                fails.append(f"{name}: footgun column '{col[1]}' is back — it launders a wrong answer.")
            if cname.startswith("price_") and cname != "price_verbatim":
                fails.append(f"{name}: unsupported price column '{col[1]}' — only price_verbatim is allowed.")
            if "price" in cname and ctype and not ctype.startswith("TEXT"):
                fails.append(f"{name}: price column '{col[1]}' has non-TEXT type {ctype} — no price magnitude allowed.")

    # coverage density: every store folder gets exactly one manifest row, including stubs.
    folders = set(store_slugs())
    covered = {r[0] for r in q("SELECT slug FROM coverage").fetchall()}
    if folders != covered:
        fails.append(
            f"coverage: folder manifest mismatch — missing {sorted(folders - covered)}, extra {sorted(covered - folders)}."
        )

    # join density: every roster on disk must have contributed rows (not just telehealth). This catches the
    # silent-drop bug this corpus-wide lens exists to kill.
    # (a roster that silently failed to parse — e.g. a spine rename — drops out here).
    on_disk = {slug_of(p) for p in glob.glob(os.path.join(STORE, "*", "offerings.md"))}
    in_db = {r[0] for r in q("SELECT DISTINCT slug FROM offerings").fetchall()}
    missing = on_disk - in_db
    if missing:
        fails.append(f"offerings: {sorted(missing)} have an offerings.md but produced no rows — a roster parse failed (spine rename?).")

    # ranking remains cohort-gated even though the base offerings table is corpus-wide.
    stats_stray = q("SELECT COUNT(*) FROM offerings_stats WHERE slug NOT IN (SELECT slug FROM telehealth)").fetchone()[0]
    if stats_stray:
        fails.append(f"offerings_stats: {stats_stray} non-telehealth row(s) — cohort ranking fence leaked.")

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

    cvals = {r[0] for r in q("SELECT DISTINCT enumeration FROM coverage WHERE enumeration IS NOT NULL").fetchall()}
    cbad = cvals - ENUMERATION_VALUES
    if cbad:
        fails.append(f"coverage: off-list enumeration value(s) {sorted(cbad)} — not in {sorted(ENUMERATION_VALUES)}.")

    meta_items = {r[0] for r in q("SELECT item FROM _meta").fetchall()}
    for item in ("built_at", "counts_are_floors", "no_price_number", "cohort_gated_ranking"):
        if item not in meta_items:
            fails.append(f"_meta: missing trust row {item!r}.")
    days_old = q("SELECT days_old FROM _meta_days_old").fetchone()[0]
    if days_old is None or days_old < 0:
        fails.append("_meta_days_old: live freshness view did not produce a non-negative days_old.")

    # the joined view resolves and is intra-cohort (one row per telehealth company).
    vfull = q("SELECT COUNT(*) FROM telehealth_full").fetchone()[0]
    nth = q("SELECT COUNT(*) FROM telehealth").fetchone()[0]
    if vfull != nth:
        fails.append(f"telehealth_full: {vfull} rows ≠ {nth} telehealth companies — the join changed cardinality.")

    return fails


# --- CLI ------------------------------------------------------------------------------------------
def _summary(conn: sqlite3.Connection, n: dict[str, int]) -> None:
    th_with_off = conn.execute("SELECT COUNT(DISTINCT t.slug) FROM telehealth t JOIN offerings o ON o.slug=t.slug").fetchone()[0]
    corpus_with_off = conn.execute("SELECT COUNT(DISTINCT slug) FROM offerings").fetchone()[0]
    stubs = conn.execute("SELECT COUNT(*) FROM coverage WHERE has_profile=0").fetchone()[0]
    built_at, days_old = conn.execute("SELECT built_at, days_old FROM _meta_days_old").fetchone()
    print(f"  _meta:     built_at {built_at} ({days_old}d old via live view)")
    print(f"  coverage:  {n['coverage']} folders ({stubs} stubs)")
    print(f"  companies: {n['companies']}  (all profiles — browsable classification, no magnitude)")
    print(f"  telehealth: {n['telehealth']}")
    print(f"  offerings:  {n['offerings']} files (corpus-wide) → {n['skus']} SKU rows across {corpus_with_off} companies")
    print(f"  telehealth ∩ offerings (joinable): {th_with_off}/{n['telehealth']}")
    print("\n  telehealth_full sample — breadth reads through enumeration, never a naked count:")
    print(f"    {'breadth':>16}  {'enum':<16} {'%pub':>4} {'glp1':>4}  brand")
    for r in conn.execute(
        """SELECT catalog_breadth, enumeration, pct_published, glp1_skus, name
           FROM telehealth_full ORDER BY sku_count DESC NULLS LAST LIMIT 8"""
    ):
        print(f"    {str(r[0]):>16}  {str(r[1]):<16} {str(r[2]) + '%':>4} {r[3]:>4}  {r[4]}")


def main() -> None:
    ap = argparse.ArgumentParser(description="build the corpus-wide derived SQLite lens over the markdown store")
    ap.add_argument("--check", action="store_true", help="drift self-test: build in-memory and assert invariants (exit nonzero on drift)")
    ap.add_argument("--db", default=os.path.join(OUT, "store.db"), help="output path (default: _out/store.db)")
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
        print("build_db --check: OK — the corpus lens's structural invariants hold.")
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
