# Proposal: Cohort Discovery Worklist

Date: 2026-06-25
Status: accepted for packet-local validation; broad verb not graduated
Source request: Brian asked for `/agent-build-propose` on discovering companies not yet in the store, using the rejected 2026-06-24 neighbor-discovery packet as context. Revised after proposal review with Brian's validation sets: masked telehealth holdouts from Notion Organizations, plus conversation-intelligence tools.
Strategic frame: [`_design/2026-06-26-coverage-strategy-frame.md`](../../../../_design/2026-06-26-coverage-strategy-frame.md)
Current outcome: validation artifacts are useful, but the broad `/cohort-discovery` verb did not earn graduation; see [`decision-surface.md`](decision-surface.md). Current follow-on synthesis: [`candidate-filtering/2026-06-26-cohort-discovery-worklist-synthesis.md`](candidate-filtering/2026-06-26-cohort-discovery-worklist-synthesis.md).

<!-- Status tracks the PROPOSAL lifecycle only: proposed -> reviewed -> accepted | revise | park | cut.
     Never flip it to a build status. `implemented`, the implementation receipt, and the gate log
     belong in implementation-notes.md -- keep this file a plan, so proposal-review can gate it before code. -->

## Required Fields

risk: medium
write_scope: First slice only: packet-local validation artifacts under `experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/`: frozen validation inputs, receipts, and, if useful, a trimmed evaluation workflow derived from `experiments/_archive/2026-06-20-cohort-discovery/cohort-discovery.workflow.js`. Do not edit `store/`, `tools/`, `skills/`, `QUERYING.md`, schemas, Signals paths, or run `/research-company`. A reusable `/cohort-discovery` skill is a follow-on packet after the value gate passes.
spend_stop: Proposal writing spends none. Future validation is dry-run discovery only: max two cohorts before review; per cohort max 4 category/web queries, 3 listicle pages, 2 demand-side seed queries, and 2 Exa `/search` novelty queries. Verification must use gathered feeder evidence first, then at most one official/company page or one corroborating source per candidate when needed. No Firecrawl company captures, no store writes, no scheduled runs. Stop and ask before a third cohort, any paid capture, broader candidate research, automated re-run, or any source family outside the approved panel.
acceptance_checks: Implementation must produce `implementation-notes.md`, frozen packet-local validation inputs, and one receipt per validation cohort. Telehealth pass: before discovery, export from Notion Organizations (`collection://d0beabe1-d50f-4a15-9349-c6fab743dac8`) where `Offering Type` contains `DTC therapeutics brand`; holdouts are only F2/F3/F4 rows whose `Website` resolves to profiled store entries, and the discovery run may not use Notion as a source. Score F3/F4 as must-hit and F2 as should-hit. F0/F1 is only a weak-known-brand over-rank check, not the hard pollution gate. Hard pollution uses Brian's curated negatives plus a human review checkpoint for generated not-in-store / uncertain candidates; no curated-negative or Brian-rejected review item may land in Tier A/B. Conversation-intelligence pass: compare output against Brian's ranked core list and adjacent transcription-dev list, reporting top-10 overlap, major rank misses, and adjacent pollution. For both cohorts, report per-feeder recall/precision/novelty plus union performance; if the union does not materially beat the best single feeder, park or downscope rather than pass with explanation. Do not graduate a verb unless Tier A/B precision is at least 80% after verification and the telehealth F3/F4 holdouts are recovered.
escalate_if: Work wants to create or mutate store profiles, auto-capture candidates, persist category/cohort panels as Signals, add schema/ontology, build entity-resolution machinery, add a new capture tool, schedule monitoring, or treat a source panel as a market census/ranking.

## Problem

Truffle's Coverage problem is now larger than this packet. The durable frame is: **what coverage deserves to exist?** Company profiles should be added strategically, not just because a source found them. The first priority is neighborhood context around already-captured companies; the second is cross-company comparison and pattern reads.

This packet tests one practical slice of that frame: can Truffle produce a defensible capture worklist for a known cohort without bloating the primary store?

Truffle can deeply capture one company, and Recipe 9 can spot listicle-based coverage gaps. The engine still lacks the upstream worklist answer: "given what we have already captured, which missing companies are worth evaluating for capture next?"

The previous answer, `/discover-neighbors`, proved the failure mode: Exa-led, shape-reviewed, then value-failed at 5 of 32 obvious docs/PM players plus missed telehealth category-definers. Better prior art exists: the 2026-06-20 cohort-discovery bake-off found that no single source is enough, but `websearch` + `listicle` recovered most of the verified pool, with cheap add-ons contributing uniques. The reviewer then found the remaining gap: the test sets were not frozen.

The job here is not "find companies near X" and not "grow Truffle autonomously." It is "stage a cohort worklist from the store outward, then test whether the resulting capture queue is useful enough to justify later coverage growth."

## Short Answer

Build discovery as a **cohort worklist**, not a neighbor search. This is a staging artifact under the coverage-strategy frame: it gathers candidates, evidence, exclusions, and queue decisions before anything reaches the primary store.

Test it first with a masked telehealth holdout drawn from Notion Organizations, then with a fuzzy conversation-intelligence cohort. Start with the store's profiled set, run a small union of external feeders, verify the candidate pool, then tier verified net-new companies by evidence strength and cohort relevance.

