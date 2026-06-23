#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
EXP = Path("experiments/2026-06-13-visual-quality-v5-capture-clean-blind-judgment")
MANIFEST = ROOT / EXP / "cleaned-tile-manifest.json"
PRUNED = ROOT / EXP / "agent-outputs/judge_pruned_evidence.yaml"
SCORES = ROOT / EXP / "blind_pqr_lite_scores.yaml"


def main() -> int:
    manifest = json.loads(MANIFEST.read_text())
    active = set()
    excluded = set()
    for site in manifest["sites"]:
        for page in site["pages"]:
            active.update(tile["path"] for tile in page["tiles"])
            excluded.update(tile["path"] for tile in page.get("excluded_tiles", []))

    pruned = yaml.safe_load(PRUNED.read_text())
    card_ids = {card["id"] for card in pruned["accepted_cards"]}
    scores = yaml.safe_load(SCORES.read_text())

    failures = []
    evidence_count = 0
    for site in scores["site_scores"]:
        for dim_name, dim in site["dimensions"].items():
            evidence = dim.get("evidence", [])
            if not evidence:
                failures.append((site["site"], dim_name, "missing_evidence", ""))
            for item in evidence:
                evidence_count += 1
                if item in card_ids:
                    continue
                if item in excluded:
                    failures.append((site["site"], dim_name, "excluded_tile", item))
                elif item not in active:
                    failures.append((site["site"], dim_name, "unknown_reference", item))

    print(f"sites={len(scores['site_scores'])}")
    print(f"accepted_card_ids={len(card_ids)}")
    print(f"score_evidence_refs={evidence_count}")
    if failures:
        for site, dim, reason, ref in failures:
            print(f"FAIL {site} {dim} {reason}: {ref}")
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
