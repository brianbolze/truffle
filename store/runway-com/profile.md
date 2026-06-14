---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: runway.com
name: Runway
aliases: [Runway Financial]          # G2 / store-listing name; the product brands simply as "Runway"
parent: []
owns: []
socials:
  x: https://x.com/runwayco
  instagram: https://www.instagram.com/runwayfinancial
  youtube: https://www.youtube.com/@runwayfinancial
  linkedin: https://www.linkedin.com/company/runway/
external: {}                          # JSON-LD sameAs carried only operated channels — no crunchbase/wikipedia/etc.

# Capture meta
captured_at: 2026-06-10
capture_method: firecrawl
site_notes: "Webflow site (data-wf-*, website-files.com CDN). Pricing is fully gated — 3 named plans (Core/Growth/Enterprise) all 'Unlock pricing', no published numbers; FAQ states pricing scales with integrations/data-warehouse complexity, not seats. Product is ONE FP&A platform with 3 surfaces: /product/planning, /product/modeling, /product/reporting. Wordmark is an inline data-URI SVG in branding.images.logo (decoded → assets/wordmark.svg). App at app.runway.com; docs at docs.runway.com (subdomain, off the marketing map)."
key_pages:
  pricing: /pricing
  planning: /product/planning
  modeling: /product/modeling
  reporting: /product/reporting
  about: /about
  security: /security
  customer_stories: /customer-stories
unverified_fields:
  - "Exact plan pricing — all three tiers are 'Unlock pricing' / quote-only; no numbers shown."
  - "Headcount — ~28 named people on /about#team (excl. 3 office dogs); a team-page roster, not an official figure."
  - "Founding year — narrative implies ~2020 ('four years later' from a pandemic start); no explicit incorporation date on-site."

# Description — one sentence
description: "An FP&A platform for high-growth startups that unifies collaborative planning, real-time financial modeling, and story-driven reporting in one tool, fronted by an AI analyst that knows your model."

# Classification — closed sets (TAXONOMIES.md)
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Single              # STRAIN: one FP&A platform; Planning/Modeling/Reporting are surfaces of it, Core/Growth/Enterprise its tiers — not separately-shopped products
business_model: Subscription
primary_industry: Finance & Fintech  # STRAIN: a B2B SaaS that operates in the financial-software sector (FP&A); the product IS financial planning, buyers are finance teams

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 100, h: 20 }                                                                          # inline-SVG wordmark (5:1), decoded from branding payload
  logomark: { src: "https://www.google.com/s2/favicons?domain=runway.com&sz=256", px: 256, transparent: false }                  # upward "↗" arrow on a BAKED amber-gradient square (apple-touch confirms)
  og:       { src: "https://cdn.prod.website-files.com/683909604bbd11a23e6dd536/685b62d054dba5ce4ff3501c_381aff7636de8015600f575109b2eac8_runway-open-graph-image.jpg", w: 1200, h: 630 }
brand_colors: { primary: "#F9A600", text: "#261B07", background: "#F8F7F5" }   # amber/gold hero + CTA on near-black-brown text over warm off-white; confirmed in screenshot
fonts: [Interphases Pro Variable]
color_scheme: light
design_framework: webflow
---

## Overview

Runway is an FP&A (financial planning & analysis) platform aimed at high-growth, venture-backed startups — the tool a company's first finance hire reaches for instead of stacked spreadsheets or heavy legacy enterprise software. It unifies three jobs in one product: **planning** (collaborative, cross-team budgets and forecasts), **modeling** (a real-time financial model wired to live data sources), and **reporting** (interactive dashboards and month-end close). The pitch leans hard into AI — the homepage headline is "FP&A for AI-fluent teams… Simulate any business decision in seconds," and an embedded **AI Analyst** can build pages, run scenarios, and explain variance in plain language. Founded out of the early-pandemic experience of CEO Siqi Chen scenario-planning layoffs in Excel, the company's stated mission is to "make business understandable and accessible to everyone" — explicitly positioning Runway as the "Figma/Notion of finance."

