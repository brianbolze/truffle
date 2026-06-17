---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: posthog.com
name: PostHog
legal_entity: "PostHog, Inc."   # footer: "© 2026 PostHog, Inc."
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-06-16
capture_method: firecrawl
site_notes: "Gatsby SSG (___gatsby + /page-data/ in rawHtml; branding.designSystem says 'tailwind' — wrong, that's the CSS lib; read framework from rawHtml). Map is ~480 URLs but ~95% blog/docs/tutorials/handbook noise; the product catalog comes from homepage links + /products + /pricing, not the map. /products renders thin in markdown (client-rendered Product OS taxonomy — labels in link text, not all slugs linked). Pricing rates ALL live inline on /pricing (markdown-clean, no JS wall) — the full per-product tiered rate cards, so a roster needs no per-SKU sweep. No JSON-LD on the homepage (fc.py signals empty). Header is text-style nav ('home.mdx' / Product OS / Pricing…), so the brand wordmark is NOT an inline header SVG — get it from /handbook/brand/assets (official posthog.com/brand/*.svg). Homepage inline SVGs are CUSTOMER logos (Lovable etc.) — the press-logo trap. Signature cream-paper bg + vivid orange-red brand hue; playful isometric hedgehog illustrations (Hogzilla)."
key_pages:
  products: /products
  pricing: /pricing
  about: /about
  ai: /ai
  platform_packages: /platform-packages
  brand_assets: /handbook/brand/assets
  product_analytics: /product-analytics
  session_replay: /session-replay
  feature_flags: /feature-flags
  data_stack: /data-stack
modules:
  offerings: offerings.md   # per-product roster (all 13 metered products + platform packages), captured 2026-06-16
unverified_fields:
  - "Headcount, revenue, funding stage — not on the marketing site (deep-research job). Site states 'significant revenue', 'over 60,000 customers', 'runs default alive', aims to IPO — all self-reported, no figures."
  - "Customer-count claim is internally inconsistent across pages: /about + homepage counter say '190254+ teams/customers' and 'just under a quarter of a million engineers'; /pricing says 'over 60,000 customers'; homepage hero says '500,000+ teams'. All quoted verbatim below — do not reconcile."
  - "PostHog AI free-tier credits disagree across pages (500 credits 'worth $5' on /pricing vs 2K credits 'worth $20' on the homepage hero)."

# Description
description: "A developer platform bundling product analytics, session replay, feature flags, experiments, surveys, and ~13 tools total into one usage-priced suite ('Product OS') for product engineers, with an open-source core, fully public rate cards, and an AI agent (PostHog AI) across it all."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Multi-product
business_model: Usage-based / Consumption
primary_industry: Technology

