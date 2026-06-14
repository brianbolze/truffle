# GPT-5.5 visual-quality evidence protocol

You are mining evidence cards from cached website screenshots. Your job is to find
specific examples, not to rate whole sites.

## Hard boundaries

- Use only screenshots/tiles listed in `tile-manifest.md` or `tile-manifest.json`.
- Use the current clean manifest, whose tile paths are under `tiles-clean/`.
- Function Health's homepage is intentionally excluded: Firecrawl rendered its live
  hero media as a flat grey block after multiple recapture attempts. Do not infer
  anything about Function's homepage hero from older tiles or raw screenshots.
- Do not read `store/<slug>/profile.md`.
- Do not use live web, Notion, Firecrawl, company reputation, SEO, tech stack, or
  prior knowledge.
- Do not output a whole-site tier, score, ranking, or verdict unless explicitly
  asked by the lead agent.

## Calibration spine

Use these parts of PQR v1:

- **Default down.** Between two interpretations, choose the less flattering one.
- **One visible tell per claim.** If you cannot point to a tile and a region, do not
  make the claim.
- **Generic is common.** Clean, competent, forgettable template execution is not a
  strong example.
- **Distinctiveness is not maximalism.** Judge ownership and craft, not how much is
  happening.
- **More design is not better design.** Busy or effortful pages can still be generic.
- **Craft and finish matter.** Zoom-level inconsistencies, mismatched icon styles,
  bad crops, weak type rhythm, and template seams are real evidence.

## Evidence families

The lead agent will assign one or more of these:

- `iconography_illustration`
- `typography_hierarchy`
- `layout_composition_components`
- `color_brand_imagery`

## Evidence card format

Return 8-14 cards. Balance strong, poor, and mixed examples. Prefer contrast pairs
where a strong and poor example illuminate the same visual dimension.

```yaml
- family: typography_hierarchy
  polarity: strong | poor | mixed
  site: example.com
  page_or_region: "homepage hero / pricing cards / footer / etc"
  tile_path: "experiments/..."
  claim: "One sentence, calibrated and concrete."
  visible_tells:
    - "Specific visual evidence."
    - "Specific visual evidence."
  contrast_with: "optional: site + tile path"
  confidence: high | medium | low
```

## What makes a card usable

- The claim can be checked by opening the cited tile.
- The visible tells are about design craft, not business quality.
- The card avoids vague adjectives unless they are backed by specifics.
- Poor examples do not get softened because the site is functional or coherent.
- Strong examples are genuinely strong, not merely acceptable.

## Suggested workflow

1. Open `tile-manifest.md` for the cohort.
2. Use overview images to choose promising pages.
3. Inspect native tiles for detail-level evidence.
4. Mine cards across the assigned family.
5. End with a short note: what the family was easy/hard to detect from static tiles.
