# Candidate Qualification — Quick Proposal (claude track)

Date: 2026-06-26
Status: plan-only proposal + prototyping kickoff. Packet-local; no store / schema / tool / skill changes.
Frame: `_design/2026-06-26-coverage-strategy-frame.md` · Kickoff: `../candidate-qualification-fresh-session-brief.md`

## Problem

Page-extraction turns listicles / SERPs into a **mixed list** of names: real companies, the publishers that *wrote* the lists, and product/feature rows. Nothing sorts them, so source/publisher noise competes with real capture targets in the ranking.

## Approach — a two-question sort, agent-led

For each extracted name, an agent decides:

1. **What is it?** real company · publisher / list-writer · directory · product/feature (inside a platform) · reference/junk · unsure.
2. **What do we do?** `capture` (worth a full profile) · `preserve` (keep as source evidence, don't capture) · `product` (tag + note its parent) · `review` (flag for a look) · `drop`.

The call is driven by short **descriptions + signal words** per kind — *not* a list of named companies (Doro-style). Code assembles the evidence card (name, domain, source page, snippet); the agent makes the call with a cited reason.

**The precision spine:** promote to `capture` only when the evidence shows the entity selling **its own product in this market**. Ranking/reviewing *others* → `preserve`, never `capture`. When a name is clear but its website is unknown, allow one cheap **homepage peek**.

## The shortcut we are deliberately NOT building

> "If a name's website == the page it was found on → it's a publisher."

Real companies publish their own *"best X"* / *"alternatives"* listicles for SEO, so this rule wrongly drops them — it would have killed **4 of 6 real companies** in the hand probe (TRT Nation, Read AI, Tana, Empirical). Replaced by the own-offering signal above.

## What it replaces

The manual first-pass triage of *"is this even a company?"* across 100–200+ extracted names per run. It does **not** replace the final capture decision.

## Evidence (full-system run — see `results-claude.md`)

End-to-end over the packet's full cached discovery (SerpApi + Exa + pages), **268 cards, zero new spend**: **both acceptance criteria pass** — 0 pure publishers in `capture` (both cohorts) and 100% of present holdouts preserved through the gate (telehealth 6/6, CI core 6/7). Dual-role companies correctly captured via the own-offering rule. Known limitation: discovery recall (6/28 holdouts present as cards) is a separate, upstream layer — this run proves the gate's precision + recall-preservation, not end-to-end discovery recall.

## Acceptance checks (evaluation runs AFTER routing; labels never feed the sorter)

- **Precision (cardinal):** zero publishers / source pages in the `capture` pile.
- **Recall preserved:** real companies surfaced by extraction stay in `capture` + `review` (don't undo extraction's recall win).
- **Both cohorts** (telehealth + conversation-intelligence) pass independently — guards telehealth overfit.
- Product/feature rows tagged + parent noted, not scored as companies.

## Scope / guardrails

Packet-local docs + scripts only. Agent does the judgment (no bespoke publisher heuristics in code). Homepage peek allowed (free fetch); no Firecrawl / paid search. Labels (qrels) used only for scoring after routing. No reusable skill this pass. Graduates toward an engine verb only after a third, non-telehealth/CI cohort passes with the same rubric.

## Plan

1. `build_cards.py` — assemble evidence cards from the existing extraction output.
2. `rubric-claude.md` — the define-by-description sorting instructions.
3. Agent sort → `routed.jsonl`.
4. `score_claude.py` — join to labels, report precision / recall.
5. `results-claude.md` — write up.
