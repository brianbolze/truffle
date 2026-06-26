#!/usr/bin/env python3
"""Prototype candidate qualification over cached cohort-discovery evidence.

This packet-local probe tests the candidate-qualification split without live
source spend: preserve useful source evidence, then route only likely
company/brand targets toward capture. Routing uses observed source/search/link
evidence only; qrels are loaded afterward for evaluation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

CANDIDATE_FILTERING = Path(__file__).resolve().parents[1]
PACKET = CANDIDATE_FILTERING.parent
if str(PACKET) not in sys.path:
    sys.path.insert(0, str(PACKET))

from page_extraction_probe import page_units  # noqa: E402
from search_harness import RAW_DIR, Qrel, Unit, all_units, build_qrels, load_json  # noqa: E402

OUTPUT_DIR = Path(__file__).resolve().parent
CARD_PATH = OUTPUT_DIR / "codex_candidate_cards.json"
EVAL_PATH = OUTPUT_DIR / "codex_qualification_eval.json"
SUMMARY_PATH = OUTPUT_DIR / "codex_qualification_summary.md"

COHORTS = ("telehealth", "conversation_intelligence")
RRF_K = 60

SOCIAL_OR_FORUM_DOMAINS = {
    "facebook.com",
    "instagram.com",
    "linkedin.com",
    "reddit.com",
    "tiktok.com",
    "twitter.com",
    "x.com",
    "youtube.com",
}

LOW_TRUST_ARTIFACT_DOMAINS = {
    "mattioli1885journals.com",
}

INFRA_OR_UTILITY_DOMAINS = {
    "google.com",
    "ncbi.nlm.nih.gov",
}

SOURCE_HINT_DOMAINS = {
    "askelephant.ai",
    "centaur.reading.ac.uk",
    "cirrusinsight.com",
    "empirical.health",
    "finance.yahoo.com",
    "forbes.com",
    "g2.com",
    "getsalesman.ai",
    "github.com",
    "goodrx.com",
    "health.yahoo.com",
    "innerbody.com",
    "itsconvo.com",
    "meetingnotes.com",
    "pmc.ncbi.nlm.nih.gov",
    "policylab.us",
    "read.ai",
    "salesforce.com",
    "selectsoftwarereviews.com",
    "simular.ai",
    "tana.inc",
    "theflowspace.com",
    "trtnation.com",
    "usnews.com",
    "years.co",
    "zapier.com",
    "zackproser.com",
}

SOURCE_TITLE_RE = re.compile(
    r"\b("
    r"affordable|alternative|alternatives|best|buyers?'? guide|characteristics|"
    r"compared|comparison|competitors|complete guide|guide|hands-on|how to|"
    r"list|pricing|review|study|tool pricing|tools compared|top|transcription|"
    r"vs|what it actually buys|which"
    r")\b",
    re.IGNORECASE,
)

PRODUCT_OR_WORKFLOW_RE = re.compile(
    r"\b(ai companion|ai features|chatgpt|copilot|notion ai|openai whisper|transcript workflow)\b",
    re.IGNORECASE,
)

GENERIC_NAV_NAMES = {
    "71%",
    "ai features",
    "home",
    "log in",
    "login",
    "mcp",
    "offer",
    "status page",
    "try now",
    "view offer",
}

RELEVANT_TELEHEALTH_LABELS = {"must_hit", "should_hit", "worth_capture"}
BOUNDARY_OR_BAD_TELEHEALTH_LABELS = {"tier_c_only", "exclude", "unsure"}
RELEVANT_CI_LABELS = {"top_10_core"}
BOUNDARY_CI_LABELS = {"core_boundary_product_workflow"}


@dataclass
class ObservedCandidate:
    """A qrel-free candidate grouped by observed cohort/domain evidence."""

    key: str
    cohort: str
    name: str
    domain: str
    rrf: float = 0.0
    search_score: float = 0.0
    evidence: list[dict[str, Any]] = field(default_factory=list)
    source_rows: set[str] = field(default_factory=set)
    feeders: set[str] = field(default_factory=set)
    tools: set[str] = field(default_factory=set)
    facets: set[str] = field(default_factory=set)


@dataclass(frozen=True)
class Qualification:
    """A packet-local route and its audit trail."""

    route: str
    confidence: str
    route_score: int
    reasons: list[str]
    blockers: list[str]
    caveats: list[str]


def write_json(path: Path, data: Any) -> None:
    """Write generated JSON with stable indentation for review."""
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def slug(value: str) -> str:
    """Create a stable key fragment."""
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def normalized(value: str) -> str:
    """Normalize text for conservative eval-time matching."""
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9&.+ ]+", " ", value.lower())).strip()


def domain_matches(domain: str | None, base_domain: str) -> bool:
    """Return whether a domain is the base domain or a subdomain of it."""
    if not domain:
        return False
    return domain == base_domain or domain.endswith(f".{base_domain}")


def has_source_hint_domain(domain: str | None) -> bool:
    """Return whether a domain is known here only as a source surface."""
    return any(domain_matches(domain, source_domain) for source_domain in SOURCE_HINT_DOMAINS)


def has_social_domain(domain: str | None) -> bool:
    """Return whether a domain is a social/forum surface."""
    return any(domain_matches(domain, social_domain) for social_domain in SOCIAL_OR_FORUM_DOMAINS)


def has_non_profile_domain_shape(domain: str | None) -> bool:
    """Catch subdomains and pseudo-domains that are not profile-worthy targets."""
    if not domain:
        return False
    if ":" in domain:
        return True
    first_label = domain.split(".", maxsplit=1)[0]
    return first_label in {
        "account",
        "app",
        "docs",
        "help",
        "home",
        "login",
        "marketing",
        "outliner",
        "support",
        "vendors",
    }


def is_source_like_name(name: str) -> bool:
    """Return whether the name reads like a page title, not an entity."""
    return bool(SOURCE_TITLE_RE.search(name))


def is_generic_nav_name(name: str) -> bool:
    """Return whether anchor/nav text is masquerading as a candidate name."""
    value = normalized(name)
    if len(re.sub(r"[^a-z0-9]+", "", value)) < 2:
        return True
    return value in GENERIC_NAV_NAMES or "@" in value


def is_low_trust_artifact(candidate: ObservedCandidate) -> bool:
    """Catch source artifacts that should not be preserved as strong evidence."""
    if candidate.domain in LOW_TRUST_ARTIFACT_DOMAINS:
        return True
    for evidence in candidate.evidence:
        url = str(evidence.get("url") or "").lower()
        if "pdfjsviewer" in url or "login/signout" in url:
            return True
    return False


def domain_to_name(domain: str) -> str:
    """Create a rough display name from a domain when anchor text is generic."""
    host = domain.split(":")[-1]
    parts = host.split(".")
    if len(parts) > 2 and parts[0] in {"www", "app", "home", "login", "marketing", "support", "vendors"}:
        parts = parts[1:]
    return parts[0].replace("-", " ").title()


def clean_unit_name(unit: Unit) -> str:
    """Select the least-bad observed name for a domain candidate."""
    title = (unit.title or "").strip()
    if title:
        title = re.sub(r"\s+", " ", title)
        title = re.sub(r"^(visit|view)\s+", "", title, flags=re.IGNORECASE)
        title = title.replace("↗", "").strip()
    if title and not is_generic_nav_name(title):
        return title[:140]
    return domain_to_name(unit.domain or "")


def should_replace_name(current: str, candidate: str) -> bool:
    """Prefer entity-ish names over generic anchors, but keep source titles."""
    if is_generic_nav_name(current):
        return True
    if is_source_like_name(current):
        return False
    if is_source_like_name(candidate):
        return False
    return len(candidate) < len(current) and not is_generic_nav_name(candidate)


def source_role(candidate: ObservedCandidate) -> str:
    """Classify the candidate's observed role in retrieved evidence."""
    if has_social_domain(candidate.domain):
        return "social_or_forum"
    if any(domain_matches(candidate.domain, domain) for domain in INFRA_OR_UTILITY_DOMAINS):
        return "non_profile_navigation_or_app_surface"
    if is_low_trust_artifact(candidate):
        return "low_trust_source_artifact"
    if has_non_profile_domain_shape(candidate.domain) or is_generic_nav_name(candidate.name):
        return "non_profile_navigation_or_app_surface"
    if is_source_like_name(candidate.name):
        return "source_page_title"
    if has_source_hint_domain(candidate.domain):
        return "source_domain_without_target_attestation"
    if PRODUCT_OR_WORKFLOW_RE.search(candidate.name):
        return "product_or_workflow"
    return "candidate_entity"


