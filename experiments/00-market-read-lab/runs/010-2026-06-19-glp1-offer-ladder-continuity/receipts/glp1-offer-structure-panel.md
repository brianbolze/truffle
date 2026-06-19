# Receipt - GLP-1 offer-structure panel

Per-brand classification of entry-offer shape, commitment/continuity lever, membership wedge, and price-visibility timing for the store's GLP-1-anchored cohort. Supports the read's table-stakes and differentiation claims.

```yaml
receipt_type:          store-query
created:               2026-06-19
evidence_mode:         store-only
source_grade:          derived
source_family:         local-store
spend_note:            none
snippet_only:          no
claim_ids_supported: [C1, C2, C3, C4, C5, C6]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/telehealth.md` frontmatter (`anchor_category: GLP-1`) | 2026-05-30…06-18 | store file | primary | none | no | C1 |
| S2 | `store/brellohealth-com/offerings.md` (`site_notes` + Portfolio + Visibility rule) | 2026-06-04 | store file | primary | none | no | C2,C4,C5,C6 |
| S3 | `store/eden-health/offerings.md` (Visibility rule, verbatim membership footnote) | 2026-06-03 | store file | primary | none | no | C3,C4 |
| S4 | `store/hims-com/offerings.md` (Visibility rule) | 2026-06-18 | store file | primary | none | no | C3,C4 |
| S5 | `store/ro-co/offerings.md` (Portfolio + Visibility) | 2026-06-18 | store file | primary | none | no | C3,C4 |
| S6 | `store/ivimhealth-com/offerings.md` (`site_notes`) | 2026-06-04 | store file | primary | none | no | C3 |
| S7 | `store/home-medvi-org/offerings.md` (Visibility) | 2026-06-04 | store file | primary | none | no | C3,C4 |
| S8 | `store/tryshed-com/offerings.md` (Portfolio) | 2026-06-04 | store file | primary | none | no | C3 |
| S9 | `store/joinfound-com/offerings.md` (`site_notes` + Portfolio) | 2026-06-04 | store file | primary | none | no | C3,C5 |
| S10 | `store/telolife-com/offerings.md` (`site_notes` + Portfolio) | 2026-06-18 | store file | primary | none | no | C5,C6 |
| S11 | `store/{henrymeds,mydrhank,joinfridays,effecty,directmeds,remedymeds,goodlifemeds}-com/offerings.md` | 2026-06-03…06-04 | store file | primary | none | no | C2,C3,C6 |
| S12 | `store/{ivyrx,joinamble,noom}-com/offerings.md` | 2026-06-04…06-18 | store file | primary | none | no | C4,C5 |

## Method

Cohort = `grep -l "anchor_category: GLP-1" store/*/telehealth.md` → 19 dirs that also carry `offerings.md` (S1). For each, read the `site_notes` frontmatter + `## Portfolio overview` + the `Visibility rule` paragraph and extracted four offer-structure attributes **verbatim from those captured fields** (no re-derivation from marketing prose): entry-offer shape, commitment/continuity lever, whether a mandatory separate membership stacks on the GLP-1 med, and when the buyer first sees the real all-in price. Membership figures quoted as captured. Generalist GLP-1 lines inside `multi/none` brands were **not** pulled into this panel (partial-denominator note in the read).

## Evidence

