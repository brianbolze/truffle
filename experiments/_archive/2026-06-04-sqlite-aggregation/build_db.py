#!/usr/bin/env python3
"""build_db — project the markdown store into a derived SQLite lens (companies ⋈ telehealth ⋈ offerings).

Throwaway probe for the parked rung-3 SQLite item. The point isn't speed (coded-queries settled that);
it's whether the one-to-many `offerings` roster × the `telehealth` cohort cuts create a JOIN/GROUP demand
that earns a real database. Markdown stays source-of-truth — this is a regenerable lens, rebuilt each run.

Two columns are deliberately lossy, to probe the price wall honestly:
  - `molecule`  — the lead `·` token of a roster row's `What` cell (page-attested free text, NOT a clean key)
  - `price_num` / `price_unit` — first `$`-figure + cadence parsed out of the verbatim price string

Stdlib + PyYAML (sqlite3 is stdlib — no new dep). Run: `python build_db.py` → writes _out/store.db + a summary.
"""

from __future__ import annotations

import glob
import os
import re
import sqlite3
import sys
from typing import Any

try:
    import yaml
except ImportError:
    sys.exit("PyYAML not importable — `pip install pyyaml`.")

ROOT = os.environ.get("WEB_RESEARCH_HOME") or os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
STORE = os.path.join(ROOT, "store")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_out")


