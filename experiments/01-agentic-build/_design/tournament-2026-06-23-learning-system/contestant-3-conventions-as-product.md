# Contestant 3 — Conventions as Product

*Bet: the convention is the object the system improves. Not lessons — the recipes, templates, and rules agents anchor on.*

## Core idea

Agents mirror whatever convention they find, so the system's real job is to keep the **conventions** sharp, not to hoard lessons. Make every convention a **versioned, single-source artifact with a visible changelog** (a "Convention Block": stamped header + body + an embedded `## Changelog`). A run never edits the convention and never writes a fix — it files a one-paragraph **Friction Note** against the convention by ID. When the same convention collects enough friction, a periodic **Sharpening pass** proposes one diff that bumps the version. Anchor-and-mirror flips from trap to engine: agents always anchor on the newest stamped version, so every accepted sharpening compounds into the next run automatically — the consult step is free.

The three objects never fuse: **Friction Note** (what I observed) ≠ **Sharpening** (the unit of work that revises the convention) ≠ **Convention Block** (the thing agents read). That separation is the whole defense.

---

## A. Directory tree

Everything is in-repo markdown, git-tracked. No new top-level concept: a *Convention Block* is just a stamped header that any existing authority doc (`SKILL.md`, `QUERYING.md`, `lead-context.md`, a packet template) already wants. The only genuinely new files are the friction log and the sharpening folder.

```text
experiments/01-agentic-build/
  CONVENTIONS.md                 # registry: one row per Convention Block, its ID, home file, version, status
  friction/
    friction-log.md              # append-only. Raw Friction Notes, one block each, never merged out
    _TEMPLATE.md                 # the Friction Note shape, shown filled
  sharpenings/
    _TEMPLATE.md                 # the Sharpening shape, shown filled
    SH-004-signal-headline-trap/ # one folder per proposed convention revision
      sharpening.md              # the proposed diff + evidence roll-up + decision surface
      decision.md                # Brian's call (or auto-apply receipt), stamped
  BRIAN.md                       # learned-preferences convention block (Brian's recurring corrections)

# Convention Blocks live IN the authority docs they govern — not copied here.
# CONVENTIONS.md only points at them. Examples of homes:
skills/research-company/SKILL.md        # CONV-RC-* blocks (capture recipe, site_notes rule)
QUERYING.md                              # CONV-Q-*  blocks (read recipes, the grouping stamp)
experiments/01-agentic-build/2026-06-21-lead-context.md   # CONV-AB-* blocks (risk calibration, packet shape)
```

**What each thing replaces.** `CONVENTIONS.md` replaces "grep every doc to find the rule that governs X." `friction/friction-log.md` replaces the buried `workflow_note` and MRL's accreting Evidence Logs. `sharpenings/` replaces MRL's fused item-of-work. `BRIAN.md` replaces re-learning Brian's taste every session. The proposal's four-section `LEARNING.md` collapses into *these* — Active Rules become the stamped blocks themselves (in their home doc, where agents already read), Inbox becomes `friction-log.md`, Promotion Queue becomes `sharpenings/`. Nothing is duplicated.

---

## B. Fully populated example files

### B1. A Convention Block (lives inside `skills/research-company/SKILL.md` — shown here as it appears in that file)

This is the distinctive move: the convention carries its own version stamp and changelog *inline*, so the agent reading the recipe sees exactly how sharp it is and why.

```markdown
<!-- CONV-RC-04 · signal-headline-read · v3 · sharpened 2026-06-23 · owner: research-company -->
### Reading a captured Signal: the headline field is the trap

The easiest-to-grep field on a Signal is the one most likely to mislead. Before a
read uses confident language ("trusted", "established", "funded"), surface the
integrity sibling that travels with the headline:

| Headline field        | Integrity sibling that must travel with it          |
|-----------------------|-----------------------------------------------------|
| Trustpilot `score`    | `paid_profile`, `review_count`, invited-review flag |
| Wayback `tenure_days` | snapshot continuity + density (CDX is non-monotone) |
| SEC `total_hits`      | match type / vehicle / CIK / existence-only flag    |

Rule: read the sibling, then label the verdict a **Judgment**, never State.
A bare headline number is snippet-grade until its sibling is in view.

#### Changelog
- v3 (2026-06-23, SH-004): generalized from 3 specific fields to "headline ⇒ find the
  sibling" after the same trap hit a 4th signal (ads transparency zero ≠ not-advertising).
- v2 (2026-06-21, SH-002): added the Wayback CDX non-monotonicity caveat.
- v1 (2026-06-20): first draft, Trustpilot-only.
```

