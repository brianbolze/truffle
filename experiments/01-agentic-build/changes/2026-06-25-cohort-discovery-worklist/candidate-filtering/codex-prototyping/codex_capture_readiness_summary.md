# Codex Capture Readiness

Date: 2026-06-26
Status: packet-local no-spend usefulness gate over boundary-resolution output; no engine changes

## Read

- Input is only boundary-resolution rows already routed as `capture_candidate` or `existing_profile`.
- Existing store profiles stay separate from new capture-ready candidates.
- Homepage confirmation is treated as company existence, not capture-worthiness.
- Owned comparison/listicle pages are preserved as biased source evidence; they do not count as neutral third-party proof.

## Spend / Evidence

- Fresh live spend: 0 direct HTTP, 0 SerpAPI, 0 Firecrawl.
- Evidence used: prior boundary result JSON plus packet-local homepage/store receipts already cached by boundary resolution.

## Route Counts

| Cohort | Input | Existing | Capture ready | Fit review | Preserve source | Reject/defer | Boundary | Unique capture domains |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| conversation_intelligence | 31 | 5 | 17 | 7 | 2 | 0 | 0 | 17 |
| telehealth | 30 | 14 | 5 | 7 | 4 | 0 | 0 | 5 |

## Capture Ready

### conversation_intelligence

| Rank | Name | Actor role | Why |
| --- | --- | --- | --- |
| 8 | Fireflies (fireflies.ai) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 14 | Otter (otter.ai) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 25 | Clari vs Gong: Revenue intelligence for your GTM team (avoma.com) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 28 | AI Meeting Assistant Comparison 2026: 8 Tools \u0026 Pricing - Meetily (meetily.ai) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 30 | The 6 Best Fireflies.ai Alternatives \u0026 Competitors in 2026 (revenue.io) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 31 | 9 Best Gong Alternatives in 2026 (Ranked by Use Case) (cuebo.ai) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 38 | Vaamo AI (vaamo.ai) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 39 | HeySam (heysam.ai) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 40 | Best AI Meeting Assistant Tools for 2026 - tl;dv (tldv.io) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 41 | 10 Best Gong Alternatives & Competitors in 2026 for ... (aviso.com) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 43 | Jiminny (jiminny.com) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 44 | SalesSavvy.AI (salessavvy.ai) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 45 | Goodmeetings (goodmeetings.ai) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 46 | Salesken (salesken.ai) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 47 | 7 Best Gong Alternatives for Sales Teams (2026) | AmpUp (ampup.ai) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 48 | Best AI Meeting Prep Tools (2026 Picks) - MaxIQ (getmaxiq.com) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |
| 52 | Vinton | AI Notetaker for Salesforce (vinton.ai) | cohort_actor | conversation_or_revenue_intelligence_actor; full_profile_would_support_comparison_across_tools |

### telehealth

| Rank | Name | Actor role | Why |
| --- | --- | --- | --- |
| 10 | Online TRT vs Traditional Testosterone Clinics (vikingalternative.com) | cohort_actor | direct_to_patient_or_online_care_surface; cohort_actor_would_improve_cross_company_comparison |
| 16 | Online HRT & Menopause Specialists in Washington (bywinona.com) | cohort_actor | direct_to_patient_or_online_care_surface; cohort_actor_would_improve_cross_company_comparison |
| 29 | Best Online ED Treatments: Top Options Compared (telyrx.com) | cohort_actor | direct_to_patient_or_online_care_surface; cohort_actor_would_improve_cross_company_comparison |
| 36 | Elektra Health - Smashing The Menopause Taboo, Together (elektrahealth.com) | cohort_actor | cohort_specific_care_surface; full_profile_would_support_category_comparison |
| 39 | Online ED Treatment — Same-Day Prescription (vyta.co) | cohort_actor | direct_to_patient_or_online_care_surface; cohort_actor_would_improve_cross_company_comparison |

## Needs Review Or Preservation

### conversation_intelligence

