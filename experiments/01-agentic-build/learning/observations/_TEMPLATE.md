---
date: YYYY-MM-DD
run: <changes/YYYY-MM-DD-slug — the packet/run where this was seen; if there's no packet, a session id. Prefer the changes/ form so it greps.>
kind: <one of: friction | surprise | wish | risk-miss | brian-correction>
graduated-into: <leave absent; gets a lesson id (e.g. L001) or a brian.md anchor (e.g. brian.md#slug) only when its lesson graduates — never at propose>
---

**Saw.** What happened, first-person, concrete. 2–4 plain sentences. Quote the file/line/command if the wording or number is the signal.

**Not claiming.** What this observation is *not* asserting — the fix you're resisting, or the generalization you haven't earned. One line. (e.g. "Not claiming this is a general grep problem; one sighting on one recipe.")

<!--
HOW TO USE THIS FILE — read before writing your first observation.

WHAT AN OBSERVATION IS: one thing a run taught us, recorded honestly. Nothing else.
  One file = one sighting, but a run can produce SEVERAL — write a separate file for each distinct thing;
  never lump two unrelated sightings into one to save effort.

FILENAME: observations/YYYY-MM-DD-short-slug-xxxx.md
  date sorts · slug lets you skim · xxxx = 4 random hex chars so two agents writing at once never collide.
  Copy this file to that name; never write into _TEMPLATE.md itself.

THREE RULES THAT DEFINE THE SHAPE — break any and you've rebuilt the system that failed:
  1. NO FIX. There is no slot for a solution, and you may not smuggle one into "Saw." If a fix is
     screaming at you, that IS the signal — record the pressure ("re-derived this by hand a 3rd time,
     felt like toil"), never the patch. Deciding what to do is the review pass's job, with cross-run
     sight you don't have.
  2. IMMUTABLE. Once written, never edit, reorder, or delete this file. The ONLY permitted later touch
     is a `graduated-into: <lesson-id>` stamp, added when the observation's lesson graduates (after Brian's gate) — not when it's merely proposed.
     Saw something that contradicts an old observation? Write a NEW one that says so. Never rewrite history.
  3. NO SUBJECT FIELD — on purpose. Whether this is about-Truffle (a recipe misleads, the store can't
     answer X) or about-Agentic-Build (a step got skipped, a correction keeps recurring) is decided at
     REVIEW, when routing — not here. Capture stays dumb. A subject field would force you to pre-judge
     the call the reviewer makes, and would lean you toward a fix-shaped frame. So it's absent. Don't add it.

`kind` is a closed set — use one of the five exact strings, don't invent a sixth:
  friction         — something was harder, slower, or more confusing than it should be.
  surprise         — the system did something you didn't expect (often a latent bug or wrong assumption).
  wish             — "I wanted X and it wasn't there." A gap, stated as a want, not a spec.
  risk-miss        — a real risk you nearly shipped past, or did. The severe ones can graduate on one sighting.
  brian-correction — Brian corrected the work, the judgment, or the taste. Feeds brian.md, not lessons.md.
  Deliberate v0 cut: positive heuristics worth keeping have no home here — this loop targets the failure cases (friction/surprise/wish/risk-miss/brian-correction) only.

WRITE IT EVEN IF IT FEELS LIKE A DUPLICATE. Sameness across runs is the whole signal — the review pass
needs the repeats to spot the pattern. You'd destroy it by self-deduping. One file = one sighting.

CANONICAL: if anything here ever disagrees with AGENTS.md, AGENTS.md wins — it's the contract; this file just carries the detail.
-->
