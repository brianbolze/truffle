---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: coda.io
name: Coda
aliases: []
legal_entity: ""                     # site states only "© 2026 Coda" — no registered legal form on captured pages
parent: [grammarly.com]              # STRAIN: page-attested via footer routing — Privacy→grammarly.com privacy policy, Press→press@grammarly.com; Legal Notices→superhuman.com + "Superhuman community support" on /pricing. Grammarly acquired Coda (Dec 2024); its corp parent later rebranded to Superhuman — see Enriched line.
owns: []
socials:
  x: https://twitter.com/coda_hq
  linkedin: https://www.linkedin.com/company/codainc
  facebook: https://www.facebook.com/codahq/
  youtube: https://www.youtube.com/channel/UC73YRwUcAjAW_euaGzDUAzg
external: {}                         # no crunchbase/wikipedia/etc. in footer or JSON-LD (no JSON-LD on homepage)

# Capture meta
captured_at: 2026-06-23
capture_method: firecrawl
site_notes: "Custom React/Vite SPA (no __NEXT_DATA__; vite markers + hashed /assets/), marketing content served via Sanity CMS (sanity-images.imgix.net). Map is swamped by user content — /@user/ published docs, /d/ docs, /packs/, /gallery/, /resources/ — so SELECT signal pages from homepage links, not the map. No JSON-LD on homepage; nav recovered from <header>. Pricing lives on /pricing (per-Doc-Maker 'Maker Billing'); named certs (SOC 2 Type II, HIPAA) are in the /pricing compare-table + /trust, not the marketing nav. Corp/legal routing points to grammarly.com (privacy, press) + superhuman.com (legal notices) — the Grammarly/Superhuman parent."
key_pages:
  product: /product
  pricing: /pricing
  ai: /product/ai
  about: /about
  trust: /trust
  developers: /developers
  packs: /product/packs
  solutions: /solutions
  compare: /compare
unverified_fields:
  - "AI model provenance — the /product/ai FAQ 'What models does Coda AI leverage?' is a collapsed accordion; the underlying model vendor is not in the captured text."
  - "Full certification list — only SOC 2 Type II + HIPAA (New!) are named (on /pricing); /trust references 'compliance standards' / 'global privacy laws' without enumerating (ISO 27001 / GDPR not confirmed on captured pages)."
  - "Desktop surfaces — only iOS + Android apps are linked in the footer; macOS/Windows apps not confirmed on captured pages."
  - "primary_job + ai_front_door are a point-in-time snapshot, not fixed — homepage hero copy and AI placement are A/B-prone."

# Description — one sentence (~160-220 chars)
description: "An all-in-one collaborative workspace that blends documents, spreadsheet-style tables, and no-code apps on one canvas, with built-in AI and 600+ integrations — billed only for the team members who create docs."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2B, B2C]            # leads with teams (50,000+ teams); a real free/prosumer + student/educator funnel underneath
offering_category: [Software / SaaS]
portfolio_shape: Single              # one product — the Coda workspace, sold in tiers; Packs/AI are surfaces of it, not separate SKUs
business_model: Subscription         # per-Doc-Maker recurring; strong free→paid (freemium) funnel
primary_industry: Technology

# Visual identity — branding payload is a hint; verified against the homepage screenshot
logo_url: https://cdn.coda.io/icons/png/color/coda-32.png   # favicon fallback — branding.images.logo was null; logos:{} module not run this capture
brand_colors: { primary: "#FFF6EC", accent: "#FFE6C9", secondary: "#00ABEC" }  # signature is the warm cream/peach hero band; #00ABEC is UI/link blue, not the brand field (verified in screenshot)
fonts: [Calibre, Inter]              # Calibre-R display/headings, Inter body (branding.fonts ranked generic "sans-serif" first — ignored)
color_scheme: light
design_framework: react/vite         # rawHtml: vite markers + hashed /assets/, no __NEXT_DATA__; content via Sanity CMS
---

## Overview

