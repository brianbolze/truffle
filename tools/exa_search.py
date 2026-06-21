#!/usr/bin/env python3
"""Exa /search — find companies/pages by a QUERY string, captured not judged.

Sibling to exa_similar.py (Exa /findSimilar). Pick by what you have:
  - a known company URL whose neighbors you want -> exa_similar.py
  - a DESCRIPTION of what you're looking for      -> this tool

Why both exist (probe-confirmed 2026-06-20): /findSimilar is anchor-NAME-bound — short/common brand
names return name-collisions, mirrors, and link-shorteners ("Honey Health" for "Hone Health"), and
its includeText/excludeText filters are silently ignored under a category, so it has no topic knob.
For topic / function / competitor discovery, /search with a description query + category=company
returns REAL companies. It is a DISCOVERY tool — strong for net-new long-tail players, but recall of
a *curated/known* set is low (a Hone-description search recovered 1/16 of a known neighbor set), so
corroborate downstream; it does not replace a cross-shop read. Full write-up:
experiments/2026-06-20-cohort-discovery/references/exa-api-capabilities-and-probes-2026-06-20.md.

Match-free + print-only like every tool/: ONE query per invocation, parsed JSON to stdout, no store
write, no cohort/Notion/vertical baked in. Matching results to a cohort and deciding where the
capture lands are the caller's job (_match.py, scripts/signals.py). Grain note: /search output is
QUERY/cohort-grain (a description, not a company), so it is NOT a company-keyed signal — like SERP
panels it usually lives in an experiment/cohort, not store/<domain>/signals/.

CLI:
  python3 tools/exa_search.py "telehealth TRT & hormone optimization clinic: labs, membership" --num-results 25
  python3 tools/exa_search.py "menopause / HRT telehealth brand" --category company
  python3 tools/exa_search.py "..." --include-domains a.com b.com           # restrict (honored with category)
  python3 tools/exa_search.py "..." --category "" --exclude-domains reddit.com  # excludeDomains only honored w/o category

Exit codes:
  0  clean capture (INCLUDING an empty result list — "Exa found nothing" is data, not failure)
  2  fetch error (network, auth, Exa HTTP error, or a response missing `results`)
  (no exit 3: Exa is a stable, documented JSON API — no version-pinned parser, so no schema-drift
   path. `schema_drift` is still emitted as `[]` for envelope uniformity across the library.)

Auth: EXA_API_KEY from env, falling back to a `.env` at the repo root (gitignored).

Load-bearing gotchas (full catalog in exa_search.md; shared Exa gotchas in exa_similar.md):
  - User-Agent MUST be curl/8.4.0 — the default urllib UA is Cloudflare-blocked at Exa's edge.
  - `type` defaults to `neural`; `auto` flips neural<->keyword between runs and breaks diff logic, so
    it is pinned. `score` is dropped (synthetic, ~rank-derived) — ordinal `rank` is the signal.
  - excludeDomains is unsupported when category is company/people (Exa silently drops it): we send it
    only when no category is set, and ALWAYS enforce it caller-side. includeDomains IS honored.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any

from _env import load_key

API_KEY_VAR = "EXA_API_KEY"
EXA_SEARCH = "https://api.exa.ai/search"
# INVARIANT: the default urllib UA is Cloudflare-blocked at Exa's edge — a 30-min debugging trap.
# Pin a curl UA (or use `requests`, which sets one). Carried from agent-workflows/INVARIANTS.
USER_AGENT = "curl/8.4.0"
DEFAULT_NUM_RESULTS = 10
DEFAULT_CATEGORY = "company"  # Exa-native filter; this tool is company discovery. Overridable ("" drops it).
DEFAULT_TYPE = "neural"  # pin neural — `type:auto` flips neural<->keyword between runs and breaks diffs.


def _utc_now() -> str:
    """This invocation's capture time, UTC ISO 8601 — the envelope's `captured_at` (when we captured,
    never a source date). Exa results carry a `publishedDate` (crawl date) which we drop, per the
    library rule that source dates, if surfaced, live inside payload items under their own names."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _http_post_json(url: str, body: dict[str, Any], api_key: str, timeout: int = 60) -> dict[str, Any]:
    """Stdlib urllib POST -> parsed JSON. No `requests` dep — the HTTP layer the tools/ library copies.
    Transport/HTTP errors (urlopen raises HTTPError on 4xx/5xx) bubble to main()'s exit-2 handler."""
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "User-Agent": USER_AGENT,  # see USER_AGENT note — non-negotiable
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def _domain_of(url: str) -> str | None:
    """Bare host of a result URL ('https://www.roon.com/x' -> 'roon.com'), a convenience field.
    Lowercased, `www.` stripped — and that's ALL. Folding api./en./i18n mirrors to an apex, and
    deduping across queries, is caller logic (the discovery orchestrator's), kept out on purpose."""
    host = urllib.parse.urlsplit(url).netloc.lower()
    host = host.split("@")[-1].split(":")[0]  # drop any userinfo / port
    if host.startswith("www."):
        host = host[4:]
    return host or None


def _excluded_hosts(exclude_domains: list[str]) -> set[str]:
    """Normalize a caller exclude list (bare domains or full URLs) to comparable bare hosts, so the
    caller-side filter below works whether Exa honored excludeDomains or silently dropped it."""
    return {_domain_of(d if "://" in d else f"https://{d}") for d in exclude_domains if d}


