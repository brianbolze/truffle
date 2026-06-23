# Contestant 6 — The Queryable Structured Log

## Core idea

**The raw observation log is append-only and never rewritten — consolidation is a `grep`, not a merge.** Each observation is a tiny markdown file with closed-set frontmatter (`kind / area / severity / status / run`), so finding "the same thing happened three runs ago" is a query over the log, not a destructive re-read that an agent has to summarize. Truffle already believes *conventions are infrastructure, queryability is the product* — this design applies that exact principle to learnings: you defeat over-compression by **never compressing the source**, and you defeat solution-collapse by making the observation file structurally incapable of holding a fix (the fix lives in a separate `lessons/` object that *links back* to the observations as evidence).

The whole model is three nouns and one verb:

> **Observations** (raw, append-only, queryable) → a **consolidation query** surfaces a cluster → a **Lesson** (the distilled rule, evidence-linked, never the same file as its observations). The verb is *query*, never *rewrite*.

---

## A. Directory tree

Everything lives in-repo under the build experiment, git-tracked, plain markdown. No index that must stay running — any "view" is a regenerable query result.

```text
experiments/01-agentic-build/learning/
  README.md                      # the contract: schema, closed sets, how to query (the ONE doc agents read)
  obs/                           # the raw log — append-only, ONE file per observation, NEVER edited after write
    2026-06-19-mrl-headline-field-misleads-trustpilot.md
    2026-06-19-mrl-headline-field-misleads-wayback.md
    2026-06-19-mrl-headline-field-misleads-sec.md
    2026-06-21-ab-scope-drift-caught-in-review.md
    2026-06-23-ab-brian-correction-simplify-not-add.md
    ...
  lessons/                       # distilled rules — the ONLY place a fix/rule lives; each links its obs evidence
    L001-headline-signal-needs-integrity-sibling.md
    L002-prefer-prune-over-append.md
    ...
  consult.md                     # GENERATED digest: active lessons only, the thing the next run reads first
  scripts/
    learn.py                     # write an obs / new lesson; query the log; regenerate consult.md
  queries/                       # saved named queries (a query IS a convention) — optional, grows lazily
    open-clusters.md             # "obs with status:open grouped by area+kind, count>=2" — the consolidation surface
```

Three object types, three reasons to exist:

