---
name: work-menu
description: Scan Truffle's scattered local evidence (backlog, both learning loops, Agentic Build packets, run-record coverage, design notes), apply an optional focus lens, and PROPOSE 5–7 routed work candidates Brian can graduate, park, or hand off. A read-only work-selection pass that never mutates a source file. Runs as a dynamic-workflow harness: blind fan-out → synthesize → adversarial graduation gate → route. Use when explicitly asked "what should Truffle work on next", "/work-menu", "run a work-selection pass", "pick next work", or to surface stale process debt. NOT a roadmap, an auto-prioritizer, or a ranker of Notion big rocks; NOT a single-PR review (that's review-change) or the learning consolidate pass (that's learning-review).
disable-model-invocation: true
argument-hint: <optional focus lens, e.g. "capture quality this week" | "workflow reliability" | "silent-wrong risks"; or "roadmap" to add roadmap mode; blank = balanced pass>
---

$ARGUMENTS

## Purpose

One read-only pass that answers **"what should Truffle improve next, from evidence we already have?"** It scans the scattered local surfaces, applies an optional focus lens, and proposes a short **routed work menu** — 5–7 candidates Brian can graduate, park, or hand off. The full frame (problem, surfaces, non-goals) lives in [`_temp/2026-06-24-truffle-work-selection-frame.md`](../../../_temp/2026-06-24-truffle-work-selection-frame.md); defer to it.

It runs as a [dynamic-workflow harness](../../docs/dynamic-workflows.md). **The harness is not about scale** — the corpus fits one window. It buys two things one window does badly, which are the frame's two named risks: **blind reads** (Phase 1 — no surface anchors the others) and an **egoless graduation gate** (Phase 3 — the agent that proposed a candidate is not the one that waves it through). The gate is the spine; over-promotion is the enemy.

## What this is not

- **Not a roadmap or auto-prioritizer.** It proposes a menu; Brian orders the big rocks. Notion stays out of scope unless run in `roadmap` mode.
- **Not a mutation.** It never writes to a source file (BACKLOG, learning, packets). Read-only. Output is chat-first; persistence is opt-in (below).
- **Not graduation.** It surfaces and routes; Brian decides. A surfaced card is a recommendation, not a committed work item.
- **Not the learning consolidate pass** (`/learning-review`) or a single-change review (`review-change`). It can *route to* those; it doesn't do them.

## Required context — defer to these, don't restate them

- [`work-menu.workflow.js`](work-menu.workflow.js) — the harness. The reader prompts, the closed sets (buckets, authority grains, routes), and the gate rubric live there, as the single source of truth. **Treat it as a template, not a verbatim script:** adapt models, surface paths, or phases to the run, but keep the four-phase shape and the gate's default-to-watch posture.
- [`learning-review/SKILL.md`](../learning-review/SKILL.md) — the gate borrows its posture (strip specifics, "what does it replace?", ≥2 sightings or a severe risk-miss, keep the "left" count honest and large). Read *How to judge well* before trusting any pass.
- the frame (linked above) — the seven subject buckets and the non-goals are its, not this skill's.

## Task

1. **Resolve the lens.** Read `$ARGUMENTS` as the focus lens. `roadmap` (alone or appended) flips on roadmap mode. **If the argument is blank, ask Brian for a lens or confirm a balanced pass — don't silently default** (a shaped pass is the point).
2. **Run the harness.** Invoke the `Workflow` tool with `scriptPath` pointing at [`work-menu.workflow.js`](work-menu.workflow.js), passing `args: { lens, engineRoot: <repo abs path>, roadmap }`. It runs Read → Synthesize → Gate → Render and returns the menu object (`brian_digest_md`, `cards`, `left`, `overflow_note`, `second_opinion`, `counts`).
3. **Trust the gate, don't second-guess it upward.** If a pass surfaces very little, that is a *clean* result, not a failure — report the honest "left" count as the work, per learning-review. Never re-promote a watch item just to lengthen the menu.
4. **Present, then offer to act.** Print `brian_digest_md` to chat as the menu. End with the decision surface (below). Act on a card only when Brian picks one — then hand off to its route's verb (`/agent-build-propose`, `/learning-review <target>`, `/deepen-offerings`, etc.).
5. **Persist only on request.** Default is chat-first. If Brian says `--persist` (or asks for cross-pass memory), write `brian_digest_md` + the cards to a dated, disposable digest — propose the home on first use (`_review/work-selection/NNN-YYYY-MM-DD.md`, mirroring learning-review's `passes/`). A persisted digest is a regenerable lens, never authoritative.

### Quick mode (skip the harness)

For a **narrow, single-lens** pass over one or two surfaces, the harness's blindness buys little — run it inline as a single agent: read the surface(s), apply the lens, gate each candidate against the rubric in the workflow's Phase-3 prompt (same default-to-watch), and render the same two views. Reach for the full harness whenever the pass spans many surfaces or the over-promotion risk is real.

## Final Response

A short decision surface for Brian:

- **lens** + counts (`raw → plausible → surfaced → on-menu`, and how many left as watch).
- **the menu** — `brian_digest_md`: candidates grouped by **subsystem bucket** (the frame's seven), each with a sharp title, one-line problem, why-now, the gate's readiness verdict (ready vs watch + why), and recommended route. (The `cards` array is the provenance audit trail behind it.)
- **left as watch** — the honest count, plus the 1–2 calls (`second_opinion`) you'd most want a second look at. Any `overflow_note`.
- `Read-only — no source file was touched; nothing was graduated. Pick a card and I'll route it.`
