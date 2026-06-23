# Judge 2 — Elegance & Generalization

*Lens: conceptual elegance and generalization weighted above all. The bar is Anthropic's in-band/out-of-band "Dreaming" split — a model a smart newcomer holds in their head. I reward clarity and memorability of the core model, hardness-to-misuse, and how cleanly the pattern lifts to `skills/` and other projects without overfitting to Agentic Build or MRL. All 7 honor the concrete output contract (tree + filled files + lifecycle + worked example + self-critique); none is prose-only.*

## 30-second skim

**Winner: Design 1 (Memory filesystem + Dreaming).** It owns the cleanest, most memorable mental model in the field — *"runs leave footprints, dreaming draws the map, Brian signs the map"* — and that model is the one explicitly held up as the bar. The in-band/out-of-band split is a *primitive*, not an arrangement of files; it lifts to any verb unchanged.

**Strongest runner-up: Design 5 (Two-Clock Ledger).** Same elegance class via a different image (two clocks at different rates + an Anti-Merge Law). Slightly more folder-machinery than Design 1, but the "Anti-Merge Law" is the single most quotable invariant any contestant produced.

**Most worth grafting:** Design 7's `brian/PREFERENCES.md` mined from real transcript corrections — the only design that *learns Brian from evidence already on disk* rather than hoping agents self-report. Graft the preferences-from-corrections idea onto the winner; leave the transcript dependency behind.

The middle (2, 6, 3) are sound but each pays an elegance tax: Design 2 is the cleanest *MVP* but its two-file model is a subset of Design 1's, not a distinct idea; Design 6 buys queryability with a closed-set schema that re-imports taxonomy-sprawl risk; Design 3's "conventions as product" is a genuinely good reframe but spreads its store across many host docs, which is harder to hold in the head. Design 4 (four agents) is the most overfit to ceremony and the hardest to lift cleanly.

---

## Per-design verdicts

### Design 1 — Memory filesystem + Dreaming *(faithful Anthropic port)*

