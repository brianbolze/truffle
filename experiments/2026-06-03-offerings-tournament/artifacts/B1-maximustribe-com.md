# Maximus — offerings

*Design B1 (roster-first), scope: GLP-1 weight-loss + TRT/testosterone lines. Built from persisted captures of maximustribe.com (fetched 2026-06-03). Prices verbatim. Within-company key = page slug; no cross-company canonical key — "semaglutide here = semaglutide elsewhere" is a query-time grouping, not asserted.*

## Portfolio overview

Maximus is a **multi-product** direct-pay telehealth brand. Its catalog is organized as **treatment categories → protocols**, where each *protocol* is the buyable thing (a monthly subscription) and a category is a non-buyable grouping. This doc covers the two largest lines:

- **Testosterone** — the flagship/origin line, the deepest by far. It splits into two interpretive sub-families the site itself draws: **Fertility-Friendly Testosterone** (Enclomiphene-based, "boosts your own production") and **Traditional TRT** (exogenous testosterone — cream/injectable). Combination protocols layer the two (Enclomiphene + cream/oral) or add a fertility adjunct (Injectable + hCG). Eight buyable protocols in all, $99.99–$299.99/mo, plus a one-time at-home test that feeds intake.
- **Weight Loss (GLP-1)** — two buyable protocols, Semaglutide and Tirzepatide, both compounded, both sold as "personalized dose" monthly plans. Available to men *and* women (the rest of the catalog is men-first).

Hierarchy (indexed level = the buyable protocol):

```
Testosterone (family, /testosterone)
├─ Fertility-Friendly
│  ├─ Enclomiphene                         /testosterone/enclomiphene-only
│  ├─ Enclomiphene + Testosterone Cream    /testosterone/Testosterone-Cream-and-Enclomiphene   ← flagship, patented
│  └─ Enclomiphene + Oral Testosterone     /testosterone/oral-testosterone-and-enclomiphene
├─ Traditional TRT
│  ├─ Testosterone Cream                   /testosterone/Testosterone-Cream
│  ├─ Oral Testosterone                    /testosterone/oral-testosterone
│  ├─ Injectable Testosterone              /testosterone/Injectable-TRT
│  └─ Injectable Testosterone + hCG        /testosterone/Injectable-TRT-and-hCG
└─ At-Home Testosterone Test               /lab-tests   (one-time, feeds intake)

Weight Loss / GLP-1 (family, /weight-loss)
├─ Semaglutide                             /weight-loss/semaglutide-standard
└─ Tirzepatide                             /weight-loss/tirzepatide-standard
```

**Pricing pattern, two shapes.** The four standalone TRT protocols plus the flagship combo publish a full **1-month / 3-month / 12-month ladder** on their own pages (price drops as plan length grows; "Starting at" = the 12-month tier) — so the actual number for each plan length is visible → `[published]`. The other three TRT protocols expose only a "Starting at" floor (no per-page ladder captured), and both GLP-1s show a "from $X/mo" floor with the real number set by prescribed dose during intake → `[partial]`. Every protocol's *final* all-in still routes through a free quiz + physician review on `app.maximustribe.com`, and a sitewide asterisk notes "Pricing varies by dosage and plan length. May vary slightly by state."

---

## Deep blocks — flagship / most-compared

### Enclomiphene + Testosterone Cream  *(the hero protocol)*
**Parent:** Testosterone · **url:** `/testosterone/Testosterone-Cream-and-Enclomiphene` · **price:** $189.99/mo (12-mo tier) · **price_visibility:** `[published]` (full ladder shown)

> H1: **"Enclomiphene + Testosterone Cream"**
> Sub-positioning H2: **"The revolutionary testosterone plan _you can only get at Maximus._"** — "Our patent-pending protocol gives you the best of both worlds: the hormonal boost of TRT plus fertility-friendly protection… Backed by our own published clinical studies."

Exact price ladder (verbatim):
- **1 Month — $289.99/mo**
- **3-Month Plan — MOST POPULAR — $239.99/mo**
- **12-Month Plan — BEST VALUE — $189.99/mo**
- Spine anchor elsewhere on page: "**Enclomiphene + Testosterone Cream** starting at **$189.99**/mo" and "Starting at $189.99/mo"
- Footnote: "\*Pricing varies by dosage and plan length. May vary slightly by state." · "Split your payment into manageable installments with Klarna."

Includes / audience: "**Best for:** Men who want our most effective, easy-to-use, once daily topical testosterone solution while maintaining fertility markers." Badges: *Patented Formulation · Fertility-Friendly · Oral + Topical · Daily.* Bundles: "Add Tadalafil to your protocol for free." Claims: "Average peak testosterone levels of 1,321 ng/dL (Results may vary)"; "Maintains important fertility markers, LH and FSH."

