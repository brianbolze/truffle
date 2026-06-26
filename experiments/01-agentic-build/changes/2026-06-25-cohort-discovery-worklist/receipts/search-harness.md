# Search Harness Receipt

Date: 2026-06-26
Status: packet-local search framing pass; no live source spend
Later note: the next page/entity extraction probe has now run; see [`page-extraction-probe.md`](page-extraction-probe.md). The current follow-on shape is the candidate-filtering synthesis at [`../candidate-filtering/2026-06-26-cohort-discovery-worklist-synthesis.md`](../candidate-filtering/2026-06-26-cohort-discovery-worklist-synthesis.md), not another query-only pass.

## What This Adds

This pass treats cohort discovery as entity search. It builds packet-local relevance judgments,
extracts ranked source units from the existing iteration-2 raw outputs, creates entity candidates
from exact-domain hits and alias mentions, then ranks them with a transparent RRF-style score.

It does not open listicle pages or fetch new sources. That omission is intentional: this receipt
shows what the current raw evidence can see before adding page extraction.

## Relevance Frame

A relevant capture candidate is not merely a mentioned company. For this packet, relevance means:

- grade 4: must-capture / F3-F4 / top-10 category-defining target;
- grade 3: should-capture / F2 / Brian-marked worth_capture;
- grade 2: core but product/workflow boundary;
- grade 1: boundary, unsure, or Tier C only;
- grade 0: hard exclude / wrong-type / adjacent pollution.

The ranker does not use the grade as a feature; grades are evaluation labels.

## Metrics Snapshot

| Variant | Candidates | Judged | P@10 | R@10 | nDCG@10 | Relevant misses |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| telehealth_external | 123 | 13 | 0.100 | 0.030 | 0.139 | 21 |
| conversation_external | 108 | 9 | 0.500 | 0.500 | 0.649 | 3 |
| conversation_store_first | 110 | 11 | 0.500 | 0.500 | 0.649 | 1 |

## Telehealth Search Diagnosis

- Relevant qrels not retrieved from existing raw units: 21.
- Telehealth retrieval by label: must_hit 6/13; should_hit 4/15; worth_capture 2/5.
- This means the current raw rows do not contain enough machine-readable evidence for the broad
  telehealth target set. A better reranker alone cannot recover names absent from the raw units.
- Top-ranked unknown domains are mostly source/publisher or long-tail operator artifacts, which is
  the expected symptom of using SERP result pages without extracting the entities inside list pages.

Most important telehealth misses:

- Hims & Hers (must_hit, grade 4)
- LifeMD (must_hit, grade 4)
- Niagen Plus (must_hit, grade 4)
- Wisp (must_hit, grade 4)
- Eden (must_hit, grade 4)
- Lifeforce (must_hit, grade 4)
- Remedy Meds (must_hit, grade 4)
- Amble (should_hit, grade 3)
- Blokes (should_hit, grade 3)
- Geviti (should_hit, grade 3)
- Invigor Medical (should_hit, grade 3)
- Ivy Rx (should_hit, grade 3)

## Conversation Intelligence Diagnosis

- External-only misses: Loom, Dovetail, AlphaSense.
- Store-first misses: Loom.
- Store-first retrieval by label: top_10_core 9/10.
- Store-first materially changes search quality because several high-relevance targets are already
  profiled locally. This supports keeping store baseline as a first-class retriever.

## Next Stage At Time Of Receipt

At this point in the packet, the evaluated retrieval stage shifted to page extraction. The search harness gives a simple gate:
page extraction must improve relevant recall and top-K precision over this raw-unit baseline,
especially for telehealth, without promoting grade-0/1 candidates into the capture queue.

Generated detail:

- JSON summary: `receipts/raw/search-harness/search-summary.json`
