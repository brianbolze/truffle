# Candidate qualification — Claude vs Codex (arbiter comparison)

Date: 2026-06-26
Status: impartial external review of two parallel tracks. Packet-local; no engine changes.
Inputs read cold: both tracks' scripts + outputs, the [strategic frame](../../../../../../_design/2026-06-26-coverage-strategy-frame.md), the [kickoff brief](../candidate-qualification-fresh-session-brief.md), the label files. Claude metrics re-run live from `score_claude.py`; Codex metrics read from its own eval JSON + a direct inspection of its capture-ready rows.

## 30-second verdict

**Adopt the Claude track. Graft one idea from Codex.** Both gates clear the cardinal bar — zero pure publishers reach capture. They separate on everything else, and the deciding axis is the frame's own stated principle: *"agents should do classification and judgement; don't develop fancy logic and heuristics in code."* Claude is exactly that — a Sonnet pass over a ~50-line rubric, cited per card. Codex is the opposite: **2,957 lines of deterministic Python across three stages with zero LLM calls**; its `method:"agent_judgment_needed"` field is a string the code writes to mean "punt to a future agent" — the judgment is deferred, never done. Claude also wins recall (TH 6/6, CI 6/7 in one pass, zero spend) and queue legibility. The one thing worth taking from Codex: its explicit `boundary_review` bucket as a first-class, caveat-tagged route — better than Claude collapsing all uncertainty into "review."

## Apples-to-apples scorecard

| Dimension | Claude | Codex | Edge |
|---|---|---|---|
| **Precision (cardinal): 0 pure publishers in capture** | PASS — verified | PASS — verified | tie on the binary; **Claude on legibility** |
| **Recall preservation (present holdouts)** | TH 6/6, CI 6/7 → capture/review, one pass | V2: TH 2 / CI 0 to capture; rest parked; needs 2 more stages + spend | **Claude** |
| **Both cohorts pass independently** | Yes — TH + CI both clean | TH yes; CI scores 0 captures at V2 | **Claude** |
| **Product/feature tagged + parent noted** | Explicit `product` route (MS Copilot → parent Microsoft) | No product route; `product_or_workflow` folds into `boundary_review` | **Claude** |
| **Frame fit (agents judge, not code heuristics)** | Direct — LLM over rubric | Inverted — deterministic tag cascade, no LLM | **Claude (decisive)** |
| **Simplicity** | Edit one markdown file; 2 moving parts | 3 stages, 6 scripts, stopword set + examples JSON + regex extractor | **Claude** |
| **Generalization to a 3rd cohort** | Rubric is cohort-agnostic; no retune | Must extend stopwords + examples + extractor per cohort | **Claude** |
| **Reproducibility / determinism** | Non-deterministic (model + ~60 homepage peeks) | Fully deterministic, re-runnable | **Codex** |
| **Named ambiguity lane** | "review" is a catch-all | First-class `boundary_review` + machine-readable caveats | **Codex** |

## Bake-off: none run — why

A clean apples-to-apples run was **not feasible**. The two tracks read different input chains from the same raw evidence: Claude builds 268 flat domain-keyed cards from `cards.jsonl`; Codex builds 374 cards (incl. 28 regex-extracted name-only candidates) from `query-panel.json` + page-extraction pages via an `ObservedCandidate` dataclass. Domain overlap is only ~255/268, so plugging one's output into the other would contaminate any score with coverage drift, not gate behavior. Fallback used instead: **Claude metrics re-run live** from `score_claude.py` against the shared label files; **Codex metrics read from its own eval artifacts** plus a direct inspection of `codex_capture_readiness_results.json`.

**Caveat on Codex's self-reported numbers: its eval oracle is broken.** It name-joins qrels to whatever row carries the brand string, so it matches *Gong* → `salesforce.com`/`askelephant.ai`/`tana.inc`/`g2.com` (listicle pages titled "Gong Alternatives") and *Hims* → `docs.google.com`. The "Codex rejected must-hit Hims" finding is therefore a **join artifact, not a routing error** — but a self-eval that mislabels its own recall is itself a strike against trusting Codex's reported pass/fail.

