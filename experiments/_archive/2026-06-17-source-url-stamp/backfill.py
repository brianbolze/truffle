#!/usr/bin/env python3
"""One-shot: backfill the source_url provenance stamp onto existing cleaned capture `.md`.

The forward fix (fc.py source_stamp) only stamps *new* captures. This converts the fragile
runtime fallback — "Tier-B reads the gitignored, prunable .payloads/manifest.jsonl" — into a
durable, committed stamp for every existing page whose URL was actually recorded. It recovers
ONLY from recorded manifest data (last-wins name -> sourceURL): no path reconstruction, because
guessing the URL is the exact failure the fix exists to kill. Pages whose name predates
manifest-recording are skipped and reported; the forward fix stamps them on next capture.

Imports source_stamp from fc.py so a backfilled stamp is byte-identical to a forward one.
Idempotent (skips an already-stamped file) and skips _archive. Dry-run by default; --apply writes.

  python3 experiments/2026-06-17-source-url-stamp/backfill.py            # dry-run, print counts
  python3 experiments/2026-06-17-source-url-stamp/backfill.py --apply    # write the stamps
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "skills" / "research-company" / "scripts"))

import fc  # noqa: E402 — after the sys.path insert above


def is_stamped(text: str) -> bool:
    """True if the file already opens with a source_url provenance comment (forward or prior-art)."""
    head = text.lstrip()[:200]
    return head.startswith("<!--") and "source_url:" in head


def manifest_urls(manifest: Path) -> dict[str, str]:
    """Last-wins name -> URL from a .payloads/manifest.jsonl — sourceURL, else the requested URL.

    Matches fc.py do_verify's 'append-ordered, last write per name wins' for re-scraped pages."""
    latest: dict[str, str] = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rec = json.loads(line)
        if rec.get("kind") != "scrape":
            continue
        name, url = rec.get("name"), (rec.get("sourceURL") or rec.get("requested"))
        if name and url:
            latest[name] = url
    return latest


def backfill(store: Path, apply: bool) -> None:
    stamped = skipped_stamped = no_name = 0
    no_manifest = 0
    unrecovered: dict[str, list[str]] = defaultdict(list)

    # date dirs that HAVE a manifest — the only place a recorded URL can come from
    seen_dirs: set[Path] = set()
    for manifest in store.glob("*/captures/**/.payloads/manifest.jsonl"):
        if "_archive" in manifest.parts:
            continue
        date_dir = manifest.parent.parent
        seen_dirs.add(date_dir)
        urls = manifest_urls(manifest)
        slug = date_dir.relative_to(store).parts[0]
        for md in sorted(date_dir.glob("*.md")):
            text = md.read_text(encoding="utf-8")
            if is_stamped(text):
                skipped_stamped += 1
                continue
            url = urls.get(md.stem)
            if not url:
                no_name += 1
                unrecovered[slug].append(md.stem)
                continue
            if apply:
                # captured date = the dir name (the capture this page belongs to)
                md.write_text(fc.source_stamp(url, date_dir.name) + text, encoding="utf-8")
            stamped += 1

    # live .md in date dirs WITHOUT a surviving manifest — unrecoverable, count for honesty
    for md in store.glob("*/captures/**/*.md"):
        if "_archive" in md.parts:
            continue
        date_dir = md.parent
        if date_dir in seen_dirs or is_stamped(md.read_text(encoding="utf-8")):
            continue
        no_manifest += 1
        unrecovered[date_dir.relative_to(store).parts[0]].append(f"{date_dir.name}/{md.stem} (no manifest)")

    verb = "STAMPED" if apply else "would stamp"
    print(f"{verb}: {stamped}")
    print(f"already stamped (skip): {skipped_stamped}")
    print(f"unrecoverable — name not in manifest: {no_name}")
    print(f"unrecoverable — no surviving manifest: {no_manifest}")
    print(f"\n{sum(len(v) for v in unrecovered.values())} unrecoverable pages across {len(unrecovered)} companies "
          "(predate manifest-recording — the forward fix stamps them on next capture):")
    for slug in sorted(unrecovered):
        print(f"  {slug}: {len(unrecovered[slug])}")
    if not apply:
        print("\n(dry-run — re-run with --apply to write)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the stamps (default: dry-run)")
    parser.add_argument("--store", default=str(ROOT / "store"))
    args = parser.parse_args()
    backfill(Path(args.store), args.apply)


if __name__ == "__main__":
    main()
