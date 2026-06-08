#!/usr/bin/env python3
"""SERP intent panel consumer — repeatable cohort evidence over captured Google SERPs.

`serpapi.py` captures one raw Google result envelope. This consumer takes a plain query set, a plain
cohort, and one or more captured envelopes, then emits a comparable evidence panel: cohort own-page
hits, third-party mentions, AI Overview ranked-brand/reference hits, and the off-cohort character of
each query surface.

This is deliberately not a market-share or traction estimator. It answers the narrower, reusable
question: "Is this buyer-intent SERP worth tracking for this cohort, and what evidence did it show?"

Examples:

    python3 tools/serp_intent_panel.py --queries queries.json --cohort cohort.json --captures captures/
    python3 tools/serp_intent_panel.py --queries queries.json --cohort cohort.json --captures captures/ --format markdown
    python3 tools/serp_intent_panel.py --queries queries.json --cohort cohort.json --captures captures/ --fetch-missing

Live SerpAPI calls only happen with `--fetch-missing`. Without that flag, missing captures are
reported as missing panel rows so fixture and repeat runs never spend API credits by surprise.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from _match import CohortMatcher, TextMode, domain_from_url, normalize_domain

ORGANIC_LIMIT = 10
TOOL_NAME = "serp_intent_panel"

LISTICLE_DOMAINS = (
    "capterra.com",
    "forbes.com",
    "g2.com",
    "goodrx.com",
    "healthline.com",
    "medicalnewstoday.com",
    "nerdwallet.com",
    "pcmag.com",
    "softwareadvice.com",
    "usnews.com",
    "verywellhealth.com",
    "webmd.com",
    "wirecutter.com",
)
LOCAL_DOMAINS = (
    "google.com",
    "maps.apple.com",
    "realself.com",
    "yelp.com",
    "zocdoc.com",
)
RETAIL_DOMAINS = (
    "amazon.com",
    "cvs.com",
    "ebay.com",
    "etsy.com",
    "gnc.com",
    "iherb.com",
    "target.com",
    "walgreens.com",
    "walmart.com",
)
LISTICLE_TEXT = re.compile(r"\b(?:best|top|review|reviews|comparison|compare|versus|vs\.?|alternatives|ranked|guide)\b", re.IGNORECASE)
# Local intent should mean geography/in-person texture, not normal telehealth words like "doctor",
# "provider", or "clinic". Those terms are expected inside healthcare buyer-intent SERPs.
LOCAL_TEXT = re.compile(r"\b(?:near me|nearby|local|locations?|areas served|in-person|walk-?in|med spa|iv clinic)\b", re.IGNORECASE)
RETAIL_TEXT = re.compile(
    r"\b(?:amazon|capsules?|coupons?|discount|gummies|homekit|oral supplement|patch(?:es)?|retail|sale|shop|store|supplements?|vitamins?|walmart)\b",
    re.IGNORECASE,
)


def utc_now() -> str:
    """Panel generation time, not source-capture time."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json(path: str | None) -> Any:
    """JSON from `path`, or stdin when `path` is absent / '-'."""
    if not path or path == "-":
        return json.load(sys.stdin)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_query_set(path: str) -> list[dict[str, Any]]:
    """Plain query-set JSON: either a list or `{queries: [...], defaults?: {...}}`.

    Query entries may be strings or objects with at least `query`. Optional `id`, `category`, `gl`,
    `hl`, and `device` are preserved for output and live-fetch comparability.
    """
    raw = load_json(path)
    defaults: Mapping[str, Any] = {}
    if isinstance(raw, list):
        items = raw
    elif isinstance(raw, Mapping) and isinstance(raw.get("queries"), list):
        items = raw["queries"]
        if isinstance(raw.get("defaults"), Mapping):
            defaults = raw["defaults"]
    else:
        raise ValueError("query set JSON must be a list, or an object with a list at 'queries'")

    records = []
    for index, item in enumerate(items, start=1):
        if isinstance(item, str):
            query = item.strip()
            if not query:
                raise ValueError(f"query entry {index} is blank")
            record = {"id": slugify(query), "query": query}
        elif isinstance(item, Mapping):
            query = string_or_none(item.get("query"))
            if query is None:
                raise ValueError(f"query entry {index} must include a non-empty 'query'")
            record = dict(item)
            record["query"] = query
            record["id"] = string_or_none(record.get("id")) or slugify(query)
        else:
            raise ValueError(f"query entry {index} must be a string or object")

        for key, fallback in (("gl", "us"), ("hl", "en"), ("device", "desktop")):
            record[key] = string_or_none(record.get(key)) or string_or_none(defaults.get(key)) or fallback
        records.append(record)
    return records


