#!/usr/bin/env python3
"""Compare Codex capture-readiness rows against Claude's qualifier output.

The point is not to crown a classifier. It is to expose where two independently
shaped gates disagree, then turn that disagreement into a smaller human decision
surface.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OUTPUT_DIR = Path(__file__).resolve().parent
PACKET = OUTPUT_DIR.parents[0]
CLAUDE_DIR = PACKET / "claude-prototyping"

CODEX_RESULTS_PATH = OUTPUT_DIR / "codex_capture_readiness_results.json"
CLAUDE_ROUTED_PATHS = (
    CLAUDE_DIR / "routed-conversation-intelligence.jsonl",
    CLAUDE_DIR / "routed-telehealth.jsonl",
)
RESULTS_PATH = OUTPUT_DIR / "codex_claude_comparison_results.json"
SUMMARY_PATH = OUTPUT_DIR / "codex_claude_comparison_summary.md"


@dataclass(frozen=True)
class FinalCall:
    """Manual adjudication for rows where route labels alone are insufficient."""

    route: str
    reason: str
    confidence: str = "medium"


FINAL_OVERRIDES: dict[str, FinalCall] = {
    "coffee.ai": FinalCall("cohort_fit_review", "Own product is an AI CRM agent; useful adjacent GTM context, not yet full CI capture."),
    "sybill.ai": FinalCall("capture_ready", "Claude's product read plus homepage evidence indicate own sales assistant / call-summary product."),
    "get-alfred.ai": FinalCall("cohort_fit_review", "Source says AI notetaker, homepage says email/calendar assistant; resolve before capture."),
    "useluminix.com": FinalCall("preserve_source_evidence", "Homepage is deep-research/newsletter; owned notetaker comparison is useful biased source evidence only."),
    "cuebo.ai": FinalCall("cohort_fit_review", "Sales roleplay/coaching is adjacent to CI; capture value needs synthesis test."),
    "knowlee.ai": FinalCall("preserve_source_evidence", "AI workforce vendor appears via owned CI listicle, but homepage is not a CI product."),
    "plotline.health": FinalCall("cohort_fit_review", "Concierge/longevity care may matter for healthspan neighborhood, but not clearly DTC telehealth capture."),
    "holisticare.io": FinalCall("preserve_source_evidence", "B2B clinic software; preserve as care-delivery/clinic-platform context, not profile capture."),
    "madisonhealthny.com": FinalCall("cohort_fit_review", "Own online TRT service, but local clinic scope keeps it out of automatic capture."),
    "superpower.com": FinalCall("cohort_fit_review", "Potentially important Function/longevity neighbor; promote only after synthesis test."),
    "jointhecollaborative.com": FinalCall("preserve_source_evidence", "Concierge menopause clinic evidence is useful, but local/high-touch scope weakens full-capture case."),
    "getrafiki.ai": FinalCall("capture_ready", "Homepage and Claude both indicate own conversation/revenue intelligence product."),
    "oliv.ai": FinalCall("capture_ready", "Own revenue AI platform around deal/call intelligence; owned listicle should be caveated, not disqualifying."),
    "vibrant-wellness.com": FinalCall("preserve_source_evidence", "Specialty lab/provider infrastructure; useful source/card, not DTC telehealth capture."),
    "vaamo.ai": FinalCall("cohort_fit_review", "Sales coaching platform looks adjacent; not enough to make full CI capture obvious."),
    "heysam.ai": FinalCall("capture_ready", "Homepage explicitly says conversation intelligence in Slack plus CRM hygiene/RFP agents."),
    "telyrx.com": FinalCall("preserve_source_evidence", "Duplicate row; capture should be driven by the primary TelyRx row."),
    "evro.ai": FinalCall("preserve_source_evidence", "Communication-coach product is adjacent, and owned Otter-alternatives page is biased source evidence."),
    "walgreens.com": FinalCall("preserve_source_evidence", "Real GLP-1 telehealth surface, but broad retailer profile is not clearly useful cohort capture."),
    "salessavvy.ai": FinalCall("cohort_fit_review", "Sales intelligence assistant evidence is thin; keep for review before profile capture."),
    "getmaxiq.com": FinalCall("capture_ready", "Homepage says AI-native revenue intelligence platform; useful for CI/revenue-intel comparison."),
}


def utc_now() -> str:
    """Return a stable UTC timestamp for generated artifacts."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json(path: Path) -> Any:
    """Load JSON with explicit encoding."""
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data: Any) -> None:
    """Write generated JSON for inspection."""
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")


