---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: airtable.com
captured_at: 2026-06-17
primary_job: database/spreadsheet/no-code
primary_user: team/org
ai_front_door: hero
pricing_model: per-seat
free_entry: free-tier
platform_posture: app-platform
---

## Platform & Integrations

- **Platform:** public REST-ish Web API: `/developers/web/api/introduction` says the Airtable API integrates Airtable data with "any external system," uses JSON, and has an official JavaScript client plus community clients. Pricing exposes "Web API," "Enterprise API," and "API calls per month" limits: 1,000 on Free, 100,000 on Team, Unlimited on Business and Enterprise Scale.
- **Integrations:** `/integrations` says "Integrate Airtable with your favorite tools to connect your most important business information and build more powerful applications." Named integrations include Box, ChatGPT, Claude, Databricks, Dropbox, GitHub, Gmail, Google Drive, Jira, Salesforce, Slack, Snowflake, Stripe, Tableau, Twilio, Typeform, WordPress, YouTube, and Zendesk.
- **Marketplace:** own nav/footer links a named Marketplace. The captured Marketplace page lists Airtable Extensions, all extensions, scripts, and open-source extensions; it says "The Airtable community has developed and published over 150 open source extensions on GitHub." Own-nav Marketplace + extension directory + API/docs earns `platform_posture: app-platform`.

## Surfaces

- **Surfaces:** web · iOS · Android · desktop · API

## Jobs

- **Jobs:** shared relational data/bases, no-code app building, interfaces, automations, reporting, views, sync/integrations, templates, portals, and AI agents. The homepage's "connected in one workspace" line is a brand metaphor, not an enumerated suite-replacement claim; center of gravity is the database/spreadsheet/no-code app-builder job.

## AI

- **AI:** front-door. Homepage subhead says "Build AI-powered workflows"; `/platform` calls Airtable an "AI-native app platform"; `/platform/ai` names Omni as an AI app builder, data analyst, and web researcher, and Field Agents as AI-powered researchers, analysts, and content creators that perform workflow tasks at scale. Airtable also lists AI Plays such as campaign concepts, event attendee research, product-content merchandising, and marketing customer insights.
- **Model provenance:** `/platform/ai` says Enterprise customers can choose models from Open AI, Anthropic, Meta, and others; it also says model providers never retain customer data and customer data is never used for model training, with an Amazon Bedrock option.

## Pricing & Packaging

- **Pricing:** Free · Team · Business · Enterprise Scale. Team is "$20USD per seat/month billed annually" ($24 billed monthly); Business is "$45USD per seat/month billed annually" ($54 billed monthly); Enterprise Scale is "Custom pricing" / Contact Sales. Pricing FAQ says Airtable plans are charged per seat, and Team/Business charge users with edit permissions.
- **Free entry:** Free plan for individuals or very small teams; includes up to 5 editors, 1,000 records/base, 1 GB attachments/base, 100 automation runs, Interface Designer, and 500 AI credits per editor each month.
- **Usage overlay:** AI credits are included by plan (500/editor/month Free, 15,000/paid user/month Team, 20,000 Business, 25,000 Enterprise Scale at list price). AI credit packs start at "$120/month for 10k credits."
- **Add-ons:** Portals start at "$120/month for 15 guests" or "$150/month for 15 guests" depending on plan; Enterprise Scale says Contact Sales. EKM and professional services are add-on/gated.

## Trust & Compliance

- **Trust:** `/company/trust-and-security` names SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27701:2019, HIPAA, TX-RAMP Level 2, GDPR/UK GDPR, CCPA/CPRA, CAIQ, SIG Lite, HECVAT, Enterprise Key Management, EU data residency, and a HackerOne bug bounty. Pricing also lists SAML SSO, SCIM user provisioning, audit logs, DLP, eDiscovery, HIPAA Compliance, and Enterprise Key Management.
- **Customers:** homepage/platform/about pages claim 500,000+ organizations and show named enterprise customers/logos; about page says 80% of the Fortune 100.
- **Status:** public status page captured at `status.airtable.com`; no SLA language was captured on the marketing/pricing pages.
