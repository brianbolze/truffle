# Proposal Review: Cohort Discovery Worklist

Mode: proposal (plan-before-code). Original boundary at review time: packet contained only `proposal.md`, status was `proposed`, and no implementation receipt existed.
Reviewer: independent; I did not author the proposal.
Date: 2026-06-25
Historical note: this reviewed the pre-implementation proposal. The later validation run and page-extraction probe are summarized in [`decision-surface.md`](decision-surface.md), under the coverage frame [`_design/2026-06-26-coverage-strategy-frame.md`](../../../../_design/2026-06-26-coverage-strategy-frame.md).

Findings first. Then a recommended lean, marked as a recommendation; the lead decides.

## Findings

### 1. The proposal now gates the right value claim, not just artifact shape

This is the main fix the rejected `/discover-neighbors` packet needed. The prior packet passed on shape: spend cap, no store writes, pointer discipline, `querycheck`. It failed because nobody checked whether the feeder surfaced the right companies. This proposal moves the gate to the value claim itself:

- predeclare a known-head set before discovery;
- measure recall, precision, novelty, and union performance;
- require category-definer recall;
- compare union output against single feeders and the rejected Exa-led baseline;
- park rather than graduate a verb if the gate fails.

That is the right axis. It also uses the 2026-06-20 bake-off correctly at the proposal level: the lesson was not "make Exa better"; it was "single-source discovery is structurally brittle, and websearch + listicle carried most of the verified pool." The proposal's cohort-worklist framing matches that evidence and avoids the neighbor-search trap.

### 2. The value gate is not executable until the validation cohorts and known-head lists are frozen

The proposal says the open call is to pick validation cohorts before implementation. That is not a minor implementation detail. The known-head set is the denominator for the load-bearing recall check, so it has to be fixed before any feeder output is seen.

Without that, the worker can still "pass" a value gate by moving the goalposts: choosing an easier cohort, retrofitting the head list from discovered output, or treating a fuzzy cohort as known after the fact. The proposal names good candidates (`docs/PM SaaS` plus a non-telehealth fuzzy cohort), but it does not yet name the actual head lists, category-definers, or the pass metric for the fuzzy cohort.

What needs to be fixed before implementation:

- the validation cohorts, with one explicitly known cohort;
- the predeclared head list for the known cohort, including must-hit category-definers;
- the source/owner of that head list, ideally Brian's existing 32-player docs/PM set if that is the intended disconfirming check;
- what the fuzzy cohort is testing if it lacks a known-head denominator, probably boundary discipline, exclusions, and Tier A/B precision rather than recall.

This can live in a short packet-local `validation-plan` section or in the lead decision, but it must exist before discovery starts.

### 3. Verification is load-bearing, but its spend and evidence boundary is under-specified

`spend_stop` caps feeder collection: category/web queries, listicle pages, demand-side seed queries, and Exa novelty queries. The acceptance check then depends on verification: each candidate must be real, in-cohort, not merely a payer/retailer/directory/content site/adjacency, and Tier A/B precision must be at least 80%.

That verification pass can quietly become the expensive part. Candidate-level checks could require many live searches or page reads, and the proposal does not say what counts against the spend cap. The opposite failure is also possible: the worker could call something "verified" from weak feeder evidence, making the precision gate unauditable.

The implementation gate should require a bounded verification rule, for example: use gathered feeder evidence first, allow at most one official/company page or one corroborating source per candidate when needed, record URL/date/source family, and stop if candidate verification wants broader web research. The exact cap is lead judgment, but the receipt needs enough evidence for a reviewer to audit "verified" without rerunning the whole discovery pass.

### 4. "Union beats best single feeder or explains why not" is too soft as a pass condition

The proposal is right to ask whether the union beats the best single feeder. That is the simplest-option test: if a cheap websearch or listicle pass does the job, do not graduate a heavier union workflow.

But the phrase "or explains why not" weakens the gate. An explanation is useful learning, but it should not let the union pass the value test. If the union does not materially improve over the best single feeder on the validation set, the lead should park this packet or downscope to the simpler feeder/recipe. The only exception I would treat as non-blocking is an arithmetic one: a union can tie the best feeder because every verified hit came from that feeder. That is not evidence for a union verb; it is evidence to keep the simpler method.

### 5. Scope and risk are otherwise well fenced

`risk: medium` is honest. This is not writing store data or changing schema, but it does shape live source behavior and future agent authority. The write scope is appropriately first-slice: packet-local validation artifacts and, if useful, a trimmed packet-local workflow. The proposal explicitly excludes `store/`, `tools/`, `skills/`, `QUERYING.md`, schema paths, Signals persistence, `/research-company`, scheduled runs, and any reusable `/cohort-discovery` skill before the value gate passes.

The `escalate_if` list catches the right high-risk drift: store mutation, auto-capture, category/cohort persistence, ontology/schema, entity-resolution machinery, new tools, monitors, and treating the source panel as a market census/ranking. The one phrase to hold tightly during implementation is "if useful, a trimmed evaluation workflow"; that must stay packet-local and evaluative, not become a reusable runner by accident.

### 6. The archived menopause bake-off is prior evidence, not independent validation

The proposal correctly compares against the archived 2026-06-20 menopause bake-off, but that run should not count as proof that the new workflow generalizes. It was the source of the recipe. It also used union-as-pool evaluation, not a predeclared known-head denominator.

Use it as a regression/comparison artifact and as prior art. Do not let it substitute for the new known-cohort validation run. The actual gate should stand or fall on the predeclared known cohort plus the second cohort's boundary/precision behavior.

### What this review could not see

I did not run live discovery or verify any candidate pool. This is a proposal-mode review only. I also could not evaluate the known-head denominator because the proposal intentionally leaves validation cohort selection open. That is the main reason this should not move straight to implementation as written.

## Recommended lean

Recommendation: `revise-once`.

The proposal is pointed at the right problem and fixes the previous review failure in kind: it tests value before graduation. The revision should be small and specific, not a rewrite:

- freeze the validation cohorts and known-head list before discovery;
- define the fuzzy cohort's pass metric if it lacks a known-head denominator;
- bound and evidence the verification step;
- make "union does not beat the best single feeder" a park/downscope outcome, not a pass-with-explanation outcome.

After that, this is narrow enough for implementation as a validation packet. No decision was made; the reviewed artifact was not edited.
