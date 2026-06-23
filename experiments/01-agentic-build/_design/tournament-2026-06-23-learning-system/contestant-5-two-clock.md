# Contestant 5 — The Two-Clock Ledger

## Core idea

MRL failed because it ran **one clock** where it needed two: the same file held raw observations, the work-items that fix them, and the steward's tidy summaries — so observing, deciding, and tidying happened in one motion and metastasized into ever-growing solution-blobs. **Split the clocks.** Clock 1 is `notices/` — a greedy, append-only stream of immutable one-observation files that are *never merged, never edited, never tidied*; singletons are welcome and divergence is the whole point. Clock 2 is `rules/` — a small, curated set of general rules, each born only by passing an explicit, evidence-cited promotion gate. The two never touch the same file, and **the link between them is a back-reference, never a move** — so nothing accretes, nothing compresses, and you can always see the raw signal a rule was distilled from.

---

## A. Directory tree

```text
experiments/01-agentic-build/learning/
├── README.md                      # the one-screen contract: two clocks, anti-merge law, gate
│
├── notices/                       # CLOCK 1 — append-only, immutable, NEVER merged or tidied
│   ├── 2026-06-19-n001-headline-field-misleads-trustpilot.md
│   ├── 2026-06-19-n002-signal-read-loop-rebuilt-each-run.md
│   ├── 2026-06-20-n014-headline-field-misleads-wayback.md
│   ├── 2026-06-20-n015-headline-field-misleads-sec.md
│   └── …                          # one file = one observation, forever. ~hundreds is healthy.
│
├── rules/                         # CLOCK 2 — curated general rules, each gate-promoted
│   ├── R03-headline-signal-needs-integrity-sibling.md
│   └── R01-quote-frontmatter-dont-rederive.md
│
├── candidates/                    # the GATE's waiting room — proposed promotions, human-gated
│   └── C07-headline-field-misleads.md
│
├── brian/                         # CLOCK 2, a dedicated lane — learns BRIAN, not the work
│   └── B02-simplify-dont-just-add.md
│
└── _consolidations/               # dated minutes of each consolidation pass (audit trail)
    └── 2026-06-22-pass.md
```

Where it lives and why: **in-repo, under the experiment**, because Agentic Build is the proving ground and the corpus must move through `git` for provenance/rollback/inspection (the frame's hard constraint, and what Brian liked about Anthropic's memory-as-a-git-folder). When the pattern graduates to user-facing verbs, the same five-folder shape drops in beside any skill — nothing about it is MRL- or build-specific.

What each folder **replaces** (least-complexity test):
- `notices/` replaces MRL's `Evidence Log` paragraphs *and* the `discovery-ledger.md`. One folder of immutable files instead of two growing prose blobs.
- `rules/` replaces MRL's `Active Rules` / `Verified Lessons` *and* the per-skill scattering of lessons.
- `candidates/` replaces the YAML item's `proposed_next_step` field — the thing that fused feedback with work-item. Now it's a separate object with its own lifecycle.
- `brian/` replaces nothing — it's the new capability the frame demands ("learn Brian over time") and MRL never had.
- `_consolidations/` replaces MRL's one-line `Steward Pass Log` with the same idea done honestly: the minutes *cite* what they read and chose to drop, so over-compression is auditable.

---

## B. Three fully-populated example files

### B.1 — A notice (Clock 1). Immutable. One observation. Note the empty solution slot.

`notices/2026-06-19-n001-headline-field-misleads-trustpilot.md`

