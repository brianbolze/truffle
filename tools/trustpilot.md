# trustpilot.py — Trustpilot profile capture

Scrapes one `trustpilot.com/review/<slug>` profile through **Firecrawl-stealth** and parses the
durable **State** of it: review count, TrustScore, rating distribution, a sample of the most-recent
reviews, and the raw integrity *flags* (paid profile, merged, asks-for-reviews, AI-assisted replies,
people-also-looked-at). Emits parsed JSON to stdout — no store write, no velocity, no trust verdict.

```bash
python3 tools/trustpilot.py honehealth.com
python3 tools/trustpilot.py https://www.trustpilot.com/review/hims.com   # full URL also accepted
python3 tools/trustpilot.py joinfridays.com --wait-ms 15000              # raise the Cloudflare wait if it doesn't clear
```

Auth: `FIRECRAWL_API_KEY` from the environment, falling back to a `.env` at the repo root (gitignored).

## The capture/judgment line (why this stays reusable)

The traction probe this tool was lifted from is mostly **judgment** — velocity formulas, solicitation
segmentation, hard-veto rules, "not measurable." **None of that is here.** The tool captures one
profile at one instant and stops. The split, concretely:

| The tool does (capture) | The caller does (judgment) |
|---|---|
| `review_count`, `trust_score`, `rating_distribution` at `captured_at` | **velocity** = Δcount / Δdays across two captures |
| `profile_flags.paid_profile / merged_profile / asks_for_reviews / ai_assisted_replies` (raw booleans) | the **integrity gate** — "merged + paid → not apples-to-apples; suppress velocity" |
| `people_also_looked_at` neighbors (raw list) | "these neighbors are off-vertical → **veto**" |
| `profile_state: removed` (a fact off the page) | "removed is a hard **red flag** for a brand claiming 400K patients" |
| `recent_reviews[]` verbatim + labels | template/duplicate detection, sentiment, SKU mentions |

It reports `paid_profile: true`; it never reports `trustworthy: false`. That boundary is what keeps it
usable for a plain "what's this brand's Trustpilot look like" read, not just the traction cohort.

## What it does now vs. what it could grow into

**Now — Trustpilot only.** One review surface, one profile per call.

**Could grow into** — other review surfaces are *scoped, latent* additions (each its own fetch + its
own shape-pinned parser, **not** a widening of this file into a general "reviews client"):

| Surface | Signal it would add | Capture path |
|---|---|---|
| Apple App Store / Google Play | app ratings, review velocity, version-pegged complaints | public RSS / iTunes API (no Firecrawl) |
| Google Business reviews | local/maps rating + count | SerpAPI `google_maps` (see [serpapi.md](serpapi.md) growth table) |
| reviews.io / ResellerRatings | alt third-party review aggregators | Firecrawl (likely same stealth shape) |
| on-site PDP reviews | first-party star ratings (Yotpo/Okendo widgets) | `/research-company` capture, not here |

Same discipline as serpapi: extend by adding a surface + its parser, not by overloading this one.

## The gotchas (most of the value)

These cost a probe (or a live bug) to learn. Carry them forward; don't relitigate them live.

- **Stealth alone is not enough — the 12s wait is load-bearing.** `proxy:"stealth"` by itself lands on
  the Cloudflare "Verifying your connection…" interstitial (charged ~5 credits, no data). Adding
  `actions:[{type:"wait",milliseconds:12000}]` lets the JS challenge resolve → ~**1 credit**, ~**29s**
  per page. If a page still returns the challenge, the tool raises (exit 2, re-runnable); `--wait-ms`
  raises the wait. (2026-05-06 feasibility; re-confirmed live 2026-06-08.)
- **⚠️ The distribution gotcha flipped.** The 2026-05-06 INVARIANT said star-distribution %s "aren't in
  the scraped markdown — compute them from a rolling sample." **As of 2026-06-08 they ARE** — the
  `## All reviews` block carries `5-star 93% … 1-star 3%` verbatim, so the tool parses them directly
  (`rating_distribution_source: "trustpilot_all_reviews"`). `<1%` is kept as the literal token, never
  invented into a number. **Fallback preserved:** if Trustpilot drops them again, `rating_distribution`
  goes null and the caller computes from `recent_reviews[].rating` (the old method) — that's why the
  per-review ratings are always emitted.
