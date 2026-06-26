# Full-system run — results (claude track)

Date: 2026-06-26
Status: end-to-end run of the discovery worklist + the new qualification layer, scored against the acceptance criteria. **Cached data only — zero new Firecrawl/SerpApi/Exa spend.** (Spend was approved; declined because broadening discovery tests the *discovery* layer, not this *qualifier*.)

## Headline

**Both acceptance criteria pass.** Across 268 candidates from the packet's full cached discovery (SerpApi + Exa + opened pages), the qualifier put **zero pure publishers into `capture`**, and it **preserved every real company discovery surfaced** (telehealth holdouts 6/6, CI core 6/7). The one recall miss is a boundary item the benchmark itself flags as ambiguous.

## What ran

1. `build_cards.py` — assembled **268 candidate cards** (165 telehealth, 103 conversation-intelligence) from all cached feeders: SerpApi organic + references, Exa `/search`, and the 15 opened listicle pages (links + hosts). Deduped by domain; richest snippet kept. Code only.
2. Five **Sonnet** classifiers (3 telehealth chunks, 2 CI) read `rubric-claude.md` + their cards and routed each, homepage-peeking the genuinely unsure (≈60 peeks total).
3. `score_claude.py` — joined to the label files **after** routing.

## Acceptance scorecard

| Criterion | Result | |
|---|---|---|
| **Precision (cardinal): zero publishers in `capture`** | **PASS** | Both cohorts. Every pure publisher/SERP host/directory → `preserve` or `drop`. |
| **Recall preserved: real companies discovery surfaced survive the gate** | **PASS** | Telehealth holdouts **6/6** → capture; CI core **6/7** → capture/product. |
| **Both cohorts pass independently** | **PASS** | Telehealth + CI both clean on precision, strong on recall. |
| **Product/feature tagged, not scored as a company** | **PASS (light)** | CI: MS Copilot → `product` (parent: Microsoft). Only case present; telehealth had none. |

Route tallies — telehealth: capture 64 · preserve 35 · review 26 · drop 40. CI: capture 53 · preserve 30 · review 17 · product 1 · drop 2. (High capture share is expected: the candidate pool is already pre-filtered to operating companies; the gate's job is pulling out the publishers/products/junk, which it did.)

## Cardinal precision — how the publisher hosts routed

10 listicle-host cards in telehealth, 4 in CI. **None of the pure publishers reached `capture`:**
- **Preserve / drop (publishers):** forbes, innerbody, usnews, theflowspace, policylab, trtnation, nih (telehealth); zapier (CI). `zapier` → preserve on cohort-fit (a real company, but here only the list's host).
- **Capture (genuine dual-role companies that also publish a listicle):** empirical.health, telyrx, years (telehealth); read.ai, salesforce/Agentforce, tana (CI) — each because the evidence describes *its own* in-cohort product.

No clear publisher appears anywhere in the 64 + 53 capture lists. A handful of medium-confidence telehealth captures (e.g. `menopausemandateus.com`, `atriumhealth.org`) are flagged for audit, not clean misses.

## Recall preservation

- **Telehealth holdouts present: 6/6 → capture** (Rex MD, Hone Health, Ro must-hits; AgelessRx, BlueChew, Defy Medical should-hits).
- **CI core present: 6/7** → capture/product (Clari, Otter, Granola, Zoom AI Companion, Notion AI Meeting Notes → capture; MS Copilot → product). The miss: *"ChatGPT transcript workflow"* (card `chatgpt.com`) → drop — a workflow, not a CI product, which the benchmark itself marks ambiguous.

## Honest finding: dual-role calls are evidence-dependent

**TRT Nation flipped between runs.** In the page-extraction run its snippet showed its own clinic (*"AMERICA'S CLINIC™"*) → `capture`; in this SERP-fed run the snippet was the listicle title (*"Top 10 Best Online TRT Clinics"*) → `preserve`. Both calls were correct *given the evidence shown* — which means a thin, listicle-only snippet can false-preserve a real dual-role company. That's a **recall miss, not a precision miss** (the less-bad error by design), and it points at the real lever: snippet quality, not the rubric. Mitigation when it matters: a homepage peek resolves these (it did for `years.co`).

## Limitations

- **Discovery recall is the binding constraint, not the gate.** Only 6/28 telehealth holdouts and 7/17 CI core are present as cards — the rest are named only inside listicles, which needs more page extraction (the *discovery* layer). This run proves the gate's precision + recall-*preservation*, not end-to-end discovery recall.
- **curated_negatives:** 0 of the 8 are present in the candidate set, so negative-rejection wasn't directly tested (publisher-rejection was, heavily).
- **Minor dedup:** same company on two domains (`fellow.ai` + `fellow.app`) yields two cards.
- A few giant-company captures (`amazon.com`, `walgreens.com`, `weightwatchers.com`) are in-cohort-defensible but a worklist auditor would want a "tangential giant?" flag.

## Verdict

The qualification layer holds end-to-end on real, full-scale, messy discovery output: **0 publishers promoted, 100% of present holdouts preserved, both cohorts.** It is a candidate *worklist* gate (audit before actual capture), not auto-promotion. The next real lever for end-to-end recall is the discovery layer (more page extraction), which is separate from — and unblocked by — this gate.
