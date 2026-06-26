# Codex Boundary Resolution

Date: 2026-06-26
Status: packet-local live-evidence pass over V2 boundary candidates; no engine changes

## Read

- V2's `boundary_review` queue can be shrunk with store baseline plus bounded homepage/search checks.
- Owned `best X` / `alternatives` pages are treated as biased source evidence, not as automatic publisher disqualification.
- Qrels remain evaluation-only after routing.

## Spend / Evidence

- Fresh live calls in latest invocation: direct HTTP homepages 9 / 40; SerpAPI focused queries 0 / 10; Firecrawl homepage scrapes 5 / 5.
- Total live cache footprint from this prototype: 47 direct homepage records; 5 SerpAPI records / 5 credits; 10 Firecrawl records / 10 credits.
- Evidence records used: {'homepage_direct': 48, 'homepage_firecrawl': 9, 'serpapi_result': 2, 'store_profile': 19}
- Cache records reused: {'homepage_direct': 39, 'homepage_firecrawl': 4}

## Cohort Summary

| Cohort | Input boundary | Resolved | Still boundary | Capture | Existing | Preserve | Reject | Source-like capture | Bad promoted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| conversation_intelligence | 106 | 36 | 70 | 26 | 5 | 3 | 2 | 0 | 0 |
| telehealth | 191 | 55 | 136 | 16 | 14 | 14 | 11 | 0 | 0 |

## conversation_intelligence

- Boundary shrink: 36 / 106 (34.0%).
- Known relevant: capture 1, existing profile 5, still boundary 9.

Top capture candidates:

