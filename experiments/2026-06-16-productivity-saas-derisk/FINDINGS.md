# Stage-2 de-risk — `productivity_saas` cohort pack on live captures

**Purpose.** The schema ([`modules/cohort-packs/PRODUCTIVITY_SAAS.md`](../../modules/cohort-packs/PRODUCTIVITY_SAAS.md)) was designed + hardened across two *paper* rounds (classify-from-knowledge). Two questions only live pages can answer: does every cut **fill from a real site**, and does `ai_front_door` read **crisply off live heroes** (its paper 76% was scored from model memory)? This probe captured 5 real sites via Firecrawl and authored each instance **page-attested** (only what the page says).

**Verdict: ready-to-register.** Five of six cuts filled 100% from real pages; `ai_front_door` read crisply on every hero; the one strain (`primary_job` on Notion) earned a rule clarification, not a new value.

## The instances

| Tool | primary_job | primary_user | ai_front_door | pricing_model | free_entry | platform_posture |
|---|---|---|---|---|---|---|
| [Notion](notion-com.md) | multi/suite ⚠️ | team/org | hero | per-seat | free-tier | app-platform |
| [Granola](granola-ai.md) | meeting-notes/recording | individual/prosumer | hero | per-seat | free-tier | has-API/integrations |
| [Calendly](calendly-com.md) | scheduling/booking | individual/prosumer | **absent** | per-seat | free-tier | has-API/integrations |
| [Linear](linear-app.md) | project/task-mgmt | team/org | hero | per-seat | free-tier | app-platform |
| [Airtable](airtable-com.md) | database/spreadsheet/no-code | team/org | hero | per-seat | free-tier | app-platform |

## What the live pages settled

- **`ai_front_door` validated — 5/5 crisp.** Granola (AI in the H1), Notion + Linear + Airtable (AI in subhead/CTA), and the discriminating case: **Calendly = `absent`** — its hero has zero AI even though it ships an AI Notetaker + a Claude connector *below the fold*. Placement, not capability — working as designed. The paper-memory mirage is retired.
- **Airtable confirms two fixes live** — its "all your teams, all their workflows—connected in one workspace" hero correctly did **not** trip `multi/suite` (the brand-metaphor exclusion → `database/spreadsheet/no-code`), and its `app-platform` rests on the **footer** Marketplace link (the stage-1 footer clause). The two rule edits that worried us most both held on a real page.
- **5 of 6 cuts filled 100%** from real pages, no prior knowledge needed. `pricing_model`, `free_entry`, `platform_posture` (own-nav directory test) resolved cleanly every time. `primary_user` filled via the documented entry-tier tie-breaker on the two heroes that name a situation ("back-to-back meetings") or audience ("professionals") rather than a persona.
- **`scheduling/booking` held** — Calendly classified cleanly off "Easy scheduling ahead / the #1 scheduling tool", distinct from `email/calendar` (no inbox/compose lead). Validates the value the second paper round added.

## The one strain → the one fix

**`primary_job` on Notion (75% fill).** Notion's 2026 hero — *"Where teams and agents Create together"* — leads with an AI-agent value prop that names **no in-set job and no enumerated plurality**, so the `multi/suite` gate had nothing to clear *and* the center-of-gravity fallback had no obvious target; the agent assigned `multi/suite` as least-wrong. This is the exact pattern the pack exists to catch. **Fix applied:** an AI-agent-hero fallback clause — resolve to the center-of-gravity job from nav/pricing (Notion ⇒ `docs/notes/wiki`), else `unclear`, **never** a strained `multi/suite`. A rule clarification, no new closed-set value. *(The `notion-com.md` instance here is recorded as-captured for the record; under the fix it resolves to `docs/notes/wiki`.)*

**Held the line** (rejected as already-handled-by-design): the per-seat + Notion-credits *hybrid* (dominant meter → cut, usage overlay → body note — the discipline that killed `gtm_motion`/`flat-rate`); the `primary_user` borderlines (the tie-breaker resolved each); the `platform_posture` curated-directory cases (the own-nav test resolved all four).

## Status

Schema is validated on real pages. Contract fixes are in. **Next:** register (SCHEMA Tier-1 + README router + QUERYING). These instances are **de-risk probe artifacts** — when the pack is registered, real store entries (with `profile.md`) come from `/research-company`, which will reflect the fixed `primary_job` rule.
