# Screenshot capture findings: Function Health

Date: 2026-06-13

## Bottom line

The best workaround found so far is **real-browser viewport tiling after a warm scroll**.

For Function Health, this produced clean, inspectable homepage tiles where Firecrawl
full-page screenshots failed to render the hero and left some lower-page media
incomplete or black.

## What worked

Use the Codex in-app Browser, not Firecrawl screenshot capture:

1. Open `https://www.functionhealth.com/`.
2. Set viewport to `1920x1400`.
3. Wait for initial page load.
4. Dismiss the privacy notice.
5. Scroll top-to-bottom once to trigger lazy media.
6. Jump to deterministic scroll offsets.
7. Capture normal viewport screenshots at each offset.

The key is step 7: **capture viewport screenshots, not one full-page screenshot**.

Observed Function Health image loading:

- Before warm scroll: `7 / 35` images loaded.
- After warm scroll: `34 / 35` images loaded.
- The remaining unloaded image was a duplicate/secondary `GETLABS.png`; the hero,
  testing cards, chart, celebrity cards, testimonial video posters, doctor headshots,
  map, pricing card, and footer assets were visible.

## Evidence

Working viewport tiles:

- `raw/browser-captures/function-homepage-iab-desktop-viewport-tiles/`
- Manifest: `raw/browser-captures/function-homepage-iab-desktop-viewport-tiles/manifest.json`

Representative good tiles:

- `tile-00-y00000.png`: real hero media rendered.
- `tile-01-y01220.png`: "Testing is easy" cards and chart section rendered.
- `tile-03-y03660.png`: celebrity/media card grid rendered.
- `tile-04-y04880.png`: testimonial video poster cards rendered.
- `tile-06-y07320.png`: comparison table rendered.

Counterexample:

- `raw/browser-captures/function-homepage-iab-desktop-fullpage-after-scroll-BAD-repeats-hero.png`

That full-page browser screenshot repeated the hero visual down the page, so browser
full-page capture has the same class of compositing problem as Firecrawl, just with a
different failure mode.

## What failed or underperformed

Firecrawl full-page screenshots:

- Default, long wait, scroll/lazyload actions, enhanced proxy, mobile UA, and forced
  canvas visibility did not reliably recover the homepage hero.
- Firecrawl did capture static pages like Function pricing/scans well, so the failure
  appears tied to runtime media/compositing/lazy loading rather than ordinary image
  fetching.

Firecrawl poster injection:

- `homepage_inject_hero_poster.png` improved the hero by inserting a static poster.
- It is useful as a targeted patch, but it is site-specific and less general than
  viewport tiling.

Browser full-page capture:

- Not usable for Function homepage.
- It repeated the WebGL/video hero through the full-page screenshot.

Local Playwright/Chrome:

- A repeatable script was started at `raw/browser_viewport_capture.py`.
- In this sandbox, headless Chromium/Chrome failed at launch with a macOS Mach port
  permission error.
- The in-app Browser path remains the confirmed working route.

## Current caveats

- The in-app Browser screenshot API returned JPEG bytes despite `.png` filenames.
  Visually this is fine, but a productionized capture script should either normalize
  bytes to PNG or name files by actual MIME type.
- Sticky header and chat widgets remain visible in repeated tiles. This is acceptable
  for the current visual-quality experiment, but a cleaner pipeline could add an
  optional overlay cleanup step.
- Viewport tiling is not a literal full-page bitmap. It is better for evidence mining
  because each tile reflects what the real browser rendered at that scroll position.

## Recommendation

Use **Firecrawl for markdown, links, image inventories, and ordinary screenshots**.

Use **real-browser viewport tiling** as the escalation path when screenshot QA sees:

- blank/grey hero media,
- black video/image cards,
- incomplete lazy sections,
- repeated/composited full-page artifacts,
- WebGL/canvas/video-heavy marketing pages.

For this experiment, Function Health homepage should be eligible again if cited from
the viewport-tile capture set rather than from Firecrawl full-page screenshots.
