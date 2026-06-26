# Implementation Notes: Cohort Discovery Worklist

Date: 2026-06-25
Status: validation plus search/page-extraction probes complete; hold broad verb; candidate-filtering synthesis added
Worktree: `/private/tmp/truffle-cohort-discovery-worklist`
Strategic frame: [`_design/2026-06-26-coverage-strategy-frame.md`](../../../../_design/2026-06-26-coverage-strategy-frame.md)

## What Changed

- Added `lead-decision.md` recording Brian's approval to implement this as a packet-local validation pass.
- Added `validation-plan.md`.
- Added frozen validation inputs:
  - `validation-inputs/telehealth-holdouts.json`
  - `validation-inputs/conversation-intelligence-targets.json`
- Added first telehealth checkpoint receipt:
  - `receipts/telehealth-human-review-queue.md`
- Added scored validation receipts:
  - `receipts/telehealth-validation.md`
  - `receipts/conversation-intelligence-validation.md`
- Added direct WebSearch addendum:
  - `receipts/websearch-addendum.md`
- Added second-iteration rerun scripts and raw/scored outputs:
  - `run_iteration2_queries.py`
  - `score_iteration2.py`
  - `receipts/raw/iteration-2/`
  - `receipts/iteration-2-validation.md`
- Added a packet-local search framing harness over the existing raw outputs:
  - `search_harness.py`
  - `receipts/search-harness.md`
  - `receipts/raw/search-harness/search-summary.json`
- Added a bounded page/entity extraction probe:
  - `page_extraction_probe.py`
  - `receipts/page-extraction-probe.md`
  - `receipts/raw/page-extraction/`
- Added a fresh-session brief and parked companion candidate-qualification prior art:
  - `candidate-filtering/candidate-qualification-fresh-session-brief.md`
  - `candidate-filtering/candidate-qualification-mini-proposal.md`
  - `candidate-filtering/candidate-qualification-mini-proposal-review.md`
- Added candidate-filtering prototype evidence and synthesis:
  - `candidate-filtering/README.md`
  - `candidate-filtering/claude-prototyping/`
  - `candidate-filtering/codex-prototyping/`
  - `candidate-filtering/2026-06-26-cohort-discovery-worklist-synthesis.md`

No store profiles, tools, skills, schemas, Signals paths, or `QUERYING.md` were changed.

## Telehealth Holdout

The telehealth oracle was frozen from Notion Organizations data source
`collection://d0beabe1-d50f-4a15-9349-c6fab743dac8`.

Filter:

- `Offering Type` contains `DTC therapeutics brand`.
- `Formidability Tier` is F2/F3/F4.
- `Website` resolves to a profiled store entry.

Frozen holdouts:

- F4: 6
- F3: 7
- F2: 15
- Total: 28

F3/F4 are must-hit. F2 are should-hit. Notion is evaluation-only and must not be used as a discovery source.

## Pollution Amendment

Brian clarified that Notion F0/F1 rows are mostly decent and should not be treated as a comprehensive junk set.

Updated rule:

- F0/F1 can be reported only as a weak known-brand over-rank check.
- Hard pollution uses Brian's curated negatives plus a human review checkpoint for generated not-in-store / uncertain candidates.
- No candidate Brian marks `tier_c_only` or `exclude` may land in Tier A/B.

Brian's curated negatives were frozen in `validation-inputs/telehealth-holdouts.json`:

- healthequity.com
- promisepharmacy.com
- absoluterx.com
- drtelex.com
- jinfiniti.com
- menmd.com
- mintmd.com
- mintmedicine.com

## First Telehealth Checkpoint

Prepared `receipts/telehealth-human-review-queue.md` after a bounded first discovery sweep.

The queue is intentionally not a comprehensive market map. It exists to test the human review step that catches candidates the store does not know yet and prevents low-formidability / wrong-type candidates from being promoted.

Brian reviewed generated candidates:

- `worth_capture`: Ulo, Alloy Women's Health, Midi Health, Mochi Health, Eucalyptus Health.
- `tier_c_only`: RoenRx, MyStart, MangoRX, BrightMeds, G-Plans Direct, Evernow.
- `exclude`: Zealthy, FitRx, AMRx.
- unresolved / keep `unsure`: Juniper.

Scoring rule for the next pass: none of the `tier_c_only` or `exclude` rows may land in Tier A/B.

## Verification

- Parsed both frozen JSON inputs with `python3 -m json.tool`.
- Ran `git diff --check` after packet edits.
- Ran an ASCII check over authored packet Markdown/JSON files; raw source stderr is preserved as
  captured tool output and excluded.
- Ran the second-iteration live source panel and scorer:
  - `python3 experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/run_iteration2_queries.py --skip-existing`
  - `python3 experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/score_iteration2.py`
- Ran the search-framed packet-local harness:
  - `python3 experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/search_harness.py`
