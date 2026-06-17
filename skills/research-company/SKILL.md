---
name: research-company
description: >
  Capture a single company's website into the web-research store as a structured, cited dossier
  (store/<domain>/profile.md) using Firecrawl. Use whenever the user wants to capture or re-capture
  a company from its website — "research company X", "/research-company acme.com", "capture acme
  into the store", "profile this competitor", "add X to the company store". One company at a time,
  keyed by canonical domain.

  It captures durable STATE (what the company is/sells/how it's positioned, from its own site) — not
  events (news/funding/M&A) or judgments (threat/fit/relevance), which belong to downstream
  consumers. NOT for answering questions from already-captured data — "tell me about X", "what does
  X charge" — that's /query-companies; if a warm fresh capture exists, this verb stops and hands
  off there instead of presenting the dossier. Only stale/new companies spend Firecrawl credits.
---

# /research-company — capture a company into the store

Turn `research company X` into a cached, structured, cited dossier at `store/<domain>/profile.md`. Firecrawl captures the site once; every later read filters that structure instead of re-scraping. **Capture mechanics are deterministic (the `fc.py` script bakes in the hazard knobs); the judgment — domain resolution, key-page selection, and the synthesis into `profile.md` — is yours.**

## Before you start — read the two authority docs (don't reinvent them)

Two contracts govern this verb. The **capture playbook** ships *with* this skill (a sibling file); the **store contract** lives in the engine repo — resolve the engine root for that one:

```bash
# engine root = the repo holding this skill (works through the ~/.claude/skills symlink):
ENGINE="$(cd "$(dirname "$(realpath "$0")")/../.." 2>/dev/null && pwd)"   # if $0 is unset, the skill dir is .../skills/research-company
# canonical fallback (single-user setup): "/Users/brianbolze/Library/Mobile Documents/com~apple~CloudDocs/Web Research"
```

1. **`firecrawl-capture.md`** (next to this file) — the capture mechanics. **§1 is the recipe; the `fc.py` calls below execute it.** §5 is the when-it-breaks lookup (geo-misroute, bot defense, map noise, SPA soft-404s) — skim it so you recognize a hazard when you hit one.
2. **`SCHEMA.md` + `TAXONOMIES.md`** (engine root) — how to write `profile.md`: the frontmatter fields, the closed value sets, the body sections. This is the enrichment contract (step 7). Read it before writing.

`scripts/fc.py` (next to this file) is the workhorse: it auto-reads `FIRECRAWL_API_KEY`, applies `maxAge:0` + `location:US` + `waitFor` + the all-formats bundle, persists raw JSON + cleaned md + screenshots to `store/<slug>/captures/<today>/`, and logs a manifest for the verify step. **Always capture through `fc.py`** — never hand-roll curl scrapes (you'll drop a hazard knob).

> **Interpreter note.** If a subshell (often a `for` loop) reports `python3: command not found`, the pyenv shim isn't on its PATH — resolve once with `PY=$(command -v python3 || echo /opt/homebrew/bin/python3)` and call `"$PY" scripts/fc.py …`. fc.py is stdlib-only, so any Python 3 works.

## The capture loop

Run in order. Steps 3–6 are the credit spend (~7–10 credits for a clean basic run = 1 map + 1 homepage + 5–8 key pages); 1–2 and 7–8 are free. Overages are add-ons, not the homepage pass (all-formats rides one credit) — enhanced-proxy retries (+4), PDF pages (+1/pg), and re-scrapes each show up per-call in `fc.py spend`.

**One phase per turn.** Never issue a step in the same message as the step that consumes its output — a big interdependent batch returns no intermediate state, and that vacuum is where fabricated "results" get narrated before any tool returns (the openai.com run invented a block, a fallback, and prices this way). Independent calls (map + homepage) still batch fine; the rule is about *dependency*, not parallelism.

**0. Pre-flight (free).** `python3 scripts/fc.py credits` — note `remainingCredits`. If low (≲20), warn the user before spending. This global balance is **headroom only** — it's a shared key, so don't diff it for this run's cost; that number comes from `fc.py spend` at step 8, summed from each call's own billed credits. (Key check is automatic; `fc.py` aborts if it can't find the key.)

**1. Resolve the domain → slug (free, and it decides the store key).** `curl -sIL https://<domain>` and see what it *resolves to*.

The final canonical host is the **store folder slug** (dots→dashes, e.g. `honehealth.com` → `honehealth-com`) **and** the `domain:` field — but **strip a bare leading `www.`** (it's a canonicalizing redirect, not a meaningful subdomain), so `www.maximustribe.com` → slug `maximustribe-com`, `domain: maximustribe.com`. Keep meaningful subdomains (`aws.amazon.com` → `aws-amazon-com`). The domain you were handed, if different, goes in `aliases:`. If it resolves to a *different live company*, flag a collision and stop to confirm — don't key on it. (A 403/429 here just means bot-defended; proceed to Firecrawl.)

Once the slug is known, stamp the run clock before any work this verb may perform:
```bash
RUN_STARTED_AT="$(python3 "$WEB_RESEARCH_HOME/scripts/runrecord.py" now)"
```
Warm-skip runs write **no** run record; this clock is only carried forward if the run actually writes an artifact. (Contract: [`RUNS.md`](../../modules/RUNS.md).)

**2. Seed from the store + freshness gate (free).** If `store/<slug>/profile.md` exists:

   - Read its `site_notes` (the capture playbook for *this* site — inherit it, don't rediscover), `key_pages`, and `captured_at`
   - Move the previous capture into `captures/_archive/<date>` so that the most recent capture is always obvious and the captures folder doesn’t look massive.
   - **Coarse freshness:** if `captured_at` is recent (< ~7 days) and the user didn't ask for a refresh, **stop without capturing and hand off** — report the warm status (per-layer clocks from `store.py find`) and route the answer through `/query-companies`. This verb decides capture-vs-skip; presenting the dossier is the consume verb's job, never this one's. Otherwise re-capture (a fresh `captures/<today>/` folder; the old one is preserved). *(On a bare/guided invocation the skip-vs-refresh call surfaces at **step 2.5** instead of auto-deciding here.)*

**2.5. Guided pre-flight — one question batch, then go (free, conditional).** Two on-ramps into the spend:

- **Express** — the invocation already carried intent (a focus, a `refresh`, a module ask, or a plain "just go"). Honor it and skip this step.
- **Guided** — a bare invocation (`/research-company acme.com`, nothing else). Before spending a credit, surface the run as **one** `AskUserQuestion` batch (never drip questions across turns), every option defaulted so the user can glance-and-accept. Shape it from what steps 1–2 found:
  - **This run** *(include only when a warm < ~7-day capture exists)* — `Skip — capture is warm` (default; the answer routes through `/query-companies`) · `Re-capture fresh`. The freshness gate's skip-vs-refresh call made explicit — the one place a human override beats the silent auto-skip. Stale/new → nothing warm; omit this question.
  - **Output scope** *(modules combine — multi-select)* — `Standard profile` (default) · `+ logos:{} brand marks` (the multi-ratio wordmark/logomark/og set for a slide / Notion-cover consumer — near-free, rides the homepage payload; [§1.2](firecrawl-capture.md)) · `+ per-SKU offerings.md` (the Tier-1 roster; [§1.1](firecrawl-capture.md)) · `+ offerings.md with flagship product images` (also pull each flagship's clean **hero product render** for a design / rendering-reference consumer — rides the same PDP capture, stored at `captures/<date>/images/<sku>.<ext>`; [§1.1](firecrawl-capture.md)) · `+ telehealth.md cohort pack` (for a telehealth company — the 8 vertical classification cuts the universal profile can't tell apart; near-free, rides the profile pages; contract [`TELEHEALTH.md`](../../modules/cohort-packs/TELEHEALTH.md), lint `cohortcheck.py`) · `+ productivity_saas.md cohort pack` (for a horizontal productivity / work-software company — the 6 cuts the universal profile reads identical; near-free, rides the profile pages; contract [`PRODUCTIVITY_SAAS.md`](../../modules/cohort-packs/PRODUCTIVITY_SAAS.md), lint `cohortcheck.py --cohort productivity_saas`). Don't offer a depth dial — page count already flexes with `portfolio_shape`; the site decides depth better than a blind setting. **`offerings.md` is shape-gated:** if `offering_category` reads Services/Consulting, or the company has no enumerable priced SKU (bespoke / project work), **warn** that there's likely nothing to roster and default to skipping it with a recorded reason ([OFFERINGS "When to write it"](../../modules/OFFERINGS.md)). Warn, don't block — the category can resolve late or wrong.
  - **Emphasis** *(free-text, optional)* — "Anything to focus on or watch for?" It *biases* page selection (step 4), never *subtracts*: the core `profile.md` contract still gets filled, anything missed goes to `unverified_fields`, so a guided profile stays corpus-comparable.

  Branch on the answer: `Skip` → stop and hand off to `/query-companies` (~$0, no capture); otherwise carry scope + emphasis through steps 3–8.

  **A non-vanilla run leaves one trace.** If the guided run deviated from a plain capture — emphasis given, a module added (offerings / logos), or a refresh forced over a still-warm capture — append a single **`Run profile:`** line to the Provenance section in step 8 (e.g. `Run profile: guided — emphasis "enterprise pricing"; +offerings`). A vanilla run adds nothing; clean profiles stay clean. *(Part of SCHEMA's fixed Provenance set as of `2.4`.)*

**3. Map + homepage, together (2 credits).** Different endpoints — safe to run in one batch:
```bash
python3 scripts/fc.py map     https://<domain>        --slug <slug> --verb research-company
python3 scripts/fc.py scrape  https://<domain>        --slug <slug> --name homepage --homepage --verb research-company
```
`--verb research-company` tags each manifest line so `scripts/runcost.py` can attribute credit cost by verb (the `/deepen-offerings` preset passes its own — §below). `map` is subdomains-off by default — a clean marketing-host inventory (the docs/dev subdomain is dropped, §5.3). It's still a **sample** (big sites) or can be **empty** (custom SPAs), so homepage `links` are the reliable discovery surface. Pull both.

**4. Pick key pages (judgment, free).** The map seeds candidates, but **select from homepage `links`** — the durable surface that also catches signal subdomains the map drops (`investors.`, `careers.`). **Only ever scrape a URL in the captured inventory — never hand-type a path from convention or prior knowledge** (`/about`, `/pricing`, `/ai`, …): a guessed path can return a real-sized 404 stub that poisons the profile (the Qualtrics run burned 4 credits this way; see BACKLOG "junk soft-404 stubs"). `verify` now fingerprints these (§5.6 junk soft-404 gate), but prevention is cheaper — it saves the wasted credit *and* the cleanup. Missing an expected page? Run `map --search "<term>"` to surface it, don't guess. **Filter map noise first** (playbook §5.3): content/funnel paths (`/blog`, `/learning`, `/case-studies`, `/partner`, `/sweepstakes`, …) + locale prefixes (`/en-uk`, `/de-eu`, …).

Then pick **~4-8 signal pages**: pricing, products/treatments, how-it-works, about — whatever carries the company's offering + model + claims. The about / company info / history page would also be helpful - whatever carries founding history, key metrics the company makes public, and key company events.

**Homepage caveat:** if the homepage is an app shell / storefront / logged-in app — a marketplace, a big retailer, a SaaS that drops you straight into the product — it carries little positioning; there the about/company page *is* the primary self-description, so lean on it plus the category/product pages. Let the site's apparent breadth guide depth (a `Single`-shape brand needs fewer pages than a `Multi-product` one; see `portfolio_shape` in TAXONOMIES).

**5. Scrape key pages — serially, no burst (1 credit each).** A parallel burst is what trips the geo/cache shell + 429s (§5.1/5.2). One at a time:
```bash
python3 scripts/fc.py scrape  https://<domain>/<path>  --slug <slug> --name <short_name> --verb research-company
```
Use a clear `--name` per page (`pricing`, `weight_loss`, `about`). Include linked PDFs if they add signal (pricing/spec sheets — 1 credit/page, prime primary source).

**6. Verify scrapes (free).** `python3 scripts/fc.py verify --slug <slug>`. It checks sourceURL-match, md5-uniqueness across pages, **and a junk soft-404 gate**. A **DUP BODY** = §5.1 contamination (identical body for distinct URLs) — re-scrape the affected page, retrying once with `--proxy enhanced` (+4 credits) if a hard block. A **JUNK SOFT-404** = the page's title/heading declares itself "not found" (a dead/guessed path) — `rm` the flagged `.md` (the 404, if it's a finding, goes in prose). Don't discard a page on HTTP status alone — SPAs return 404 with full *correct* content (§5.6); trust the body, but a "Page Not Found" headline is the tell that it's junk, not content. (`verify` also lints `profile.md` once it exists — it just defers here, pre-write; you re-run it in step 7. It exits nonzero on any issue.)

**7. Enrich → write `profile.md` (free, the valuable step).** Read the *whole* capture — every `captures/<today>/*.md`, the screenshots in `.payloads/*.png`, the homepage's `branding` payload, and its **structured layer** (`python3 scripts/fc.py signals --slug <slug>` slices the `rawHtml` JSON-LD + `<header>`/`<nav>` region out of the persisted homepage payload — targeted, free, never the 2 MB blob) — and write `store/<slug>/profile.md` **exactly per SCHEMA's write rules + `TAXONOMIES.md`**: stamp `schema_version` to SCHEMA's current contract version (top of `SCHEMA.md`), the frontmatter (identity, generic classification from the closed sets, visual identity), and the body sections. The two contract rules a capture most often trips on: fill only fields the captured pages support (else `unverified_fields` — never a guess), and read `design_framework` from `rawHtml`, never `branding.designSystem` (reliably wrong). Beyond those, hold SCHEMA's trust line: trace every volatile figure (price, count, date) to a captured page — grep or screenshot — or it's `unverified_fields`; quote it verbatim; never read market position from a site's emphasis; keep `parent`/`owns` to **explicit ownership/legal attestation** — `partner`/`family`/`group`/"family of partners" is affiliation, so it goes in prose and the relation field stays empty ([relation-evidence](../../SCHEMA.md#relation-evidence)); and the rare identity-only prior lands *marked* on the `Enriched (model knowledge)` Provenance line.

Treat the structured layer **exactly like `branding` — a hint to verify, never source-of-truth** (it's self-authored). Confirm each value against the page/screenshot, then land it per SCHEMA's [Structured layer](../../SCHEMA.md#structured-layer) note: `socials` ← `sameAs` (channels they operate); `external` ← `sameAs` (third-party records — crunchbase/wikipedia/bloomberg/…); `aliases` ← `alternateName`, **`legal_entity` ← `legalName`** (2.6 — site-derivable only, empty otherwise); self-reported ratings → **Credibility** (verbatim + flagged); `logo_url` ← JSON-LD `logo` only when it's a real brand mark (ahead of the favicon fallback — but NOT an OG/share image or a 3rd-party theme asset); and the recovered mega-nav hierarchy → **Nav structure**, validated for completeness against the screenshot. Founders/founding-date stay prose-only at the deep-research edge — never a frontmatter field.

**Completeness self-check (scratch, never stored).** The bakeoff's strongest finding was *under-extraction* — a polished profile that silently drops captured prices, offerings, certs, counts, or nav lines ([FINDINGS](../../experiments/2026-06-13-research-company-model-bakeoff/FINDINGS.md)). Before you synthesize, scratch-list the packet-backed facts (every priced line, offering/category, proof point, nav branch); after writing, pass back over that list for *packet facts I omitted* and *claims I can't support*, and fix both. The list is working scratch — it never lands in the store.

**Optional claim-audit (recommended for relation-heavy or high-stakes captures).** A skeptical second-model pass (e.g. GPT-5.5) over the packet catches over-assertion the lint can't — an unsupported `owns`/`parent`, a pharmacy/integration posture stated as fact, a volatile price, missing uncertainty. The bakeoff found this is the cheap catch for the writer's main failure mode (over-reading suggestive language); recommended-not-required.

Then **lint the written profile**: re-run `python3 scripts/fc.py verify --slug <slug>`. Now that `profile.md` exists it also checks for leaked tool-call tags (`</invoke>`, `</content>` — these reached 4 profiles in the first batch), the `## Provenance` section, the required frontmatter keys, and — when a `logos:{}` block is present — its per-slot measurements. Fix anything it flags (nonzero exit) before step 8.

**8. Record the run, then summarize (free).** Update `site_notes` with anything this run learned about the site (JS-walls, map noise, geo quirks, where pricing hides) — that's the carry-forward for next time. Then `python3 scripts/fc.py spend --slug <slug>` for this run's **attributed** cost (summed from each call's own `creditsUsed` — defensible, no "shared key, can't attribute" hedge), and optionally `fc.py credits` for remaining headroom.

**Write the run record _before_ you report back — the run is not done until it's written** (this is the bookkeeping step agents drop). List only the markdown artifacts this run actually wrote:
```bash
python3 "$WEB_RESEARCH_HOME/scripts/runrecord.py" write \
  --slug <slug> \
  --verb research-company \
  --started-at "$RUN_STARTED_AT" \
  --artifact profile.md
```
Tool is env-detected for **both Claude Code and Codex** — no `--tool` needed. Add `--artifact offerings.md` / `--artifact telehealth.md` / `--artifact productivity_saas.md` / `--artifact visual.md` only if this run wrote them. Pass `--model <id>` if you know it (a session `export RUNREC_MODEL=…` is authoritative; otherwise it falls back to `unknown`); add `--status partial` if the run fell short of a clean capture. If a *second* LLM materially helped (a GPT-5.5 claim-audit, a specialist pass), add `--components-json '[{"tool":"codex","model":"gpt-5.5","role":"claim-audit"}]'` — **list only helpers that actually ran**. Keep `--note` to one line of run color, never company State.

Finally, report a run summary:
> Captured **<name>** (`<domain>`) → `store/<slug>/profile.md`. N pages, M credits spent (X remaining). Notable: <1-line site quirk or finding>. <Any `unverified_fields` worth flagging.>

## Enrichment is the product — don't shortchange step 7

`fc.py` only moves bytes. The dossier's value is *your synthesis across the whole capture*: reconcile the homepage against the product pages, make the visual read no scraper can, classify from the closed sets (use `Other` + a body note over a forced fit). Earn each body section with evidence; omit it rather than pad. The SCHEMA's positive examples set the bar.

## v1 scope — what this verb does NOT do (on purpose)

Tier-0 `profile.md` is the **default** — one company → one dossier, no hand-holding. Three opt-in extensions are live: **`offerings.md`** (Tier-1 per-SKU roster — separate recipe in [`firecrawl-capture.md` §1.1](firecrawl-capture.md), **only** when a cohort needs the per-SKU grain, telehealth first; lint `scripts/offeringscheck.py`; deepen an existing roster later with the `/deepen-offerings` preset), the **`logos:{}`** module (multi-ratio brand marks added to `profile.md` — [§1.2](firecrawl-capture.md); near-free, measured by `fc.py logos`), and two **cohort packs** — **`telehealth.md`** (vertical cuts for a telehealth company; contract [`TELEHEALTH.md`](../../modules/cohort-packs/TELEHEALTH.md), lint `cohortcheck.py --cohort telehealth`) and **`productivity_saas.md`** (6 cuts for horizontal productivity / work software; contract [`PRODUCTIVITY_SAAS.md`](../../modules/cohort-packs/PRODUCTIVITY_SAAS.md), lint `cohortcheck.py --cohort productivity_saas`).

A separate **sibling** skill — **`/visual-evidence`** — mines an *already-captured* company's screenshots into a blind visual-evidence layer (`store/<domain>/visual.md`: cited cards across typography / layout / color-brand / iconography + a `Visual & brand impression`). It runs **after** capture, never inside it — the capturing agent has read the dossier, so it can't be the blind miner (blinding is the whole game). Contract [`modules/VISUAL.md`](../../modules/VISUAL.md); it reuses cached captures (Tier-A) and re-renders contaminated pages in a real browser (Tier-B), no Firecrawl.

Still **not** built: `brand.md`, `.web-research/config.yaml` resolution, per-section TTL, Notion promotion — clean later additions, not a rebuild; don't build them here.

## Optional: fan-out for big sites

For a large key-page set, a sub-agent per page (scrape + clean) with the lead agent reconciling into `profile.md` is fine — but **serialize the scrapes within each agent** (the burst hazard is real). For the typical 4-8 page company, a single serial pass is simpler and sufficient. Don't fan out by default.

---

*Maintainer note: this verb's output is the contract `QUERYING.md` reads. If you change the **output format** — the frontmatter shape, the `captures/` layout, or the inline `#`-comment convention — update the engine's `QUERYING.md` and run `scripts/querycheck.py`.*