def evidence_types(candidate: ObservedCandidate) -> list[str]:
    """Summarize evidence unit types."""
    return sorted(
        {
            str(evidence.get("unit_type"))
            for evidence in candidate.evidence
            if evidence.get("unit_type")
        }
    )


def build_observed_candidates() -> list[ObservedCandidate]:
    """Build candidates from observed domains only, with no qrel inputs."""
    rows = load_json(RAW_DIR / "query-panel.json")
    units = all_units(rows) + page_units()
    candidates: dict[str, ObservedCandidate] = {}
    for unit in units:
        if not unit.domain:
            continue
        key = f"domain:{unit.cohort}:{unit.domain}"
        name = clean_unit_name(unit)
        candidate = candidates.get(key)
        if candidate is None:
            candidate = ObservedCandidate(
                key=key,
                cohort=unit.cohort,
                name=name,
                domain=unit.domain,
            )
            candidates[key] = candidate
        elif should_replace_name(candidate.name, name):
            candidate.name = name

        rrf_add = 1 / (RRF_K + max(unit.rank, 1))
        candidate.rrf += rrf_add
        candidate.source_rows.add(unit.row_id)
        candidate.feeders.add(unit.feeder)
        candidate.tools.add(unit.tool)
        if unit.facet:
            candidate.facets.add(unit.facet)
        candidate.evidence.append(
            {
                "row_id": unit.row_id,
                "feeder": unit.feeder,
                "tool": unit.tool,
                "unit_type": unit.unit_type,
                "rank": unit.rank,
                "domain": unit.domain,
                "url": unit.url,
                "title": unit.title,
                "facet": unit.facet,
                "rrf_add": round(rrf_add, 6),
            }
        )

    for candidate in candidates.values():
        repeated_bonus = min(len(candidate.evidence), 6) * 0.002
        feeder_bonus = max(len(candidate.feeders) - 1, 0) * 0.006
        candidate.search_score = candidate.rrf + repeated_bonus + feeder_bonus
        candidate.evidence.sort(key=lambda row: (row.get("rank") or 999, row.get("row_id") or ""))
    return sorted(
        candidates.values(),
        key=lambda candidate: (-candidate.search_score, candidate.name.lower(), candidate.domain),
    )


