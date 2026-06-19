# Operator Prompt - Loop 2

Use this prompt to run Consumer + Developer Review in a fresh agent session.

```md
Run Loop 2 for the Market Read Lab.

Working directory:
`/Users/brianbolze/Library/Mobile Documents/com~apple~CloudDocs/Web Research`

Target run:
`experiments/00-market-read-lab/runs/NNN-YYYY-MM-DD-short-slug`

Read:
- `experiments/00-market-read-lab/README.md`
- `experiments/00-market-read-lab/triage.md`
- `experiments/00-market-read-lab/templates/consumer-review.md`
- `experiments/00-market-read-lab/templates/developer-review.md`
- the target run's `scout.md`
- the target run's `read.md`
- the target run's `run-notes.md`
- the target run's receipts

Then:
1. Gate before review:
   - If the `run-notes.md` header does not say `run_status: read-done`, stop. Do not
     edit review files, `triage.md`, or receipts.
   - If `scout.md`, `read.md`, or `run-notes.md` is missing or too incomplete to review,
     update only the `run-notes.md` header to `run_status: needs-human-review` and
     `termination_reason: needs-human-review`, then stop.
2. Fill `consumer-review.md` verdict-first: decide whether the produced read was
   valuable enough for a human or agent to trust, reuse, or act on. Use jobs,
   value diagnostics, and the Strategist / Pantry / First Contact lenses only
   after that judgment.
3. Fill `developer-review.md` around Truffle capability pressure first. Pay special
   attention to where the read crossed from State or Signals into Judgment, then
   apply the Steward, Dev Agent, and Founder lenses.
   - If the run used `bounded-live`, audit whether the source panel stayed inside
     `live_evidence_plan`, every outside source was logged, spend was purposeful,
     and weak evidence stopped as `insufficient-evidence` instead of expanding scope.
4. Submit candidate triage items or adjustments only when the review adds new evidence.
5. Never edit sections titled `Human Notes` in `triage.md`; those are Brian/human-only.
6. Do not implement, spike, or offer to implement system changes.
7. Do not graduate triage items. Graduation is an explicit human decision after review.
8. When both reviews are complete, update only the `run-notes.md` YAML header to
   `run_status: reviewed` and `termination_reason: completed`.

Important:
- Consumer Review tests whether the read provided judgment-ready ingredients:
  useful, sourced, deep/fresh enough, and cheaper to reuse than generic Claude +
  web search.
- Developer Review tests whether the system learned something reusable, including
  whether State / Signals / Judgments stayed clear enough.
- Use prior completed runs as evidence and triage context, not templates. Runs
  `000`-`002` are pre-autonomy historical runs and should not be copied for current
  artifact conventions.
- For current/news/policy/pricing claims, actively test source rigor; do not accept
  snippet-grade evidence as decision-grade just because the run caveated it.
- No-op is acceptable if the review adds no new pressure.
- Prefer concrete evidence from the run over persona performance. Cut weak rows or
  sections rather than filling every table mechanically.
- `reviewed` means the run has been reviewed; it does not graduate any triage item or
  approve a system change.
```
