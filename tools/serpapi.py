#!/usr/bin/env python3
"""SerpAPI Google fetcher + parser — captures AI Overview AND organic search, nothing else.

Scope is deliberately narrow: Google `engine=google` organic results + the AI Overview
block. SerpAPI does far more (News, Shopping, Maps/Local, Scholar, Trends, …) — see
serpapi.md for what a later extension would add. This tool is `engine=google` only.

Two-call pipeline (only the first call is needed for --organic-only):
  1. engine=google&q=<query>             -> SERP: organic_results AND ai_overview.page_token (if AIO rendered)
  2. engine=google_ai_overview&page_token=<token>  -> AIO text_blocks + references (skipped if no AIO / --organic-only)

The two signals have different stability profiles — capture both, diff independently:
  - AI Overview: LLM-synthesized, drifts week-to-week / hour-to-hour (sub-corpus rotation).
  - Organic search: SEO-mediated editorial corpus, far more stable; ranks shift on a slower clock.
  When AIO names a brand and organic doesn't, that disagreement IS the AIO-instability tell.

Generic on purpose: emits clean parsed JSON to stdout, no cohort / Notion / vertical baked in.
A caller that wants brand-matching runs it over this output — matching is not this tool's job.

CLI:
  python3 tools/serpapi.py "best NAD provider 2026"
  python3 tools/serpapi.py "best NAD provider 2026" --organic-only
  python3 tools/serpapi.py "compounded tirzepatide online" --gl us --hl en --device desktop

Exit codes:
  0  clean capture
  2  fetch error (network, auth, etc.)
  3  schema drift detected (parser is version-pinned — stop the run; never silently parse-on)

Auth: SERP_API_KEY from env, falling back to a `.env` at the repo root (gitignored).

Pinned parser version: v2 — bump only on an intentional schema migration, never to paper over drift.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

from _env import load_key


def _utc_now() -> str:
    """This invocation's capture time, UTC ISO 8601 — the envelope's `captured_at`.

    Wall-clock of *when we captured*, never a source-reported date (this tool surfaces none,
    but the library rule is uniform: source dates live inside payload items, not the envelope).
    """
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


PARSER_VERSION = "v2"
API_KEY_VAR = "SERP_API_KEY"
SERPAPI_BASE = "https://serpapi.com/search.json"
USER_AGENT = "web-research-tools/serpapi"
ORGANIC_RESULTS_LIMIT = 10  # full first SERP page; standard convention


def _http_get_json(url: str, timeout: int = 30) -> dict[str, Any]:
    """Stdlib urllib GET -> parsed JSON. No `requests` dep — the HTTP layer every tool here copies.
    Transport/HTTP errors (urlopen raises HTTPError on 4xx/5xx) bubble to main()'s exit-2 handler."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def fetch_google_search(query: str, api_key: str, gl: str = "us", hl: str = "en", device: str = "desktop") -> dict[str, Any]:
    """First call: engine=google. Returns the full SERP response."""
    params = {"engine": "google", "q": query, "api_key": api_key, "gl": gl, "hl": hl, "device": device}
    return _http_get_json(f"{SERPAPI_BASE}?{urllib.parse.urlencode(params)}")


def fetch_ai_overview(page_token: str, api_key: str) -> dict[str, Any]:
    """Second call: engine=google_ai_overview. Returns the AIO body."""
    params = {"engine": "google_ai_overview", "page_token": page_token, "api_key": api_key}
    return _http_get_json(f"{SERPAPI_BASE}?{urllib.parse.urlencode(params)}")


def validate_aio_shape_v2(aio: dict[str, Any]) -> list[str]:
    """Schema-drift complaints against the pinned v2 AIO shape — empty list means OK.

    Google has shifted the AI surface ~3 times in the past year; surface-area drift is this
    capture's highest-impact failure mode. We pin to a known shape and fail loud rather than
    parse a changed structure into plausible-but-wrong output.
    """
    issues = []
    if not isinstance(aio, dict):
        return [f"ai_overview is not a dict (got {type(aio).__name__})"]
    if "text_blocks" not in aio:
        issues.append("ai_overview missing 'text_blocks'")
    elif not isinstance(aio["text_blocks"], list):
        issues.append("ai_overview.text_blocks is not a list")
    else:
        valid_types = {"paragraph", "heading", "list"}
        for i, block in enumerate(aio["text_blocks"]):
            if not isinstance(block, dict):
                issues.append(f"text_blocks[{i}] is not a dict")
                continue
            if "type" not in block:
                issues.append(f"text_blocks[{i}] missing 'type'")
                continue
            if block["type"] not in valid_types:
                issues.append(f"text_blocks[{i}].type='{block['type']}' not in {valid_types}")
    if "references" not in aio:
        issues.append("ai_overview missing 'references'")
    return issues