def route_candidate(candidate: ObservedCandidate) -> Qualification:
    """Route a candidate using only observed retrieval evidence."""
    reasons: list[str] = ["has_domain_key"]
    blockers: list[str] = []
    caveats: list[str] = []
    role = source_role(candidate)
    score = 2

    if len(candidate.evidence) >= 3:
        score += 1
        reasons.append("repeated_evidence")
    if len(candidate.feeders) >= 2:
        score += 1
        reasons.append("multi_surface_evidence")
    if {"page_extraction", "page_outbound_links"} & candidate.feeders:
        score += 1
        reasons.append("source_page_attestation")

    if role == "social_or_forum":
        blockers.append("social_or_forum_surface")
        return Qualification(
            route="reject_or_defer",
            confidence="high",
            route_score=score - 4,
            reasons=reasons,
            blockers=blockers,
            caveats=["may be weak visibility evidence, but not a company-profile target"],
        )

    if role in {"low_trust_source_artifact", "non_profile_navigation_or_app_surface"}:
        blockers.append(role)
        return Qualification(
            route="reject_or_defer",
            confidence="medium",
            route_score=score - 4,
            reasons=reasons,
            blockers=blockers,
            caveats=["artifact should not feed capture queue without separate verification"],
        )

    if role in {"source_page_title", "source_domain_without_target_attestation"}:
        blockers.append(role)
        confidence = "high" if role == "source_page_title" else "medium"
        return Qualification(
            route="preserve_source_evidence",
            confidence=confidence,
            route_score=score - 3,
            reasons=reasons,
            blockers=blockers,
            caveats=["preserve market evidence; do not promote page publisher as the target"],
        )

    if role == "product_or_workflow":
        blockers.append("product_or_workflow_surface")
        return Qualification(
            route="product_or_workflow_target",
            confidence="medium",
            route_score=score,
            reasons=reasons,
            blockers=blockers,
            caveats=["route separately from company-profile capture"],
        )

    if score >= 4:
        return Qualification(
            route="capture_candidate",
            confidence="high" if score >= 6 else "medium",
            route_score=score,
            reasons=reasons,
            blockers=blockers,
            caveats=caveats,
        )

    caveats.append("insufficient repeated or cross-surface evidence for capture")
    return Qualification(
        route="reject_or_defer",
        confidence="low",
        route_score=score,
        reasons=reasons,
        blockers=blockers,
        caveats=caveats,
    )


