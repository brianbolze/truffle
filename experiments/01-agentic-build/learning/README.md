<!-- Human-facing orientation on the /learning system. Plain English. -->

# learning/ — a cross-run learning loop for Agentic Build

Truffle learns *within* a run (e.g. `site_notes`) but had no way to learn *across* runs. This folder is that loop: a cheap **capture** half (every run can record atomic, honest observation notes) and a gated **review** half (an out-of-band pass clusters the notes into lessons you approve). The one rule it all rests on: **a note can never hold a fix, and is never rewritten** — which makes the failure that killed the last attempt (Market Read Lab's `triage.md`, ~345 observations compressed to ~2 fused-to-fixes) impossible by construction.

## The lifecycle (five stages)
1. **Capture** — a run writes an `observations/` file per distinct thing it noticed (as many as it saw — one sighting each, never two lumped together): what it saw, no fix.
2. **Review** — you run the review skill; it reads *all* observations, clusters repeats, writes a `reviews/` note, and adds a *proposed* lesson to `lessons.md`.
3. **Approve** — you accept / park / drop it. The only human gate.
4. **Sharpen** — the accepted lesson is written into the skill / recipe / convention it improves.
5. **Consult** — the next run reads the now-sharper thing and doesn't repeat the mistake.

## Two routes out of review
- **about-Truffle** (a recipe misleads, the store can't answer X) → enters Agentic Build's workflow: frame → proposal → review → implement → verify. *Agentic Build* changes Truffle; the loop just feeds the queue.
- **about-Agentic-Build** (a step gets skipped, a correction keeps recurring) → a light internal edit, second look, no change-packet.

## Where to look
- `observations/` — raw sightings, append-only, immutable. One file = one sighting.
- `lessons.md` — reviewed, decided patterns (the curated short list).
- `brian.md` — Brian's recurring preferences, a protected lane.
- `reviews/` — what each pass read, proposed, and deliberately left alone.
- `AGENTS.md` — the tight agent-facing contract (auto-loaded on entry).

Full rationale: [proposal](../_design/2026-06-23-learning-system-proposal.md).
