#!/usr/bin/env python3
"""Exa /findSimilar — neighbor/company discovery for ONE anchor, captured not judged.

Give it a company URL or domain; it asks Exa "what pages are most similar to this one" and
emits a ranked list of neighbor companies. That's the whole job. Scope is deliberately narrow:
ONE anchor per invocation, findSimilar only. Looping over many anchors, folding mirror/i18n
subdomains to an apex, deduping, and matching the neighbors to a cohort/tracked-set is the
*caller's* discovery-orchestration job — never this tool's. (The experiment this was distilled
from baked all of that in — Notion dedupe, a hard-coded shortlist, a supply-side mission. Gone.)

Generic on purpose: emits parsed JSON to stdout, no cohort / Notion / vertical baked in. The
tool knows nothing about telehealth or any other domain.

CLI:
  python3 tools/exa_similar.py ro.co
  python3 tools/exa_similar.py https://ro.co --num-results 25
  python3 tools/exa_similar.py hims.com --exclude-domains hims.ca forhims.co.uk   # mirror/i18n hygiene
  python3 tools/exa_similar.py acme.com --category ""                             # drop the company filter

Exit codes:
  0  clean capture (INCLUDING an empty neighbor list — "Exa found nothing similar" is data, not failure)
  2  fetch error (network, auth, Exa HTTP error, or an unexpected response missing `results`)
  (no exit 3: Exa is a stable, documented JSON API — no version-pinned parser, so no schema-drift path.
   `schema_drift` is still emitted as `[]` for envelope uniformity across the library.)

Auth: EXA_API_KEY from env, falling back to a `.env` at the repo root (gitignored).

Load-bearing gotchas (see exa_similar.md for the full catalog):
  - User-Agent MUST be curl/8.4.0 — the default urllib UA is Cloudflare-blocked at Exa's edge.
  - `score` is dropped on purpose: it's a synthetic, near-rank-derived value, useless as an
    absolute relevance score. Ordinal `rank` is the signal.
  - findSimilar is ALWAYS neural (costDollars reports under `search.neural`); the `type` param is
    silently ignored here, so there's no auto/neural mode to pin (that risk lives on `/search`).
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
EXA_FINDSIMILAR = "https://api.exa.ai/findSimilar"
# INVARIANT: the default urllib UA is Cloudflare-blocked at Exa's edge — a 30-min debugging trap.
# Pin a curl UA (or use `requests`, which sets one). Carried from agent-workflows/INVARIANTS.
USER_AGENT = "curl/8.4.0"
DEFAULT_NUM_RESULTS = 10
DEFAULT_CATEGORY = "company"  # Exa-native filter; this tool is company/neighbor discovery. Overridable.


def _utc_now() -> str:
    """This invocation's capture time, UTC ISO 8601 — the envelope's `captured_at`.

    Wall-clock of *when we captured*, never a source date. Exa results carry a `publishedDate`
    (a crawl date) which we drop; the library rule is uniform — source dates, if surfaced, live
    inside payload items under their own names, never in the envelope.
    """
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


def _normalize_anchor(arg: str) -> str:
    """Accept a bare domain ('ro.co'), a domain+path, or a full URL -> a URL Exa can anchor on.
    findSimilar wants a URL; a scheme-less input gets https:// prepended. We do NOT strip paths —
    similarity is to the *page* you point at, so a deep link is a legitimate, more-specific anchor."""
    arg = arg.strip()
    if "://" not in arg:
        arg = f"https://{arg}"
    return arg


def _domain_of(url: str) -> str | None:
    """Bare host of a neighbor URL ('https://www.roon.com/x' -> 'roon.com'), a convenience field.
    Lowercased, `www.` stripped — and that's ALL. Folding api./en./i18n mirrors to an apex, and
    deduping across anchors, is caller logic (the discovery orchestrator's), kept out on purpose."""
    host = urllib.parse.urlsplit(url).netloc.lower()
    host = host.split("@")[-1].split(":")[0]  # drop any userinfo / port
    if host.startswith("www."):
        host = host[4:]
    return host or None


def find_similar(
    anchor: str,
    api_key: str | None = None,
    num_results: int = DEFAULT_NUM_RESULTS,
    exclude_domains: list[str] | None = None,
    category: str = DEFAULT_CATEGORY,
) -> dict[str, Any]:
    """Full pipeline: POST /findSimilar for one anchor -> the shared envelope + a ranked `neighbors` list.

    `excludeSourceDomain` is always on — you never want the anchor's own pages back. `exclude_domains`
    is the caller's extra hygiene list (the anchor's known mirror/i18n/vanity TLDs). `category=""`
    drops Exa's company filter for an unfiltered neighbor sweep.
    """
    api_key = api_key or load_key(API_KEY_VAR)
    anchor_url = _normalize_anchor(anchor)
    exclude_domains = exclude_domains or []

    body: dict[str, Any] = {
        "url": anchor_url,
        "numResults": num_results,
        "excludeSourceDomain": True,  # don't return the anchor's own domain
    }
    if exclude_domains:
        body["excludeDomains"] = exclude_domains
    if category:  # falsy (e.g. --category "") => unfiltered sweep
        body["category"] = category

    resp = _http_post_json(EXA_FINDSIMILAR, body, api_key=api_key)
    if "results" not in resp:
        # Not drift (Exa is stable); an unexpected body — surface it loud as a transport-class failure.
        raise RuntimeError(f"Exa response missing 'results' (got keys {list(resp.keys())}): {str(resp)[:300]}")

    neighbors = [
        {
            "rank": i,  # ordinal — the ONLY relevance signal we trust (score is synthetic; dropped)
            "title": r.get("title"),
            "url": r.get("url"),
            "domain": _domain_of(r.get("url") or ""),
        }
        for i, r in enumerate(resp.get("results", []), start=1)
    ]

    cost_total = (resp.get("costDollars") or {}).get("total")
    return {
        # --- the reserved envelope spine (tools/README.md), identical across the library ---
        "tool": "exa_similar",
        "source": "exa.ai",  # the external system hit (via api.exa.ai/findSimilar)
        "captured_at": _utc_now(),  # THIS invocation's wall-clock, UTC — not a source date
        "ok": True,  # transport failures never reach here (exit 2); Exa has no drift path
        "input": {
            "anchor": anchor_url,
            "num_results": num_results,
            "category": category or None,
            "exclude_domains": exclude_domains,
        },
        "schema_drift": [],  # always empty — stable API, no version-pinned parser (kept for uniformity)
        "cost": {"usd": cost_total},  # Exa meters in dollars (costDollars.total)
        # --- payload, beside the spine (never nested under a generic `data`) ---
        "neighbors": neighbors,
        "neighbor_count": len(neighbors),
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("anchor", help="Anchor company: a domain ('ro.co'), a domain+path, or a full URL")
    p.add_argument(
        "--num-results",
        type=int,
        default=DEFAULT_NUM_RESULTS,
        help=f"How many neighbors to request (default: {DEFAULT_NUM_RESULTS})",
    )
    p.add_argument(
        "--exclude-domains",
        nargs="*",
        default=[],
        metavar="DOMAIN",
        help="Extra domains to exclude beyond the anchor's own (its mirror/i18n/vanity TLDs)",
    )
    p.add_argument(
        "--category",
        default=DEFAULT_CATEGORY,
        help=f"Exa result category filter (default: {DEFAULT_CATEGORY!r}; pass --category '' to drop it)",
    )
    args = p.parse_args()

    try:
        result = find_similar(
            args.anchor,
            num_results=args.num_results,
            exclude_domains=args.exclude_domains,
            category=args.category,
        )
    except Exception as e:
        sys.stderr.write(f"Error finding neighbors for {args.anchor!r}: {e}\n")
        sys.exit(2)

    print(json.dumps(result, indent=2))
    if result.get("schema_drift"):  # never fires today; kept uniform with the drift-prone tools
        sys.exit(3)


if __name__ == "__main__":
    main()
