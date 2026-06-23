# Findings — Experiment 2 (breadth): a DTC consumer-health brand (AG1)

> **Verdict: the fed-in playbook eliminated every self-inflicted waste from the linear run — but a genuinely NEW hazard (geo-misrouted, cache-collided identical content that the `sourceURL` check could not catch) cost 5 credits and is the headline lesson. The SCHEMA held for a totally different shape (real multi-SKU DTC catalog vs. clean SaaS), straining in exactly two predicted places (`is_multi_product`, `brand_colors`) plus one new one (`primary_industry` for a wellness/supplement brand). `offerings.md` now clearly earns its keep.**

Run: hand-capture of **drinkag1.com** (AG1, formerly Athletic Greens), 2026-05-30. Profile at [`store/drinkag1-com/profile.md`](../../store/drinkag1-com/profile.md); raw payloads + 3 screenshots + cleaned markdown in `store/drinkag1-com/captures/2026-05-30/`. Companion to the [first-capture FINDINGS](../2026-05-30-first-capture/FINDINGS.md) (linear.app).

---

## Did the fed-in playbook help? (the "did it do better" metric)

**Yes — unambiguously, on everything it covered.** Linear's run wasted credits on: a forgotten `branding` re-scrape, a split pricing screenshot/html call, `/product` login-wall dead-ends, and a contamination re-scrape. **AG1 hit zero of those** — every one was pre-empted by feeding the punch list in:

