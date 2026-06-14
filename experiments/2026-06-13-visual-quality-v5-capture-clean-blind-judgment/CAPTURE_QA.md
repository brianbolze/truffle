# Capture QA

Date: 2026-06-13

## Bottom Line

The V5 active evidence set is usable after one tile exclusion.

- Worker-facing manifest: `cleaned-tile-manifest.md` / `cleaned-tile-manifest.json`
- Page overviews audited: 51
- Active tiles: 319
- Explicitly excluded tiles: 1
- New Firecrawl spend: none
- Live-web visual judgment: none

## QA Method

1. Started from the 2026-06-13 clean tile set.
2. Removed all reference-anchor and expected-quality notes from the worker manifest.
3. Restored Function Health homepage using the verified in-app browser viewport tiles,
   not the broken Firecrawl homepage screenshots.
4. Built a V5 overview contact sheet:
   `raw/overview-contact-sheet.png`
5. Visually checked known failure cases from prior capture work:
   Function homepage, Amble, Pepti, Belmar, Mills, Jinfiniti, Hallandale, and
   Infusive.

## Restorations

### Function Health Homepage

Status: `browser_viewport_restored`

Used:

- `experiments/2026-06-13-gpt55-visual-quality-examples/raw/browser-captures/function-homepage-iab-desktop-viewport-tiles/`
- `experiments/2026-06-13-visual-quality-v5-capture-clean-blind-judgment/raw/function-homepage-browser-viewport-overview-480w.png`

Decision:

- Include Function homepage in V5.
- Use only the verified browser viewport tiles.
- Do not use older Firecrawl homepage screenshots, which rendered the hero as a
  flat grey block.

Notes:

- Real hero media is visible.
- Lazy-loaded sections are materially present.
- Sticky header and chat widgets recur in the viewport tiles. This is acceptable
  for evidence mining as page chrome, but cards should not claim those widgets are
  capture failures.

## Exclusions

### Hallandale Homepage Tile 02

Excluded tile:

- `experiments/2026-06-13-gpt55-visual-quality-examples/tiles-clean/hallandalerx-com/homepage/tile-02-y02440.png`

Reason:

- Large blank grey media frame in the `Redefining quality` section.
- Treating it as visual-design evidence would risk scoring a capture/media load
  failure rather than the page.

Decision:

- Exclude this tile from the active tile list.
- Keep Hallandale homepage otherwise usable for hero, product, text, marquee, and
  footer evidence.
- Keep Hallandale products, quality, and new-provider pages active.

## Prior Recaptures Used

These were already cleaned in the 2026-06-13 run and are accepted in V5:

- Amble homepage and key pages: Transcend consent dismissed.
- Pepti homepage and key pages: cookie UI removed.
- Belmar homepage and key pages: CookieYes banner rejected.
- Mills homepage and key pages: newsletter/cookie overlays removed.

## Artifact Handling Decisions

- Jinfiniti purple promo/nav bars are visible sticky site chrome in the viewport
  tiles. They may be cited as visible page behavior only when they obscure or
  compete with content; do not call them screenshot corruption.
- Hallandale's oversized clipped marquee remains active. It appears as page
  presentation behavior rather than a failed media load.
- Small persistent widgets, such as chat/accessibility buttons and footer reCAPTCHA
  marks, are tolerated when they do not cover the inspected design region.
- No modal, cookie banner, newsletter overlay, black card, or full-page repeated-hero
  compositing artifact remains in the active evidence set.

## Result

Proceed to evidence mining and pruning using only paths in
`cleaned-tile-manifest.md`, plus the manifest's explicit exclusion note.
