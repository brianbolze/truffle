# Mini Proposal: Generic Candidate Qualification

Date: 2026-06-26
Status: parked prior art; do not treat as governing proposal
Source request: Brian pushed back that candidate filtering must generalize beyond telehealth; use `TAXONOMIES.md` guidance to avoid overfitting categorical fields.
Strategic frame: [`_design/2026-06-26-coverage-strategy-frame.md`](../../../../../_design/2026-06-26-coverage-strategy-frame.md)
Fresh-session brief: [`candidate-qualification-fresh-session-brief.md`](candidate-qualification-fresh-session-brief.md)

<!-- Parked prior art only. This proposal pre-dates the coverage frame and should not anchor
     the next agent's framing or solution search. -->

## How To Use This

Read this only after an independent frame/options pass from the coverage frame, decision
surface, and page-extraction receipt.

Keep the problem diagnosis and evaluation cautions:

- source pages can be valuable evidence without being profile-worthy candidates;
- qrels and Brian-reviewed labels must stay evaluation-only;
- candidate filtering must preserve page-extraction recall while improving queue precision;
- routing labels should not become durable schema or a vertical-specific taxonomy by accident.

Do not inherit the specific routing labels, implementation sketch, or acceptance checks unless
the fresh pass re-derives them from the coverage frame and validates them against the packet
evidence.

## Required Fields

risk: medium
write_scope: Packet-local follow-on only: `candidate-qualification` probe script, fixtures/receipts under this same change folder, and updates to packet-local receipts/decision notes. Do not edit `SCHEMA.md`, `TAXONOMIES.md`, `store/`, `tools/`, `skills/`, Signals paths, or create a reusable `/cohort-discovery` skill.
spend_stop: No new live source gathering required for the first implementation; use existing raw SERP/Exa/page-extraction captures. Stop before any new SerpAPI, Exa, Firecrawl, store capture, or source-family expansion.
acceptance_checks: Produce a packet-local qualification receipt that labels page-augmented candidates across both telehealth and conversation-intelligence runs without using qrels or Brian-reviewed labels as qualifier inputs. The receipt must join qrels only after routing to score before/after P@10, R@10, nDCG@10, grade-3/4 retrieved count, Tier A/B queue precision, named regressions, remaining misses, and label counts. Add a small adjudicated negative surface from current qrel-null top unknown pages/domains so source/publisher cleanup is auditable. Passing requires the proposed Tier A/B queue to remove evidence-only source/publisher pages without materially reducing page-extraction recall or suppressing valid positives such as Midi Health.
escalate_if: Work wants durable taxonomy/schema values, vertical-specific exclusion labels as engine defaults, new live source spend, automatic capture, store writes, or a reusable skill.

## Problem

The page-extraction probe proved a real retrieval fix: opening source pages surfaced candidate companies hidden behind SERP snippets. But it also exposed the next failure mode: extracted evidence mixes **companies worth capturing** with **source pages, publishers, comparison pages, products, parent companies, and adjacent tools**.

Under the coverage frame, this is the staging problem before promotion: preserve useful market evidence while deciding which normalized candidates are profile-worthy capture targets.

The tempting fix is to add vertical-specific negative categories, like `retailer/pharmacy` for telehealth. That is the wrong abstraction. It would not transfer to productivity SaaS, conversation intelligence, fintech, consumer goods, or most future cohorts.

Per `TAXONOMIES.md`, closed categorical fields earn their keep only when they group reliably across the whole store. This qualification layer has not earned durable schema. It should stay packet-local and search-specific until repeated cohorts prove stable values.

## Short Answer

Add a **generic candidate qualification stage** between entity extraction and ranking. It should separately label evidence provenance and candidate routing, then rank only candidates that qualify for a capture queue.

Do not add telehealth-specific exclusions, and do not add durable taxonomy fields yet.

## Constraints / Non-Goals

- Not a new `SCHEMA.md` or `TAXONOMIES.md` field.
- Not a telehealth-only filter.
- Not a final entity-resolution system.
- Not a market taxonomy or cohort ontology.
- Not a capture queue autopilot.
- Not a source-quality verdict; source pages may remain useful evidence even when they are not capture targets.
- Not an answer-key-driven reranker; qrels and Brian-reviewed labels are evaluation-only.

## Options considered

1. **Hard-code vertical negatives.** For telehealth, labels such as pharmacy, retailer, payer, content site, and clinic directory would clean this one run. This is fast but wrong: each new cohort would need a new exclusion menu, and the system would drift into project-specific rules. [cut]
2. **Use existing store taxonomies directly.** Reuse `entity_type`, `offering_category`, `target_market`, and `primary_industry` as candidate filters. This has some value after capture, but it is too late and too coarse for search-result qualification. A Zapier article and Gong are both in the technology neighborhood, but only one is a capture target for conversation intelligence. [could have]
3. **Packet-local generic qualification routes.** Label evidence units by provenance, then label normalized candidates by route and reason. Keep the routing labels generic and provisional; use them to filter/rank the capture queue while preserving source pages as evidence. [should have] -- **recommended**

## Recommendation

Choose option 3.

Use two routing fields plus evidence provenance:

- **Evidence role:** describes the evidence unit only, such as `official_page`, `third_party_list_or_review`, `comparison_page`, `directory_or_marketplace`, `search_result`, `outbound_link`, or `unknown_evidence`. This is provenance, not a candidate-level veto.
- **Candidate route:** `capture_target`, `evidence_only`, `boundary_review`, `exclude`.
- **Route reason:** `profileable_company_or_brand`, `source_or_publisher`, `product_or_workflow`, `parent_or_owner`, `adjacent`, `wrong_type`, `uncertain`.

These are not store taxonomies. They are retrieval-time labels for deciding what can enter a capture worklist. Keep cohort nuance as a short free-text reason unless it changes the route. The labels should remain in the receipt unless repeated cohorts prove they deserve a durable engine surface.

## Implementation Sketch

1. Start from the existing search/page-extraction candidate set in this packet.
2. Build a small packet-local adjudication fixture from current page-augmented top qrel-null pages/domains for both cohorts. Label only expected route for scoring: capture target, evidence-only source/publisher, product/workflow, parent/owner, adjacent, wrong type, or uncertain.
3. Add a packet-local qualifier that assigns evidence roles and candidate routes using only candidate name/domain, matched aliases, source rows, page title, outbound-link context, page text snippets, and domain/source patterns. Do not use qrel labels, grades, or Brian-reviewed labels as qualifier inputs.
4. Route candidates:
   - promote `capture_target` to the proposed capture queue;
   - keep `evidence_only` as supporting evidence;
   - send `boundary_review` to human review before promotion;
   - suppress `exclude` from Tier A/B.
5. Score after routing by joining qrels and the adjudicated fixture only in the receipt. Report before/after P@10, R@10, nDCG@10, grade-3/4 retrieved count, Tier A/B precision, named regressions, remaining misses, and label counts for telehealth and conversation intelligence.
6. Write a receipt comparing old rank, evidence role, candidate route, route reason, proposed queue rank, and reason. Include corrections such as Midi Health as a positive evaluation target, but not as an automatic qualifier input.

## Review Notes

The review should focus on whether the labels are genuinely generic and whether the automatic qualifier is separated from the evaluation answer key. If any label only makes sense in telehealth or does not affect routing/metrics, cut or rename it.

The main value claim is simple: qualification should remove source/publisher pages from the capture queue without suppressing valid cohort members or losing the page-extraction recall gain. If it cannot do that over both telehealth and conversation intelligence using the same routing model, park this slice rather than promote it.
