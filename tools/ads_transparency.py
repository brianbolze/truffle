#!/usr/bin/env python3
"""Google Ads Transparency Center fetcher — paid-ads presence + recency for an advertiser/domain.

Scope: SerpAPI `engine=google_ads_transparency_center`, text-search by domain (or advertiser
name), first page of creatives only. This answers "is anyone running Google ads that land on
this domain, and how recently/how long" — a PUSH/resourcing signal, never demand or spend.

What the first page CAN see: presence, advertiser legal name, per-creative format and
first/last-shown dates (epoch + ISO mirror). What it CANNOT see: total ad volume (page 1 is
not the universe), budget, performance, or Meta/TikTok presence (different channels entirely —
the Meta Ad Library route stays deferred per BACKLOG.md).

CLI:
  python3 tools/ads_transparency.py hims.com
  python3 tools/ads_transparency.py "Hone Health" --region US

Exit codes:
  0  clean capture (including a clean zero — no creatives found is a valid result)
  2  fetch error (network, auth, etc.)
  3  schema drift detected (parsed fields suppressed; stop the run)

Auth: SERP_API_KEY from env, falling back to a `.env` at the repo root (gitignored).

Pinned parser version: v1 — bump only on an intentional schema migration.
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

PARSER_VERSION = "v1"
API_KEY_VAR = "SERP_API_KEY"
SERPAPI_BASE = "https://serpapi.com/search.json"

# SerpAPI's google_ads_transparency_center `region` is a numeric Google geo-target ID,
# NOT an ISO country code — passing "US" 400s ("Unsupported `US` region parameter."). Map
# the codes we actually use to their IDs; a numeric value passes straight through, so any
# region stays reachable without growing this table (full list:
# serpapi.com/google-ads-transparency-center-regions).
REGION_IDS: dict[str, str] = {
    "US": "2840",
    "GB": "2826",
    "UK": "2826",
    "CA": "2124",
    "AU": "2036",
}


def resolve_region(region: str) -> str:
    """Normalize a --region value to the numeric geo-target ID SerpAPI expects.

    Country code (case-insensitive) → ID via REGION_IDS; an already-numeric value is trusted
    as-is so the table need not enumerate every region. Unknown codes fail loudly here rather
    than as an opaque 400 from SerpAPI.
    """
    normalized = region.strip().upper()
    if normalized.isdigit():
        return normalized
    try:
        return REGION_IDS[normalized]
    except KeyError:
        raise ValueError(
            f"unsupported region {region!r}: pass a country code "
            f"({', '.join(sorted(REGION_IDS))}) or a numeric Google geo-target ID "
            f"(serpapi.com/google-ads-transparency-center-regions)"
        ) from None


def _utc_now() -> str:
    """This invocation's capture time — the envelope's `captured_at`, never a source date."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _epoch_to_iso(value: Any) -> str | None:
    try:
        return datetime.fromtimestamp(int(value), tz=timezone.utc).strftime("%Y-%m-%d")
    except (TypeError, ValueError, OSError):
        return None


def fetch(text: str, region: str | None) -> dict[str, Any]:
    params: dict[str, str] = {
        "engine": "google_ads_transparency_center",
        "text": text,
        "api_key": load_key(API_KEY_VAR),
    }
    if region:
        params["region"] = resolve_region(region)
    url = f"{SERPAPI_BASE}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=90) as resp:
        return json.load(resp)


def validate_shape_v1(raw: dict[str, Any]) -> list[str]:
    """Complaint list; non-empty ⇒ schema drift. A zero-creative response is NOT drift."""
    complaints: list[str] = []
    if "error" in raw:
        # "hasn't returned any results" is a CLEAN ZERO (advertiser runs no Google ads),
        # not drift — SerpAPI reports it via the error field. Handled by caller.
        if "hasn't returned any results" not in raw["error"]:
            complaints.append(f"serpapi error field: {raw['error']}")
        return complaints
    creatives = raw.get("ad_creatives")
    if creatives is None:
        # Legit zero-result responses still carry search_metadata; missing both is drift.
        if "search_metadata" not in raw:
            complaints.append("missing both ad_creatives and search_metadata")
        return complaints
    if not isinstance(creatives, list):
        complaints.append("ad_creatives is not a list")
        return complaints
    if creatives:
        missing = sum(
            1 for c in creatives if not c.get("advertiser") or "last_shown" not in c
        )
        if missing > len(creatives) / 2:
            complaints.append(
                f"{missing}/{len(creatives)} creatives missing advertiser/last_shown"
            )
    return complaints


def parse_creatives(raw: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for c in raw.get("ad_creatives") or []:
        out.append(
            {
                "advertiser": c.get("advertiser"),
                "advertiser_id": c.get("advertiser_id"),
                "format": c.get("format"),
                "target_domain": c.get("target_domain"),
                "first_shown": c.get("first_shown"),
                "first_shown_iso": _epoch_to_iso(c.get("first_shown")),
                "last_shown": c.get("last_shown"),
                "last_shown_iso": _epoch_to_iso(c.get("last_shown")),
            }
        )
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("text", help="domain (preferred) or advertiser name to search")
    ap.add_argument("--region", default=None, help="optional region filter, e.g. US")
    args = ap.parse_args()

    envelope: dict[str, Any] = {
        "tool": "ads_transparency",
        "source": "serpapi.com (google_ads_transparency_center)",
        "captured_at": _utc_now(),
        "ok": False,
        "parser_version": PARSER_VERSION,
        "input": {"text": args.text, "region": args.region},
        "schema_drift": [],
        "cost": "1 SerpAPI search",
    }

    try:
        raw = fetch(args.text, args.region)
    except Exception as exc:  # noqa: BLE001 — single exit path for any transport failure
        envelope["error"] = f"fetch failed: {exc}"
        print(json.dumps(envelope, indent=2))
        return 2

    drift = validate_shape_v1(raw)
    if drift:
        envelope["schema_drift"] = drift
        print(json.dumps(envelope, indent=2))
        return 3

    creatives = parse_creatives(raw)
    envelope["ok"] = True
    envelope["ad_creatives"] = creatives
    envelope["n_creatives_first_page"] = len(creatives)
    if "error" in raw and not creatives:
        envelope["note"] = "clean zero — source returned no results for this advertiser/domain"
    print(json.dumps(envelope, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
