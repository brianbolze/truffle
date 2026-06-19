# Scout

## Prior Context Read

- `triage.md`:
- `scout-context.md`:
- Last 3 `run-notes.md` files:
- Current run artifacts, if resuming:

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
|  | market/system-test/mixed | yes/no | store-only/local-existing/bounded-live/live-external-needs-approval |  |  |  |

## Selected Question(s)

1.

These may be Scout recommendations until Brian or the operator confirms one.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question:
selected_slug:          # 3-5 word kebab-case folder slug, e.g. telehealth-category-crowdedness
run_type:              # market | system-test | mixed
autonomous_eligible:   # yes | no
evidence_mode:         # store-only | local-existing | bounded-live | live-external-needs-approval
expected_denominator:
likely_source_panel:
allowed_sources: []
disallowed_actions: []
live_evidence_plan: null  # required only for bounded-live
approval_needed:       # yes | no
why_autonomous_safe:
loop1_failure_mode:
```

## Selection Notes

Consider decision leverage, evidence readiness, freshness pressure, reuse pressure, surprise potential, system-test value, and artifact pressure.

Treat prior run patterns as hypotheses, not defaults. Prefer testing whether the same pressure recurs over copying a previous run's exact method.

Autonomous runs should prefer `autonomous_eligible: yes` and `evidence_mode: store-only`.
Use `bounded-live` only when the question genuinely needs a small outside source panel and the contract includes a filled `live_evidence_plan`.
Use `live-external-needs-approval` when the source need is broader, unclear, or missing a bounded plan.
