# Contestant 1 — Memory filesystem + Dreaming

*A faithful port of Anthropic's agent-memory + "Dreaming" design to Truffle.*

## Core idea

Two channels, never blurred. **In-band:** during a run, the agent reads a tiny folder of markdown memories with ordinary file tools and appends raw, timestamped observations to an append-only log — it never edits the rules. **Out-of-band:** a separately-invoked **`/dream`** verb is the *only* writer that can promote, edit, or retire a rule — it reads many runs' observations plus the whole memory store, finds what recurs, and emits an evidence-backed proposal for Brian to approve. The split is the whole defense: runs can only *observe*, dreaming is the only place observation turns into rule, and dreaming runs with cross-run eyes so it can't overfit to the one case the run saw.

The mental model is one sentence: **runs leave footprints, dreaming draws the map, Brian signs the map.**

---

## A. Directory tree

Everything lives under one folder, inside the experiment, fully git-tracked. No tool, no daemon, no index.

```text
experiments/01-agentic-build/
  .memory/                              # the entire learning store. One folder of markdown.
    README.md                           # 20-line contract: what writes, what reads, the two channels
    rules.md                            # ACTIVE memory — the rules in-band runs consult. Curated, small.
    observations/                       # IN-BAND, append-only. The footprints. Never edited, only added.
      2026-06-19.md                     # one file per day; runs append dated blocks. Cheap to grep.
      2026-06-20.md
      2026-06-23.md
    retired/                            # SUBTRACTIVE half output. Rules dreaming cut, with the why. Never deleted.
      rules.md                          # tombstones: the old rule text + reason + date + evidence link
    dreams/                             # OUT-OF-BAND output. One file per dream pass. The proposals.
      2026-06-23-dream-001.md           # inputs scanned, patterns found, proposed diffs, evidence, Brian's verdict
  CLAUDE-DREAM.md                       # the /dream verb's own brief (the prompt for the out-of-band pass)
```

That is the entire system: **one active file (`rules.md`), one append log (`observations/`), one trash-with-receipts (`retired/`), one proposal archive (`dreams/`).** When the corpus is thin, only `rules.md` and one observations file exist. It scales by adding dated files, never by adding structure.

**Why not in `.claude/memory/`?** Anthropic's location is per-agent and session-scoped; Truffle's learning object is the *experiment*, and it must travel in the repo so `git log` is the audit trail. `.memory/` beside the packets keeps the footprints next to what made them. (When this graduates to user-facing verbs, each gets its own `skills/<verb>/.memory/` — same shape, different root. See §G.)

---

## B. Fully-populated example files

### B1. `.memory/rules.md` — the active memory (what in-band runs read)

```markdown
# Agentic Build — active memory

Rules in-band runs consult. ONE writer: the /dream verb, after Brian approves a proposal.
A run NEVER edits this file — it appends to observations/ instead. Each rule cites the dream that
promoted it and the observations behind it, so you can always trace and challenge it.

Format per rule:
- **R-NN — one-line rule.** (promoted <date> · dream-NNN · seen in N runs)
  When it bites / what to do. ≤3 lines.

---

## Reading the store (market-read & query verbs)

- **R-03 — The greppable headline field is the misleading one; quote its integrity sibling.**
  (promoted 2026-06-23 · dream-001 · seen in 8 runs)
  Before a read uses confident language on a captured Signal, surface the confound that travels with it:
  Trustpilot score → paid-profile/review-volume; Wayback `tenure_days` → snapshot-density/continuity;
  SEC `total_hits` → match/CIK/existence. State the sibling or label the verdict a Judgment.

## Writing the packet (build verbs)

- **R-01 — A run logs observations, not fixes.** (promoted 2026-06-23 · dream-001 · seen in 4 runs)
  At close, append friction/wish/risk-miss to observations/ as what-you-saw. Proposing the fix is /dream's job.

## Brian's taste (corrections that recur)

- **R-02 — Simplify, don't add. Name what a new field/rule/file replaces.** (promoted 2026-06-23 · dream-001 · seen in 3 corrections)
  Brian's most frequent correction. Before proposing any addition, state what it retires. A change that
  only adds is suspect. (Evidence: overwhelmed-flagged the first lead-context draft for being a policy manual.)
```

### B2. `.memory/observations/2026-06-19.md` — the in-band append log (the footprints)