- **Standout strength.** The mental model is the strongest in the field and it is *load-bearing*, not decoration: in-band runs can only **observe** (append, with a forced `not:` field and no `fix:` field); out-of-band `/dream` is the **only writer** that turns observation into rule, and it runs with cross-run eyes. The split *is* the defense against all four failure modes simultaneously, and it's the exact pattern the frame names as prior art — so it generalizes by construction. The escalation ladder ("observation → rule → change packet," each crossing a gate) is the cleanest statement of the frame's "observation is not a rule is not a skill edit."
- **Fatal flaw (really a soft spot).** `/dream` is a manual verb with no scheduler (correctly, per the no-daemon constraint), so the loop only compounds when Brian remembers to invoke it — and the design *names* this honestly as Weakness 1. It's the same single-point-of-failure every no-daemon design here shares; Design 1 neither hides it nor over-solves it. Not fatal, but it caps autonomy.
- **Four failure modes.** Beats all four structurally and most convincingly: (1) collapse — `not:` field, no `fix:` field, only `/dream` writes rules; (2) anchor-mirror — runs never copy a template, the only anchor is the contract-owned block; (3) conflation — observations and rules are different folders, linked never merged; (4) over-compression — observations never compressed, "divergence I am NOT merging away" + WATCH blocks are mandatory parts of every dream. Best-in-field on the KEY criterion.
- **5-stage progression.** Full distance, and the stages map to *real seams* (Investigate/Verify live in the dream where cross-run sight exists, not at observe-time where it can't) rather than being narrated onto a flat structure.

### Design 2 — Two-Ledger MVP

- **Standout strength.** The single asymmetry — *append-only evidence ⟂ editable work, linked by id, never copied* — is the most ruthlessly minimal correct answer. Three files, one rule, one pre-commit lint that makes append-only mechanical without a daemon. The frame's "design for a thin corpus, don't over-build" is honored better here than anywhere else.
- **Fatal flaw.** Conceptually it is a *strict subset* of Design 1 (observations + work, minus the named out-of-band "dreaming" pass and the subtractive/retired half). On the elegance lens specifically, "two ledgers" is a less memorable, less generative image than "footprints/map/signature" or "two clocks" — it's the right *engineering*, but the *idea* doesn't lift as vividly. Harvest is also a manual single-point-of-failure (same as D1) but without D1's tombstone/retired discipline for the subtractive half.
- **Four failure modes.** Beats all four; collapse-defense is especially strong (the log file *physically cannot hold a fix* — 5 backward-only fields). Marginally thinner than D1/D5 on over-compression because there's no mandated "divergence I'm not merging" artifact, only the append-only guarantee.
- **5-stage progression.** Full distance, cleanly mapped; the MRL contrast (same finding graduates in 4 moves vs accreting 14 paragraphs) is the most concrete proof in the field.

### Design 3 — Conventions as Product

- **Standout strength.** The sharpest *reframe*: the object the system improves is the **convention agents anchor on**, and anchor-and-mirror flips from trap to engine (agents always mirror the newest stamped version, so every accepted sharpening compounds for free). This is the most direct answer to the frame's "invest in conventions" leaning, and the inline version-stamp + changelog is genuinely elegant — the agent reading a recipe sees how sharp it is and why.
- **Fatal flaw.** The store is *distributed across host docs* (Convention Blocks live inside `SKILL.md`, `QUERYING.md`, lead-context). That's clever for consult-locality but it makes the learning system harder to hold in one head and harder to lift wholesale to a new project — you can't point at one folder and say "that's the loop." The `against: <one convention ID>` attribution is also a real seam (the author admits friction often indicts a *pair* of conventions or none), and the whole consolidation leans on that tagging being clean.
- **Four failure modes.** Beats all four, with the most interesting take on #2 (converts anchor-mirror into the engine). #3 strong (three named objects). #4 via append-only + `consumed-by:` in place.
- **5-stage progression.** Full distance; the "rule was enumerative, not general → generalize v2→v3" worked example is the best illustration of *Distill* (case → shape) of any entry.

### Design 4 — Roles & Incentive Design (`.claude/agents/`)

- **Standout strength.** The correct *diagnosis* — MRL "rewarded the wrong thing," so fix WHO does what, not where bytes land — and the firewall between the agent that *observes* and the agent that *proposes* is the single most important split, here made a hard role boundary with tool-scoping. The Editor's "what does this replace?" gate and anti-anchor clause encode Brian's taste into the role contract itself.
- **Fatal flaw.** Four agents (Observer/Curator/Editor/Pruner) is real ceremony for a 3-packet corpus — the design *is* the bureaucracy the frame's non-goals warn against ("no granular policy-manual of forks" in spirit). The author concedes this and offers to ship Observer + merged Curator/Editor first — which is essentially conceding the elegant core is smaller than the design. Worse for this lens: incentives are *prompt-deep, not enforced* (an Observer can smuggle a fix into "what happened"), so the firewall is discipline dressed as structure. And it leans on Claude Code honoring role-scoped subagent contracts — a platform assumption.
- **Four failure modes.** Beats all four *if the role contracts hold*; that conditional is the weakness. The split-cast defense against collapse and conflation is genuinely strong; the anchor-mirror defense (Observer writes from feeling, never reads templates) is clever.
- **5-stage progression.** Full distance, with each stage owned by a different role — elegant on paper, but the stage boundaries are agent-prompt conventions, not file-structural seams, so they're softer than D1/D5/D6.

### Design 5 — Two-Clock Ledger

- **Standout strength.** Co-cleanest model in the field via a distinct image: **two clocks ticking at different rates** (fast greedy `notices/`, slow curated `rules/`) joined by the **Anti-Merge Law** — *"compression happens by adding a rule that points at notices, never by shrinking the notices."* That law is the most quotable, hardest-to-misuse invariant any contestant wrote; it makes over-compression *structurally impossible*, not merely discouraged. The dedicated `brian/` lane and the two written gate tests (Generalization test = "state it without naming a run/company"; Replacement test = "what does it replace?") are excellent.
- **Fatal flaw.** Five folders (`notices/`, `rules/`, `candidates/`, `brian/`, `_consolidations/`) is slightly more surface than the two-channel D1 or three-file D2 — the model is as elegant but the *instantiation* carries more parts to lift. "Shape" (≥3 notices sharing a shape) is a judgment call the gate leans on heavily, and the author honestly flags both under/over-clustering risk.
- **Four failure modes.** Beats all four, best-in-field on over-compression (the Anti-Merge Law + auditable consolidation minutes that *cite what was deliberately left unconsolidated*). Collapse defeated by the no-solution-slot notice + mandatory "What I am NOT claiming" block.
- **5-stage progression.** Full distance; the `_consolidations/` minutes ("read 41 notices, promoted 1 cluster, deliberately left 38") is the only design that makes the *Verify/compression* step itself auditable.

### Design 6 — Queryable Structured Log

- **Standout strength.** Applies Truffle's own deepest principle — *"conventions are infrastructure, queryability is the product"* — to learnings: defeat over-compression by **never compressing the source**, and make consolidation a `grep`/query over closed-set frontmatter rather than a destructive re-read. "Consolidation is a query, not a merge" is a clean, memorable one-liner, and the closed sets fit Truffle's frontmatter ethos hand-in-glove.
- **Fatal flaw.** The closed-set schema (`kind`/`area`/`severity`/`status`/`gate`) is load-bearing *and* filled by the same agents whose judgment we don't fully trust — so it re-imports the exact taxonomy-sprawl/mis-tag risk the engine fights (and that Brian's memory flags as a defense concern). The author names it: a mis-tagged obs lands in the wrong `area` and the `--min-count 2` gate never fires — MRL's "can't see across runs" failure in a new outfit. Also the heaviest day-one build (folder-of-files + `learn.py` + generated digest) for a 4-observation corpus; the author concedes the honest v0 is "one `obs.md` + grep," i.e. closer to Design 2.
- **Four failure modes.** Beats all four structurally (obs template has no fix field; obs ⟂ lessons; raw log never merged). Anchor-mirror only "mostly" defeated, per the author (early lessons could set a tone).
- **5-stage progression.** Full distance; the `gate` field forcing the agent to *name why it's a fact* before a lesson can exist is a nice Verify mechanism.