def search(
    query: str,
    api_key: str | None = None,
    num_results: int = DEFAULT_NUM_RESULTS,
    search_type: str = DEFAULT_TYPE,
    category: str = DEFAULT_CATEGORY,
    include_domains: list[str] | None = None,
    exclude_domains: list[str] | None = None,
    include_text: str | None = None,
    exclude_text: str | None = None,
) -> dict[str, Any]:
    """Full pipeline: POST /search for one query -> the shared envelope + a ranked `results` list.

    `category=""` drops Exa's company filter (aggregators/news leak in). `exclude_domains` is enforced
    CALLER-SIDE because Exa silently drops `excludeDomains` under a company/people category (we still
    send it to the API when no category is set, where it's honored) — so `result_count` can come back
    below `num_results` when excluded hosts are removed. `include_domains` is honored as-is.
    """
    api_key = api_key or load_key(API_KEY_VAR)
    include_domains = include_domains or []
    exclude_domains = exclude_domains or []

    body: dict[str, Any] = {"query": query, "numResults": num_results, "type": search_type}
    if category:  # falsy (e.g. --category "") => unfiltered sweep
        body["category"] = category
    if include_domains:
        body["includeDomains"] = include_domains
    # Only send excludeDomains where Exa honors it (no category); the caller-side filter below is the
    # real enforcement (Exa silently ignores it under a company/people category).
    if exclude_domains and not category:
        body["excludeDomains"] = exclude_domains
    if include_text:  # Exa wants a list of strings (a short phrase); honored on /search, unlike findSimilar
        body["includeText"] = [include_text]
    if exclude_text:
        body["excludeText"] = [exclude_text]

    resp = _http_post_json(EXA_SEARCH, body, api_key=api_key)
    if "results" not in resp:
        # Not drift (Exa is stable); an unexpected body — surface it loud as a transport-class failure.
        raise RuntimeError(f"Exa response missing 'results' (got keys {list(resp.keys())}): {str(resp)[:300]}")

    excluded = _excluded_hosts(exclude_domains)
    kept = [r for r in resp.get("results", []) if _domain_of(r.get("url") or "") not in excluded]
    results = [
        {
            "rank": i,  # ordinal — the ONLY relevance signal we trust (Exa's score is synthetic; dropped)
            "title": r.get("title"),
            "url": r.get("url"),
            "domain": _domain_of(r.get("url") or ""),
        }
        for i, r in enumerate(kept, start=1)
    ]

    cost_total = (resp.get("costDollars") or {}).get("total")
    return {
        # --- the reserved envelope spine (tools/README.md), identical across the library ---
        "tool": "exa_search",  # = source_type; sibling to exa_similar (different endpoint, different grain)
        "source": "exa.ai",  # the external system hit (via api.exa.ai/search)
        "captured_at": _utc_now(),  # THIS invocation's wall-clock, UTC — not a source date
        "ok": True,  # transport failures never reach here (exit 2); Exa has no drift path
        "input": {
            "query": query,
            "num_results": num_results,
            "type": search_type,
            "category": category or None,
            "include_domains": include_domains,
            "exclude_domains": exclude_domains,
            "include_text": include_text,
            "exclude_text": exclude_text,
        },
        "schema_drift": [],  # always empty — stable API, no version-pinned parser (kept for uniformity)
        "cost": {"usd": cost_total},  # Exa meters in dollars (costDollars.total)
        # --- payload, beside the spine (never nested under a generic `data`) ---
        "results": results,
        "result_count": len(results),
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("query", help="Natural-language description of what to find (a cohort/company description)")
    p.add_argument(
        "--num-results",
        type=int,
        default=DEFAULT_NUM_RESULTS,
        help=f"How many results to request (default: {DEFAULT_NUM_RESULTS})",
    )
    p.add_argument(
        "--type",
        default=DEFAULT_TYPE,
        choices=["neural", "keyword", "auto", "fast"],
        help=f"Search mode (default: {DEFAULT_TYPE!r}; avoid 'auto' — it flips between runs and breaks diffs)",
    )
    p.add_argument(
        "--category",
        default=DEFAULT_CATEGORY,
        help=f"Exa result category filter (default: {DEFAULT_CATEGORY!r}; pass --category '' to drop it)",
    )
    p.add_argument(
        "--include-domains",
        nargs="*",
        default=[],
        metavar="DOMAIN",
        help="Restrict results to these domains (honored even with a category)",
    )
    p.add_argument(
        "--exclude-domains",
        nargs="*",
        default=[],
        metavar="DOMAIN",
        help="Drop these domains; enforced caller-side (Exa silently ignores the param under a category)",
    )
    p.add_argument("--include-text", help="Require this short phrase in result page text (Exa: a few words)")
    p.add_argument("--exclude-text", help="Exclude results whose page text contains this short phrase")
    args = p.parse_args()

    try:
        result = search(
            args.query,
            num_results=args.num_results,
            search_type=args.type,
            category=args.category,
            include_domains=args.include_domains,
            exclude_domains=args.exclude_domains,
            include_text=args.include_text,
            exclude_text=args.exclude_text,
        )
    except Exception as e:
        sys.stderr.write(f"Error searching for {args.query!r}: {e}\n")
        sys.exit(2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
