# learning/ — the contract

Two jobs happen here: **capturing** what a run noticed, and, out-of-band, **consolidating**
sightings into proposed lessons. Capture is greedy and dumb; consolidation is gated and rare.
Keep them separate — that separation is the whole point of this folder.

## Capturing during a run → `observations.md`

Append one row per sighting. This is the stream of *system-learning* signals: something was
hard, unexpected, wanted, unseeable at the needed grain, risky, or corrected by Brian. A
neutral market finding is **not** a learning signal — it stays in the run's `read.md`, not here.

- **One row per sighting.** Two runs noticing the same shape means two rows. Never merge, dedup, rewrite, or reorder rows — that is the failure the old triage queue made.
- **Record the symptom, not the fix.** `Saw` is what happened; `Not claiming` is the wanted shape or boundary you are deliberately *not* asserting. No build proposal, field, tool, or recipe goes in a row, even if the fix feels obvious.
- **Cite the run.** Put the run path in `Run` and an evidence pointer (a `read.md` claim ID, or `file:line`) in `Evidence pointer`.
- **Use the closed kind set** — pick the closest one; don't invent a sixth:
  - `friction` — the run was harder, slower, or more confusing than it should be.
  - `surprise` — the system or evidence did something unexpected, including a useful trap avoided.
  - `wish` — "I wanted X and it wasn't there," including source-family wants.
  - `gap` — Truffle can't see this at the needed grain; the run's structural frontier.
  - `risk-miss` — a risk almost shipped, or did ship, past the run or review.
  - `brian-correction` — Brian corrected judgment, taste, scope, or communication.
- **Don't double-log `gap` + `wish`.** If a `gap` row already names the missing grain or source family, the obvious wanted shape belongs in its `Not claiming`, not a second `wish` row. Add a `wish` only when it is a genuinely distinct want.
- **Tags are loose recurrence handles** — not a taxonomy, and not approval to build.

Runs append observations. Runs do **not** propose lessons, mark readiness, or touch
`lessons.md`, `brian.md`, or `passes/`.

## Running a learning pass → `lessons.md` + `passes/`

Run it with the [`/learning-review`](../../../.claude/skills/learning-review/SKILL.md) skill (target `market-read-lab`) — it carries the full procedure and judgment.

A pass is out-of-band — it is not Loop 2 and not per-run. MRL produces many observations per
run, so a per-run trigger would just rebuild Loop 2. Run a pass on a nudge: after several runs,
after a severe `risk-miss`, or when Brian asks.

1. Read **all** active observations first.
2. Read prior passes, `lessons.md`, and `brian.md` only as dedupe context.
3. Cluster by **shape**, not topic.
4. Propose **sparingly**; leave most observations unconsolidated.
5. Add proposed lessons to `lessons.md` at state `proposed`.
6. Put Brian-lane candidates in the pass note — **not** directly in `brian.md`.
7. Graduate or stamp **nothing** without Brian's nod.
8. Edit **no** live Truffle skill, recipe, schema, or template.

Close every pass note with the **Anti-Merge attestation**: confirm no observation was edited,
merged, summarized, deleted, or stamped this pass. Compression happens only by *adding* a
lesson that points at rows — never by shrinking the stream. Use [`passes/_TEMPLATE.md`](passes/_TEMPLATE.md).

## The Brian lane

`brian-correction` observations feed [`brian.md`](brian.md), not `lessons.md` — communication
preferences, judgment corrections, recurring taste calls, and process tells that are about
**Brian**, not about MRL as a system. A single correction is enough; it doesn't need to recur.
But a pass only *proposes* a `brian.md` entry; Brian's nod writes it. This keeps "learn Brian"
from diluting general process lessons.

## Graduation

Lesson states, routes, and the two graduation tests live in [`lessons.md`](lessons.md). A lesson
must state its rule generally — no single run or company named — and name what it replaces.
Graduation into a live Truffle change stays a human decision.

## Pointers

- Observation + pass contracts in full: [`../_design/2026-06-24-learning-migration-proposal.md`](../_design/2026-06-24-learning-migration-proposal.md).
- Sibling loop (file-per-sighting variant, same gated principle): [`../../01-agentic-build/learning/AGENTS.md`](../../01-agentic-build/learning/AGENTS.md).