def load_cohort(path: str) -> list[Mapping[str, Any]]:
    """Plain cohort JSON accepted by `_match.py`: list or `{cohort|brands: [...]}` wrapper."""
    raw = load_json(path)
    if isinstance(raw, list):
        cohort = raw
    elif isinstance(raw, Mapping) and isinstance(raw.get("cohort"), list):
        cohort = raw["cohort"]
    elif isinstance(raw, Mapping) and isinstance(raw.get("brands"), list):
        cohort = raw["brands"]
    else:
        raise ValueError("cohort JSON must be a list, or an object with a list at 'cohort' or 'brands'")
    if not all(isinstance(member, Mapping) for member in cohort):
        raise ValueError("cohort entries must be objects")
    return cohort


def load_capture_index(paths: Sequence[str]) -> dict[str, list[dict[str, Any]]]:
    """Captured `serpapi.py` envelopes keyed by normalized input query.

    Directories are scanned recursively for `.json`; non-SerpAPI JSON files are ignored so a fixture
    directory can hold queries, cohort, and captures side by side.
    """
    index: dict[str, list[dict[str, Any]]] = {}
    for path_text in paths:
        path = Path(path_text)
        candidates = sorted(path.rglob("*.json")) if path.is_dir() else [path]
        for candidate in candidates:
            raw = load_json(str(candidate))
            for envelope in iter_serpapi_envelopes(raw):
                query = envelope_query(envelope)
                if query is None:
                    raise ValueError(f"SerpAPI envelope missing input.query: {candidate}")
                envelope = dict(envelope)
                envelope["_capture_path"] = str(candidate)
                index.setdefault(query_key(query), []).append(envelope)

    for captures in index.values():
        captures.sort(key=lambda item: string_or_none(item.get("captured_at")) or "")
    return index


def iter_serpapi_envelopes(raw: Any) -> list[Mapping[str, Any]]:
    """SerpAPI envelopes from a bare object, a list, or a simple combined-captures object."""
    if isinstance(raw, Mapping) and raw.get("tool") == "serpapi":
        return [raw]
    if isinstance(raw, list):
        return [item for item in raw if isinstance(item, Mapping) and item.get("tool") == "serpapi"]
    if isinstance(raw, Mapping) and isinstance(raw.get("captures"), list):
        return [item for item in raw["captures"] if isinstance(item, Mapping) and item.get("tool") == "serpapi"]
    return []


def build_panel(
    queries: Sequence[Mapping[str, Any]],
    cohort: Sequence[Mapping[str, Any]],
    capture_index: Mapping[str, Sequence[Mapping[str, Any]]],
    *,
    fetch_missing: bool = False,
    organic_only: bool = False,
    text_mode: TextMode = "cohort_context",
    write_fetched_captures: str | None = None,
) -> dict[str, Any]:
    """Query set + cohort + captures -> comparable evidence panel."""
    matcher = CohortMatcher(cohort)
    query_rows = []
    fetched_captures = []

    for query_record in queries:
        query = required_string(query_record, "query")
        captures = list(capture_index.get(query_key(query), ()))
        capture = dict(captures[-1]) if captures else None
        capture_status = "captured" if capture else "missing"

        if capture is None and fetch_missing:
            capture = fetch_serpapi_capture(query_record, organic_only=organic_only)
            capture_status = "fetched_live"
            fetched_captures.append(capture)
            if write_fetched_captures:
                write_capture(capture, write_fetched_captures, required_string(query_record, "id"))

        if capture is None:
            query_rows.append(missing_query_row(query_record))
            continue

        query_rows.append(analyze_query(query_record, capture, matcher, capture_status=capture_status, text_mode=text_mode))

    summary = summarize_panel(query_rows)
    return {
        "tool": TOOL_NAME,
        "source": "serpapi_envelopes",
        "generated_at": utc_now(),
        "ok": summary["missing_query_count"] == 0 and summary["schema_drift_query_count"] == 0,
        "input": {
            "query_count": len(queries),
            "cohort_count": len(cohort),
            "fetch_missing": fetch_missing,
            "organic_only_for_live_fetch": organic_only,
            "fetched_live_count": len(fetched_captures),
        },
        "summary": summary,
        "queries": query_rows,
        "notes": [
            "Measures buyer-intent SERP visibility for a cohort; does not measure demand, spend, conversion, market share, or traction.",
            "Capture provenance remains in each query row; repeat panels should compare like-for-like query, gl, hl, device, and capture source.",
        ],
    }


