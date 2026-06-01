---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.0"

# Identity
domain: posthog.com
name: PostHog
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Gatsby SSG (___gatsby + /page-data/ in rawHtml; branding.designSystem says 'tailwind' — wrong, that's the CSS lib). Map is 487 URLs but ~95% blog/docs/tutorials/handbook noise; the product catalog comes from homepage links + /products, not the map. /products renders thin in markdown (client-rendered nav-style page) — the full product taxonomy is in its link text, not prose. Pricing rates live inline on /pricing (markdown-clean, no JS wall). Signature cream-paper bg + orange accent; playful hedgehog illustrations."
key_pages:
  products: /products
  pricing: /pricing
  about: /about
  ai: /ai
  product_analytics: /product-analytics
  session_replay: /session-replay
  feature_flags: /feature-flags
  data_stack: /data-stack
unverified_fields:
  - "Headcount, revenue, funding stage — not on the marketing site (deep-research job)."
  - "Full per-product rate cards beyond the 4 headline products — /pricing has a per-product calculator; only the four most-popular rates captured verbatim."

# Description
description: "A developer platform bundling product analytics, session replay, feature flags, experiments, surveys, and 10+ other tools into one usage-priced suite for product engineers, with an open-source core and an AI assistant across it all."

# Classification
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Multi-product
business_model: Usage-based / Consumption
primary_industry: Technology

# Visual identity
logo_url: https://posthog.com/favicon-32x32.png   # STRAIN: branding.images.logo was an ambiguous cloudinary doc png; favicon fallback used
brand_colors: { primary: "#EB9D2A", accent: "#EEEFE9" }   # STRAIN: orange is the vision-confirmed brand hue (CTAs, hedgehog); payload ranked the cream paper-bg #E1D7C2 as "primary" — inverted
fonts: [IBM Plex Sans, Ubuntu]
color_scheme: light
design_framework: gatsby
---

## Overview

PostHog is an all-in-one product and data platform for software builders — what it calls "Product OS." A single install gives a team product analytics, web analytics, session replay, feature flags, A/B experiments, surveys, error tracking, logs, and a built-in data warehouse, plus an AI assistant ("PostHog AI") that works across all of them. It targets "product engineers" — developers who own product outcomes — and positions itself as the consolidation play against a stack of point tools (Amplitude, Mixpanel, FullStory, Heap, LaunchDarkly, Pendo). Open-source core, usage-based pricing, no-sales go-to-market.

## What they offer

A bundled suite of **10+ products** (their count), all on one platform, all with a free tier. The enumerable lines:

- **Product Analytics:** events, funnels, trends, paths, retention — "$0.00005/event" after a 1M-events/mo free tier
- **Web Analytics:** GA-style site analytics
- **Session Replay:** "Watch people use your product" — "$0.005/recording" after 5K recordings/mo free
- **Feature Flags:** flag management + rollouts — "$0.0001/request" after 1M requests/mo free
- **Experiments:** A/B and multivariate testing (billed with feature flags)
- **Surveys:** in-product surveys — 1,500 responses/mo free
- **Error Tracking:** exception capture — 100K exceptions/mo free
- **Logs:** "Search and analyze your logs in PostHog" — 50 GB/mo free
- **Data Warehouse / Managed warehouse:** "$0.000015/row" after 1M rows/mo free; 120+ sources/destinations, SQL editor, BI
- **Data Pipelines (CDP):** import (ELT) + reverse ETL/export
- **AI Observability:** LLM traces/generations/evals — 100K events/mo free
- **PostHog AI:** natural-language agent across the suite (build insights, write HogQL, summarize replays, create flags/experiments) — 2K credits/mo free (worth $20)
- **PostHog Code (new):** "proactively finds bugs, fixes them, and creates pull requests automatically"
- **Workflows:** 10K messages/channel/mo free

## How it works / model

Self-serve, product-led, **no outbound sales** ("You never have to 'jump on a quick call'"). Install via SDK/snippet or an AI wizard (`npx @posthog/wizard`) and an MCP server so coding agents configure PostHog without leaving the IDE. Monetization is **usage-based / pay-per-use**: every product has a generous monthly free tier (they claim "more than 90% of companies use PostHog for free"), and you only pay — and only add a card — when you exceed it. Adding a card also unlocks 6 projects (vs 1), 7-year data retention (vs 1), and email support. Rates decrease with volume; per-product billing limits prevent surprise bills. Their stated pricing philosophy: operate "like a utility" with razor-thin margins, "match the cheapest major competitor for each product at every scale," and cut prices rather than raise them.

## Positioning & audience

Targets **"product engineers"** — *"We make dev tools for product engineers."* The wedge is consolidation + transparency: one platform with shared context replacing a dozen integrated point tools, sold without a sales team. Heavy anti-incumbent framing ("there are other dev tool companies, but they not like us"; "While Salesforce hikes prices 6% annually, PostHog proves there's room for startups that do the opposite"). Differentiators they lead with: open-source codebase, generous free tiers, no auto-renewal/lock-in tricks, engineering-background support, public handbook + roadmap + compensation. Explicitly long-term/independent: *"We have zero intention of selling our business."*

## Nav structure

```
- Product OS — /products
  - Data platform: Data I/O (sources/import ELT, reverse ETL/export), Data modeling, Managed warehouse, CDP, SQL editor, BI
  - Understand product usage: Web Analytics, Product Analytics, Graphs & trends, Funnels, User Paths, Lifecycle, Heatmaps
  - LLM/AI: Traces, Generations, Evals, User activity
  - Debug & fix issues: Error Tracking — /error-tracking, Logs — /logs, Session Replay — /session-replay, Activity timeline — /profiles
  - Ship features & get feedback: Feature Flags — /feature-flags, Experiments, No-code A/B Tests, Early Access Features, Endpoints, Webhooks, Workflows, Surveys, Support, User interviews
- Pricing — /pricing
- Docs — /docs (incl. /docs/api, /docs/model-context-protocol)
- Community
- Company
  - About / Why PostHog? — /about
  - Roadmap — /roadmap (public, votable)
  - Changelog — /changelog
  - People / Teams — /teams
  - Handbook — /handbook (incl. /handbook/why-does-posthog-exist, sales manual, compensation)
  - Careers — /careers
- PostHog AI — /ai
- Data stack — /data-stack
- Get started – free — app.posthog.com/signup
```

## Credibility & proof

- **Scale claim:** "over 190254+ customers" / "Just under a quarter of a million engineers use us" — claims far more than competitors ("most have around 1-3k customers")
- **Startup penetration:** "65% of every Y Combinator batch use our products"
- **Customer logo wall:** Y Combinator, Airbus, Supabase, ElevenLabs, ResearchGate, Hasura, Exa, Lovable, LinkedIn, AssemblyAI (homepage + /customers, with named case studies)
- **Proof points in case studies:** Hasura "improved conversion rates by 10-20%"; YC "gathers 30% more data than with Google Analytics"
- **Open source:** entire codebase public on GitHub (github.com/posthog/posthog) — "audit our entire codebase"
- **Radical transparency:** public handbook, public roadmap, published employee compensation, public sales manual
- **G2 badge** displayed on homepage

## Visual & brand impression

Distinctive and deliberately un-corporate. A warm cream/off-white "paper" canvas (#EEEFE9) with a single saturated orange accent (#EB9D2A) on CTAs, set against playful isometric 3D illustrations — a giant hedgehog ("Hogzilla"), a "keyboard garden" of stacked product blocks, hand-drawn hogs throughout. The copy is irreverent and self-aware (a fake "Shameless CTA" e-commerce cart: "Act now and get $0 off your first order"; a "Trash" nav item; merch jokes). Reads as a confident, engineering-led indie brand that treats marketing-speak as the enemy — design maturity is high but intentionally anti-slick. Light color scheme throughout.

## Strategic read

PostHog is running an unusually coherent bundling-plus-transparency strategy: build *every* tool a product engineer needs, give each a generous free tier, price like a metered utility, and grow on internet reputation instead of a sales team — which structurally aligns them with customers (they win by being the cheapest/widest, not by extracting from accounts). The "10+ products and counting" cadence and autonomous "small teams" (mini-startups inside PMF) are the engine; the open-source core + public handbook are the moat-via-trust. The newest bets — PostHog AI as a cross-product agent and PostHog Code (autonomous bug-fix → PR) — push from "measure your product" toward "an AI co-pilot that also builds it," reframing the whole suite as infrastructure for AI agents as much as for humans.

## Provenance

- **Pages:** 7 analyzed via Firecrawl (maxAge:0, location:US, waitFor) — homepage, /products, /pricing, /about, /ai, /product-analytics, /session-replay; map (487 URLs) used for inventory only.
- **Verify:** all 7 sourceURLs matched; all body md5s unique (no §5.1 geo/cache contamination).
- **Credits:** 8 (1 map + 7 scrapes; no enhanced-proxy retries, no PDFs).
- **Couldn't get:** full per-product rate cards (calculator-driven on /pricing — 4 headline rates captured); headcount/revenue/funding (not on marketing site). /products markdown is thin (client-rendered) — product taxonomy reconstructed from its link text + homepage.
