# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L001 (bounded-live coverage radar — graduated), L002 (headline Signal needs its
  confound sibling), L003 (review/forum *bodies* are an uncaptured ingredient), L004
  (denominators are partial; reconciliation travels with the read), L005 (query-time
  grouping enough when the corpus carries the cut; structured-absence ≠ market-absence),
  L006 (price-visibility token reports buyer-reachability, not intermediary take rate;
  `proposed`). Run 036/037 observations: the schema-edge-entity-type thread (035 investor
  subtractive gate / 036 marketplace two-sided economics / 037 hardware hybrid revenue)
  is now well-mapped across three non-DTC shapes — a 4th would be a parked next step, not
  fresh pressure.
- `scout-context.md`: select for value + reach + roadmap learning, not store-answerability;
  name the builder lens; gap-probes are first-class; calibration that shows where Truffle
  added little is valid; don't merely execute a parked step.
- Last 3 `run-notes.md` files: 035 (finance/investor schema fit — empty business_model
  subtractive gate), 036 (marketplace schema fit — positive fit, no two-sided-economics
  field), 037 (wearable hybrid revenue — single-valued business_model lossy on co-primary
  revenue; "no new primitive needed").
- `question_history.py` map (38 runs): heavily tested shapes — `relation-pressure`
  (001/014/016/017/026/030), price-visibility/offer reads (008/010/012/023/033/035/036),
  `schema-edge-entity-type` (027/035/036/037), source-rigor signal reads
  (005/006/007/018/034). Under-tested **value jobs**: "Make AI safe to delegate to"
  (grounded, non-invented agent inputs) has **never been the explicit subject of a run** —
  it is the engine's #1 stated value job and the most-claimed yet least-calibrated.
  "Trust the cache over time" tested only lightly (018 change-pulse, 032 staleness).
- Current run artifacts, if resuming: fresh scaffold.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| C1 **(recommended)** If an agent is delegated a concrete buyer-facing brief — "compare the captured compounded-GLP-1 telehealth brands across four ingredient *types*: entry price, offer/continuity structure, trust/proof claims, and geographic availability" — and is restricted to store-only cited evidence, what fraction of that brief is answerable with decision-grade cited ingredients, and which ingredient *types* force the agent to flag "not captured" or invent? | calibration | yes | store-only | Directly tests the engine's #1 value job ("Make AI safe to delegate to") — never the explicit subject of a run. The deliverable is a typed grounding map: where the store is a safe agent substrate vs where delegation forces invention. | Whether the store grounds a realistic delegated task across ingredient *types*, or whether some types (likely proof-claims, availability) are systematically prose-gestured / uncaptured at decision grade. Tests the store-as-agent-substrate, not another offer table. | The grounding frontier itself — which captured ingredient types are decision-grade-cited vs invention-forcing — on the densest cohort, so residual gaps are load-bearing. | Store-only profiles + their cited fields/prose; per-ingredient verdict on "decision-grade cited" vs "gestured" vs "absent". | Collapsing into yet another GLP-1 offer read instead of a per-ingredient-type *grounding* verdict; or counting a bare prose mention as a decision-grade cited ingredient. |
| C2 Across the most price-volatile captured cohort (compounded GLP-1), how stale is the captured market-sensitive State (price, offer terms), and can a delegated agent tell per-*claim* (not just per-capture) which facts are decision-unsafe today? | calibration | yes | store-only | Freshness is a delegation risk, lightly tested. | Per-claim vs per-capture staleness legibility. | The "trust the cache over time" job at claim grain. | Store-only `captured_at` + per-claim freshness signals. | Re-runs 032's staleness shape without enough new pressure; overlaps C1's freshness dimension. |
| C3 Across the captured SaaS/Technology slice, what pricing tiers + packaging does each disclose, and where is the positioning whitespace a strategist could exploit? | value-read | yes | store-only | Recognizable strategist read on a non-telehealth slice. | Pattern-extraction on SaaS pricing/packaging. | A non-telehealth value-read. | Store-only profiles + body pricing. | Heavy overlap with run 028 (SaaS pricing-visibility); low marginal learning. |
| C4 For an anchor wearable (Oura), what competitor/substitute set do 2 best-of listicles name vs the store's captured neighbors — does the store under- or over-call the substitute set? | gap-probe | yes | bounded-live | Cross-shop is a recognizable buyer question; tests relation coverage against an external panel. | Relation/neighborhood coverage vs an external source panel. | A bounded external check of the store's substitute map. | 2 listicles + store positioning prose; bounded-live plan. | `relation-pressure` is heavily tested store-only (030 did Exa cross-shop); marginal learning unless the external panel diverges sharply. |
| C5 Across the captured connected-hardware cohort (Oura/Whoop/Eight Sleep/Peloton + foils), what clinical / accuracy / FDA-clearance proof claims does each make, and does the store capture proof at decision grade or only gesture? | value-read | yes | store-only | Proof is a real buyer concern for health wearables. | Proof-claim capture grain on a hardware cohort. | Proof-device grain on wearables (cf. 021 telehealth proof devices). | Store-only profiles. | Re-tests 021's proof-device finding on the cohort 037 just read; freshness/overlap risk. |
| C6 Cutting the whole captured store by "can a delegated agent answer a cold buyer question (price / availability / proof) from cited State alone," which company *profiles* are agent-ready vs which have a load-bearing field that is empty or prose-only? | calibration | yes | store-only | Generalizes C1 store-wide. | Profile-level agent-readiness distribution. | The grounding frontier store-wide. | Store-only; exhaustive grep. | Too broad/inward for one run; C1's single-cohort cut is the sharper, bounded version. |

