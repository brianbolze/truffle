# V5 findings

Date: 2026-06-13

## Bottom Line

Graduate **visual evidence mining**, not blind PQR-lite scoring yet.

V5 materially improved the workflow: screenshot health was handled first, Function
homepage was restored correctly from browser viewport tiles, evidence cards were
blind, and scoring cited visible evidence. The blind score ranking was directionally
useful and avoided the worst prior failure on Infusive.

But the scoring layer still has two live calibration risks:

- Pepti was overrewarded for ambitious/polished visual systems despite inconsistency.
- Belmar was overrewarded for competent generic corporate healthcare execution.

Those are not harmless misses; they are exactly the cases this module must price
correctly.

## What Ran

- Built a new blinded cleaned manifest:
  - `cleaned-tile-manifest.md`
  - `cleaned-tile-manifest.json`
- Added Function Health homepage from verified browser viewport tiles.
- Audited screenshot health in `CAPTURE_QA.md`.
- Excluded one contaminated active tile:
  - Hallandale homepage `tile-02-y02440.png`, due to a large blank grey media frame.
- Ran four blind GPT-5.5 evidence agents:
  - typography / hierarchy
  - layout / composition / components
  - color / brand / imagery
  - iconography / illustration / product graphics
- Ran a blind judge/pruning pass.
- Ran a blind PQR-lite scoring pass after pruning.
- Compared scores to hidden/reference anchors only in the lead session.

## Evidence Output

Raw evidence:

- 48 raw cards across four families.
- All raw card tile paths validated against active manifest paths.
- No excluded tile citations.

Pruned evidence:

- 37 accepted cards.
- 11 rejected cards.
- The judge note says 36 cards, but the structured YAML contains 37 accepted cards.
- Accepted cards remained path-valid.

Useful retained examples:

- Function: strong typography, layout, color, and medical graphics.
- Ro: strong components/product graphics, mixed generic/assembled imagery.
- Geviti: distinctive but busy and under-systematized.
- Pepti: strong app/catalog systems, but color/product evidence tension.
- Infusive: cohesive software graphics capped by noisy type and layout collision.
- Jinfiniti: sticky chrome and mixed product/science graphics.
- Mills/Kingsberg/Anazao: weak foundations with visible tells.

## Blind Scoring Result

Overall PQR-lite ranking:

| Site | Blind overall |
|---|---:|
| Function Health | 5 |
| Pepti | 4 |
| Ro | 4 |
| Amble | 4 |
| Geviti | 3 |
| Nurx | 3 |
| Hallandale | 3 |
| Belmar | 3 |
| Infusive | 2 |
| Jinfiniti | 2 |
| Kingsberg | 2 |
| Anazao | 2 |
| Mills | 2 |

Post-hoc anchor comparison:

- 8/13 exact under the coarse 1-10 to 1-5 bridge.
- 13/13 within one point.
- No two-point misses.
- No top-tier false positives.
- Infusive was correctly capped at 2.

## Pass Bar Check

- Clean active screenshots or explicit exclusions: pass.
- Function homepage restored only from verified viewport tiles: pass.
- Every dimension score backed by cited evidence: pass, validated by script.
- Generic-but-polished sites not overrewarded: partial fail. Belmar stayed high by
  one.
- Ambitious-but-inconsistent sites not overrewarded: partial fail. Pepti stayed high
  by one.
- Scoring/ranking blind: pass.
- Post-hoc agreement useful: pass directionally, fail as autonomous scoring.

## What This Means

The reusable module should be:

1. Capture QA gate.
2. Cleaned/blinded manifest builder.
3. Family evidence mining.
4. Judge/prune pass.
5. Evidence-card output for downstream human or deterministic review.

Do not yet graduate:

- a standalone blind PQR-lite score,
- an automatic frontmatter field,
- a downstream decision gate that treats score as ground truth.

## Remaining Risks

- The judge can prune away too much evidence for clean conventional sites, which
  undercut Nurx and Hallandale.
- The scorer still prices some polished ambition as `4` when the reference anchor
  expects `3`.
- Generic corporate coherence still wants to settle at `3` unless the prompt or a
  deterministic cap forces it down.
- The `1` score boundary remains untested; the scorer used `2` for the whole bottom
  band.

## Recommendation

Graduate option **1: visual evidence-mining module only**.

Next smallest scoring experiment:

- Keep the V5 capture/evidence/prune pipeline.
- Add deterministic cap rules on top of pruned cards:
  - no overall `4` without accepted positive evidence in at least three families and
    no accepted generic/template cap card,
  - coherent corporate template defaults to `2` unless distinct craft evidence is
    retained,
  - ambitious visual systems need both component finish and brand-system coherence
    to reach `4`,
  - if judge pruning removes all evidence for a known-clean conventional site, require
    a second positive-evidence retrieval pass before scoring.

The scoring layer is close enough to keep testing, but not ready to trust.
