#!/usr/bin/env python3
from __future__ import annotations

import json
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[3]
EXP = Path("experiments/2026-06-13-visual-quality-v5-capture-clean-blind-judgment")
MANIFEST = ROOT / EXP / "cleaned-tile-manifest.json"
OUT = ROOT / EXP / "raw/overview-contact-sheet.png"


def load_font(size: int = 18):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    font = load_font(18)
    small = load_font(14)
    col_w = 300
    label_h = 76
    gap = 18
    cols = 4
    cells = []

    for site in manifest["sites"]:
        for page in site["pages"]:
            overview = ROOT / page["overview"]
            with Image.open(overview) as im:
                im = im.convert("RGB")
                thumb_h = round(im.height * (col_w / im.width))
                thumb = im.resize((col_w, thumb_h), Image.LANCZOS)
            label = f"{site['site']} / {page['page']}\n{page['source_kind']} · {len(page['tiles'])} tiles"
            cell = Image.new("RGB", (col_w, label_h + thumb_h), "white")
            draw = ImageDraw.Draw(cell)
            y = 8
            for line in textwrap.wrap(label, width=34):
                draw.text((8, y), line, fill=(20, 20, 20), font=font if y == 8 else small)
                y += 22
            cell.paste(thumb, (0, label_h))
            cells.append(cell)

    rows = (len(cells) + cols - 1) // cols
    row_heights = []
    for r in range(rows):
        row_cells = cells[r * cols : (r + 1) * cols]
        row_heights.append(max(cell.height for cell in row_cells))

    sheet_w = cols * col_w + (cols + 1) * gap
    sheet_h = sum(row_heights) + (rows + 1) * gap
    sheet = Image.new("RGB", (sheet_w, sheet_h), (245, 245, 242))

    y = gap
    for r in range(rows):
        x = gap
        for cell in cells[r * cols : (r + 1) * cols]:
            sheet.paste(cell, (x, y))
            x += col_w + gap
        y += row_heights[r] + gap

    OUT.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(OUT)


if __name__ == "__main__":
    main()
