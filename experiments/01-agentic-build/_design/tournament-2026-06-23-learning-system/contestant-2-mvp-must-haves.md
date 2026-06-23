# Contestant 2 — The Two-Ledger MVP

*Tournament entry: the smallest system that genuinely defeats all four failure modes and serves all four Must-Haves. Nothing more.*

## Core idea

**One append-only log of observations that is never edited, and one human-gated list of work that points back at it.** An agent's only job at the moment of learning is to *append a raw observation* — it is structurally forbidden from writing a fix. Work items are minted by a separate, deliberate **harvest** pass that links observations into clusters; a fix is a normal change-packet that cites them. Two files, one rule — `observations.log.md` is write-once; everything else is downstream of it and regenerable. That single asymmetry (append-only evidence ⟂ editable work) is what MRL fused into one file and is what killed it.

The whole design is three files and one verb. Everything else is a seam I name but do not build.

---

## A. Directory tree

```text
experiments/01-agentic-build/
  learning/
    observations.log.md      # APPEND-ONLY. Raw observations. Never edited, never deleted, never reordered.
    work.md                  # Human-gated. Open work items (clusters of obs) + their state. Editable.
    RULES.md                 # ~40 lines. The contract: who appends, what harvest does, what graduates. Read by every agent.
```

That is the entire system at v0. Three files, one folder.

- `observations.log.md` is the **divergent stream** the MRL retro begged for ("keep a divergent idea stream that never gets merged"). It is the source of truth. It only ever grows.
- `work.md` is the **clean backlog**, explicitly *downstream* of the log. It can be wrong, pruned, reframed — because the evidence behind it is safe in the log and can never be tidied away.
- `RULES.md` replaces the lead-context "Learning Loop" section, the proposal's four-section `LEARNING.md`, and MRL's `triage.md` operating-convention preamble — three scattered descriptions of the loop collapse into one.

**What this folder replaces:** MRL's `triage.md` (single fused file), the proposal's `LEARNING.md` (four-section mega-file), and the per-packet `workflow_note` graveyard (the lessons that "stay buried in one packet file"). The log promotes `workflow_note` from a packet field to a first-class append target.

**Graduated rules don't live here.** A distilled rule lands in the skill/convention it sharpens (`.claude/skills/<verb>/`, a recipe, lead-context). The learning folder holds *evidence and pending work*, never the canonical rule — so it cannot bloat into a parallel policy manual (the explicit Non-Goal). The skill is where the lesson is consulted; `work.md` just records *that* it graduated and points at the diff.

### The append-only discipline, made mechanical

`observations.log.md` is protected by one git pre-commit check, not a daemon:

```bash
# scripts/check_obs_append_only.sh  (~15 lines; runs in existing pre-commit gate)
# Fails the commit if any EXISTING line of observations.log.md changed.
# New lines appended at EOF are fine. Edits/deletions/reorders are rejected.
git diff --cached -U0 -- experiments/01-agentic-build/learning/observations.log.md \
  | grep -E '^-' | grep -v '^---' && { echo "observations.log.md is append-only"; exit 1; } || exit 0
```

This is the cheapest possible enforcement of the one rule the whole design rests on. No service, no scheduler — just the convention made into a lint, exactly the engine's "the string IS the contract" posture. (If even this is too much for v0, the rule lives in `RULES.md` and is enforced by review. The check is the upgrade, not the foundation.)

---

## B. Fully-populated example files

### `observations.log.md`

```markdown
# Agentic Build — Observation Log

APPEND-ONLY. Add at the bottom. Never edit, reorder, or delete a line above this one.
One observation = one block. No fixes here — a fix is a work item (work.md), not an observation.
Format: `## OBS-NNN` + 5 fields. If you're proposing a solution, you're in the wrong file.

---

## OBS-014
- when: 2026-06-20 · run 005 (trustpilot signals read)
- who: read-agent
- saw: I sorted brands by Trustpilot trust_score and concluded remedymeds (4.6) was trustworthy and hims (3.0) was the problem. The review *bodies* show both have the same dominant complaint: billing-after-cancel. The score gap was invitation posture, not quality.
- felt: the easiest field to grep was the one that misled me. I trusted the headline number because it was the only number.
- kind: friction
<!-- never edited below this line -->

