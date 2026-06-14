# FRAME — External traction signals for companies

Date: 2026-06-14 · Status: problem frame (not system design). Graduates the parked **Traction module / verb** ([BACKLOG](../BACKLOG.md)). Solution shape is deliberately out of scope.

## Short answer

The engine answers *"what is this company?"* well — a cited **State** snapshot. It can't yet answer *"how is it **doing**?"* — growing, winning its category, formidable, fading. That's a different kind of fact: external, time-axis, often comparative. The repo already names it **Signals** and flags it a first-class *future*. This frame defines the problem.

- **Two consumers.** Per-company **competitor triage** ("formidable rival?") and cohort **market maps** (crowdedness / dominance / hotness).
- **Split like visual-quality.** Graduate the cited, axis-specific **evidence layer**; hold the viewer-relative **"formidable?" verdict** as a consumer-owned future. *No blend.*
- **Reuse what exists.** Six `tools/` already capture raw signal. The gaps: *comparability* (repeat-capture deltas), a *durable home* for time-series, and the *comparative read* (its own frame).
- **The hard boundary.** Not a Pitchbook / Crunchbase clone — capture easy, first-party, obvious signals (tickers, big announced rounds, who wins the SERP); refuse the paid-data swamp and the single score.

## Problem statement

Every competitive or strategic look asks a traction question — *gaining ground, leading its space, worth worrying about?* Today that read is redone from scratch: throwaway searches, nothing accumulates, nothing's comparable run-to-run, and the **judgment** ("formidable") tangles with the **evidence** ("ranks #1, raised a Series B, reviews climbing"). The engine's bet is *capture once, read back* — traction is the obvious next layer, sitting right on the State store.

The catch: traction is **Signals** (time-axis, external, append-only); "formidable" is **Judgment** (viewer-relative). Keeping the store trustworthy means *not collapsing the two* — the line the visual-quality frame just walked.

## Why this matters

- **Recurring, expensive to repeat.** Every competitor look re-derives the same picture; a cited, accumulating layer makes it cheap, consistent, and cheaper on every reuse.
- **The missing axis for market maps.** Hotness / dominance need Signals — already flagged a first-class future because the maps reach backward for it.
- **Asymmetric failure cost.** A confident-but-wrong blended score, or a half-built Pitchbook clone that burns budget, destroys trust faster than it adds value. Honest axis evidence is safe; a wrong number isn't.

## Long-term capability goal

Given a company — or a cohort — produce a **cited, axis-specific traction read** that:

1. **Captures** repeatable external signals cheaply (reuse `tools/`).
2. Makes repeat captures **comparable** — deltas, velocity, movement, not just a fresh snapshot.
3. **Accumulates** into a durable timeline, *without polluting the State snapshot*.
4. **Rolls up** across a cohort for relative reads. *(comparative — its own frame.)*
5. **Feeds** a consumer-owned formidability judgment — never emits one as truth.

Only #1 has real machinery today. The frame says which graduate now, which are probes, which defer.

## Primary use cases

- **Competitor triage** (per-company) — is this rival formidable / worth attention?
- **Market maps** (cohort) — crowdedness, dominance, hotness. *Comparative.*
- **Brief / strategy enrichment** — a traction read beside the State dossier and visual-brand impression.
- **Ad-hoc market-scanning** — sizing up any company or space quickly.
- **(Future, consumer-owned)** — a formidability verdict; depth-gating a capture. Engine supplies the signal; the project makes the call.

## What makes this hard

Most are documented in prior systems, not speculative:

- **Market share is rarely observable.** Everything here is a **proxy / triangulation**, never a measurement — saying so, and flagging what the method can't see, is the whole game.
- **Grain is the constant trap.** Company review velocity ≠ SKU demand; SERP rank ≠ conversion; roster breadth ≠ traction. The live system makes *"every signal keeps its grain"* rule #1.
- **Signal/judgment entanglement.** "Formidable" is viewer-relative; the evidence isn't. A blended number hides the boundary (`tools/BACKLOG` and visual-quality both refuse it).
- **Individual signals are fragile.** AI Overview blanked *11/12 categories at once*; Trends batch-normalization swung a brand **14×**; Reddit was too sparse to keep. Disaggregate and fail safe — don't average noise into a clean score.
- **The signals are gamed.** Reviews farmed, profiles removed or merged, SERPs worked, microsites spun up for exact-match intent. Evidence is *adversarial* — integrity vetoes are core, not edge cases.
- **Disagreement is itself signal.** AIO says #1, organic says #9 — that gap is the tell. Averaging destroys it.
- **Comparison is unaddressed.** The engine keys on per-domain State; it's never done relative/cohort work. Prior art's insight: the natural grain for comparison is **category-keyed** ("who wins *best TRT clinic 2026*"), not brand-keyed — a different shape than the store.
- **Cost compounds on the time axis.** *Repeat* capture multiplies Firecrawl spend; credit-hungry axes (careers/roadmap) blow the budget. Cadence and scope discipline are mandatory.
- **Captures without synthesis are worthless.** Prior art's kill criterion: no synthesis for two months → cut it.

## What prior art already tells us

Two prior systems inform this: the deprecated `agent-workflows/competitive-traction`, and — more important — the **live** Teleprescribe **traction v2** layer that already consumes this engine's State + tools. Territory, not a design to port:

