#!/usr/bin/env python3
"""tile — Tier-A native-resolution tiling for the visual-evidence module.

A full-page marketing screenshot is 1920×(7k–24k); read whole it downsamples ~7× and hides
the very defects visual judgment turns on (amateur charts, clip-art icons, render seams). So
the module never mines the whole page — it mines native-resolution *tiles*. This slices the
screenshot the capture already stored (`captures/<date>/.payloads/<page>.png`) into overlapping
1920×1400 tiles plus a 480w overview — `sips` measures, ImageMagick (`magick`) crops/resizes, the
recipe-time split the logos module already uses (`sips`'s `--cropOffset` silently centers and can't
offset, so the actual cut is magick's job). It's the cheap default; `shoot.py` is the browser-
re-render escalation for pages the cached screenshot can't be trusted for (it emits the same shape).

CLI:  python3 scripts/tile.py --slug <slug> [--capture <date>] [--pages homepage pricing ...]
"""

from __future__ import annotations

import argparse
import json
import math
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TILE_HEIGHT = 1400
OVERLAP = 180
OVERVIEW_WIDTH = 480


def sips_dims(path: str) -> tuple[int, int]:
    """Pixel (width, height) of an image via `sips -g` — the macOS-native measure the logos module uses."""
    out = subprocess.check_output(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", path], text=True
    )
    width = height = 0
    for line in out.splitlines():
        if "pixelWidth:" in line:
            width = int(line.split(":")[1])
        elif "pixelHeight:" in line:
            height = int(line.split(":")[1])
    return width, height


def magick_crop(src: str, dst: str, width: int, top: int, height: int) -> None:
    """Crop a `width`×`height` tile at vertical offset `top` (magick's explicit +0+top — sips can't offset)."""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    subprocess.check_call(
        ["magick", src, "-crop", f"{width}x{height}+0+{top}", "+repage", dst],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def magick_overview(src: str, dst: str, width: int) -> None:
    """A small full-page overview so the QA gate can see page shape at a glance."""
    subprocess.check_call(
        ["magick", src, "-resize", f"{width}x", dst],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def tile_offsets(scroll_height: int, tile_height: int, overlap: int) -> list[int]:
    """Top y-offset of each tile, overlapping by `overlap`, last tile pinned to the floor."""
    step = tile_height - overlap
    count = max(1, math.ceil(max(scroll_height - overlap, 1) / step))
    offsets = []
    for index in range(count):
        offsets.append(min(index * step, max(scroll_height - tile_height, 0)))
    return offsets


def latest_capture(slug: str) -> str:
    """Newest dated capture dir under the slug (excludes _archive) — the default tiling source."""
    captures = os.path.join(ROOT, "store", slug, "captures")
    dates = [d for d in os.listdir(captures) if d[:4].isdigit() and os.path.isdir(os.path.join(captures, d))]
    if not dates:
        raise SystemExit(f"no dated capture under store/{slug}/captures")
    return sorted(dates)[-1]


def tile_page(payloads: str, tiles_root: str, page: str) -> dict:
    """Slice one page's cached screenshot into tiles + an overview; return its manifest record."""
    src = os.path.join(payloads, f"{page}.png")
    if not os.path.exists(src):
        return {"page": page, "missing": True}
    width, height = sips_dims(src)
    page_dir = os.path.join(tiles_root, page)
    tiles = []
    for index, y in enumerate(tile_offsets(height, TILE_HEIGHT, OVERLAP)):
        actual_height = min(TILE_HEIGHT, height - y)
        rel = os.path.join(page, f"tile-{index:02d}-y{y:05d}.png")
        magick_crop(src, os.path.join(tiles_root, rel), width, y, actual_height)
        tiles.append({"index": index, "y": y, "height": actual_height,
                      "path": os.path.relpath(os.path.join(tiles_root, rel), ROOT)})
    magick_overview(src, os.path.join(page_dir, "overview-480w.png"), OVERVIEW_WIDTH)
    return {"page": page, "width": width, "height": height, "tiles": tiles}


def main() -> None:
    parser = argparse.ArgumentParser(description="Tier-A: slice cached screenshots into native-resolution tiles.")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--capture", help="capture date dir (default: newest)")
    parser.add_argument("--pages", nargs="*", help="page names to tile (default: every top-level .payloads/*.png)")
    args = parser.parse_args()

    capture = args.capture or latest_capture(args.slug)
    payloads = os.path.join(ROOT, "store", args.slug, "captures", capture, ".payloads")
    tiles_root = os.path.join(ROOT, "store", args.slug, "captures", capture, "tiles")
    if not os.path.isdir(payloads):
        raise SystemExit(f"no .payloads under store/{args.slug}/captures/{capture}")

    if args.pages:
        pages = args.pages
    else:  # every cached page screenshot; the QA gate / --pages curates out capture-experiment variants
        pages = sorted(f[:-4] for f in os.listdir(payloads) if f.endswith(".png"))

    records = [tile_page(payloads, tiles_root, page) for page in pages]
    manifest = {"slug": args.slug, "capture": capture, "source": "tile", "pages": records}
    with open(os.path.join(tiles_root, "manifest.json"), "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)

    made = [r for r in records if not r.get("missing")]
    missing = [r["page"] for r in records if r.get("missing")]
    print(f"tiled {len(made)} page(s) → store/{args.slug}/captures/{capture}/tiles/  "
          f"({sum(len(r['tiles']) for r in made)} tiles)")
    if missing:
        print(f"missing screenshots (skipped): {', '.join(missing)}")


if __name__ == "__main__":
    main()