def analyze_query(
    query_record: Mapping[str, Any],
    capture: Mapping[str, Any],
    matcher: CohortMatcher,
    *,
    capture_status: str,
    text_mode: TextMode,
) -> dict[str, Any]:
    """One SerpAPI envelope -> one compact query evidence row."""
    organic_results = organic_top10(capture)
    organic_matches = organic_match_entries(organic_results, matcher, text_mode=text_mode)
    own_page_matches = [match for match in organic_matches if match["kind"] == "own_page"]
    third_party_mentions = [match for match in organic_matches if match["kind"] == "mention"]
    ranked_brand_matches = ranked_brand_match_entries(capture, matcher, text_mode=text_mode)
    reference_matches = reference_match_entries(capture, matcher, text_mode=text_mode)
    matched_positions = {match["position"] for match in organic_matches}
    character = serp_character(organic_results, matched_positions)
    labels = usefulness_labels(
        organic_match_count=len(organic_matches),
        own_page_count=len(own_page_matches),
        ranked_brand_count=len(ranked_brand_matches),
        reference_count=len(reference_matches),
        character=character,
    )

    return {
        "id": query_record.get("id"),
        "category": query_record.get("category"),
        "query": required_string(query_record, "query"),
        "capture_status": capture_status,
        "capture": {
            "captured_at": capture.get("captured_at"),
            "path": capture.get("_capture_path"),
            "ok": capture.get("ok"),
            "schema_drift": capture.get("schema_drift") or [],
            "input": capture.get("input"),
        },
        "organic_top10_match_count": len(organic_matches),
        "organic_matched_result_count": len(matched_positions),
        "organic_distinct_cohort_count": len({match["slug"] for match in organic_matches}),
        "own_page_matches": own_page_matches,
        "third_party_mention_matches": third_party_mentions,
        "ai_overview": {
            "present": bool(capture.get("ai_overview_present")),
            "skipped": bool(capture.get("ai_overview_skipped")),
            "ranked_brand_match_count": len(ranked_brand_matches),
            "ranked_brand_matches": ranked_brand_matches,
            "reference_match_count": len(reference_matches),
            "reference_matches": reference_matches,
        },
        "serp_character": character,
        "query_usefulness_labels": labels,
    }


def organic_match_entries(
    organic_results: Sequence[Mapping[str, Any]],
    matcher: CohortMatcher,
    *,
    text_mode: TextMode,
) -> list[dict[str, Any]]:
    """Organic top-10 matches with SERP row provenance kept beside each match."""
    out = []
    for index, item in enumerate(organic_results):
        position = result_position(item, index)
        text = join_text(item.get("title"), item.get("snippet"))
        url = string_or_none(item.get("link"))
        matches = matcher.match_record(
            url=url,
            text=text,
            where={"payload": "organic_results", "index": index, "position": position},
            text_mode=text_mode,
        )
        for match in matches:
            out.append(
                {
                    "slug": match["slug"],
                    "kind": match["kind"],
                    "match_method": match["match_method"],
                    "position": position,
                    "title": item.get("title"),
                    "link": item.get("link"),
                    "domain": match.get("domain") or domain_from_url(url),
                    "matched_text": (match.get("text_hit") or {}).get("text"),
                }
            )
    return out