```markdown
---
id: n001
date: 2026-06-19
clock: notice
source: runs/005-2026-06-19-trustpilot-signals-reputation-landscape
kind: surprise            # one of: friction | surprise | wish | risk-miss | brian-correction
skill: query-companies    # which verb/convention this touched (best guess, not binding)
status: open              # open | linked  (linked = a candidate/rule cites it; STILL immutable)
linked_by: []             # back-refs filled by Clock 2; this file's BODY is never edited
---

## What happened
Reading Trustpilot signal captures, the easiest field to grep — `trust_score` —
gave the most confident-sounding, most wrong answer. remedymeds reads "4.7 Excellent",
hims reads "3.0". A naive sort makes hims the trust problem.

## Why it's worth a notice
The score gap is an artifact of invited-review / paid-profile posture, not quality.
The decision-grade signal (review *bodies*) shows both have the same billing-after-cancel
complaint cluster. The headline number inverts the truth.

## What I am NOT claiming
Not proposing a fix, a field, or a rule. This is one sighting on one signal type.
Whether it generalizes is Clock 2's job, not mine.
```

**The discipline that defeats accretion:** a notice has no "proposed_next_step", no "evidence log", no status that can climb. It is born done. The author's *only* job is to record the sighting honestly and stop. The "What I am NOT claiming" section is a forced guard against collapsing observation into solution — every notice writes it.

### B.2 — A rule (Clock 2). General. Cites its evidence. Has a kill-switch.

`rules/R03-headline-signal-needs-integrity-sibling.md`

```markdown
---
id: R03
clock: rule
status: active            # active | retired
promoted: 2026-06-22
promoted_by: consolidation 2026-06-22-pass.md
from_candidate: C07
distilled_from: [n001, n014, n015]   # the RAW notices — provenance, never deleted
applies_to: query-companies, SIGNALS.md consumers
review_after: 2026-09-22  # staleness date; a consult that contradicts it can retire it early
---

## Rule
A headline signal field must travel with its integrity sibling before a read uses
confident language. Three confirmed instances; treat as a family, not three forks:

| Headline field      | Lies because…                          | Required sibling                    |
|---------------------|----------------------------------------|-------------------------------------|
| Trustpilot score    | invited-review / paid-profile posture  | review volume + paid_profile flag   |
| Wayback tenure_days | snapshot density / CDX nondeterminism  | continuity + snapshot count         |
| SEC total_hits      | name-match ≠ entity match              | CIK / vehicle / existence flag      |

Verdicts like "trusted", "established", "funded" stay **labeled Judgments**, never State.

## Why this is general (and not a policy fork per signal)
The instances differ in root cause but share ONE shape: the cheap-to-grep number is
the wrong number. The rule names the *shape*, so a fourth signal inherits it for free
instead of spawning a fourth fork. (This is exactly the generalization MRL never made —
it logged the family as ~10 ever-growing evidence paragraphs and never abstracted it.)

## How to consult me
`/research-company`, `/query-companies`, and any SIGNALS reader: when a read leans on a
headline signal field, surface its sibling in the same breath or downgrade the language.

## Kill-switch
Retire if a consult shows the sibling-rule producing false caution on a clean field,
or if SCHEMA promotes the siblings to first-class fields (then the rule is redundant —
say so and retire). Retiring moves nothing; it flips `status` and logs why.
```

### B.3 — A Brian-rule (Clock 2, the `brian/` lane). Learns the *person*.

`brian/B02-simplify-dont-just-add.md`

```markdown
---
id: B02
clock: brian
status: active
promoted: 2026-06-22
distilled_from: [n008, n022, n031]   # three notices tagged kind:brian-correction
review_after: 2026-12-22             # Brian-taste rules age slowly
---

## The preference
When improving a doc, prompt, or rule, Brian wants it SIMPLIFIED, not extended.
The reflex "add a section/field/rule" is usually wrong; the right move is "what does
this replace?" Three corrections logged this verbatim ("slim and correct what's there",
"what does this replace", an `/overwhelmed` run triggered by additive drift).

## How to consult me
Before any consolidation proposes a new rule, field, or template line: state what it
replaces. If it replaces nothing, default to NOT adding it and flag the tension to Brian.
A net-negative diff is a feature, not a failure.

## Evidence it's real, not one mood
n008 (frame review), n022 (lead-context edit), n031 (the /overwhelmed signal the frame
itself names as a learnable event). Three independent sightings → durable taste, not noise.
```