## OBS-019
- when: 2026-06-20 · run 006 (wayback tenure read)
- who: read-agent
- saw: Used Wayback `tenure_days` as "how established is this brand." onemedical showed snapshot_count going DOWN and last_seen moving backwards with an identical digest — CDX nondeterminism. tenure_days measures the archiver's crawl, not the brand's age.
- felt: same shape as OBS-014 — reached for the headline number, it lied. Wanted a corroborating field (WHOIS reg date) and there wasn't one.
- kind: friction

## OBS-023
- when: 2026-06-20 · run 007 (sec-edgar funding read)
- who: read-agent
- saw: SEC `total_hits` read as "funding footprint." A common brand name (multiple CIKs, name collisions, existence-only matches) inflates hits with no relation to capital raised. directmeds "funded" read was a false positive.
- felt: third time this run-family. Grep-the-headline-number → wrong. Starting to feel like a pattern, not three accidents.
- kind: friction

## OBS-024
- when: 2026-06-21 · packet 03 close (visual-evidence skill)
- who: build-lead
- saw: Brian cut my proposal from 3 new fields to 1 and said "what does the other two replace? if nothing, they're not earning it." I'd added them because they were cheap, not because a question needed them.
- felt: I default to additive. Brian's correction was "subtract first." This is the second time he's said a version of this.
- kind: brian-correction
```

Note what is **absent**: no `priority`, no `status`, no `proposed_next_step`, no `evidence_summary`. The log holds *what was seen and felt*, full stop. The instant you add a `proposed_next_step` field to an observation you have re-built MRL-002, where the fix lived on the evidence and the two grew together until neither could close. The five fields are deliberately all backward-looking (what happened) — none is forward-looking (what to do).

### `work.md`

```markdown
# Agentic Build — Work

Open work items. A work item is a *cluster of observations worth acting on*, plus a decision.
Created only by a harvest pass or a Brian call — never auto-minted at observation time.
An item links observations; it does NOT copy their evidence. Evidence stays in the log.

States: `proposed` → `accepted` → `graduated` | `parked` | `dropped`.
Graduated = the lesson is now in the skill/convention itself (link the diff). Parked = real but waiting. Dropped = decided not worth it (keep the row, it records the decision).

---

## W-002 — Headline signal fields mislead a naive read
- state: accepted (2026-06-22, Brian)
- observations: OBS-014, OBS-019, OBS-023  (+ harvest 2026-06-22 flagged 2 more in raw runs)
- pattern: across Trustpilot score / Wayback tenure_days / SEC total_hits, the *easiest-to-grep* field is the most misleading; each needs an integrity sibling or a corroborating source to be read safely.
- decision: graduate as a reading-discipline line in the signals query recipe. NOT a new schema field, NOT a score, NOT a monitor.
- graduation: → `QUERYING.md` Recipe (signals-read): "headline signal fields travel with their confound sibling; never read a lone number as a verdict." Diff: `<commit-sha>`.
- next: close to `graduated` once the recipe line lands and one later read consults it.

## W-005 — Build-lead defaults to additive, not subtractive
- state: proposed (2026-06-22, harvest)
- observations: OBS-024  (1 sighting; watching for a 2nd before graduating)
- pattern: agents add fields/rules/stages because they're cheap, not because a question needs them. Brian repeatedly corrects this ("what does it replace?").
- decision: PENDING. Candidate: add a one-line "subtract-first" gate to the proposal template's decision surface. Hold for a 2nd sighting per the graduation threshold.
- graduation: —
- next: harvest re-checks next pass; graduate on 2nd independent sighting OR one more Brian correction.
```

`W-005` is the design earning its keep on the "**learn Brian**" requirement: a Brian-correction observation (`kind: brian-correction`) is a first-class input, and once it recurs it graduates into the *template agents anchor on* — so Brian's taste gets encoded structurally instead of re-corrected every packet.

### `RULES.md`

```markdown
# Agentic Build — Learning Loop (the whole contract)

