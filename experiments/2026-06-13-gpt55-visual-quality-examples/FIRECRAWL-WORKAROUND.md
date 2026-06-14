# Firecrawl Screenshot Workaround - Function Health

Date: 2026-06-13

## Bottom Line

Function's homepage hero is recoverable for visual-reference screenshots, but not by
waiting, scrolling, mobile emulation, or enhanced proxy.

The failure is the hero's WebGL/canvas path. Firecrawl renders the page with the
hero canvas hidden and blank:

- `canvas.flute-canvas.is-hidden`
- `opacity: 0; visibility: hidden; display: none`
- `/interact` diagnostics reported `webgl: false`

The working workaround is to use Firecrawl scrape `actions` to inject Function's own
declared hero poster image when that canvas is hidden, then scroll bottom/top before
the final full-page screenshot.

This is a patched capture. Label it as such. It is good enough for visual-quality
reference work, but it is not a pristine screenshot of Firecrawl's unmodified browser
render.

Firecrawl support independently confirmed the same root cause: their rendering
browser does not expose WebGL, so Function's `flutieHero` module cannot initialize.
They recommended `metadata.ogImage` as the clean one-call stand-in. That is a useful
fallback, but it is a social/share image, not the live page's hero media layer.
For screenshot-fidelity work, the hero manifest poster is closer because it sits
behind the page's real nav/copy/CTA instead of replacing the hero with a separate
Open Graph composition.

## What Worked

Desktop action:

- Action file: `raw/actions/function-inject-hero-poster.json`
- Output: `store/functionhealth-com/captures/2026-06-13/.payloads/homepage_inject_hero_poster.png`
- Size: `1920x11930`
- Result: hero media present; lower testimonial/chart sections render normally.

Mobile action:

- Action file: `raw/actions/function-mobile-inject-hero-poster.json`
- Output: `store/functionhealth-com/captures/2026-06-13/.payloads/homepage_mobile_inject_hero_poster.png`
- Size: `360x13820`
- Result: hero media present in mobile layout; lower sections render normally.

The injected assets are Function's own first hero poster URLs from:

- `https://pm3i9nzo0jeqag2m.public.blob.vercel-storage.com/lucid/hero/manifest.json`

The Firecrawl `metadata.ogImage` fallback is:

- `https://cdn.prod.website-files.com/68823b2fd9cc28b78fb3ee65/6917a20e06dfd004f71f8f66_Open%20Graph_alt.png`

## What Did Not Work

- Long wait: `homepage_wait30`
- Lazy-load scroll actions: `homepage_lazyload`
- Enhanced proxy plus lazy-load actions: `homepage_enhanced_lazyload`
- Mobile emulation plus iPhone UA and lazy-load actions: `homepage_mobile_lazyload`
- Forcing the canvas visible: `homepage_force_canvas_visible`

The force-visible probe proved the canvas itself had no useful pixels. It changed
visibility state but still produced a blank/washed hero.

## Interact Probe

`/interact` was useful for diagnosis, not for the full-page workaround.

- First interact attempt against the plain homepage scrape timed out and then reused
  a wedged live browser session on retry.
- A second inspect-only interact probe against the fixed scrape succeeded:
  `raw/function-interact-fixed-inspect.json`
- It confirmed:
  - `webgl: false`
  - hidden canvas state persisted
  - testimonial videos were loaded with `readyState: 4`
  - the injected hero poster was loaded at `1920x1080`

So the defect is not a blanket media/video loading failure. It is specifically the
WebGL/canvas hero renderer.

## Spend

Attributable scrape spend added by this follow-up: 3 credits.

The June 13 Function scrape manifest totals 8 scrape credits including earlier
attempts. Remaining credits were observed at 2085 before the follow-up and 2073
after interact testing; `/interact` responses did not include per-call `creditsUsed`,
so treat that global delta as an observed session delta, not attribution-grade
accounting.

## Recommended Recipe

For Function-style failures:

1. Run normal screenshot QA first.
2. If the hero is blank, inspect `rawHtml` for a hidden canvas and a manifest URL.
3. Use a scrape `executeJavascript` action to inject the site's own poster image
   behind the hero copy when the canvas is hidden.
4. Scroll to bottom, wait, scroll back to top, wait, then take the final full-page
   screenshot.
5. Keep the output labeled as a patched visual-reference capture.
