# Proposal Review: Generic Candidate Qualification

Mode: proposal review of now-parked prior art. At review time, the mini proposal had an active
companion-slice status, and I found no candidate-qualification implementation in the packet.
Reviewer: independent; I did not author the mini proposal.
Date: 2026-06-26
Strategic frame: [`_design/2026-06-26-coverage-strategy-frame.md`](../../../../../_design/2026-06-26-coverage-strategy-frame.md)
Fresh-session brief: [`candidate-qualification-fresh-session-brief.md`](candidate-qualification-fresh-session-brief.md)

Use this review for durable cautions, not as approval of the parked proposal. The most reusable
warnings are: do not leak evaluation labels into qualification; separate evidence-unit role from
candidate route; preserve page-extraction recall while improving queue precision; adjudicate
source/publisher negatives explicitly.

Findings first. Then a recommended lean, marked as a recommendation; the lead decides.

## Findings

### 1. The implementation sketch leaks evaluation labels into the qualifier

The proposal says the qualifier should assign labels using candidate evidence plus `qrel
labels`. That collapses the test boundary. The search harness explicitly treats grades as
evaluation labels, not ranking features, and the mini proposal's pass condition depends on
not promoting grade-0/1 rows while preserving valid positives such as Midi Health.

If qrels or Brian's prior corrections are available to the automatic qualifier, the probe can
pass by reading the answer key: promote known positives, demote known negatives, and then
report clean Tier A/B output. That would not prove the design works on new cohorts.

Revise the proposal so qrels are evaluation-only. The qualifier can use candidate name/domain,
matched aliases, source rows, page title, outbound-link context, and page text evidence. It
should write its proposed route first; only then should the receipt join qrel labels to score
what happened. If human corrections are part of the workflow, keep that as an explicit
post-qualification review lane, not an input to the automatic qualifier.

### 2. `source_page` conflates an evidence role with a capture-target decision

The core idea is right: source pages should remain useful evidence without competing as
capture targets. The proposed `Result role` axis, though, appears to label each candidate
as `subject_candidate`, `source_page`, or `publisher_or_directory`, then routes
`source_page` and `publisher_or_directory` away from capture.

That is risky because some domains are both evidence sources and profileable companies.
The current outputs already show this shape: a vendor can publish a comparison article, a
parent can host a competitor page, and a product company can appear through its own blog or
outbound links. In conversation intelligence, examples include domains like Read AI,
Salesforce, and Granola. In telehealth, a clinic or health brand can also publish ranked
provider pages.

Revise the model to separate two facts:

- evidence-unit role: this specific row/page/link is a source, directory, comparison page,
  official page, or mention;
- candidate route: this normalized company/brand/domain is or is not a profileable in-cohort
  capture target.

`source_page` should not be a candidate-level veto by itself. It should explain evidence
provenance or confidence unless the candidate is only a publisher/directory and not a
profileable cohort member.

### 3. The pass gate can show cleanliness while losing retrieval value

The acceptance check asks for top-20 before/after, label counts, remaining misses, and no
grade-0/1 or obvious source/publisher page in Tier A/B. That is close, but it does not
require the qualification stage to preserve the page-extraction gain.

The prior receipt's gate was stronger: page extraction had to improve relevant recall and
top-K precision over the raw-unit baseline. Qualification should inherit that shape: improve
capture-queue precision by removing source/publisher pages without materially reducing
relevant recall or losing grade-3/4 positives from the page-augmented top 20.

As written, a too-aggressive filter could remove source pages and several valid candidates,
then still look clean if the remaining Tier A/B queue has no judged low-grade rows. The
receipt should report before/after P@10, R@10, nDCG@10, Tier A/B precision, retrieved
grade-3/4 count, and named regressions. "No grade-0/1" is not enough because many source and
publisher rows are currently qrel-null, not grade 0/1.

### 4. The source/publisher negative sample needs a small adjudicated surface

"No obvious source/publisher page" is the right human-language goal, but it is too subjective
as an acceptance gate. The existing page-extraction summary reports no low-grade/boundary
rows in the top 20 while the implementation notes still say source domains remain in the top
ranks. That means the current qrels do not fully encode the source/publisher problem this
slice is meant to fix.

The revision does not need a big new oracle. A small packet-local adjudication is enough:
take the page-augmented top unknown domains/pages for both cohorts, label whether each is a
capture target, evidence-only source, product/workflow, parent/owner, adjacent, or uncertain,
and use that fixed table to score the before/after queue. This keeps the probe cheap while
making the negative gate auditable.

### 5. The scope fences are good, but the label set should be trimmed to what routes

The proposal handles the main risk correctly: packet-local only, no new live source gathering,
no schema or taxonomy change, no store writes, no reusable skill. `risk: medium` is honest
because this could shape future discovery authority even if the first implementation spends
nothing and writes only receipts.

The label direction is also right: generic retrieval-time labels beat telehealth-specific
negative categories. The current three-axis menu may still be broader than the first probe
needs. Labels such as `specialist`, `generalist_in_cohort`, `adjacent`,
`infrastructure_or_enabler`, and `channel_or_distribution` are plausible, but unless they
drive a distinct route or metric they become a proto-taxonomy in receipt clothing.

For the first implementation, keep only labels needed to answer the value claim: profileable
capture target, evidence-only source/publisher, product/workflow, parent/owner, adjacent or
wrong type, uncertain; plus a compact cohort-fit reason. Add nuance only when a row would be
routed differently.

### What this review could not see

I did not run or score a qualification implementation because none exists yet. This is a
proposal-mode review of `candidate-qualification-mini-proposal.md` plus the packet receipts
that motivate it.

## Historical Recommended Lean

At review time, the recommendation was `revise-once`.

That is no longer the active path. The proposal is now parked prior art, and the next pass
should start from [`candidate-qualification-fresh-session-brief.md`](candidate-qualification-fresh-session-brief.md).

Reusable cautions from this review:

- remove qrel labels from qualifier inputs and keep them evaluation-only;
- split evidence-unit role from candidate capture-target route;
- make before/after metrics preserve page-extraction recall while improving queue precision;
- add a tiny adjudicated source/publisher negative surface;
- trim labels that do not change routing.

Do not treat this as approval to implement the parked proposal as written.