# Two AIO list-item formats observed live; a list item that fails BOTH is treated as
# considerations/noise and excluded:
#   1. "Labeled" — "Best for X: BrandName description". Label starts with one of
#      Best | Other | Recommended | Top. Considerations lists in the same AIO use category
#      labels (Lab Fees, Costs, Safety, …) which this prefix excludes.
#   2. "Bare"    — the list item is just the brand name, no colon. Discriminated by being
#      short (<60 chars), no colon, capital-letter start.
BRAND_LABEL_PREFIX = re.compile(r"^(best|other|recommended|top)\b", re.IGNORECASE)
BARE_BRAND_MAX_CHARS = 60


def classify_list_item(snippet: str) -> tuple[str | None, str | None, str]:
    """Return (label, after_colon, fmt) where fmt is one of {'labeled', 'bare', 'reject'}."""
    if ":" in snippet:
        label, after = snippet.split(":", 1)
        label, after = label.strip(), after.strip()
        if BRAND_LABEL_PREFIX.match(label):
            return label, after, "labeled"
        return label, after, "reject"
    if len(snippet) <= BARE_BRAND_MAX_CHARS and snippet[:1].isupper():
        return None, snippet.rstrip(" ."), "bare"
    return None, snippet, "reject"


def extract_ranked_brands(aio: dict[str, Any]) -> list[dict[str, Any]]:
    """Parse text_blocks list items into ranked brand entries.

    A single entry can name multiple brands ("Other Notable Options: Ways2Well, Hone, Javan")
    — this captures the raw snippet; splitting/matching individual brands is the caller's job.
    Each entry carries its `format` ('labeled'|'bare') so a downstream writer can tell a
    positioned pick from a bare name. Empty list = no brand-list block (genuinely possible —
    that's a signal, not a bug).
    """
    out = []
    pos = 0
    for block in aio.get("text_blocks", []):
        if block.get("type") != "list":
            continue
        for item in block.get("list", []):
            snippet = item.get("snippet", "").strip()
            if not snippet:
                continue
            label, after, fmt = classify_list_item(snippet)
            if fmt == "reject":
                continue
            pos += 1
            out.append(
                {
                    "position": pos,
                    "label": label,
                    "after_colon": after,
                    "raw_snippet": snippet,
                    "format": fmt,
                    "reference_indexes": block.get("reference_indexes", []),
                }
            )
    return out


def extract_narrative_paragraphs(aio: dict[str, Any]) -> list[str]:
    """Paragraph blocks — the prose 'Based on 2025/2026 data…' lead-in around the ranked list."""
    return [s for block in aio.get("text_blocks", []) if block.get("type") == "paragraph" and (s := block.get("snippet", "").strip())]


def extract_headings(aio: dict[str, Any]) -> list[str]:
    return [s for block in aio.get("text_blocks", []) if block.get("type") == "heading" and (s := block.get("snippet", "").strip())]


