# Findings — query affordance (rung 2)

> **Verdict: rung 2 works. The bet holds — a thin affordance beats grep-from-scratch, and the SQLite index (rung 3) stays parked.** The binding constraint is *capture-structure consistency*, not storage. That's an argument for schema discipline at capture time, not a database.

Run: `digest.py` over 77 competitive-intel brands (latest snapshot each), 2026-05-29. Raw dumps in `_out/` (gitignored).

## Results

| Query | Brands surfaced | Clean section | Degraded (price-only / mention-only) |
|---|---|---|---|
| Sermorelin | **30 / 77** | 14 | 11 / 5 |
| TRT | **31 / 77** | 13 | 9 / 9 |
| Tirzepatide | **40 / 77** | 16 | 16 / 8 |

- **Coverage is complete on presence.** Surfaced-brand count = raw `grep -l` count exactly. The affordance drops *nothing* that mentions the term.
- **One read replaces ~30 file opens.** Sermorelin digest = 191 lines / ~19 KB, answer-ready in a single read. Baseline = open 30 files, ~30× the token load, and easy to miss brands.
- **Answer-ready for the canonical query.** Even "price-only" hits carry real numbers — Sermorelin pricing for ~25 brands ($99, $116/mo, $126, $130, $159, $179/mo, $187, $195, $199/mo …) is right there. You can answer *"how do brands describe + price Sermorelin?"* from the digest alone.

## Where it breaks (the useful part)

- **Fidelity, not coverage, is the axis that matters.** ~45–60% of hits land in a clean `###` section; the rest degrade to price-lines or a "would need to open the file" pointer.
- **The cause is upstream:** degraded hits are brands where the term lives in nav/prose, or where products weren't captured into a consistent `## Products` / `### <product>` shape. **The affordance is only as good as the capture's structure.**
- **Implication:** the lever is a consistent offering schema *at capture time* (Tier-1 "product index"), which would push fidelity toward 30/30. That's exactly "spend on conventions, not infrastructure" — a schema, not a DB.

## What this means for the engine

1. **Ship a `digest`-style affordance as rung 2.** ~80 lines, no deps. Wrap it in a skill the agent reaches for (the discoverability half of the agent-workflows failure).
2. **The frontmatter + products schema is what raises fidelity** — prioritize the convention spend over an index.
3. **Defer rung 3 (SQLite).** Nothing here needed it. Revisit only when a query wants true aggregation/joins (counts, ranking) rather than consolidated retrieval.

## Caveats / cleanup

- Heuristic, single fixture (telehealth), three terms. Not a controlled A/B against a live agent — a proxy on cost + a read-through on fidelity.
- Minor formatting artifact: price-line bullets render as `- -` (source line already starts with `-`). Cosmetic.
- `digest.py` keys on the *latest* snapshot per brand and a naive frontmatter parse — fine for a probe, not hardened.
