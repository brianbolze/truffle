---
created: 2026-06-20
last_updated: 2026-06-20
status: Phase-0 output — tool/technique survey (deep-research, adversarially verified)
source: /deep-research run wf_6febbde5-511 (6 angles, 27 sources, 124 claims → 25 verified, 22 confirmed / 3 killed)
---

# Phase 0 — ad-intelligence tool survey

## 30-second recommendation

For a **space → top-K messaging clusters, keyed to advertisers**, file-first/low-infra pipeline,
the verified evidence points to **two capture tracks sharing one LLM-clustering layer**:

- **Track A — US DTC social (the must-have for telehealth).** `curious_coder/facebook-ads-library-scraper`
  for keyword/**space** discovery (~$0.75/1k ads) → `apify/facebook-ads-scraper` for full creative
  enrichment (body copy, CTA, links, image+video URLs, carousel cards; ~$3.40–5.80/1k). **~$3/run**
  for ~500 creatives. US-inclusive, currently-running.
- **Track B — Google / YouTube (complement, already owned).** SerpApi
  `google_ads_transparency_center` `text=` keyword discovery → `…_ad_details` per-ad enrichment for
  copy. Per-call-heavy (~hundreds of SERP credits/run); image-only ads need OCR. Google/Display/YouTube only.
- **Foreplay API** — premium third contender if budget allows: one real public REST API among the
  ad-spy platforms; keyword/space discovery + full creative + **pre-derived `emotional_drivers` /
  `niches` / `product_category`** that shortcut clustering. 1 credit/ad.

**Clustering:** **LLM thematic clustering** (Claude reads creatives → named angles, advertiser IDs
passed alongside) — best fit at small N, zero infra, outputs nameable angles directly. Optionally
seed a small fixed taxonomy as a run-to-run **stabilizer**. Embedding+KMeans not worth it here.

**Two killed (don't pursue):** the **official Meta Ad Library API** (US commercial ads invisible — EU/UK
only) and the **beyondops TikTok actor** (filter-only, no keyword search; creative/pricing claims refuted).

## Comparison — capture sources × the five dimensions

| Source | 1. Creative copy? | 2. Space-queryable? | 3. Access + cost | 4. Risk/stability | 5. Freshness |
|---|---|---|---|---|---|
| **Meta Ad Library — official API** (`ads_archive`) | Yes (`ad_creative_bodies`…) | Yes (`search_terms`) | Free, OAuth | First-party, stable | **US commercial ads NOT returned — EU/UK only, ~1yr.** ❌ disqualifying |
| **Apify `apify/facebook-ads-scraper`** | **Yes — strongest** (body.text, ctaText, linkUrl, image/videoHd/Sd, cards[]) | **No** — Page/Ad-Library-URL keyed, no free-text field | Apify actor, ~$3.40–5.80/1k pay-per-result | Vendor-maintained; gripes: empty/private data, runs stall ~6k | Live Ad Library, **US included** |
| **Apify `curious_coder/facebook-ads-library-scraper`** | Plausibly yes (under-doc claim *refuted*; verify empirically) | **Yes** — Ad-Library search URLs (`q=`, `search_type=keyword_unordered`) | Apify actor, **$0.75/1k** pay-per-event | Stability complaints (Jun 2025) | Live Ad Library |
| **SerpApi `google_ads_transparency_center`** (owned) | List = **no copy**; copy needs 2nd `…_ad_details` call (advertiser_id+creative_id); image-only → OCR | **Yes** for discovery (`text=`); ad_details = no discovery | SerpApi credits, **2 calls/ad** to copy level | First-party SerpApi, stable | Currently-running; Google/Display/YouTube |
| **TikTok — official Commercial Content API** | Yes | Yes (`search_term`+type) | Free, **approval ~2 days**, **EU-data only** | Stable, gated | Archive (EU) |
| **TikTok — Apify `coregent/…creative-center-scraper`** | Yes (raw `caption` = real copy) | Yes (searchTerms/industries/countries) | Apify actor, $3.20/1k | Vendor-maintained | Creative Center |
| **Foreplay API** | **Yes + transcriptions + derived signals** (emotional_drivers/niches/product_category) | **Yes** (Discovery endpoints, 100M+ ads) | Public REST, key-auth, **1 credit/ad** + plan | Vendor SaaS; API excludes legacy plans | Live DB |
| Other ad-spy (AdSpy/BigSpy/MagicBrief/Atria/Minea/Anstrex) | — | — | **No public API confirmed** (presumed UI-only — *not verified*) | — | — |

## Clustering technique

| Method | Fit for ~few-hundred creatives, file-first, no vector DB |
|---|---|
| **LLM thematic clustering** ✅ | Recommended default. Outputs human-nameable angles directly; zero standing infra; one scriptable Python→API loop; keeps advertiser attribution by passing IDs alongside each creative. |
| Hand-seeded taxonomy | Best as a **stabilizer** layered on the LLM pass for run-to-run consistency (e.g. price/urgency · efficacy/results · safety-clinical · identity/transformation · convenience/telehealth-access) — not standalone. |
| Embedding + KMeans | Adds an embedding dep + a separate label-naming step for little gain at small N; opaque clusters. Skip. |

## The store's role (two jobs)

The open question the research flagged: a keyword/space query ("compounded semaglutide", "GLP-1
weight loss") **may not reliably map to the right advertiser set** by itself — DTC brands vary
on-creative wording. So **our store's telehealth cohort earns its keep twice**:

1. **Seed/anchor** — feed known advertiser domains/pages as a backbone so the space isn't only
   keyword-discovered (raises recall + keying reliability).
2. **Keying destination** — the eval's store-keyability metric = % of surfaced advertisers that
   resolve to a captured `store/<domain>/`, plus a propose-capture list for those that don't.

## Caveats (from the verification)

- **Docs ≠ recall.** Every confirmed capability/price claim rests on primary vendor docs — which say
  nothing about real-world coverage. The Apify-actor run-stalling / empty-data gripes are exactly what
  only the bake-off reveals. **Recall on a real telehealth advertiser set is the bake-off's core job.**
- **Pricing rots** — re-verify Apify/SerpApi/Foreplay costs at build time.
- **Unassessed (named but no surviving claim):** TikTok Creative Center "Top Ads" standalone, LinkedIn /
  Pinterest / Reddit ad libraries — low-priority for compounded-Rx DTC anyway, but genuinely unassessed,
  not dismissed. Ad-spy "no API" for all-but-Foreplay is *not-confirmed*, not confirmed-absent.

## Open questions → for the bake-off to settle

1. `curious_coder` creative-text completeness (verify body/headline coverage empirically).
2. Apify-actor **recall** on a real telehealth weight-loss/hormone advertiser set.
3. Reliability of **space→advertiser keying** from keyword alone vs needing the store seed list.
4. Whether any other ad-spy platform exposes a real API (only Foreplay confirmed).

## Key sources

Meta API limits · [facebook.com/ads/library/api](https://www.facebook.com/ads/library/api) ·
[ads_archive ref](https://developers.facebook.com/docs/graph-api/reference/ads_archive/) ·
Apify actors · [apify/facebook-ads-scraper](https://apify.com/apify/facebook-ads-scraper) ·
[curious_coder/facebook-ads-library-scraper](https://apify.com/curious_coder/facebook-ads-library-scraper) ·
[coregent TikTok](https://apify.com/coregent/tiktok-ads-library-creative-center-scraper/api/python) ·
SerpApi · [GATC engine](https://serpapi.com/google-ads-transparency-center-api) ·
[GATC ad details](https://serpapi.com/google-ads-transparency-center-ad-details) ·
TikTok · [Commercial Content API](https://developers.tiktok.com/products/commercial-content-api) ·
Foreplay · [public OpenAPI](https://public.api.foreplay.co/openapi.json) · [foreplay.co/api](https://foreplay.co/api)