def fetch_and_parse(
    query: str,
    api_key: str | None = None,
    organic_only: bool = False,
    gl: str = "us",
    hl: str = "en",
    device: str = "desktop",
) -> dict[str, Any]:
    """Full pipeline: SERP -> organic_results (top-10) + (optionally) AIO body -> parsed dict.

    Always populates `organic_results` from the first call. The AIO body is the second call,
    skipped when `organic_only=True` or the SERP carried no AIO page_token.
    """
    api_key = api_key or load_key(API_KEY_VAR)
    serp = fetch_google_search(query, api_key=api_key, gl=gl, hl=hl, device=device)

    organic_results = [
        {
            "position": o.get("position"),
            "title": o.get("title"),
            "link": o.get("link"),
            "snippet": o.get("snippet"),
            "displayed_link": o.get("displayed_link"),
        }
        for o in serp.get("organic_results", [])[:ORGANIC_RESULTS_LIMIT]
    ]

    # Shared envelope (reserved top-level keys — same across every tool/ tool, so a caller reads
    # provenance + freshness identically) followed by serpapi's own payload fields beside it.
    result: dict[str, Any] = {
        "tool": "serpapi",  # which tool produced this blob when many land together
        "source": "serpapi.com",  # the external system actually hit (distinct from `tool`)
        "captured_at": _utc_now(),  # this invocation's wall-clock, UTC — not a source date
        "ok": True,  # coarse: did the capture complete cleanly? false -> see schema_drift
        "input": {"query": query, "gl": gl, "hl": hl, "device": device},
        "schema_drift": [],  # non-empty -> parsed fields suppressed, exit 3
        "parser_version": PARSER_VERSION,  # AIO shape is drift-prone, so it's version-pinned
        "cost": {"credits": 1},  # SerpAPI meters credits; bumped to 2 if the AIO call fires
        # --- payload ---
        "ai_overview_present": False,
        "ai_overview_skipped": organic_only,  # explicit so "absent" vs "skipped" stays distinguishable
        "ranked_brands": [],
        "narrative_paragraphs": [],
        "headings": [],
        "references": [],
        "organic_results": organic_results,
    }

    aio_block = serp.get("ai_overview") or {}
    page_token = aio_block.get("page_token")
    # Google sometimes returns the AIO body INLINE (text_blocks populated, no page_token)
    # instead of behind the follow-up call — same shape as the second-call response, so the
    # parsers work on it unchanged. SerpAPI docs only describe the page_token flow; this
    # branch catches the inline case (live-observed 2026-05-07).
    inline_aio = aio_block if aio_block.get("text_blocks") else None

    if organic_only or (not page_token and not inline_aio):
        # Explicitly skipped OR Google rendered no AIO. Either way organic carries the rank
        # signal — AIO-absent is data, never a reason to fall back to organic-as-AIO.
        return result

    if page_token:
        aio_resp = fetch_ai_overview(page_token, api_key=api_key)
        result["cost"]["credits"] = 2  # the second SerpAPI call fired (inline-AIO path stays at 1)
        aio = aio_resp.get("ai_overview", aio_resp)
        # Google sometimes declines to render the async body even after returning a page_token.
        # SerpAPI surfaces this as {"error": "Google hasn't returned any results for this query."}
        # on the second call — semantically identical to "no AIO", so treat it as
        # ai_overview_present=False, NOT schema drift (live-observed 2026-W21 on 6/7 categories).
        if isinstance(aio, dict) and "error" in aio and "text_blocks" not in aio:
            result["ai_overview_skipped"] = True
            result["ai_overview_unavailable_reason"] = aio["error"]
            return result
    else:
        aio = inline_aio

    drift = validate_aio_shape_v2(aio)
    if drift:
        # Fail loud, don't parse-on. A changed shape fed through the parsers yields
        # plausible-but-wrong ranked_brands/references — so suppress them and let `schema_drift`
        # carry the truth. This keeps `fetch_and_parse` honest for an importing caller, not just
        # the CLI (main() exits 3). `ai_overview_present` stays True: Google DID render one; we
        # just refuse to trust our parse of it. Bump PARSER_VERSION only on an intended migration.
        result["ai_overview_present"] = True
        result["ok"] = False  # capture didn't complete cleanly — the parse is suppressed
        result["schema_drift"] = drift
        sys.stderr.write(
            f"WARNING: ai_overview schema drift for query={query!r}: {drift}\n"
            f"Parser pinned to {PARSER_VERSION} — parsed fields suppressed; review the shape before bumping (exit 3).\n"
        )
        return result

    result["ai_overview_present"] = True
    result["ranked_brands"] = extract_ranked_brands(aio)
    result["narrative_paragraphs"] = extract_narrative_paragraphs(aio)
    result["headings"] = extract_headings(aio)
    result["references"] = [
        {"index": r.get("index"), "source": r.get("source"), "title": r.get("title"), "link": r.get("link")}
        for r in aio.get("references", [])
    ]
    return result


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("query", help="Search query (e.g. 'best NAD provider 2026')")
    p.add_argument(
        "--organic-only",
        action="store_true",
        help="Skip the AIO body fetch (1 SerpAPI credit instead of 2) — for backfill or known-unstable AIO.",
    )
    p.add_argument("--gl", default="us", help="Google country (default: us)")
    p.add_argument("--hl", default="en", help="Google UI language (default: en)")
    p.add_argument("--device", default="desktop", help="desktop | mobile | tablet (default: desktop)")
    args = p.parse_args()

    try:
        result = fetch_and_parse(args.query, organic_only=args.organic_only, gl=args.gl, hl=args.hl, device=args.device)
    except Exception as e:
        sys.stderr.write(f"Error fetching {args.query!r}: {e}\n")
        sys.exit(2)

    print(json.dumps(result, indent=2))

    if result.get("schema_drift"):
        sys.exit(3)


if __name__ == "__main__":
    main()
