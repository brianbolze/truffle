# Frame Review: Honest Query-Time Company Groupings

**Date**: 2026-06-24
**Mode**: frame
**Reviewer**: independent (did not author)
**Reviewed**: `frame.md` (this packet), on its own terms — proposal/implementation in this
packet were deliberately not read, so the frame is judged before any solution, not against
what it became.

## Findings (most important first)

**1. Solution-space discipline is the strongest part — it holds the line.**
The headline frame test is "has it jumped to solutions?" This one explicitly refuses to:
define "market," mint a durable grouping/cohort entity, force fuzzy questions into schema,
or have Truffle judge strategic relevance (Non-Goals). That maps cleanly onto Truffle's
"no new entity / ontology by default" posture and the engine's State-vs-Judgments line. The
frame stays in problem-space. Good — this is the failure mode the mode exists to catch, and
it didn't happen.

**2. The success condition is a reader's mental state, not an observable test.**
"Legible enough that the reader does not confuse X with Y" describes a state of mind, with
no way to tell from an answer whether it was met. The four confusions it lists (store vs
market coverage, category vs buyer-defined market, source list vs census, temporary set vs
durable fact) are sharp and the best content in the frame — but as written a proposal can
claim success without a falsifiable check. Frame-stage gap, not a blocker: name what an
honest answer must *show* (e.g. the set's basis + what it omits + the claim ceiling), so the
later acceptance check has something to bind to. Right now success is asserted, not testable.

**3. Root cause is implied but never named.**
The frame lists two failure modes (mechanical, interpretive) vividly, but stops at symptoms.
The underlying cause — a grouping carries no record of *how it was assembled or what it
excludes*, so its provenance silently upgrades from "set someone built" to "the market" —
is left for the reader to infer. The `/frame` rubric asks for the problem to be root-caused;
this is one inference short. Naming it would also tighten finding 2, since the honest-answer
contract falls straight out of it.

**4. The value connection the rubric asks for is absent.**
Reviewer-context's frame rubric is "the `/frame` skill + the value / pillar / persona links."
The frame never names which pillar it moves or whose shoes feel the pain. It reads as
**Synthesis** (read-time honesty on interpreted cross-company outputs) with a **Steward /
Beekeeper-Brian** "false completeness is a footgun" motivation — both live, named concerns
in the local docs. Stating that would anchor "why now" in strategy rather than in MRL
incident reports alone. Absence noted, not fatal — but it's a rubric line left unanswered.

**5. "Why This Matters" leans on an asserted trend.**
"Truffle is increasingly used to generate market reads" carries the urgency but is stated
flat. The Evidence Base (MRL discovery-ledger, triage MRL-001/002, QUERYING Recipe 8) plausibly
backs it — I did not open those files, so I can confirm they are *cited*, not that they
support the "increasingly" claim. If the trend is the load-bearing reason to act now, the
frame should say how many real reads hit this, not assert a direction.

**6. Open questions are missing.**
The `/frame` template wants open questions; this frame has none. At least three are live and
would sharpen scope before a proposal: (a) is the honest-answer contract a query-time
*output discipline*, a `QUERYING.md` recipe, or guidance — and does that risk the "no
standing infrastructure" line? (b) who/what enforces it — the answering agent, a check, or
nothing? (c) does this stay read-only, or does any grouping ever earn persistence (which the
Non-Goals currently forbid by default — is "by default" leaving a door open on purpose)?
Listing these is frame-stage work; their absence makes the frame look more settled than it is.

## Scope / size

Within frame size defaults (~530 words, target 500-750). Skim-first structure is good and
matches the house style. No padding to cut.

## What this review could not see

I scoped to `frame.md` only (correct for frame mode), so I cannot speak to whether the
proposal already closed findings 2/3/6 — by design. I did not open the three Evidence Base
files, so finding 5's "cited but unverified" caveat stands: I confirmed the citations exist
as references, not that they support the specific claims.

## Recommended lean (recommendation — the lead decides)

**Revise, lightly, then proceed.** The frame is sound where it matters most: it stays in
problem-space and refuses the over-build. Before a proposal, it would benefit from (a) an
observable success contract — what an honest answer must show — (b) the root cause named in
one line, and (c) the pillar/persona anchor. None are blockers; all are cheap and would give
the proposal firmer ground. If the lead would rather let the proposal carry 2/3/6, that's a
defensible call — but the value anchor (finding 4) is worth adding to the frame itself.

No decision was made; the reviewed artifact was not edited.
