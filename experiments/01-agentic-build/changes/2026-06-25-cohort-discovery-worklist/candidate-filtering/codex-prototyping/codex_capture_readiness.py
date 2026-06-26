#!/usr/bin/env python3
"""Gate boundary-resolved candidates by capture usefulness, not just existence.

Boundary resolution answered "is there a plausible official surface?" This
packet-local slice asks the narrower coverage question: is full
`/research-company` capture better than preserving the evidence and a light
candidate card?
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OUTPUT_DIR = Path(__file__).resolve().parent
CANDIDATE_FILTERING = OUTPUT_DIR.parents[0]
PACKET = CANDIDATE_FILTERING.parent
if str(OUTPUT_DIR) not in sys.path:
    sys.path.insert(0, str(OUTPUT_DIR))
if str(PACKET) not in sys.path:
    sys.path.insert(0, str(PACKET))

from codex_boundary_resolution import (  # noqa: E402
    Qrel,
    best_qrel,
    build_qrels,
    canonical_domain,
    compact_norm,
    domain_stem,
    is_bad_or_boundary_eval,
    is_relevant_eval,
)

BOUNDARY_RESULTS_PATH = OUTPUT_DIR / "codex_boundary_resolution_results.json"
RESULTS_PATH = OUTPUT_DIR / "codex_capture_readiness_results.json"
SUMMARY_PATH = OUTPUT_DIR / "codex_capture_readiness_summary.md"
CACHE_DIR = OUTPUT_DIR / "boundary-resolution-cache"
HOMEPAGE_DIR = CACHE_DIR / "homepages"
FIRECRAWL_DIR = CACHE_DIR / "firecrawl"

INPUT_ROUTES = {"capture_candidate", "existing_profile"}
ROUTES = (
    "existing_profile",
    "capture_ready",
    "cohort_fit_review",
    "preserve_source_evidence",
    "reject_or_defer",
    "boundary_review",
)

LISTICLE_RE = re.compile(
    r"\b(best|top|alternatives?|competitors?|vs\.?|versus|compared|comparison|guide|pricing|ranked|buyer'?s guide)\b",
    re.IGNORECASE,
)
SOURCE_ONLY_RE = re.compile(r"\b(newsletter|directory|marketplace|reviews?|roundup|listicle)\b", re.IGNORECASE)

CI_STRONG_RE = re.compile(
    r"\b("
    r"conversation intelligence|conversational intelligence|revenue intelligence|ai notetaker|note taker|notetaker|"
    r"meeting assistant|meeting notes?|meeting insights?|meeting workflows?|transcription|"
    r"call coaching|sales coaching|sales meeting|sales calls?|salesforce data"
    r")\b",
    re.IGNORECASE,
)
CI_WEAK_RE = re.compile(
    r"\b("
    r"sales intelligence|crm agent|crm updates?|pipeline|forecasting|revops|"
    r"revenue teams?|sales teams?|deal questions?|buying signals|outreach|ai workforce|communication coach"
    r")\b",
    re.IGNORECASE,
)
CI_PRESERVE_RE = re.compile(r"\b(email & calendar|calendar assistant|deep research|newsletter)\b", re.IGNORECASE)

TELEHEALTH_CORE_RE = re.compile(
    r"\b("
    r"telehealth|online doctor|online visit|online hrt|online prescriptions?|"
    r"hormone replacement|menopause|trt|testosterone|erectile dysfunction|ed treatment|"
    r"medical weight loss|glp-?1|clinician|physicians?|prescription"
    r")\b",
    re.IGNORECASE,
)
TELEHEALTH_DIRECT_RE = re.compile(
    r"\b("
    r"serving 48 states|online doctor|online visits?|online hrt|online prescriptions?|"
    r"fast delivery|get rx approvals online|care team in your pocket|membership includes|"
    r"reviewed by board-certified physicians|telehealth"
    r")\b",
    re.IGNORECASE,
)
TELEHEALTH_ADJACENT_RE = re.compile(
    r"\b("
    r"platform for clinics|platform helps|lab testing|test catalog|biomarker|biomarkers|"
    r"for providers|licensed providers|longevity platform|healthspan|concierge healthcare|"
    r"functional medicine|wellness platform"
    r")\b",
    re.IGNORECASE,
)
LOCAL_CLINIC_RE = re.compile(
    r"\b("
    r"clearwater|nyc|new york|bay area|san francisco|palo alto|near me|"
    r"clinic in|functional medicine in|men'?s health clinic|premier .* clinic|book now|discovery call"
    r")\b",
    re.IGNORECASE,
)
BROAD_HEALTH_RE = re.compile(
    r"\b("
    r"walgreens|pharmacy, health & wellness|photo gifts|store pickup|contact lenses|"
    r"retail pharmacy|broad pharmacy"
    r")\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class EvidenceSnapshot:
    """Compact no-spend evidence used by the usefulness gate."""

    source_role: str
    source_titles: tuple[str, ...]
    source_domains: tuple[str, ...]
    homepage_title: str | None = None
    homepage_description: str | None = None
    homepage_text_excerpt: str | None = None
    homepage_cache_path: str | None = None


@dataclass
class ReadinessDecision:
    """A route plus the visible judgement inputs that produced it."""

    route: str
    confidence_band: str
    actor_role: str
    full_capture_better_than_card: bool
    neighborhood_context: bool
    cross_company_synthesis: bool
    reasons: list[str] = field(default_factory=list)
    caveats: list[str] = field(default_factory=list)
    duplicate_of: str | None = None


def utc_now() -> str:
    """Return a stable UTC timestamp for generated prototype artifacts."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slug(value: str) -> str:
    """Create the same cache-key shape used by boundary resolution."""
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def clean_text(value: str) -> str:
    """Normalize whitespace for evidence matching and display."""
    return re.sub(r"\s+", " ", value).strip()


