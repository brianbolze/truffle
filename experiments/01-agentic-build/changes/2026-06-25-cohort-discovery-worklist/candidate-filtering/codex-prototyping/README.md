# Codex Prototyping: Candidate Qualification

Status: packet-local Codex evidence only; do not treat as durable Truffle design.

## Start Here

Read in this order:

1. `codex_claude_comparison_summary.md`
2. `codex_claude_comparison_results.json`
3. `codex_capture_readiness_summary.md`
4. `codex_capture_readiness_results.json`
5. `codex_boundary_resolution_summary.md`
6. `codex_boundary_resolution_results.json`
7. `codex_handoff_next_session.md`
8. `codex_candidate_qualification_v2.py`
9. `codex_v2_candidate_cards.json`

Read V1 only when comparing baselines.

## Current Read

The latest Codex pass compares Codex capture-readiness output against Claude's independent qualifier on the same 61 rows. It joins by cohort + resolved domain, treats `existing_profile` vs Claude `capture` as store-awareness alignment, and turns route disagreements into a proposed final route surface.

The useful result is the calibration split:

- both lanes agree that source/publisher artifacts should not become captures;
- Claude is more willing to capture owned in-cohort offerings;
- Codex is more conservative around adjacent tools, local clinics, and broad health giants;
- the merged proposal is 21 `capture_ready`, 19 `existing_profile`, 11 `cohort_fit_review`, and 10 `preserve_source_evidence`.

The previous Codex pass is capture readiness over boundary-resolution output. It starts only from rows boundary resolution routed as `capture_candidate` or `existing_profile`, then asks whether full `/research-company` capture is more useful than preserving source evidence plus a lightweight card.

That result split:

- existing store profiles stay distinct from new capture-ready candidates;
- homepage confirmation proves existence, not capture-worthiness;
- owned `best X` / `alternatives` pages remain biased source evidence and do not count as neutral third-party proof;
- adjacent tools/platforms and local/offline clinics move to review or source preservation instead of capture.

The prior Codex pass is boundary resolution over V2 output. It tested a bounded evidence ladder:

- store baseline;
- direct homepage checks;
- focused SerpAPI for high-value name-only cases;
- Firecrawl homepage fallback when direct fetch was insufficient.

The useful result is not "make a capture queue now." It is the split:

- owned `best X` / `alternatives` listicles are biased source evidence, not automatic publisher disqualification;
- homepage confirmation proves an official company surface, not capture-worthiness;
- capture readiness still needs a usefulness / cohort-fit gate.

## Artifacts

| Artifact | Role |
| --- | --- |
| `codex_candidate_qualification_prototype.py` | V1 deterministic baseline; explains why source-role routing was too conservative. |
| `codex_candidate_cards.json` | V1 card output. |
| `codex_qualification_eval.json` | V1 evaluation output. |
| `codex_qualification_summary.md` | V1 summary. |
| `codex_candidate_qualification_v2.py` | V2 active card/routing fixture; kind before route, qrels only after routing. |
| `codex_v2_kind_examples.json` | V2 packet-local kind examples. |
| `codex_v2_candidate_cards.json` | V2 boundary-review input for the resolver. |
| `codex_v2_qualification_eval.json` | V2 evaluation output. |
| `codex_v2_qualification_summary.md` | V2 summary. |
| `codex_boundary_resolution.py` | Latest Codex prototype; resolves V2 boundary rows with bounded evidence. |
| `codex_boundary_resolution_results.json` | Boundary-resolution results and evaluation. |
| `codex_boundary_resolution_summary.md` | Boundary-resolution human readout. |
| `boundary-resolution-cache/` | Live evidence receipts; keep with the prototype. |
| `codex_capture_readiness.py` | No-spend usefulness gate over boundary-resolution `capture_candidate` / `existing_profile` rows. |
| `codex_capture_readiness_results.json` | Capture-readiness results, evidence snapshots, caveats, and post-route qrel evaluation. |
| `codex_capture_readiness_summary.md` | Capture-readiness human readout and route counts. |
| `codex_claude_comparison.py` | Joins Codex readiness rows to Claude routed output and proposes final routes for disagreements. |
| `codex_claude_comparison_results.json` | Full Codex-vs-Claude row comparison with proposed final routes. |
| `codex_claude_comparison_summary.md` | Disagreement-first comparison readout. |
| `codex_handoff_next_session.md` | Next-session handoff and recommended next slice. |

## Next Slice

Do not restart from all candidates. Next useful work is either:

- run a downstream usefulness test on the proposed `capture_ready` rows; or
- agent-review the merged `cohort_fit_review` rows and decide whether any deserve manual promotion/demotion before proposing a durable design.

Do not update `store/`, schema, `tools/`, `skills/`, or durable docs from this prototype alone.
