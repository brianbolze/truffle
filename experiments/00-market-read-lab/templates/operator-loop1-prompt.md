# Operator Prompt - Loop 1

Use this prompt to run the Read stage in a fresh agent session.

```md
Run Loop 1 for the Market Read Lab.

Working directory:
`/Users/brianbolze/Library/Mobile Documents/com~apple~CloudDocs/Web Research`

Target run:
`experiments/00-market-read-lab/runs/NNN-YYYY-MM-DD-short-slug`

Read:
- `experiments/00-market-read-lab/README.md`
- `experiments/00-market-read-lab/scout-context.md`
- `experiments/00-market-read-lab/templates/read.md`
- `experiments/00-market-read-lab/templates/run-notes.md`
- `experiments/00-market-read-lab/templates/receipt.md`
- `experiments/00-market-read-lab/discovery-ledger.md`
- `experiments/00-market-read-lab/triage.md`
- the last 3 completed `run-notes.md` files, if any
- the target run's `scout.md`
- the target run's `run-notes.md`
- the target run's existing receipts, especially any denominator seed

Then:
1. Gate before research:
   - If the `run-notes.md` header does not say `run_status: scout-only`, stop. Do not
     edit `read.md`, receipts, reviews, or `triage.md`.
   - If `scout.md` lacks a filled `Selected Run Contract`, update only the
     `run-notes.md` header to `run_status: needs-human-review` and
     `termination_reason: failed-loop1-exit-check`, then stop.
   - A filled contract has non-empty `selected_question`, `question_mode`,
     `builder_lens`, `autonomous_eligible`, `evidence_mode`, `reach_reason`,
     `approval_needed`, `allowed_sources`, `disallowed_actions`, and
     `loop1_failure_mode`. Empty
     `allowed_sources: []` is not enough for Loop 1.
   - If `evidence_mode: bounded-live`, it must also have a filled `live_evidence_plan`
     with `budget_class: light`, ceilings, an evidence goal, allowed source families,
     disallowed source families, fail-closed conditions, and stop rules.
   - Treat the `Selected Run Contract` as canonical. If it conflicts with the candidate
     table, trust the contract.
2. Check the contract before research:
   - Continue only when `autonomous_eligible: yes`, `approval_needed: no`, and
     `evidence_mode` is `store-only`, `local-existing`, or `bounded-live`.
   - Use only `allowed_sources`.
   - Do not perform any `disallowed_actions`.
   - For `bounded-live`, use free/local/cached sources first; use outside sources only
     from the approved source families; spend capture credit only when it is likely to
     verify, date, or falsify a load-bearing claim.
   - For `bounded-live`, stop with `termination_reason: insufficient-evidence` rather
     than broadening into a crawl when the plan is not enough.
   - For `bounded-live`, stop before exceeding any selected ceiling. The default light
     ceiling is 2 source families, 6 outside sources read/captured, and 20 paid capture
     credits unless Scout set a lower ceiling.
   - If the run needs live browsing outside a bounded plan, paid capture outside a
     bounded plan, broad external research, write-back, or reframing, update the header
     to `run_status: needs-human-review` and `termination_reason: blocked-by-approval`,
     then stop.
3. Create the target run's `read.md` from `templates/read.md` if it does not exist,
   then answer the selected question there. Keep State (captured facts), Signals
   (dated changes or indicators), and Judgments (market interpretation)
   distinguishable; label judgments and tie them back to the state/signals they rely on.
   - Fill `Gap Map` even when the direct answer is strong. For `gap-probe` runs, a
     clean gap map can be the main result.
4. Treat any denominator or membership list as partial unless proven otherwise.
5. Preserve raw learning in `run-notes.md` `Discovery ledger` before compressing
   anything into pressure tags or triage. Include observations, wishes, frictions,
   surprises, source ideas, singletons, and mapped gaps with evidence pointers.
6. Capture receipts for non-obvious inputs, derived lists, or operator observations.
   Use `templates/receipt.md` for new receipts. At minimum, each new receipt should
   record URL or local path, capture date or store clock, source type, source grade,
   source family, spend note, snippet-only status, and claim IDs supported.
   For `bounded-live`, also fill `run-notes.md` `live_evidence_used` for every
   outside source used.
7. For current/news/policy/pricing claims, search snippets are direction-finding only.
   Receipts must record exact URLs, capture dates, source type, and whether each claim is
   primary or secondary before the read uses confident language.
8. Fill the target run's `run-notes.md`, including `pressure_lenses_fired` and the
   `Loop 1 exit check` section.
9. Before finishing, run the mandatory exit check:
   - `run_status` was `scout-only` before Loop 1.
   - `Selected Run Contract` was present and consistent with the run header.
   - `autonomous_eligible: yes`.
   - `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`.
   - `approval_needed: no`.
   - If `bounded-live`, `live_evidence_plan` was present and followed.
   - If `bounded-live`, every outside source was logged in `live_evidence_used`.
   - If `bounded-live`, stop rules and spend notes were recorded.
   - No disallowed action happened.
   - Required citations / receipts are present and source-graded.
   - No snippet was treated as evidence.
   - Current/news/pricing/policy claims carry capture dates and source grade.
   - Absence language says "not found", not "not true."
10. Set final header:
   - If every exit-check item passes, set `run_status: read-done` and
     `termination_reason: completed`.
   - If any item fails, set `run_status: needs-human-review` and
     `termination_reason: failed-loop1-exit-check`. Do not tell the operator to start
     Loop 2.
11. Do not run Consumer Review or Developer Review yet.
12. Do not implement, spike, or offer to implement system changes. Do not write
    `triage.md` in Loop 1 unless the operator explicitly asked for it; keep raw
    learning in the run Discovery ledger for Loop 2 to append to `discovery-ledger.md`.
13. If `run_status: read-done`, end by telling the operator to start Loop 2 in a fresh
    session. Do not offer to run Loop 2 yourself.

Important:
- Keep artifacts outside `store/`.
- Treat this as a market read plus system-learning run.
- Treat prior run recipes as evidence, not templates; only repeated pressure earns
  a convention or helper candidate. Runs `000`-`003` are historical or incomplete
  pre-contract runs and should not be copied for artifact shape, headers, stage
  behavior, or source rigor.
- If `scout.md` does not contain a selected question, fail closed to
  `needs-human-review`; do not choose a question inside Loop 1.
- If `bounded-live` is used without a plan, source grades, source-use log, receipts,
  ceilings, or stop-rule notes, fail closed to `needs-human-review`.
- If "no new primitive needed" is the honest result, say so.
- Use `pressure_lenses_fired` for short `kebab-case` recurrence tags: denominator,
  source, capture, freshness, tooling, schema, or coverage pressure. These tags are
  not approvals. Use the tag guide in `run-notes.md`, then fill the Fired tag table;
  if no existing tag fits, coin one there and explain it.
```
