# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients, capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Discovery disposition |
|---|---|---|---|
| **Capture** | Strength: `profile.md` prose (Overview, What-they-offer, site_notes, unverified_fields) carries a full luxury-posture read without `offerings.md` or the structured token. No capture failure — luxury "no price" is named as deliberate posture by each brand's own site copy. Gap: AP service-price-list + Lange overhaul pricelist referenced but not fetched (correctly out of scope). | C1–C7: all 7 carry explicit "no e-commerce / authorized dealers only / price on request" language from captured pages. | No-op; the prose surface held. |
| **Structure** | Strength: State/Judgment boundary held and was tested by design — luxury scarcity gate (dealer waitlist/allocation) kept as Judgment ("market posture," "not owned-page State"). Contracted failure mode (forcing a telehealth intake-gate lens) named and avoided. Weak point: SCHEMA price-visibility token + `offerings.md` 0/7 off telehealth → structured surface carries no signal. Depth-backfill gap, not a structural defect. | C8; read.md S1; Gap Map. | Watch for recurrence (run-028 branch in MRL-008). |
| **Query / access** | Strength: `query-time-grouping-enough` fired cross-vertical again — whole read is a grouping over existing prose State; no durable object, no `gate_type` enum needed. Gap: watch cohort can't be drawn by a single `primary_industry` grep — Casio under `Technology` → `Consumer Goods` filter under-counts by 1. | G1; read.md Companies Seen. | Watch for recurrence — MRL-001 cross-field flavor on a non-telehealth slice. |
| **Freshness / automation** | No freshness pressure for the structural read (luxury posture durable; uniform 2026-05-31). Accessible-tier inline prices are point-in-time, flagged honestly, not overstated. | read.md Missing/Stale Coverage, Evidence Limits. | No-op. |
| **Synthesis** | Strength: two-part output (price-presentation map + generalization verdict) reads at a glance. Cartier category-grain straddler + MoonSwatch/Moflin product-grain exceptions surfaced with named evidence. Gate-type × gate-grain vocab correctly held recur-watch, not baked into a recipe. | read.md Result, Market Pattern, Gap Map. | No-op; well-shaped. |
| **Guardrails** | Contracted failure mode named in scout (`loop1_failure_mode`) and avoided. Absence language "not published by convention," never "capture failure." Luxury price levels held as unreachable store-only (out of scope, not a gap). Loop-1 exit check passed every gate. Mild stress: cross-field denominator (Casio under Technology) not anticipated *before* the run. | run-notes Loop 1 exit check; read.md Source Gaps; scout.md expected_denominator. | No-op on discipline; denominator is an MRL-001 watch. |

## Lenses

**Steward — Is the system still honest?** Yes. The hardest test was the luxury scarcity gate: the read named it a market posture, quoted site copy, and held the dealer-waitlist/allocation reality as Judgment, not State. The 0/7 structured-surface count was framed as a coverage signal, not a market fact — the run-028 trap named and avoided. One verification note (now cleared by Loop-2 evidence verifier): the Cartier category split is the most load-bearing single data point in the generalization verdict — its prices ($2,130–$38,520 Love line / $49–$355 fragrance) were confirmed verbatim in `cartier-com/profile.md`, evidence-grade not inference.

**Dev Agent — Can repeated toil be removed?** No new toil introduced; the read reused the run-010 prose-surface variant (glob profile.md → read What-they-offer/site_notes/unverified_fields → label). The one friction (hand-adding Casio after a Consumer Goods grep) is a known denominator flavor (MRL-001) and shouldn't trigger a helper for a 7-brand cohort — but the cross-field under-count *would* warrant a QUERYING recipe note if it recurs on non-watch vertical reads. No `gate_type`/`price_visibility` enum should be built; the vocab distinction is a 3-vertical observation, not a greppable field.

**Founder — Does the response compound the asset without ontology gravity?** Yes. Real reader value + a clean generalization verdict, all from existing captured prose, no new field/object/token migration/module. `query-time-grouping-enough` fires cross-vertical a third time — the compounding signal that the lab's most-reused recipe holds under strain across maximally different verticals. The one ontology-gravity risk (coining `gate_type`/`gate_grain` as schema-sounding vocab) is explicitly resisted in the run; that resistance is correct and should be maintained.

## Recommendation

- **No-op / keep as observation:** Gate-type × gate-grain vocab (O1/O2/W1) stays recur-watch until a 4th vertical (e.g. Finance/VC rate-card vs advisory-quote) fires the same distinction. State/Judgment boundary on the scarcity gate held cleanly — no new guardrail.
- **Watch for recurrence:** O3 (structured-surface absence, 3rd vertical) — MRL-008 run-028 branch; a 4th vertical would be decisive for a cross-vertical backfill argument. G1 (cross-field Industry under-count) — a second non-telehealth instance would strengthen toward a QUERYING recipe note.
- **Submit triage evidence (to existing items, no new MRL items):** MRL-002 (3rd-vertical recipe generalization + first non-telehealth *market read*), MRL-008 (3rd-vertical confirmation of structured-surface-absence branch), MRL-001 (first cross-field `primary_industry` under-count on a non-telehealth cohort). All are mature third-sighting confirmations of existing pressure, not new axes.

## Optional triage evidence

Three dated Evidence Log entries submitted to MRL-002, MRL-008, and MRL-001 (text in `triage.md`). No new MRL items — every finding is a confirmation/extension of an existing acknowledged item. No graduation, no build.
