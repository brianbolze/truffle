# Judge 3 — Brian-Fit & Pragmatism

*Independent ranking. Lens weights: beats-the-4-failure-modes [KEY], conceptual elegance [KEY], internalizes-Brian [KEY] — then right-sized/scales, Truffle-ethos fit, frame fidelity, generalizability. Pragmatism and Brian-fit dominate.*

## 30-second skim

**Winner: Design 2 (Two-Ledger MVP). Runner-up: Design 5 (Two-Clock).** Both nail the one asymmetry the whole frame turns on — append-only evidence ⟂ editable work — but Design 2 ships it in three files with one lint and earns the "what does this replace?" test at every layer, which is exactly Brian's posture. Design 5 is the same skeleton with more folders and a cleaner Anti-Merge Law; it's the better-articulated *concept* but heavier to build today. Design 1 (Dreaming port) is conceptually elegant and the closest in spirit to the prior art Brian flagged, but the manual `/dream` cadence is a real reliability gap and it's slightly more apparatus than the corpus needs. Designs 3, 4, 6 each overbuild a single dimension (conventions registry / four agents / closed-set query schema) — strong ideas, premature machinery at n=3. **Design 7 (transcript mining) is the most exciting bet and the riskiest: it's the only one that captures Brian's corrections in his own words for free, but it's built on an undocumented Claude Code internal — graft the idea, don't ship the foundation.**

No design is prose-only; all seven produced real trees and populated files. None gets penalized on the output contract.

---

## Per-design verdicts

### Design 1 — Memory filesystem + Dreaming
- **Standout strength:** The cleanest in-band/out-of-band split, faithfully ported from the exact prior art (Anthropic Dreaming) Brian named in the frame. "Runs leave footprints, dreaming draws the map, Brian signs the map" is the most memorable one-line model in the field, and the `not:` field on observations is a genuinely clever structural block on solution-collapse. The escalation ladder (observation → rule → change packet, each crossing a gate) maps the frame's "Observation is not a rule…" line into structure better than anyone.
- **Fatal flaw:** Not fatal, but real — `/dream` is a manual verb with no nudge that survives discipline, so the loop only compounds when Brian remembers to run it, and the author honestly admits it. Slightly more apparatus (4 directory roles + a separate `CLAUDE-DREAM.md` brief) than 3 packets need; the `retired/` + `dreams/` + `observations/` + `rules.md` spread is more than Design 2's three files for the same defended properties.
- **4 failure modes:** Beats all four structurally. Collapse → `not:` field, no `fix:` slot. Anchor-mirror → runs never copy a template. Conflate → observations folder ⟂ rules.md. Over-compression → observations never merged, "divergence I am NOT merging away" block is mandatory. Among the strongest on the KEY criterion.
- **5-stage progression:** Full. Maps each stage explicitly and the citation chain (R-03 → dream-001 → 8 observations) makes compounding inspectable.
- **Brian-fit:** Good but not best — `brian-correction` is a `kind` value that bubbles into a "Brian's taste" section via dreaming. Honest that this depends on agents noticing and logging corrections; no dedicated lane as durable as Design 5's `brian/`.

