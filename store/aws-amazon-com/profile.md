---
schema_version: 1

# Identity
domain: aws.amazon.com               # primary key — a SUBDOMAIN of amazon.com; still unique & resolvable, so domain-as-key holds for a subsidiary
name: Amazon Web Services
aliases: [AWS]                        # universally known as "AWS"; legal entity is "Amazon Web Services, Inc."
parent: [amazon.com]                 # AWS is the cloud-computing subsidiary / division of Amazon.com, Inc.
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "MAP EXPLODES worst of the corpus: /v2/map on aws.amazon.com returns ~300 URLs dominated by docs.aws.amazon.com (separate docs host), /blogs/*, /marketplace/*, /solutions/case-studies/*, and ~15 locale prefixes (/ko/ /cn/ /th/ /tr/ /de/ ...) — the actual product catalog is buried. Map is near-useless for key-page selection here; navigate by KNOWN paths instead (/products/, /pricing/, /what-is-aws/, /ec2/, /s3/). CATALOG IS JS-WALLED AT SCALE: /products/ renders only the FIRST alphabetical page of services (Amplify..AppSync) behind a client-side 'Search All AWS Products' filter — you CANNOT scrape the 240+ service list; capture the CATEGORY shape + flagship services instead (grounded in /pricing, /ec2, /s3, and map titles). Top-nav mega-menus (Products/Solutions/Pricing/Resources) are client-rendered — labels only in markdown. Homepage markdown is front-loaded with ~85 lines of cookie-consent boilerplate — skip past it. Stack: React-based on awsstatic CDN (a0/d1.awsstatic.com); branding.designSystem.framework says 'custom' (miss). branding.images.logo is an inline data-URI SVG (not hostable, like linear) — favicon fallback = https://a0.awsstatic.com/libra-css/images/site/fav/favicon.ico. BRAND-COLOR TRAP: branding.colors captured dark-slate UI chrome (#232B37) + console blue (#0073BB) but MISSED the iconic AWS 'Smile' orange #FF9900 entirely — the true brand hue is absent from the payload (a third brand_colors failure mode). fonts[0]=Amazon Ember IS correct here. No geo/cache contamination; US+maxAge:0+waitFor:4000 applied. Parent: footer = '© 2026, Amazon Web Services, Inc. or its affiliates.'"
key_pages:
  products: /products/                              # full service catalog — JS-walled (client-side filter); categories are the capturable shape
  what_is_aws: /what-is-aws/                        # the 'why AWS' / about-equivalent (leadership, infra, security)
  pricing: /pricing/                                # pay-as-you-go + Savings Plans + Private Pricing model
  free_tier: https://aws.amazon.com/free/           # free-tier funnel (referenced from hero CTA)
  ec2: /ec2/                                        # flagship Compute service
  s3: /s3/                                          # flagship Storage service
  global_infra: /about-aws/global-infrastructure/   # Regions / Availability Zones map
  marketplace: /marketplace                         # AWS Marketplace (3rd-party software platform)
  console: https://console.aws.amazon.com           # the actual product (sign-in)
unverified_fields:
  - "Full service list (240+) — JS-walled behind the /products client-side filter; only the category shape + flagship services are captured, not the complete catalog."
  - "Per-service pricing — each service prices on its own /<service>/pricing page; not enumerated. Model captured at /pricing/ (usage-based + Savings Plans)."
  - "Revenue / headcount / segment financials — an Amazon 10-K / earnings fact (AWS is a reported segment of Amazon), not on this marketing site."

