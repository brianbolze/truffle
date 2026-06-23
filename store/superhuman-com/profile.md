---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: superhuman.com
name: Superhuman
aliases: [Grammarly, grammarly.com]   # the company rebranded from Grammarly → Superhuman in 2025; grammarly.com still hosts the Grammarly product + privacy/trust (see Overview)
legal_entity: ""                      # not stated on-site (no ©/legalName captured); privacy policy routes to grammarly.com — noted in prose, not asserted as the legal name
parent: []
owns: [coda.io]                       # "Grammarly acquires Coda" (about page, 2025) — coda.io is the acquired entity's live domain; Superhuman Mail was folded onto this domain
socials:
  linkedin: https://www.linkedin.com/company/superhumanhq
  x: https://x.com/Superhuman
  instagram: https://www.instagram.com/superhuman__hq/
  tiktok: https://www.tiktok.com/@superhumanhq
  facebook: https://www.facebook.com/SuperhumanCo
  threads: https://www.threads.com/@superhuman__hq
external: {}

# Capture meta
captured_at: 2026-06-23
capture_method: firecrawl
site_notes: "Next.js marketing site (the 'super-funnel' funnel app), assets on Contentful CDN (superhumanstatic.com). superhuman.com is now the unified suite/parent brand (formerly Grammarly), not the standalone email client — that's /products/mail. Pricing is the suite-wide /plans (nav 'Pricing' → /plans; /pricing also resolves). Trust center /legal/trust federates out to per-product portals (grammarly.com/trust, coda.io/trust, trust.superhuman.com) — compliance detail lives on the /solutions/enterprise matrix, not /legal/trust. Privacy policy links to grammarly.com. No JSON-LD on homepage; socials from footer."
key_pages:
  pricing: /plans
  platform: /superhuman-platform
  about: /company/about
  go: /products/go-ai-assistant
  mail: /products/mail
  grammarly: /products/grammarly
  coda: /products/coda
  enterprise: /solutions/enterprise
  trust: /legal/trust
  agent_store: /store/agents
unverified_fields:
  - "Coda integration count differs by page: '800+' (homepage, /products/coda) vs '600+' (/solutions/enterprise FAQ) — both recorded verbatim, neither verified."
  - "Compliance certs (SOC 2 Type 2, ISO 27001/27017/27018/27701/42001, SOC 3, PCI DSS, GDPR/CCPA/FERPA) are page-stated on /solutions/enterprise; actual attestations live on per-product trust portals (not captured). ISO 27701/42001 marked 'Coming soon' for some products."
  - "legal_entity not stated on captured pages (privacy policy points to grammarly.com but no legal name/© given)."
  - "Homepage is a marketing funnel ('super-funnel'); hero positioning + AI framing are a point-in-time snapshot, not fixed. Superhuman Go is in Beta (Enterprise early access stated to open February 2026)."

description: "An AI productivity suite — Grammarly rebranded — bundling AI writing (Grammarly), a docs-and-database workspace (Coda), email (Superhuman Mail), and a proactive cross-app assistant (Go) into one per-seat subscription that works everywhere you work."

# Classification
entity_type: Company
target_market: [B2B, B2C]
offering_category: [Software / SaaS]
portfolio_shape: Multi-product
business_model: Subscription
primary_industry: Technology

# Visual identity
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 168, h: 25 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=superhuman.com&sz=256", px: 256, transparent: false }   # dark-maroon rounded-square app icon, baked background → a colored tile on a dark slide
  og:       { src: "https://superhumanstatic.com/super-funnel/main/public/images/v3/social-share.png", w: 2400, h: 1260 }
brand_colors: { primary: "#714CB6", secondary: "#0C4243", accent: "#D4C7FF" }   # purple primary, dark-teal secondary (the "Becoming Superhuman" band + footer), lavender accent/logomark; brand imagery also leans on a deep maroon ground (og/icon)
fonts: [Super Sans VF]               # custom variable display sans; branding.fonts then lists generic CSS fallbacks (Roboto/Oxygen/Ubuntu/Fira Sans)
color_scheme: light
design_framework: next.js            # __NEXT_DATA__ + /_next/ in rawHtml (the "framer" sitemap filename is the Mail subsite, not this site)
---

## Overview

