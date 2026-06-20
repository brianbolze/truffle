# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

Reviewed via the Loop 2 adversarial workflow (developer pass, Sonnet). Paired with the
evidence verifier (overall **PASS** — all 5 load-bearing claims re-derived locally; one
cosmetic receipt fix applied: S2 `Snippet-only?` now `no`).

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Later shaping question |
|---|---|---|---|
| **Capture** | The corpus-label mismatch is the sharpest capability gap surfaced to date: a captured "telehealth" corpus that excludes an entire care modality. | 0 behavioral `anchor_category` (local grep corroborated); 0/5 head + full union store-absent. | Is behavioral health *in scope* for this store by design? Capture decision waits on that framing call. |
| **Structure** | State/Judgment boundary held. The one boundary-crossing moment (excluding 7 payers, F1) was hand-done and logged, not automated. | F1 in run-notes; "scope vs gap" left unadjudicated. | Should the extraction layer carry a "care-platform vs payer/carrier" filter so the named set isn't silently inflated? |
| **Query / access** | Selection-bias blindspots at corpus-construction time cannot be resolved at query time — confirmed at *modality* scale now, not just audience. | 0 store-only query can surface the behavioral head. | A QUERYING whitespace recipe must carry the compound guardrail (anchored-only fix ≠ sufficient; selection-bias needs outside evidence/capture). |
| **Freshness / automation** | Bounded-live discipline clean: 12 net credits, stop rule fired after 2 listicles, all 4 sources logged, no drift. | `live_evidence_used` + exit check 11/11. | None — the standing light plan held on a 4th run. |
| **Synthesis** | Coverage-radar recipe now stable across 3 maximally different lanes; output shape (tiered worklist + boundary statement) reusable. | GLP-1/012 → menopause/022 → behavioral/024, identical shape. | Name the bounded-live coverage-radar recipe in QUERYING (human-gated); do not build a helper. |
| **Guardrails** | F1 (platforms-vs-payers) is a new, consequential extraction confound — corrupts set *membership*, not just rank/tail. | Healthline extract returned 7 insurers as "brands" (~60% inflation if naive). | Carry a platforms-only filter as a prerequisite of the coverage-radar recipe. |

## Lenses

**Steward** — System stays honest. Provenance, freshness, and the State/Signals/Judgment
split are all clean; absence is "not found by two local methods," never "doesn't exist";
the scope-vs-gap framing is left to a human. The verifier's only catch was cosmetic.

**Dev Agent** — The repeated toil here is real but already tracked: aggregating an external
named set + token-diffing the store is the MRL-002 bounded-live recipe, now 3-sighted. The
right move is a *named recipe* (a few searches + 2 JSON scrapes + a token diff) plus the F1
platforms-only guard — **not** a helper, field, or edge. Grep-verifiable, few knobs.

**Founder** — Compounds the warm/cited/cheap asset without ontology gravity: no `store/`
mutation, no durable primitive, a proposed-only worklist. The corpus-identity reframe ("DTC
Rx-commerce, not telehealth") is high-leverage characterization that costs nothing to keep.

## Recommendation

- **No-op / keep as observation:** the "diminishing novelty past ~3 coverage-radar sightings"
  signal — correctly self-read by the run; no item warranted.
- **Watch for recurrence:** therapy-vs-psychiatry sub-lane split as a capture-scoping decision
  (S1 in the Discovery ledger) — one sighting.
- **Submit triage candidate:** append Evidence Logs to **MRL-001, MRL-002, MRL-008, MRL-009**
  (below). **No new item** — F1 absorbs into MRL-008; the boundary finding sharpens MRL-001's
  compound guardrail but doesn't earn its own item.

## Triage submissions

Append-only Evidence Logs (no graduation, no `Human Notes`, no implementation):

- **MRL-001** — selection-bias flavor now confirmed at **care-modality** scale (3rd sighting:
  020 hypothesized → 022 audience-scale → 024 modality-scale). Same mechanism (construction
  seeding), same tool (bounded-live panel, 12–14 credits), now scale-invariant from audience
  slices to entire care modalities. Three-run evidence for the compound QUERYING guardrail.
- **MRL-002** — 3rd sighting of the bounded-live coverage-radar recipe; stable across 3 lanes.
  Earns *naming* the recipe in QUERYING (not building a helper). New prerequisite: the F1
  platforms-only filter before cross-source intersection.
- **MRL-008** — new **platforms-vs-payers** extraction confound (F1): Healthline's extract
  returned 7 insurers as "brands" (~60% inflation if naive). Distinct from the affiliate-
  ordering confound (012) — that corrupts rank/tail; this corrupts set *membership*.
- **MRL-009** — 2nd behavioral-shaped tiered capture worklist (after 022's menopause one):
  Tier-1 BetterHelp/Talkspace/Brightside/Doctor on Demand/MDLive; Tier-2 Grow/Amwell/Teladoc/
  Sesame/LiveHealth; Tier-3 Cerebral/Talkiatry/Brave. Proposed-only; a scope decision precedes
  capture; several Tier-1/2 names are multi-service (`multi/none`), not behavioral-pure.

**Do not graduate, spike, or implement system changes.**
