# Telehealth Validation Receipt

Date: 2026-06-25
Status: initial validation failed; superseded by WebSearch, iteration-2, and page-extraction addenda

## Run Boundary

No store writes, no `/research-company`, no Firecrawl captures.

Live captures:

- SerpAPI organic-only category queries: 4 credits.
- SerpAPI organic-only demand query: 1 credit.
- Exa `/search` novelty query: USD 0.017.

Queries stayed within the approved cap.

## Source Panel

Category / listicle / direct-enumeration SERPs:

- `best online telehealth weight loss GLP-1 providers 2026`
- `best online TRT clinic 2026`
- `best menopause telehealth HRT online 2026`
- `telehealth hormone optimization clinic online 2026`

Demand-side SERP:

- `Ro Hims Hers GLP-1 telehealth alternatives Mochi Noom`

Exa novelty:

- `direct to consumer telehealth brands for GLP-1 weight loss TRT menopause HRT`

Useful source URLs surfaced:

- Forbes GLP-1 list: https://www.forbes.com/health/weight-loss/best-affordable-online-glp1-providers/
- U.S. News GLP-1 provider list: https://health.usnews.com/best-diet/medication/top-glp-1-weight-loss-medication-providers
- Policy Lab TRT list: https://policylab.us/testosterone-replacement-therapy/online-trt/
- PPARX TRT list: https://www.pparx.org/testosterone/best-online-trt-clinics/
- Policy Lab HRT list: https://policylab.us/hormone-replacement-therapy/hrt-online/
- Flow Space menopause telehealth list: https://www.theflowspace.com/reproductive-health/menopause/online-menopause-treatment-2941951/
- Fierce Healthcare Novo / telehealth GLP-1 article: https://www.fiercehealthcare.com/health-tech/hims-hers-lifemd-stock-skyrockets-after-inking-deal-novo-nordisk-sell-wegovy
- Zealthy self-promotional GLP-1 list: https://getzealthy.com/post/most-trusted-places-to-buy-glp-1s-online-in-2026

## Holdout Recovery

F3/F4 must-hit holdouts recovered: 10 of 13 after the WebSearch addendum.

Recovered:

- Hims & Hers
- LifeMD
- One Medical
- Wisp
- Eden
- Hone Health
- Noom Med
- Peter MD
- Remedy Meds
- Ro

Missed:

- Niagen Plus
- Rex MD
- Lifeforce

F2 should-hit holdouts recovered: 5 of 15.

Recovered:

- Amble
- Defy Medical
- Fridays
- Marek Health
- Maximus Tribe

Not recovered:

- AgelessRx
- Blokes
- BlueChew
- Geviti
- Invigor Medical
- Ivy Rx
- Kingsberg Medical
- Nurx
- ProHealth
- Rugiet Ready

## Feeder Notes

| Feeder | Holdout recall | Useful novelty | Notes |
| --- | ---: | ---: | --- |
| Category/listicle/direct SERP | 8/13 F3/F4; 5/15 F2 | medium | Best feeder. GLP-1, TRT, and HRT surfaces recovered most visible category brands. |
| Demand SERP | 4/13 F3/F4; 0/15 F2 | low | Added LifeMD and reinforced Hims/Ro/Noom; not enough incremental lift. |
| Exa `/search` | 0/13 F3/F4; 0/15 F2 | high but low-confidence | Returned mostly long-tail clinics / wellness operators; useful for candidate review, not recall. |
| Union | 9/13 F3/F4; 5/15 F2 | medium | Only +1 F3/F4 over the best single feeder. |

The union did not materially beat the best single feeder. Under the proposal gate, this should not pass.

WebSearch addendum note: direct WebSearch added One Medical, but did not recover Niagen Plus, Rex MD, or Lifeforce. It also did not improve F2 recall. See `websearch-addendum.md`.

## Pollution Gate

Brian-reviewed hard labels from `telehealth-human-review-queue.md` were applied before scoring:

- `worth_capture`: Ulo, Alloy Women's Health, Midi Health, Mochi Health, Eucalyptus Health.
- `tier_c_only`: RoenRx, MyStart, MangoRX, BrightMeds, G-Plans Direct, Evernow.
- `exclude`: Zealthy, FitRx, AMRx.
- unresolved / keep `unsure`: Juniper.

The gate caught a real issue: the GLP-1 SERP panel surfaced Zealthy's own list promoting Zealthy, RoenRx, and FitRx. Those must not land in Tier A/B.

After applying Brian labels, no `tier_c_only` or `exclude` item is eligible for Tier A/B.

## Interpretation

The validation failed for a useful reason: "DTC therapeutics brand" is too broad for four category queries. The query panel can recover GLP-1, TRT, and menopause/HRT heads, but it misses other F3/F4 shapes: NAD/longevity, primary care, ED, and healthspan/labs.

This argues against graduating a single broad `/cohort-discovery` verb from this packet. The next version should either:

- split telehealth into subcohorts before discovery, or
- generate query panels from anchor categories in the masked store baseline instead of using one broad cohort phrase.

Recommendation: revise/downscope; do not call this implemented.
