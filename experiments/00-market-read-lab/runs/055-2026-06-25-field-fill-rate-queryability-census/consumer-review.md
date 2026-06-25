# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable? Yes** — for one consumer in particular: the **Pantry / downstream-system
  builder**. It is the first run to hand that consumer a *dependability map* of the store's
  own frontmatter rather than answering a market question.
- **Why:** every prior schema-fit run (036–054) silently *assumed* the fields it reasoned
  from were populated. This run measures that assumption store-wide and finds it is true for
  the required scalar contract, false for relations, and uneven (concentration-lopsided) for
  the group-by fields. A builder deciding "which field can I filter on" now has the answer.
- **Where Truffle added value:** the four-tier map (read.md Result) is directly actionable —
  Tier 1 = build on it; Tier 2 = read through `entity_type`; Tier 3 = don't partition on it;
  Tier 4 = telehealth-only. Plus the `unverified_fields` 136/136 finding (S4): a universal,
  dependable honesty hook a downstream consumer can always reach for.
- **Where Truffle added little or fell short:** **near-zero value for the end buyer** — this
  is an introspection read, not a market read; a buyer asking about a company gets nothing.
  It belongs to the builder lane, continuing the 038/039/041 CR1 "lands on builder not buyer"
  pattern, but here *by design* (the question is a system-test, not a buyer question).
- **What the consumer can do now:** choose query keys with eyes open — filter on
  `entity_type` / `primary_industry` for coarse cuts, never on `parent`/`owns` for a
  population, and treat `offerings.md`/`signals/` as telehealth-scoped. And: strip inline
  comments before parsing values (R1).
- **What made it safer/better than generic Claude + web search:** generic tooling cannot
  produce this at all — it requires the local corpus. The census is a fact about *this store*,
  unobtainable externally.
- **Biggest limit:** a fill-rate is a coverage fact, not a market fact, and the run says so
  repeatedly — but a careless reader could still quote "13% of companies have a parent" as if
  it were a market structure claim. The framing guards against it; the risk is at relay.
- **Human follow-up needed:** none required. If a builder wants to act on R1, that is a
  docs/recipe call for an out-of-band learning pass, not this run.

## Value diagnostics

| Signal | Evidence / gap |
|---|---|
| **Useful** | Yes — a decision aid ("which field can I build on") with a concrete tiered answer, not a summary. |
| **Judgment-ready** | Yes for a builder; the tiers are cited to counts (C1–C7). The map itself is the run's Judgment, clearly labeled. |
| **Sourced & cited** | Strong — every tier traces to a reproducible local count; no external claims, so no source-grade exposure. |
| **Deep enough** | Census = full corpus (N=136), not examples. Deepest possible denominator for this question. |
| **Fresh enough** | Fill-rates are a snapshot of the corpus as of this run; will drift as the store grows — noted in Next-run advice. |
| **Kept / reusable** | The method is a one-liner to re-run; the read is a reusable baseline. No warm files beyond the run artifacts. |
| **Shortfall mapped** | Yes — relation sparsity (G1), module skew (G2), and the parsing trap (R1) are all named as boundaries, not hidden. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Build on top without re-capturing** | **Yes — directly.** The dependability map is exactly the "which state can a downstream system query" question. | A builder still needs per-field semantics from SCHEMA; this adds the empirical fill layer. |
| **Trust the cache over time** | Partly — `unverified_fields` (S4) and `captured_at` (100%) are the dependable trust hooks the read surfaces. | Freshness *decay* is out of scope (covered by run-052). |
| **Compare a whole field** | Indirectly — explains *why* some cross-field comparisons collapse (Tier-1 concentration, S3). | — |

(Other jobs — cold-start, five-second brief, delegate-to — not served; this is a system-test.)

## Lens check

- **Strategist:** lands quickly and plainly via the tier table; the novel insight (100%-filled
  ≠ good partition key, S3) is genuinely hard to get elsewhere.
- **The Pantry / downstream system:** this is *its* read. It can now pick query keys, gate on
  `entity_type`, and avoid the `parent`/`owns` partition trap — without re-browsing. The one
  thing it must internalize is R1 (strip inline comments) or it will mis-ingest empties.
- **First Contact:** would trust it — the method is transparent and reproducible, and the
  coverage-fact-not-market-fact framing is repeated enough to be credible.

## Raw learning to preserve

New consumer-side sighting logged to `run-notes.md` Observations as **CR1** (the read's value
lands on the Pantry/builder, and the buyer-facing value is nil *by design* — a system-test,
not a market read). Existing S1–S4/G1/G2/R1 already capture the substantive findings.

**No lessons proposed, nothing graduated, no system change implemented.**
