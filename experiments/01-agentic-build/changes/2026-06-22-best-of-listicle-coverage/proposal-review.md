# Proposal Review: Best-Of Listicle Coverage Radar

Reviewer: independent (agent-build-review, mode `proposal`)
Date: 2026-06-24
Reviewed: `proposal.md` in this packet, against the proposal-mode rubric (the packet's stated fields) and the reviewer disciplines.

## Findings

**1. Scope and required fields are strong; this is the proposal's core asset.** The five required fields are honest and tightly drawn. `write_scope` names a primary target (`QUERYING.md`), an explicitly optional add-on, and an exclusion list (`store/`, tools, prompts, schemas, receipts, run artifacts). `escalate_if` enumerates exactly the boundary crossings a reader would worry about — helper script, network, persistent Signal, category object, store write, capture campaign, auto-writeback. `spend_stop: none` is correct for a docs-only change and says why. On the proposal-mode emphases (scope creep, persistence/new-entity risk, hidden standing infrastructure, additive-only), the proposal pre-empts each one rather than leaving it for the reviewer to surface. This is the right shape for a medium-risk packet.

**2. "Additive — what does it replace?" is answered, but only partially.** The reviewer-context asks of additive changes: what does this replace? The proposal earns the addition well (the method recurred across runs 012/022/024; naming it stops re-invention and stops premature promotion to a primitive). But it does not claim to retire anything, and the §0 grouping stamp in `QUERYING.md` already carries an "outside list" row and a completeness rule. So the new recipe is genuinely net-new surface in a doc that already gestured at the concept. That is defensible — a stamp row is not a recipe — but the proposal should say explicitly that the recipe *operationalizes* the existing stamp row rather than duplicating it, so a future editor does not treat them as two competing homes for the same idea.

**3. Status mismatch: this is a proposal artifact that already records implementation.** The header says `Status: implemented` and the doc carries an Implementation Receipt. The packet has no separate `change`/diff artifact and no persisted prior `proposal-review.md`, yet the body twice references a "Proposal review" that "found the evidence threshold met." Two consequences worth flagging, neither fatal to the proposal's logic:
   - The prior proposal review was apparently never persisted to the packet. The decision trail rests on a summary inside the artifact it reviewed, which is weaker provenance than a standing review file.
   - Reviewing this in `proposal` mode means I am judging the plan, not auditing the patch. A real audit of whether the shipped recipe stayed in `write_scope` and passed `acceptance_checks` is `change`-mode work and was not performed here. I confirmed only that a recipe matching the described shape exists in `QUERYING.md` (numbered 9), which grounds the review but is not a change audit.

**4. Minor internal drift: insertion point named as "Recipe 8," shipped as Recipe 9.** The Implementation Sketch says to add the recipe "probably after Recipe 8"; the shipped recipe is Recipe 9 and `QUERYING.md`'s §0 stamp already cross-references "Recipe 9" for outside lists. Low-stakes (the sketch hedged with "probably"), but it shows the proposal's recipe-numbering was a guess against a moving doc. Not a reason to revise.

**5. The caveat discipline is the load-bearing risk control, and it holds.** The medium-risk rating is justified on the right grounds: the danger is not the edit but that the docs *shape future autonomous bounded-live behavior and paid-source confidence*. The proposal's mitigation — "make the caveats louder than the mechanics," recurrence over rank, store-absent ≠ market-absent, propose-don't-write, no new spend authority — is the correct lever and is stated as a binding acceptance check, not an aspiration. This is the part most likely to decay under future edits; the in-doc "next reviewer should focus on scope creep" note is a good tripwire to preserve.

**6. Simplest option was genuinely considered.** Five options are laid out with the cheaper ones (helper script, persistent Signal, capture campaign) explicitly rejected for crossing the persistence/automation boundary MRL is testing. Option 1 (docs-only) is the floor, and option 2 is correctly gated to "only if tiny." No evidence of reaching past the simplest thing that works.

## What I could not see

- No diff was audited (that is `change` mode). I verified the recipe exists and matches shape, not that the implementation honored every acceptance check.
- The prior proposal review is not in the packet; I could not confirm what it actually checked versus what the body summarizes.
- I did not re-run the deterministic gate; I took the receipt's pass/fail report at face value.

## Recommended lean

**Recommendation (the lead decides):** treat the proposal itself as **accept** — the evidence threshold (three sightings), scope discipline, and caveat controls are all met, and the recommendation to choose option 1 with option 2 gated tightly is the right call. This is a recommendation, not a decision.

One thing for the lead to resolve separately from the proposal's merits: the packet conflates `proposal` and `change` in a single file with no persisted proposal review. If the lead wants a clean decision trail, the `change` should get its own audit pass (`agent-build-review` mode `change`) before the packet is considered closed, rather than relying on the self-reported receipt.

No decision was made; the reviewed artifact was not edited.
