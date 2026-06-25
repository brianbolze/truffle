# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [coverage-caveat, source-panel, source-rigor, query-time-grouping-enough, depth-backfill]
```

## 30-second operator read

- Did the run work? Yes — clean store-only calibration of the engine's #1 value job
  ("Make AI safe to delegate to"), never a run's explicit subject before. Result is sharp:
  grounding is **ingredient-type-shaped, not brand-shaped** — strong on offer/price, dark
  on state-availability and independent proof, and the dark spots mirror the *industry's*
  intake-gating, not a schema gap.
- What was awkward? Nothing operationally; one grep set the panel, profiles carried the
  four ingredient types in frontmatter + body. The work was judgment (decision-grade vs
  gestured vs absent), not retrieval.
- What should the next agent know? The headline is the typed grounding map (read.md
  Result). Two observations matter most: G1 (state-level availability is the systematically
  invention-forcing type — intake-gated, not a capture miss) and R1 (self-reported
  proof/scale is captured *with* honest flags, but the flag is prose-grade — a delegated
  agent that relays the claim without it launders marketing into fact; the delegation-relay
  grain of L002). "No new primitive needed" is the honest outcome.

## What happened

Selected an 8-brand panel (henrymeds, hims, ro, joinfound, lifemd, ivimhealth, hellowisp,
remedymeds) from the 57 GLP-1-mentioning store profiles via `grep -ril`. Read the SCHEMA
price-visibility / business_model contract, then judged each of four ingredient *types* —
entry price, offer/continuity structure, trust/proof claims, geographic availability —
per-brand as decision-grade-cited / gestured / absent, using frontmatter tokens +
`unverified_fields` + body prose. Synthesized the typed grounding map. No live evidence, no
spend, no store mutation.

## Observations

Greedy raw learning for this run. Preserve singletons here, then Loop 2 appends the
useful rows to `learning/observations.md`. Do not merge rows, dedup into backlog items,
or translate wishes into build proposals inside the run.

Use short IDs such as `F1`, `S1`, `W1`, `G1` so reviews can cite them. Kinds are the
closed set: `friction` · `surprise` · `wish` · `gap` · `risk-miss` · `brian-correction`.
Record the symptom in `Saw`; put the boundary you are deliberately not asserting in
`Not claiming` (no fix, no build proposal).

| ID | Kind | Saw | Not claiming | Evidence pointer | Tags |
|---|---|---|---|---|---|
| G1 | gap | **State-level geographic availability** is the systematically invention-forcing ingredient type for a delegated buyer brief: the binary "all-50 / broadly available" claim is captured for ~3/8, but "can I get this in MY state" is unanswerable for ~6/8 (henrymeds doesn't enumerate; joinfound's ~40-state list is behind a gated picker; remedymeds/ivimhealth carry no state line). It is **intake-gated** — the data isn't on the marketing site — so even a refresh capture wouldn't recover it without entering the funnel. hellowisp is the exception (per-state license page). | That the store *should* capture state availability or that a field is missing — it's a source-scope (intake-flow) boundary the store honestly flags; per L004/L005 "not captured" ≠ "not available." | read.md Result(4); henrymeds unverified_fields:33; joinfound:35-36; remedymeds:27/127; hellowisp:93/137 | coverage-caveat, source-panel |
| R1 | risk-miss | Trust/proof and scale claims are captured *with* honest self-reported flags (henrymeds 4.4 self-reported; remedymeds 4.7 badge-image + "250,000+ members" internally inconsistent across its own pages; ivim "470K+"), but the flag lives in **prose**. A delegated agent that surfaces the captured claim without carrying its self-reported/unverified label launders marketing into apparent fact — the protection is read-discipline-dependent, not structural. | That the capture is wrong or a flag field is needed — the store flags correctly; only that the flag is prose-grade and depends on the downstream agent preserving it. The delegation-relay grain of L002. | read.md Result(3); remedymeds:106/108/139; ivim:118; henrymeds:104 | source-rigor, query-time-grouping-enough |
| S1 | surprise | Grounding for a delegated brief is **ingredient-type-shaped, not brand-shaped**: the *same* brand grounds strongly on offer structure + advertised price and weakly on state availability + independent proof. The frontier cuts across the four types uniformly, not across "well-captured vs thin" brands — so "is this company agent-ready?" is the wrong question; "is this ingredient *type* agent-ready?" is the right one. | That grounding never varies by brand — capture richness still differs (hellowisp/hims deeper than remedymeds); only that the dominant axis of the frontier is ingredient type, not brand. | read.md Result(1)-(4); panel-wide pattern | query-time-grouping-enough, coverage-caveat |
| G2 | gap | The two grounding shortfalls (state availability; independent verification of price/scale/proof) share **one root**: the decision-grade fact lives **off the marketing site** — behind intake (price, state lists) or in filings/IR (audited scale for public cos hims/lifemd). Delegation analogue of run-036 G2 (marketplace take rate off-site) and run-037 Source Gaps (hybrid economics off-site): the same "decision-grade lives off the captured surface" boundary, now hit by the grounding-for-delegation lens. | That the store should capture intake/filings — only that these are the source families a fully-grounded delegated brief would need; spend/approval-gated. | read.md Source Gaps; run-036 G2; run-037 Source Gaps | source-panel, depth-backfill |
| W1 | wish | If anything ever graduates from R1, the lightest path is a **read/relay convention** — "carry the self-reported flag and the intake-gated price caveat into any delegated output" — NOT a new provenance field or a capture mandate. Load-bearing reason: the store already holds the flag; the failure is at relay, so the fix is a synthesis/output discipline, mirroring L004's "reconciliation travels with the read." | That it should graduate now — only the lightest path *if* a real delegated consumer + a second cohort showing the same relay risk appear. "No new primitive needed" stays live. | read.md What Would Change; lessons.md L002/L004 | query-time-grouping-enough |

## Inputs and scope

- **Panel (8):** henrymeds-com, hims-com, ro-co, joinfound-com, lifemd-com, ivimhealth-com,
  hellowisp-com, remedymeds-com.
- **Denominator draw:** `grep -ril -E "glp-1|semaglutide|tirzepatide" store/*/profile.md`
  → 57 profiles; purposively narrowed to 8 well-captured DTC weight-loss brands. A panel,
  not a census (L004).
- **Ingredient types judged:** (1) entry price, (2) offer/continuity structure, (3)
  trust/proof claims, (4) geographic availability — each scored decision-grade-cited /
  gestured / absent per brand from frontmatter tokens + `unverified_fields` + body prose.
- **Contract files:** SCHEMA price-visibility token; TAXONOMIES business_model.
- **Exclusions:** the ~49 other GLP-1-mentioning profiles (TRT/longevity/sexual-health
  brands that mention GLP-1 in passing, or thinner captures) — out of panel, not out of
  store.
- **Source panel:** store-only. No live evidence, no spend.

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
```

## Live evidence used

Required for every outside source used in `bounded-live`. Leave `[]` for local-only runs.

```yaml
live_evidence_used: []
```

## Friction log

None. One grep set the panel; profiles carried the four ingredient types in frontmatter +
body. No missing helper, no path confusion. The effort was per-cell grounding judgment, not
retrieval.

## Evidence limits

- Prices are promo-period / A-B snapshots across the panel (every profile flags active
  promos or an own A-B engine) — used as structure illustration, not live magnitudes.
- Intake-gated facts (all-in/per-dose price, enumerated state lists) are uncaptured by
  design — flagged in each profile, not asserted.
- Self-reported ratings, scale, and outcome figures are captured verbatim but not
  independently verified; remedymeds's scale figures are internally inconsistent across its
  own pages.
- n=8 single-cohort panel; the type-shaped grounding frontier is mapped on DTC GLP-1, not
  generalized beyond it (a 2nd cohort is the named hardening test).

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browse, no spend, no store mutation, no schema-change proposal)
- Required citations / receipts present and source-graded: **pass** (all store paths + line numbers; contract cites)
- No snippet treated as evidence: **pass** (store-only)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (prices labeled point-in-time snapshots, structure-only; no live magnitude asserted; self-reported claims labeled)
- Absence language says "not found", not "not true": **pass** (G1 framed as intake-gated/"not captured," per L004/L005)

## Surprises

The expected finding was "the store grounds the dense GLP-1 cohort well." The sharper,
unexpected result is that grounding cuts by **ingredient type, not brand** (S1): the same
profile is a strong agent substrate for offer structure and a weak one for state
availability. And the two weak types share a single root (G2) — the fact lives off the
marketing site — which makes the grounding frontier a mirror of the *industry's* disclosure
frontier (intake-gating), not a Truffle coverage defect. The store is as transparent as the
sites it captured, and honestly flags where they go dark.

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

Fired: `coverage-caveat` (the grounding frontier is a coverage/source-scope boundary),
`source-panel` (the two shortfalls need a non-marketing source family — intake flow,
filings/IR), `source-rigor` (self-reported claims captured but unverified; relay risk),
`query-time-grouping-enough` (the typed grounding map reads from existing store evidence; no
field needed), `depth-backfill` (the off-site decision-grade facts). No new tag needed —
the run is the delegation-job lens on the recurring "decision-grade lives off the captured
surface" pressure (036 G2 / 037 source gap), not a new mechanism.

"No new primitive needed" is the honest outcome here.

## Next-run advice

- The "decision-grade lives off the marketing/captured surface" boundary now has three
  sightings (036 marketplace take rate, 037 hybrid economics, 038 GLP-1 price/availability).
  A learning pass might cluster these into one "the store's grounding frontier is the
  *source-scope* frontier — what the captured surface exposes — and decision-grade economics
  / eligibility / audited scale routinely sit off it" lesson. That's the pass's call.
- If re-running the delegation lens, test a **second cohort** (TRT or longevity) for the
  same ingredient-type-shaped frontier — that would harden or dissolve S1's "type-shaped,
  not brand-shaped" claim beyond GLP-1.
- Avoid re-running as another GLP-1 price/offer table (008/010/012/023) — the value here is
  the grounding/relay lens, not the offers.
