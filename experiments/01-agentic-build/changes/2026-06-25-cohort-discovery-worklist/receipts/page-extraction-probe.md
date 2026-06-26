# Page Extraction Probe Receipt

Date: 2026-06-26
Status: live page/entity extraction probe complete

## Boundary

- Fixed panel: 11 telehealth result/list pages and 4 conversation-intelligence pages.
- Source method: direct HTTP fetch with stdlib HTML reduction; Firecrawl fallback for 2 direct-fetch-blocked pages.
- Spend: estimated 2 Firecrawl base scrape credits; no SerpAPI or Exa calls.
- Writes only packet-local raw/reduced page envelopes and this receipt.

## Fetch Result

- Pages fetched with usable text: 15/15.
- Page units added: 168.

## Metrics

| Variant | Candidates | Judged | P@10 | R@10 | nDCG@10 | Relevant misses |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| telehealth_raw | 123 | 13 | 0.100 | 0.030 | 0.139 | 21 |
| telehealth_page_augmented | 240 | 25 | 0.600 | 0.182 | 0.562 | 11 |
| conversation_raw | 108 | 9 | 0.500 | 0.500 | 0.649 | 3 |
| conversation_page_augmented | 131 | 11 | 0.600 | 0.600 | 0.718 | 3 |

## Read

- Telehealth moved from P@10 0.100, R@10 0.030, nDCG@10 0.139 to P@10 0.600, R@10 0.182, nDCG@10 0.562.
- Telehealth retrieval by label after page extraction: must_hit 11/13; should_hit 7/15; worth_capture 4/5.
- Conversation moved from P@10 0.500, R@10 0.500, nDCG@10 0.649 to P@10 0.600, R@10 0.600, nDCG@10 0.718.
- The improvement comes from page text and outbound links naming entities hidden behind source result pages.
- This supports making page/entity extraction part of the evaluated recipe before adding new discovery sources.
- The ranker still needs a candidate-type filter / verification gate: source domains remain in the top ranks.

Remaining telehealth misses:

- Niagen Plus (must_hit, grade 4)
- Lifeforce (must_hit, grade 4)
- Amble (should_hit, grade 3)
- Geviti (should_hit, grade 3)
- Invigor Medical (should_hit, grade 3)
- Ivy Rx (should_hit, grade 3)
- Kingsberg Medical (should_hit, grade 3)
- Nurx (should_hit, grade 3)
- ProHealth (should_hit, grade 3)
- Rugiet Ready (should_hit, grade 3)
- Eucalyptus Health (worth_capture, grade 3)

Generated detail:

- Page panel: `receipts/raw/page-extraction/page-panel.json`
- Run summary: `receipts/raw/page-extraction/run-summary.json`
- Score summary: `receipts/raw/page-extraction/score-summary.json`

Low-grade or boundary rows in top 20: none.
