---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: linear.app
captured_at: 2026-06-17
primary_job: project/task-mgmt   # H1 "The product development system" = brand-metaphor "system" (no enumerated plurality → does NOT clear multi/suite); center-of-gravity from /pricing Core line "Issues, projects, cycles, initiatives"
primary_user: team/org           # H1 "for teams and agents"; /pricing "Trusted by more than 33,000 companies"
ai_front_door: hero              # hero subhead "Designed for the AI era" + "New Coding Sessions" hero CTA
pricing_model: per-seat          # /pricing "$10 per user/month", "$16 per user/month"
free_entry: free-tier            # /pricing "Free $0 — Free for everyone" (perpetual, capped at 2 teams / 250 issues)
platform_posture: app-platform   # own nav → /integrations directory + "Build your own integration… submit it to the directory"
---

## Platform & integrations
- **Platform:** a categorized third-party **integration directory** linked from the product's own nav (Resources → Integrations) — sections include Essentials, **Agents**, **AI clients**, Engineering, Automations, Customer Experience, Security & Compliance, Analytics, Collaboration, Media & Design. Explicit third-party build/submit mechanism (the `app-platform` tell): *"Build your own integration — Create your own integration with Linear's API and submit it to the directory"* (/integrations). Public API + webhooks page-attested as a Core feature: *"API and webhook access"* (/pricing), plus *"MCP access"* ("Linear MCP"). No integration *count* claimed on the page.

## Surfaces
- **Surfaces:** web · macOS · Windows · iOS · Android · API · MCP — footer links a Download page; no `self-hosted`/open-source token surfaced (the footer GitHub link is github.com/linear, not a self-host offer).

## Jobs
- **Jobs:** the full surface spans the homepage's numbered pipeline — **1.0 Intake** (route conversations/feedback into labeled issues; Linear Asks via Slack/email/web forms), **2.0 Plan** (projects, documents, initiatives, roadmaps, PRDs), **3.0 Build** (issues, cycles, agents, Git automations), **4.0 Diffs** (PR/agent-output review), **5.0 Monitor** (Pulse, Insights, dashboards). Center of gravity is issue/project/cycle tracking — /pricing's Core line is *"Issues, projects, cycles, initiatives"* ⇒ gravity `project/task-mgmt`. The hero leads with the brand-metaphor *"system"* (*"The product development system"*), naming no enumerated plurality/"all-in-one", so per the `multi/suite` gate it resolves to the gravity job, **not** `multi/suite`.

## AI
- **AI:** woven through the front door. Hero subhead *"Designed for the AI era"*; OG/title *"Purpose-built for planning and building products with AI agents."* Named AI products on captured pages: **Linear Agent** (beta), **Coding Sessions** (the "New" hero CTA), **Triage Intelligence**, **Code Intelligence** (beta), **Linear Agent automations** (beta), plus an **Agents** integration category that deploys third-party coding agents (Codex, Cursor, Copilot, Devin) inside Linear. Model provenance: **not stated as Linear's own model** — the page shows third-party agent vendors; a product mockup references "Opus 4.8" illustratively, not as a stated dependency.

## Pricing & packaging
- **Pricing:** Free · Basic · Business · Enterprise; per-user/month `[published]` for the named tiers, Enterprise `[on-request]` ("Custom / Annual billing only / Contact sales"). Verbatim: Free *"$0 — Free for everyone — Unlimited members, 2 teams, 250 issues, Agent platform, Linear Agent"*; Basic *"$10 per user/month — Billed yearly"* (5 teams, unlimited issues); Business *"$16 per user/month — Billed yearly"* (unlimited teams, Triage Intelligence, Code Intelligence (beta), Linear Insights, Linear Asks). Prices shown "Billed yearly" (annual default; monthly not surfaced). Free-tier caps: 2 teams / 250 issues / 10MB file upload. **Usage overlay:** Coding Sessions carries *"** Requires AI credits"* — a usage meter under one feature, but plan metering is per-seat ⇒ `pricing_model: per-seat`. No open-source/source-available license surfaced.

## Trust & compliance
- **Trust:** /security attests **SOC 2 Type II** ("regular Service Organization Controls audits"), **ISO/IEC 27001:2022 certified**, **GDPR**, and **HIPAA** ("Request BAA"); separate trust portal at **trust.linear.app** ("Request SOC 2 / Request ISO"). Security surface: SSO (Google), SAML + SCIM (Enterprise), IP restrictions, domain claiming, audit log, third-party app management, multi-region hosting. Named customer logos (page-attested, /customers): **Retool, Mercury, Cash App, Vercel, Runway, Perplexity** (homepage adds Ramp); social proof *"Trusted by more than 33,000 companies"*. Status page: linearstatus.com (footer); Enterprise tier lists an Uptime SLA.

## Provenance
- **Pages read (cited captures, 2026-06-17):** `homepage.md` (hero → `ai_front_door`/`primary_user`/`primary_job`), `pricing.md` (tiers, meter, free tier, API/MCP), `security.md` (trust seals), `integrations.md` (the directory + submit mechanism → `platform_posture`), `customers.md` (named logos). Rides the `profile.md` capture — no new endpoints.
- **All 6 cuts filled from real pages** — no off-site knowledge used. `multi/suite` correctly not tripped (brand-metaphor "system" exclusion); `app-platform` rests on the own-nav directory + submit-to-directory mechanism.
- **Rotation caveat:** `primary_job` + `ai_front_door` are the most rotation-prone (homepage A/B + 2026 AI-rebrand churn) — point-in-time snapshot of the 2026-06-17 capture, not fixed.
- **Run profile:** first live store instance of the `productivity_saas` cohort pack (seeding the registered-but-empty pack).
