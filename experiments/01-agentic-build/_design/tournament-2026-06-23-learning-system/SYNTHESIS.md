# Agentic Build — Learning System: Decision Surface

> **Historical — design-exploration artifact, not the spec.** The shipped system evolved past this: it ships one-file-per-observation + `lessons.md` (not a flat `observations.log.md` / `work.md`), and the append-only lint is deferred. Canonical spec: the [proposal](../2026-06-23-learning-system-proposal.md) and the live `learning/` folder. Kept for the rationale, not the shape.

*Synthesis of the 7-design tournament, reconciling 3 independent judges (failure-mode skeptic, elegance/generalization, Brian-fit/pragmatism). 2026-06-23.*

---

## 30-second skim

**Build Design 2 (Two-Ledger MVP) now, with three grafts.** It's the smallest thing that fully defeats all four failure modes: one append-only observation log that *physically cannot hold a fix*, one human-gated work file that points back at it, one 15-line lint that makes the rule mechanical instead of hoped-for. Two of three judges ranked it #1; the third ranked it #1 on its own lens and only put it #3 overall on pure elegance.

**The split that matters:** the elegance judge crowned **Design 1 (Dreaming port)** for the cleanest mental model. The two pragmatic judges said Design 1's manual `/dream` cadence is a real reliability gap and its apparatus is more than 3 packets need. I side with the pragmatists — but **steal Design 1's vocabulary and Design 5's Anti-Merge Law as the framing**, because Design 2's one genuine weakness (a flat log that gets hard to navigate at scale) is exactly where Designs 5/6 graduate it.

**Three grafts onto the winner:** (1) a dedicated `brian/` lane from Design 5, (2) an optional, fenced `mine.py` transcript feeder from Design 7 for the `/overwhelmed`-and-corrections signal, (3) the Anti-Merge Law from Design 5 as the stated invariant. All three are cheap and all three patch a named hole in the MVP.

Per-design depth: [contestant files](.) · judges: [1](judge-1-failure-mode-skeptic.md) · [2](judge-2-elegance-generalization.md) · [3](judge-3-brian-fit-pragmatism.md).

---

## 1. Consensus ranking

| Rank | Design | J1 (skeptic) | J2 (elegance) | J3 (Brian-fit) | Consensus read |
|---|---|---|---|---|---|
| **1** | **2 — Two-Ledger MVP** | 1 | 3 | 1 | Winner. Two firsts; only the elegance lens demoted it (as "a subset of D1"). |
| **2** | **5 — Two-Clock** | 4 | 2 | 2 | The graduation target. Same asymmetry, best-articulated, heavier today. |
| **3** | **1 — Dreaming port** | 5 | 1 | 3 | Most elegant model; docked by both pragmatic lenses for manual cadence. |
| 4 | 6 — Queryable log | 2 | 5 | 4 | Best ethos-fit on paper; author concedes v0 collapses toward D2. |
| 5 | 3 — Conventions as Product | 3 | 4 | 5 | Sharpest single reframe; overbuilt registry, shaky attribution. |
| 6 | 4 — Roles & Incentive | 6 | 7 | 6 | Right diagnosis; 4 agents at n=3 is the warned-against ceremony. |
| 7 | 7 — Transcript Mining | 7 | 6 | 7 | Best idea, worst foundation. Universally "graft it, don't ship it." |

**Where the judges agreed (strong signal):**
- All seven designs converged on the *same skeleton* — append-only raw observations ⟂ a separate gated rule/work object, linked by id, consolidated by a manual out-of-band pass. That convergence is itself the verdict: it's the correct answer to the frame. The contest was never the idea; it was **who makes the wall load-bearing, who survives scale, who closes the loop to Consult, who learns Brian.**
- Design 7 is last as a *foundation* and first as a *feeder* on all three lenses. Unanimous.
- Design 4 (four agents) is over-engineered for a 3-packet corpus on all three lenses.

**Where they disagreed (the real signal):**

1. **Design 2 vs Design 1 — engineering vs. elegance.** The elegance judge ranked D1 first and called D2 "conceptually a strict subset of D1, minus the named dreaming pass." The two pragmatic judges inverted this: D2's lint makes its one rule *enforced* (not just stated), and D1's `/dream` only compounds when Brian remembers to run it. **Why it matters:** this is the classic "best concept" vs. "best artifact" fork. For a thin corpus you'll actually maintain, enforced-and-small beats elegant-and-manual. The disagreement resolves toward D2 *because* the elegance win (the dreaming model) can be grafted as vocabulary without inheriting the cadence risk.

