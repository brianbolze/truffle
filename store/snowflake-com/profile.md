---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.2"

# Identity
domain: snowflake.com
name: Snowflake
aliases: ["Snowflake Inc.", "Snowflake AI Data Cloud", "snowflakedb"]
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Adobe Experience Manager (AEM: etc.clientlibs, cq-, data-cmp Core Components, /content/dam/) with a React client layer (clientlib-react). Map returns ~490 URLs but is ~95% docs.snowflake.com — the marketing pages (/product/*, /pricing-options, /company/*) come from homepage links, not the map. Pricing lives on /pricing-options as per-credit list prices by edition × cloud × region (selector defaults AWS us-east-1). Company stats on /company/overview/about-snowflake. Mega-nav flyouts (Product/Solutions/Why/Resources/Developers) are client-rendered and don't surface in markdown — nav reconstructed from footer + per-page sub-navs + homepage platform cards. Marketo forms; no A/B-test fingerprint seen."
key_pages:
  homepage: /en/
  platform: /en/product/platform/
  workloads: /en/product/
  ai: /en/product/ai/
  pricing: /en/pricing-options/
  about: /en/company/overview/about-snowflake/
  why_snowflake: /en/why-snowflake/
unverified_fields:
  - "Per-credit prices are list prices for a single edition/cloud/region snapshot (AWS, US East N. Virginia); they vary by cloud, region, and edition, and capacity/committed-use discounts apply (see CreditConsumptionTable.pdf, not captured)."
  - "Headcount '6,780+ employees in 40+ offices' is stamped 'as of October 2023' on the site — stale, carried verbatim, not current."
  - "Revenue / funding / market-cap not on the marketing site (public co., NYSE: SNOW — a deep-research/investor-relations job, not capture)."

description: "A cloud data platform — the self-styled 'AI Data Cloud' — unifying data engineering, analytics, AI/ML, and secure data sharing in one fully-managed service across AWS, Azure, and GCP, billed by consumption (per-credit)."

# Classification
entity_type: Company
target_market: [B2B, B2G]
offering_category: [Software / SaaS, Marketplace / Platform]
portfolio_shape: Multi-product
business_model: Usage-based / Consumption
primary_industry: Technology

# Visual identity
logo_url: https://www.snowflake.com/etc.clientlibs/snowflake-site/clientlibs/clientlib-react/resources/favicon-96x96.png?v=3  # STRAIN: branding.images.logo is an inline data-URI SVG; fell back to favicon per SCHEMA
brand_colors: { primary: "#249EDC", background: "#FFFFFF" }   # Snowflake sky-blue on white; vision-confirmed against screenshot
fonts: [Texta, Lato]               # Texta = headings, Lato = body (branding payload + verified)
color_scheme: light
design_framework: Adobe Experience Manager (AEM)   # read from rawHtml: etc.clientlibs, cq-, data-cmp, /content/dam/ — React client layer (clientlib-react)
---

## Overview

Snowflake is an enterprise cloud-data platform it markets as "The AI Data Cloud" — a single, fully-managed service that ingests, stores, processes, analyzes, governs, and shares data, and increasingly runs AI/ML and agents on it. It runs on top of AWS, Azure, and GCP (not its own datacenters), separating storage from elastic compute so customers pay only for what they consume. The pitch is consolidation: collapse data silos and a fragmented tooling stack onto one governed platform spanning the full data lifecycle. It sells to large enterprises (12,062 customers, 766 of the Forbes Global 2000) and is a public company (NYSE: SNOW) led by CEO Sridhar Ramaswamy.

## What they offer

One platform sold as a set of distinct **workloads** plus a fast-growing AI layer. Consumption-based; no per-seat tiers — pricing is per compute "credit" by edition (below).

- **Platform / core engine:** the fully-managed data cloud — elastic compute, optimized storage, security & governance, cross-cloud. "Easy. Connected. Trusted."
- **Data Engineering:** "reliable, continuous data pipelines for the enterprise in the language of your choice." (Openflow ingestion, Snowpark.)
- **Analytics:** "data analytics faster with optimal pricing and near-zero maintenance."
- **AI (Cortex AI + Snowflake ML):** "Securely create and deploy LLMs and ML models customized with your data." Hosts third-party frontier LLMs in-perimeter — **Anthropic (Claude)** and **Meta (Llama)** named — plus Cortex Analyst, Cortex Search, Notebooks, Model Registry.
- **Applications & Collaboration:** live data sharing across clouds/orgs, the **Snowflake Marketplace** (3,400 listings), and Native Apps.
- **Snowflake Intelligence:** the headline agent product — "any user can securely talk to all your company's data… using plain English" via a personalized enterprise agent.
- **Notable platform features:** Cortex Code, Horizon Catalog (governance/universal AI catalog), Snowflake Trail (observability), Openflow, Notebooks, and **Snowflake Postgres** (managed Postgres, now GA) and Apache Iceberg open-table-format support.

## How it works / model

- **Delivery:** SaaS on AWS/Azure/GCP; "Start for free" self-serve signup (signup.snowflake.com) and enterprise "Contact Sales" / "Talk to Sales" for VPS and large deals.
- **Monetization — consumption (per-credit) + storage:**
  - **Standard:** "$2.00 / per credit ($USD)" — "entry-level… core functionality."
  - **Enterprise:** "$3.00 / per credit" — "Most Popular… high-growth, large-scale customers."
  - **Business Critical:** "$4.00 / per credit" — "highly regulated industries… sensitive data." (Tri-Secret Secure, private connectivity, failover.)
  - **Virtual Private Snowflake (VPS):** "Talk to Sales" — Business Critical features in a fully isolated environment.
  - **On-Demand Storage:** "$23.00 per TB / per month ($USD)" (after compression). "Two ways to buy: On-demand or pre-paid capacity." (Prices = AWS / US East N. Virginia list; vary by cloud/region/edition.)
- **Journey:** free trial → consumption ramps as workloads land → enterprise expands via committed-use/pre-paid capacity and higher editions; heavy migration motion (free code-conversion tools, migration-partner ecosystem) to pull workloads off on-prem/legacy warehouses.

## Positioning & audience

Targets enterprise data & AI leaders; competes with the cloud-native warehouse/lakehouse field (Databricks, Google BigQuery, AWS Redshift, Microsoft Fabric). Claimed edge is the triad **"Easy. Connected. Trusted."** — a fully-managed, near-zero-maintenance platform; interoperability with open table formats (Iceberg) and a cross-cloud data-sharing network; enterprise-grade security/governance for regulated workloads. The 2026 narrative is overtly **agentic AI** ("Making AI Real for Business," Snowflake Intelligence, Cortex agents) and recent moves (intent to acquire Natoma for agent connectivity; a $6B AWS commitment for enterprise agentic AI) reinforce it. Claimed **354% reported ROI**.

## Nav structure

Mega-menu flyouts are client-rendered (not in markdown); below is reconstructed from the footer, per-page sub-navs, and homepage cards.

```
- Product — /en/product/
  - Platform — /en/product/platform/
  - Snowflake Intelligence — /en/product/snowflake-intelligence/
  - Data Engineering — /en/product/data-engineering/
  - Analytics — /en/product/analytics/
  - AI — /en/product/ai/
    - Cortex AI — /en/product/features/cortex/
    - Snowflake ML — /en/product/features/end-to-end-ml-workflows/
  - Applications & Collaboration — /en/product/applications-and-collaboration/
  - Features: Cortex Code, Marketplace, Notebooks, Openflow, Horizon Catalog,
    Snowflake Trail, Snowflake Postgres — /en/product/features/*
  - Pricing — /en/pricing-options/
- Solutions
  - Industries — /en/solutions/industries/ (Financial Services, Healthcare & Life Sciences,
    Manufacturing, Public Sector, Retail & Consumer Goods, Telecom, Technology,
    Advertising/Media & Entertainment)
  - Professional Services — /en/solutions/professional-services/
- Why Snowflake — /en/why-snowflake/
  - Partners — /en/why-snowflake/partners/
- Resources — /en/resources/ (Library, Live Demos, Fundamentals, Training,
  Certifications, Snowflake University, Documentation — docs.snowflake.com)
- Developers — /en/developers/
- Company — /en/company/overview/ (About, Leadership & Board, Careers, Investor Relations,
  Trust Center, Newsroom, ESG, Snowflake Ventures, End Data Disparity)
```

## Credibility & proof

- **Scale stats:** "12,062 Global Customers" (as of Jul 31 2025); "6.3B Average Daily Queries"; "3,400 Marketplace Listings"; "Over 7,200 brands" (pricing page); "766… Forbes Global 2000 companies that use Snowflake."
- **Customer logos / case studies:** Booking.com, Fanatics, Toyota Motor Europe, Indeed, BlackRock (Aladdin), AT&T, Warner Music Group, Western Union, Pizza Hut, NatWest, Siemens, Sanofi, DoorDash, NYC Health+Hospitals, Roku, Penske, Canva, Kraft Heinz, Cisco — with quantified outcomes (e.g., Indeed "43–74% cost savings" querying Iceberg).
- **Partnerships:** LLM providers Anthropic & Meta in-platform; official data-collaboration partner of **Team USA / LA28 Olympic & Paralympic Games**; broad partner network + Snowflake Ventures.
- **Trust/governance:** Trust Center (trust.snowflake.com), FedRAMP/Gov cloud regions (incl. DoD), Business Critical edition for regulated data.
- **Awards:** Forbes Cloud 100, CNBC Disruptor, InfoWorld Technology of the Year, LinkedIn Top Startups, multiple Best Places to Work (through 2026).
- **Company footprint:** founded ~2012; "6,780+ employees… over 40 offices worldwide (as of October 2023)"; CEO Sridhar Ramaswamy.

## Visual & brand impression

Mature, polished enterprise-tech identity. Clean light theme — white backgrounds, generous whitespace, the signature **sky-blue (#249EDC)** as the single dominant accent on pill-shaped CTAs, paired with cool grays and occasional deep-navy/purple section blocks. Big condensed display headings (Texta) over readable Lato body; high-production lifestyle photography and 3D product-UI renders (Cortex Agents dashboards). The overall read is confident, modern, and corporate — the visual language of a category-leading public SaaS company, not a scrappy startup. AI/agents motifs are front-and-center across the homepage and event banners (Summit 26, Dev Day).

## Strategic read

The whole site is mid-pivot from "cloud data warehouse" to **"AI Data Cloud" / agentic enterprise** — Snowflake Intelligence is the hero, Cortex AI is woven through every workload, and the homepage tagline is literally "Making AI Real for Business." The defensible asset underneath the AI messaging is the **governed, cross-cloud data platform + data-sharing network/Marketplace** (3,400 listings, network effects) that the AI features sit on. Consumption pricing means growth = workload migration, hence the heavy migration tooling and the Postgres/Iceberg/open-format plays to absorb adjacent data estates. Watch the Anthropic relationship: Claude is a named in-perimeter LLM and Anthropic's president shares the Summit keynote — Snowflake is positioning as a neutral host for frontier models rather than competing on its own foundation model.

## Provenance

- **Pages:** 7 analyzed via Firecrawl scrape (maxAge:0, location US, all-formats homepage) — homepage, platform, workloads (product overview), ai, pricing, about, why_snowflake; plus a 490-URL map (sample, ~95% docs.snowflake.com). Synthesis across all pages + homepage screenshot + branding payload.
- **Verify:** all 7 sourceURLs matched requested; all body md5s unique (no §5.1 geo/cache contamination); HTTP 200 on all.
- **Credits:** 5 this run (4 key-page scrapes + verify free) on top of a prior same-day partial (map + homepage + platform + workloads = 4) → 9 total for the captures dir.
- **Couldn't get:** mega-nav flyout contents (client-rendered, absent from markdown — reconstructed from footer/sub-navs); full per-edition × cloud × region price matrix (behind selectors + CreditConsumptionTable.pdf, not scraped); financials (off-site, investor relations).
- **Structured layer (schema 2.2):** ran `fc.py signals` on the persisted 2026-05-31 homepage rawHtml — JSON-LD present but no `sameAs`/`logo`/`alternateName`, so no new structured-layer fields. Re-stamped 2.0→2.2.
