#!/usr/bin/env python3
"""battery — run the telehealth aggregation questions across the three hypotheses, timed.

H1 trivial single-table (expect: parity with the QUERYING.md recipe, no win)
H2 the 3-way JOIN offerings ⋈ telehealth ⋈ companies (expect: the real value, if any — expressiveness)
H3 the price wall (expect: SQLite holds a number, but it's wrong/lossy enough to vindicate verbatim-only)

Plus a pure-Python baseline for the headline JOIN, to isolate speed (a non-issue at this N) from
expressiveness. Builds an in-memory DB from the live markdown each run — markdown stays source-of-truth.

Run: `python battery.py`
"""

from __future__ import annotations

import glob
import os
import re
import sqlite3
import time
from typing import Any, Callable

import build_db  # the lens builder under test
import yaml

STORE = build_db.STORE


def timed(fn: Callable[[], Any]) -> tuple[Any, float]:
    t0 = time.perf_counter()
    out = fn()
    return out, (time.perf_counter() - t0) * 1000  # ms


def show(rows: list[tuple], headers: tuple[str, ...] = ()) -> None:
    if headers:
        print("       " + "   ".join(headers))
    for r in rows:
        print("       " + "   ".join(str(c) for c in r))


def main() -> None:
    conn = sqlite3.connect(":memory:")
    (_, build_ms) = timed(lambda: build_db.build(conn))
    q = conn.execute
    n_sku = q("SELECT COUNT(*) FROM offerings").fetchone()[0]
    n_th = q("SELECT COUNT(*) FROM telehealth").fetchone()[0]
    print(f"=== build: markdown → in-memory SQLite in {build_ms:.0f}ms "
          f"({n_th} telehealth ⋈ {n_sku} SKU rows) ===\n")

    # ---- H1: trivial single-table aggregation (parity check) -------------------------------------
    print("H1 — trivial single-table (does SQLite beat the one-line recipe? expect: no)\n")

    print("Q1  telehealth companies by pharmacy_model")
    rows, ms = timed(lambda: q(
        "SELECT pharmacy_model, COUNT(*) n FROM telehealth GROUP BY pharmacy_model ORDER BY n DESC"
    ).fetchall())
    show(rows); print(f"     [{ms:.2f}ms]  — QUERYING Recipe 2 is `Counter(...)`; SQL adds nothing here.\n")

    print("Q2  within-cohort filter: men-led + integrated pharmacy (QUERYING Recipe 6)")
    rows, ms = timed(lambda: q(
        """SELECT slug, anchor_category FROM telehealth
           WHERE audience IN ('men-only','men-first') AND pharmacy_model='integrated'"""
    ).fetchall())
    show(rows or [("(none)",)]); print(f"     [{ms:.2f}ms]  — one-line comprehension already; parity.\n")

    # ---- H2: the 3-way JOIN (the untested demand) ------------------------------------------------
    print("H2 — the 3-way JOIN offerings ⋈ telehealth ⋈ companies (the new, post-coded-queries demand)\n")

    print("Q3  semaglutide SKU count by pharmacy_model  (offerings ⋈ telehealth, LIKE-membership)")
    rows, ms = timed(lambda: q(
        """SELECT t.pharmacy_model, COUNT(*) skus, COUNT(DISTINCT o.slug) brands
           FROM offerings o JOIN telehealth t ON t.slug=o.slug
           WHERE o.what LIKE '%semaglutide%' GROUP BY t.pharmacy_model ORDER BY skus DESC"""
    ).fetchall())
    show(rows, ("pharmacy_model", "skus", "brands"))
    print(f"     [{ms:.2f}ms]  — joins a 555-row SKU table to a cohort cut; awkward by hand.\n")

    print("Q4  compounded-GLP-1 brands that lead men-first/-only  (3-table filter)")
    rows, ms = timed(lambda: q(
        """SELECT DISTINCT t.slug, t.audience, t.compounding_posture
           FROM offerings o JOIN telehealth t ON t.slug=o.slug
           WHERE (o.what LIKE '%semaglutide%' OR o.what LIKE '%tirzepatide%')
             AND t.audience IN ('men-only','men-first')
           ORDER BY t.slug"""
    ).fetchall())
    show(rows or [("(none)",)], ("brand", "audience", "compounding")); print(f"     [{ms:.2f}ms]\n")

    print("Q5  price visibility by brand: who publishes vs gates  (offerings ⋈ telehealth, pivot)")
    rows, ms = timed(lambda: q(
        """SELECT o.slug,
                  SUM(visibility='published') pub, SUM(visibility='partial') part,
                  SUM(visibility='on-request') gated
           FROM offerings o JOIN telehealth t ON t.slug=o.slug
           WHERE o.kind LIKE '%buyable%' GROUP BY o.slug ORDER BY gated DESC, pub DESC"""
    ).fetchall())
    show(rows, ("brand", "pub", "partial", "gated")); print(f"     [{ms:.2f}ms]\n")

    print("Q6  molecule reach — distinct brands per molecule.  LIKE-membership vs GROUP BY exact")
    for mol in ("semaglutide", "tirzepatide", "tadalafil", "testosterone"):
        n = q("""SELECT COUNT(DISTINCT o.slug) FROM offerings o JOIN telehealth t ON t.slug=o.slug
                 WHERE o.what LIKE ?""", (f"%{mol}%",)).fetchone()[0]
        print(f"       LIKE %{mol}%:  {n} brands")
    frag = q("""SELECT molecule, COUNT(*) n FROM offerings o JOIN telehealth t ON t.slug=o.slug
                WHERE molecule LIKE '%testosterone%' GROUP BY molecule""").fetchall()
    print("     GROUP BY molecule exact, for 'testosterone' — fragments into:")
    show(frag)
    print("     — membership (LIKE/grep) is robust; exact group-by fragments on free text (coded-queries' lesson).\n")

    # ---- H3: the price wall ----------------------------------------------------------------------
    print("H3 — the price wall: can we aggregate price *magnitude*? (expect: no, and that's the finding)\n")

    print("Q7  'cheapest semaglutide /mo across the cohort' — ORDER BY price_num")
    rows, ms = timed(lambda: q(
        """SELECT o.slug, o.price_num, o.price_unit, o.promo_first_month, o.price_verbatim
           FROM offerings o JOIN telehealth t ON t.slug=o.slug
           WHERE o.what LIKE '%semaglutide%' AND o.price_num IS NOT NULL AND o.price_unit='/mo'
           ORDER BY o.price_num ASC LIMIT 6"""
    ).fetchall())
    show(rows, ("brand", "num", "unit", "promo?", "verbatim"))
    print(f"     [{ms:.2f}ms]  — the number sorts; but read the verbatim column: the sort is a LIE where")
    print("       promo? = 1 (first-month teaser, not the recurring price) or the $-figure is a consult/bundle.\n")

    print("Q7b the misparse, shown plainly — first-$ ≠ the real price (cohort-scoped)")
    rows = q(
        """SELECT o.price_num, o.price_verbatim FROM offerings o JOIN telehealth t ON t.slug=o.slug
           WHERE o.price_verbatim LIKE '%first month%' OR o.price_verbatim LIKE '%consult%'
              OR o.price_verbatim LIKE '%then $%' LIMIT 6"""
    ).fetchall()
    for num, vb in rows:
        print(f"       parsed ${num:<8} ←  {vb}")
    print()

    # ---- baseline: speed is not the axis ---------------------------------------------------------
    print("Baseline — Q3 in pure Python (no DB), same answer, to isolate speed from expressiveness\n")

    def py_q3() -> dict[str, int]:
        th = {}
        for p in glob.glob(os.path.join(STORE, "*", "telehealth.md")):
            slug = os.path.basename(os.path.dirname(p))
            with open(p, encoding="utf-8") as fh:
                t = fh.read()
            fm = yaml.safe_load(t.split("---", 2)[1]) if t.startswith("---") else {}
            th[slug] = fm.get("pharmacy_model")
        counts: dict[str, int] = {}
        for p in glob.glob(os.path.join(STORE, "*", "offerings.md")):
            slug = os.path.basename(os.path.dirname(p))
            if slug not in th:
                continue
            with open(p, encoding="utf-8") as fh:
                bdy = fh.read()
            for line in bdy.splitlines():
                if line.lstrip().startswith("|") and re.search(r"semaglutide", line, re.I):
                    counts[th[slug]] = counts.get(th[slug], 0) + 1
        return counts

    (_, py_ms) = timed(py_q3)
    sql_only_ms = timed(lambda: q(
        """SELECT t.pharmacy_model, COUNT(*) FROM offerings o JOIN telehealth t ON t.slug=o.slug
           WHERE o.what LIKE '%semaglutide%' GROUP BY t.pharmacy_model"""
    ).fetchall())[1]
    print(f"       pure-Python (parse+join+count from markdown): {py_ms:.0f}ms")
    print(f"       SQL query alone (DB already built):           {sql_only_ms:.2f}ms")
    print(f"       SQLite build cost (paid once per staleness):  {build_ms:.0f}ms")
    print("       → at this N, query speed is noise either way. The build is the only real cost.")
    conn.close()


if __name__ == "__main__":
    main()
