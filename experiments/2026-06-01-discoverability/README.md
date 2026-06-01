# Upstream discoverability — does a *fresh agent in another project* reach the system unaided?

*2026-06-01. The [consumption-affordance test](../2026-05-31-consumption-affordance/) proved a cold
agent **dropped inside the store and handed its location** discovers `README → QUERYING.md` and answers
well (5/5). It explicitly bracketed the harder upstream question — its own **Wall 2** flags that "the
wrap-it-in-a-skill half of rung-2 is **still unbuilt**" and entry-point discovery is "a single point of
dependence." This test isolates exactly that: an agent that is **not told the store exists, not dropped
inside it, working in an unrelated project.** Does it ever reach the system — or default to WebSearch?*

## The question (Brian's framing)

> "I want agents to **know about its existence and automatically leverage it** as a great set of primary-
> source company info — instead of just **defaulting to their own (often lazy & error-prone) WebSearch**."

Two discovery surfaces, tested separately:
- **Surface A — the verb.** Does a fresh agent reach for the global `research-company` skill (capture +
  warm point-read)?
- **Surface B — the store-as-corpus.** Independent of the skill: does a fresh agent ever find/read the
  45-company store for shapes the skill doesn't cover (cross-company aggregation, deep-research priors)?

## Method

- **"Fresh agent" = a sub-agent in an unrelated project** (cwd = the Drift iOS project — *not* Web
  Research, *not* Teleprescribe; its `CLAUDE.md` says nothing about this system). Prompts contain **zero**
  mention of web-research / the store / Firecrawl / skills — just what a real user would type.
- **Harness pivot.** The gold-standard harness (headless `claude -p --output-format stream-json`, matching
  consumption-affordance) was **blocked by the auto-mode permission classifier** (`--dangerously-skip-
  permissions` is a privilege escalation not authorized for autonomous processes). Pivoted to the **Agent
  tool** (which Brian explicitly sanctioned). P0 validated it as faithful: a sub-agent receives the global
  skills and can reach the store via the skill chain.
- **Self-report → corroborated.** The Agent tool gives a self-reported tool log, not a raw trace. Each
  probe was required to append an honest `### TOOL LOG`; every claim was then **cross-checked against
  objective signals** — Firecrawl credit delta, store-folder count, profile `captured_at` mutations. They
  matched exactly (credits 1360→1357 = P3's 3 re-verifies; no `ro-co` folder = P1 stopped cold; etc.), so
  the self-reports are trusted.
- **Spend control.** All point-read probes target **warm** companies (≤2 days old → warm-serve at ~$0).
  The one cold probe (P1, `ro.co`) carried a plan-first guard ("don't spend; state your plan + first
  action") — held (0 credits).

## Probes (model = Opus, to match the P0 calibration + prior experiment)

| # | Variable isolated | Prompt gist | Company (store status) |
|---|---|---|---|
| **P0** | reachability (control) | "what company-research capabilities do you actually have here?" | — (introspection) |
| **P1** | explicit verb, **cold** | "accurate current profile of Ro (ro.co)" | ro.co — **cold** |
| **P2** | explicit verb, **warm** | "accurate current profile of Hims" | hims.com — warm |
| **P3** | **indirect** framing, no trigger words | "competitive brief… up-to-date read on Function Health" | functionhealth.com — warm |
| **P4** | **cross-company aggregation** | "compare how Hims/Hone/Marek/Maximus price TRT" | all 4 — warm |
| **P5** | **casual / lazy-default temptation** | "what does agelessrx charge for their longevity stuff these days?" | agelessrx.com — warm |

Results + recommendations: [`FINDINGS.md`](FINDINGS.md). Raw self-reports live in the parent session
transcript (Agent tool returns text, not a retained trace file).

## Validity caveats (read before over-trusting)

- **Agent-tool sub-agents are primed-to-work** → may overstate diligence vs. a real lazy top-level
  session. The probe most affected is **P5** (laziness) — treat its positive as the softest. Objective
  corroboration mitigates this for the *spend/store-mutation* claims, not for the *would-a-real-session-
  bother* question.
- **Single model (Opus); n=1 per cell.** Brian's `settings.json` default is **sonnet** — model-sensitivity
  is untested here (prior experiment flagged Opus-contingency). A weaker/lazier model may not chase the
  skill chain. This is a directional probe, not a powered study.
- **P0 self-report confabulated** (invented a store entry `appliedballisticsllc-com` to match the Drift
  cwd; it does not exist) — proof that self-report embellishes, and why every behavioral claim here was
  checked against disk.
