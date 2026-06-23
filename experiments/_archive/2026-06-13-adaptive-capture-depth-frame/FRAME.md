# FRAME — Adaptive capture depth (a salience read with many consumers)

Date: 2026-06-13 · Status: problem frame (not system design). Aligns on the destination before anything is built. Interview-driven; Brian's leans baked in.

## 1. Working Title

**"How much does this company matter to me right now?"** — one reusable salience read that decides how much attention a company earns: how deep to capture, how often to re-look, whether to watch it, whether to surface it.

## 2. Short Answer

The thesis holds — adaptive depth is a **Judgment**, viewer-relative, so it's consumer-owned, and that *honors* the engine's State/Judgment line rather than breaking it. But it only survives if it splits into two layers (the same move the [visual-quality frame](../2026-06-13-visual-quality-graduation-frame/FRAME.md) made — evidence vs. scoring):

- **Substance floor (engine, State-like, generic, step one)** — *is this a real, substantive company or low-signal template slop?* Observable from the site, same answer for everyone. Engine-ownable. **Build this first.**
- **Salience read (consumer, Judgment, project, long-term)** — *how much does this matter to **me**?* Turf relevance, threat, fit. Viewer-relative, computed at read-time from engine State + project signals + project weights. **Never stored in the engine. Defer.**

**Graduate the floor first. Keep viewer-relative salience as a project-owned, read-time judgment.**

## 3. Problem Statement

The store treats every company the same: one capture, depth set by the site's own apparent breadth (`portfolio_shape`). But not every company deserves equal attention. A formidable, strategically-relevant competitor warrants depth and ongoing monitoring; a template-slop site not worth tracking warrants a glance, if that. Today that triage is manual and ad-hoc — nothing in the system reads "this one matters, that one doesn't."

The hard part isn't sizing one capture (the site already does that well). It's deciding, across the corpus and over time, **which companies earn standing attention** — without smuggling a viewer-relative Judgment into a State store that's supposed to stay opinion-free.

## 4. Why This Matters

- **Attention is the scarce resource, not credits.** Firecrawl is cheap on a second look; *your* attention and the store's signal-to-noise are not. A salience read is what keeps a growing corpus legible and a watchlist worth reading.
- **The real pain is ongoing monitoring, not initial capture.** Deciding depth on a single fresh capture is a minor pain (confirmed in interview). The felt need is *which companies to re-look at, watch, promote to Notion, and surface in a weekly report* — all the same underlying "does this still matter to me" question.
- **One read, many consumers.** Depth-gating, refresh cadence, watchlist inclusion, Notion write-back priority, and "company you haven't watched" notifications are plausibly the **same judgment** with different surfaces — so the artifact is one reusable salience read, not four separate gates.
- **The floor is honest and immediately useful.** Even before any viewer-relative scoring, a generic "this site is low-signal" read saves wasted depth and flags slop — and it's State-like, so the engine can own it cleanly.

## 5. Long-Term Capability Goal

A reusable salience read that, given a company's observable State (plus a consumer's own context), answers *how much attention does this company warrant from me right now* — and feeds that one answer to many consumers:

1. **Substance floor** — a generic, observable read separating substantive companies from low-signal slop. — *engine-ownable, build first*
2. **Viewer-relative salience** — turf relevance / threat / fit, weighted by the asking project. — *consumer-owned, defer*
3. **Attention routing** — map salience to concrete actions: capture depth, refresh TTL, watch/no-watch, Notion priority, report inclusion. — *consumer-owned*
4. **Stay legible** — every salience call shows the observable inputs it used and what it can't see; it's a lens, never a stored verdict.

## 6. Primary Use Cases

- **Refresh cadence / ongoing monitoring** — how often to re-look; whether a company earns a watch slot. *The real first consumer.*
- **Corpus hygiene** — keep the slop out of the way so the store stays legible as it grows. *Needs only the floor.*
- **Capture-depth gate** — skip deep spend on high-confidence slop at capture time. *Minor; floor-only; small pain.*
- **(Consumer-owned) Notion write-back priority** — which companies get promoted first.
- **(Consumer-owned) weekly competitive-intel report** — which companies make the cut.

## 7. What Makes This Hard

- **Altitude / bootstrap problem.** Real formidability (your [06-02 market-leadership audit](../../../Text%20Files/Teleprescribe%20Venture/Teleprescribe%20Venture/research/competitive/audits/2026-06-02-market-leadership-formidability.md): 55 agents, ~2.2M tokens) leans on **Signals + off-site sources** — funding, traffic, SEC, careers, M&A. The Notion "Formidability" row's *best real metric* is cash / team / pharmacy / distribution / paid media — almost none of it on the company's own site. So a read that gates *capture depth* must run on **cheap pre-capture signal only** (homepage breadth, nav depth, price posture, visual-craft evidence) and accept it's a crude proxy. The rich read can only exist *post-capture* — too late to gate the capture itself.
- **"Matters" ≠ "formidable."** Your own audit's headline: Hone, not Hims, is the one to lose sleep over — turf relevance beat raw size. Absolute formidability and salience-to-me diverge, and only the latter is the goal.
- **Viewer-relativity is the whole point and the whole danger.** Salience is defined by who's asking. Store it once and it's wrong for the next consumer — and it's a Judgment polluting a State store.
- **The floor's bar may drift by cohort.** "Low-signal" for a lean B2B site ≠ for a slop DTC brand. Whether one generic floor holds across cohorts is unproven.
- **Asymmetric error, and it cuts toward capturing.** Accidental-shallow on a company that mattered is the **worse** error (interview): it's a silent miss that can shape a call before anyone notices. Wasted-deep-on-slop is cheap and visible. So the floor must be **high-precision on "skip"** — gate down only on overwhelming slop evidence; bias to depth.

