# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients, capabilities,
and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | The PostHog token-absence claim was *underspecified* in the read: its `offerings.md` is on the module-schema track (v1.2), which predates the token convention independently — a routine module-backfill gap, not part of the "post-2.3 untokenized" tell. The real signal is the v2.6 *profile* being untokenized. (Corrected in read.md / run-notes G1.) | posthog profile schema 2.6 untokenized; offerings schema 1.2; SCHEMA.md:99 | DR1 · gap |
| **Structure** | `business_model` single-valued lossiness is now n=2 named runs (run-037 S1 wearable hybrids; run-044 G2 Notion's subscription+credits). Both land the same lightest-path (ranked multi-select) and both correctly stay no-build. Pressure is on TAXONOMIES doc clarity, not a new field. | run-037 S1; run-044 G2; TAXONOMIES:76 | G2 · gap (existing) |
| **Query / access** | S2's "clean positive cohort key" vs run-039 G1's "SaaS collapse" are the *same field behaving differently by cohort shape*, not opposites. The field works when the cohort IS its primary-tag semantics (pure-play metered) and collapses when the cohort cuts across models (SaaS) or is tagged by primary leg only (hybrids). A queryability guardrail: know the cohort's structural uniformity before using the field as a key. | read.md Result(3); run-039 G1; run-044 G2 | DR2 · surprise |
| **Freshness / automation** | No new pressure. Pricing-snapshot caveat (4 pre-2.3 captures from 2026-05-31 on volatile pricing pages) inherited, correctly flagged with clocks, named as a cousin of run-043 S3 without escalating. | read.md Missing/Stale Coverage | — |
| **Synthesis** | State→Judgment boundary cleanly managed. The Market Pattern section is the explicit synthesis crossing; everything above it is State dated to capture clock. One low-stakes inference ("each vendor meters the thing that scales with the customer's value") bleeds into Result(2) but belongs in Market Pattern — minor, doesn't affect the gap-map conclusions. | read.md Market Pattern vs Result(2) | — |
| **Guardrails** | The Loop 1 failure mode ("absent token ≠ published") held cleanly for all 5/6 untokenized members. PostHog being post-2.3 yet untokenized was a real guardrail stress-test the read handled correctly — calling it a "hint," not a conclusion, and naming a follow-up probe rather than asserting a finding. | read.md Result(4)/What Would Change | (guard held) |

## Lenses

**Steward** — System stayed honest. Provenance, freshness clocks, and the State/Signals→Judgment
separation all held; the verifier confirmed every load-bearing count (token tallies, cohort grep, billing
units, the Stripe L006 non-trap). The only correction was a precision tightening (PostHog offerings-module
vintage), now applied — the headline survives unchanged.

**Dev Agent** — No new helper warranted. The cohort draw is a one-line grep; the read names the toil-free
path. The recurring `denominator-reconciliation` pattern (n=4) gets a *boundary condition* from this run,
not a new instance: a model-draw can succeed where an industry-draw fails, when the cohort *is* the model.

**Founder** — Compounds the warm asset while staying light. Receipt C1 leaves a reusable cohort+token
table; the run reaches a confident "no new primitive needed" and resists both a normalized price field
(would launder false precision — banned by "evidence, not scores") and a stage/maturity-style field.

## Recommendation

- **No-op / keep as observation:** Yes — "no new primitive needed" is the run's correct outcome. The
  business_model multi-select want (n=2) and the queryability-guardrail framing (DR2) are observations for
  a future learning pass, not builds.
- **Watch for recurrence:** `denominator-reconciliation` (n=4, plus this run's boundary condition);
  `business_model` single-valued lossiness (n=2: run-037 S1, run-044 G2); `query-time-grouping-enough`
  third consecutive pricing-shape run (023, 043, 044).
- **Severe `risk-miss` to surface now:** None.

## Raw learning to preserve

Builder-side sightings appended to `run-notes.md` Observations (DR1, DR2 below) and lifted to
`learning/observations.md` by this Loop 2 pass.

**Do not propose lessons, graduate, spike, or implement system changes.**