2. **Design 6's rank swing (2 / 5 / 4).** The skeptic loved it (cross-run detection as a mechanical `--min-count 2` query — directly kills MRL's "couldn't see across runs"). The elegance and Brian-fit judges docked it: the load-bearing closed-set schema is filled by the same agents we don't fully trust (re-importing taxonomy-sprawl risk), and its own author concedes the honest v0 ≈ Design 2 with more schema. **Why it matters:** D6 and D2 are the same design at different schema-weights. The disagreement is really "how much structure does n=3 justify?" — and two of three say "less, for now."

3. **Design 5's rank swing (4 / 2 / 2).** The skeptic put it 4th (immutability is convention, not lint — unlike D2; "shape"-clustering reintroduces steward judgment). The other two put it 2nd (its Anti-Merge Law is the cleanest invariant anyone wrote; auditable consolidation minutes are unique). **Why it matters:** this isn't really disagreement about quality — it's about *timing*. All three agree D5 is excellent; two see it as where D2 graduates, one sees the un-enforced immutability as a present risk. Consensus: D5 is the roadmap, not the day-one build.

---

## 2. The two finalists

**Design 2 — Two-Ledger MVP.** Three files, one folder, one lint. `observations.log.md` is append-only and has *no field for a fix* — the failure mode is defeated by the file's shape, not by discipline. `work.md` is the human-gated backlog that links observations by id and never copies their evidence. A 15-line pre-commit check rejects any edit to an existing log line. The MRL-008 contrast is the field's most concrete proof-of-cure: the same finding that accreted 14 paragraphs and never graduated in the real lab closes in 4 moves here. Names its two seams (findability at scale, harvest-discipline) and correctly *defers* them.

**Design 5 — Two-Clock Ledger.** The same core asymmetry (`notices/` ⟂ `rules/`), articulated more rigorously. Its **Anti-Merge Law** — "compress by adding a rule that points at notices, never by shrinking notices" — is the single most quotable, hardest-to-misuse invariant in the tournament. It has the best dedicated Brian lane and the only *auditable* consolidation mechanism (minutes that cite what was read and deliberately left unconsolidated). Costs: five folders vs. three files, immutability is convention rather than lint, and "shape"-clustering leans on a judgment call.

### Recommendation: **Build Design 2.** Frame it with Design 5's language.

Design 2 is the only entry that internalizes your own operating principle — *simplest thing that works, cut the rest, name what each piece replaces* — **in its own structure**. It defeats all four failure modes at the lowest byte-count, fits file-first/git/propose-don't-write with no new concept, works at n=3 *today*, and the one rule the whole safety argument rests on is mechanically enforced for ~15 lines of shell. Design 5 is strictly heavier for the identical asymmetry, and its extra rigor (Anti-Merge Law, audit minutes) can be *adopted as language and a one-line rule* inside Design 2 without building five folders. You graduate toward Design 5's shape when the flat log actually hurts — not before.

---

## 3. Recommended concrete shape

The winner's skeleton, plus three named grafts. Everything in-repo, git-tracked, plain markdown.

```text
experiments/01-agentic-build/learning/
  RULES.md                     # ~45-line contract: the two ledgers, the Anti-Merge Law, the graduation bar
  observations.log.md          # APPEND-ONLY. Raw observations. Never edited/reordered/deleted. (Design 2)
  work.md                      # Human-gated backlog: clusters of observations + their state. (Design 2)
  brian.md                     # GRAFT A — dedicated Brian-preference lane. (Design 5)
  scripts/
    check_obs_append_only.sh   # ~15-line pre-commit lint: rejects edits to existing log lines. (Design 2)
    mine.py                    # GRAFT B — optional, fenced transcript feeder; PROPOSES obs blocks only. (Design 7)
    coverage.md                # which transcript ranges mine.py has read (avoid re-mining)
```

Five files and two small scripts. `mine.py` is optional and degrades gracefully — if it never runs, the system is unchanged.

