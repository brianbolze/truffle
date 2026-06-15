# FRAME — Agentic visual-quality judgment for websites

Date: 2026-06-13 · Status: problem frame (not system design). Aligns on the destination before the first graduated module is built.

## 1. Working Title

**Visual-quality judgment from screenshots** — can an agent reliably help judge how good a website *looks*, using only visible evidence and a calibrated rubric?

## 2. Short Answer

The destination is reusable visual-quality judgment over time. But the work splits cleanly into two layers, and only one is ready:

- **Evidence mining (perception)** — *what is visibly on the page* — works. Five runs show agents reliably name concrete visual tells (template slop, stock clichés, clip-art icons, render defects, real craft) with cited screenshots. This is **State-like** and graduatable.
- **Scoring (pricing)** — *how good that adds up to* — does not yet. Models carry a persistent upward calibration offset and still misprice the business-critical cases. This is **Judgment-like** (viewer-relative) and stays experimental.

**Graduate the evidence layer first. Keep scoring as a future experiment until calibration proves out.**

## 3. Problem Statement

Competitive and creative work constantly asks a visual question — *does this site look polished, formidable, basic, or amateur?* Today that read is manual, unrepeatable, and locked in one person's head. We want an agent to produce that read from captured screenshots: reliably, with its reasoning visible, against a rubric that can be tuned rather than re-argued each time.

The hard part isn't getting a model to emit a number. It's getting a number we'd *trust* — one that tracks a taste-calibrated human within tolerance, and fails safe when it can't.

## 4. Why This Matters

- **It's a recurring, expensive-to-repeat judgment.** Every competitor look-over re-derives the same visual read from scratch. A reliable evidence layer makes it cheap and consistent.
- **It feeds the human-facing brief.** The brief's first external consumer (a creative director) values visual/brand signal and judges "does this land in 5 seconds." A `Visual & brand impression` grounded in cited evidence is directly useful — even with no score attached.
- **It builds a calibration asset.** Evidence cards accumulate into a reusable library of "what strong vs. weak looks like" — the substrate any future scoring would need anyway.
- **The failure cost is asymmetric.** A miscalibrated score that reads template slop as "strong" would actively mislead any gate built on it. Shipping evidence without a trusted score is honest; shipping a confident wrong score is not.

## 5. Long-Term Capability Goal

A reusable visual-quality module that, given clean captured screenshots of a site, can:

1. **Mine** falsifiable visual evidence (cited tells across typography, layout/components, color/brand/imagery, iconography/graphics). — *ready*
2. **Prune** that evidence to what's real, deduped, and artifact-free. — *ready, with a known over-pruning risk*
3. **Score** the site against a calibrated rubric, reliably enough to trust without a human re-checking each one. — *future*
4. **Stay tunable** — rubric anchors and weights adjustable without re-running models, with calibration measured against ground truth, not eyeballed.

"Reliable" has a specific meaning here (see Principles): it means *tracks a defined bar within tolerance and degrades to evidence-only when it can't* — not *objectively correct*.

## 6. Primary Use Cases

- **Brief enrichment** — a cited visual/brand impression **+ a curated specimen strip** (a few tiles selected via the cards) for the human-facing handoff. *Needs only the evidence layer.*
- **Calibration library** — accumulated strong/weak exemplars for tuning future judgment and onboarding new raters.
- **Competitor visual reads at scale** — consistent look-overs across a cohort without manual re-derivation.
- **Execution-quality signal for formidability reads** — the evidence feeds a *consumer-side* judgment of company formidability ("does this company execute well?") as one signal alongside funding, SEO presence, catalog breadth, etc. The engine supplies the signal; the project makes the call (consistent with Non-Goals §11). Same downstream consumer as the adaptive-capture-depth frame.
- **(Future) quality scoring** — a tunable rubric score, once calibration is trusted.
- **(Future, consumer-owned) decision gates** — e.g. depth-gating a capture. The depth-gate never needed a *score* — it's a Judgment of its own ("how much does this company matter to me"), framed separately in the forthcoming adaptive-capture-depth frame. This layer *feeds* that gate one cheap signal (a homepage-glance "real company or template slop?"); it doesn't own it. Don't build scoring to serve it.

