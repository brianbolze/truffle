# Lead-only evaluation

Date: 2026-06-13

## Blinding Check

Evidence agents, judge, and scorer received only:

- `WORKER_PROTOCOL.md`
- `cleaned-tile-manifest.md`
- `CAPTURE_QA.md`
- raw evidence outputs for the judge
- pruned evidence for the scorer

They were not given Brian/reference ratings, prior anchor notes, expected high/mid/low
labels, company dossiers, `profile.md`, Notion, live web, or prior scoring findings.

Reference anchors below come from the lead session after blind scoring, chiefly the
anchor notes in the prior 2026-06-13 tile manifest and the earlier calibration runs.

## Comparison Method

Blind PQR-lite uses a 1-5 scale. Brian/reference anchors were originally 1-10
snapshots, so this comparison uses a coarse bridge:

- 9-10 -> 5
- 7-8 -> 4
- 5-6 -> 3
- 2-4 -> 2

This is not a claim of exact equivalence. It is enough to detect one-bucket misses
and known false-positive traps.

## Results

| Site | Reference snapshot | Expected PQR-lite | Blind PQR-lite | Delta | Read |
|---|---:|---:|---:|---:|---|
| Function Health | 10 | 5 | 5 | 0 | Match. |
| Ro | 8 | 4 | 4 | 0 | Match. |
| Nurx | 7 | 4 | 3 | -1 | Conservative miss; judge pruned all Nurx cards, so scorer defaulted to generic competence. |
| Hallandale | 8 | 4 | 3 | -1 | Conservative miss; product grid recognized, broader sparse brand system held it down. |
| Geviti | 7 | 4 | 3 | -1 | Conservative but defensible; avoided prior overreward for distinctive atmosphere. |
| Amble | 7 | 4 | 4 | 0 | Match, but still close to the overreward boundary. |
| Pepti | 6 | 3 | 4 | +1 | High; ambition and polished app graphics still pull it upward. |
| Belmar | 4 | 2 | 3 | +1 | High; coherent corporate healthcare template still overcredited. |
| Mills | 4 | 2 | 2 | 0 | Match. |
| Jinfiniti | 3 | 2 | 2 | 0 | Match. |
| Kingsberg | 2 | 2 | 2 | 0 | Match. |
| Anazao | 2 | 2 | 2 | 0 | Match. |
| Infusive | 2.5 | 2 | 2 | 0 | Match; the dark-gradient trap was capped correctly. |

Summary:

- Exact coarse matches: 8/13.
- Within one PQR-lite point: 13/13.
- No two-point misses.
- No `5` false positives.
- Known false-positive traps improved but did not disappear.

## What Improved

- Infusive was no longer seduced upward by dark SaaS gloss. The scorer held it at 2
  because typography noise, heavy effects, and a tab/content collision capped the
  site.
- Mills, Jinfiniti, Kingsberg, and Anazao landed in the weak band rather than being
  treated as merely solid.
- Function and Ro landed where expected.
- The score rationales cited visible evidence instead of general reputation or copy.

## What Still Failed

- Pepti remains high by one. The scorer acknowledged the overpowered neon-acid
  palette, but still gave overall 4 because typography, catalog cards, and app/mockup
  systems looked polished in the pruned evidence.
- Belmar remains high by one. The judge pruned some generic Belmar praise, but the
  scorer still treated competent corporate execution as a 3 rather than a 2.
- Nurx and Hallandale were low by one. This is the opposite error: the pruning pass
  removed or failed to retain enough positive evidence for conventional but genuinely
  polished sites.
- The scorer did not use score `1`. That may be acceptable for this cohort if `1`
  means broken/amateur, but it means the bottom boundary remains under-tested.

## Interpretation

The V5 pipeline is better than prior absolute-rating runs. Capture QA plus native
tiles plus judge pruning reduced the large upward offset and killed the Infusive
false positive.

But blind scoring is still not stable enough to graduate as an autonomous quality
score. The remaining errors are exactly the business-critical ones:

- ambitious-but-inconsistent sites can still be overrewarded,
- coherent generic templates can still be overrewarded,
- pruning can remove too much evidence for clean conventional sites.

The evidence-mining layer is more trustworthy than the scoring layer.