def ranked_brand_match_entries(capture: Mapping[str, Any], matcher: CohortMatcher, *, text_mode: TextMode) -> list[dict[str, Any]]:
    """AI Overview ranked-brand text matches, when SerpAPI captured that payload."""
    out = []
    for index, item in enumerate(iter_dicts(capture.get("ranked_brands"))):
        text = join_text(item.get("raw_snippet"), item.get("after_colon"))
        matches = matcher.match_record(
            text=text,
            where={"payload": "ranked_brands", "index": index, "position": item.get("position")},
            text_mode=text_mode,
        )
        for match in matches:
            out.append(
                {
                    "slug": match["slug"],
                    "aio_position": item.get("position"),
                    "label": item.get("label"),
                    "format": item.get("format"),
                    "raw_snippet": item.get("raw_snippet"),
                    "matched_text": (match.get("text_hit") or {}).get("text"),
                }
            )
    return out


def reference_match_entries(capture: Mapping[str, Any], matcher: CohortMatcher, *, text_mode: TextMode) -> list[dict[str, Any]]:
    """AI Overview citation/reference matches, separate from parser-recognized ranked-brand lists."""
    out = []
    for index, item in enumerate(iter_dicts(capture.get("references"))):
        text = join_text(item.get("source"), item.get("title"))
        url = string_or_none(item.get("link"))
        matches = matcher.match_record(
            url=url,
            text=text,
            where={"payload": "references", "index": index, "reference_index": item.get("index")},
            text_mode=text_mode,
        )
        for match in matches:
            out.append(
                {
                    "slug": match["slug"],
                    "kind": match["kind"],
                    "match_method": match["match_method"],
                    "reference_index": item.get("index"),
                    "source": item.get("source"),
                    "title": item.get("title"),
                    "link": item.get("link"),
                    "domain": match.get("domain") or domain_from_url(url),
                    "matched_text": (match.get("text_hit") or {}).get("text"),
                }
            )
    return out


def serp_character(organic_results: Sequence[Mapping[str, Any]], matched_positions: set[int]) -> dict[str, Any]:
    """Mechanical off-cohort shape: enough to compare query surfaces without judging traction."""
    type_counts: Counter[str] = Counter()
    matched_type_counts: Counter[str] = Counter()
    unmatched_type_counts: Counter[str] = Counter()
    unmatched_domains: Counter[str] = Counter()
    unmatched_samples = []

    for index, item in enumerate(organic_results):
        position = result_position(item, index)
        labels = classify_organic_result(item)
        type_counts.update(labels)
        if position in matched_positions:
            matched_type_counts.update(labels)
            continue
        unmatched_type_counts.update(labels)
        domain = result_domain(item)
        if domain:
            unmatched_domains[domain] += 1
        unmatched_samples.append(
            {
                "position": position,
                "title": item.get("title"),
                "link": item.get("link"),
                "domain": domain,
                "result_character": labels,
            }
        )

    total = len(organic_results)
    unmatched_count = len(unmatched_samples)
    if unmatched_count:
        type_counts["off_cohort"] = unmatched_count
    return {
        "organic_result_count": total,
        "unmatched_result_count": unmatched_count,
        "type_counts": dict(sorted(type_counts.items())),
        "matched_type_counts": dict(sorted(matched_type_counts.items())),
        "unmatched_type_counts": dict(sorted(unmatched_type_counts.items())),
        "top_unmatched_domains": [{"domain": domain, "count": count} for domain, count in unmatched_domains.most_common(8)],
        "sample_unmatched_results": unmatched_samples[:5],
    }


def classify_organic_result(item: Mapping[str, Any]) -> list[str]:
    """Small heuristics for SERP texture; generic and intentionally non-authoritative."""
    labels = []
    domain = result_domain(item)
    text = join_text(item.get("title"), item.get("snippet"), item.get("displayed_link"), item.get("link")) or ""
    if domain_matches(domain, LISTICLE_DOMAINS) or LISTICLE_TEXT.search(text):
        labels.append("listicle_like")
    if domain_matches(domain, LOCAL_DOMAINS) or LOCAL_TEXT.search(text):
        labels.append("local_clinic_like")
    if domain_matches(domain, RETAIL_DOMAINS) or RETAIL_TEXT.search(text):
        labels.append("supplement_retail_like")
    return labels or ["unclassified"]


