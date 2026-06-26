# Codex vs Claude Capture Gate Comparison

Date: 2026-06-26
Status: packet-local comparison over the 61 Codex capture-readiness rows; no engine changes

## Read

- Joined Codex capture-readiness rows to Claude routed candidates by cohort + resolved domain.
- Claude did not model existing store profiles separately, so `existing_profile` vs Claude `capture` is treated as store-awareness alignment.
- Proposed final routes are comparison guidance, not durable Truffle design.

## Counts

| Metric | Counts |
| --- | --- |
| comparison_class_counts | {"aligned": 19, "aligned_duplicate_handling_gap": 1, "aligned_store_awareness_gap": 15, "disagreement_adjudicated": 21, "missing_in_claude": 4, "store_source_role_split": 1} |
| codex_route_counts | {"capture_ready": 22, "cohort_fit_review": 14, "existing_profile": 19, "preserve_source_evidence": 6} |
| claude_normalized_route_counts | {"capture_ready": 41, "cohort_fit_review": 7, "missing_in_claude": 4, "preserve_source_evidence": 7, "reject_or_defer": 2} |
| proposed_final_route_counts | {"capture_ready": 21, "cohort_fit_review": 11, "existing_profile": 19, "preserve_source_evidence": 10} |

## By Cohort

| Cohort | Input | Comparison classes | Proposed final routes |
| --- | --- | --- | --- |
| conversation_intelligence | 31 | {"aligned": 12, "aligned_store_awareness_gap": 4, "disagreement_adjudicated": 13, "missing_in_claude": 2} | {"capture_ready": 17, "cohort_fit_review": 6, "existing_profile": 5, "preserve_source_evidence": 3} |
| telehealth | 30 | {"aligned": 7, "aligned_duplicate_handling_gap": 1, "aligned_store_awareness_gap": 11, "disagreement_adjudicated": 8, "missing_in_claude": 2, "store_source_role_split": 1} | {"capture_ready": 4, "cohort_fit_review": 5, "existing_profile": 14, "preserve_source_evidence": 7} |

## Disagreements / Missing

| Cohort | Rank | Domain | Codex / Claude | Class | Proposed final | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| conversation_intelligence | 7 | gong.io | existing_profile / missing | missing_in_claude | existing_profile | Store baseline wins; do not create duplicate capture work. |
| conversation_intelligence | 8 | fireflies.ai | capture_ready / missing | missing_in_claude | capture_ready | Absent from Claude's broader routed set; keep Codex no-spend readiness call. |
| telehealth | 9 | trtnation.com | existing_profile / preserve | store_source_role_split | existing_profile | Store baseline wins; do not create duplicate capture work. |
| conversation_intelligence | 21 | coffee.ai | cohort_fit_review / preserve | disagreement_adjudicated | cohort_fit_review | Own product is an AI CRM agent; useful adjacent GTM context, not yet full CI capture. |
| conversation_intelligence | 24 | sybill.ai | cohort_fit_review / capture | disagreement_adjudicated | capture_ready | Claude's product read plus homepage evidence indicate own sales assistant / call-summary product. |
| conversation_intelligence | 27 | get-alfred.ai | preserve_source_evidence / capture | disagreement_adjudicated | cohort_fit_review | Source says AI notetaker, homepage says email/calendar assistant; resolve before capture. |
| conversation_intelligence | 29 | useluminix.com | preserve_source_evidence / review | disagreement_adjudicated | preserve_source_evidence | Homepage is deep-research/newsletter; owned notetaker comparison is useful biased source evidence only. |
| conversation_intelligence | 31 | cuebo.ai | capture_ready / review | disagreement_adjudicated | cohort_fit_review | Sales roleplay/coaching is adjacent to CI; capture value needs synthesis test. |
| conversation_intelligence | 34 | knowlee.ai | cohort_fit_review / preserve | disagreement_adjudicated | preserve_source_evidence | AI workforce vendor appears via owned CI listicle, but homepage is not a CI product. |
| telehealth | 30 | plotline.health | cohort_fit_review / preserve | disagreement_adjudicated | cohort_fit_review | Concierge/longevity care may matter for healthspan neighborhood, but not clearly DTC telehealth capture. |
| telehealth | 33 | holisticare.io | cohort_fit_review / drop | disagreement_adjudicated | preserve_source_evidence | B2B clinic software; preserve as care-delivery/clinic-platform context, not profile capture. |
| telehealth | 34 | madisonhealthny.com | cohort_fit_review / capture | disagreement_adjudicated | cohort_fit_review | Own online TRT service, but local clinic scope keeps it out of automatic capture. |
| telehealth | 40 | superpower.com | cohort_fit_review / capture | disagreement_adjudicated | cohort_fit_review | Potentially important Function/longevity neighbor; promote only after synthesis test. |
| telehealth | 41 | jointhecollaborative.com | preserve_source_evidence / capture | disagreement_adjudicated | preserve_source_evidence | Concierge menopause clinic evidence is useful, but local/high-touch scope weakens full-capture case. |
| conversation_intelligence | 36 | getrafiki.ai | cohort_fit_review / capture | disagreement_adjudicated | capture_ready | Homepage and Claude both indicate own conversation/revenue intelligence product. |
| conversation_intelligence | 37 | oliv.ai | cohort_fit_review / capture | disagreement_adjudicated | capture_ready | Own revenue AI platform around deal/call intelligence; owned listicle should be caveated, not disqualifying. |
| telehealth | 44 | vibrant-wellness.com | cohort_fit_review / drop | disagreement_adjudicated | preserve_source_evidence | Specialty lab/provider infrastructure; useful source/card, not DTC telehealth capture. |
| conversation_intelligence | 38 | vaamo.ai | capture_ready / review | disagreement_adjudicated | cohort_fit_review | Sales coaching platform looks adjacent; not enough to make full CI capture obvious. |
| conversation_intelligence | 39 | heysam.ai | capture_ready / review | disagreement_adjudicated | capture_ready | Homepage explicitly says conversation intelligence in Slack plus CRM hygiene/RFP agents. |
| telehealth | 52 | madisonhealthny.com | cohort_fit_review / capture | disagreement_adjudicated | cohort_fit_review | Own online TRT service, but local clinic scope keeps it out of automatic capture. |
| conversation_intelligence | 42 | evro.ai | cohort_fit_review / preserve | disagreement_adjudicated | preserve_source_evidence | Communication-coach product is adjacent, and owned Otter-alternatives page is biased source evidence. |
| telehealth | 59 | walgreens.com | preserve_source_evidence / capture | disagreement_adjudicated | preserve_source_evidence | Real GLP-1 telehealth surface, but broad retailer profile is not clearly useful cohort capture. |
| conversation_intelligence | 44 | salessavvy.ai | capture_ready / review | disagreement_adjudicated | cohort_fit_review | Sales intelligence assistant evidence is thin; keep for review before profile capture. |
| conversation_intelligence | 48 | getmaxiq.com | capture_ready / preserve | disagreement_adjudicated | capture_ready | Homepage says AI-native revenue intelligence platform; useful for CI/revenue-intel comparison. |
| telehealth | 161 | ivimhealth.com | existing_profile / missing | missing_in_claude | existing_profile | Store baseline wins; do not create duplicate capture work. |
| telehealth | 237 | remedymeds.com | existing_profile / missing | missing_in_claude | existing_profile | Store baseline wins; do not create duplicate capture work. |