Three files. One rule: the log is append-only; everything else is downstream of it.

## observations.log.md — the divergent stream
- WHO writes: any agent, at packet close or mid-run, when something taught us something real.
  Also the harvest pass, when re-reading raw runs surfaces an observation no one logged.
- WHAT: one OBS block, 5 fields (when/who/saw/felt/kind). Backward-looking only.
- kind ∈ {friction, wish, risk-miss, brian-correction, heuristic-worth-keeping}.
- HARD LINE: no fixes, no proposals, no priorities here. If you're writing what to DO, stop — that's work.md, and it's gated.
- APPEND-ONLY: never edit/reorder/delete an existing line (pre-commit check enforces). Wrong obs? Append a correcting OBS that links it. Never rewrite history.

## work.md — the clean backlog (downstream, editable, prunable)
- WHO writes: the harvest pass (proposes), Brian (accepts/parks/drops). Agents do NOT mint work items at observation time.
- A work item LINKS observations by id; it never copies their evidence. The log stays the single source of evidence.
- A fix is a normal change-packet that cites the work item. Skill/template/recipe edits are PROPOSED, never silently applied.

## Harvest — the consolidation pass (manual verb, not a daemon)
- WHEN: after ~5 new packets, OR after any painful failure, OR when Brian asks. Never on a clock.
- DOES: read the RAW log (not work.md) end to end. Cluster repeats into proposed work items. Cut nothing from the log.
- MUST NOT over-compress: every cluster keeps ALL its OBS ids. If two obs disagree, that's signal — make two clusters, not one averaged one.
- Output: new/updated rows in work.md (state: proposed) + a 5-line harvest note appended to the log itself (so the harvest is itself auditable).

## Graduation threshold (when an observation earns a rule)
A work item may graduate (proposed → accepted → into a skill/convention) when ONE holds:
- the same friction appears in ≥2 packets/runs (count the OBS ids, not paragraphs);
- Brian explicitly corrects the process or judgment;
- independent review catches a material miss;
- the miss is severe enough that one occurrence justifies a guardrail.
Most observations never graduate. Deleting a weak *work item* is fine (keep the row, mark `dropped`). Deleting an *observation* is never fine.