- **The live consumer draws the engine/project line.** v2 keeps traction as a *project judgment* layer — engine owns generic State + capture tools; the project owns the signal cards, project grain (SKU/molecule), and every judgment. *"The Web Research tools should stay generic. This layer should not."* So even the evidence layer is project-flavored today; only the generic machinery is a lift candidate.
- **Vocabulary, spine, and calibration already exist.** v2's labels (`supply only / visibility / trust-flow proxy / plausible movement / not measurable / vetoed`) are "axis-specific, no blend" made concrete; its `raw → card → interpretation → decision` spine keeps evidence portable; it calibrates by separating known-scale *anchors* from *contaminated controls*, never an absolute number.

<details>
<summary>More banked prior-art detail</summary>

- **Append-only per-period files; `git diff` = the change report.** A working time-axis shape (arguably a more concrete `log.md` than OKF specifies — see Open Questions).
- **No blended score; the rollup was narrative.** Leaderboard table + ranked leaders + repeating playbooks + cohort gaps. Composites deliberately avoided.
- **Tool lessons:** organic SEO is the stable spine; AIO opportunistic (fragile); Trends solo-per-brand, not batched; Reddit paused; Ad Library noisy. These map onto the six `tools/`.
- **Level-reads beat delta-reads before a baseline exists.** v2 flipped from "who's gaining" to "who's leading" — deltas need history a cold cohort lacks.

</details>

## Initial scope implication

First to graduate is narrow on purpose: **the per-company evidence layer.**

- Reuse the six `tools/`; add **comparability** (deltas/velocity over repeat captures). Output **axis-specific cited evidence** — *no blend, no frontmatter score, no autonomous verdict.*
- **Respect the engine/project line.** The engine hardens the *generic* machinery (capture + a comparability primitive + generic labels/grain); the *labeled panel* stays project-side (Teleprescribe v2) until a second consumer earns lifting it.
- **Probe capital/growth** — easy first-party funding only (tickers, announced rounds/M&A), bounded against paid tools. Prove what's gettable before building.
- **Defer talent/roadmap** — real signal, but careers scraping is credit-hungry. Not now.
- **Comparative/cohort → its own frame.** Named here as the bridge to maps; it's cross-cutting (touches offerings and visual-quality too).
- **Destination/storage shape** (snapshot vs. timeline; the `log.md` riff) — open for design, not decided here.

## Non-goals

- **Not** a Pitchbook / Crunchbase / AlphaSense replacement; no paid-data ingestion.
- **Not** a blended traction or market-share *score* as the product.
- **Not** the formidability / threat / fit **judgment** — consumer-owned.
- **Not** real-time monitoring (the parked **Monitoring** item is separate).
- **Not** polluting the State snapshot — time-axis Signals never land in `profile.md`.
- **Not** the comparative/cohort design — sibling frame.
- **Not** company discovery — you hand it a domain (or cohort).
- **Not** unbounded UGC harvesting — reviews/forums carry PII + ethics limits; persist aggregate counts and integrity flags, never identifiers.

## Open questions

1. **Where do time-series Signals live?** The architecture's deferred Signals-layer call: domain-keyed `log.md`, category/cohort ledgers, project-side, or comparator-only. OKF's `log.md` inspires but underspecifies; prior art's per-period files are the concrete precedent.
2. **Capture grain** — per-company vs. category-keyed (prior art favors category for comparison). How do the triage and maps consumers share one shape?
3. **The comparability primitive** — the generic envelope delta/velocity comparator (`tools/BACKLOG`'s top item). First real step regardless of storage.
4. **Capital/growth boundary** — which easy first-party funding signals are reliably gettable, and where's the line against the paid-data swamp?
5. **Cadence + budget** — how fresh is "fresh enough" when repeat capture multiplies cost? What's the kill criterion (prior art: no synthesis in 2 months → cut)?
6. **Engine vs. project ownership** — v2 draws it at generic-tools (engine) vs. cards-and-judgment (project). Durable line, or does a generic evidence spine eventually graduate once a second consumer needs it?
7. **Verb, module, or tools-only?** *(Don't answer yet — the design brainstorm decides.)*

## Proposed decision

> **Frame the destination as reusable external traction Signals for two consumers (triage + maps). Graduate the per-company, axis-specific evidence layer first — everything else is a probe, a deferral, or a sibling frame.**

Ship only the **generic** machinery (capture + a comparability primitive, cited axis output, no blend, no verdict); keep the labeled panel + judgment project-side until a second consumer earns lifting it. Probe capital/growth inside the first-party boundary; defer talent/roadmap on cost; spin comparative/cohort into its own frame; resolve the storage shape (incl. the OKF `log.md` riff) in design.

**Recommendation:** the destination is a trustworthy traction read; the first step is *cited evidence per axis*, not a score. Build the layer that's proven, keep judgment with the consumer, don't pretend to be a data vendor.

<sub>**Sources** — **live** Teleprescribe **traction v2** (`research/competitive/mine/traction/v2/`: project-judgment framing, evidence labels, signal-card spine, grain/integrity discipline, anchors+controls calibration) · deprecated `agent-workflows/competitive-traction` (category-keyed append-only shape, no-blend rollup, AIO/Trends/Reddit lessons, synthesis kill criterion) · engine [Frame](2026-05-29-frame.md) + [Architecture](2026-05-30-architecture.md) (State/Signals/Judgments, deferred Signals layer) · [`tools/`](../tools/README.md) + [`tools/BACKLOG.md`](../tools/BACKLOG.md) (six captures; comparator/delta as next primitive) · [visual-quality frame](../experiments/2026-06-13-visual-quality-graduation-frame/FRAME.md) (the evidence-vs-score split) · Google [OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/) (`log.md` inspiration, underspecified). Authored 2026-06-14.</sub>
