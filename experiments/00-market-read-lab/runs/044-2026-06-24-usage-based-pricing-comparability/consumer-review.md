# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable? Yes.** A clean, honest answer to a real buyer question.
- **Why:** The read answers "can I compare metered infra costs from the store?" with the correct and
  *complete* result — verbatim pricing is present and high-quality for 5/6, but the cohort is structurally
  not cost-comparable because each vendor meters its own consumption primitive. Unit-incommensurability,
  not missing data, is the ceiling. A buyer walks away knowing exactly what to take (shape compares,
  magnitude doesn't, bring your own workload) and exactly what the store can and cannot hand them.
- **Where Truffle added value:** A dated, cited, per-brand rate card assembled in one pass; a clear
  structural ceiling (no cross-vendor $/unit ranking is possible); the correct negative (absent token ≠
  unpublished price). Provenance + capture clocks are the differentiator a generic answer lacks.
- **Where Truffle added little or fell short:** The price-visibility token — the store's one cross-cohort
  shorthand for "can I get a price?" — functions on only 1/6 of this cohort, so it adds no comparison
  value here. AWS is captured at philosophy-grain (no rate), so it can't be priced even at profile grain.
- **What the consumer can do now:** Use the verbatim rate table (C1) as a dated per-vendor starting point;
  use the pricing *shape* (metered + free tier + committed-use discount + self-serve→enterprise) as the
  cross-vendor frame; model their own workload for any $/unit ranking (the store can't supply that, and no
  store could); check capture clocks before trusting rates in a negotiation (4/6 are 2026-05-31); **not**
  use the token as a filter across this cohort.
- **What made it safer / better than generic Claude + web search:** Dated, cited evidence that traces to a
  specific `/pricing` capture rather than a memory snippet; the explicit absence-language discipline
  (absent token ≠ published — a precision a generic model would not maintain); and the cohort-key behavior
  finding (S2/G2), which requires awareness of the store's own taxonomy and prior runs. The structural
  ceiling insight itself any reasoning model could reach; the *grounding* is what makes it citable.
- **Biggest limit:** Token coverage (G1) — 1/6 tokenized, so the store's pricing-transparency shorthand is
  inert on this cohort. AWS philosophy-grain is the secondary limit.
- **Human follow-up needed:** Buyer supplies their own workload numbers to turn the rate cards into a bill.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer, decision aid, or next step. | Strong — structural ceiling + dated rate table is directly actionable. |
| **Judgment-ready** | Fresh, rare, cited ingredients. | Strong for 5/6 (verbatim rates + clocks); AWS philosophy-grain only. |
| **Sourced & cited** | Claims trace to dated captures. | Strong — every rate cites `profile:line` + `captured_at`; verifier confirmed counts. |
| **Deep enough** | Covers the intended set. | Yes — all 6 core members + 5 foils. |
| **Fresh enough** | Capture dates visible where they matter. | Yes — 4/6 dated 2026-05-31 flagged as volatile-snapshot. |
| **Kept / reusable** | Warm files for the next ask. | Yes — receipt C1 holds the cohort draw + token counts for reuse. |
| **Shortfall mapped** | Names where Truffle couldn't support. | Yes — token coverage + AWS grain + the off-store workload model all named. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Compare a whole field** | Partly — compares *shape* cleanly; *magnitude* is structurally un-comparable. | The un-comparability is the finding, not a fixable gap. |
| **Five-second brief input** | Yes — verbatim rates + the "meters its own primitive" one-liner are brief-ready. | — |
| **Build on top without re-capturing** | Secondarily — G1 token gap + S2 cohort-key contrast are reusable builder signals. | A tokenized post-2.3 metered cohort would test G1 further. |

## Lens check

- **Strategist:** Lands plainly — "you can't rank these on price; here's why" is a fast, defensible take.
- **The Pantry / downstream system:** Per-brand device+sub prices are consumable as ingredients; the
  *comparison* (year-cost ranking) is the run's own Judgment, not a queryable field — so a downstream
  system gets the rates, not a "cheapest" answer. Correctly labeled.
- **First Contact:** Yes — provenance + capture clocks + honest absence-language make the run trustworthy.

## Value frontier

**Buyer-primary** — and that matters. Runs 038/039/041 CR1 landed on the *builder* (the reads surfaced
schema/query gaps a buyer couldn't use). Run-043 landed on the buyer (a usable TCO). This run follows
run-043: the store delivers an artifact a developer/CTO can act on directly. The G1 token gap and the S2
cohort-key contrast are builder-lane byproduct, not the reason the run has value. Second consecutive
buyer-frontier run — the "lands on builder not buyer" streak is now clearly broken on *value-read* runs.

## Raw learning to preserve

Consumer-side sightings appended to `run-notes.md` Observations (CR1 below) and lifted to
`learning/observations.md` by this Loop 2 pass.

**Do not propose lessons, graduate anything, or implement system changes.**
