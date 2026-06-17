---
# De-risk probe instance (experiments/) — not a store entry; values validated against modules/cohort-packs/PRODUCTIVITY_SAAS.md.
schema_version: "1.0"
domain: airtable.com
captured_at: 2026-06-16
primary_job: database/spreadsheet/no-code   # "one workspace" is brand-metaphor → does NOT clear multi/suite → center-of-gravity = database/no-code
primary_user: team/org
ai_front_door: hero                          # hero subhead "Build AI-powered workflows…"; /ai "AI-native platform"
pricing_model: per-seat                      # "$20 per seat/month"; "charged per seat"
free_entry: free-tier                        # perpetual Free plan, up to 5 editors
platform_posture: app-platform               # footer links a named "Marketplace" (own-nav-link test) + Templates + Web API
---

## Platform & integrations
- **Platform:** public Web API (footer "API" → /developers/web/api/introduction; pricing lists "Web API" with "API calls per month" 1,000→Unlimited, plus an "Enterprise API"). Own footer links a named **Marketplace** (/marketplace, title "Apps - Airtable Marketplace") **+ Templates** (/templates) **+ Developer docs** ⇒ `app-platform`. Pricing names "Pre-built extensions" + "Scripting and custom extensions" and (Enterprise) an "App Library."
- **Integrations (verbatim, /integrations):** *"Integrate Airtable with your favorite tools to connect your most important business information and build more powerful applications."* Named connectors across categories: Box, ChatGPT, Claude, Databricks, Dropbox, GitHub, Gmail, Google Drive, Jira, Salesforce, Slack, Snowflake, Stripe, Tableau, Twilio, Typeform, Zendesk, … Count not stated as a single number.

## Surfaces
- **Surfaces:** web · iOS · Android · API  *(pricing names iOS/Android; desktop referenced generically but no OS named → not asserted, per "empty over guessed")*

## Jobs
- **Jobs:** a no-code database/app builder spanning records/bases + interface/app building + automations + multiple views (Grid, Kanban, Calendar, Gallery, Gantt/Timeline, Forms, Dashboard) + synced integrations. Hero *"All your teams, all their workflows—connected in one workspace"* is a **brand-metaphor "one workspace"** that does **not** enumerate replacement → does **not** clear `multi/suite`; center-of-gravity ⇒ `database/spreadsheet/no-code`.

## AI
- **AI:** front-door. Homepage subhead *"Build AI-powered workflows that unify data… No code required."* /ai H1 *"AI that's built for the way your business actually works"* + *"AI-native platform… intelligent agents."* Named: **Omni** ("your Airtable sidekick"), **Field Agents / AI Field Agents** (tagged NEW), **Airtable AI**. Metered in **AI credits** (Free 500/editor/mo → Enterprise 25,000/paid user/mo; packs "from $120/month for 10k credits").
- **Model provenance (/ai):** *"Enterprise customers decide which models are enabled. Choose between models from Open AI, Anthropic, Meta, and others."* + *"model providers never retain your data and your data is never used for model training."*

## Pricing & packaging
- **Pricing `[published]`:** Free · Team · Business · Enterprise Scale; **per-seat/mo**. Team **$20**/seat (annual; $24 mo); Business **$45**/seat (annual; $54 mo); Enterprise Scale **Custom / Contact Sales** `[on-request]`. Charged only for edit-permission users.
- **Free tier:** $0; up to **5 editors**, 50 commenters; 1,000 records/base; 1 GB/base; 100 automation runs; 1,000 API calls/mo; 500 AI credits/editor/mo.
- **Add-ons:** Portals (guest access, "from $120 for 15 guests/mo"); AI credit packs; Enterprise Key Management. No open-source / source-available license in nav/footer.

## Trust & compliance
- **Trust (/company/trust-and-security):** **SOC 2 Type 2**, **ISO 27001:2022**, **ISO 27701:2019**, **HIPAA**, **TX-RAMP L2**; **GDPR**/UK-GDPR, **CCPA/CPRA**, DPA, EU data residency, **Enterprise Key Management**. SAML SSO, 2FA, record-level revision history. CAIQ/SIG-Lite/HECVAT completed. Bug bounty via **HackerOne**.
- **Named customers:** *"Trusted by 500,000+ … companies worldwide"* (logo strip rendered as images).
- **Status/SLA:** not on pages scraped.

*Capture note: homepage hero via WebFetch (Firecrawl timed out 2×); /marketplace body is JS-gated, so `app-platform` rests on the footer link label (title confirmed "Apps - Airtable Marketplace").*
