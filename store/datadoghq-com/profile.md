---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.2"

# Identity
domain: datadoghq.com
name: Datadog
aliases: [datadog.com]
parent: []
owns: []
socials: { x: "https://twitter.com/datadoghq", instagram: "https://www.instagram.com/datadoghq/", facebook: "https://www.facebook.com/datadoghq/", linkedin: "https://www.linkedin.com/company/datadog", github: "https://github.com/DataDog", youtube: "https://www.youtube.com/channel/UCPO2QgTCReBAThZca6MB9jg" }   # JSON-LD sameAs
external: { wikipedia: "https://en.wikipedia.org/wiki/Datadog" }   # JSON-LD sameAs — third-party record

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Marketing site is Hugo-generated (static) with React/webpack widgets; brand purple #632CA6, font NationalWeb (Klim 'National'). `map` is overwhelmingly docs.datadoghq.com noise (~480/500 URLs) — the homepage mega-nav is the real discovery surface for marketing/product pages. Product catalog is huge (~90 products under 7 pillars) — captured the shape, not every product page. Pricing page is one giant per-product table (~330KB md); prices are per-host/per-GB/per-million-events, mostly metered. Founders + full exec/board bios on /about/leadership/. Marketo demo form + 'Marketo Forms 2 proxy' boilerplate trails every page (ignore)."
key_pages:
  product: /product/
  pricing: /pricing/
  leadership: /about/leadership/
  analyst: /about/analyst/
  customers: /customers/
  solutions: /solutions/
unverified_fields:
  - "Pricing here is a representative sample of headline per-host/per-GB rates — the full per-product matrix (~90 products, many tiers) is on /pricing/ but not transcribed line-by-line; treat the table as the source."
  - "Headcount, revenue, funding not on captured pages (public co., NASDAQ: DDOG — financials are a deep-research/IR job, not this capture)."

# Description — one sentence
description: "A cloud observability and security SaaS platform that unifies infrastructure, application, log, network, user-experience, and security monitoring for engineering and security teams across one usage-metered platform of ~90 products."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2B]
offering_category: [Software / SaaS]
portfolio_shape: Catalog   # ~90 products across 7 pillars — too many to enumerate as SKUs; capture the shape (pillar × product)
business_model: Usage-based / Consumption   # per-host + per-GB + per-million-events metering, with committed-use discounts; Free tier funnels in
primary_industry: Technology

# Visual identity
logo_url: https://corp.dd-static.net/img/dd_logo_n_70x75.png
brand_colors: { primary: "#632CA6", accent: "#7700FF" }
fonts: [NationalWeb]
color_scheme: light
design_framework: hugo   # from rawHtml — Hugo static generator + React/webpack widgets (not the branding payload)
---

## Overview

Datadog is a SaaS observability-and-security platform that gives engineering, operations, and security teams unified, real-time visibility into modern cloud stacks. It started as infrastructure monitoring and has expanded into a single platform spanning observability (infra, APM, logs, network, RUM), security (cloud, code, SIEM, app protection), digital experience, software delivery, service management, and a fast-growing AI layer. The pitch — "See inside any stack, any app, at any scale, anywhere" — is consolidation: replace many point tools with one correlated platform where metrics, traces, logs, and security signals share context. Sold to businesses (developers through enterprises), public company (NASDAQ: DDOG), HQ New York.

## What they offer

A broad **Catalog** of ~90 products organized under 7 platform pillars (mega-nav taxonomy). Pricing is mostly **metered** (per host, per GB ingested, per million events) with Free/Pro/Enterprise tiers and committed-use discounts; representative headline rates below, verbatim from `/pricing/`:

- **Observability:** Infrastructure Monitoring (Free / Pro **"$15 per host"** / Enterprise), APM (**"$31"** per host, standalone **"$36"**, APM Pro **"$41"**, APM Enterprise **"$47"**), Log Management (**"$0.10 per ingested GB"** + indexing/retention; Flex Logs metered per million events), Network Monitoring, Database Monitoring, Continuous Profiler (**"$19 per host"** standalone), Serverless, Metrics, Data Streams/Quality/Jobs Monitoring
- **Security:** Cloud Security (CSPM, CIEM, vuln mgmt, compliance), Cloud SIEM, Code Security (SAST, IAST, SCA, IaC Security, Secret Scanning), App & API Protection, Workload Protection, Sensitive Data Scanner
- **Digital Experience:** Browser & Mobile Real User Monitoring, Session Replay, Product Analytics, Experiments, Synthetic Monitoring, Mobile App Testing, Error Tracking
- **Software Delivery:** Internal Developer Portal, CI Visibility, Test Optimization, Continuous Testing, Feature Flags, Code Coverage, DORA Metrics, IDE Plugins
- **Service Management:** Incident Response, Software Catalog, SLOs, Case Management, Event Management, Workflow Automation, App Builder
- **AI:** LLM Observability, GPU Monitoring, and the **Bits AI** family — Bits AI Agents, Bits AI SRE, Bits AI Security Analyst, plus an MCP Server, Pup CLI, and Agent Directory
- **Platform capabilities:** Dashboards, Alerts, Watchdog (anomaly detection), Notebooks, 900+ Integrations, OpenTelemetry support, Fleet Automation, Governance Console, API, Marketplace

