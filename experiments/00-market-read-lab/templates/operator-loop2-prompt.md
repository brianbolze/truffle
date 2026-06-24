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
- `experiments/00-market-read-lab/learning/observations.md`
- `experiments/00-market-read-lab/learning/lessons.md`
- `experiments/00-market-read-lab/templates/consumer-review.md`
- `experiments/00-market-read-lab/templates/developer-review.md`
- the target run's `scout.md`
- the target run's `read.md`
- the target run's `run-notes.md`
- the target run's receipts

Then:
1. Gate before review:
   - If the `run-notes.md` header does not say `run_status: read-done`, stop. Do not
     edit review files, any `learning/` file, or receipts.
   - If `scout.md`, `read.md`, or `run-notes.md` is missing or too incomplete to review,
     update only the `run-notes.md` header to `run_status: needs-human-review` and
     `termination_reason: needs-human-review`, then stop.
2. Create `consumer-review.md` from `templates/consumer-review.md` if it does not
   exist, then fill it verdict-first: decide where Truffle created reader value and
   where it added little or fell short. Use jobs, value diagnostics, and the
   Strategist / Pantry / First Contact lenses only after that judgment.
3. Create `developer-review.md` from `templates/developer-review.md` if it does not
   exist, then fill it around Truffle capability pressure first. Record gaps and
   strengths as observations before turning anything into a proposed response. Pay
   special attention to where the read crossed from State or Signals into Judgment,
   then apply the Steward, Dev Agent, and Founder lenses.
   - If the run used `bounded-live`, audit whether the source panel stayed inside
     `live_evidence_plan`, every outside source was logged, spend was purposeful,
     and weak evidence stopped as `insufficient-evidence` instead of expanding scope.
4. Append the run's preserved raw learning, plus any review-generated raw learning, to
   `experiments/00-market-read-lab/learning/observations.md`. Preserve singletons,
   wishes, frictions, surprises, and gaps even when they do not recur yet. One row per
   sighting; do not merge rows. Before setting `run_status: reviewed`, verify the
   observation stream has rows for this run; if there truly is no new raw learning, add
   a "no new raw learning" row with the run pointer.
5. Do not propose or graduate lessons. Consolidating observations into lessons is an
   out-of-band learning pass, never a run stage — leave `learning/lessons.md`,
   `learning/brian.md`, and `learning/passes/` untouched.
6. Do not implement, spike, or offer to implement system changes.
7. When both reviews are complete, update the `run-notes.md` YAML header to
   `run_status: reviewed` and `termination_reason: completed`.

Important:
- Consumer Review tests whether the read provided judgment-ready ingredients and
  where the value frontier is: useful, sourced, deep/fresh enough, reusable, or
  meaningfully short.
- Developer Review tests what the system learned or failed to support, including
  whether State / Signals / Judgments stayed clear enough.
- Use prior completed runs as evidence and learning context, not templates. Runs
  `000`-`003` are historical or incomplete pre-contract runs and should not be copied
  for current artifact conventions.
- For current/news/policy/pricing claims, actively test source rigor; do not accept
  snippet-grade evidence as decision-grade just because the run caveated it.
- No-op is acceptable if the review adds no new pressure.
- No-op is acceptable for lessons, not for the cross-run observation stream.
- Prefer concrete evidence from the run over persona performance. Cut weak rows or
  sections rather than filling every table mechanically.
- `reviewed` means the run has been reviewed; it does not propose or graduate any
  lesson or approve a system change.
```
