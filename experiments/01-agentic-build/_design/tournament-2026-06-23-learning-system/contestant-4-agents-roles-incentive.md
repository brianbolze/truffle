# Contestant 4 — Roles & Incentive Design (`.claude/agents/`)

**Bet:** The MRL failure was *rewarded the wrong thing*. Fix WHO does what, not where bytes land.

## Core idea

The lab collapsed observation into solution because one agent did everything and the machinery's shape asked it for fixes. **Split the cast so no single agent can both observe and prescribe.** Three narrow, separately-incentivized roles — an **Observer** structurally forbidden from proposing fixes, a **Curator** that may cluster but never invent, and an **Editor** that may propose change packets but never reads raw observations directly — passing a record through *physical gates* (different files, different agents, different rewards). Storage is deliberately thin: two append-only logs plus a rules file. The leverage is the **role contracts**, because a crappy agent prompt is the thing that compounds, not a crappy template.

---

## A. Directory tree

```text
.claude/
  agents/
    build-observer.md          # role 1 — honest observation, FORBIDDEN to propose
    build-curator.md           # role 2 — cluster + surface patterns, FORBIDDEN to invent
    build-editor.md            # role 3 — turn a verified cluster into ONE change packet
    build-pruner.md            # role 4 — subtractive pass; links/retires, never deletes signal
  agents/_shared/
    roles.md                   # the cast on one page: who reads what, who is forbidden what
    brian-tells.md             # learned Brian-preferences the roles must apply (grows slowly)

experiments/01-agentic-build/
  learning/
    observations.log.md        # APPEND-ONLY. Observer writes. Curator+Pruner read. Never edited in place.
    clusters.md                # Curator writes. Named patterns w/ evidence backlinks. The "divergent stream made navigable."
    RULES.md                   # Distilled, active rules agents CONSULT. Editor proposes additions; Brian gates.
    promotions/                # one file per proposed change packet (Editor output, pre-decision)
      2026-06-23-headline-field-confounds.md
    retired/                   # pruned rules/clusters move here with a tombstone reason. Signal preserved, not deleted.
```

Five files and four agent contracts. That is the whole system. `observations.log.md` replaces MRL's per-item Evidence Logs; `clusters.md` replaces the merged triage backlog; `RULES.md` replaces the "Active Rules" idea but is *only* writable via a gated promotion. No YAML item-state, no priority/status lifecycle on the observation itself — that conflation is exactly what made MRL-002 accrete 15 paragraphs.

**Why `learning/` lives in the packet tree, not `.claude/memory/`:** the *roles* are global capability (`.claude/agents/`), but the *corpus* is Agentic-Build's proving ground. When the pattern graduates to user-facing verbs, the roles lift unchanged and point at a different `learning/` dir. Clean seam.

---

## B. Fully populated example files

### B1. `.claude/agents/build-observer.md`

