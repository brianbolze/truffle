# Codex Handoff: Candidate Qualification Next Session

Date: 2026-06-26
Status: updated after Codex-vs-Claude comparison; no engine changes made

## Current Short Take

Start with `README.md`, then the Codex-vs-Claude comparison:

- Script: `codex_claude_comparison.py`
- Results: `codex_claude_comparison_results.json`
- Summary: `codex_claude_comparison_summary.md`

The comparison joins the 61 Codex capture-readiness rows to Claude's routed output by cohort + resolved domain. It found:

- 19 direct aligned rows
- 15 store-awareness alignments (`existing_profile` vs Claude `capture`)
- 1 duplicate-handling alignment
- 1 source-vs-store split (TRT Nation: existing profile, but the specific listicle evidence should be preserved)
- 4 rows missing from Claude's routed set
- 21 adjudicated disagreements

Merged proposed final routes:

- 19 `existing_profile`
- 21 `capture_ready`
- 11 `cohort_fit_review`
- 10 `preserve_source_evidence`

By cohort:

- Conversation intelligence: 17 capture-ready, 5 existing, 6 fit-review, 3 preserve-source.
- Telehealth: 4 capture-ready, 14 existing, 5 fit-review, 7 preserve-source.

Read: both lanes agree on the shape. Claude is more willing to capture owned in-cohort offerings; Codex is more conservative around adjacent tools, local clinics, and broad health giants. The merged surface is useful enough for the next decision, but still prototype guidance, not durable design.

Prior pass: capture readiness:

- Script: `codex_capture_readiness.py`
- Results: `codex_capture_readiness_results.json`
- Summary: `codex_capture_readiness_summary.md`

This no-spend gate starts only from boundary-resolution rows already routed as `capture_candidate` or `existing_profile`. It turns 61 rows into:

- 19 `existing_profile`
- 22 `capture_ready`
- 14 `cohort_fit_review`
- 6 `preserve_source_evidence`
- 0 `reject_or_defer`
- 0 `boundary_review`

By cohort:

- Conversation intelligence: 17 capture-ready, 5 existing, 7 fit-review, 2 preserve-source.
- Telehealth: 5 capture-ready, 14 existing, 7 fit-review, 4 preserve-source.

Acceptance checks passed: no source/listicle/directory artifact was capture-ready, no homepage-only row was capture-ready without usefulness reasons, and existing store profiles stayed distinct.

Prior pass: boundary resolution:

- Script: `codex_boundary_resolution.py`
- Results: `codex_boundary_resolution_results.json`
- Summary: `codex_boundary_resolution_summary.md`
- Cache: `boundary-resolution-cache/`

It shrank V2 boundary review from 297 rows to 206 rows without promoting source-like artifacts or known bad/boundary rows into capture.

The key lesson is Brian's gotcha: **owned `best X` / `alternatives` listicles are biased source evidence, not automatic publisher disqualification.** Resolve the publisher domain through store/homepage evidence before deciding whether it is a real company target.

The second lesson is equally important: **homepage confirmation proves "real company surface," not "capture-worthy."** Capture readiness now applies that gate, but treat it as prototype evidence rather than design truth.

## Previous Short Take

The next slice should run the candidate-qualification system end to end with a controlled uncertainty budget.

V2 showed that the right shape is:

1. build qrel-free evidence cards;
2. classify kind before route;
3. preserve source/listicle evidence separately;
4. send ambiguous company/product/source cases to `boundary_review`;
5. use qrels only after routing for evaluation.

What remains unproven is whether the system can resolve boundary cases cheaply enough to improve capture readiness without turning into an open-ended crawler.

## Current Artifacts

- V1 deterministic prototype: `codex_candidate_qualification_prototype.py`
- V1 outputs: `codex_candidate_cards.json`, `codex_qualification_eval.json`, `codex_qualification_summary.md`
- V2 Doro-shaped prototype: `codex_candidate_qualification_v2.py`
- V2 example set: `codex_v2_kind_examples.json`
- V2 outputs: `codex_v2_candidate_cards.json`, `codex_v2_qualification_eval.json`, `codex_v2_qualification_summary.md`
- Boundary-resolution prototype: `codex_boundary_resolution.py`
- Boundary-resolution outputs: `codex_boundary_resolution_results.json`, `codex_boundary_resolution_summary.md`
- Boundary-resolution live cache: `boundary-resolution-cache/`
- Capture-readiness prototype: `codex_capture_readiness.py`
- Capture-readiness outputs: `codex_capture_readiness_results.json`, `codex_capture_readiness_summary.md`
- Codex-vs-Claude comparison: `codex_claude_comparison.py`
- Comparison outputs: `codex_claude_comparison_results.json`, `codex_claude_comparison_summary.md`

V2 is useful only as a baseline fixture. Boundary resolution, capture readiness, and the Codex-vs-Claude comparison are prototype evidence, not final design.

## Fresh-Session Read Order