| Route | Rank | Name | Actor role | Caveat |
| --- | --- | --- | --- | --- |
| cohort_fit_review | 21 | Conversation Intelligence Software Guide for Sales 2026 (coffee.ai) | adjacent_gtm_tool_or_platform | owned SEO/listicle page is biased source evidence, not neutral market proof; homepage confirmation alone is insufficient |
| cohort_fit_review | 24 | 6 Best Clari Alternatives in 2026 (Top Competitors ... (sybill.ai) | adjacent_gtm_tool_or_platform | owned SEO/listicle page is biased source evidence, not neutral market proof; homepage confirmation alone is insufficient |
| preserve_source_evidence | 27 | Best AI Meeting Notetakers 2026: 7 Tested (Bot-Free Picks) (get-alfred.ai) | adjacent_productivity_or_research_tool | owned SEO/listicle page is biased source evidence, not neutral market proof; homepage proves company existence only |
| preserve_source_evidence | 29 | Granola vs Otter vs Fireflies vs Fathom: Best AI Notetaker 2026 (useluminix.com) | adjacent_productivity_or_research_tool | owned SEO/listicle page is biased source evidence, not neutral market proof; homepage proves company existence only |
| cohort_fit_review | 33 | Revenue Intelligence Platforms: A Buyer's Guide (salesmotion.io) | adjacent_gtm_tool_or_platform | owned SEO/listicle page is biased source evidence, not neutral market proof; homepage confirmation alone is insufficient |
| cohort_fit_review | 34 | Best Conversation Intelligence Software 2026 (knowlee.ai) | adjacent_gtm_tool_or_platform | owned SEO/listicle page is biased source evidence, not neutral market proof; homepage confirmation alone is insufficient |
| cohort_fit_review | 36 | Rafiki AI (getrafiki.ai) | adjacent_gtm_tool_or_platform | homepage confirmation alone is insufficient |
| cohort_fit_review | 37 | Gong vs Clari Compared: AI Agents, Product ... (oliv.ai) | adjacent_gtm_tool_or_platform | owned SEO/listicle page is biased source evidence, not neutral market proof; homepage confirmation alone is insufficient |
| cohort_fit_review | 42 | Best Otter.ai Alternatives in 2026: Compared for Every Use Case (evro.ai) | adjacent_gtm_tool_or_platform | owned SEO/listicle page is biased source evidence, not neutral market proof; homepage confirmation alone is insufficient |

### telehealth

| Route | Rank | Name | Actor role | Caveat |
| --- | --- | --- | --- | --- |
| cohort_fit_review | 30 | Longevity Medicine 101: The Ultimate 2026 Guide (plotline.health) | adjacent_tool_or_platform | owned SEO/listicle page is biased source evidence, not neutral market proof; needs agent judgment before full company capture |
| preserve_source_evidence | 31 | TRT Clinic Comparison: Clearwater 2026 (Updated Guide) (myconfidenceclinic.com) | local_or_offline_clinic | owned SEO/listicle page is biased source evidence, not neutral market proof; full capture would likely add store bloat before neighborhood value |
| cohort_fit_review | 33 | How Top Clinics Are Making Longevity Medicine Their 2026 ... (holisticare.io) | adjacent_tool_or_platform | owned SEO/listicle page is biased source evidence, not neutral market proof; needs agent judgment before full company capture |
| cohort_fit_review | 34 | Online TRT Clinic - Telemedicine TRT for Men (madisonhealthny.com) | local_clinic_with_online_service_surface | do not capture solely because homepage confirms telemedicine language |
| cohort_fit_review | 40 | Superpower vs Function Health | What's the difference? (superpower.com) | adjacent_tool_or_platform | owned SEO/listicle page is biased source evidence, not neutral market proof; needs agent judgment before full company capture |
| preserve_source_evidence | 41 | The Collaborative: Home (jointhecollaborative.com) | local_or_offline_clinic | full capture would likely add store bloat before neighborhood value |
| cohort_fit_review | 42 | Telehealth - Biohackr Health (biohackr.health) | local_clinic_with_online_service_surface | do not capture solely because homepage confirms telemedicine language |
| cohort_fit_review | 44 | Foundation Zoomer | Healthspan Optimization & Aging ... (vibrant-wellness.com) | adjacent_tool_or_platform | needs agent judgment before full company capture |
| preserve_source_evidence | 51 | TelyRx (telyrx.com) | cohort_actor | underlying company may still be capture-ready via the primary row |
| cohort_fit_review | 52 | Madison Health NY (madisonhealthny.com) | local_clinic_with_online_service_surface | do not capture solely because homepage confirms telemedicine language |
| preserve_source_evidence | 59 | GLP-1s for Weight Loss - Online Treatment (walgreens.com) | broad_health_retail_or_pharmacy | homepage confirms a real company surface, not capture-worthiness |

## Acceptance Checks

- Source/listicle/directory artifacts capture-ready: 0.
- Homepage-only capture-ready rows without usefulness reasons: 0.
- Known bad/boundary eval rows capture-ready: 0.
- Existing profiles stayed distinct: True.

## Files

- Results JSON: `codex_capture_readiness_results.json`
- Summary: `codex_capture_readiness_summary.md`

## Readout

The gate turns the previous 42 capture candidates into a smaller capture-ready set plus explicit review/preservation buckets. The most important behavior is negative: real homepages are not enough. Rows with owned SEO/listicle evidence keep that evidence visible, but only cohort usefulness makes a new full capture worthwhile.
