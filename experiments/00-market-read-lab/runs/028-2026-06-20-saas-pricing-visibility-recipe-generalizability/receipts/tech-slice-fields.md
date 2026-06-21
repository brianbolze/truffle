# Receipt - Tech-slice business_model + price-visibility derivation

Supports the SaaS pricing-visibility landscape (C1, C2) and the token-substrate count (C3).

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: primary
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/<tech-co>/profile.md` frontmatter (`business_model`, `primary_industry`, `captured_at`) | 2026-05-31 (19) / 2026-06-04…06-18 (5) | store file (own-site capture) | primary | none | no | C1, C3 |
| S2 | `store/<tech-co>/profile.md` `What they offer` + Overview prose | same | store file | primary | none | no | C2 |
| S3 | `SCHEMA.md:99,142,147` (price-visibility token convention) | repo | local-store | primary | none | no | C3 |

## Method

1. Denominator: `grep -m1 '^primary_industry:' store/*/profile.md | grep Technology` →
   24 profiled Tech companies (count `profile.md`, not directories — MRL-001 run-027).
2. C1: `grep -m1 '^business_model:'` over the 24 → 15 Subscription / 6 Usage-based / 2
   Transactional / 1 Marketplace; all 24 non-empty.
3. C3: counted `[published]`/`[partial]`/`[on-request]` token lines per profile → only
   airtable(5), notion(9), waldo(4) non-zero; 21/24 zero. offerings.md present for
   airtable, notion, posthog, waldo = **4/24** (corrected by Loop-2 verifier from an
   earlier "+1" miscount; stripe/clerky/airbnb have offerings.md but are not Technology).
4. C2: read `What they offer`/Overview prose per company; classified price visibility as
   published (real price/rate card shown), partial (price shown but top tier gated), or
   on-request (no public price, quote/contact-sales). Prose-read, not field-lookup,
   because the structured token is absent for 21/24.

## Evidence

- business_model (verbatim): Subscription ×15 (airtable, alpha-sense, clari, cloudflare,
  delighted, dovetail, gong, granola-ai, linear-app, listenlabs-ai, notion, openai,
  qualtrics, typeform, usertesting); Usage-based ×6 (aws-amazon, datadoghq, posthog,
  snowflake, twilio, waldo-fyi); Transactional ×2 (apple, casio); Marketplace ×1 (upwork).
- Published-price prose: cloudflare ($0/$20/$25/$200/$250/mo), linear ($10/$16/user),
  notion ($8/$10/mo), typeform ($28–$379/mo), twilio (from $15, pay-as-you-go),
  posthog ("published end-to-end", from $0.00005/event), snowflake ("per compute credit
  by edition"), aws (pay-as-you-go), datadog (usage rates), delighted ($19–$249/mo),
  airtable ($120/$150/mo), apple (from $599/$1099), upwork (commission).
- On-request prose: clari ("quote-priced"), alpha-sense ("no public pricing / contact
  us"), gong ("quote"), qualtrics ("custom / tailored per suite"), usertesting ("quote /
  contact us"), listenlabs ("no public pricing").
- Token count: 3/24 profiles carry the price-visibility token; the 3 are 3 of the 4 with
  offerings.md (posthog has offerings.md but 0 tokens) and were captured after the 05-31
  batch (06-17/06-04/06-18).

## Limits

- Denominator is an industry-grep floor (may miss tech-adjacent cos under other
  industries; excludes stubs). Not a SaaS census.
- 19/24 captured 2026-05-31 — price *points* may be stale; the *visibility posture* is
  structurally stable.
- Price-visibility classification is a read-time Judgment from prose (no structured token
  to verify against for 21/24); the published/on-request split is a labeled interpretation.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | business_model filled 24/24, splits 15/6/2/1 | S1 | floor denominator |
| C2 | ~14 publish / ~6 quote-gated; visibility tracks GTM | S2 | read-time Judgment from prose |
| C3 | universal price-visibility token populated 3/24; offerings.md 4/24 | S1, S3 | substrate gap, not schema defect |
