# Run Notes

```yaml
run_status:            # scout-only | read-done | needs-human-review | reviewed
evidence_mode:         # store-only | local-existing | bounded-live | live-external-needs-approval
autonomous_eligible:   # yes | no
termination_reason:    # completed | needs-human-review | blocked-by-approval | insufficient-evidence | failed-loop1-exit-check
learning_tags: []  # short recurrence tags, not approvals
```

## 30-second operator read

- Did the run work?
- What was awkward?
- What should the next agent know?

## What happened

Brief path taken.

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
|  | friction/surprise/wish/gap/risk-miss/brian-correction |  |  |  |  |

## Inputs and scope

Store slices, queries, files, source panels, exclusions.

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

- Status was `scout-only` before Loop 1:
- `Selected Run Contract` was present and consistent with header:
- `autonomous_eligible: yes`:
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`:
- `approval_needed: no`:
- If `bounded-live`, `live_evidence_plan` was present and followed:
- If `bounded-live`, every outside source was logged in `live_evidence_used`:
- If `bounded-live`, stop rules and spend notes were recorded:
- No disallowed action happened:
- Required citations / receipts present and source-graded:
- No snippet treated as evidence:
- Current/news/pricing/policy claims carry capture dates and source grade:
- Absence language says "not found", not "not true":

## Surprises

Anything unexpected after touching the data.
Summarize the surprises here after preserving concrete sightings in the Observations
section.

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

"No new primitive needed" is a valid outcome.

## Next-run advice

What to try, avoid, or re-check.
