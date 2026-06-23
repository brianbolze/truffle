---
created: 2026-06-20
last_updated: 2026-06-20
status: frame — ad-cluster discovery verb (bake-off experiment)
authors: Brian + Claude
---

# Frame: ad-cluster discovery verb

## 30-second skim

Goal: a verb that takes a **space** ("What ads are telehealth / compounded-Rx D2C brands
running right now?") and returns the **top-K trending ad clusters** in it — checking the store
first for companies the creatives can key to, but **not limited** to the store.

This is a **different shape** from the engine's existing ads layer. `tools/ads_transparency.py`
is **company → presence** (does `hims.com` run Google ads, since when) and is **blind to ad
messaging**. The ask is **space → creative themes** — a *discovery + clustering* verb whose
output (clusters / "trending" / relevance) is **reader-relative judgment**, so it lives in this
experiment, not the shared store, until it proves out.

The experiment **pits multiple pipelines against each other** (a Claude Workflow bake-off) and
picks a winner on a rubric — rather than committing to one technique blind.

## Decisions (2026-06-20)

1. **Cluster unit is itself a variable** — the bake-off clusters along multiple dimensions and
   reports which is most useful. Priority: **messaging-angle (primary)** → offer/price →
   advertiser-intensity → format/channel.
2. **v1 = prevalent-now, not velocity.** Drop the "trending" claim from v1 outputs; report top-K
   *most prevalent now*. (Per-company captures still land in the store, so a later repeat run can
   diff for true trending — a free option, not designed for in v1.)
3. **Tool survey before pipelines.** A discovery phase runs first: dig the **Apify** actor catalog
   and a **`/deep-research`** session on the broader ad-intelligence tool/technique landscape. The
   P-A/P-B/P-C pipelines below are *provisional contenders* the survey may add to or replace.
4. **Storage:** per-company raw captures → `store/<domain>/signals/ads_*` (reusable State/Signal);
   space-level cluster-map → experiment-local (judgment).

Remaining fork: **budget ceiling** — confirm before any paid capture run. The discovery phase is
research-only (cheap).

## What we already have (don't reinvent)

- **`tools/ads_transparency.py`** (live) — Google Ads Transparency, per-domain: format +
  first/last-shown + advertiser legal name. 1 SERP credit/call. Good for *who advertises +
  recency*; **weak for clusters** (no copy/imagery semantics).
- **`ad_library.py`** (deferred) — Meta Ad Library via Apify. The only source with real creative
  **text + image + keyword search** — the natural messaging source, but flagged unstable
  (actor pin, cost, push-not-demand framing) in `tools/BACKLOG.md`.
- **Engine conventions** (`tools/README.md`) — capture prints a JSON envelope, match-free; store
  home `store/<domain>/signals/<source_type>/<captured_at>.json`. Cluster-maps are synthesis →
  experiment-local.

## Constraints / what to protect

- **File-first, anti-Doro** — no living service, graph, or embeddings store. A cluster-map is a
  dated markdown/JSON artifact, regenerable.
- **Capture ≠ judgment** — raw creatives *can* be per-company store signals; the cluster/trending
  read is a labeled judgment, stays experiment-local.
- **Push, not demand** — running an ad proves budget + motion, not that it works. Every output
  says so.
- **Propose-don't-write** — an advertiser found that isn't in the store → a capture *proposal*,
  never an auto-write.
- **Brian's time + $ are scarce** — confirm before paid runs; smallest useful bake-off.

## Non-goals (v1)

- A standing monitor / scheduled ad-watch.
- A blended "ad-activity score."
- Cross-channel completeness (every ad platform).
- Minting a durable ad-cluster taxonomy into `SCHEMA.md` / `TAXONOMIES.md`.

## Proposed approach — a pipeline bake-off (to confirm)

*Provisional — the Phase-0 tool survey may add or replace contenders.* Each pipeline = **seed**
(who advertises?) × **source** (get creatives) × **cluster** (creatives → K themes), clustered
messaging-angle-first. Pit a few end-to-end and judge **comparatively** (tournament/rubric per
`.claude/docs/dynamic-workflows.md`), not by absolute scores.

- **P-A — Lean / store-first:** store telehealth domains → `ads_transparency.py` (Google ATC) →
  Claude thematic cluster. Cheapest, leans on live tooling; weak on messaging.
- **P-B — Messaging-rich:** open-discover advertisers (SERP listicle + Meta keyword search) →
  Meta Ad Library creatives → Claude cluster. Richest angles; needs Apify; most $.
- **P-C — Search-only baseline:** Firecrawl/web search ("what ads are [category] brands running
  2026," trade press, ad-spy galleries) → Claude cluster. No ad-platform API — tests whether
  plain search + Claude beats the APIs.

Workflow shape: fan-out the pipelines in parallel → each emits a candidate cluster-map (shared
structured schema) → an adversarial judge panel scores the rubric below → synthesize the winner
+ a "what each technique uniquely caught" note. Sub-agent briefs follow
`.claude/docs/effective-prompts.md`: role + why + pointers, not micro-script.

## Eval rubric (comparative)

- **Coverage** — distinct advertisers + creatives surfaced.
- **Messaging richness** — can you name the angle from the output?
- **Store-keyability** — % of surfaced advertisers that key to a store company (+ a
  proposed-capture list for those that don't).
- **Trending signal** — can it say what's *new/rising*, or only what exists? (gated on the
  time-axis fork)
- **Cost + reproducibility** — credits/$ spent; would a fresh agent reproduce it next week?

## Phase plan

- **Phase 0 — tool survey.** ✅ Done → [`phase-0-tool-survey.md`](phase-0-tool-survey.md). Resolved the
  contender set (supersedes the provisional P-A/P-B/P-C below): Track A = Apify
  `curious_coder` discovery → `apify/facebook-ads-scraper` enrichment (US DTC social, must-have);
  Track B = SerpApi GATC `text=` → `ad_details` (Google/YouTube, already owned); Foreplay API =
  premium optional. Shared LLM-clustering layer. Official Meta API + beyondops TikTok actor killed.
- **Phase 1a — de-risk probe.** ✅ Done → [`probes/PROBE-FINDINGS.md`](probes/PROBE-FINDINGS.md). Track A
  (Apify/Meta) validated as the **space-discovery + creative engine** (one call → 10 live US GLP-1 ads
  with copy). Track B (SerpApi/Google) **can't discover a space** — enriches *known* advertisers only,
  credit-heavy. Tracks are **asymmetric**: A = engine, B = optional channel-divergence probe.
- **Phase 1b — build (next).** Capture + LLM-clustering pipeline around Track A as the spine; Track B
  scoped to a sampled per-seed Google-channel comparison (or deferred). Keep capture experiment-local
  until the verb proves out; graduate to `tools/` after.
- **Phase 1c — run + judge.** ✅ Done → [`runs/2026-06-20/ad-cluster-map.md`](runs/2026-06-20/ad-cluster-map.md).
  275 creatives → 10 verified angles; price-transparency the runaway leader. 2-method bake-off + judge
  + adversarial verify (killed 2/12). Store-keyed + propose-capture worklist produced.
- **Phase 2 — verdict.** ✅ [`FINDINGS.md`](FINDINGS.md): **graduate lean** — Track A → `tools/ad_library.py`
  capture + keep the clustering `workflow.js` as a recipe (Judgment stays project-side); Track B optional.

Test space (assumed default): **telehealth / compounded-Rx D2C** — where we have keyable store
companies.

## Folder

```
2026-06-20-ad-cluster-discovery/
  FRAME.md                 ← this
  phase-0-tool-survey.md   ← Phase-0 output (next)
  (workflow.js, pipelines/, runs/, FINDINGS.md — Phase 1+)
```
