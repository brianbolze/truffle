---
name: research-company
description: >
  Capture a single company's website into the web-research store as a structured, cited dossier
  (store/<domain>/profile.md) using Firecrawl. Use whenever the user wants to research, capture,
  profile, or "look up" a company from its website — "research company X", "/research-company
  acme.com", "capture acme into the store", "what does acme.com do / sell / charge", "profile this
  competitor", "add X to the company store". One company at a time, keyed by canonical domain.

  It captures durable STATE (what the company is/sells/how it's positioned, from its own site) — not
  events (news/funding/M&A) or judgments (threat/fit/relevance), which belong to downstream
  consumers. A warm, fresh company is served from the store at ~$0; only stale/new companies spend
  Firecrawl credits.
---

# /research-company — capture a company into the store

Turn `research company X` into a cached, structured, cited dossier at `store/<domain>/profile.md`. Firecrawl captures the site once; every later read filters that structure instead of re-scraping. **Capture mechanics are deterministic (the `fc.py` script bakes in the hazard knobs); the judgment — domain resolution, key-page selection, and the synthesis into `profile.md` — is yours.**

## Before you start — read the two authority docs (don't reinvent them)

This skill orchestrates; the contract lives in the engine repo. Resolve the engine root and read:

```bash
# engine root = the repo holding this skill (works through the ~/.claude/skills symlink):
ENGINE="$(cd "$(dirname "$(realpath "$0")")/../.." 2>/dev/null && pwd)"   # if $0 is unset, the skill dir is .../skills/research-company
# canonical fallback (single-user setup): "/Users/brianbolze/Library/Mobile Documents/com~apple~CloudDocs/Web Research"
```

1. **`_design/references/firecrawl-capture.md`** — the capture mechanics. **§1 is the recipe; the `fc.py` calls below execute it.** §5 is the when-it-breaks lookup (geo-misroute, bot defense, map noise, SPA soft-404s) — skim it so you recognize a hazard when you hit one.
2. **`SCHEMA.md` + `TAXONOMIES.md`** — how to write `profile.md`: the frontmatter fields, the closed value sets, the body sections. This is the enrichment contract (step 7). Read it before writing.

`scripts/fc.py` (next to this file) is the workhorse: it auto-reads `FIRECRAWL_API_KEY`, applies `maxAge:0` + `location:US` + `waitFor` + the all-formats bundle, persists raw JSON + cleaned md + screenshots to `store/<slug>/captures/<today>/`, and logs a manifest for the verify step. **Always capture through `fc.py`** — never hand-roll curl scrapes (you'll drop a hazard knob).

> **Interpreter note.** If a subshell (often a `for` loop) reports `python3: command not found`, the pyenv shim isn't on its PATH — resolve once with `PY=$(command -v python3 || echo /opt/homebrew/bin/python3)` and call `"$PY" scripts/fc.py …`. fc.py is stdlib-only, so any Python 3 works.

## The capture loop

Run in order. Steps 3–6 are the credit spend (~7–10 credits for a clean basic run = 1 map + 1 homepage + 5–8 key pages); 1–2 and 7–8 are free. Overages are add-ons, not the homepage pass (all-formats rides one credit) — enhanced-proxy retries (+4), PDF pages (+1/pg), and re-scrapes each show up per-call in `fc.py spend`.

**0. Pre-flight (free).** `python3 scripts/fc.py credits` — note `remainingCredits`. If low (≲20), warn the user before spending. This global balance is **headroom only** — it's a shared key, so don't diff it for this run's cost; that number comes from `fc.py spend` at step 8, summed from each call's own billed credits. (Key check is automatic; `fc.py` aborts if it can't find the key.)

**1. Resolve the domain → slug (free, and it decides the store key).** `curl -sIL https://<domain>` and see what it *resolves to*.

The final canonical host is the **store folder slug** (dots→dashes, e.g. `honehealth.com` → `honehealth-com`) **and** the `domain:` field — but **strip a bare leading `www.`** (it's a canonicalizing redirect, not a meaningful subdomain), so `www.maximustribe.com` → slug `maximustribe-com`, `domain: maximustribe.com`. Keep meaningful subdomains (`aws.amazon.com` → `aws-amazon-com`). The domain you were handed, if different, goes in `aliases:`. If it resolves to a *different live company*, flag a collision and stop to confirm — don't key on it. (A 403/429 here just means bot-defended; proceed to Firecrawl.)

**2. Seed from the store + freshness gate (free).** If `store/<slug>/profile.md` exists:

   - Read its `site_notes` (the capture playbook for *this* site — inherit it, don't rediscover), `key_pages`, and `captured_at`
   - Move the previous capture into `captures/_archive/<date>` so that the most recent capture is always obvious and the captures folder doesn’t look massive.
   - **Coarse freshness:** if `captured_at` is recent (< ~7 days) and the user didn't ask for a refresh, **serve the existing dossier and stop** — that's the ~$0 warm path. Otherwise re-capture (a fresh `captures/<today>/` folder; the old one is preserved).

**3. Map + homepage, together (2 credits).** Different endpoints — safe to run in one batch:
```bash
python3 scripts/fc.py map     https://<domain>        --slug <slug>
python3 scripts/fc.py scrape  https://<domain>        --slug <slug> --name homepage --homepage
```
The map is a **sample** (big sites) or can be **empty** (custom SPAs) — homepage `links` are the reliable discovery surface. Pull both.

**4. Pick key pages (judgment, free).** Merge map URLs + homepage links. **Only ever scrape a URL that appears in this captured inventory — never hand-type a path from convention or prior knowledge** (`/about`, `/pricing`, `/ai`, …). A guessed path that doesn't exist can return a real-sized 404 error stub that silently passes `verify` and poisons the profile (the Qualtrics run burned 4 credits this way; see BACKLOG "junk soft-404 stubs"). If a page you expect is missing from the inventory, run a second `map --search "<term>"` to surface it, don't guess it. **Filter the noise first** (playbook §5.3): drop `/partner|/people|/hero-*-lp|/sweepstakes|/campaign|/blog|/post`, locale prefixes (`/en-uk`, `/de-eu`, …), and duplicate funnel slugs.

Then pick **~4-8 signal pages**: pricing, products/treatments, how-it-works, about — whatever carries the company's offering + model + claims. The about / company info / history page would also be helpful - whatever carries founding history, key metrics the company makes public, and key company events.

**Homepage caveat:** if the homepage is an app shell / storefront / logged-in app — a marketplace, a big retailer, a SaaS that drops you straight into the product — it carries little positioning; there the about/company page *is* the primary self-description, so lean on it plus the category/product pages. Let the site's apparent breadth guide depth (a `Single`-shape brand needs fewer pages than a `Multi-product` one; see `portfolio_shape` in TAXONOMIES).

**5. Scrape key pages — serially, no burst (1 credit each).** A parallel burst is what trips the geo/cache shell + 429s (§5.1/5.2). One at a time:
```bash
python3 scripts/fc.py scrape  https://<domain>/<path>  --slug <slug> --name <short_name>
```
Use a clear `--name` per page (`pricing`, `weight_loss`, `about`). Include linked PDFs if they add signal (pricing/spec sheets — 1 credit/page, prime primary source).

**6. Verify scrapes (free).** `python3 scripts/fc.py verify --slug <slug>`. It checks sourceURL-match **and** md5-uniqueness across pages. A **DUP BODY** = §5.1 contamination (identical body for distinct URLs) — re-scrape the affected page, retrying once with `--proxy enhanced` (+4 credits) if a hard block. Don't discard a page on HTTP status alone — SPAs return 404 with full correct content (§5.6); trust the body. (`verify` also lints `profile.md` once it exists — it just defers here, pre-write; you re-run it in step 7. It exits nonzero on any issue.)

**7. Enrich → write `profile.md` (free, the valuable step).** Read the *whole* capture — every `captures/<today>/*.md`, the screenshots in `.payloads/*.png`, and the homepage's `branding` payload — and write `store/<slug>/profile.md` **exactly per SCHEMA's write rules + `TAXONOMIES.md`**: `schema_version: 1`, the frontmatter (identity, generic classification from the closed sets, visual identity), and the body sections. The two contract rules a capture most often trips on: fill only fields the captured pages support (else `unverified_fields` — never a guess), and read `design_framework` from `rawHtml`, never `branding.designSystem` (reliably wrong).

Then **lint the written profile**: re-run `python3 scripts/fc.py verify --slug <slug>`. Now that `profile.md` exists it also checks for leaked tool-call tags (`</invoke>`, `</content>` — these reached 4 profiles in the first batch), the `## Provenance` section, and the required frontmatter keys. Fix anything it flags (nonzero exit) before step 8.

**8. Record + summarize (free).** Update `site_notes` with anything this run learned about the site (JS-walls, map noise, geo quirks, where pricing hides) — that's the carry-forward for next time. Then `python3 scripts/fc.py spend --slug <slug>` for this run's **attributed** cost (summed from each call's own `creditsUsed` — defensible, no "shared key, can't attribute" hedge), and optionally `fc.py credits` for remaining headroom. Report a run summary:
> Captured **<name>** (`<domain>`) → `store/<slug>/profile.md`. N pages, M credits spent (X remaining). Notable: <1-line site quirk or finding>. <Any `unverified_fields` worth flagging.>

## Enrichment is the product — don't shortchange step 7

`fc.py` only moves bytes. The dossier's value is *your synthesis across the whole capture*: reconcile the homepage against the product pages, make the visual read no scraper can, classify from the closed sets (use `Other` + a body note over a forced fit). Earn each body section with evidence; omit it rather than pad. The SCHEMA's positive examples set the bar.

## v1 scope — what this verb does NOT do (on purpose)

Tier-0 `profile.md` only. **No** `offerings.md`/`brand.md` (Tier-1, opt-in, lands when a project enables them), **no** `.web-research/config.yaml` resolution, **no** per-section TTL, **no** Notion promotion. v1 = one company → one `profile.md`, no hand-holding. Those are clean later additions, not a rebuild — don't build them here.

## Optional: fan-out for big sites

For a large key-page set, a sub-agent per page (scrape + clean) with the lead agent reconciling into `profile.md` is fine — but **serialize the scrapes within each agent** (the burst hazard is real). For the typical 4-8 page company, a single serial pass is simpler and sufficient. Don't fan out by default.

---

*Maintainer note: this verb's output is the contract `QUERYING.md` reads. If you change the **output format** — the frontmatter shape, the `captures/` layout, or the inline `#`-comment convention — update the engine's `QUERYING.md` and run `scripts/querycheck.py`.*
