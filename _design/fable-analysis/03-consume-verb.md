# `/query-companies` — the consume verb

*Shipped 2026-06-09. Rung-2 fix for the cross-company consumption routing miss: a sibling skill, read-only, under the ~65-line fence. It is a router + guardrail layer over `QUERYING.md`, not a recipe book.*

## What Shipped

- `skills/query-companies/SKILL.md` — 46 lines; final runtime contract.
- `skills/query-companies/agents/openai.yaml` — lightweight UI/index metadata.
- Global links: `~/.claude/skills/query-companies` and `~/.agents/skills/query-companies`.
- Repo orientation updated: `CLAUDE.md` and `README.md` now route consume work through `/query-companies`, while keeping `QUERYING.md` as the recipe contract.

## Final Description

```yaml
name: query-companies
description: >
  Use for named-company comparison or lookup prompts that can be answered from
  the local web-research company store, especially pricing, offerings, ownership,
  catalog breadth, cohort cuts, and price-visibility: "compare X and Y", "what
  do these competitors charge / offer", "which brands sell <thing>", "who owns
  X", "is X in the web-research store", "what has the store captured on X".
  Answers are captured-state snapshots from cited primary-source dossiers instead
  of WebSearch. Do not browse, WebSearch, curl, or open live company pages just
  to verify; resolve with store.py find, answer from store files, and cite local
  paths plus governing capture clocks. Read-only: never scrapes, never spends.
  If current/latest or missing/stale capture is required, suggest /research-company
  refresh; for incomplete rosters suggest /deepen-offerings; for external signals
  use tools/. Not for general web search, news/funding events, financials,
  judgments, or non-company topics.
```

## Behavior Contract

1. Resolve the store through `$WEB_RESEARCH_HOME` first; quote it because the path has spaces.
2. Resolve every named company with `python "$WEB_RESEARCH_HOME/scripts/store.py" find <each>`; report status before answering.
3. Route by `QUERYING.md`'s one-rule table: `rg` for locate, PyYAML parse for structure, `store.db` only for many-pivot asks after rebuild.
4. Answer captured state from store files only. Cite local path + governing clock; prices use the `offerings.md` clock when that layer supplies the fact.
5. Gaps are hand-offs, never silent live fallback: cold/missing/currentness need -> `/research-company`; thin roster -> `/deepen-offerings`; external signal -> specific `tools/*.py`.

Trust rules stay as pointers, not restatements: negatives, counts, prices, and cohort cuts all defer to `QUERYING.md`.

## Verification

Controlled fresh sub-agent invocation passed: when explicitly told to use `/query-companies`, it resolved Hims + Hone, answered from local `offerings.md` rows, cited `store/hims-com/offerings.md` captured `2026-06-03` and `store/honehealth-com/offerings.md` captured `2026-06-04`, and reported no live web / no scrape / no credits.

The stricter naked prompt in the already-running Codex harness did **not** pass: repeated fresh sub-agents still treated testosterone pricing as a current-public-page task. That is a routing/discoverability caveat, not a recipe failure. Re-test in a new top-level session after the skill index reloads before claiming implicit routing solved.

## Scope Notes

- The verb consumes durable company state; it does not make latest/current claims unless the captured clock supports them.
- No corpus counts are baked here; status is computed at call time by `store.py find`.
- The skill owns routing and guardrails only. Query recipes remain in `QUERYING.md`; capture mechanics remain in `/research-company`; roster deepening remains in `/deepen-offerings`.