def canonical_domain(value: str | None) -> str | None:
    """Normalize URLs/domains into a bare host."""
    if not value:
        return None
    raw = value.strip().lower()
    raw = re.sub(r"^https?://", "", raw).split("/", maxsplit=1)[0].split(":", maxsplit=1)[0]
    return raw.removeprefix("www.") or None


def canonical_cohort(value: str) -> str:
    """Normalize cohort spelling across the two prototype lanes."""
    return value.replace("_", "-")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    """Load JSONL records with explicit encoding."""
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                row = json.loads(line)
                row["source_file"] = path.name
                rows.append(row)
    return rows


def load_claude_rows() -> list[dict[str, Any]]:
    """Load Claude routed rows from both cohort files."""
    rows: list[dict[str, Any]] = []
    for path in CLAUDE_ROUTED_PATHS:
        rows.extend(load_jsonl(path))
    return rows


def index_claude(rows: list[dict[str, Any]]) -> dict[tuple[str, str], dict[str, Any]]:
    """Index Claude rows by cohort/domain."""
    index: dict[tuple[str, str], dict[str, Any]] = {}
    for row in rows:
        domain = canonical_domain(row.get("domain"))
        if domain:
            index[(canonical_cohort(str(row["cohort"])), domain)] = row
    return index


def normalized_claude_route(row: dict[str, Any] | None) -> str:
    """Map Claude routes into the Codex readiness menu for comparison."""
    if row is None:
        return "missing_in_claude"
    route = row["route"]
    if route == "capture":
        return "capture_ready"
    if route == "preserve":
        return "preserve_source_evidence"
    if route == "review":
        return "cohort_fit_review"
    if route == "drop":
        return "reject_or_defer"
    if route == "product":
        return "preserve_source_evidence"
    return "boundary_review"


def compare_class(codex_row: dict[str, Any], claude_row: dict[str, Any] | None, domain: str) -> str:
    """Classify the relationship between the two prototype calls."""
    codex_route = codex_row["capture_readiness"]["route"]
    claude_norm = normalized_claude_route(claude_row)
    if claude_row is None:
        return "missing_in_claude"
    if codex_route == "existing_profile" and claude_norm == "capture_ready":
        return "aligned_store_awareness_gap"
    if codex_route == "existing_profile" and claude_norm == "preserve_source_evidence":
        return "store_source_role_split"
    if codex_row["capture_readiness"].get("duplicate_of") and claude_norm == "capture_ready":
        return "aligned_duplicate_handling_gap"
    if codex_route == claude_norm:
        return "aligned"
    if domain in FINAL_OVERRIDES:
        return "disagreement_adjudicated"
    if codex_route in {"cohort_fit_review", "preserve_source_evidence"} and claude_norm == "capture_ready":
        return "claude_more_aggressive"
    if codex_route == "capture_ready" and claude_norm in {"cohort_fit_review", "preserve_source_evidence", "reject_or_defer"}:
        return "codex_more_aggressive"
    return "route_disagreement"


def default_final_call(codex_row: dict[str, Any], claude_row: dict[str, Any] | None, domain: str) -> FinalCall:
    """Pick a proposed final route from agreement or explicit adjudication."""
    codex_route = codex_row["capture_readiness"]["route"]
    claude_norm = normalized_claude_route(claude_row)
    if domain in FINAL_OVERRIDES:
        return FINAL_OVERRIDES[domain]
    if codex_route == "existing_profile":
        return FinalCall("existing_profile", "Store baseline wins; do not create duplicate capture work.", "high")
    if claude_row is None:
        return FinalCall(codex_route, "Absent from Claude's broader routed set; keep Codex no-spend readiness call.", "medium")
    if codex_row["capture_readiness"].get("duplicate_of"):
        return FinalCall("preserve_source_evidence", "Duplicate evidence row; preserve while capturing via the primary candidate.", "high")
    if codex_route == claude_norm:
        return FinalCall(codex_route, "Codex and Claude agree after route normalization.", "high")
    if codex_route == "cohort_fit_review" or claude_norm == "cohort_fit_review":
        return FinalCall("cohort_fit_review", "At least one lane says review; do not promote before adjudication.", "medium")
    return FinalCall(codex_route, "No override; keep Codex route and flag for audit.", "low")


