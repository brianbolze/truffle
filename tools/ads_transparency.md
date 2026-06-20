# ads_transparency.py — Google Ads Transparency Center capture

Paid-ads **presence + recency + tenure** for an advertiser, searched by domain (preferred) or
name, via SerpAPI `engine=google_ads_transparency_center`. One SerpAPI search per call.

```bash
python3 tools/ads_transparency.py hims.com
python3 tools/ads_transparency.py "Hone Health" --region US
```

## What it can and cannot see

- **Can:** whether ads landing on a domain are running, the advertiser's legal name (often ≠
  brand name, e.g. Hone → "TIME THERAPEUTICS INC."), per-creative format, and first/last-shown
  dates — so both *recency* ("last shown yesterday") and *advertising tenure* ("first creative
  Feb 2026").
- **Cannot:** total ad volume (first page only — do not report `n_creatives_first_page` as "they
  run N ads"), budget/spend, performance, or non-Google channels. Meta/Instagram presence is a
  different surface (Apify route, deferred — see [`BACKLOG.md`](BACKLOG.md)).
- This is a **push/resourcing signal, not demand.** Running ads proves budget and an active
  acquisition motion, not that the ads work.

## Output shape

Standard envelope (`tool` / `source` / `captured_at` / `ok` / `input` / `schema_drift` /
`parser_version` / `cost`) plus:

```json
{
  "ad_creatives": [
    {"advertiser": "Maximus Health INC", "advertiser_id": "AR…", "format": "text",
     "target_domain": "maximustribe.com",
     "first_shown": 1770000000, "first_shown_iso": "2026-02-12",
     "last_shown": 1781000000, "last_shown_iso": "2026-06-10"}
  ],
  "n_creatives_first_page": 40
}
```

## Gotchas (dated)

- **2026-06-10** — Domain-text search matches on `target_domain`, which makes it collision-proof
  for generic brand names (searching `maximustribe.com` cleanly avoids the
  government-services "Maximus"). Prefer domains over names.
- **2026-06-10** — Zero creatives is a **clean result** (`ok: true`, empty list), not drift:
  legit zero-responses still carry `search_metadata`. Only missing-both ⇒ exit 3.
- **2026-06-10** — `advertisers[]` came back empty on domain searches in testing; the signal
  lives in `ad_creatives[]`. Advertiser identity rides each creative.
- **2026-06-20** — `--region` is a **numeric Google geo-target ID**, not an ISO code: SerpAPI
  400s on `region=US` ("Unsupported `US` region parameter."). The tool now maps the country
  codes we use (US→2840, GB/UK→2826, CA→2124, AU→2036) and passes a numeric value through
  as-is, so `--region US` works and any other region is reachable by its ID (full list:
  serpapi.com/google-ads-transparency-center-regions). Unknown codes fail with a clear error.
- **Recency rule of thumb for consumers:** treat "active" as any creative `last_shown` within
  ~35 days of `captured_at`; older-only creatives = "ran ads, not currently visible."

## Credits

1 SerpAPI search per invocation (same metered pool as `serpapi.py`).