Free tier exists on most products; everything funnels to a free trial → committed annual contract. Per-SKU depth defers to `offerings.md`.

## How it works / model

Customers install the Datadog Agent (or send via OpenTelemetry/integrations) to stream telemetry into the SaaS platform, then turn on whichever products they need à la carte. **Land-and-expand**: start with one product (often Infrastructure or APM) on a Free tier or trial, then expand across pillars as more telemetry and teams onboard. Revenue is **consumption-metered** — billed per monitored host, per GB of logs ingested, per million events/spans, etc. — typically committed annually with on-demand overage, plus enterprise sales for large accounts. Self-serve signup + an enterprise sales motion (Sales/Customer Success reps referenced throughout pricing FAQ) coexist.

## Positioning & audience

- **Audience:** developers, DevOps/SRE, IT operations, and security teams — from startups to large enterprises ("Thousands of customers"). Industry solutions span financial services, healthcare, retail, government, gaming, media, tech.
- **Claimed edge:** one *integrated* platform where observability and security share context, vs. stitching point tools — "AI-Powered Observability and Security," "monitoring consolidation." The AI-native angle (Bits AI agents, Watchdog) is the current headline thrust.
- **Competes with:** New Relic, Dynatrace, Splunk, Grafana, Elastic, plus cloud-native tools and security point vendors — depending on pillar.

## Nav structure

```
- Product — /product/   (mega-nav, 7 pillars)
  - Observability
    - Infrastructure: Infrastructure Monitoring, Metrics, Network Monitoring, Container Monitoring, Kubernetes Autoscaling, Serverless, Cloud Cost Management, Cloudcraft, Storage Management, GPU Monitoring — /product/<slug>/
    - Applications: APM /product/apm/, Universal Service Monitoring, Continuous Profiler /product/code-profiling/, Dynamic Instrumentation, LLM Observability
    - Data: Database Monitoring, Data Streams Monitoring, Data Observability (Quality, Jobs)
    - Logs: Log Management, Sensitive Data Scanner, Audit Trail, Observability Pipelines, Error Tracking, BYOC Logs
  - Security
    - Code Security: Code Security, SCA, SAST, IAST, IaC Security, Secret Scanning
    - Cloud Security: Cloud Security (CSPM, CIEM, Vuln Mgmt, Compliance)
    - Threat Management: Cloud SIEM, Workload Protection, App & API Protection, Sensitive Data Scanner
    - Security Labs — securitylabs.datadoghq.com · Open Source — opensource.datadoghq.com
  - Digital Experience: Browser RUM, Mobile RUM, Product Analytics, Experiments, Session Replay, Synthetic Monitoring, Mobile App Testing, Error Tracking
  - Software Delivery: Internal Developer Portal, CI Visibility /product/ci-cd-monitoring/, Test Optimization, Continuous Testing, IDE Plugins, DORA Metrics, Feature Flags, Code Coverage
  - Service Management: Incident Response, Software Catalog, SLOs, Case Management; Actions: Workflow Automation, App Builder; Agentic: Bits AI SRE, Watchdog, Event Management
  - AI: LLM Observability, GPU Monitoring, AI Integrations; Bits AI Agents / SRE / Security Analyst, MCP Server, Pup CLI, Agent Directory, Watchdog
  - Platform Capabilities: Metrics, Watchdog, Alerts, Dashboards, Notebooks, Mobile App, Fleet Automation, Governance Console, Access Control, DORA Metrics; Collaboration; Extensibility (OpenTelemetry, Integrations, IDE Plugins, MCP Server, API, Marketplace)
- Customers — /customers/
- Pricing — /pricing/
- Solutions — /solutions/   (Industry × Technology × Use Case)
  - Industry: Financial Services, Manufacturing & Logistics, Healthcare/Life Sciences, Retail/E-Commerce, Government, Education, Media & Entertainment, Technology, Gaming
  - Technology: AWS, Azure, Google Cloud, Oracle Cloud, Kubernetes, OpenShift, Pivotal, OpenAI, SAP, OpenTelemetry
  - Use Case: Application Security, Cloud Migration, Monitoring Consolidation, SOAR, DevOps, FinOps, Shift-Left Testing, DEM, Security Analytics, CNAPP, Hybrid/On-Prem Monitoring, Log Analysis, Real-Time BI, Edge/IoT
- About — /about/leadership/
  - Contact, Partners, Newsroom, Events & Webinars, Leadership, Careers, Analyst Reports, Investor Relations (investors.datadoghq.com), ESG Report, Trust Hub
- Blog — /blog/   (The Monitor, Engineering, AI, Security Labs)
- Docs — docs.datadoghq.com · Login — app.datadoghq.com · Get Started (Free Trial)
```

