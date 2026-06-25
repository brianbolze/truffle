# Receipt - External named-set + store diff (wearable/sleep/recovery trackers)

Supports the coverage-radar denominator: the externally-named "best 2026 tracker" set
from two independent editorial listicles + SERP leads, and its token-match diff against
the store's captured cohort.

```yaml
receipt_type: source-panel
created: 2026-06-25
evidence_mode: bounded-live
source_grade: secondary
source_family: SERP/listicle
spend_note: paid-credit
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | firecrawl_search "best fitness and sleep tracker 2026 wearable buying guide" (searchId 019efe3f-7ef2-7149-a6d1-2153698dd6b6) | 2026-06-25 | SERP / search result | direction-finding | paid-credit (2, refunded 1 → net 1) | yes (snippets) | C1, C4 |
| S2 | https://www.sleepfoundation.org/best-sleep-trackers | scraped 2026-06-25; page modified 2026-04-22 | editorial best-of listicle (sleep axis) | secondary | paid-credit (1) | no | C1, C2, C3 |
| S3 | https://www.wareable.com/fitness-trackers/the-best-fitness-tracker | scraped 2026-06-25 (Firecrawl cache 2026-06-23); page modified 2026-06-02 | editorial best-of listicle (fitness axis) | secondary | paid-credit (1, cache hit) | no | C1, C2, C3, C4 |
| S4 | store/ token-match (`ls store/` grep major tracker brands) | store clock per profile (oura/whoop/eightsleep 2026-06-24; apple 2026-05-31) | local-store | primary (store state) | none | no | C1, C3 |

Failed (not billed, not counted as a read): https://www.pcmag.com/picks/the-best-fitness-trackers
— Firecrawl returned "we do not support this site." Substituted wareable.com for the
fitness-axis list.

## Method

L001 coverage-radar recipe applied to a consumer-hardware category: 1 SERP query → 2
independent editorial best-of listicles (one sleep-axis, one fitness-axis, chosen to
span the category's known blur) → cross-source intersection of named brands → token-match
diff against `ls store/` for each named brand. Plain-markdown scrapes only; no JSON
extraction, no PDF, no funnel. Stopped after the 2nd editorial list corroborated a stable
named set (stop rule fired).

## Evidence

**S2 — Sleep Foundation "Best Sleep Trackers of 2026" (sleep axis).**
Top picks: Oura Ring 4, Eight Sleep Pod 5 Cover, Bía Smart Sleep Mask, Muse S Athena, RISE App.
In-depth review set also names: Withings (Sleep Tracking Mat), Whoop, Apollo Neuro, Apple
Watch, SLEEPON Go2sleep, Wellue O2Ring.

**S3 — Wareable "Best fitness tracker 2026" (fitness axis).**
Picks: Hume Band 2.0, Hume Band, Fitbit Air, Whoop 5.0, Withings ScanWatch Light, Oxiline
Pressure XS Pro, Oxiline Pulse XS Pro, Xiaomi Smart Band 10, Fitbit Charge 6, Huawei Watch
Fit 4, Amazfit Active 2, Amazfit Bip 6. Also names Garmin, Apple Watch, Google/Pixel,
Samsung, Ultrahuman Ring Pro in body/nav/related.
Vendor-bias flag: Hume Band is ranked #1–#2 and the page carries "Buy 1 Hume Band, Get 1
free" + "50% OFF … code WRBL20" + affiliate links — Hume is an advertiser on this page.

**S1 — SERP snippet leads (direction-finding only, not decision-grade):**
Consumer Reports → "Amazfit, Apple, Fitbit, Google, and Samsung"; Wired → "Garmin
Vivoactive 6 … Oura"; PCMag → "Fitbit Air"; Circular → "Circular Ring 2, Whoop 5.0,
Withings Sleep Analyzer, Fitbit Charge 6" (Circular ranks its own ring #1 — vendor bias);
Wirecutter → "Fitbit Inspire 3".

**S4 — store token-match.** `ls store/` matches for tracker brands: apple-com,
eightsleep-com, ouraring-com, whoop-com. No match for fitbit / garmin / withings /
samsung / amazfit / google / ultrahuman / huawei / xiaomi / hume / polar / coros /
zepp / circular / muse / bia / sleepon.

**Cross-source intersection → store diff:**

| Brand | SleepFound (S2) | Wareable (S3) | SERP leads (S1) | ≥2 independent? | In store (S4)? |
|---|---|---|---|---|---|
| Oura | ✓ top pick | mentioned | Wired, Circular | yes | ✓ captured |
| Whoop | ✓ review | ✓ pick | Circular | yes | ✓ captured |
| Apple Watch | ✓ review | mentioned | Consumer Reports | yes | ✓ captured |
| Eight Sleep | ✓ top pick | — | — | sleep-axis only | ✓ captured |
| **Fitbit (Google)** | implied/review-set | ✓ Air + Charge 6 | CR, Circular, Wirecutter, PCMag | **yes** | ✗ **missing** |
| **Garmin** | — | ✓ mentioned/related | Wired top pick | **yes** | ✗ **missing** |
| **Withings** | ✓ review (mat) | ✓ ScanWatch Light | Circular | **yes** | ✗ **missing** |
| **Samsung (Galaxy)** | — | ✓ nav/category | Consumer Reports | **yes** | ✗ **missing** |
| **Amazfit** | — | ✓ Active 2 + Bip 6 | Consumer Reports | **yes** | ✗ **missing** |
| Google / Pixel Watch | — | ✓ (Fitbit parent) | Consumer Reports | yes | ✗ missing |
| Ultrahuman | — | ✓ Ring Pro (related) | — | single-source | ✗ missing |
| Huawei | — | ✓ Watch Fit 4 | — | single-source | ✗ missing |
| Xiaomi | — | ✓ Smart Band 10 | — | single-source | ✗ missing |
| Hume | — | ✓ #1–2 (advertiser) | — | single-source + vendor-biased | ✗ missing |
| Muse / Bía / RISE / Apollo Neuro / SLEEPON / Wellue | ✓ (S2 only) | — | — | single-source / niche | ✗ missing |

## Limits

- Two editorial lists + SERP snippets is a light panel, not a census: brands named by
  only one list (Huawei, Xiaomi, Hume, Muse, Bía, Ultrahuman) are leads, not a
  corroborated denominator. SERP rows are snippet-grade direction-finding.
- The "≥2 independent" column mixes one full-scrape corroboration (S2/S3) with
  snippet-grade SERP leads (S1); treat the high-confidence missing-set as
  Fitbit/Garmin/Withings/Samsung/Amazfit/Google, each named by both a full editorial
  list and ≥1 SERP source.
- PCMag (the planned fitness-axis list) was unscrapeable; wareable.com substituted. A
  different 2nd list could shift the single-source tail.
- "Missing" = not captured in the store as of 2026-06-25; says nothing about whether the
  brand should be captured.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | The store holds 4 of the externally-named tracker brands (Oura, Whoop, Apple, Eight Sleep) and lacks the mainstream-volume majority (Fitbit, Garmin, Withings, Samsung, Amazfit, Google). | S1–S4 | Light panel; missing-set high-confidence only for the ≥2-source brands. |
| C2 | The category splits into sub-categories with near-disjoint listicle populations: the sleep-axis list (Oura, Eight Sleep, Bía, Muse, RISE) and the fitness-axis list (Hume, Fitbit, Huawei, Amazfit, Garmin) intersect on almost nothing but Oura/Whoop. | S2 vs S3 | Two lists; a 3rd could overlap more. |
| C3 | The store's "wearable/recovery" cohort and the editorial "tracker" category only overlap on 4 brands; the store's Peloton/Therabody/Hyperice/Nike appear in neither tracker list (different category). | S2, S3, S4 | Category-boundary judgment, not a defect. |
| C4 | Listicle rankings carry vendor/affiliate bias (Wareable ranks advertiser Hume #1–2; Circular ranks its own ring #1) even where the named set corroborates. | S1, S3 | L004 instance. |
