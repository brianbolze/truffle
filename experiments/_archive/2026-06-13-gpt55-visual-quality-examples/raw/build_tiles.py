#!/usr/bin/env python3
"""Build native-resolution screenshot tiles for the GPT-5.5 visual-quality run."""

from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RUN = ROOT / "experiments/2026-06-13-gpt55-visual-quality-examples"
TILES = RUN / "tiles-clean"

TILE_HEIGHT = 1400
OVERLAP = 180

SITES = [
    {
        "site": "functionhealth.com",
        "slug": "functionhealth-com",
        "capture": "2026-06-01",
        "anchor": "high control; Brian rating snapshot 10; homepage excluded because Firecrawl rendered the real hero media as a flat grey block",
        "pages": ["pricing", "scans"],
    },
    {
        "site": "ro.co",
        "slug": "ro-co",
        "capture": "2026-06-04",
        "anchor": "high control; Brian rating snapshot 8",
        "pages": ["homepage", "weight-loss", "pricing", "os"],
    },
    {
        "site": "nurx.com",
        "slug": "nurx-com",
        "capture": "2026-06-04",
        "anchor": "high control; Brian rating snapshot 7",
        "pages": ["homepage", "our_services", "team", "weight_management"],
    },
    {
        "site": "hallandalerx.com",
        "slug": "hallandalerx-com",
        "capture": "2026-06-02",
        "anchor": "high-ish control; Brian rating snapshot 8",
        "pages": ["homepage", "products", "quality", "new-provider-landing"],
    },
    {
        "site": "gogeviti.com",
        "slug": "gogeviti-com",
        "capture": "2026-06-03",
        "anchor": "mid/high control; Brian rating snapshot 7; prior distinctive-art-direction trap",
        "pages": ["homepage", "pricing", "blueprint", "clinic"],
    },
    {
        "site": "joinamble.com",
        "slug": "joinamble-com",
        "capture": "2026-06-13",
        "anchor": "mid control; Brian rating snapshot 7; prior overrating trap; recaptured with Transcend consent dismissed",
        "pages": ["homepage", "glp1", "sermorelin", "nad"],
    },
    {
        "site": "hellopepti.com",
        "slug": "hellopepti-com",
        "capture": "2026-06-13",
        "anchor": "mid control; Brian rating snapshot 6; prior visual-ambition trap; recaptured with cookie bar removed",
        "pages": ["homepage", "how_it_works", "about", "providers"],
    },
    {
        "site": "belmarpharmasolutions.com",
        "slug": "belmarpharmasolutions-com",
        "capture": "2026-06-13",
        "anchor": "low/mid control; Brian rating snapshot 4; coherent-B2B-template trap; recaptured with CookieYes banner rejected",
        "pages": ["homepage", "clinicians", "open-account", "account-form"],
    },
    {
        "site": "millspharmacy.com",
        "slug": "millspharmacy-com",
        "capture": "2026-06-13",
        "anchor": "low control; Brian rating snapshot 4; duplicated vendor-template blocks; recaptured to remove newsletter/cookie overlays",
        "pages": ["homepage", "compounding", "quality_safety", "weight_management"],
    },
    {
        "site": "jinfiniti.com",
        "slug": "jinfiniti-com",
        "capture": "2026-06-09",
        "anchor": "low control; Brian rating snapshot 3; amateur charts/illustration target",
        "pages": ["homepage", "agingsos_advanced_panel", "intracellular_nad_test", "shop"],
    },
    {
        "site": "kingsbergmedical.com",
        "slug": "kingsbergmedical-com",
        "capture": "2026-06-09",
        "anchor": "low control; Brian rating snapshot 2",
        "pages": ["homepage", "services", "testosterone", "semaglutide"],
    },
    {
        "site": "anazaohealth.com",
        "slug": "anazaohealth-com",
        "capture": "2026-06-09",
        "anchor": "low control; Brian rating snapshot 2; stock/clipart/template target",
        "pages": ["homepage", "hormone_replacement_therapy", "weight_management", "quality"],
    },
    {
        "site": "goinfusive.com",
        "slug": "goinfusive-com",
        "capture": "2026-06-09",
        "anchor": "low control; Brian rating snapshot 2.5; dark-gradient template seduction trap",
        "pages": ["homepage", "services", "platform", "qualify"],
    },
]


def identify(path: Path) -> tuple[int, int]:
    output = subprocess.check_output(
        ["magick", "identify", "-format", "%w %h", str(path)],
        text=True,
    )
    width, height = output.strip().split()
    return int(width), int(height)


def crop_tile(src: Path, dst: Path, width: int, y: int, height: int) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.check_call(
        [
            "magick",
            str(src),
            "-crop",
            f"{width}x{height}+0+{y}",
            "+repage",
            str(dst),
        ]
    )


def make_overview(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.check_call(["magick", str(src), "-resize", "480x", str(dst)])


def main() -> None:
    manifest: list[dict] = []
    missing: list[str] = []

    for site in SITES:
        site_record = {
            "site": site["site"],
            "slug": site["slug"],
            "capture": site["capture"],
            "anchor": site["anchor"],
            "pages": [],
        }
        for page in site["pages"]:
            src = (
                ROOT
                / "store"
                / site["slug"]
                / "captures"
                / site["capture"]
                / ".payloads"
                / f"{page}.png"
            )
            if not src.exists():
                missing.append(str(src.relative_to(ROOT)))
                continue

            width, height = identify(src)
            step = TILE_HEIGHT - OVERLAP
            tile_count = max(1, math.ceil(max(height - OVERLAP, 1) / step))
            page_dir = TILES / site["slug"] / page
            tiles = []
            for index in range(tile_count):
                y = min(index * step, max(height - TILE_HEIGHT, 0))
                actual_height = min(TILE_HEIGHT, height - y)
                dst = page_dir / f"tile-{index:02d}-y{y:05d}.png"
                crop_tile(src, dst, width, y, actual_height)
                tiles.append(
                    {
                        "index": index,
                        "y": y,
                        "height": actual_height,
                        "path": str(dst.relative_to(ROOT)),
                    }
                )

            overview = page_dir / "overview-480w.png"
            make_overview(src, overview)
            site_record["pages"].append(
                {
                    "page": page,
                    "source": str(src.relative_to(ROOT)),
                    "width": width,
                    "height": height,
                    "overview": str(overview.relative_to(ROOT)),
                    "tiles": tiles,
                }
            )
        manifest.append(site_record)

    (RUN / "tile-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    lines = [
        "# Tile manifest",
        "",
        f"Tile height: {TILE_HEIGHT}px; overlap: {OVERLAP}px. Paths are relative to repo root.",
        "",
    ]
    for site in manifest:
        lines.extend(
            [
                f"## {site['site']}",
                "",
                f"- Store slug: `{site['slug']}`",
                f"- Capture: `{site['capture']}`",
                f"- Anchor note: {site['anchor']}",
            ]
        )
        for page in site["pages"]:
            lines.append(
                f"- `{page['page']}`: {page['width']}x{page['height']}; "
                f"overview `{page['overview']}`; {len(page['tiles'])} tiles"
            )
        lines.append("")
    if missing:
        lines.extend(["## Missing inputs", ""])
        lines.extend(f"- `{item}`" for item in missing)
        lines.append("")
    (RUN / "tile-manifest.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
