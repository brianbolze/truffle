# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

Do not default to "capture more data." Ask whether the run exposed a reusable system need: capture, structure, query, freshness, automation, access, or guardrails.
Record the gap as an observation first. Do not convert it into a recipe, field, tool,
or build proposal inside the run unless the review adds enough evidence for a triage
candidate.

Market reads may make judgments. When they do, ask whether the read clearly crossed from State or Signals into Judgment, and whether Truffle should support that boundary or leave the judgment downstream.

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Discovery disposition |
|---|---|---|---|
| **Capture** | Strength: classification carries cleanly across non-telehealth captures. **Gap:** 9 of 135 dirs are capture-only stubs (raw `captures/`, no `profile.md`). | read.md C6; receipt R1 | recur-watch — directory ≠ profiled company |
| **Structure** | **The load-bearing gap.** Closed-set classification layer has no slot for capital-allocator economics; the `Investor / Holding` gating rule is under-specified → 7 firms, 4 `offering_category` encodings, lone store-wide `business_model: Other`. | read.md C4/C5; S1/S2/G1 | ready-for-triage — meets promote threshold (7 sightings) |
| **Query / access** | Minor: no single "classification table for cohort X" helper; assembled via a roster loop + per-field grep. One sighting. | run-notes friction log | recur-watch only |
| **Freshness / automation** | N/A — classification is durable State; nothing freshness-sensitive. | — | no-op |
| **Synthesis** | Strength: the read held the `# STRAIN` partition (capture-fidelity vs classification strain) and the State-vs-Judgment boundary cleanly; failure-mode trap actively avoided. | read.md Market Pattern #3; verifier PASS | no-op (positive) |
| **Guardrails** | Strength: store-only, no spend, no mutation; exit check all-pass; absence framed "not found" throughout; verifier independently re-derived every count. | run-notes exit check; verifier PASS | no-op (positive) |

## Lenses

**Steward** — Is the system still honest? Provenance, freshness, grain, State / Signals / Judgments separation, and visible uncertainty.

**Dev Agent** — Can repeated toil be removed with a convention, recipe, or tiny helper? Prefer grep-verifiable contracts and fewer knobs.

**Founder** — Does the response compound the warm / cited / cheap-to-reask asset while staying light? Avoid ontology gravity and one-off surfaces.

**Lens reads.** *Steward:* the run is honest — the positive finding (taxonomy generalizes
for sellers) is as load-bearing as the break and isn't buried; State/Judgment separation
held; the new `schema-edge-entity-type` tag is a legitimate narrow coin the existing tags
don't cover. *Dev Agent:* the fix is a one-line gating-rule tightening in TAXONOMIES.md —
zero new values, no downstream blast radius — preferred over a new `offering_category`
value. *Founder:* 7 firms is a real non-singleton population; a consumer filtering
`entity_type: Investor / Holding` then grouping on `offering_category` gets noise, not
signal — the groupability promise is broken today. The edge is the non-offering *entity*,
not a vertical, which usefully reframes the engine's risk surface.

## Recommendation

- **No-op / keep as observation:** O3 (STRAIN markers are mostly capture-fidelity) —
  notice-only; O1 positive calibration — keep as observation.
- **Watch for recurrence:** G2 stub denominator (append to MRL-001); the query-helper
  friction (one sighting).
- **Submit triage evidence (mature):** the capital-allocator encoding inconsistency —
  **new** item; recurrence (7/4/3) clears the bar and no existing MRL item covers the
  entity-type-scope axis.

## Optional triage evidence

1. **NEW ITEM — `schema-edge-entity-type`: capital-allocator encoding inconsistency.**
   The `Investor / Holding` gating rule is under-specified: 7 firms → 4 `offering_category`
   encodings (rule honored 3/7), and the lone store-wide `business_model: Other` (blueowl)
   marks a gap the value set doesn't fill (AUM/fee economics). Preferred resolution (W1):
   an **entity-type-gated convention** that pins one encoding — *not* a new
   `offering_category` value. Recurrence 7 ≥ promote threshold. Pointers: `run-notes.md`
   S1/S2/G1/W1; read.md C4/C5; receipt R1.
2. **EVIDENCE → MRL-001.** 9 of 135 dirs are capture-only stubs (no `profile.md`);
   profiled N=126. Concrete store-wide instance of "directory count ≠ profiled company
   count." Pointer: `run-notes.md` G2; read.md C6.

**Do not graduate, spike, or implement system changes.**
