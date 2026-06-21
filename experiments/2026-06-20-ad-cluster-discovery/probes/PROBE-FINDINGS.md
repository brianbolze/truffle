---
created: 2026-06-20
status: Phase-1a probe findings (hands-on, live API calls)
space tested: "compounded semaglutide" / hims.com · region omitted
raw: ./out/*.json
---

# Phase 1a — two-track probe findings

**One-line:** Track A (Apify/Meta) is validated as the **space-discovery + creative engine** in a
single call; Track B (SerpApi/Google) **cannot discover a space** — it only enriches *known*
advertisers — so the two tracks are **asymmetric**, not co-equal discovery contenders.

## Track A — Apify `apify/facebook-ads-scraper` ✅ strong

- **One actor call** with a keyword Ad Library search URL (`q=compounded semaglutide&search_type=keyword_unordered&country=US`)
  returned **10 live US compounded-GLP-1 ads with full creative copy**. Space discovery + enrichment together.
- **Copy** at `snapshot.body.text`; **advertiser** at `pageName`. Rich fields: `adArchiveID`, `pageId`,
  `snapshot`, `startDate`/`endDate`, `isActive`, `publisherPlatform`, `spend`, `impressionsWithIndex`.
- Sample angle, verbatim: *"Why pay $1,000+ for brand-name GLP-1 when you can get the same active
  ingredient for 89% less? … ✅ Medication included ✅ Any dose you need"* — **Dad Club Co.** (price-anchor vs brand-name).
- **Verdict:** the spine. Does the load-bearing job (space → creatives → nameable angles), US-inclusive, ~$3/500 ads.

## Track B — SerpApi `google_ads_transparency_center` ⚠️ enrichment-only

- **Topic query → 200 but 0 creatives.** `text=` does **NOT** do space/topic discovery (confirms the survey's hedge).
- **Domain query `hims.com` → 13 creatives** with `ad_creative_id` + `advertiser_id`. `ad_details` → clean
  **`title`/`headline`/`snippet`/`visible_link`** copy (text ads readable; no OCR needed). Image ads would need OCR.
- **Cost shape:** per advertiser = 1 list search + **1 `ad_details` search per creative** → ~14 SerpApi searches for hims alone. Credit-heavy at cohort scale.
- **Verdict:** a per-**known**-advertiser Google/YouTube channel — seed-bound, not a discovery method. Different channel, same brands.

## Decision-grade implications

1. **The tracks are complementary, not competing.** Only A discovers a space; B profiles a known seed
   list on a different channel. So the v1 "bake-off" is really *A = the engine*, *B = an optional
   channel-divergence probe* (do known brands run different angles on Google vs Meta?).
2. **Track A graduates to the spine.** Build the capture + clustering around it.
3. **Track B should be scoped or deferred** — it's seed-bound and credit-heavy (1 + N searches/advertiser).
   If kept in v1, cap it to the store seed advertisers + a sampled creatives-per-brand to control credits.

## Engine bug found (small, separate)

`tools/ads_transparency.py` accepts `--region` and its docstring shows `--region US`, but SerpApi GATC
**rejects `region=US`** (`"Unsupported US region parameter"`) — it wants a numeric Google region code.
The live tool only sends `region` when `--region` is passed, so the default path is fine, but the
documented example is stale. Flag for a one-line doc/param fix (out of scope for this experiment).