| Brand | Entry-offer shape (GLP-1) | Commitment / continuity lever | Mandatory separate membership on the GLP-1? | When you see the real all-in |
|---|---|---|---|---|
| brellohealth | med-included all-in 3-mo plan (consult+med+supplies+app+classes+community) | **3-mo total charged upfront**, auto-renew "every 10 weeks"; "$X/Month" = total÷3 | no (one SKU adds Lumen $19.90/mo) | **buy-first** — price shown pre-intake ("No Intake Form Required Before You Pay") |
| telolife | med-included all-in cash, single GLP-1 | 3/6/9/12-mo bundles **prepay** the same $199/mo rate (no per-mo discount) | no | **fully published**, no intake wall |
| effecty | med-included, "price-transparent, no-membership" | 1/3/12-mo, longer plan steps price down; "same price at every dose" | no | published on grid |
| henrymeds | flat-monthly all-in (visit+med+supplies+shipping), "no separate membership fee" | flat monthly | no | GLP-1 "$179/mo" family floor; exact dose **intake-gated** |
| mydrhank | "From $X/mo" floor, free consult, "no membership tier, no separate consult fee" | floor; binding plan set in intake | no | floor shown, real all-in set in **gated intake** |
| joinfridays | all-in "no membership fees, no sign-up fees, no lab fees" | annual floor vs month-to-month, both shown | no | compounded "starting at" floor moves w/ dose; brand insurance-priced |
| directmeds | all-inclusive monthly, cash-pay, no membership | monthly | no | listing↔PDP prices disagree on GLP-1 → partial |
| remedymeds | single GLP-1, all-in (med+unlimited care+free labs+shipping+community) | month-to-month "membership" (manual calls recurring charge a "membership"; homepage says "No Memberships or Hidden Fees") | self-billed all-in, not a stacked separate fee | $299/$399 published; microdose/branded on-request |
| goodlifemeds | auto-renew subscription; one bundled price covers consult+med+shipping | monthly | no | WL published; sexual-health/hair revert to "Starting at" floors |
| eden-health | **med-only price + mandatory Eden Membership** | monthly | **yes — $39 first month, auto-renews $99/mo**; "Medication is not available without a membership" | med shown; membership stacked → every line partial |
| hims | other lines bundle consult; **weight-loss billed separately** | monthly | **yes (weight-loss only) — $39 first month → $149/mo**; "Medication is not available without a membership" | WL partial; other lines published |
| ro-co | **membership wrapping a separately-billed med roster** | monthly Ro Body membership $39/$74/$149 | **yes** | GLP-1 partial: promo first-month shown, all-in = dose ladder **+** membership; ladders behind "See pricing details" expander |
| ivimhealth | med floor + separate program fee | monthly | **yes — $74.99/mo program fee + "membership required thereafter"** | med floor + program fee |
| home-medvi | mixed: compounded "No membership or hidden fees" / branded membership | monthly | **branded SKUs yes — "$99 Membership + Medication Cost"** | compounded $179→$299 published; branded med cost intake-gated |
| tryshed | multi-line; compounded sema/tirz value wedge | 1/6/12-mo plan grids (per-mo drops w/ longer prepay) | **partial — Foundayo + Zepbound slug add $125/mo Shed Membership** | category cards over-state vs PDP 1-mo tier; some lines partial |
| joinfound | membership program over ~16-med toolkit; compounded = flat "one flat price, no separate membership" | 12-mo upfront plan ($149/mo insurance / $199/mo cash); $17/mo deep-discount in-network line | **yes for the program/brand lane; compounded lane has none** | compounded flat; brand/insurance lines gated → mostly partial/on-request |
| noom | program-tier subscription (GLP-1Rx / Plus / Microdose); clinician-selected med inside | program subscription | program-level fee (not per-drug) | per-drug **on-request**; published program floor |
| ivyrx | almost everything partial; per-month floors | "$49.75/week = $199/mo (paid upfront with a 12-month plan)" — lowest rate assumes **12-mo prepay** | no | per-month floor; GLP-1 also scales by dose ("4 doses/month") |
| joinamble | subscription therapeutics + NEW one-time medkits | plan-length table (12-mo cheapest → 1-mo dearest), "same price, every dose"; medkits = one-time upfront | no | PDP plan table |

## Limits

- **Partial denominator** — 19 GLP-1-*anchored* brands with `offerings.md`; generalist GLP-1 lines inside `multi/none` brands (and any GLP-1-anchored brand lacking `offerings.md`) are not scored. Not a census.
- **Promo/A-B-volatile prices** — nearly every `site_notes` flags struck-through/countdown/first-month promo or A/B engines (brello Deadline Funnel, ro ro-experiments, hims, goodlife SUMMER30, medvi). Every figure is a **captured floor ≤ ~3 weeks old**, not a live quote.
- **Membership semantics vary** — "membership" means a mandatory separate stacked fee (eden, ivim), a wrapper over separately-billed meds (ro), a marketing word for an all-in recurring charge (remedy), or a line-specific add-on (hims WL, shed Foundayo). The C3 split is a Judgment over these distinctions, not a clean field.
- Cannot prove these are the *market's* table stakes — only the captured cohort's.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 19 GLP-1-anchored brands carry `offerings.md`; partial denominator | S1 | not a census |
| C2 | All-in bundling of consult+med+supplies+shipping into one recurring price is the near-universal compounded-GLP-1 entry offer | S2,S11 | promo-volatile prices |
| C3 | Cohort splits into med-included-flat vs med-priced-plus-mandatory-membership business models | S3,S4,S5,S6,S7,S8,S9,S11 | "membership" semantics vary [J] |
| C4 | The "$X/month" headline rarely equals what you pay — three mechanisms (upfront-÷-N, stacked membership, dose-floor) | S2,S3,S4,S7,S12 | [J] over verbatim site_notes |
| C5 | Commitment laddering (longer prepay → lower per-month) is table stakes; differentiation is real-discount vs same-rate-prepay | S2,S9,S10,S12 | telolife prepays at flat rate |
| C6 | Fully published, no-intake-wall all-in pricing is the cohort's real whitespace; buy-first is an outlier | S2,S10,S11 | small n on the "published" pole |
