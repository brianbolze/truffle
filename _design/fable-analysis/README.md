# Fable analysis — consumability

*2026-06-09. A deep-dive on achieving the engine's consumption goals, requested with fresh eyes. Produced by a 9-agent workflow — 3 evidence agents (live-consumer ethnography · prior-art distillation · a live 8-question probe), 3 design agents, 3 adversarial reviewers — then synthesized. Probe record: [`experiments/2026-06-09-consumption-mechanics/`](../../experiments/2026-06-09-consumption-mechanics/FINDINGS.md). Ship-sets A, B, and C have since landed.*

## TL;DR

**The consume side works — it was invisible and unaccountable, not broken.** The live probe answered 8/8 real consumption questions correctly, store-first, $0, cold; 10/10 cold agents found `README → QUERYING.md` unaided. The failures were **visibility failures** (stubs no recipe could see, a derived db that's silently stale, baked numbers in QUERYING.md that rotted) and **one routing failure**: consumption intent had no verb. Ship-set A fixed the trust surface; ship-set B added `/query-companies` as the read-only consume verb.

**The live consumer validates the architecture.** competitive-mine built its own judgment lens (cartography) *on the engine's own parsers*, refused to bake judgments into the store, and quotes State/Signals/Judgments back approvingly. The demand is better **State plumbing** — capture-status, clocks, faithful spine — not a smarter engine.

**One meta-lesson ran through everything:** between the probe and this synthesis, 5 stubs became profiles (15→10) — counts rot in *hours* on a live store. **Trust signals must be computed at call time, never written down.** Every recommendation below follows that rule.

## Recommendations — three ship-sets, in order

| # | Ship | Fixes (observed, not imagined) | Size | Status |
|---|---|---|---|---|
| **A** | **Trust surface** → [02](02-trust-surface.md): `store.py find` sees stubs + prints clocks/`predates:` · `store.py health` · QUERYING.md strip-the-baked-numbers + one answer-trust convention · fenced `FIELD_VERSIONS` | Stub false-negatives (probe #1) · no staleness visibility (Q7) · stale doc numbers (probe #3) · the remembered stamp-check tax | **S** | ✅ shipped 2026-06-09 |
| **B** | **`/query-companies` verb** → [03](03-consume-verb.md): sibling read-only router over QUERYING.md, 46 lines; per-company status report before any answer; gaps are hand-offs, never silent web fallback | The P4 routing miss · warm/stale/missing made visible · the store finally read via `WEB_RESEARCH_HOME` | **S** | ✅ shipped 2026-06-09; implicit-routing re-test passed 2026-06-09 (in-repo; cross-project discovery unobserved) |
| **C** | **Corpus-wide lens** → [04](04-derived-lens.md): un-gate `offerings` · `coverage` + `_meta` tables · rebuild-before-read convention · fences restated honestly (ranking stays cohort-gated) | Silent store.db staleness (probe #2) · capture-status manifest the consumer asked for · Beekeeper gets fences *in the artifact* | **M** | ✅ shipped 2026-06-09 |

A, B, and C are shipped. The deferred items below stay deferred until their triggers fire.

## Explicitly not built — and the trigger that changes it

- **JSON-export verb** (the consumer's faithful-spine ask) — rule of two; trigger: a *second* project rebuilds the spine.
- **Rebuild-on-capture hooks** — many writers; partial freshness automation lies. The 0.5s rebuild convention wins.
- **A staleness threshold / "stale" verdict** — no consumption policy exists; report dates until a consumer defines one.
- **Judgment columns** (molecule, price_num, archetypes) — cartography is the blessed project-side home; absorbing it re-grows Doro.
- **Store-scan utility · logo-path contract** — observed once each; named so deferral is visible.

## Open decisions for Brian

1. **Enumeration backfill.** Many active rosters still read as `enumeration: unknown` — every breadth answer there is a floor. Inspect `coverage` / `telehealth_full` before budgeting `/deepen-offerings`; retiring it means real Firecrawl spend across the cohort you're actively mining.
2. ~~**Implicit routing re-test.**~~ Resolved 2026-06-09: a naked pricing prompt in a fresh top-level session routed to `/query-companies` unaided (store-only, clocks cited). Residual: cross-project discovery via the global skill links is unobserved — tracked in BACKLOG.

## What I'd push back on

Nothing in this round needs new infrastructure — the adversaries' strongest finding was that the *designs themselves* kept over-claiming ("structurally impossible", "nothing can drift") and under-shipping the subtractive fixes. The discipline that matters: **strip the lies before adding the features** (A's QUERYING cleanup precedes everything), and keep every trust signal computed, never baked.

## Docs

[01 — Evidence](01-evidence.md) (what the consumer does · what's proven · the probe) · [02 — Trust surface](02-trust-surface.md) · [03 — Consume verb](03-consume-verb.md) · [04 — Derived lens](04-derived-lens.md). The raw adversary verdicts flagged real bugs (e.g. `AVG(price_verbatim)` *executes* in SQLite; `store.py find` structurally could not see stubs before ship-set A).
