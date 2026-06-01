#!/usr/bin/env python3
"""Store-aware query-affordance probe (rung-2 candidate).

Adapts experiments/2026-05-29-query-affordance/digest.py to THIS store's
layout (store/<domain>/profile.md + captures/<date>/*.md), to test whether a
"one read instead of N" helper materially beats cold-grep on the consumption
battery. Deliberately dumb: stdlib only, heuristic grabs, no index.

Modes:
  facets                  Frontmatter table across all profiles (serves Q2 / Q5).
                          Reads the field if present; falls back to the legacy
                          name (portfolio_shape <- is_multi_product) and to the
                          `# parent:` COMMENT for the empty parent/owns fields.
  term  T [T ...]         Cross-brand digest: per company, the profile-body
                          bullets/sentences mentioning any term, with price
                          lines flagged. Optionally scans captures (--captures).

Usage:
  python3 digest.py facets
  python3 digest.py term "weight loss" GLP semaglutide tirzepatide Wegovy Zepbound Ozempic
  python3 digest.py term "compounded" "not approved" "not been evaluated" --captures
"""

import argparse
import glob
import os
import re
import sys

STORE = os.path.join(os.path.dirname(__file__), "..", "..", "store")

FM_FIELDS = [
    "name",
    "domain",
    "entity_type",
    "target_market",
    "offering_category",
    "business_model",
    "portfolio_shape",
    "is_multi_product",
]
PRICE_RE = re.compile(r"\$\s?\d")


def read(path):
    return open(path, encoding="utf-8", errors="replace").read()


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    return (m.group(1), m.group(2)) if m else ("", text)


def parse_fm(fm_text):
    """Flat scalar/inline-list parse; strips trailing ' # comment'. Also captures
    a `# parent:` comment line into _parent since the real field is unused."""
    fm, parent_comment = {}, ""
    for line in fm_text.splitlines():
        cm = re.match(r"^#\s*parent:\s*(.+)$", line)
        if cm:
            parent_comment = cm.group(1).strip()
            continue
        mm = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if mm:
            val = mm.group(2)
            val = re.split(r"\s+#", val, 1)[0].strip()  # drop inline comment
            fm[mm.group(1)] = val
    if parent_comment:
        fm["_parent"] = parent_comment
    return fm


def profiles():
    for p in sorted(glob.glob(os.path.join(STORE, "*", "profile.md"))):
        yield p, read(p)


def cmd_facets(_args):
    rows = []
    for path, text in profiles():
        fm = parse_fm(split_frontmatter(text)[0])
        shape = fm.get("portfolio_shape") or (
            f"(is_multi_product={fm['is_multi_product']})"
            if "is_multi_product" in fm
            else ""
        )
        rows.append(
            {
                "name": fm.get("name", os.path.basename(os.path.dirname(path))),
                "domain": fm.get("domain", ""),
                "entity": fm.get("entity_type", ""),
                "market": fm.get("target_market", ""),
                "offering": fm.get("offering_category", ""),
                "model": fm.get("business_model", ""),
                "shape": shape,
                "parent": fm.get("_parent", ""),
            }
        )
    cols = [
        "name",
        "domain",
        "entity",
        "market",
        "offering",
        "model",
        "shape",
        "parent",
    ]
    print(f"# Store facets ({len(rows)} companies)\n")
    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join(["---"] * len(cols)) + "|")
    for r in rows:
        print("| " + " | ".join(str(r[c]).replace("|", "\\|") for c in cols) + " |")
    print(
        f"\n_Note: `shape` falls back to legacy is_multi_product (portfolio_shape "
        f"unused in corpus). `parent` is read from the `# parent:` COMMENT "
        f"(parent/owns frontmatter fields are empty in every profile)._"
    )


def matching_lines(body, terms):
    tl = [t.lower() for t in terms]
    out = []
    for ln in body.splitlines():
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        low = s.lower()
        if any(t in low for t in tl):
            out.append(s)
    return out


def cmd_term(args):
    terms = args.terms
    print(f"# Cross-brand digest: {terms}\n")
    hits = clean_price = no_price = 0
    blocks = []
    for path, text in profiles():
        fm_text, body = split_frontmatter(text)
        fm = parse_fm(fm_text)
        name, domain = fm.get("name", "?"), fm.get("domain", "")
        lines = matching_lines(body, terms)
        if args.captures:
            cap_glob = os.path.join(os.path.dirname(path), "captures", "*", "*.md")
            for cf in sorted(glob.glob(cap_glob)):
                for ln in matching_lines(read(cf), terms):
                    lines.append(f"[{os.path.basename(cf)}] {ln}")
        if not lines:
            continue
        hits += 1
        priced = [ln for ln in lines if PRICE_RE.search(ln)]
        (clean_price := clean_price + 1) if priced else (no_price := no_price + 1)
        block = [f"## {name} ({domain})"]
        block += [f"- {ln}" for ln in lines[:8]]
        if not priced:
            block.append("- ⚠ no $ price line found for these terms")
        blocks.append("\n".join(block))
    print("\n\n".join(blocks))
    print(
        f"\n\n---\n_Coverage: {hits} companies match. "
        f"{clean_price} have a $ price line, {no_price} do not._"
    )


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("facets").set_defaults(fn=cmd_facets)
    pt = sub.add_parser("term")
    pt.add_argument("terms", nargs="+")
    pt.add_argument("--captures", action="store_true")
    pt.set_defaults(fn=cmd_term)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
