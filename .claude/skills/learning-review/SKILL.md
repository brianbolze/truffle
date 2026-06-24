---
name: learning-review
description: Run the out-of-band review/consolidate pass over a learning loop — read every observation, cluster repeats by shape, and PROPOSE lessons for Brian to approve (never promote). Works for either target — Agentic Build or Market Read Lab — passed as the first argument; if no target is given, the skill ASKS which one. Use when explicitly asked to consolidate learnings, run a learning review pass, or when observations have piled up since the last review (the cadence nudge in the target's learning/AGENTS.md). NOT for reviewing a single incoming change/PR.
disable-model-invocation: true
argument-hint: <target: agentic-build | market-read-lab> [optional scope note]
---

$ARGUMENTS

## Resolve the target first

This skill runs the review pass for **one** learning loop. Read the first argument as the target:

| Target | Learning dir | Observations live in | Pass notes go in | Back-stamp |
|---|---|---|---|---|
| `agentic-build` | `experiments/01-agentic-build/learning/` | one file per sighting in `observations/` | `reviews/NNN-YYYY-MM-DD-pass.md` | a `graduated-into:` stamp on the observation file, after Brian's nod only |
| `market-read-lab` | `experiments/00-market-read-lab/learning/` | rows in a single `observations.md` table | `passes/NNN-YYYY-MM-DD-pass.md` | none in v0 — grep `lessons.md` for a row to see if it's already used |

**If no known target was given, ask Brian which one — do not guess or default.** Everything below operates inside the resolved `<target>/learning/`, and defers to that target's `AGENTS.md` for every rule that differs between the two.

## Purpose

Run one **review / consolidate pass**: read every observation, cluster the repeats, and **propose** lessons. This is the out-of-band half of the learning loop — the verb that turns raw observations into candidate rules for Brian to gate.

This is the single hardest step to get right. The prior system (Market Read Lab's old `triage.md`) died here by over-compressing — ~345 observations collapsed to ~2, each fused to a fix. Your job is the opposite instinct: **propose sparingly, preserve divergence, and leave most observations untouched.** The "left unconsolidated" count is the honest half of the work, not an afterthought.

## What this is not

- **Not** a single incoming change/PR review (for Agentic Build, that's `review-change`).
- **Not** capture — you never *write* observations here; agents do that in-band during their own runs (for Agentic Build, `/agent-learning-mine` can also feed them retroactively).
- **Not** a promotion gate — you only ever propose (`state: proposed`); Brian decides (the gate + states live in `lessons.md`).
- **Not** an editor of live skills/recipes — you never sharpen the thing a lesson improves; that happens after Brian approves, elsewhere.

## Required context — defer to these, don't restate them

Read these inside your resolved `<target>/learning/`. They are the contract, and this skill defers to them for **every** rule, closed set, route, and file shape.

- `AGENTS.md` — the contract: kinds, the Anti-Merge Law, the immutability + stamp policy, graduation triggers. **Authoritative for everything that differs between targets.**
- `lessons.md` — the lesson lifecycle, states, routes, graduation gate, and the two self-tests. The first lesson block models the shape.
- `brian.md` — the protected Brian lane and its entry format.
- the pass-note template (`reviews/_TEMPLATE.md` or `passes/_TEMPLATE.md`, per the table above) — the exact note shape you will write, including the Anti-Merge attestation.
- the observation grain — Agentic Build: `observations/_TEMPLATE.md`; Market Read Lab: the column legend atop `observations.md`.
- prior pass notes — dedupe context only. The raw observations are the source; don't let the tidy view become your evidence corpus.

## Task

1. **Ground in the contract.** Read the files above for your target. The rules live there; this skill is only the procedure and the judgment.
2. **Read every raw observation first** — all of them (every file in `observations/`, or every row of `observations.md`), including ones a prior pass already used (they're context for the shape, even when spent). Only then read prior passes and lessons as dedupe context. A single agent reads the whole corpus; it's thin — do not fan out or build machinery.
3. **Cluster by SHAPE, not topic** — group by shared underlying pressure / failure mode, not surface subject. (The over- and under-cluster traps: see *How to judge well*.)
4. **Gate each cluster.** Propose a lesson only for a cluster that earns graduation per the gate in `lessons.md`, and only if it passes both self-tests there. Most clusters — and nearly all singletons — will *not* qualify. That's correct.
5. **Propose, don't promote.** For each cluster that earns it, append a lesson to `lessons.md` at `state: proposed`, in the shape the first lesson models. For a Brian-taste correction, *propose* a `brian.md` candidate in the pass note instead — don't write it into `brian.md`; that lane holds accepted entries only, and the entry lands there on Brian's nod.
6. **Assign the route now**, per your target's routes in `lessons.md`. Capture stayed dumb on purpose; routing is decided here. Record it on the lesson row, not the observation.
7. **Promote and stamp nothing this pass** — follow your target's stamp policy in `AGENTS.md`. (Agentic Build: leave the `graduated-into:` stamp for after Brian's nod, `brian-correction` included — an in-pass stamp on a later-rejected entry leaves a dangling ref, the very thing this loop exists to prevent. Market Read Lab: there is no stamp in v0 — a proposed lesson just *lists* its source rows.) Either way, a pass graduates nothing.
8. **Write the pass note.** Copy your target's template into its pass-notes folder as `NNN-YYYY-MM-DD-pass.md` — NNN is the next zero-padded, monotonically increasing number (highest existing prefix + 1). Fill the "deliberately left unconsolidated" list honestly and the Anti-Merge attestation truthfully.
9. **Hand Brian the decision surface** (see Final Response). Stop. Do not sharpen any skill.

## How to judge well

The contract says *what* the rules are. This is *how* to apply them without repeating the last system's mistakes.

- **Cluster by shape, but don't sand off the edges.** Two observations cluster when they'd be fixed by the *same* rule, not when they're vaguely "about docs" or "about counting." If stating the shared rule forces you to hedge ("usually", "in cases like"), you've over-clustered — split it back apart. A cluster you can't state crisply isn't a cluster yet.
- **Singletons are the asset, not backlog to clear.** A lone, non-severe sighting almost never earns a lesson — it waits for a 2nd. Park the *idea* by naming it in the "left" list ("watching for a 2nd sighting"), not by proposing from n=1. The single-sighting exceptions are exactly the ones the gate in `lessons.md` names — don't widen them.
- **Keep the `left` count honest — and large.** Most observations should sit unconsolidated most passes. A pass that consumes everything is the 345→2 failure running in the other direction. If your "left" list is short, distrust yourself: re-read what you consolidated and ask whether each really earned it.
- **Test 1 (`lessons.md`) is the real filter — apply it ruthlessly before proposing.** Strip every company name, packet id, and run slug out of the rule. If a sharp, general rule survives → it's a lesson. If it dissolves into one case → it's still an observation; leave it.
- **"What does it replace?" gates additive lessons.** A lesson that corrects an existing recipe/skill/convention is strong. A lesson that only adds a new rule with nothing retired is suspect — default to not proposing it (this mirrors Brian's own simplify-don't-add reflex).
- **Severe `risk-miss` bypasses the cadence, not the gate.** If a miss could affect store correctness, a contract, live behavior, write authority, or Brian's decision surface, surface it in this pass even below the normal review threshold. Still do the self-tests and route it honestly.
- **Compress only by adding.** If you feel the urge to tighten, merge, or summarize an observation's text — stop. That's the Anti-Merge Law (`AGENTS.md`); compression is only a new lesson pointing back at the raw notes.

## Output

- Append/advance any earned lessons in `<target>/learning/lessons.md` (`state: proposed`); propose `brian-correction` clusters as `brian.md` candidates in the pass note — don't write `brian.md`.
- Promote and stamp nothing — a pass graduates nothing (follow the target's stamp policy in `AGENTS.md`).
- Write the pass note from the template into the target's pass-notes folder (`reviews/` or `passes/`), as `NNN-YYYY-MM-DD-pass.md`.
- No live skill, recipe, or convention is edited.

## Final Response

End with a short decision surface for Brian:

- target + pass-note path
- **proposed** — each lesson id + one-line rule + route, and any `brian.md` candidate, all awaiting his approval
- **left** — how many observations stayed unconsolidated, and the one or two you most want a second opinion on
- the Anti-Merge attestation, in one line
- `No live skill or recipe was edited; nothing was promoted or stamped — every entry awaits your nod.`
