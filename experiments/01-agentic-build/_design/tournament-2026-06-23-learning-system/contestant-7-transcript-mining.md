# Contestant 7 — Transcript Mining ("the session is the lab notebook")

## Core idea

The richest learning signal isn't in dutiful hand-written notes — agents skip or sanitize those. It's in the **raw session transcripts**, which already exist on disk (confirmed: 460 JSONL files, 1.3 GB, May 30 → today, under `~/.claude/projects/…Web-Research/`) and already contain Brian's mid-session corrections *in his own words* — "verb runs is a little misleading," "your proposal is too long," "I don't love 'claim grammar' — find simpler language," plus every `/overwhelmed` invocation as a hard friction signal. So this design adds **no capture step at all**. A periodic, human-triggered `mine` pass reads transcripts, extracts *friction events* (a correction, a redo, an `/overwhelmed`, a reviewer catch), and writes them as raw, atomic, append-only **observation cards**. A separate `distill` pass clusters recurring observations and proposes rules — but only after asking the falsification question: *"would a rule here have prevented a real, repeated mistake?"* The mined stream is the divergent record the MRL retro begged for; the proposed rules are the clean layer downstream of it. Capture is free and honest because the agent isn't writing it — it's reading what already happened.

---

## A. Directory tree

Everything lives in-repo under the Agentic Build experiment, plus one tiny tool. No daemon, no DB, no living state — the transcripts are the upstream source of truth and they already exist whether or not we ever run the pass.

```text
experiments/01-agentic-build/learning/
  README.md                      # the contract: what each layer is, what writes/reads it (≤120 lines)
  observations/                  # RAW divergent stream — atomic, append-only, never merged
    2026-06-14-verb-runs-misleading.md
    2026-06-23-proposal-too-long.md
    2026-06-23-claim-grammar-jargon.md
    INDEX.md                     # one grep-friendly line per card (id · date · tag · headline · source)
  rules/
    ACTIVE.md                    # the consult surface — compact rules an agent reads at packet start
    RETIRED.md                   # pruned rules kept with their tombstone (why retired, when, by whom)
  brian/
    PREFERENCES.md               # learned-about-Brian: recurring corrections, taste, voice
  proposals/                     # one file per distill pass — the human decision surface
    2026-06-23-distill-pass-001.md
  mining/
    mine.py                      # the only code: transcript JSONL → candidate observation cards (stdout)
    coverage.md                  # which session-id ranges have been mined, to avoid re-mining (just a log)
```