### Enclomiphene  *(the starter / most-reviewed)*
**Parent:** Testosterone · **url:** `/testosterone/enclomiphene-only` · **price:** $99.99/mo (12-mo tier) · **price_visibility:** `[published]`

> H1: **"Enclomiphene"** · BEST FOR strip: "Men who want to naturally boost testosterone while preserving fertility and supporting daily energy in a once-a-day pill."

Exact price ladder (verbatim):
- **1 Month — $199.99/mo**
- **3-Month Plan — MOST POPULAR — $149.99/mo**
- **12-Month Plan — BEST VALUE — $99.99/mo**
- Spine anchor: "**Enclomiphene** starting at **$99.99**/mo"; footnote "\*Pricing varies by dosage and plan length. May vary slightly by state."

Includes / claims: "Stimulates your body's natural testosterone production"; "No testicular shutdown associated with traditional TRT"; "Up to 2x increase to testosterone without the testicular shutdown, shrinkage, infertility, and dependence of traditional alternatives." Badges: *Starter · Fertility-Friendly · Oral · Daily.* "Add Tadalafil to your protocol for free."

### Semaglutide  *(GLP-1, flagship weight-loss)*
**Parent:** Weight Loss / GLP-1 · **url:** `/weight-loss/semaglutide-standard` · **price:** from $149.99/mo · **price_visibility:** `[partial]` (floor shown; dose-set at intake)

> H1: **"Semaglutide"** · tagline above H1: "Quiet the food noise. Lose the weight." · molecule framing: "GLP-1" / "Body Weight Support (Semaglutide)"

Exact price string (verbatim):
- "Personalized doses — from **$149.99**/mo ~~$229.99~~ — Save $80 ~~$229.99/mo~~"
- Restated: "**Weight Loss Protocol Semaglutide** starting at **$149.99**/mo" · "As low as $149.99 per month"
- "Split your payment into manageable installments with Klarna."

Includes / audience / footnotes: "Your dose, your plan. A licensed prescriber sets it from your weight, history, and goals. Not a flat protocol." "Compounded semaglutide is available by prescription only after medical evaluation, is not FDA-approved, and is not appropriate for everyone." Form: once-weekly self-injection; "Maximus uses only the **base form** of Semaglutide… Some pharmacies use salt forms… not equivalent." "Do you charge extra for higher doses? We offer flat-rate monthly plans that include access to all dose tiers." HSA/FSA eligible; "available nationwide in all states but AL, MS, LA."

### Tirzepatide  *(GLP-1 + GIP, premium weight-loss)*
**Parent:** Weight Loss / GLP-1 · **url:** `/weight-loss/tirzepatide-standard` · **price:** from $249.99/mo · **price_visibility:** `[partial]` (floor shown; dose-set at intake)

> H1: **"Tirzepatide"** · tagline above H1: "Lose weight without fighting your willpower." · molecule framing: "GLP-1 + GIP" / "Dual-action technology"

Exact price string (verbatim):
- "Personalized doses — from **$249.99**/mo ~~$329.99~~ — Save $80 ~~$329.99/mo~~"
- Restated: "**Weight Loss Protocol Tirzepatide** starting at **$249.99**/mo" · "As low as $249.99 per month"
- (On `/weight-loss` category card: "Starting at **$249.99**/mo ~~$329.99~~ Save $80")

Includes / footnotes: "It's the only medication that activates both GLP-1 and GIP receptors." "Compounded tirzepatide is available by prescription only after medical evaluation, is not FDA-approved." "Your dose, your plan. A licensed prescriber sets it." Form: once-weekly self-injection; base-form only (same salt-form caveat as semaglutide). Same flat-rate-includes-all-doses and AL/MS/LA exclusion.

### Injectable Testosterone  *(traditional TRT anchor)*
**Parent:** Testosterone · **url:** `/testosterone/Injectable-TRT` · **price:** $99.99/mo (12-mo tier) · **price_visibility:** `[published]`

> H1: **"Injectable Testosterone"** · BEST FOR: "Men who want tried-and-true TRT with strong, consistent results through weekly at-home injections."

Exact price ladder (verbatim):
- **1 Month — $199.99/mo**
- **3-Month Plan — MOST POPULAR — $149.99/mo**
- **12-Month Plan — BEST VALUE — $99.99/mo**
- Spine anchor: "**Injectable Testosterone** starting at **$99.99**/mo"; footnote "\*Pricing varies by dosage and plan length. May vary slightly by state."

Form / claims: "1-2 shots weekly"; "pharmaceutical-grade MCT oil" (vs seed oils); "subcutaneous injections using ultra-fine insulin needles." Badges: *Traditional TRT · Injectable · Weekly.*