def compact_evidence(candidate: ObservedCandidate, limit: int) -> list[dict[str, Any]]:
    """Keep enough evidence for a reviewer/model to audit the route."""
    compact: list[dict[str, Any]] = []
    for evidence in candidate.evidence[:limit]:
        compact.append(
            {
                "row_id": evidence.get("row_id"),
                "feeder": evidence.get("feeder"),
                "unit_type": evidence.get("unit_type"),
                "rank": evidence.get("rank"),
                "domain": evidence.get("domain"),
                "title": evidence.get("title"),
                "url": evidence.get("url"),
                "facet": evidence.get("facet"),
            }
        )
    return compact


def candidate_card(candidate: ObservedCandidate, rank: int, evidence_limit: int) -> dict[str, Any]:
    """Create the qrel-free evidence card seen by the qualifier."""
    qualification = route_candidate(candidate)
    return {
        "candidate_id": candidate.key,
        "cohort": candidate.cohort,
        "rank": rank,
        "name": candidate.name,
        "domain": candidate.domain,
        "ranker": {
            "search_score": round(candidate.search_score, 6),
            "rrf": round(candidate.rrf, 6),
            "evidence_count": len(candidate.evidence),
        },
        "routing_inputs": {
            "feeders": sorted(candidate.feeders),
            "source_rows": sorted(candidate.source_rows),
            "facets": sorted(candidate.facets),
            "evidence_types": evidence_types(candidate),
            "observed_source_role": source_role(candidate),
        },
        "qualification": {
            "route": qualification.route,
            "confidence": qualification.confidence,
            "route_score": qualification.route_score,
            "reasons": qualification.reasons,
            "blockers": qualification.blockers,
            "caveats": qualification.caveats,
        },
        "evidence": compact_evidence(candidate, evidence_limit),
    }


def qrel_aliases(qrel: Qrel) -> list[str]:
    """Return eval-only aliases for a qrel."""
    aliases = [qrel.name, *qrel.aliases]
    if qrel.domain:
        aliases.append(qrel.domain.split(".")[0])
    return [alias for alias in aliases if alias]


def eval_match(candidate: ObservedCandidate, qrel: Qrel) -> bool:
    """Match observed candidates to qrels only after routing."""
    if qrel.domain and candidate.domain == qrel.domain:
        return True
    name = normalized(candidate.name)
    domain = normalized(candidate.domain.replace(".", " "))
    for alias in qrel_aliases(qrel):
        alias_norm = normalized(alias)
        if not alias_norm or len(alias_norm) < 3:
            continue
        if alias_norm == name or alias_norm in name or alias_norm in domain:
            return True
    return False


