#!/usr/bin/env python3
"""offeringscheck — lint an opt-in `offerings.md` against the module contract.

`offerings.md` is the per-SKU layer (SCHEMA "Tier-1 modules" → _design/2026-06-03-offerings-module.md):
a roster table whose load-bearing invariant is that every price is real. The tournament that designed it
caught exactly two failure modes a human eye misses — a *misattributed price* and a *molecule guessed from
the brand name* — so this script asserts the structural rules that make those greppable:

  1. roster column presence   — the seven spine columns are all there (Molecule is NOT one of them).
  2. price_visibility set      — every Visibility cell is `published | partial | on-request` (or `—`).
  3. every row is slug-keyed   — the within-company key column is never blank.
  4. grep-verifiable price     — every `$` amount in the doc is findable in a cited capture (the anti-
                                 hallucination check: a verbatim number can't survive the grep if invented).
  5. no cross-company canon     — no `Molecule` lead column and no canonical-key frontmatter field; molecule
                                 stays a descriptive token inside `What`, grouped across brands at query time.

Per-file by design (`--slug hims-com`): the fan-out's adversarial verifier runs it on one draft. No `--slug`
lints every `store/*/offerings.md`. Exit 0 = the module contract holds; nonzero prints how it broke.
Stdlib-only on purpose (matches skills/research-company/scripts/fc.py) — no PyYAML.

CLI:  python scripts/offeringscheck.py [--slug <slug>]
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, "store")

VISIBILITY_OK = {"published", "partial", "on-request"}  # the one closed set; `—` (no price) also allowed
# The seven spine columns (2026-06-03 design). Matched by the first word so "Price (verbatim)" and
# "What (molecule · form · access)" still resolve — and so a bare "Molecule" column trips check 5.
SPINE_PREFIXES = ["offering", "kind", "parent", "slug", "price", "visibility", "what"]
# A standalone molecule/canonical column or frontmatter key is the B2 pivot the design rejected.
CANON_KEY_RE = re.compile(r"^(molecule|canonical|global)\b|_(canonical|id)$", re.I)
# A `$` amount: requires the sigil so image widths (`w_499`) and years never match. Comma optional.
PRICE_RE = re.compile(r"\$\s?(\d[\d,]*(?:\.\d+)?)")


def frontmatter_keys(text: str) -> list[str] | None:
    """Top-level frontmatter keys via a column-0 scan (stdlib-only). None if no leading '---' fence."""
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return [m.group(1) for line in parts[1].splitlines() if (m := re.match(r"([A-Za-z_][A-Za-z0-9_]*):", line))]


def split_row(line: str) -> list[str]:
    """A markdown table row → trimmed cells (drop the leading/trailing empty splits from the outer pipes)."""
    cells = [c.strip() for c in line.strip().split("|")]
    return cells[1:-1] if cells and cells[0] == "" and cells[-1] == "" else cells


def parse_roster(text: str) -> tuple[list[str], list[list[str]]]:
    """The `## Roster` table → (header cells, data rows). Empty header if no roster table is found.

    Walks from the `## Roster` heading to the first `| … |` header, skips the `|---|` rule, then collects
    body rows until the table ends. Robust to the `### Verbatim anchors` subsection that follows it.
    """
    lines = text.splitlines()
    start = next((i for i, ln in enumerate(lines) if re.match(r"^##\s+Roster\b", ln)), None)
    if start is None:
        return [], []
    header: list[str] = []
    rows: list[list[str]] = []
    for ln in lines[start + 1 :]:
        s = ln.strip()
        if s.startswith("## ") and not s.startswith("## Roster"):
            break  # next top-level section ends the roster
        if not s.startswith("|"):
            continue
        if re.fullmatch(r"\|[\s:|-]+\|", s):
            continue  # the |---| alignment rule
        cells = split_row(ln)
        if not header:
            header = cells
        else:
            rows.append(cells)
    return header, rows


def captures_text(slug: str) -> str:
    """All capture markdown for a company, commas stripped from numbers — the corpus a price must grep into.

    Stripping `,` lets a doc's `$1,899` match a capture's `$1899` (and vice versa); the `$` sigil in
    PRICE_RE still guards against bare-number false positives. Empty string if the company has no captures.
    """
    out: list[str] = []
    for p in glob.glob(os.path.join(STORE, slug, "captures", "**", "*.md"), recursive=True):
        with open(p, encoding="utf-8") as f:
            out.append(f.read())
    return re.sub(r"(?<=\d),(?=\d)", "", "\n".join(out))


def check(slug: str) -> list[str]:
    """Lint one company's offerings.md. Returns a list of failure strings ([] = clean)."""
    path = os.path.join(STORE, slug, "offerings.md")
    fails: list[str] = []
    if not os.path.isfile(path):
        return [f"{slug}: no offerings.md (module not active here)"]
    with open(path, encoding="utf-8") as f:
        text = f.read()

    # --- frontmatter: fence + doc-meta keys + no canonical-key field (check 5a) ---
    keys = frontmatter_keys(text)
    if keys is None:
        fails.append(f"{slug}: no leading '---' frontmatter fence.")
    else:
        for required in ("schema_version", "domain", "captured_at"):
            if required not in keys:
                fails.append(f"{slug}: frontmatter missing '{required}'.")
        for k in keys:
            if CANON_KEY_RE.search(k):
                fails.append(f"{slug}: frontmatter key '{k}' looks like a cross-company canonical key — the design forbids one (molecule rides in `What`).")

    for section in ("## Portfolio overview", "## Roster"):
        if section not in text:
            fails.append(f"{slug}: missing required section '{section}'.")

    # --- roster structure (checks 1, 2, 3, 5b) ---
    header, rows = parse_roster(text)
    if not header:
        fails.append(f"{slug}: no roster table found under '## Roster'.")
        return fails
    hdr_lower = [h.lower() for h in header]
    col = {pref: next((i for i, h in enumerate(hdr_lower) if h.startswith(pref)), None) for pref in SPINE_PREFIXES}
    for pref, i in col.items():
        if i is None:
            fails.append(f"{slug}: roster is missing the '{pref}' column (have: {header}).")
    if any(h == "molecule" for h in hdr_lower):
        fails.append(f"{slug}: roster has a standalone 'Molecule' column — the rejected B2 pivot; molecule belongs inside `What`.")

    vis_i, slug_i = col["visibility"], col["slug"]
    for r, cells in enumerate(rows, 1):
        if vis_i is not None and vis_i < len(cells):
            v = cells[vis_i].strip().strip("`").lower()
            if v and v != "—" and v not in VISIBILITY_OK:
                fails.append(f"{slug}: roster row {r} visibility '{cells[vis_i]}' not in {{published, partial, on-request, —}}.")
        if slug_i is not None and slug_i < len(cells):
            if not cells[slug_i].strip().strip("`"):
                fails.append(f"{slug}: roster row {r} ({cells[0] if cells else '?'}) has an empty Slug — every row is slug-keyed.")

    # --- grep-verifiable price (check 4): every `$` amount must sit in a cited capture ---
    amounts = {m.group(1).replace(",", "") for m in PRICE_RE.finditer(text)}
    if amounts:
        corpus = captures_text(slug)
        if not corpus:
            fails.append(f"{slug}: offerings.md cites prices but store/{slug}/captures/ is empty — nothing to grep-verify against.")
        else:
            for amt in sorted(amounts, key=lambda a: float(a)):
                # match the `$`-anchored amount with or without thousands commas; corpus already comma-stripped
                if not re.search(r"\$\s?" + re.escape(amt) + r"(?:\.\d+)?\b", corpus):
                    fails.append(f"{slug}: price '${amt}' is not greppable in any store/{slug}/captures/ page — misattributed or hallucinated?")
    return fails


def main() -> None:
    ap = argparse.ArgumentParser(description="lint offerings.md against the module contract")
    ap.add_argument("--slug", help="lint one company (default: every store/*/offerings.md)")
    args = ap.parse_args()

    if args.slug:
        slugs = [args.slug]
    else:
        slugs = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(STORE, "*", "offerings.md")))
        if not slugs:
            print("offeringscheck: no store/*/offerings.md found (module not active anywhere yet).")
            return

    all_fails: list[str] = []
    for slug in slugs:
        fails = check(slug)
        all_fails += fails
        print(f"offeringscheck {slug}: {'OK' if not fails else str(len(fails)) + ' issue(s)'}")
        for f in fails:
            print("  FAIL:", f)
    if all_fails:
        sys.exit(f"\n{len(all_fails)} failure(s) across {len(slugs)} file(s).")
    print(f"\nOK — {len(slugs)} offerings.md file(s) conform to the module contract.")


if __name__ == "__main__":
    main()
