#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[3]
EXP = Path("experiments/2026-06-13-visual-quality-v5-capture-clean-blind-judgment")
PRIOR = Path("experiments/2026-06-13-gpt55-visual-quality-examples")
BASE_MANIFEST = ROOT / PRIOR / "tile-manifest.json"
FUNCTION_BROWSER_DIR = (
    PRIOR / "raw/browser-captures/function-homepage-iab-desktop-viewport-tiles"
)
FUNCTION_BROWSER_MANIFEST = ROOT / FUNCTION_BROWSER_DIR / "manifest.json"
FUNCTION_OVERVIEW = EXP / "raw/function-homepage-browser-viewport-overview-480w.png"
OUT_JSON = EXP / "cleaned-tile-manifest.json"
OUT_MD = EXP / "cleaned-tile-manifest.md"

TILE_EXCLUSIONS = {
    ("hallandalerx-com", "homepage"): {
        "paths": {
            "experiments/2026-06-13-gpt55-visual-quality-examples/tiles-clean/hallandalerx-com/homepage/tile-02-y02440.png"
        },
        "reason": (
            "Large blank grey media frame in the Redefining quality section; "
            "do not use as design evidence."
        ),
    }
}


def rel(path: Path) -> str:
    return path.as_posix()


def make_overview(tile_paths: list[Path], out_path: Path, width: int = 480) -> None:
    thumbs = []
    for tile_path in tile_paths:
        with Image.open(ROOT / tile_path) as im:
            im = im.convert("RGB")
            height = round(im.height * (width / im.width))
            thumbs.append(im.resize((width, height), Image.LANCZOS))

    total_height = sum(t.height for t in thumbs)
    sheet = Image.new("RGB", (width, total_height), "white")
    y = 0
    for thumb in thumbs:
        sheet.paste(thumb, (0, y))
        y += thumb.height

    out_abs = ROOT / out_path
    out_abs.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_abs)


def function_homepage_page() -> dict:
    with FUNCTION_BROWSER_MANIFEST.open() as f:
        manifest = json.load(f)

    captures = manifest["captures"]
    tile_paths = [FUNCTION_BROWSER_DIR / item["name"] for item in captures]
    make_overview(tile_paths, FUNCTION_OVERVIEW)

    return {
        "page": "homepage",
        "source_kind": "browser_viewport_restored",
        "source": rel(FUNCTION_BROWSER_DIR),
        "width": manifest["pageInfo"]["innerWidth"],
        "height": manifest["pageInfo"]["scrollHeight"],
        "viewport_height": manifest["pageInfo"]["innerHeight"],
        "overview": rel(FUNCTION_OVERVIEW),
        "qa_note": (
            "Restored from verified real-browser viewport tiles after warm scroll; "
            "not from broken Firecrawl homepage screenshots."
        ),
        "tiles": [
            {
                "index": item["i"],
                "y": item["actualY"],
                "height": manifest["pageInfo"]["innerHeight"],
                "path": rel(FUNCTION_BROWSER_DIR / item["name"]),
            }
            for item in captures
        ],
    }


def cleaned_page(site: dict, page: dict) -> dict:
    exclusion = TILE_EXCLUSIONS.get((site["slug"], page["page"]))
    excluded_paths = exclusion["paths"] if exclusion else set()
    active_tiles = [tile for tile in page["tiles"] if tile["path"] not in excluded_paths]
    excluded_tiles = [tile for tile in page["tiles"] if tile["path"] in excluded_paths]

    out = {
        "page": page["page"],
        "source_kind": "firecrawl_clean_tile",
        "source": page["source"],
        "width": page["width"],
        "height": page["height"],
        "overview": page["overview"],
        "tiles": active_tiles,
    }
    if excluded_tiles:
        out["excluded_tiles"] = excluded_tiles
        out["qa_note"] = exclusion["reason"]
    return out


def cleaned_site(site: dict) -> dict:
    pages = []
    if site["slug"] == "functionhealth-com":
        pages.append(function_homepage_page())

    for page in site["pages"]:
        pages.append(cleaned_page(site, page))

    return {
        "site": site["site"],
        "slug": site["slug"],
        "capture": site["capture"],
        "pages": pages,
    }


def write_markdown(manifest: dict) -> None:
    lines = [
        "# Cleaned blinded tile manifest",
        "",
        "Paths are relative to repo root. This worker-facing manifest contains only",
        "site/page/tile inventory and capture QA notes.",
        "",
        f"- Base clean tile source: `{PRIOR}/tiles-clean/`",
        f"- Function homepage restored source: `{FUNCTION_BROWSER_DIR}/`",
        f"- Tile height: {manifest['tile_height']}px; overlap: {manifest['overlap']}px where applicable",
        "",
    ]

    for site in manifest["sites"]:
        lines.extend(
            [
                f"## {site['site']}",
                "",
                f"- Store slug: `{site['slug']}`",
                f"- Capture: `{site['capture']}`",
            ]
        )
        for page in site["pages"]:
            note = f"; QA note: {page['qa_note']}" if page.get("qa_note") else ""
            excluded = (
                f"; {len(page['excluded_tiles'])} excluded tiles"
                if page.get("excluded_tiles")
                else ""
            )
            lines.append(
                f"- `{page['page']}` ({page['source_kind']}): "
                f"{page['width']}x{page['height']}; overview `{page['overview']}`; "
                f"{len(page['tiles'])} active tiles{excluded}{note}"
            )
        lines.append("")

    (ROOT / OUT_MD).write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    with BASE_MANIFEST.open() as f:
        base = json.load(f)

    manifest = {
        "experiment": EXP.as_posix(),
        "blinding": "Worker-facing tile inventory only; no external judgment inputs.",
        "tile_height": 1400,
        "overlap": 180,
        "sites": [cleaned_site(site) for site in base],
    }

    (ROOT / OUT_JSON).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    write_markdown(manifest)


if __name__ == "__main__":
    main()