### B2. `friction/friction-log.md` (append-only; the divergent stream that never gets merged out)

```markdown
# Friction Log — Agentic Build

Append-only. One Friction Note per observation. A run files friction; it does NOT
propose a fix and does NOT edit a Convention Block. Notes are never deleted — when a
Sharpening consumes them, they get a `consumed-by:` stamp in place and stay.

See `_TEMPLATE.md` for the shape. The only required discipline: name the convention
you hit by ID (or `unknown` if no convention governs it — that's a coverage gap worth
seeing).

---

### FN-031 · 2026-06-20 · run-034 (ads-transparency read)
- against: CONV-RC-04 (signal-headline-read), v2
- flavor: trap-recurrence
- observed: A clean `0` from Google Ads Transparency for remedymeds/eden was almost
  read as "not advertising." It means "not visible on Transparency for this exact
  target_domain" — they may run Meta ads or land on a different domain. Same shape as
  the Trustpilot-score and Wayback-tenure traps, on a 4th signal source.
- wish: the rule names 3 specific fields; I wanted the *general* form so I'd have
  applied it to a source the rule never listed.
- consumed-by: SH-004

### FN-032 · 2026-06-20 · run-028 (SaaS price-visibility read)
- against: unknown
- flavor: coverage-gap
- observed: `[on-request]` token populated 3/24 off telehealth. A naive grep reads
  "SaaS doesn't gate prices" — the inverse of truth. No convention warned me.
- wish: a read-discipline line: an empty *structured* surface is a coverage signal,
  not a market fact.
- consumed-by: —    # still open; one sighting

### FN-033 · 2026-06-23 · packet (honest-query-time-groupings)
- against: CONV-AB-02 (packet decision-surface)
- flavor: brian-correction
- observed: Brian cut my decision-surface from ~400 words to ~250 and said "lead with
  the call, move root-cause to the linked notes." Second time this session.
- wish: the template should pre-state this so I draft it tight the first time.
- consumed-by: —    # routed to BRIAN.md as a candidate preference
```

### B3. A Sharpening (`sharpenings/SH-004-signal-headline-trap/sharpening.md`)

```markdown
# SH-004 · Generalize the signal-headline-read rule from 3 fields to a shape

- targets: CONV-RC-04 (signal-headline-read) · v2 → v3
- home file: skills/research-company/SKILL.md
- status: PROPOSED
- risk: low (docs-only writing rule; reversible; no schema/code/live behavior)
- opened: 2026-06-23, by sharpening pass over friction-log FN-005, FN-018, FN-031

## Why now (the evidence, rolled up — not merged away)
Four independent Friction Notes hit CONV-RC-04 across four different signal sources,
each re-deriving "the headline field misleads" from scratch:
- FN-005 (run-005, Trustpilot score) — v1 already covers
- FN-018 (run-006, Wayback tenure) — v2 added
- FN-029 (run-007, SEC hits) — v2 covers
- FN-031 (run-034, ads-transparency zero) — **NOT covered**; the rule listed fields,
  not the shape, so the agent nearly missed it.
The trap is general; the convention was enumerative. That gap is what bit run-034.

## Proposed diff (the actual revision)
Replace the field-list framing with the general rule + the table as *examples*:
- before: "These three fields mislead: [score, tenure, hits]"
- after:  "The easiest-to-grep field is the trap; find its integrity sibling. (examples table)"
Adds one line generalizing zero/absence on external sources. Stamp bumps v2 → v3.

## What this replaces
It does NOT add a rule — it *generalizes* one, so the next new signal source is
covered by default instead of needing a v4. Net rule count unchanged; coverage up.

## Decision surface (for Brian — ≤250 words)
**Problem.** A good read-rule was written as a list of 3 fields; a 4th signal source
hit the same trap and the list didn't cover it.
**Decision needed.** Apply the generalization (v2→v3) to SKILL.md, or hold.
**Recommendation: apply.** Low risk, docs-only, reversible; 4 independent sightings.
**Risk:** low. No code, schema, or live behavior.
**You'd be surprised by:** nothing — this only widens an existing rule.
```

