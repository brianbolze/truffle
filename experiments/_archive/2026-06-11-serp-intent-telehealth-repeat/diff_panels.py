"""Mechanical diff of two serp_intent_panel.py outputs (baseline vs rerun).

Compares per-query cohort visibility: own-page ranks, third-party mentions,
AI Overview presence/references, off-cohort counts, labels. Emits one JSON
object to stdout. Movement description only — no demand/traction inference.

Usage: python3 diff_panels.py <baseline-panel.json> <rerun-panel.json>
"""
from __future__ import annotations

import json
import sys
from typing import Any


def slug_positions(matches: list[dict[str, Any]], key: str = "position") -> dict[str, list[int]]:
    out: dict[str, list[int]] = {}
    for m in matches:
        out.setdefault(m["slug"], []).append(m[key])
    return {s: sorted(v) for s, v in out.items()}


def diff_slug_map(base: dict[str, list[int]], cur: dict[str, list[int]]) -> dict[str, Any]:
    new = sorted(set(cur) - set(base))
    dropped = sorted(set(base) - set(cur))
    moved = {}
    unchanged = {}
    for s in sorted(set(base) & set(cur)):
        if base[s] != cur[s]:
            moved[s] = {"baseline": base[s], "rerun": cur[s]}
        else:
            unchanged[s] = base[s]
    return {"new": new, "dropped": dropped, "moved": moved, "unchanged": unchanged}


def row_diff(b: dict[str, Any], r: dict[str, Any]) -> dict[str, Any]:
    b_aio, r_aio = b["ai_overview"], r["ai_overview"]
    return {
        "id": b["id"],
        "query": b["query"],
        "organic_top10_match_count": {"baseline": b["organic_top10_match_count"],
                                      "rerun": r["organic_top10_match_count"]},
        "own_pages": diff_slug_map(slug_positions(b["own_page_matches"]),
                                   slug_positions(r["own_page_matches"])),
        "mentions": diff_slug_map(slug_positions(b["third_party_mention_matches"]),
                                  slug_positions(r["third_party_mention_matches"])),
        "aio_present": {"baseline": b_aio["present"], "rerun": r_aio["present"]},
        "aio_references": diff_slug_map(
            slug_positions(b_aio["reference_matches"], key="reference_index"),
            slug_positions(r_aio["reference_matches"], key="reference_index")),
        "aio_ranked_brand_count": {"baseline": b_aio["ranked_brand_match_count"],
                                   "rerun": r_aio["ranked_brand_match_count"]},
        "off_cohort_count": {"baseline": b["serp_character"]["type_counts"].get("off_cohort", 0),
                             "rerun": r["serp_character"]["type_counts"].get("off_cohort", 0)},
        "labels": {"baseline": b.get("query_usefulness_labels", []),
                   "rerun": r.get("query_usefulness_labels", [])},
        "captured_at": {"baseline": b["capture"]["captured_at"],
                        "rerun": r["capture"]["captured_at"]},
    }


def main() -> None:
    baseline_path, rerun_path = sys.argv[1], sys.argv[2]
    base = json.load(open(baseline_path))
    cur = json.load(open(rerun_path))
    b_rows = {q["id"]: q for q in base["queries"]}
    r_rows = {q["id"]: q for q in cur["queries"]}
    out = {
        "tool": "serp_intent_panel_diff",
        "baseline_path": baseline_path,
        "rerun_path": rerun_path,
        "baseline_generated_at": base["generated_at"],
        "rerun_generated_at": cur["generated_at"],
        "query_ids_match": sorted(b_rows) == sorted(r_rows),
        "rows": [row_diff(b_rows[i], r_rows[i]) for i in sorted(b_rows) if i in r_rows],
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
