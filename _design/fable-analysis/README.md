# Fable analysis — consumability

*2026-06-09. A deep-dive on achieving the engine's consumption goals, requested with fresh eyes. Produced by a 9-agent workflow — 3 evidence agents (live-consumer ethnography · prior-art distillation · a live 8-question probe), 3 design agents, 3 adversarial reviewers — then synthesized. **Proposals, not decisions.** Probe record: [`experiments/2026-06-09-consumption-mechanics/`](../../experiments/2026-06-09-consumption-mechanics/FINDINGS.md).*

## TL;DR

**The consume side works — it's invisible and unaccountable, not broken.** The live probe answered 8/8 real consumption questions correctly, store-first, $0, cold; 10/10 cold agents have found `README → QUERYING.md` unaided. The failures are **visibility failures** (stubs no recipe can see, a derived db that's silently stale, baked numbers in QUERYING.md that are now wrong) and **one routing failure** (consumption intent has no verb — and the rival skill that caused the P4 warm-re-scrape is *installed again*, despite BACKLOG saying otherwise).

**The live consumer validates the architecture.** competitive-mine built its own judgment lens (cartography) *on the engine's own parsers*, refused to bake judgments into the store, and quotes State/Signals/Judgments back approvingly. The demand is better **State plumbing** — capture-status, clocks, faithful spine — not a smarter engine.

**One meta-lesson ran through everything:** between the probe and this synthesis, 5 stubs became profiles (15→10) — counts rot in *hours* on a live store. **Trust signals must be computed at call time, never written down.** Every recommendation below follows that rule.

## Recommendations — three ship-sets, in order

| # | Ship | Fixes (observed, not imagined) | Size | Status |
|---|---|---|---|---|
| **A** | **Trust surface** → [02](02-trust-surface.md): `store.py find` sees stubs + prints clocks/`predates:` · `store.py health` · QUERYING.md strip-the-baked-numbers + one answer-trust convention · fenced `FIELD_VERSIONS` | Stub false-negatives (probe #1) · no staleness visibility (Q7) · stale doc numbers (probe #3) · the remembered stamp-check tax | **S** | ✅ shipped 2026-06-09 |
| **B** | **`/query-companies` verb** → [03](03-consume-verb.md): sibling read-only router over QUERYING.md, ~65 lines; per-company status report before any answer; gaps are hand-offs, never silent web fallback. Ships atomically with A's `find` change; **re-probe with the rival installed** | The P4 routing miss (live again) · warm/stale/missing made visible · the store finally read via `WEB_RESEARCH_HOME` | **S/M** | ▶ next |
| **C** | **Corpus-wide lens** → [04](04-derived-lens.md): un-gate `offerings` (6 rosters invisible today) · `coverage` + `_meta` tables · rebuild-before-read convention · fences restated honestly (ranking stays cohort-gated) | Silent store.db staleness (probe #2) · capture-status manifest the consumer asked for · Beekeeper gets fences *in the artifact* | **M** | — |

A before B (the verb depends on `find`); C independent but reads better after A's QUERYING cleanup.

## Explicitly not built — and the trigger that changes it

- **JSON-export verb** (the consumer's faithful-spine ask) — rule of two; trigger: a *second* project rebuilds the spine.
- **Rebuild-on-capture hooks** — many writers; partial freshness automation lies. The 0.5s rebuild convention wins.
- **A staleness threshold / "stale" verdict** — no consumption policy exists; report dates until a consumer defines one.
- **Judgment columns** (molecule, price_num, archetypes) — cartography is the blessed project-side home; absorbing it re-grows Doro.
- **Store-scan utility · logo-path contract** — observed once each; named so deferral is visible.

## Open decisions for Brian

1. **The rival skill.** `competitive-research-audit` is installed (BACKLOG line 34 is stale). Options: keep-and-outcompete (recommended — it's the honest re-probe condition, and it serves non-store domains) · uninstall · patch it to check the store first. BACKLOG line needs updating either way.
2. **Enumeration backfill.** 37/47 telehealth rosters are `enumeration: unknown` — every breadth answer is a floor. Retiring it = `/deepen-offerings` passes across the active cohort = real Firecrawl spend. Worth it for the cohort you're actively mining?
3. **Verb name.** `query-companies` recommended (verb-object house style; "compare-companies" too narrow, "consume-store" presumes store knowledge).

## What I'd push back on

Nothing in this round needs new infrastructure — the adversaries' strongest finding was that the *designs themselves* kept over-claiming ("structurally impossible", "nothing can drift") and under-shipping the subtractive fixes. The discipline that matters: **strip the lies before adding the features** (A's QUERYING cleanup precedes everything), and keep every trust signal computed, never baked.

## Docs

[01 — Evidence](01-evidence.md) (what the consumer does · what's proven · the probe) · [02 — Trust surface](02-trust-surface.md) · [03 — Consume verb](03-consume-verb.md) · [04 — Derived lens](04-derived-lens.md). Each design doc ends with an "Adversarial review — what changed" section; the raw adversary verdicts flagged real bugs (e.g. `AVG(price_verbatim)` *executes* in SQLite; `store.py find` structurally cannot see stubs).