## What they offer

One platform, sold as three tiered plans — **pricing is quote-only across the board** (no seats; priced by integrations + data complexity):

- **Core plan:** "For scaling teams with a first finance hire, preparing for board meetings, forecasts, and their next fundraise" — unlimited users, full feature access, core integrations, AI features, SLA support — **"Unlock pricing"** `[on-request]`
- **Growth plan (marked "Popular"):** "For high-growing teams with dedicated FP&A ownership" — everything in Core + specialized integrations, higher integration limits, SSO, priority support — **"Unlock pricing"** `[on-request]`
- **Enterprise plan:** "For large or complex organizations with custom workflows, entities, and reporting requirements" — everything in Core/Growth + custom integrations, white-glove modeling support, dedicated SLA — **"Unlock pricing"** `[on-request]`

The product itself splits into three surfaces (one platform, not separate SKUs):

- **Planning:** collaborative business planning — human-readable formulas, role-based access/permissions, private cells, full edit audit trail; "plan together with clarity, speed, and control."
- **Modeling:** real-time financial modeling — automated data connections, human-readable formulas, flexible segmentation/dimensions, instant drill-ins; "turn complex business logic into clear, scalable simulations."
- **Reporting:** story-driven reporting — month-end close ("15 days to one click"), interactive dashboards, AI variance analysis, real-time data sync; "stop building reports, start telling stories."

Platform-wide essentials shown across pages: **scenario planning** (build/compare scenarios without duplicating the model), **sales & marketing forecasts** (CRM deals, ARR, churn, CAC, ROI-by-channel tied to revenue goals), **750+ integrations**, **investor updates**, **templates**, and the **AI Analyst** copilot. No implementation fees; onboarding, training, and a dedicated CSM are included in every plan.

## How it works / model

B2B SaaS subscription, annual-contract / sales-led: every plan routes through "Talk to a human" / "Get a personalized sneak peek" (a demo + scoping call) rather than self-serve signup. Pricing is deliberately unlisted — per the pricing FAQ, "Runway pricing is based on your systems, integrations, and deployment complexity… Publishing flat numbers would be misleading." Tiers move up with the **number and type of integrations** (specialized connectors / data warehouses push you to Growth or Enterprise), explicitly **not** seat count ("all plans include unlimited seats"). Customers signing before a feature launches are grandfathered into current pricing. Implementation is Runway-guided and phaseable; live data flows in through 750+ integrations (ERP/HRIS/CRM/accounting/data-warehouse) feeding one always-current model.

## Positioning & audience

Targets finance leaders and operators at high-growth startups (seed → scale), with case studies in SaaS (Rootly, AwardSpring, RevenueCat), consulting, and consumer brands. The claimed edge is **flexibility + accessibility + AI**: as powerful as Excel but collaborative, traceable, and connected to live data — and "fun." Repeated framing pits Runway against (a) spreadsheets and (b) "ugly enterprise software," the two options the founder says existed before. The site maintains a deep competitive surface — dedicated `/vs/` and `/compare/` pages against Abacum, Aleph, Anaplan, Causal, Cube, Datarails, Drivetrain, Jirav, LiveFlow, Mosaic, Pigment, Vena, Workday, and Excel — signalling an actively contested modern-FP&A category.

## Nav structure

```
- Customers — /customer-stories
- Product (flyout)
  - Planning — /product/planning
  - Reporting — /product/reporting
  - Modeling — /product/modeling
  - Knowledge:
    - Changelog — /product-updates
    - Product docs — https://docs.runway.com/
    - Integrations — https://docs.runway.com/integrations/integrations-directory
  - Latest update — (rotating; e.g. /product-updates/use-last-close-in-formulas)
- Pricing — /pricing
- Resources (flyout)
  - Customer stories — /customer-stories
  - Changelog — /product-updates
  - Glossary — /resources/glossary
  - Blog — /blog
- Company (flyout)
  - About — /about
  - Careers — /careers
  - Security — /security
- Login — https://app.runway.com/
- Talk to a human — /demo
```

