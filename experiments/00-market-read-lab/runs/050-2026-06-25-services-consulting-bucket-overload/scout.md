# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue): L001–L006 read. Strongest live pressure: L005 (query-time grouping enough only when the corpus carries the cut) and L006 (a category/price token over-claims on edge entity types). Recent observation stream (036–049) shows a recurring CR1 frontier — "value lands on builder/Pantry, not the buyer; map-not-ingredient" — across 7+ runs, plus a recurring anti-sprawl W1 ("lightest path is a query recipe, NOT a new field").
- `scout-context.md`: two-test selection (value/reach + design); optimize the slate for reader value, reach, source-family diversity, calibration; don't prefer store-answerability.
- Last 3 `run-notes.md` files: 047 (saas competitor edge, bounded-live), 048 (deep-tech traction momentum, store-only), 049 (render brief flag fidelity, local-existing). All three landed builder-facing value; the schema-edge runs (036/037/042/045/046) have repeatedly tested whether a *new* entity type fits the universal taxonomy — none has yet tested whether the *dominant existing* category bucket is itself overloaded.
- Current run artifacts: fresh scaffold (050), no prior receipts. Quick grounding grep: `offering_category` primary tokens across 145 profiles → `Services / Consulting` 73, `Biotech / Pharma` 53, `Software / SaaS` 34, `Physical Products / Hardware` 16, `Marketplace / Platform` 7, others ≤5. The Services/Consulting bucket visibly mixes telehealth care-wrappers, creative agencies, VC/holding, registered-agent/legal-doc, and compounding-as-a-service (many carry STRAIN comments).

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1 (SELECTED).** The store's biggest `offering_category` bucket is `Services / Consulting` (73 of 145). Is it a meaningful category or a residual catch-all — what distinct buyer-relevant sub-shapes hide inside it (telehealth care-wrappers, creative agencies, VC/holding, registered-agent/legal-doc, compounding-as-a-service), and does the dominant token discriminate anything a reader can use at this grain? | gap-probe / calibration | yes | store-only | The most-populated classification token carries the most schema weight; if overloaded it silently degrades every cross-store cut, neighborhood, and shortlist that leans on it. High reach (half the store). | Discriminating power / load-bearingness of the dominant category token; the L005 persistence boundary applied to the biggest bucket (sub-type vs query-time vs `entity_type` carries it). Extends 036–046 from "does a *new* type fit" to "is the existing dominant bucket meaningful." | Reaches the schema's own most-loaded token rather than a fresh vertical; tests whether `entity_type` quietly does the discriminating work `offering_category` can't. | A store-wide read of every Services/Consulting profile's `entity_type`, `offering_category` STRAIN/qualifier prose, and one-line offer shape; an honest sub-shape tally with an explicit ambiguous/not-found bucket; no claim the tally is exhaustive. | Minting durable sub-categories from a query-time grouping (L005 trap); over-claiming completeness when STRAIN prose is uneven. |
| C2. Take the store's deepest, best-priced cohort (GLP-1 telehealth, ~19 anchors) and run a clean *buyer* decision ("cheapest legitimate first-month start, no long lock-in — which 3?"). Can ANY store-only read land primary value on the end buyer, or is the recurring CR1 "value-on-builder" frontier structural? | calibration | yes | store-only | Tests the most-recurring observation-stream frontier directly. A clean buyer landing falsifies "store is structurally a builder tool"; a failure sharpens why. | Whether store-only reads can be buyer-facing at all; a value-frontier boundary, not a new primitive. | Reaches the consumer-value ceiling of store-only. | Comparable per-brand entry price/lock-in with capture clocks; explicit unit-incomparability caveats (010/023). | Re-confirming 010/023 price-incomparability with no new learning. |
| C3. Across the whole store, which entities expose a real acquisition wedge a buyer can act on without intake — free tier, free trial, free/low first dose, no-card demo — and is "acquisition surface" a query-time cut or does it need a token? | value-read | yes | store-only | A cross-vertical buyer/competitor-useful pattern. | Persistence boundary for an "acquisition surface" cut. | Cross-vertical pattern extraction beyond telehealth. | Per-entity acquisition-surface evidence from offerings/pricing prose; honest "silent" bucket. | Inferring a free tier from absence; reading marketing copy as a structured field. |
| C4. For a bounded panel (≤6) of GLP-1 brands with published prices, has the captured price/offer changed since `captured_at` per the brand's live page today? | gap-probe | yes | bounded-live | Tests the freshness/staleness frontier with real outside evidence. | Freshness-monitoring source panel; does the capture clock predict staleness? | Reaches live pricing — the one thing store-only can't refresh. | A tight `live_evidence_plan`: brand owned pricing pages only, ≤6 sources, capture dates, primary grade. | Sprawling into a re-capture; treating one stale price as "store is stale." |
| C5. Inside `Services / Consulting`, do the creative/strategy agencies (run-045 set) plus any VC/holding entities form a coherent substitute neighborhood, or does the bucket mix non-substitutable jobs? | gap-probe | yes | store-only | Relation-pressure on the catch-all bucket. | relation neighborhood vs category overload. | Substitute-set resolution inside a heterogeneous bucket. | entity_type + offer-shape per profile. | Repeats 045/039 shape; largely a subset of C1. |
| C6. Read the 2 `Media / Content` + 2 CPG entities for schema fit. (Logged as a coverage note, not a candidate — n=2 is too thin for an honest read.) | — | — | — | Denominator too small. | — | — | — | Would force a completeness claim off n=2. |

