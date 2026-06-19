---
created: 2026-06-19
authors: codex
status: proposed
---

# Bounded Live Evidence Proposal

**Proposal:** let autonomous Market Read Lab runs use outside sources and spend a small amount of capture credit when the selected question genuinely needs it.

Do this with a light run contract, not a browsing-control system. The contract should tell the agent what kind of evidence would make the answer trustworthy, what source families are in bounds, when to stop, and how to leave receipts. It should not micromanage search-query counts or tool-call counts.

## Why

The Strategist questions we want to test are not always answerable from cached company State.

Owned pages are useful, but many real market reads need surfaces like SERPs, listicles, reviews, forums, ads, social, Wayback, or fresh news. Blocking all live sources makes the lab safer, but it also hides obvious gaps in Truffle's source coverage.

The goal is not "let the agent browse." The goal is **small, autonomous source panels that expose what the store is missing**.

## Proposed v0

Add one autonomous live mode:

```yaml
evidence_mode: bounded-live
```

This mode is allowed only when Scout fills a live evidence plan:

```yaml
live_evidence_plan:
  approved_by: Brian
  approval_scope: autonomous Market Read Lab runs
  budget_class: light
  review_after: 3 bounded-live runs
  evidence_goal:
  source_families_allowed: []
  source_families_preferred: []
  source_families_disallowed:
    - login-only or paywalled sources
    - broad crawling
    - private / non-public data
  stop_when:
    - the source panel is good enough to answer with visible caveats
    - the next source would expand the question rather than verify it
    - the remaining uncertainty is a framing judgment, not a sourcing gap
    - sources conflict in a way that needs human interpretation
  disallowed_actions:
    - write-back to store/
    - code, schema, or template changes
    - durable primitive creation
    - triage graduation
```

`budget_class: light` means: use the smallest useful source panel. Prefer free/local/cached sources first. Spend capture credits when a source is likely to verify, date, or falsify a load-bearing claim. Stop with "insufficient evidence" rather than broadening into a crawl.

Do not encode `5 searches`, `3 scrapes`, or `N tool calls` into the contract. Those numbers look safe but are mostly fake precision. If a tool needs operational rate limits later, put them in the tool wrapper, not in the market-read convention.

Approval is a standing policy window, not a per-run prompt. Review after a small batch of bounded-live runs and tighten only where actual failures show up.

Every outside source used must be logged:

```yaml
live_evidence_used:
  - source_or_query:
    source_family:
    action_taken: searched | opened | captured | scraped | read-local-signal
    reason:
    source_grade: primary | secondary | lead
    captured_at:
    spend_note: none | free | paid-credit
    claim_ids_supported: []
```

## Agent Context

Give the agent judgment-rich context rather than a rigid tool budget:

- What would make the answer trustworthy?
- Which source family is likely to carry that evidence?
- Which source families are only leads?
- What is the expected denominator or sample frame?
- What uncertainty should remain visible instead of chased?
- What source gap would be useful to report even if the run cannot close it?

Source-family guidance:

| Source family | Good for | Main caveat |
|---|---|---|
| Owned / official pages | Pricing, product, claims, partnership, policy, source-of-truth facts. | Marketing copy is still self-reported; date it. |
| SERPs / listicles | Denominator seeds, third-party category framing, default-player discovery. | Leads, not proof; snippets are never decision-grade. |
| Reviews / forums | Objections, distrust, regret, praise, language mining. | Directional sample, not representative market truth. |
| Ads / social / creators | Channel story, offer hooks, audience identity, promise language. | Volatile and algorithmic; keep claims narrow. |
| Wayback / dated signals | Tenure, launch timing, offer-change direction. | Snapshot density and missing captures matter. |
| News / regulatory / manufacturer pages | Fresh events that can invalidate cached reads. | Prefer primary sources; secondary news needs explicit grade. |

## Guardrails

- **Budget class is a judgment boundary.** `light` allows a small source panel, not a census.
- **Stop beats sprawl.** When the next step is "keep searching broadly," stop and write the gap.
- **Snippets are leads.** Search/news snippets can point to a source; they cannot support confident claims alone.
- **Spend is allowed, but must be purposeful.** Paid capture is acceptable for load-bearing sources, not speculative expansion.
- **Current claims need receipts.** Pricing, policy, launch, partnership, regulatory, and news claims need URL, capture date, and source type.
- **No graduation.** Live evidence can inform `read.md` and triage submissions, but cannot mutate State, templates, skills, code, or schema.

## What Changes

Small convention updates only:

- Skill rule: allow autonomous full-cycle runs when `evidence_mode: bounded-live` and `live_evidence_plan` is present.
- Scout context: let Scouts select high-value Strategist questions that need a light live panel.
- Run notes template: add `live_evidence_plan` and `live_evidence_used`.
- Receipt template: keep `external-source`, `source-panel`, and `direction-finding` grades; do not add a new ledger system.
- Loop prompts: fail closed if live evidence is used without a plan, receipts, source grades, or stop-rule notes.

Current adoption boundary: the live runner contract still only accepts `store-only`,
`local-existing`, and `live-external-needs-approval`. This proposal is not active until
`README.md`, Scout/Loop prompts, `run-notes.md`, `receipt.md`, the local skill, and
`new_run.py` deliberately add `bounded-live`.

## Stress Tests

**Review/forum read:** Allowed, but the result should say "in this sampled panel, objections clustered around..." not "customers think..." unless the panel is intentionally representative.

**Current pricing or policy read:** Allowed, but primary owned/regulatory/manufacturer pages should outrank news and snippets. If primary pages cannot be captured, the claim stays a lead.

**SERP/listicle denominator:** Allowed, but the denominator is a seed or cross-check. The read must state inclusion rules and avoid "complete market" language.

**Credit-spend drift:** If the agent is still spending because the question keeps widening, the run has failed the stop rule. End with the source gap and submit pressure.

**Weak evidence after a light panel:** The correct outcome is "not enough evidence," not "search harder." The lab learns from that gap.

## Pushback

This should be more ambitious than the current no-live rule, but simpler than the first draft.

Do not build a general browsing agent, source registry, or hard call-budget ledger. Start with one mode, one budget class, one source-family plan, and one receipt trail. Let agents use judgment inside that frame; judge the runs afterward.
