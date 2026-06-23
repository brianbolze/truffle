# Judge 1 — Failure-Mode Skeptic

*Lens: which design most structurally prevents the four failure modes, and which actually reaches Verify/Distill/Consult instead of stalling at Fail/Investigate. I distrust elegance that rots after 50 runs.*

## The shared shape — and why it matters

Every one of the seven converged on the same skeleton: **append-only raw observations ⟂ separate gated work/rule object, linked by id, consolidated by a manual out-of-band pass.** That convergence is itself a verdict — it is the correct answer to the frame, and it cleanly defeats failure modes 1, 3, and 4 *on paper* for all of them. So the contest is NOT "who has the idea." It is: **who makes the wall load-bearing rather than a comment, who survives scale, who actually closes the loop to Consult, and who internalizes Brian.** That is where they separate hard.

None is prose-only; all honor the concrete output contract (tree + filled examples + lifecycle + worked example + failure-mode map + self-critique). No heavy penalty on that axis. The separation is quality of structure.

---

## Per-design verdicts

### Design 1 — Memory filesystem + Dreaming (Anthropic port)
**Standout strength:** The escalation ladder made *structural* — "observation → rule → change packet," each arrow crossing a human gate or a different verb. The `not:` field (what I'm NOT claiming) and the absent `fix:` field are a genuinely clever forcing function, and the mandatory "divergence I am NOT merging away" + WATCH blocks in every dream are the single best anti-over-compression mechanic in the field — it forces the consolidator to *name what it refused to merge*, which is exactly MRL's missing audit.

**Fatal flaw:** It's a faithful *port* of a design built for idle-compute Dreaming, and it knows it — the author admits `/dream` only fires when Brian remembers. Strip the daemon (correctly, per non-goals) and you've kept the ceremony of the original (four folders, dream-pass archive, CLAUDE-DREAM.md) without the engine that made it run. The richest structure of any entry, carrying the most rot surface if the manual cadence slips.

**Beats the 4 modes:** Strongly, all four — arguably the most *explicit* defeat of over-compression of the set (the carve-out block).
**5-stage reach:** Full Fail→Consult, with the cleanest citation chain (R-03 → dream-001 → 8 obs) proving compounding. Reaches Consult convincingly.
**Brian:** "brian-correction" kind + a "Brian's taste" rules section — present but bolted on; weakest of the top tier on this, depends on agents self-labeling a correction.

### Design 2 — The Two-Ledger MVP
**Standout strength:** Ruthless right-sizing. Three files, one rule (append-only log ⟂ editable work), and a **15-line pre-commit lint that makes the one load-bearing rule mechanical** instead of a convention you hope holds. It is the only design that turns "the log is immutable" from prose into an enforced gate at the cheapest possible cost — perfectly inside Truffle's "the string IS the contract / lint gates are the system" ethos. The MRL-008 contrast (same finding graduates in 4 moves vs. accreting 14 paragraphs) is the most convincing worked proof of the loop closing.

**Fatal flaw:** Findability degrades as a single flat `observations.log.md` grows; harvest quality is capped by what the harvester can hold in context, and the seam (shard + tags) is named-not-built. Real, but it's a *thin-corpus-appropriate deferral*, not a design error — and the schema migrates mechanically.

**Beats the 4 modes:** Strongly all four, and #1 (collapse) is enforced by a file that *physically cannot hold a fix* (5 backward-only fields) — the same defense as the leaders but at a fraction of the complexity.
**5-stage reach:** Full Fail→Consult; Distill lands in `QUERYING.md`/the recipe (where it's actually consulted), not the learning folder — correctly puts the rule where compounding happens.
**Brian:** `kind: brian-correction` is first-class input and W-005 shows it graduating into the *template agents anchor on* — structurally encoding taste, not re-correcting. Strong, and cheaper than the dedicated-lane designs.

### Design 3 — Conventions as Product
**Standout strength:** The sharpest single *insight* in the tournament: it inverts anchor-and-mirror from trap into engine. Agents always mirror — so make the thing they mirror a versioned, changelogged, single-source Convention Block living *in the doc they already read* (SKILL.md, QUERYING.md). Every accepted sharpening compounds into the next run for free; the consult step is literally just reading the newest stamp. This is the only design where compounding is automatic rather than a separate "go read the rules" step, and it directly answers the frame's "conventions are the leverage point."

**Fatal flaw:** Attribution. "One convention per friction note" assumes clean `against: CONV-ID` tagging that won't hold — real friction indicts the *interaction* of two conventions, or one that doesn't exist yet. The whole consolidation leans on grep-by-ID; `against: unknown` notes (often the most valuable coverage gaps) have no ID to group by and rot in the log. The author sees this and accepts it, but it's the load-bearing seam and it's genuinely soft.

**Beats the 4 modes:** Strongly — and it's the *only* one that converts mode #2 into a feature rather than merely defending against it.
**5-stage reach:** Full Fail→Consult, with the tightest Consult of all (stamped block in the home doc).
**Brian:** Dedicated `BRIAN.md` Convention Block, sharpened from `brian-correction` friction, consulted before drafting anything Brian reads. Among the strongest.

### Design 4 — Roles & Incentive Design (.claude/agents)
**Standout strength:** Correctly diagnoses that MRL *rewarded the wrong thing* and attacks WHO does what — Observer (forbidden to propose, tool-scoped to one file) ⟂ Curator (clusters, never invents) ⟂ Editor (the only proposer, must Investigate→Verify→Distill) ⟂ Pruner. The Editor's mandatory "what does this replace?" + anti-anchor "sharpen the existing rule, don't append a sibling" is the most explicit anti-policy-table-fork mechanism in the field, and it walks the full 5-stage pipeline by *construction* because each stage is a different agent that can't skip the prior one.

**Fatal flaw:** The incentives are **prompt-deep, not enforced** — "FORBIDDEN to propose" is an instruction an Observer can smuggle past by writing a fix into "what happened." The firewall is discipline, not a wall (the author admits this; the lint is named-not-built). And four agents for a 3-packet corpus is real ceremony — exactly the bureaucracy the frame warns against. The defense is the costliest to operate of any design.

**Beats the 4 modes:** Strongly in *intent*, but enforcement is softer than Designs 2/6 because it rests on subagent contract-honoring (a platform property, not a structural guarantee).
**5-stage reach:** Full Fail→Consult, and the most *legible* mapping of stages-to-actors.
**Brian:** `brian-tells.md` consulted by every role, checked by the Editor against proposals. Strong and well-integrated.

### Design 5 — Two-Clock Ledger
**Standout strength:** The Anti-Merge Law stated as a single crisp invariant — "compression happens by *adding* a rule that points at notices, never by *shrinking* the notices" — plus the `_consolidations/` minutes that *cite what they read and chose to drop* ("read 41, promoted 1, deliberately left 38, edited none"). That auditable-restraint record is the honest version of MRL's useless Steward Pass Log and is a real contribution. The two written gate tests (Generalization: state it without naming a run; Replacement: what does it replace?) are clean.

**Fatal flaw:** One-file-per-notice means hundreds of tiny files with no enforcement that the log stays immutable (no lint, unlike Design 2) — it's a convention again. And "shape" is a judgment call the gate leans on entirely; the author honestly flags both under- and over-clustering risk at Clock 2, which reintroduces the steward-overfitting the design exists to kill. Strong principles, slightly weaker mechanics than 2/6 because nothing *enforces* the law.

**Beats the 4 modes:** Strongly all four; the Anti-Merge Law is the most quotable defeat of over-compression.
**5-stage reach:** Full Fail→Consult.
**Brian:** Dedicated `brian/` lane with its own slower review cadence — among the strongest, on par with 3.

### Design 6 — Queryable Structured Log
**Standout strength:** Applies Truffle's actual house principle — "conventions are infrastructure, queryability is the product" — to learnings: closed-set frontmatter (`kind/area/severity/status/gate`) makes "did this happen before?" a **`grep`/query, not a destructive re-read an agent must summarize.** That is the most *Truffle-native* framing in the field and it directly targets MRL's "can't see across runs" by making cross-run detection a mechanical `--min-count 2` query rather than a human holding 345 obs in context. The `gate` field forcing the agent to *name why it's a fact* (cross-run/brian/review/severe-once) before a lesson can exist is a sharp, cheap Verify mechanism.

**Fatal flaw:** Query quality is the new single point of failure — it moves the risk from "agent over-compresses" to "agent mis-tags `area`/`kind`, the same finding lands in two buckets, and `--min-count 2` never fires." The closed sets are load-bearing and filled by the same agents we don't fully trust; sloppy tagging silently recreates MRL's blindness in a new outfit. The author names this squarely and the mitigation (tagging lint) is named-not-built. The full tree (per-file + learn.py + generated digest) is also heavier than 3 packets need — though the author explicitly says start as one `obs.md` + grep and grow, which defuses it.

**Beats the 4 modes:** Strongly all four; #1 and #3 are structural (obs template has no fix field, different folders/mutability).
**5-stage reach:** Full Fail→Consult; `consult.md` regenerated digest is a clean Consult surface.
**Brian:** `brian-taste` is just another `area` value — corrections consolidate by the *same* query as technical patterns, graduating to a lesson on the same gate. Elegant economy: learns Brian with zero special subsystem. I rate this the most *parsimonious* Brian-handling, slightly behind 3/5 on dedicated prominence but ahead on simplicity.

### Design 7 — Transcript Mining
**Standout strength:** The boldest and most original bet, and it did the homework — empirically confirmed 460 JSONL transcripts (1.3 GB) containing Brian's corrections *verbatim* ("your proposal is too long", every `/overwhelmed` firing as a labeled friction event). It is the only design with **zero capture step** — it reads what already happened instead of trusting agents to dutifully self-report, which directly attacks the `workflow_note`-rots problem at its root. If capture honesty is the real bottleneck (it plausibly is — agents skip/sanitize notes), this is the only design that removes the bottleneck rather than disciplining it.

**Fatal flaw:** The load-bearing dependency is an **undocumented Claude Code internal** the author confirmed by reading, not an API — schema can change any release, files can clear, multi-machine splits the corpus, `cwd` scoping only works because Brian runs from one path. The author is admirably honest (degrades to "mine git log + notes"), but a learning system whose primary input can vanish on a Claude Code update is fragile in a way the frame's "file-first, attributable, revertible" constraint specifically guards against. Second flaw the author names: transcript mining over-indexes on *noticed* friction and is blind to silent failures (confident-wrong that Brian never caught) — the most dangerous misses leave no trace.

**Beats the 4 modes:** Strongly for rules; honestly flags that the *distill agent itself can still anchor* on the last proposal's framing (mode #2 residual, mitigation weak). Slightly behind the leaders on enforcement.
**5-stage reach:** Full Fail→Consult; the mine→distill→promote→consult chain is complete and the `/overwhelmed`-as-label idea is the single best Brian-signal in the tournament.
**Brian:** Paradoxically the best raw *signal* (verbatim corrections, `/overwhelmed` as ground truth) wrapped in the most fragile *delivery*. `PREFERENCES.md` with ≥2-sighting discipline is strong.

---

## Ranked list (best → worst)

1. **Design 2 — Two-Ledger MVP.** Wins on the lens that matters most: it makes the one load-bearing rule (append-only) *mechanically enforced* by a 15-line lint at the lowest complexity of any entry, defeats all four modes structurally, closes the full loop to Consult in the right place (the recipe, not the learning folder), and right-sizes for a 3-packet corpus without sacrificing scale (named seams migrate cleanly). Best ethos fit. Hardest to make rot.
2. **Design 6 — Queryable Structured Log.** The most Truffle-native framing (queryability is the product), turns cross-run detection into a mechanical query that directly kills MRL's blindness, and learns Brian with zero special machinery. Loses to #2 only because tag-quality is an un-enforced single point of failure where #2's append-only lint is enforced — and its full tree is heavier than #2's three files.
3. **Design 3 — Conventions as Product.** The sharpest insight (anchor-and-mirror becomes the engine; compounding is automatic via stamped blocks in the home doc) and excellent Brian handling. Drops below 2/6 because its consolidation leans entirely on `against:` attribution that won't hold cleanly, and `unknown`-tagged coverage gaps — often the best signal — have no ID to group by.
4. **Design 5 — Two-Clock Ledger.** Cleanest *principles* (Anti-Merge Law, auditable consolidation minutes, two written gate tests, dedicated Brian lane). Falls behind 3 because nothing *enforces* the immutability (convention, not lint, unlike #2) and "shape"-clustering reintroduces steward judgment risk; hundreds of tiny files with no findability aid.
5. **Design 1 — Memory filesystem + Dreaming.** Full loop, best explicit over-compression defense (the carve-out/WATCH blocks), strong citation chain. Penalized for being the highest-ceremony design carrying the most rot surface, a faithful port of a daemon-dependent original run without the daemon, and the weakest (bolted-on) Brian handling of the top tier.
6. **Design 4 — Roles & Incentive Design.** Correct diagnosis (rewarded the wrong thing) and the most legible stage-to-actor mapping, but its firewall is prompt-deep not enforced, and four agents for a 3-packet corpus is the exact bureaucracy the frame warns against — defense at the highest operating cost, resting on a platform property (subagent contract-honoring) rather than a structural guarantee.
7. **Design 7 — Transcript Mining.** The most original bet and the best raw Brian signal, but ranked last *as a primary architecture* because its load-bearing input is an undocumented, unowned, mutable Claude Code internal — fragile against the frame's "file-first, attributable, revertible" constraint — and it's structurally blind to silent (uncorrected) failures. Brilliant as a feeder, risky as a foundation.

---

## Recommendation

**Winner: Design 2 (Two-Ledger MVP).** Under a failure-mode-skeptic lens, the question is not "best idea" but "what won't rot after 50 runs and can't be cheated." Design 2 is the only entry that makes its single load-bearing invariant *mechanically enforced* at near-zero cost, sits exactly inside Truffle's lint-gates-are-the-system ethos, reaches Consult in the place that actually compounds, and is honest about its one real seam (findability) as a deferral rather than a flaw. It is the hardest to corrupt and the cheapest to run.

**Strongest runner-up: Design 6 (Queryable Structured Log)** — the same structural defenses with a more Truffle-native query framing and a more parsimonious Brian handling; it loses only on enforced-vs-conventional tag discipline. (Design 3 is the runner-up on *insight*, but 6 is the safer build.)

**One idea most worth grafting:** From **Design 7**, treat **`/overwhelmed` invocations (and verbatim Brian corrections mined from transcripts) as first-class, pre-labeled friction events** feeding the winner's observation log. The frame explicitly names `/overwhelmed` as a learnable signal; Design 7 proved it's sitting in readable transcripts right now. Graft it as an *optional feeder* into Design 2's log — not the primary capture path (which stays the forced packet-close append), so the fragile dependency degrades gracefully — giving the winner the best Brian-signal in the tournament without inheriting Design 7's foundational fragility. Design 3's stamped-changelog-in-the-home-doc Convention Block is the second-most-graftable idea, for making Consult automatic.
