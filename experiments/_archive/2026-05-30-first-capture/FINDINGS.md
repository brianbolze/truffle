# Findings — first end-to-end capture (linear.app)

> **Verdict: the lifecycle holds, and the SCHEMA fits a clean B2B SaaS with almost no friction.** A single rich homepage pass + map carried ~80% of the profile; the screenshot is load-bearing (pricing, logo wall, color scheme); and three real capture hazards surfaced that the eventual verb must defend against — chiefly *response/URL contamination*, *JS-walled pricing*, and *client-rendered nav/flyouts*. Deliberately a different shape than the telehealth corpus, and it generalized.

Run: hand-capture of `linear.app`, 2026-05-30. Raw payloads + screenshots in `store/linear-app/captures/2026-05-30/.payloads/`; cleaned page markdown alongside; profile at `store/linear-app/profile.md`.

## What worked

- **Map + homepage in parallel is the right spine.** `/v2/map` returned **149 URLs each with `{url, title, description}`** — rich enough to pick key pages *without* scraping them first (e.g. `/customers/scale` → "compressed bug resolution time by 52%"). The homepage full pass (`onlyMainContent:false`, 16.9 KB markdown) alone yielded the hero, all five product surfaces, the changelog, testimonials, the "33,000 teams" claim, and the complete footer.
- **The footer is the reliable nav source.** Linear's top-bar mega-menu ("Product"/"Resources") is client-rendered and absent from markdown, but the footer carried the full IA — enough to reconstruct a complete `## Nav structure`.
- **Screenshots downloaded cleanly** (Python `urlretrieve`; object-form `{"type":"screenshot","fullPage":true}` → URL, as INVARIANTS predicted) and were *decisive*: they gave the verified `color_scheme: dark`, the four pricing tiers + amounts, and the logo wall (Vercel, Cursor, OpenAI, Coinbase, Cash App, Ramp…).
- **SCHEMA classification was unambiguous** for a clean SaaS: `B2B` / `Software / SaaS` / `Subscription` / `Technology` all had exact-fit closed-set values — **zero `Other` needed.** The "describe the company, not what it means to you" line held: nothing tempted a vertical/judgment field.

## Where the SCHEMA fit — and where it fought

- **Fit:** identity, capture-meta, description, classification, nav, credibility — all natural. `description` at ~210 chars wanted the full budget but landed.
- **`is_multi_product` is genuinely ambiguous for a unified-but-multi-surface product.** Linear is one app with five first-class surfaces (Intake/Plan/Build/Diffs/Monitor) + cross-cutting features (Asks, Agents, Insights…), one per-seat price. Resolved `false` via the Notion precedent already in TAXONOMIES — but that precedent is doing real work, and this will recur for every platform product. **SCHEMA should keep/strengthen that tie-breaker.**
- **The visual-identity block assumes `branding` is present — and it must be requested explicitly.** I omitted `branding` from the first homepage pass and got nothing, costing a re-scrape. Once requested it's **rich and accurate**: `colorScheme: dark`, fonts (Inter/SF Pro Display), full color set, typography, spacing, even component styles. Three real quirks to encode: (a) `branding.colors.primary` is the dominant **text** color (`#D0D6E0`), *not* the brand hue — the brand hue is `accent` (`#5E6AD2`); a "copy, don't analyze" reader will mislabel it, so the verb should prefer `accent` for "brand color." (b) `branding.images.logo` returns the wordmark as an **inline data-URI SVG**, not a hostable URL — so a `logo_url` still needs a fallback chain (favicon → og:image → empty). (c) `branding.designSystem.framework` said `"custom"` though the site is plainly Next.js (`__NEXT_DATA__` in rawHtml) — trust rawHtml for framework, not branding.
- **`key_pages` (flat dict) undersells a surface-rich product.** It worked, but a SaaS with 5 "surface" pages *and* a parallel feature-page set wanted a hint of structure (surfaces vs. features). Not worth a schema change yet — flag only.
- **No home for pricing tiers without `offerings.md`.** I parked verbatim tiers in "How it works / model." Fine, but for SaaS the pricing table is core signal — argues `offerings.md` (or a small pricing block) earns its place early for software companies.

