# Developer Review

Question: **What system change does this suggest?**
Verdict: **No new State primitive; very likely no new Signals primitive yet either — the
result may resolve to "monitoring is a consumer/project cadence, not engine Signals." Land
the run's two submissions as MRL-007 (category-scoped exogenous-signal anchor, held, one
sighting) + MRL-008 (minimal-monitor panel + source-rigor convention). Hold both behind
recurrence; anti-Doro guardrails attached.**

> Operator correction after review: the no-build verdict still holds, but the source-rigor
> assessment was too generous. Declaring a panel snippet-grade is not enough if the read then
> uses confident regulatory/pricing language. MRL-008 now includes citation-grain requirements.

## Steward

**Caveat discipline is strong, and it adds a genuinely new corpus-health insight:
`synthesis-staleness`.**

- Partly handled, but under-reviewed: the panel is declared snippet-grade, yet the read still
  uses confident regulatory/pricing language. The reusable learning is source rigor: snippets
  find leads; primary URLs and capture dates are what make current-event claims usable. The
  run also introduces a caveat sibling —
  **channel-completeness vs company-completeness** — that's reusable as-is (a cohort read
  assembled only from DTC pages is structurally incomplete on manufacturer-direct and
  regulatory facts no matter how many brands it captures).
- **The load-bearing finding:** a read inherits the half-life of its most volatile claim, and
  that claim can decay **while the underlying captures stay fresh**. The store's GLP-1 captures
  (May 30–Jun 18 2026) are fresh; Run 000's *read* is stale anyway — because the decaying facts
  (legality, manufacturer price) aren't captured per-company at all. This is **not** a stale-
  capture problem the Signals layer catches; it's a missing-grain problem, so no per-domain
  freshness signal could have flagged it.
- **Park for later (one sighting):** whether fast-moving fields (price, legal status) should
  carry a volatility / half-life marker so a read can cite a governing clock. May belong to the
  consumer, not the store — do not act now.

## Founder

**Anti-Doro check: the temptation is loud here — resist all of it on one sighting.**

- The pull is toward a `store/_market/<topic>/…` signals path, a regulatory/manufacturer
  "entity" with no domain, or a standing monitor. Each is premature machinery off a single
  run. The hardest part — **FDA has no company home at all** — is exactly where a non-company
  entity type would get invented; that's the red flag the anti-Doro line warns about.
- The run itself surfaces the honest fork — **engine Signals vs consumer/project cadence** —
  and the right call now is **no-build**: a documented panel convention captures the value
  without infrastructure. If it recurs, the lightest landing is a market/topic-scoped path or
  a project-side monitor — explicitly **not** a graph, entity-resolution, or served monitor.
- **Recurrence gate (mirrors Run 001's discipline):** one more run surfacing a homeless
  category-level signal = recurrence; *then* design where it lives. One sighting → submit, not
  graduate.

## Dev Agent

**Cheapest asset is a recipe/template, not a tool — and this is the second improvised lab
artifact, not the first.**

- The run hand-built a 3-source external panel + a staleness-delta table (prior assumption →
  current external reality → verdict). Run 000 improvised a denominator recipe; this is a
  **different artifact, same meta-pattern** of in-run improvisation. The 80/20 is to document
  the panel+delta shape as a reusable Loop-1 recipe for "stress a stored read against fresh
  external events."
- **No script justified:** the panel is 4 Firecrawl searches and a hand-diff; automation buys
  nothing at one sighting and would be the standing infrastructure the engine refuses. Recipe,
  not script — same posture as prior runs.

## Triage Submissions

- **New — MRL-007 (P3):** category-scoped / non-company exogenous-signal anchor — **held, one
  sighting**. Category-level events (FDA legality, manufacturer reference pricing) govern the
  whole cohort but have no per-domain home; FDA has none at all. Do not build; if it recurs,
  decide where such signals live, anti-Doro guardrails attached. The fork may resolve to
  "monitoring is a consumer/project job."
- **New — MRL-008 (Low):** minimal-monitor source-panel + source-rigor convention —
  documented template, not a built monitor or script. Also the **2nd sighting** of a lab read
  improvising an artifact (after Run 000's denominator recipe).
- **Evidence, no new item:** directionally supports Run 000's prediction that the branded tier
  was "the live edge… where a freshness/Signal layer would earn its keep." Attach to MRL-007 /
  MRL-008 after primary-source confirmation.
- **No-op:** no new State primitive; possibly no new Signals primitive either — the
  monitoring-is-a-consumer-job fork stays open for human review.
