# Cohort discovery — technique bake-off

**Date:** 2026-06-20 · **Status:** scaffolded, not yet run.

## Hypothesis

A reusable `cohort-discovery` verb can take a plain cohort description —
*"menopause telehealth / compounded-Rx D2C brands"* — and return a **ranked roster of the
most relevant / formidable companies in that space**: store-first, but its real job is
surfacing the **net-new** companies worth capturing. Several discovery and ranking
techniques already exist in the repo; we don't know which win on coverage, precision,
novelty, or cost. **This probe races them.**

This experiment chooses the *recipe* — it is not the production verb. Output = this
`FINDINGS.md` (+ the workflow, kept as a template if one earns it). Designed **generic**;
menopause telehealth is only the validation cohort.

## Two bake-offs

1. **Recall race** — which *discovery* technique finds the most of the real cohort, with
   the least junk, cheapest?
2. **Rank race** — which *formidability signal* best orders the verified set, measured
   against an LLM pairwise-style tournament as the reference ranking?

## The field

**Discovery techniques (recall race)** — each runs as an isolated subagent, blind to the
others, so we can measure its *standalone* yield:

| Technique | How | Repo source |
|---|---|---|
| `store` | grep the local store for in-cohort brands | `scripts/store.py`, `store/*/telehealth.md` |
| `llm` | parametric enumeration, no tools — the cheap floor | — |
| `listicle` | SERP → ≥2 authoritative "best of" lists → union (cross-source recurrence) | `tools/serpapi.py` + MRL recipe (runs 012/022/024) |
| `exa` | Exa /findSimilar neighbors from seed brands | `tools/exa_similar.py` |
| `websearch` | category-query enumeration | `firecrawl_search` (MCP) |
| `demand` | demand-side cross-shop: "alternatives to X", owned `/compare`·`/vs` pages | `firecrawl_search` / scrape |

**Formidability signals (rank race):**

| Signal | How | Source |
|---|---|---|
| `listicle_recurrence` | # of authoritative lists / techniques that named it | from discovery (free) |
| `serp_visibility` | appears for category queries, and at what rank | `tools/serpapi.py` (a few category SERPs, once) |
| `ads_presence` | actively running paid ads + recency | `tools/ads_transparency.py` |
| `judgment` | LLM pairwise-style tournament — the **reference** ranking | opus subagent |

## Method (the workflow)

`cohort-discovery.workflow.js`, staged:

1. **Discover** — fan-out, one isolated agent per technique (barrier; dedupe needs all).
2. **Verify** — dedupe by domain, then adversarially check each is *real* + *in-cohort*
   (kills hallucinations and confounds — payers, retailers, adjacents; cf. run-024's
   "payers aren't platforms" trap). The survivors are the **verified pool**.
3. **Signals** — gather formidability signals for the verified pool only.
4. **Rank** — LLM tournament produces the reference order; cheap-signal orders computed
   in-script; report which cheap signal best predicts the tournament.
5. **Capture** — auto-`/research-company` the top-K **net-new** brands. **Arg-gated,
   default OFF.**

**Eval = union-as-pool.** The verified in-cohort union is the truth pool. Each discovery
technique is scored on **recall** (% of pool it found alone), **precision** (% of its raw
hits that survived verification), **novelty** (net-new vs store), and **cost**. No external
gold set.

## Spend & boundary

- Discovery spends light SERP / Exa / Firecrawl-search credits.
- **Capture stage spends Firecrawl** (one `/research-company` per top-K net-new). Gated by
  `capture: true`; **run discovery dry first** to inspect the roster before spending.
- Model allocation (per-subtask, cost-aware): tool-running + verify agents on Sonnet; the
  judgment tournament inherits Opus. Tune in the script.

## Run

```bash
# dry: discovery + rank bake-off, NO captures
# (invoke the Workflow tool with scriptPath to cohort-discovery.workflow.js)
#   args: { capture: false }   ← default

# end-to-end: also capture top-K net-new
#   args: { capture: true, topK: 8 }
```

Args (all optional; defaults baked for the menopause validation cohort): `cohort`,
`seeds[]`, `category_queries[]`, `topK`, `capture`.

## Files

- `cohort-discovery.workflow.js` — the probe.
- `FINDINGS.md` — results + the recipe recommendation (after a run).
