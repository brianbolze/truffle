# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [denominator-reconciliation, coverage-caveat, depth-backfill, query-time-grouping-enough, source-rigor, tooling-ergonomics]
```

## 30-second operator read

- **Did the run work?** Yes. Clean whole-store calibration census (N=136). The required
  scalar contract is genuinely 100% filled, but "present" splits into four dependability
  tiers — and two are traps: (a) high-fill fields are concentration-lopsided so they
  read well but partition badly; (b) the inline-`#`-comment empty convention masks true
  emptiness from a naive parser. Relations (`parent` 13% / `owns` 11%) are too sparse to
  be a population key; module layers (offerings/visual/signals) are a telehealth overlay,
  not store-wide. "No new primitive needed" stays live.
- **What was awkward?** My own first census pass over-counted `business_model` as 100%
  non-empty because the empty lines carry `# empty — VC…` comments — I had to strip
  inline comments to find the 6 true empties (R1, the parsing trap, reproduced on myself).
- **What should the next agent know?** This is a *positive* answer to "what can a
  downstream system build on": required scalars + `unverified_fields` (the lone
  always-present guard, 136/136) are bedrock. It also re-confirms three recurring shapes
  at whole-store grain — `primary_industry` is a lopsided partition key (52% one value;
  denominator-reconciliation, now n=6 across 036/037/039/042/054, here store-wide), the
  vertical-relation axis is structurally first-class but populated too thinly to partition
  on (039 S1), and subtractive-empty is `entity_type`-gated (035, now sized).

## What happened

Store-only. Grepped/awk'd the frontmatter of all 136 `store/*/profile.md`: per-field
present vs non-empty rate; value-distribution + modal-share (concentration) for the
group-by fields; comment-stripped re-count to separate true-empty from comment-masked;
located the subtractive empties against `entity_type`; bucketed optional-module presence
(`offerings.md`/`visual.md`/`signals/`) and body length by `primary_industry`. No external
sources, no spend, no mutation. Findings written to `read.md` as a four-tier dependability
map.

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
| S1 | surprise | The store's dependability is **tiered, not binary**: the required scalar contract is 100% filled (domain/name/captured_at/entity_type/primary_industry/description/target_market/offering_category/business_model/portfolio_shape/color_scheme), but "present" splits four ways — dependable-and-discriminating, subtractive-empty-but-meaningful, too-sparse-to-partition, and telehealth-only-overlay. "Is the field filled?" alone does not tell a consumer what it can build on. | That any tier is broken — each is working as designed; only that a downstream consumer must combine fill-rate + value-concentration + entity_type-gating + the comment convention to know the dependability tier. Calibration, not a defect. | read.md Result Tiers 1–4; C1 census (N=136) | query-time-grouping-enough, coverage-caveat |
| S3 | surprise | A **100%-filled field is not a 100%-useful partition key**: `primary_industry` puts 52% of the store in one Healthcare pile, `entity_type` is 90% `Company`, `target_market` 43% `[B2C]`. High fill + high concentration = reads cleanly but groups lopsidedly. Whole-store version of run-039 G1 (the SaaS pile is one undifferentiated bucket). | That these fields are bad — they're dependable to read; only that fill-rate overstates their power as a *partition* key when one value dominates. | read.md Result Tier-1 table + C2; run-039 G1 | denominator-reconciliation, query-time-grouping-enough |
| G1 | gap | The vertical-relation fields are too sparse to be a population key: `parent` 18/136 (13%), `owns` 16/136 (11%), `aliases` 80/136 (58%). Filtering/grouping on `parent`/`owns` silently drops ~87–89% of the store, and the field alone cannot separate a true-negative (`[]` because no parent exists) from a not-captured one. The vertical axis is structurally first-class (039 S1) yet populated too thinly to partition on. | That a relation backfill or new field is needed — only that the existing structured relation axis can answer "does THIS company name a parent?" but not "show me all subsidiaries." L005-corollary sized store-wide; spend/approval-gated if ever chased. | read.md Result Tier-3 + C5; run-039 S1; lessons.md L005 | relation-pressure, depth-backfill, coverage-caveat |
| S2 | surprise | Subtractive emptiness is **perfectly `entity_type`-gated**: every empty `business_model` (6), `portfolio_shape` (7), and `offering_category` (3) belongs to an `Investor / Holding` entity (firstround, lsvp, sequoiacap, spero-vc, standishspring, thrivecap, blueowl). The closed set has no value for AUM/carry economics, so the blank *encodes* shape rather than missing data. Whole-store confirmation of run-035's empty-business_model-for-investors sighting. | That the empties should be filled — they're correctly empty; only that a consumer must read them through `entity_type`, not as coverage holes. | read.md Result Tier-2 + C3; business_model/portfolio_shape empties = the 7 investors | schema-edge-entity-type, query-time-grouping-enough |
| G2 | gap | The optional **module layers are a telehealth overlay, not store-wide substrate**: `offerings.md`/`visual.md`/`signals/` run 81%/49%/74% on the 71 Healthcare profiles vs 18%/11%/3% (Tech), 0%/0%/0% (Energy). Yet the profile *body* is uniform depth (~8–9k chars) across verticals. A downstream system consuming `offerings.md` or `signals/` as a store-wide ingredient is really leaning on a telehealth-concentrated layer. | That the asymmetry is a defect — deep telehealth is an intentional cohort choice; only that the module layers are not a store-wide ingredient and their absence outside Healthcare is a coverage fact. | read.md Result Tier-4 + C6; module-presence-by-vertical table | coverage-caveat, depth-backfill |
| R1 | risk-miss | The **fail-loud-by-comment convention defeats naive structured parsing**: the store records subtractive emptiness as `business_model:    # empty — VC economics…`, and a parser that splits on `:` and takes the remainder reads the **comment as the value**. My own first census pass counted `business_model` 100% non-empty until I stripped inline `#` comments, which exposed the 6 true empties. The guard that protects a human reader actively misleads a naive machine consumer. Cousin of run-037 DR2 (STRAIN comment = unreliable second channel), here on the structured-emptiness channel. | That the convention is wrong or the parser must change — only that a downstream consumer reading frontmatter values MUST strip inline comments first, or it ingests comment text as data. A read-side parsing hazard, not a schema defect. | read.md Trap A + C7; first-pass vs comment-stripped business_model counts | source-rigor, tooling-ergonomics |
| S4 | surprise | `unverified_fields` is the **one always-present guard field**: 136/136 non-empty — every profile self-discloses its soft spots. The single most reliable provenance/honesty surface in the store, and (unlike the headline fields) it never degrades to empty. | That it is structured or machine-graded — it's a free-text list; only that its *presence* is universal, making it the dependable hook for "what did this capture flag about itself." | read.md Result Tier-1 + C4; unverified_fields 136/136 | source-rigor, query-time-grouping-enough |
| CR1 | surprise | (Consumer review) The read's value lands squarely on the **Pantry/builder** consumer and is **nil for the end buyer** — but *by design*: this is a system-test/introspection read, not a market read. Continues the 038/039/041 CR1 "lands on builder not buyer" shape, here as an intended property rather than a shortfall. | That the read failed the buyer — it never targeted one; only that a whole-store reliability census is structurally a builder deliverable. | consumer-review.md Verdict; read.md Question/frame | query-time-grouping-enough, coverage-caveat |
| DR1 | risk-miss | (Developer review / evidence-verify) read.md Tier-2 first phrased "7 investor empties" as if all 7 had an empty `business_model`; in fact `business_model` is empty for 6 (the VCs) and the 7th, blueowl, carries `business_model: Other` (asset-manager fees, closed-set misfit) and is empty only for `portfolio_shape`. Core claim ("every subtractive empty is `Investor / Holding`") survives and is *strengthened* (blueowl gets `Other`, not blank). Precision slip caught + corrected in read.md, cousin of run-042 VR1. | That the finding was wrong — only that the count phrasing overstated `business_model` empties by one; the entity-gating story is intact and sharper. | developer-review.md; read.md Tier-2 (corrected); blueowl business_model: Other | source-rigor, schema-edge-entity-type |