## Selected Question(s)

1. **C1** — agent-delegation grounding calibration on the compounded-GLP-1 cohort (recommended).
2. C2 — per-claim freshness-as-delegation-risk (backup; partial overlap with 032 and C1's freshness dimension).

These may be Scout recommendations until Brian or the operator confirms one.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: >
  If an agent is delegated a concrete buyer-facing brief — compare the captured
  compounded-GLP-1 telehealth brands across four ingredient types (entry price, offer /
  continuity structure, trust / proof claims, and geographic availability), restricted to
  store-only cited evidence — what fraction of that brief is answerable with decision-grade
  cited ingredients, and which ingredient TYPES force the agent to flag "not captured" or
  invent? The deliverable is a typed grounding map of the store as an agent substrate, not
  another buyer's-guide offer table.
selected_slug: agent-delegation-grounding-calibration
run_type: system-test
question_mode: calibration
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: >
  Captured compounded-GLP-1 / semaglutide telehealth brands already in the store (the ~19
  anchors read by runs 008/010/012/023/034). The cohort draw is a query-time judgment
  (anchor_category / offering prose), not a structured field; pick a bounded panel of the
  6-10 best-captured GLP-1 brands so each of the 4 ingredient types can be judged per-brand
  without sampling the whole tail.
likely_source_panel: store-only (profile.md frontmatter + body; per-claim citation grain)
builder_lens: >
  The store as an agent grounding substrate — does it ground a realistic delegated brief
  across ingredient TYPES, or do some types (suspect: proof-claims and state-by-state
  availability) systematically resolve only as prose gestures / unverified_fields rather
  than decision-grade cited ingredients? Tests the engine's #1 value job ("Make AI safe to
  delegate to") directly, which no prior run has made its explicit subject.
reach_reason: >
  Reaches past "can the store group / answer X" into "can a delegated agent ANSWER a
  realistic buyer brief from cited State without inventing." The result is a typed map of
  where grounding holds vs forces invention — useful whether the verdict is strong or
  shows a shortfall. New lens on a familiar cohort: the novelty is the grounding/invention
  frontier, not the GLP-1 offers (already read by 008/010/012/023/034).
allowed_sources:
  - "store/ (captured compounded-GLP-1 telehealth profiles)"
  - "experiments/00-market-read-lab/learning/"
  - "SCHEMA.md / TAXONOMIES.md (to read what a decision-grade cited ingredient should look like)"
disallowed_actions:
  - "Live browsing, SERP, or Firecrawl spend"
  - "store/ mutation or write-back"
  - "Durable primitive / field creation or lesson graduation"
  - "Proposing a schema or capture change (map the grounding frontier; do not fix it)"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: >
  Answerable entirely from local store profiles and the SCHEMA/TAXONOMIES contract; no
  spend, no live evidence, no write-back. A pure store-only grounding calibration.
loop1_failure_mode: >
  Two traps: (1) collapsing into another GLP-1 price/offer read instead of a per-ingredient
  -TYPE grounding verdict (decision-grade-cited vs gestured vs absent); (2) inflating the
  grounding fraction by counting a bare prose mention or a stale capture as a decision-grade
  cited ingredient. Per L004/L005, "not captured" is not "not true," and an empty/prose-only
  field is a coverage signal, not a market fact.
```

## Selection Notes

C1 wins the two-test screen. **Value:** it targets the engine's most-claimed, least-tested
value job ("Make AI safe to delegate to") — the grounding of agent inputs — which the
38-run history map shows has never been a run's explicit subject. **Reach:** it crosses
from "can the store group/answer this" (the shape of most prior runs) into "can a delegated
agent answer a realistic buyer brief from cited State without inventing," producing a typed
grounding map that is useful whether the verdict is strong or exposes a shortfall (a valid
calibration outcome per `scout-context.md`).

The compounded-GLP-1 cohort is reused deliberately, not lazily: it is the densest captured
cohort (runs 008/010/012/023/034), so any ingredient TYPE that still forces invention there
is a sharp, load-bearing finding rather than a thin-coverage artifact. The novelty is the
lens (grounding/invention frontier across ingredient types), not the offers. The named
failure mode guards exactly the overlap risk — this must end as a per-ingredient-type
grounding verdict, not a buyer's-guide table.

C2 is the backup (freshness as a delegation risk) but overlaps run 032 and C1's own
freshness dimension. C3/C5 were rejected as re-runs of 028 / 021 with low marginal learning;
C4 as a bounded-live relation check whose store-only cousin (030) is already heavily tested;
C6 as too broad/inward — C1 is its sharper single-cohort version.
