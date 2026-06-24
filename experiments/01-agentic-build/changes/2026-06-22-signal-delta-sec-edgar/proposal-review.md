# Proposal Review: signal_delta SEC EDGAR branch

**Reviewer**: independent (did not author)
**Mode**: proposal
**Date**: 2026-06-24
**Reviewed**: `experiments/01-agentic-build/changes/2026-06-22-signal-delta-sec-edgar/proposal.md`

## Verdict at a glance

A tight, well-scoped proposal that holds Truffle's evidence boundaries hard. The
required fields are honest and the non-goals are doing real work. My findings are mostly
minor; the one that matters is procedural, not technical — the artifact is already marked
`implemented`, so the proposal decision is being reviewed after the fact.

## Findings (most important first)

### 1. The proposal is already `implemented` — the decision gate fired before this review

`Status: implemented`, plus a full Implementation Receipt, means the proposal→accept→build
sequence already ran. Reviewing it in `proposal` mode now is retrospective: I can judge
whether the *decision* was sound, but I can't gate it. That's fine for a test run, but
worth flagging because per lead-context this is `medium` risk, and the posture is
"medium-risk packets need independent review **by default**" before build. If independent
proposal review is meant to be a gate, an already-implemented packet means the gate was
satisfied some other way (the proposal's own "Review Notes" reference a prior proposal
review). Not a fault in the proposal's content — a note on where this review sits in the
lifecycle.

### 2. Risk classification is defensible at `medium`, and the proposal defends it well

The three risk questions from lead-context: (a) live behavior / write authority — no, the
branch is a local comparator, no store writes, `spend_stop: none` with inline fixtures
only; (b) contract future agents rely on — yes, `signal_delta.py` is a committed tool, and
the proposal names exactly this ("future agents may trust... a sloppy capital-signal delta
would create false confidence"); (c) unclear acceptance/rollback/spend — no, all three are
concrete. So the risk driver is the committed-tool contract surface, correctly identified.
`medium` is right; it does not touch persistence, schema, or paid capture, so it does not
cross into `high`. Good calibration.

### 3. Non-goals carry the scope discipline — and they do the job

The Constraints / Non-Goals list is the strongest part of the packet. It pre-empts exactly
the drift this kind of branch invites: no amount/valuation/round inference, no cross-source
reconciliation, no card schema / lint gate / SQLite / monitor / stored delta object, no
fetching inside the comparator. These map cleanly onto the engine's hard lines (no new
schema/entity/monitor; evidence not scores; no standing infrastructure). The `escalate_if`
field then re-fences the same boundary from the build side. This is additive code, but the
proposal answers "what does it replace?" implicitly and correctly — it replaces the
*fallback veto* for `sec_edgar` with a real branch, so it's not net-new surface area so
much as filling a typed hole. That's the right framing and it's defensible.

### 4. Simplest option was genuinely considered

Three options, with option 2 (docs-only) explicitly the lower-code-risk path and rejected
for a stated reason (preserves the manual comparison the comparator exists to remove), and
option 3 (broader funding layer) parked as a separate higher-risk packet. This is not a
strawman set — option 2 is a real alternative and the rejection reason is sound. Passes the
"was the simplest option really considered?" stress.

### 5. The "stricter vs looser event key" question is the real open risk, and it's under-resolved in the proposal

Review Notes flag that a strict factual-content event key can show a *re-parsed* card as
"newly visible / no longer visible" when only a citation or flag changed — i.e. churn that
looks like movement but isn't. The proposal punts this to implementation review ("default
to stricter output with clear caveats unless implementation review identifies a cleaner
stable key"). That punt is reasonable for a proposal, but it leaves the packet's
correctness hinging on a decision the proposal doesn't actually make. For a `medium`-risk
committed tool whose whole value is *not* creating false confidence, the event-key
stability is the load-bearing detail. The acceptance_checks pin the *no-amount/no-score*
boundary thoroughly but do **not** pin event-key stability (no fixture for "re-parsed card
with changed citation must not surface as movement"). That's the one substantive gap.

### 6. write_scope honestly hedges the doc blast radius — verify it didn't undercount

`write_scope` lists the tool, tests, and `tools/signal_delta.md`, "plus small references
in `QUERYING.md` / `SIGNALS.md` if implementation changes the documented branch list." The
Implementation Receipt then reports touching `QUERYING.md`, `SIGNALS.md`,
`tools/signal_delta.md`, `tools/BACKLOG.md`, root `BACKLOG.md`, **and** Market Read Lab
notes. The two BACKLOG files and the MRL notes were not named in `write_scope`. Per
lead-context `write_scope` is "expected scope, not a perfect file lock," and these are
low-risk doc/backlog edits, so this is within tolerance — but it is a (small) boundary
expansion that, per the heuristic "if implementation expands the boundary, note it," should
have been called out as such rather than just appearing in the receipt. Minor.

### What this review could not see / did not do

- I reviewed in `proposal` mode, so I did **not** verify the diff line-by-line against the
  accepted proposal, run the acceptance_checks, or confirm `write_scope` adherence in the
  code — that's `change` mode. I did a light existence check: `tools/signal_delta.py`
  exists and contains `GRAIN["sec_edgar"]`, the `sec_edgar` subject branch, and
  `_level_sec_edgar` / `_delta_sec_edgar` / `branch_sec_edgar` mirroring the Trustpilot /
  Wayback pattern — so the proposal's factual claims about the existing code and the shipped
  shape are not from memory; they check out. I did **not** read the branch bodies or tests
  closely enough to judge whether finding #5 (event-key stability) was actually resolved
  well in code. If that matters, run a `change`-mode review.
- "No issues" is not the claim. The scope discipline is genuinely strong; finding #5 is a
  real unresolved correctness risk that a proposal-stage reader should carry into the
  implementation review.

## Recommended lean

**Accept (as a sound decision)** — with one carry-forward. *This is a recommendation; the
lead decides.*

The proposal is the right-sized, boundary-respecting change, correctly classified
`medium`, with non-goals that hold the line and a real options analysis. If this were a
live gate I'd lean accept-after-confirming finding #5 is pinned. Because it's already
implemented, the actionable form is: **confirm in a `change`-mode pass that event-key
stability is handled (re-parsed cards don't masquerade as movement) and that a fixture
pins it** — the acceptance_checks as written don't, and that's the one place this branch
could quietly create the false confidence its own risk note warns against.

---

No decision was made; the reviewed artifact was not edited.
