---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: 1

# Identity
domain: aws.amazon.com
name: Amazon Web Services (AWS)
aliases: []
parent: [amazon.com]              # subsidiary of Amazon; runs its own P&L and sells directly → Company, not Brand
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "AWS proprietary 'libra-css' marketing stack (a0.awsstatic.com/libra) — NOT Next.js (corrects an old playbook note); rawHtml shows no __NEXT_DATA__/webpackJsonp, the lone '_next' substring is incidental. Mega-nav (Products/Solutions/Pricing/Resources) is client-rendered — collapsed/empty in homepage markdown; reconstruct the offering taxonomy from /products + footer, not the top nav. Product & pricing catalogs are paginated client-side (homepage map shows only 8 of 231 products / 180 priced) — the counts are the signal, not the list. Map is huge and dominated by docs.aws.amazon.com + /blogs noise; pull canonical marketing roots (/products, /about-aws, /pricing) via `map --search`, not the default sample. Company self-description lives on /what-is-aws + /about-aws (homepage is a thin marketing shell)."
key_pages:
  what_is_aws: /what-is-aws/
  products: /products/
  pricing: /pricing/
  free_tier: /free/
  about: /about-aws/
  our_origins: /about-aws/our-origins/
  security: /security/
  global_infrastructure: /about-aws/global-infrastructure/
unverified_fields:
  - "Product/service count — site states 231 products listed (180 with pricing pages); treat as a point-in-time catalog size, not a fixed number."
  - "Headcount, revenue, funding — not on the marketing site (reported at the Amazon parent level); a deep-research job, not capture."

# Description — one sentence
description: "The world's most broadly adopted cloud platform: 200+ on-demand compute, storage, database, networking, security, and AI/ML services billed pay-as-you-go, serving startups, enterprises, and governments. An Amazon subsidiary, launched 2006."

# Classification — closed sets (see TAXONOMIES.md)
entity_type: Company
target_market: [B2B, B2G]
offering_category: [Software / SaaS]
portfolio_shape: Catalog
business_model: Usage-based / Consumption
primary_industry: Technology

# Visual identity — branding payload is a hint; confirmed against screenshot
logo_url: https://a0.awsstatic.com/libra-css/images/site/fav/favicon.ico   # branding logo is an inline data-URI SVG (the navy "Smile" wordmark) → favicon fallback
brand_colors: { primary: "#161D26", secondary: "#0073BB" }   # primary = near-black navy wordmark/nav; secondary = signature AWS blue (links/accents). See Visual note.
fonts: [Amazon Ember, Amazon Ember Display]
color_scheme: light
design_framework: custom            # AWS proprietary "libra-css" marketing stack (read from rawHtml: awsstatic/libra markers; no Next.js)
---

## Overview

Amazon Web Services is the cloud-computing arm of Amazon, launched in spring 2006 when Amazon S3 (storage) and then EC2 (compute) first let any organization rent infrastructure on demand instead of building it. Two decades on, AWS sells a catalog of **231 listed cloud services** spanning compute, storage, databases, networking, security, analytics, and a deep generative-AI stack (Amazon Bedrock, Nova, Quick) — positioned as "the world's most comprehensive and broadly adopted cloud." It serves the full market spectrum: fastest-growing startups, the largest enterprises, and "leading government agencies." Customers consume services à la carte and pay only for what they use.

## What they offer

A catalog too large to enumerate (231 services across ~25+ categories); the shape is what matters — capture by category, not by SKU:

- **Compute:** EC2 (the original 2006 service), App Runner, App2Container, plus serverless/containers
- **Storage:** S3 (the original 2006 service), tiered by access frequency
- **Databases:** Aurora, RDS, Redshift, and managed engines
- **Networking & content delivery:** CloudFront, App Mesh, VPC, Network Firewall
- **Security, identity & compliance:** Cognito, Inspector, CloudHSM, Certificate Manager, GuardDuty — a flagship pillar ("security is our top priority")
- **AI / ML & generative AI:** Amazon Bedrock (incl. Nova models, agentic AgentCore), Amazon Quick (work AI assistant), SageMaker
- **Developer tools:** Amplify, App Studio, SDKs & CLI
- **Application integration, migration, business applications, analytics, supply chain** — and more

Adjacent surfaces: **AWS Marketplace** (third-party software), **AWS Partner Network**, **AWS Training**, and the **AWS Free Tier** (sign-up grants "$100 in AWS Free Tier credits right away, plus up to $100 more," services free for up to 6 months within limits). Per-service depth is an `offerings.md` job, not Tier-0.

## How it works / model

Self-service: customers create an account, consume services through the AWS Console / APIs / SDKs, and are billed by usage. Pricing is explicitly utility-style — *"AWS pricing is similar to how you pay for utilities like water and electricity. You only pay for the services you consume."* Four published payment shapes:

- **Pay-as-you-go:** the default for the "vast majority" of services — no long-term contracts or upfront commitment
- **Save when you commit:** Savings Plans — lower rates on Compute & ML for a committed $/hour over a 1- or 3-year term
- **Pay less by using more:** tiered volume discounts (e.g. S3 storage and EC2 data-transfer-out)
- **Flat rate:** bundled-service plans with simple monthly billing, no overage
- **Private Pricing:** negotiated discounts on 200+ services in exchange for a usage commitment (enterprise / direct or via partners)