## 7. What Makes This Hard

Each is documented across v1–v5, not speculative:

- **Calibration offset.** Models anchor "coherent professional template" ~1–2 buckets high — they rate against *all websites* (where a working template beats the median), not against the contemporary DTC/health bar. `weak` was never once issued, even on sites that earn it. Rule-tightening has hit its ceiling; the anchors themselves are off.
- **Seduction patterns.** *Distinctive ≠ well-executed* (Pepti's ambition; Geviti's atmosphere) and *gloss reads as art direction* (Infusive's dark-SaaS gradient scored `excellent` against a human's 2.5). The seductive cases are exactly the ones the module must price correctly.
- **Capture fidelity is a prerequisite, not a detail.** Modals, cookie banners, grey/blank heroes, black media cards, lazy-load gaps, and full-page compositing artifacts all contaminate evidence. Worse, full-page screenshots downsample ~7× at read time and hide the very defects that matter (amateur charts, clip-art icons). Native-resolution tiling and a screenshot-QA gate are mandatory upstream.
- **Ground truth is one person's taste, and it drifts.** The bar is subjective (±1 re-look drift is normal) and not an objective measure. This caps what "reliable" can ever mean and forces tolerance-band evaluation, not exact-match.
- **The pruning trade-off.** A judge strict enough to kill generous mixed claims can also strip real evidence from clean conventional sites (Nurx, Hallandale under-rewarded in v5). Perception and pruning pull against each other — and clean-conventional is the *modal* case in a DTC/health corpus, so this failure lands on the bulk of real captures, not the margins. Fix it before graduating, not after.
- **The bottom boundary is under-tested.** Scoring collapses the whole weak band into one value; the `1`/`weak` floor has never been exercised.

## 8. Principles

- **Capture hygiene before judgment.** Screenshot QA is phase 1, not cleanup. A page with a modal or broken hero is *unusable evidence*, not a poor-design example. Split capture status from design judgment.
- **Evidence before verdict.** Small, falsifiable cards — one visible tell, one cited tile — beat whole-site vibes. The card library is the durable asset; the verdict is a lens over it.
- **Blind the judge.** No ratings, dossiers, prior labels, profile prose, Notion, or live web leaking into perception or scoring. Reputation contaminates the read.
- **Separate perception from pricing.** They are different layers with different reliability. The whole graduation decision rests on not collapsing them.
- **Default down; generic is common.** Coherent-but-conventional is the median, not high quality. Distinctiveness is not maximalism.
- **Map to the engine's State/Judgment line.** Observable visual evidence ≈ **State** (what the page *is*) → engine-ownable. A quality score ≈ **Judgment** (what it's *worth*, relative to the viewer) → consumer-owned until proven reliable. The graduation boundary is the engine's own boundary.
- **"Reliable" = tracks the bar within tolerance, and fails safe.** When confidence is low or capture is degraded, return evidence and abstain from a score — never emit a confident guess.

## 9. What We Think We Know

### What we know

Strongly supported by the v1–v5 runs:

- Agents **perceive** visual quality accurately — they name the right tells with cited evidence, even when they misprice them.
- **Screenshot QA must precede** any fanout; contaminated evidence poisons everything downstream.
- **Native-resolution tiles** surface defects that full-page downsampling hides.
- **Blinding is achievable and matters** — evidence and scores hold up when reputation is withheld.
- **Relative ordering and discrimination are good**, and **inter-rater agreement is tight** (≤1-bucket spread). The scale separates sites; its absolute anchors are what's wrong.
- Scoring carries a **persistent upward calibration offset** that rule-tightening alone does not fix. Even v5's best run (8/13 exact, 13/13 within one, no two-bucket misses, no top-tier false positives) still over-rewarded the ambitious-but-inconsistent (Pepti) and generic-but-coherent (Belmar) cases, and over-pruning under-rewarded clean conventional sites.

