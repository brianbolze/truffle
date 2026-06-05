---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: keeps.com
name: Keeps
aliases: []
parent: [thirtymadison.com]           # footer + all legal/fulfillment route to Thirty Madison (patient.thirtymadison.com); sibling brands Cove, Facet, Nurx
owns: []
socials: { instagram: "https://www.instagram.com/keeps", facebook: "https://www.facebook.com/getkeeps", x: "https://twitter.com/getkeeps" }  # footer anchors (no JSON-LD on homepage to seed from)
external: {}                          # no third-party records declared on-site (no JSON-LD sameAs)

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Next.js SPA (rawHtml: __NEXT_DATA__ + 112x /_next/; istio-envoy / Istio infra; keeps.com 308-redirects to www.keeps.com). branding.designSystem said 'custom' (ignored). NO JSON-LD on the homepage and no <header>/<nav> element (nav in a bare div) — BUT the full mega-nav DOES serialize into the homepage markdown (Hair Loss + Sexual Health dropdowns, each with its product-card list), so rebuild Nav from markdown, not signals. Map is ~80% content noise (95 URLs: /learn 31, /faq 13, /drug-facts 12) — pull the catalog from homepage links + /our-products, NOT the map: the 4 new Chew/Drop compound SKUs + chew-3-in-1 + daily-hair-defense-supplement are homepage-linked but ABSENT from the map. Per-SKU prices ARE on the /our-products cards (list->promo, e.g. '$50 $33.33'); the homepage 'Half the cost' table gives per-MONTH equivalents (Finasteride $25/mo, Minoxidil $10/mo, consult first-free then $5/visit). ED prices live on the product PDPs ('starting from $X/dose'), not on /condition/ed. Legal/fulfillment route to parent Thirty Madison (patient.thirtymadison.com)."
key_pages:
  our_products: /our-products
  about: /about-us
  hair_loss_hub: /hair-loss
  condition_ed: /condition/ed
  quiz: /quiz
  sh_quiz: /sh-condition-routing
  reviews: /reviews
  press: /press
  pdp_finasteride: /our-products/finasteride
  pdp_minoxidil_foam: /our-products/minoxidil-foam
  pdp_sildenafil: /our-products/sildenafil-citrate
  pdp_tadalafil: /our-products/tadalafil
unverified_fields:
  - "Pharmacy/fulfillment ownership not stated — Keeps claims it 'built our own supply chain' but names no pharmacy entity or accreditation; legal + fulfillment route to parent Thirty Madison (patient.thirtymadison.com)."
  - "Pay model (cash-pay vs insurance/HSA/FSA) not stated on captured pages — site frames itself as DTC ('selling directly to you') but states no payment rail."
  - "ED 'Powerhouse 3-in-1' / 'Triple-action' compounds are homepage-featured but quiz-gated — no public slug or price (behind /sh-condition-routing)."
  - "Card prices ('$50 $33.33') are list -> promo (the 'up to 1 month FREE with a 3-month plan' offer); billed every 3/6/12 mo, default cadence shown. Per-month framing ($25/mo finasteride) and per-shipment framing ($80 $53.33) don't fully reconcile — captured verbatim, not normalized; a point-in-time promo snapshot."
  - "Customer count ('hundreds of thousands of guys') is a self-reported, unquantified claim. Review count 6,979 is a homepage/our-products widget figure."
  - "Headcount, funding, revenue — not on the marketing site (deep-research job)."

description: "A DTC men's hair-loss telehealth brand, part of Thirty Madison, that prescribes finasteride, minoxidil, and compounded multi-ingredient regimens through online providers and ships them on subscription at ~half local-pharmacy cost, plus a companion ED line."

# Classification
entity_type: Company                 # runs its own P&L + storefront under parent Thirty Madison -> Company, not Brand
target_market: [B2C]
offering_category: [Services / Consulting, Biotech / Pharma Products]   # telehealth prescribing service + Rx/OTC pharma products (corpus convention for the cohort)
portfolio_shape: Multi-product       # hair-loss Rx + hair OTC cosmetics + sexual-health Rx + a supplement — distinct enumerable lines, hair-loss dominant
business_model: Subscription         # auto-refill shipments every 3/6/12 months; OTC items also one-time
primary_industry: Healthcare & Life Sciences

