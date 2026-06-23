<!-- Agent-facing contract for the /learning system. Auto-loaded when an agent touches this folder. Keep TIGHT; point outward. -->

# /learning — the contract

You're in Truffle's cross-run learning loop. Two halves: **capture** (every run, dumb and honest) and **review** (out-of-band skill, gated). This file is the rule set; the templates carry the detail.

## If you hit friction during a run → capture
Copy `observations/_TEMPLATE.md` to `observations/YYYY-MM-DD-short-slug-xxxx.md` (xxxx = 4 random hex). Record **what you saw and what you're *not* claiming — never a fix.**

If a fix is screaming at you, record the **pressure / urge**, not the patch.

**One file per sighting — not one per run.** Log every distinct thing you noticed as its own file (several per run is normal); never lump two unrelated sightings into one (that rebuilds the fused "feedback ticket" that failed before).

**Three hard rules that define the shape:**
1. **No fix.** No slot for a solution, and don't smuggle one into "Saw" (not even the root cause — record the *symptom*, the pressure). Deciding what to do is review's job; it has the cross-run sight you don't.
2. **Immutable.** Never edit, reorder, or delete an observation. The one permitted later touch is a `graduated-into: <lesson-id>` stamp, added when a lesson graduates (after Brian's gate) — never at propose. Contradiction? Write a *new* observation.
3. **No subject field.** about-Truffle vs about-Agentic-Build is decided at review, not capture. Capture stays dumb.

**`kind` is a closed set — one of exactly these five:** `friction | surprise | wish | risk-miss | brian-correction`. Don't invent a sixth. (Positive heuristics worth keeping aren't captured in v0 — friction/surprise/wish/risk-miss/brian-correction only.)

## If you're running a review pass → consolidate
Run the [`/agent-learning-review`](../../../.claude/skills/agent-learning-review/SKILL.md) skill — it carries the full procedure and judgment for this pass.

Copy `reviews/_TEMPLATE.md`. Read the raw observations first — prior reviews and lessons are dedupe context, not the source. Cluster repeats, *propose* lessons in `lessons.md` (never promote — that's Brian's gate). Route each cluster's subject and name what you deliberately left unconsolidated.

Heuristic for when to trigger: **≥5 observations since the last review.**

Exception: a severe `risk-miss` that could affect store correctness, a contract, live behavior, write authority, or Brian's decision surface gets surfaced immediately; do not wait for the cadence threshold.

**The Anti-Merge Law:** compression happens only by *adding* a lesson that points at observations — never by shrinking, merging, or summarizing them.

## Graduation heuristics
A lesson earns graduation on one of: ≥2 independent runs · a Brian correction · an independent review catch · one miss severe enough to justify a guardrail. It must first pass two self-tests: **state it without naming a run/company**, and **what does it replace?** (see `lessons.md`).

## Pointers
- Why this exists / the five-stage lifecycle → `README.md`
- Observation shape → `observations/_TEMPLATE.md` · Review shape → `reviews/_TEMPLATE.md`
- Lesson lifecycle + gate → `lessons.md` · Brian's preferences → `brian.md`
- Full rationale → [proposal](../_design/2026-06-23-learning-system-proposal.md)