## Inputs and scope

- **Slice:** all `store/*/profile.md` (N=136), frontmatter only; bodies used only to read
  body length and confirm empty-vs-default.
- **Method:** grep/awk for per-field present vs non-empty; values read as text *before* any
  inline `#` comment; modal-share per group-by field; module presence via `offerings.md` /
  `visual.md` / `signals/` existence; verticals bucketed by `primary_industry`.
- **Reference:** SCHEMA.md / TAXONOMIES.md as the field contract.
- **Exclusions:** no external sources, no Firecrawl, no `store/` mutation, no re-capture.

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

Repeated manual steps, took a long time, confusing paths, missing helpers, schema mismatches.
Summarize the operational friction here after preserving concrete sightings in the
Observations section.

## Evidence limits

Coverage gaps, stale captures, weak source grain, risky inference.

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
- No disallowed action happened: **pass** (no external source, no mutation, no spend)
- Required citations / receipts present and source-graded: **pass** (claim IDs C1–C7 are all
  local-derivation receipts; no external/current claims requiring URLs)
- No snippet treated as evidence: **pass** (no snippets used)
- Current/news/pricing/policy claims carry capture dates and source grade: **n/a** (no such claims)
- Absence language says "not found", not "not true": **pass** (fill-rates framed as
  capture-coverage facts, not market facts, throughout)

## Surprises

The store-internal census surfaced a methodological surprise on the operator: the
fail-loud-by-comment convention (R1) masked true emptiness from the first grep pass — a
neat demonstration that the human-protective guard is anti-machine-readable. Substantive
surprise: a 100%-filled field can still be a weak partition key (S3), so "fill-rate" alone
overstates queryability.

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

Fired: `denominator-reconciliation` (S3 — lopsided partition key, n=6 now), `coverage-caveat`
+ `depth-backfill` (G2 module overlay), `query-time-grouping-enough` (S1/S2 — no primitive),
`source-rigor` + `tooling-ergonomics` (R1 parsing trap), `relation-pressure` (G1). No new tag
coined — existing tags cover the run. (`schema-edge-entity-type` used in-row for S2 but not a
header tag in the guide table; left as a row tag.)

"No new primitive needed" is a valid outcome — and it is this run's outcome.

## Next-run advice

- The strongest parked sibling is **C3 — offerings-roster completeness self-disclosure**
  (store-only): G2 shows `offerings.md` exists on 71 profiles but says nothing about whether
  each roster is comprehensive; a natural follow-up.
- R1 (the inline-comment parsing trap) is the one finding with a concrete, cheap read-side
  remedy ("strip inline comments before reading a frontmatter value"). If a learning pass
  ever clusters it, it routes to docs/recipe, not a build. Do not act on it inside a run.
- Avoid re-running a whole-store census soon; this one is the baseline. Re-run only if the
  store grows materially or a field contract changes.
