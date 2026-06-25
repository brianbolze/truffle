# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [schema-edge-entity-type, query-time-grouping-enough, denominator-reconciliation, source-rigor, freshness-monitoring]
```

## 30-second operator read

- **Did the run work?** Yes. A clean store-only gap-probe on a fresh axis (commercialization
  maturity) and a near-untouched vertical (deep-tech). Real result: a careful human reader
  **can** rank the 8 cos shipping-vs-vision from captured State, but only from **prose**
  (milestones + `unverified_fields`) — every structured/headline field is maturity-blind, and
  `description` actively over-claims. Split answer by reader type: safe for a human, an
  over-claim risk for a shallow delegated agent. "No new field needed" stays live.
- **What was awkward?** Nothing operationally — store reads were fast. The one notable thing:
  `business_model` is **blank** for 2/8 (cfs, sora), an L005-style subtractive absence the
  schema has no value for ("pre-revenue / no model yet").
- **What should the next agent know?** This is the deep-tech run that run-039's slate
  *rejected as enum-fit* — it works **only** because it's pitched on the maturity axis, not
  business_model. The off-surface source-family gap (filings/trade-press to confirm
  self-reported milestones) is the 4th sighting of the same boundary (036 G2 / 037 / 038 G2).

## What happened

Read all 8 deep-tech profiles in full (frontmatter + bodies + `unverified_fields`).
Confirmed the cohort (7 pre-revenue + euclid as an operating-services foil; ford/uber
excluded per contract). Built a maturity ranking from dated milestones prose, then compared
it against the structured fields. Wrote `read.md` + two store-derived receipts (denominator,
maturity-classification). No external/live sources; no spend.

## Observations

Greedy raw learning for this run. Preserve singletons here, then Loop 2 appends the
useful rows to `learning/observations.md`. Do not merge rows, dedup into backlog items,
or translate wishes into build proposals inside the run.

| ID | Kind | Saw | Not claiming | Evidence pointer | Tags |
|---|---|---|---|---|---|
| G1 | gap | The present-tense `description` field **launders vision into shipping** on pre-revenue deep-tech: electra "**Builds** the EL9," evoloh "**Manufactures** electrolyzer stacks," sorafuel "**Produces** sustainable aviation fuel" — yet electra has delivered zero, evoloh delivers 2026-27, sorafuel has no production (pilot still to be built). The single field most likely to be quoted in a cold-start is the one that over-claims maturity hardest. | That `description` is wrong or should encode stage — it accurately states positioning/intent; only that read as attainment it over-claims, and it's the maturity-blind field a shallow consumer leans on. | read.md Result(2), C3; electra/evoloh/sorafuel `description` lines | schema-edge-entity-type, source-rigor |
| G2 | gap | No structured field encodes commercialization maturity. `business_model` is **blank** for cfs-energy + sorafuel (closed set has no "pre-revenue/no-model-yet" value — subtractive absence, cousin of run-035's empty-business_model-for-investors), intent-only where populated; `offering_category` shares the same hardware value `[Physical Products / Hardware]` for beta-team (public, shipping components; also lists Services / Consulting) and electra (zero deliveries), so the value they share encodes no maturity. The gradient compresses to flat across all structured fields. | That a maturity/stage field should be built — n=8, single cohort, prose carries it; a stage field would rot (captor judgment on a continuum, fastest-decaying, mostly-blank). "No new primitive needed" stays live. | read.md Result(2)/(3), C3; cfs+sora blank business_model; electra vs beta offering_category | schema-edge-entity-type, query-time-grouping-enough |
| S1 | surprise | `unverified_fields` is the **unsung maturity-protector**: across all 8 it honestly flags exactly the maturity-relevant absences ("current production… planned pilot"; "pre-order pipeline is site-reported, not a price card"; "capital raised is self-reported"). The one near-structured surface that guards against over-claim — but it's a free-text list whose protection depends on the downstream reader carrying it (L002/L004/038-R1 relay shape, here on the maturity axis). | That `unverified_fields` is sufficient or structured — it's prose-grade and relay-dependent; only that it, not any typed field, is what makes the read safe. | read.md Result(4), C2; `unverified_fields` across the 8 | source-rigor, query-time-grouping-enough |
| S2 | surprise | Counter to the recent "store falls short for the buyer" run streak, the store here is **a genuine strength**: the 8 rank *cleanly* on maturity because the bodies carry dated, specific anchors (IPO/10-Q, first-flight date, FAA cert-application date, NRC milestone, "operational in 2027", "pilot in 18–24 months"). The gap-probe found a positive — maturity is legible from State, just not queryable. | That maturity is always recoverable — depends on the captor writing a milestones block; only that for this cohort the prose carried it well. | read.md Result(1), C2; per-profile milestones | query-time-grouping-enough, source-rigor |
| G3 | gap | **Fourth sighting** of denominator-reconciliation: `primary_industry` scatters the cohort across Automotive (electra) / Manufacturing (verdego, beta) / Energy (other 5), and the energy draw pulls in **euclidpower** — a commercially operating renewable-energy services+SaaS firm, **not** pre-revenue deep-tech. An industry/category draw does not recover the entity-shape cohort "pre-revenue deep-tech." (After run-036 G3, run-037 G2, run-039 DR1.) | That industry tags are wrong — each is individually defensible; only that the recurrence (n=4 across distinct entity-shape cohorts) is now consistent. | read.md Companies Seen, C1; `primary_industry` grep; euclid profile | denominator-reconciliation |
| R1 | risk-miss | **Delegation over-claim risk against the engine's #1 value job.** A delegated agent doing the cheap thing — quoting `description` + frontmatter — would present sorafuel ("Produces SAF") and electra ("Builds the EL9") as shipping companies, when neither has commercial output. The protection (milestones + `unverified_fields` + "self-reported" labels) lives only in prose, so safety is read-discipline-dependent, not structural. Maturity-axis instance of run-038 R1. | That the capture is wrong or a flag field is needed — the store flags honestly; only that the guard is prose-grade and fails at relay if the consumer is shallow. | read.md Market Pattern, Result(2); G1; run-038 R1 | source-rigor, query-time-grouping-enough |
| W1 | wish | If anything ever graduates from G1/R1, the lightest path is a **read/relay convention** — "for pre-revenue/deep-tech, rank maturity from the milestones block + `unverified_fields`; treat present-tense `description` as positioning not attainment; carry the self-reported flag" — NOT a `stage`/`maturity` field. Load-bearing reason: a stage field is a rotting captor judgment, mostly-blank store-wide, failing engine-dev's fillable-cut bar. Mirrors run-036/037/039/040 anti-sprawl W1 landings. | That it should graduate now — only the lightest path *if* a 2nd pre-revenue cohort shows the same description-overclaim AND a consumer needs to *filter* by maturity. | read.md What Would Change; .claude/rules/engine-dev.md | query-time-grouping-enough |
| G4 | gap | The **filings / IR / trade-press** source family is the off-surface panel needed to independently date/confirm the self-reported milestones (10-Q for beta-team; press for the rest) that the whole maturity read rests on. **Fourth sighting** of "decision-grade fact lives off the captured surface" after run-036 G2 (marketplace take rate), run-037 (hybrid economics), run-038 G2 (price/state/scale) — now on the maturity axis. | That the store should capture filings — only that it's the panel a *confirmed* (vs site-attested) maturity read would need; spend/approval-gated, not chased here. | read.md Source Gaps; run-036 G2 / 037 / 038 G2 | source-panel, depth-backfill |

## Inputs and scope

- **Slice (n=8, read in full):** electra-aero, verdegoaero-com, blueenergy-co, cfs-energy,
  euclidpower-com, evoloh-com, sorafuel-com, beta-team. All captured 2026-06-14.
- **Cohort verdict:** 7 pre-revenue deep-tech + euclidpower as an operating-services foil.
- **Excluded foils (per Scout contract):** ford-com, uber-com.
- **Sources:** store `profile.md` frontmatter + bodies + `unverified_fields` only; one
  `grep` of `primary_industry` store-wide for the denominator finding. No external sources,
  no modules beyond profile bodies, no spend.

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
# For bounded-live, paste the selected Scout plan here.
# Default light ceilings: 2 source families, 6 outside sources read/captured,
# 20 paid capture credits. Lower if Scout set a tighter plan.
# Fail closed before exceeding the ceiling, adding an unplanned source family,
# broadening into search/crawl, or using login/paywalled/private sources.
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

No operational friction — store reads were fast and the cohort small. The only "friction"
is conceptual and is the finding itself: maturity has to be reconstructed by hand from
prose because no field carries it.

## Evidence limits

- All maturity anchors are **site-attested / self-reported** (funding, orders, pipelines,
  partner/offtake deals), flagged as such by the profiles. Only beta-team has linked SEC
  filings, and those were not scraped. The ranking is relative and defensible, not audited.
- The cohort is a **known-partial, capture-biased** slice (8 profiles that happen to be in
  the store), not a deep-tech census. Findings G1/G2/R1 stand at n=8, single cohort.
- blueenergy + sorafuel captures sit close behind fast-moving Apr–May 2026 milestones, so
  their absolute stage is the most freshness-sensitive in the set.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (read-only; no live browsing, no spend, no write-back)
- Required citations / receipts present and source-graded: **pass** (2 store-derived receipts, graded)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (all dated 2026-06-14, store-derived; milestones labelled self-reported)
- Absence language says "not found", not "not true": **pass** ("not found in the captured slice"; "site-attested, not audited")

## Surprises

The gap-probe found a **positive**: maturity is cleanly legible from captured State (S2),
breaking the recent run streak where the store fell short for the buyer. The catch is that
it's legible-not-queryable, and the protection lives in prose. Second surprise: 2/8 carry a
**blank** `business_model` (S1/G2) — the schema has no value for pre-revenue.

## Learning tags

Short `kebab-case` recurrence handles for system pressure this run exposed. They mirror
the run header's `learning_tags`. These are not a fixed taxonomy and not permission to
build — a learning pass decides what, if anything, recurs into a lesson.

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

Which tags fired, if any? Did this run need a new or clearer tag? Mirror them into the
header `learning_tags`.

**Fired this run:** `schema-edge-entity-type` (maturity-blind fields on a new entity shape),
`query-time-grouping-enough` (prose carries it; no field needed), `denominator-reconciliation`
(industry draw ≠ pre-revenue cohort, n=4), `source-rigor` (self-reported milestones; prose-grade
guard), `freshness-monitoring` (stage decays fastest). No new tag coined — existing tags fit.
The maturity axis is a new *application* of `schema-edge-entity-type`, not a new tag.

"No new primitive needed" is a valid outcome — and is the standing outcome here.

## Next-run advice

- A clean **2nd pre-revenue cohort** (early biotech, pre-launch consumer hardware) would test
  whether G1/R1 (present-tense `description` over-claims maturity) generalizes beyond deep-tech.
- The parked **bounded-live follow-on** (scout Q5: company newsroom + 1 trade article to confirm
  self-reported milestones) is the natural sharpener for G4 — but only with a tighter,
  PDF-aware spend ceiling given run-040's breach.
- Avoid re-running this as a `business_model`/enum-fit read; the value here was the maturity axis.
