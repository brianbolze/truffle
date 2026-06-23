---
# De-risk probe instance (experiments/) — not a store entry; values validated against modules/cohort-packs/PRODUCTIVITY_SAAS.md.
schema_version: "1.0"
domain: calendly.com
captured_at: 2026-06-16
primary_job: scheduling/booking
primary_user: individual/prosumer
ai_front_door: absent
pricing_model: per-seat
free_entry: free-tier
platform_posture: has-API/integrations
---

## Platform & integrations
- **Platform:** Public API + integration catalog, **no** third-party app directory in its own nav ⇒ `has-API/integrations`. Integration claim quoted verbatim: *"Connect Calendly to the tools you already use — Boost productivity with 100+ integrations"* (homepage); the /integration page positions *"Integrate Calendly, boost productivity."* API availability: **public** — footer links *"API & connectors"* and *"Developer tools"*; /integration card *"Calendly APIs — Leverage Calendly's APIs for custom Calendly integrations within your product"* and a *"Build With Us… Visit our Developer Portal to explore our API docs"* (developer.calendly.com). Custom webhooks page-stated. The catalog is a directory of connectors Calendly integrates *with* (Zoom, Salesforce, HubSpot, Zapier, Make, Stripe, a "Claude" AI-assistant connector) — **not** a marketplace of third-party-built apps published into Calendly, so it does **not** clear `app-platform`. Count is a claim, not verified.

## Surfaces
- **Surfaces:** web · iOS · Android · browser-extension (Chrome · Edge · Firefox · Safari) · API. (Footer "Downloads": App Store, Google Play, Chrome/Edge/Firefox/Safari extensions, Outlook add-in. No macOS/Windows desktop app, no self-hosted/OSS.)

## Jobs
- **Jobs:** Lead job is scheduling/booking; the homepage explicitly frames surface area beyond it — *"More than a scheduling link… functionality goes way beyond just a scheduling link"* — spanning Notetaker (*"Meeting recaps and action items"*), Contacts (*"Relationship management tools"*), Payments (*"Flexible ways to get paid"*), routing forms, round-robin/collective events, automated workflows, admin management. Center of gravity is unambiguously **scheduling/booking** (hero, first nav item, `<title>` all lead with scheduling); the adjacent jobs are below the fold and framed as extensions, so this is **not** `multi/suite` (no enumerated "all-in-one/replaces X/Y/Z" claim in the hero).

## AI
- **AI:** AI is **not** on the front door. Homepage hero is *"Easy scheduling ahead"* with zero AI mention. AI surfaces only (a) on /integration as a third-party **"Claude"** connector in an "AI Assistants" category — *"Schedule directly from Claude with Calendly's Claude connector"* — and (b) implicitly via the **Notetaker** product (*"Meeting recaps and action items"*), which is **not** branded "AI" anywhere on the captured homepage hero. No model provenance stated on the pages captured. Placement read: `absent` (hero), with a latent AI-ish capability (Notetaker) living below the fold and an AI integration partner — neither in the H1/subhead/primary CTA.

## Pricing & packaging
- **Pricing:** Free · Standard · Teams · Enterprise `[published]` for the first three; Enterprise `[partial]` (floor shown, *"Starts at $15k/yr — Talk to sales"*). Standard **$10/seat/mo** (billed yearly, *"Save 16%"*), Teams **$16/seat/mo** (*"Recommended plan," "Save 20%"*) ⇒ `per-seat`. Free is *"Always free — For personal use"* (perpetual; capped: **1 event type, connect 1 calendar**) ⇒ `free-tier`. Monthly/annual toggle present (*"Billed yearly / Billed monthly"*); annual = the discounted rate. Paid trial: FAQ states a **14-day trial** that auto-downgrades to Free (so the free tier is genuinely perpetual, not a disguised trial). SSO is a paid **Security add-on** on Teams. No open-source / self-host / license note.

## Trust & compliance
- **Trust:** /security page is explicit. **Certifications (y):** SOC 2 Type 2, SOC 3, ISO/IEC 27001, GDPR, CCPA, CSA STAR (Level One), PCI compliant (via processor). Security capabilities: SSO/SAML, SCIM, encryption in transit (TLS 1.2+) and at rest (AES-256), audit log, data-deletion API, semi-annual pen testing. Vendor security docs shared via **Whistic**; a **security white paper** (PDF) is linked. **Named customer logos:** DoorDash, Lyft, Compass, L'Oréal, Zendesk, Dropbox, Gong, Carnival, Indiana University (homepage); Crocs, Bitly, G2, Pendo (security page). Homepage claims *"Trusted by more than 100,000 of the world's leading organizations"* and *"86% of the Fortune 500."* Public **status page**: calendlystatus.com (footer). Stated scale: *"more than 200,000,000 meetings."
