# Codex Candidate Qualification V2

Date: 2026-06-26
Status: packet-local Doro-shaped prototype; no engine changes

## Read

- V2 keeps routing qrel-free, adds `kind` before `route`, and uses `boundary_review` for ambiguity.
- Code builds cards and matcher hints; the classify-by-example proxy returns an inspectable result shape for later agent adjudication.
- Qrels and Brian-reviewed labels are joined only after routing for evaluation.

## Outputs

- Kind examples: `codex_v2_kind_examples.json`
- Candidate cards: `codex_v2_candidate_cards.json`
- Evaluation JSON: `codex_v2_qualification_eval.json`
- Summary: `codex_v2_qualification_summary.md`

## Cohort Summary

| Cohort | Candidates | Capture | Boundary | Preserve | Reject | Source-like capture |
| --- | --- | --- | --- | --- | --- | --- |
| telehealth | 239 | 5 | 191 | 19 | 24 | 0 |
| conversation_intelligence | 135 | 0 | 106 | 16 | 13 | 0 |

## Evaluation Notes

### telehealth

- Known relevant seen: 14 cards / 11 unique qrels.
- Known relevant routed to capture: 2.
- Known relevant routed to boundary review: 11.
- Known bad/boundary rows promoted to capture: 0.

Top capture candidates:

| Rank | Name | Domain | Kind | Eval label |
| --- | --- | --- | --- | --- |
| 1 | Healthspan | gethealthspan.com | company_or_brand | unjudged |
| 4 | Want a Longer Lifespan? You Should Care About Your ... | honehealth.com | company_or_brand | must_hit |
| 7 | MyHealthspan | myhealthspan.com | company_or_brand | unjudged |
| 22 | Defymedical | defymedical.com | company_or_brand | should_hit |
| 23 | gennev.com | gennev.com | company_or_brand | unjudged |

Top boundary review:

| Rank | Name | Domain | Kind | Eval label | Caveat |
| --- | --- | --- | --- | --- | --- |
| 9 | TRT Nation |  | company_or_brand | unjudged | name-only candidate needs domain/entity resolution before capture |
| 10 | Online TRT vs Traditional Testosterone Clinics | vikingalternative.com | company_or_brand | unjudged | plausible company domain, but observed page title has source/listicle shape |
| 13 | Online TRT |  | company_or_brand | unjudged | name-only candidate needs domain/entity resolution before capture |
| 15 | Function | 100 Healthy Years | functionhealth.com | uncertain | unjudged | low evidence; classify before rejecting |
| 16 | Online HRT & Menopause Specialists in Washington | bywinona.com | uncertain | unjudged | low evidence; classify before rejecting |
| 17 | TRT Online: A Smarter Way to Treat Low Testosterone | struthealth.com | uncertain | unjudged | low evidence; classify before rejecting |
| 18 | Local TRT Clinic |  | company_or_brand | unjudged | name-only candidate needs domain/entity resolution before capture |
| 19 | Traditional Testosterone Clinics |  | company_or_brand | unjudged | name-only candidate needs domain/entity resolution before capture |
| 25 | Online Testosterone Therapy |  | company_or_brand | unjudged | name-only candidate needs domain/entity resolution before capture |
| 26 | 5 Best Telehealth Platforms for Erectile Dysfunction - REX MD | rexmd.com | company_or_brand | must_hit | plausible company domain, but observed page title has source/listicle shape |

Known relevant not capture/boundary:

| Rank | Name | Route | Eval label | Why |
| --- | --- | --- | --- | --- |
| 120 | Hims | reject_or_defer | must_hit |  |

### conversation_intelligence

- Known relevant seen: 27 cards / 6 unique qrels.
- Known relevant routed to capture: 0.
- Known relevant routed to boundary review: 23.
- Known bad/boundary rows promoted to capture: 0.

Top capture candidates:

_None._

Top boundary review:

| Rank | Name | Domain | Kind | Eval label | Caveat |
| --- | --- | --- | --- | --- | --- |
| 3 | Granola |  | company_or_brand | top_10_core | name-only candidate needs domain/entity resolution before capture |
| 4 | Jamie AI |  | company_or_brand | core_boundary_product_workflow | name-only candidate needs domain/entity resolution before capture |
| 6 | Fathom |  | company_or_brand | top_10_core | name-only candidate needs domain/entity resolution before capture |
| 7 | Gong |  | company_or_brand | top_10_core | name-only candidate needs domain/entity resolution before capture |
| 8 | Fireflies |  | company_or_brand | unjudged | name-only candidate needs domain/entity resolution before capture |
| 11 | Clari |  | company_or_brand | top_10_core | name-only candidate needs domain/entity resolution before capture |
| 13 | Meeting note tool pricing: Granola vs. Fireflies vs. Fathom ... | granola.ai | company_or_brand | top_10_core | plausible company domain, but observed page title has source/listicle shape |
| 14 | Otter |  | company_or_brand | top_10_core | name-only candidate needs domain/entity resolution before capture |
| 21 | Conversation Intelligence Software Guide for Sales 2026 | coffee.ai | company_or_brand | unjudged | plausible company domain, but observed page title has source/listicle shape |
| 22 | Salesman AI |  | company_or_brand | unjudged | name-only candidate needs domain/entity resolution before capture |

Known relevant not capture/boundary:

| Rank | Name | Route | Eval label | Why |
| --- | --- | --- | --- | --- |
| 15 | 10 Best Gong Alternatives and Competitors in 2026 | preserve_source_evidence | top_10_core | source page can preserve market evidence without becoming a profile target |
| 18 | Top 6 Gong Alternatives for Revenue Teams (2026) | preserve_source_evidence | top_10_core | source page can preserve market evidence without becoming a profile target |
| 49 | Best Otter alternatives for AI meeting notes in 2026 | preserve_source_evidence | top_10_core | source page can preserve market evidence without becoming a profile target |
| 85 | Gong | preserve_source_evidence | top_10_core | source domain evidence has a lower capture ceiling |

## What This Would Replace

- Replaces the v1 deterministic `source_role -> route` gate with `kind -> route` adjudication.
- Keeps source evidence preservation and candidate cards as the stable packet-local shape.
- Does not create a reusable skill, durable schema, or automatic capture queue.

## Cheapest Disconfirming Check

The borrowed Doro shape helps only if source/listicle artifacts stay out of capture while plausible companies and domainless brands move to capture or boundary review instead of false reject.
