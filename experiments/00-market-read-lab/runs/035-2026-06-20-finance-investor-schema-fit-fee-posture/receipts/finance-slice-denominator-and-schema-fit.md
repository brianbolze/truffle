# Receipt - Finance/Investor slice denominator + schema-fit field census

Supports the run's denominator reconciliation (union = 9, not ~16) and the per-subtype
schema-fit field census (which structured fields populate vs are empty-by-contract).

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5, C6, C7]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/profile.md` frontmatter (grep) | per-profile captured_at (2026-05-30…06-14) | local-store | derived | none | no | C1, C2 |
| S2 | blueowl-com/profile.md | 2026-05-30 | local-store / owned-official | primary | none | no | C2, C5 |
| S3 | spero-vc/profile.md | (per frontmatter) | local-store / owned-official | primary | none | no | C4 |
| S4 | sequoiacap/lsvp/firstround/thrivecap/standishspring profile.md `unverified_fields` | 2026-06-14 (most) | local-store | primary | none | no | C3 |
| S5 | runway-com, stripe-com profile.md | (per frontmatter) | local-store | primary | none | no | C6 |
| S6 | TAXONOMIES.md:19,72,108; SCHEMA.md:66,70 | repo HEAD | local-store / contract | primary | none | no | C7 |

## Method

1. `grep -rl '^primary_industry: Finance & Fintech' store/*/profile.md` → 9 files.
2. `grep -rl '^entity_type: Investor / Holding' store/*/profile.md` → 7 files; verified
   all 7 ⊂ the 9 (set difference: stripe-com, runway-com are the 2 non-investor Finance).
3. For each of the 9, extracted `entity_type`, `offering_category`, `portfolio_shape`,
   `business_model`, `primary_industry`, `description`, and `unverified_fields` from the
   frontmatter block (`awk` between the first two `---`), quoting verbatim — no
   re-derivation from body prose (MRL-002/009 guard).
4. Read TAXONOMIES.md / SCHEMA.md for the contracted `entity_type` value, the
   portfolio_shape empty-by-rule, and the 8-value `business_model` closed set.

## Evidence

- **Denominator:** Finance & Fintech = 9 {blueowl, firstround, lsvp, sequoiacap, runway,
  standishspring, stripe, spero-vc, thrivecap}. Investor/Holding = 7 (all ⊂ the 9).
  **Union = 9.** Scout contract's "~16" over-counted (it assumed the two sets were
  largely disjoint; they nest). Consulting & Professional Services (6) is a separate
  vertical, adjacent context only.
- **Exact-line hazard:** a naive `grep -h '^primary_industry: Finance & Fintech' | uniq`
  shows 4 distinct *lines* (6 value-only + 3 carrying inline `# comment` suffixes — the
  YAML value is clean, the difference is the comment). `grep -rl` (substring, per-file) is
  robust; an exact-line `==` match against the bare string under-counts by 3. Mirrors
  run-033 G1.
- **business_model census (7 allocators):** empty ×6 (firstround, lsvp, sequoiacap,
  standishspring, spero-vc, thrivecap), `Other` ×1 (blueowl). Fintech products: stripe
  = `Usage-based / Consumption`, runway = `Subscription`.
- **portfolio_shape census (7 allocators):** empty ×7 (empty-by-rule).
- **Fee/AUM disclosure (7 allocators):** on-site disclosed = blueowl ($315B AUM, own
  stat) + spero (Fund II $125M) ; flagged not-on-site/deep-research = sequoiacap, lsvp,
  firstround, thrivecap, standishspring (5/7).
- **Closed set check:** business_model = {Subscription, Transactional/One-time,
  Usage-based/Consumption, Marketplace/Commission, Freemium, Advertising,
  Services/Project-based, Licensing}. No value covers AUM management-fee + carried-interest.

## Limits

- n=9 and subtype-skewed (5/7 allocators are early/multi-stage VC). Cannot support a
  general "finance vertical" market claim; supports a schema-fit verdict + a subtype map.
- Cannot prove the store's 9 is representative of the real finance market (no external
  denominator drawn; store-only by contract). Absence of fee/AUM disclosure = "not found
  on the captured marketing pages," not "the firm has no fees."

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Finance slice union = 9 (7 investors ⊂ 9); ~16 estimate over-counted | S1 | whitespace-dirty industry strings |
| C2 | 6/7 allocators `business_model` empty, 1 `Other`; portfolio_shape empty 7/7 | S1, S2 | empty is contracted, not a coverage gap |
| C3 | 5/7 allocators flag AUM/fees/fund-size "not on marketing site (deep-research)" | S4 | market disclosure norm, not capture failure |
| C4 | spero discloses Fund II $125M, 2024 vintage; Fund I unstated | S3 | partial disclosure |
| C5 | blueowl discloses ~$315B AUM (own marketing stat) + business_model Other | S2 | self-reported, not independently verified |
| C6 | stripe = published usage-based; runway = quote-gated subscription | S5 | the 2 fintech products fit the schema cleanly |
| C7 | entity_type value + portfolio_shape empty-rule are contracted; no fee value in business_model set | S6 | the subtractive gate is by-design |