## Credibility & proof

- **G2 rating:** "G2.com 4.8/5 stars" badge in the nav; JSON-LD reports `ratingValue 4.8`, `ratingCount 38` — **self-reported on-site**, links to the Runway Financial G2 profile.
- **SOC 2 Type II:** "SOC 2 Type II compliant with enterprise-grade access controls and data handling" (badge on /pricing; detail on /security).
- **Named customers (logo wall + about):** AngelList, Superhuman, MyFitnessPal, Kick, Kit, Sandbox VR, MotherDuck, Lambda, Sprig, VitalBio, Rootly, Pinpoint, 818 Tequila, RevenueCat, Stake. "Companies are coming to us faster than we can onboard them."
- **Case-study metrics (self-reported):** Rootly "100% automated reports"; AwardSpring "3-4 weeks → 10-15 mins spent planning"; Paul Gastello (consulting) "99.9%+ time savings."
- **Investor/angel roster (about page):** Garry Tan (YC/Initialized), a16z, Elad Gil, Naval Ravikant, Dylan Field (Figma), Eric Ries, Claire Hughes Johnson (ex-Stripe COO), Henry Ward (Carta), Akshay Kothari (Notion COO), Scott Belsky, Balaji Srinivasan, and others.

## Visual & brand impression

Polished, confident, modern-SaaS aesthetic. Warm off-white canvas (`#F8F7F5`) with a signature **amber/gold** (`#F9A600`) used for the hero gradient and CTAs, set against near-black-brown text (`#261B07`) — distinctive in a category that defaults to corporate blue. Heavy use of real, legible product screenshots (dashboards, scenario tables, the AI Analyst chat) rather than abstract illustration; the /about page swaps to charming vintage-style illustrations for its founder narrative. Custom variable typeface (Interphases Pro Variable). Personality shows through — a testimonial reads "Onboarding is #REF! awesome" (a spreadsheet-error in-joke), and the team page lists three office dogs under "Morale." Reads as a well-funded, design-led company that wants finance to feel approachable.

## Strategic read

Two things stand out. **(1) AI is now the headline, not a feature.** The top-of-page promise shifted to "FP&A for AI-fluent teams" with an AI Analyst that builds and reasons over your model — Runway is betting the category re-forms around an agent that "knows your model as well as you do." **(2) Pricing opacity is a deliberate enterprise-sales posture.** Unlimited seats + integration-based, quote-only pricing keeps Runway out of per-seat price comparisons and frames every deal as a scoped enterprise rollout — consistent with the white-glove onboarding and dedicated-CSM model. The unusually broad `/vs/` page set is the tell that modern FP&A (Pigment, Mosaic, Causal, Abacum, Drivetrain, et al.) is a crowded, knife-fight category where comparison SEO is a core acquisition channel.

## Provenance

- **Pages:** 6 analyzed via Firecrawl (homepage, /pricing, /product/planning, /product/modeling, /product/reporting, /about) + map (291 URLs) + homepage structured layer (JSON-LD + nav) + 6 full-page screenshots + logos module.
- **Verify:** all 6 sourceURLs matched; all body md5s unique; no junk soft-404s.
- **Credits:** 7 (1 map + 1 homepage + 5 key pages; signals/logos/verify are free). 5,689 remaining at pre-flight.
- **Couldn't get:** exact pricing (quote-only, all tiers); explicit founding date and headcount (narrative/roster only — left to deep research).
- **Run profile:** guided — "go deep"; +logos (2.5 module). `offerings.md` requested but **skipped with reason**: pricing is 100% on-request and the product is one platform (no enumerable priced SKU grain a family line collapses) — the plan/module breadth is captured here in *What they offer*; activating `offerings.md` would only restate it.