def usefulness_labels(
    *,
    organic_match_count: int,
    own_page_count: int,
    ranked_brand_count: int,
    reference_count: int,
    character: Mapping[str, Any],
) -> list[str]:
    """Comparable query labels that say whether the SERP is worth tracking, not who is winning."""
    labels = []
    counts = character.get("unmatched_type_counts") if isinstance(character.get("unmatched_type_counts"), Mapping) else {}
    listicle_count = int(counts.get("listicle_like", 0))
    local_count = int(counts.get("local_clinic_like", 0))
    retail_count = int(counts.get("supplement_retail_like", 0))
    off_cohort_count = int(character.get("unmatched_result_count", 0))
    total_signal = organic_match_count + ranked_brand_count + reference_count

    if total_signal == 0:
        labels.append("no cohort signal")
    if listicle_count >= 3:
        labels.append("listicle-heavy")
    if local_count >= 3:
        labels.append("local-clinic-heavy")
    if retail_count >= 3:
        labels.append("supplement/retail drift")
    if off_cohort_count >= 8 and organic_match_count <= 1:
        labels.append("noisy")
    elif off_cohort_count >= 7 and organic_match_count <= 3:
        labels.append("noisy")
    elif listicle_count + local_count + retail_count >= 5:
        labels.append("noisy")
    if total_signal > 0 and own_page_count > 0 and off_cohort_count <= 5 and not labels:
        labels.append("clean")
    return labels or ["noisy"]


def missing_query_row(query_record: Mapping[str, Any]) -> dict[str, Any]:
    """A missing capture is explicit evidence about the run, not silently dropped input."""
    return {
        "id": query_record.get("id"),
        "category": query_record.get("category"),
        "query": required_string(query_record, "query"),
        "capture_status": "missing",
        "capture": None,
        "organic_top10_match_count": 0,
        "organic_matched_result_count": 0,
        "organic_distinct_cohort_count": 0,
        "own_page_matches": [],
        "third_party_mention_matches": [],
        "ai_overview": {
            "present": False,
            "skipped": False,
            "ranked_brand_match_count": 0,
            "ranked_brand_matches": [],
            "reference_match_count": 0,
            "reference_matches": [],
        },
        "serp_character": {
            "organic_result_count": 0,
            "unmatched_result_count": 0,
            "type_counts": {},
            "top_unmatched_domains": [],
            "sample_unmatched_results": [],
        },
        "query_usefulness_labels": ["no_capture"],
    }