And its `decision.md` once Brian rules:

```markdown
# SH-004 — decision
- ruling: APPROVED (Brian, 2026-06-23)
- applied: SKILL.md CONV-RC-04 bumped to v3, commit `a1b2c3d`
- friction consumed: FN-005, FN-018, FN-029, FN-031 (stamped `consumed-by: SH-004` in log)
- note: Brian — "good. this is the right altitude — one rule, not a fork per source."
```

### B4. `BRIAN.md` (the system learns Brian, not just the work)

```markdown
<!-- CONV-BRIAN · brian-preferences · v4 · 2026-06-23 -->
# What Brian keeps correcting

A Convention Block like any other: stamped, changelogged, sharpened from friction
notes flavored `brian-correction`. Agents consult this before drafting anything
Brian will read. Each line is evidence-backed — the FN that earned it is cited.

- **Lead with the call; root-cause on tap, not volunteered.** Decision surfaces open
  with the recommendation, not the problem history. [FN-033, FN-019]
- **Simplify, don't just add.** When sharpening a convention, ask what the change
  *replaces*. A net-new rule needs a stronger bar than a generalization. [FN-007, FN-022]
- **Counts rot — don't bake them.** Never write a surface-count or "Nth sighting" into
  a durable rule; hold as recur-watch instead. [FN-015]
- **Absence isn't proof.** Say "not found in capture" vs "not true in market." [FN-032 pending]

#### Changelog
- v4 (2026-06-23, SH-006): added "lead with the call" after a 2nd brian-correction sighting.
- v3 (2026-06-22): added "counts rot."
```

---

## C. Rules / lifecycle

Four roles, each a verb that starts, writes evidence, and stops. No daemon.

| Step | Who triggers | Writes | Reads | Gate |
|------|-------------|--------|-------|------|
| **File friction** | any run/packet at close | one Friction Note appended to `friction-log.md`, naming the convention by ID | the Convention Block it hit | none — friction is cheap and always welcome |
| **Sharpen** | a human-invoked `/sharpen` pass, run *after a batch or a painful failure* | a `sharpenings/SH-NNN/` folder + a proposed diff to one Convention Block | the whole friction log + `CONVENTIONS.md` | the pass *proposes*, never applies |
| **Decide** | Brian (or auto-apply for the safe class) | `decision.md`; on approval, the Convention Block edit + version bump + `CONVENTIONS.md` row update | the sharpening's decision surface | **human-gated** except the safe class |
| **Consult** | every future run | nothing — it just reads the newest stamped Convention Block | the block in its home doc | free; this is where compounding happens |

**Writes vs reads.** Runs write *only* friction. The sharpen pass writes *only* proposals. Only the decide step (human or safe-auto) writes the convention itself. Three writers, three objects, no fusion.

**What consolidates.** The sharpen pass groups friction *by convention ID* (the registry makes this a `grep`, not judgment). It proposes a diff only when a convention has accreted enough signal — and it proposes the *smallest generalizing* edit, not a fork. Crucially, **grouping is navigation, not deletion**: friction notes are stamped `consumed-by:` in place, never removed, so the divergent record survives (defeats over-compression).

**What prunes / staleness.** A Convention Block can be *retired* by a sharpening (status `RETIRED` in `CONVENTIONS.md`, block struck-through with a tombstone pointing to its replacement). The friction that earned it stays. Staleness is visible: a block whose `sharpened` date is old *and* has open friction against it is the sharpen pass's first target. Nothing silently rots because the version stamp is right there in the doc the agent reads.

