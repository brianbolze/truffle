"""Mechanical diff of paired wayback.py envelopes (June 8 pilot vs this re-run).

For tenure files: compares first_seen, last_seen, snapshot_count, confidence,
tenure_days. For diff files: compares selected snapshot timestamps, per-side
text hashes, and text_changed. Emits one JSON object to stdout. Movement
description only — no demand/traction inference.

Usage: python3 diff_wayback.py <baseline-dir> <rerun-dir>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def tenure_view(d: dict[str, Any]) -> dict[str, Any]:
    return {k: d.get(k) for k in
            ("first_seen", "last_seen", "first_seen_confidence",
             "tenure_days", "snapshot_count")}


def diff_view(d: dict[str, Any]) -> dict[str, Any]:
    sel = [s.get("timestamp") for s in d.get("selected_snapshots") or []]
    hashes = [c.get("text_sha256") for c in d.get("contents") or []]
    return {
        "selection_state": (d.get("selection") or {}).get("state"),
        "cdx_snapshot_count": (d.get("selection") or {}).get("snapshot_count"),
        "selected_timestamps": sel,
        "text_sha256": hashes,
        "text_changed": d.get("text_changed"),
        "ok": d.get("ok"),
    }


def main() -> None:
    base_dir, rerun_dir = Path(sys.argv[1]), Path(sys.argv[2])
    rows = []
    for base_file in sorted(base_dir.glob("*.json")):
        rerun_file = rerun_dir / base_file.name
        if not rerun_file.exists():
            rows.append({"name": base_file.stem, "status": "not run — no rerun file"})
            continue
        b = json.load(open(base_file))
        r = json.load(open(rerun_file))
        view = diff_view if (b.get("input") or {}).get("mode") == "diff" else tenure_view
        bv, rv = view(b), view(r)
        changed = sorted(k for k in bv if bv[k] != rv[k])
        rows.append({
            "name": base_file.stem,
            "mode": (b.get("input") or {}).get("mode", "tenure"),
            "url": (b.get("input") or {}).get("url"),
            "changed_fields": changed,
            "baseline": bv,
            "rerun": rv,
            "captured_at": {"baseline": b.get("captured_at"), "rerun": r.get("captured_at")},
        })
    out = {
        "tool": "wayback_pair_diff",
        "baseline_dir": str(base_dir),
        "rerun_dir": str(rerun_dir),
        "rows": rows,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
