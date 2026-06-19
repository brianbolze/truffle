# Developer Review

Question: **What system change does this suggest?**
Verdict: **No new State primitive. Reframe one triage item, hold one helper behind a 2nd run, and
queue one corpus-health backfill the run submitted but never landed in the queue.**

## Steward

**Provenance and caveats are strong; the corpus-health pressure is real and concrete.**

- Well-handled: grain stated (per-SKU vs brand-weighted, both in the receipt), governing capture
  clocks named, union reported as a **floor** not a census, verbatim-string-only limit flagged. This
  is the caveat discipline a market read needs — reusable as-is.
- **Corpus-health gap (queue it):** altRx (GLP-1-led, no `telehealth.md`/`offerings.md`) and Marque
  (no `telehealth.md`) are in-cohort but **unqueryable on the cohort cuts**. The run submitted this as
  a backfill candidate, but it never made it into `triage.md`. → submitting as **MRL-003**.
- **Token-grain observation (logged, not queued):** the `Visibility` token conflates *"hides its own
  price"* with *"doesn't set the branded-drug price"* (retail / insurance-set). It's a genuine
  semantic limit of a single field, but it's a **single sighting** and only bites if branded-tier
  tracking becomes a tracked question — at which point it's a **Signal/freshness** job, not a State
  field. Holding as a watch-item, consistent with the run's own "one sighting → watch before acting"
  discipline.

## Founder

**Anti-Doro check on the query-helper (MRL-002): hold the code; submit the convention.**

- The run is right that there's no new *State* object here — visibility, molecule grouping, and cohort
  scoping are all query-time reads over layers the store already has. "No new primitive" holds.
- But the helper itself is **one run of evidence**. The 7-minute cost was partly the agent
  re-deriving steps and partly model latency; the operator-observation asserts "not just model
  slowness," but that's an assertion, not a measured second data point. Building `cohort_members()` /
  `reconcile()` off a single run is exactly the premature-machinery move the anti-Doro line warns
  against.
- **The cheap 80/20 is a written convention, not a tool:** submit the standard denominator recipe
  (membership = `telehealth.anchor_category` ∪ roster-molecule rows, gated by `value_chain_role`;
  *not* a raw body grep — the bluechew negation and One Medical false-positive prove why) plus the
  standard "not-captured ≠ not-offered / union is a floor" caveat language. That would capture most
  of the re-derivation cost with zero living infrastructure, if acknowledged. → adjustment to MRL-002.
- **MRL-001 was mis-framed by its own source run.** At review time, it still carried the original
  *"source-panel convention"* / P1 framing, but Run 0's headline finding was the **inversion**: the
  internal store **out-completed** the external Notion source, and the correct move was a query-time
  **union + dedupe of two curated internal lists** (`store.py resolve`), *not* capturing an external
  panel. → adjustment to MRL-001: reframe to denominator **reconciliation**, demote external panel to
  a conditional fallback ("only when *both* internal lists are thin"), and lower the priority if Brian
  agrees.

## Dev Agent

**Cheapest automation is a doc + recipe, not a script.**

- The reusable asset with the best cost/value here is a **QUERYING recipe entry**: the membership
  formula above + the symmetric-diff-as-radar pattern + caveat language. It's a template/convention,
  the class of thing this lens should reach for first.
- A committed helper (`cohort_members(anchor=…)`, `reconcile(name_list)`) is plausibly worth it later,
  but only after a **second market read** confirms the same four steps recur and the latency is
  structural. Until then it's speculative tooling. (Captured in the MRL-002 adjustment.)
- Rendering/linting: nothing new needed — the run wrote clean receipts by hand and the artifacts
  follow the templates.

## Triage Submissions

- **Adjustment — MRL-001:** reframe *source-panel convention* → *denominator reconciliation*; external
  panel is a conditional fallback, not the default; include the symmetric-diff write-back set (per the
  consumer review) as a named Pantry-facing output; demote from P1 if Brian agrees. New evidence:
  review independently confirms the run's inversion that the triage entry had not absorbed.
- **Adjustment — MRL-002:** split into (a) **submit the denominator recipe convention** — cheap, no
  code; (b) **hold the committed helper** until a 2nd run proves the latency is structural, not
  model-slowness. New evidence: Founder/Dev-Agent anti-Doro pressure.
- **New — MRL-003:** depth-backfill the in-cohort module gaps (`altrx-com`, `marquelongevitylab-com`)
  so they're queryable on the cohort cuts. Run-submitted, never queued; Steward confirms as live
  corpus-health pressure.
- **No-op / watch (not queued):** branded-drug `Visibility` ambiguity — single sighting, Signal-layer
  if it recurs. **No new State primitive** — the pricing-visibility capability is query-time-answerable
  from an existing field; confirmed.