# Description — one sentence
description: "Amazon Web Services is Amazon's cloud-computing subsidiary, offering 240+ on-demand, usage-priced infrastructure and platform services — compute (EC2), storage (S3), databases, networking, analytics, and a deep AI/ML stack (Bedrock, SageMaker, Nova) — to businesses, startups, and governments on the world's largest cloud infrastructure."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company          # an OPERATING business (own P&L, brand, domain) — so Company fits, UNLIKE benadryl's Other. But it is a SUBSIDIARY of Amazon; the parent link has no field. See Overview + FINDINGS.
target_market: [B2B, B2G]     # businesses (startups→enterprises) primary; governments/public-sector a strong explicit second (GovCloud, "leading government agencies")
offering_category: [Software / SaaS]   # closest closed value for cloud services. STRAIN: AWS is cloud INFRASTRUCTURE (IaaS/PaaS), not application-SaaS — the taxonomy has no "Cloud Infrastructure / IaaS" value. See body.
portfolio_shape: Catalog      # the SCALE EXTREME: 240+ distinct, separately-priced services across ~25 categories — un-enumerable, captured as shape
business_model: Usage-based / Consumption   # metered pay-as-you-go, + optional Savings Plans / Reserved commitments
primary_industry: Technology  # cloud computing — clean

# Visual identity — lifted from Firecrawl `branding` (homepage pass), confirmed against screenshot
logo_url: https://a0.awsstatic.com/libra-css/images/site/fav/favicon.ico   # branding.images.logo is an inline data-URI SVG (not hostable, like linear); favicon is the URL fallback. The wordmark+Smile-arrow logo is orange.
brand_colors: { primary: "#FF9900", secondary: "#232B37", accent: "#0073BB", background: "#FFFFFF" }   # primary #FF9900 = AWS "Smile" orange, the TRUE brand hue — added from the visual/logo because branding.colors OMITTED it (a new failure mode). secondary #232B37 = dark-slate nav chrome; accent #0073BB = console/link blue. (branding.colors gave only slate+blue+near-black text; see site_notes.)
fonts: [Amazon Ember, Amazon Ember Display]   # branding.fonts[0] correct here (Amazon's house font); Arial/Helvetica/Roboto are fallback-stack noise
color_scheme: light           # verified from screenshot + branding.colorScheme
design_framework: react       # rawHtml react hints on awsstatic CDN; branding.designSystem said "custom" — miss (consistent with the corpus pattern)
---

## Overview

Amazon Web Services (AWS) is **Amazon's cloud-computing subsidiary** — the world's most broadly adopted cloud platform, offering **over 240 services** spanning compute, storage, databases, networking, analytics, security, and an increasingly central AI/ML stack, billed on **usage-based, pay-as-you-go** pricing. It sells to "millions of customers — including the fastest-growing startups, largest enterprises, and leading government agencies." The site (`aws.amazon.com`) is the product-marketing and sign-up front end; the actual product is the AWS Console (`console.aws.amazon.com`).