### What we suspect (unproven)

- **Deterministic caps on top of pruned evidence** could close the residual offset (v5 proposal — untested).
- **Anchored/comparative placement** ("place against these labeled references") may beat absolute rating — comparative judgment is more reliable for humans and models alike (v3 proposal — never run at scale).
- **Decomposing into binary cue-detection + deterministic, re-tunable scoring** could make scoring auditable and fixable without re-running models (v4 design — never launched).
- A **second positive-evidence retrieval pass** for clean conventional sites could fix the over-pruning underreward (v5 proposal — untested).

None of these has cleared the bar. Scoring stays future/experimental.

## 10. Initial Scope Implication

The first graduated module is narrow on purpose: **the evidence layer only.**

- Capture-QA gate → cleaned/blinded manifest → family evidence mining → judge/prune → **evidence-card output** for a human or a later deterministic step.
- Output shape is cited, falsifiable cards (+ optional prose impression for the brief) — **no autonomous score, no frontmatter quality field, no decision gate** treating a score as ground truth.
- Scoring continues as a *separate experiment track* against the frozen 124-site ground-truth snapshot, using the suspected-but-unproven levers above. It graduates only on its own evidence.

## 11. Non-Goals

- **Not** scoring company legitimacy, threat, fit, or formidability — those are the consumer's Judgments, not the engine's.
- **Not** judging clinical/regulatory quality, truth of claims, or business strength.
- **Not** SEO, traffic, funding, or headcount — those are Signals (time-axis), a different layer.
- **Not** copy quality, IA/navigation, or UX flow — a different axis from visual presentation.
- **Not** CMS/framework/code quality.
- **Not** a live-web audit — judgment runs on captured screenshots, after QA.
- **Not** mobile/responsive or interaction quality yet — desktop screenshots only to date.
- **Not** an autonomous quality gate. Today's output informs a human; it does not decide.

## 12. Open Questions

1. **Can the scoring offset actually be killed**, or is "evidence + human-priced verdict" the honest permanent shape? (The decisive question.) Before chasing the offset, name the consumer who needs a *number* — both consumers today (human judgment via the brief; relative triage, which already orders well) are served without one.
2. **Which lever first** — deterministic caps, anchored comparison, or cue-detection + deterministic scoring? They're not mutually exclusive; what's the cheapest decisive test?
3. **Where does the evidence layer live** — inside `/research-company` capture, a sibling preset, or an offline helper over cached artifacts?
4. ~~**What's the output contract** — pure cards, prose impression, both?~~ **Resolved (shipped `b710aeb`):** the brief renders the prose **impression** (its primary deliverable) + a **curated specimen strip** in the Brand system tab — a few tiles selected *via* the cards (cards as the curation index; their one-line claims become captions). The raw card records stay the audit trail, never rendered.
5. **How is calibration re-measured over time** as the ground-truth bar drifts (±1 re-look) and as cohorts change?
6. **Does a single-rater taste bar generalize**, or does any reliable score stay personal to its rater?

## 13. Proposed Decision

**Frame the long-term destination as visual-quality judgment — but graduate only the evidence-mining layer first, unless future calibration proves scoring is reliable.**

- Ship the evidence layer (capture-QA → blinded mining → prune → cited cards) as the first reusable module. It's State-like, proven, and immediately useful to the brief.
- Hold scoring as an explicit experiment track against frozen ground truth. It graduates only when it tracks the bar within tolerance *and* stops mispricing the seductive cases — measured, not eyeballed.
- Until then, never emit a standalone visual-quality score as if it were ground truth, and never gate a downstream decision on one.

---

**Recommendation:** the destination is reliable visual-quality judgment; the first step is evidence, not scores. Build the layer that works, keep proving the layer that doesn't.
