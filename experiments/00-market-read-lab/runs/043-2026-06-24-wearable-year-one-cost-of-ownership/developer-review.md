# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | Strength — DTC device pricing (device + sub + cadence + required status) is captured richly, on-surface, with point-in-time flags. The "decision-grade fact off the captured surface" pattern *inverts* here: the price ingredient mostly lives on-site. | read.md Source Gaps; R1 | S1 · surprise |
| **Structure** | Gap — the required-vs-optional sub status (the TCO-dominant fact) has no structured home; lives in prose/`STRAIN:`. Single-valued `business_model` is lossy on hybrids (re-confirms run-037 from the buyer side). | read.md Gap Map(1) | G1 · gap |
| **Query / access** | Gap — entity-grain mismatch: a catalog-grain captured company (Apple) cannot answer a SKU-grain buyer question (Apple Watch TCO). A *new flavor* of denominator-reconciliation — grain **within** a profile, not cohort-draw contamination. | read.md Gap Map(4) | G2 · gap |
| **Freshness / automation** | Gap — every device price is a sale snapshot; a TCO is only as fresh as the capture, and prices here move on flash-sale cadence. | read.md Gap Map(3) | S3 · surprise |
| **Synthesis** | Watch — the year-one TCO crosses from State into **Judgment** (an assembled, normalized range). The read labels it as a range, not a field; that boundary held. | read.md Result; consumer-review CR1 | CR1 · gap |
| **Guardrails** | Strength — store-only contract held; no spend, no external source, no store mutation; absence language stayed "not captured," not "not there." | run-notes exit check | — |

## Lenses

**Steward** — System stayed honest. State (per-offering prices) and Judgment (the
assembled TCO range) were kept distinguishable; uncertainty (sale snapshots, gated
checkout, grain wall) is visible. The Oura case is the sharpest: the read calls the sub
"required for value" while State says the ring still *functions* without it — the verifier
sharpened that Oura is the **only** member where a buyer can pay $0 recurring (device-only
floor $244). Logged VR1.

**Dev Agent** — The repeated toil (assemble device + sub + required-flag across a hybrid
cohort) is real but n=1 cohort here; not yet a recipe. The lightest future path stays
run-037 W1's ranked-multi-select `business_model` — and only if a *sorting* consumer
appears. A normalization recipe would be premature at one cohort.

**Founder** — The run compounds a warm, cheap-to-reask asset (cohort draw + R1) without
adding ontology gravity. "No new primitive needed" stays the honest disposition; the
buyer value came from synthesis over existing State, exactly the light path.

## Recommendation

- **No-op / keep as observation:** Yes — all sightings stay observations; no field, recipe,
  or tool proposed. "No new primitive needed" holds.
- **Watch for recurrence:** `query-time-grouping-enough`, `depth-backfill` (the hybrid
  composite-cost legibility gap — now seen via run-037 schema-lens AND this buyer-lens),
  `denominator-reconciliation` (G2 is a *new flavor* — intra-profile grain mismatch, worth
  watching separately from the n=4 industry-draw pattern).
- **Severe `risk-miss` to surface now:** None. The Oura "$0-recurring possible" nuance (VR1)
  is a precision sharpening, not a shipped error.

## Raw learning to preserve

Appended to `run-notes.md` Observations: **VR1** (verifier — Oura sub is value-gating not
strictly mandatory; device-only floor $244, the cohort's only $0-recurring path) and
**CR1** (consumer — year-one TCO is the run's Judgment, not a queryable field). S1–S4 / G1 /
G2 / W1 stand from Loop 1.

**Did not** propose, graduate, spike, or implement system changes.
