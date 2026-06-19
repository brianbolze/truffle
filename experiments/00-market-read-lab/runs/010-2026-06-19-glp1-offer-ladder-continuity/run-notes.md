# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [query-time-grouping-enough, coverage-caveat, freshness-monitoring]
```

> **Loop 2 outcome (2026-06-19):** Reviewed via a 3-pass adversarial workflow (evidence verifier +
> consumer + developer, Sonnet). The verifier re-checked **14 load-bearing sub-claims** against the
> underlying `offerings.md` files: **13 confirmed verbatim, 1 partial-but-defensible** (the ≈9/≈7
> business-model split count — mixed-lane brands tryshed/joinfound could be classed differently),
> **0 contradicted**. Every quoted membership figure (eden $39→$99, hims-WL $39→$149, ro $39/$74/$149,
> ivim $74.99, medvi $99, shed +$125, found $149/$199) and the C4 mechanisms (brello upfront÷3,
> telolife bundles = flat $199/mo prepay, ivyrx 12-mo prepay) matched verbatim. 009's "quote, don't
> re-derive" guard held. One **evidence-fidelity hedge** applied to `read.md` C6 — the "fully published,
> no-wall pricing is a differentiator" framing now flags its small-n pole (telolife + effecty only).
> Triage: a consolidated Evidence Log entry appended to **MRL-002** (offer-structure as the *third* State
> surface; the prose-vs-field extraction wrinkle; an ambiguous-cell flag for membership semantics). Two
> single-sighting **watches** (a price-staleness-threshold convention; a cancellation/refund capture-grain
> field) — neither earns a queue item yet. No graduation.

## 30-second operator read

- **Did the run work?** Yes. Store-only, no spend, no mutation. A **new `offerings.md` field surface** — offer *structure* (bundle composition, billing cadence, commitment, membership wedge, price-visibility timing) — not the price-Visibility column (000/008) or positioning Notes (009).
- **What was awkward?** Classifying the **membership wedge**. "Membership" means four different things across the cohort (a mandatory stacked fee, a wrapper over separately-billed meds, a marketing word for an all-in recurring charge, a line-specific add-on). The C3 business-model split is a Judgment over those distinctions, not a clean captured field.
- **What the next agent should know:** the standout, store-evidenced finding is that **the "$X/month" headline is systematically not what you pay**, for three recurring reasons (upfront-total÷N, med-only-plus-membership, dose-floor-set-in-intake). That's the offer-structure echo of 008/009's "posture tracks business model, not molecule." `offerings.md` carried all of it off disk with zero re-capture.

## What happened

Gated on the contract (scout-only → store-only → autonomous → approval:no, all pass). Derived the cohort by `grep -l "anchor_category: GLP-1" store/*/telehealth.md` → 19 dirs that also carry `offerings.md`. For each, read the `site_notes` frontmatter + `## Portfolio overview` + `Visibility rule` paragraph and extracted four offer-structure attributes **verbatim** (entry-offer shape, commitment/continuity lever, mandatory-separate-membership flag, when the real all-in is visible). Built one derived receipt ([`receipts/glp1-offer-structure-panel.md`](receipts/glp1-offer-structure-panel.md)) and wrote the read keeping the table-stakes and business-model-split claims explicitly labeled `[J]` and tied to per-brand captured State. No external fetch, no `store/` write.

## Inputs and scope

- `store/*/telehealth.md` frontmatter (`anchor_category: GLP-1`) — cohort derivation → 19 brands.
- `store/<domain>/offerings.md` `site_notes` + `## Portfolio overview` + `Visibility rule` for all 19 (captures 2026-05-30…06-18).
- **Exclusions:** generalist GLP-1 lines inside `multi/none` brands not scored; GLP-1-anchored brands lacking `offerings.md` not in frame. Partial denominator, stated plainly.

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
# For bounded-live, paste the selected Scout plan here.
```

## Live evidence used

Required for every outside source used in `bounded-live`. Leave `[]` for local-only runs.

```yaml
live_evidence_used: []
# For bounded-live entries:
# - source_or_query:
#   source_family:
#   action_taken: searched | opened | captured | scraped | read-local-signal
#   reason:
#   source_grade: primary | secondary | direction-finding
#   captured_at:
#   spend_note: none | free | paid-credit
#   claim_ids_supported: []
```

## Friction log

- **Same latest-capture / field-extract loop** as 008/009, but on a *third* field surface — the `site_notes` + Portfolio + Visibility-rule prose rather than the `Visibility` column (008) or `Credibility & access`/`Notes` (009). Extraction was one `awk`/`grep` per brand; the only real labor was the Judgment of the membership-wedge split.
- **The classification cells came from prose `site_notes`, not a structured field.** Unlike 008's `Visibility` column or 009's `access_model` frontmatter, offer-structure (cadence, commitment, membership wedge) lives in narrative `site_notes` + Portfolio paragraphs. Faithful to quote, but not greppable as a field — a coverage-grain observation, not a request to schematize.

## Evidence limits

- **Partial denominator** — 19 GLP-1-anchored brands with `offerings.md`; generalist GLP-1 lines and any anchored brand without `offerings.md` are out of frame. Not a census. Findings are structural (don't depend on the exact denominator), so completeness is not load-bearing.
- **Promo/A-B-volatile prices** — flagged in nearly every `site_notes`; figures are captured floors ≤ ~3 weeks old, not live quotes. The *structure* findings are durable; the specific numbers rot fast.
- **Intake-gated dose ladders** — several brands show only a floor; the true per-dose all-in is behind a quiz and uncaptured.
- **C3/C4/C5/C6 are derived Judgments**, labeled `[J]` throughout and tied to verbatim captured fields.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live fetch, no mutation, no spend; partial denominator flagged; prices read as captured floors)
- Required citations / receipts present and source-graded: **pass** (one derived receipt, S1–S12 graded; 19 brands primary)
- No snippet treated as evidence: **pass** (no snippets used; pure captured State)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (every price ties to a dated capture; no current/news claims; prices labeled captured-floor)
- Absence language says "not found", not "not true": **pass** ("not scored", "not captured", "on-request", "uncaptured" — never "no such thing exists")

## Surprises

- **The sticker price is theater — and it's category-wide.** Three independent mechanisms converge to make "$X/month" not equal what you pay. A buyer comparing two "$199/mo" brands is very likely comparing med-only-plus-membership against all-in-charged-upfront. More decision-relevant than any single price.
- **"No membership" is itself a positioning claim.** henry, mydrhank, fridays, medvi actively market *against* the wedge ("no membership, no hidden fees") — the absence of a fee is a marketed differentiator.
- **The bundle that doesn't discount.** telolife's 3/6/9/12-mo bundles divide to exactly the month-to-month $199/mo — they *prepay* the rate, they don't lower it; the "savings" are a card/wallet discount + Cherry financing framing. Commitment laddering looks like a discount but sometimes isn't.

## Pressure tags

Short `kebab-case` tags for system pressure this run exposed. These are recurrence handles, not a fixed taxonomy and not permission to build.

Use an existing tag when it fits; coin a narrow tag only when the guide misses the thing.

| Tag | Use when |
|---|---|
| `denominator-reconciliation` | The answer depends on defining / cleaning / reconciling the company or source **set**. |
| `source-rigor` | Source grade blocks confidence: snippets, weak secondary sources, missing URLs, or missing capture dates. |
| `source-panel` | A repeated external source **set** seems needed to answer this kind of question. |
| `coverage-caveat` | Store coverage, stale captures, or incomplete modules materially limit the answer. |
| `depth-backfill` | A specific field/module is missing across otherwise relevant companies. |
| `query-time-grouping-enough` | The read was answerable by grouping existing store evidence; no durable category object is needed. |
| `freshness-monitoring` | Current pricing, news, policy, regulation, or launch motion could change or materially improve the answer. |
| `relation-pressure` | Competitors, named parents, suppliers, partners, or other counterparties seem repeatedly useful. |
| `tooling-ergonomics` | Repeated manual steps suggest a helper, query recipe, or template tweak. |

Which tags fired, if any? Did this run need a new or clearer tag?

"No new primitive needed" is a valid outcome.

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `query-time-grouping-enough` | The whole read was a grouping of existing `offerings.md` offer-structure State; no durable "offer-shape" or "membership-model" category object is needed or wanted. | no-op — reinforces MRL-002 recipe scope (now a *third* State surface: offer-structure, after pricing 008 and positioning 009) |
| `coverage-caveat` | Partial cohort (19 anchored brands, generalists out of frame); promo/A-B-volatile prices; intake-gated dose ladders — all bound the completeness claim. | watch / strengthens MRL-001 |
| `freshness-monitoring` | Prices are promo/A-B-volatile (struck-through, countdowns, A/B engines); the *structure* is durable but the figures rot fast. | watch — first clean `freshness-monitoring` fire in the recent State runs; pricing-figure staleness is a real consumer-of-the-read risk |

No new tag needed. "No new primitive needed" is the honest outcome — this is a recurrence read on a new field surface.

## Triage submissions

No new items. This run **adds recurrence evidence** to existing queue items; Loop 2 may append Evidence Log entries to:

- **MRL-002** (query recipes) — a *third* State-read surface recurred cleanly: offer-*structure* (latest-capture → `site_notes`/Portfolio/Visibility-rule read → membership-wedge + commitment classification), after price-posture (008) and positioning (009). Same latest-capture + field-extract idiom, but the extract is from **narrative `site_notes`, not a structured field** — a useful contrast (008's `Visibility` column and 009's `access_model` were greppable; offer-structure is prose). Strengthens "State reads beyond pricing"; still recipe-level, no helper.
- **MRL-001** (denominator reconciliation) — the GLP-1-anchored cut was clean (one `anchor_category` grep), but the *business-model split* (membership-wedge) was the hand-drawn boundary this time — the labor moved from cohort-edge to within-cohort classification. A useful contrast data point.

No graduation, no implementation, no spike proposed.

## Next-run advice

- **Quantify the "$X/month ≠ what you pay" pattern** in a tight store-only follow-up: across the cohort, what share of headline monthly prices are (a) upfront-÷-N, (b) med-only-plus-membership, or (c) dose-floor? Turns the qualitative finding into a number.
- **Test the membership-wedge split on a second cohort** (TRT or longevity already have `offerings.md`) — does "med-included vs med-plus-membership" recur as the business-model tell off the offer-structure surface, the way price-posture did on the pricing surface (008→TRT)?
- **A captured cancellation/refund-terms field** is the gap that would turn "commitment is the real lock-in" from a cadence inference into evidence — flag for human judgment, do not build.
- Tell the operator to start **Loop 2** in a fresh session.

---

**Loop 1 complete — `run_status: read-done`.** Start Loop 2 for review.
