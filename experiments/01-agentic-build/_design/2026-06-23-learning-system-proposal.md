---
created: 2026-06-23
last_updated: 2026-06-23
authors: both
status: approved by Brian 2026-06-23
---

# Proposal: A learning loop for Agentic Build

*The concrete answer to the [Skills That Learn frame](../2026-06-23-learning-system-frame.md): how agents capture what a run taught us and turn it into a sharper system — without the learning step corrupting Truffle.*

## Context

We're trying to get to a world where agents can work on and improve Truffle autonomously, with minimal input required from Brian.

Today, Truffle has some per-run learning mechanisms (e.g. `site_notes`), but it has **no effective cross-run learning loop**. The one attempt — Market Read Lab's `triage.md` — is failing because it lets agents *collapse observations into solutions* and *over-compress* them (~345 raw observations tidied down to ~2). We want agents to make Truffle sharper over time, with Brian in the loop only for the calls that need him.

This shape came out of a 7-design tournament; all seven independently converged on the same skeleton.

## Recommendation

**A small folder of markdown — `learning/` — split into a cheap capture half and a gated review half.**

- **Capture (in-band, every run).** An agent writes *one short observation file* — what it saw, never a fix. Each agent writes its own file, so writes never collide and an agent can't anchor on someone else's entry.
- **Review (out-of-band, runs a skill).** A review pass reads *all* observations, clusters repeats, and **proposes** lessons. You approve. An approved lesson then sharpens the relevant skill / verb / convention.

The one rule the whole design rests on: **an observation can never hold a fix, and is never rewritten** (save a one-time `graduated-into` stamp when it graduates — see Key design decisions). That structurally prevents the failure that killed the last system — feedback and fixes physically can't fuse (no fix slot), and nothing compresses the raw record away (immutability is convention until the pre-commit check lands).

We considered many approaches, and are recommending the lightest version: it defeats all four frame failure modes at the lowest cost, it's enforced by file shape (not by hope), and it fits Truffle's existing instincts — file-first, git-tracked, "invest in conventions", "propose don't write," no living infrastructure. The richer designs are where this *grows*, not where it *starts*.

## Scope & routing

**The learning system never changes Truffle and never decides a fix at capture time.** It captures observations and surfaces clusters; the change happens elsewhere, routed by what the learning is *about*.

For v0 it captures observations from **Agentic Build runs**, in **both subjects** — capture stays dumb, and the subject is decided later, at review:

