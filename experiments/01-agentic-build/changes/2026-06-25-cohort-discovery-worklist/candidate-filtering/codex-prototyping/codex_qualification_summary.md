# Codex Candidate Qualification Prototype

Date: 2026-06-26
Status: packet-local prototype; no implementation proposal or engine changes

## Read

- Prototype shape: build qrel-free observed-domain evidence cards, preserve source evidence separately, and route only likely company/brand targets toward capture.
- Routing input excludes qrels, aliases, and Brian-reviewed labels; qrels are added back only for evaluation matching.
- The visible disconfirming check passes if no source-like candidates are routed to `capture_candidate`.

## Outputs

- Candidate cards: `codex_candidate_cards.json`
- Evaluation JSON: `codex_qualification_eval.json`
- Summary: `codex_qualification_summary.md`

## Cohort Summary

| Cohort | Candidates | Capture | Preserve source | Product/workflow | Reject/defer | Source-like capture |
| --- | --- | --- | --- | --- | --- | --- |
| telehealth | 226 | 5 | 38 | 1 | 182 | 0 |
| conversation_intelligence | 120 | 0 | 52 | 3 | 65 | 0 |

## Evaluation Notes

### telehealth

- Known relevant seen: 13.
- Known relevant preserved outside reject/defer: 4.
- Known relevant routed directly to capture: 2.
- Known bad/boundary rows promoted to capture: 0.

Top capture candidates:

| Rank | Name | Domain | Confidence | Eval label |
| --- | --- | --- | --- | --- |
| 1 | Healthspan | gethealthspan.com | medium | unjudged |
| 4 | Want a Longer Lifespan? You Should Care About Your ... | honehealth.com | medium | must_hit |
| 7 | MyHealthspan | myhealthspan.com | medium | unjudged |
| 18 | Defymedical | defymedical.com | medium | should_hit |
| 19 | gennev.com | gennev.com | medium | unjudged |

Known relevant not routed to capture:

| Rank | Name | Route | Eval label | Why |
| --- | --- | --- | --- | --- |
| 21 | 5 Best Telehealth Platforms for Erectile Dysfunction - REX MD | preserve_source_evidence | must_hit | source_page_title; preserve market evidence; do not promote page publisher as the target |
| 46 | AgelessRx | reject_or_defer | should_hit | insufficient repeated or cross-surface evidence for capture |
| 47 | BlueChew | reject_or_defer | should_hit | insufficient repeated or cross-surface evidence for capture |
| 81 | Online ED Treatment | FDA-Approved Meds - Eden Telemed | reject_or_defer | must_hit | insufficient repeated or cross-surface evidence for capture |
| 109 | Hims | reject_or_defer | must_hit | non_profile_navigation_or_app_surface; artifact should not feed capture queue without separate verification |
| 113 | Ro | reject_or_defer | must_hit | insufficient repeated or cross-surface evidence for capture |
| 146 | https://getroman.pxf.io/c/1955282/1558337/15530?subid1=FAYKKxoAK0wfRMJTfqX7JX_XXq9VbjAJemW&subid2=%2Fhealth%2Fweight-loss%2Fbest-affordable- | preserve_source_evidence | must_hit | source_page_title; preserve market evidence; do not promote page publisher as the target |
| 156 | joinmidi.com | reject_or_defer | worth_capture | insufficient repeated or cross-surface evidence for capture |
| 161 | myalloy.com | reject_or_defer | worth_capture | insufficient repeated or cross-surface evidence for capture |
| 183 | Midi Health | reject_or_defer | worth_capture | insufficient repeated or cross-surface evidence for capture |

### conversation_intelligence

- Known relevant seen: 22.
- Known relevant preserved outside reject/defer: 18.
- Known relevant routed directly to capture: 0.
- Known bad/boundary rows promoted to capture: 0.

Top capture candidates:

| Rank | Name | Domain | Confidence | Eval label |
| --- | --- | --- | --- | --- |

Known relevant not routed to capture:

| Rank | Name | Route | Eval label | Why |
| --- | --- | --- | --- | --- |
| 7 | Meeting note tool pricing: Granola vs. Fireflies vs. Fathom ... | preserve_source_evidence | top_10_core | source_page_title; preserve market evidence; do not promote page publisher as the target |
| 8 | 10 Best Gong Alternatives and Competitors in 2026 | preserve_source_evidence | top_10_core | source_page_title; preserve market evidence; do not promote page publisher as the target |
| 11 | Top 6 Gong Alternatives for Revenue Teams (2026) | preserve_source_evidence | top_10_core | source_page_title; preserve market evidence; do not promote page publisher as the target |
| 15 | 6 Best Clari Alternatives in 2026 (Top Competitors ... | preserve_source_evidence | top_10_core | source_page_title; preserve market evidence; do not promote page publisher as the target |
| 16 | Clari vs Gong: Revenue intelligence for your GTM team | preserve_source_evidence | top_10_core | source_page_title; preserve market evidence; do not promote page publisher as the target |
| 19 | Granola vs Otter vs Fireflies vs Fathom: Best AI Notetaker 2026 | preserve_source_evidence | top_10_core | source_page_title; preserve market evidence; do not promote page publisher as the target |
| 21 | 9 Best Gong Alternatives in 2026 (Ranked by Use Case) | preserve_source_evidence | top_10_core | source_page_title; preserve market evidence; do not promote page publisher as the target |
| 25 | Clari | reject_or_defer | top_10_core | insufficient repeated or cross-surface evidence for capture |
| 27 | Gong vs Clari Compared: AI Agents, Product ... | preserve_source_evidence | top_10_core | source_page_title; preserve market evidence; do not promote page publisher as the target |
| 31 | 10 Best Gong Alternatives & Competitors in 2026 for ... | preserve_source_evidence | top_10_core | source_page_title; preserve market evidence; do not promote page publisher as the target |

## What This Would Replace

- Replaces raw rank-to-capture behavior with an auditable route.
- Replaces human-only candidate review with a reusable evidence-card contract.
- Does not replace page/entity extraction, qrels, or full `/research-company` capture.

## Cheapest Disconfirming Check

Inspect `source_like_capture_count` and the top capture candidates. If listicles, publishers, social pages, or low-trust artifacts still enter capture, this layer fails its first job.