- Ran the page/entity extraction probe:
  - `python3 experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/page_extraction_probe.py`
  - `python3 experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/page_extraction_probe.py --firecrawl-failed`
  - `python3 experiments/01-agentic-build/changes/2026-06-25-cohort-discovery-worklist/page_extraction_probe.py --score-only`

## Scored Validation Result

Telehealth failed the pass gate, even after the direct WebSearch addendum:

- F3/F4 must-hit recovery: 10/13.
- F2 should-hit recovery: 5/15.
- Direct WebSearch added One Medical, but still missed Niagen Plus, Rex MD, and Lifeforce.
- Union did not materially beat the best single feeder enough to justify a broad telehealth verb.
- The human pollution gate worked: no Brian-marked `tier_c_only` or `exclude` row is eligible for Tier A/B.

Conversation intelligence was stronger after the direct WebSearch addendum, but exposed a boundary issue:

- External-only top-10 overlap: 7/10.
- Store-first union top-10 overlap: 9/10.
- Union materially beat any single feeder.
- The benchmark mixes company capture targets, product rows, and workflow rows; scoring should split those before any graduation decision.

Overall recommendation: do not graduate the verb from this packet. Move to lead review only with a revise/downscope recommendation.

## Iteration 2 Rerun Result

The rerun tested better query construction over the same raw source families, using anchor-category
language from captured store profiles rather than one broad telehealth phrase.

Result:

- Telehealth got worse mechanically: 6/13 F3/F4 and 4/15 F2, despite recovering Rex MD.
- Conversation intelligence held its prior shape: external-only 7/10 top-10 overlap; store-first
  9/10, with Loom still missed.
- SerpAPI AIO drift appeared in 3 rows; organic results remained usable and the drift is recorded
  in `receipts/raw/iteration-2/run-summary.json`.

Conclusion: better prompts/queries alone do not earn the broad verb. The next packet should
downscope to explicit subcohort plus page-extraction validation, not broaden the source panel.

## Search-Framed Addendum

Brian reframed the problem as classic search: define relevance, generate candidates, rank, and
score top-K quality rather than only asking which source family found which holdout.

The packet-local harness converts the frozen inputs into graded relevance judgments, extracts entity
candidates from the existing iteration-2 raw outputs, applies a transparent RRF-style ranker, and
reports P@K / R@K / nDCG@K plus miss tables. It spends nothing and does not open new pages.

Result:

- Telehealth external raw-unit search is poor at top-K: P@10 0.100, R@10 0.030, nDCG@10 0.139.
- Telehealth retrieval by label matches the prior shape: must-hit 6/13, should-hit 4/15, worth_capture 2/5.
- Conversation intelligence remains much stronger: store-first top-10 retrieval is 9/10, with Loom still missed.
- The top telehealth ranks include publisher/source domains and long-tail artifacts, confirming the next
  improvement should be page/entity extraction from result pages, not another query-only pass.

This addendum did not reverse the packet decision. It set the next gate: page extraction should
improve relevant recall and top-K precision over the raw-unit baseline without promoting grade-0/1 candidates.

## Page Extraction Probe Result

Brian greenlit modest credit spend to test the search-framed next step. The probe fetched a fixed
panel of 11 telehealth result/list pages and 4 conversation-intelligence pages. Direct HTTP yielded
13/15 pages; Firecrawl fallback recovered the two blocked GLP-1 pages, for an estimated 2 Firecrawl
base scrape credits. No SerpAPI or Exa calls were added.

Result:

- Telehealth improved from P@10 0.100 / R@10 0.030 / nDCG@10 0.139 to P@10 0.600 / R@10 0.182 / nDCG@10 0.562.
- Telehealth retrieval by label improved to must-hit 11/13, should-hit 7/15, worth_capture 4/5.
- Conversation intelligence improved from P@10 0.500 / R@10 0.500 / nDCG@10 0.649 to P@10 0.600 / R@10 0.600 / nDCG@10 0.718.
- Remaining must-hit telehealth misses are Niagen Plus and Lifeforce.
- The top ranks still include source domains; no grade-0/1 reviewed item lands in the top 20 after Midi Health is corrected to `worth_capture`.

Conclusion: page/entity extraction is worth keeping in the evaluated recipe. It is not enough by
itself to graduate a broad verb. The next version needs candidate-type filtering / verification
gating plus focused coverage for remaining subcohorts such as NAD/longevity and healthspan labs.

## Remaining Work

- Use `candidate-filtering/2026-06-26-cohort-discovery-worklist-synthesis.md` as the current follow-on shape.
- Run one more packet-local validation on a third cohort before graduating any reusable verb.
- Keep page/listicle extraction in the evaluated workflow rather than relying on snippets.
- Add candidate filtering as agent-led qualification plus usefulness judgment, not durable regex machinery.
- Score discovery recall separately from filter recall preservation.
- Split conversation-intelligence scoring into company targets versus product/workflow targets.

Brian note for follow-on: do not add a new discovery source first. The iteration-2 rerun tried
better prompts/queries over the same raw tools; the next attempt should make page extraction,
candidate filtering, and usefulness / gap coverage explicit before expanding the tool surface.