# Visual identity — branding payload is a hint; verified against screenshot + the SVG marks
logo_url: "https://www.keeps.com/assets/next/icons/logo.svg"   # 2.5 canonicalizes to the wordmark — the dark "keeps" lowercase wordmark SVG (hostable URL, no file)
logos:                               # 2.5 module — measured by fc.py logos; the consumer applies the size bar
  wordmark: { src: "https://www.keeps.com/assets/next/icons/logo.svg", w: 119, h: 44 }                                 # dark "keeps" lowercase wordmark (renders on light)
  logomark: { src: "https://www.google.com/s2/favicons?domain=keeps.com&sz=256", px: 32, transparent: true }           # the red crown symbol; only a 32px favicon resolves (under the 128px deck bar — recorded per schema); the on-brand crown SVG (54x26, #FF4646) is wider-than-square
  og:       { src: "https://keeps.com/images/keeps-living-room.jpg", w: 1414, h: 943 }                                 # real Keeps unboxing share cover (white cartons w/ red crown, "HAIR TODAY. HAIR TOMORROW." insert)
brand_colors: { primary: "#E22631", accent_green: "#032B24", text: "#231E20", background: "#FFFFFF" }  # STRAIN: #E22631 = branding red (the crown SVG is the brighter #FF4646); #032B24 dark green = link/CTA-band accent; warm cream section bands read off the screenshot
fonts: [Apercu]                      # branding.fonts[0] — a clean geometric grotesque sans (heading + body)
color_scheme: light
design_framework: next.js            # rawHtml: __NEXT_DATA__ + /_next/ (112 hits); branding.designSystem said "custom" (ignored per §5.4)
---

## Overview

Keeps is a **DTC men's hair-loss telehealth brand** and a **Thirty Madison** company (sibling to Cove, Facet, and Nurx; all legal and fulfillment route through `patient.thirtymadison.com`). It sells the two FDA-approved hair-loss molecules — **finasteride (generic Propecia®)** and **minoxidil (generic Rogaine®)** — plus a growing line of **compounded, multi-ingredient prescription formulas** (the new Chew and Drop "X-in-1" products), an OTC styling/cosmetics range, and a hair supplement. A licensed provider reviews an online consultation, confirms the plan, and treatments ship on a **3/6/12-month subscription** "at half the cost of your local pharmacy." A companion **sexual-health (erectile-dysfunction)** line — sildenafil and tadalafil — is positioned as "New to Keeps." Founded in **2018** by **Steve Gutentag and Demetri Karagas**; the brand is squarely **men-only** ("help more men keep more hair," "Men of Action").

## What they offer

Hair loss is the flagship; sexual health, cosmetics, and a supplement are companion lines. All medications gate on a provider-reviewed online consultation. Per-SKU detail (full priced roster) in `offerings.md`.

- **Hair-loss Rx — single molecules:** Finasteride (generic Propecia®) **`$80 $53.33`** `[published]`; Minoxidil+ Spray, a "compounded" minoxidil/caffeine/tretinoin/melatonin formula **`$135 $108`** `[published]`; Ketoconazole Shampoo 2% **`$33 $22`** `[published]`. Homepage per-month framing: finasteride **$25/mo**, minoxidil **$10/mo** `[published]`.
- **Hair-loss Rx — new compounded "X-in-1" formulas (hero of the site):** Chew+ 5-In-1 Dutasteride & Minoxidil **`$149`**, Chew 3-In-1 Finasteride & Minoxidil **`$129.99`**, Drop+ 11-In-1 Dutasteride & Minoxidil **`$174.99`**, Drop 4-In-1 Finasteride & Minoxidil **`$159.99`**, Topical Finasteride & Minoxidil Gel **`$180 $120`** — all `[published]`, all flagged "New."
- **Hair — OTC:** Minoxidil Foam 5% **`$50 $33.33`** / Solution 5% **`$33 $22`** `[published]`; Thickening Shampoo **`$22 $17.60`**, Conditioner **`$22 $17.60`**, Pomade **`$25 $20`** `[published]`; Daily Hair Defense Supplement (vitamins + saw palmetto) **`$81`** `[published]`.
- **Sexual health (ED), "New to Keeps":** Sildenafil Citrate (generic Viagra®, 25/50/100mg) **"starting from $3.20/dose"** `[partial]`; Tadalafil (generic Cialis®, 2.5/5/10/20mg) **"starting from $4.80/dose"** `[partial]`. Plus homepage-featured **compounded** ED ("Powerhouse 3-in-1," "Triple-action by design") that are **quiz-gated** — no public price `[on-request]`.
- **Provider care:** "first visit free, **$5 per visit thereafter**"; "unlimited provider messaging for one year" `[published]`.