Superhuman is an AI productivity suite that bundles four products — **Grammarly** (AI writing), **Coda** (a docs/database team workspace), **Superhuman Mail** (a fast email client), and **Go** (a proactive AI assistant) — under one brand and one per-seat subscription, pitched as "Superpowers, everywhere you work." The unifying idea is AI that follows you across every app and tab rather than being one more destination.

The company is the **rebranded Grammarly**: per its own timeline, Grammarly (founded 2009) acquired Coda and Superhuman Mail and in 2025 relaunched as "Superhuman," the unified brand, while launching Go. As a result "Grammarly" is now simultaneously the former company name *and* one of the four products in the suite; grammarly.com still hosts the Grammarly product and the privacy/trust pages. Go is delivered today through the Grammarly Chrome/Edge browser extension.

## What they offer

Four suite products, sold as bundled per-seat tiers (not individually priced):

- **Go:** the proactive AI assistant — works in every tab/tool, connects to 100+ apps, "offers help before you even ask"; Chrome/Edge extension (desktop Mac/Windows "coming soon"); included in all plans (free) `[published]`. In Beta.
- **Grammarly:** "AI that's built for better writing" — always-there writing partner across every app, writing agents (tone, rewrites, AI Detector, Plagiarism Checker), Grammarly docs; "trusted by 40M+ users daily"; correctness in 6 languages, paragraph translation in 19 `[published]`
- **Coda:** "the all-in-one AI workspace for teams" — docs + spreadsheet structure + apps, automations, forms, "Connect Slack, Jira, Salesforce, and 800+ tools," Coda AI `[published]`
- **Mail (Superhuman Mail):** "the most productive email app ever made" — Split Inbox, Instant Reply, Auto Drafts/Labels/Summarize, follow-up reminders, Snippets, share & comment; built for Gmail/Outlook; CRM (HubSpot, Salesforce, Pipedrive) read in inbox; "save 4 hours every single week" `[published]`
- **Agent Store + Superhuman Platform:** an "ever-growing roster" of agents built by Superhuman and partners (Gmail, Google Calendar, Jira, Salesforce, HubSpot, Notion, and many more); a no-code Agent Builder, an Agents SDK (closed beta, built on Coda Packs — coda.io/packs), available across "1M+ apps." Catalog-scale — shape captured, agents not enumerated.

Pricing tiers (per member / month, billed annually; all `[published]` except Enterprise):

- **Free:** **$0** — Grammarly + Coda + Go, "for individuals" `[published]`
- **Pro:** **$12** (annual; **$30** monthly) — "for professionals and small teams"; adds unlimited rewrites/translations (19 languages), AI Detector, brand tones, custom-domain docs, 30-day version history `[published]`
- **Business:** **$33** (annual; **$40** monthly) — "best value, for growing businesses"; adds **Mail**, CRM in inbox, unlimited automations/version history, Jira/GitHub/Figma sync `[published]`
- **Enterprise:** **Custom** (Contact Sales) — adds analytics, advanced security/admin controls, SAML SSO, custom roles, DLP, BYOK, dedicated support; "per-user, annual subscription with volume discounts" `[on-request]`

## How it works / model

PLG funnel: free self-serve sign-up ($0 individual tier) → paid per-seat upgrade (Pro/Business) → sales-assisted Enterprise (Contact sales / demo) and a dedicated Education motion (/edu). Recurring per-seat subscription revenue, discounted annually; the suite bundle is positioned as cheaper than buying the products separately. Go anchors the platform as a connective AI layer across a customer's existing tools; the Agent Store / SDK extend it.

## Positioning & audience

Pitched at modern knowledge-work teams and enterprises ("the suite for highly impactful teams"), with a free individual on-ramp inherited from Grammarly's prosumer base. Core claim: instead of adding another destination/tool, Superhuman becomes the AI layer *across* the tools you already use ("eliminate the toggle tax"). Dedicated enterprise and education solutions. Competes against point AI assistants, writing tools (its own Grammarly heritage), doc/workspace tools (Notion via Coda), and email tools (Gmail/Outlook, which Mail sits on top of).

## Nav structure