### Design 2 — Two-Ledger MVP
- **Standout strength:** Maximum defended-property-per-byte. Three files, one folder, one lint, and the entire safety argument rests on a single named asymmetry (append-only `observations.log.md` ⟂ editable `work.md`). It earns "what does this replace?" out loud at every layer (the folder replaces `triage.md` + the proposal's `LEARNING.md` + the `workflow_note` graveyard; W-005 *is* the learn-Brian requirement). The 15-line pre-commit append-only check is the lightest possible mechanical enforcement and fits "the string IS the contract" exactly. The MRL-008 contrast ("same finding, two ledgers: graduates in four moves, evidence still all there") is the most concrete proof-of-cure any contestant offers.
- **Fatal flaw:** None fatal. The honest seams: findability degrades as the log grows (deferred shard-by-month, correctly not built now), and harvest is a human-discipline single point of failure (shared by every no-daemon design here). Both named, both cheap to open later.
- **4 failure modes:** Beats all four, and is the most explicit that the log file *physically cannot hold a fix* (5 backward-only fields). Over-compression defense is load-bearing and tied directly to the MRL 345→2 autopsy.
- **5-stage progression:** Full, and the worked example is the tightest end-to-end walk in the field.
- **Brian-fit:** `kind: brian-correction` is first-class input; W-005 graduates Brian's "subtract-first" taste into the template agents anchor on. Slightly less ceremonious than Design 5's dedicated lane, but structurally equivalent and lighter — which is itself a Brian-fit point.

### Design 3 — Conventions as Product
- **Standout strength:** The single best reframe of a failure mode — it converts anchor-and-mirror from trap to engine by making agents always mirror the *newest stamped convention version*. Inline version stamp + changelog living *in the doc agents already read* (not a separate store) is elegant and directly serves the frame's "conventions should be improvable, not calcified" should-have. `BRIAN.md` as just-another-Convention-Block is clean.
- **Fatal flaw:** Overbuilt for the corpus. A `CONVENTIONS.md` registry + per-sharpening folders + `consumed-by` stamping + a friction-log + the convention-block header discipline is a lot of moving parts at n=3. The "one convention per friction note" attribution assumption is shaky (the author admits friction often indicts the *interaction* of two conventions), and `against: unknown` notes — often the most valuable — have no ID to group by, undercutting the consolidation engine.
- **4 failure modes:** Beats all four on paper. Anchor-mirror is its showcase. Over-compression via `consumed-by:` in place is sound.
- **5-stage progression:** Full.
- **Brian-fit:** Strong — `BRIAN.md` with cited evidence per line and a changelog. But it sits inside the heaviest machinery, so the Brian-learning rides on more apparatus than it needs.

### Design 4 — Roles & Incentive (`.claude/agents/`)
- **Standout strength:** The sharpest diagnosis — "the MRL failure rewarded the wrong thing; fix WHO does what, not where bytes land." Splitting Observer (forbidden to propose, tool-scoped to one file) from Editor (only proposer, must verify before distilling) is the most direct structural firewall against collapse, and the anti-anchor clause ("sharpen the existing rule, don't append a sibling") is excellent.
- **Fatal flaw:** Four agent contracts for a 3-packet corpus is the clearest over-engineering in the field — the exact bureaucracy the frame warns against. Worse, the firewall is *prompt-deep, not enforced*: "FORBIDDEN to propose" is an instruction an agent can smuggle past, and the whole design leans on Claude Code honoring role-scoped subagent contracts — a platform assumption, not a wall. The author concedes both. The storage layer (the thing actually being judged) is deliberately thin and underspecified relative to the role prose.
- **4 failure modes:** Beats all four *if* role isolation holds; softer than the file-structural designs because the defense is incentive/prompt rather than a file that can't hold a fix.
- **5-stage progression:** Full, and the separation of capture-agent from investigate-agent enforces the stages well.
- **Brian-fit:** `brian-tells.md` is a solid populated lane that roles consult and the Editor checks against. Good, sourced.

### Design 5 — Two-Clock Ledger
- **Standout strength:** The best-articulated *concept*. The Anti-Merge Law — "compression happens by adding a rule that points at notices, never by shrinking the notices" — is the single cleanest statement of the over-compression defense anyone wrote, and the `_consolidations/` minutes ("read 41 notices, promoted 1 cluster, deliberately left 38 unconsolidated") make over-compression *auditable*, which no one else does. The Generalization test ("state the rule without naming any run/company") and Replacement test are Brian's principles made into explicit gates. Dedicated `brian/` lane with slow-aging review dates is the strongest learn-Brian structure in the field.
- **Fatal flaw:** Heavier than Design 2 for the same core asymmetry — five folders (`notices/`, `rules/`, `candidates/`, `brian/`, `_consolidations/`) where Design 2 ships three files. One-file-per-notice means hundreds of files early; "shape" clustering is a judgment call the author honestly flags as the gate's soft spot. Right-sized for *scale*, slightly over-sized for *now*.
- **4 failure modes:** Beats all four, arguably the most rigorously (Anti-Merge Law + auditable minutes). Tied with Design 2 on the KEY criterion, ahead on articulation.
- **5-stage progression:** Full, with the `kind` taxonomy keeping the incentive on harvesting divergence — directly answering the frame's "aimed at the wrong target" hazard.
- **Brian-fit:** Best dedicated structure (`brian/B02`, sourced, slow-aging). Edges Design 2 here specifically.

### Design 6 — Queryable Structured Log
- **Standout strength:** Applies Truffle's own deepest principle — "conventions are infrastructure, queryability is the product" — to learnings: consolidation is a `grep` over closed-set frontmatter, not a destructive re-read. The closed sets (`kind/area/severity/status/gate`) mirror the engine's existing frontmatter discipline perfectly, and `brian-taste` as just-another-`area` value is clean.
- **Fatal flaw:** Most honest self-critique in the field, and it's damning: query quality is the new single point of failure (sloppy `area` tags → cross-run pattern never fires, MRL's blindness in a new outfit), and the author admits the full tree is the *target, not the day-one build* — the honest v0 is "one `obs.md` + grep," which is essentially Design 2 with more schema. A `learn.py` + generated `consult.md` + closed-set vocab is more machinery than 4 observations need, and inventing the `area` vocabulary before the corpus reveals the real axes courts the taxonomy-sprawl the engine fights.
- **4 failure modes:** Beats all four structurally (no fix field in obs; obs ⟂ lessons). Residual anchor-mirror risk in early lessons setting tone, honestly flagged.
- **5-stage progression:** Full; the `gate` field forcing a named verification reason is a nice touch.
- **Brian-fit:** Solid — `brian-taste` obs consolidate on the same gate as technical patterns. No special subsystem, which is elegant but gives Brian-learning no protected lane.