## What was awkward (capture mechanics — the useful part)

1. **JS-walled pricing.** The pricing **$ values are not in the markdown** — the price node renders as a scrambler artifact (`$01234567890123456789…`). Recovered cleanly from the **screenshot** and from an **html-format** scrape (`$10` Basic, `$16` Business, billed yearly). The verb must screenshot pricing *and* pull html — **in the same call** (I split them and wasted a credit; formats ride free on one credit).
2. **Cross-response contamination (new hazard).** One `/features` scrape returned **`/about` content** — `data.metadata.sourceURL` said `/about` despite the requested URL. A re-scrape fixed it. competitor-watch's INVARIANTS don't cover this. **New invariant: verify `metadata.sourceURL` (or `url`) matches the requested path on every response; re-scrape on mismatch.**
3. **Redirect-equivalent + login-wall URLs.** `/product` and `/features` resolve to the same Features page; bare `/product` returned the **login wall** (217-char markdown). **The verb must treat thin markdown (<~500 chars or login markers) as a failed page** and dedupe redirect-equivalent URLs by resolved `sourceURL`.
4. **Client-rendered content pages scrape thin.** `/method` (the "Linear Method" manifesto) came back ~1 KB — mostly client-rendered. Needs a longer `waitFor` or a screenshot fallback for content-heavy marketing pages.
5. **iCloud read-after-write lag.** The store lives in iCloud Drive; rapid read-after-write on `.payloads/` was racy. Prefer **write to local scratch → persist to the iCloud store**, or tolerate lag explicitly. (`.gitignore` already excludes `**/.payloads/` — good.)

## Firecrawl credits

- **This probe: ~14 calls** (1 map + 13 scrapes), inflated by learning: the contamination re-scrape, the `/product` dead-ends, the forgotten-`branding` re-scrape, and the split pricing screenshot/html call.
- **A codified clean run ≈ 9–10 credits:** 1 map + 1 homepage (markdown+html+rawHtml+links+branding+screenshot, all on **one** credit) + ~7 key pages (markdown+links+screenshot each, 1 credit each).
- **All formats ride free on the 1-credit/page base** — request them together, never split to "save credits."

## What the eventual `/research-company` verb must handle

1. **Always request `branding` + `rawHtml` on the homepage pass.** Don't trust format defaults.
2. **Verify `sourceURL` == requested path per response; re-scrape on mismatch; dedupe redirect-equivalents** by resolved URL.
3. **Pricing = one call with markdown + links + html + screenshot.** Parse `$` from html/screenshot, never markdown.
4. **Reconstruct nav from footer + map** when the mega-nav is client-rendered; don't trust top-bar markdown.
5. **Thin-markdown guard:** `<~500` chars or login-wall markers ⇒ failed page ⇒ retry with longer `waitFor` or screenshot fallback.
6. **Logo fallback chain** (above). Treat the **screenshot as required** for SaaS, not optional — it carries pricing, logos, and color scheme.
7. **`is_multi_product` tie-breaker** for unified-multi-surface products (keep the Notion precedent explicit).
8. **Persist payloads via local scratch → iCloud** to dodge read-after-write lag.

## Caveats

- Single fixture (one clean SaaS), hand-run. The contamination hazard (#2) was observed once — worth watching whether it recurs or was transient Firecrawl flakiness.
- The probe ran in a session with severe tool-output display buffering (results flushed in big delayed batches). It didn't corrupt any data — every payload was re-verified from disk — but it slowed verification and is why the run took more passes than a clean codified verb would. Practical implication for the verb's own testing: prefer direct-stdout checks and write-then-read patterns, and expect iCloud read-after-write lag.