def best_qrel(candidate: ObservedCandidate, qrels: list[Qrel]) -> Qrel | None:
    """Find the strongest eval-only qrel match for a candidate."""
    matches = [qrel for qrel in qrels if qrel.cohort == candidate.cohort and eval_match(candidate, qrel)]
    if not matches:
        return None
    return sorted(matches, key=lambda qrel: qrel.grade, reverse=True)[0]


def is_relevant_eval(qrel: Qrel | None) -> bool:
    """Use qrels only after routing to evaluate preservation and queue quality."""
    if qrel is None:
        return False
    if qrel.cohort == "telehealth":
        return qrel.label in RELEVANT_TELEHEALTH_LABELS
    if qrel.cohort == "conversation_intelligence":
        return qrel.label in RELEVANT_CI_LABELS
    return False


def is_boundary_or_bad_eval(qrel: Qrel | None) -> bool:
    """Use qrels only after routing to detect known bad/boundary promotions."""
    if qrel is None:
        return False
    if qrel.cohort == "telehealth":
        return qrel.label in BOUNDARY_OR_BAD_TELEHEALTH_LABELS
    if qrel.cohort == "conversation_intelligence":
        return qrel.label in BOUNDARY_CI_LABELS
    return False


def eval_row(card: dict[str, Any], qrel: Qrel | None) -> dict[str, Any]:
    """Attach qrel fields only in evaluation outputs."""
    return {
        "rank": card["rank"],
        "name": card["name"],
        "domain": card["domain"],
        "route": card["qualification"]["route"],
        "confidence": card["qualification"]["confidence"],
        "observed_source_role": card["routing_inputs"]["observed_source_role"],
        "qrel_grade": qrel.grade if qrel else None,
        "qrel_label": qrel.label if qrel else None,
        "qrel_name": qrel.name if qrel else None,
        "reason_sample": card["qualification"]["reasons"][:4],
        "blockers": card["qualification"]["blockers"],
        "caveats": card["qualification"]["caveats"],
    }


def summarize_cohort(cards: list[dict[str, Any]], qrel_by_card: dict[str, Qrel | None]) -> dict[str, Any]:
    """Evaluate one cohort's routed candidates."""
    route_counts = Counter(card["qualification"]["route"] for card in cards)
    top_15 = cards[:15]
    top_15_routes = Counter(card["qualification"]["route"] for card in top_15)
    capture_cards = [card for card in cards if card["qualification"]["route"] == "capture_candidate"]
    source_like_capture = [
        card
        for card in capture_cards
        if card["routing_inputs"]["observed_source_role"] != "candidate_entity"
    ]
    relevant_seen = [card for card in cards if is_relevant_eval(qrel_by_card[card["candidate_id"]])]
    relevant_preserved = [card for card in relevant_seen if card["qualification"]["route"] != "reject_or_defer"]
    relevant_capture = [card for card in relevant_seen if card["qualification"]["route"] == "capture_candidate"]
    boundary_promoted = [card for card in capture_cards if is_boundary_or_bad_eval(qrel_by_card[card["candidate_id"]])]

    return {
        "candidate_count": len(cards),
        "route_counts": dict(sorted(route_counts.items())),
        "top_15_route_counts": dict(sorted(top_15_routes.items())),
        "source_like_capture_count": len(source_like_capture),
        "known_relevant_seen": len(relevant_seen),
        "known_relevant_preserved": len(relevant_preserved),
        "known_relevant_capture": len(relevant_capture),
        "known_boundary_or_bad_promoted": len(boundary_promoted),
        "top_capture_candidates": [eval_row(card, qrel_by_card[card["candidate_id"]]) for card in capture_cards[:12]],
        "source_like_capture_candidates": [
            eval_row(card, qrel_by_card[card["candidate_id"]])
            for card in source_like_capture[:12]
        ],
        "known_boundary_or_bad_promoted_candidates": [
            eval_row(card, qrel_by_card[card["candidate_id"]])
            for card in boundary_promoted[:12]
        ],
        "known_relevant_not_capture": [
            eval_row(card, qrel_by_card[card["candidate_id"]])
            for card in relevant_seen
            if card["qualification"]["route"] != "capture_candidate"
        ][:15],
    }