```markdown
# Observations — 2026-06-19

Append-only. One block per observation. A run NEVER edits a prior block — it adds its own.
Fields are fixed (the string IS the contract): kind / run / saw / not (what I am NOT claiming).
kind ∈ {friction, wish, risk-miss, surprise, brian-correction}. NO "fix:" field — that's /dream's job.

---

- id: OBS-2026-06-19-001
  kind: surprise
  run: mrl/runs/005-trustpilot-signals-reputation-landscape
  saw: The Trustpilot trust_score is the easiest field to grep and the most misleading. remedymeds 4.6
       reads "near-excellent" but the review *bodies* show the same billing-after-cancel cluster as hims 3.0.
       The score gap is invitation posture, not quality.
  not: Not claiming a fix. Not claiming this generalizes past Trustpilot yet.

- id: OBS-2026-06-19-002
  kind: surprise
  run: mrl/runs/006-wayback-offer-tenure-landscape
  saw: Wayback tenure_days is the headline field and it misleads — it measures archiver re-crawl cadence,
       not brand age. A naive "established since" read off it is wrong without snapshot-density context.
  not: Not proposing a schema change. Just: the convenient number lied again, second signal now.
```

### B3. `.memory/dreams/2026-06-23-dream-001.md` — the out-of-band proposal (the map)

```markdown
# Dream pass 001 — 2026-06-23

Out-of-band consolidation. Cross-run visibility. PROPOSES; does not apply. Brian-gated.
Invoked by: /dream  ·  Scanned: observations/2026-06-19.md … 2026-06-23.md (47 blocks, 31 runs) + rules.md (2 rules)

## Verdict (Brian)
- [x] APPROVE R-03 (promote)   [ ] revise   [ ] reject
- [x] APPROVE retire of draft R-99
- Signed: Brian, 2026-06-23. Note: "yes — and fold the SEC case in, don't spawn a 3rd rule."

---

## ADDITIVE half — patterns that recur, proposed as rules

### Proposal P1 → promote R-03 "greppable headline field misleads"
**Prevalence:** 8 observation blocks across 8 distinct runs (005,006,007,011,012,018,019,021), 3 signal families.
**Evidence (verbatim, linked — NOT compressed):**
  - OBS-2026-06-19-001 (Trustpilot score vs review body) → observations/2026-06-19.md
  - OBS-2026-06-19-002 (Wayback tenure_days vs archiver cadence) → observations/2026-06-19.md
  - OBS-2026-06-19-007 (SEC total_hits vs CIK/existence) → observations/2026-06-19.md
  - [+5 more, listed with run ids]
**Why a rule now, not before:** 3+ independent signal families show the SAME shape (greppable head misleads,
  integrity sibling rescues it). Generalizes past any one signal — passes the "rule, not policy-fork" bar.
**Proposed rule text:** [R-03 as it appears in rules.md B1 above]
**Counter-evidence / divergence I am NOT merging away:**
  - OBS-...-019 (visual.md polarity) is adjacent but DIFFERENT: the fix there is "don't aggregate," not
    "surface the sibling." Kept as its own watch (P3), not folded into R-03. Do not collapse these.

### Proposal P2 → promote R-02 "simplify, don't add" (Brian-taste)
**Prevalence:** 3 brian-correction blocks (lead-context v1 "policy manual", MRL triage YAML sprawl, an
  overwhelmed flag). Distinct from work-lessons — this is a *taste* rule that should gate every proposal.
**Evidence:** OBS-...-014, OBS-...-022, OBS-...-031 (all kind: brian-correction). Verbatim linked.

## SUBTRACTIVE half — memory to cut

### Proposal P3 → RETIRE draft R-99 "always sort cohorts by anchor_category"
**Why:** contradicted by run 020 (audience-axis cut) and run 035 (axis breaks on capital allocators).
  Overfit to telehealth. Tombstone it; the underlying signal lives on as a watch, not a rule.
**Action:** move R-99 text → retired/rules.md with this reason + evidence links. Never silent-delete.

## WATCH — seen once, NOT promoted (preserves divergence; does not become a rule)
- W1: visual.md polarity "don't aggregate" (1 run). Hold for 2nd sighting.
- W2: capital-allocators have no pricing surface (1 run). Hold.
```

---

## C. Rules / lifecycle