1. `README.md`
2. `codex_claude_comparison_summary.md`
3. `codex_claude_comparison_results.json`
4. `codex_capture_readiness_summary.md`
5. `codex_capture_readiness_results.json`
6. `codex_boundary_resolution_summary.md`
7. `codex_boundary_resolution_results.json`
8. `codex_candidate_qualification_v2.py`
9. `codex_v2_candidate_cards.json`
10. `codex_v2_qualification_summary.md`
11. `codex_v2_kind_examples.json`

Only read V1 (`codex_candidate_qualification_prototype.py` and `codex_qualification_summary.md`) when comparing baselines or explaining why deterministic source-role routing was rejected.

## What V2 Proved

- Source/listicle/publisher artifacts stayed out of `capture_candidate`.
- Known bad/boundary rows were not promoted to capture.
- Domainless conversation-intelligence brands such as Gong, Granola, Fathom, Clari, and Otter moved to `boundary_review` instead of false reject.
- The shared kind/route menu worked across telehealth and conversation intelligence.

## What V2 Did Not Prove

- It did not verify homepages or official domains.
- It did not spend credits, run fresh SerpAPI/Exa, or fetch new source pages.
- It did not decide which boundary cases truly deserve capture.
- It did not test a full capture queue with acceptance criteria.
- It did not replace model/agent adjudication; the classify-by-example logic is a proxy for the result shape.

## Boundary Resolution Result

- Input boundary rows: 297.
- Output routes: 42 `capture_candidate`, 19 `existing_profile`, 17 `preserve_source_evidence`, 13 `reject_or_defer`, 206 still `boundary_review`.
- Conversation intelligence: 36/106 boundary rows resolved; 26 capture candidates, 5 existing profiles.
- Telehealth: 55/191 boundary rows resolved; 16 capture candidates, 14 existing profiles.
- Acceptance checks: source-like capture = 0; known bad/boundary promoted = 0.
- Total live cache footprint from the prototype: 47 direct homepage records; 5 SerpAPI records / 5 credits; 10 Firecrawl records / 10 credits.

Important caveat: many capture candidates are "official domain confirmed" only. They are not yet "worth full profile capture."

## Recommended Next Slice

Do not add more routing heuristics yet. The merged comparison is good enough to test usefulness.

Recommended next move: run a downstream synthesis usefulness test on the proposed 21 `capture_ready` rows. Ask whether adding these profiles would materially improve cohort reads like pricing, positioning, offer structure, or source-attested alternatives. Promote only the first small batch that clearly improves those reads.

If continuing inside this lane instead, agent-review the merged `cohort_fit_review` rows rather than all candidates:

- promote only rows where full capture clearly improves neighborhood/cross-company synthesis;
- demote rows where owned SEO/listicle evidence is doing most of the work;
- keep existing profiles and duplicate capture-ready domains distinct.

Do not turn the prototype route menu or regexes into durable Truffle design without a proposal/review pass.

## Previous Recommended Slice

Start from `boundary_review` candidates, not all candidates. For each boundary item, allow a small escalation ladder:

1. **No-spend local check:** use existing candidate card, source rows, outbound links, and store baseline.
2. **Cheap homepage peek:** fetch or scrape the candidate homepage only when there is a candidate domain or a strong inferred domain.
3. **Focused SerpAPI query:** only for domainless high-value names or ambiguous brand/source collisions.
4. **Optional Firecrawl scrape:** only when direct fetch is blocked or homepage content is needed to resolve kind.

The output should not be full company capture. It should be an updated qualification result:

```text
kind
route
confidence_band
method
evidence_added
spend
alternatives
reasons
caveats
```

## Acceptance Shape

Evaluate after routing, not during routing.

- Source/listicle artifacts in `capture_candidate`: target `0`.
- Known bad/boundary rows promoted to capture: target `0`.
- Telehealth known relevant preserved as capture or boundary: should improve over V2.
- Conversation-intelligence top-core targets should remain in boundary/capture, not reject.
- Boundary queue should shrink meaningfully after homepage/SERP resolution.
- Every spend action should be attributable to a candidate and a reason.

## Spend Guardrail

Use an explicit per-run spend cap before any live calls.

Suggested first cap:

- SerpAPI: at most 10 focused queries.
- Firecrawl: at most 10 homepage scrapes.
- Direct HTTP: okay for candidate homepages, but cache outputs packet-locally.

Stop if source/publisher artifacts enter capture, if the boundary queue mostly remains unresolved, or if resolving one candidate requires multi-step browsing beyond the cap.

## Older Packet Context

Use these only if the next session needs packet-wide context beyond the Codex lane:

- `../candidate-qualification-fresh-session-brief.md`
- `../../decision-surface.md`
- `../../receipts/page-extraction-probe.md`
- `../../reference/doro-candidate-qualification-notes.md`

Do not start from the parked mini-proposal. Treat V2 and boundary resolution as prototype evidence, not final design.

## Cleanup Recommendation

Do not archive V1/V2 yet.

Keep V1 because it documents the deterministic baseline and why V2 exists. Keep V2 outputs because they are the fixture for the boundary-resolution pass. Keep `boundary-resolution-cache/` because it is the live-evidence receipt. Defer updates to broader docs, schemas, tools, skills, and store paths until the merged comparison is reviewed.
