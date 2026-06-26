# Validation Plan: Cohort Discovery Worklist

Date: 2026-06-25
Status: frozen inputs; scored validation plus search/page-extraction probes recorded in `receipts/`.
Strategic frame: [`_design/2026-06-26-coverage-strategy-frame.md`](../../../../_design/2026-06-26-coverage-strategy-frame.md)

## Purpose

Test whether a union-based cohort discovery pass finds companies worth capturing without
over-promoting weak or wrong-type candidates.

This is a coverage-governance validation slice, not a reusable discovery verb. The frame-level
question is what coverage deserves promotion into the primary store.

## Cohorts

### 1. Telehealth Masked Holdout

Use `validation-inputs/telehealth-holdouts.json`.

- Notion Organizations supplies the evaluation oracle only.
- The discovery pass must not read Notion.
- Packet-local logic masks the listed F2/F3/F4 profiled store entries from the store
  baseline; `store/` itself is not modified.
- F3/F4 holdouts are must-hit.
- F2 holdouts are should-hit.
- Brian's curated negatives are the hard pollution sample.
- F0/F1 Notion rows are not a hard pollution set because Notion is already curated.

### 2. Conversation Intelligence / AI Meeting Tools

Use `validation-inputs/conversation-intelligence-targets.json`.

- Compare the discovered/tiered output to Brian's ranked core list.
- Keep adjacent transcription-dev tools separated unless explicitly boundary-labeled.
- Treat OpenAI Whisper as an intentional ambiguity because it is dual-listed.

## Human Review Checkpoint

After discovery, dedupe, and initial verification, pause before final scoring and prepare a
short review queue for Brian containing:

- generated candidates not already in the holdout set;
- generated candidates not already in the profiled store;
- candidates the verifier marked uncertain, wrong-type, or low-formidability.

Brian marks each as `worth_capture`, `tier_c_only`, `exclude`, or `unsure`.

Hard gate: no candidate Brian marks `tier_c_only` or `exclude` may land in Tier A/B.

## Pass / Park Rules

- Pass requires telehealth F3/F4 recovery, Tier A/B precision >=80%, and no hard-pollution
  item in Tier A/B.
- If the union does not materially beat the best single feeder, park or downscope to the
  simpler feeder. Do not pass with an explanation.
- If candidate verification needs broader web research than the approved cap, stop and ask.

## Spend Boundary

Per cohort:

- max 4 category/web queries;
- max 3 listicle pages;
- max 2 demand-side seed queries;
- max 2 Exa `/search` novelty queries;
- verification uses gathered evidence first, then at most one official/company page or one
  corroborating source per candidate when needed.

No `/research-company`, no Firecrawl company captures, no store writes, no scheduled run.
