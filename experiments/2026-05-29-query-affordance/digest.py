#!/usr/bin/env python3
"""Thin query-affordance probe.

Given a product/term, pull the matching slice from each brand's LATEST
competitive-intel snapshot into ONE consolidated markdown digest — so an agent
answers a cross-brand question in a single read instead of opening N files.

Deliberately dumb: no index, no deps, heuristic section-grab. The point is to
see how far "rung 2" gets us before we'd reach for a real schema/index (rung 3).

Usage:
    python3 digest.py "Sermorelin"
    python3 digest.py "TRT" --snapshots /path/to/snapshots
"""

import argparse
import glob
import os
import re

DEFAULT_SNAPSHOTS = os.path.expanduser(
    "~/Library/Mobile Documents/com~apple~CloudDocs/Text Files/Teleprescribe Venture/"
    "Teleprescribe Venture/agent-workflows/competitive-intel/snapshots"
)

HEADING_RE = re.compile(r"^(#{2,6})\s+(.*)$")


def latest_snapshot(brand_dir):
    files = sorted(glob.glob(os.path.join(brand_dir, "*.md")))
    return files[-1] if files else None


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
            if mm:
                fm[mm.group(1)] = mm.group(2).strip()
    return fm


def matching_sections(text, term):
    """Heading-sections (## .. ######) whose title contains the term."""
    lines = text.splitlines()
    headings = [
        (i, len(m.group(1)), m.group(2))
        for i, line in enumerate(lines)
        for m in [HEADING_RE.match(line)]
        if m
    ]
    term_l = term.lower()
    out = []
    for k, (idx, level, title) in enumerate(headings):
        if term_l in title.lower():
            end = len(lines)
            for idx2, level2, _ in headings[k + 1 :]:
                if level2 <= level:
                    end = idx2
                    break
            out.append("\n".join(lines[idx:end]).strip())
    return out


def price_lines(text, term):
    return [
        ln.strip()
        for ln in text.splitlines()
        if term.lower() in ln.lower() and "$" in ln
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("term")
    ap.add_argument("--snapshots", default=DEFAULT_SNAPSHOTS)
    ap.add_argument("--max-section-chars", type=int, default=1200)
    args = ap.parse_args()

    brands = sorted(
        d for d in glob.glob(os.path.join(args.snapshots, "*")) if os.path.isdir(d)
    )
    hits, sectioned, price_only, mention_only = 0, 0, 0, 0
    chunks = []

    for bd in brands:
        f = latest_snapshot(bd)
        if not f:
            continue
        text = open(f, encoding="utf-8", errors="replace").read()
        if args.term.lower() not in text.lower():
            continue
        hits += 1
        fm = parse_frontmatter(text)
        name = fm.get("competitor", os.path.basename(bd))
        domain = fm.get("domain", "")
        date = fm.get("captured_at", "")[:10]
        secs = matching_sections(text, args.term)
        prices = price_lines(text, args.term)

        block = [f"## {name} ({domain}) — {date}"]
        if secs:
            sectioned += 1
            for s in secs[:2]:
                block.append(s[: args.max_section_chars])
        elif prices:
            price_only += 1
            block.append("_Price-bearing mentions (no dedicated section):_")
            block += [f"- {p}" for p in prices[:5]]
        else:
            mention_only += 1
            block.append(
                f"_Mentioned, but no section or price line found "
                f"(would need to open {os.path.relpath(f, args.snapshots)})._"
            )
        chunks.append("\n".join(block))

    print(f'# Cross-brand digest: "{args.term}"\n')
    print(
        f"_Scanned {len(brands)} brands · {hits} mention the term "
        f"({sectioned} with a dedicated section, {price_only} price-only, "
        f"{mention_only} mention-only)._\n"
    )
    print("\n\n".join(chunks))
    print(
        f"\n\n---\n_Coverage: {hits}/{len(brands)} brands. "
        f"Fidelity: {sectioned} clean, {price_only + mention_only} would need a file open._"
    )


if __name__ == "__main__":
    main()
