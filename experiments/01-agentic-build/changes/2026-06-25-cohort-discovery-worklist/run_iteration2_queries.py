#!/usr/bin/env python3
"""Run the second cohort-discovery validation panel.

This is intentionally packet-local. It reruns the same raw source families used by
the first validation, but changes query construction: broad telehealth becomes a
small set of anchor-category query families derived from captured store language.
It writes raw tool envelopes under receipts/raw/iteration-2/ and does not score
or interpret the results.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
PACKET = Path(__file__).resolve().parent
RAW_DIR = PACKET / "receipts" / "raw" / "iteration-2"


QUERY_PANEL: list[dict[str, Any]] = [
    {
        "id": "telehealth-ed-serp",
        "cohort": "telehealth",
        "feeder": "category_serp",
        "tool": "serpapi",
        "query": "online erectile dysfunction treatment telehealth brand sildenafil tadalafil subscription 2026",
        "notes": "Derived from sexual-health/ED anchor language in captured BlueChew/Rugiet/Ro/Hims-style profiles; no holdout brand names.",
    },
    {
        "id": "telehealth-longevity-nad-serp",
        "cohort": "telehealth",
        "feeder": "category_serp",
        "tool": "serpapi",
        "query": "online longevity clinic NAD injections healthspan telehealth 2026",
        "notes": "Derived from longevity/NAD anchor language in captured AgelessRx/Eden/Shed/Rugiet-style profiles.",
    },
    {
        "id": "telehealth-healthspan-labs-serp",
        "cohort": "telehealth",
        "feeder": "category_serp",
        "tool": "serpapi",
        "query": "healthspan telehealth biomarkers longevity clinic online 2026",
        "notes": "Covers the healthspan/labs shape missed by the broad telehealth query.",
    },
    {
        "id": "telehealth-menopause-hrt-serp",
        "cohort": "telehealth",
        "feeder": "category_serp",
        "tool": "serpapi",
        "query": "online menopause HRT telehealth providers women's health 2026",
        "notes": "Retains one women/HRT family so the narrower panel does not regress the prior HRT coverage.",
    },
    {
        "id": "telehealth-glp1-serp",
        "cohort": "telehealth",
        "feeder": "category_serp",
        "tool": "serpapi",
        "query": "online GLP-1 weight loss telehealth providers 2026",
        "notes": "Retains the GLP-1 family that carried much of the first run.",
    },
    {
        "id": "telehealth-trt-serp",
        "cohort": "telehealth",
        "feeder": "category_serp",
        "tool": "serpapi",
        "query": "online TRT clinic testosterone replacement telehealth labs 2026",
        "notes": "Retains the TRT/hormone-optimization family that carried much of the first run.",
    },
    {
        "id": "telehealth-mens-health-demand-serp",
        "cohort": "telehealth",
        "feeder": "demand_serp",
        "tool": "serpapi",
        "query": "Strut Health TRT Nation alternatives men's health telehealth",
        "notes": "Demand-side query using non-holdout captured store anchors.",
    },
    {
        "id": "telehealth-longevity-demand-serp",
        "cohort": "telehealth",
        "feeder": "demand_serp",
        "tool": "serpapi",
        "query": "Healthspan Shed Function Health alternatives longevity telehealth",
        "notes": "Demand-side query using non-holdout captured store anchors.",
    },
    {
        "id": "telehealth-ed-exa",
        "cohort": "telehealth",
        "feeder": "exa_search",
        "tool": "exa_search",
        "query": "direct to consumer erectile dysfunction telehealth subscription brands sildenafil tadalafil chewable online clinic",
        "num_results": 25,
    },
    {
        "id": "telehealth-longevity-exa",
        "cohort": "telehealth",
        "feeder": "exa_search",
        "tool": "exa_search",
        "query": "direct to consumer longevity healthspan telehealth clinic NAD injections biomarker labs prescription",
        "num_results": 25,
    },
    {
        "id": "ci-ai-meeting-serp",
        "cohort": "conversation_intelligence",
        "feeder": "category_serp",
        "tool": "serpapi",
        "query": "AI meeting assistant tools for meeting notes summaries sales calls 2026",
    },
    {
        "id": "ci-conversation-intelligence-serp",
        "cohort": "conversation_intelligence",
        "feeder": "category_serp",
        "tool": "serpapi",
        "query": "conversation intelligence software sales call analysis Gong Clari alternatives 2026",
    },
    {
        "id": "ci-enterprise-call-analysis-serp",
        "cohort": "conversation_intelligence",
        "feeder": "category_serp",
        "tool": "serpapi",
        "query": "enterprise conversation intelligence software call recording coaching forecasting 2026",
    },
    {
        "id": "ci-meeting-notetaker-serp",
        "cohort": "conversation_intelligence",
        "feeder": "category_serp",
        "tool": "serpapi",
        "query": "AI meeting notetaker apps Otter Granola Fathom Fireflies 2026",
    },
    {
        "id": "ci-gong-demand-serp",
        "cohort": "conversation_intelligence",
        "feeder": "demand_serp",
        "tool": "serpapi",
        "query": "Gong alternatives conversation intelligence software Clari Chorus Avoma 2026",
    },
    {
        "id": "ci-notetaker-demand-serp",
        "cohort": "conversation_intelligence",
        "feeder": "demand_serp",
        "tool": "serpapi",
        "query": "Otter Granola Fathom alternatives AI meeting notes 2026",
    },
    {
        "id": "ci-meeting-notes-exa",
        "cohort": "conversation_intelligence",
        "feeder": "exa_search",
        "tool": "exa_search",
        "query": "AI meeting notes apps conversation intelligence software sales call analysis meeting summaries",
        "num_results": 25,
    },
    {
        "id": "ci-enterprise-ci-exa",
        "cohort": "conversation_intelligence",
        "feeder": "exa_search",
        "tool": "exa_search",
        "query": "enterprise conversation intelligence platforms call coaching revenue intelligence",
        "num_results": 25,
    },
]


def utc_now() -> str:
    """Return this run's UTC timestamp for summary provenance."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def output_path(row: dict[str, Any]) -> Path:
    """Return the raw JSON path for one panel row."""
    suffix = "serpapi" if row["tool"] == "serpapi" else "exa"
    return RAW_DIR / suffix / f"{row['id']}.json"


