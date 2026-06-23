# Telehealth SERP Intent Smoke

Date: 2026-06-08

This was a smoke test of `tools/serp_intent_panel.py`, not a traction or demand read. The panel
took a query set, cohort, and SerpAPI envelopes and produced comparable SERP-visibility evidence.

## What Worked

- Cold no-fetch run made missing captures explicit: 4/4 query rows returned `capture_status:
  "missing"` and `no_capture`.
- Live fetch filled all 4 captures and wrote the envelopes under `captures/`.
- Cached-only rerun worked without `--fetch-missing`.
- Repeatability check passed: ignoring expected run-provenance fields (`generated_at`,
  `fetch_missing`, `fetched_live_count`, `capture_status`, and cache path), live and cached evidence
  shapes matched.
- No schema drift was reported by `serpapi.py`.
- SerpAPI credits spent: 6 total.

## Post-Smoke Calibration

The first live/cached output showed two reusable-tool issues worth fixing before commit:

- AIO citations carried cohort evidence even when `ranked_brands` was empty, so the consumer now
  emits `ai_overview.reference_matches` separately from `ai_overview.ranked_brand_matches`.
- SERP-character heuristics were too broad for telehealth: ordinary words like "doctor," "provider,"
  "clinic," and "buy" made normal telehealth pages look local/retail-heavy. The consumer now uses
  tighter local/retail patterns and drives query labels from unmatched/off-cohort result character.

The cached-only calibrated rerun is saved as:

- `panel-calibrated.json`
- `panel-calibrated.md`

## Commands Run

```bash
python3 tools/serp_intent_panel.py --queries experiments/2026-06-08-serp-intent-telehealth-smoke/queries.json --cohort experiments/2026-06-08-serp-intent-telehealth-smoke/cohort.json --captures experiments/2026-06-08-serp-intent-telehealth-smoke/captures --format json > experiments/2026-06-08-serp-intent-telehealth-smoke/panel-missing.json

python3 tools/serp_intent_panel.py --queries experiments/2026-06-08-serp-intent-telehealth-smoke/queries.json --cohort experiments/2026-06-08-serp-intent-telehealth-smoke/cohort.json --captures experiments/2026-06-08-serp-intent-telehealth-smoke/captures --format markdown > experiments/2026-06-08-serp-intent-telehealth-smoke/panel-missing.md

python3 tools/serp_intent_panel.py --queries experiments/2026-06-08-serp-intent-telehealth-smoke/queries.json --cohort experiments/2026-06-08-serp-intent-telehealth-smoke/cohort.json --captures experiments/2026-06-08-serp-intent-telehealth-smoke/captures --fetch-missing --write-fetched-captures experiments/2026-06-08-serp-intent-telehealth-smoke/captures --format json > experiments/2026-06-08-serp-intent-telehealth-smoke/panel-live.json

python3 -c 'import json, sys; sys.path.insert(0, "tools"); from serp_intent_panel import render_markdown; panel=json.load(open("experiments/2026-06-08-serp-intent-telehealth-smoke/panel-live.json")); print(render_markdown(panel), end="")' > experiments/2026-06-08-serp-intent-telehealth-smoke/panel-live.md

python3 tools/serp_intent_panel.py --queries experiments/2026-06-08-serp-intent-telehealth-smoke/queries.json --cohort experiments/2026-06-08-serp-intent-telehealth-smoke/cohort.json --captures experiments/2026-06-08-serp-intent-telehealth-smoke/captures --format json > experiments/2026-06-08-serp-intent-telehealth-smoke/panel-cached.json

python3 tools/serp_intent_panel.py --queries experiments/2026-06-08-serp-intent-telehealth-smoke/queries.json --cohort experiments/2026-06-08-serp-intent-telehealth-smoke/cohort.json --captures experiments/2026-06-08-serp-intent-telehealth-smoke/captures --format markdown > experiments/2026-06-08-serp-intent-telehealth-smoke/panel-cached.md
```

## Query Read

The calibrated run gives a sharper split than the initial smoke. This is SERP visibility only.

| Query | SERP-visibility read |
|---|---|
| `TRT online prescription` | Worth tracking cautiously. Own-page hits for Hims, Hone Health, and TRT Nation; third-party mentions for Peter MD and Hone Health; AIO references cited Hims, Hone Health, and TRT Nation. Still listicle-heavy/noisy. |
| `sermorelin online prescription` | Best clean candidate in this smoke. Five own-page matches across AgelessRx, Strut, HydraMed, and Hone Health; AIO references cited AgelessRx, Hone Health, and Strut. |
| `compounded tirzepatide online` | Worth tracking cautiously for GLP-1 visibility, but noisy. Own-page matches for Brello and Ivim; third-party mentions for Ro and Brello; AIO references cited Brello and Ivim. |
| `NAD injection online` | Noisiest candidate. Own-page matches for AgelessRx, Hone Health, and HydraMed; AIO references cited Hone Health and AgelessRx; high off-cohort count suggests reformulation before treating it as stable. |

AI Overview was present for every query. None produced parser-recognized `ranked_brands`, but AIO
references did carry cohort evidence after the calibration patch.

## Out Of Scope

- No market share, demand, spend, conversion, or traction inference.
- No blended score.
- No edits to `tools/serpapi.py`.
- No writes to Notion, Linear, or Teleprescribe project files.
- No commit.
