#!/usr/bin/env python3
"""compare — CLI for the N-company specimen sheet: 2-6 store companies → one side-by-side HTML.

The logic lives in scripts/present/ (frame + approach: _design/2026-06-12-presentation-layer.md);
this file only parses arguments and writes the file.
"""

from __future__ import annotations

import argparse
import os
import sys

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
if SCRIPTS not in sys.path:
    sys.path.insert(0, SCRIPTS)

from present import OUT  # noqa: E402
from present.assets import load_screenshot  # noqa: E402
from present.compare import render_compare  # noqa: E402
from present.model import extract_model  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description="render N store companies into one side-by-side comparison sheet")
    ap.add_argument("company", nargs="+", help="2-6 companies (name, domain, alias, or store slug)")
    ap.add_argument("--no-fetch", action="store_true", help="skip remote logo/font fetches")
    args = ap.parse_args()
    if not 2 <= len(args.company) <= 6:
        ap.error("give between 2 and 6 companies")

    models = []
    for q in args.company:
        m = extract_model(q, fetch=not args.no_fetch)
        if m is None:
            print(f"{q} → not in store (try: python scripts/store.py find '{q}')")
            sys.exit(1)
        # N narrow columns don't need brief-grade specimens; 640px keeps the sheet AirDrop-able.
        m["screenshot"] = load_screenshot(m["slug"], width=640)
        models.append(m)

    os.makedirs(OUT, exist_ok=True)
    stem = "compare-" + "+".join(m["slug"].removesuffix("-com") for m in models)
    out_path = os.path.join(OUT, f"{stem}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(render_compare(models))
    print(f"{len(models)} companies → {out_path}  ({os.path.getsize(out_path) // 1024} KB)")
    print(f"  paste into your reply: [Open comparison sheet](<{out_path}>)")


if __name__ == "__main__":
    main()
