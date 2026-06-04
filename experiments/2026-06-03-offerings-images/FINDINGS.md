# Probe: hero product-image extraction for `offerings.md` (2026-06-03)

> **Question.** Can we durably capture a **clean hero product render** per flagship SKU (for the
> Teleprescribe Product Rendering System) cheaply and reliably? Run on Hims's already-persisted
> `captures/2026-06-03/.payloads/` — **zero new Firecrawl spend**. n=1 site (Hims; Cloudinary CDN).

## Verdict — feasible, with one recipe change + a headed download

**Source the render from `images[]` filtered by URL path — not `og:image`.** Visual proof: the path-filtered
pick (`/products/.../HH-WL-Foundayo-Pill-...-Float-FDA`) is a **clean isolated product render**; the
`og:image` (`Hims-SEO-WL-Image`) is a **lifestyle/SEO marketing card** (model on a colored backdrop), useless
as a product reference. og:image is reliably *present* but reliably the *wrong content* → fallback only.

## The four findings

1. **`images[]` requires the rich format bundle.** Lean PDP scrapes (`markdown,links,screenshot`) carry **no
   `images[]` and no html** — only `og:image` survives in metadata. The rich `--homepage` pass carries
   `images[]` (98 on the WL category page). **So flagship PDP scrapes must add the `images` format** — it's
   **free** (rides the 1-credit base, recipe §3). This is the only capture-recipe change idea 1 needs.
2. **Path heuristic selects the render.** Product renders sit under `/products/` `/pdps/` with tokens
   `Float`/`-product`/`-pill`/`-pen`/`vial`; noise is path-separable (`f_svg` icons, `/footer/`,
   `navigation`, `qr-code`, `/testimonials/`, `-BA-`/`-Before`/`-After`, `-SEO-`/`-Share`, `Expert-Section`
   editorial). Caveat: bare `/storefront/` is too broad (caught an editorial section) — require a
   product-name token alongside. Width regex must accept the `,w_499` comma form (Cloudinary).
3. **Download needs headers; bare `urlretrieve` 403s.** The Hims CDN is bot-defended like the HTML pages
   (§5.2). **Bare fetch AND naive UA both 403**; **Referer (`https://www.hims.com/`) + a real browser UA
   succeeds** — og:image → valid 109KB JPEG, product render → valid 9.6KB WebP. Validate magic bytes after
   download (some `images[]` entries are **mangled Cloudinary fragments** — split on the transform path).
4. **Cloudinary URLs are resolution-transformable.** `w_499` → `w_1200` (or drop the cap) yields a higher-res
   reference asset for free — nice-to-have for a rendering library.

## Recommended shape (idea 1 = asset capture, not a roster field)

- Add `images` to flagship PDP scrapes (free). Select hero via path-score → validate magic bytes →
  headed download (Referer=company root + browser UA) → optional Cloudinary upscale.
- Store `captures/<date>/images/<sku>.<ext>`; reference from the flagship **deep block**. No roster column.
- Keep `og:image` as the fallback when `images[]` is absent/empty (lean scrape) or all candidates fail.

## What this n=1 probe CANNOT claim

- **Generalization across hosts.** Hims = Cloudinary + bot-defended. Eden (Webflow), Hone (WordPress) will
  differ in image hosting, og:image quality, and bot defense — the headed-download trick may not carry, and
  the token list (`Float`, `el-rot-fda-badge`) is Hims-flavored. The **approach** (path-score +
  magic-byte validation + headed fetch + screenshot fallback) generalizes; the **exact tokens** don't.
- **og:image quality is site-dependent.** On a simpler site og:image may *be* the clean render — which is
  why it stays a fallback, not a reject.
- **Fallback of last resort** = the full-page `.png` screenshot we already persist (the render is in it,
  just composited with page background).

## Repro
`python3 probe.py` (reads the persisted payloads; writes `out/product.png` = the clean render evidence).

---

# n>1 validation — 5 more sites, real vision analysis (2026-06-03)

> Workflow `hero-image-validation` (11 agents, ~600K tok): per site, a vision agent classified all 11
> candidates + named the true hero; an **independent adversarial agent** re-checked the claimed hero + the
> heuristic's rank-1; a synthesis agent ruled on generalization. Platform-diverse: eden=Webflow,
> hone=WordPress, ro/gogeviti/agelessrx=custom/Contentful. Ran on pre-downloaded candidates — **zero spend**.

## Verdict: GO-WITH-CHANGES

| Site | Platform | rank-1 a clean hero? | og:image content |
|---|---|---|---|
| honehealth | WordPress | ✅ yes | product render (the one near-hit) |
| ro.co | custom | ✅ yes (r01–r09 identical render) | lifestyle card |
| gogeviti | custom | ✅ yes | lifestyle card |
| eden | Webflow | ❌ lifestyle model (no product) | product-in-context |
| agelessrx | custom | ❌ packaging-only box | lifestyle card |

- **Precision@1 = 3/5** (raw 60%, directional on n=5) — ground-truthed on the *adversarial* `rank1_confirmed`, not the analyzer's self-claim.
- **Site-level recall = 5/5** — every platform had an adversarially-confirmed clean hero **inside the downloaded top-10**. The heuristic never failed to put a usable hero in front of the picker; it only failed to *rank it first* on 2/5.
- **Download = 6/6 platforms** (incl. Hims) via headed Referer+UA. Generalizes.
- **og:image = 0/5 clean renders.** Content quality is a platform lottery (WordPress/Yoast set a render; custom/Webflow default to marketing cards). Reliable to fetch, reliably-enough wrong → **fallback only, never primary**.

## The two failure modes (both understood, both fixable)
1. **Recall miss — Webflow `nav-` over-rejection.** The NEG token `/nav`+`nav` nukes Webflow's hero-naming convention (`nav-nad.webp`, `nav-sermorelin.webp`) — eden's 3 best renders were thrown out *entirely* (never downloaded). This is the dangerous class: a recall miss can't be recovered by a later vision pick. **Fix: reject `/nav/` path SEGMENTS, not any filename containing `nav`.**
2. **Precision miss — packaging vs. isolated render.** agelessrx rank-1 was a NAD+ patches *carton* (packaging-only); the clean B12 vial was r02. The path heuristic structurally can't see "isolated-on-white" vs "box shot."

## Per-SKU recall gap (the real limitation)
Site-level recall is 5/5, but **specific molecules** had renders that fell outside top-10 and were never captured: hone missed 8 (`Hone_Men_Enclomiphene_1200x1200`, topiramate, naltrexone…), ro missed 6 (`Generic_-_viagra_-_renders`), eden missed 3. A flagship SKU's render can exist on-page yet not get grabbed. **Mitigation: raise the candidate cap (download is free/headed) — recall-first.**

## The simplification (vs. the synthesis's full tuning list)
The heuristic doesn't run alone in production — it feeds a **vision-capable Opus capture agent**. So split the labor: the **deterministic heuristic does RECALL** (proven 5/5 — surface clean heroes into the candidate set, don't over-reject), and **Opus does PRECISION by looking** (it correctly read agelessrx packaging-vs-vial, eden model-vs-vial). That collapses most recommended tuning (per-platform regex profiles, aspect-ratio math, hero/packaging POS split) — the agent handles precision for free. **Keep only the recall-protecting fixes:** the Webflow nav-segment fix + a higher candidate cap. og:image stays last-resort fallback.
