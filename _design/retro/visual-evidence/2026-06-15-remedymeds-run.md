# Retro — Remedy Meds visual-evidence run (2026-06-15)

Fourth `/visual-evidence` run (`remedymeds-com`). Landed clean: [`store/remedymeds-com/visual.md`](../../../store/remedymeds-com/visual.md), 33 cards, lint exit 0, `qa_status: exclusions-noted`. No Tier-B — all five cached pages rendered clean.

## Lesson 1 — the "judge under-prunes, curate to ~16" rule may be solving the wrong problem

Blokes and Good Life both concluded: judge over-accepts vs. the 8–14 contract target, so hand-curate down and add a hard count ceiling to the prompt. This run: 49 raw → judge accepted **34** (~69%), same ceiling pattern, third data point.

But I went the other way — **kept 33, did not curate to 14.** Reason: the seed exemplar the contract itself cites ([`goinfusive-com/visual.md`](../../../store/goinfusive-com/visual.md)) has **~38 cards**. So the de-facto gold standard is a *comprehensive audit trail*, and the "8–14 typical" line in VISUAL.md contradicts the one instance everyone is told to match. Before we build a hard ceiling into the judge prompt, resolve that: **is the deliverable a tight card set, or a tight impression over a comprehensive card set?** I read it as the latter (cards = falsifiable drill-down; impression = the ~5-sec glance), which fits Brian's two-zoom-level preference. If that's right, the prior two retros' fix is premature and the contract's number is the bug. Worth settling before the experiment — otherwise we'll tune the judge toward a target that may be wrong.

## Lesson 2 — the judge misses mid-animation; the human QA driver is the backstop

Judge accepted a `poor` "garbled overlapping text" layout card on `homepage/tile-04`. I pulled the native tile: settled top row, **double-rendered bottom row, cards mid-flight, blank "verified" icon** — a staggered reveal caught mid-animation, exactly the capture caveat the contract says must never become a `poor` design card. The blind miner can't tell artifact from defect by construction, and the judge (also blind) inherited the miss. Dropped it at write time → 33. **The QA-gate vision pass before *and* a spot-check of any `poor` structural card after the judge is load-bearing** — the workflow can't self-catch this. Didn't Tier-B re-render: the region isn't load-bearing (component discipline already covered by clean tiles), so re-shooting a page for one card was unwarranted (consistent with Blokes' "Tier-B is overreach for non-load-bearing artifacts").

## Confirms / minor

- **Path duality (recurs, 4th time).** Workflow runs in project cwd; miners need absolute tile paths; rewrite to repo-relative when authoring. This belongs in SKILL.md now — it's bitten every run.
- **Lint gotcha for programmatic authoring.** Generated the YAML via script and single-quoted the `id` — `visualcheck` captures id via `\S+`, so `'typography_01'` kept its quotes and the impression's `[typography_01]` citation didn't match. Emit `id` unquoted; quote everything else. One-line fix, but anyone scripting card generation will hit it.

## Net

Output: calibrated, marketing-vs-utility-page split reads true (skews `strong` because the marketing pages genuinely are well-built). Process: clean, but surfaced the real open question — the card-count target itself, not the judge's adherence to it.
