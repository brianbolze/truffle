# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

Do not default to "capture more data." Ask whether the run exposed a reusable system need: capture, structure, query, freshness, automation, access, or guardrails.
Record the gap as an observation first. Do not convert it into a recipe, field, tool, or
build proposal inside the run — consolidation into a lesson is an out-of-band pass.

Market reads may make judgments. When they do, ask whether the read clearly crossed from State or Signals into Judgment, and whether Truffle should support that boundary or leave the judgment downstream.

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | Competitor edges are captured **as prose**, uneven grain (list / per-product / comparison-set), and mostly target **off-store** companies — decision-grade where present but not a dependable channel. | datadog:74, gong:59-60, dovetail:85, listenlabs:121; named rivals absent from `store/` | G2 · gap |
| **Structure** | **Axis-asymmetric relation support:** vertical (`parent`/`owns`) is first-class and rich; horizontal (competes-with / substitute) has no field. Plus a cross-profile **consistency** gap in the vertical axis (Coda's owner differs across coda.io vs superhuman.com). | parent/owns frontmatter; coda.io vs superhuman.com | S1 · surprise; G3 · gap |
| **Query / access** | `primary_industry` is a **leaky cohort key** for SaaS (returns 4 hardware/marketplace entities); and `offering_category` has no sub-category leaf, so no structured query separates sub-markets — they must be re-read from prose each time. | grep returns apple/casio/eightsleep/upwork; ~19× `[Software / SaaS]` | S2 · surprise; G1 · gap |
| **Freshness / automation** | Not a pressure point this run — captures fresh (~06-17); read flags that competitor-*positioning* (vs structural identity) is freshness-sensitive but did not need a refresh. | captured_at ~2026-06-17 | (noted, not logged) |
| **Synthesis** | **Strength:** the read cleanly labeled the 7-cluster map as Judgment-not-State and kept the partial-denominator caveat throughout — the State/Judgment boundary held under pressure. | read.md Result(2) "LLM judgment, not store State" | (strength) |
| **Guardrails** | **Held:** store-only honored, no mutation, no primitive minted, "no new primitive needed" reached honestly with the flip-condition named. No snippet/external evidence. | run-notes exit check all pass | W1 · wish |

## Lenses

**Steward** — Is the system still honest? Provenance, freshness, grain, State / Signals / Judgments separation, and visible uncertainty.

**Dev Agent** — Can repeated toil be removed with a convention, recipe, or tiny helper? Prefer grep-verifiable contracts and fewer knobs.

**Founder** — Does the response compound the warm / cited / cheap-to-reask asset while staying light? Avoid ontology gravity and one-off surfaces.

## Lenses

**Steward** — System stayed honest. The hardest test was the 7-cluster map, which is the
run's own judgment; the read labeled it as such and cited every competitor edge to a captor
line. State/Signals/Judgment grain held. The one Steward-flag is G3: the vertical relation
can read **inconsistently across profiles** (Coda's owner), because `parent`/`owns` has no
cross-profile reconciliation — a chain can disagree with itself and both ends look clean.

**Dev Agent** — The repeated toil (hand-filtering the leaky industry draw, grepping
competitor lines out of bodies) is real but **not yet worth a helper** at one slice. If it
recurs, the lightest fix is a query recipe, not a field (W1). Resisting the field is the
right call: a competitor field would be mostly empty/dangling today (engine-dev "every field
is a cut you can fill reliably").

**Founder** — The run compounds the asset cheaply (read + receipt are reusable) without
adding ontology gravity. The temptation to mint a horizontal-relation primitive is correctly
deferred; building it now would create a mostly-empty surface that points off-store.

## Recommendation

Record the disposition as an observation; do not propose or graduate a lesson here.

- **No-op / keep as observation:** S1, G1, G2, S2, W1, CR1 — all logged; "no new primitive
  needed" is the honest disposition. No build, no recipe, no field this run.
- **Watch for recurrence:** `relation-pressure` (axis-asymmetry S1 + horizontal absence) and
  `query-time-grouping-enough` (G1 is the first **failure-side** sighting of L005 — worth a
  learning pass's attention precisely because every prior L005 sighting confirmed the
  success side). `denominator-reconciliation` (leaky industry key S2) is now a 3rd sighting
  after run-036 G3 / run-037 G2 — industry is not an entity-shape cohort key.
- **Severe `risk-miss` to surface now:** None. G3 (M&A-chain inconsistency) is a real but
  low-severity honesty gap — both records are STRAIN-flagged, so a careful reader is warned;
  it is not a silent error. Logged as a gap, not escalated.

## Raw learning to preserve

All sightings preserved in `run-notes.md` Observations (S1, G1, G2, G3, S2, W1) plus this
review's **DR1** and the consumer review's **CR1**. Loop 2 appends them to
`learning/observations.md`.

**DR1 (new, developer-review):** `denominator-reconciliation` recurrence — `primary_industry`
returning 4 non-SaaS entities is the **third** sighting that an industry draw is the wrong
key for an entity-shape cohort (run-036 G3 marketplaces-scatter-across-industries; run-037 G2
hardware-cohort-needs-judgment; now SaaS-draw-pulls-hardware/marketplace). The pattern is
consistent enough to flag for a learning pass, though still no build.

**Do not propose lessons, graduate, spike, or implement system changes.**
