# Automated Routine Planning & Budgeting

Date: 2026-06-16  Status: Planning

---

## Existing Plans
- Claude -- Claude Max 20x -- $200/mo -- Usage limit resets weekly
- Firecrawl -- Hobby (6.5k credits/mo) -- $28/month -- Renews on the 6th of every month
- SerpApi -- Free Plan (250 searches/mo) -- Free -- Resets on the 6th of every month

#### Upgrade Options
- Claude -- None - I'm already on the max subscription plan. I could pay for "additional usage", but that's metered pricing and gets super expensive. Much better off just getting the most out of the base subscription (amortized cost).
- Firecrawl:
    - Hobby: Max 5 concurrent requests
        - 5,000 cr/mo -- $19/mo
        - 6,500 cr/mo -- $28/mo -- **current**
        - 8,000 cr/mo -- $37/mo
    - Standard: Max 50 concurrent requests
        - 100,000 cr/mo -- $99/mo
        - 130,000 cr/mo -- $156/mo
        - 160,000 cr/mo -- $213/mo
    - Growth: Max 100 concurrent requests
        - 500,000 cr/mo -- $399/mo
- SerpApi:
    - Free: **current**
        - 250 searches/mo
    - Starter: _Brian's open to upgrading to this plan_
        - 1,000 searches/mo
        - $25/mo
        - 200 search throughput / hour
    - Developer:
        - 5,000 searches/mo
        - $75/mo
        - 1,000 search throughput / hour
    - Production:
        - 15,000 searches/mo
        - $150/mo
        - 3,000 search throughput / hour

---

## Measured baseline (2026-06-16)

One run per variant from the 6-row bench (`experiments/2026-06-16-routine-cost-bench/results.csv`), cross-checked against the `scripts/runcost.py` credit log. **n=1 per variant — point estimates, not distributions.** Tokens shown in K/M (raw integers in the CSV); `min` is bench wall-clock session time — `runcost`'s Firecrawl-only fetch latency (median 112s) is a different metric and is not used here.

**Confidence ordering for planning:** credits are exact (Firecrawl's own per-call ledger); tokens are solid (per-session, marker-isolated); **minutes are the softest** — n=1, and several runs were measured while parallel captures contended for Firecrawl's 5-concurrent cap, so wall-clock reads as an upper bound. And **B (Wisp) is the vast-catalog ceiling, not a typical brand** — budget a normal cohort capture at A/D (6–8 cr, ~9M tok), not B's 24 cr / 27M tok.

### Corpus + historical baseline (the denominator)

The store today: **132 companies**, 62 with `offerings.md`, 26 with `visual.md`. What it cost to build, from the full `runcost.py` capture ledger:

| Window | n | median | mean | p90 | max | total |
|--------|--:|-------:|-----:|----:|----:|------:|
| **All-time** | 135 | 9 | 10.6 | 17 | 60 | **1,434 cr** |
| **Recent** (since 2026-06-10) | 36 | 8 | 8.6 | 13 | 24 | 311 cr |

All-time's fat tail (max 60) is early big-catalog captures; discipline since has tightened the recent window to median 8 / p90 13. **Plan a fresh routine against the recent numbers**; the all-time total (~1,434 cr built the whole 132-company store) is the anchor for any "refresh everything" math. *(Credit-recorded runs only; ~10 legacy runs predate per-call logging.)*

### Per-verb cost (one run each)

| Var | What ran | Credits | Min | in | out | cache_create | cache_read | **total tok** |
|-----|----------|--------:|----:|----:|----:|-------------:|-----------:|----------:|
| A | cold core, no modules — **the floor** | 6 | 13.6 | 99K | 80K | 619K | 8.43M | **9.23M** |
| B | cold full — cohort + offerings + logos | 24 | 43.1 | 93K | 209K | 1.16M | 25.79M | **27.25M** |
| C | visual-evidence | 0\* | 12.7 | 86K | 75K | 246K | 4.12M | **4.53M** |
| D | deepen-offerings | 8 | 15.9 | 86K | 94K | 284K | 8.47M | **8.93M** |
| E | warm, freshness gate ON (0 fetch) | 0 | 0.6 | 86K | 7K | 114K | 667K | **0.87M** |
| F | warm, forced full re-fetch (gate OFF) | 10 | 15.1 | 88K | 39K | 220K | 4.48M | **4.83M** |

\* CSV `credits` cell reads `9`, but that's the tool-call count — visual-evidence makes **0 Firecrawl calls** (reuses cached screenshots / browser re-render); the row note says "0 credits (9 calls)".

### Marginal reads

- **B − A (full module bundle + catalog depth vs the floor):** +18 credits, +29.5 min, **+18.0M tokens (B ≈ 3× A)**. Almost the entire delta is cache_read (+17.4M) and output (+130K) — the cost of cohort + offerings + logos on a deep catalog.
- **E vs F (what the freshness gate saves):** on a warm company the default gate turns F's 10-credit / 15.1-min / 4.83M-token re-fetch into E's **0-credit / 0.6-min / 0.87M-token no-op** — saving 10 credits, 14.5 min, ~3.95M tokens (F ≈ 5.5× the tokens, ~25× the wall time of E).
- **C (visual = 0 credits):** **token + time only** — 0 Firecrawl credits, 12.7 min, 4.53M tokens. Mid-weight on tokens, zero on spend.
- **D (deepen):** 8 credits (= baseline median), 15.9 min, 8.93M tokens — token load ≈ the floor capture (A), but spent as a targeted roster backfill rather than a fresh core.

### Drift check

Live `runcost.py captures --since 2026-06-10`: **n=36, median 8 cr, mean 8.6, p90 13, max 24, total 311 cr.**

Every measured capture sits **inside** that baseline — nothing reads as drift:
- A (6), D (8 = median), F (10) → within the body (all ≤ p90 13).
- **B (24) = the baseline max** → catalog-depth tail, not drift. The window's max=24 *is* this Wisp run (the bench is folded into the 36), so B **defines** the tail rather than running past it.
- C (0), E (0) → below the floor by design (visual reuses cached shots; warm gate skips the fetch).

### Token framing

**cache_read dominates** — 91–95% of total token volume on every capture variant (76% on the tiny warm-gated E). The "cost" is overwhelmingly cached-context reads, not fresh input/output.

Per-run totals (above) scale ~linearly: **K runs/week ≈ K × per-run total.**

| Verb | /run | 5/wk | 10/wk | 20/wk |
|------|-----:|-----:|------:|------:|
| Floor (A) | 9.23M | 46M | 92M | 185M |
| Full (B) | 27.25M | 136M | 272M | 545M |
| Warm gated (E) | 0.87M | 4.4M | 8.7M | 17M |

No weekly token ceiling is asserted here — Anthropic doesn't publish a Max-20x token cap. These are per-run loads; whether a given weekly mix fits headroom is something to watch live via `/cost`, not against a fixed number.

### Signals

Not benchmarked here. Per-source cost lives in `runcost.py signals`: SEC EDGAR + Trends free, Trustpilot ~1 Firecrawl credit/capture (30 cr / 31 captures — same budget as captures), Exa ~$0.022/call, SerpApi ~2 cr/capture — and **SerpApi Free's 250 searches/mo is the tight ceiling.**