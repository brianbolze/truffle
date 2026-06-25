# Receipt - usage-based dev-infra cohort, verbatim pricing, token presence

Supports the cohort draw, the verbatim metered-rate table, the cohort-key behavior, and the
price-visibility-token presence/vintage claims.

```yaml
receipt_type: store-query
created: 2026-06-24
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `grep -rl "business_model: Usage-based" store/*/profile.md` | 2026-06-24 read | store query / derived | derived | none | no | C3 |
| S2 | store/datadoghq-com/profile.md:37,54-64; site_notes:17 | captured 2026-05-31 (schema 2.2) | owned/official → store file | primary | none | no | C1, C2, C4 |
| S3 | store/snowflake-com/profile.md:29,53,66-71 | captured 2026-05-31 (2.2) | store file | primary | none | no | C1, C2, C4 |
| S4 | store/twilio-com/profile.md:56,59-62,67 | captured 2026-05-31 (2.2) | store file | primary | none | no | C1, C2, C4 |
| S5 | store/posthog-com/profile.md:36,64-73; offerings.md | captured 2026-06-16 (2.6) | store file | primary | none | no | C1, C2, C4 |
| S6 | store/stripe-com/profile.md:62-66,74-75 | captured 2026-06-04 (2.5) | store file | primary | none | no | C1, C4, C5 |
| S7 | store/aws-amazon-com/profile.md:57,65,69-77 | captured 2026-05-31 (2.2) | store file | primary | none | no | C1, C2 |
| S8 | SCHEMA.md:99,142 (price-visibility token convention) | contract reference | contract doc | primary | none | no | C4 |

## Method

1. `grep -rl "business_model: Usage-based" store/*/profile.md` → 8 hits: datadoghq, snowflake, stripe,
   twilio, posthog, aws, blueenergy, waldo. Excluded blueenergy (energy) + waldo (small app) as non-infra
   by hand; the remaining 6 are the cohort.
2. For each member, read the frontmatter (`business_model`, `offering_category`, `schema_version`,
   `captured_at`) and the `What they offer` section for verbatim `/pricing` rates.
3. Counted price-visibility tokens per member: `grep -oiE "\[published\]|\[partial\]|\[on-request\]"`
   over `profile.md` (and `offerings.md` for posthog).

## Evidence

- **Verbatim billing units (no two shared):** Datadog `"$15 per host"`, `"$0.10 per ingested GB"`;
  Snowflake `"$2.00–$4.00 / per credit"`, `"$23.00 per TB / per month"`; Twilio `$0.0083`/SMS,
  `$1`/active-user-hour; PostHog `"$0.00005/event"`, `"$0.005/recording"`; Stripe `"2.9% + 30¢ per
  successful transaction"`; AWS utility, *no single rate quoted* (`"pay for the services you consume"`).
- **Token counts:** Stripe 23 `[published]` + 2 `[on-request]`; datadoghq/snowflake/twilio/aws **0**
  (schema 2.2, predate the 2.3 token convention); posthog **0** on profile.md *and* offerings.md (2.6).
- **Schema vintage:** 4/6 are schema 2.2 (pre-token); stripe 2.5, posthog 2.6 (post-token).

## Limits

- A `grep` cohort draw is only as complete as the `business_model` tagging — there may be metered
  businesses tagged primarily as something else (e.g. Notion, `Subscription` + usage-credits layer), so
  the cohort is *pure-play metered*, not *all metered-revenue* (see read G2).
- Captured rates are dated point-in-time snapshots from volatile `/pricing` pages, not durable prices.
- Token absence = "predates convention" per SCHEMA.md:99, **not** `[published]` — this receipt asserts
  absence-of-token, never absence-of-price.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Verbatim metered rates present for 5/6 (AWS philosophy-grain) | S2–S7 | Dated snapshots |
| C2 | No two brands share a billing unit → not cost-comparable | S2–S7 | Comparability ceiling is market structure |
| C3 | `business_model: Usage-based` is a clean positive cohort key | S1 | Coarse; pulls 2 non-infra; misses hybrids |
| C4 | Price-visibility token on only 1/6 (vintage, not opacity) | S2–S6, S8 | Absent ≠ published |
| C5 | Stripe = L006 non-trap (%-of-volume published to its paying side) | S6 | Single entity; confirms run-037 DR3 scope |
