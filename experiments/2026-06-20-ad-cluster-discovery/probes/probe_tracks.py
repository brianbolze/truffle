#!/usr/bin/env python3
"""De-risk probe: do Track A (Apify Meta) and Track B (SerpApi Google) actually return
ad COPY for a US telehealth/compounded-Rx SPACE query? Throwaway — inspect, then build.

Usage: python3 probe_tracks.py ["compounded semaglutide"]
Writes raw responses to ./out/ and prints a tight summary. Caps hard to stay cheap.
"""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from _env import load_key  # noqa: E402

OUT = Path(__file__).resolve().parent / "out"
OUT.mkdir(exist_ok=True)

SPACE = sys.argv[1] if len(sys.argv) > 1 else "compounded semaglutide"
REGION = "US"


def get_json(url: str, timeout: int = 120) -> object:
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return json.load(r)


def post_json(url: str, body: dict, timeout: int = 300) -> object:
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}, method="POST"
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def dig(obj: object, *path: str) -> object:
    for p in path:
        if isinstance(obj, dict) and p in obj:
            obj = obj[p]
        else:
            return None
    return obj


def track_b() -> None:
    print("\n=== Track B — SerpApi google_ads_transparency_center ===")
    key = load_key("SERP_API_KEY")
    base = "https://serpapi.com/search.json"
    disc_url = base + "?" + urllib.parse.urlencode(
        {"engine": "google_ads_transparency_center", "text": SPACE, "region": REGION, "api_key": key}
    )
    try:
        disc = get_json(disc_url)
    except Exception as exc:  # noqa: BLE001
        print(f"  discovery FAILED: {exc}")
        return
    (OUT / "trackB_discovery.json").write_text(json.dumps(disc, indent=2))
    creatives = disc.get("ad_creatives") or [] if isinstance(disc, dict) else []
    advs = {c.get("advertiser_id"): c.get("advertiser") for c in creatives}
    print(f"  discovery text='{SPACE}': {len(creatives)} creatives, {len(advs)} distinct advertisers")
    if not creatives:
        print(f"  (no creatives — raw top keys: {sorted(disc.keys()) if isinstance(disc, dict) else disc})")
        return
    print(f"  creative[0] keys: {sorted(creatives[0].keys())}")
    print(f"  advertisers: {[a for a in advs.values() if a][:8]}")
    c0 = creatives[0]
    cid = c0.get("creative_id") or c0.get("ad_creative_id") or c0.get("id")
    if c0.get("advertiser_id") and cid:
        det_url = base + "?" + urllib.parse.urlencode(
            {
                "engine": "google_ads_transparency_center_ad_details",
                "advertiser_id": c0["advertiser_id"],
                "creative_id": cid,
                "api_key": key,
            }
        )
        try:
            det = get_json(det_url)
            (OUT / "trackB_ad_details.json").write_text(json.dumps(det, indent=2))
            print(f"  ad_details OK — top keys: {sorted(det.keys()) if isinstance(det, dict) else det}")
        except Exception as exc:  # noqa: BLE001
            print(f"  ad_details FAILED: {exc}")
    else:
        print(f"  could not find creative_id on creative[0] (have: {sorted(c0.keys())})")


def track_a() -> None:
    print("\n=== Track A — Apify apify/facebook-ads-scraper ===")
    token = load_key("APIFY_API_KEY")
    q = urllib.parse.quote(SPACE)
    search_url = (
        f"https://www.facebook.com/ads/library/?active_status=active&ad_type=all"
        f"&country=US&q={q}&search_type=keyword_unordered&media_type=all"
    )
    body = {"startUrls": [{"url": search_url}], "resultsLimit": 10, "activeStatus": "active"}
    run_url = f"https://api.apify.com/v2/acts/apify~facebook-ads-scraper/run-sync-get-dataset-items?token={token}"
    try:
        items = post_json(run_url, body, timeout=300)
    except urllib.error.HTTPError as exc:
        print(f"  HTTP {exc.code}: {exc.read().decode()[:400]}")
        return
    except Exception as exc:  # noqa: BLE001
        print(f"  FAILED: {exc}")
        return
    (OUT / "trackA_items.json").write_text(json.dumps(items, indent=2))
    n = len(items) if isinstance(items, list) else 0
    print(f"  items returned: {n}")
    if not n:
        return
    it = items[0]
    print(f"  item[0] keys: {sorted(it.keys())}")
    for path in (("body", "text"), ("snapshot", "body", "text"), ("adText",), ("text",), ("snapshot", "caption")):
        v = dig(it, *path)
        if isinstance(v, str) and v.strip():
            print(f"  COPY via {'/'.join(path)}: {v[:180]!r}")
            break
    else:
        print("  no obvious body-copy field — inspect out/trackA_items.json")
    adv = it.get("pageName") or dig(it, "snapshot", "page_name") or it.get("advertiser")
    print(f"  advertiser/page: {adv!r}")


if __name__ == "__main__":
    track_b()
    track_a()
    print(f"\nRaw responses written to {OUT}")
