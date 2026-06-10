# Evidence — how the store is actually consumed

*Three independent agents, 2026-06-09: an ethnography of the live consumer, a prior-art distillation across the consumption experiments, and a live 8-question mechanics probe (cold agent, recipes only, $0). Probe record: [`experiments/2026-06-09-consumption-mechanics/`](../../experiments/2026-06-09-consumption-mechanics/FINDINGS.md). Numbers below are as-of probe time and **already rotted once during this analysis** — see the postscript.*

## 1. The live consumer: Teleprescribe competitive-mine

A 47-brand DTC-telehealth competitive analysis (`…/Teleprescribe Venture/research/competitive-mine/`). Pipeline: **cartography** (project-side SQLite + CSV exports, built read-only from the store) → strategic-lens (Notion stance) → viz (positioning map) → traction (separate Signals overlay, joined by slug, "never writes into the clean spine") → gauntlet (wedge tournaments whose claims are re-verified directly in the cartography DB).

**The headline: it built its own judgment lens — and that was correct.** Cartography exists to *deliberately add the judgments the store refuses* (canonical molecule key, normalized price magnitude), kept honest via a multi-agent judge→verify→repair pipeline with per-value trace + confidence. It did **not** use the engine's `build_db.py` — but its spine importer (`build_base.py`) **imports the engine's own `offeringscheck.parse_roster`**, so the SKU spine can't drift from the store contract. The consumer quotes the State/Signals/Judgments split back approvingly (`traction/v2/FRAME.md`): **the demand is for better generic State plumbing, not for the engine to move up the stack.**

**Question shapes observed (12):** within-slice price bands · visibility/gating posture · membership/all-in math · category coverage via prominence · enumeration-gated breadth · company control panel · archetype clustering · prevalence checks for strategy claims ("21 of 47 brands…[cartography.db, verified]") · **dedupe scouted brands against the captured set** · traction proxies per slug/SKU · launch-date provenance from cached captures · visual identity for viz.

**Frictions (with evidence):**

1. **"Store exists ≠ captured."** Stub folders (captures only, no `profile.md`) make dedupe false-negative; the scout note asks for an explicit priority rule for "in store but not captured."
2. **Enumeration floors** — 37/47 brands `enumeration: unknown`; breadth rankable across only 9. Engine trust-debt a `/deepen-offerings` backfill would retire.
3. **Derived-copy drift** — exports hold 48 brands while the project's own DATA-MAP prose still says 47. Lenses regenerate; prose doesn't.
4. **Three clocks** — price truth is `offerings_captured_at`, not the profile clock.
5. **Two-system add dance** — engine capture, then project `/cartography-add`.
6. Tool transport flakiness (Trustpilot, wayback slash-variants, sandbox network approvals); JS-only pages defeat simple fetches; **relative logo paths** silently couple every viz consumer to `$WEB_RESEARCH_HOME`.

**Wants from the engine** (observed, not speculative): a faithful-spine export (build_base re-implements ~90% of build_db's parsing) · a capture-status manifest (slug → docs present + three clocks + enumeration) · a store-scan term-inventory utility · enumeration backfill · a logo asset-path contract. **Stays project-side:** the judgment layer, archetypes, traction judgments, strategic verdicts.

## 2. Prior art — what's proven vs. asserted

The rung ladder, honestly scored:

- **Rung 1 (grep / YAML-parse): proven repeatedly.** Five experiments, three cohorts, cold agents; full battery ~1.3s at N=45. Including the sharp edge: `grep | uniq` is provably wrong, parse instead.
- **Rung 2 (recipes + skill): half proven at analysis time.** QUERYING.md worked **once an agent was inside the store** — 10/10 cold agents found `README → QUERYING.md` and answered correctly, zero live recaptures (consumption-affordance). The *skill* half was proven only for single-company capture (4/4). **Postscript:** `/query-companies` has since shipped; explicit invocation passed, implicit routing still needs a fresh-session re-test.
- **Rung 3 (derived index): mechanism proven, cold-consumer safety untested.** Build/JOIN mechanics, speed-irrelevance (164ms build / 0.17ms query vs 9ms pure-Python), and the failure modes (price wall, enumeration trap, cross-type footgun) are all proven. No probe has ever hit the lens cold.

**The P4 incident, precisely:** a fresh agent asked to compare TRT pricing across Hims/Hone/Marek/Maximus — all four warm — never touched the store. The comparison intent pattern-matched a rival global skill (`competitive-research-audit`, zero store awareness); the agent re-scraped all four live, hit 403s/timeouts/aggregator contamination, and shipped figures it itself flagged unverified. Not unfindability — **routing**: QUERYING.md is only visible once you're already inside the store. (Caveats: n=1, Opus-only, primed sub-agents.)

**Postscript after ship-set B (2026-06-09):** the rival-specific condition above is no longer current; that skill has been retired/archived. The active miss-mode is simpler: naked pricing/comparison prompts can still default to current public pages. `/query-companies` now exists and passes when invoked explicitly; implicit routing needs a fresh top-level session re-test after the skill index reloads.

## 3. The live probe — 8 questions, cold, $0

**All 8 answered correctly, store-first, ~14 tool calls. Every recipe worked as written. The failures are visibility failures, not recipe failures.**

| Q | Result |
|---|---|
| Henry Meds + freshness | ✅ 2 steps; friction: freshness is per-layer |
| Women-only/first cohort | ✅ 2 steps; trap: QUERYING says cohort is "13/13" — it's 49 |
| Semaglutide pricing | ✅ 3 steps, ~70 SKU rows / 39 brands verbatim; stop-line hit exactly where documented |
| Delighted's parent | ✅ 2 steps; relations not reciprocal — only the reverse-join finds children; doc says "1/23/8", actual 3/31/8 |
| Hims ketamine (negative) | ✅ strong "not offered" — but rules give signals, not a verdict procedure |
| B2B SaaS corpus-wide | ✅ generalizes beyond telehealth (23 membership / 19 primarily) |
| Stalest + stubs | ⚠️ primitives work, **no recipe exists**; found **15 stub folders invisible to every profile-globbing recipe** |
| "brello?" | ✅ resolver folded the alias zero-shot |

**store.db side-check: stale, silently.** Built Jun 6; markdown newer in 5+ companies; rugiet missing entirely — a Recipe-7 semaglutide query would have silently dropped its SKUs. No `built_at` meta, no banner; `--check` tests schema drift, not freshness. *"Nothing would have told me."*

**Ranked frictions:** (1) stub invisibility · (2) silent store.db staleness · (3) stale baked numbers in QUERYING.md ("13/13", "1/23/8", footer `schema_version: 1`) — the doc violates its own anti-reconciliation principle · (4) re-typed PyYAML boilerplate · (5) no per-company relations view.

## Postscript: the count-rot demo

At probe time the store held 105 folders / 90 profiles / 15 stubs. **One hour later, mid-analysis: 95 profiles, 10 stubs** — a parallel session was capturing. Any number baked into prose is wrong within hours on a live store. That is the empirical case for the design thread running through docs 02–04: **trust signals must be computed at call time, never written down.**