| Object | Mutability | Holds | Never holds |
|---|---|---|---|
| **`obs/*.md`** | write-once, append-only as a stream | one observation + evidence | a fix, a rule, a policy |
| **`lessons/L*.md`** | editable (it's a curated rule) | the distilled general rule + status + linked obs | raw narrative (that stays in obs) |
| **`consult.md`** | regenerated, never hand-edited | active lessons, terse | anything not promoted |

The split between `obs/` (capture) and `lessons/` (distill) **is** the wall between failure-mode #1 (collapse) and #3 (conflation). An agent physically cannot write a fix into an obs file — the template has no field for it.

---

## B. Fully populated example files

### B1. An observation file — `obs/2026-06-19-mrl-headline-field-misleads-trustpilot.md`

```markdown
---
id: O-2026-06-19-trustpilot-score-misleads
kind: surprise            # closed set: failure | friction | surprise | wish | risk-miss | brian-correction
area: signals-read        # closed set: capture | signals-read | query | review | scope | doc-style | brian-taste | tooling
severity: 3               # 1 trivial .. 4 load-bearing; this misled a real read
run: runs/005-trustpilot-signals-reputation-landscape
source: run-notes         # run-notes | review | brian | retro
status: open              # open | clustered:L001 | parked
date: 2026-06-19
---

**Observation.** The Trustpilot `trust_score` headline field (e.g. remedymeds "Excellent 4.7")
read as decision-grade, but it is the most misleading field on the capture: it omits
paid-profile / invited-review / merged-profile posture, and the review *bodies* show
remedymeds' dominant complaint cluster is billing-after-cancel — structurally identical to
hims (3.0). The score gap reflects invitation posture, not quality.

**Evidence.** runs/005 run-notes; remedymeds vs hims body-vs-score contradiction.

<!-- NO "proposed fix" field exists. If you have a fix instinct, it goes to a lesson, not here. -->
```

### B2. A lesson file — `lessons/L001-headline-signal-needs-integrity-sibling.md`

```markdown
---
id: L001
rule: A headline Signal field must travel with its integrity/confound sibling before a read uses confident language.
area: signals-read
status: active            # proposed | active | retired | superseded:Lxxx
severity: 4
promoted: 2026-06-20
promoted_by: consolidation-2026-06-20
gate: cross-run           # why it graduated: cross-run (≥2 runs) | brian | review | severe-once
applies_to: skills/research-company SIGNALS reads; QUERYING signals recipes
evidence:                 # the obs this rule distills — links, never copies
  - O-2026-06-19-trustpilot-score-misleads
  - O-2026-06-19-wayback-tenure-misleads
  - O-2026-06-19-sec-totalhits-misleads
supersedes: []
---

## Rule

The easiest-to-grep headline field is often the most misleading one. Before any read uses
confident language ("trusted", "established", "funded"), surface the field's integrity sibling:

- **Trustpilot `trust_score`** → paid-profile + review-volume + (where decision-grade) review bodies.
- **Wayback `tenure_days`** → snapshot continuity/density; tenure ≠ brand age without it.
- **SEC `total_hits`** → match/vehicle/CIK/existence-only flags; a hit ≠ funding.

Verdicts like *trusted / established / funded* stay labeled Judgments, never State.

## Why this exists (challenge me)

Three signal families, three different root causes, same consumer failure — see the 3 linked
obs. Promoted on the cross-run gate (3 independent runs, severity 4). It does NOT yet justify
a schema field, monitor, or score; it is a read-discipline rule. Retire if a capture-time
integrity-sibling convention makes the read-time check redundant.
```

### B3. A Brian-taste observation — `obs/2026-06-23-ab-brian-correction-simplify-not-add.md`

```markdown
---
id: O-2026-06-23-simplify-not-add
kind: brian-correction
area: brian-taste         # this is how the system learns BRIAN, not just the work
severity: 3
run: experiments/01-agentic-build/changes/0003-learning-ledger
source: brian
status: open
date: 2026-06-23
---

**Observation.** Reviewing the learning-ledger packet, Brian cut the proposed 4-section
LEARNING.md to a single append-only log + a query. Direct quote: "every field/rule must earn
its place — what does this replace?" Pattern: when an agent proposes *adding* structure, Brian's
default correction is *subtract until it breaks*.

**Evidence.** Packet 0003 decision-surface thread; prior identical cut on the MRL triage template.
```

> Note: `brian-taste` is just another `area` value. Brian's recurring corrections accrue in the same log as everything else and consolidate by the same query — so "simplify, don't add" graduates into a real lesson (`L002`) on the same cross-run gate as any technical pattern. The system learns Brian by treating his corrections as first-class observations, not a special subsystem.

---

## C. Rules / lifecycle

**What writes (cheap, forced, never blocked).**
- At packet/run close, the agent appends **0..N** obs files via `learn.py add` — one file per distinct observation. Forced like `site_notes` is forced (the close checklist asks "any obs?"), but honest `none` is fine. One file = one observation keeps the log atomic and greppable.
- Obs files are **write-once**. A later run that sees the same thing writes a *new* obs (it does not edit the old one). Recurrence is represented by *count in the log*, not by a growing evidence paragraph. This is the direct structural fix for MRL-002's 15-paragraph accretion.

**What reads.**
- Every run reads `consult.md` first (active lessons only — terse, ~1 screen). That is the *Consult* stage. It does not read `obs/` to operate.
- A consolidation pass reads `obs/` via query.

**What consolidates (the only step that produces rules).**
- Triggered manually (`learn.py consolidate`) after several packets **or** after any severity-4 failure. No daemon.
- It runs the standing query in `queries/open-clusters.md`: group `status:open` obs by `area + kind`, surface any cluster with `count >= 2` (or any single `severity:4`). The query **returns the cluster; it does not mutate the obs.**
- For each surfaced cluster the agent does the 5-stage work (below) and proposes a **Lesson** — a new `lessons/Lxxx.md` linking the obs as `evidence`. Proposing a lesson flips those obs' `status` from `open` → `clustered:Lxxx` (a one-field stamp, the only edit ever made to an obs, and it's mechanical/auditable).
- **A lesson is proposed, never auto-activated.** It lands `status: proposed`. Brian (or, for the low-risk class, the consolidation agent under the lead-context risk rules) flips it to `active`. Activation regenerates `consult.md`.

**What prunes (subtractive, but never destructive).**
- A lesson can be `retired` or `superseded:Lxxx` — a frontmatter flip, never a delete. The file and its evidence links stay in git. `consult.md` drops it on next regen, so the *active surface* shrinks while the *audit trail* is complete.
- Obs are **never pruned**. They are the divergent record. They cost ~15 lines each; the log is designed to be skimmed by query, not by eye. (If volume ever truly bites — thousands — obs roll into dated `obs/archive/YYYY-QN/` folders, still greppable. Not needed at current scale.)
- An obs that never clustered stays `open` forever. That is a feature: it is preserved divergent signal, visible to the next consolidation, not garbage. "Never graduated" ≠ "deleted."

