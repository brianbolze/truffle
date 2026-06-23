# Findings — cohort discovery bake-off

**Run 1:** 2026-06-20, menopause telehealth, dry (no captures). 89 agents · 2.6M tokens · ~26 min.
Verified pool: **29 in-cohort** (52 candidates → verify cut 23). **7 in store, 22 net-new.**

## Recall race (which discovery technique wins)

| Technique | raw hits | found (in pool) | recall | precision | net-new | notes |
|---|---|---|---|---|---|---|
| **websearch** (firecrawl_search) | 29 | 20 | **0.69** | 0.69 | **17** | clear winner — nearly is the cohort alone |
| listicle (SERP "best of") | 19 | 10 | 0.34 | 0.53 | 8 | solid #2; also feeds the best rank proxy |
| llm (parametric) | 16 | 7 | 0.24 | 0.44 | 6 | cheap floor; noisiest |
| store (baseline) | 9 | 7 | 0.24 | **0.78** | 0 | highest precision, capped at what's captured |
| demand (alternatives/compare) | 11 | 6 | 0.21 | 0.55 | 4 | marginal, but cheap + a few uniques |
| exa (/findSimilar) | — | — | **FAILED** | — | — | agent execution failure, NOT a real 0 (key + CLI verified working). Re-run before judging. |

**Union earns its keep:** websearch found 20/29; the other 9 came from listicle/llm/demand/store. No single technique is complete, but **websearch + listicle ≈ most of the pool.**

## Rank race (which cheap signal tracks the LLM tournament)

Top-8 agreement with the judgment ranking: **listicle_recurrence 6/8 · serp_visibility 6/8 · ads_presence 4/8.**
→ **listicle recurrence is a free formidability proxy** that matches the Opus tournament 6/8. You don't need the tournament to rank.

## Issues surfaced

1. **Exa execution failure** — inconclusive, needs re-run. Smoke test hint: neighbors for midihealth were generic-health (healthassist, medevice), so Exa *precision* for this cohort may be low regardless — confirm.
2. **One-company-two-domains double-count** — `hers.com` + `forhers.com` are the same brand (Hims & Hers women's line); both entered the pool AND the top-K. Domain-keying can't catch this (the anti-Doro entity-resolution gap, live).
3. **Formidability ≠ cohort-relevance** — the tournament floated generalist giants (hers/forhers #1–2) above menopause pure-plays. For "fill out THIS cohort," raw formidability surfaces brands you already know over the specialist long tail you actually want. The verb likely wants relevance×formidability, or tiered (specialist vs generalist) ranking.
4. **Cost** — the per-domain signal agents are the waste: ads = 29 Sonnet agents each shelling one CLI. Batch ads + serp into one agent over the whole pool (≈ −28 agents).

## The byproduct (already valuable)

Net-new menopause **specialists** found — beats the hand-built MRL-022 worklist on coverage:
midihealth · myalloy · evernow · bywinona · elektrahealth · pandiahealth · onstella · tryelsie · lasara · gayawellness · calythea · zivhealth · joinjosie.
MRL-022's HerMD / Allara did **not** surface (likely defunct / PCOS-adjacent) — automated discovery corrected the manual list.

## Verdict (the recipe)

- **Best discovery:** `websearch` core + `listicle` second. `llm`/`demand` are cheap add-ons for a few uniques. `store` is the precision baseline. `exa` = re-run before deciding.
- **Best cheap formidability proxy:** `listicle_recurrence` (or SERP visibility) — free, 6/8 vs tournament.
- **Before graduating a verb:** (a) fix Exa + batch the signal stage (cost); (b) resolve formidability-vs-relevance ranking; (c) decide whether to handle one-company-multi-domain or accept it.
- **Generalizability:** untested off menopause — a SaaS sub-cohort re-run is the fast-follow.