### Design 7 — Transcript Mining
- **Standout strength:** The only design with **zero capture step** and the only one that learns Brian *in his own words for free* — it mines the 460 JSONL session transcripts (empirically confirmed) for `/overwhelmed` firings and verbatim corrections ("your proposal is too long," "verb runs is a little misleading," "find simpler language"). This is the single best answer to the frame's "internalize Brian's preferences and context" goal, because it doesn't depend on an agent remembering to log a correction — the correction already happened and is on disk. `/overwhelmed` as a free labeled training signal is inspired.
- **Fatal flaw:** The load-bearing foundation is an **undocumented Claude Code internal** not under anyone's control — schema can change any release, files can be cleared, multi-machine work splits the corpus. The author is admirably honest that this is "a found dependency, not a guaranteed one." It also over-indexes on *noticed* friction (silent failures leave no transcript correction — the most dangerous misses are invisible), and `mine.py` is the one piece of standing-ish code that brushes the "no living infrastructure" line hardest. The downstream layer (cards → rules) is essentially Design 2's two-ledger shape, so the novel part is the fragile part.
- **4 failure modes:** Beats all four for *rules*; honestly concedes the distill agent itself can still anchor on the last proposal's framing (non-structural mitigation).
- **5-stage progression:** Full.
- **Brian-fit:** Best *idea* in the field by a wide margin — but riding on the least durable foundation.

---

## Ranked list (best → worst)

1. **Design 2 — Two-Ledger MVP.** Most defended-property-per-byte; the single append-only⟂editable asymmetry, three files, one lint, "what does this replace?" earned at every layer. Right-sized for now, named seams for scale, most buildable today, fits the ethos exactly. The frame's MVP made real.
2. **Design 5 — Two-Clock.** Same core asymmetry, best-articulated concept (Anti-Merge Law, auditable consolidation minutes, strongest `brian/` lane) — loses to #2 only on being heavier than the corpus needs today.
3. **Design 1 — Dreaming port.** Most elegant model and closest to the prior art Brian flagged; beats all four modes structurally. Docked for manual-cadence reliability gap and slightly-more-than-needed apparatus.
4. **Design 6 — Queryable log.** Best ethos-fit on paper (queryability-as-product), but the author concedes the real v0 collapses toward Design 2 and the closed-set vocab is premature schema at n=3.
5. **Design 3 — Conventions as Product.** Best single reframe (anchor-mirror as engine) and clean `BRIAN.md`, but the registry + sharpening folders + attribution assumptions overbuild for the corpus.
6. **Design 4 — Roles & Incentive.** Sharpest diagnosis, but four agents at n=3 is the clearest over-engineering and the firewall is prompt-deep, not file-structural; the storage layer being judged is underspecified.
7. **Design 7 — Transcript Mining.** The most valuable *idea* (free, in-his-own-words Brian-learning) but the worst *foundation* (undocumented CC internal, blind to silent failures); the durable layer just re-implements #2. Graft the idea, not the build.

*Note on the tail: #6 over #3 over #4 because #6's overbuild is at least the engine's own native idiom and degrades gracefully to #2; #3's and #4's overbuilds add genuinely new apparatus. #7 is last on pragmatism/buildability despite topping Brian-fit-of-idea, because the lens weights a real, buildable, durable artifact and its foundation is none of those.*

---

## Recommendation

**Winner: Design 2 (Two-Ledger MVP).** It is the only design that fully internalizes Brian's "find the simplest thing that works and cut the rest" *in its own structure* — three files, one lint, every layer justifying what it replaces. It beats all four failure modes with a file that physically cannot hold a fix, fits the file-first/git/propose-don't-write ethos without a single new concept, works at n=3 today, and names (without prematurely building) its scaling seams. It's the most buildable artifact in the field.

**Strongest runner-up: Design 5 (Two-Clock).** Same winning asymmetry, articulated even more rigorously, with the field's best Brian-learning lane and the only auditable-consolidation mechanism (the minutes file). If the team expects the corpus to grow fast, #5's structure is where #2 graduates to anyway — they are the same design at two scales.

**The one idea most worth grafting (from a non-winner): Design 7's `/overwhelmed`-and-correction transcript mining as a *supplementary, best-effort* feeder into Design 2's `observations.log.md`.** Every other design depends on an agent *remembering* to log a Brian correction — the frame's own honest soft spot. Transcript mining removes that dependency for the highest-value signal (Brian's verbatim corrections and every `/overwhelmed` firing) and gets it for free from data that already exists. Graft it as a `mine.py` that *proposes observation blocks for review* — never as the system's foundation, and pinned/fail-loud against the undocumented schema. It makes the winner's weakest requirement (learn-Brian-without-an-agent-noticing) its strongest, at the cost of one optional, clearly-fenced script.