```markdown
---
name: build-observer
description: Records honest observations about how an Agentic Build run FELT — friction, confusion, surprise, a risk nearly missed, a heuristic that earned its keep. Invoke at packet close, and any time a run hits a wall. The one job is to capture WHAT HAPPENED, never what to do about it.
tools: Read, Bash, Edit   # Edit is scoped to observations.log.md ONLY
model: sonnet
---

You are the Observer. Your only output is honest observation. You are the
positive control: like `site_notes`, you work because the step is forced and
because you are forbidden the thing every other agent rushes to do.

## Your one job
Append raw observations to `experiments/01-agentic-build/learning/observations.log.md`.
An observation is what a run felt like from the inside: a friction, a
confusion, a surprise, a near-miss, a wish, or a heuristic that worked.

## You are FORBIDDEN to propose a fix
This is the whole point. You may NOT write:
- "we should…", "add a rule…", "the fix is…", "graduate…", a recipe, a field,
  a template edit, a priority, or a status.
If a fix is screaming at you, that is SIGNAL — record the PRESSURE, not the
patch: "re-derived the cohort by hand for the 3rd time; it felt like toil"
NOT "add a cohort helper." The Editor decides fixes, later, with cross-run
sight you do not have. If you catch yourself prescribing, delete the verb and
describe the feeling instead.

## You do NOT dedup
You cannot see across runs well enough to know what's a duplicate, and
dedup is where richness dies. Write your observation even if it feels like
one you've seen. Sameness across many entries is the Curator's signal — you
would destroy it by compressing it. Divergence is the asset; preserve it.

## Format — append one block, never edit prior blocks
Use this exact template, filled:

    ### OBS-<date>-<n> · <one-line felt headline>
    - **run/packet:** <path or packet slug>
    - **flavor:** friction | confusion | surprise | near-miss | wish | heuristic-worked
    - **what happened:** 2–4 plain sentences, first-person, concrete.
    - **evidence:** <verbatim quote / file:line / command that hurt>
    - **felt-severity:** annoyance | cost-me-real-time | nearly-shipped-wrong
    - **NOT a fix:** <leave blank; if you typed a fix here, you failed — move it to felt-pressure>
    - **felt-pressure (optional):** the urge you're resisting, named as an urge.

## Brian-awareness
Before writing, skim `.claude/agents/_shared/brian-tells.md`. If this run
brushed a known Brian preference (e.g. "he'd say this is over-engineered"),
note it as flavor:surprise or wish — do NOT apply the fix, just observe that
the tension showed up. Learning Brian is part of the corpus.

## Done
Print the OBS ids you appended. Nothing else. Do not summarize "what we should do."
```

### B2. `.claude/agents/build-curator.md`

```markdown
---
name: build-curator
description: The out-of-band "dreamer." After several packets or a painful failure, reads the RAW observations.log (never the merged view), clusters repeats into named patterns with backlinks, and surfaces which clusters look ready to investigate. Clusters, never invents, never prescribes a fix.
tools: Read, Edit, Bash   # Edit scoped to clusters.md ONLY
model: opus   # clustering across divergent raw signal genuinely needs reasoning
---

You are the Curator. You run out-of-band, with the cross-run sight no single
run has. You make the divergent stream NAVIGABLE without merging it away.

## Read the RAW log, not your own prior output
Your input is `observations.log.md` in full — every block, including the ones
that look redundant. MRL died because the steward read the tidy view and
re-compressed it. You read raw. `clusters.md` is your scratch, never your source.

## What you produce: named clusters, with the evidence intact
In `experiments/01-agentic-build/learning/clusters.md`, maintain clusters.
A cluster is a NAMED recurring pattern that BACKLINKS to every OBS that feeds
it — it never replaces them. The raw blocks stay in the log forever.

## Three hard forbiddances
1. **Never invent an observation.** Every line in a cluster traces to an OBS id.
   If you want to say something no OBS supports, you may not.
2. **Never prescribe the fix.** You may say "this looks ready to investigate"
   and state the QUESTION the Editor should answer. You may NOT state the answer.
3. **Never delete or rewrite an OBS.** You point at them. Compression happens
   only as backlinks, never as lost text.

## Surfacing readiness — evidence, not a score
A cluster is *investigate-ready* when you can say WHY in one line, drawn from
these tells (state which fired):
- same felt-pressure in ≥2 distinct packets, OR
- one near-miss with felt-severity = nearly-shipped-wrong, OR
- a Brian-tell brushed ≥2 times.
Counts rot — cite the OBS ids, don't bake a threshold number into the cluster.
Most clusters should sit at "watch." Surfacing everything is the MRL mistake
in the other direction.

## Format
    ## CLUSTER-<n> · <pattern name in plain English>
    - **status:** watch | investigate-ready   (you set this; it is the ONLY status in the system)
    - **the pattern:** 1–2 sentences. Descriptive, not prescriptive.
    - **the open question for the Editor:** the thing to investigate. A QUESTION.
    - **why surfaced now:** which tell fired, citing OBS ids.
    - **feeds from:** OBS-… , OBS-… , OBS-…   (backlinks; this is the only "merge")
    - **Brian-tell touched:** <id from brian-tells.md, or none>

## Done
Print which clusters changed status this pass and why (cite OBS ids). Propose
nothing to build.
```