---

## Roster — complete at the indexed (buyable protocol) level

Molecule/form is in **What**. Prices verbatim; `mo` ladders show 1-mo / 3-mo / 12-mo where the page published them.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (one line) |
|---|---|---|---|---|---|---|
| Testosterone | family | — | `/testosterone` | — | — | Category landing for all testosterone protocols; not itself buyable. |
| Enclomiphene | buyable | Testosterone | `/testosterone/enclomiphene-only` | $199.99 / $149.99 / **$99.99**/mo (1/3/12-mo); "starting at **$99.99**/mo" | `[published]` | Oral enclomiphene; daily pill, stimulates natural T, fertility-friendly. Molecule: enclomiphene. |
| Oral Testosterone | buyable | Testosterone | `/testosterone/oral-testosterone` | "Starting at $149.99/mo" | `[partial]` | Daily oral testosterone capsules (typically 3–4/day); floor only, no per-page ladder captured. Molecule: oral testosterone (native/undecanoate not stated). |
| Testosterone Cream | buyable | Testosterone | `/testosterone/Testosterone-Cream` | $209.99 / $159.99 / **$109.99**/mo (1/3/12-mo); "starting at **$109.99**/mo" | `[published]` | Daily topical testosterone; "peak ~1,321 ng/dL," liver-safe absorption. Molecule: testosterone (topical cream). |
| Injectable Testosterone | buyable | Testosterone | `/testosterone/Injectable-TRT` | $199.99 / $149.99 / **$99.99**/mo (1/3/12-mo); "starting at **$99.99**/mo" | `[published]` | Weekly at-home subcutaneous injection in MCT oil. Molecule: injectable testosterone (ester not stated; page url cites cypionate). |
| Enclomiphene + Testosterone Cream | buyable | Testosterone | `/testosterone/Testosterone-Cream-and-Enclomiphene` | $289.99 / $239.99 / **$189.99**/mo (1/3/12-mo); "starting at **$189.99**/mo" | `[published]` | Patented combo: topical T + enclomiphene; flagship, "you can only get at Maximus." Free Tadalafil add-on. Molecules: testosterone (cream) + enclomiphene. |
| Enclomiphene + Oral Testosterone | buyable | Testosterone | `/testosterone/oral-testosterone-and-enclomiphene` | "Starting at $199.99/mo" | `[partial]` | All-oral fertility-friendly combo; floor only (from `/testosterone` card). Free Tadalafil add-on. Molecules: oral testosterone + enclomiphene. |
| Injectable Testosterone + hCG | buyable | Testosterone | `/testosterone/Injectable-TRT-and-hCG` | "Starting at $299.99/mo" | `[partial]` | Weekly injectable TRT + hCG for testicular function/fertility; floor only (from `/testosterone` card). Molecules: injectable testosterone + hCG. |
| At-Home Testosterone Test | buyable | Testosterone | `/lab-tests` | **$99.99** (one-time) | `[published]` | One-time at-home hormone test (10 markers); no commitment, feeds protocol intake. |
| Weight Loss / GLP-1 | family | — | `/weight-loss` | — | — | Category landing for GLP-1 protocols (men + women); not itself buyable. |
| Semaglutide | buyable | Weight Loss / GLP-1 | `/weight-loss/semaglutide-standard` | "from **$149.99**/mo" (~~$229.99~~, Save $80) | `[partial]` | Compounded semaglutide, once-weekly injection, personalized dose; base form only. Molecule: semaglutide (GLP-1). |
| Tirzepatide | buyable | Weight Loss / GLP-1 | `/weight-loss/tirzepatide-standard` | "from **$249.99**/mo" (~~$329.99~~, Save $80) | `[partial]` | Compounded tirzepatide, once-weekly injection, personalized dose; base form only. Molecule: tirzepatide (GLP-1 + GIP). |

**Buyable count (TRT + GLP-1 scope): 10** — 7 testosterone protocols (Enclomiphene, Oral T, Testosterone Cream, Injectable, Enclo + Cream, Enclo + Oral, Injectable + hCG) + 1 at-home test + 2 GLP-1 (Semaglutide, Tirzepatide). The two `family` rows (`/testosterone`, `/weight-loss`) are non-buyable groupings, not counted.

### Notes on counting / equivalence
- A free **Tadalafil** add-on rides on the enclomiphene-based protocols ("Add Tadalafil to your protocol for free") — it is not a standalone buyable line in this scope and gets no row; Tadalafil's own ED line lives at `/vardenafil-tadalafil-sildenafil-bloodflow` (out of scope here).
- No cross-brand equivalence asserted. "Semaglutide / Tirzepatide" naming and "base form" claims are Maximus's own words, keyed to these slugs only.