```
- Product (flyout)
  - Superhuman Go — /products/go-ai-assistant
  - Grammarly — /products/grammarly
  - Coda — /products/coda
  - Superhuman Mail — /products/mail
  - Agent Store — /store/agents
- Enterprise — /solutions/enterprise
- Education — /edu
- Pricing — /plans
- [Contact sales] — /contact-sales   · [Log in] — /auth/signin   · [Sign up] — /auth/signup
Footer:
- Products: Go · Grammarly · Coda · Mail · Agent Store
- Company: Contact Us · About · Mission & Values · Careers · Help Center · Status · Partners · Superhuman Platform
- Legal: Terms · Privacy Policy (→ grammarly.com) · Trust · Customer Business Agreement · Legal Notices · Your Privacy Choices
- Connect: LinkedIn · X · TikTok · Instagram · Threads · Facebook
```

## Credibility & proof

- **Self-reported scale (flagged self-reported):** "40M+ daily active users" / Grammarly "trusted by 40M+ users daily"; "50K+ organizations"; "1M+ apps and websites"; "200B words analyzed daily"; Superhuman Mail "saves teams over 20 million hours every single year."
- **Named customer logos:** HubSpot, Zoom, DoorDash, Zapier, Geico, OpenAI, Expensify, Rivian (homepage/plans "trusted by"); OpenAI, Figma, Cursor, ElevenLabs, Runway, Retool (enterprise page); Mail page adds Function, a16z, HubSpot, Cursor, Brex.
- **Named testimonials:** Jen Igartua (CEO, Go Nimbly); Brandon Sammut (Chief People & AI Transformation Officer, Zapier); Dean Macris (CISO, Dispel); Ben Terrill (former Sr. Director CS, Brex); plus Webflow, Tempo, CedCommerce.
- **Compliance (page-stated on /solutions/enterprise, verbatim; not independently verified — see unverified_fields):** SOC 2 (Type 2) across Go/Grammarly/Coda/Mail; SOC 3; ISO 27001, 27017, 27018; ISO 27701 (Grammarly, Mail — Coda/Go "Coming soon"); ISO 42001 (Grammarly, Coda, Mail — Go "Coming soon"); PCI DSS (Grammarly, Coda); GDPR, CCPA, FERPA; US data centers, encryption in transit and at rest; HIPAA on Enterprise (Grammarly/Coda/Go); BYOK (Grammarly/Mail); legal hold & e-discovery (Coda). "Business customers always have data training off by default."

## Visual & brand impression

Confident, modern, high-energy brand. The signature mark is a lavender (#D4C7FF) rounded-square logomark holding a dark person/navigation-arrow glyph, paired with a heavy geometric all-caps wordmark ("SUPERHUMAN," custom *Super Sans VF*). The palette is multi-tonal: a purple primary (#714CB6), a deep teal-green band (#0C4243, the "Becoming Superhuman" section + footer), lavender accents, and a deep maroon ground used in brand imagery (the og card, the app icon). The homepage itself reads light/airy — a soft purple gradient hero over an off-white body with pastel illustrative product tiles (blue/green/pink). Polished, well-resourced, consumer-grade design maturity; aspirational, human-centered tone ("You're already superhuman").

## Strategic read

This is a consolidation play wearing a rebrand: a single company (ex-Grammarly) folding three formerly distinct products (Grammarly, Coda, Superhuman Mail) plus a new proactive assistant (Go) into one suite and one per-seat bundle, with an agent marketplace/SDK turning it into a platform. The strategic bet is the "AI layer across every app" — Go as connective tissue over a customer's existing stack rather than a new silo. Worth flagging for any consumer: "Superhuman" the brand now means the *suite/company*, not the email client (that's "Superhuman Mail"), and "Grammarly" denotes both the former company and a current product — easy to conflate.

## Provenance

- **Pages:** Analyzed 10 pages via Firecrawl (Next.js, US/en-US, maxAge:0, serial): homepage, /plans, /superhuman-platform, /company/about, /products/{go-ai-assistant, mail, grammarly, coda}, /solutions/enterprise, /legal/trust. Plus map (363 URLs) + homepage branding/rawHtml/screenshot. Structured layer: no JSON-LD on homepage; socials from footer; nav from `<header>` region + screenshot.
- **Verify:** All 10 sourceURLs matched; all bodies md5-unique; no junk soft-404s.
- **Credits:** 11 (1 map + 1 homepage rich + 9 key pages; logos/signals free).
- **Couldn't get:** Per-product trust-portal cert attestations (federated off-site); exact agent count (Catalog-scale); legal entity name (not on-site).
- **Run profile:** express — +productivity_saas cohort pack; +logos (wordmark extracted from inline branding SVG, white fill normalized to currentColor).
