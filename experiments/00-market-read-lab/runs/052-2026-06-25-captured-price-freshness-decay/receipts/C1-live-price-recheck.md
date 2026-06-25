# Receipt - Live price re-check vs captured State

Supports the freshness-decay read: live vendor-page headline prices re-checked against
each brand's already-captured `offerings.md`/`profile.md` price, with capture age.

```yaml
receipt_type: external-source
created: 2026-06-25
evidence_mode: bounded-live
source_grade: primary
source_family: owned/official
spend_note: paid-credit
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | https://ouraring.com/ | live fetch, Firecrawl cachedAt 2026-06-25T06:55Z (fresh) | owned/official / vendor marketing | primary | paid-credit (1) | no | C1 |
| S2 | https://www.eightsleep.com/product/pod-cover/ | live fetch, Firecrawl cachedAt 2026-06-24T02:05Z (**cache hit — not a true 06-25 re-check**) | owned/official / vendor PDP | primary | paid-credit (1) | no | C2 |
| S3 | https://www.onepeloton.com/exercise-bikes | live fetch, Firecrawl cacheState `miss` (fresh 2026-06-25) | owned/official / vendor PLP | primary | paid-credit (1) | no | C3, C4 |
| L1 | store/ouraring-com/offerings.md (captured_at 2026-06-24) | store clock 2026-06-24 | local-store | derived | none | no | C1 |
| L2 | store/eightsleep-com/offerings.md (captured_at 2026-06-24) | store clock 2026-06-24 | local-store | derived | none | no | C2 |
| L3 | store/onepeloton-com/offerings.md (captured_at 2026-06-10) | store clock 2026-06-10 | local-store | derived | none | no | C3, C4 |

## Method

For each panel brand, read the captured headline price + `captured_at` from the store
first (L1–L3), then fetched the matching live vendor marketing page as plain markdown
(`formats:["markdown"]`, `onlyMainContent:true`; no PDF, no JSON-extraction) and compared
the live displayed price to the captured value. Stop rule fired at 3 open-page-verifiable
brands (oura, eightsleep, peloton); Therabody + Hyperice were **not** re-checked (panel
contract: do not add brands to chase a rounder number once ≥3 verify). Spend: 3 paid
credits of an 8-credit ceiling; 3 outside sources of a 5-source ceiling.

## Evidence

- **Oura (1-day age).** Captured (06-24): Ring 4 "From $244" (flash sale), Ring 4 Ceramic
  "$279" (cross-sell). Live (06-25): homepage hero "Take up to 44% off Oura Ring 4 / Flash
  Sale and free shipping **through June 26th**"; "Oura Ring 4 — From $244"; "Oura Ring 4
  Ceramic — $279". → **Match. The dated flash sale (ends June 26) is still live on June 25.**
- **Eight Sleep (1-day age, cache caveat).** Captured (06-24): Pod 5 Queen "$2,749
  (~~$2,999~~)", "4th July Sale". Live fetch returned Pod 5 "$2,749 / $2,999 / $250 off"
  and "4th July Sale" → **Match — but the fetch was a Firecrawl cache hit dated 2026-06-24**,
  i.e. the same day as the original capture, so it is not an independent 06-25 re-check.
- **Peloton (15-day age).** Captured (06-10): Original Bike (refurbished) "Refurbished from
  **$695** (~~$1,145~~) … limited-time, ends **June 15, 2026**"; refurb Bike+ "$1,395";
  Cross Training Bike+ MSRP "$2,695". Live (06-25, fresh): no "$695" anywhere; the Affirm
  footnote prices the "Refurbished Peloton Bike … Based on a price of **$1,145**"; refurb
  Bike+ "Refurbished from $1,395"; Cross Training Bike+ "From $2,695". → **Refurb Original
  Bike DIVERGED: the $695 promo expired (ended June 15, 10 days before re-check); live is
  back to $1,145 (the struck-through regular price at capture). Durable MSRP ($2,695) and
  refurb Bike+ ($1,395) MATCH.**

## Limits

- Each live re-check is itself a point-in-time snapshot; a price differing today is "a
  different/expired promo," not a measured decay *rate*. n=3 brands, mixed ages (2×1-day,
  1×15-day) — too thin for a rate.
- S2 is a Firecrawl **cache hit** dated 06-24, so the Eight Sleep "unchanged" finding is
  trivially same-day, not a true 15-day-or-even-1-day independent re-check. A freshness
  test run through a cache can silently fail to actually re-fetch.
- Therabody + Hyperice (both captured 06-24, mid-Prime-Day) were not re-checked, so the
  Prime-Day-sale persistence question is unverified for them.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Oura's captured headline prices ($244 Ring 4, $279 Ceramic) still match live at 1-day age; the dated flash sale (ends Jun 26) is still running. | S1, L1 | 1-day age — minimal time to decay. |
| C2 | Eight Sleep's captured Pod 5 price ($2,749/$2,999) matches live. | S2, L2 | Cache hit dated 06-24 — not an independent 06-25 re-check. |
| C3 | Peloton's captured refurb Original Bike promo ($695, "ends June 15") has expired; live price reverted to $1,145 at 15-day age. | S3, L3 | The $1,145 live figure is read from the Affirm financing footnote ("based on a price of $1,145"), not a product card. |
| C4 | Peloton's durable MSRPs / non-dated refurb prices (Cross Training Bike+ $2,695; refurb Bike+ $1,395) match live at 15-day age. | S3, L3 | A stale Affirm footnote ($1,995 basis for refurb Bike+) persists live, as it did at capture. |
