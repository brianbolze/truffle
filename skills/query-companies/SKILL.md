---
name: query-companies
description: >
  Use for named-company comparison or lookup prompts that can be answered from
  the local web-research company store, especially pricing, offerings, ownership,
  catalog breadth, cohort cuts, price-visibility, and broad single-company
  briefs: "tell me about X", "compare X and Y", "what do these competitors
  charge / offer", "which brands sell <thing>", "who owns X", "is X in the
  web-research store", "what has the store captured on X".
  Answers are captured-state snapshots from cited primary-source dossiers instead
  of WebSearch. Do not browse, WebSearch, curl, or open live company pages just
  to verify; resolve with store.py find, answer from store files, and cite local
  paths plus governing capture clocks. Read-only: never scrapes, never spends.
  If current/latest or missing/stale capture is required, suggest /research-company
  refresh; for incomplete rosters suggest /deepen-offerings; for external signals
  use tools/. Not for general web search, news/funding events, financials,
  judgments, or non-company topics.
---

# /query-companies — answer from the company store, not the live web

Router + guardrails over `QUERYING.md`. Read-only; never scrapes, never spends.
Recipes live in `QUERYING.md`; this file only fixes order of operations and
points at the trust rules.

## Steps

1. Resolve the store: `$WEB_RESEARCH_HOME` first; if unset (harnesses that skip
   the shell profile), fall back to the canonical single-user path
   `"/Users/brianbolze/Library/Mobile Documents/com~apple~CloudDocs/Web Research"`.
   Quote it — the path has spaces.
2. Resolve names -> slugs, always: `python "$WEB_RESEARCH_HOME/scripts/store.py" find <each>`.
   Report per-company status before answering: clocks per layer / `STUB` / not in store.
   If `find` prints `likely candidate`, inspect that slug before calling it a miss.
   If it prints `ambiguous candidates`, do not pick silently: use nearby context
   only if it clearly disambiguates; otherwise ask the user which company they
   meant, listing the candidate slugs/names.
3. Route via `QUERYING.md`'s one-rule table: for a human-facing ask about one
   profiled company, run `render.py` and **paste the link line it prints into
   your reply** (rendering without linking buries the artifact); `rg` for
   locate; PyYAML parse for structure; `store.db` only for many-pivot asks,
   and rebuild it first.
4. Group answers wear the §0 stamp: if the answer covers more than one company,
   open with `QUERYING.md` §0's one-line stamp (`Group · Set · Leaves out · Claim`).
   The set-type caps the claim; a question that needs more than the type allows
   becomes "open question," not a clean number.
5. Answer captured state from store files only. No WebSearch/browser/curl. Cite path
   + governing clock; prices use the offerings clock when they come from `offerings.md`.
6. Gaps are hand-offs, never silent live fallback: cold -> suggest `/research-company`;
   thin roster -> `/deepen-offerings`; external signal -> the specific `tools/*.py`.

## Trust Rules

- Negatives: apply `QUERYING.md`'s before-trusting-a-negative check first.
- Counts: enumeration-gated (`QUERYING.md` Recipe 4); floors are floors.
- Prices: verbatim + intra-cohort + hand-normalized; never a sorted `$ / mo` table.
- Cohort cuts: unclear/empty = "couldn't tell," not "no."
- Groups: every multi-company answer opens with the §0 stamp; the set-type caps the
  claim (store coverage ≠ market; empty field = "at least N," not "the rest don't";
  outside-list miss = "not in our store," not "not in the market").

## Scope

State only. Events, judgments, and financials are out of store scope; say so.
