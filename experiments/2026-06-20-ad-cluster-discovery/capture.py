#!/usr/bin/env python3
"""Phase-1 capture: pull a creative corpus for the ad-cluster bake-off.

Track A (spine) — Apify apify/facebook-ads-scraper, keyword Ad Library search URLs → US Meta ads
with full body copy. SPACE discovery + enrichment in one call.
Track B (capped) — SerpApi google_ads_transparency_center per store-seed domain → ad_details copy.
Seed-bound (no space discovery); a Google/YouTube channel-divergence sample.

Output: runs/<date>/corpus.json (unified creative records) + raw/ provenance + run-meta.json.
Experiment-local; does NOT touch store/. Graduate to a tools/ capture tool after the verb proves out.

SAFE BY DEFAULT: dry-run prints the plan + estimated spend and calls nothing. Pass --go to spend.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from _env import load_key  # noqa: E402

# Track A — the space, as keyword queries (the compounded-Rx DTC core: weight + hormone + sexual health)
DEFAULT_KEYWORDS = [
    "compounded semaglutide",
    "GLP-1 weight loss",
    "compounded tirzepatide",
    "testosterone replacement therapy",
    "online ED treatment",
]
# Track B — anchor priority for selecting the capped seed sample
ANCHOR_PRIORITY = ["GLP-1", "TRT", "sexual-health", "multi/none", "longevity/NAD", "peptides", "hair", "labs"]

APIFY_ACTOR = "apify~facebook-ads-scraper"
SERPAPI_BASE = "https://serpapi.com/search.json"
APIFY_COST_PER_RESULT = 0.0045  # ~$4.20-4.50/1k, Scale tier


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def dig(obj: object, *path: str) -> object:
    for p in path:
        obj = obj[p] if isinstance(obj, dict) and p in obj else None
    return obj


def meta_search_url(keyword: str) -> str:
    q = urllib.parse.quote(keyword)
    return (
        f"https://www.facebook.com/ads/library/?active_status=active&ad_type=all"
        f"&country=US&q={q}&search_type=keyword_unordered&media_type=all"
    )


def post_json(url: str, body: dict, timeout: int = 300) -> object:
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}, method="POST"
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def get_json(url: str, timeout: int = 120) -> object:
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return json.load(r)


def track_a(keywords: list[str], per_query: int, raw_dir: Path, go: bool) -> list[dict]:
    token = load_key("APIFY_API_KEY") if go else "DRY"
    records: list[dict] = []
    seen: set[str] = set()
    for kw in keywords:
        url = meta_search_url(kw)
        if not go:
            print(f"  [A] would scrape Meta Ad Library q='{kw}' (limit {per_query})")
            continue
        run_url = f"https://api.apify.com/v2/acts/{APIFY_ACTOR}/run-sync-get-dataset-items?token={token}"
        body = {"startUrls": [{"url": url}], "resultsLimit": per_query, "activeStatus": "active"}
        try:
            items = post_json(run_url, body)
        except urllib.error.HTTPError as exc:
            print(f"  [A] q='{kw}' HTTP {exc.code}: {exc.read().decode()[:200]}")
            continue
        except Exception as exc:  # noqa: BLE001
            print(f"  [A] q='{kw}' failed: {exc}")
            continue
        (raw_dir / f"meta_{kw.replace(' ', '_')}.json").write_text(json.dumps(items, indent=2))
        n_new = 0
        for it in items if isinstance(items, list) else []:
            aid = str(it.get("adArchiveID") or it.get("adId") or "")
            if not aid or aid in seen:
                continue
            seen.add(aid)
            n_new += 1
            snap = it.get("snapshot") or {}
            records.append(
                {
                    "channel": "meta",
                    "advertiser": it.get("pageName") or dig(it, "snapshot", "page_name"),
                    "advertiser_id": str(it.get("pageId") or ""),
                    "source": kw,
                    "copy": dig(snap, "body", "text"),
                    "headline": snap.get("title") or snap.get("caption"),
                    "cta": snap.get("cta_text"),
                    "link": snap.get("link_url"),
                    "format": it.get("publisherPlatform") or snap.get("display_format"),
                    "is_active": it.get("isActive"),
                    "first_shown": it.get("startDateFormatted") or it.get("startDate"),
                    "last_shown": it.get("endDateFormatted") or it.get("endDate"),
                    "ad_id": aid,
                }
            )
        print(f"  [A] q='{kw}': {n_new} new creatives")
    return records


def track_b(seed_sample: list[dict], per_domain: int, raw_dir: Path, go: bool) -> list[dict]:
    key = load_key("SERP_API_KEY") if go else "DRY"
    records: list[dict] = []
    for brand in seed_sample:
        domain = brand["domain"]
        if not go:
            print(f"  [B] would GATC '{domain}' + up to {per_domain} ad_details")
            continue
        list_url = SERPAPI_BASE + "?" + urllib.parse.urlencode(
            {"engine": "google_ads_transparency_center", "text": domain, "api_key": key}
        )
        try:
            lst = get_json(list_url)
        except Exception as exc:  # noqa: BLE001
            print(f"  [B] {domain} list failed: {exc}")
            continue
        creatives = (lst.get("ad_creatives") or []) if isinstance(lst, dict) else []
        (raw_dir / f"google_{domain}.json").write_text(json.dumps(lst, indent=2))
        n = 0
        for c in creatives[:per_domain]:
            adv, cid = c.get("advertiser_id"), c.get("ad_creative_id") or c.get("creative_id")
            if not (adv and cid):
                continue
            det_url = SERPAPI_BASE + "?" + urllib.parse.urlencode(
                {"engine": "google_ads_transparency_center_ad_details", "advertiser_id": adv, "creative_id": cid, "api_key": key}
            )
            try:
                det = get_json(det_url)
            except Exception:  # noqa: BLE001
                continue
            ac = (det.get("ad_creatives") or [{}])[0] if isinstance(det, dict) else {}
            headline, snippet = ac.get("headline"), ac.get("snippet")
            copy = " — ".join(x for x in (ac.get("title"), headline, snippet) if x)
            records.append(
                {
                    "channel": "google",
                    "advertiser": c.get("advertiser") or brand.get("name"),
                    "advertiser_id": adv,
                    "source": domain,
                    "store_domain": brand.get("store_slug") or domain,
                    "copy": copy or None,
                    "headline": headline,
                    "cta": None,
                    "link": ac.get("visible_link") or c.get("target_domain"),
                    "format": c.get("format"),
                    "is_active": None,
                    "first_shown": c.get("first_shown"),
                    "last_shown": c.get("last_shown"),
                    "ad_id": str(cid),
                }
            )
            n += 1
        print(f"  [B] {domain}: {n} enriched creatives")
    return records


def pick_seed_sample(seed: list[dict], limit: int) -> list[dict]:
    rank = {a: i for i, a in enumerate(ANCHOR_PRIORITY)}
    ordered = sorted(seed, key=lambda b: (rank.get((b.get("anchor_category") or "").strip(), 99), b["domain"]))
    return ordered[:limit]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--go", action="store_true", help="actually spend (default: dry-run)")
    ap.add_argument("--append", action="store_true", help="merge into today's existing corpus.json")
    ap.add_argument("--tracks", default="ab", help="which tracks: a, b, or ab")
    ap.add_argument("--per-query", type=int, default=60, help="Track A: ads per keyword")
    ap.add_argument("--per-domain", type=int, default=3, help="Track B: creatives enriched per seed brand")
    ap.add_argument("--track-b-limit", type=int, default=18, help="Track B: number of seed brands")
    ap.add_argument("--keywords", nargs="*", default=DEFAULT_KEYWORDS)
    args = ap.parse_args()

    seed = json.loads((HERE / "seed-telehealth.json").read_text())
    seed_sample = pick_seed_sample(seed, args.track_b_limit)

    a_on, b_on = "a" in args.tracks, "b" in args.tracks
    est_apify = len(args.keywords) * args.per_query * APIFY_COST_PER_RESULT if a_on else 0
    est_serp = len(seed_sample) * (1 + args.per_domain) if b_on else 0

    print(f"=== capture plan ({'GO — SPENDING' if args.go else 'DRY-RUN — no spend'}) ===")
    if a_on:
        print(f"Track A (Meta/Apify): {len(args.keywords)} queries x {args.per_query} ads "
              f"≈ ${est_apify:.2f} Apify  | keywords: {args.keywords}")
    if b_on:
        print(f"Track B (Google/SerpApi): {len(seed_sample)} brands x (1 + {args.per_domain}) "
              f"≈ {est_serp} SerpApi searches | sample: {[b['domain'] for b in seed_sample]}")
    if not args.go:
        print("\nDry-run only. Re-run with --go to execute.")
        return 0

    run_dir = HERE / "runs" / datetime.now(timezone.utc).strftime("%Y-%m-%d")
    raw_dir = run_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    corpus: list[dict] = []
    corpus_path = run_dir / "corpus.json"
    if args.append and corpus_path.exists():
        corpus = json.loads(corpus_path.read_text())
        print(f"appending to existing corpus ({len(corpus)} records)")
    seen = {(r["channel"], r["ad_id"]) for r in corpus}
    new: list[dict] = []
    if a_on:
        new += track_a(args.keywords, args.per_query, raw_dir, go=True)
    if b_on:
        new += track_b(seed_sample, args.per_domain, raw_dir, go=True)
    corpus += [r for r in new if (r["channel"], r["ad_id"]) not in seen]

    corpus_path.write_text(json.dumps(corpus, indent=2))
    meta = {
        "captured_at": utc_stamp(),
        "keywords": args.keywords,
        "track_b_sample": [b["domain"] for b in seed_sample],
        "per_query": args.per_query,
        "per_domain": args.per_domain,
        "counts": {
            "total": len(corpus),
            "meta": sum(1 for r in corpus if r["channel"] == "meta"),
            "google": sum(1 for r in corpus if r["channel"] == "google"),
            "distinct_advertisers": len({(r["advertiser"] or "").lower() for r in corpus}),
        },
        "est_cost": {"apify_usd": round(est_apify, 2), "serpapi_searches": est_serp},
    }
    (run_dir / "run-meta.json").write_text(json.dumps(meta, indent=2))
    print(f"\nCorpus: {meta['counts']} → {run_dir/'corpus.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