# --- parse ----------------------------------------------------------------------------------------
def frontmatter(path: str) -> dict[str, Any]:
    """The QUERYING.md canonical reader: the YAML between the first two `---` fences."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    return yaml.safe_load(text.split("---", 2)[1]) if text.startswith("---") else {}


def body(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    return text.split("---", 2)[2] if text.startswith("---") else text


def slug_of(path: str) -> str:
    return os.path.basename(os.path.dirname(path))


def molecule_of(what: str) -> str | None:
    """Lead `·` token of a `What` cell, cleaned. None for devices (`—`) / `not stated`.

    Deliberately heuristic: the molecule is page-attested free text (OFFERINGS rule 4 — never a stored
    canonical key), so this lead-token grab is exactly the kind of lossy normalization the store refuses
    to bake. We do it here only to see how clean a GROUP BY molecule comes out.
    """
    head = re.split(r"·", what)[0]
    head = re.sub(r"[*_`]", "", head).strip().lower()
    if head in ("", "—", "-", "not stated", "n/a"):
        return None
    return head


def price_of(verbatim: str) -> tuple[float | None, str | None, bool]:
    """(price_num, price_unit, promo_first_month) — first `$`-figure + cadence. Intentionally crude.

    This is the wall: a verbatim price like `$39 for the first month, auto-renews at $149/month` collapses
    to a single number + unit only by *throwing away* the structure that makes it correct. We capture the
    breakage, not paper over it.
    """
    m = re.search(r"\$\s?([\d,]+(?:\.\d+)?)", verbatim)
    num = float(m.group(1).replace(",", "")) if m else None
    unit = None
    low = verbatim.lower()
    if re.search(r"/\s*mo|/\s*month|per month|per mo\b", low):
        unit = "/mo"
    elif re.search(r"/\s*yr|/\s*year|per year|per yr\b", low):
        unit = "/yr"
    elif re.search(r"per use|/\s*use|per dose|/\s*dose", low):
        unit = "/use"
    elif num is not None:
        unit = "flat"
    promo = "first month" in low or "first mo" in low
    return num, unit, promo


# header-name → canonical column. Roster cols vary (eden adds Form/Category) so we key on NAME, not index.
def col_map(header_cells: list[str]) -> dict[int, str]:
    out: dict[int, str] = {}
    for i, raw in enumerate(header_cells):
        h = raw.strip().lower()
        if h.startswith("offering"):
            out[i] = "offering"
        elif h.startswith("kind"):
            out[i] = "kind"
        elif h.startswith("parent"):
            out[i] = "parent"
        elif h.startswith("slug"):
            out[i] = "slug"
        elif h.startswith("price"):
            out[i] = "price_verbatim"
        elif h.startswith("visibility"):
            out[i] = "visibility"
        elif h.startswith("what"):
            out[i] = "what"
    return out


def split_row(line: str) -> list[str]:
    cells = line.split("|")
    if cells and not cells[0].strip():
        cells = cells[1:]
    if cells and not cells[-1].strip():
        cells = cells[:-1]
    return cells


def parse_roster(path: str) -> list[dict[str, Any]]:
    """Pull the `## Roster` markdown table into row dicts, header-keyed. Robust to extra project-local cols."""
    rows: list[dict[str, Any]] = []
    lines = body(path).splitlines()
    cols: dict[int, str] | None = None
    for line in lines:
        if not line.lstrip().startswith("|"):
            if cols is not None:
                cols = None  # left the table
            continue
        cells = split_row(line)
        if cols is None:
            if any("offering" in c.lower() for c in cells) and any("kind" in c.lower() for c in cells):
                cols = col_map(cells)
            continue
        if all(set(c.strip()) <= {"-", ":"} for c in cells):  # separator row
            continue
        rec = {v: "" for v in ("offering", "kind", "parent", "slug", "price_verbatim", "visibility", "what")}
        for i, cell in enumerate(cells):
            if i in cols:
                rec[cols[i]] = re.sub(r"[*`]", "", cell).strip()
        if not rec["offering"]:
            continue
        rows.append(rec)
    return rows


# the full standard profile.md frontmatter — "all standard company profile fields" (carried verbatim;
# lists/maps land as JSON text so the column stays queryable with json_extract / LIKE).
PROFILE_FIELDS = [
    "name", "domain", "aliases", "parent", "owns", "entity_type", "target_market",
    "offering_category", "portfolio_shape", "business_model", "primary_industry", "description",
    "logo_url", "brand_colors", "fonts", "color_scheme", "design_framework", "socials", "external",
    "logos", "key_pages", "site_notes", "unverified_fields", "capture_method", "schema_version",
    "captured_at",
]


def cell(value: Any) -> str | None:
    """Normalize a frontmatter value to a TEXT cell: None stays None, list/dict → JSON, scalar → str."""
    import json

    if value is None:
        return None
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


# --- build ----------------------------------------------------------------------------------------
def build(conn: sqlite3.Connection) -> dict[str, int]:
    cur = conn.cursor()
    cur.executescript(
        "DROP VIEW IF EXISTS telehealth_full; DROP VIEW IF EXISTS offerings_stats;"
        "DROP TABLE IF EXISTS companies; DROP TABLE IF EXISTS telehealth; DROP TABLE IF EXISTS offerings;"
    )
    cur.execute(
        "CREATE TABLE companies (slug TEXT PRIMARY KEY, "
        + ", ".join(f'"{f}" TEXT' for f in PROFILE_FIELDS)
        + ")"
    )
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
          molecule TEXT, price_num REAL, price_unit TEXT, promo_first_month INTEGER
        );
        """
    )
    n = {"companies": 0, "telehealth": 0, "offerings": 0, "skus": 0}

    insert_company = (
        "INSERT INTO companies VALUES (" + ",".join("?" * (1 + len(PROFILE_FIELDS))) + ")"
    )
    for path in sorted(glob.glob(os.path.join(STORE, "*", "profile.md"))):
        fm, slug = frontmatter(path), slug_of(path)
        cur.execute(insert_company, (slug, *[cell(fm.get(f)) for f in PROFILE_FIELDS]))
        n["companies"] += 1

    for path in sorted(glob.glob(os.path.join(STORE, "*", "telehealth.md"))):
        fm, slug = frontmatter(path), slug_of(path)
        cur.execute(
            "INSERT INTO telehealth VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (slug, fm.get("domain"), fm.get("value_chain_role"), fm.get("pharmacy_model"),
             fm.get("audience"), fm.get("compounding_posture"), fm.get("anchor_category"),
             fm.get("modality"), fm.get("access_model"), fm.get("pay_model"), str(fm.get("captured_at"))),
        )
        n["telehealth"] += 1

    for path in sorted(glob.glob(os.path.join(STORE, "*", "offerings.md"))):
        fm, slug = frontmatter(path), slug_of(path)
        n["offerings"] += 1
        for r in parse_roster(path):
            num, unit, promo = price_of(r["price_verbatim"])
            cur.execute(
                "INSERT INTO offerings VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (slug, fm.get("domain"), r["offering"], r["kind"], r["parent"], r["slug"],
                 r["price_verbatim"], r["visibility"], r["what"],
                 molecule_of(r["what"]), num, unit, int(promo)),
            )
            n["skus"] += 1

    # per-company offerings aggregates — the HONEST ones: counts, price-visibility posture, molecule presence.
    # all are over-the-roster facts that don't launder the price wall. The two price columns are the lone
    # magnitude stat, deliberately narrow: the *published, monthly* band only (mixing /use + /yr + promo
    # floors would be a lie) — and even this is a floor-y range, not a comparable number. `buyable` excludes
    # family umbrella rows; molecule presence is LIKE-membership (page-attested text), never an adjudicated lane.
    cur.execute(
        """
        CREATE VIEW offerings_stats AS
        SELECT slug,
          SUM(kind LIKE '%buyable%')                                    AS sku_count,
          SUM(kind = 'family')                                          AS line_count,
          SUM(kind LIKE '%buyable%' AND visibility='published')         AS published_skus,
          SUM(kind LIKE '%buyable%' AND visibility='partial')           AS partial_skus,
          SUM(kind LIKE '%buyable%' AND visibility='on-request')        AS gated_skus,
          ROUND(100.0 * SUM(kind LIKE '%buyable%' AND visibility='published')
                / NULLIF(SUM(kind LIKE '%buyable%'), 0))                AS pct_published,
          SUM(kind LIKE '%buyable%' AND (what LIKE '%semaglutide%' OR what LIKE '%tirzepatide%')) AS glp1_skus,
          MIN(CASE WHEN visibility='published' AND price_unit='/mo' THEN price_num END) AS mo_price_min,
          MAX(CASE WHEN visibility='published' AND price_unit='/mo' THEN price_num END) AS mo_price_max
        FROM offerings GROUP BY slug
        """
    )

    # the joined surface: every standard profile field + the 8 telehealth cohort cuts + offerings aggregates,
    # keyed on slug. a VIEW, not a table — regenerates with the build, never goes stale. `c.*` carries the
    # profile's own captured_at; the cohort pack's is aliased so it doesn't collide. LEFT JOIN on stats so a
    # telehealth company with no offerings.md still appears (its stat columns NULL).
    cur.execute(
        """
        CREATE VIEW telehealth_full AS
        SELECT c.*,
               t.value_chain_role, t.pharmacy_model, t.audience, t.compounding_posture,
               t.anchor_category, t.modality, t.access_model, t.pay_model,
               t.captured_at AS telehealth_captured_at,
               s.sku_count, s.line_count, s.published_skus, s.partial_skus, s.gated_skus,
               s.pct_published, s.glp1_skus, s.mo_price_min, s.mo_price_max
        FROM companies c
        JOIN telehealth t ON c.slug = t.slug
        LEFT JOIN offerings_stats s ON s.slug = c.slug
        """
    )
    conn.commit()
    return n


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    db = os.path.join(OUT, "store.db")
    if os.path.exists(db):
        os.remove(db)
    conn = sqlite3.connect(db)
    n = build(conn)
    print(f"built {db}")
    print(f"  companies:  {n['companies']}  ({len(PROFILE_FIELDS)} profile fields each)")
    print(f"  telehealth: {n['telehealth']}")
    print(f"  offerings:  {n['offerings']} files → {n['skus']} SKU rows")
    th_with_off = conn.execute(
        "SELECT COUNT(DISTINCT t.slug) FROM telehealth t JOIN offerings o ON o.slug=t.slug"
    ).fetchone()[0]
    print(f"  telehealth ∩ offerings (joinable): {th_with_off}/{n['telehealth']}")
    vcols = [r[1] for r in conn.execute("PRAGMA table_info(telehealth_full)").fetchall()]
    vrows = conn.execute("SELECT COUNT(*) FROM telehealth_full").fetchone()[0]
    print(f"  view telehealth_full: {vrows} rows × {len(vcols)} cols (profile + 8 cohort cuts + 9 offerings aggregates)")
    print("\n  offerings aggregates sample (sku_count · %pub · glp1 · published /mo band):")
    for r in conn.execute(
        """SELECT name, sku_count, pct_published, glp1_skus, mo_price_min, mo_price_max
           FROM telehealth_full ORDER BY sku_count DESC LIMIT 8"""
    ):
        band = f"${r[4]:.0f}–${r[5]:.0f}/mo" if r[4] is not None else "—"
        print(f"    {r[1]:>3} SKUs · {str(r[2]) + '%':>4} pub · {r[3]:>2} GLP-1 · {band:>14}  {r[0]}")
    conn.close()


if __name__ == "__main__":
    main()
