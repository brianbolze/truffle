#!/usr/bin/env python3
"""Shared Firecrawl `/v2/scrape` caller — the one POST every Firecrawl tool makes, classified once.

Earned its place the way `_env.py` did: on the SECOND caller. `trustpilot.py` was the first Firecrawl
tool and inlined the call; `source_page.py` is the second, so the call + parse + error-classification
lifts here. It owns ONLY the HTTP call, the JSON parse, and the failure classification — never the
request recipe (formats / proxy / actions / wait are the caller's, who alone knows its source) and
never the output envelope.

Why a result object, not a raise: a scrape has four failure modes a caller must tell apart to bill
and report honestly —

  - missing key                    -> no call made, nothing charged
  - transport failure (pre-answer) -> nothing charged
  - HTTP error status (4xx/5xx)    -> the scrape didn't run, treat as not charged
  - answer received but unusable   -> CHARGED (success:false, or a body we couldn't parse)

`reached` carries exactly that last bit: did Firecrawl answer at all, i.e. was a credit metered. The
caller reads `reached` for its cost line and `raw` / `error` for its envelope. The helper never raises
for these expected modes — a tool whose contract is "always emit one envelope" (source_page) and a
tool whose contract is "raise -> exit 2" (trustpilot) both build their own path from one result.

Scope: this owns the call only — NOT the request recipe. The hazard knobs that make a scrape correct
(`maxAge:0` + `location:US` + `waitFor` against the silent geo-misroute/cache collision; the
all-cheap-formats-ride-one-credit rule; the avoid-list: `json` LLM extract, enhanced proxy, `/crawl`,
monitoring) live in the caller's `body` and are documented once in the canonical capture playbook —
[`skills/research-company/firecrawl-capture.md`](../skills/research-company/firecrawl-capture.md).
Read it before changing a caller's `body` or adding a third caller. The per-call billed truth is
`metadata.creditsUsed` (playbook §"Budget telemetry") — prefer it over a fixed estimate.

Sibling caller, deliberately NOT shared with this: `fc.py`'s `post()` in the same skill dir is the
store-writing `/research-company` capture pipeline — store-coupled, settings.json key source. This is
the generic `tools/`-library Firecrawl caller — bare-shell, `_env` key, print-don't-write. Different
couplings, so two callers, not one; both follow the same playbook.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

from _env import load_key

API_KEY_VAR = "FIRECRAWL_API_KEY"
SCRAPE_ENDPOINT = "https://api.firecrawl.dev/v2/scrape"


@dataclass
class ScrapeResult:
    """One scrape outcome, classified for billing + reporting.

    reached  — Firecrawl returned a response body we read, so a credit was metered. False for a missing
               key or a transport failure before any answer; True even when that answer was unusable or
               unparseable (the scrape still ran and charged).
    raw      — the parsed JSON response object, or {} when unreached / unparseable / non-object.
    error    — a human-readable failure of the call/parse ITSELF (missing key, transport, HTTP error,
               bad JSON), or None on a clean transport + parse. A clean call whose PAYLOAD is unusable
               (success:false, thin content) is not an error here — that read belongs to the caller.
    """

    reached: bool
    raw: dict[str, Any]
    error: str | None


def scrape(body: dict[str, Any], *, timeout: int, api_key: str | None = None) -> ScrapeResult:
    """POST one `/v2/scrape` request and classify the outcome into a ScrapeResult (never raises for the
    expected failure modes). `body` is the caller's full request payload — it must carry `url` and
    `formats`; the recipe (proxy, actions, waitFor, onlyMainContent, location) stays the caller's. Pass
    `api_key` to use a preloaded key; otherwise it is loaded here, and a missing key becomes an
    unreached result rather than a raise."""
    try:
        key = api_key or load_key(API_KEY_VAR)
    except RuntimeError as exc:  # _env.load_key fails loud on a missing key; soften to a result here
        return ScrapeResult(reached=False, raw={}, error=str(exc))

    request = urllib.request.Request(
        SCRAPE_ENDPOINT,
        data=json.dumps(body).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = response.read()
    except urllib.error.HTTPError as exc:
        # The API answered with an error status — no successful scrape ran; treat as unreached (no credit).
        return ScrapeResult(reached=False, raw={}, error=f"firecrawl HTTP {exc.code}: {exc.reason}")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return ScrapeResult(reached=False, raw={}, error=f"firecrawl transport error: {exc}")

    # A body came back -> Firecrawl answered, so a credit was metered. A parse failure here is still
    # `reached` (charged), just unusable — exactly the case the inlined callers used to crash on.
    try:
        parsed = json.loads(payload)
    except (json.JSONDecodeError, ValueError) as exc:
        return ScrapeResult(reached=True, raw={}, error=f"firecrawl returned unparseable JSON: {exc}")
    if not isinstance(parsed, dict):
        return ScrapeResult(reached=True, raw={}, error="firecrawl returned a non-object JSON body")
    return ScrapeResult(reached=True, raw=parsed, error=None)