def command_for(row: dict[str, Any]) -> list[str]:
    """Build the subprocess command for one source-tool invocation."""
    if row["tool"] == "serpapi":
        return [sys.executable, "tools/serpapi.py", row["query"]]
    if row["tool"] == "exa_search":
        return [
            sys.executable,
            "tools/exa_search.py",
            row["query"],
            "--num-results",
            str(row.get("num_results", 25)),
        ]
    raise ValueError(f"Unsupported tool: {row['tool']}")


def classify_raw(row: dict[str, Any], out_path: Path, returncode: int | None = None) -> dict[str, Any]:
    """Classify whether a raw envelope is usable for retrieval scoring.

    SerpAPI exit 3 means AIO parser drift. That should stay visible, but the tool
    still emits organic results. For this packet's retrieval recall scorer, those
    organic rows are usable evidence even when AIO fields are suppressed.
    """
    try:
        data = json.loads(out_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {
            "capture_ok": False,
            "usable_for_scoring": False,
            "schema_drift": [],
        }

    schema_drift = data.get("schema_drift") or []
    capture_ok = bool(data.get("ok")) and (returncode in (None, 0))
    if row["tool"] == "serpapi":
        usable_for_scoring = bool(data.get("organic_results"))
    elif row["tool"] == "exa_search":
        usable_for_scoring = "results" in data
    else:
        usable_for_scoring = False

    return {
        "capture_ok": capture_ok,
        "usable_for_scoring": usable_for_scoring,
        "schema_drift": schema_drift,
    }


def run_query(row: dict[str, Any], skip_existing: bool) -> dict[str, Any]:
    """Run one query and persist stdout/stderr beside the raw envelope."""
    out_path = output_path(row)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    stderr_path = out_path.with_suffix(".stderr")
    if skip_existing and out_path.exists() and out_path.stat().st_size > 0:
        status = classify_raw(row, out_path)
        return {
            "id": row["id"],
            "cohort": row["cohort"],
            "feeder": row["feeder"],
            "tool": row["tool"],
            "skipped": True,
            "ok": status["capture_ok"] or status["usable_for_scoring"],
            "capture_ok": status["capture_ok"],
            "usable_for_scoring": status["usable_for_scoring"],
            "schema_drift": status["schema_drift"],
            "path": str(out_path),
        }

    proc = subprocess.run(
        command_for(row),
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=120,
    )
    out_path.write_text(proc.stdout, encoding="utf-8")
    stderr_path.write_text(proc.stderr, encoding="utf-8")
    status = classify_raw(row, out_path, returncode=proc.returncode)
    ok = status["capture_ok"] or status["usable_for_scoring"]
    return {
        "id": row["id"],
        "cohort": row["cohort"],
        "feeder": row["feeder"],
        "tool": row["tool"],
        "ok": ok,
        "capture_ok": status["capture_ok"],
        "usable_for_scoring": status["usable_for_scoring"],
        "schema_drift": status["schema_drift"],
        "returncode": proc.returncode,
        "path": str(out_path),
        "stderr_path": str(stderr_path),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run packet-local iteration-2 discovery source panel.")
    parser.add_argument("--skip-existing", action="store_true", help="Do not rerun rows that already have a nonempty raw JSON file.")
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    (RAW_DIR / "query-panel.json").write_text(json.dumps(QUERY_PANEL, indent=2) + "\n", encoding="utf-8")

    results = [run_query(row, skip_existing=args.skip_existing) for row in QUERY_PANEL]
    summary = {
        "captured_at": utc_now(),
        "panel_count": len(QUERY_PANEL),
        "ok_count": sum(1 for row in results if row["ok"]),
        "capture_ok_count": sum(1 for row in results if row.get("capture_ok")),
        "usable_for_scoring_count": sum(1 for row in results if row.get("usable_for_scoring")),
        "schema_drift_count": sum(1 for row in results if row.get("schema_drift")),
        "results": results,
    }
    (RAW_DIR / "run-summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    failures = [row for row in results if not row["ok"]]
    if failures:
        for row in failures:
            print(f"FAIL {row['id']} -> {row['stderr_path']}", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