def compact_codex(row: dict[str, Any]) -> dict[str, Any]:
    """Serialize the Codex side for comparison."""
    readiness = row["capture_readiness"]
    resolution = row["boundary_resolution"]
    return {
        "route": readiness["route"],
        "actor_role": readiness["actor_role"],
        "confidence": readiness["confidence_band"],
        "reasons": readiness["reasons"],
        "caveats": readiness["caveats"],
        "duplicate_of": readiness.get("duplicate_of"),
        "resolved_domain": resolution.get("resolved_domain"),
        "boundary_method": resolution.get("method"),
        "source_role": row["evidence_snapshot"]["source_role"],
    }


def compact_claude(row: dict[str, Any] | None) -> dict[str, Any] | None:
    """Serialize the Claude side for comparison."""
    if row is None:
        return None
    return {
        "route": row["route"],
        "normalized_route": normalized_claude_route(row),
        "kind": row["kind"],
        "confidence": row["confidence"],
        "reason": row["reason"],
        "peeked": row.get("peeked"),
        "is_source_domain": row.get("is_source_domain"),
        "source_file": row.get("source_file"),
    }


def comparison_row(codex_row: dict[str, Any], claude_row: dict[str, Any] | None) -> dict[str, Any]:
    """Build one row in the joined comparison table."""
    domain = canonical_domain(codex_row["boundary_resolution"].get("resolved_domain") or codex_row.get("domain")) or ""
    final = default_final_call(codex_row, claude_row, domain)
    return {
        "candidate_id": codex_row["candidate_id"],
        "cohort": codex_row["cohort"],
        "rank": codex_row["rank"],
        "name": codex_row["name"],
        "domain": domain,
        "codex": compact_codex(codex_row),
        "claude": compact_claude(claude_row),
        "comparison_class": compare_class(codex_row, claude_row, domain),
        "proposed_final": {
            "route": final.route,
            "confidence": final.confidence,
            "reason": final.reason,
        },
    }


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize agreement, disagreements, and proposed final routes."""
    by_cohort: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_cohort[row["cohort"]].append(row)

    cohorts: dict[str, Any] = {}
    for cohort, cohort_rows in sorted(by_cohort.items()):
        cohorts[cohort] = {
            "input_rows": len(cohort_rows),
            "comparison_class_counts": dict(sorted(Counter(row["comparison_class"] for row in cohort_rows).items())),
            "codex_route_counts": dict(sorted(Counter(row["codex"]["route"] for row in cohort_rows).items())),
            "claude_normalized_route_counts": dict(
                sorted(Counter((row["claude"] or {}).get("normalized_route", "missing_in_claude") for row in cohort_rows).items())
            ),
            "proposed_final_route_counts": dict(sorted(Counter(row["proposed_final"]["route"] for row in cohort_rows).items())),
        }

    return {
        "schema": "codex-claude-comparison-eval-v0",
        "input_rows": len(rows),
        "comparison_class_counts": dict(sorted(Counter(row["comparison_class"] for row in rows).items())),
        "codex_route_counts": dict(sorted(Counter(row["codex"]["route"] for row in rows).items())),
        "claude_normalized_route_counts": dict(
            sorted(Counter((row["claude"] or {}).get("normalized_route", "missing_in_claude") for row in rows).items())
        ),
        "proposed_final_route_counts": dict(sorted(Counter(row["proposed_final"]["route"] for row in rows).items())),
        "cohorts": cohorts,
        "live_spend_used": {
            "direct_http_homepages": 0,
            "serpapi_queries": 0,
            "firecrawl_homepage_scrapes": 0,
        },
    }


def markdown_table(rows: list[list[str]]) -> list[str]:
    """Render a compact Markdown table."""
    if not rows:
        return []
    output = [
        "| " + " | ".join(rows[0]) + " |",
        "| " + " | ".join("---" for _ in rows[0]) + " |",
    ]
    for row in rows[1:]:
        output.append("| " + " | ".join(row) + " |")
    return output


def route_label(row: dict[str, Any]) -> str:
    """Return compact Codex vs Claude label."""
    claude_route = (row["claude"] or {}).get("route", "missing")
    return f"{row['codex']['route']} / {claude_route}"


def write_summary(output: dict[str, Any]) -> None:
    """Write a disagreement-first readout."""
    evaluation = output["evaluation"]
    rows = output["results"]
    lines = [
        "# Codex vs Claude Capture Gate Comparison",
        "",
        "Date: 2026-06-26",
        "Status: packet-local comparison over the 61 Codex capture-readiness rows; no engine changes",
        "",
        "## Read",
        "",
        "- Joined Codex capture-readiness rows to Claude routed candidates by cohort + resolved domain.",
        "- Claude did not model existing store profiles separately, so `existing_profile` vs Claude `capture` is treated as store-awareness alignment.",
        "- Proposed final routes are comparison guidance, not durable Truffle design.",
        "",
        "## Counts",
        "",
    ]
    counts = [["Metric", "Counts"]]
    for key in ("comparison_class_counts", "codex_route_counts", "claude_normalized_route_counts", "proposed_final_route_counts"):
        counts.append([key, json.dumps(evaluation[key], sort_keys=True)])
    lines.extend(markdown_table(counts))
    lines.extend(["", "## By Cohort", ""])
    cohort_rows = [["Cohort", "Input", "Comparison classes", "Proposed final routes"]]
    for cohort, stats in evaluation["cohorts"].items():
        cohort_rows.append(
            [
                cohort,
                str(stats["input_rows"]),
                json.dumps(stats["comparison_class_counts"], sort_keys=True),
                json.dumps(stats["proposed_final_route_counts"], sort_keys=True),
            ]
        )
    lines.extend(markdown_table(cohort_rows))

    disagreements = [
        row
        for row in rows
        if row["comparison_class"]
        not in {"aligned", "aligned_store_awareness_gap", "aligned_duplicate_handling_gap"}
    ]
    lines.extend(["", "## Disagreements / Missing", ""])
    table = [["Cohort", "Rank", "Domain", "Codex / Claude", "Class", "Proposed final", "Reason"]]
    for row in disagreements:
        table.append(
            [
                row["cohort"],
                str(row["rank"]),
                row["domain"],
                route_label(row),
                row["comparison_class"],
                row["proposed_final"]["route"],
                row["proposed_final"]["reason"],
            ]
        )
    lines.extend(markdown_table(table))

    lines.extend(["", "## Capture-Ready Proposal", ""])
    capture_rows = [row for row in rows if row["proposed_final"]["route"] == "capture_ready"]
    capture_table = [["Cohort", "Rank", "Domain", "Name", "Why"]]
    for row in capture_rows:
        capture_table.append([row["cohort"], str(row["rank"]), row["domain"], row["name"], row["proposed_final"]["reason"]])
    lines.extend(markdown_table(capture_table))

    lines.extend(
        [
            "",
            "## Files",
            "",
            f"- Results JSON: `{RESULTS_PATH.name}`",
            f"- Summary: `{SUMMARY_PATH.name}`",
            "",
            "## Readout",
            "",
            "The two lanes agree on the basic shape: source/publisher artifacts should not become captures, and real dual-role companies need product evidence. The main tension is calibration: Claude is more willing to capture owned in-cohort offerings, while Codex is more conservative around adjacent tools, local clinics, and broad health giants.",
            "",
        ]
    )
    with SUMMARY_PATH.open("w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def run() -> dict[str, Any]:
    """Run the comparison and write artifacts."""
    codex_rows = load_json(CODEX_RESULTS_PATH)["results"]
    claude_rows = load_claude_rows()
    claude_index = index_claude(claude_rows)
    rows: list[dict[str, Any]] = []
    for codex_row in codex_rows:
        domain = canonical_domain(codex_row["boundary_resolution"].get("resolved_domain") or codex_row.get("domain"))
        key = (canonical_cohort(str(codex_row["cohort"])), domain or "")
        rows.append(comparison_row(codex_row, claude_index.get(key)))
    output = {
        "schema": "codex-claude-comparison-results-v0",
        "generated_at": utc_now(),
        "inputs": {
            "codex": str(CODEX_RESULTS_PATH.relative_to(OUTPUT_DIR)),
            "claude": [str(path.relative_to(PACKET)) for path in CLAUDE_ROUTED_PATHS],
            "join_key": "cohort + resolved_domain",
        },
        "results": rows,
        "evaluation": summarize(rows),
    }
    write_json(RESULTS_PATH, output)
    write_summary(output)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare Codex capture readiness with Claude routed output.")
    parser.parse_args()
    output = run()
    print(
        json.dumps(
            {
                "results": len(output["results"]),
                "comparison_class_counts": output["evaluation"]["comparison_class_counts"],
                "proposed_final_route_counts": output["evaluation"]["proposed_final_route_counts"],
                "live_spend_used": output["evaluation"]["live_spend_used"],
                "outputs": {
                    "results": str(RESULTS_PATH),
                    "summary": str(SUMMARY_PATH),
                },
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