def evaluate(cards: list[dict[str, Any]], candidates_by_id: dict[str, ObservedCandidate]) -> dict[str, Any]:
    """Evaluate routed cards against qrels after qualification."""
    qrels = list(build_qrels().values())
    qrel_by_card = {
        card["candidate_id"]: best_qrel(candidates_by_id[card["candidate_id"]], qrels)
        for card in cards
    }
    by_cohort: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for card in cards:
        by_cohort[card["cohort"]].append(card)

    return {
        "schema": "codex-candidate-qualification-eval-v1",
        "boundary": {
            "inputs": [
                "receipts/raw/iteration-2/query-panel.json",
                "receipts/raw/page-extraction/pages/*.json",
            ],
            "live_spend": "none; cached page-extraction outputs only",
            "routing_uses_qrels": False,
            "qrels_used_for": "evaluation-only matching after routing",
            "candidate_generation": "observed domain evidence only; no qrel-seeded alias candidates",
        },
        "cohorts": {
            cohort: summarize_cohort(cohort_cards, qrel_by_card)
            for cohort, cohort_cards in by_cohort.items()
        },
    }


def markdown_table(rows: list[list[str]]) -> list[str]:
    """Format a small Markdown table."""
    if not rows:
        return []
    header = rows[0]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def write_summary(evaluation: dict[str, Any]) -> None:
    """Write the human-facing prototype readout."""
    lines = [
        "# Codex Candidate Qualification Prototype",
        "",
        "Date: 2026-06-26",
        "Status: packet-local prototype; no implementation proposal or engine changes",
        "",
        "## Read",
        "",
        "- Prototype shape: build qrel-free observed-domain evidence cards, preserve source evidence separately, and route only likely company/brand targets toward capture.",
        "- Routing input excludes qrels, aliases, and Brian-reviewed labels; qrels are added back only for evaluation matching.",
        "- The visible disconfirming check passes if no source-like candidates are routed to `capture_candidate`.",
        "",
        "## Outputs",
        "",
        f"- Candidate cards: `{CARD_PATH.name}`",
        f"- Evaluation JSON: `{EVAL_PATH.name}`",
        f"- Summary: `{SUMMARY_PATH.name}`",
        "",
        "## Cohort Summary",
        "",
    ]
    summary_rows = [["Cohort", "Candidates", "Capture", "Preserve source", "Product/workflow", "Reject/defer", "Source-like capture"]]
    for cohort, cohort_eval in evaluation["cohorts"].items():
        counts = cohort_eval["route_counts"]
        summary_rows.append(
            [
                cohort,
                str(cohort_eval["candidate_count"]),
                str(counts.get("capture_candidate", 0)),
                str(counts.get("preserve_source_evidence", 0)),
                str(counts.get("product_or_workflow_target", 0)),
                str(counts.get("reject_or_defer", 0)),
                str(cohort_eval["source_like_capture_count"]),
            ]
        )
    lines.extend(markdown_table(summary_rows))
    lines.extend(["", "## Evaluation Notes", ""])
    for cohort, cohort_eval in evaluation["cohorts"].items():
        lines.extend(
            [
                f"### {cohort}",
                "",
                f"- Known relevant seen: {cohort_eval['known_relevant_seen']}.",
                f"- Known relevant preserved outside reject/defer: {cohort_eval['known_relevant_preserved']}.",
                f"- Known relevant routed directly to capture: {cohort_eval['known_relevant_capture']}.",
                f"- Known bad/boundary rows promoted to capture: {cohort_eval['known_boundary_or_bad_promoted']}.",
                "",
                "Top capture candidates:",
                "",
            ]
        )
        top_rows = [["Rank", "Name", "Domain", "Confidence", "Eval label"]]
        for row in cohort_eval["top_capture_candidates"][:10]:
            top_rows.append(
                [
                    str(row["rank"]),
                    str(row["name"]),
                    str(row["domain"] or ""),
                    str(row["confidence"]),
                    str(row["qrel_label"] or "unjudged"),
                ]
            )
        lines.extend(markdown_table(top_rows) or ["_None._"])
        if cohort_eval["known_boundary_or_bad_promoted_candidates"]:
            lines.extend(["", "Known bad/boundary promoted:", ""])
            bad_rows = [["Rank", "Name", "Domain", "Eval label"]]
            for row in cohort_eval["known_boundary_or_bad_promoted_candidates"]:
                bad_rows.append(
                    [
                        str(row["rank"]),
                        str(row["name"]),
                        str(row["domain"] or ""),
                        str(row["qrel_label"] or ""),
                    ]
                )
            lines.extend(markdown_table(bad_rows))
        if cohort_eval["known_relevant_not_capture"]:
            lines.extend(["", "Known relevant not routed to capture:", ""])
            miss_rows = [["Rank", "Name", "Route", "Eval label", "Why"]]
            for row in cohort_eval["known_relevant_not_capture"][:10]:
                why = "; ".join(row["blockers"] + row["caveats"])
                miss_rows.append(
                    [
                        str(row["rank"]),
                        str(row["name"]),
                        str(row["route"]),
                        str(row["qrel_label"] or ""),
                        why,
                    ]
                )
            lines.extend(markdown_table(miss_rows))
        lines.append("")

    lines.extend(
        [
            "## What This Would Replace",
            "",
            "- Replaces raw rank-to-capture behavior with an auditable route.",
            "- Replaces human-only candidate review with a reusable evidence-card contract.",
            "- Does not replace page/entity extraction, qrels, or full `/research-company` capture.",
            "",
            "## Cheapest Disconfirming Check",
            "",
            "Inspect `source_like_capture_count` and the top capture candidates. If listicles, publishers, social pages, or low-trust artifacts still enter capture, this layer fails its first job.",
            "",
        ]
    )
    SUMMARY_PATH.write_text("\n".join(lines), encoding="utf-8")


