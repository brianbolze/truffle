# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

The run is a store-only gap-probe on the most product-hostile entity type the schema-edge
series has hit. Its core finding is adversarially sound — grep counts verified (80/8),
`portfolio_shape` values check out, Parlance pricing tokens check out. The 3-pass review
caught **one real precision overreach** (the "identical 5-field tuple" claim), now corrected
in read.md + run-notes G2/G3 and logged as VR1/DR1.

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | No capture gap — the 5 profiles carry the buyer decision in prose; `offerings.md` correctly skipped (no SKU grain). | Each profile's body sections; provenance notes the deliberate `offerings.md` skip. | S1 · surprise |
| **Structure** | **Two structural gaps.** (1) No field isolates the cohort — `offering_category` is non-isolating (80), `business_model` contaminated (8). (2) Within-cohort, the 4 typing fields are degenerate; the closed `offering_category` set is taxonomy-bottomed-out (`[Services / Consulting]`, no finer leaf). | C1/C2; TAXONOMIES.md has no `Services / Creative Agency`. | G1 · gap; G2 · gap |
| **Query / access** | The agency cohort is **not queryable** — a reader must already know the 5 names; no structured draw approximates it. The buyer's first screen (firm scale) is unstructured, forcing sequential full reads. | grep tests; portfolio_shape 3/5 degenerate. | G3 · gap; CR2 · friction |
| **Freshness / automation** | No pressure — captures ≤3 weeks; agency rosters/pricing drift slowly. | captured_at 06-04→06-18. | — |
| **Synthesis** | **Read-discipline pressure caught and corrected.** The single-pass read overstated field-sameness ("identical tuple"); the 3-pass Loop 2 verifier caught it (as in run-042 VR1). Evidence that the adversarial Loop 2 shape earns its cost. | run-notes G2 correction; VR1/DR1. | VR1 · risk-miss; DR1 · gap |
| **Guardrails** | **Strong.** `unverified_fields` honestly flags firm-scale/revenue as deep-research (not invented); `[on-request]` faithfully reports "no list price exists." Both stop a delegated agent fabricating sizes/prices. | ideo:32, redantler:27; S2. | S2 · surprise |

## Lenses

**Steward** — The system stays honest. State reading is grounded in file:line throughout;
`unverified_fields` and the faithful price-visibility token make absences visible. One mild
editorial intrusion: read.md Market Pattern characterizes schema *design intent* ("built for
sellers with a catalog") — clearly in a synthesis section, labeled as such, not State-as-fact.
State/Signals/Judgment separation holds for a store-only run.

**Dev Agent** — No toil to remove with a helper: three greps + six reads answered it. The
*finding* is that no grep-verifiable contract isolates the cohort — but the right response is
**not** to mint one (see Founder). The price-visibility token's per-offering, never-a-scalar
contract is working as designed (S3 — invisible to a frontmatter filter, but that's a
deliberate SCHEMA choice, not a bug).

**Founder** — The anti-sprawl instinct is correct and the run holds it (W1: no firm-scale
field — a rotting captor judgment, mostly-blank, fails engine-dev's fillable-cut bar). **One
reasoning gap (DR2):** W1's *lighter* alternative — "the closed `offering_category` set lacks
an agency/specialization value" — is offered without testing whether *that* value would also
rot. Distinguishing "creative agency" vs "management consultancy" vs "dev shop" is itself a
captor judgment, not site-derivable, so it likely fails the same fillable-cut bar. The
graduation hold is right; the lighter-fix path is under-examined.

## Recommendation

- **No-op / keep as observation.** "No new primitive needed" is the correct disposition, held
  hard: prose serves the human buyer, the price-visibility token reads faithfully, and both
  candidate fixes (firm-scale; specialization-leaf) fail the fillable-cut bar.
- **Watch for recurrence** (`schema-edge-entity-type`, `denominator-reconciliation`,
  `query-time-grouping-enough`): a **second pure-services cohort** (management/strategy
  consultancies, law firms, dev shops) showing the same non-isolating + degenerate pattern
  would move G1/G2 from single-cohort sighting toward a general "services entity type defeats
  the product spine" shape. Until then, n=5, single cohort.
- **Severe `risk-miss` to surface now:** none. VR1 is a corrected precision overreach (caught
  in-run, fixed in-place), not a shipped risk. The S2/S3 token reading is consistent with and
  *extends* L006's sharpened scope (the third entity-type confirmation: 037 DR3 no-price
  intermediary fires, 044 S3 transparent intermediary safe, 045 S2 services-no-price safe) —
  an out-of-band signal for L006's graduation check, not a conflict.

## Raw learning to preserve

New rows from this review: **DR1** (portfolio_shape degeneracy is 3/5 not 2/5 — understated
evidence, same conclusion), **DR2** (W1's specialization-leaf alternative under-examined
against the fillable-cut bar). Plus the verifier's **VR1** (the "identical tuple" overreach,
corrected). All preserved to `learning/observations.md`. Confirmations (no new row): G1 scope
correct, foil usage well-scoped, S2/S3 consistent with L005/L006, State/Judgment separation
clean.

**Did not propose lessons, graduate, spike, or implement system changes.**
