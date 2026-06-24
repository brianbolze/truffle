---
date: YYYY-MM-DD
run: <changes/YYYY-MM-DD-slug — the packet/run where this was seen; if there's no packet, a session id. Prefer the changes/ form so it greps.>
kind: <one of: friction | surprise | wish | risk-miss | brian-correction>
graduated-into: <leave absent; gets a lesson id (e.g. L001) or a brian.md anchor (e.g. brian.md#slug) only when its lesson graduates — never at propose>
---

**Saw.** What happened, first-person, concrete. 2–4 plain sentences. Quote the file/line/command if the wording or number is the signal.

**Not claiming.** What this observation is *not* asserting — the fix you're resisting, or the generalization you haven't earned. One line. (e.g. "Not claiming this is a general grep problem; one sighting on one recipe.")

If a fix is screaming at you, name the pressure or urge you felt — not the patch.

<!--
The rules — no-fix, immutable + the one `graduated-into:` stamp, no-subject, one-file-per-sighting — live in AGENTS.md, auto-loaded whenever you're in this folder. This comment carries only what's specific to filling out THIS file; if the two ever disagree, AGENTS.md wins.

FILENAME: copy this file to observations/YYYY-MM-DD-short-slug-xxxx.md (xxxx = 4 random hex, so two agents writing at once never collide). Never write into _TEMPLATE.md.

`kind` — one of the five (AGENTS.md owns the closed set); the glosses:
  friction         — harder, slower, or more confusing than it should be.
  surprise         — the system did something you didn't expect (often a latent bug or wrong assumption).
  wish             — "I wanted X and it wasn't there" — a gap stated as a want, not a spec.
  risk-miss        — a real risk you nearly shipped past, or did (surface immediately if severe).
  brian-correction — Brian corrected the work, judgment, or taste. Feeds brian.md, not lessons.md.

WRITE IT EVEN IF IT FEELS LIKE A DUPLICATE — sameness across runs is the signal the review pass needs; self-deduping destroys it.
-->
