---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: warbyparker.com
name: Warby Parker
aliases: []
parent: []
owns: []
socials:
  instagram: https://www.instagram.com/warbyparker/
  tiktok: https://www.tiktok.com/@warbyparker
  youtube: https://www.youtube.com/warbyparker/
  x: https://twitter.com/warbyparker
  facebook: https://www.facebook.com/warbyparker
external: {}                          # JSON-LD sameAs carried only operated channels — no third-party records (crunchbase/wikipedia/etc.) declared

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Next.js storefront (rawHtml /_next/; ignore branding designSystem 'custom'). Catalog shape — the /map returns ~466 URLs, ~90% individual /eyeglasses|/sunglasses|/contacts|/accessories PDPs; select pages from homepage links, not the map. No /pricing page — house frames are flat-priced ($95, some $145) on the category pages. Mega-nav flyouts are client-rendered (header buttons fire aria-controls='modal-desktop'; sub-items not in markdown) — reconstruct nav from footer + screenshot. /overview is a dead 404 (153c). Eye exams have no clean top-level URL — booking lives at /appointments/eye-exams/booking. PDP hero renders lazy-load (img.warbyparker.com/AIR_ASSETS came back blank; i.warbycdn.com /s/f/ are color swatches, /s/c/ are try-on crops) — clean frame renders were cropped from the PDP full-page screenshots. Impact 'pairs distributed' counter flickers across pages/renders (15M/20M on /history, 25M on /buy-a-pair-give-a-pair)."
key_pages:
  eyeglasses: /eyeglasses
  sunglasses: /sunglasses
  contacts: /contacts
  insurance: /insurance
  intelligent_eyewear: /intelligent-eyewear
  history: /history
  buy_a_pair_give_a_pair: /buy-a-pair-give-a-pair
  retail: /retail
  eye_exam_booking: /appointments/eye-exams/booking
unverified_fields:
  - "Retail store count — /retail is a locator (lists individual stores, links to stores.warbyparker.com); no national total is stated on captured pages."
  - "Per-box contacts prices and the eye-exam fee — behind brand/Rx selection and the booking flow; not shown on captured category pages (only avg-savings figures: glasses $100, contacts $115, exams $40)."
  - "Impact counter is a point-in-time snapshot, not fixed — 'pairs distributed' renders as 15M and 20M on /history and 25M on /buy-a-pair-give-a-pair; reported the discrepancy rather than picking one."
  - "Home Try-On appears to be ending — the /eyeglasses FAQ carries the question 'Why is Warby Parker ending the Home Try-On program?' but the answer is collapsed/client-rendered and was not captured."

# Description — one sentence (~160-220 chars)
description: "A direct-to-consumer eyewear brand that designs prescription glasses and sunglasses in-house, selling online, by app, and in its own stores — frames from $95 including lenses, plus resold contacts and in-store eye exams."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2C]
offering_category: [Physical Products / Hardware, Services / Consulting]   # primary: in-house-designed eyewear (maker → not Retail/E-Commerce; its stores are a channel). secondary: in-store optometry / eye exams. Contacts is a resold line (noted in body), not elevated to a category.
portfolio_shape: Catalog                # hundreds of frame styles, un-enumerable — capture shape + exemplars (see offerings.md)
business_model: Transactional / One-time   # buy a pair; no membership/subscription
primary_industry: Retail & E-Commerce      # DTC consumer eyewear retail (healthcare-adjacent via optometry + Rx lenses; consumer-retail is the operating sector)

# Visual identity — branding payload is a hint, verified against the screenshot
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 195, h: 16 }                                                              # extracted inline brand <svg> (the "WARBY PARKER" wordmark); recolored from the captured white header variant to brand navy #072369 for usability (geometry untouched)
  logomark: { src: "https://www.google.com/s2/favicons?domain=warbyparker.com&sz=256", px: 180, transparent: false }  # white "WP" on an opaque bright-blue square (baked background)
  og:       { src: "https://img.warbyparker.com/24.04.09.SummerCore/Homepage/ladybug.png?originWidth=2880&originHeight=1320", w: 2880, h: 1320 }   # declared og:image — a summer-campaign lifestyle shot (gold cat-eye on a leaf), not a branded cover
brand_colors: { primary: "#072369", accent: "#1050D0" }   # deep navy primary (top bar, headlines), bright blue accent (CTAs/links); confirmed on the homepage screenshot
fonts: [ABC Social, Ivory]              # branding.fonts (fontAbcSocial / fontIvoryLl); ABC Social sans for UI/body
color_scheme: light
design_framework: next.js              # rawHtml /_next/ (NOT branding.designSystem, which read 'custom')
---

## Overview