**Graft A — `brian.md` (from Design 5's `brian/` lane).** Design 2 handles Brian as just-another work item (`W-005`). Every judge flagged "learn Brian" as the frame's soft spot, and a dedicated lane is the strongest structure for it without new machinery. It's one file, same format as `work.md`, fed by `kind: brian-correction` observations.

**Graft B — `mine.py` (from Design 7).** The frame names `/overwhelmed` as a learnable signal, and Design 7 *proved* it's sitting in readable transcripts now (460 confirmed JSONL files with your corrections verbatim). Every other design depends on an agent *remembering* to log a correction. `mine.py` removes that dependency for the highest-value signal — but it only **proposes** observation blocks for review, never writes rules, and is pinned + fail-loud against the undocumented schema. It feeds the log; it is not the foundation.

**Graft C — the Anti-Merge Law (from Design 5), as one stated rule in `RULES.md`.** Not a structure, a sentence. It makes the over-compression defense explicit and quotable instead of implicit.

### Key template 1 — `observations.log.md` (the append-only stream)

```markdown
# Agentic Build — Observation Log

APPEND-ONLY. Add at the bottom. Never edit, reorder, or delete a line above this one.
One observation = one block. NO fixes here — a fix is a work item (work.md), not an observation.
If you are writing what to DO, you are in the wrong file.

ANTI-MERGE LAW: consolidation compresses by ADDING a work item that POINTS at observations,
never by shrinking or merging the observations themselves. Singletons are welcome. Divergence is the asset.

---

## OBS-014
- when: 2026-06-20 · run 005 (trustpilot signals read)
- who: read-agent
- saw: Sorted brands by Trustpilot trust_score; concluded remedymeds (4.6) trustworthy, hims (3.0) the
       problem. The review BODIES show both have the same billing-after-cancel cluster. The score gap is
       invitation posture, not quality.
- felt: the easiest field to grep was the one that misled me. I trusted the headline because it was the only number.
- kind: friction
<!-- never edited below this line -->

## OBS-024
- when: 2026-06-21 · packet 03 close (visual-evidence skill)
- who: build-lead
- saw: Brian cut my proposal from 3 new fields to 1 and said "what do the other two replace? if nothing,
       they're not earning it." I'd added them because they were cheap, not because a question needed them.
- felt: I default to additive. The correction was "subtract first." Second time this session.
- kind: brian-correction
```

Five fields, all backward-looking (`when / who / saw / felt / kind`). The instant you add a forward-looking `proposed_next_step`, you have rebuilt MRL-002, where the fix lived on the evidence and the two grew together until neither could close. `kind ∈ {friction, wish, risk-miss, surprise, brian-correction, heuristic-worth-keeping}`.

### Key template 2 — `work.md` (the gated, editable backlog)

```markdown
# Agentic Build — Work

A work item = a cluster of observations worth acting on, plus a decision. Created only by a harvest pass
or a Brian call — never auto-minted at observation time. Links observations by id; NEVER copies their evidence.

States: proposed → accepted → graduated | parked | dropped.
Graduated = the lesson now lives in the skill/convention itself (link the diff).

---

## W-002 — Headline signal fields mislead a naive read
- state: accepted (2026-06-22, Brian)
- observations: OBS-014, OBS-019, OBS-023
- pattern: across Trustpilot score / Wayback tenure_days / SEC total_hits, the easiest-to-grep field is the
  most misleading; each needs an integrity sibling to be read safely.
- decision: graduate as a reading-discipline line in the signals query recipe. NOT a schema field, NOT a score.
- graduation: → QUERYING.md signals-read recipe. Diff: <commit-sha>.

## W-005 — Build-lead defaults to additive, not subtractive
- state: proposed (2026-06-22, harvest) — routed to brian.md once it clears a 2nd sighting
- observations: OBS-024
- pattern: agents add fields/rules because they're cheap, not because a question needs them.
- decision: PENDING. Hold for a 2nd sighting per the graduation bar.
```

### The lifecycle (unchanged from Design 2)

| Step | Trigger | Writes | Gated? |
|---|---|---|---|
| **Append** | packet close, or mid-run friction | one OBS block to the log | no — append is safe, it's just evidence |
| **Mine** (optional) | weekly / after a rough session | `mine.py` *proposes* OBS blocks from transcripts for review | no — proposal only |
| **Harvest** | ~5 packets, a painful failure, or Brian asks | proposed work items in `work.md` + brian.md candidates | no — proposing is safe |
| **Accept/Park/Drop** | Brian reviews `work.md` | work-item state | **human gate** |
| **Graduate** | accepted item with a clear fix | a normal change-packet writes the rule into the skill/recipe | **human gate** |
| **Consult** | next run of the affected verb | nothing — it reads the now-sharper skill | n/a |

---

## 4. How it beats the four failure modes + supports the 5 stages

**Four failure modes (all defeated structurally, not by discipline):**

1. **Collapse observation → solution.** The log file *physically cannot hold a fix* — 5 backward-only fields, a "wrong file" guard, and the lint. Fixes only exist in gated `work.md`. This is the load-bearing defense.
2. **Anchor-and-mirror.** There is no per-case template to mirror. The log format is fixed and can't encode a solution; graduated rules live in the skill, so the thing agents anchor on is the *curated convention* — exactly where you want anchoring. A bad observation can't become a de-facto standard because an observation isn't a standard.
3. **Conflate feedback with item-of-work.** This *is* the architecture: append-only evidence ⟂ editable work, two files, linked by id, never copied. MRL-002's 15-paragraph accretion is impossible by construction.
4. **Over-compression.** The Anti-Merge Law: no operation in the system destroys a raw observation. The clean view (`work.md`) is explicitly downstream of the divergent stream. MRL's 345→2 collapse can't happen because nothing rewrites the 345.

**Five-stage progression:**
1. **Fail** → an OBS block, rich (`saw` + `felt`), dated, attributed, isolated (no fix attached).
2. **Investigate** → harvest clusters OBS into a work item's `pattern:`; the *why* lives in editable work, the *what-happened* stays immutable in the log.
3. **Verify** → Brian flips `proposed → accepted` against counted, linked OBS ids — a human decision on evidence, not an agent's compression.
4. **Distill** → a gated change-packet writes the *general* rule into the skill/recipe; `work.md` links the diff.
5. **Consult** → the next run reads the sharpened convention, not the learning folder. Compounding by construction.

---

## 5. Open questions for Brian

These are genuine forks the tournament did not settle — your call:

1. **The transcript-corpus dependency (Graft B).** `mine.py` reads `~/.claude/projects/…/*.jsonl` — an undocumented Claude Code internal. All three judges said "graft the idea, fence the foundation." **The fork:** ship `mine.py` now as an optional, fail-loud feeder (high value, low blast radius if it breaks), or defer it entirely until the manual log proves insufficient? My lean: ship it fenced — the durable layer (markdown observations) survives even if transcripts vanish, so the downside is bounded.

2. **`.claude/agents` roles (Design 4).** Do you want the capture/propose firewall enforced by *separate subagents* (Observer can't propose because it's a different agent with scoped tools), or by *file shape* (the log can't hold a fix)? Design 2 chose file-shape; it's lighter but the firewall is "prompt-deep." Worth the four-agent ceremony only if you find agents are smuggling fixes into observations in practice.

3. **Medium / schema weight (Design 6 vs Design 2).** Flat markdown log + grep (D2) vs. one-file-per-observation with closed-set frontmatter + a query script (D6). Same design, different scale. The judges' consensus: start flat, add the schema only when the log crosses ~30 entries and editing it becomes an accretion risk. **Confirm you want the lighter start.**

4. **Lint vs. convention for immutability.** Design 2's pre-commit check is the cheapest enforcement; Design 5 leaves it to review. The lint is ~15 lines and runs in your existing gate. Recommend the lint — but it's a (small) bit of standing machinery, so flagging it.

5. **When does the harvest pass actually fire?** Every design's honest weakness is the same: nothing runs on a clock (correctly — no daemon), so the loop stalls if no one invokes harvest. The mitigation is a packet-close nudge ("≥5 observations since last harvest?"). Is a convention-nudge enough, or do you want a scheduled routine (which crosses the no-living-infrastructure line)?

---

## 6. Strongest dissent

**The best argument against building Design 2: you are picking the engineering over the idea, and the idea is what generalizes.**

The elegance judge's case is real. Design 1's in-band/out-of-band split — *"runs leave footprints, dreaming draws the map, Brian signs the map"* — is a **primitive a newcomer holds in their head on first read**, and it lifts to any future user-facing verb (`skills/<verb>/.memory/`) with zero reshaping. Design 2, by contrast, is a well-built instance of the shared skeleton with a clever lint; it doesn't *teach* you anything the way the Dreaming model does. When this graduates from a 3-packet experiment to the whole engine's learning layer, the design you want to scale is the one with the cleanest mental model — and a manual-cadence problem is fixable (a nudge, a routine), whereas a less-memorable architecture is a tax you pay forever. **Choosing D2 optimizes the thing that's easy to measure now (byte-count, enforceability at n=3) over the thing that compounds (conceptual leverage at n=300).**

**Why I still recommend Design 2:** the dissent's own escape hatch is the graft. Design 1's *vocabulary and mental model cost nothing to adopt* — you can frame Design 2's harvest pass as "dreaming" and its log as "footprints" in `RULES.md` and get the conceptual leverage without the cadence risk or the four-folder apparatus. The elegance is portable; the manual-`/dream` reliability gap is not easily portable away. So: build the enforced, right-sized artifact, narrate it in the elegant design's language, and graduate toward Design 5's rigor when the corpus earns it. You lose nothing the dissent actually values.

---

*Per-contestant designs and full judge rankings: [tournament folder](.).*
