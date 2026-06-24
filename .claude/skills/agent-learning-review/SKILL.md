---
name: agent-learning-review
description: Run the out-of-band review pass over the Agentic Build learning loop — read all observations, cluster repeats by shape, and PROPOSE lessons for Brian to approve. Use when explicitly asked to consolidate learnings, run a learning review pass, or when observations have piled up since the last review (cadence nudge in AGENTS.md). NOT for reviewing a single incoming change/PR — that's review-change.
disable-model-invocation: true
argument-hint: <optional: scope note, or leave blank to review all observations>
---

$ARGUMENTS

## Purpose

Run one **review / consolidate pass** over `learning/`: read every observation, cluster the repeats, and **propose** lessons. This is the out-of-band half of the learning loop — the verb that turns raw observations into candidate rules for Brian to gate.

This is the single hardest step to get right. The prior system (Market Read Lab's `triage.md`) died here by over-compressing — ~345 observations collapsed to ~2, each fused to a fix. Your job is the opposite instinct: **propose sparingly, preserve divergence, and leave most observations untouched.** The "left unconsolidated" count is the honest half of the work, not an afterthought.

## What this is not

- **Not** a single-change/PR review — that's `review-change`.
- **Not** capture — you never *write* observations here; agents do that in-band during their own runs.
- **Not** a promotion gate — you only ever propose (`state: proposed`); Brian decides (the gate + states live in `lessons.md`).
- **Not** an editor of live skills/recipes — you never sharpen the thing a lesson improves; that happens after Brian approves, elsewhere.

## Required context

Read these first — they are the contract, and this skill defers to them for **every** rule, closed set, and file shape. Do not restate them; point at them.

- [`learning/AGENTS.md`](../../../experiments/01-agentic-build/learning/AGENTS.md) — the contract (kinds, Anti-Merge Law, the immutability + one-stamp rule, graduation triggers).
- [`learning/lessons.md`](../../../experiments/01-agentic-build/learning/lessons.md) — the lesson lifecycle, states, graduation gate, and the two self-tests. `L001` models the shape.
- [`learning/brian.md`](../../../experiments/01-agentic-build/learning/brian.md) — the protected Brian lane and its entry format.
- [`learning/reviews/_TEMPLATE.md`](../../../experiments/01-agentic-build/learning/reviews/_TEMPLATE.md) — the exact note shape you will write, including the Anti-Merge attestation.
- [`learning/observations/_TEMPLATE.md`](../../../experiments/01-agentic-build/learning/observations/_TEMPLATE.md) — so you read each observation in its intended grain.
- Prior `learning/reviews/*-pass.md` notes — dedupe context only. The raw observations are the source; don't let the tidy view become your evidence corpus.

## Task

1. **Ground in the contract.** Read the files above. The rules live there; this skill is only the procedure and the judgment.
2. **Read every raw observation first** in `learning/observations/` — all of them, including the ones a prior pass already stamped `graduated-into:` (they're context for the shape, even when spent). Only after that, read prior reviews/lessons as dedupe context. A single agent reads the whole corpus; it's thin — do not fan out or build machinery.
3. **Cluster by SHAPE, not topic** — group by shared underlying pressure / failure mode, not surface subject. (The over- and under-cluster traps: see *How to judge well*.)
4. **Gate each cluster.** Propose a lesson only for a cluster that earns graduation per the gate in `lessons.md`, and only if it passes both self-tests there. Most clusters — and nearly all singletons — will *not* qualify. That's correct.
5. **Propose, don't promote.** For each cluster that earns it, append a lesson to `lessons.md` at `state: proposed`, in the `L00x` shape `L001` models. Route Brian-correction clusters to `brian.md` instead (that kind and its lane are defined in `AGENTS.md`/`brian.md`).
6. **Assign subject + routing now.** Each surfaced cluster gets its subject (`about-Truffle` | `about-Agentic-Build`) and destination *at this step* — capture stayed dumb on purpose. Record it on the lesson row, not the observation. (Routing rules: `lessons.md` / `reviews/_TEMPLATE.md`.)
7. **Stamp `graduated-into:`** only on observations whose lesson *actually graduates this pass* — i.e. a `brian-correction` you distill into `brian.md`. A lesson you leave at `state: proposed` just lists its observations on its `lessons.md` row; do **not** stamp those — the stamp lands later, when Brian's gate graduates the lesson. This is the **one** permitted touch; nothing else about an observation may change.
8. **Write the pass note.** Copy `reviews/_TEMPLATE.md` to `reviews/NNN-YYYY-MM-DD-pass.md` — NNN is the next zero-padded, monotonically increasing pass number (take the highest existing prefix and add one). Fill the "deliberately left unconsolidated" list honestly and the Anti-Merge attestation truthfully.
9. **Hand Brian the decision surface** (see Final Response). Stop. Do not sharpen any skill.

## How to judge well

The contract says *what* the rules are. This is *how* to apply them without repeating the last system's mistakes.

- **Cluster by shape, but don't sand off the edges.** Two observations cluster when they'd be fixed by the *same* rule, not when they're vaguely "about docs" or "about counting." If stating the shared rule forces you to hedge ("usually", "in cases like"), you've over-clustered — split it back apart. A cluster you can't state crisply isn't a cluster yet.
- **Singletons are the asset, not backlog to clear.** A lone, non-severe sighting almost never earns a lesson — it waits for a 2nd. Park the *idea* by naming it in the "left" list ("watching for a 2nd sighting"), not by proposing from n=1. The single-sighting exceptions are exactly the ones the gate in `lessons.md` names — don't widen them.
- **Keep the `left` count honest — and large.** Most observations should sit unconsolidated most passes. A pass that consumes everything is the 345→2 failure running in the other direction. If your "left" list is short, distrust yourself: re-read the observations you consolidated and ask whether each really earned it.
- **Test 1 (`lessons.md`) is the real filter — apply it ruthlessly before proposing.** Strip every company name, packet id, and run slug out of the rule. If a sharp, general rule survives → it's a lesson. If it dissolves into one case → it's still an observation; leave it. This is what keeps an observation from collapsing into a one-case fix.
- **"What does it replace?" gates additive lessons.** A lesson that corrects an existing recipe/skill/convention is strong. A lesson that only adds a new rule with nothing retired is suspect — default to not proposing it (this mirrors Brian's own simplify-don't-add reflex in `brian.md`).
- **Severe `risk-miss` bypasses the cadence, not the gate.** If a miss could affect store correctness, a contract, live behavior, write authority, or Brian's decision surface, surface it in this pass even below the normal review threshold. Still do the self-tests and route it honestly.
- **Compress only by adding.** If you feel the urge to tighten, merge, or summarize an observation's text — stop. That's the Anti-Merge Law (`AGENTS.md`); compression is only a new lesson pointing back at the raw notes.

## Output

- Append/advance any earned lessons in `learning/lessons.md` (`state: proposed`); route `brian-correction` clusters to `learning/brian.md`.
- Stamp `graduated-into:` only on observations whose lesson graduated this pass (proposed lessons link their observations on the row, unstamped) — nothing else touched.
- Write `learning/reviews/NNN-YYYY-MM-DD-pass.md` from the template (NNN = next monotonic pass number).
- No live skill, recipe, or convention is edited.

## Final Response

End with a short decision surface for Brian:

- review-note path
- **proposed** — each lesson id + its one-line rule + subject/route, awaiting his approval
- **left** — how many observations stayed unconsolidated, and the one or two you most want a second opinion on
- the Anti-Merge attestation, in one line
- `No live skill or recipe was edited; nothing was promoted.`