def build_cards(evidence_limit: int) -> tuple[list[dict[str, Any]], dict[str, ObservedCandidate]]:
    """Build routed cards and the observed candidate index."""
    candidates = build_observed_candidates()
    cards: list[dict[str, Any]] = []
    candidates_by_id: dict[str, ObservedCandidate] = {}
    ranks_by_cohort: Counter[str] = Counter()
    for candidate in candidates:
        if candidate.cohort not in COHORTS:
            continue
        ranks_by_cohort[candidate.cohort] += 1
        card = candidate_card(candidate, ranks_by_cohort[candidate.cohort], evidence_limit)
        cards.append(card)
        candidates_by_id[candidate.key] = candidate
    return cards, candidates_by_id


def main() -> None:
    parser = argparse.ArgumentParser(description="Prototype cached candidate qualification.")
    parser.add_argument("--evidence-limit", type=int, default=8)
    args = parser.parse_args()

    cards, candidates_by_id = build_cards(evidence_limit=args.evidence_limit)
    evaluation = evaluate(cards, candidates_by_id)
    write_json(CARD_PATH, {"schema": "codex-candidate-cards-v1", "cards": cards})
    write_json(EVAL_PATH, evaluation)
    write_summary(evaluation)
    print(
        json.dumps(
            {
                "cards": len(cards),
                "outputs": {
                    "cards": str(CARD_PATH),
                    "eval": str(EVAL_PATH),
                    "summary": str(SUMMARY_PATH),
                },
                "source_like_capture_counts": {
                    cohort: cohort_eval["source_like_capture_count"]
                    for cohort, cohort_eval in evaluation["cohorts"].items()
                },
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
