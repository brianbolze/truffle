# V5 worker protocol

Use only local screenshots and tiles listed in:

- `experiments/2026-06-13-visual-quality-v5-capture-clean-blind-judgment/cleaned-tile-manifest.md`
- `experiments/2026-06-13-visual-quality-v5-capture-clean-blind-judgment/cleaned-tile-manifest.json`

Do not read company dossiers, `profile.md`, Notion, live websites, Firecrawl outputs
outside the listed tiles, or prior scoring/evaluation files.

Do not infer from company reputation, business model, copy claims, SEO, funding,
or prior knowledge. Judge only the visible screenshots/tiles.

## Capture Rules

- Cite only active tile paths in the cleaned manifest.
- Do not cite `excluded_tiles`.
- Function Health homepage is available only through the listed browser viewport
  tiles. Do not use older Firecrawl homepage screenshots.
- If a visible issue looks like a cookie banner, modal, blank media, black card,
  or compositing artifact, mark it as a capture caveat and do not use it as design
  evidence unless the manifest says it is acceptable page chrome.

## Calibration

- Default down when uncertain.
- One visible tell per claim.
- Generic competence is common, not high quality.
- Distinctiveness is not maximalism.
- More design is not better design.
- Foundations are necessary but not sufficient.
- Genericness and broken fundamentals should cap top-end claims.
- Every claim must cite visible evidence.

## Evidence Card Format

Return 8-14 cards in YAML:

```yaml
cards:
  - family: typography_hierarchy
    polarity: strong | mixed | poor
    site: example.com
    page_or_region: "homepage hero / pricing cards / footer / etc"
    tile_path: "experiments/..."
    claim: "One calibrated sentence."
    visible_tells:
      - "Specific visual evidence."
      - "Specific visual evidence."
    contrast_with: "optional: site + tile path"
    confidence: high | medium | low
notes: |-
  Short note on what was easy/hard to detect from static tiles.
```

Usable cards are inspectable, specific, visual, and free of overall site scores.