Do not graduate a skill until a dry validation run proves recall and precision against known cohorts. The value gate is the product here.

## Constraints / Non-Goals

- Not a census, market-share claim, or objective ranking.
- Not a stored cohort/category object.
- Not auto-capture; output is propose-don't-write candidates for `/research-company`.
- Not a Notion-backed discovery run. Notion Organizations is the evaluation oracle for the telehealth holdout, hidden from the discovery agent.
- Not Exa-led. Exa `/search` can be an optional long-tail novelty feeder; Exa `/findSimilar` stays out unless the question is URL-neighbor similarity.
- Not heavy entity resolution. Domain remains the key; one-company/many-domain cases are flagged in the receipt, not solved with Doro-style machinery.

## Options considered

1. **Stay with Recipe 9 only.** Keep discovery as bounded-live listicle radar. Lowest complexity, already documented, but too narrow: it misses direct brand enumeration, demand-side substitutes, and long-tail specialists. [should have]
2. **Add a named verb around one feeder.** Fast to invoke, but already falsified in spirit. Whether the feeder is Exa, listicles, or web search, single-source discovery is structurally brittle and can look clean while missing category-definers. [cut]
3. **Validate a cohort-discovery union, then graduate.** Reuse the existing bake-off shape: store baseline + web/category search + Recipe 9 listicles + demand-side `/vs`/alternatives + optional Exa `/search`; verify hard; tier net-new capture candidates. Test against masked telehealth holdouts and a conversation-intelligence boundary list. [should have] -- **recommended**

## Recommendation

Choose option 3, but make the first implementation a **validation packet**, not an engine verb.

The key shift is from "source output" to "coverage worklist." The store supplies the denominator we actually own: profiled companies only, with stubs separate. External sources supply candidate names, not truth. Verification decides cohort membership. The output is a caveated capture queue, not a market map.

This replaces ad-hoc discovery and the failed Exa-only verb with the smallest recipe prior evidence says can work. Masking known telehealth profiles tests the exact rediscovery failure without mutating `store/`; the conversation-intelligence list tests whether the recipe can handle a fuzzy SaaS boundary without promoting adjacent transcription APIs. If the union does not recover known strong players before capture spend, it should not become a reusable skill.

## Implementation Sketch

1. **Freeze validation inputs before discovery.** Telehealth: query Notion Organizations for `Offering Type` contains `DTC therapeutics brand`, then write a packet-local holdout file from F2/F3/F4 rows that resolve to profiled store entries. Current schema uses `Formidability Tier` values `F0 Shell`, `F1 Presence`, `F2 Established`, `F3 Institutional`, `F4 Apex`; F3/F4 are must-hit and F2 is should-hit. Separately freeze Brian's curated low-formidability / wrong-type negatives and a human-review checkpoint for generated not-in-store / uncertain candidates. F0/F1 can be reported as a weak-known-brand over-rank check, but it is not a hard pollution proxy because Notion is already curated. Conversation intelligence: use Brian's ranked core list -- Gong, Clari, Loom, Otter, Granola AI, Dovetail, Zoom AI Companion, Microsoft Copilot for Teams, AlphaSense, Fathom AI, Notion AI Meeting Notes, OpenAI Whisper, ChatGPT transcript workflow, Claude transcript workflow, Rewind, Apple Voice Memos, Jamie AI -- and the adjacent transcription-dev list -- Rev, Deepgram, ElevenLabs, AWS Transcribe, OpenAI Whisper, AssemblyAI, Nuance, Verbit, Descript, Symbl.ai. Whisper is intentionally dual-listed; the receipt must classify that ambiguity explicitly.
2. **Mask, don't mutate.** For telehealth, pretend selected profiled holdouts are absent from the store baseline in packet-local logic only. Keep `store/` untouched and keep Notion unavailable to discovery.
3. **Run a small feeder union.** Core feeders: category web search/direct brand enumeration and Recipe 9 listicles. Add demand-side alternatives/owned `/vs` pages when seeds exist. Use Exa `/search` only as a novelty probe and report its incremental uniques separately.
4. **Dedupe and verify.** Fold obvious domain variants, resolve against the store, then verify each candidate is real and in-cohort using bounded evidence. Exclude payers, retailers, directories, content sites, defunct brands, and adjacencies unless included.
5. **Tier and score.** Tier A = verified, masked/not-profiled, corroborated across source families or category-defining. Tier B = verified single-source or long-tail specialist. Tier C = plausible but uncertain. Score telehealth by F3/F4 recall, F2 recall, curated-negative Tier A/B pollution, and Brian's human review of generated not-in-store / uncertain candidates. Score conversation intelligence by top-10 overlap, rank deltas, and whether adjacent transcription-dev tools are separated from end-user meeting/CI tools. If the union does not beat the best single feeder, park or downscope. Only after passing should a later packet add a lightweight `/cohort-discovery` skill.

## Review Notes

Review should focus on the acceptance gate. If it tests only file shape, spend caps, or caveat wording, it repeats the rejected packet's miss. The load-bearing value claim is measurable: union discovery should recover obvious missing companies better than ad hoc search or any single feeder, while keeping the capture queue clean enough to spend on.

Open call for review: whether the F2 telehealth threshold should be a hard numeric pass rate or a reported should-hit metric. F3/F4 recall and curated-negative / human-review pollution are hard gates.