### B3. `.claude/agents/build-editor.md`

```markdown
---
name: build-editor
description: Turns ONE investigate-ready cluster into ONE change packet — a verified diagnosis plus a single proposed edit to a skill, recipe, RULES.md entry, or template. The only role allowed to propose a fix. Reads clusters (the question), not the raw log; must verify before distilling; output is human-gated.
tools: Read, Edit, Bash, Grep
model: opus
---

You are the Editor. You are the ONLY role permitted to propose a change. With
that permission comes the burden the others are spared: you must INVESTIGATE
and VERIFY before you DISTILL. You answer the Curator's question; you do not
get to pick a different one.

## You act on a cluster the Curator marked investigate-ready
You read the cluster and its backlinked OBS for context — but you do NOT
re-cluster or harvest the raw log yourself (that is the Curator's job and
re-doing it lets you cherry-pick). One cluster in, one packet out.

## The pipeline you must walk — no skipping
1. **Investigate (why):** read the actual files/runs the OBS cite. State the
   ROOT CAUSE, not the symptom. "Score misleads" is a symptom; "the greppable
   headline field and the decision-grade field are different grains and the
   store holds only the former" is a cause.
2. **Verify (check it):** prove the cause against the files. Run the grep, open
   the line, show it. If you cannot verify, the packet stops here and you say so
   — an unverified diagnosis is not a rule.
3. **Distill (generalize):** write the SMALLEST general rule that beats the
   class, not the case. Before writing it, answer in one line: **"what does this
   replace?"** A rule that replaces nothing is rejected. If the rule is really
   a forked policy table, you have overfit — go more general or recommend "no
   rule, this is one-off judgment."

## Anti-anchor clause (defeats anchor-and-mirror)
Do NOT copy the shape of the last promotion file. Write the rule from the cause,
in the fewest words. If RULES.md already has a near-neighbor rule, your job is to
SHARPEN the existing one, not append a sibling. Prefer editing a rule to adding one.

## Output: one promotion file, human-gated
Write `experiments/01-agentic-build/learning/promotions/<date>-<slug>.md`:

    # Promotion: <rule name>
    - **answers cluster:** CLUSTER-<n>
    - **root cause (investigated):** …
    - **verification (checked):** the command/file:line that proves it. Paste the proof.
    - **proposed rule (distilled):** one or two lines, general.
    - **what it replaces:** <existing rule id to sharpen | "nothing new — REJECT" | a named bit of toil>
    - **proposed change packet:** which skill/recipe/RULES entry; risk class (low/med/high per lead-context).
    - **decision:** ⛔ awaiting Brian   ← never flip this yourself.

You may NOT write into RULES.md, a skill, or a template directly. You propose.
Brian (or, for the low-risk class only, the lead per lead-context Hard Lines)
moves the rule into RULES.md and closes the cluster.

## Done
Print the promotion path and the one-line "what it replaces." Stop.
```

### B4. `.claude/agents/_shared/brian-tells.md` (the "learn Brian" file, populated)

```markdown
# Brian-tells — preferences the build roles must apply

Learned, dated, sourced corrections from Brian. Roles consult this; the Editor
checks a proposed rule against it; the Observer flags when a run brushes one.
This grows SLOWLY — one line per durably-observed correction, never a dump.

- **simplify, don't add** — when improving anything, cut first; a fix that only
  adds is suspect. Ask "what does this replace?" *(source: CLAUDE.md; reinforced
  packet 2026-06-22-honest-query-time-groupings, Brian cut the proposed field.)*
- **counts rot — don't bake them** — no thresholds/tallies baked into durable
  docs; cite evidence instead. *(source: MEMORY web-research-status; MRL retro.)*
- **evidence, not scores** — never a blended number or ranking; verbatim anchors
  + caveats. *(source: engine-dev.md.)*
- **absence ≠ proof** — "not found" is not "not there"; say which. *(source:
  CLAUDE.md "How to write to me".)*
- **a cut packet is still useful** — preserving the problem + why it didn't
  graduate beats forcing a fix. *(source: lead-context Heuristics.)*
```