| Rank | Name | Resolved domain | Method | Eval |
| --- | --- | --- | --- | --- |
| 8 | Fireflies | fireflies.ai | serpapi_organic | unjudged |
| 14 | Otter | otter.ai | serpapi_organic | top_10_core |
| 21 | Conversation Intelligence Software Guide for Sales 2026 | coffee.ai | homepage_direct | unjudged |
| 24 | 6 Best Clari Alternatives in 2026 (Top Competitors ... | sybill.ai | homepage_direct | unjudged |
| 25 | Clari vs Gong: Revenue intelligence for your GTM team | avoma.com | homepage_direct | unjudged |
| 27 | Best AI Meeting Notetakers 2026: 7 Tested (Bot-Free Picks) | get-alfred.ai | homepage_direct | unjudged |
| 28 | AI Meeting Assistant Comparison 2026: 8 Tools \u0026 Pricing - Meetily | meetily.ai | homepage_direct | unjudged |
| 29 | Granola vs Otter vs Fireflies vs Fathom: Best AI Notetaker 2026 | useluminix.com | homepage_direct | unjudged |

Top existing profiles:

| Rank | Name | Store name | Domain | Eval |
| --- | --- | --- | --- | --- |
| 3 | Granola | Granola | granola.ai | top_10_core |
| 7 | Gong | Gong | gong.io | top_10_core |
| 11 | Clari | Clari | clari.com | top_10_core |
| 13 | Meeting note tool pricing: Granola vs. Fireflies vs. Fathom ... | Granola | granola.ai | top_10_core |
| 35 | Clari | Clari | clari.com | top_10_core |

Top unresolved:

| Rank | Name | Domain | Reason | Eval |
| --- | --- | --- | --- | --- |
| 4 | Jamie AI |  | insufficient_evidence_after_budgeted_resolution | core_boundary_product_workflow |
| 6 | Fathom |  | insufficient_evidence_after_budgeted_resolution | top_10_core |
| 22 | Salesman AI |  | insufficient_evidence_after_budgeted_resolution | unjudged |
| 23 | Read AI | read.ai | insufficient_evidence_after_budgeted_resolution | unjudged |
| 53 | Leadoff.ai | leadoff.ai | homepage_unavailable | unjudged |
| 54 | Leexi | leexi.ai | homepage_unavailable | unjudged |
| 57 | Best AI Notetakers in 2026: Otter vs Fireflies vs Fathom vs MeetGeek ... | usecarly.com | homepage_unavailable | top_10_core |
| 58 | Best Revenue Intelligence Platforms in 2026: Clari, Gong ... | tellius.com | homepage_unavailable | top_10_core |

## telehealth

- Boundary shrink: 55 / 191 (28.8%).
- Known relevant: capture 0, existing profile 6, still boundary 5.

Top capture candidates:

| Rank | Name | Resolved domain | Method | Eval |
| --- | --- | --- | --- | --- |
| 10 | Online TRT vs Traditional Testosterone Clinics | vikingalternative.com | homepage_direct | unjudged |
| 16 | Online HRT & Menopause Specialists in Washington | bywinona.com | homepage_direct | unjudged |
| 29 | Best Online ED Treatments: Top Options Compared | telyrx.com | homepage_direct | unjudged |
| 30 | Longevity Medicine 101: The Ultimate 2026 Guide | plotline.health | homepage_direct | unjudged |
| 31 | TRT Clinic Comparison: Clearwater 2026 (Updated Guide) | myconfidenceclinic.com | homepage_direct | unjudged |
| 33 | How Top Clinics Are Making Longevity Medicine Their 2026 ... | holisticare.io | homepage_direct | unjudged |
| 34 | Online TRT Clinic - Telemedicine TRT for Men | madisonhealthny.com | homepage_direct | unjudged |
| 36 | Elektra Health - Smashing The Menopause Taboo, Together | elektrahealth.com | homepage_direct | unjudged |

Top existing profiles:

| Rank | Name | Store name | Domain | Eval |
| --- | --- | --- | --- | --- |
| 9 | TRT Nation | TRT Nation | trtnation.com | unjudged |
| 15 | Function | 100 Healthy Years | Function Health | functionhealth.com | unjudged |
| 17 | TRT Online: A Smarter Way to Treat Low Testosterone | Strut Health | struthealth.com | unjudged |
| 26 | 5 Best Telehealth Platforms for Erectile Dysfunction - REX MD | Rex MD | rexmd.com | must_hit |
| 49 | REX MD | Rex MD | rexmd.com | must_hit |
| 53 | Function Health | Function Health | functionhealth.com | unjudged |
| 57 | AgelessRx | AgelessRx | agelessrx.com | should_hit |
| 58 | BlueChew | BlueChew | bluechew.com | should_hit |

Top unresolved:

| Rank | Name | Domain | Reason | Eval |
| --- | --- | --- | --- | --- |
| 62 | Kinsyn | kinsyn.com | insufficient_evidence_after_budgeted_resolution | unjudged |
| 63 | Newsletter | preferences.mail.sheknows.com | insufficient_evidence_after_budgeted_resolution | unjudged |
| 64 | Veedma | veedma.com | insufficient_evidence_after_budgeted_resolution | unjudged |
| 66 | Best Online TRT Clinics in 2026: Pricing \u0026 Treatment Options | hormoneonline.com | insufficient_evidence_after_budgeted_resolution | unjudged |
| 67 | EverSpan Life: 100+ Biomarkers | Dedicated Clinician | everspanlife.com | insufficient_evidence_after_budgeted_resolution | unjudged |
| 68 | NADclinic- Producers of the worlds premium NAD+ | nadclinic.com | insufficient_evidence_after_budgeted_resolution | unjudged |
| 69 | Truman Health | trumanhealth.ca | insufficient_evidence_after_budgeted_resolution | unjudged |
| 70 | DirectMeds | directmeds.com.au | insufficient_evidence_after_budgeted_resolution | unjudged |

## Files

- Results JSON: `codex_boundary_resolution_results.json`
- Summary: `codex_boundary_resolution_summary.md`
- Live evidence cache: `boundary-resolution-cache/`

## Readout

This pass should be treated as prototype evidence, not an engine contract. The useful rule is the owned-listicle split: preserve the article as biased source evidence, but resolve the domain through homepage/store evidence before deciding whether the company belongs in a capture queue.