## Selected Question(s)

1. **C1 — Services / Consulting bucket overload / discriminating-power probe.** Highest reach (half the store), genuinely novel against the 036–046 entity-type-edge series, store-only and autonomous-safe, aimed at a live schema pressure point (L005 persistence boundary on the highest-traffic token + L006 token-over-claim cousin).

Runner-up: C2 (buyer-facing calibration) — strong design value but risks re-confirming 010/023 without new learning.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "The store's largest offering_category bucket is `Services / Consulting` (73 of 145 entities). Is that a meaningful, buyer-useful category or a residual catch-all? Read every Services/Consulting profile's entity_type, offering_category STRAIN/qualifier prose, and one-line offer shape; tally the distinct sub-shapes hiding inside the bucket (with an explicit ambiguous/not-found bucket); and judge whether the dominant token discriminates anything a downstream reader or cross-store cut can use at this grain — or whether entity_type / query-time grouping already carries the load."
selected_slug: services-consulting-bucket-overload
run_type: system-test
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Captured store profiles whose offering_category primary token is `Services / Consulting` (~73 by a frontmatter grep; treat as partial until the read reconciles maker-vs-reseller and hybrid-primary edge cases)."
likely_source_panel: "store/*/profile.md frontmatter (offering_category, entity_type, STRAIN comments) + the one-line offer/positioning prose; SCHEMA.md / TAXONOMIES.md for the token's intended meaning."
builder_lens: "Discriminating power and load-bearingness of the store's most-populated category token; the L005 persistence boundary applied to the dominant bucket (sub-type vs query-time vs entity_type carries it); cousin to L006 token-over-claim."
reach_reason: "Probes the schema's own most-loaded token rather than a new vertical — tests whether the biggest classification surface is meaningful or residual, which silently affects every cross-store cut, neighborhood, and shortlist."
allowed_sources:
  - "store/ (profile.md frontmatter + body prose only; no mutation)"
  - "SCHEMA.md, TAXONOMIES.md"
  - "experiments/00-market-read-lab/learning/ (context only)"
disallowed_actions:
  - "Mutating store/ or any profile"
  - "Live browsing, Firecrawl spend, or any outside capture"
  - "Minting a durable sub-category, field, or stored object"
  - "Writing any learning/ file or proposing/graduating a lesson"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Pure read over already-captured local store frontmatter and prose; no spend, no live browsing, no write-back, no primitive creation."
loop1_failure_mode: "Minting durable sub-categories from a query-time grouping (L005 trap), or over-claiming the sub-shape tally is exhaustive when STRAIN/qualifier prose is unevenly populated (say 'not found', not 'not there')."
```

## Selection Notes

C1 advances the schema-fit thread from "does a *new* entity type fit the universal taxonomy" (036/037/042/045/046) to "is the *existing dominant* bucket itself load-bearing" — an under-tested grain. It is store-only, autonomous-safe, and falsifiable: a clean discriminating tally vindicates the token; a residual catch-all sharpens L005's persistence boundary on the highest-traffic surface. C2/C4 are logged for a future cycle (C4 needs a bounded-live plan; C2 risks re-confirming known price-incomparability). C6 is a coverage note, not a runnable question.
