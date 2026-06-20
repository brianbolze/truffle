# Consumer Review

Question: **Was the read itself valuable enough for a human or agent to trust, reuse, or act on?**

## Verdict

- **Valuable? Yes.** This is a useful read, not an elegant refusal. The "you can't rank these
  prices" conclusion is load-bearing *because it ships with the fix*: a 4-axis normalization
  rubric plus a per-brand receipt that pre-sorts all 19 brands into the incommensurable kinds.
  The consumer leaves with the structure to build a defensible compare, not with "it's
  complicated."
- **Why:** It proves the failure with a worked example (Eden's `$99` headline → `~$198`
  effective once the mandatory `$99` membership is added, which *inverts* the naive ascending
  sort) and then explicitly fences that derived number as **[J], not captured State** —
  demonstrating the trap instead of falling into it. That is exactly the failure mode the scout
  contract flagged.
- **What the consumer can do now:** (1) build a decision-grade compare by holding the four axes
  constant — the receipt already tags every brand; (2) trust `visibility: published/partial` as
  the comparability gate; (3) avoid the named landmines (~6/19 exclude a mandatory fee, ~8/19
  are promo, 2 self-conflict across surfaces); (4) use the "two pricing architectures wearing
  the same `$X/mo` costume" pattern directly for positioning.
- **What made it safer / better than generic Claude + web search:** Generic Claude would scrape
  live pages and confidently emit a "cheapest" table — manufacturing the exact false confidence
  this run dismantles. The value is the meta-audit of Truffle's *own* captured State: per-surface
  fidelity (it holds both of directmeds' conflicting numbers rather than papering over them),
  fully cited to dated captures, zero spend. The finding is structural (units differ *within* the
  cohort), so it is robust to denominator size in a way a fresh snapshot is not.
- **Biggest limit:** Entry-tier only and freshness-bound. One leading price per brand; dose
  ladders not exploded (intake-gated for ~half the cohort); ~8 prices are point-in-time promos
  across a 2026-06-03→18 spread. The rubric is sound but the *inputs* to an actual compare are
  thin and decaying — the read enables the compare more than it delivers one.
- **Human follow-up needed:** The design recommendation (*don't persist a derived effective-
  monthly field; lean on the flag + query-time rubric*) is a well-argued **Judgment**, not a
  finding. The read correctly keeps it advisory (scout fenced "create durable primitives" as
  disallowed). A human signoff is the right gate before it hardens into store policy.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Decision aid, not a summary. | Strong — names the landmine *and* the rubric to avoid it. |
| **Judgment-ready** | Fresh, rare, cited ingredients. | Strong — derived figures fenced as [J]; verbatim rows cited per-brand. |
| **Sourced & cited** | Traceable to dated captures. | Strong — one receipt, per-brand `captured_at`, store-graded primary. |
| **Deep enough** | Covers the cohort, not examples. | Yes for membership — all 19; **gap** on per-dose depth (entry-tier only). |
| **Fresh enough** | Stale/changed signals visible. | Yes — promo + capture-spread caveats explicit. |
| **Kept / reusable** | Warm files for the next ask. | Yes — the comparability panel is a reusable, pre-tagged asset. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Compare a whole field** | Served — inverted into "why the naive compare lies + how to do it right." Primary job. | A real per-dose matrix would need fresh capture. |
| **Make AI safe to delegate to** | Strongly served — this is the guardrail that stops a downstream agent inventing a ranking. | — |
| **Five-second brief input** | Served — "`$X/mo` costume" + two-architectures pattern are strategist-ready. | — |
| **Build on top without re-capturing** | Served — the receipt panel is queryable without re-browsing. | — |

## Lens check

- **Strategist:** Lands fast and is non-obvious — "the headline number can't referee a
  pricing-optics arms race." Glad it exists if positioning against this cohort.
- **The Pantry / downstream system:** High-quality ingredients — stable verbatim rows, dated,
  derived figures labeled [J], freshness visible. Directly reusable.
- **First Contact:** Trustworthy. Uncertainty surfaced (conflicts unresolved, floors gated,
  promo decay); nothing overclaimed.

## Evidence-verification note

An adversarial evidence pass spot-checked 5 brands' prices, the C3 fee count, the C5 field
reading, and the derived figures against the actual `offerings.md` files. All load-bearing
claims (C1–C4, the 6-brand fee count, derived-figure labeling, store-only provenance) survived
falsification. Two cosmetic imprecisions it flagged were corrected in `read.md`/the receipt
this cycle: the C5 headline now states `partial` is a comparability *gate* (it also spans dose-
floors/conflicts, not only "cost-on-top"), and the directmeds conflict pair + a tryshed brand-
level membership caveat were fixed in the receipt.

## Triage submissions

No new graduation candidate from the consumer lens. The read reinforces existing
`compare-a-whole-field` / `query-time-grouping-enough` value rather than adding new consumer-side
evidence. No-op. **Did not graduate or implement any system change.**