| Linear lesson, fed in | AG1 outcome |
|---|---|
| Homepage: all formats on ONE credit, request `branding` + `rawHtml` explicitly | First try, complete — branding + rawHtml + screenshot + links all present, no re-scrape |
| Verify `metadata.sourceURL` == requested URL | Applied on every response from the start (but see new hazard — it wasn't enough) |
| Pricing = screenshot + html same call | Applied (turned out unnecessary — prices were in markdown; see below) |
| Thin-markdown guard (<500c / wall) | Caught the thin/again-EU `about-us`, triggered the redo |
| Reconstruct nav from footer + map | Applied — nav *was* client-rendered as predicted |
| Local scratch → iCloud persist | Applied — zero read-after-write races this run |
| `branding` quirks (framework wrong; primary≠hue) | Both anticipated — saw `designSystem:"bootstrap"` (wrong, it's Next.js) and the primary/accent question immediately |

### Credits: **12 actual vs. linear's ~9–10 clean-run estimate**

- **2** — map + homepage (both clean, first try).
- **5 — WASTED** — a parallel batch of 5 key-page scrapes all returned compromised content (the new hazard below).
- **5** — re-scrapes with the fix (1 test + 3 + 1 about), all clean.

**Net read:** the *output* is a 7-credit clean run (1 map + 6 pages). The 5 wasted credits were **100% the new hazard**, not playbook failure or rediscovery. With the new `maxAge:0 + location:US + waitFor` knob now written into `site_notes`, **the next AG1 capture should land at ~7 credits — beating linear's 9–10 estimate.** So: the playbook made the *known* parts cheaper than linear; a new unknown made *this* run more expensive; the new lesson is now captured, closing the loop the architecture promises (`site_notes` carry-forward).

---

## NEW capture hazards (beyond linear's punch list)

1. **Geo-misroute + cache collision returns identical wrong content — and `sourceURL` still reports the requested URL.** The headline. A parallel burst of 5 scrapes returned a **byte-identical `/en-eu/` European homepage shell** (md5 match across 4 URLs; €-prices, `/en-eu/` links) for `/products/...`, `/ingredients`, `/ag1-membership` — yet `metadata.sourceURL` correctly said `/products/greens-powder-pouch` etc. on each. **Linear's invariant ("verify sourceURL; re-scrape on mismatch") PASSES here while the content is wrong.** It is necessary but not sufficient.
   - **New guard:** compute a **content md5 (or length) dedup across captured pages** — two distinct URLs returning identical bodies is the real contamination signal. (sourceURL-match is a weak prior; body-identity is the strong one.)
   - **The fix that worked:** scrape pages **individually** (no parallel burst) with `location:{country:"US",languages:["en-US"]}` + **`maxAge:0`** + `waitFor:~3500`.
2. **Firecrawl's default response cache (`maxAge` ≈ 2 days) is itself a contamination vector.** The instant ~0.5s responses on two of the bad scrapes were cache hits. For *first-capture correctness*, force `maxAge:0`. (Re-reads / freshness passes can re-enable caching — it's a capture-time, not query-time, rule.)
3. **Bot defense is real: plain `curl` to `drinkag1.com` returns HTTP 429.** Confirms the INVARIANTS "Firecrawl-only, never WebFetch on first capture" rule with teeth, and explains why a **parallel burst** tripped rate-limiting → fallback shell. Throttle / serialize on bot-defended DTC sites.
4. **Map explodes with marketing-funnel noise on a DTC brand.** `/v2/map` returned **485 URLs**, but ~80% were funnel/junk: **94 `/partner/*`, 26 `/people/*`**, dozens of `/hero-*-lp`, `/sweepstakes-*`, affiliate landers, + 8 locale subtrees (`/en-uk`, `/de-eu`, ...). Linear's 149 URLs were almost all signal. **Key-page selection for DTC needs aggressive filtering** (drop `/partner|/people|/hero-*-lp|/sweepstakes|/campaign|locale-prefixed`); the signal set was ~20 pages.

---

## Did the recurring ones show up again?

- **`is_multi_product` — YES, and resolved OPPOSITE (true).** Linear was the unified-app `false`; AG1 is the **flagship-plus-stack `true`** (AG1 / AGZ / D3+K2 / Omega-3 are separately-named, separately-bought, separately-positioned). The TAXONOMIES test worked, but note the tension that made it *hard*: the brand **self-positions as anti-proliferation** ("we never make anything new just to sell you on more"). **Both of the first two captures landed on the ambiguous edge of this field** — strong evidence it's the single least-stable classifier. The Notion tie-breaker covers the SaaS direction; AG1 shows the field also needs a "flagship + companion SKUs ⇒ true" cue.
- **pricing-on-homepage / JS-walled — DID NOT recur.** AG1's prices ($79/mo, $99 one-time, $219/3-mo) were **plainly in the markdown** once US-geo'd. So "prices are JS-walled, recover from screenshot/html" is a **linear/SaaS trait, not a universal rule**. Keep the screenshot+html-same-call as cheap insurance, but don't *assume* markdown lacks prices — for DTC the markdown often has them.
- **`brand_colors` — YES, and INVERTED.** Linear: `primary` = body text gray, true hue = `accent`. AG1: `primary` (#0C3D3D deep green) **IS** a true brand hue (logo/header/footer/pouch); `accent` (#46DE46) is the bright CTA green. **This kills any positional heuristic** like "accent = the brand color." AG1 also genuinely has a *two-color* identity, so "the brand color" is itself ambiguous. Reinforces: retain multiple colors + a vision-confirmed note; do not auto-pick a slot. (Logged as the open SCHEMA question, per brief — not solved here.)
- **`sourceURL`-contamination — YES, in a worse form** (see New Hazard #1). The guard must be upgraded from URL-match to body-identity.

---

## Where the SCHEMA generalized vs. strained (linear + AG1)

**Generalized cleanly across both shapes:**
- **`aliases`** — finally exercised by the Athletic Greens → AG1 rebrand, and worked perfectly. The redirect verify was a **free** `curl -I` (301 → drinkag1.com) before spending any Firecrawl credit — a nice cheap pattern worth keeping in the verb.
- Identity, capture-meta, `description` (~220c landed), `target_market` (B2C clean), `business_model` (Subscription clean, one-time noted as secondary), nav, credibility, visual/brand impression, strategic read — all natural.

**Strained:**
- **`primary_industry` (NEW strain).** A supplement/wellness DTC brand straddles **Healthcare & Life Sciences** vs **Consumer Goods** with no clean fit — chose Healthcare for the clinical-research/NSF/nutrition-science positioning, but it's a documented judgment call. The "heaviest taxonomy" lives up to its billing; supplement brands are a recurring straddle to watch.
- **`offering_category`.** Needed a 2-value hybrid (**CPG + Retail/E-Commerce**), and the CPG↔Retail/E-Commerce line is inherently fuzzy for *any* DTC brand (everything direct-to-consumer is both). Workable, minor.
- **`is_multi_product` + `brand_colors`** — the two recurring strains (above).
- **No home for a real product catalog → `offerings.md` now clearly earns its keep.** Linear flagged "no home for pricing tiers"; AG1 makes it acute: a genuine multi-SKU catalog (AG1 + variants/flavors/travel + AGZ + D3K2 + Omega + bundles, each with its own price/form/claims) had to be compressed into the `## What they offer` prose. **For DTC/CPG, `offerings.md` (per-SKU price/form/claims, breadth-first) is the right structure** and should be the first opt-in module enabled for a commerce-shaped project. The flat `key_pages` dict also wanted product-vs-content grouping again (same flag as linear's surfaces-vs-features).

---

## Caveats

- Two fixtures now (one clean B2B SaaS, one heavy B2C DTC). The lifecycle and SCHEMA hold across both; the recurring-hard fields (`is_multi_product`, `brand_colors`) are confirmed by *both* hitting their ambiguous edges.
- The geo/cache hazard (New #1) was observed decisively (md5-identical across 4 URLs) — not flakiness. But the exact trigger (parallel burst vs. default cache vs. proxy geo) wasn't fully isolated; the fix (`maxAge:0` + `location:US` + serialize) addresses all three and is now in `site_notes`. Worth one controlled probe before the verb hard-codes which knob is load-bearing.
- Prices/claims are US-locale, captured 2026-05-30; AG1 runs 8+ locale storefronts with different pricing/currency.
</content>