def load_json(path: Path) -> Any:
    """Load JSON with explicit encoding."""
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data: Any) -> None:
    """Write inspectable JSON output."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")


def cache_record_for(domain: str | None) -> tuple[dict[str, Any] | None, Path | None]:
    """Read cached homepage evidence only; never fetch live sources."""
    host = canonical_domain(domain)
    if not host:
        return None, None
    fallback: tuple[dict[str, Any] | None, Path | None] = (None, None)
    for directory in (HOMEPAGE_DIR, FIRECRAWL_DIR):
        path = directory / f"{slug(host)}.json"
        if path.exists():
            record = load_json(path)
            if record.get("ok") and any(record.get(key) for key in ("title", "description", "text_excerpt")):
                return record, path
            if fallback == (None, None):
                fallback = (record, path)
    return fallback


def source_domains(row: dict[str, Any]) -> tuple[str, ...]:
    """Return unique source domains from the preserved evidence rows."""
    domains: list[str] = []
    for evidence in row.get("evidence", []):
        domain = canonical_domain(evidence.get("source_domain") or evidence.get("domain"))
        if domain and domain not in domains:
            domains.append(domain)
    return tuple(domains)


def source_titles(row: dict[str, Any]) -> tuple[str, ...]:
    """Return compact source titles from the preserved evidence rows."""
    titles: list[str] = []
    for evidence in row.get("evidence", []):
        title = clean_text(str(evidence.get("title") or ""))
        if title and title not in titles:
            titles.append(title)
    return tuple(titles[:8])


def source_role(row: dict[str, Any], domain: str | None, titles: tuple[str, ...], domains: tuple[str, ...]) -> str:
    """Classify the source grain separately from the underlying company."""
    host = canonical_domain(domain)
    own_titles = [title for title, source_domain in zip(titles, domains, strict=False) if host and source_domain == host]
    title_haystack = " ".join([row.get("name") or "", *titles])
    if row["candidate_source"] == "extracted_name":
        return "third_party_named_candidate"
    if own_titles and any(LISTICLE_RE.search(title) for title in own_titles):
        return "owned_seo_or_comparison_page"
    if LISTICLE_RE.search(str(row.get("name") or "")):
        return "owned_seo_or_comparison_page"
    if SOURCE_ONLY_RE.search(title_haystack):
        return "source_or_directory_artifact"
    if row["candidate_source"] == "observed_domain":
        return "owned_homepage_or_service_page"
    return "candidate_card"


def evidence_snapshot(row: dict[str, Any]) -> EvidenceSnapshot:
    """Collect cached evidence for one row without spending."""
    resolution = row["resolution"]
    domain = resolution.get("resolved_domain") or row.get("domain")
    cache, path = cache_record_for(domain)
    titles = source_titles(row)
    domains = source_domains(row)
    role = source_role(row, domain, titles, domains)
    return EvidenceSnapshot(
        source_role=role,
        source_titles=titles,
        source_domains=domains,
        homepage_title=clean_text(str(cache.get("title") or "")) or None if cache else None,
        homepage_description=clean_text(str(cache.get("description") or "")) or None if cache else None,
        homepage_text_excerpt=clean_text(str(cache.get("text_excerpt") or ""))[:700] or None if cache else None,
        homepage_cache_path=str(path.relative_to(OUTPUT_DIR)) if path else None,
    )


def haystack(row: dict[str, Any], snapshot: EvidenceSnapshot) -> str:
    """Build qrel-free text used for usefulness classification."""
    resolution = row["resolution"]
    names = [str(resolution.get("canonical_name") or ""), str(resolution.get("resolved_domain") or "")]
    if row["candidate_source"] == "extracted_name" or snapshot.source_role != "owned_seo_or_comparison_page":
        names.append(str(row.get("name") or ""))
    parts = [
        *names,
        snapshot.homepage_title or "",
        snapshot.homepage_description or "",
        snapshot.homepage_text_excerpt or "",
    ]
    return clean_text(" ".join(parts))


def gate_existing_profile(row: dict[str, Any], snapshot: EvidenceSnapshot) -> ReadinessDecision:
    """Keep existing store profiles distinct from new capture-ready work."""
    reasons = ["already_captured_in_store", "do_not_recapture_existing_profile"]
    caveats = list(row["resolution"].get("caveats") or [])
    if snapshot.source_role == "owned_seo_or_comparison_page":
        caveats.append("owned SEO/listicle evidence is biased source evidence; keep it separate from store truth")
    return ReadinessDecision(
        route="existing_profile",
        confidence_band="high",
        actor_role="existing_store_profile",
        full_capture_better_than_card=False,
        neighborhood_context=True,
        cross_company_synthesis=True,
        reasons=reasons,
        caveats=dedupe(caveats),
    )


def telehealth_decision(row: dict[str, Any], snapshot: EvidenceSnapshot) -> ReadinessDecision:
    """Gate telehealth candidates by DTC/cohort value versus local/source noise."""
    text = haystack(row, snapshot)
    reasons: list[str] = []
    caveats: list[str] = []
    source_biased = snapshot.source_role == "owned_seo_or_comparison_page"
    if source_biased:
        caveats.append("owned SEO/listicle page is biased source evidence, not neutral market proof")

    if BROAD_HEALTH_RE.search(text):
        return ReadinessDecision(
            route="preserve_source_evidence",
            confidence_band="high",
            actor_role="broad_health_retail_or_pharmacy",
            full_capture_better_than_card=False,
            neighborhood_context=False,
            cross_company_synthesis=True,
            reasons=["broad_health_or_pharmacy_surface_not_specific_cohort_actor", "preserve_relevant_service_page_evidence"],
            caveats=dedupe(caveats + ["homepage confirms a real company surface, not capture-worthiness"]),
        )

    local = bool(LOCAL_CLINIC_RE.search(text))
    direct = bool(TELEHEALTH_DIRECT_RE.search(text))
    core = bool(TELEHEALTH_CORE_RE.search(text))
    adjacent = bool(TELEHEALTH_ADJACENT_RE.search(text))

    if local and not direct:
        return ReadinessDecision(
            route="preserve_source_evidence",
            confidence_band="medium",
            actor_role="local_or_offline_clinic",
            full_capture_better_than_card=False,
            neighborhood_context=False,
            cross_company_synthesis=True,
            reasons=["local_or_offline_clinic_scope", "lightweight_card_preserves_pattern_evidence"],
            caveats=dedupe(caveats + ["full capture would likely add store bloat before neighborhood value"]),
        )
    if adjacent and not (core and direct):
        return ReadinessDecision(
            route="cohort_fit_review",
            confidence_band="medium",
            actor_role="adjacent_tool_or_platform",
            full_capture_better_than_card=False,
            neighborhood_context=True,
            cross_company_synthesis=True,
            reasons=["adjacent_platform_may_help_healthspan_or_care_delivery_synthesis"],
            caveats=dedupe(caveats + ["needs agent judgment before full company capture"]),
        )
    if core and direct and not local:
        return ReadinessDecision(
            route="capture_ready",
            confidence_band="medium",
            actor_role="cohort_actor",
            full_capture_better_than_card=True,
            neighborhood_context=True,
            cross_company_synthesis=True,
            reasons=["direct_to_patient_or_online_care_surface", "cohort_actor_would_improve_cross_company_comparison"],
            caveats=dedupe(caveats),
        )
    if core and direct and local:
        return ReadinessDecision(
            route="cohort_fit_review",
            confidence_band="medium",
            actor_role="local_clinic_with_online_service_surface",
            full_capture_better_than_card=False,
            neighborhood_context=True,
            cross_company_synthesis=True,
            reasons=["cohort_relevant_service_but_local_clinic_scope"],
            caveats=dedupe(caveats + ["do not capture solely because homepage confirms telemedicine language"]),
        )
    if core and not local and not adjacent:
        return ReadinessDecision(
            route="capture_ready",
            confidence_band="medium",
            actor_role="cohort_actor",
            full_capture_better_than_card=True,
            neighborhood_context=True,
            cross_company_synthesis=True,
            reasons=["cohort_specific_care_surface", "full_profile_would_support_category_comparison"],
            caveats=dedupe(caveats + ["does not rely on homepage existence alone"]),
        )
    if core:
        return ReadinessDecision(
            route="cohort_fit_review",
            confidence_band="low",
            actor_role="possible_cohort_actor",
            full_capture_better_than_card=False,
            neighborhood_context=True,
            cross_company_synthesis=True,
            reasons=["cohort_language_present_but_capture_value_unclear"],
            caveats=dedupe(caveats + ["homepage confirmation alone is insufficient"]),
        )
    return ReadinessDecision(
        route="boundary_review",
        confidence_band="low",
        actor_role="uncertain_company_surface",
        full_capture_better_than_card=False,
        neighborhood_context=False,
        cross_company_synthesis=False,
        reasons=["insufficient_no_spend_evidence_for_usefulness"],
        caveats=dedupe(caveats),
    )


def conversation_decision(row: dict[str, Any], snapshot: EvidenceSnapshot) -> ReadinessDecision:
    """Gate conversation-intelligence candidates by cohort and adjacent value."""
    text = haystack(row, snapshot)
    caveats: list[str] = []
    if snapshot.source_role == "owned_seo_or_comparison_page":
        caveats.append("owned SEO/listicle page is biased source evidence, not neutral market proof")

    strong = bool(CI_STRONG_RE.search(text))
    weak = bool(CI_WEAK_RE.search(text))
    preserve_only = bool(CI_PRESERVE_RE.search(text)) and not strong

    if preserve_only:
        return ReadinessDecision(
            route="preserve_source_evidence",
            confidence_band="medium",
            actor_role="adjacent_productivity_or_research_tool",
            full_capture_better_than_card=False,
            neighborhood_context=False,
            cross_company_synthesis=True,
            reasons=["underlying_company_not_core_cohort_actor", "owned_or_source_page_still_preserves_cohort_boundary_evidence"],
            caveats=dedupe(caveats + ["homepage proves company existence only"]),
        )
    if strong:
        return ReadinessDecision(
            route="capture_ready",
            confidence_band="medium",
            actor_role="cohort_actor",
            full_capture_better_than_card=True,
            neighborhood_context=True,
            cross_company_synthesis=True,
            reasons=["conversation_or_revenue_intelligence_actor", "full_profile_would_support_comparison_across_tools"],
            caveats=dedupe(caveats),
        )
    if weak:
        return ReadinessDecision(
            route="cohort_fit_review",
            confidence_band="medium",
            actor_role="adjacent_gtm_tool_or_platform",
            full_capture_better_than_card=False,
            neighborhood_context=True,
            cross_company_synthesis=True,
            reasons=["adjacent_sales_or_revenue_platform", "needs_agent_judgment_before_full_capture"],
            caveats=dedupe(caveats + ["homepage confirmation alone is insufficient"]),
        )
    return ReadinessDecision(
        route="boundary_review",
        confidence_band="low",
        actor_role="uncertain_company_surface",
        full_capture_better_than_card=False,
        neighborhood_context=False,
        cross_company_synthesis=False,
        reasons=["insufficient_no_spend_evidence_for_usefulness"],
        caveats=dedupe(caveats),
    )


def dedupe(values: list[str]) -> list[str]:
    """Preserve order while removing duplicate strings."""
    output: list[str] = []
    for value in values:
        if value and value not in output:
            output.append(value)
    return output


def decide(row: dict[str, Any], snapshot: EvidenceSnapshot) -> ReadinessDecision:
    """Route one boundary-resolved row through the capture-readiness gate."""
    if row["resolution"]["route"] == "existing_profile":
        return gate_existing_profile(row, snapshot)
    if row["cohort"] == "telehealth":
        return telehealth_decision(row, snapshot)
    if row["cohort"] == "conversation_intelligence":
        return conversation_decision(row, snapshot)
    return ReadinessDecision(
        route="boundary_review",
        confidence_band="low",
        actor_role="unknown_cohort",
        full_capture_better_than_card=False,
        neighborhood_context=False,
        cross_company_synthesis=False,
        reasons=["unsupported_cohort_for_packet_local_gate"],
    )


def apply_capture_dedupes(rows: list[dict[str, Any]]) -> None:
    """Keep one capture-ready row per new domain and preserve duplicate evidence."""
    first_by_domain: dict[tuple[str, str], str] = {}
    for row in rows:
        readiness = row["capture_readiness"]
        if readiness["route"] != "capture_ready":
            continue
        domain = canonical_domain(row["boundary_resolution"].get("resolved_domain") or row.get("domain"))
        if not domain:
            continue
        key = (row["cohort"], domain)
        if key not in first_by_domain:
            first_by_domain[key] = row["candidate_id"]
            continue
        readiness["route"] = "preserve_source_evidence"
        readiness["full_capture_better_than_card"] = False
        readiness["duplicate_of"] = first_by_domain[key]
        readiness["reasons"] = dedupe(
            ["duplicate_capture_ready_domain", "preserve_as_supporting_source_evidence", *readiness["reasons"]]
        )
        readiness["caveats"] = dedupe(
            [*readiness["caveats"], "underlying company may still be capture-ready via the primary row"]
        )


def qrel_eval_for(row: dict[str, Any], qrels: list[Qrel]) -> dict[str, Any]:
    """Attach qrel labels only after routing has already happened."""
    match = best_qrel(row, qrels)
    return {
        "qrel_label": match.label if match else None,
        "qrel_name": match.name if match else None,
        "qrel_domain": match.domain if match else None,
        "is_known_relevant": is_relevant_eval(match),
        "is_known_bad_or_boundary": is_bad_or_boundary_eval(match),
    }


def serialize_snapshot(snapshot: EvidenceSnapshot) -> dict[str, Any]:
    """Serialize evidence details without hiding caveats."""
    return {
        "source_role": snapshot.source_role,
        "source_titles": list(snapshot.source_titles),
        "source_domains": list(snapshot.source_domains),
        "homepage": {
            "title": snapshot.homepage_title,
            "description": snapshot.homepage_description,
            "text_excerpt": snapshot.homepage_text_excerpt,
            "cache_path": snapshot.homepage_cache_path,
        },
    }


def serialize_decision(decision: ReadinessDecision) -> dict[str, Any]:
    """Serialize a readiness decision."""
    return {
        "route": decision.route,
        "confidence_band": decision.confidence_band,
        "actor_role": decision.actor_role,
        "full_capture_better_than_card": decision.full_capture_better_than_card,
        "neighborhood_context": decision.neighborhood_context,
        "cross_company_synthesis": decision.cross_company_synthesis,
        "reasons": decision.reasons,
        "caveats": decision.caveats,
        "duplicate_of": decision.duplicate_of,
    }


def output_row(row: dict[str, Any], snapshot: EvidenceSnapshot, decision: ReadinessDecision, qrels: list[Qrel]) -> dict[str, Any]:
    """Join boundary-resolution identity with capture-readiness judgement."""
    return {
        "candidate_id": row["candidate_id"],
        "cohort": row["cohort"],
        "rank": row["rank"],
        "name": row["name"],
        "domain": row.get("domain"),
        "candidate_source": row["candidate_source"],
        "ranker": row.get("ranker", {}),
        "boundary_resolution": row["resolution"],
        "evidence_snapshot": serialize_snapshot(snapshot),
        "capture_readiness": serialize_decision(decision),
        "post_route_eval": qrel_eval_for(row, qrels),
    }


def load_target_rows() -> list[dict[str, Any]]:
    """Load only rows that boundary resolution already routed to candidate/existing."""
    data = load_json(BOUNDARY_RESULTS_PATH)
    return [row for row in data["results"] if row["resolution"]["route"] in INPUT_ROUTES]


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Build route counts and acceptance checks after the readiness gate."""
    by_cohort: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_cohort[row["cohort"]].append(row)

    cohorts: dict[str, Any] = {}
    for cohort, cohort_rows in sorted(by_cohort.items()):
        route_counts = Counter(row["capture_readiness"]["route"] for row in cohort_rows)
        actor_counts = Counter(row["capture_readiness"]["actor_role"] for row in cohort_rows)
        unique_capture_domains = sorted(
            {
                canonical_domain(row["boundary_resolution"].get("resolved_domain") or row.get("domain"))
                for row in cohort_rows
                if row["capture_readiness"]["route"] == "capture_ready"
            }
            - {None}
        )
        source_like_capture = [
            row
            for row in cohort_rows
            if row["capture_readiness"]["route"] == "capture_ready"
            and row["capture_readiness"]["actor_role"]
            in {"local_or_offline_clinic", "broad_health_retail_or_pharmacy", "adjacent_productivity_or_research_tool"}
        ]
        homepage_only_capture = [
            row
            for row in cohort_rows
            if row["capture_readiness"]["route"] == "capture_ready"
            and row["boundary_resolution"].get("method") in {"homepage_direct", "homepage_firecrawl"}
            and not (
                row["capture_readiness"]["neighborhood_context"]
                and row["capture_readiness"]["cross_company_synthesis"]
                and row["capture_readiness"]["full_capture_better_than_card"]
            )
        ]
        bad_promoted = [
            row
            for row in cohort_rows
            if row["capture_readiness"]["route"] == "capture_ready"
            and row["post_route_eval"]["is_known_bad_or_boundary"]
        ]
        cohorts[cohort] = {
            "input_rows": len(cohort_rows),
            "route_counts": dict(sorted(route_counts.items())),
            "actor_role_counts": dict(sorted(actor_counts.items())),
            "unique_capture_ready_domains": unique_capture_domains,
            "unique_capture_ready_domain_count": len(unique_capture_domains),
            "source_like_capture_count": len(source_like_capture),
            "homepage_only_capture_count": len(homepage_only_capture),
            "known_bad_or_boundary_capture_ready_count": len(bad_promoted),
            "known_relevant_existing_or_capture_count": sum(
                1
                for row in cohort_rows
                if row["post_route_eval"]["is_known_relevant"]
                and row["capture_readiness"]["route"] in {"existing_profile", "capture_ready"}
            ),
        }

    route_counts = Counter(row["capture_readiness"]["route"] for row in rows)
    return {
        "schema": "codex-capture-readiness-eval-v0",
        "routing_uses_qrels": False,
        "qrels_used_for": "evaluation-only matching after capture-readiness routing",
        "live_spend_used": {
            "direct_http_homepages": 0,
            "serpapi_queries": 0,
            "firecrawl_homepage_scrapes": 0,
        },
        "input": {
            "boundary_results": str(BOUNDARY_RESULTS_PATH.relative_to(OUTPUT_DIR)),
            "input_routes": sorted(INPUT_ROUTES),
            "input_rows": len(rows),
        },
        "route_counts": dict(sorted(route_counts.items())),
        "cohorts": cohorts,
        "acceptance_checks": {
            "source_listicle_directory_capture_ready_count": sum(
                stats["source_like_capture_count"] for stats in cohorts.values()
            ),
            "homepage_only_capture_ready_count": sum(stats["homepage_only_capture_count"] for stats in cohorts.values()),
            "known_bad_or_boundary_capture_ready_count": sum(
                stats["known_bad_or_boundary_capture_ready_count"] for stats in cohorts.values()
            ),
            "existing_profiles_stayed_distinct": route_counts.get("existing_profile", 0)
            == sum(1 for row in rows if row["boundary_resolution"]["route"] == "existing_profile"),
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


def row_name(row: dict[str, Any]) -> str:
    """Display a compact candidate identity."""
    domain = row["boundary_resolution"].get("resolved_domain") or row.get("domain") or ""
    return f"{row['name']} ({domain})" if domain else str(row["name"])


def write_summary(output: dict[str, Any]) -> None:
    """Write a short human-facing readout for the readiness gate."""
    evaluation = output["evaluation"]
    lines = [
        "# Codex Capture Readiness",
        "",
        "Date: 2026-06-26",
        "Status: packet-local no-spend usefulness gate over boundary-resolution output; no engine changes",
        "",
        "## Read",
        "",
        "- Input is only boundary-resolution rows already routed as `capture_candidate` or `existing_profile`.",
        "- Existing store profiles stay separate from new capture-ready candidates.",
        "- Homepage confirmation is treated as company existence, not capture-worthiness.",
        "- Owned comparison/listicle pages are preserved as biased source evidence; they do not count as neutral third-party proof.",
        "",
        "## Spend / Evidence",
        "",
        "- Fresh live spend: 0 direct HTTP, 0 SerpAPI, 0 Firecrawl.",
        "- Evidence used: prior boundary result JSON plus packet-local homepage/store receipts already cached by boundary resolution.",
        "",
        "## Route Counts",
        "",
    ]
    rows = [["Cohort", "Input", "Existing", "Capture ready", "Fit review", "Preserve source", "Reject/defer", "Boundary", "Unique capture domains"]]
    for cohort, stats in evaluation["cohorts"].items():
        counts = stats["route_counts"]
        rows.append(
            [
                cohort,
                str(stats["input_rows"]),
                str(counts.get("existing_profile", 0)),
                str(counts.get("capture_ready", 0)),
                str(counts.get("cohort_fit_review", 0)),
                str(counts.get("preserve_source_evidence", 0)),
                str(counts.get("reject_or_defer", 0)),
                str(counts.get("boundary_review", 0)),
                str(stats["unique_capture_ready_domain_count"]),
            ]
        )
    lines.extend(markdown_table(rows))
    lines.extend(["", "## Capture Ready", ""])

    for cohort in sorted(evaluation["cohorts"]):
        capture_rows = [
            row for row in output["results"] if row["cohort"] == cohort and row["capture_readiness"]["route"] == "capture_ready"
        ]
        lines.extend([f"### {cohort}", ""])
        if not capture_rows:
            lines.extend(["_None._", ""])
            continue
        table = [["Rank", "Name", "Actor role", "Why"]]
        for row in capture_rows:
            table.append(
                [
                    str(row["rank"]),
                    row_name(row),
                    row["capture_readiness"]["actor_role"],
                    "; ".join(row["capture_readiness"]["reasons"][:2]),
                ]
            )
        lines.extend(markdown_table(table))
        lines.append("")

    lines.extend(["## Needs Review Or Preservation", ""])
    for cohort in sorted(evaluation["cohorts"]):
        review_rows = [
            row
            for row in output["results"]
            if row["cohort"] == cohort
            and row["capture_readiness"]["route"] in {"cohort_fit_review", "preserve_source_evidence", "reject_or_defer", "boundary_review"}
        ]
        lines.extend([f"### {cohort}", ""])
        table = [["Route", "Rank", "Name", "Actor role", "Caveat"]]
        for row in review_rows:
            table.append(
                [
                    row["capture_readiness"]["route"],
                    str(row["rank"]),
                    row_name(row),
                    row["capture_readiness"]["actor_role"],
                    "; ".join(row["capture_readiness"]["caveats"][:2]),
                ]
            )
        lines.extend(markdown_table(table) if len(table) > 1 else ["_None._"])
        lines.append("")

    checks = evaluation["acceptance_checks"]
    lines.extend(
        [
            "## Acceptance Checks",
            "",
            f"- Source/listicle/directory artifacts capture-ready: {checks['source_listicle_directory_capture_ready_count']}.",
            f"- Homepage-only capture-ready rows without usefulness reasons: {checks['homepage_only_capture_ready_count']}.",
            f"- Known bad/boundary eval rows capture-ready: {checks['known_bad_or_boundary_capture_ready_count']}.",
            f"- Existing profiles stayed distinct: {checks['existing_profiles_stayed_distinct']}.",
            "",
            "## Files",
            "",
            f"- Results JSON: `{RESULTS_PATH.name}`",
            f"- Summary: `{SUMMARY_PATH.name}`",
            "",
            "## Readout",
            "",
            "The gate turns the previous 42 capture candidates into a smaller capture-ready set plus explicit review/preservation buckets. The most important behavior is negative: real homepages are not enough. Rows with owned SEO/listicle evidence keep that evidence visible, but only cohort usefulness makes a new full capture worthwhile.",
            "",
        ]
    )
    with SUMMARY_PATH.open("w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def run() -> dict[str, Any]:
    """Run the no-spend capture-readiness gate."""
    qrels = list(build_qrels().values())
    rows: list[dict[str, Any]] = []
    for row in load_target_rows():
        snapshot = evidence_snapshot(row)
        decision = decide(row, snapshot)
        rows.append(output_row(row, snapshot, decision, qrels))
    apply_capture_dedupes(rows)
    evaluation = summarize(rows)
    output = {
        "schema": "codex-capture-readiness-results-v0",
        "generated_at": utc_now(),
        "results": rows,
        "evaluation": evaluation,
    }
    write_json(RESULTS_PATH, output)
    write_summary(output)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate boundary-resolved rows by capture readiness/usefulness.")
    parser.parse_args()
    output = run()
    print(
        json.dumps(
            {
                "results": len(output["results"]),
                "route_counts": output["evaluation"]["route_counts"],
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
