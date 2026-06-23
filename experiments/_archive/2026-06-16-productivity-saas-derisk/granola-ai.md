---
# De-risk probe instance (experiments/) — not a store entry; values validated against modules/cohort-packs/PRODUCTIVITY_SAAS.md.
schema_version: "1.0"
domain: granola.ai
captured_at: 2026-06-16
primary_job: meeting-notes/recording
primary_user: individual/prosumer
ai_front_door: hero
pricing_model: per-seat
free_entry: free-tier
platform_posture: has-API/integrations
---

## Platform & integrations
- **Platform:** Public API + MCP, no third-party app directory in its own nav ⇒ `has-API/integrations` (not `app-platform`). The Business tier lists **"API access"** and **"MCP integration in all your apps"** (/pricing), and **"Advanced integrations with Attio, Notion, Slack, Hubspot, Affinity, and Zapier"** — a first-party integration list, not a marketplace. The homepage "Granola MCP Connector" section frames the direction *inward*: **"Connect Granola in a few clicks and your AI apps become aware of your meeting notes"** (logos shown: Bolt, Figma, Manus, Replit, OpenAI, Claude, Cursor, Lovable, Tasklet, v0, Duckbill) — these are apps Granola feeds, not apps built on Granola. **No marketplace/gallery/template-directory link anywhere in nav or footer** — the footer's "Product" column is Pricing / Enterprise / AI notepad vs notetaker / use-cases / Explore. API availability: **public** (page-attested via "API access" on a paid tier; no /developers or /api docs page surfaced in nav).

## Surfaces
- **Surfaces:** macOS · Windows · iOS · API — hero states **"Available for macOS, Windows, iPhone"**; security page: "Granola is an app for Desktop and iPhone." No web app, no self-hosted (Enterprise FAQ on security page asks "Can I use a version of Granola in a private cloud?" but the answer is not rendered, so not attested).

## AI
- **AI:** AI is the product's spine, not a feature. Two named AI surfaces: the **Notepad** ("The AI notepad for back-to-back meetings" — uses computer audio to transcribe and "uses meeting context to write clear notes") and **Chat** ("AI chat that already knows what you're working on" / "Granola Chat — Perfect meeting memory," nav). Function: transcribes meeting audio without a bot, then generates/enhances notes, briefs, action items, and follow-ups; cross-meeting Q&A via Chat. **Model provenance is page-stated** (security page): "Granola uses best-in-class transcription providers (like **Deepgram and Assembly**) and AI providers (like **OpenAI and Anthropic**)"; "We do not allow third parties (like OpenAI or Anthropic) to use your data to train their AI models"; "Granola trains on your anonymized data ... You can opt out"; Enterprise has model training off by default. "Bring your own models" appears as an unanswered Enterprise FAQ (security page) — not attested.

## Pricing & packaging
- **Pricing:** `[published]` — three tiers, all **"per user per month"**: **Basic $0** ("Great for a free taste of Granola"), **Business $14** ("Great for individuals or small teams"), **Enterprise $35** ("Great for larger companies"). Per-seat meter ⇒ `pricing_model: per-seat`. Free entry is a **perpetual free tier**, not a trial: homepage states **"Unlimited meeting notes for free. Take as many notes as you'd like. Upgrade to view and work with notes older than 30 days"** and Basic lists "See limited meeting history" ⇒ `free-entry: free-tier`. Business unlocks "Unlimited meeting notes and history," advanced AI models, the integrations above, API + MCP, centralized billing. Enterprise adds SSO, SCIM, admin controls, org-wide retention. No annual/monthly toggle shown (monthly pricing only). Granola contributes "1.5% of your subscription" to Stripe Climate.

## Trust & compliance
- **Trust:** **SOC 2 Type 2** — security page ("our security practices meet SOC 2 Type 2 standards") and enterprise page ("SOC 2 Type II certified"). **GDPR** — "committed to GDPR compliance," DPA available on request. Public **Trust page** (trust.granola.ai) and public **status page** (status.granola.ai, footer); public Vulnerability Disclosure Policy + three published security post-mortems. **SSO/SAML + SCIM provisioning** on Enterprise. Data: US-hosted AWS VPC, encrypted at rest/in transit, no stored audio recordings. **HIPAA: not confirmed** — the pricing FAQ poses "Is Granola SOC 2 / HIPAA compliant?" but the answer is collapsed/unrendered; no affirmative HIPAA claim on any captured page. **Named customers/logos:** Brex, Vercel, Zapier, Vanta, Linear, PostHog, Intercom, Ramp, Mercury, Replit, Cursor, Bumble, Index Ventures (homepage logo wall + pricing/enterprise case studies). Enterprise stats cited: "260+ hours saved annually per user," "69% adoption ... within 6 months."
