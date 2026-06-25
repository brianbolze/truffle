# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

The run is clean and well-scoped. It separates State from Judgment throughout — the maturity
ranking is explicitly the read agent's Judgment derived from prose State, and the Gap Map
labels the structured-field gap. The positive finding (S2) is the right kind of surprise to
name; the risks (G1/R1) verified against the actual profile text; the no-new-field
conclusion (W1) is consistent with engine-dev's anti-sprawl stance. An adversarial evidence
pass caught one factual overreach (the read called two `offering_category` lists "identical"
when they only overlap) — corrected in read.md, run-notes G2, and the receipt, and logged as
VR1.

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation |
|---|---|---|---|
| **Capture** | Self-reported milestones (funding/orders/pipelines/partners) are captured and honestly flagged, but not independently confirmed; filings/IR/trade-press is the off-surface panel a confirmed read would need. | read.md Source Gaps; G4 chain (036 G2 / 037 / 038 G2) | G4 · gap |
| **Structure** | No structured maturity/stage signal; `description` present-tense over-claims (5/7, not just the 3 named); `business_model` blank on 2/7 and maturity-blind even when populated; shared `offering_category` value encodes no maturity. | read.md Result(2)/(3); G1/G2/DR1/CR3 | G1·gap, G2·gap, DR1·gap, CR3·gap |
| **Query / access** | Cohort not recoverable from `primary_industry`/`offering_category` (scatters; pulls euclid foil). 4th sighting. | Companies Seen; C1 | G3 · gap |
| **Freshness / automation** | Stage is the fastest-decaying fact in the cohort ("pilot in 18–24 months"); blueenergy/sorafuel sit closest behind milestones. | Evidence limits | (covered in G2/freshness tag) |
| **Synthesis** | The store's honest-absence discipline (`unverified_fields`, `[on-request]`, "self-reported") is the load-bearing guard — but prose-grade and relay-dependent; over-claim reaches the body lead (CR1). | read.md Result(4), Market Pattern | S1·surprise, CR1·gap |
| **Guardrails** | The adversarial verifier caught a precision overreach ("identical" categories) the read would otherwise have shipped — evidence the 3-pass Loop 2 shape earns its keep. | verifier overreaches_found | VR1 · risk-miss |

## Lenses

**Steward** — Honest. State/Judgment stayed separated; the one precision slip ("identical")
was caught and fixed. The cohort concept itself has no clean structured boundary even within
its 7 members (beta-team is revenue-generating on non-flagship lines — DR2), and the run is
appropriately explicit that "pre-revenue deep-tech" is a reader judgment, not a field.

**Dev Agent** — The repeated toil (reconstruct maturity by hand from prose every time) is
real but should **not** be removed with a `stage` field — it would be a rotting captor
judgment, mostly-blank store-wide, failing the fillable-cut bar. The lightest correct
response is a read/relay convention (W1), if anything.

**Founder** — The asset stays warm and light: receipts + ranking compound for the next
deep-tech ask without minting ontology. The value lands again primarily on the
builder/Pantry side (maturity diagnosable, not queryable) — the same "map not ingredient"
frontier as runs 038/039 CR1 — even though Q1 was deliberately pitched at an end-reader
question. Worth naming that the streak-break was partial.

## Recommendation

- **No-op / keep as observation:** the maturity-field gap (G2) and the cohort-draw gap (G3)
  stay observations; no build. "No new primitive needed" is the standing verdict.
- **Watch for recurrence:** `denominator-reconciliation` is now **n=4** across distinct
  entity-shape cohorts (036/037/039/042) — consistent enough that the next learning pass
  should weigh it. The off-surface source-family gap is also n=4 (G4). Counting note: the
  off-surface chain is n=4 *sightings* but one (run-037 Source Gaps) was prose-only, so n=3
  *observation rows* — fairly cited.
- **Severe `risk-miss` to surface now:** none severe. VR1 (the "identical" overreach) was
  caught in-loop and fixed; R1 (delegated-agent maturity over-claim) is a live but
  prose-guarded risk against the #1 value job, already logged.

## Raw learning to preserve

New review-surfaced sightings appended to `run-notes.md` Observations and lifted to
`learning/observations.md`: **VR1** (precision overreach "identical"→"overlapping", caught
by the verifier pass), **DR1** (description over-claim is 5/7 pre-revenue profiles, not the
3 named — widens G1), **DR2** (beta-team is a cohort boundary case — revenue-generating on
non-flagship lines; "pre-revenue deep-tech" has no clean structured boundary even within the
7). CR1/CR2/CR3 are logged via the consumer review.

**No lessons proposed, nothing graduated, no spike or system change.**