Naming conventions (the string IS the contract):
- **Observation card**: `observations/<YYYY-MM-DD>-<kebab-slug>.md`, where the date is the *session* date, not the mining date. Immutable once written.
- **Rule id**: `R-<NN>` inside `ACTIVE.md`; rules are addressed by id forever, even after retirement (the id moves to `RETIRED.md`, never reused).
- **Tags** are a closed set, declared in `README.md`: `friction` (the loop fought the agent), `correction` (Brian changed the agent's output), `overwhelmed` (an `/overwhelmed` fired), `redo` (work thrown away and redone), `review-catch` (independent review caught a real miss). One tag per card — if two apply, the card splits.

Why this shape and not the proposal's single `LEARNING.md`: a single file with four sections fuses the divergent stream and the clean layer in one place, which is precisely how MRL's `triage.md` rotted (15-paragraph evidence logs growing under one item). Here the **raw stream is physically separate files** (can't be compressed in place — deleting divergence means deleting a file, which shows in `git`), and the **consult surface is a different file that an agent reads but never appends to**. The grain separation is structural, not a discipline you have to remember.

---

## B. Fully populated example files

### B1. `observations/2026-06-23-proposal-too-long.md`

```markdown
---
id: OBS-2026-06-23-proposal-too-long
tag: overwhelmed
session: 2bd9f1c4-…   # transcript file id
session_date: 2026-06-23
cwd: Web Research
git_branch: master
mined_at: 2026-06-23
mined_by: mine.py v1 + Sonnet pass
status: open            # open | clustered | promoted | dropped
cluster: null           # set by distill pass, never by mining
---

# Brian invoked /overwhelmed on a proposal that was too long

**What happened (verbatim trigger):**
> `/overwhelmed` — "and your proposal is too long - make it easier to read by humans.
> Keep it to 1,000-1,400 words. Plain English."

**Context:** Agentic Build learning-system proposal. The agent produced a long,
section-heavy proposal; Brian fired `/overwhelmed` to force a rewrite.

**Why this is a friction event, not a one-off:** `/overwhelmed` is a *named escape hatch*
— Brian built a skill specifically to dig out from over-built output. Each firing is a
labeled training example that the prior output over-reached.

**Would a rule have prevented it?** Candidate — but needs a second sighting before
promotion (see distill threshold). Possible rule shape: "Decision-surface docs default
to ≤1,400 words, plain English; earn more only with risk." Already half-present in
lead-context Size Defaults — so the real signal may be *the existing default isn't being
consulted*, which is a different fix than adding a new rule.

**Do NOT in this card:** propose the rule edit. That's the distill pass's job.
```

### B2. `rules/ACTIVE.md` (the consult surface)

```markdown
# Active rules — consult at packet start

Compact, evidence-backed rules an Agentic Build agent must read before working.
Each rule links to the observation cards that earned it. To challenge a rule, read
its evidence; to retire it, move it to RETIRED.md with a tombstone. Adding a rule
requires ≥2 observation cards OR one severe miss — see learning/README.md.

This file is READ by agents and WRITTEN only by an approved distill proposal. Agents
never append here mid-run.

---

## R-03 · Decision surfaces stay short and plain
Default Brian-facing decision docs to ≤1,400 words, plain English, skim-first.
Length reads as anxiety, not thoroughness. Earn more only when risk justifies it.
*Earned by:* OBS-2026-06-23-proposal-too-long, OBS-2026-06-18-decision-surface-bloat
*Promoted:* 2026-06-23 · proposal 001 · approved by Brian

## R-05 · No coined jargon in shared docs
When a doc introduces a coined term ("claim grammar", "coverage caveat"), prefer the
plainest existing word. Brian rejects neologisms on sight; they cost a rewrite.
*Earned by:* OBS-2026-06-23-claim-grammar-jargon, OBS-2026-06-10-vocab-pushback
*Promoted:* 2026-06-23 · proposal 001 · approved by Brian
```

### B3. `brian/PREFERENCES.md` (learns Brian, not the work)

```markdown
# What we've learned about Brian (from his own corrections)

Mined from recurring corrections across sessions. This is taste + voice + recurring
asks — the stuff a new agent should internalize to need fewer correction rounds.
Each line cites the observation cards behind it. Pruned like any rule.

- **Simplify, don't add.** When improving a doc/prompt/rule, his first move is "what can
  we cut / what does this replace," not "what to bolt on." Over-built output draws
  `/overwhelmed`. *(OBS-…-proposal-too-long, OBS-…-decision-surface-bloat, 4 more)*
- **Plain English over coined terms.** Rejects neologisms; asks for "simpler language."
  *(OBS-…-claim-grammar-jargon, OBS-…-vocab-pushback)*
- **Precision on shared vocabulary.** Catches when a word is overloaded ("verb runs is a
  little misleading" — user-facing verbs vs internal skills). Define terms before building
  on them. *(OBS-2026-06-14-verb-runs-misleading)*
- **Don't lose the divergent signal.** "I definitely don't want to lose these" — resists
  premature compression; wants the raw kept even when tidying. *(OBS-…-dont-lose-these)*

Confidence note: every line here is ≥2 sightings. One-offs stay in observations/, not here.
```

---

## C. Rules / lifecycle — what writes, reads, consolidates, prunes

Three verbs, all human-triggered. Nothing runs unattended.

| Step | Trigger | Who/what | Writes | Reads | Gate |
|---|---|---|---|---|---|
| **1. Mine** | manual `mine` (e.g. weekly, or after a rough session) | `mine.py` + a cheap Sonnet pass | new cards in `observations/` + `INDEX.md` line; appends to `mining/coverage.md` | transcript JSONL since last coverage mark | none — raw, append-only, cheap, reversible |
| **2. Distill** | manual `distill`, only when `observations/` has enough material | a reasoning agent (inherit main model) | one `proposals/<date>-distill-pass-NNN.md` | all `open` cards, `ACTIVE.md`, `PREFERENCES.md` | **human-gated** — proposal only |
| **3. Promote** | Brian approves a proposal | the approving agent | edits `ACTIVE.md` / `PREFERENCES.md`; flips card `status` | the approved proposal | Brian's approval IS the gate |
| **4. Consult** | every Agentic Build packet start | the working agent | nothing | `ACTIVE.md` + `PREFERENCES.md` | n/a |
| **5. Prune** | during distill, or on demand | distill agent proposes | moves rule → `RETIRED.md` with tombstone | rule + its cards | human-gated |

**What each layer may and may not do (the anti-rot rules):**

- **Mining never proposes a fix.** `mine.py` + the Sonnet pass emit observation cards only. The card template has a "Do NOT propose the rule edit here" line baked in. This is the structural defeat of *collapse-observation-into-solution*: the tool that captures literally cannot promote.
- **Observations are immutable and atomic.** One friction event per file. A card is never edited after writing (except `status` and `cluster`, set by distill). You cannot grow a 15-paragraph evidence log because new evidence = a new file, and the link between them is a `cluster` id, not an append. This is the structural defeat of *conflate-feedback-with-item-of-work*: feedback (cards) and the unit of work (a rule/proposal) are different files with different lifecycles. A card can be `dropped` without touching any rule; a rule can be retired without deleting its cards.
- **Distill clusters by reading, proposes by threshold.** It groups `open` cards, but it **must not merge them** — clustering sets a shared `cluster` id and leaves every card on disk. The clean view (a proposal) is downstream of the divergent record, never a replacement. This is the structural defeat of *over-compression*: the raw 345-equivalent never gets thrown away; a proposal is a *lens* over it, regenerable, and the cards outlive it.
- **Promotion threshold (in `README.md`, enforced by the distill agent):** a rule may be proposed only when **≥2 observation cards** show the same friction across **distinct sessions**, OR a single **severe** miss (something that could corrupt the store / a contract / live behavior). Most cards never promote — and that's success, not failure. The threshold is the structural defeat of *anchor-and-mirror*: a rule can't exist because one early draft said so; it needs independent re-occurrence, and the evidence (which sessions) is visible on the rule.
- **Pruning preserves evidence.** Retiring a rule moves it to `RETIRED.md` with a tombstone (why, when, who); its observation cards stay in `observations/`. Staleness is removed by humans (or proposed by distill when a rule's cards are all old and the friction stopped recurring), never silently.
- **Anti-anchor on the cards themselves:** `mine.py` runs against transcripts, not against existing cards, so a bad early card can't seed a template the next mining pass copies. Each pass re-derives from raw sessions.

**`mine.py` — what it actually does (kept dumb on purpose):**
1. Walk `~/.claude/projects/…Web-Research/*.jsonl` newer than the last `coverage.md` mark.
2. For each `type:"user"` line with real human text (drop `tool_result`, `<task-notification>`, `<system-reminder>`, attachments), flag *friction candidates*: lines matching the correction lexicon (`no,` / `not what` / `too long|heavy|much` / `simplify` / `instead` / `revert` / `actually` …) and **every** `/overwhelmed` invocation (a free, unambiguous label).
3. Emit each candidate with its surrounding turn, `sessionId`, `cwd`, `gitBranch`, `timestamp` as a draft card to stdout.
4. A cheap **Sonnet** pass (mechanical, per CLAUDE.md model guidance) judges each candidate: *is this a genuine friction/correction, or just conversational?* and writes survivors as cards. Reasoning is amortized to Sonnet because it's classification, not design.

---

## D. Worked example — the "headline field is the most misleading" finding, end to end

Anchor finding: Trustpilot score, Wayback `tenure_days`, SEC `total_hits` — the easiest-to-grep number is the most misleading one. In MRL this lived as ever-growing evidence-log paragraphs under MRL-008 and never graduated cleanly. Here is the same signal through this system. (Note: this finding originated in *run* artifacts, not Brian-corrections; it shows the design handles agent-discovered friction too, not just human corrections — `mine.py`'s lexicon and the `review-catch` tag fire on run-notes and Loop-2 reviewer turns in the transcript exactly as on Brian's turns.)

**Step 1 — Mine (capture).** Three separate sessions (runs 005, 006, 007) each contain a reviewer/agent turn flagging "the headline field misleads." `mine.py` catches three independent friction candidates across three session ids; Sonnet confirms each. Three cards land:

```markdown
# observations/2026-06-19-trustpilot-score-misleads.md
---
id: OBS-2026-06-19-trustpilot-score-misleads
tag: review-catch
session: 5a…07  · session_date: 2026-06-19 · status: open · cluster: null
---
# Trustpilot headline score misleads without its integrity siblings
> Loop-2 review: "score-only read says remedymeds 4.6 ≈ excellent and hims 3.0 is the
> problem; the review *bodies* show both have the same billing-after-cancel cluster.
> The gap is invitation posture, not quality."
**Would a rule have prevented a real mistake?** Yes — a downstream agent sorting by score
would rank backwards. Severity: medium (misleads a read, doesn't corrupt the store).
```
(plus `…-wayback-tenure-misleads.md` and `…-sec-total-hits-misleads.md`, same shape, different sessions.)

**Step 2 — Investigate.** The distill pass reads the three open cards, notices the shared shape, and asks *why*: each is a single greppable headline number standing in for a richer, less-greppable truth (score↔bodies, tenure↔snapshot-density, hits↔match/vehicle/CIK). The investigation is written into the proposal, not the cards.

**Step 3 — Verify.** Verification = the threshold check, made concrete: *are these the same friction in distinct sessions, and would one rule have prevented a real repeated mistake?* Three distinct session ids, three would-have-prevented "yes"es → verified as a real cross-run pattern, not one agent's bad day. The distill agent records the check in the proposal:

```markdown
# proposals/2026-06-23-distill-pass-002.md
## Cluster C1: "greppable headline number misleads"
Evidence: OBS-…-trustpilot-score-misleads, OBS-…-wayback-tenure-misleads,
          OBS-…-sec-total-hits-misleads  (3 cards, 3 distinct sessions)
Verified: same failure shape recurs independently; each would have caused a wrong read.
Proposed rule R-07 (below). Recommend: approve.
Anti-overfit check: this is a *reading discipline*, not a per-signal fork. Do NOT
propose three signal-specific rules (that's the policy-table-soup failure). One rule.
```

**Step 4 — Distill (generalize).** The proposal generalizes past the three instances to one rule:

```markdown
### Proposed R-07 · Don't read a signal by its headline field alone
A captured Signal's most greppable field (Trustpilot score, Wayback tenure_days,
SEC total_hits) is often its most misleading. Before a read uses confident language,
require the integrity sibling to travel with it (review bodies; snapshot density;
match/vehicle/CIK). Keep "trusted / established / funded" as labeled Judgments.
Earned by: the 3 cards above. One rule, not three — it's a reading discipline.
```

**Step 5 — Consult (compounding).** Brian approves. `R-07` lands in `ACTIVE.md`; the three cards flip to `status: promoted, cluster: C1`. The next signals-read packet reads `ACTIVE.md` at start, sees R-07, and writes the integrity sibling into the read *without re-deriving the lesson*. The friction stops recurring — which later lets a distill pass notice R-07's cards are all old and propose nothing further. Crucially: this rule is also generalizable to a real Truffle convention (it's already half-stated in SIGNALS.md), so the proposal can carry a secondary recommendation: "graduate R-07 into SIGNALS.md as a convention" — the product-gap-escapes-the-build-loop path.

Contrast with MRL: there, this same insight accreted as paragraph after paragraph under one never-graduating item, fused with its proposed-next-step, compressed in the steward's summary. Here it's three immutable cards → one verified cluster → one general rule, every hop inspectable in `git`.

---

## E. Map to the 5 stages and the 4 failure modes

**5-stage memory progression:**
1. **Fail** → `mine.py` captures the friction event verbatim from the transcript with full provenance (session, cwd, branch, timestamp). Richer than a hand-note because it's the actual exchange, not a sanitized recollection.
2. **Investigate** → the distill pass writes the *why* (shared mechanism) into the proposal, reading clustered cards together.
3. **Verify** → the threshold IS the verification: ≥2 distinct sessions + a "would-have-prevented" yes turns a guess into a checked cross-run fact; recorded in the proposal.
4. **Distill** → the proposal generalizes the cluster into one rule beyond the specific cases (R-07 is a reading discipline, not three signal forks).
5. **Consult** → `ACTIVE.md` (+ `PREFERENCES.md`) is read at every packet start; the agent applies the rule instead of re-deriving it. Compounding is visible: the friction's cards stop being added.

**4 failure modes — how each is structurally defeated (not just discouraged):**
1. **Collapse observation into solution** → the *capturing* tool (`mine.py`/Sonnet) is physically incapable of proposing a rule; cards carry a "do not propose here" line; only the separate distill pass proposes. Different tools, different files.
2. **Anchor-and-mirror** → mining re-derives from raw transcripts every pass, never from existing cards, so a bad first card can't become a template. Rules require ≥2 *independent* sessions, so one early draft can't self-promote.
3. **Conflate feedback with item-of-work** → observation cards (feedback) and rules/proposals (work) are different files with different lifecycles; a card drops without touching a rule, a rule retires without deleting cards. No 15-paragraph fused log is *possible* — new evidence is a new file linked by `cluster` id.
4. **Over-compression** → the raw stream is one-file-per-event, append-only, never merged; clustering sets an id and leaves every card on disk. The clean layer (proposals/rules) is a regenerable lens *downstream* of the divergent record. Deleting divergence would show as deleted files in `git`.

Honest gap: failure mode 2 is defeated for *rules* but the **distill agent itself can still anchor** on the framing of the last proposal it reads. Mitigation is weak (a "re-derive from cards, don't copy prior proposals" instruction); not structural. See self-critique.

---

## F. Self-critique — top 2 weaknesses

**1. The transcript corpus is real but fragile, opaque, and unowned.** Everything hinges on `~/.claude/projects/…/*.jsonl` — an *undocumented Claude Code internal* I confirmed by reading it, not a supported API. The schema (`type`, `message.content`, `cwd`, `isSidechain`) can change in any release; the files can be cleared; multi-machine work splits the corpus; and the `cwd`/`gitBranch` scoping only works because Brian runs Truffle from one path. **This is the load-bearing dependency and it is not under our control.** Mitigations and their cost: (a) treat `mine.py` as best-effort and *additive* — observation cards, once written, are normal in-repo markdown that survive even if transcripts vanish, so the durable layer doesn't depend on continued access (cheap, already true); (b) the `mine` pass can also ingest `git log` + packet `workflow_note`s as a fallback corpus when transcripts are unreadable (moderate — a second extractor); (c) version-pin the JSONL parser and fail loud when the schema drifts rather than mining garbage (cheap). What I *won't* do is copy transcripts into the repo — 1.3 GB of raw sessions would bloat git and leak content Brian never chose to commit. The honest statement: **the capture source is a found dependency, not a guaranteed one; the design degrades to "mine git log + notes" if it disappears, which is weaker but not broken.**

**2. Mining precision/recall is unproven and could drown distill in noise — or miss the quiet failures.** The correction lexicon catches loud frictions ("too long", `/overwhelmed`) well, but (a) it will surface false positives ("actually, that's perfect") that the Sonnet pass must filter, costing tokens and trust if it's sloppy, and (b) it is blind to *silent* failures — the agent that confidently did the wrong thing and Brian never corrected because he didn't notice. Transcript mining over-indexes on **noticed** friction; the most dangerous misses leave no correction in the transcript. Fixing (a) is cheap (tune the lexicon, let Sonnet be strict, accept lower recall early). Fixing (b) is genuinely hard and out of scope here — it needs the run-artifact / Loop-2-review signal (which `mine.py` does also read, partially covering it) or a replay/eval harness (the frame's parked could-have). I'd rather state the blind spot plainly than pretend transcript mining sees everything: **it learns from the mistakes that got caught, which is most of the cross-run value but not all of it.**

Smaller trade-off worth naming: this adds a second learning surface (mined cards) alongside the existing per-packet `workflow_note`. That's defensible only if cards *replace* the expectation that `workflow_note` carries cross-run learning — `workflow_note` stays a per-run convenience, and the cross-run job moves entirely to mining. If both try to do cross-run learning, we've added machinery without removing any. The rule: **mining is the cross-run learner; `workflow_note` is demoted to a per-run aid and is itself just another thing `mine.py` reads.**