# Visual identity
logo_url: https://posthog.com/brand/posthog-logo.svg   # canonicalized to the wordmark (official brand asset)
logos:
  wordmark: { src: https://posthog.com/brand/posthog-logo.svg, w: 800, h: 140 }                                  # color hedgehog (blue/orange-red/yellow spines) + "PostHog" in bold black; transparent SVG
  logomark: { src: "https://posthog.com/icons/icon-512x512.png?v=6e5ac8d4a5b381b5caa29396fbf7c955", px: 512, transparent: false }  # square app icon: white hedgehog on a baked black square. Color transparent alt: https://posthog.com/brand/posthog-logomark.svg (50x30)
  og:       { src: "https://posthog.com/images/og/default.png", w: 1200, h: 632 }                                # product screenshot cover w/ wordmark top-left
brand_colors: { primary: "#F54E00", accent: "#1D4AFF" }   # vivid brand palette from the hedgehog mark + brand page (#F54E00 orange-red, #1D4AFF blue, #F1A82C yellow). Website CANVAS is cream #EEEFE9 with a muted-orange CTA (#EB9D2A / button #CD8407) — the branding payload mis-ranks the cream bg as "primary"
fonts: [IBM Plex Sans, Open Runde]   # IBM Plex Sans = body (branding.fonts[0]); Open Runde = display/headings (fontStack). "Squeak" is the informal hedgehog-pairing display font (brand page)
color_scheme: light
design_framework: gatsby   # rawHtml ___gatsby + /page-data/ — NOT branding.designSystem ("tailwind", the CSS lib)
---

## Overview

PostHog is an all-in-one product-and-data platform for software builders — what it calls **"Product OS."** A single install gives a team product analytics, web analytics, session replay, feature flags, A/B experiments, surveys, error tracking, logs, a built-in data warehouse, and data pipelines, plus an AI agent (**PostHog AI**) that works across all of them. It targets **"product engineers"** — developers who own product outcomes — and positions itself as the consolidation play against a stack of point tools (Amplitude, Mixpanel, FullStory, Heap, LaunchDarkly, Pendo). Open-source core, **fully public usage-based pricing**, no-sales go-to-market.

## What they offer

A bundled suite of **~13 products** (their count: "10+ products and counting"), all on one platform, all with a generous monthly free tier, all **pay-per-use** after it. Full per-product roster with verbatim tiered pricing is in **[`offerings.md`](offerings.md)** (captured 2026-06-16, `indexed-complete`). The lines, with entry rates:

- **Product Analytics** — events, funnels, trends, paths, retention — "From $0.00005/event" after 1M events/mo free
- **Web Analytics** — GA-style site analytics — *billed with Product Analytics*
- **Session Replay** — "Watch people use your product" — "From $0.005/recording" (web) after 5K/mo free; mobile metered separately
- **Feature Flags** — flag management + rollouts — "From $0.0001/request" after 1M/mo free
- **Experiments** — A/B + multivariate, no-code A/B — *billed with Feature Flags*
- **Surveys** — in-product surveys — "From $0.10/response" after 1.5K/mo free
- **Error Tracking** — exception capture + alerts — "From $0.00037/exception" after 100K/mo free
- **Logs** — search/analyze logs — "From $0.25/GB" after 50 GB/mo free
- **Managed warehouse** — built-in data warehouse, SQL editor + BI, 120+ sources/destinations — "From $0.000015/row" after 1M rows/mo free
- **Data Pipelines (CDP)** — ELT import + reverse-ETL/export — realtime destinations "From $0.000500/trigger event"; batch exports "From $0.00001500/row"
- **PostHog AI** — NL agent across the suite — "From $0.01/credit" after 500 credits/mo free; a flat **20% markup over the underlying LLM provider's cost**
- **AI Observability** — LLM traces/generations/evals/costs — "From $0.00006/event" after 100K/mo free
- **Workflows** — automations/messaging — emails "From $0.003000/email"; destinations "From $0.0007500/dispatch"

Plus **platform packages** (org-level governance/support add-ons, the only flat fees): **Boost $250/mo**, **Scale $750/mo**, **Enterprise** (bespoke, "Contact us"). Pricing is **published end-to-end** — every rate card is public; only the Enterprise package is on-request. See `offerings.md` for the per-product roster + the full volume ladders.

## How it works / model

Self-serve, product-led, **no outbound sales** ("You never have to 'jump on a quick call'"). Install via SDK/snippet or an AI wizard (`npx @posthog/wizard`) and an **MCP server** so coding agents (Claude, Cursor) configure PostHog without leaving the IDE. Monetization is **usage-based / pay-per-use**: every product has a generous monthly free tier (they claim "more than 90% of companies use PostHog for free" on /pricing; the homepage says "98%"), and you only pay — and only add a card — when you exceed it. Adding a card also unlocks 6 projects (vs 1), 7-year data retention (vs 1), and email support. Rates **decrease with volume**; per-product billing limits prevent surprise bills. Stated pricing philosophy: operate "like a utility" with razor-thin margins, "match the cheapest major competitor for each product at every scale," make a profit on every product (no loss leaders), and **cut prices rather than raise them**. Runs **"default alive"** — "we don't rely on investors to grow."

## Positioning & audience

Targets **"product engineers"** — *"We make dev tools for product engineers."* The wedge is **consolidation + transparency**: one platform with shared context replacing a dozen integrated point tools, sold without a sales team. Heavy anti-incumbent framing ("there are other dev tool companies, but they not like us"; "While Salesforce hikes prices 6% annually, PostHog proves there's room for startups that do the opposite"). Differentiators they lead with: open-source codebase, generous free tiers, no auto-renewal/lock-in tricks, engineering-background support, public handbook + roadmap + compensation, side-project-insurance against viral usage spikes. Explicitly long-term/independent: *"We have zero intention of selling our business"* — aims to **IPO rather than sell**, and says the stack "will reach at least $100bn in value."

## Nav structure

```
- Product OS — /products
  - Data platform: Data I/O (sources/import ELT, reverse ETL/export), Data modeling, Managed warehouse, CDP, SQL editor, BI
  - Understand product usage: Web Analytics, Product Analytics, Graphs & trends, Funnels, User Paths, Lifecycle, Heatmaps
  - LLM/AI: Traces, Generations, Evals, User activity
  - Debug & fix issues: Error Tracking — /error-tracking, Logs — /logs, Session Replay — /session-replay, Activity timeline
  - Ship features & get feedback: Feature Flags — /feature-flags, Experiments — /experiments, No-code A/B Tests, Early Access Features, Endpoints — /endpoints, Webhooks, Workflows — /workflows, Surveys — /surveys, Support, User interviews
  - Data exploration: PostHog AI — /ai, Notebooks — /notebooks, Dashboards — /dashboards
- Pricing — /pricing  (incl. Platform packages — /platform-packages)
- Docs — /docs (incl. /docs/api, /docs/model-context-protocol)
- Community
- Company
  - About / Why PostHog? — /about
  - Roadmap — /roadmap (public, votable)  ·  Changelog — /changelog
  - People / Teams — /teams  ·  Handbook — /handbook (sales manual, compensation)
  - Brand assets — /handbook/brand/assets  ·  Careers — /careers  ·  Store (merch) — /merch  ·  Trash — /trash
- Get started – free — app.posthog.com/signup
```

## Credibility & proof

- **Scale claims (self-reported, inconsistent — quoted verbatim):** homepage hero "500,000+ teams are shipping with PostHog"; /about + the live counter "over 190254+ customers / teams" and "Just under a quarter of a million engineers use us … far more than any of our competitors — most have around 1-3k customers"; /pricing "over 60,000 customers."
- **Startup penetration:** "65% of every Y Combinator batch use our products."
- **Customer logo wall:** Y Combinator, Airbus, Supabase, ElevenLabs, ResearchGate, Hasura, Exa, Lovable, LinkedIn, AssemblyAI (homepage + /customers, with named case studies).
- **Proof points in case studies:** Hasura "improved conversion rates by 10-20%"; YC "gathers 30% more data than with Google Analytics."
- **Open source:** entire codebase public on GitHub (github.com/posthog/posthog), MIT-licensed — "audit our entire codebase"; self-host option.
- **Radical transparency:** public handbook, public votable roadmap, published employee compensation, public sales/marketing manuals.
- **G2 badge** on homepage; **SOC 2** + **HIPAA** (BAA available on Boost+).
- **Stability posture:** "default alive … we've never had layoffs"; "zero intention of selling."

## Visual & brand impression

Distinctive and deliberately un-corporate. A warm cream/off-white "paper" canvas (#EEEFE9) carrying a vivid multi-color hedgehog mark (blue #1D4AFF / orange-red #F54E00 / yellow), with a muted-orange accent on CTAs, set against playful isometric 3D illustrations — a giant hedgehog ("Hogzilla"), a "keyboard garden" of stacked product blocks, hand-drawn hogs throughout. The copy is irreverent and self-aware (a fake "Shameless CTA" e-commerce cart: "Act now and get $0 off your first order"; a "Trash" nav item; a "demo.mov" / "home.mdx" file-style nav; merch jokes). Reads as a confident, engineering-led indie brand that treats marketing-speak as the enemy — design maturity is high but intentionally anti-slick. Light color scheme throughout. *(A blind, cited visual-evidence read is in [`visual.md`](visual.md).)*

## Strategic read

PostHog is running an unusually coherent **bundling-plus-transparency** strategy: build *every* tool a product engineer needs, give each a generous free tier, price like a metered utility with public rate cards, and grow on internet reputation instead of a sales team — which structurally aligns them with customers (they win by being the cheapest/widest, not by extracting from accounts). The "10+ products and counting" cadence and autonomous "small teams" (mini-startups inside PMF) are the engine; the open-source core + public handbook are the moat-via-trust. The newest bets — **PostHog AI** as a cross-product agent and an **AI Observability** line — push from "measure your product" toward "an AI co-pilot that also reasons over the whole stack," reframing the suite as infrastructure for AI-native teams (and AI agents via MCP) as much as for humans.

## Provenance

- **Pages:** 7 analyzed via Firecrawl (maxAge:0, location:US, waitFor) — homepage, /pricing, /products, /about, /ai, /platform-packages, /handbook/brand/assets; map (~480 URLs) used for inventory only. Product PDP slugs not linked in markdown (/web-analytics, /error-tracking, /logs, /workflows, /endpoints, /cdp, /llm-analytics, /heatmaps) curl-verified to resolve (200).
- **Verify:** all 7 sourceURLs matched; all body md5s unique (no §5.1 geo/cache contamination); no junk soft-404s.
- **Credits:** 8 (1 map + 7 scrapes; no enhanced-proxy retries, no PDFs).
- **Couldn't get:** headcount/revenue/funding (not on marketing site — self-reported claims only, internally inconsistent customer counts flagged in `unverified_fields`). /products markdown is thin (client-rendered) — taxonomy reconstructed from its link text + /pricing + homepage.
- **Structured layer (schema 2.6):** ran `fc.py signals` on the 2026-06-16 homepage rawHtml — no `application/ld+json` present, so no JSON-LD fields; Nav recovered from `links` + the `<nav>` region. `legal_entity` from the footer "© 2026 PostHog, Inc.". Re-stamped 2.2→2.6.
- **Run profile:** deep capture — refreshed over the (16-day-old, schema 2.2) 2026-05-31 profile; added the **`logos:{}`** module (official brand assets), a full **`offerings.md`** roster, and a **`/visual-evidence`** pass.