## How it works / model

A three-step DTC telehealth journey: **(1) Pick your plan** (or take the hair-loss / sexual-health quiz) — a licensed medical provider reviews the online consultation and confirms it's medically appropriate; **(2) Get it delivered** — treatment ships discreetly every **3, 6, or 12 months** "at a fraction of the cost of your local pharmacy"; **(3) Keep your hair** — track progress with unlimited provider messaging; adjust, pause, or cancel anytime. Consultation is **asynchronous** (online questionnaire + provider messaging — no video visit named). Revenue is **subscription** (recurring auto-refill), with OTC items also buyable one-time. The pitch is price: a "Half the cost" table contrasts Keeps vs. "Other Guys" (finasteride $25/mo vs $65/mo; minoxidil $10/mo vs $18/mo; consult first-free + $5/visit vs $100+/visit), justified by "building our own supply chain and selling directly to you."

## Positioning & audience

Targets **men** (broadly 20s–30s, the "start early" message; testimonials are men 27–31) who are starting to notice hair loss and want a simple, affordable, science-backed fix without a clinic visit. Positioned against (a) the local pharmacy / dermatologist (slow, expensive) and (b) gimmicks it explicitly dismisses — "laser helmets… or gummy vitamins… stuff on the market that doesn't work." Claimed edge: **only FDA-approved/clinically-proven treatments**, **half the cost**, top dermatologist advisors, and a no-nonsense masculine voice ("No skeevy before-and-after shots"). The ED line extends the same men's-health franchise. Deeper voice work belongs in `brand.md`.

## Nav structure

```
- Hair Loss (mega-dropdown) — "Explore our clinically-proven prescription and over-the-counter options"
  - Take our hair loss quiz — /quiz
  - Male Pattern Baldness — /hair-loss
  Treatments:
  - Chew+ 5-In-1: Dutasteride & Minoxidil [Rx, New] — /our-products/chew-plus-5-in-1-dutasteride-and-minoxidil
  - Chew 3-In-1: Finasteride & Minoxidil [Rx, New] — /our-products/chew-3-in-1-finasteride-and-minoxidil
  - Drop+ 11-In-1: Dutasteride & Minoxidil [Rx, New] — /our-products/drop-plus-11-in-1-dutasteride-and-minoxidil
  - Drop 4-In-1: Finasteride & Minoxidil [Rx, New] — /our-products/drop-4-in-1-finasteride-and-minoxidil
  - Topical Finasteride & Minoxidil [Rx] — /our-products/topical-finasteride-and-minoxidil
  - Finasteride [Rx] — /our-products/finasteride
  - Minoxidil Foam/Solution — /our-products/minoxidil-foam
  - Minoxidil+ Spray [Rx] — /our-products/minoxidil-spray
  - Ketoconazole Shampoo [Rx] — /our-products/ketoconazole
  - Thickening Shampoo — /our-products/thickening-shampoo
  - Thickening Conditioner — /our-products/thickening-conditioner
  - Thickening Pomade — /our-products/thickening-pomade
  - Daily Hair Defense Supplement — /our-products/daily-hair-defense-supplement
  - See All Products — /our-products
- Sexual Health (mega-dropdown) — "Take control of your sexual health with an expert-recommended treatment plan"
  - Take our sexual health quiz — /sh-condition-routing
  - Erectile Dysfunction — /condition/ed
  Treatments:
  - Sildenafil Citrate (generic Viagra®) [Rx] — /our-products/sildenafil-citrate
  - Tadalafil (generic Cialis®) [Rx] — /our-products/tadalafil
- learn (blog) — /learn
- about us — /about-us
- FAQ — /faq
- Get Started — /quiz
- Sign In (account)
Footer — Get Started /quiz · Our Products /our-products · Hair Loss 101 /hair-loss · Learn /learn ·
  Our Story /about-us · FAQs /faq · Contact /contact · Press /press · Careers /careers
  Thirty Madison family: Keeps · Cove (withcove.com) · Facet (facet.thirtymadison.com) · Nurx (nurx.com)
  Legal (all on patient.thirtymadison.com): Privacy · Terms · Informed Consent · Accessibility
```

## Credibility & proof