### Design 7 — Transcript Mining

- **Standout strength.** The boldest and most original bet: **add no capture step at all** — the richest signal (Brian's mid-session corrections, every `/overwhelmed`) already exists verbatim in 460 JSONL transcripts on disk, confirmed empirically. This is the only design that escapes the forcing-function dependency every other design shares (agents must remember to write honest notes), and the only one that *learns Brian from evidence already captured* rather than hoping for self-report. `mine.py` kept deliberately dumb + a cheap Sonnet classifier is the right model-per-subtask call.
- **Fatal flaw.** The load-bearing dependency is an *undocumented Claude Code internal* not under anyone's control — schema can change any release, files can be cleared, multi-machine work splits the corpus, `cwd` scoping only works because Brian runs from one path. The author states this plainly and degrades to "mine git log + notes," but a learning system whose capture source is a found, unguaranteed dependency is the least *trustable* foundation here. It also over-indexes on *noticed* friction and is blind to silent confident-wrong failures (the most dangerous ones). Elegance-wise the core idea is memorable, but the system around it (mine/distill/promote + lexicon tuning + schema-pinning) is more moving parts than the model implies.
- **Four failure modes.** Beats all four for *rules*; honestly concedes the *distill agent itself* can still anchor on the last proposal's framing — a residual, non-structural gap.
- **5-stage progression.** Full distance; "the threshold IS the verification (≥2 distinct sessions + would-have-prevented yes)" is a crisp Verify.

---

## Ranked list (best → worst)

1. **Design 1 — Memory filesystem + Dreaming.** The clearest, most memorable model in the field and the one the frame itself nominates as the bar; the in-band/out-of-band split is a primitive that beats all four failure modes at once and lifts to any verb unchanged. Wins the KEY criteria (elegance + failure modes + generalization).
2. **Design 5 — Two-Clock Ledger.** Co-elegant via a distinct image; the Anti-Merge Law is the hardest-to-misuse invariant produced and makes over-compression structurally impossible. Loses to D1 only on folder-count and "shape"-judgment dependence.
3. **Design 2 — Two-Ledger MVP.** The most ruthlessly right-sized correct answer and best thin-corpus fit, but its model is a subset of D1's rather than a distinct, generative idea — superb engineering, slightly less memorable concept.
4. **Design 3 — Conventions as Product.** Best *reframe* (the convention is the object; anchor-mirror becomes the engine) and the truest answer to "invest in conventions," but the store distributed across host docs is harder to hold in one head and to lift wholesale.
5. **Design 6 — Queryable Structured Log.** Cleanest fit with Truffle's "queryability is the product" ethos and a memorable "consolidate = query not merge," but the load-bearing closed-set schema re-imports tag-sprawl risk and it's the heaviest day-one build for a thin corpus.
6. **Design 7 — Transcript Mining.** Most original idea and the only evidence-based Brian-learning, but the capture source is an unguaranteed Claude Code internal — the least trustable foundation — and it's blind to silent failures; better as a *graft* than a spine.
7. **Design 4 — Roles & Incentive Design.** Correct diagnosis and the right firewall (observe ⟂ propose), but four agents is ceremony for a 3-packet corpus, the incentives are prompt-deep not enforced, and the stage seams are agent conventions rather than structure — hardest to lift cleanly and most at odds with the frame's no-policy-manual non-goal.

---

## Recommendation

- **Winner: Design 1 (Memory filesystem + Dreaming).** It best satisfies the lens's KEY criteria — conceptual elegance, beating the four failure modes, and clean generalization — with a model a newcomer holds in their head on first read. Its observe/dream/sign split is the frame's own prior art made concrete, and `skills/<verb>/.memory/` lifts it to user-facing verbs with zero reshaping.
- **Strongest runner-up: Design 5 (Two-Clock Ledger).** Equally elegant via a different, equally portable image; its Anti-Merge Law is the single best invariant in the tournament and worth preserving even if D1 wins.
- **Idea most worth grafting (from a non-winner): Design 7's `brian/PREFERENCES.md` mined from real corrections.** Every design tries to "learn Brian," but only D7 sources it from corrections *already on disk* rather than hoping agents log them. Graft "mine Brian's recurring corrections (incl. every `/overwhelmed`) into a dedicated, evidence-cited preferences file" onto the winner's `/dream` pass — keeping it as one optional input, not a transcript-dependent spine. (Design 5's dedicated `brian/` lane and Design 3's `BRIAN.md` are the natural homes for it.)
