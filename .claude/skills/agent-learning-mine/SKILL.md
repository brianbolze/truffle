---
name: agent-learning-mine
description: Retroactively mine past Claude Code session transcripts into raw learning-loop observations — the optional, fenced capture feeder the learning-system proposal anticipated. Use to seed or backfill `learning/observations/` from friction already on disk (Brian corrections, `/overwhelmed` firings, reviewer catches) that in-band capture missed. One sighting per file, never a fix — defers to `learning/AGENTS.md` for every rule. NOT the review/consolidate pass (that's agent-learning-review); it never proposes a fix or a lesson.
disable-model-invocation: true
argument-hint: <optional: --since YYYY-MM-DD, or a scope note; blank = mine recent sessions>
---

$ARGUMENTS

## Purpose

Mine past session transcripts for friction and write it into `learning/observations/` as raw observation files. This is **retroactive capture** — a sibling to the in-band capture a run does live, feeding the *same* `observations/` folder under the *same* rules. It catches what live capture misses: friction in older sessions, and the quiet kind an agent never self-reported.

It is the proposal's **"optional, fenced `mine.py` feeder"** — best-effort, and degrades gracefully. The markdown observations are the durable layer; they survive even if transcript access ever vanishes.

## What this is not

- **Not** the review/consolidate pass — it never clusters, proposes, or writes a lesson. That is `agent-learning-review`, run separately afterward.
- **Not** a fix-proposer — it writes raw observations only; the no-fix rule is the whole point.
- **Not** live infrastructure — you run it by hand, it writes evidence, it stops.

## Required context — defer to these, don't restate them

The observation contract lives in the learning folder; this skill carries only the mining *procedure*. Read these first and obey them for the card shape, the five `kind`s, and the no-fix / immutable / one-file-per-sighting rules:

- [`learning/AGENTS.md`](../../../experiments/01-agentic-build/learning/AGENTS.md) — the contract.
- [`learning/observations/_TEMPLATE.md`](../../../experiments/01-agentic-build/learning/observations/_TEMPLATE.md) — the exact file you write (frontmatter, `Saw.` / `Not claiming.`, no fix slot).

## Task

1. **Ground in the contract** above. The rules are theirs; this skill is only the procedure.
2. **Distill the corpus.** Run `python3 .claude/skills/agent-learning-mine/scripts/extract.py` (optionally `--since YYYY-MM-DD`). It turns the raw transcripts (1+ GB) into small per-session **digests** — human turns verbatim, `/overwhelmed` firings, and friction-flagged assistant lines — in a scratch dir outside the repo, and prints that path. It **fails loud** if the transcript format has drifted; if it does, stop and report — don't mine garbage.
3. **Read existing observations** in `learning/observations/` so you don't re-nominate what's already captured.
4. **Nominate candidates from the digests.** For a large corpus, fan out reader subagents (Sonnet is plenty — this is extraction against a clear rubric) over digest batches. Each candidate is one sighting + a verbatim quote as its evidence + a proposed `kind` — and **no fix** (defer to the template). You hold synthesis: dedup identical sightings (keep genuine cross-session repeats — those are the signal), drop weak or fix-smuggling ones, and **verify each quote against the digest** before trusting it.
5. **Write raw observation files** per the template — one file per sighting, immutable shape. Stamp the `run:` field with the session id it came from, marked as mined (the template allows a session id when there is no packet).
6. **Report and stop.** Do not consolidate or propose. Run `/agent-learning-review` separately when you want the clustering pass.

## Hard lines

- **Raw observations only** — no fix, no lesson, no routing decision (the template's three rules govern).
- **Fenced + best-effort** — the transcript store is an undocumented Claude Code internal; fail loud on drift, never silently emit empty or malformed cards.
- **Digests are scratch** — they hold transcript content; leave them in the temp dir, never commit them.
- **Mining sees only *noticed* friction** — say so in your report; a confident-but-wrong run no one caught leaves no trace, so absence from the log is not proof.

## Final response

End with:

- the scratch digest dir + how many sessions it distilled
- how many observations you wrote, by `kind`, and from which sessions
- the honest blind-spot line (mining sees only what was noticed)
- `No lesson was proposed and nothing was consolidated — run /agent-learning-review for that.`