Coda is an all-in-one collaborative workspace that merges three things usually kept in separate tools — documents, spreadsheet-style tables/databases, and lightweight no-code apps — onto a single editable canvas, with AI and 600+ integrations ("Packs") layered in. It positions as "a new kind of doc" that grew into an "all-in-one work operating system," sold to teams (product, sales, engineering, design, marketing, HR, IT) from startups to enterprise, plus a free/prosumer and student tier. Founded by **Shishir Mehrotra** (CEO) and **Alex DeNeui** (CTO) — ex-Microsoft/Google, met at MIT. Coda's corporate ownership now sits under the **Grammarly / Superhuman** parent (see Strategic read).

## What they offer

One product — the Coda workspace — sold in four plans, billed per **"Doc Maker"** (people who create docs); Editors and Viewers are always free. AI and the Packs integration catalog ride on top.

- **Free:** "Free for you and your team" — collaborative docs, connected tables/charts/kanban/forms, formulas & automations, AI trial `[published]`
- **Pro:** **$10/month per Doc Maker** (Editors free) — unlimited objects, 30-day version history, hidden pages, custom domains, custom icons & branding `[published]`
- **Team:** **$30/month per Doc Maker** — unlimited automations & version history, doc locking, manage folder access, cross-doc sync `[published]`
- **Enterprise:** **Custom** — SAML SSO, SCIM provisioning, advanced access controls, audit events, SOC 2 Type II report, HIPAA `[on-request]`
- **Coda AI:** included for Doc Makers (not a separate add-on); pooled credits, with extra-credit add-ons at **$2 / $6 / $12 per Doc Maker/month** (2,000 / 6,000 / unlimited credits) `[published]`

Capability families (all part of the one product): **Docs & team hubs**, **Trackers & apps** (tables, views, kanban, forms), **Coda AI** (AI chat, AI assistant, AI column), **Packs** (600+ integrations / third-party app marketplace), **Publishing** (publish a doc as a website), **API**. 15% off on annual billing.

## How it works / model

- **Maker Billing — the signature model:** "Instead of charging for everyone, we only charge for the people who create docs and pages. Editors are free." Charging is per Doc Maker in a workspace, prorated as makers are added/removed. Editors, Viewers, and Guest Editors are always free.
- **PLG funnel:** self-serve free signup → upgrade a workspace to Pro/Team with one or more Doc Makers → Enterprise via sales.
- **AI metering:** Coda AI is included for Doc Makers; each workspace gets a monthly credit pool (1 credit ≈ 40 characters / 7.5 words), with paid credit add-ons beyond the allotment.
- **Discounts:** students & educators (varies), non-profits 50%, eligible startups get the Team plan free for 6 months.

## Positioning & audience

Pitched as the way to escape tool sprawl — "replace hundreds of apps," consolidate docs + spreadsheets + bespoke apps into "a single platform they'll never outgrow." Targets cross-functional teams by role (product, sales, marketing, design, engineering, IT, HR), by scenario (planning/OKRs, meetings, project management, knowledge management), and by team size (startups → small business → enterprise). Explicitly benchmarks against **Notion, Airtable, Confluence, Quip, and Google Docs** (dedicated `/compare` pages). Claimed edge: one canvas that blends doc + spreadsheet + app + AI, plus per-maker pricing instead of per-seat. Third-party pull-quote (self-reported): *"It's more powerful than Google Docs and more flexible than Airtable or Notion."* — Fast Company.

## Nav structure

```
- Product — /product
  - Explore: Docs & team hubs — /product/docs-and-team-hubs · Trackers & apps — /product/trackers-and-apps
  - AI & integrations: Coda AI — /product/ai · Integrate your tools — /product/integrations · Consolidate your tools — /product/tool-consolidation
  - More: What's new — /product/whats-new · Packs — /product/packs · Publishing — /product/publishing
- Compare — /compare
  - vs Notion — /compare/notion · vs Confluence — /compare/confluence · vs Quip — /compare/quip · vs Airtable — /compare/airtable
- Solutions — /solutions
  - By role: Product — /solutions/role/product-teams · Marketing — /solutions/role/marketing · Sales — /solutions/role/sales (+ engineering, product-design)
  - By scenario: Planning & OKRs — /solutions/scenario/okrs · Meetings — /solutions/scenario/meetings · Project management — /solutions/scenario/projects
  - By team size: Enterprise — /solutions/team-size/enterprise · Startups — /solutions/team-size/startups · Small business — /solutions/team-size/small-businesses
  - Case studies — /solutions/case-studies (e.g. Qualtrics)
- Resources — /resources
  - Learn: Guides — /resources/guides · Interactive sessions — /resources/webinars/training-recordings · Webinars — /resources/webinars
  - Connect: Help center — help.coda.io · Community — community.coda.io · Hire a Services Partner — /partners/hire-a-services-partner · Partner with us — /partners
  - Extend: Pack Studio — /resources/packs/why-build-packs · Formula list — /formulas · API — /developers
- Gallery — /gallery
- Blog — /blog
- Pricing — /pricing
- Request a demo — /contact/sales/request-a-demo  ·  Get started — /signup
```

