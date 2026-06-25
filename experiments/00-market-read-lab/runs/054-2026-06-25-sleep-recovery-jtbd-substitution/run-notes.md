# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
learning_tags: [relation-pressure, denominator-reconciliation, query-time-grouping-enough, depth-backfill, coverage-caveat]
```

## 30-second operator read

- **Did the run work?** Yes. Clean gap-probe. The store cannot recover the cross-industry
  sleep/recovery substitute *set* from any structured field; it's a reader Judgment
  assembled from prose. Per-member State is excellent; the JTBD neighborhood is
  unqueryable. "No new primitive needed" stays live.
- **What was awkward?** Nothing operationally — pure grep over local store. The buyer-goal
  set is full-text-dependent, so completeness is method-bounded (said so explicitly).
- **What should the next agent know?** This is the 5th `denominator-reconciliation`
  sighting that `primary_industry` ≠ entity/goal cohort key (036/037/039/042, now 054),
  the first at the **buyer-goal grain**; and it re-confirms the horizontal-substitute-
  relation absence (039 S1 / 047). Candidate C4 (bounded-live "best sleep tech 2026"
  coverage radar) is the parked sibling.

## What happened

Store-only. Greped `store/*/profile.md` for a JTBD/use-case field (none exists), then
pulled frontmatter for the 8 device/recovery members + 3 telehealth Rx-sleep entrants,
counted the only shared `offering_category` tag's breadth (19), and grepped supplement
adjacency for the fuzzy edge. Assembled the substitute set by hand from `description` +
body; concluded it is a Judgment, not queryable State.

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
| G1 | gap | No structured field encodes the buyer goal / use-case a company serves — grep for `use_case`/`jtbd`/`condition`/`vertical` frontmatter returns zero across 145 profiles. So the sleep/recovery substitute set is recoverable only by full-text reading of `description`+body — a reader Judgment, not queryable State. "Diagnosable but not queryable / map-not-ingredient" frontier (cousin 039 CR1, 043 CR1) now at the **buyer-goal grain**. | That a JTBD field should be built — n=1 goal, open-ended buyer-framed cut; prose carries it for a human. "No new primitive needed" stays live. | read.md Result(1), C1; receipts/C1-no-jtbd-field.md | relation-pressure, query-time-grouping-enough, depth-backfill |
| G2 | gap | **5th sighting** that `primary_industry` ≠ entity/goal cohort key: the 8 device/recovery members scatter across Technology / Healthcare & Life Sciences / Sports & Recreation; add Services+Biotech for telehealth entrants. A naive industry draw recovers none of the JTBD set. First time the recurrence hits at the **buyer-goal grain** (after 036 G3 marketplaces, 037 G2 hardware, 039 DR1 SaaS, 042 G3 deep-tech). | That industry tags are wrong — each is individually defensible; only that the recurrence is now n=5 and extends to buyer-goal cohorts. | read.md Result(2), C2; receipts/C2-industry-scatter.md | denominator-reconciliation |
| S1 | surprise | The telehealth Rx-sleep entrants (rexmd/rugiet/malemd) are **doubly buried**: tag-disjoint from devices (`Services/Consulting`+`Biotech/Pharma`, not Hardware) AND "sleep" is one minor line among ED/TRT/GLP-1/hair, visible only by grepping `description`. No device/wearable draw would ever surface them as sleep substitutes. | That they belong in the set definitively — they sell a real Rx sleep line; only that they're structurally invisible to any cohort draw. | read.md Result(4), C4; rexmd/rugiet/malemd descriptions | denominator-reconciliation, depth-backfill |
| G3 | gap | **Re-confirms** horizontal-substitute-relation absence (039 S1, 047): Oura/Whoop/Eight Sleep are mutual sleep-buyer substitutes but the store carries zero edges between them — relation support is vertical-only (`parent`/`owns`). The JTBD neighborhood can't be traversed even one hop. | That a substitute relation should be built — it'd be mostly empty/dangling today (039 W1 logic); only that the axis is structurally absent. | read.md Result(5); frontmatter (no horizontal relation field) | relation-pressure |
| S2 | surprise | The only shared structured tag, `offering_category:[Physical Products / Hardware]`, is simultaneously **over-inclusive** (19 profiles store-wide — pulls in watches/Casio/Apple catalog) and **under-inclusive** (misses all telehealth+supplement entrants). "Draw all Hardware" is both too wide and too narrow for the sleep/recovery JTBD. | That the tag is broken — it's a coarse leaf working as designed; only that it's not a JTBD key in either direction. | read.md Result(3), C3; 19-profile grep | denominator-reconciliation, query-time-grouping-enough |
| W1 | wish | Wanted a way to filter the store by **buyer goal** across cohorts. Lightest path if anything ever graduates is a **query-time recipe** ("grep description+body for the goal across all cohorts; ignore industry/category as keys") — NOT a JTBD field or substitute relation. Load-bearing reason: JTBD is open-ended/buyer-framed (fails the fillable-cut bar), and no filter/sort consumer has appeared. Mirrors anti-sprawl W1 landings of 036/037/039/042/043. | That it should graduate now — only the lightest path *if* a filter/sort consumer + a 2nd cross-industry JTBD scatter appear. | read.md What Would Change; .claude/rules/engine-dev.md | query-time-grouping-enough, relation-pressure |
| S3 | surprise | Completeness is **method-bounded**: the substitute set was assembled by keyword grep (`sleep`/`recovery`/`melatonin`/`magnesium`/`circadian`); a brand serving the job without those tokens, or a whole solution type the store holds none of (CPAP/mattress/app), would be missed. Honestly flagged as "not found," not "not there" (L004 discipline self-applied). | That the set is complete — it's explicitly partial; only that store-only completeness here is full-text-grep-bounded. | read.md Missing/Stale Coverage, C5 | coverage-caveat, source-rigor |
| CR1 | surprise | (Consumer review) Value lands on builder/Pantry not buyer for the 7th+ time, but with a **new sub-flavor**: here the per-member ingredient layer is genuinely decision-grade and the limit is **purely the cross-member index structure** (no JTBD shelf). Prior CR1s (038/039/041) had both a thin-ingredient problem AND a no-index problem; this run isolates the latter — the farm is good, the catalog lacks the shelf. | That this justifies a JTBD field — the "no new primitive needed" stay is already in G1/W1; only that the builder-not-buyer streak has a sharper isolated-cause variant. | consumer-review.md; read.md Gap Map | query-time-grouping-enough, relation-pressure |
| CR2 | gap | (Consumer review) The assembled substitute set has a **soft center** whose inclusion is itself an unlabeled Judgment: Apple (catalog-grain, run-043 G2), Peloton/Nike (recovery fringe, neither self-brands as sleep). The run flags method-bounded *completeness* (S3) but not that **edge-member inclusion grain** (store-grounded vs reader-inferred) is invisible to a downstream reader. | That including them is wrong — they're plausible substitutes; only that the inclusion claim's grain (Judgment vs State) isn't surfaced. | consumer-review.md; read.md Companies Seen / Evidence Limits | query-time-grouping-enough, source-rigor |
| DR1 | gap | (Developer review) The proposed query-time recipe ("grep description+body for the buyer goal") has a **silent reliability gradient**: reliable for conventional-vocabulary goals (sleep/recovery), silently partial for jargon-fragmented goals or sparse older captures — and it produces a set that *looks* complete with no failure signal. The recipe framing (W1) does not yet name this gradient. | That the recipe is wrong here — it's appropriate for this goal; only that "grep for the goal" hides a vocabulary/vintage-dependent partiality risk. | developer-review.md; read.md C5 / Missing coverage; run-notes W1 | coverage-caveat, query-time-grouping-enough, depth-backfill |
| DR2 | surprise | (Developer review) The telehealth double-burial (S1) is a **structural inversion of L005's corollary**. L005 says "structured absence = coverage signal, not market fact." Here the entrants are **present and correctly tagged** (`Services/Consulting`,`Biotech/Pharma`) — not absent but **misrouted**: a buyer-goal draw returns nothing because correct producer-shaped tags create invisible routing. "Tag-correct and therefore invisible" is a mechanism distinct from missing data (L004) and wrong tags. | That the tags are wrong — they're individually correct; only that correct producer tags can systematically exclude a captured player from a buyer-goal draw. | developer-review.md; read.md Result(4), C4; lessons.md L005 | denominator-reconciliation, schema-edge-entity-type |

## Inputs and scope

- **Slice:** the full 145-profile store, queried by full-text grep on buyer-goal tokens
  (`sleep`, `recovery`, `melatonin`, `magnesium`, `circadian`) plus frontmatter pulls.
- **Members assembled (partial):** devices/recovery — eightsleep, ouraring, whoop, apple
  (Watch, catalog-grain), therabody, hyperice, nike (minor), onepeloton (weak);
  telehealth Rx-sleep — rexmd, rugiet, malemd; supplement/compounding adjacency (fuzzy) —
  anazaohealth, keeps.
- **Exclusions:** waldo-fyi (false positive — "while you sleep" is a brand-monitoring
  metaphor, not a sleep product).
- **Source panels:** none (store-only by contract; no external denominator).

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

None operationally — the whole read was local grep + frontmatter reads. The only
"friction" is conceptual and is the finding itself: there is no structured handle for a
buyer goal, so the set must be hand-assembled from prose (G1).

## Evidence limits

- Member set is **full-text-grep-bounded** and therefore partial (S3); "not found" ≠
  "not there." No external denominator consulted (store-only).
- Substitution membership (which brands are *true* substitutes vs adjacent) is a run
  Judgment, not store State — Apple is catalog-grain, Peloton/Nike sit on the recovery
  edge, telehealth Rx-sleep is a minor line. The boundary is reader-drawn.
- Single buyer goal (n=1); the industry-scatter recurrence (G2) generalizes from prior
  runs, but the buyer-goal-grain framing is first-sighted here.

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
- No disallowed action happened: **pass** (no live browsing, no spend, no store mutation, no primitive/lesson)
- Required citations / receipts present and source-graded: **pass** (C1, C2 receipts)
- No snippet treated as evidence: **pass** (all local store-derived)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no current/external claims; store clocks per profile)
- Absence language says "not found", not "not true": **pass** (S3 / Missing coverage explicit)

## Surprises

The store turned out to be both **over- and under-inclusive on its one shared tag**
(S2) and the telehealth entrants **doubly buried** (S1). The cleanest surprise: with
every member captured well, the JTBD set is *still* unqueryable — the limit is the
producer-shaped axes, not coverage.

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

**Fired:** `relation-pressure` (no horizontal substitute relation, G3), `denominator-
reconciliation` (5th industry≠cohort sighting, G2/S1/S2), `query-time-grouping-enough`
(prose carries the set; no field needed, G1/W1), `depth-backfill` (telehealth sleep
line buried, S1), `coverage-caveat` (method-bounded completeness, S3). No new tag
needed.

"No new primitive needed" is a valid outcome — and is this run's outcome.

## Next-run advice

- The bounded-live sibling **C4** ("best sleep tech 2026" coverage radar at the JTBD
  level) is the natural follow-up — it would test whether whole solution types
  (CPAP / mattress / app) are absent, which store-only cannot see.
- `denominator-reconciliation` (industry ≠ cohort key) is now n=5 across distinct
  cohort shapes including buyer-goal — a strong candidate for the next out-of-band
  learning pass to weigh for a lesson (not a run action).
- Avoid re-running the within-cohort wearable read (043/053 covered it); the value here
  was specifically the cross-industry crossing.