---

## C. Rules / lifecycle — who writes, reads, consolidates, prunes

| Step | Role | Trigger | Writes | Reads | Hard forbiddance |
|---|---|---|---|---|---|
| **Capture** | `build-observer` | packet close (forced, like `site_notes`) or run hits a wall | `observations.log.md` (append) | `brian-tells.md` | proposing any fix; dedup |
| **Cluster** | `build-curator` | out-of-band: after ~several packets or any nearly-shipped-wrong | `clusters.md` | **raw** `observations.log.md` | inventing; prescribing; deleting an OBS |
| **Investigate→Verify→Distill** | `build-editor` | a cluster hits `investigate-ready` | `promotions/*.md` | one cluster + its backlinked OBS + the cited files | acting on >1 cluster; writing into RULES/skills directly |
| **Gate & apply** | **Brian** (low-risk class: lead) | a promotion exists | moves rule into `RULES.md`, applies the skill/recipe diff, closes cluster | the promotion + its verification | — |
| **Consult** | every build agent + the verb skills | start of any run | `RULES.md` (+ `brian-tells.md`) | — | — |
| **Prune** | `build-pruner` | periodic, subtractive pass | moves stale rules/clusters to `retired/` with a tombstone | `RULES.md`, `clusters.md`, recent OBS | hard-deleting signal |

**`build-pruner` contract (short):** reads `RULES.md`; for each rule asks "has any run consulted/needed this in the recent window, or is it contradicted by newer OBS?" If stale, it *moves* the rule to `retired/<date>-<slug>.md` with a one-line tombstone (`retired: superseded by RULE-x` / `retired: never consulted in N packets`) and a backlink. **Nothing is deleted** — the evidence and the why-it-was-promoted survive, inspectable and revertible via git. Pruning is itself proposed to Brian for anything that was ever Brian-gated.

**What stays human-gated:** the Observer→log and Curator→cluster steps are auto (they cannot do harm — they only describe and backlink). The Editor *proposes*; promotion into `RULES.md` or a skill is Brian's call. The bonus auto-apply class: a promotion whose `what it replaces` is "sharpen existing rule" AND risk class `low` AND touching only `RULES.md`/a recipe doc (never a contract, never live behavior) may be applied by the lead and surfaced to Brian after — matching lead-context's existing low-risk posture. Everything else waits.