---

## C. Rules / lifecycle — what writes, reads, consolidates, prunes

The whole system runs on **two clocks ticking at different rates**, and one law connecting them.

**The Anti-Merge Law (the heart of the design):**
> A file in `notices/` is *write-once*. It is never edited, merged, summarized, deduped, or deleted. Clock 2 may only *reference* a notice by id (`distilled_from`, `linked_by`); it may never absorb its text or retire its file. Compression happens by *adding a rule that points at notices*, never by *shrinking the notices*.

This single law structurally kills over-compression: there is no operation in the system that destroys raw signal. The clean view (a rule) is literally a different file that *links down* to the divergent record.

| Step | Who/what triggers it | Writes to | Clock |
|---|---|---|---|
| **Notice** | Any run/packet at close; any agent any time it's surprised, frustrated, wishing, or corrected by Brian | a new immutable file in `notices/` | 1 (fast, greedy) |
| **Consult** | Every run, at *start* — agents read `rules/` + `brian/` (small, curated, cheap to read) before working | nothing (read-only) | — |
| **Consolidate** | Manually invoked `/agent-build-consolidate`, after ~N notices accrue or after a painful failure. Never a daemon. | proposes files in `candidates/`; writes minutes to `_consolidations/` | 2 (slow, curated) |
| **Promote** | Brian (or auto-apply for the safe class, below) approves a candidate | new file in `rules/` or `brian/`; back-fills `linked_by` on cited notices | 2 |
| **Retire** | A consult that contradicts a rule, or a `review_after` date passing without re-confirmation | flips rule `status: retired` + one line why | 2 |

**What consolidation may and may not do** (the rule that would have saved MRL):
- MAY: read across all notices, cluster by shape, and draft a *candidate* that cites ≥N notice ids.
- MAY: in the minutes, say "I read 40 notices, saw these 3 clusters, propose 1 rule, and am *deliberately leaving 37 notices unconsolidated because they're singletons or don't share a shape*."
- MUST NOT: edit, merge, or delete any notice.
- MUST NOT: promote anything itself beyond the safe class — it *proposes* to `candidates/`, human-gated.

**Staleness** is removed only from Clock 2, never Clock 1. Rules carry a `review_after` date; a rule that isn't re-confirmed retires (status flip, evidence kept). Notices never go stale — a 2026 notice is permanent provenance even after its rule retires. *Pruning preserves evidence by construction*: retiring a rule leaves both the rule file (status: retired) and every notice it cited fully intact.

**The promotion gate** (a candidate becomes a rule only when):
1. **≥3 notices share a *shape*** (not just a topic) — forces generalization, kills the one-case fork; OR
2. **a Brian correction** (one is enough — `kind: brian-correction` notices fast-track to `brian/`); OR
3. **a single severe risk-miss** where one occurrence justifies a guardrail.