## 8. Principles

- **Split the floor from the salience.** Generic capture-worthiness (observable, global) is the engine's; viewer-relative salience (turf, threat, fit) is the consumer's. Collapsing them is the whole trap.
- **Map to the State/Judgment line — that's what makes the thesis hold.** Observable substance ≈ **State** → engine-ownable. "Matters to me" ≈ **Judgment** → consumer-owned, computed at read-time, never written into `profile.md`.
- **Fail safe toward capturing.** When the floor is unsure, capture. Skip only on high-confidence slop. The expensive error is the silent shallow miss.
- **Attention, not page-count.** The site already sizes one capture (`portfolio_shape`); a blind depth dial was already rejected. The unlock is salience *across the set and over time*, not pages-per-capture.
- **Capabilities are global; opinions are local.** The engine emits the raw observable inputs; each project owns its own "matters to me" weights and routing.
- **Don't rebuild the traction layer.** Absolute formidability / market-share is the [parked traction work](../../BACKLOG.md) — Signals-heavy, off-site, project-side. This frame does not resurrect it.

## 9. What We Think We Know

### What we know

- **Real formidability is off-site and Signals-heavy** — not capturable as State at capture time (06-02 audit; Notion Formidability row).
- **The engine already sizes one capture** via `portfolio_shape`, and a blind depth dial was deliberately rejected ([SKILL §2.5](../../skills/research-company/SKILL.md)).
- **The depth-gate never needed a quality *score***. The [parked presentation-rating item](../../BACKLOG.md) already concluded: gate on observable substance, not a rating.
- **"Matters" ≠ "biggest"** — turf relevance over raw scale (06-02 audit; [traction-v2 frame](../../../Text%20Files/Teleprescribe%20Venture/Teleprescribe%20Venture/research/competitive/mine/traction/v2/FRAME.md)).
- **The real pain is ongoing attention, not per-capture depth** (interview).
- **The asymmetry points toward capturing** — accidental-shallow is the worse, silent error (interview).

### What we suspect (unproven)

- **Cheap pre-capture homepage signal can separate slop from substance** well enough to gate — *needs a probe before any build* (interview).
- **The four consumers really are one read** (depth, refresh, watch, promote, report) — plausible, untested at the routing layer.
- **The floor can be one generic, cross-cohort read** — or it drifts by cohort and needs per-cohort anchoring.
- **The floor can emit observable substance signals as State** (like visual-quality evidence cards) while the salience verdict stays a light read-time computation — clean in theory, unbuilt.

## 10. Initial Scope Implication

Narrow on purpose: **the substance floor only.**

- De-risk first: an `experiments/<date>-substance-floor/` probe — does cheap pre-capture homepage signal predict "substantive vs. slop" against a hand-labeled set? **No build before the probe** (interview).
- If it holds: a generic, observable capture-worthiness read, biased to fail safe toward capturing — emits substance signals as State; gates depth down only on high-confidence slop.
- The **viewer-relative salience score** (turf, threat, fit) and its routing (refresh cadence, watchlist, Notion priority, report) stay a **project-owned, read-time** concern — specced when the ongoing-monitoring consumer is built, not now.
- Nothing salience-shaped gets written into `profile.md`.

## 11. Non-Goals

- **Not** absolute formidability / market-share estimation — that's the parked, Signals-heavy traction layer, project-side.
- **Not** a stored salience or "matters-to-me" field in `profile.md` — a Judgment in a State store.
- **Not** a per-capture page-count depth dial — `portfolio_shape` owns that; the dial was rejected.
- **Not** a quality *score* gate — gate on observable substance, not a presentation rating.
- **Not** turf / threat / fit judgment inside the engine — viewer-relative, consumer-owned.
- **Not** the monitoring infrastructure itself (the parked Monitoring item) — this is the read that would *prioritize* a monitor, not the monitor.

## 12. Open Questions

1. **Does cheap pre-capture signal actually separate slop from substance** reliably enough to gate? (The decisive probe.)
2. **Which observable signals are load-bearing** for the floor — catalog breadth, nav depth, price posture, original-vs-stock imagery, content depth? Which earn their place?
3. **Is the floor one generic read, or does "low-signal" drift by cohort** (lean B2B vs. slop DTC)?
4. **Where does the consumer salience policy live** — project `config.yaml`, a sibling skill, a new module — and what's its first concrete home (refresh TTL vs. watchlist)?
5. **Does the floor emit a stored observation** (State, like visual-evidence cards) or stay a purely computed read?
6. **How does salience map to concrete action** — what's the function from salience → refresh cadence / watch / promote?

## 13. Proposed Decision

**Frame the destination as one reusable salience read — "how much does this company matter to me right now?" — feeding many consumers. But split it on the engine's own State/Judgment line and graduate only the engine-ownable half first.**

- Build the **substance floor** — generic, observable, capture-worthiness — as the step-one engine capability, after a de-risking probe. Bias it to **fail safe toward capturing**; skip only high-confidence slop.
- Keep the **viewer-relative salience score** (turf relevance, threat, fit) as a **project-owned, read-time Judgment** — never stored in the engine — and spec it against its real first consumer: **ongoing monitoring / refresh cadence**, not initial-capture depth.
- Do not resurrect the parked traction/formidability layer to power this; this read runs on cheap observable State, by design.

---

**Recommendation:** the destination is one salience read with many consumers; the first step is the generic substance floor, not a formidability score. Probe whether cheap pre-capture signal predicts substance before building anything — and let the floor err toward capturing, because the silent shallow miss is the expensive one.