def summarize_panel(rows: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    """Small run-level counts; keep conclusions project-side."""
    labels = Counter(label for row in rows for label in row.get("query_usefulness_labels", []))
    return {
        "query_count": len(rows),
        "captured_query_count": sum(1 for row in rows if row.get("capture_status") != "missing"),
        "missing_query_count": sum(1 for row in rows if row.get("capture_status") == "missing"),
        "schema_drift_query_count": sum(1 for row in rows if ((row.get("capture") or {}).get("schema_drift") or [])),
        "clean_query_count": labels.get("clean", 0),
        "no_cohort_signal_query_count": labels.get("no cohort signal", 0),
        "noisy_query_count": labels.get("noisy", 0),
    }


def render_markdown(panel: Mapping[str, Any]) -> str:
    """Markdown evidence panel for humans; JSON remains the lossless output."""
    lines = [
        "# SERP Intent Panel",
        "",
        f"Generated: `{panel.get('generated_at')}`",
        "",
        "Measures buyer-intent SERP visibility for a cohort. It does not measure demand, spend, conversion, market share, or traction.",
        "",
        "| Query | Organic matches | Own pages | Mentions | AIO ranked | AIO refs | Labels |",
        "|---|---:|---|---|---:|---:|---|",
    ]
    for row in iter_dicts(panel.get("queries")):
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row.get('query')}`",
                    str(row.get("organic_top10_match_count", 0)),
                    markdown_match_list(row.get("own_page_matches")),
                    markdown_match_list(row.get("third_party_mention_matches")),
                    str((row.get("ai_overview") or {}).get("ranked_brand_match_count", 0)),
                    str((row.get("ai_overview") or {}).get("reference_match_count", 0)),
                    ", ".join(row.get("query_usefulness_labels", [])),
                ]
            )
            + " |"
        )

    for row in iter_dicts(panel.get("queries")):
        lines.extend(
            [
                "",
                f"## {row.get('query')}",
                "",
                f"- Capture: `{row.get('capture_status')}`"
                + capture_suffix(row.get("capture") if isinstance(row.get("capture"), Mapping) else None),
                f"- Own-page matches: {markdown_match_list(row.get('own_page_matches'))}",
                f"- Third-party mentions: {markdown_match_list(row.get('third_party_mention_matches'))}",
                f"- AIO ranked-brand matches: {markdown_ranked_list((row.get('ai_overview') or {}).get('ranked_brand_matches'))}",
                f"- AIO reference matches: {markdown_reference_list((row.get('ai_overview') or {}).get('reference_matches'))}",
                f"- Off-cohort: {markdown_character(row.get('serp_character') if isinstance(row.get('serp_character'), Mapping) else {})}",
                f"- Labels: {', '.join(row.get('query_usefulness_labels', []))}",
            ]
        )
    return "\n".join(lines) + "\n"


def markdown_match_list(value: Any) -> str:
    """Compact slug@position list for table cells and bullets."""
    matches = iter_dicts(value)
    if not matches:
        return "none"
    return ", ".join(f"{match.get('slug')}@{match.get('position')}" for match in matches)


def markdown_ranked_list(value: Any) -> str:
    """Compact slug@AIO-position list."""
    matches = iter_dicts(value)
    if not matches:
        return "none"
    return ", ".join(f"{match.get('slug')}@{match.get('aio_position')}" for match in matches)


def markdown_reference_list(value: Any) -> str:
    """Compact slug@reference-index list."""
    matches = iter_dicts(value)
    if not matches:
        return "none"
    return ", ".join(f"{match.get('slug')}@ref{match.get('reference_index')}" for match in matches)


def markdown_character(character: Mapping[str, Any]) -> str:
    """One-line off-cohort texture for markdown."""
    counts = character.get("unmatched_type_counts") if isinstance(character.get("unmatched_type_counts"), Mapping) else {}
    if not counts:
        return "not captured"
    parts = [f"off_cohort={character.get('unmatched_result_count', 0)}"]
    parts.extend(f"{key}={value}" for key, value in sorted(counts.items()))
    return ", ".join(parts)


def capture_suffix(capture: Mapping[str, Any] | None) -> str:
    """Capture provenance phrase for markdown."""
    if not capture:
        return ""
    parts = []
    if capture.get("captured_at"):
        parts.append(f"captured_at `{capture.get('captured_at')}`")
    if capture.get("path"):
        parts.append(f"path `{capture.get('path')}`")
    return f" ({'; '.join(parts)})" if parts else ""


def fetch_serpapi_capture(query_record: Mapping[str, Any], *, organic_only: bool) -> dict[str, Any]:
    """Run the existing SerpAPI parser only when the caller explicitly opts into live capture."""
    from serpapi import fetch_and_parse

    return fetch_and_parse(
        required_string(query_record, "query"),
        organic_only=organic_only,
        gl=required_string(query_record, "gl"),
        hl=required_string(query_record, "hl"),
        device=required_string(query_record, "device"),
    )


def write_capture(capture: Mapping[str, Any], directory: str, query_id: str) -> None:
    """Optional cache write for live-fetched missing captures; never used for fixture-only runs."""
    target_dir = Path(directory)
    target_dir.mkdir(parents=True, exist_ok=True)
    captured_at = string_or_none(capture.get("captured_at")) or utc_now()
    filename = f"{captured_at.replace(':', '').replace('-', '')}-{slugify(query_id)}.json"
    with open(target_dir / filename, "w", encoding="utf-8") as f:
        json.dump(capture, f, indent=2)
        f.write("\n")


def organic_top10(capture: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    """Organic rows from the capture, pinned to the first Google page."""
    return iter_dicts(capture.get("organic_results"))[:ORGANIC_LIMIT]


def result_position(item: Mapping[str, Any], index: int) -> int:
    """Stable organic position even when a fixture omits `position`."""
    value = item.get("position")
    if isinstance(value, int):
        return value
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return index + 1


def result_domain(item: Mapping[str, Any]) -> str | None:
    """Best-effort domain for organic character counts."""
    return domain_from_url(string_or_none(item.get("link"))) or normalize_domain(string_or_none(item.get("displayed_link")))


def domain_matches(domain: str | None, candidates: Sequence[str]) -> bool:
    """Exact or subdomain match against a small heuristic domain list."""
    normalized = normalize_domain(domain)
    if not normalized:
        return False
    return any(normalized == candidate or normalized.endswith(f".{candidate}") for candidate in candidates)


def envelope_query(envelope: Mapping[str, Any]) -> str | None:
    """SerpAPI input query from the shared envelope."""
    raw_input = envelope.get("input")
    if not isinstance(raw_input, Mapping):
        return None
    return string_or_none(raw_input.get("query"))


def query_key(query: str) -> str:
    """Case/whitespace-insensitive lookup key; no fuzzy query matching."""
    return " ".join(query.strip().lower().split())


def slugify(value: str) -> str:
    """Filesystem-safe-ish identifier for query IDs and optional capture writes."""
    return re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-") or "query"


def join_text(*parts: Any) -> str | None:
    """SERP title/snippet text for matching and classification."""
    clean = [str(part).strip() for part in parts if part is not None and str(part).strip()]
    return "\n".join(clean) if clean else None


def string_or_none(value: Any) -> str | None:
    """Non-empty string or `None`."""
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def required_string(value: Mapping[str, Any], key: str) -> str:
    """Required non-empty string field from a mapping."""
    text = string_or_none(value.get(key))
    if text is None:
        raise ValueError(f"missing required {key!r}: {value!r}")
    return text


def iter_dicts(value: Any) -> list[Mapping[str, Any]]:
    """List members that are objects."""
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def parse_args() -> argparse.Namespace:
    """CLI parser kept small: captured envelopes first, live capture behind one explicit flag."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--queries", required=True, help="Query-set JSON: list or `{queries: [...]}`")
    parser.add_argument("--cohort", required=True, help="Cohort JSON: list or `{cohort|brands: [...]}`")
    parser.add_argument("--captures", nargs="*", default=[], help="Captured serpapi.py JSON files or directories")
    parser.add_argument("--format", choices=["json", "markdown"], default="json", help="Output format (default: json)")
    parser.add_argument("--fetch-missing", action="store_true", help="Run serpapi.py's parser for missing captures; makes live API calls")
    parser.add_argument("--organic-only", action="store_true", help="Use organic-only mode for live missing captures")
    parser.add_argument("--write-fetched-captures", help="Directory to write live-fetched missing capture envelopes")
    parser.add_argument(
        "--text-mode",
        choices=["cohort_context", "open_text"],
        default="cohort_context",
        help="Text matching mode for title/snippet and ranked-brand text (default: cohort_context)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        queries = load_query_set(args.queries)
        cohort = load_cohort(args.cohort)
        captures = load_capture_index(args.captures)
        panel = build_panel(
            queries,
            cohort,
            captures,
            fetch_missing=args.fetch_missing,
            organic_only=args.organic_only,
            text_mode=args.text_mode,
            write_fetched_captures=args.write_fetched_captures,
        )
    except Exception as e:
        sys.stderr.write(f"{TOOL_NAME}: {e}\n")
        sys.exit(2)

    if args.format == "markdown":
        print(render_markdown(panel), end="")
    else:
        print(json.dumps(panel, indent=2))

    if not panel.get("ok"):
        sys.exit(1)


if __name__ == "__main__":
    main()
