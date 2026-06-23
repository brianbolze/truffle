# consumption-mechanics — do the documented consumption recipes work for a cold agent?

**Hypothesis:** the documented consumption recipes ([`QUERYING.md`](../../QUERYING.md)) work for a
cold agent without hand-holding — a competent reader pointed only at QUERYING.md can answer real
consumption questions store-first, correctly, in few steps.

Throwaway probe; FINDINGS feed doc fixes + backlog, nothing here is reusable code.

## Method

A live probe (2026-06-09, store at ~105 folders / 90 profiles): an agent with **no prior session
context** reads QUERYING.md once, then answers 8 consumption questions spanning every recipe class —
point read (1), cohort cut (2), cross-brand pricing to the normalization ceiling (3), relations (4),
a negative with the before-trusting-a-negative rules (5), corpus-wide non-telehealth filter (6),
store health/staleness visibility (7), alias resolution (8). Plus one side-check: is
`scripts/_out/store.db` stale relative to the markdown, and would anything have said so?

Per question we log: tool-call count, whether the recipe worked **as written**, traps hit
(wrong/stale doc claims, missing affordances, near-miss footguns), and the single affordance that
would have made it one step.

Rules: python3 + PyYAML + `rg` + `scripts/store.py` only, per the recipes. No web, no Firecrawl.
Nothing in the repo modified except this experiment folder.

## Verdict (one line)

**Hypothesis substantially holds** — all 8 questions answered correctly from the store, every
recipe worked as written — but the doc's own *numbers* are stale (cohort size, relation counts),
store *health* is invisible (15 stub folders no recipe can see), and `store.db` was stale with
nothing to say so. Details: [FINDINGS.md](FINDINGS.md).