**Parent / entity boundary (the headline strain — no SCHEMA field):** AWS → **Amazon** (`amazon.com`); legal entity **Amazon Web Services, Inc.**; relationship *subsidiary-of* (the footer reads *"© 2026, Amazon Web Services, Inc. or its affiliates."*). This differs in kind from a product brand like Benadryl→Kenvue: **AWS is an operating business** with its own P&L (a reported Amazon segment), its own brand, and its own domain — which is exactly why `entity_type: Company` fits AWS but not Benadryl. Yet the *same gap* applies: the frontmatter has no `parent` / `subsidiary_of` field, so the link to Amazon is recorded only in prose + `site_notes`. And note the domain consequence: the store could hold **both** `amazon.com` (the retailer) and `aws.amazon.com` (the cloud arm) as distinct domain-keyed entities with nothing structurally linking them — domain-as-key *holds* (it's unique), but it can't express containment.

## What they offer

**240+ services across ~25 categories** — far too many to enumerate (and the live catalog is JS-walled). Captured **breadth-first by category** with verified flagship services (grounded in the homepage, `/pricing`, `/ec2`, `/s3`, and map titles — not from memory). A future `offerings.md` would index the *categories* and a few flagships each, never the full SKU list:

- **Compute** — **Amazon EC2** (resizable virtual servers; the flagship), **AWS Lambda** (serverless functions), **AWS Fargate**, **AWS Batch**.
- **Storage** — **Amazon S3** (object storage; the other iconic service), plus block/file/archive tiers.
- **Databases** — **Amazon Aurora**, **Amazon RDS**, **AWS DMS** (migration).
- **Networking & Content Delivery** — **Amazon VPC**, **Elastic Load Balancing** (NLB/ALB), **AWS PrivateLink**, **Site-to-Site VPN**.
- **AI / ML / Generative AI** (the current center of gravity) — **Amazon Bedrock** (managed foundation models — incl. Anthropic Claude), **Amazon SageMaker**, **Amazon Nova** & **Titan** (Amazon's own models), **Amazon Q** / **Amazon Quick** (AI assistants), **Amazon Transcribe**.
- **Security, Identity & Compliance** — **AWS IAM** / **IAM Identity Center**, **Amazon Inspector**, **Amazon Cognito**, **AWS KMS** / **CloudHSM**, **Security Hub**, **Amazon Detective**, **Network Firewall**, **Certificate Manager**.
- **Analytics** — **Amazon EMR**, plus data-lake / warehouse / streaming services.
- **Application Integration / Dev Tools / Containers** — **Amazon EventBridge**, **AWS CodePipeline**, **AWS CDK**, ECS/EKS, **AWS App Runner**, **AppSync**, **Amplify**.
- **Migration / IoT / Robotics / Business Apps / Media** — **AWS DataSync**, **AWS IoT**, **AWS RoboMaker**, **AWS Supply Chain**, **AWS Elemental**.
- **AWS Marketplace** — a curated catalog of third-party software (a platform/marketplace alongside AWS's own services).

**`portfolio_shape: Catalog` — the scale extreme of the field.** Where Linear is `Single` (one app) and AG1 is `Flagship + companions` (a hero + 3 companions), AWS is `Catalog` at industrial scale: 240+ services, each separately documented, separately adopted, separately metered — you absolutely comparison-shop EC2 vs. Fargate vs. Lambda. The capture lesson is that at this scale the job is *not* enumeration but **portfolio-shape** (categories × flagships), exactly the doro breadth-first rule.

## How it works / model

**Usage-based, pay-as-you-go** is the core model — you pay per unit of consumption (compute-hours, GB-months, requests) with **no upfront commitment**, and can layer on discounts:

- **On-Demand** — the default; pay for what you use.
- **Savings Plans** — commit to a $/hour amount of Compute or ML usage for 1 or 3 years for lower rates.
- **Reserved Instances** — capacity/price commitments.
- **Private Pricing** — negotiated discounts across 200+ services for large committed customers (sales-assisted).
- **AWS Free Tier** — a funnel for new accounts (the hero CTA is "Start free with AWS").
- Tooling: **AWS Pricing Calculator**, Cost Explorer, budgets.

This metered-consumption model is precisely what `business_model: Other` flags — it is neither a fixed Subscription nor a one-time Transaction. Delivery is fully self-serve via the Console, CLI, SDKs, and APIs; enterprise/gov customers get account management and Private Pricing.

## Positioning & audience

- **Who:** B2B across the full size range (startups → enterprises) and **B2G** (government/public sector, regulated industries — financial services, healthcare). Explicitly "millions of customers."
- **Against:** other hyperscale clouds (Microsoft Azure, Google Cloud). The site competes on **breadth** ("greatest choice… over 240 services"), **scale** ("world's largest and most extensive global infrastructure"), **maturity** ("20 years"), and **security/reliability**.
- **Claimed edge:** most comprehensive + broadly adopted cloud; **Gartner Magic Quadrant Leader for Strategic Cloud Platform Services for the 15th straight year**; the most extensive global infrastructure (Regions × Availability Zones); a fast-expanding GenAI stack (Bedrock, Nova, Q) as the current headline.

## Nav structure

Top bar mega-menus are client-rendered (labels only in markdown); structure below is the stable IA reconstructed from the footer + known paths.

```
- Products — /products/  (240+ services, grouped by category: Compute, Storage, Database, Networking,
    Analytics, AI/ML, Security, Containers, Serverless, Dev Tools, Migration, IoT, Business Apps, Media, …)
- Solutions — /solutions/  (by use case + by industry; case studies under /solutions/case-studies/)
- Pricing — /pricing/  (+ Free Tier /free/, Pricing Calculator calculator.aws)
- Resources / Documentation — docs.aws.amazon.com (separate host), /getting-started/, Architecture Center
- Learn — Training & Certification /training/, /what-is/<topic> explainer library
- AWS Marketplace — /marketplace
- Partners — AWS Partner Network /partners/
- Trust / Security — /security/, AWS Trust Center /trust-center/
- Global Infrastructure — /about-aws/global-infrastructure/
- Utility: Contact us · Support · My account · Sign in to Console (console.aws.amazon.com) · Create account
- Footer: © 2026, Amazon Web Services, Inc. or its affiliates
```

## Credibility & proof

- **Analyst:** Gartner Magic Quadrant **Leader for Strategic Cloud Platform Services — 15th consecutive year**, highest on "Ability to Execute."
- **Scale:** "world's largest and most extensive global infrastructure"; "millions of customers"; 20 years operating.
- **Marquee customers (case studies):** Netflix, Pinterest ("600 million monthly users… on EC2 and S3"), BMW Group, Siemens Mobility, Volkswagen, Fortinet — spanning enterprise, automotive, public sector, ISVs.
- **Security/compliance posture:** dedicated Trust Center, "most secure cloud computing environment," trusted by government / financial / healthcare; extensive compliance attestations.

## Visual & brand impression

Enterprise-technical and restrained — **light-mode** content on a **dark-slate (#232B37) top nav and footer**, with **console blue (#0073BB)** for links/secondary actions. The capture surfaces a notable brand-color trap: the **iconic AWS "Smile" orange (#FF9900)** — the logo arrow and "Powered by AWS" mark — appears only as small accents on the page chrome (hero 3D-render shapes), so Firecrawl's `branding.colors` **missed it entirely**, returning only the slate/blue UI palette. The hero pairs an abstract colorful 3D render with the headline "Get the greatest choice of cloud and AI capabilities"; below it, a dense grid of case-study and product cards (BMW, customer logos) in **Amazon Ember** type. Overall read: high-maturity but utilitarian/corporate — built for breadth and credibility, not the editorial polish of a DTC site. This is the **third distinct `brand_colors` failure mode** in the corpus: not "which slot is the brand color" (linear/AG1) but "the brand color isn't in the payload at all."

## Strategic read

The durable state: AWS is the **scale-leader cloud platform**, monetized by **metered consumption** across a 240+-service portfolio, selling breadth + global infrastructure + 20-year maturity to everyone from solo developers to governments. The capture catches it mid-pivot to **generative AI as the organizing narrative** — Bedrock (hosting Anthropic's Claude among others), Amazon's own Nova/Titan models, and Q/Quick assistants are the homepage headliners, and "agentic AI" is the next live-event hook. For a competitor/market read, the structurally interesting facts are (a) it is a **subsidiary** whose performance rolls up into Amazon, and (b) its **usage-based** model and **portfolio breadth** are precisely the two places the current SCHEMA taxonomy has no clean value — see FINDINGS.

## Provenance

- **Pages analyzed (all Firecrawl `/v2/scrape`, 2026-05-30, US locale + maxAge:0 + waitFor:4000):** homepage (`/`, full pass: markdown + html + rawHtml + links + branding + full-page screenshot), `/products/` (catalog hub — JS-walled, first page only), `/what-is-aws/`, `/pricing/`, `/ec2/`, `/s3/` — each markdown + links + screenshot. Site inventory via `/v2/map` (299 URLs, mostly docs/blog/marketplace/locale noise).
- **Raw payloads + screenshots:** `captures/2026-05-30/.payloads/`; cleaned page markdown: `captures/2026-05-30/*.md`.
- **Service catalog** captured as **category shape + flagship services**, grounded in captured pages (homepage, /pricing, /ec2, /s3) and map titles — NOT enumerated (240+ services are JS-walled; see `unverified_fields`).
- **Entity boundary:** AWS is a **subsidiary of Amazon** (`amazon.com`); `entity_type: Company` (it operates as a business) but the parent link has no frontmatter field — recorded in the identity NOTE, `description`, Overview, `site_notes`. Flagged as a SCHEMA gap in the Experiment-3 FINDINGS.
- **Couldn't get:** the full service list, per-service pricing, segment financials (see `unverified_fields`); the true brand orange from `branding` (added from the visual).