## Credibility & proof

- **Customer logos (homepage):** LG Electronics, Itaú, Perplexity AI, SoFi, MidJourney, Dust AI — "Thousands of customers love & trust Datadog."
- **Analyst recognition:** Leader, 2025 Gartner® Magic Quadrant™ for Observability Platforms; Leader, Gartner MQ for Digital Experience Monitoring (2025); Leader, The Forrester Wave™: AIOps Platforms, Q2 2025 — plus a multi-year history of Gartner APM/Observability and Forrester AIOps placements (`/about/analyst/`).
- **Leadership / founders:** Co-founders **Olivier Pomel** (CEO, ex-Wireless Generation VP Technology, original VLC author) and **Alexis Lê-Quôc** (CTO, ex-Wireless Generation Director of Operations) — both MS CS, École Centrale Paris. Exec team: David Obstler (CFO), Sara Varni (CMO), Adam Blitzer (COO), Yanbing Li (CPO), David Galloreese (Chief People Officer), Sean Walters (CRO), Emilio Escobar (CISO), Kerry Acocella (General Counsel). Board includes Dev Ittycheria (ex-MongoDB CEO), Ami Vora (Anthropic Head of Product), and investors from Index Ventures and ICONIQ.
- **Trust signals:** public company (NASDAQ: DDOG), Trust Hub (/trust/), ESG Report, certification program, dedicated Security Labs research, large partner/marketplace network, free trial with no-card self-serve.

## Visual & brand impression

Polished, confident enterprise-SaaS aesthetic. Light/white base broken by deep-purple and vivid gradient (magenta→blue) feature bands; the signature Datadog purple (#632CA6, with a brighter #7700FF accent) anchors buttons and section fills. Hero pairs a tight headline ("AI-Powered Observability and Security") with a clean product screenshot on white. Lower page mixes product UI captures, the playful purple "join our Pack" careers band, and team photography — humanizing the otherwise dense, technical surface. The footer is an enormous multi-column product index (a deliberate "we do everything" signal). Typeface is NationalWeb (Klim's National), a crisp humanist sans. Overall read: mature, broad, developer-credible, leaning hard into an AI-native refresh.

## Strategic read

The footer's sheer length *is* the strategy — Datadog has gone from single-product (infra monitoring) to an ~90-product platform spanning the full observability + security + delivery lifecycle, betting that buyers consolidate point tools onto one correlated platform. Two current thrusts stand out: (1) **security** is now a co-equal pillar to observability (CNAPP, SIEM, code/app security), pushing Datadog into Wiz/CrowdStrike/Splunk adjacency; (2) an aggressive **AI-native** pivot — the Bits AI agent family, MCP Server, Agent Directory, and a "State of AI Engineering" report position Datadog as both the monitor *of* AI systems (LLM/GPU observability) and an AI-agent operator *within* the platform. The consumption-metered model is the growth flywheel (and the customer's cost-control anxiety — hence Cloud Cost Management and the GovernanceConsole as first-party answers).

## Provenance

- **Pages:** 5 analyzed (Firecrawl scrape, US geo, all-formats): homepage, /product/, /pricing/, /about/leadership/, /about/analyst/. Map captured but ~96% docs-subdomain noise — discovery driven by homepage mega-nav.
- **Verify:** `fc.py verify` — all 5 sourceURLs match, all bodies md5-unique (no §5.1 contamination).
- **Credits:** 6 (1 map + 1 homepage + 4 key pages); ~1463 remaining on the shared key.
- **Couldn't get:** Full ~90-product pricing matrix transcribed line-by-line (sampled headline rates instead); financials/headcount (not on marketing pages — IR/deep-research job). No bot defense or geo issues encountered.
- **Structured layer (schema 2.2):** read this capture's homepage JSON-LD via `fc.py signals` ($0 re-enrichment from the persisted 2026-05-31 rawHtml, hint-to-verify) — filled `socials` (x/ig/fb/linkedin/github/youtube) + `external` (wikipedia); founders already in prose; JSON-LD `logo` lateral to the existing logo — kept current. Re-stamped 2.0→2.2.