And the candidate must pass two written tests, answered in the candidate file:
- **Generalization test:** "State the rule without naming any specific run or company." If you can't, it's not a rule yet — it's a notice. (Defeats failure mode 1.)
- **Replacement test:** "What does this rule replace?" If nothing, default to not promoting. (Brian's own principle, made structural.)

**Safe-class auto-apply (bonus):** a candidate may auto-promote *without Brian* only if it is (a) a pure doc clarification with a net-non-positive line count, AND (b) cites ≥3 notices, AND (c) touches no contract/schema/skill-behavior. Everything else is human-gated. The auto-applied diff still lands as a reviewable `git` commit citing the candidate, so "automatic" still means "visible".

---

## D. Worked example — the "headline field is the most misleading" finding, end to end

**Stage 1 — Fail / Capture.** Run 005 reads Trustpilot. The agent notices the easy field lies. It writes **`notices/2026-06-19-n001-headline-field-misleads-trustpilot.md`** (full content in B.1). It does *not* propose a fix — the "What I am NOT claiming" block forbids it. Clock 1 ticks once. *Contrast MRL: this same observation became the first paragraph of MRL-008's Evidence Log, fused to a `proposed_next_step`, and started accreting.*

**Stage 2 — Investigate.** Two later runs hit the same shape on *different* signals. Each writes its own immutable notice — **never** appended to n001:

`notices/2026-06-20-n014-headline-field-misleads-wayback.md`
```markdown
---
id: n014
date: 2026-06-20
clock: notice
source: runs/006-2026-06-19-wayback-offer-tenure-landscape
kind: surprise
skill: query-companies
status: open
linked_by: []
---
## What happened
`tenure_days` is the grep-friendly Wayback field and it misleads: snapshot density
varies wildly, and CDX returned a snapshot_count going *backwards* (2517→2516) — archive
nondeterminism a naive read calls "a lost snapshot".
## Why it's worth a notice
Same smell as n001: the cheap field is the wrong field. But different root cause
(archiver mechanics, not review posture). Logging separately so the difference survives.
## What I am NOT claiming
Not asserting these are the same rule. They rhyme. Clock 2 decides if that's a family.
```

`notices/2026-06-20-n015-headline-field-misleads-sec.md` — same structure, SEC `total_hits` (name-match ≠ entity, CIK collisions).

Three immutable files now sit in `notices/`. The *investigation* — "why does each lie?" — lives in each notice's body, captured at the moment of richest context, by the agent who actually hit it. Nothing is merged, so all three root causes survive distinct.

**Stage 3 — Verify.** `/agent-build-consolidate` runs (manually invoked after the run batch). It greps `notices/`, finds n001/n014/n015 share a *shape* ("cheapest-to-grep field is most misleading"). Three notices, three independent runs → gate condition 1 met. It writes a **candidate**, not a rule:

`candidates/C07-headline-field-misleads.md`
```markdown
---
id: C07
clock: candidate
proposed: 2026-06-22
cites: [n001, n014, n015]
target: new rule in rules/
risk: low        # doc-level convention, no schema/behavior change
---
## Proposed rule
Headline signal fields must travel with their integrity sibling before confident language.
## Generalization test (PASS)
Stated without naming any run/company: "the cheapest-to-grep field on a signal is the
one most likely to mislead; surface its integrity sibling or downgrade the language."
## Replacement test
Replaces: nothing additive — it *consolidates* three would-be per-signal cautions into
one shape, and pre-empts a 4th fork when the next signal type appears.
## Evidence
n001 (Trustpilot score), n014 (Wayback tenure), n015 (SEC hits). Three signals, one shape.
## NOT promoting yet
Awaiting Brian (low-risk → eligible for safe-class auto-apply if doc-only; see gate).
```
The minutes file `_consolidations/2026-06-22-pass.md` records: *"Read 41 notices. One promotable cluster (C07, 3 notices). Deliberately left 38 unconsolidated — singletons or no shared shape. Did not merge or edit any notice."* That sentence is the audit that MRL's `Steward Pass Log` never gave — you can see exactly what was compressed and what was preserved.

**Stage 4 — Distill.** Brian approves C07 (or it auto-applies as doc-only safe-class). Consolidation creates **`rules/R03-headline-signal-needs-integrity-sibling.md`** (full content in B.2): a *general* rule naming the shape, with a table of the three instances as evidence — not three forked policies. It back-fills `linked_by: [R03]` on n001/n014/n015 (the *only* permitted touch to a notice — a frontmatter back-ref, never the body). C07 moves to a `promoted` state; the candidate file can be deleted because its content now lives in R03 *and* the notices are intact — no signal lost.

**Stage 5 — Consult / Applied change.** Next run starts by reading `rules/`. It hits R03 *before* doing any signal read, and surfaces the integrity sibling automatically instead of re-deriving the lesson run-by-run (as MRL did ten times). The applied change: R03 also drives a one-line proposed edit to `SIGNALS.md` / the `/query-companies` guardrail ("headline signal reads must cite their sibling") — proposed as a packet, human-gated, `git`-tracked. **Compounding achieved:** the skill is sharper on run N+1 because of what failed on run N, and the next *new* signal type inherits the caution for free.

---

## E. Map to the 5 stages and the 4 failure modes

**5-stage memory progression:**
1. **Fail** → a notice file, written at close with full context, "What happened" + "Why worth a notice".
2. **Investigate** → each notice's body carries the *why* at peak context; divergent root causes survive because notices are never merged.
3. **Verify** → consolidation requires ≥3 notices sharing a *shape* (or a severe single), turning a hunch into a cited, checkable cluster in a candidate.
4. **Distill** → the Generalization test forces a run/company-free statement before a rule is born; R03 names the shape, not the case.
5. **Consult** → every run reads `rules/` + `brian/` at start; small curated set, cheap to read, replaces re-derivation.

**4 failure modes — how the structure defeats each:**
1. **Collapse observation→solution** → notices have *no* solution slot and a mandatory "What I am NOT claiming" block; solutions can only be born in Clock 2, behind the Generalization+Replacement gate.
2. **Anchor-and-mirror** → an agent writing a notice has nothing to mirror (notices are atomic, templated, immutable — a bad one doesn't become a standard; it's just one more sighting). Rules are few and gate-guarded, so a crap first draft can't entrench.
3. **Conflate feedback with item-of-work** → these are *different folders with different clocks*: `notices/` (feedback) and `candidates/`→`rules/` (work). The link is a back-reference, never a fusion. Nothing can both accrete evidence and climb a status — those live in different files.
4. **Over-compression** → the Anti-Merge Law: no operation in the system destroys a notice. Compression only *adds* a linking rule; the ~345-to-2 collapse is structurally impossible, and the minutes file makes every consolidation choice auditable.

**Plus the frame's fifth hazard — "aimed at the wrong target":** the `brian/` lane and the `kind` taxonomy (friction/surprise/wish/risk-miss/brian-correction) keep the incentive on *harvesting divergent signal*, not on "produce a recipe" — the exact mis-aim MRL had.

---

## F. Self-critique — top 2 weaknesses

**1. The notice stream can rot into noise; `grep`-ability degrades as it grows.** Hundreds of immutable files is the *point*, but with no merge, finding "do we already have a notice like this?" gets harder over time, and consolidation's clustering quality is the whole ballgame. If consolidation is lazy or rare, notices pile up unconsolidated and the rules lag reality — a slower version of MRL's thinness. **Cost to fix:** add a `kind` + `skill` frontmatter index (already in the schema) and a dead-simple `learning/INDEX.md` regenerated by a script that lists notice ids by `skill` and `kind` — a *derived lens*, disposable, not authoritative (consistent with engine ethos). That's ~30 lines of Python and one convention; cheap. The deeper risk — consolidation never being run — is a *discipline* problem the design can't fully solve; it's mitigated by making consolidation a single slash command and tying it to packet-batch close, but it ultimately needs Brian (or a routine) to fire it. I'd rather under-automate here than reintroduce a daemon.

**2. "Shape" is a judgment call, and the gate leans on it heavily.** The Generalization test ("≥3 notices share a *shape*") is the firewall against forking — but *what counts as the same shape* is exactly the call an overfitting agent gets wrong. n014 (Wayback mechanics) and n001 (review posture) have genuinely different root causes; a too-eager consolidator could *under*-cluster (3 forks) or a too-aggressive one could *over*-cluster (jam unrelated notices into one mushy rule — a new flavor of over-compression sneaking in at Clock 2). **Cost to fix:** the candidate file's Generalization test is the explicit, inspectable place this judgment is shown and challenged — Brian can reject a candidate for bad clustering, and the cited notices are right there to check against. That makes the failure *visible and reversible* rather than silent, but it does keep a human in the loop for the hardest call, which caps how autonomous Clock 2 can get in v0. Loosening it safely needs replay/eval (the frame's parked could-have), not more rules.
