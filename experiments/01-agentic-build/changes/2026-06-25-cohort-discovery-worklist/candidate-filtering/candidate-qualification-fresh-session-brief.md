# Fresh Session Brief: Candidate Qualification

Date: 2026-06-26
Status: historical kickoff brief; superseded by `2026-06-26-cohort-discovery-worklist-synthesis.md`
Strategic frame: [`_design/2026-06-26-coverage-strategy-frame.md`](../../../../../_design/2026-06-26-coverage-strategy-frame.md)

## Purpose

Help a new agent think fresh about candidate qualification before proposing implementation.
Do not start from the parked mini proposal. Start from the frame-level question:

**How should Truffle stage source-discovered entities so useful market evidence is preserved, but only profile-worthy companies/brands are promoted toward full capture?**

## Read Order

0. Read the current synthesis:
   [`2026-06-26-cohort-discovery-worklist-synthesis.md`](2026-06-26-cohort-discovery-worklist-synthesis.md).
1. Read the strategic coverage frame:
   [`_design/2026-06-26-coverage-strategy-frame.md`](../../../../../_design/2026-06-26-coverage-strategy-frame.md).
2. Read this packet's current decision surface:
   [`decision-surface.md`](../decision-surface.md).
3. Read the page extraction result:
   [`receipts/page-extraction-probe.md`](../receipts/page-extraction-probe.md).
4. Read the search baseline only if needed:
   [`receipts/search-harness.md`](../receipts/search-harness.md).
5. Ask Brian frame questions before solutioning.
6. Only after an independent frame and options pass, read the parked prior art:
   [`candidate-qualification-mini-proposal.md`](candidate-qualification-mini-proposal.md) and
   [`candidate-qualification-mini-proposal-review.md`](candidate-qualification-mini-proposal-review.md).

## Frame Questions To Ask Brian

- What should the next artifact decide: capture queue readiness, evidence preservation, or both?
- Should candidate qualification be optimized for Brian review, agent autonomy, or later reusable engine behavior?
- What is the minimum acceptable human-review surface before a candidate can enter Tier A/B?
- Which mistakes are worse for this layer: missing real capture targets, promoting source/publisher noise, or overfitting to telehealth?
- Should product/workflow targets be routed separately now, or explicitly out of scope for company coverage growth?

## Brainstorming Direction

Generate multiple approaches before recommending one. At minimum, compare:

- a checklist/manual review lane;
- a deterministic rules-and-receipts qualifier;
- a lightweight model-assisted adjudication pass;
- a two-stage approach that separates evidence preservation from capture-target routing;
- a no-new-layer option that keeps qualification inside human review until more cohorts prove the need.

For each approach, name what it replaces, what it risks, how it would be evaluated, and what would make it too heavy.

## Guardrails

- Do not create a reusable `/cohort-discovery` or candidate-qualification skill in this pass.
- Do not edit `store/`, schemas, `TAXONOMIES.md`, `tools/`, `skills/`, Signals paths, or `QUERYING.md`.
- Do not add new live source spend unless Brian explicitly approves it.
- Do not treat source/listicle/directory pages as company profiles.
- Do not use qrels or Brian-reviewed labels as qualifier inputs; use them only for evaluation after routing.
- Preserve the coverage-frame split: source evidence can be useful without becoming a company profile, and promotion remains a judgment-bearing staging decision.

## Success Shape

The output should be a recommendation, not code by default:

- a concise frame of the candidate-qualification problem;
- 2-4 viable approaches with tradeoffs;
- one recommended next slice;
- acceptance checks that measure both recall preservation and queue precision;
- a clear note on what stays packet-local versus what might later graduate.
