# Iteration 2 Validation Receipt

Date: 2026-06-26
Status: rerun complete; broad telehealth still fails; query-family-only revision not enough
Later note: the page/entity extraction probe has now run and improved recall; see [`page-extraction-probe.md`](page-extraction-probe.md). Query tuning alone remains insufficient.

## What Changed

Added a packet-local rerun path:

- `run_iteration2_queries.py` writes a fixed source panel to `receipts/raw/iteration-2/`.
- `score_iteration2.py` scores raw retrieval against the frozen validation inputs.
- `receipts/raw/iteration-2/query-panel.json` freezes the rerun query panel.
- `receipts/raw/iteration-2/score-summary.json` stores the computed scoring output.

This stays packet-local. No `store/`, tools, skills, schemas, Signals paths, or `/research-company`
captures were changed.

## Rerun Shape

The rerun tested Brian's follow-on note: improve prompts/queries over the same raw tools before
adding sources. Telehealth moved from one broad query shape to anchor-category families derived from
captured store profile language:

- ED / sexual health.
- longevity / NAD.
- healthspan / biomarker labs.
- menopause / HRT.
- GLP-1.
- TRT / hormone optimization.
- two demand-side queries using non-holdout store anchors.
- two Exa `/search` novelty probes.

Conversation intelligence used the same source families: category SERP, demand SERP, and Exa
`/search`, with the local store baseline applied for company-profile hits.

Live spend:

- SerpAPI: 28 credits.
- Exa `/search`: USD 0.088.

Run quality:

- 18 of 18 raw rows are usable for retrieval scoring.
- 15 of 18 completed cleanly.
- 3 SerpAPI rows hit AI Overview schema drift, but still emitted organic results. The runner records
  these as `capture_ok: false`, `usable_for_scoring: true`, and preserves the drift messages in
  `run-summary.json`.

## Telehealth Result

Mechanical retrieval score from raw source output:

- F3/F4 must-hit recovery: 6/13.
- F2 should-hit recovery: 4/15.

F3/F4 hits:

- One Medical.
- Rex MD.
- Hone Health.
- Noom Med.
- Peter MD.
- Ro.

F3/F4 misses:

- Hims & Hers.
- LifeMD.
- Niagen Plus.
- Wisp.
- Eden.
- Lifeforce.
- Remedy Meds.

F2 hits:

- AgelessRx.
- BlueChew.
- Defy Medical.
- Fridays.

F2 misses:

- Amble.
- Blokes.
- Geviti.
- Invigor Medical.
- Ivy Rx.
- Kingsberg Medical.
- Marek Health.
- Maximus Tribe.
- Nurx.
- ProHealth.
- Rugiet Ready.

Compared with the prior scored receipt, this is worse on broad telehealth recall: prior recovery was
10/13 F3/F4 and 5/15 F2 after the WebSearch addendum. The new panel did recover Rex MD and added
some F2 evidence, but it lost too many heads that the broader GLP-1/TRT/HRT page-enumeration pass
had found.

Interpretation:

- Better category-language prompts alone do not fix broad telehealth discovery.
- Exa `/search` is still mostly a novelty feeder: useful examples surfaced, but curated-set recall
  stayed low.
- NAD/healthspan queries still missed Niagen Plus and Lifeforce.
- The raw scorer intentionally does not open list pages, so it is stricter than the earlier manual
  WebSearch/page-enumeration receipt. That limitation is not an excuse to pass; it says the next
  packet should make page extraction explicit rather than relying on snippets.

## Conversation Intelligence Result

External-only retrieval:

- Top-10 overlap: 7/10.
- Misses: Loom, Dovetail, AlphaSense.

Store-first retrieval:

- Top-10 overlap: 9/10.
- Miss: Loom.
- Store baseline supplies Gong, Clari, Granola AI, Dovetail, and AlphaSense.

Adjacent pollution:

- AssemblyAI surfaced as an adjacent transcription-dev tool.
- It is boundary-labeled in scoring, not treated as a core promotion.

Interpretation:

This rerun confirms the previous receipt: conversation intelligence is the better evidence for the
store-first union shape, but the benchmark still mixes company-profile targets with product/workflow
rows. The scoring layer should keep those lanes separate before any reusable verb graduates.

## Decision Impact

Do not graduate `/cohort-discovery` from this packet.

The implementation is improved because the rerun is now reproducible and scored from frozen inputs.
The value claim did not improve. Follow-on work should use the candidate-filtering synthesis:
keep page extraction, add agent-led qualification plus usefulness judgment, and score discovery
recall separately from filter recall rather than another broad telehealth prompt pass.
