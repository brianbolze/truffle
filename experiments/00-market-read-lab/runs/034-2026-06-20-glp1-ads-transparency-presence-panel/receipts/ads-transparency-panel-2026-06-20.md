# Receipt - GLP-1 ads-transparency presence panel

Google Ads Transparency Center captures for a 6-brand GLP-1 panel, supporting the
run's presence/recency/tenure/format claims and the push-vs-demand boundary.

```yaml
receipt_type: source-panel
created: 2026-06-20
evidence_mode: bounded-live
source_grade: primary
source_family: ads/social
spend_note: paid-credit
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5, C6, C7]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `receipts/ads/hims.com.json` (SerpAPI google_ads_transparency_center, text=hims.com, region US) | 2026-06-21T00:06Z | ads/social / primary | primary | paid-credit (1) | no | C1,C2,C3,C5 |
| S2 | `receipts/ads/ro.co.json` | 2026-06-21 | ads/social | primary | paid-credit (1) | no | C1,C2,C3,C4,C5 |
| S3 | `receipts/ads/henrymeds.com.json` | 2026-06-21 | ads/social | primary | paid-credit (1) | no | C1,C2,C5,C6 |
| S4 | `receipts/ads/remedymeds.com.json` (clean zero) | 2026-06-21 | ads/social | primary | paid-credit (1) | no | C1,C7 |
| S5 | `receipts/ads/eden.health.json` (clean zero) | 2026-06-21 | ads/social | primary | paid-credit (1) | no | C1,C7 |
| S6 | `receipts/ads/lifemd.com.json` | 2026-06-21 | ads/social | primary | paid-credit (1) | no | C1,C2,C6 |
| S7 | `ls -d store/*/signals/ads_transparency` (store coverage) | store, 2026-06-20 | local-store | derived | none | no | C5 |

## Method

Panel = 6 high-recognition DTC GLP-1 domains drawn from the store GLP-1-anchored cohort
(`grep -rl 'anchor_category:.*GLP-1' store/*/telehealth.md` → 25 brands), domain-keyed and
resolved from each `store/<dir>/profile.md` `domain:` line. One
`tools/ads_transparency.py <domain> --region US` call per domain (6 SerpAPI searches, 6
credits — at the planned ceiling, 0 over). Per-domain stats derived by parsing
`ad_creatives[]`: `n_creatives_first_page`, distinct advertiser legal-names, min
`first_shown_iso` (tenure), max `last_shown_iso` (recency), distinct `format`. "Active"
= max `last_shown` within 35 days of `captured_at` (2026-06-21), per the tool's recency
rule. Store ads coverage = count of `store/*/signals/ads_transparency` dirs.

## Evidence

| Domain | n_first_page | Advertiser (legal) | First shown | Last shown | Active ≤35d | Formats |
|---|---|---|---|---|---|---|
| hims.com | 14 | Hims, Inc. | 2022-06-29 | 2026-06-20 | YES | image, text |
| ro.co | 40 (page cap) | Roman Health Ventures Inc. | 2023-02-16 | 2026-06-20 | YES | image, text, video |
| henrymeds.com | 2 | ADONIS HEALTH INC. | 2024-01-02 | 2025-11-24 | no (~209d) | image, text |
| remedymeds.com | 0 | — | — | — | ZERO | — |
| eden.health | 0 | — | — | — | ZERO | — |
| lifemd.com | 1 | LifeMD, Inc. | 2022-07-14 | 2025-08-16 | no (~309d) | text |

Store-wide ads coverage: **1 / 130** profiles carry a `signals/ads_transparency` dir
(`store/waldo-fyi`); **0** GLP-1 brands. Other signal types: wayback 47, trustpilot 20,
sec_edgar 20, trends 5, serpapi 2, exa_similar 2.

## Limits

- **Push/resourcing, not demand.** Running ads proves budget + an active Google
  acquisition motion; it says nothing about conversion, performance, or whether the brand
  is winning. Do not rank "who's doing best" from this.
- **First-page only.** `n_creatives_first_page` is a capped first-page count (ro.co's 40
  is the cap), NOT total ad volume. Only presence / recency / tenure / format are safe.
- **Zero ≠ not advertising.** remedymeds.com / eden.health returned clean zero = *not
  visible on Google Ads Transparency for that exact target_domain* — they may advertise on
  Meta (different surface), or land ads on a different domain than the store's `domain:`
  key. `eden.health` is itself an uncertain ad-landing domain for the "Eden" GLP-1 brand.
- **Advertiser legal-name ≠ brand.** ro→"Roman Health Ventures Inc.", henrymeds→"ADONIS
  HEALTH INC.", which is why domain-keyed search (not name search) was used.
- **Single capture, single region (US), single point in time.** No time-delta; tenure is
  the only longitudinal axis and it is first/last-shown bookends, not a continuous run.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | The ads-transparency surface returns a readable presence/recency/tenure result for each of the 6 panel domains (incl. clean zeros). | S1–S6 | Panel of 6, not the ~19–25 cohort. |
| C2 | 4/6 have advertising tenure on record (hims/ro since 2022–23; lifemd 2022; henrymeds 2024). | S1,S2,S3,S6 | Tenure = first/last bookend, not continuity. |
| C3 | 2/6 (hims, ro) are actively visible (last_shown 2026-06-20); 2/6 (henrymeds, lifemd) ran ads but are now quiet on Google. | S1,S2,S3,S6 | "Active" = last_shown ≤35d. |
| C4 | ro.co shows the richest format mix (image+text+video) and hits the first-page cap (40). | S2 | 40 is a cap, not a volume. |
| C5 | The store cannot see this today: 1/130 profiles carry an ads signal; 0 GLP-1 brands. | S7,S1 | Tool exists + resolves; coverage ~0. |
| C6 | Long tenure ≠ currently active: lifemd advertising since 2022 but last_shown 2025-08 (~309d quiet). | S6,S3 | Google surface only. |
| C7 | 2/6 clean zeros are "not visible on this surface," not "not advertising." | S4,S5 | Could run on Meta / a different domain. |