Warby Parker is a direct-to-consumer eyewear company that designs its own prescription **glasses and sunglasses in-house** and sells them online, through its iOS app, and across its own retail stores. Founded in 2010 by four Wharton classmates (Neil Blumenthal, Andrew Hunt, David Gilboa, Jeffrey Raider) after one lost his glasses and balked at the replacement cost, the company's founding thesis is explicit on `/history`: the eyewear industry "is dominated by a single company that has been able to keep prices artificially high," so Warby "circumvent[s] traditional channels, design[s] glasses in-house, and engag[es] with customers directly" to sell at "a fraction of the going price." The result is a flat, legible price: **most frames are $95 including prescription lenses** (with scratch-resistant and anti-reflective coatings at no extra cost). It added **contacts** in fall 2019 and now also runs **in-store eye exams**, vision-insurance processing, and a virtual prescription-renewal test.

## What they offer

Breadth across the lines (per-line price-visibility token; verbatim prices where shown). Per-SKU/exemplar depth lives in [`offerings.md`](offerings.md) — the catalog is hundreds of styles, so this is the shape:

- **Eyeglasses:** in-house-designed prescription frames — **"Starting at $95, including prescription lenses with scratch-resistant, anti-reflective coatings"**; premium styles **$145** (e.g. Melva) `[published]`
- **Sunglasses:** same frame catalog with tinted/prescription lenses — from **$95** `[published]`
- **Lens options (any frame):** Single-vision (incl. at $95), Progressives, Blue-light, Light-responsive (photochromic), Anti-fatigue; polycarbonate lenses + coatings included `[published]`
- **Contacts:** a **resold** range of major third-party brands (Acuvue, Air Optix, Biofinity, Biotrue, Dailies, Clariti, MyDay, Precision7, Avaira, Total30…) **plus Warby's own brand, Scout by Warby Parker** (90-packs); per-box price is behind brand/Rx selection `[on-request]`
- **Eye exams:** comprehensive exams "at most of our stores," booked at `/appointments/eye-exams/booking`; price not shown ("Save $40 on average") `[on-request]`
- **Intelligent Eyewear:** forthcoming **AI smart glasses** built with **Google** (AI) and **Samsung** (hardware), shown at Google I/O 2026, "launching this fall"; sign-up only, no price `[on-request]`
- **Accessories:** cases, chains, clip-ons, lens kits (noted from nav/footer; not separately captured)

> Note on classification: Warby is a *maker* of eyewear (frames designed in-house), so its own stores are a channel, not a "Retail / E-Commerce" business; the genuine second category is the **eye-care service** layer (optometry/exams). The **contacts** line is true reselling of other brands' products — a real hybrid wrinkle, captured here rather than as a third category tag.

## How it works / model

Customer journey: **discover** (browse online/app, a Style Quiz, or virtual try-on in the Advisor app) → **get a prescription** (bring your own, renew via the virtual vision test, or book an in-store eye exam) → **buy** (online, in app, or in store) → frames ship free with a **free 30-day return** window. Warby makes money on **one-time product sales** (no membership/subscription); the flat $95 frame price is the anchor. Vertical integration — in-house design + direct sales + owned stores + owned optometry — is the cost lever that funds the low price. **Omnichannel:** a large U.S. retail fleet (store locator at `/retail`; also Canada) layered on the e-commerce core, with most eye exams performed in those stores.

**Insurance & payment (a distinctive operational layer):** Warby accepts vision insurance directly — an instant in-checkout benefit check, automatic application when in-network, and out-of-network reimbursement support; **FSA/HSA accepted.** It is "in-network with most major vision carriers" (UnitedHealthcare, Spectera, Davis Vision, Superior Vision, MetLife Vision, FEP Vision, CareFirst, Guardian Vision, Community Eye Care; Eyemed/Cigna noted separately). Claimed average savings: **glasses ~$100, contacts ~$115, eye exams ~$40.**

## Positioning & audience

Mass-market consumers who want **design-forward eyewear without the markup** — positioned against the (unnamed, but clearly Luxottica) incumbent that "keep[s] prices artificially high." The pitch braids three things: a **single transparent price** ($95, lenses included), a **design/quality** story ("higher-quality, better-looking… at a fraction of the going price"; a "Designed in New York, made in Italy" Tratto capsule), and a **social mission** (Buy a Pair, Give a Pair). Tone is friendly and editorial ("buying glasses should be easy and fun… leave you happy and good-looking, with money in your pocket").

## Nav structure

Top nav (header) — flyout sub-menus are client-rendered and were not captured in full; sub-links below are recovered from on-page links + footer:

```
- Eyeglasses — /eyeglasses
  - Lenses guide — /eyeglasses/lenses
  - Progressives — /eyeglasses/progressives
  - Blue-light — /eyeglasses/blue-light
  - Light-responsive — /eyeglasses/light-responsive
  - Anti-fatigue — /eyeglasses/anti-fatigue-lenses
  - Shop $95 frames — /eyeglasses?prices=95
- Sunglasses — /sunglasses
  - Lenses guide — /sunglasses/lenses
- Contacts — /contacts
- Eye exams — /appointments/eye-exams/booking
- Insurance — /insurance
  - Flexible spending (FSA/HSA) — /flexible-spending-accounts
- Accessories — /accessories
- Style quiz — /quiz/frames
- Intelligent Eyewear — /intelligent-eyewear
```