Revenue is metered consumption at scale; the Free Tier is the top-of-funnel acquisition lever.

## Positioning & audience

Targets businesses, developers, and the public sector (B2B + B2G) — from college-dorm startups to the largest enterprises and "the most security sensitive organizations like government, healthcare, and financial services." The claimed edge is **breadth + reach + trust**: "the greatest choice of innovative cloud and AI capabilities… on the most extensive global infrastructure, with industry-leading security, reliability, and performance." The current homepage hero leads with **security** ("Meet your unique security requirements… protecting even the most sensitive workloads—including government, financial services, and healthcare"), and AI is the loudest product motion (agentic-AI launch livestreams, Nova cost-reduction case studies). Competes against Microsoft Azure and Google Cloud, though neither is named on-site.

## Nav structure

Top mega-nav (Products / Solutions / Pricing / Resources) is client-rendered and did not render into markdown; reconstructed from /products taxonomy + footer:

```
- Products — /products/  (231 services, filterable by category: Compute, Storage, Databases,
    Networking, Security/Identity/Compliance, AI/ML, Developer Tools, Migration,
    Application Integration, Business Applications, Analytics, Supply Chain, …)
- Solutions — /solutions/  (by industry + by use case)
  - Industries — /industries/ : Financial Services, Healthcare & Life Sciences, Government,
      Telecom, Advertising & Marketing, Manufacturing, Media & Entertainment, Games (+10 more)
- Pricing — /pricing/  (Overview · Free Tier · Cost Optimization · Resources)
- Free Tier — /free/
- About AWS — /about-aws/  (Our Origins · Our Values · Our Impact · Our People ·
    Our Customers and Partners · Global Infrastructure · Sustainability)
- Security — /security/  (Security Services · Use Cases · Compliance · Data Protection · Partners)
- Marketplace — /marketplace
- Resources — Getting Started · Training · Architecture Center · Builder Center · re:Post · FAQs
```

## Credibility & proof

- **Scale claim:** "the world's most comprehensive and broadly adopted cloud"; "powered innovation for 20 years"; "the largest global community of innovators"
- **Named customers (homepage carousel):** Pinterest (600M monthly users on EC2/S3), Toyota, Siemens Mobility, Cox Automotive, Intuit (100M+ customers), Adidas, Tapestry, Fortinet, BMW Group
- **Analyst validation:** points to Gartner and IDC analyst reports
- **Compliance posture:** government FedRAMP High / DoD IL-4/5 in AWS GovCloud (US) referenced; "architected to be the most secure global cloud infrastructure"
- **Heritage:** continuous operation since 2006; current CEO Matt Garman was AWS's first product manager

## Visual & brand impression

Mature, enterprise-grade, restrained. A **light** layout — white page canvas with a near-black navy (#161D26) global nav and footer, and the signature AWS blue (#0073BB) for links/accents. The hero pairs a sober security headline with a bright, playful 3D-cube illustration (orange/blue/rainbow) on a warm cream panel — a deliberate softening of an otherwise corporate, information-dense, card-grid page (case-study carousels, an industry matrix, free-tier CTAs). Type is Amazon's proprietary **Amazon Ember** family. Tone reads professional and builder-oriented, medium-energy; the recognizable AWS "Smile" arrow wordmark renders in navy here rather than its classic orange. Overall: the confident, utilitarian polish of a category-defining infrastructure incumbent, not a flashy DTC brand.

## Strategic read

AWS is the canonical `Catalog` entity — its breadth (231 services) is itself the moat and the product, so the durable Tier-0 read is the *shape* (category map + consumption model), not any SKU. Two things stand out in this capture: (1) the homepage now leads with **security for regulated/government workloads**, not raw compute — a defensive, trust-first posture aimed at the highest-value, stickiest segment; and (2) **generative AI is the dominant new-product motion** (Bedrock/Nova/Quick/agentic AgentCore saturate the "What's new" and case-study slots), the lever AWS is using to reframe a 20-year infrastructure franchise as the AI build platform. The pay-as-you-go + commit-to-save pricing ladder is the consumption-economics flywheel that makes it hard to leave.

## Provenance

- **Pages:** 7 analyzed via Firecrawl (`maxAge:0`, `location:US`, all-formats homepage) — homepage, /what-is-aws/, /products/, /pricing/, /about-aws/, /about-aws/our-origins/, /security/; plus 2 `map` calls (1 sample + 1 `--search` for products/about canonical roots).
- **Verify:** all 7 sourceURLs matched; all 7 body md5s unique — no geo/cache contamination. All HTTP 200, basic proxy.
- **Credits:** 10 (2 map + homepage + 6 key pages + 1 map-search). Remaining headroom ~1451.
- **Couldn't get:** full product/pricing catalogs (client-side paginated — only first 8 of 231/180 render; counts captured, not the lists); mega-nav flyout contents (client-rendered, not in markdown — taxonomy reconstructed from /products + footer); headcount/revenue/funding (Amazon-parent financials, off the marketing site).
