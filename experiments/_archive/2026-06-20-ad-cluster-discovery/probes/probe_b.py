#!/usr/bin/env python3
"""Nail Track B's real capability: does GATC text= support SPACE (topic) discovery, or only
known advertiser/domain lookup? And can we reach ad COPY via ad_details? Throwaway."""
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
KEY = load_key("SERP_API_KEY")
BASE = "https://serpapi.com/search.json"


def call(params: dict) -> tuple[int, object]:
    url = BASE + "?" + urllib.parse.urlencode({**params, "api_key": KEY})
    try:
        with urllib.request.urlopen(url, timeout=120) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode()[:600]


print("=== topic query 'compounded semaglutide' (no region) ===")
code, body = call({"engine": "google_ads_transparency_center", "text": "compounded semaglutide"})
if isinstance(body, dict):
    tc = body.get("ad_creatives") or []
    print(f"  status {code}: {len(tc)} creatives, {len({c.get('advertiser_id') for c in tc})} advertisers")
    if tc:
        print(f"  advertisers: {[c.get('advertiser') for c in tc][:8]}")
else:
    print(f"  status {code}: {body}")

print("\n=== domain query 'hims.com' (no region) ===")
code, body = call({"engine": "google_ads_transparency_center", "text": "hims.com"})
if isinstance(body, dict):
    creatives = body.get("ad_creatives") or []
    print(f"  status {code}: {len(creatives)} creatives")
    if creatives:
        print(f"  creative[0] keys: {sorted(creatives[0].keys())}")
        (OUT / "trackB_domain.json").write_text(json.dumps(body, indent=2))
        c0 = creatives[0]
        cid = c0.get("creative_id") or c0.get("ad_creative_id") or c0.get("id")
        adv = c0.get("advertiser_id")
        print(f"  advertiser_id={adv!r}  creative_id={cid!r}")
        if adv and cid:
            dcode, det = call(
                {"engine": "google_ads_transparency_center_ad_details", "advertiser_id": adv, "creative_id": cid}
            )
            if isinstance(det, dict):
                (OUT / "trackB_ad_details.json").write_text(json.dumps(det, indent=2))
                print(f"  ad_details status {dcode}: top keys {sorted(det.keys())}")
            else:
                print(f"  ad_details status {dcode}: {det}")
else:
    print(f"  status {code}: {body}")
