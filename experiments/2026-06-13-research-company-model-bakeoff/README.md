# /research-company model bakeoff

Date: 2026-06-13

## Objective

Compare Claude Opus 4.8-style `/research-company` output against GPT-5.5 output on the part of the workflow where model judgment matters: evidence selection, schema-faithful synthesis, and downstream usefulness.

This is not a live-scrape race by default. V1 freezes evidence from existing captures so both models see the same pages, screenshots, payload hints, schema docs, and module contracts.

## Frame

Question: given the same captured company-site evidence, which model produces the more trustworthy and useful store artifact?

Primary artifacts:

- `profile.md`
- `offerings.md` when the sample asks for per-SKU grain
- `telehealth.md` when the sample is in the telehealth cohort

Non-goals:

- proving which model browses better
- comparing old historical Claude profiles against fresh GPT outputs
- measuring live-site drift, Firecrawl failures, or cookie-overlay handling in the main score
- promoting any candidate output into `store/` before blind review

## Method

1. Build frozen evidence packets under `_out/packets/<sample_id>/`.
2. Run each model against the packet protocol, writing candidates under `_out/<model>/<sample_id>/`.
3. Run mechanical checks where possible.
4. Blind-review `Model A` vs `Model B` with `RUBRIC.md`.
5. Run a downstream query test that answers practical questions from each candidate only.

## Sample

The V1 sample is intentionally small and mixed:

- direct-to-consumer telehealth brands with `profile + offerings + telehealth`
- pharmacy / healthcare operators where the model must avoid overfitting to telehealth
- non-health controls with very different portfolio shapes

The exact sample lives in `sample.json`.

## Current Run State

- Scaffold: ready.
- Packet builder: `scripts/build_packets.py`.
- Frozen packets: built under `_out/packets/`.
- Logo evidence: added to every packet under `logos/`; `logos:{}` is now a required profile module.
- GPT-5.5 candidate outputs: original V1 pass complete under `_out/gpt55/`, but superseded for final comparison until rerun/patched with the required logo module; see `GPT55_RUN_LOG.md`.
- Blind review: pending until comparable Claude candidates are generated or selected.

## Files

- `sample.json` - fixed V1 company sample and requested output modules.
- `RUN_PROTOCOL.md` - instructions for a model generating candidate dossiers.
- `RUBRIC.md` - blind scoring rubric and hard penalties.
- `DOWNSTREAM_QUERY_TEST.md` - consumer-side usefulness test.
- `scripts/build_packets.py` - deterministic packet builder from cached captures.
