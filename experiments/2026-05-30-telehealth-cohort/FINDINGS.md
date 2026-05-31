# Findings — Experiment 5 (a real cohort): six telehealth brands

> **Verdict: an apples-to-apples cohort is the strongest evidence yet that cross-company querying works. On the four closed-set axes the brief named, five of six are byte-identical (`target_market`, `offering_category`, `business_model`, `primary_industry`), and `is_multi_product` is the one split — 5 `true` / 1 `false` (TeloLife) — where the `false` is a REAL single-vertical brand, i.e. signal, not a classification wobble. The SCHEMA's own telehealth example (`offering_category: [Services / Consulting, Biotech / Pharma Products]`) fit all six perfectly. The §5 hazards behaved as a *playbook* now: applied prophylactically from page one, they produced a 39-credit, zero-contamination, zero-rescrape run across six DTC/Cloudflare sites — but the cohort promoted several "AG1 quirks" to confirmed DTC/telehealth patterns and surfaced THREE new ones (SPA soft-404, map-returns-0-on-SPA, and a domain-key collision). The Hone strawman check is the headline secondary result: the closed-set classification was 100% right against reality, while every payload-lifted field (colors/fonts/framework) and the gender scope were wrong.**

Run: hand-captures of **eden.health, honehealth.com, getpetermd.com, hims.com, telolife.com, gethealthspan.com**, 2026-05-30, following [`_design/references/firecrawl-capture.md`](../../_design/references/firecrawl-capture.md) §1. Profiles in each `store/<slug>/profile.md`; payloads + screenshots + cleaned markdown in each `captures/2026-05-30/`. Free per-brand head-start from agent-workflows weekly snapshots (site_notes inherited). Capture mechanics via a thin helper, [`fc.py`](fc.py) (bakes in maxAge:0 + location:US + waitFor + the format bundle + md5-dedup/sourceURL manifest). **Corpus is now eleven** (linear, AG1, nike, aws, benadryl + these six).

---

## 1. CONSISTENCY — the headline (did the six classify the same?)

The whole point of the cohort: near-identical companies must classify identically, or cross-company grouping silently fragments. **They did.**

| Brand | target_market | offering_category | business_model | primary_industry | is_multi_product |
|---|---|---|---|---|---|
| Eden | `[B2C]` | `[Services/Consulting, Biotech/Pharma]` | Subscription | Healthcare & Life Sciences | **true** |
| Hone | `[B2C]` | `[Services/Consulting, Biotech/Pharma]` | Subscription | Healthcare & Life Sciences | **true** |
| PeterMD | `[B2C]` | `[Services/Consulting, Biotech/Pharma]` | Subscription | Healthcare & Life Sciences | **true** |
| Hims | `[B2C]` | `[Services/Consulting, Biotech/Pharma]` | Subscription | Healthcare & Life Sciences | **true** |
| Healthspan | `[B2C]` | `[Services/Consulting, Biotech/Pharma]` | Subscription | Healthcare & Life Sciences | **true** |
| **TeloLife** | `[B2C]` | `[Services/Consulting, Biotech/Pharma]` | Subscription | Healthcare & Life Sciences | **false** |

- **4 of 4 brief-named closed-set axes: 6/6 identical.** A query like "all B2C subscription telehealth companies in Healthcare with offering = Services + Biotech/Pharma" returns the whole cohort, cleanly. No near-miss strings, no fragmentation. This is the queryability proof the project is built on, now demonstrated on a real cohort rather than a contrived one.
- **`offering_category` is the strongest result.** All six independently landed on the *exact* two-value hybrid `[Services / Consulting, Biotech / Pharma Products]` — and in the same order (Services first). That's the SCHEMA's own worked telehealth example, and it generalized to six real sites with zero strain. The closed-set discipline did exactly its job.
- **The one divergence is real, not a wobble.** TeloLife's `is_multi_product: false` is correct: it pivoted (see §3) to a **single-vertical GLP-1 weight-loss brand** — semaglutide vs tirzepatide are drug *options*, 3/6/9/12-mo are *duration* variants, of the one program. Every peer is genuinely multi-vertical (`true`). So the split is a *true negative*, the most valuable kind: a query for "multi-product telehealth brands" correctly excludes TeloLife. The field discriminated exactly where it should.

**Net:** on an apples-to-apples set, the closed-set taxonomy did not drift. The #1 threat to cross-company querying did not materialize.

---

## 2. The Hone strawman check (brief called this out)

honehealth.com is the worked example in [`SCHEMA.md`](../../SCHEMA.md). Reality vs. the strawman:

