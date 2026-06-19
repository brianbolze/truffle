# Operator Prompt - Scout Only

Use this prompt to generate candidate Market Read Lab questions in a fresh agent session.

```md
Run Scout-only for the Market Read Lab.

Working directory:
`/Users/brianbolze/Library/Mobile Documents/com~apple~CloudDocs/Web Research`

Target run:
`experiments/00-market-read-lab/runs/NNN-YYYY-MM-DD-short-slug`

Read:
- `experiments/00-market-read-lab/README.md`
- `experiments/00-market-read-lab/scout-context.md`
- `experiments/00-market-read-lab/templates/run-notes.md`
- `experiments/00-market-read-lab/triage.md`
- the last 3 completed `run-notes.md` files, if any
- the target run's existing `scout.md`, if present
- the target run's existing `run-notes.md`, if present
- the target run's existing receipts, if any

Then:
1. Generate 5-10 candidate market or system-test questions in the target run's
   `scout.md`. Start with straightforward operator question types, then annotate
   what each candidate teaches the system.
2. For each candidate, name why it is worth a run, what trustworthy evidence would
   require, the failure mode to watch, `autonomous_eligible: yes/no`, and
   `evidence_mode: store-only | local-existing | bounded-live | live-external-needs-approval`.
3. Recommend 1-2 selected questions, but do not answer them. Fill the
   `Selected Run Contract` for the best selected question, including a concise
   `selected_slug` for the final run folder. Treat that block as the canonical
   handoff to Loop 1.
   - Use `bounded-live` only when the selected question genuinely needs a small
     outside source panel and the contract includes a filled `live_evidence_plan`.
   - Use `live-external-needs-approval` when the source need is broader, unclear,
     or missing a bounded plan.
4. Update only the YAML header at the top of the target run's `run-notes.md`:
   - Mirror `autonomous_eligible` and `evidence_mode` from the `Selected Run Contract`.
   - If the selected question is unattended-safe, set `run_status: scout-only` and
     `termination_reason: completed`.
   - `bounded-live` may be unattended-safe only when `approval_needed: no` and
     `live_evidence_plan` is complete.
   - If the selected question needs live external evidence outside a bounded plan,
     approval, or human reframing, set `run_status: needs-human-review`, use
     `termination_reason: blocked-by-approval` or `needs-human-review`.
   - Leave `pressure_lenses_fired: []` unchanged unless Scout clearly sees a
     pressure lens from prior runs.
5. Do not write `read.md`, review files, or `triage.md`. Do not fill the body of
   `run-notes.md` below the YAML header.
6. Do not implement, spike, or offer to implement system changes.

Important:
- Use prior runs and triage as evidence inputs, not templates. Current conventions live
  in `templates/` and the operator prompts.
- Runs `000`-`003` are historical or incomplete pre-contract runs; do not copy their
  headers, stage behavior, source rigor, or artifact shape.
- There is no shared question queue yet. Candidate questions live in run `scout.md`
  files; `triage.md` is for system pressure, not a question backlog.
- Follow `scout-context.md` for current question-selection policy, including question
  archetypes, selection bias, and when to choose each evidence mode.
- `selected_slug` should be short kebab-case, usually 3-5 meaningful words, based on
  the selected question rather than the temporary scaffold name.
- `approval_needed: yes` means the run must stop at Scout until Brian/operator approval.
- A bounded-live plan must name the evidence goal, allowed/preferred source families,
  disallowed families, stop rules, and `budget_class: light`.
- If `run_status: scout-only`, end by telling the operator to start Loop 1 in a
  fresh session. If `run_status: needs-human-review`, end by asking for approval or
  question refinement instead.
```
