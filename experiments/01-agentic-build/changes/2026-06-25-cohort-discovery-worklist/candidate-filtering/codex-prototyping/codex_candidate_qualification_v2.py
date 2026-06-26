#!/usr/bin/env python3
"""Doro-shaped candidate qualification prototype over cached evidence.

V1 proved that evidence cards plus a routing gate can keep source pages out of
capture, but deterministic domain-only routing was too conservative. This v2
keeps candidate generation qrel-free, adds a small classify-by-example layer,
and introduces `boundary_review` for ambiguous company/product/source grain.
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

OUTPUT_DIR = Path(__file__).resolve().parent
CANDIDATE_FILTERING = OUTPUT_DIR.parents[0]
PACKET = CANDIDATE_FILTERING.parent
if str(OUTPUT_DIR) not in sys.path:
    sys.path.insert(0, str(OUTPUT_DIR))
if str(PACKET) not in sys.path:
    sys.path.insert(0, str(PACKET))

from codex_candidate_qualification_prototype import (  # noqa: E402
    INFRA_OR_UTILITY_DOMAINS,
    SOCIAL_OR_FORUM_DOMAINS,
    SOURCE_HINT_DOMAINS,
    ObservedCandidate,
    build_observed_candidates,
    domain_matches,
    has_non_profile_domain_shape,
    is_generic_nav_name,
    is_low_trust_artifact,
    is_source_like_name,
    normalized,
    write_json,
)
from search_harness import Qrel, build_qrels  # noqa: E402

EXAMPLES_PATH = OUTPUT_DIR / "codex_v2_kind_examples.json"
CARD_PATH = OUTPUT_DIR / "codex_v2_candidate_cards.json"
EVAL_PATH = OUTPUT_DIR / "codex_v2_qualification_eval.json"
SUMMARY_PATH = OUTPUT_DIR / "codex_v2_qualification_summary.md"

COHORTS = ("telehealth", "conversation_intelligence")

RELEVANT_TELEHEALTH_LABELS = {"must_hit", "should_hit", "worth_capture"}
BOUNDARY_OR_BAD_TELEHEALTH_LABELS = {"tier_c_only", "exclude", "unsure"}
RELEVANT_CI_LABELS = {"top_10_core"}
BOUNDARY_CI_LABELS = {"core_boundary_product_workflow"}

PRODUCT_OR_WORKFLOW_RE = re.compile(
    r"\b(ai companion|ai features|chatgpt|claude|copilot|notion ai|openai whisper|transcript workflow)\b",
    re.IGNORECASE,
)

NAME_SPLIT_RE = re.compile(r"\s+(?:vs\.?|versus)\s+|,|/|\+", re.IGNORECASE)
ALTERNATIVE_RE = re.compile(
    r"\b([A-Z][A-Za-z0-9&.+]*(?:\s+[A-Z][A-Za-z0-9&.+]*){0,3})\s+"
    r"(?:alternative|alternatives|competitor|competitors|vs\.?|versus)\b"
)
SUFFIX_RE = re.compile(r"[-|]\s*([A-Z][A-Za-z0-9&.+]*(?:\s+[A-Z][A-Za-z0-9&.+]*){0,3})\s*$")

ENTITY_STOPWORDS = {
    "AI",
    "AI Meeting Assistant",
    "AI Meeting Note",
    "AI Meeting Notes",
    "AI Note Taker",
    "AI Tools",
    "Affordable Online HRT",
    "Apps",
    "Best",
    "Best AI Note",
    "Best Online TRT",
    "Boost Sexual Vitality",
    "Choose",
    "Clinics",
    "Complete Buyer",
    "Complete Buyer's Guide",
    "Conversation Intelligence",
    "Conversation Intelligence Software",
    "Don",
    "Don't Choose",
    "ED",
    "FDA Approved Meds",
    "GLP",
    "Guide",
    "Hands On Review",
    "Health",
    "HRT",
    "Home Use",
    "Know Before",
    "Meeting Assistant",
    "Meeting Assistant in 2026?",
    "Meeting Notes Tools",
    "Meeting Transcription",
    "Meetings",
    "Online",
    "Online TRT Clinic",
    "Online TRT Clinics",
    "PMC",
    "Policy Lab",
    "Providers",
    "Revenue Teams",
    "Sales Calls",
    "TRT",
    "Taker",
    "Takers",
    "Telehealth Platforms",
    "Tested",
    "The",
    "Tools",
    "Top",
    "What",
    "What to Know Before",
    "Why I Switched",
    "Work",
}


@dataclass
class CandidateV2:
    """A qrel-free candidate for kind-first qualification."""

    candidate_id: str
    cohort: str
    name: str
    domain: str | None
    candidate_source: str
    search_score: float
    evidence: list[dict[str, Any]] = field(default_factory=list)
    source_rows: set[str] = field(default_factory=set)
    feeders: set[str] = field(default_factory=set)
    facets: set[str] = field(default_factory=set)
    alternatives: list[dict[str, Any]] = field(default_factory=list)


@dataclass(frozen=True)
class ExampleMatch:
    """Nearest classify-by-example result."""

    example_id: str
    kind: str
    route: str
    confidence_band: str
    overlap: int
    gap: int
    tags: list[str]


@dataclass(frozen=True)
class QualificationV2:
    """Doro-shaped inspectable qualification result."""

    kind: str
    route: str
    confidence_band: str
    method: str
    reasons: list[str]
    blockers: list[str]
    alternatives: list[dict[str, Any]]
    caveats: list[str]
    nearest_examples: list[dict[str, Any]]


def load_examples() -> list[dict[str, Any]]:
    """Load the packet-local kind examples."""
    with EXAMPLES_PATH.open(encoding="utf-8") as handle:
        data = json.load(handle)
    return list(data["examples"])


def has_domain_in(domain: str | None, domains: set[str]) -> bool:
    """Return whether a domain matches any domain in a set."""
    return any(domain_matches(domain, item) for item in domains)


def base_domain(domain: str | None) -> str | None:
    """Return a simple base domain for display and rough matching."""
    if not domain:
        return None
    parts = domain.split(".")
    if len(parts) <= 2:
        return domain
    return ".".join(parts[-2:])


def domain_stem(domain: str | None) -> str:
    """Return a rough brand stem from a domain."""
    if not domain:
        return ""
    host = base_domain(domain) or domain
    return host.split(".")[0].replace("-", " ").title()


def title_values(candidate: ObservedCandidate) -> list[str]:
    """Return compact title strings from candidate evidence."""
    titles: list[str] = []
    for evidence in candidate.evidence:
        title = str(evidence.get("title") or "").strip()
        if title and title not in titles:
            titles.append(title)
    return titles


def clean_extracted_name(value: str) -> str | None:
    """Normalize a title fragment into a plausible name-only candidate."""
    cleaned = re.sub(r"\s+", " ", value.strip(" -:|()[]{}'\"“”‘’.,"))
    cleaned = re.sub(r"^(best|top|the)\s+", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+(alternatives?|competitors?|compared|pricing|review)$", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+(or|and)$", "", cleaned, flags=re.IGNORECASE)
    if not cleaned or len(cleaned) < 3:
        return None
    if cleaned in ENTITY_STOPWORDS:
        return None
    if cleaned.title() in ENTITY_STOPWORDS:
        return None
    if cleaned.lower() in {"health", "online", "tools", "meeting", "telehealth"}:
        return None
    if len(cleaned.split()) > 4:
        return None
    if not re.search(r"[A-Z]", cleaned):
        return None
    return cleaned[:80]


def extract_names_from_title(title: str) -> list[str]:
    """Extract qrel-free name-only candidates from comparison/listicle titles."""
    found: list[str] = []
    for match in ALTERNATIVE_RE.finditer(title):
        name = clean_extracted_name(match.group(1))
        if name:
            found.append(name)
    chunks = re.split(r"[:|-]", title)
    for chunk in chunks:
        if re.search(r"\b(vs\.?|versus)\b", chunk, flags=re.IGNORECASE):
            for piece in NAME_SPLIT_RE.split(chunk):
                name = clean_extracted_name(piece)
                if name:
                    found.append(name)
    suffix_match = SUFFIX_RE.search(title)
    if suffix_match:
        suffix_name = clean_extracted_name(suffix_match.group(1))
        if suffix_name and re.search(r"\b[A-Z]{2,}\b|[A-Z][a-z]+[A-Z]|&|\+", suffix_name):
            found.append(suffix_name)
    deduped: list[str] = []
    for name in found:
        if name not in deduped:
            deduped.append(name)
    return deduped[:8]


def alternative_from_name(name: str, source_id: str, source_title: str, source_domain: str | None) -> dict[str, Any]:
    """Create an alternative target record from an extracted name."""
    return {
        "name": name,
        "domain": None,
        "source": source_id,
        "source_title": source_title,
        "source_domain": source_domain,
        "reason": "extracted_from_source_title",
    }


def candidate_tags(candidate: CandidateV2) -> set[str]:
    """Build classify-by-example tags from qrel-free evidence."""
    tags: set[str] = set()
    if candidate.domain:
        tags.add("domain_key")
    else:
        tags.add("name_only")
    if candidate.candidate_source == "extracted_name":
        tags.update({"name_only", "mentioned_in_source", "entity_name"})
    if len(candidate.evidence) >= 3:
        tags.add("repeated_evidence")
    if len(candidate.feeders) >= 2:
        tags.add("multi_surface")
    if {"page_extraction", "page_outbound_links"} & candidate.feeders:
        tags.add("mentioned_in_source")
    if has_domain_in(candidate.domain, SOURCE_HINT_DOMAINS):
        tags.add("source_domain")
    if has_domain_in(candidate.domain, SOCIAL_OR_FORUM_DOMAINS):
        tags.add("source_domain")
        tags.add("social_or_forum")
    if has_domain_in(candidate.domain, INFRA_OR_UTILITY_DOMAINS) or has_non_profile_domain_shape(candidate.domain):
        tags.add("utility_domain")
    if is_source_like_name(candidate.name):
        tags.add("source_title")
    else:
        tags.add("not_source_title")
    if is_generic_nav_name(candidate.name):
        tags.add("nav_anchor")
    if PRODUCT_OR_WORKFLOW_RE.search(candidate.name):
        tags.update({"product_name", "workflow_name"})
    if not is_source_like_name(candidate.name) and not is_generic_nav_name(candidate.name):
        tags.add("entity_name")
    if candidate.domain and domain_stem(candidate.domain).lower() in normalized(candidate.name):
        tags.add("official_domain_possible")
    if candidate.alternatives:
        tags.add("has_alternatives")
    if not tags & {"multi_surface", "repeated_evidence"}:
        tags.add("low_evidence")
    return tags


def nearest_examples(tags: set[str], examples: list[dict[str, Any]]) -> list[ExampleMatch]:
    """Return nearest examples by simple tag overlap."""
    matches: list[ExampleMatch] = []
    for example in examples:
        example_tags = set(example["tags"])
        overlap = len(tags & example_tags)
        matches.append(
            ExampleMatch(
                example_id=str(example["id"]),
                kind=str(example["kind"]),
                route=str(example["route"]),
                confidence_band=str(example["confidence_band"]),
                overlap=overlap,
                gap=0,
                tags=sorted(example_tags),
            )
        )
    matches.sort(key=lambda item: (-item.overlap, item.example_id))
    if len(matches) > 1:
        best = matches[0].overlap
        matches = [
            ExampleMatch(
                example_id=item.example_id,
                kind=item.kind,
                route=item.route,
                confidence_band=item.confidence_band,
                overlap=item.overlap,
                gap=best - item.overlap,
                tags=item.tags,
            )
            for item in matches
        ]
    return matches[:3]


def qualification_from_tags(candidate: CandidateV2, examples: list[dict[str, Any]]) -> QualificationV2:
    """Classify kind first, then choose route with Doro-style confidence ceilings."""
    tags = candidate_tags(candidate)
    matches = nearest_examples(tags, examples)
    best = matches[0]
    reasons = sorted(tags)
    blockers: list[str] = []
    caveats: list[str] = []
    alternatives = list(candidate.alternatives)
    method = "classify_by_example"
    kind = best.kind
    route = best.route
    confidence = best.confidence_band

    if "social_or_forum" in tags or "utility_domain" in tags or "nav_anchor" in tags or is_low_trust_candidate(candidate):
        kind = "nav_or_artifact"
        route = "reject_or_defer"
        confidence = "high"
        method = "exact"
        blockers.append("non_profile_artifact")
    elif "product_name" in tags or "workflow_name" in tags:
        kind = "product_or_workflow"
        route = "boundary_review"
        confidence = "medium"
        caveats.append("route separately from company-profile capture")
    elif "source_title" in tags and ("source_domain" in tags or not candidate.domain):
        kind = "directory_or_listicle"
        route = "preserve_source_evidence"
        confidence = "high"
        caveats.append("source page can preserve market evidence without becoming a profile target")
    elif "source_domain" in tags:
        kind = "source_or_publisher"
        route = "preserve_source_evidence"
        confidence = "medium"
        caveats.append("source domain evidence has a lower capture ceiling")
    elif "source_title" in tags and candidate.domain:
        kind = "company_or_brand"
        route = "boundary_review"
        confidence = "medium"
        method = "agent_judgment_needed"
        caveats.append("plausible company domain, but observed page title has source/listicle shape")
    elif candidate.candidate_source == "extracted_name":
        kind = "company_or_brand"
        route = "boundary_review"
        confidence = "medium"
        caveats.append("name-only candidate needs domain/entity resolution before capture")
    elif {"multi_surface", "repeated_evidence"} <= tags:
        kind = "company_or_brand"
        route = "capture_candidate"
        confidence = "medium"
    elif "mentioned_in_source" in tags:
        kind = "company_or_brand"
        route = "boundary_review"
        confidence = "low"
        caveats.append("source-only company evidence needs corroboration before capture")
    else:
        kind = "uncertain"
        route = "boundary_review"
        confidence = "low"
        method = "agent_judgment_needed"
        caveats.append("low evidence; classify before rejecting")

    if matches[0].gap == 0 and len(matches) > 1 and matches[1].gap <= 1:
        if route == "capture_candidate":
            route = "boundary_review"
            confidence = "medium"
            caveats.append("nearest examples are close; ambiguity gap blocks automatic capture")
        method = "agent_judgment_needed"

    return QualificationV2(
        kind=kind,
        route=route,
        confidence_band=confidence,
        method=method,
        reasons=reasons,
        blockers=blockers,
        alternatives=alternatives[:8],
        caveats=caveats,
        nearest_examples=[
            {
                "id": match.example_id,
                "kind": match.kind,
                "route": match.route,
                "overlap": match.overlap,
                "gap": match.gap,
            }
            for match in matches
        ],
    )


def is_low_trust_candidate(candidate: CandidateV2) -> bool:
    """Detect low-trust artifacts from candidate evidence."""
    observed = ObservedCandidate(
        key=candidate.candidate_id,
        cohort=candidate.cohort,
        name=candidate.name,
        domain=candidate.domain or "",
        evidence=candidate.evidence,
    )
    return is_low_trust_artifact(observed)


def convert_domain_candidate(candidate: ObservedCandidate) -> CandidateV2:
    """Convert a v1 observed-domain candidate into a v2 card candidate."""
    alternatives: list[dict[str, Any]] = []
    for title in title_values(candidate):
        for name in extract_names_from_title(title):
            if normalized(name) not in normalized(candidate.name):
                alternatives.append(alternative_from_name(name, candidate.key, title, candidate.domain))
    return CandidateV2(
        candidate_id=candidate.key,
        cohort=candidate.cohort,
        name=candidate.name,
        domain=candidate.domain,
        candidate_source="observed_domain",
        search_score=candidate.search_score,
        evidence=list(candidate.evidence),
        source_rows=set(candidate.source_rows),
        feeders=set(candidate.feeders),
        facets=set(candidate.facets),
        alternatives=alternatives,
    )


def build_name_candidates(domain_candidates: list[ObservedCandidate]) -> list[CandidateV2]:
    """Extract qrel-free name-only candidates from source titles and alternatives."""
    grouped: dict[str, CandidateV2] = {}
    for source in domain_candidates:
        if not (is_source_like_name(source.name) or source.evidence):
            continue
        for title in title_values(source):
            for name in extract_names_from_title(title):
                if normalized(name) in normalized(source.name) and source.domain and domain_stem(source.domain).lower() in normalized(name):
                    continue
                key = f"name:{source.cohort}:{re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')}"
                candidate = grouped.get(key)
                evidence_rows = [
                    {
                        "row_id": evidence.get("row_id"),
                        "feeder": evidence.get("feeder"),
                        "tool": evidence.get("tool"),
                        "unit_type": "extracted_name",
                        "rank": evidence.get("rank"),
                        "domain": None,
                        "url": evidence.get("url"),
                        "title": title,
                        "facet": evidence.get("facet"),
                        "source_domain": source.domain,
                    }
                    for evidence in source.evidence[:3]
                ]
                if candidate is None:
                    candidate = CandidateV2(
                        candidate_id=key,
                        cohort=source.cohort,
                        name=name,
                        domain=None,
                        candidate_source="extracted_name",
                        search_score=source.search_score * 0.75,
                        evidence=evidence_rows,
                        source_rows=set(source.source_rows),
                        feeders=set(source.feeders),
                        facets=set(source.facets),
                        alternatives=[
                            {
                                "name": source.name,
                                "domain": source.domain,
                                "source": source.key,
                                "reason": "source_page_that_named_candidate",
                            }
                        ],
                    )
                    grouped[key] = candidate
                else:
                    candidate.search_score += source.search_score * 0.1
                    candidate.evidence.extend(evidence_rows)
                    candidate.source_rows.update(source.source_rows)
                    candidate.feeders.update(source.feeders)
                    candidate.facets.update(source.facets)
                    candidate.alternatives.append(
                        {
                            "name": source.name,
                            "domain": source.domain,
                            "source": source.key,
                            "reason": "source_page_that_named_candidate",
                        }
                    )
    return list(grouped.values())


def build_v2_candidates() -> list[CandidateV2]:
    """Build qrel-free domain and extracted-name candidates."""
    observed = build_observed_candidates()
    domain_candidates = [convert_domain_candidate(candidate) for candidate in observed]
    name_candidates = build_name_candidates(observed)
    candidates = domain_candidates + name_candidates
    candidates.sort(key=lambda item: (-item.search_score, item.cohort, item.name.lower()))
    return candidates


def compact_evidence(candidate: CandidateV2, limit: int) -> list[dict[str, Any]]:
    """Keep enough compact evidence to audit a qualification."""
    compact: list[dict[str, Any]] = []
    for evidence in candidate.evidence[:limit]:
        compact.append(
            {
                "row_id": evidence.get("row_id"),
                "feeder": evidence.get("feeder"),
                "unit_type": evidence.get("unit_type"),
                "rank": evidence.get("rank"),
                "domain": evidence.get("domain"),
                "source_domain": evidence.get("source_domain"),
                "title": evidence.get("title"),
                "url": evidence.get("url"),
                "facet": evidence.get("facet"),
            }
        )
    return compact


def card_for_candidate(candidate: CandidateV2, rank: int, qualification: QualificationV2, evidence_limit: int) -> dict[str, Any]:
    """Serialize one v2 candidate card."""
    return {
        "candidate_id": candidate.candidate_id,
        "cohort": candidate.cohort,
        "rank": rank,
        "name": candidate.name,
        "domain": candidate.domain,
        "candidate_source": candidate.candidate_source,
        "ranker": {
            "search_score": round(candidate.search_score, 6),
            "evidence_count": len(candidate.evidence),
        },
        "matcher_hints": {
            "tags": sorted(candidate_tags(candidate)),
            "source_rows": sorted(candidate.source_rows),
            "feeders": sorted(candidate.feeders),
            "facets": sorted(candidate.facets),
        },
        "qualification": {
            "kind": qualification.kind,
            "route": qualification.route,
            "confidence_band": qualification.confidence_band,
            "method": qualification.method,
            "reasons": qualification.reasons,
            "blockers": qualification.blockers,
            "alternatives": qualification.alternatives,
            "caveats": qualification.caveats,
            "nearest_examples": qualification.nearest_examples,
        },
        "evidence": compact_evidence(candidate, evidence_limit),
    }


def qrel_aliases(qrel: Qrel) -> list[str]:
    """Return eval-only aliases for a qrel."""
    aliases = [qrel.name, *qrel.aliases]
    if qrel.domain:
        aliases.append(qrel.domain.split(".")[0])
    return [alias for alias in aliases if alias]


def eval_match(candidate: CandidateV2, qrel: Qrel) -> bool:
    """Match observed candidates to qrels only after routing."""
    if qrel.domain and candidate.domain == qrel.domain:
        return True
    name = normalized(candidate.name)
    domain = normalized((candidate.domain or "").replace(".", " "))
    for alias in qrel_aliases(qrel):
        alias_norm = normalized(alias)
        if not alias_norm or len(alias_norm) < 3:
            continue
        if alias_norm == name or alias_norm in name or alias_norm in domain:
            return True
    return False


def best_qrel(candidate: CandidateV2, qrels: list[Qrel]) -> Qrel | None:
    """Find the strongest eval-only qrel match for a candidate."""
    matches = [qrel for qrel in qrels if qrel.cohort == candidate.cohort and eval_match(candidate, qrel)]
    if not matches:
        return None
    return sorted(matches, key=lambda item: item.grade, reverse=True)[0]


def is_relevant_eval(qrel: Qrel | None) -> bool:
    """Use qrels only after routing to evaluate recall preservation."""
    if qrel is None:
        return False
    if qrel.cohort == "telehealth":
        return qrel.label in RELEVANT_TELEHEALTH_LABELS
    if qrel.cohort == "conversation_intelligence":
        return qrel.label in RELEVANT_CI_LABELS
    return False


def is_boundary_or_bad_eval(qrel: Qrel | None) -> bool:
    """Use qrels only after routing to detect bad/boundary capture promotions."""
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
        "candidate_source": card["candidate_source"],
        "kind": card["qualification"]["kind"],
        "route": card["qualification"]["route"],
        "confidence_band": card["qualification"]["confidence_band"],
        "method": card["qualification"]["method"],
        "qrel_grade": qrel.grade if qrel else None,
        "qrel_label": qrel.label if qrel else None,
        "qrel_name": qrel.name if qrel else None,
        "alternatives": card["qualification"]["alternatives"][:3],
        "caveats": card["qualification"]["caveats"],
    }


def unique_qrel_count(cards: list[dict[str, Any]], qrel_by_card: dict[str, Qrel | None]) -> int:
    """Count unique qrel keys represented in a card subset."""
    return len(
        {
            qrel_by_card[card["candidate_id"]].key
            for card in cards
            if qrel_by_card[card["candidate_id"]] is not None
        }
    )


def summarize_cohort(cards: list[dict[str, Any]], qrel_by_card: dict[str, Qrel | None]) -> dict[str, Any]:
    """Evaluate one cohort's routed candidates."""
    route_counts = Counter(card["qualification"]["route"] for card in cards)
    kind_counts = Counter(card["qualification"]["kind"] for card in cards)
    capture_cards = [card for card in cards if card["qualification"]["route"] == "capture_candidate"]
    boundary_cards = [card for card in cards if card["qualification"]["route"] == "boundary_review"]
    source_like_capture = [
        card
        for card in capture_cards
        if card["qualification"]["kind"] in {"source_or_publisher", "directory_or_listicle", "nav_or_artifact"}
    ]
    relevant_seen = [card for card in cards if is_relevant_eval(qrel_by_card[card["candidate_id"]])]
    relevant_preserved = [
        card
        for card in relevant_seen
        if card["qualification"]["route"] in {"capture_candidate", "boundary_review", "preserve_source_evidence"}
    ]
    relevant_capture = [card for card in relevant_seen if card["qualification"]["route"] == "capture_candidate"]
    relevant_boundary = [card for card in relevant_seen if card["qualification"]["route"] == "boundary_review"]
    boundary_promoted = [card for card in capture_cards if is_boundary_or_bad_eval(qrel_by_card[card["candidate_id"]])]

    return {
        "candidate_count": len(cards),
        "route_counts": dict(sorted(route_counts.items())),
        "kind_counts": dict(sorted(kind_counts.items())),
        "source_like_capture_count": len(source_like_capture),
        "known_relevant_seen": len(relevant_seen),
        "known_relevant_unique_seen": unique_qrel_count(relevant_seen, qrel_by_card),
        "known_relevant_preserved": len(relevant_preserved),
        "known_relevant_capture": len(relevant_capture),
        "known_relevant_boundary_review": len(relevant_boundary),
        "known_boundary_or_bad_promoted": len(boundary_promoted),
        "top_capture_candidates": [eval_row(card, qrel_by_card[card["candidate_id"]]) for card in capture_cards[:12]],
        "top_boundary_review": [eval_row(card, qrel_by_card[card["candidate_id"]]) for card in boundary_cards[:12]],
        "source_like_capture_candidates": [
            eval_row(card, qrel_by_card[card["candidate_id"]])
            for card in source_like_capture[:12]
        ],
        "known_boundary_or_bad_promoted_candidates": [
            eval_row(card, qrel_by_card[card["candidate_id"]])
            for card in boundary_promoted[:12]
        ],
        "known_relevant_not_capture_or_boundary": [
            eval_row(card, qrel_by_card[card["candidate_id"]])
            for card in relevant_seen
            if card["qualification"]["route"] not in {"capture_candidate", "boundary_review"}
        ][:15],
    }


