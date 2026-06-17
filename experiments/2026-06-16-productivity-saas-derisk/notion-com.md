---
# De-risk probe instance (experiments/) — not a store entry; values validated against modules/cohort-packs/PRODUCTIVITY_SAAS.md.
schema_version: "1.0"
domain: notion.com
captured_at: 2026-06-16
primary_job: multi/suite
primary_user: team/org
ai_front_door: hero
pricing_model: per-seat
free_entry: free-tier
platform_posture: app-platform
---

## Platform & integrations
- **Platform:** Public API + integration directory + own-nav marketplace clears `app-platform`. Footer links **"Connections"** and **"Templates"**, and the top nav has **"Connections — Connect your apps"**; the `/connections` directory is a browsable third-party catalog ("*Extend Notion with connections that sync your data, automate workflows, and connect your favorite tools*") filterable by type (**Public API · AI connector · Embed · SCIM/SSO**) and developer (**Made by Notion · Technology partners**), with a disclaimer "*Notion partners with select companies to build integrations. Notion does not endorse or certify these integrations.*" — i.e. third-party-built apps in the product's own nav.
- **API:** `public` — pricing page "Plans and features" lists **"Public API — Build bespoke integrations,"** **"Webhooks — Send real-time updates to your integrations,"** plus a **Developer platform** row (**"CLI — Build on Notion and deploy Workers with code or coding agents"** and **"Workers (Beta) — Run custom code on Notion to extend agents"**). Nav + footer link **Developers** (developers.notion.com / notion.dev).
- **Integration count:** not stated as a headline number; per-connection install counts shown (e.g. Slack "14K", Google Drive "38K", GitHub "3.7K") — page-attested, unverified.

## Surfaces
- **Surfaces:** web · macOS · Windows · iOS · Android · browser-extension (Web Clipper) · CLI · API. (Footer "Download": iOS & Android, Mac & Windows, Web Clipper; pricing lists CLI + Public API. No `self-hosted` — none claimed.)

## Jobs
- **Jobs:** spans docs, knowledge base/wikis, projects/task-mgmt, databases, AI meeting notes, enterprise search, plus bundled **Notion Calendar** and **Notion Mail** — nav groups "Docs / Knowledge Base / Projects" and "Notion AI / Agents / AI Meeting Notes / Enterprise Search." Center of gravity is **not a single classic job**: the homepage hero leads with **agents + automation + "capture context, find answers"** ("*Where teams and agents Create together*" / "*Capture context, find answers, and automate tasks with AI built for your team*"), and the section header reads "**Bring all your work together.**" Pricing H1 "**One tool to run your company**" and an OpenAI testimonial ("*a single platform where you can do all your work… Notion is that single place*") reinforce the all-work-in-one framing. Per the contract's multi/suite gate this is a borderline call — see contract_gaps. Tagged `multi/suite` on the gravity-is-diffuse + "bring all your work together" framing rather than forcing a single job; **gravity (if one must be named): docs/notes/wiki + knowledge base.**

## AI
- **AI:** AI is the front-door story. Named products: **Notion AI** ("AI tools for work"; core = "chat, generate, autofill, translate"), **Agents / Notion Agent / Custom Agents** ("*You assign the tasks. Notion Agent does the work*"; "*Completes complex, multi-step tasks using context from Notion, your connected apps, and the web*"), **AI Meeting Notes** ("*Perfect notes, every time*"), **Enterprise Search** ("*One search for everything*" — across Slack, Google Drive, Jira), and **Research mode (Beta)**. Model provenance: page does not name a model vendor; states only "*our LLM providers utilize zero data retention for Enterprise*," "*AI Subprocessors are prohibited from using Customer Data to train models*," and "*Notion AI will not use your data to train our models unless you opt in*" (/pricing FAQ, /security).

## Pricing & packaging
- **Pricing:** Free · Plus · Business · Enterprise — `[published]` per-seat; Business marked "Recommended."
  - **Free** $0 /member/mo — "*For individuals to organize personal projects and life*"; Trial of Notion AI, ≤5 MB file uploads, 7-day page history, 10 guests.
  - **Plus** $10 /member/mo — small teams; unlimited blocks/uploads, 30-day history.
  - **Business** $20 /member/mo — Notion Agent, AI Meeting Notes, Enterprise Search (Beta), SAML SSO.
  - **Enterprise** — "Custom pricing" `[on-request]` (Contact Sales); SCIM, audit log, zero data retention.
- **Usage/credit overlay (alongside per-seat):** **Custom Agents** — "*Free to try, then $10 per 1,000 monthly Notion credits*"; **Workers (Beta)** — "*Free to try now. Starts using credits on August 11.*" So the AI/agent layer is metered in **Notion credits** on top of per-seat. Recorded `per-seat` as the primary meter (the seat price is the headline for the workspace) with the credit meter noted here — see contract_gaps.
- **Billing:** monthly or annual; "*Save up to 20% with yearly*." Students/educators: Plus free (1-member). Custom-domain add-on $8–10/mo per domain.

## Trust & compliance
- **Certifications (y):** SOC 2 Type 2; ISO 27001, ISO 27701, ISO 27017, ISO 27018; HIPAA (Enterprise + BAA); BSI C5 — all on /security. GDPR/CCPA mapped. Reports via Trust portal on request (not self-serve). Public bug bounty (HackerOne).
- **Named customers/logos:** homepage — OpenAI, Figma, Ramp, Cursor, Vercel, Nvidia, Volvo, L'Oréal, Discord, Lovable, 1Password, Affirm, Riot Games, Clay, Remote, Faire, Toyota. Claims: "*Trusted by 98% of the Forbes Cloud 100*," "*Over 100M users worldwide*," "*62% of Fortune 100*," "*Over 50% of YC companies*."
- **Reliability:** "*guaranteed uptime of 99.9%*"; public status page (status.notion.so / notion-status.com); AWS + Cloudflare infra.