- **About Truffle** (a recipe misleads, the store can't answer X, `/research-company` misses Y) → the review surfaces a candidate, and it enters **[Agentic Build](../../01-agentic-build/README.md)'s workflow** (frame → proposal → review → implement → verify → graduate). The learning system feeds the queue; *Agentic Build* changes Truffle. This just becomes a second discovery channel — gaps caught *while building*, alongside Market Read Lab's gaps caught *while using Truffle*.
- **About Agentic Build itself** (a step got skipped, the same correction keeps recurring, the process feels clunky) → a **light internal edit** to its own skills/docs, a second look, no change-packet. The ceremony is for changing the engine, not for the build system improving itself.

So "graduate a lesson" isn't one thing: *route to the build workflow* (about-Truffle) or *light edit* (about-the-process). Same capture, two destinations.

*Deferred should-have: an about-Truffle lesson currently enters the build queue directly; routing the bigger, prioritization-worthy gaps onward to `BACKLOG.md` / the Notion roadmap (the frame's "product gaps escape the build loop") isn't wired yet.*

**This `/learnings` approach is meant to be the canonical pattern — not one of several.** We expect it to prove out, and then likely (a) move `learning/` out of `experiments/01-agentic-build/` into a first-class home, and/or (b) fold its conventions into Truffle's rules so other verbs inherit it. The goal is **one** learning system — so Market Read Lab's failing `triage.md` should be reworked onto this pattern, not maintained alongside it.

## What it looks like

The folder (living in `experiments/01-agentic-build/learning/` for now — see Questions):

```
learning/
  README.md       — human orientation (plain English, diagrams welcome)
  AGENTS.md       — agent orientation; auto-loaded when an agent touches the folder. Tight, points outward.
  CLAUDE.md       — one line: @AGENTS.md  (so Codex and Claude Code both pick it up)
  observations/   — one file per observation; agents add, never edit
    2026-06-23-cohort-count-grep-inflation-7f3a.md
  lessons.md      — reviewed + decided patterns (the curated short list)
  brian.md        — your preferences, learned over time
  reviews/        — notes from each review pass (what it read, proposed, and skipped)
```

**The lifecycle**, mapped to the frame's five stages:

1. **Capture (Fail).** A run hits friction → writes one observation file. No fix in it.
2. **Review (Investigate).** You run the review skill → it clusters repeats across runs, writes a `reviews/` note ("read 41, proposed 1, left 38 untouched"), and adds a *proposed* entry to `lessons.md`.
3. **Approve (Verify).** You accept / park / drop the proposed lesson. This is the only human gate.
4. **Sharpen (Distill).** The accepted lesson is written into the skill/recipe it improves.
5. **Consult.** The next run reads the now-sharper skill and doesn't repeat the mistake.

A few specifics:

- **Observation filenames:** `YYYY-MM-DD-short-slug-xxxx.md` — date sorts them, the slug lets you skim, the short random tag means two agents writing at once never clash.
- **`AGENTS.md` is the forcing function.** Auto-loading the rules whenever an agent enters the folder is *why* capture stays honest — the same reason `site_notes` works and `workflow_note` rots. Keep it tight and pointing outward (to the frame, the lesson format), not a manual.
- **The review pass is a skill you run** (later trivially a scheduled routine). It only ever *proposes*; it never edits a live skill itself.

<details>

  <summary>Worked examples — both routes, end to end</summary>

  **Route A — a learning *about Truffle* (→ the build workflow).** An Agentic Build agent is working a packet on the `/query-companies` verb. Along the way — *unrelated to its task* — it notices a real bug: a cohort census count is inflated because the recipe greps the whole file instead of the frontmatter, so any company that merely *mentions* the category gets counted. Fixing it is out of scope for its packet, so it doesn't — it just writes `observations/2026-06-23-cohort-count-grep-inflation-7f3a.md` — *what I saw, no fix.* At review, this clear bug earns a candidate on a single sighting (it needn't recur). Because it's *about Truffle*, the candidate enters **Agentic Build's workflow** — framed, proposed, reviewed, implemented, verified — and only then does the fix land. The trail stays intact: fix diff ↔ build packet ↔ lesson ↔ the observation.

  **Route B — a learning *about Agentic Build itself* (→ light edit).** An agent notices it keeps getting corrected for adding fields instead of simplifying. It writes an observation — *what I saw, no fix.* The review pass clusters it with two prior sightings and proposes a lesson. Because it's *about the process*, the fix is a **light edit** to an `agent-build-______` skill (or `lead-context.md`) with a second look from a separate sub-agent — no change-packet formality needed.

  Contrast both with the real `triage.md` — e.g. its headline-field finding (MRL-008) accreted ~15 paragraphs fused to a proposed fix and never graduated, because feedback and fix lived in one record.
</details>

## Key design decisions

The load-bearing rules and decisions that keep this from rotting into the last system. (Exact field formats, tag sets, and the review-skill prompt are build details — they live in the folder's `AGENTS.md`, not here.)

- **The Anti-Merge Law.** Compression happens by *adding* a lesson that points at observations — never by shrinking, merging, or summarizing them. A review pass that absorbs observation text into a tidy summary breaks the rule even if it deletes nothing. This single invariant is what makes the 345→2 triage collapse from Market Read Lab structurally impossible.
- **Observations are immutable — with one exception.** Once written, an observation is never edited or deleted. The *only* permitted touch is a `graduated-into: <lesson-id>` stamp added when its lesson graduates (after Brian's gate, not at propose) — so a reviewer can see at a glance which raw notes are already spent, without rewriting the note. A note inside a still-proposed (or parked/dropped) lesson stays unstamped and available.
- **An observation records what was seen and what it is *not* claiming — never a fix.** It has room for the sighting and an explicit "not claiming X" line, and no slot for a proposed solution. Append-only is held by convention today; the planned mechanical upgrade is a pre-commit check that rejects edits to existing observations — it ships with the review skill, the way Truffle treats lint gates.
- **A lesson must earn graduation.** It graduates only on one of: the same thing in ≥2 independent runs, a Brian correction, an independent review catch, or one miss severe enough to justify a guardrail. And it must pass two cheap self-tests first — *state it without naming a run or company* (or it isn't a rule yet) and *what does it replace?*.
- **Lessons can be retired — never silently.** When a graduated lesson proves wrong, you challenge it at the skill (revert the diff) and log a fresh observation saying so; the trail stays intact. `lessons.md` rows carry a state (`proposed → accepted → graduated | parked | dropped`), and dropped rows stay — they record a decision.
- **`brian.md` is a protected lane.** Your recurring preferences and corrections live there, fed by `brian-correction` observations — kept out of `lessons.md` so "learn Brian" doesn't dilute into general process lessons.
- **The review fires on a nudge, not a hope.** v0's starting convention is a packet-close prompt ("≥5 observations since the last review?"), so consolidation can't silently fall behind the way the last steward did. It graduates to a scheduled routine when volume earns it.

## Additional options considered

The tournament's seven approaches, and why the recommendation wins now. We kept the best idea from several and grafted them in (last column).

| Approach | The core bet | Verdict |
|---|---|---|
| **Two-ledger (recommended)** | Smallest thing that beats all four failures; enforced by file shape | **Build this** |
| Faithful Claude "Dreaming" port | Cleanest mental model (in-band vs out-of-band) | Adopt its *framing*; skip its 5-folder weight |
| Two-clock | Rigorous "never merge the raw notes" law + audit minutes | **Graft** the audit minutes (`reviews/`) |
| Transcript-mining | Learn Brian from corrections already on disk | **Graft** as an optional, fenced feeder |
| Conventions-as-product | Make the convention agents copy the thing that improves | Right instinct; lives in *how lessons graduate* |
| Role/incentive via `.claude/agents` | Separate "observer" and "proposer" agents | Over-built for now (4 agents at 3 packets) |
| Queryable structured log | Consolidation as a query, not a re-read | Premature schema; revisit when the corpus is large |

Full reasoning and the three independent judges: [tournament folder](tournament-2026-06-23-learning-system/).

## Questions to address

**Resolved (by the tournament + discussion with Brian):**

- **One file or a folder?** A folder, one file per observation — for concurrency safety and to stop agents anchoring on each other's notes.
- **Does every change need a change packet?** No — only changes that touch live Truffle. Internal build-system tweaks stay light.
- **Can an observation hold a fix?** No. That separation is the core defense, enforced by file shape.
- **Can we actually "learn Brian"?** Yes — ~460 session transcripts on disk already hold your verbatim corrections and every `/overwhelmed`. An optional, fenced `mine.py` can feed those in as observations; the markdown layer survives if that source ever vanishes.
- **Both subjects, or just the process?** Both — *about-Truffle* and *about-Agentic-Build*. The subject decides routing, not whether something is captured (see Scope & routing).
- **Rework Market Read Lab's learning system?** Yes — migrate its failing `triage.md` onto this pattern rather than run two disjointed systems. (Timing is open, below.)

**Open (we won't fully know until we build / run it):**

- **When and how it becomes canonical.** We expect to move `learning/` out of the experiment into a first-class home and fold its conventions into Truffle's rules as it proves out (see Scope & routing). The *trigger and exact shape* — and the timing of the Market Read Lab migration — are open.
- **Whether the cadence nudge is enough.** v0 starts with the packet-close nudge (Key design decisions); the open question is whether that holds or we move to the scheduled routine sooner. Cadence is the one real single point of failure — it's how the last steward fell behind.
- **When findability needs more.** A flat `lessons.md` + a growing `observations/` folder is fine now; at scale it may want "sharding" by month or a light tag (an `INDEX.md` of one grep-line per observation is the cheap first step). Don't pre-build it.
- **The capture half is blind to silent failures.** It only sees what an agent notices and reports honestly — a confident-but-wrong run no one caught leaves no observation. Absence from the log isn't proof the system is clean.
- **Whether `mine.py`'s transcript dependency holds** across Claude Code updates (it reads an undocumented internal — hence "optional, fenced, degrade gracefully").
- **A safe auto-apply class** — lowest-risk doc edits, applied without a gate by reusing lead-context's risk rules — is anticipated but deferred; the natural pressure-valve if approval fatigue shows up.

## References

- [Frame: Skills That Learn](../2026-06-23-learning-system-frame.md) — the problem this solves.
- [Tournament + SYNTHESIS](tournament-2026-06-23-learning-system/SYNTHESIS.md) — the 7 designs, 3 judges, and the decision surface.
- [Anthropic "Dreaming" talk](https://www.youtube.com/watch?v=tTcxVv8HHNw) — the in-band / out-of-band framing this borrows.
- [Operating Principles](https://app.notion.com/p/38684b6d1f49806a8922e20061e644fa) — "Learning loops," "Invest in conventions," no living infrastructure.
- Supersedes the earlier combined draft at [`../2026-06-23-learning-system-proposal.md`](../2026-06-23-learning-system-proposal.md).