Footer adds: About — /about · Careers — /about/jobs · Accessibility — /product/accessibility · Coda on Coda — /about/coda-on-coda · Status — status.coda.io · Sitemap — /sitemap · iOS & Android apps.

## Credibility & proof

All figures are self-reported on Coda's own pages:
- **Scale (self-reported):** "50,000+ teams" · "80% of the Fortune 100 use Coda" · "186 million+ docs engaged" · "600+ integrations."
- **Customer logo wall:** Figma, The New York Times, Square, Robinhood, BuzzFeed, TED, Uber.
- **Case studies:** Qualtrics ("saves money with Coda"), Intercom, Huge ("eliminated three to four hours of meetings every week").
- **Press quote (self-reported):** *"It's more powerful than Google Docs and more flexible than Airtable or Notion."* — Fast Company.
- **Security/compliance:** SOC 2 Type II report, HIPAA compliance ("New!"), SAML SSO, SCIM, audit events (Enterprise); **99.9% uptime commitment** to Enterprise; public status page (status.coda.io). Pack security: "Encrypted login credentials never touch Pack code."

## Visual & brand impression

A polished, mature SaaS marketing site with a distinctive **warm cream / peach** signature palette (`#FFF6EC`, `#FFE6C9`) for hero and feature bands — a deliberate softening against the stark-white default of the category — punctuated by a light-blue testimonial band and the multi-color Coda wordmark. Heavy use of real product screenshots (the canvas, connected tables, kanban, AI panels) rather than abstract illustration, plus a recognizable customer logo wall, signals product confidence. Typography pairs a **Calibre** display face for headlines with **Inter** for body. Tone is professional and warm; light color scheme throughout.

## Strategic read

- **Maker Billing is the strategic wedge.** Pricing only for creators ("we don't charge per seat") is positioned as a structural advantage for large rollouts where most people consume rather than create — it lets Coda expand seats without the per-head cost that gates Notion/Airtable adoption. It also reframes Coda from "another per-seat SaaS" to a consolidation play ("replace dozens of apps").
- **Owned by the Grammarly / Superhuman parent.** Coda's privacy policy and press both route to **grammarly.com**, while legal notices route to **superhuman.com** and the pricing page lists "Superhuman community support." This is the corporate-integration footprint of Grammarly's December 2024 acquisition of Coda (CEO Shishir Mehrotra also leads the parent), after which Grammarly's corporate parent rebranded to **Superhuman**. The Coda brand and product still operate under their own name and © (see Enriched line for the identity prior).
- **AI as included, not upsell.** Coda AI is bundled for Doc Makers "not a separate add-on, not a separate license," with usage metered in a shared credit pool — a different stance from rivals charging a separate AI seat.

## Provenance

- **Pages:** homepage + 8 key pages (product, pricing, product/ai, about, trust, developers, packs, solutions) + map — 9 scrapes, Firecrawl, `maxAge:0` + US locale.
- **Verify:** all 9 sourceURLs matched; all bodies md5-unique; no junk soft-404s.
- **Credits:** 10 (1 map + 9 scrapes).
- **Couldn't get:** AI model vendor (FAQ accordion collapsed); full certification list beyond SOC 2 Type II + HIPAA; desktop app availability (only iOS/Android linked).
- **Run profile:** express — +productivity_saas cohort pack (see `productivity_saas.md`); no emphasis given.
- **Enriched (model knowledge):** Grammarly acquired Coda (Dec 2024); Grammarly's corporate parent subsequently rebranded to Superhuman (2025) — used only to resolve the grammarly.com / superhuman.com footer routing to the parent relationship, not for any product claim.
