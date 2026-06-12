#!/usr/bin/env python3
"""render — CLI for the human-facing lens: store/<slug>/ → self-contained HTML brief(s) + index.

The logic lives in scripts/present/ (frame + approach: _design/2026-06-12-presentation-layer.md);
this file only parses arguments and writes files, so the command agents learned stays stable.
The markdown stays the source of truth; every output is a regenerable lens.
"""

from __future__ import annotations

import argparse
import os
import sys

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
if SCRIPTS not in sys.path:
    sys.path.insert(0, SCRIPTS)

from present import OUT  # noqa: E402
from present.assets import build_fonts  # noqa: E402
from present.brief import render_html  # noqa: E402
from present.index import render_index_html  # noqa: E402
from present.model import extract_index, extract_model  # noqa: E402

from store import load as store_load  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description="render store/<slug>/ into self-contained HTML briefs")
    ap.add_argument("company", nargs="*", help="company name, domain, alias, or store slug")
    ap.add_argument("--all", action="store_true",
                    help="render every company in the store — pre-warms font/logo/image caches so a live demo never waits on a fetch")
    ap.add_argument("--index", action="store_true",
                    help="render the corpus index (index.html) — the store's human front door; pair with --all so row links resolve")
    ap.add_argument("--no-fetch", action="store_true", help="skip remote logo/font fetches; use local assets and fallbacks")
    args = ap.parse_args()

    queries = sorted(store_load()) if args.all else args.company
    if not queries and not args.index:
        ap.error("name at least one company, or pass --all / --index")

    os.makedirs(OUT, exist_ok=True)
    for q in queries:
        m = extract_model(q, fetch=not args.no_fetch)
        if m is None:
            print(f"{q} → not in store (try: python scripts/store.py find '{q}')")
            continue
        out_path = os.path.join(OUT, f"{m['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(render_html(m))
        size = os.path.getsize(out_path) // 1024
        print(f"{q} → {out_path}  ({size} KB)")
        # The brief is invisible unless the link lands in the agent's reply — hand over the exact
        # markdown (angle brackets: the repo path contains spaces) so no one re-derives it from prose.
        print(f"  paste into your reply: [Open {m.get('name') or m['slug']} brief](<{out_path}>)")

    if args.index:
        rows = extract_index(fetch=not args.no_fetch)
        # 00- prefix: the index sorts to the top of the briefs folder, where a human looks first.
        out_path = os.path.join(OUT, "00-index.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(render_index_html(rows, build_fonts([], fetch=not args.no_fetch)))
        print(f"index → {out_path}  ({len(rows)} companies, {os.path.getsize(out_path) // 1024} KB)")
        print(f"  paste into your reply: [Open the company index](<{out_path}>)")


if __name__ == "__main__":
    main()