**The promotion bar** (when friction earns a sharpening): same spirit as the proposal's, but it gates the *convention revision*, not a lesson —
- the same convention collects ≥2 independent friction notes, **or**
- one friction note is a `brian-correction` (Brian's word is evidence-of-one), **or**
- a miss severe enough that one sighting justifies tightening the rule.
One sighting of a generic friction → stays in the log as recur-watch (this is exactly MRL's "hold for a 2nd sighting" discipline, but the held thing is a *note*, not a fused mega-item).

**The safe auto-apply class (bonus).** A sharpening may self-apply *without* Brian iff all hold: `risk: low`, it *generalizes or clarifies* an existing block (never adds a net-new rule or fork), targets a docs-only writing rule, and consumes ≥3 friction notes. It still writes a full `decision.md` receipt and commits a reviewable diff — Brian can revert any time. Everything else is human-gated.

---

## D. Worked example — the headline-field trap, end to end

Anchor finding: *the easiest-to-grep headline field is the most misleading one* (Trustpilot `score`, Wayback `tenure_days`, SEC `total_hits` each mislead a naive read).

**Stage 1 — Fail/Capture (run-005, Trustpilot).** A read sorts brands by Trustpilot score; remedymeds (4.6) reads "near-excellent," hims (3.0) reads "the trust problem." Reviewer catches it: the gap is invitation posture, not quality. The run files:

```markdown
### FN-005 · 2026-06-19 · run-005
- against: unknown        # no convention warned me
- flavor: trap
- observed: Sorting by Trustpilot score is misleading; remedymeds 4.6 vs hims 3.0 isn't
  a quality gap — it's paid-profile/invited-review posture. The score-only read is wrong.
- wish: a rule telling me the headline field needs its integrity sibling before I trust it.
- consumed-by: —
```

**Stage 2 — Investigate (the sharpen pass).** A `/sharpen` pass over the log sees FN-005 alone — one sighting, `against: unknown`. It does NOT jump to a fix (defeats failure-mode 1). It records the investigation in a stub and holds: *"headline-field trap; one sighting; if a 2nd headline metric misleads the same way, this earns a Convention Block."* The note stays in the log, untouched.

**Stage 3 — Verify (runs 006, 007).** Wayback `tenure_days` (FN-018) and SEC `total_hits` (FN-029) hit the identical shape on different signals. Now three independent sightings across three sources — the diagnosis ("headline ⇒ misleading without its sibling") is a checked pattern, not a guess. Bar met.

**Stage 4 — Distill (Sharpening SH-001 → births CONV-RC-04).** The pass proposes a *new* Convention Block — but written as the **general shape with the three as examples**, not three forks:

```markdown
# SH-001 · Add a signal-headline-read convention
- targets: NEW → CONV-RC-04, home skills/research-company/SKILL.md
- status: PROPOSED · risk: low
- evidence: FN-005, FN-018, FN-029 (3 independent sources, same shape)
- proposed block: "The easiest-to-grep field is the trap; surface its integrity
  sibling, then label the verdict a Judgment." (examples table: score/tenure/hits)
- replaces: three would-be per-source rules with one shape.
```

Brian approves (`decision.md`: *"yes — one rule, examples not forks"*). CONV-RC-04 v1 lands in SKILL.md with its inline changelog. FN-005/018/029 get stamped `consumed-by: SH-001` in the log (preserved, not deleted).

**Stage 5 — Consult (run-034, automatic compounding).** A later ads-transparency read opens SKILL.md, sees CONV-RC-04 v1 stamped right there, and applies it — but v1 enumerated only 3 fields, so the agent *almost* misreads a clean `0`. It catches itself late and files **FN-031** against CONV-RC-04 v2 with `flavor: trap-recurrence` and `wish: I wanted the general form`. That friction feeds **SH-004** (Example B3): generalize v2→v3 so the rule covers *any* new signal source by default.

**Applied change.** v3 lands (Example B1). The *next* signal source Truffle ever adds is covered with zero new rule — the convention got sharper, the anchor agents mirror got better, and nobody re-derived the trap. That is anchor-and-mirror as an engine: each run anchors on a strictly-sharper version than the last.

---

## E. Map to the 5 stages and the 4 failure modes

**5-stage memory progression:**
1. **Fail** — Friction Note captures the miss with run ID + the convention it hit, enough to act on cold.
2. **Investigate** — the sharpen pass diagnoses *why* (here: rule was enumerative, not general) before proposing; a one-sighting note is held with its investigation stub, not actioned.
3. **Verify** — the ≥2-independent-sightings bar (or a Brian correction) turns the diagnosis into a checked fact before any convention moves.
4. **Distill** — the Sharpening writes the *general shape* into the Convention Block, not the specific case (the table is examples, not the rule).
5. **Consult** — future runs read the stamped block in its home doc with zero re-derivation; the version stamp tells them how sharp it is. Compounding is structural: the anchor is always the newest version.

**4 failure modes:**
1. **Collapse observation into solution** — *defeated structurally.* A run can only write a Friction Note (no convention-edit authority). The fix is a separate object (Sharpening) produced by a separate pass that must clear an evidence bar.
2. **Anchor-and-mirror** — *converted to the engine.* Agents do mirror — but they mirror a stamped, continuously-sharpened single source. A crappy first draft can't entrench: it carries a low version, accumulates friction against its ID, and becomes the sharpen pass's first target. The dynamic that was the disease is the cure.
3. **Conflate feedback with item-of-work** — *defeated by three named objects.* Friction Note (feedback) ≠ Sharpening (work) ≠ Convention Block (the artifact). They dedupe (by convention ID), graduate (note→sharpening), and close (sharpening→decision) precisely *because* they're distinct. MRL-002's 15-paragraph accretion is impossible: friction lives in the append-only log, the work lives in `sharpenings/`, and neither grows the convention.
4. **Over-compression** — *defeated by append-only + consumed-by.* The friction log is never merged out; consolidation stamps notes `consumed-by:` in place. The clean view (the Convention Block) is downstream of the divergent record (the log), never a replacement — exactly the retro's prescription. MRL's 345→2 collapse can't happen because the 345 stay in the log, individually traceable.

---

## F. Self-critique

**Weakness 1 — the friction log can still rot into a swamp at scale.** Append-only + never-delete is the anti-over-compression defense, but a 2,000-note log is its own burial. The version-stamp/registry keeps *conventions* findable, but raw friction is only as findable as its `against:` tag, and `against: unknown` notes (the coverage gaps — often the most valuable, per the retro) have no ID to group by. *Fixing it costs:* a periodic archival sweep that moves `consumed-by:`-stamped notes to `friction/archive/YYYY-QN.md` (preserved, out of the working view) and a light triage of `unknown`-tagged notes into provisional convention IDs. That's more machinery — it must stay subtractive-from-the-working-view, not a second backlog. I'd ship without it and add it only when the log actually hurts (it won't at ~3 packets).

**Weakness 2 — "one convention per friction note" assumes clean attribution that won't always hold.** Real friction often indicts *the interaction between two conventions* (e.g., a read recipe AND the packet template), or names a convention that doesn't exist yet. Forcing a single `against:` ID risks mis-filing, which silently corrupts the by-ID grouping the whole consolidation leans on. *Fixing it costs:* allow `against:` to be a list and accept `unknown`/`new:<slug>` freely — cheap in the template, but it weakens the "grep-by-ID" consolidation into "judgment-assisted grouping," reintroducing exactly the steward-overfitting risk the design is trying to avoid. The honest trade: I keep single-ID + `unknown` as the default for grep-ability, accept some mis-attribution, and rely on the sharpen pass (which reads full notes, not just tags) to catch cross-convention friction. It's a real seam, not a solved problem.

**Honest scope note.** This design is strongest where conventions are explicit, written artifacts agents anchor on — which is most of Truffle (`SKILL.md`, `QUERYING.md`, lead-context). It's weaker for friction that isn't *about* a convention at all (a product gap, a missing ingredient). Those route out via `against: unknown` + a `flavor: product-gap` tag to product planning, but that's a hand-off, not something this system resolves — and I'd rather be honest that the conventions-as-product lens deliberately doesn't try to.