## What each track does better

**Claude does better**
- **Honors the frame literally.** Verified: a Sonnet classifier reads `rubric-claude.md` and emits a cited route per card. The "own-offering signal" is a single, transferable decision rule, not packet-fitted code.
- **Recall in one pass, zero spend.** Re-run confirms TH 6/6 must/should-hits and CI 6/7 core → capture/review/product. The lone CI miss ("ChatGPT transcript workflow" → drop) is flagged ambiguous by the benchmark itself.
- **Legible capture queue.** Each capture row is a real domain with a quoted own-product reason. Dual-role hosts (empirical.health, telyrx.com, years.co) are captured *because* the evidence shows their own in-cohort offering — and each cites it.
- **Lowest maintenance + best generalization.** Behavior change = edit a markdown file. No stopword list, examples JSON, or name-extractor to keep in sync per cohort.

**Codex does better**
- **Determinism / reproducibility.** No LLM in the hot path; re-runs are bit-identical and free. Genuine for audit and regression — but bought by hard-coding the judgment.
- **Explicit ambiguity as a named state.** `boundary_review` separates "too little evidence to decide" from "flag for a human," with per-row machine-readable caveats (`source_title`, `name_only`, etc.). This is the one design idea worth porting.
- **Existing-store awareness.** Stage 3 splits out `existing_profile` so already-captured companies don't re-enter the queue. Worth a lightweight nod in Claude's gate.

## Two findings that cut against Codex's headline claims

1. **Codex is not "more precise" than Claude — its capture-ready rows are *less* legible.** Its acceptance check "0 source/listicle artifacts capture-ready" passes only because it keys on the domain. But the rows are *named after listicle titles* ("9 Best Gong Alternatives… (cuebo.ai)", "10 Best Gong Alternatives… (aviso.com)"), and `revenue.io` / `aviso.com` / `cuebo.ai` reach capture-ready via *owned-listicle* evidence — the exact dual-role path Codex claimed to handle more conservatively than Claude. Same call as Claude, worse presentation.
2. **The three-stage pipeline doesn't close its own loop.** After V2 + boundary resolution + capture readiness and ~15 live credits, ~206 of 297 boundary rows remain unresolved, and the final capture-ready list (22 rows) is *smaller* than Claude's direct capture list (117) while requiring more orchestration. The residual boundary pile grows with every new cohort and never resolves without an agent step the architecture omits.

## Recommended direction: adopt Claude + one graft

**Keep (Claude):** the single-pass LLM-over-rubric gate; the own-offering precision rule; the explicit `product`+parent route; the build-cards/score scripts; rubric-as-contract.

**Graft (from Codex):** a first-class **`review` → `boundary_review`** split with a machine-readable `caveat` tag per routed row (`dual_role`, `thin_snippet`, `name_only`, `adjacent`, `local_clinic`, `tangential_giant`). This makes the review queue sortable and auditable **without adding a pipeline stage**. Optionally add a one-line `existing_profile` check so store-covered companies skip the queue.

**Do not adopt:** the deterministic tag cascade, the kind-examples JSON, the stopword list, the regex name-extractor, or the three-stage orchestration — they invert the frame's core principle and front-load cohort-specific judgment into code that must be hand-maintained per market.

## Known risk to watch on the adopted track

Claude's recall is only as good as the richest feeder snippet: TRT Nation flipped capture↔preserve between runs purely on snippet shape (own-clinic copy vs. listicle title). This is an upstream discovery-layer problem, but it can silently false-preserve a real dual-role company. **Mitigation:** require a homepage peek for any card whose only evidence is a source-page snippet — not just the cards the agent self-flags as unsure.

## Cheapest next step

Edit `rubric-claude.md` to (a) split `review` into `boundary_review` with a closed `caveat` tag set, and (b) require a homepage peek when the sole evidence is a source-page snippet. Re-run the five Sonnet classifiers over the existing cards (zero new spend) and re-score. Then run the **same rubric against a third, non-telehealth/CI cohort** — that is the real graduation gate before this becomes a reusable engine verb.