| Field | Strawman (SCHEMA.md) | Captured reality | Verdict |
|---|---|---|---|
| `entity_type` | Company | Company | ✅ |
| `target_market` | `[B2C]` | `[B2C]` | ✅ |
| `offering_category` | `[Services/Consulting, Biotech/Pharma]` | same | ✅ |
| `is_multi_product` | true | true | ✅ |
| `business_model` | Subscription | Subscription | ✅ |
| `primary_industry` | Healthcare & Life Sciences | Healthcare & Life Sciences | ✅ |
| `brand_colors` | `{primary #0E3A2F green, accent #C7A867 gold}` | **#F8F93F yellow + #0E0B20 navy** | ❌ invented |
| `fonts` | `[Söhne, Tiempos]` | **[DM Sans, STIX Two Text]** | ❌ invented |
| `design_framework` | `next.js` | **WordPress** | ❌ wrong |
| `description` | "…to **men**…" | mixed-gender (full Women's Care line) | ❌ over-narrowed |

**The lesson is clean and important: the closed-set classification is *guessable* (a knowledgeable author nailed all six enums from memory), but the payload-lifted fields are *not* — they must be captured.** Colors, fonts, framework, and the gender scope were all plausibly wrong in the strawman. This validates both halves of the SCHEMA's instruction at once: closed-set fields are stable enough to grade against, and "lift visual identity straight from `branding`… copy, don't analyze" / "classify from what you captured, not memory" is exactly the right rule for everything else.

---

## 3. is_multi_product across the cohort — the tie-breaker held, and the field is EASY here

Eleven-company picture for this field is now well-mapped, and the telehealth shape adds a clean lesson:

- **5× `true`** (Eden, Hone, PeterMD, Hims, Healthspan): all multi-vertical — weight loss / hormones / hair / longevity / sexual / mental are distinct, separately-chosen programs, each its own page + price. The "would you comparison-shop them?" test is trivially yes.
- **1× `false`** (TeloLife): single vertical (GLP-1 weight loss); molecule + duration are variants of one program. Trivially no.
- **None hit the "hard middle."** Experiment-3 concluded the field is "only hard in the middle" (AG1's flagship-plus-companions; Benadryl's one-molecule-many-forms). The telehealth cohort confirms the *easy* poles: **a vertical IS a product**, so a multi-vertical clinic is an obvious `true` and a single-vertical brand an obvious `false`. The tie-breakers ("flagship + named companions ⇒ true"; "one purpose, many forms ⇒ false") were never even stressed — verticals make the call unambiguous. Good news for the field's reliability on this whole category.

**TeloLife is also the experiment's vivid argument for capturing live, not from memory:** the 2026-05-11 weekly snapshot had it as a *multi-vertical Shopify* brand (would have classified `true`). It has since dropped longevity + hair, rebuilt on a custom SPA, and rebranded — now correctly `false`. A memory/snapshot-based classifier would have gotten it backwards.

---

## 4. §5 hazards across the cohort — promotions + NEW ones for the playbook

### Recurred → promote from "AG1 quirk" to confirmed DTC/telehealth pattern
- **§5.2 bot defense is the category default.** Plain `curl` → **403 on hims.com**, **blocked/no-response on petermd.com**; Cloudflare fronts Hone/PeterMD/Hims. The "first capture = Firecrawl-only, never WebFetch" rule is not situational for telehealth — it's the baseline. (Webflow/Eden, SPA/Telo, Vercel/Healthspan were also Firecrawl-only by necessity.)
- **§5.3 map funnel-noise is universal.** PeterMD ~494 URLs dominated by paid-funnel slugs (`/trt-survey`, `/landing-page*`, `/your-trt-assessment`…); Healthspan ~494 dominated by `/research/article/*` (250+); Eden ~485–496 by `/post/*` blog; Hims 292 with `investors.`/`support.` subdomains. **In every case the signal set (~10–20 pages) had to be hand-picked, and the `/treatment/*` or `/programs/*` catalog came from homepage links, not the map.** Promote: for DTC/telehealth, treat map as a taxonomy-revealer, filter funnel/blog/locale, and extract the real catalog from homepage links.
- **§5.4 `branding.designSystem.framework` is reliably WRONG — now ~9/10 across the whole corpus.** This cohort: Webflow→"custom", WordPress→"bootstrap", WordPress→"custom", Next.js→"custom"; only TeloLife's "custom" was plausibly right (it IS a bespoke SPA). **Hard rule, not a quirk: ignore the field; read the framework from `rawHtml`** (`data-wf-*`/website-files.com = Webflow; `wp-content`/woocommerce = WordPress; `__NEXT_DATA__`/`/_next/` = Next.js; hashed `/assets/*` = a Vite/React SPA). The cohort spans 4 distinct stacks (Webflow, WordPress×2, Next.js, custom SPA, + Hims unverified) — `rawHtml` nailed each.
- **§5.1 geo/cache contamination did NOT fire — because the fix was applied from page one.** All 39 scrapes: unique bodies, matching sourceURLs (the md5-dedup manifest was clean on every brand). Confirms Experiment-3: `maxAge:0` + `location:US` + `waitFor` + serialize *prophylactically* keeps the hazard latent. The guard is now cheap insurance, not a reaction.
- **`branding.colors` slot instability, continued.** Three brands (Hone #F8F93F, PeterMD #FFFF64, Healthspan #FEF38E) had `primary` = a true (yellow) hue; Hims' `secondary` #0000EE is a junk link-blue (not a brand color); Eden's `primary` #4EEAFF cyan is a soft accent, not the dominant. `logo` was a data-URI SVG or null on all six (favicon/S3 fallback used every time). No positional rule survives — vision-confirm against the screenshot, as before.

### NEW hazards the playbook should absorb
1. **SPA "soft-404" (TeloLife).** `/packages` and `/pricing` returned **HTTP 404 status but rendered full, correct content** (client-side routing). The §5.5 verify checks sourceURL + body-md5 but **not** status code — good, because a status-based "discard 404s" filter would have wrongly thrown away real pricing. **New guidance: on SPAs, do not discard a page on status code alone — trust body length/content (the md5-dedup + a thin-markdown guard already cover the real failure modes).**
2. **`/v2/map` returns 0 URLs on a custom SPA (TeloLife).** No crawlable sitemap → empty map. Not a failure — discover routes from homepage links (we did). Extends §5.3: map is a *sample on big sites* and can be *empty on SPAs*; homepage links are the durable discovery surface either way.
3. **A/B-testing instrumentation as content noise + pricing flicker (Healthspan, VWO).** The homepage markdown carries a large inline VWO campaign blob (noise), and VWO makes pricing/IA flicker between runs (e.g. Rapamycin $64↔$65, Goals-grid present/absent). **Single-capture pricing on VWO-instrumented sites is point-in-time, not stable** — worth a one-line caveat in such profiles' `unverified_fields`.
4. **Domain-key hazards (the alias-check curl earned its keep three times).** See §6.

---

## 5. Credits per brand vs. the ~7–10 budget

**39 credits total** (balance 2105 → 2066), all clean — zero contamination, zero re-scrapes, zero wasted:

| Brand | Credits | = map + scrapes |
|---|---|---|
| Eden | 7 | 1 + 6 |
| Hone | 7 | 1 + 6 |
| PeterMD | 7 | 1 + 6 |
| Hims | 7 | 1 + 6 |
| Healthspan | 7 | 1 + 6 |
| **TeloLife** | **4** | 1 + 3 (single-vertical ⇒ fewer key pages) |

- **Five brands landed at exactly 7 — the low end of the 7–10 budget** — and TeloLife came in *under* at 4 because a single-vertical brand has fewer key pages worth walking. The budget is accurate; the breadth-first / shape-not-SKU discipline keeps even multi-vertical catalogs at 6 key pages.
- **Beats AG1's 12 (which had 5 wasted on the §5.1 misroute).** The whole cohort confirms the architecture's promise: once the hazards are in the playbook and applied from page one, captures are cheap and clean. The free alias-check curls (§1.1) and the `site_notes` carry-forward from prior weekly snapshots removed all rediscovery cost.

---

## 6. Domain / parent / brand-of (BACKLOG gaps)

### Parent / brand-of — 1 of 6, the 4th corpus sighting
- **Hims → Hims & Hers Health, Inc. (NYSE: HIMS, founded 2017), with sibling brand Hers (forhers.com).** hims.com is the men's consumer brand of a public parent. Per the Experiment-3 nuance, it operates as a full business (own storefront/brand/transactions) → `entity_type: Company` (like AWS), not `Other` (like Benadryl). **Recorded as a commented `# NOTE` block + prose, since the SCHEMA still has no `parent:` / `brand-of:` / `sibling-of:` frontmatter field.** This is now the **4th independent sighting** of the relationship gap (after AWS→Amazon, Benadryl→Kenvue, Nike→Jordan/Converse) — well past the BACKLOG ≥2 bar. Flagged, not invented, per brief.
- The other five appear independent (named founders, no parent surfaced): Eden (cofounders Adam McBride/Josh Khan), Healthspan (founder Daniel + Dr. Elana Miller story), PeterMD, Hone, TeloLife.

### Domain-key hazards — the alias-check curl (§1.1, FREE) caught three, and they argue for a store convention
The brief listed brand domains that turned out to diverge from canonical for **three of six**. The free `curl -sIL` resolved each before a single credit was spent:
- **Eden — same-day migration.** `tryeden.com → www.tryeden.com → www.eden.health` (301 chain, the migration landed *on capture day*). Keyed on the new canonical `eden.health`, old domain → `aliases` (AG1 precedent).
- **PeterMD — blocked/non-canonical marketing domain.** `petermd.com` does **not** resolve (Cloudflare-blocked on curl); the live site is **getpetermd.com**. Keyed on getpetermd.com; petermd.com noted as a non-resolving alias.
- **Healthspan — namespace COLLISION (the sharp one).** `healthspan.com` resolves to its **own live 200 site** — a *different company* (the UK consumer-supplement brand), NOT this telehealth clinic. The telehealth brand is **gethealthspan.com**. This is the cleanest demonstration that **"domain is the key" only works if you key on the *resolved canonical*, never the brand's casually-stated domain** — the obvious domain belonged to someone else.

**Store-convention recommendation (decision for Brian):** I keyed all folders on the resolved canonical domain (`eden-health`, `getpetermd-com`, `gethealthspan-com`) rather than the brief's illustrative slugs (`tryeden-com`, `petermd-com`, `healthspan-com`), to keep folder == `domain:` == canonical key (consistent with `store/drinkag1-com`). This deviates from the brief's literal slug examples — easy to rename if you'd rather, but the collision (healthspan.com) makes keying-on-canonical the safer default. Candidate playbook addition: **make the §1.1 alias-check curl mandatory and have it decide the store key** (resolved canonical → folder + `domain:`; everything else → `aliases:` or a collision flag).

### `target_market` B2B2C — a consistency-vs-accuracy tension (flag)
I set all six to `[B2C]`. Eden runs a dedicated **B2B2C "Partner with Eden"** program (real second motion); PeterMD/Hone/Healthspan run affiliate/creator programs. A strict reading would add `B2B2C` to Eden. I kept it in prose to protect cohort consistency (the whole point of §1), but flag it: **if a consumer wants "find B2B2C telehealth," Eden is currently invisible to that query.** Not resolved here — it's the same "rank multi-select, primary first" judgment the SCHEMA already allows; worth a convention note on when a secondary channel earns an enum slot.

---

## 7. Other cohort signals (durable state worth recording)

- **The "men's health" brands are now mixed-gender.** Hone (explicit dual Men's/Women's grids), PeterMD ("For Her" line), Hims (sibling Hers), Eden (women's hormone therapy — but, notably, **no men's TRT**, the lone catalog inversion). The category is converging on whole-household coverage; "men's health telehealth" is an increasingly leaky label.
- **Three of six are yellow-forward brands** (Hone #F8F93F, PeterMD #FFFF64, Healthspan #FEF38E) — a real visual convergence in the category. Hims (warm tan/brown) and TeloLife (sage green) are the outliers; Eden is neutral.
- **Two of six use a `get`-prefixed canonical** (getpetermd.com, gethealthspan.com) while marketing under the bare brand name — a DTC naming pattern that *is* the domain-key hazard above.
- **Compounded-GLP-1 + the FDA-language compliance dance is category-wide.** PeterMD's persistent Tirzepatide buy-panel softening ("Clinically proven" vs descriptive "FDA-approved"), Hims' off-label-use framing on T2D-only GLP-1 PDPs, and the universal "compounded drugs not FDA-evaluated" disclaimers are a shared regulatory posture — exactly the kind of *state* the engine should record (events/judgments stay downstream).
- **The `[Services, Biotech/Pharma]` hybrid spans an internal spread the enum absorbs cleanly:** Healthspan/Hone are membership+coaching-heavy (more service-weighted), Telo/Eden are Rx-fulfillment-heavy (more product-weighted) — yet the same two-value hybrid fits all. No strain, but it shows the hybrid is doing real work holding a spectrum together under one queryable label.

---

## Caveats

- Eleven fixtures now; these six are the first true *cohort* (deliberately near-identical), which is what makes the §1 consistency result meaningful — it's the case most likely to fragment, and it didn't.
- All hand-run, US-locale, 2026-05-30, single capture each. VWO (Healthspan) and A/B/render flicker mean point-in-time pricing; `unverified_fields` flags the quiz-walled prices across the cohort (the real per-SKU price almost always lives behind the intake quiz — a structural limit of marketing-site capture, not a miss).
- TeloLife was deliberately walked light (4 credits) because it's single-vertical — its `false` is the most-scrutinized call here and is well-grounded (old multi-vertical snapshot + fresh single-vertical site both inspected).
- Playbook corrections to fold into [`firecrawl-capture.md`](../../_design/references/firecrawl-capture.md): (1) §5.4 framework-is-wrong is now a hard rule (~9/10); (2) NEW §5 entries — SPA soft-404 (don't discard on status), map-returns-0-on-SPA, VWO/A-B flicker caveat; (3) promote the §1.1 alias-check curl to mandatory + let it decide the store key (canonical → folder/`domain:`, else `aliases:`/collision flag). All flagged, none silently folded.
