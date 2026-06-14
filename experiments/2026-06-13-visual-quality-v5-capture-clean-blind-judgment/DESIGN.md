# V5 capture-clean evidence to blind judgment calibration

Date: 2026-06-13

## Objective

Test whether the 2026-06-13 evidence-mining run can become a reusable visual-quality
module, without leaking Brian/reference quality labels into evidence mining,
evidence pruning, or blind scoring.

This is not a fresh live-web audit. Visual judgment uses only local screenshots and
tiles after capture QA.

## Cohort

Same 13-site cohort as the 2026-06-13 visual-quality example experiment:

- Function Health
- Ro
- Nurx
- Hallandale
- Geviti
- Amble
- Pepti
- Belmar
- Mills
- Jinfiniti
- Kingsberg
- Anazao
- Infusive

The worker-facing manifest removes anchor notes, Brian ratings, expected quality
bands, and prior evaluation labels.

## Evidence Rules

- Screenshot health is phase 1, not cleanup after judgment.
- Use Firecrawl-derived clean tiles where they pass QA.
- Escalate to browser viewport tiles when Firecrawl screenshots show grey/blank
  hero media, black cards, modal/cookie contamination, lazy-load failures, or
  full-page compositing artifacts.
- Restore Function Health homepage only from the verified in-app browser viewport
  tile set:
  `experiments/2026-06-13-gpt55-visual-quality-examples/raw/browser-captures/function-homepage-iab-desktop-viewport-tiles/`
- Do not use `profile.md`, company dossiers, live websites, Notion, or current web
  pages for visual judgment.
- Every claim needs one visible tell and a cited tile path.

## Workflow

1. Build a cleaned blinded tile manifest.
2. Audit screenshot health and mark pages as clean, restored, degraded, or excluded.
3. Mine evidence cards by family:
   - typography / hierarchy
   - layout / composition / component finish
   - color / brand system / imagery
   - iconography / illustration / product graphics
4. Judge/prune the evidence cards:
   - reject weak, vague, duplicate, or artifact-derived claims
   - merge overlapping cards
   - preserve visible evidence and polarity
5. Produce blind PQR-lite site-level dimension scores only from cleaned screenshots
   and pruned evidence.
6. Lead session compares the blind output to hidden/reference anchors post-hoc.

## PQR-Lite Scoring

Dimensions use a 1-5 scale:

- `typography_hierarchy`
- `layout_components`
- `color_brand_imagery`
- `iconography_graphics`
- `overall_visual_quality`

Calibration:

- Default down.
- Generic competence is common, not high quality.
- Distinctiveness is not maximalism.
- More design is not better design.
- Foundations are necessary but not sufficient.
- Genericness and broken fundamentals cap top-end scores.
- Every score needs visible evidence.

## Pass Bar

The system is not ready to graduate unless:

- Active screenshots are clean or explicitly excluded.
- Function homepage is restored only from verified viewport tiles.
- Every score cites visible evidence.
- Generic-but-polished sites are not overrewarded.
- Ambitious-but-inconsistent sites are not overrewarded.
- Scoring and ranking are produced blind.
- Post-hoc evaluation shows useful agreement with Brian/reference anchors or explains
  disagreement using visible evidence.

## Decision Options

Final synthesis must choose one:

1. Graduate as a visual evidence-mining module only.
2. Graduate as a blind PQR-lite scoring module only.
3. Graduate both.
4. Graduate neither yet.