- **Two star-image vocabularies — don't conflate them.** `![Rated N out of 5 stars]` marks a *review*;
  `![TrustScore N out of 5]` marks the *company score* (and each people-also-looked-at card's score).
  The TrustScore alt-text also **rounds** (`TrustScore 5 out of 5` on a 4.8 profile) — so the real score
  is parsed from the bare decimal line, never the alt-text.
- **Featured vs feed.** The "Reviews shaping this summary" block near the top is cherry-picked and skews
  positive (it was 22/23 five-star on Hone). The tool samples only the `## All reviews` feed below it —
  the genuine most-recent reviews.
- **Profile state is data, not failure.** `not_found` (404), `removed` (Trustpilot pulled it —
  "goes against our guidelines"), and `empty` ("Be the first to review", 0 reviews) all exit **0** with
  the state named — mirroring serpapi's "AIO-absent is data." Only transport/challenge is exit 2; only a
  reshaped *active* page is exit 3. All four states verified live 2026-06-08
  (honehealth=active, getpetermd=removed, vitalityrx=not_found, getopt=empty).
- **Merged/paid profiles aren't apples-to-apples — but that's the caller's call.** Hims is
  `merged + paid + ai_assisted_replies` with an 85% negative-reply rate and a 3.0/"Average" score whose
  distribution (40/11/12/9/28) looks nothing like a solicited peer's (Hone 93/2/<1/<1/3). The tool
  surfaces every one of those flags raw; comparing a merged profile against an unmerged one is a mistake
  the *caller* must avoid. (Live 2026-06-08.)
- **Parser is version-pinned (`v1`); drift fails loud.** On an `active` profile that yields no count AND
  no score AND no reviews, the tool warns to stderr, sets `schema_drift`, suppresses the trust-bearing
  fields, and exits 3 — never parse-on into plausible-but-wrong State. Bump the version only on an
  *intentional* migration.

## Output shape

Conforms to the library's reserved envelope spine (`tool · source · captured_at · ok · input ·
schema_drift`, plus optional `parser_version · cost`); the Trustpilot payload sits beside it.

```jsonc
{
  // --- reserved envelope spine (tools/README.md) ---
  "tool": "trustpilot",
  "source": "trustpilot.com",                 // the SIGNAL origin; fetched via Firecrawl (see capture.via)
  "parser_version": "v1",                     // optional: this upstream is drift-prone
  "captured_at": "2026-06-08T17:08:10Z",      // THIS invocation's wall-clock — the caller diffs counts ACROSS these
  "ok": true,                                 // false only on schema drift; transport failures exit 2 (no stdout)
  "input": { "slug": "honehealth.com", "wait_ms": 12000 },
  "schema_drift": [],                         // non-empty -> ok:false, exit 3
  "cost": { "firecrawl_credits": 1 },         // optional: the source meters credits
  // --- payload, beside the spine ---
  "trustpilot_url": "https://www.trustpilot.com/review/honehealth.com",
  "profile_state": "active",                  // active | empty | removed | not_found
  "review_count": 11573,
  "reviews_last_12m": 5553,                   // null if Trustpilot doesn't show it
  "trust_score": 4.8,
  "rating_label": "Excellent",                // Excellent | Great | Average | Poor | Bad
  "rating_distribution": { "5": "93%", "4": "2%", "3": "<1%", "2": "<1%", "1": "3%" },
  "rating_distribution_source": "trustpilot_all_reviews",  // null when absent -> compute from recent_reviews
  "profile_flags": {
    "claimed": true,
    "paid_profile": true,
    "asks_for_reviews": true,                 // true | false | null (null = neither badge shown)
    "ai_assisted_replies": true,
    "merged_profile": false,
    "negative_reply_rate_pct": 97             // null when not stated
  },
  "people_also_looked_at": [                  // [] when none; survives even on empty/removed profiles
    { "name": "Maximus", "domain": "maximustribe.com", "trust_score": 4.4, "review_count_label": "975" }
  ],
  "recent_reviews": [                         // the `## All reviews` feed (most-recent), cap 30
    { "review_id": "6a26b8b7…", "rating": 5, "title": "Easy and thorough.", "body": "Easy and thorough.",
      "date_of_experience": "June 8, 2026", "posted": "2 hours ago",
      "verified": false, "unprompted": true,
      "reviewer_name": "Jason", "reviewer_country": "US", "reviewer_review_count": 3 }
  ],
  "recent_reviews_sample_size": 20,
  "capture": {                                // fetch provenance (named field — NOT the metered cost)
    "via": "firecrawl-stealth", "status_code": 200, "proxy_used": "stealth",
    "fetch_seconds": 28.9, "source_url": "https://www.trustpilot.com/review/honehealth.com",
    "markdown_chars": 29602
  }
}
```

On a non-active state the trust-bearing fields are null/empty and `profile_state` carries the story
(still `ok:true`, exit 0 — a pulled/missing profile is data):

```jsonc
{ "ok": true, "profile_state": "removed", "review_count": null, "trust_score": null,
  "recent_reviews": [], "people_also_looked_at": [], "schema_drift": [], "capture": { "status_code": 200, … } }
```

**Credits:** ~1 Firecrawl credit per profile when the wait clears (~29s). A blocked challenge wastes the
call (exit 2) — re-run or raise `--wait-ms`.
