# Reference: Firecrawl capture playbook

The hard-won mechanics of capturing a company website with Firecrawl — what to call, in what order, what it costs, and what breaks. **This is the engine's capture contract; the `/research-company` verb implements it.** Distilled from our hand-captures ([linear](../../experiments/2026-05-30-first-capture/FINDINGS.md), [AG1](../../experiments/2026-05-30-breadth/FINDINGS.md), [shapes: nike/aws/benadryl](../../experiments/2026-05-30-shapes/FINDINGS.md), [telehealth cohort ×6](../../experiments/2026-05-30-telehealth-cohort/FINDINGS.md)), reconciled against agent-workflows' `competitor-watch` + `INVARIANTS.md`, and verified against docs.firecrawl.dev (2026-05-30).

> **§1 is the recipe — follow it in order.** §2–§5 are reference + a hazard-lookup. §6 is **still-open** (*watch, don't codify*), §7 is the **avoid-list** (features we deliberately don't touch). The rest is provenance, in toggles.

## 1. The capture recipe

Do this in order. Knobs that matter are inline; the *why* is in the section linked on each.

0. **Verify the key** (§4): `echo "${FIRECRAWL_API_KEY:+present}"`. Empty ⇒ read from `~/.claude/settings.json`.
1. **Alias check — MANDATORY, free, and it decides the store key** (§2): `curl -sIL` the brand's domain (and any suspected former domain). Whatever it *resolves to* is the canonical key → it becomes the store folder slug **and** the `domain:` frontmatter; the brand's casually-stated domain (if different) goes under `aliases:` — or gets a **collision flag** if it resolves to a *different live company* (don't key on it). A 403/429/blocked here just means bot-defended — go straight to Firecrawl. *(In the telehealth cohort this one free step caught a same-day domain migration, a blocked non-canonical domain, and a namespace collision — 3 of 6 brands. Never key on the domain you were handed; key on the one that resolves.)*
2. **Map** (§2): `/v2/map` with `limit:500`, `location:{country:"US"}`. **Filter funnel + locale noise** (§5.3) before picking the ~15–20 signal pages.
3. **Homepage — the rich pass** (§3): one `/v2/scrape` with **all cheap formats together** (`markdown, html, rawHtml, links, branding, images, screenshot{fullPage}`), plus `maxAge:0` + `location:{country:"US",languages:["en-US"]}` + `waitFor:3500`. (Map step 2 may run alongside this — different endpoint, safe.)
4. **Key pages — serially, no burst** (§5.1/§5.2): one `/v2/scrape` each (`markdown, links, screenshot{fullPage}`), same `maxAge:0` + `location` + `waitFor`. **Serialize** — a parallel burst is what triggers the geo/cache shell and 429s.
5. **Verify every response** (§5.1): `metadata.sourceURL` == requested URL **and** the body md5 is unique across pages. Identical bodies for distinct URLs = the silent geo/cache contamination — re-scrape. (sourceURL-match alone is *not* sufficient.) **Do NOT gate on the HTTP status code** — app-style SPAs return `404` for valid deep links while still rendering full, correct content (§5.6); trust the body (md5-unique + not thin), not the status.
6. **Persist** (§5.5): raw JSON + screenshots → local scratch → the store's `captures/<date>/.payloads/` (download shots with Python `urlretrieve`, not `curl -o`).
7. **Hand off to enrichment** — writing `profile.md` is the SCHEMA's job, not this doc's.

**Clean-run budget: ~7–10 credits** = 1 map + 1 rich homepage + ~5–8 key pages (1 credit each).

## 2. Endpoints

| Endpoint | When | Cost |
|---|---|---|
| **`/v2/map`** ([doc](https://docs.firecrawl.dev/features/map)) | First. Site inventory → pick key pages without scraping. Returns `{url, title, description}` per URL. `limit:500` (per-call billing makes the higher cap free; 250 default drops subtrees). `search:"<term>"` for relevance-ordered second passes — map is a *sample*, not exhaustive. | **1 / call** |
| **`/v2/scrape`** ([doc](https://docs.firecrawl.dev/features/scrape)) | The workhorse — homepage + each key page. | **1 / page** (§3) |
| `/v2/batch/scrape` ([doc](https://docs.firecrawl.dev/features/batch-scrape)) | **Avoid for first capture.** Same 1cr/URL, but concurrent at the team's full browser limit — exactly what trips the geo/cache hazard (§5.1) + 429s (§5.2). | 1 / URL |
| `actions` (a `/v2/scrape` **option**) | Not used yet. Browser steps (`click`, `wait`, `scroll`, …) run *before* capture — the likely lever for client-rendered nav (§6). Rides the page credit. **Not** the `Interact` endpoint (metered 2cr/browser-min). | rides page credit |
| `/v2/search` ([doc](https://docs.firecrawl.dev/features/search)) | **Not for Tier-0 capture.** Web/news search with `includeDomains`/`excludeDomains`/time filters + optional inline scrape (`scrapeOptions`). Sits at the *consumer layer*, not capture: (a) future Discovery ("find companies related to X") — right tool, wrong phase; (b) external-links frontmatter fill (`linkedin`/`x`/`wikipedia` handoff hooks) — borderline Tier-0, cheap; (c) news/M&A for deep-research consumers — output goes project-side, not into the profile. | ~2cr / 10 results |

**PDFs are first-class.** A public PDF URL (pricing sheet, spec sheet, investor one-pager) scrapes like any page — auto-detected, `parsers:["pdf"]`, **1 credit / PDF page**. Don't skip linked PDFs in key-page selection if you think they add signal; they're prime primary-source material. (`/parse` is the sibling for local/non-public DOCX/XLSX/PDF ≤50 MB — not needed for web capture.)

## 3. The all-formats-ride-one-credit rule

**Request every cheap format together on one scrape. Never split formats to "save credits" — you save nothing and lose retroactive analysis.** `/v2/scrape` bills **per page, not per format**:

```
# homepage pass — all of these ride the single 1-credit base:
formats: ["markdown","html","rawHtml","links","branding","images",{"type":"screenshot","fullPage":true}]
```

| Format | Gives you |
|---|---|
| `markdown` | Clean body copy — default extraction surface. |
| `html` | Cleaned HTML. **Recovery surface for JS-walled values** (linear's `$` prices were scrambler artifacts in markdown, clean in html). |
| `rawHtml` | Unmodified `<head>`/`<script>` — **source of truth for framework** (`__NEXT_DATA__`, `/_next/`); don't trust `branding.designSystem` (§5.4). |
| `links` | On-page anchor inventory — feeds nav reconstruction when the nav is client-rendered. |
| `branding` | Structured visual identity (colors, fonts, typography, `colorScheme`). **Must be requested explicitly** — omitting it cost linear a re-scrape. |
| `images` | All image URLs — feeds the logo fallback chain (§5.4). Default to homepage only. |
| `screenshot{fullPage:true}` | Visual ground truth — **load-bearing** (pricing, logo walls, verified `color_scheme`). URLs expire 24h — download immediately (§5.5). |

**Cost add-ons** ([billing](https://docs.firecrawl.dev/billing)) — everything above rides the base free; only these add credits:

| Add-on | Extra |
|---|---|
| `json` format (LLM extraction) | **+4 / page** — extract from the free surfaces instead |
| Enhanced proxy (`enhanced`, or `auto` when it escalates) | **+4 / page** (=5) |
| `zeroDataRetention` | +1 / page |
| PDF parsing | +1 / PDF page |

*Key pages don't need `rawHtml`/`branding`/`images` — `["markdown","links",{"type":"screenshot","fullPage":true}]` suffices.*

**Freshness = `maxAge`, not a separate feature.** A non-zero `maxAge` returns a cache hit in milliseconds (docs: up to ~500% faster) but **still bills 1 credit** — the cache buys *speed/reliability, not credits*. Real credit savings come only from the **store-level skip** (`captured_at` + TTL deciding *not to call*). Division of labor: the store's TTL decides whether to fetch; when re-fetching a stale section, pass `maxAge = that section's TTL` (the fast cache path); reserve **`maxAge:0` for first capture / correctness-critical pages** — docs warn it bypasses cache, runs slower, and fails more, which is *why* `maxAge:0` + a parallel burst produced the §5.1 misroute (the full pipeline under load is the fragile case).

**Budget telemetry — read it per-call, not by diffing the global balance.** Every scrape response carries its own billed cost in **`metadata.creditsUsed`** (1 base; +4 enhanced proxy; +1/PDF pg) alongside `proxyUsed` — that's the **attribution-grade** number. Map returns no such field but bills a flat **1/call** (the documented constant). `fc.py` records both to the run manifest and `fc.py spend` sums them into an exact, attributable run total. **Do NOT diff `GET /v2/team/credit-usage` to measure a run** — the key is shared, so concurrent calls from other projects pollute the delta (this is what produced the unattributable 8–58 spread and the "shared key, can't attribute" hedge). That endpoint returns `remainingCredits` / `planCredits` + the billing window at **zero cost**, but its job is **pre-flight headroom only** (warn/abort when low), never run accounting. (Sibling `GET /v2/team/token-usage` tracks the LLM-extraction bucket — relevant only as a signal to keep the extract features we avoid untouched.)

## 4. API key

Lives in the harness env, sourced from `~/.claude/settings.json` → `env.FIRECRAWL_API_KEY`. Check before any call:

```bash
echo "${FIRECRAWL_API_KEY:+present (len ${#FIRECRAWL_API_KEY})}"
# if empty:
python3 -c "import json,os;print(json.load(open(os.path.expanduser('~/.claude/settings.json')))['env']['FIRECRAWL_API_KEY'])"
```

Then `-H "Authorization: Bearer $FIRECRAWL_API_KEY"`. Never `source` an untrusted `.env`.

## 5. Hazards — the "when it breaks" lookup

### 5.1 Geo-misroute + cache collision — *the headline; INVARIANTS doesn't cover it*
A parallel burst returned a **byte-identical `/en-eu/` shell** for 4 different URLs (€-prices), yet `metadata.sourceURL` reported each requested URL correctly. **"Verify sourceURL" PASSES while the body is wrong** — necessary but not sufficient. Firecrawl's default 2-day cache (`maxAge` 172800000ms) is itself a contamination vector (the instant ~0.5s "scrapes" were cache hits). **Fix (all four):** `maxAge:0` · `location:{country:"US",languages:["en-US"]}` · **serialize** (no burst) · **content-md5 dedup across pages** (the strong guard). Plus `waitFor:~3500` for SPAs (integer ms; combined waits ≤60s).

### 5.2 Bot defense / 403 / 429
Plain `curl` to `drinkag1.com` → **429**; many DTC/Cloudflare sites 403 WebFetch. **First captures are Firecrawl-only.** A parallel burst trips rate-limiting → the §5.1 shell. **Fix:** throttle/serialize. **Proxy** (`basic`/`enhanced`/`auto`): `basic` (1cr) handles most; `enhanced` (+4) is the anti-bot proxy; `auto` escalates basic→enhanced on failure. (v1's `stealth` = v2's `enhanced` — agent-workflows still writes `stealth`.) A hard geo-*block* is **visible** as `blocked.` in `metadata.url` (retry once with `enhanced` + `location:US`); a misroute (§5.1) is *silent*.

### 5.3 Map funnel-noise (DTC) — and the map can come back *empty*
AG1's map: **485 URLs, ~80% junk** (94 `/partner/*`, 26 `/people/*`, `/hero-*-lp`, `/sweepstakes-*`, 8 locale subtrees). Linear's 149 were nearly all signal. **Fix:** for DTC, drop `/partner|/people|/hero-*-lp|/sweepstakes|/campaign|` and locale-prefixed paths (`/en-uk`, `/de-eu`, …) before picking key pages. The telehealth cohort confirmed this is universal: every site's map was dominated by funnel/blog/research noise (`/post/*`, `/research/article/*`, paid-funnel landing slugs), and the real product catalog (`/treatment/*`, `/programs/*`) had to be pulled from **homepage links**, not the map. **NEW: a custom SPA can return 0 URLs** (TeloLife — no crawlable sitemap). An empty map is not a failure; fall back to homepage links (the durable discovery surface on *any* site). Net: treat map as a *sample on big sites and possibly empty on SPAs* — homepage links are the reliable source for the key-page set.

### 5.4 Branding quirks
- **Framework: IGNORE `branding.designSystem.framework` entirely — always read the stack from `rawHtml`.** This is a hard rule, not a hedge: the field has been wrong **~9 of 10 times** across the whole corpus (linear "custom", AG1 "bootstrap", AWS "custom", Nike "bootstrap", benadryl "unknown" — all Next.js; the telehealth cohort: Webflow→"custom", WordPress×2→"bootstrap"/"custom", Next.js→"custom"; Maximus's Gatsby→"custom"; only a genuine bespoke SPA's "custom" was right). The `rawHtml` cheat-sheet: `data-wf-*` / `website-files.com` = **Webflow**; `wp-content` (+ `woocommerce`/`elementor`) = **WordPress**; `__NEXT_DATA__` / `/_next/` = **Next.js**; `___gatsby` / `/page-data/` (+ `gatsby-*`) = **Gatsby (React SSG)**; hashed `/assets/*` with no other marker = a custom **React/Vite SPA**; `cdn.shopify.com` = **Shopify**.
- **`branding.images.logo` is unreliable** — inline data-URI SVG (linear), hostable CDN SVG (AG1), `null` (agent-workflows' 3 probes). Use a fallback chain: `<img>` with "logo" in alt/filename → `metadata.favicon` → `og:image` → empty.
- **Color slots are NOT semantically stable** → §6.
- **Don't set `removeBase64Images:true`.** It strips inline data-URI images — and linear's logo came back as an inline data-URI SVG that we needed. Default (keep) is correct for us.

### 5.5 Payload persistence & pruning
Persist every raw response + screenshot to `captures/<date>/.payloads/` (gitignored) — write-once, replay without re-spending. **Download screenshots with Python `urllib.request.urlretrieve`, not `curl -o`** (curl exits 56 on iCloud FUSE paths; URLs expire 24h). iCloud is read-after-write racy — **local scratch → then the store**. Prune progressively (≤14d: all; 15–90d: weekly; 91–365d: monthly; older: quarterly; earliest-per-brand: forever) — ref impl: agent-workflows' `competitive-intel/scripts/prune-payloads.py`.

### 5.6 SPA-shaped sites — soft-404s, empty maps, and A/B flicker
Modern single-page apps (custom React/Vite, headless-CMS+Next.js) break three lazy assumptions; the telehealth cohort hit all three:
- **Soft-404.** Valid deep links can return HTTP **`404`** while rendering full, correct content (TeloLife `/pricing`, `/packages` — real pricing under a 404 status). **Never discard a page on status code alone** — the §5.1 body checks (md5-unique + a thin-markdown guard) are the real signal. (Folded into recipe step 5.)
- **Empty map.** No crawlable sitemap ⇒ `/v2/map` returns 0 URLs. Discover routes from **homepage links** instead (see §5.3).
- **A/B-test instrumentation (e.g. VWO) makes a single capture point-in-time, not stable** (Healthspan: a large inline VWO campaign blob leaks into the markdown as *noise*, and per-SKU prices flicker run-to-run, e.g. $64↔$65, plus homepage modules toggle in/out). **Fix:** treat the testing-tool blob as noise, and when you spot A/B instrumentation, add a one-line caveat to the profile's `unverified_fields` that captured pricing/IA is a snapshot, not a fixed truth.

## 6. Still-open — watch, don't codify (n=2)

- **Client-rendered nav recovery.** Both sites hung their mega-nav/footer outside markdown (even with all formats + `onlyMainContent:false`). We reconstructed from **footer + map + links** — worked twice, but it's a workaround. Candidate real fix: an `actions` `click` to open the flyout, then capture (cheap; untested). **Also note (per Brian): nav can vary by page — that variation is itself signal; keep nav in the captures, don't strip it.** Need more sites before choosing an approach.
- **`brand_colors` slot semantics.** `branding.colors` slots aren't stable: linear's `primary` = body text, true hue = `accent`; AG1's `primary` *was* the brand hue, `accent` the CTA green — a clean **inversion**, and AG1 has a genuine two-color identity. No positional heuristic survives. **Current approach:** retain multiple colors + a vision-confirmed note; never auto-pick a slot.

## 7. Don't use these — and why

The anti-Doro line makes these calls easy: Firecrawl's fanciest features pay credits (and often LLM tokens) for work Opus does free, or pull toward concerns the Frame refused.

| Feature | Why not |
|---|---|
| **LLM extraction** — `json`/`extract`, `/agent` (FIRE-1), `query`, `summary` | Pays Firecrawl credits **+ LLM tokens** (`json` = +4/page) for extraction/reasoning Opus does better and free. Extract from the free `markdown`/`html`/`screenshot` surfaces instead — this is the per-call LLM economics the Frame exists to refuse. |
| **`monitoring` + webhooks** | Hosted scheduled change-detection + push callbacks → violates "not real-time, not a served API." Our freshness is pull-based; scheduled runs are *our* cron over the verb. |
| **`change-tracking`** | Diffing is in the Refused list. (Nuance: basic git-diff mode is free, but it duplicates what `captures/` + git history already give us — don't adopt.) |
| **`/crawl`** | Bills 1 credit/page across the *whole* site — on AG1's 485-URL, ~80%-junk map that's a budget bonfire. Our `map` → selective `scrape` is strictly better. |
| **Firecrawl scraping MCP** | Prefer the raw API (curl): transparent, already allowlisted, and keeps exact control of the knobs our hazards depend on (`maxAge:0`, the format bundle, content-md5 dedup) that a wrapper may hide. |

---

<details>
<summary>Reconciliation with agent-workflows INVARIANTS</summary>

**Agree (their rule holds, our runs confirm):** cheap formats ride one credit (`json`/enhanced-proxy add +4); `/v2/map` `limit:500`, per-call; first-capture = Firecrawl-only, never WebFetch; `rawHtml` mandatory on homepage; payload sidecars gitignored, screenshots expire 24h; homepage often needs a content-vs-nav split (their two-pass A/B — our one rich `onlyMainContent:false` pass carried ~80%, nav came from footer+map).

**Where our runs extend them (INVARIANTS is silent):** the **silent geo-misroute + cache-collision** (§5.1) — they handle only the *visible* `blocked.` geo-block; our additions are `maxAge:0`, **content-md5 dedup**, and serialize-don't-burst (refines their "max 4 concurrent" — on bot-defended DTC, concurrency *causes* the bug). Plus the **DTC map funnel-noise filter** (§5.3) and **`branding.designSystem` framework is wrong** (§5.4, added to their `branding.logo`-is-unreliable flag).

</details>

<details>
<summary>Source verification (docs.firecrawl.dev, 2026-05-30)</summary>

Primary sources: [billing](https://docs.firecrawl.dev/billing), [scrape](https://docs.firecrawl.dev/features/scrape) / [API ref](https://docs.firecrawl.dev/api-reference/endpoint/scrape), [map](https://docs.firecrawl.dev/features/map), [batch](https://docs.firecrawl.dev/features/batch-scrape), [proxies](https://docs.firecrawl.dev/features/proxies), [stealth](https://docs.firecrawl.dev/features/stealth-mode), [interact](https://docs.firecrawl.dev/features/interact), [rate-limits](https://docs.firecrawl.dev/rate-limits).

Confirmed facts: scrape `1 credit/page` base; map `1 credit/call`; add-ons `json +4`, `enhanced proxy +4`, `ZDR +1/pg`, `PDF +1/pg` (nothing else priced); `maxAge` default `172800000`ms (2d), `0` = always-fresh; `waitFor` integer ms (combined ≤60s); `location.country` ISO-3166-1 alpha-2, default `US`; proxy `basic`/`enhanced`/`auto` (v1 `stealth`→v2 `enhanced`). v2 format set: `markdown, summary, html, rawHtml, links, images, screenshot, json, branding, audio, video, query, changeTracking`. Re-verify before trusting when behavior drifts.

</details>
