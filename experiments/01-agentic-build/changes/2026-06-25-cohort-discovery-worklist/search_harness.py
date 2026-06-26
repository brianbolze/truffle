#!/usr/bin/env python3
"""Evaluate cohort discovery as a search problem over candidate entities.

This stays packet-local and spends nothing. It reuses the frozen validation inputs
and iteration-2 raw retrieval envelopes, then asks search-shaped questions:

- Which judged targets were retrieved?
- Which retrieved entities would rank into a capture worklist?
- Which misses are retrieval misses versus ranking/evidence misses?
"""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from score_iteration2 import CI_ALIASES, CI_STORE_BASELINE_HITS, TELEHEALTH_ALIASES, alias_pattern

PACKET = Path(__file__).resolve().parent
RAW_DIR = PACKET / "receipts" / "raw" / "iteration-2"
OUTPUT_DIR = PACKET / "receipts" / "raw" / "search-harness"
TELEHEALTH_INPUT = PACKET / "validation-inputs" / "telehealth-holdouts.json"
CI_INPUT = PACKET / "validation-inputs" / "conversation-intelligence-targets.json"
K_VALUES = (5, 10, 20, 50)
RRF_K = 60

REVIEWED_TELEHEALTH = [
    {
        "name": "Ulo",
        "domain": "tryulo.com",
        "grade": 3,
        "label": "worth_capture",
        "aliases": ["ulo", "tryulo", "tryulo.com"],
    },
    {
        "name": "Alloy Women's Health",
        "domain": "myalloy.com",
        "grade": 3,
        "label": "worth_capture",
        "aliases": ["alloy", "alloy women's health", "myalloy", "myalloy.com"],
    },
    {
        "name": "Mochi Health",
        "domain": "joinmochi.com",
        "grade": 3,
        "label": "worth_capture",
        "aliases": ["mochi", "mochi health", "joinmochi", "joinmochi.com"],
    },
    {
        "name": "Eucalyptus Health",
        "domain": "eucalyptus.health",
        "grade": 3,
        "label": "worth_capture",
        "aliases": ["eucalyptus", "eucalyptus health", "eucalyptus.health"],
    },
    {
        "name": "MangoRX",
        "domain": "mangorx.com",
        "grade": 1,
        "label": "tier_c_only",
        "aliases": ["mangorx", "mango rx", "mangorx.com"],
    },
    {
        "name": "RoenRx",
        "domain": "roenrx.com",
        "grade": 1,
        "label": "tier_c_only",
        "aliases": ["roenrx", "roen rx", "roenrx.com"],
    },
    {
        "name": "MyStart",
        "domain": "mystart.com",
        "grade": 1,
        "label": "tier_c_only",
        "aliases": ["mystart", "mystart.com"],
    },
    {
        "name": "BrightMeds",
        "domain": "brightmeds.com",
        "grade": 1,
        "label": "tier_c_only",
        "aliases": ["brightmeds", "bright meds", "brightmeds.com"],
    },
    {
        "name": "G-Plans Direct",
        "domain": "gplansdirect.com",
        "grade": 1,
        "label": "tier_c_only",
        "aliases": ["g-plans direct", "gplans direct", "gplansdirect", "gplansdirect.com"],
    },
    {
        "name": "Evernow",
        "domain": "evernow.com",
        "grade": 1,
        "label": "tier_c_only",
        "aliases": ["evernow", "evernow.com"],
    },
    {
        "name": "Midi Health",
        "domain": "joinmidi.com",
        "grade": 3,
        "label": "worth_capture",
        "aliases": ["midi", "midi health", "joinmidi", "joinmidi.com"],
        "notes": ["Brian: absolutely worth capturing; at least should-have, arguably must-have."],
    },
    {
        "name": "Juniper",
        "domain": "myjuniper.com",
        "grade": 1,
        "label": "unsure",
        "aliases": ["juniper", "myjuniper", "myjuniper.com"],
    },
    {
        "name": "Zealthy",
        "domain": "getzealthy.com",
        "grade": 0,
        "label": "exclude",
        "aliases": ["zealthy", "getzealthy", "getzealthy.com"],
    },
    {
        "name": "FitRx",
        "domain": "fitrx.com",
        "grade": 0,
        "label": "exclude",
        "aliases": ["fitrx", "fit rx", "fitrx.com"],
    },
    {
        "name": "AMRx",
        "domain": "amrx.com",
        "grade": 0,
        "label": "exclude",
        "aliases": ["amrx", "am rx", "amrx.com"],
    },
]