def evaluate(cards: list[dict[str, Any]], candidates_by_id: dict[str, CandidateV2]) -> dict[str, Any]:
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
        "schema": "codex-candidate-qualification-v2-eval-v0",
        "boundary": {
            "inputs": [
                "receipts/raw/iteration-2/query-panel.json",
                "receipts/raw/page-extraction/pages/*.json",
                "codex-prototyping/codex_v2_kind_examples.json",
            ],
            "live_spend": "none; cached page-extraction outputs only",
            "routing_uses_qrels": False,
            "qrels_used_for": "evaluation-only matching after routing",
            "candidate_generation": "observed domains plus qrel-free name extraction from source titles",
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
    """Write the human-facing v2 readout."""
    lines = [
        "# Codex Candidate Qualification V2",
        "",
        "Date: 2026-06-26",
        "Status: packet-local Doro-shaped prototype; no engine changes",
        "",
        "## Read",
        "",
        "- V2 keeps routing qrel-free, adds `kind` before `route`, and uses `boundary_review` for ambiguity.",
        "- Code builds cards and matcher hints; the classify-by-example proxy returns an inspectable result shape for later agent adjudication.",
        "- Qrels and Brian-reviewed labels are joined only after routing for evaluation.",
        "",
        "## Outputs",
        "",
        f"- Kind examples: `{EXAMPLES_PATH.name}`",
        f"- Candidate cards: `{CARD_PATH.name}`",
        f"- Evaluation JSON: `{EVAL_PATH.name}`",
        f"- Summary: `{SUMMARY_PATH.name}`",
        "",
        "## Cohort Summary",
        "",
    ]
    summary_rows = [["Cohort", "Candidates", "Capture", "Boundary", "Preserve", "Reject", "Source-like capture"]]
    for cohort, cohort_eval in evaluation["cohorts"].items():
        counts = cohort_eval["route_counts"]
        summary_rows.append(
            [
                cohort,
                str(cohort_eval["candidate_count"]),
                str(counts.get("capture_candidate", 0)),
                str(counts.get("boundary_review", 0)),
                str(counts.get("preserve_source_evidence", 0)),
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
                f"- Known relevant seen: {cohort_eval['known_relevant_seen']} cards / {cohort_eval['known_relevant_unique_seen']} unique qrels.",
                f"- Known relevant routed to capture: {cohort_eval['known_relevant_capture']}.",
                f"- Known relevant routed to boundary review: {cohort_eval['known_relevant_boundary_review']}.",
                f"- Known bad/boundary rows promoted to capture: {cohort_eval['known_boundary_or_bad_promoted']}.",
                "",
                "Top capture candidates:",
                "",
            ]
        )
        capture_rows = [["Rank", "Name", "Domain", "Kind", "Eval label"]]
        for row in cohort_eval["top_capture_candidates"][:10]:
            capture_rows.append(
                [
                    str(row["rank"]),
                    str(row["name"]),
                    str(row["domain"] or ""),
                    str(row["kind"]),
                    str(row["qrel_label"] or "unjudged"),
                ]
            )
        lines.extend(markdown_table(capture_rows) if len(capture_rows) > 1 else ["_None._"])
        lines.extend(["", "Top boundary review:", ""])
        boundary_rows = [["Rank", "Name", "Domain", "Kind", "Eval label", "Caveat"]]
        for row in cohort_eval["top_boundary_review"][:10]:
            caveat = "; ".join(row["caveats"][:2])
            boundary_rows.append(
                [
                    str(row["rank"]),
                    str(row["name"]),
                    str(row["domain"] or ""),
                    str(row["kind"]),
                    str(row["qrel_label"] or "unjudged"),
                    caveat,
                ]
            )
        lines.extend(markdown_table(boundary_rows) if len(boundary_rows) > 1 else ["_None._"])
        if cohort_eval["known_relevant_not_capture_or_boundary"]:
            lines.extend(["", "Known relevant not capture/boundary:", ""])
            miss_rows = [["Rank", "Name", "Route", "Eval label", "Why"]]
            for row in cohort_eval["known_relevant_not_capture_or_boundary"][:10]:
                why = "; ".join(row["caveats"])
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
            "- Replaces the v1 deterministic `source_role -> route` gate with `kind -> route` adjudication.",
            "- Keeps source evidence preservation and candidate cards as the stable packet-local shape.",
            "- Does not create a reusable skill, durable schema, or automatic capture queue.",
            "",
            "## Cheapest Disconfirming Check",
            "",
            "The borrowed Doro shape helps only if source/listicle artifacts stay out of capture while plausible companies and domainless brands move to capture or boundary review instead of false reject.",
            "",
        ]
    )
    SUMMARY_PATH.write_text("\n".join(lines), encoding="utf-8")


def build_cards(evidence_limit: int) -> tuple[list[dict[str, Any]], dict[str, CandidateV2]]:
    """Build v2 routed cards and candidate index."""
    examples = load_examples()
    candidates = build_v2_candidates()
    cards: list[dict[str, Any]] = []
    candidates_by_id: dict[str, CandidateV2] = {}
    ranks_by_cohort: Counter[str] = Counter()
    for candidate in candidates:
        if candidate.cohort not in COHORTS:
            continue
        ranks_by_cohort[candidate.cohort] += 1
        qualification = qualification_from_tags(candidate, examples)
        card = card_for_candidate(candidate, ranks_by_cohort[candidate.cohort], qualification, evidence_limit)
        cards.append(card)
        candidates_by_id[candidate.candidate_id] = candidate
    return cards, candidates_by_id


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Doro-shaped candidate qualification prototype.")
    parser.add_argument("--evidence-limit", type=int, default=8)
    args = parser.parse_args()

    cards, candidates_by_id = build_cards(evidence_limit=args.evidence_limit)
    evaluation = evaluate(cards, candidates_by_id)
    write_json(CARD_PATH, {"schema": "codex-v2-candidate-cards-v0", "cards": cards})
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