| Step | Who/what triggers | Writes | Reads | Gate |
|---|---|---|---|---|
| **Consult** (in-band) | Any run, at start | — | `rules.md` (progressive: read headers, open the section that matches the verb) | none |
| **Observe** (in-band) | Any run, at close | appends one block to `observations/<today>.md` | — | none — but it can ONLY append, never edit a rule |
| **Dream** (out-of-band) | Brian runs `/dream` manually (cadence: every ~5–10 runs, or after a painful failure) | a new `dreams/<date>-NNN.md` proposal | all of `observations/`, `rules.md`, `retired/`, run transcripts/packets via `git log` | proposal only — applies nothing |
| **Approve** | Brian checks the boxes in the dream file | — | the dream file | **human gate** |
| **Apply** | the SAME `/dream` session, after approval | edits `rules.md` (promote) and `retired/rules.md` (retire) | the approved dream file | only approved items; each edit cites its dream |

**Progressive disclosure (in-band):** `rules.md` is sectioned by verb-area (Reading / Writing / Brian's taste). A run greps for its area and reads only that section — Anthropic's "load only what's relevant." When `rules.md` outgrows one screen, dreaming splits it into `rules/<area>.md`; never before.

**What consolidates:** only `/dream`, and only by *promoting an observation cluster into a rule* — never by rewriting observations. The footprints are immutable.

**What prunes:** the subtractive half of `/dream`. Staleness is removed by *tombstoning into `retired/`* (text + reason + evidence link), never silent deletion. Observations are never pruned — they're the cheap, append-only divergent record; if `observations/` ever gets heavy, dreaming archives whole *months* into `observations/archive/` untouched, it does not compress them.

**The escalation ladder (the anti-fork law):** observation → (dream finds recurrence ≥ N or severity) → rule → (rule needs code/template change) → a normal **change packet** in `changes/`. A rule is the most a dream may produce; touching a skill or contract is always a packet Brian sees. This is the proposal's "Observation is not a rule. A rule is not a skill edit. A skill edit is a change packet." made structural — each arrow crosses a human gate or a separate verb.

**Promotion bar (when an observation may become a rule):** the same as the proposal — recurs in ≥2 runs, OR a Brian correction, OR an independent review catch, OR severe enough that one occurrence earns a guardrail. Dreaming must *show* which bar was cleared in the proposal. Most observations never graduate; that's correct.

**Low-risk auto-apply (bonus):** a dream proposal tagged `class: editorial` (typo/dead-link/rename in `rules.md`, no new rule, no behavior change) may be applied without a check-box, logged in the dream file as `auto-applied`. New rules and any retire are always human-gated.

---

## D. Worked example — "the greppable headline field is the misleading one"

**1 · Fail / capture (in-band, during run 005).** The agent reads `rules.md` (Consult), does the Trustpilot read, hits the surprise, and at close appends to `observations/2026-06-19.md`:

```markdown
- id: OBS-2026-06-19-001
  kind: surprise
  run: mrl/runs/005-trustpilot-signals-reputation-landscape
  saw: Trustpilot trust_score is the easiest field to grep and the most misleading. remedymeds 4.6 reads
       "near-excellent"; the review bodies show the same billing-after-cancel cluster as hims 3.0.
  not: Not claiming a fix. Not claiming this generalizes past Trustpilot yet.
```
Note the `not:` line — the agent is structurally stopped from proposing a fix. It records what it saw and what it is *not* claiming. (Run 006 and 007 independently append OBS-002 and OBS-007 — Wayback `tenure_days`, SEC `total_hits` — same shape, different signal.)

**2 · Investigate (out-of-band, `/dream` pass).** Brian runs `/dream`. It greps all of `observations/`, clusters by shape, and *sees across runs* that three different signal families produced the same footprint. It writes the WHY into the proposal: "the convenient field is convenient because it's a scalar; the scalar drops the context that makes it true." This investigation lives in `dreams/2026-06-23-dream-001.md` under P1, with all three verbatim observations linked, not summarized.

**3 · Verify.** In the same dream pass, the diagnosis is checked against the evidence: are these really the same mechanism, or three coincidences? The proposal records the test it passed — *"3+ independent signal families show the identical head-misleads / sibling-rescues shape; this is a mechanism, not a coincidence"* — and explicitly carves OUT the `visual.md polarity` case as a *different* mechanism (don't-aggregate, not surface-sibling), so verification doesn't over-merge. That carve-out is the "divergence I am NOT merging away" block in B3.

**4 · Distill.** The proposal states R-03 as a *general* rule — not "handle Trustpilot," but "the greppable headline field misleads; quote its integrity sibling" — covering all three signals and any future one. This is the leap from case to rule, and it's visible and challengeable in the dream file before it's real.

**5 · Consult (applied change).** Brian checks `[x] APPROVE R-03`. The same `/dream` session writes R-03 into `rules.md` (B1), citing dream-001 and the 8 runs. On the **next** market-read run, the agent greps `rules.md` § "Reading the store", finds R-03, and surfaces the integrity sibling *without re-deriving the lesson*. The loop has compounded: the skill is sharper, and you can trace exactly why by following R-03 → dream-001 → the 8 observations.

**If the rule later needs teeth in code** (e.g. a lint that fails a read citing a bare score): that is NOT something `/dream` does — it spawns a normal change packet in `changes/`, which Brian reviews as any other build. The rule stays a writing-rule until a packet earns the code.

---

## E. Map to the 5 stages and 4 failure modes

**5-stage progression:**
1. **Fail** — `observations/<date>.md` append at run close; fixed fields force enough detail (`saw`/`not`/`run`).
2. **Investigate** — the WHY is written in the dream proposal's "Why a rule now" block, with cross-run evidence — not at observe-time, where the agent can't see across runs.
3. **Verify** — the dream proposal must state which promotion bar was cleared and show the diagnosis survives counter-evidence (the carve-out block); Brian's check-box is the final verification.
4. **Distill** — the proposed rule is phrased generally (R-03 covers 3 signals + future ones), reviewable before it's real.
5. **Consult** — next run greps `rules.md` and reads the rule instead of re-deriving; the citation chain proves it compounded.

**4 failure modes — how the structure defeats each:**
1. **Collapse observation into solution** — defeated *structurally*: the observation file has a `not:` field and NO `fix:` field; only `/dream` (cross-run) may produce a rule. A run literally cannot write a fix into memory.
2. **Anchor-and-mirror** — defeated: runs only ever append free observations and read `rules.md`; they never copy a template into the rule store. The only "template" is the immutable observation block + the curated rule format, both owned by the contract, not by the last run's draft. A bad first draft has nowhere to entrench.
3. **Conflate feedback with item-of-work** — defeated: `observations/` (feedback, append-only, immutable) and `rules.md` + `changes/` (items of work) are *different files in different folders*. An observation is linked from a dream, never mutated into one. MRL-002's 15-paragraph accretion can't happen because evidence accretes in the cheap append log, and the *rule* stays one line citing it.
4. **Over-compression** — defeated: `observations/` is never compressed or deduped — dreaming *links* evidence, never merges it, and the "divergence I am NOT merging away" + WATCH blocks are mandatory parts of every proposal. The clean view (`rules.md`) is explicitly downstream of the full divergent record, which survives forever.

---

## F. Self-critique (adversarial)

**Weakness 1 — `/dream` is a manual verb, so the loop only compounds when Brian remembers to run it.** Anthropic's Dreaming runs on idle compute; ours can't (no daemon, by constraint). If Brian doesn't invoke `/dream`, observations pile up un-promoted and the next run re-derives lessons that are sitting one grep away. *Mitigation cost:* cheap — add a one-line nudge to the packet-close step ("N observations since last dream; consider `/dream`") computed from a `git log` count, no standing process. But that's a convention people skip; the honest fix (a scheduled routine) bumps the "no living infrastructure" line, which I've deliberately refused. I'd rather under-automate than reintroduce the daemon MRL's triage-steward effectively was.

**Weakness 2 — the in-band/out-of-band purity has a real cost: latency to learning.** A lesson seen in run 005 can't sharpen run 006 until a dream pass runs *and* Brian approves. For a genuinely severe one-shot miss (a run that almost polluted the store), waiting for the next dream is too slow. The clean model trades immediacy for safety, and that's usually right — but it means the system is *slower* to learn than the naive "edit the skill now" anti-pattern it correctly rejects. *Mitigation cost:* moderate — allow a run to file a `kind: risk-miss` observation tagged `severity: high`, which the packet-close step surfaces to Brian immediately as a one-off (out of band, by hand), bypassing the dream cadence for that single item. It adds one branch to the close step and one tag value; it does not add a fork-table. I'd accept that cost; anything more is the policy-soup MRL died of.

**Honest gap I'm not fixing:** "learn Brian over time" is handled only as much as Brian's corrections get logged as `kind: brian-correction` and promoted to the "Brian's taste" section. That depends on agents actually noticing and logging a correction as such — a soft spot. A stronger design might mine `git log` and overwhelmed-flags for corrections automatically; I've left that to a future `/dream` capability rather than build it now, because the corpus (3 packets, 1 note) can't yet tell a real taste-pattern from noise.
