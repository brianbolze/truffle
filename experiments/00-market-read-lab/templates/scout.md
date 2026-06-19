# Scout

## Prior Context Read

- `triage.md`:
- `scout-context.md`:
- Last 3 `run-notes.md` files:
- Current run artifacts, if resuming:

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
|  | market/system-test/mixed | yes/no | store-only/local-existing/live-external-needs-approval |  |  |  |

## Selected Question(s)

1.

These may be Scout recommendations until Brian or the operator confirms one.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question:
run_type:              # market | system-test | mixed
autonomous_eligible:   # yes | no
evidence_mode:         # store-only | local-existing | live-external-needs-approval
expected_denominator:
likely_source_panel:
allowed_sources: []
disallowed_actions: []
approval_needed:       # yes | no
why_autonomous_safe:
loop1_failure_mode:
```

## Selection Notes

Consider decision leverage, evidence readiness, freshness pressure, reuse pressure, surprise potential, system-test value, and artifact pressure.

Treat prior run patterns as hypotheses, not defaults. Prefer testing whether the same pressure recurs over copying a previous run's exact method.

Autonomous runs should prefer `autonomous_eligible: yes` and `evidence_mode: store-only`.
Questions that need live external evidence are allowed as candidates, but should not be selected for unattended Loop 1 without explicit approval.
