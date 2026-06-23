#!/usr/bin/env python3
"""audit_completeness — for each telehealth offerings.md, surface what it SELF-REPORTS about how
comprehensive it was, beside its roster size — to find the dig-deeper candidates.

The Ro.co lesson: `sku_count` is a count of *what got enumerated*, and offerings.md deliberately does NOT
always enumerate the whole catalog (Firecrawl-credit care — see OFFERINGS.md `portfolio_shape` depth dial +
the `## Provenance` scope note). So a low count can mean "small catalog" OR "capture stopped early," and the
DB can't tell them apart. This reads each file's own completeness verdict + "not enumerated" scope lines so a
human can. No Firecrawl — pure read of existing files.

Run: `python audit_completeness.py`
"""

from __future__ import annotations

import glob
import os
import re

import build_db  # reuse frontmatter / parse_roster / STORE

STORE = build_db.STORE

# The load-bearing distinction the Ro.co lesson taught: a "not enumerated" note is benign when it omits
# LEAF detail (dose/term/PDP — the contract's design) but a real gap when it omits whole LINES/catalogs
# (the count then misrepresents catalog breadth). A third state — no note at all — is its own blind spot.
BREADTH_CUES = [
    "out of scope", "out of this run", "not enumerated here", "sibling brand", "off-host", "off host",
    "storefront", "subdomain", "another domain", "condition line", "couldn't reach", "could not reach",
    "rostered by name", "not in scope", "weight-loss-only", "weight loss only",
]
LEAF_CUES = [
    "dose", "quantity", "term leaf", "leaf sku", "pdp not captured", "pdps", "variant", "gift card",
    "gift-card", "a/b", "bulk", "per-drug price", "titration", "dose ladder", "supply-tier",
]
COMPLETE_CUES = [
    "complete at the indexed level", "high confidence", "roster is complete", "complete across",
    "confidence the roster is complete",
]


def section(md: str, header: str) -> str:
    """Return the text of a `## <header>` section, up to the next `## ` or EOF."""
    m = re.search(rf"^##\s+{re.escape(header)}.*?$(.*?)(?=^##\s|\Z)", md, re.M | re.S)
    return m.group(1).strip() if m else ""


def cue_lines(md: str, cues: list[str]) -> list[str]:
    hits = []
    for line in md.splitlines():
        low = line.lower()
        if any(c in low for c in cues) and line.strip():
            hits.append(line.strip().lstrip("-* ").strip())
    return hits


def main() -> None:
    # roster counts from the live parse (not the DB — keep this script standalone + current)
    th_slugs = {
        os.path.basename(os.path.dirname(p))
        for p in glob.glob(os.path.join(STORE, "*", "telehealth.md"))
    }
    rows = []
    for off in sorted(glob.glob(os.path.join(STORE, "*", "offerings.md"))):
        slug = os.path.basename(os.path.dirname(off))
        if slug not in th_slugs:
            continue
        roster = build_db.parse_roster(off)
        buyable = sum(1 for r in roster if "buyable" in r["kind"].lower())
        with open(off, encoding="utf-8") as fh:
            md = fh.read()
        fm = build_db.frontmatter(off)
        prof = build_db.frontmatter(os.path.join(STORE, slug, "profile.md"))
        prov = section(md, "Provenance")
        scope_text = prov or md
        breadth = cue_lines(scope_text, BREADTH_CUES)
        complete = cue_lines(scope_text, COMPLETE_CUES)
        stated = bool(complete) or "scope:" in scope_text.lower() or "enumerated" in scope_text.lower()
        # tier: the count-trust verdict. breadth-gap = the roster likely UNDERSTATES the catalog (dig deeper);
        # no-note = can't tell (self-report missing); indexed-complete = trust the count at the indexed level.
        tier = "breadth-gap" if breadth else ("no-note" if not stated else "indexed-complete")
        rows.append({
            "slug": slug, "shape": (prof.get("portfolio_shape") or "?"), "buyable": buyable,
            "cap": str(fm.get("captured_at")), "tier": tier, "breadth": breadth, "complete": complete,
        })

    order = {"breadth-gap": 0, "no-note": 1, "indexed-complete": 2}
    rows.sort(key=lambda r: (order[r["tier"]], r["buyable"]))
    tiers = {t: sum(1 for r in rows if r["tier"] == t) for t in order}
    print(f"telehealth offerings.md completeness audit — {len(rows)} files (no Firecrawl; reads self-reports)")
    print(f"  breadth-gap (dig deeper): {tiers['breadth-gap']}   "
          f"no-note (can't tell): {tiers['no-note']}   indexed-complete (trust count): {tiers['indexed-complete']}\n")
    print(f"  {'brand':<18}{'shape':<22}{'SKUs':>5}  {'tier':<17} evidence")
    print("-" * 110)
    for r in rows:
        ev = (r["breadth"][0] if r["breadth"]
              else (r["complete"][0] if r["complete"] else "(no completeness note in Provenance)"))
        print(f"  {r['slug']:<18}{r['shape']:<22}{r['buyable']:>5}  {r['tier']:<17} {ev[:52]}")

    print("\n=== breadth-gap self-reports (the roster likely understates the catalog — dig deeper) ===")
    for r in rows:
        if r["tier"] == "breadth-gap":
            print(f"\n{r['slug']}  ({r['shape']}, {r['buyable']} SKUs, cap {r['cap']}):")
            for line in r["breadth"]:
                print(f"   – {line[:170]}")


if __name__ == "__main__":
    main()
