#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
EXP = Path("experiments/2026-06-13-visual-quality-v5-capture-clean-blind-judgment")
MANIFEST = ROOT / EXP / "cleaned-tile-manifest.json"
AGENT_DIR = ROOT / EXP / "agent-outputs"


def main() -> int:
    manifest = json.loads(MANIFEST.read_text())
    active = set()
    excluded = set()
    for site in manifest["sites"]:
        for page in site["pages"]:
            active.update(tile["path"] for tile in page["tiles"])
            excluded.update(tile["path"] for tile in page.get("excluded_tiles", []))

    failures = []
    total = 0
    for path in sorted(AGENT_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text())
        cards = data.get("cards", []) + data.get("accepted_cards", [])
        for card in cards:
            total += 1
            tile_path = card.get("tile_path")
            if tile_path in excluded:
                failures.append((path.name, tile_path, "excluded"))
            elif tile_path not in active:
                failures.append((path.name, tile_path, "not_active"))

    print(f"checked_cards={total}")
    print(f"active_tile_paths={len(active)}")
    print(f"excluded_tile_paths={len(excluded)}")
    if failures:
        for source, tile_path, reason in failures:
            print(f"FAIL {source} {reason}: {tile_path}")
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