## Capture-Ready Proposal

| Cohort | Rank | Domain | Name | Why |
| --- | --- | --- | --- | --- |
| conversation_intelligence | 8 | fireflies.ai | Fireflies | Absent from Claude's broader routed set; keep Codex no-spend readiness call. |
| telehealth | 10 | vikingalternative.com | Online TRT vs Traditional Testosterone Clinics | Codex and Claude agree after route normalization. |
| conversation_intelligence | 14 | otter.ai | Otter | Codex and Claude agree after route normalization. |
| telehealth | 16 | bywinona.com | Online HRT & Menopause Specialists in Washington | Codex and Claude agree after route normalization. |
| conversation_intelligence | 24 | sybill.ai | 6 Best Clari Alternatives in 2026 (Top Competitors ... | Claude's product read plus homepage evidence indicate own sales assistant / call-summary product. |
| conversation_intelligence | 25 | avoma.com | Clari vs Gong: Revenue intelligence for your GTM team | Codex and Claude agree after route normalization. |
| conversation_intelligence | 28 | meetily.ai | AI Meeting Assistant Comparison 2026: 8 Tools \u0026 Pricing - Meetily | Codex and Claude agree after route normalization. |
| conversation_intelligence | 30 | revenue.io | The 6 Best Fireflies.ai Alternatives \u0026 Competitors in 2026 | Codex and Claude agree after route normalization. |
| telehealth | 36 | elektrahealth.com | Elektra Health - Smashing The Menopause Taboo, Together | Codex and Claude agree after route normalization. |
| telehealth | 39 | vyta.co | Online ED Treatment — Same-Day Prescription | Codex and Claude agree after route normalization. |
| conversation_intelligence | 36 | getrafiki.ai | Rafiki AI | Homepage and Claude both indicate own conversation/revenue intelligence product. |
| conversation_intelligence | 37 | oliv.ai | Gong vs Clari Compared: AI Agents, Product ... | Own revenue AI platform around deal/call intelligence; owned listicle should be caveated, not disqualifying. |
| conversation_intelligence | 39 | heysam.ai | HeySam | Homepage explicitly says conversation intelligence in Slack plus CRM hygiene/RFP agents. |
| conversation_intelligence | 40 | tldv.io | Best AI Meeting Assistant Tools for 2026 - tl;dv | Codex and Claude agree after route normalization. |
| conversation_intelligence | 41 | aviso.com | 10 Best Gong Alternatives & Competitors in 2026 for ... | Codex and Claude agree after route normalization. |
| conversation_intelligence | 43 | jiminny.com | Jiminny | Codex and Claude agree after route normalization. |
| conversation_intelligence | 45 | goodmeetings.ai | Goodmeetings | Codex and Claude agree after route normalization. |
| conversation_intelligence | 46 | salesken.ai | Salesken | Codex and Claude agree after route normalization. |
| conversation_intelligence | 47 | ampup.ai | 7 Best Gong Alternatives for Sales Teams (2026) | AmpUp | Codex and Claude agree after route normalization. |
| conversation_intelligence | 48 | getmaxiq.com | Best AI Meeting Prep Tools (2026 Picks) - MaxIQ | Homepage says AI-native revenue intelligence platform; useful for CI/revenue-intel comparison. |
| conversation_intelligence | 52 | vinton.ai | Vinton | AI Notetaker for Salesforce | Codex and Claude agree after route normalization. |

## Files

- Results JSON: `codex_claude_comparison_results.json`
- Summary: `codex_claude_comparison_summary.md`

## Readout

The two lanes agree on the basic shape: source/publisher artifacts should not become captures, and real dual-role companies need product evidence. The main tension is calibration: Claude is more willing to capture owned in-cohort offerings, while Codex is more conservative around adjacent tools, local clinics, and broad health giants.