## Staleness
- The LOG is never pruned (it's history; git already dates it).
- work.md: `dropped`/`graduated` rows move under a `## Closed` heading after harvest; never deleted (they record a decision).
- A graduated rule that later proves wrong is challenged AT THE SKILL (revert the diff), and a fresh OBS is logged saying so. The trail is: skill diff ↔ work item ↔ observations.
```

---

## C. Rules / lifecycle

| Step | Trigger | Who/what | Writes | Gated? |
|---|---|---|---|---|
| **Append** | packet close, or any run, or mid-task friction | any agent | one OBS block to `observations.log.md` | no (append is safe — it's just evidence) |
| **Harvest** | ~5 packets, painful failure, or Brian asks | a `/agent-build-harvest` invocation (manual) | proposed work items in `work.md` + a harvest note in the log | no (proposing is safe) |
| **Accept/Park/Drop** | Brian reviews `work.md` | Brian | work item state | **human-gated** |
| **Graduate** | accepted item with a clear fix | a normal change-packet | the diff into the skill/recipe/template + `graduation:` link in `work.md` | **human-gated** (it's a change packet) |
| **Consult** | next run of the affected verb | any agent | nothing — it reads the now-sharper skill | n/a |
| **Prune** | next harvest | harvest pass | moves closed rows under `## Closed`; never touches the log | no |

**The one asymmetry that makes it safe to delegate:** appending and proposing are *write-cheap and reversible* — agents do them freely. Accepting and graduating *change the system* — only Brian/a change-packet does them. An agent steward can run the whole left side autonomously and never corrupt anything, because its only powers are "add evidence" and "suggest" — exactly the powers that can't metastasize. That is the minimum that makes the steward role safe to delegate (an open question in the frame).

**Why nothing runs continuously:** harvest is a verb you invoke, like `/research-company`. No daemon, no scheduler, no standing state. "Automatic" = automatically *surfaced* by the next harvest, never automatically *applied*. Fully inside "no living infrastructure."

---

## D. Worked example — the headline-field finding, end to end

**The anchor observation:** *"the easiest-to-grep headline field is the most misleading one"* (Trustpilot score, Wayback `tenure_days`, SEC `total_hits` each mislead a naive read).

**Stage 1 — Fail / Capture.** Three runs each hit it independently. Three separate appends to the log — *not* one merged entry:

```markdown
## OBS-014  (run 005) saw: sorted by trust_score, concluded remedymeds trustworthy / hims the problem; bodies show identical billing complaints. felt: trusted the headline number because it was the only number. kind: friction
## OBS-019  (run 006) saw: tenure_days read as brand age; CDX nondeterminism, it measures the archiver. felt: same shape — headline number lied. kind: friction
## OBS-023  (run 007) saw: SEC total_hits read as funding; name-collision false positive. felt: third time. starting to feel like a pattern. kind: friction
```

Critically: at this stage **no fix exists anywhere**. No `proposed_next_step`. This is exactly where MRL went wrong — its template *asked* for `proposed_next_step` at capture time, so OBS-014's equivalent was born fused to "add a QUERYING recipe," and the fix and evidence then grew together for 15 paragraphs. Here, the three observations are inert evidence. They can't collapse into a fix because the file they live in forbids fixes.

**Stage 2 — Investigate.** Harvest runs (after ~5 packets). It reads the raw log, sees OBS-014/019/023 rhyme, and re-reading the raw runs flags 2 more the agents missed (the anti-over-compression rule: harvest *adds* to the divergent stream, it never subtracts). It writes a **proposed** work item:

```markdown
## W-002 — Headline signal fields mislead a naive read
- state: proposed (2026-06-22, harvest)
- observations: OBS-014, OBS-019, OBS-023 (+2 from raw runs)
- pattern: easiest-to-grep field = most misleading; each needs an integrity sibling or corroborating source.
- decision: PENDING (candidate: a reading-discipline recipe line; explicitly NOT a schema field/score/monitor)
```

The investigation (the *why*: "the convenient grain is the wrong grain") lives in the work item's `pattern:`, where it can be reframed freely — because the raw evidence is untouchable in the log.

**Stage 3 — Verify.** Brian reviews `work.md`. Five linked OBS ids across three signal families clear the ≥2-packets threshold. He flips it to `accepted` and writes the boundary that prevents the MRL disease — *recipe line, not a field, not a score, not a monitor*:

```markdown
- state: accepted (2026-06-22, Brian)
- decision: graduate as a reading-discipline line in the signals query recipe. NOT a new schema field, NOT a score, NOT a monitor.
```

The verification is a *checked fact* because it's a human decision on counted, linked evidence — not a guess, not an agent's averaging of 15 paragraphs.

**Stage 4 — Distill.** A change-packet (gated, like any change) writes the general rule into the convention agents actually read:

```markdown
# QUERYING.md, signals-read recipe — appended line:
**Headline signal fields travel with their confound sibling.** trust_score needs paid-profile/volume
flags; tenure_days needs snapshot-density/WHOIS corroboration; total_hits needs CIK/match-type.
Never read a lone headline number as a verdict — it is the field most likely to mislead.
```

`work.md` records the graduation with the diff sha. The *rule* now lives in the recipe (where it's consulted), not in the learning folder (which keeps only the evidence + the pointer). The learning folder cannot bloat into a policy manual because the policy lives elsewhere.

**Stage 5 — Consult.** The next signals read opens `QUERYING.md`, hits the line, and never re-derives the lesson. Compounding achieved: run 005 paid for the mistake once; every read after consults the rule for free. If the rule ever proves wrong, the trail is intact — `QUERYING.md` diff ↔ W-002 ↔ OBS-014/019/023 — revert the diff, log a fresh OBS, done.

**Contrast with what actually happened in MRL:** this exact finding is real in `triage.md` — it's MRL-008, which by 2026-06-20 carried *fourteen* dated Evidence Log paragraphs, spawned sub-branches, and **still hadn't graduated**. The fix and the evidence were the same object, so it could neither close nor compound; it just accreted. Same finding, two ledgers: it graduates in four moves and the evidence is still all there.

---

## E. Map to the 5 stages and the 4 failure modes

**5-stage memory progression:**
1. **Fail** → an OBS block appended to the log. Rich (saw + felt), dated, attributed, and *isolated* (no fix attached).
2. **Investigate** → harvest clusters OBS into a work item's `pattern:` field; the *why* lives in editable work, the *what-happened* stays immutable in the log.
3. **Verify** → Brian flips `proposed → accepted` against counted, linked OBS ids — a human decision on evidence, not an agent's compression.
4. **Distill** → a gated change-packet writes the general rule into the skill/recipe/template; `work.md` links the diff.
5. **Consult** → next run reads the sharpened convention, not the learning folder. Compounding by construction.

**4 failure modes — how each is structurally defeated:**
1. **Collapse observation into solution** → the log file *physically cannot hold a fix* (5 backward-only fields; `RULES.md` hard line; the "wrong file" guard). Fixes only exist in gated work. This is the load-bearing defense.
2. **Anchor-and-mirror** → there is no per-case template to mirror. The log format is 5 fixed fields that can't encode a solution; graduated rules live in the skill, so the thing agents anchor on is the *curated convention*, which is exactly where you *want* anchoring. A bad OBS can't become a de-facto standard because an OBS isn't a standard.
3. **Conflate feedback with item-of-work** → this is the *entire architecture*: two files, append-only evidence ⟂ editable work, linked by id, never copied. Dedupe/graduate/close happen on work items; evidence is immutable. (Directly fixes MRL's fused-record disease.)
4. **Over-compression** → the log is append-only and never pruned; harvest is *forbidden from cutting it* and required to keep every OBS id. The clean view (`work.md`) is explicitly downstream of the divergent stream that the idea-harvest proved was the cure (345 obs were recoverable *because the raw runs were never edited* — this makes that property a rule instead of luck).

---

## F. Self-critique

**Weakness 1 — Findability degrades as the log grows.** At ~30 OBS this is a clean append file; at ~800 it's a wall of text and an agent can't reliably tell its new friction echoes OBS-014 from 600 lines up. Harvest catches cross-run patterns only as well as the harvester can hold the log in context. **The seam (named, not built):** when the log gets long, shard by month (`observations/2026-06.log.md`) and add a one-line `grep`-able `tags:` field to each OBS — both are *additive to the same format*, no redesign. **Cost to fix now:** a tagging vocabulary I'd be inventing before the corpus tells me the real axes — premature, and it risks the taxonomy-sprawl the engine fights. So I deliberately defer it; the risk is a painful harvest or two in the gap before I shard. Honest call: right for a thin corpus, will need the seam opened within a few dozen OBS.

**Weakness 2 — Harvest is a human-discipline single point of failure.** Nothing *runs*, so if no one invokes harvest, observations pile up un-clustered and the loop silently stalls — which is precisely how MRL's steward fell behind. The append side is robust (cheap, safe, enforced by lint); the *consolidate* side depends on someone remembering to run a verb. **What fixing it would cost:** the obvious fix — a scheduled harvest — is exactly the "standing infrastructure / daemon" the frame rules out, so I won't. The honest mitigation is a *prompt*, not a process: the packet-close checklist ends with "≥5 packets since last harvest? run `/agent-build-harvest`," making the trigger impossible to miss without buying automation. It's a nudge, not a guarantee. I'm accepting a real reliability gap to stay inside "no living infrastructure" — and I think that's the right trade for Truffle, but it *is* a trade, and a busier future may force revisiting it (the bonus auto-apply class is the natural place that pressure resolves).

**Third, named honestly:** the design assumes the *raw Claude Code session transcript* isn't the evidence corpus — it builds on packet artifacts + deliberate appends (the frame's open question). If transcripts turn out richly readable, an OBS could cite a transcript span instead of being hand-written, raising capture fidelity. That's strictly additive (another thing the `saw:` field can point at), so it doesn't threaten the shape — but it means today's capture is only as good as what an agent bothers to write down, which is the same forcing-function dependency that makes `site_notes` work and `workflow_note` rot.