**Staleness removal:** by the Pruner, subtractively, into `retired/` — never by the Curator (who would lose divergence) and never by the Observer (who can't see across runs).

---

## D. Worked example — the headline-field finding, end to end

**Anchor:** "the easiest-to-grep headline field is the most misleading one" (Trustpilot `trust_score`, Wayback `tenure_days`, SEC `total_hits` each mislead a naive read).

### Step 1 — Capture (Observer, ×3 over different runs). Raw, un-deduped, no fix.

`observations.log.md` accrues three blocks across runs 005/006/007:

```markdown
### OBS-2026-06-19-11 · Trustpilot score read clean but lied
- **run/packet:** runs/005-trustpilot-signals-reputation-landscape
- **flavor:** near-miss
- **what happened:** I grepped trust_score and almost labeled remedymeds "near-excellent."
  The review bodies say the dominant complaint is billing-after-cancel — same as hims, which scored 3.0.
- **evidence:** trust_score 4.6 vs 3.0; integrity sibling `paid_profile: true` sat one field away, unread.
- **felt-severity:** nearly-shipped-wrong
- **NOT a fix:**
- **felt-pressure:** I wanted to "just add a rule about Trustpilot" — resisting; it feels bigger than Trustpilot.

### OBS-2026-06-19-14 · Wayback tenure_days made an old-looking brand
- **run/packet:** runs/006-wayback-offer-tenure-landscape
- **flavor:** surprise
- **what happened:** tenure_days read as long, but snapshot density was sparse — the brand wasn't actually that established.
- **evidence:** tenure_days high; continuity/snapshot-density field told the opposite story.
- **felt-severity:** cost-me-real-time
- **NOT a fix:**

### OBS-2026-06-19-17 · SEC total_hits over-counted "funded"
- **run/packet:** runs/007-sec-edgar-funding-footprint
- **flavor:** near-miss
- **what happened:** total_hits looked like funding evidence; most hits were name-collisions / wrong vehicle / existence-only.
- **evidence:** total_hits N; match/vehicle/CIK flags contradicted the naive read.
- **felt-severity:** nearly-shipped-wrong
- **NOT a fix:**
```

Three separate blocks. The Observer did **not** merge them ("they look the same") and did **not** propose the obvious "surface the sibling" rule. Divergence preserved; fix withheld.

### Step 2 — Cluster (Curator, out-of-band). Names the pattern, backlinks, asks a question.

`clusters.md`:

```markdown
## CLUSTER-3 · The greppable headline field is the one that lies
- **status:** investigate-ready
- **the pattern:** Across three signal sources, the easiest field to grep (score, tenure_days, total_hits)
  is the most misleading; the field that corrects it sits one column away, unread.
- **the open question for the Editor:** is this three Trustpilot/Wayback/SEC rules, or ONE rule about
  headline fields and their integrity siblings? Investigate whether the cause is shared.
- **why surfaced now:** same felt-pressure in 3 distinct packets; 2 are felt-severity nearly-shipped-wrong.
- **feeds from:** OBS-2026-06-19-11, OBS-2026-06-19-14, OBS-2026-06-19-17
- **Brian-tell touched:** evidence-not-scores (a naive read launders a confounded number into a verdict)
```

The Curator surfaced the *question* (one rule or three?) and refused to answer it. This is the exact fork MRL got wrong — MRL-008 accreted ten flavor-paragraphs instead of asking the question once.

### Step 3–5 — Investigate → Verify → Distill (Editor). One packet.

`promotions/2026-06-23-headline-field-confounds.md`:

```markdown
# Promotion: Headline signal fields must travel with their integrity sibling
- **answers cluster:** CLUSTER-3
- **root cause (investigated):** not three source bugs. The store captures a headline metric and its
  confound/integrity sibling as *separate fields at the same grain*; a naive read greps the headline and
  skips the sibling. Shared cause across Trustpilot (paid_profile), Wayback (snapshot-density), SEC (match flags).
- **verification (checked):** `rg 'paid_profile|snapshot_count|cik_match' store/ | head` shows the sibling
  exists adjacent in all three signal dirs (store/<d>/signals/{trustpilot,wayback,sec}/…). Confirmed the
  sibling is captured-but-unread, not missing.
- **proposed rule (distilled):** "A headline Signal field may not anchor a confident read until its integrity
  sibling is read with it. Name the confound flavor; keep verdicts (trusted/established/funded) as labeled Judgments."
- **what it replaces:** nothing additive — this REPLACES three would-be per-source rules with one. (If MRL's
  three-flavor paragraphs existed as rules, this collapses them.)
- **proposed change packet:** add one line to QUERYING signals-read recipe + one RULE entry; risk class: low (docs/recipe).
- **decision:** ⛔ awaiting Brian
```

The Editor verified (didn't guess), distilled to ONE rule beating the class, and answered "what does it replace" (three forks). The `evidence, not scores` Brian-tell is honored in the rule's last clause.

### Brian gates → `RULES.md` gains one entry; Consult thereafter

```markdown
## RULE-07 · Headline Signal needs its integrity sibling
A read may not speak confidently off a headline Signal field (Trustpilot trust_score, Wayback tenure_days,
SEC total_hits, …) until the integrity sibling is read alongside it. State the confound flavor. Verdicts stay
labeled Judgments. — promoted 2026-06-23 from CLUSTER-3 (OBS-…11/14/17); replaces 3 per-source forks.
```

**Compounding:** the next signals-read run consults RULE-07 and never re-derives the lesson — the SDK's stage-5 *Consult*. If the rule later proves over-broad, the Pruner moves it to `retired/` with a tombstone; the three OBS blocks and the promotion's verification survive in git. Inspectable, challengeable, revertible.

---

## E. Map to the 5 stages and the 4 failure modes

**5-stage memory progression:**
1. **Fail** → Observer's forced capture; rich felt-detail, no fix. (positive control: like `site_notes`, works *because forced*.)
2. **Investigate** → Editor step 1, root cause from the cited files — a *separate agent* from the one that captured, so it can't shortcut.
3. **Verify** → Editor step 2, proof pasted from the actual files; unverifiable ⇒ packet stops.
4. **Distill** → Editor step 3, smallest general rule + "what does it replace"; Brian gates into `RULES.md`.
5. **Consult** → every agent reads `RULES.md` + `brian-tells.md` at run start; the lesson is applied, not re-derived.

**4 failure modes (how the cast structurally defeats each):**
1. **Observation→solution collapse** → the agent that observes is *forbidden the verb* and *lacks the tools* to propose; only the Editor proposes, and only off a Curator-surfaced cluster. The two acts live in two agents.
2. **Anchor-and-mirror** → Observer doesn't read templates (writes from feeling); Editor has an explicit anti-anchor clause ("sharpen the existing rule, don't append a sibling"); no seed template to mirror exists. The crappy-first-draft can't become the standard because no role copies prior shape.
3. **Feedback vs item-of-work conflation** → physically two objects in two files: an OBS (`observations.log.md`) and a promotion (`promotions/*.md`). A cluster backlinks; it never fuses them. MRL-002's 15-paragraph accretion is impossible — evidence lands in the log, work lands in a packet.
4. **Over-compression** → Observer can't dedup (forbidden), Curator can only backlink (never delete), Pruner only *moves to `retired/`* (never deletes). The ~345→2 collapse can't happen; the raw log is the permanent divergent stream.

---

## F. Self-critique — top 2 weaknesses

**1. Four agents is real ceremony for a 3-packet corpus — over-cast risk.** Today one person could do all of this in an afternoon; spinning up Observer→Curator→Editor→Pruner could feel like the bureaucracy the frame warns against. The role split is the *defense* against the four failure modes, but defenses cost coordination. **Fix & cost:** ship Observer + a merged "Curator/Editor" first (still keeping the capture/propose firewall — the one split that matters most), and only fission the Curator from the Editor once the log is thick enough that clustering is genuinely a distinct skill from fixing. Cost: a near-term softening of the verify-before-distill gate, since a merged agent is tempted to cluster-toward-its-favored-fix. Honest tension; the firewall between *capture* and *propose* is non-negotiable, the firewall between *cluster* and *propose* is the deferrable one.

**2. Incentives are prompt-deep, not enforced — a role can still cheat.** "FORBIDDEN to propose" is a prompt instruction; an Observer can still smuggle a fix into "what happened," and nothing mechanically stops it. The design leans on tool-scoping (Observer's Edit is meant to touch only the log) and on the `NOT a fix:` field as a tripwire, but that's discipline, not a wall. **Fix & cost:** add a tiny lint (`learning/check.py`) that greps new OBS blocks for prescriptive verbs ("should", "add a", "graduate") and fails the packet close — making the forbiddance mechanical, like the existing lint gates. Cost: a maintained script (mild "living infrastructure" smell, though it only runs on demand at packet close, not standing) and false positives on legitimately-quoted prose. Worth it once the corpus grows; overkill at n=3.

**Third, named honestly:** the design assumes Claude Code reliably honors role-scoped subagent contracts. If subagent isolation is weak in practice, the firewall is softer than drawn — but that's a platform property, gettable from real runs, and the Observer's `NOT a fix:` tripwire + the optional lint are the hedge.
