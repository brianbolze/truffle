# V3 comparison against Brian's ratings

Ground truth: Brian's Notion `Web design rating` (Organizations DB). Anazao (2) and Mills (4) were already in Notion; Infusive (2.5), Jinfiniti (3), and Kingsberg (2) were rated by Brian during this session, before he saw any agent output. Controls (Function 10, Amble 6, Belmar 4) carried over from v1/v2.

Bucket mapping (same as v1/v2): excellent ≈ 9–10 · strong ≈ 7–8 · solid ≈ 5–6 · basic ≈ 3–4 · weak ≈ 1–2.

| Company | Brian | Brian bucket | Blind median | Delta (buckets) |
|---|---:|---|---|---:|
| Function Health (control) | 10 | excellent | excellent | 0 |
| Amble (control) | 6 | solid | excellent | **+2** |
| Belmar Pharma (control) | 4 | basic | strong | **+2** |
| Mills Pharmacy | 4 | basic | strong | **+2** |
| Jinfiniti | 3 | basic | solid | +1 |
| Kingsberg Medical | 2 | weak | basic | +1 |
| AnazaoHealth | 2 | weak | basic | +1 |
| Infusive | 2.5 | weak/basic | strong | **+2.5** |

- **Exact bucket matches: 1/8** (Function). v1 and v2 were 6/9 each — on a top-heavy sample.
- **Severe misses (≥2 buckets): 4/8** (Amble, Belmar, Mills, Infusive). The declared pass bar was zero.
- **Direction: 23/24 individual ratings at or above Brian's bucket; 1/24 below** (sonnet's `strong` on Function). This is a systematic upward offset, not noise.
- **`weak` was never issued by any evaluator** — the floor of the scale went unused even on Brian-rated-2 sites.

## Model comparison (Opus vs Sonnet)

| Rater | Mean delta (buckets) | Note |
|---|---:|---|
| opus-a | +1.6 | gave the run's two `excellent` false positives (Amble, Infusive) |
| opus-b | +1.7 | |
| sonnet-a | +0.8 | at-or-below Opus on all 8; +1 on six companies, +2.5 on Infusive, −1 on Function |

Sonnet was uniformly ~1 bucket more conservative than Opus — which made it better calibrated on this bottom-heavy sample but undershot the one top control. Can't yet distinguish "better calibrated" from "biased lower in a direction that happened to fit this sample."
