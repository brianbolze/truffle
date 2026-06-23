---
# De-risk probe instance (experiments/) — not a store entry; values validated against modules/cohort-packs/PRODUCTIVITY_SAAS.md.
schema_version: "1.0"
domain: linear.app
captured_at: 2026-06-16
primary_job: project/task-mgmt
primary_user: team/org
ai_front_door: hero
pricing_model: per-seat
free_entry: free-tier
platform_posture: app-platform
---

**Platform & integrations:** Curated third-party integration directory linked from the product's own footer (Features → "Integrations"; Resources → "Developers"). The /integrations page groups apps by category (Essentials, Agents, AI clients, Engineering, Automations, etc.) and explicitly invites third-party building: *"Build your own integration — Create your own integration with Linear's API and submit it to the directory"* (/integrations). Public API + webhooks are page-attested: /pricing lists *"API and webhook access"* as a Core feature, and *"MCP access"* ("Linear MCP") is a named platform surface. The own-nav link to a directory of third-party-built apps + the submit-to-directory mechanism ⇒ `app-platform` (no commerce/"marketplace" branding — contract allows "commerce optional"). API count: no integration count claimed on the page.

**Surfaces:** web · macOS · Windows · iOS · Android · API · MCP — footer links a "Download" page and a "Mobile" feature page; no `self-hosted` / open-source token surfaced (footer GitHub link is github.com/linear, not a self-host offer).

**Jobs:** Full surface spans a numbered product pipeline on the homepage — *"1.0 Intake"* (turn conversations/customer feedback into routed, labeled issues), *"2.0 Plan"* (projects, documents, initiatives, roadmaps, PRDs), *"3.0 Build"* (issues, agents, cycles, Git automations), *"4.0 Diffs"* (PR/agent-output review inside Linear), *"5.0 Monitor"* (Pulse, Insights, dashboards). Center of gravity is issue/project/cycle tracking ("Issues, projects, cycles, initiatives" is the Core line on /pricing) ⇒ gravity `project/task-mgmt`. The hero does NOT name enumerated plurality or "all-in-one" — it leads with the brand-metaphor *"system"* ("The product development system"), which per the contract's `multi/suite` gate does not clear suite, so it falls to the gravity job, not `multi/suite`.

**AI:** AI is woven through the front door. Hero subhead: *"Designed for the AI era."* Below-fold framing: *"A new species of product tool. Purpose-built for modern teams with AI workflows at its core"* and *"Powered by AI agents — Designed for workflows shared by humans and agents. From drafting PRDs to pushing PRs."* Named AI products on the page: **Linear Agent** (beta), **Triage Intelligence**, **Code Intelligence** (beta), **Linear Agent automations** (beta), **Coding Sessions** (the "New" hero CTA), and an **Agents** integration category that deploys third-party coding agents (Codex/OpenAI, Cursor, GitHub Copilot, Devin/Cognition, etc.) inside Linear. Model provenance: not stated as Linear's own model; the page shows third-party agent vendors and one issue card references "Upgrade to Claude Opus 4.5"/"Opus 4.8" inside a product mockup (illustrative, not a stated dependency).

**Pricing & packaging:** Free · Basic · Business · Enterprise; per-user/month `[published]` for the three paid-or-free named tiers, Enterprise `[on-request]` ("Custom / Annual billing only / Contact sales"). Verbatim: Free *"$0 — Free for everyone — Unlimited members, 2 teams, 250 issues, Agent platform, Linear Agent (beta)"*; Basic *"$10 per user/month — Billed yearly"* (5 teams, unlimited issues); Business *"$16 per user/month — Billed yearly"* (unlimited teams, Triage Intelligence, Code Intelligence, Insights, Asks). Prices shown "Billed yearly" (annual default; monthly not surfaced in scrape). Free-tier caps: 2 teams / 250 issues / 10MB file upload. Usage note: Coding Sessions carries a footnote *"** Requires AI credits"* (a usage meter sits under one feature, but plan metering is per-seat ⇒ `pricing_model: per-seat`).

**Trust & compliance:** /security page attests **SOC 2 Type II** ("regular Service Organization Controls audits"), **ISO/IEC 27001:2022 certified**, **GDPR**, and **HIPAA** ("Request BAA"); a separate trust portal at trust.linear.app ("Request SOC 2 / Request ISO"). Security surface: SSO (Google), SAML, SCIM, passkeys, IP restrictions, domain claiming, audit logs (3-month retention), app approvals, multi-region hosting (EU or US), TLS 1.2 in transit / AES-256 at rest. Named enterprise customers on the homepage/customer quotes: **OpenAI**, **Ramp**, **Opendoor** (plus social proof "Linear powers over 33,000 product teams… from ambitious startups to major enterprises"). Status page: linearstatus.com (footer); Enterprise tier lists "Uptime SLA."