- **Reviews:** "**6,979 Reviews**" with a star widget (our-products page); before/after testimonials with named users + treatment duration (Virgil C., Roy, Nathan B.).
- **Self-reported scale:** "helped **hundreds of thousands of guys**" (about page) — unquantified claim, flagged self-reported.
- **Efficacy claim:** "Our FDA-approved treatments are **90% effective** at treating hair loss" — a marketing claim, recorded not endorsed.
- **Named clinical leadership / advisors:** **Dr. Parth Shah** (Keeps Sexual Health Clinical Lead — board-certified family physician, Virtua Health, CVS MinuteClinic Medical Director); medical advisors **Jerry Shapiro, MD** (Professor of Dermatology, NYU; 150 peer-reviewed papers) and **Antonella Tosti, MD** (Professor of Clinical Dermatology, U. Miami; 600+ publications; "Tosti alopecia" named for her).
- **Press:** "FEATURED IN" — **Fast Company, CNBC, Business Insider, WSJ** (logo wall).
- **Sourcing:** hair-loss claims cited to the American Hair Loss Association; finasteride side-effect figure "less than 4% (3.8%)" cited to clinical trials.
- **LegitScript:** not shown in the captured markdown (seal may be image-only / on an uncaptured page) — *not found, not confirmed absent.*

## Visual & brand impression

Warm, clean, masculine-but-approachable DTC design — a clear step above MVP and consistent with a well-funded brand. The palette pairs **warm cream/beige section bands** with a punchy **coral-red (#E22631 / crown #FF4646)** for the crown logomark and CTAs, a **deep forest green (#032B24)** action band, and **near-black (#231E20)** text on white. Typography is **Apercu** throughout — a geometric grotesque sans that reads modern and confident. Imagery alternates clean white-carton product renders (each stamped with the red crown), real before/after grids, and lifestyle photography of younger men; the og/share cover is an actual unboxing shot ("HAIR TODAY. HAIR TOMORROW. / Let's do this."). Copy voice is plain, wry, and de-stigmatizing ("Losing your hair sucks… we get it," "Things that do NOT cause hair loss: …Masturbation — you do you"). The crown motif (the brand's only symbol) ties packaging, favicon, and site together.

## Strategic read

Keeps is the **hair-loss-first, price-led** node of the Thirty Madison men's-health portfolio — narrower and more product-catalog-shaped than diagnostics-gated peers (Hone) or broad multi-condition players (Hims). Two strategic moves are visible in this capture: (1) a **push up-market into proprietary compounded "X-in-1" formulas** (Chew+/Drop+ dutasteride+minoxidil, $149–$175) layered on top of the cheap commodity generics — higher AOV + differentiation against undifferentiated finasteride/minoxidil sellers; (2) **category extension into ED** ("New to Keeps") to widen the men's-health wallet off the same telehealth + subscription rails. The whole model leans on **price** ("half the cost," "$5/visit") and **trust** (FDA-approved-only, marquee derm advisors) rather than diagnostics or membership.

## Provenance

- **Pages:** homepage (rich pass: markdown/html/rawHtml/links/branding/images/screenshot), /our-products (rich pass — catalog index + prominence), /about-us, /condition/ed, /hair-loss, and 2 ED PDPs (/our-products/sildenafil-citrate, /our-products/tadalafil) — 7 scrapes + 1 map. Firecrawl `maxAge:0`, `location:US`, `waitFor:3500`. Next.js SPA.
- **Verify:** all sourceURLs matched, all 7 bodies md5-unique (clean); no junk soft-404s.
- **Credits:** 8 (1 map + homepage + our_products + about + condition_ed + hair_loss + 2 ED PDPs).
- **Couldn't get:** pharmacy/fulfillment ownership (claimed "own supply chain," none named; routes to parent Thirty Madison); pay model (cash vs insurance/HSA — unstated); quiz-gated ED compound prices (Powerhouse/Triple-action, behind /sh-condition-routing); financials/headcount (not on site).
- **Structured layer (schema 2.2):** no JSON-LD on the homepage (absent — `socials` seeded from footer anchors, verified to Keeps handles; `external` empty); no `<header>`/`<nav>` element (nav rebuilt from the serialized mega-nav markdown + screenshot, not signals).
- **Run profile:** Express invocation (intent carried, step-2.5 batch skipped) — `+telehealth.md` cohort pack, `+offerings.md` per-SKU roster, `+logos` brand-mark module all enabled. Wordmark = hostable `logo.svg` (no file); logomark = google-s2 favicon (32px, the only square mark — the on-brand crown SVG is 54×26, wider-than-square), `transparent` judged true on the rendered favicon; og = the declared unboxing share cover. Stamped 2.5.