Footer groups (selected): **Shop** (Eyeglasses, Sunglasses, Contacts, Accessories, New collections, Gift cards, Add a pair and save); **Learn/help** (Eyewear A to Z `/learn`, Eyeglasses/Sunglasses lens guides, Measure your PD, Renew a prescription `/virtual-vision-test`, Find a location `/retail`, FAQ `/help`, Customer reviews); **Company** (Our story `/history`, How our glasses are made, Impact `/impact-report`, Buy a Pair Give a Pair, Jobs); **Apps** (Advisor / iOS app, Virtual Try-On); legal + country switch (USA/Canada).

## Credibility & proof

- **Social mission — Buy a Pair, Give a Pair:** 1-for-1 — "for every pair… purchased, a pair of glasses is distributed to someone in need." Self-reported impact: **"Over 25 million pairs distributed"** on `/buy-a-pair-give-a-pair` (note: `/history` rendered "over 15 million" and "over 20 million" in the same capture — figure flagged as a moving/inconsistent counter). Reach "over 80 countries… over 40 cities in the United States." Partner: VisionSpring.
- **Pupils Project (2015):** school-based vision program — "over 350,000 pairs… to students across the country"; partnership messaging with **Bloomberg Philanthropies**.
- **Cited third-party research (verbatim, on `/buy-a-pair-give-a-pair`):** reading glasses "can increase productivity by up to 32% and boost income by 33%" (source: VisionSpring); a 2021 *JAMA Ophthalmology* / Johns Hopkins Wilmer study found students who received glasses gained "two to four months of education." (Claims attributed to named sources, not Warby's own data.)
- **Product ratings (self-reported, per-PDP):** e.g. Durand **4.5★ (326)**, Percey **4.5★ (307)**.
- **Guarantees:** free shipping, **free 30-day returns**, free scratched-lens replacement; 30-day free-return window also in JSON-LD.
- **HQ / contact (JSON-LD):** 233 Spring St, New York, NY 10013; customer service 888-492-7297.

## Visual & brand impression

Confident, premium-but-accessible DTC design. A **deep navy** (`#072369`) utility bar carries the centered white "WARBY PARKER" wordmark; the body is bright and white-heavy with **bright-blue** (`#1050D0`) CTAs and links. Large display headlines ("SEE SUMMER BETTER") sit over editorial product-and-lifestyle photography — frames shot cleanly on warm seasonal backdrops (a green leaf, soft pink), human portraits in glasses, and a "Warby Parker in the wild" UGC strip. The overall feel is editorial, calm, and design-led — the look of a brand selling taste and value rather than discount. Typography pairs a clean grotesque (ABC Social) for UI with a display face (Ivory) for headlines.

## Strategic read

- **Vertical integration is the moat and the price story** — design + DTC + owned stores + owned optometry is what makes "$95, lenses included" sustainable, and it's the explicit anti-Luxottica wedge from day one.
- **Two live shifts worth watching:** (1) **Intelligent Eyewear** — a Google/Samsung AI-glasses partnership ("launching this fall") pushes Warby from corrective eyewear toward the smart-glasses category, a category-redefining bet; (2) **Home Try-On appears to be ending** — the classic 5-frames-mailed-home program that built the brand is referenced in the FAQ as being discontinued (answer not captured), suggesting the funnel has shifted to virtual try-on (Advisor app) + the now-large store fleet.
- **Insurance handling is an underrated DTC unlock** — instant benefit check + auto-applied in-network coverage + FSA/HSA removes the friction that usually keeps insured shoppers in legacy optical chains.

## Provenance

- **Pages (12 analyzed, firecrawl):** homepage, `/eyeglasses`, `/sunglasses`, `/contacts` (the three category backbones, captured rich for the offerings prominence read), `/insurance`, `/intelligent-eyewear`, `/history`, `/buy-a-pair-give-a-pair`, `/retail`, plus 3 flagship PDPs (`/eyeglasses/durand/whiskey-tortoise`, `/eyeglasses/percey/chestnut-crystal`, `/sunglasses/boaz/jet-black`) for hero renders. `/overview` returned a dead 404 (153c, discarded).
- **Verify:** all sourceURLs matched the requests; all 13 page bodies were md5-unique (no geo/cache contamination).
- **Credits:** 14 (1 map + 13 scrapes incl. the dead /overview; logo + hero asset fetches were headed/free).
- **Couldn't get:** national store count (locator only); per-box contacts pricing + eye-exam fee (selection/booking-gated); full mega-nav flyout sub-items (client-rendered); the Home Try-On FAQ answer (collapsed/client-rendered); clean PDP product renders via CDN (lazy-loaded blanks / color swatches — hero renders cropped from PDP screenshots instead).
- **Run profile:** guided — output scope "all modules": **+logos** (wordmark extracted from inline brand SVG, recolored to navy; logomark + og measured) and **+offerings** (Catalog → shape + exemplars) **with hero product images** (3 flagship frame renders cropped from PDP full-page screenshots → `captures/2026-06-04/images/`).
- **Enriched (model knowledge):** Warby Parker is publicly traded (NYSE: WRBY) — not stated on captured pages; recorded for identity resolution only.
