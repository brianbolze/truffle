# FRAME — Unattended routines for Truffle

Date: 2026-06-17 · Status: problem frame. This sets the **permission boundary** for scheduled/background work — what the engine may do with no one watching. Runner shape, config, queueing, and install mechanics are out of scope; budget math lives in [routine budgeting](2026-06-16-routine-budgeting.md), per-run telemetry in [run records](2026-06-17-run-records.md).

## Short answer

Truffle is demand-driven today: someone asks, then it captures, enriches, queries, or renders. The roadmap names a different class of work — **useful maintenance that should happen without someone remembering to ask.**

The frame: **unattended batch work, not an automation platform.** A routine starts, does bounded repo work, leaves evidence, and stops. The repo may own repeatable work and its rules; it must not become a standing service, a scheduler product, or a hidden judgment engine. The wedge is the *floor* — regenerating disposable read surfaces (the HTML briefs), which spends nothing and can't corrupt the store. Every rung above it is gated.

## Problem — and why it matters

The store compounds only when someone tends it, and tending doesn't scale to the maintenance the roadmap now names. Each loop is a different supply-side pillar going starved:

- **Refresh** — stale records don't force themselves back into view; dates are visible but inert. → *Freshness*
- **Enrichment** — depth is uneven; thin records (no cohort pack, offerings, or visual) stay thin until someone notices. → *Depth*
- **Expansion** — coverage is opportunistic; companies enter only when a project happens to need them. → *Coverage*
- **Monitoring** — change detection (launches, rebrands, pricing shifts) needs comparable captures over time. → *Freshness*

They share one question: **what may the engine do unattended, bounded how, and trustable-after-the-fact how?** And because repeat capture spends real credits, unattended work needs tighter budget discipline than a one-off session.

## What good means

- **Bounded** — every routine has a reason to run, a work scope, a spend ceiling, and a stop condition.
- **Inspectable** — success, failure, absence, skips, and partial work stay distinguishable after the fact.
- **File-first** — markdown + JSON stay the source of truth; derived lenses remain disposable.
- **Permissioned** — read-only, derived writes, store writes, and paid capture are *different authorities*, not one generic "automation" permission.
- **Separable** — the clock that starts a routine is not the routine's brain. The repo owns intent and policy; the runner only invokes it. This single line is what keeps the engine from becoming a scheduler product — the rest of "no living infrastructure" is the existing anti-Doro principle, not re-derived here.
- **Cheap to retire** — a routine that yields no synthesis, coverage, freshness, or alerts gets cut, not kept alive.

What it is *not*, beyond the above: a blended score for importance/threat/momentum; automatic mutation of a project's KB; or a replacement for the existing capture / enrichment / signals / query / presentation verbs.

## Boundaries

The State / Signals / Judgments split stays load-bearing:

- **State routines** may refresh or deepen what a company *is now*.
- **Signals routines** may append dated evidence about movement over time.
- **Judgment routines do not write shared truth.** Viewer-relative reads — threat, fit, importance, formidability — stay project-side. Alerts hold the same line: a cited change or a failed check, never urgency/importance for a specific viewer.

**Expansion is the dangerous edge.** The engine may work from bounded candidate sources, but the "hand it a domain" discipline has to be reframed before a routine discovers companies freely — or discovery becomes a slop pump.

## Risk gradient

Safest first — work that can't corrupt the store or spend money, up to work that rewrites source records unattended. A map, not a build sequence.

1. **Derived maintenance** — regenerate disposable read surfaces (HTML briefs). No spend, no store mutation. → *Synthesis*
2. **Health & candidate surfacing** — flag stale / shallow / missing / changed items without touching them. Produces the worklist for 3–6; no mutation.
3. **Budgeted enrichment** — add specific earned depth to known companies. → *Depth*
4. **Budgeted refresh** — update stale known companies. → *Freshness*
5. **Store expansion** — bring in new companies, under strong candidate discipline. → *Coverage*
6. **Monitoring & alerts** — turn repeated Signals into cited change notices. → *Freshness*

Levels 1–2 are safe by construction (no spend, no mutation); 3+ each need an explicit authority grant.

## Pillars & personas

**Pillars.** Routines are the *unattended supply line for the supply-side pillars* — Coverage, Depth, Freshness. They must never quietly cross into **Synthesis**, the read-time judgment layer (that's the Judgment boundary above). **Access** is untouched: routines write state, they don't change read-back.

**Personas.** This family is **Steward-owned, Founder-gated, Pantry-policed:**

- **The Steward** is the beneficiary — automation is the corpus-caretaker's hands (gaps surfaced, rot refreshed). Litmus: a routine that doesn't serve the Steward is suspect.
- **The Founder** holds the gate — "compound the moat" vs. "stay light" is the live tension behind every non-goal.
- **The Pantry** polices the edge — its red line ("grow ingredients, don't cook the meal") *is* the Judgment boundary; refresh + monitoring directly feed its "freshness it can detect cheaply."
- **First Contact** is unserved by design — automation is invisible at first run; don't justify a routine by onboarding.

## Open questions

1. **Worklist** — who picks what runs, and on what cadence? Explicit queues, corpus health, signal movement, project priority, or a mix?
2. **Default authority** — propose-only, derived writes, store writes, or spend-and-recapture? And where does human approval sit — before candidates, before spend, or before store writes?
3. **Engine-owned alert** — a cited delta / failed check / stale record, or an interpreted importance call? The Judgment line decides this.
4. **Kill criterion** — how long may a routine run without producing synthesis, coverage, freshness, or alerts before it's cut?

## Proposed decision

Treat the roadmap items as one family — **unattended repo maintenance routines** — allowed when they're bounded, inspectable, file-first, and honest about the State / Signals / Judgments line.

On sequencing authority: **start at the floor.** Level 1 (derived-surface regen, beginning with the HTML briefs) needs no authority and can't spend or corrupt — it's the cheapest way to learn the runner + receipt shape before granting any authority that mutates the store or spends credits. Hold levels 3+ behind an explicit, per-authority decision.

<sub>Related: [engine frame](2026-05-29-frame.md), [architecture](2026-05-30-architecture.md), [pillars](../documentation/strategic-pillars.md), [personas](../documentation/personas.md), [traction frame](2026-06-14-traction-frame.md), [routine budgeting](2026-06-16-routine-budgeting.md), [run records](2026-06-17-run-records.md).</sub>
