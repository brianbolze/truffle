# Developer Review

Question: **What Truffle system behavior does this run pressure?**

**Headline:** Honest, well-labeled run that surfaces one genuinely new system observation — **offer-structure is a third distinct State-read surface, but unlike the first two it lives in narrative `site_notes` prose, not a greppable field.** No new primitive needed; it sharpens MRL-002.

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | The store captures billing *cadence* (auto-renew every 10 weeks, 12-mo prepay) but not lock-in *friction* (cancellation policy, refund terms, early-termination fee). A concrete named field gap, not a vague "more data." | Watch — single sighting; note as a candidate field only if a second lock-in read needs it. Do **not** schematize from one run. |
| **Structure** | The membership-wedge classification is where State most strains into Judgment: "membership" carries four distinct meanings across the cohort (mandatory stacked fee / wrapper over separate meds / marketing word for an all-in charge / line-specific add-on). | Keep the Judgment downstream and labeled. The receipt already names this; the recipe should require flagging ambiguous cells. |
| **Query / access** | Third State-read surface in the series — but offer-structure attributes are **not greppable as discrete fields** (vs 008's `Visibility` column and 009's `access_model` frontmatter). Extraction was read-prose-then-extract, not field-lookup. | A *prose-surface variant* of the MRL-002 recipe: when the attribute isn't a discrete field, quote the sentence verbatim and label the interpretation as a Judgment cell. Recipe-level, no helper. |
| **Freshness / automation** | `freshness-monitoring` fired for the first time in the State-read series — price figures are promo/A-B-volatile (countdowns, A/B engines, struck-through heroes) in nearly every brand's `site_notes`. | Watch — the system has no convention for *how stale* a price can be before a read should refuse to quote it; that threshold is currently implicit. Not a build; a possible future synthesis convention. |
| **Synthesis** | The `[J]`-labeling discipline held: C3/C4/C5/C6 all labeled, each tied to verbatim prose, no figure presented as current. The 009 field-fidelity lesson ("quote, don't re-derive") was applied. | No-op — the read template + labeling worked as intended. |
| **Guardrails** | Store-only contract honored end-to-end: no live fetch, no spend, no mutation. The "no external completeness check" decision was reasoned and consistent with MRL-001 (structural findings don't need a fuller denominator). | No-op — guardrails behaved. |

## Lenses

**Steward** — System stayed honest. Provenance complete (S1–S12, dated), State/Signals/Judgment separation clean, uncertainty visible (partial denominator, price-rot, membership-semantics caveat). The one strain: the C3 "business-model split" reads cleaner in the summary than the underlying evidence — remedy ("No Memberships" homepage vs. internal "membership" charge) and tryshed/joinfound (mixed lanes) are genuine edge cases that needed human placement. Worth a recipe note, not a correction.

**Dev Agent** — The repeated toil is the *third* variant of the same State-read loop (latest-capture → field/prose extract → group/label). It is converging into a recipe family, but each surface had a different extraction grain. The new wrinkle is prose-vs-field: the prior recipe guard assumed a grep-able field name; this surface needs an extract-from-prose idiom. Still a documented recipe, not a helper — prefer grep-verifiable contracts where the field exists, and an explicit "quote-the-sentence + label-as-Judgment" rule where it doesn't.

**Founder** — Compounds the warm/cited asset (a reusable per-brand offer-structure panel) while staying light. No ontology gravity: the run explicitly wanted no durable "offer-shape" or "membership-model" category object. The cancellation/refund-field idea is the one place ontology gravity could creep in — correctly held as a single-sighting watch.

## Recommendation

- **No-op / keep as observation:** the price-staleness-threshold gap (freshness convention) and the cancellation/refund-field gap (capture-grain) — both single sightings, watch only.
- **Watch for recurrence:** does the membership-wedge (med-included vs med-plus-membership) recur as the business-model tell on a *second* cohort's offer-structure surface, the way price-posture did (000→008)?
- **Submit triage candidate:** none new. Append recurrence evidence to **MRL-002**.

## Triage submissions

No new item. Consolidated Evidence Log entry appended to **MRL-002** this run (offer-structure as a third State-read surface + the prose-vs-field extraction wrinkle + the ambiguous-cell flag). No graduation, no implementation, no spike.