**What stays human-gated.**
- Lesson `proposed → active` (except an explicit low-risk class).
- Any lesson whose `applies_to` touches a skill/contract → the actual skill edit is a separate change packet (the existing Agentic Build flow). The lesson is the *spec for the edit*, not the edit.

**Risk class for the bonus auto-apply.** A lesson may carry `auto: ok` only if `area` ∈ {doc-style, query} **and** `severity ≤ 2` **and** `gate: cross-run`. Those are reversible, non-contract, evidence-backed. Everything else is human-gated. This reuses the lead-context risk model rather than inventing a new one.

**Closed sets (the contract — mirrors Truffle's frontmatter discipline).**
- `kind`: failure | friction | surprise | wish | risk-miss | brian-correction
- `area`: capture | signals-read | query | review | scope | doc-style | brian-taste | tooling
- `severity`: 1–4
- obs `status`: open | clustered:Lxxx | parked
- lesson `status`: proposed | active | retired | superseded:Lxxx
- `gate`: cross-run | brian | review | severe-once

New values are added the way Truffle adds any closed-set value — deliberately, in `README.md`, asking what it divides. Not forked per case.

---

## D. Worked example — the headline-field finding, end to end

The anchor: *"the easiest-to-grep headline field is the most misleading one"* (Trustpilot score, Wayback `tenure_days`, SEC `total_hits` each mislead a naive read).

**Stage 1 — Fail/Capture (run 005, 006, 007 close).** Three separate runs each hit the same shape on a different signal. Each writes its OWN obs file — no merging, no shared paragraph:

```text
obs/2026-06-19-mrl-headline-field-misleads-trustpilot.md   kind:surprise area:signals-read severity:3 status:open
obs/2026-06-19-mrl-headline-field-misleads-wayback.md      kind:surprise area:signals-read severity:3 status:open
obs/2026-06-19-mrl-headline-field-misleads-sec.md          kind:surprise area:signals-read severity:3 status:open
```

(File B1 above is the trustpilot one, filled.) At this point there is **no rule and no fix anywhere** — the obs template can't hold one. Failure-mode #1 defeated at the source.

**Stage 2 — Investigate (consolidation pass, triggered after run 007).** `learn.py consolidate` runs the standing query:

```bash
$ python scripts/learn.py query --status open --group area,kind --min-count 2
area=signals-read kind=surprise  →  3 obs  [trustpilot, wayback, sec]   ← cluster surfaced
area=scope        kind=friction  →  1 obs                               (below threshold, stays open)
```

The query *returns the three obs*; it does not touch them. The agent reads all three raw files (divergence intact — over-compression defeated) and investigates: why do all three mislead? Root cause differs per field (paid-profile posture / snapshot density / match-existence), but the *consumer* failure is identical: a greppable headline read without its integrity context.

**Stage 3 — Verify.** The agent confirms the pattern is real and cross-run (3 independent runs, not one case generalized) and checks it isn't already covered by an active lesson. Verified fact: *headline ≠ decision-grade for these three signal families; root causes differ, so the rule must name the sibling per family, not flatten them.*

**Stage 4 — Distill.** The agent writes `lessons/L001-headline-signal-needs-integrity-sibling.md` (file B2 above) — a **general** rule ("surface the integrity sibling before confident language"), with the three obs as `evidence:` links and `gate: cross-run`. It stamps the three obs `status: open → clustered:L001` (the one allowed mechanical edit). Lands `status: proposed`.

```bash
$ python scripts/learn.py promote --from-query --rule "headline signal needs integrity sibling" \
    --evidence O-...-trustpilot,O-...-wayback,O-...-sec --gate cross-run
wrote lessons/L001-...  (status: proposed)
stamped 3 obs → clustered:L001
```

**Stage 5 — Consult + applied change.** Brian reviews the one-screen decision surface (rule + why + 3 evidence links), approves → `status: active`. `consult.md` regenerates:

```markdown
## consult.md  (generated 2026-06-20 — DO NOT EDIT, run `learn.py regen`)
- **L001** [signals-read] Headline Signal field must travel with its integrity sibling before
  confident language (trust_score→paid/volume/bodies; tenure_days→snapshot density;
  total_hits→match/vehicle/CIK). Verdicts stay Judgments. ·evidence:3 obs ·gate:cross-run
```

The next run that consumes a signal reads `consult.md`, sees L001, and applies the integrity-sibling check **instead of re-deriving it** — the compounding the 5-stage progression wants. If/when `applies_to` (the `research-company` SIGNALS step) is edited, that is a separate change packet whose spec is L001 — and L001's `evidence` links let anyone trace the skill edit back to the three runs that earned it.

**Contrast with what MRL did:** MRL fused all three into MRL-008's ever-growing Evidence Log, never graduated it, and the idea-harvest had to send five agents to re-read raw runs to recover the divergence. Here the divergence was never lost (3 standing obs), the rule graduated cleanly (a separate linked object), and recurrence was a `--min-count 2` query, not a human re-read.

---

## E. Map to the 5 stages and the 4 failure modes

**5-stage memory progression**
1. **Fail** → one append-only obs file per failure, closed-set frontmatter, evidence inline. Forced at close like `site_notes`.
2. **Investigate** → the consolidation query *returns the raw cluster*; the agent reads the actual obs files (not a summary) to find why. Divergence is the input to investigation, not a casualty of it.
3. **Verify** → the `gate` field forces the agent to name *why* it's a fact (cross-run / brian / review / severe-once) before a lesson can exist; single-case generalizations can't pass `cross-run`.
4. **Distill** → the Lesson is a separate object holding a *general* rule, linking obs as evidence, never copying their narrative. Distillation is structurally distinct from capture.
5. **Consult** → `consult.md` (active lessons only) is read first by every run; the rule is applied, not re-derived. Compounding lands here.

**4 failure modes (and where I'm honest about limits)**
1. **Collapse observation→solution** → *Defeated structurally:* the obs template has no fix field; a fix can only exist as a Lesson, which requires a gate. An agent literally cannot write a policy into the log.
2. **Anchor-and-mirror** → *Mostly defeated:* there is no master template to mirror — obs are uniform tiny records (nothing to copy badly), and lessons anchor on the closed-set schema in `README.md`, not on the previous lesson's prose. *Residual risk:* the first few lessons could still set a tone; mitigated by `README.md` carrying a canonical filled example (B2) as the anchor instead of "whatever you find."
3. **Conflate feedback with item-of-work** → *Defeated:* obs (feedback) and lessons (the unit that fixes it) are different files in different folders with different mutability. Dedup/graduate/close happen on lessons; obs just accrue and stay queryable. MRL-002's 15-paragraph fusion is impossible by construction.
4. **Over-compression** → *Defeated:* the raw log is never compressed or merged — consolidation is a non-mutating query. The clean view (`consult.md`) is strictly downstream and regenerable; killing it loses nothing. The 345→2 collapse can't happen because nothing rewrites the 345.

---

## F. Self-critique (adversarial)

**Weakness 1 — Query quality is the new single point of failure.** I moved the risk from "an agent over-compresses" to "the consolidation query mis-clusters." If `area`/`kind` are tagged sloppily, the *same* finding lands in two areas and the `--min-count 2` gate never fires — the cross-run pattern stays invisible, exactly MRL's "couldn't see across runs" failure in a new outfit. The closed sets are load-bearing, and they're filled by the same agents whose judgment we don't fully trust. *Cost to fix:* a thin tagging lint (`learn.py lint` flags obs whose body keywords don't match their `area`, à la Truffle's `querycheck.py`) plus periodic "fuzzy" consolidation passes that group by embedding/keyword similarity, not just exact `area+kind`. That adds a script and a soft-match step — real complexity creep against the "what does this replace?" bar. I'd ship exact-match first and add fuzzy only when a missed cluster is observed, not preemptively.

**Weakness 2 — At thin corpus this is heavier than the problem.** Today there are ~3 packets and 1 real `workflow_note`. A folder-of-files + a script + closed sets + a generated digest is more machinery than 4 observations need; the honest v0 might be a single append-only `obs.md` with the same frontmatter per `##` entry and `grep`, no `learn.py`, no separate files. The per-file split and the script earn their keep only once the log is big enough that *editing one file becomes a merge-conflict / accretion risk* — i.e. exactly the scale MRL hit. *Cost to fix:* start as one `obs.md` + manual `grep` + the `lessons/` folder; promote to one-file-per-obs + `learn.py` only when the log crosses ~30 entries. The schema is identical either way, so the migration is mechanical — but it means the full tree in section A is the *target*, not the day-one build, and I should have led with the smaller seed.

**The deeper bet I'm exposed on:** this design assumes *finding the pattern* is the hard part and makes it a query. If the real bottleneck is *investigating* (stage 2) — the slow human/agent reasoning about why — then making clustering cheap doesn't move the needle much, and I've optimized the wrong stage. My defense: MRL's own autopsy says the divergence was destroyed *before* anyone could investigate (345→2), so protecting the raw log to enable investigation is the right first lever. But I'd want the first 10 real consolidation passes to confirm that query-surfacing, not reasoning, was the binding constraint.