@dataclass
class Qrel:
    """A judged entity target for search-style evaluation."""

    key: str
    cohort: str
    name: str
    grade: int
    label: str
    domain: str | None = None
    aliases: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


@dataclass
class Unit:
    """One retrievable text unit from a raw source envelope."""

    cohort: str
    row_id: str
    feeder: str
    tool: str
    unit_type: str
    rank: int
    text: str
    domain: str | None = None
    url: str | None = None
    title: str | None = None
    facet: str | None = None


@dataclass
class Candidate:
    """A candidate entity with accumulated retrieval evidence."""

    key: str
    cohort: str
    name: str
    domain: str | None = None
    qrel_key: str | None = None
    qrel_grade: int | None = None
    qrel_label: str | None = None
    rrf: float = 0.0
    search_score: float = 0.0
    evidence: list[dict[str, Any]] = field(default_factory=list)
    source_rows: set[str] = field(default_factory=set)
    feeders: set[str] = field(default_factory=set)
    tools: set[str] = field(default_factory=set)
    facets: set[str] = field(default_factory=set)
    exact_domain_hit: bool = False
    alias_hit: bool = False
    store_baseline_hit: bool = False


def load_json(path: Path) -> Any:
    """Load JSON from the packet with explicit encoding."""
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data: Any) -> None:
    """Write generated JSON with stable indentation for review."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def slug(value: str) -> str:
    """Create a stable human-readable key fragment."""
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def canonical_domain(value: str | None) -> str | None:
    """Normalize a URL or domain to the domain key shape used by the harness."""
    if not value:
        return None
    raw = value.strip()
    if not raw:
        return None
    parsed = urlparse(raw if "://" in raw else f"https://{raw}")
    host = parsed.netloc or parsed.path.split("/")[0]
    host = host.lower().removeprefix("www.")
    return host or None


def norm(value: str) -> str:
    """Normalize text before conservative alias matching."""
    return re.sub(r"\s+", " ", value.lower())


def qrel_key(cohort: str, name: str) -> str:
    """Return the canonical qrel candidate key for a cohort/name pair."""
    return f"qrel:{cohort}:{slug(name)}"


def add_qrel(qrels: dict[str, Qrel], item: Qrel) -> None:
    """Add or merge a qrel; duplicate labels preserve the highest grade."""
    existing = qrels.get(item.key)
    if existing is None:
        qrels[item.key] = item
        return
    existing.grade = max(existing.grade, item.grade)
    existing.label = "|".join(sorted(set(existing.label.split("|") + item.label.split("|"))))
    if existing.domain is None:
        existing.domain = item.domain
    existing.aliases = sorted(set(existing.aliases + item.aliases))
    existing.notes = sorted(set(existing.notes + item.notes))


def aliases_for(name: str, supplied: list[str] | None = None) -> list[str]:
    """Build alias terms from curated constants plus domain/name fallbacks."""
    base = supplied or TELEHEALTH_ALIASES.get(name) or CI_ALIASES.get(name) or [name]
    return sorted(set(alias for alias in base if alias))


def build_qrels() -> dict[str, Qrel]:
    """Create packet-local relevance judgments from frozen validation inputs."""
    qrels: dict[str, Qrel] = {}
    telehealth = load_json(TELEHEALTH_INPUT)
    for row in telehealth["holdouts"]:
        grade = 4 if row["gate"] == "must_hit" else 3
        add_qrel(
            qrels,
            Qrel(
                key=qrel_key("telehealth", row["name"]),
                cohort="telehealth",
                name=row["name"],
                grade=grade,
                label=row["gate"],
                domain=canonical_domain(row["website"]),
                aliases=aliases_for(row["name"]),
                notes=[row["formidability_tier"]],
            ),
        )
    for row in telehealth["curated_negatives"]:
        add_qrel(
            qrels,
            Qrel(
                key=qrel_key("telehealth", row["name"]),
                cohort="telehealth",
                name=row["name"],
                grade=0,
                label="curated_negative",
                domain=canonical_domain(row["website"]),
                aliases=aliases_for(row["name"], [row["name"], row["website"]]),
                notes=[row["reason"]],
            ),
        )
    for row in REVIEWED_TELEHEALTH:
        add_qrel(
            qrels,
            Qrel(
                key=qrel_key("telehealth", row["name"]),
                cohort="telehealth",
                name=row["name"],
                grade=row["grade"],
                label=row["label"],
                domain=canonical_domain(row["domain"]),
                aliases=aliases_for(row["name"], row["aliases"]),
                notes=row.get("notes", []),
            ),
        )

    ci = load_json(CI_INPUT)
    for row in ci["core_ranked"]:
        grade = 4 if row["rank"] <= 10 else 2
        label = "top_10_core" if row["rank"] <= 10 else "core_boundary_product_workflow"
        add_qrel(
            qrels,
            Qrel(
                key=qrel_key("conversation_intelligence", row["name"]),
                cohort="conversation_intelligence",
                name=row["name"],
                grade=grade,
                label=label,
                aliases=aliases_for(row["name"]),
                notes=[f"rank={row['rank']}"],
            ),
        )
    for row in ci["adjacent_transcription_dev_tools"]:
        grade = 1 if row["name"] == "OpenAI Whisper" else 0
        add_qrel(
            qrels,
            Qrel(
                key=qrel_key("conversation_intelligence", row["name"]),
                cohort="conversation_intelligence",
                name=row["name"],
                grade=grade,
                label="adjacent_transcription_dev",
                aliases=aliases_for(row["name"]),
                notes=[row.get("note", "adjacent transcription-dev tool")],
            ),
        )
    return qrels


def row_facet(row_id: str) -> str:
    """Infer a lightweight query facet from the frozen row id."""
    if "ed-" in row_id:
        return "ed"
    if "longevity" in row_id or "healthspan" in row_id or "nad" in row_id:
        return "longevity_healthspan"
    if "menopause" in row_id or "hrt" in row_id:
        return "menopause_hrt"
    if "glp1" in row_id:
        return "glp1"
    if "trt" in row_id or "mens-health" in row_id:
        return "mens_health_trt"
    if "meeting" in row_id or "notetaker" in row_id or "notes" in row_id:
        return "meeting_notes"
    if "conversation" in row_id or "enterprise-ci" in row_id or "call-analysis" in row_id:
        return "conversation_intelligence"
    return "general"


def unit_text(*parts: Any) -> str:
    """Join source fields into a matchable unit body."""
    return norm(" ".join(str(part or "") for part in parts))


def units_for_row(row: dict[str, Any]) -> list[Unit]:
    """Extract ranked result/text units from one raw retrieval envelope."""
    folder = "serpapi" if row["tool"] == "serpapi" else "exa"
    data = load_json(RAW_DIR / folder / f"{row['id']}.json")
    facet = row_facet(row["id"])
    units: list[Unit] = []
    if row["tool"] == "serpapi":
        for item in data.get("organic_results", []):
            units.append(
                Unit(
                    cohort=row["cohort"],
                    row_id=row["id"],
                    feeder=row["feeder"],
                    tool=row["tool"],
                    unit_type="organic",
                    rank=int(item.get("position") or 100),
                    text=unit_text(item.get("title"), item.get("snippet"), item.get("displayed_link"), item.get("link")),
                    domain=canonical_domain(item.get("link")),
                    url=item.get("link"),
                    title=item.get("title"),
                    facet=facet,
                )
            )
        for item in data.get("references", []):
            units.append(
                Unit(
                    cohort=row["cohort"],
                    row_id=row["id"],
                    feeder=row["feeder"],
                    tool=row["tool"],
                    unit_type="reference",
                    rank=int(item.get("index", 99)) + 1,
                    text=unit_text(item.get("source"), item.get("title"), item.get("link")),
                    domain=canonical_domain(item.get("link")),
                    url=item.get("link"),
                    title=item.get("title") or item.get("source"),
                    facet=facet,
                )
            )
        for index, value in enumerate(data.get("headings", []), start=1):
            units.append(
                Unit(
                    cohort=row["cohort"],
                    row_id=row["id"],
                    feeder=row["feeder"],
                    tool=row["tool"],
                    unit_type="ai_heading",
                    rank=index,
                    text=unit_text(value),
                    title=str(value),
                    facet=facet,
                )
            )
        for index, value in enumerate(data.get("narrative_paragraphs", []), start=1):
            units.append(
                Unit(
                    cohort=row["cohort"],
                    row_id=row["id"],
                    feeder=row["feeder"],
                    tool=row["tool"],
                    unit_type="ai_narrative",
                    rank=index + 10,
                    text=unit_text(value),
                    title=str(value)[:120],
                    facet=facet,
                )
            )
        for item in data.get("ranked_brands", []):
            units.append(
                Unit(
                    cohort=row["cohort"],
                    row_id=row["id"],
                    feeder=row["feeder"],
                    tool=row["tool"],
                    unit_type="ai_ranked_brand",
                    rank=int(item.get("position") or 100),
                    text=unit_text(item.get("label"), item.get("after_colon"), item.get("raw_snippet")),
                    title=item.get("raw_snippet"),
                    facet=facet,
                )
            )
    elif row["tool"] == "exa_search":
        for item in data.get("results", []):
            units.append(
                Unit(
                    cohort=row["cohort"],
                    row_id=row["id"],
                    feeder=row["feeder"],
                    tool=row["tool"],
                    unit_type="exa_result",
                    rank=int(item.get("rank") or 100),
                    text=unit_text(item.get("title"), item.get("url"), item.get("domain")),
                    domain=canonical_domain(item.get("domain") or item.get("url")),
                    url=item.get("url"),
                    title=item.get("title"),
                    facet=facet,
                )
            )
    return units


def all_units(rows: list[dict[str, Any]]) -> list[Unit]:
    """Extract units for every frozen query-panel row."""
    units: list[Unit] = []
    for row in rows:
        units.extend(units_for_row(row))
    return units


def display_name_for_domain(domain: str, title: str | None) -> str:
    """Choose a readable candidate name for a direct-result domain."""
    if title:
        cleaned = re.split(r"\s[-|:]\s", title)[0]
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        if cleaned:
            return cleaned[:80]
    return domain


def qrel_domain_index(qrels: dict[str, Qrel]) -> dict[tuple[str, str], str]:
    """Map cohort/domain to qrel key for exact-domain hits."""
    index = {}
    for key, item in qrels.items():
        if item.domain:
            index[(item.cohort, item.domain)] = key
    return index


def get_candidate(candidates: dict[str, Candidate], key: str, cohort: str, name: str) -> Candidate:
    """Fetch or create a candidate record."""
    if key not in candidates:
        candidates[key] = Candidate(key=key, cohort=cohort, name=name)
    return candidates[key]


def add_evidence(candidate: Candidate, unit: Unit, method: str, matched_aliases: list[str] | None = None) -> None:
    """Accumulate one evidence hit and update rank features."""
    weight = 0.8 if unit.unit_type in {"ai_heading", "ai_narrative", "ai_ranked_brand"} else 1.0
    rrf_add = weight / (RRF_K + max(unit.rank, 1))
    candidate.rrf += rrf_add
    candidate.source_rows.add(unit.row_id)
    candidate.feeders.add(unit.feeder)
    candidate.tools.add(unit.tool)
    if unit.facet:
        candidate.facets.add(unit.facet)
    if method == "alias":
        candidate.alias_hit = True
    if method == "domain":
        candidate.exact_domain_hit = True
    candidate.evidence.append(
        {
            "row_id": unit.row_id,
            "feeder": unit.feeder,
            "tool": unit.tool,
            "unit_type": unit.unit_type,
            "rank": unit.rank,
            "method": method,
            "matched_aliases": matched_aliases or [],
            "domain": unit.domain,
            "url": unit.url,
            "title": unit.title,
            "facet": unit.facet,
            "rrf_add": round(rrf_add, 6),
        }
    )


def candidate_from_qrel(candidate: Candidate, item: Qrel) -> None:
    """Attach judgment metadata to a candidate."""
    candidate.qrel_key = item.key
    candidate.qrel_grade = item.grade
    candidate.qrel_label = item.label
    candidate.name = item.name
    if item.domain:
        candidate.domain = item.domain


def match_aliases(unit: Unit, item: Qrel) -> list[str]:
    """Return aliases from a qrel observed in one source unit."""
    found = []
    for alias in item.aliases:
        if alias_pattern(alias).search(unit.text):
            found.append(alias)
    return found


def build_candidates(units: list[Unit], qrels: dict[str, Qrel], include_store_baseline: bool) -> dict[str, Candidate]:
    """Build entity candidates from exact-domain hits, alias mentions, and unknown domains."""
    candidates: dict[str, Candidate] = {}
    domain_index = qrel_domain_index(qrels)
    for unit in units:
        if unit.domain:
            matched_key = domain_index.get((unit.cohort, unit.domain))
            if matched_key:
                item = qrels[matched_key]
                candidate = get_candidate(candidates, item.key, item.cohort, item.name)
                candidate_from_qrel(candidate, item)
                add_evidence(candidate, unit, "domain")
            else:
                candidate_key = f"domain:{unit.cohort}:{unit.domain}"
                candidate = get_candidate(
                    candidates,
                    candidate_key,
                    unit.cohort,
                    display_name_for_domain(unit.domain, unit.title),
                )
                candidate.domain = unit.domain
                add_evidence(candidate, unit, "domain")
        for item in qrels.values():
            if item.cohort != unit.cohort:
                continue
            found = match_aliases(unit, item)
            if not found:
                continue
            candidate = get_candidate(candidates, item.key, item.cohort, item.name)
            candidate_from_qrel(candidate, item)
            add_evidence(candidate, unit, "alias", found)

    if include_store_baseline:
        for item in qrels.values():
            if item.cohort != "conversation_intelligence" or item.name not in CI_STORE_BASELINE_HITS:
                continue
            candidate = get_candidate(candidates, item.key, item.cohort, item.name)
            candidate_from_qrel(candidate, item)
            candidate.store_baseline_hit = True
            candidate.rrf += 1 / (RRF_K + 1)
            candidate.source_rows.add("store_baseline")
            candidate.feeders.add("store_baseline")
            candidate.tools.add("store")
            candidate.evidence.append(
                {
                    "row_id": "store_baseline",
                    "feeder": "store_baseline",
                    "tool": "store",
                    "unit_type": "store_profile",
                    "rank": 1,
                    "method": "store_baseline",
                    "matched_aliases": ["local store profile"],
                    "domain": item.domain,
                    "url": None,
                    "title": item.name,
                    "facet": "store_baseline",
                    "rrf_add": round(1 / (RRF_K + 1), 6),
                }
            )
    score_candidates(candidates)
    return candidates


def score_candidates(candidates: dict[str, Candidate]) -> None:
    """Apply a simple transparent rerank over RRF and evidence diversity."""
    for candidate in candidates.values():
        diversity_bonus = 0.004 * len(candidate.feeders) + 0.002 * len(candidate.source_rows)
        exact_bonus = 0.004 if candidate.exact_domain_hit else 0
        store_bonus = 0.006 if candidate.store_baseline_hit else 0
        candidate.search_score = candidate.rrf + diversity_bonus + exact_bonus + store_bonus


def ranked_candidates(candidates: dict[str, Candidate], cohort: str) -> list[Candidate]:
    """Return candidates ranked by the transparent packet-local search score."""
    cohort_candidates = [candidate for candidate in candidates.values() if candidate.cohort == cohort]
    return sorted(
        cohort_candidates,
        key=lambda item: (
            item.search_score,
            item.rrf,
            len(item.feeders),
            item.exact_domain_hit,
            item.name.lower(),
        ),
        reverse=True,
    )


def relevant_qrels(qrels: dict[str, Qrel], cohort: str) -> list[Qrel]:
    """Return qrels that count as capture-relevant for recall/precision."""
    return [item for item in qrels.values() if item.cohort == cohort and item.grade >= 3]


def dcg(grades: list[int]) -> float:
    """Compute discounted cumulative gain for graded relevance."""
    return sum((2**grade - 1) / math.log2(index + 2) for index, grade in enumerate(grades))


def metrics_at_k(ranked: list[Candidate], qrels: dict[str, Qrel], cohort: str) -> dict[str, Any]:
    """Compute small search metrics over judged targets."""
    relevant_keys = {item.key for item in relevant_qrels(qrels, cohort)}
    qrels_in_cohort = [item for item in qrels.values() if item.cohort == cohort]
    ideal_grades = sorted((item.grade for item in qrels_in_cohort), reverse=True)
    out: dict[str, Any] = {}
    for k_value in K_VALUES:
        top = ranked[:k_value]
        retrieved_relevant = [candidate for candidate in top if candidate.qrel_key in relevant_keys]
        precision = len(retrieved_relevant) / k_value
        recall = len({candidate.qrel_key for candidate in retrieved_relevant}) / max(len(relevant_keys), 1)
        grades = [candidate.qrel_grade or 0 for candidate in top]
        ideal = dcg(ideal_grades[:k_value])
        ndcg = dcg(grades) / ideal if ideal else 0.0
        out[f"@{k_value}"] = {
            "precision": round(precision, 3),
            "recall": round(recall, 3),
            "ndcg": round(ndcg, 3),
            "relevant_hits": len(retrieved_relevant),
        }
    return out


def miss_table(candidates: dict[str, Candidate], qrels: dict[str, Qrel], cohort: str) -> list[dict[str, Any]]:
    """Classify relevant qrels not found by the current retrieval evidence."""
    rows = []
    for item in relevant_qrels(qrels, cohort):
        candidate = candidates.get(item.key)
        if candidate is not None:
            continue
        rows.append(
            {
                "name": item.name,
                "grade": item.grade,
                "label": item.label,
                "domain": item.domain,
                "diagnosis": "not_retrieved_in_existing_raw_units",
                "notes": item.notes,
            }
        )
    return rows


def retrieval_breakdown(candidates: dict[str, Candidate], qrels: dict[str, Qrel], cohort: str) -> dict[str, Any]:
    """Group grade-3+ retrieval by judgment label so broad metrics stay legible."""
    breakdown: dict[str, dict[str, int]] = {}
    for item in relevant_qrels(qrels, cohort):
        row = breakdown.setdefault(item.label, {"total": 0, "retrieved": 0, "missed": 0})
        row["total"] += 1
        if item.key in candidates:
            row["retrieved"] += 1
        else:
            row["missed"] += 1
    return dict(sorted(breakdown.items()))


def candidate_to_json(candidate: Candidate, rank: int, include_evidence: bool = False) -> dict[str, Any]:
    """Serialize a candidate with review-friendly rank features."""
    row = {
        "rank": rank,
        "key": candidate.key,
        "name": candidate.name,
        "domain": candidate.domain,
        "qrel_grade": candidate.qrel_grade,
        "qrel_label": candidate.qrel_label,
        "search_score": round(candidate.search_score, 6),
        "rrf": round(candidate.rrf, 6),
        "feeders": sorted(candidate.feeders),
        "source_rows": sorted(candidate.source_rows),
        "facets": sorted(candidate.facets),
        "exact_domain_hit": candidate.exact_domain_hit,
        "alias_hit": candidate.alias_hit,
        "store_baseline_hit": candidate.store_baseline_hit,
        "evidence_count": len(candidate.evidence),
    }
    if include_evidence:
        row["evidence"] = candidate.evidence[:8]
    return row


def summarize_variant(
    name: str,
    candidates: dict[str, Candidate],
    qrels: dict[str, Qrel],
    cohort: str,
) -> dict[str, Any]:
    """Summarize one cohort/search variant."""
    ranked = ranked_candidates(candidates, cohort)
    judged = [candidate for candidate in ranked if candidate.qrel_key is not None]
    unknown = [candidate for candidate in ranked if candidate.qrel_key is None]
    low_grade_in_top20 = [
        candidate_to_json(candidate, rank + 1)
        for rank, candidate in enumerate(ranked[:20])
        if candidate.qrel_grade is not None and candidate.qrel_grade <= 1
    ]
    return {
        "variant": name,
        "cohort": cohort,
        "candidate_count": len(ranked),
        "judged_candidate_count": len(judged),
        "metrics": metrics_at_k(ranked, qrels, cohort),
        "retrieval_breakdown": retrieval_breakdown(candidates, qrels, cohort),
        "misses": miss_table(candidates, qrels, cohort),
        "top_ranked": [candidate_to_json(candidate, index + 1, include_evidence=True) for index, candidate in enumerate(ranked[:15])],
        "top_unknown_domains": [candidate_to_json(candidate, index + 1) for index, candidate in enumerate(unknown[:15])],
        "low_grade_or_boundary_in_top20": low_grade_in_top20,
    }


def write_receipt(summary: dict[str, Any], output_path: Path) -> None:
    """Write the human-facing search harness receipt."""
    tele = summary["variants"]["telehealth_external"]
    ci_external = summary["variants"]["conversation_external"]
    ci_store = summary["variants"]["conversation_store_first"]
    lines = [
        "# Search Harness Receipt",
        "",
        "Date: 2026-06-26",
        "Status: packet-local search framing pass; no live source spend",
        "",
        "## What This Adds",
        "",
        "This pass treats cohort discovery as entity search. It builds packet-local relevance judgments,",
        "extracts ranked source units from the existing iteration-2 raw outputs, creates entity candidates",
        "from exact-domain hits and alias mentions, then ranks them with a transparent RRF-style score.",
        "",
        "It does not open listicle pages or fetch new sources. That omission is intentional: this receipt",
        "shows what the current raw evidence can see before adding page extraction.",
        "",
        "## Relevance Frame",
        "",
        "A relevant capture candidate is not merely a mentioned company. For this packet, relevance means:",
        "",
        "- grade 4: must-capture / F3-F4 / top-10 category-defining target;",
        "- grade 3: should-capture / F2 / Brian-marked worth_capture;",
        "- grade 2: core but product/workflow boundary;",
        "- grade 1: boundary, unsure, or Tier C only;",
        "- grade 0: hard exclude / wrong-type / adjacent pollution.",
        "",
        "The ranker does not use the grade as a feature; grades are evaluation labels.",
        "",
        "## Metrics Snapshot",
        "",
        "| Variant | Candidates | Judged | P@10 | R@10 | nDCG@10 | Relevant misses |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        _metric_row("telehealth_external", tele),
        _metric_row("conversation_external", ci_external),
        _metric_row("conversation_store_first", ci_store),
        "",
        "## Telehealth Search Diagnosis",
        "",
        f"- Relevant qrels not retrieved from existing raw units: {len(tele['misses'])}.",
        _breakdown_line("Telehealth retrieval by label", tele["retrieval_breakdown"]),
        "- This means the current raw rows do not contain enough machine-readable evidence for the broad",
        "  telehealth target set. A better reranker alone cannot recover names absent from the raw units.",
        "- Top-ranked unknown domains are mostly source/publisher or long-tail operator artifacts, which is",
        "  the expected symptom of using SERP result pages without extracting the entities inside list pages.",
        "",
        "Most important telehealth misses:",
        "",
        *[
            f"- {row['name']} ({row['label']}, grade {row['grade']})"
            for row in tele["misses"][:12]
        ],
        "",
        "## Conversation Intelligence Diagnosis",
        "",
        f"- External-only misses: {', '.join(row['name'] for row in ci_external['misses']) or 'none'}.",
        f"- Store-first misses: {', '.join(row['name'] for row in ci_store['misses']) or 'none'}.",
        _breakdown_line("Store-first retrieval by label", ci_store["retrieval_breakdown"]),
        "- Store-first materially changes search quality because several high-relevance targets are already",
        "  profiled locally. This supports keeping store baseline as a first-class retriever.",
        "",
        "## Next Packet",
        "",
        "Make page extraction the next evaluated retrieval stage. The search harness gives a simple gate:",
        "page extraction must improve relevant recall and top-K precision over this raw-unit baseline,",
        "especially for telehealth, without promoting grade-0/1 candidates into the capture queue.",
        "",
        "Generated detail:",
        "",
        f"- JSON summary: `{summary['outputs']['summary_json']}`",
    ]
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _metric_row(label: str, variant: dict[str, Any]) -> str:
    """Format one metrics row for the generated receipt."""
    at10 = variant["metrics"]["@10"]
    return (
        f"| {label} | {variant['candidate_count']} | {variant['judged_candidate_count']} | "
        f"{at10['precision']:.3f} | {at10['recall']:.3f} | {at10['ndcg']:.3f} | "
        f"{len(variant['misses'])} |"
    )


def _breakdown_line(label: str, breakdown: dict[str, Any]) -> str:
    """Format label-level retrieval counts for the generated receipt."""
    parts = [
        f"{name} {values['retrieved']}/{values['total']}"
        for name, values in breakdown.items()
    ]
    return f"- {label}: " + "; ".join(parts) + "."


def build_summary() -> dict[str, Any]:
    """Build the full search-harness summary from existing packet inputs."""
    qrels = build_qrels()
    rows = load_json(RAW_DIR / "query-panel.json")
    units = all_units(rows)
    external_candidates = build_candidates(units, qrels, include_store_baseline=False)
    store_first_candidates = build_candidates(units, qrels, include_store_baseline=True)
    summary_path = OUTPUT_DIR / "search-summary.json"
    receipt_path = PACKET / "receipts" / "search-harness.md"
    return {
        "schema": "cohort-discovery-search-harness-v1",
        "inputs": {
            "query_panel": str((RAW_DIR / "query-panel.json").relative_to(PACKET)),
            "telehealth_qrels": str(TELEHEALTH_INPUT.relative_to(PACKET)),
            "conversation_qrels": str(CI_INPUT.relative_to(PACKET)),
            "live_spend": "none; reused existing iteration-2 raw outputs",
        },
        "outputs": {
            "summary_json": str(summary_path.relative_to(PACKET)),
            "receipt": str(receipt_path.relative_to(PACKET)),
        },
        "qrel_counts": {
            cohort: {
                "total": sum(1 for item in qrels.values() if item.cohort == cohort),
                "grade_3_plus": sum(1 for item in qrels.values() if item.cohort == cohort and item.grade >= 3),
                "grade_0_or_1": sum(1 for item in qrels.values() if item.cohort == cohort and item.grade <= 1),
            }
            for cohort in ("telehealth", "conversation_intelligence")
        },
        "unit_count": len(units),
        "variants": {
            "telehealth_external": summarize_variant("telehealth_external", external_candidates, qrels, "telehealth"),
            "conversation_external": summarize_variant(
                "conversation_external",
                external_candidates,
                qrels,
                "conversation_intelligence",
            ),
            "conversation_store_first": summarize_variant(
                "conversation_store_first",
                store_first_candidates,
                qrels,
                "conversation_intelligence",
            ),
        },
        "limits": [
            "No live retrieval or page opening.",
            "SERP/listicle result pages are treated as source units, not extracted pages.",
            "Alias matching is conservative but still not full entity resolution.",
            "Ranking features are transparent heuristics for error analysis, not a durable score.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build packet-local search harness outputs.")
    parser.add_argument("--summary", default=str(OUTPUT_DIR / "search-summary.json"))
    parser.add_argument("--receipt", default=str(PACKET / "receipts" / "search-harness.md"))
    args = parser.parse_args()

    summary = build_summary()
    summary_path = Path(args.summary)
    receipt_path = Path(args.receipt)
    summary["outputs"]["summary_json"] = str(summary_path.relative_to(PACKET))
    summary["outputs"]["receipt"] = str(receipt_path.relative_to(PACKET))
    write_json(summary_path, summary)
    write_receipt(summary, receipt_path)
    print(json.dumps({"summary": str(summary_path), "receipt": str(receipt_path)}, indent=2))


if __name__ == "__main__":
    main()
