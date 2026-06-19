# Run Notes

```yaml
run_status:            # scout-only | read-done | needs-human-review | reviewed
evidence_mode:         # store-only | local-existing | live-external-needs-approval
autonomous_eligible:   # yes | no
termination_reason:    # completed | needs-human-review | blocked-by-approval | failed-loop1-exit-check
pressure_lenses_fired: []  # short recurrence tags, not approvals
```

## 30-second operator read

- Did the run work?
- What was awkward?
- What should the next agent know?

## What happened

Brief path taken.

## Inputs and scope

Store slices, queries, files, source panels, exclusions.

## Friction log

Repeated manual steps, took a long time, confusing paths, missing helpers, schema mismatches.

## Evidence limits

Coverage gaps, stale captures, weak source grain, risky inference.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1:
- `Selected Run Contract` was present and consistent with header:
- `autonomous_eligible: yes`:
- `evidence_mode` was `store-only` or `local-existing`:
- `approval_needed: no`:
- No disallowed action happened:
- Required citations / receipts present and source-graded:
- No snippet treated as evidence:
- Current/news/pricing/policy claims carry capture dates and source grade:
- Absence language says "not found", not "not true":

## Surprises

Anything unexpected after touching the data.

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
|  |  | no-op / watch for recurrence / submit triage candidate |

## Triage submissions

Concrete proposed queue items, with priority/status suggestions.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

What to try, avoid, or re-check.
