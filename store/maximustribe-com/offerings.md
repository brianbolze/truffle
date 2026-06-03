---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: maximustribe.com     # company key; each offering's slug (its relative url) is its key *within* Maximus
captured_at: 2026-06-03      # own freshness; captures/2026-06-03/ holds the source pages
---

## Portfolio overview

Maximus (maximustribe.com) is a direct-pay "performance medicine" telehealth brand — **Multi-product**, a real
multi-line catalog (testosterone, weight loss, peptides, labs, oxytocin, hair, blood flow), all subscription, no
insurance. This doc enumerates the two lines with a per-SKU capture this run — **testosterone** and **weight loss
(GLP-1)** — at the buyable-protocol grain; the other lines are real but **not enumerated** here (no per-SKU capture).
Both captured lines sell the same way: a **category** page (non-buyable) groups a set of **protocols** (the buyable
monthly subscription), and every protocol's final dose + all-in routes through a free quiz → physician review →
optional at-home lab on `app.maximustribe.com`.

**The shape finding — testosterone splits into the site's own two sub-families, and pricing shows in two depths:**
- **Testosterone** is the flagship/origin line and by far the deepest. The category page itself draws two buckets:
  **Fertility-Friendly Testosterone** (enclomiphene-based — "boosts your own production," preserves LH/FSH) and
  **Traditional TRT** (exogenous testosterone — cream / oral / injectable). Combos layer the two, or add hCG.
- **Four protocols publish a full 1-/3-/12-month ladder on their own PDP** (price drops as the plan lengthens;
  "Starting at" = the 12-month tier) → the real per-plan number is visible → **`published`**. The remaining
  testosterone protocols expose only a category-card **"Starting at $X/mo" floor** (no per-page ladder captured),
  and both GLP-1s show a **"from $X/mo"** floor with the real number dose-set at intake → **`partial`**.
- **Not "TRT" monolithically:** the line's *fertility-friendly* half (enclomiphene) explicitly "stimulates your
  body's natural testosterone production" with "no testicular shutdown" — Maximus frames it *against* TRT, not as
  TRT. A reader must not collapse "Maximus testosterone" into "exogenous T."

**Prominence (calibrated).** Testosterone is the lead line **[HIGH]** — the profile records it as the flagship/origin
line and the rest of the catalog is badged **NEW**; it carries the deepest lineup (7 protocols + an at-home test) and
its own dedicated category page. Within testosterone, the company's *own* **PATENTED** hero — "The revolutionary
testosterone plan _you can only get at Maximus_," **Starting at $189.99/mo**, pointing at the
enclomiphene + tadalafil + testosterone-cream combo — is the line's labelled flagship **[HIGH]** (it owns the
category-page hero slot; note it is a *different* SKU from the captured `Testosterone-Cream-and-Enclomiphene` PDP that
shares the $189.99 floor). The per-card badges ("Best Outcomes," "Fastest Results," "Starter," "MOST POPULAR,"
"BEST VALUE") are the company's own labels **[MED]**, but they sit on *every* card and the captured card order is
duplicated/rotating, so card *ranking* is **[LOW]**. Weight loss is a co-equal, lighter line **[MED]** — two SKUs,
its own category page, sold to men *and* women (the rest of the catalog is men-first); within it Tirzepatide is
presented first and pricier ($249.99 vs $149.99) **[MED]**. The homepage's own H1 rotates (captured as
"Maximum growth hormones"), so no single homepage creative is used for ranking **[LOW]**.

## Roster

Complete at the indexed (buyable-protocol) level for the two captured lines. Within-company key = **Slug** (the
relative URL). Price quoted verbatim with its on-page markers; molecule/form is **page-attested only** (never
inferred from the brand — see the molecule note under Verbatim anchors). An offering here is never asserted equal to
a same-molecule offering at another brand.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Testosterone | family | — | `/testosterone` | — | — | Category landing for all testosterone protocols; splits Fertility-Friendly (enclomiphene) vs Traditional TRT. Not itself buyable. |
| Enclomiphene | buyable | Testosterone | `/testosterone/enclomiphene-only` | `1 Month $199.99/mo` · `3-Month Plan … $149.99/mo` · `12-Month Plan … $99.99/mo`; `Enclomiphene starting at $99.99/mo` | published | enclomiphene · oral pill, once daily · quiz + lab gated. "Starter / Fertility-Friendly"; "stimulates your body's natural testosterone production." Full PDP ladder. |
| Testosterone Cream | buyable | Testosterone | `/testosterone/Testosterone-Cream` | `1 Month $209.99/mo` · `3-Month Plan … $159.99/mo` · `12-Month Plan … $109.99/mo`; `Testosterone Cream starting at $109.99/mo` | published | testosterone (topical; no ester named) · cream, once daily · quiz + lab gated. "Traditional TRT"; "peak ~1,321 ng/dL," lymphatic/liver-safe absorption. Full PDP ladder. |
| Injectable Testosterone | buyable | Testosterone | `/testosterone/Injectable-TRT` | `1 Month $199.99/mo` · `3-Month Plan … $149.99/mo` · `12-Month Plan … $99.99/mo`; `Injectable Testosterone starting at $99.99/mo` | published | testosterone (injectable; ester not stated in body — see anchor) · weekly subcutaneous injection (1–2/wk), MCT oil · quiz + lab gated. Full PDP ladder. |
| Enclomiphene + Testosterone Cream | buyable | Testosterone | `/testosterone/Testosterone-Cream-and-Enclomiphene` | `1 Month $289.99/mo` · `3-Month Plan … $239.99/mo` · `12-Month Plan … $189.99/mo`; `Enclomiphene + Testosterone Cream starting at $189.99/mo` | published | testosterone (cream) + enclomiphene · daily cream + daily pill · quiz + lab gated. Patented combo; "Add Tadalafil to your protocol for free." Full PDP ladder. |
| Oral Testosterone | buyable | Testosterone | `/testosterone/oral-testosterone` | `Starting at $149.99/mo` | partial | oral testosterone (no ester named) · daily pills (typically 3–4) · quiz + lab gated. Floor only — category card, no PDP captured. |
| Enclomiphene + Oral Testosterone | buyable | Testosterone | `/testosterone/oral-testosterone-and-enclomiphene` | `Starting at $199.99/mo` | partial | oral testosterone + enclomiphene · all-oral, daily · quiz + lab gated. "Patented Formulation / Fertility-Friendly"; "Add Tadalafil … for free." Floor only — category card, no PDP. |
| Injectable Testosterone + hCG | buyable | Testosterone | `/testosterone/Injectable-TRT-and-hCG` | `Starting at $299.99/mo` | partial | injectable testosterone + hCG · weekly injection · quiz + lab gated. "Combines injectable TRT + hCG for testicular function." Floor only — category card, no PDP. |
| Enclomiphene + Tadalafil + Testosterone Cream | buyable | Testosterone | `/testosterone/enclomiphene-tadalafil-testosterone-cream` | `Starting at $189.99/mo` | partial | enclomiphene + tadalafil + testosterone cream (from the slug + hero name) · oral + topical, daily · quiz + lab gated. The category-page **PATENTED hero**; floor only, no card/PDP captured. [anchor a] |
| At-Home Testosterone Test | buyable | Testosterone | `/lab-tests` | `$99.99` (one-time) | published | not a drug — at-home hormone test (10 markers) · one-time kit, free shipping · "No commitment to buy treatment"; feeds protocol intake. |
| Weight Loss | family | — | `/weight-loss` | — | — | Category landing for the GLP-1 protocols (men + women). Not itself buyable. |
| Semaglutide | buyable | Weight Loss | `/weight-loss/semaglutide-standard` | `from $149.99/mo` (~~$229.99~~, `Save $80`); `Weight Loss Protocol Semaglutide starting at $149.99/mo` | partial | semaglutide (GLP-1 receptor agonist) · compounded, once-weekly self-injection, base form · dose set at intake. "available nationwide in all states but AL, MS, LA." |
| Tirzepatide | buyable | Weight Loss | `/weight-loss/tirzepatide-standard` | `from $249.99/mo` (~~$329.99~~, `Save $80`); `Weight Loss Protocol Tirzepatide starting at $249.99/mo` | partial | tirzepatide (GLP-1 + GIP receptor agonist) · compounded, once-weekly self-injection, base form · dose set at intake. Same AL/MS/LA exclusion. |

**Buyable count (in scope): 11** — 7 testosterone protocols (Enclomiphene, Testosterone Cream, Injectable, Enclo +
Cream, Oral, Enclo + Oral, Injectable + hCG) + the patented Enclo + Tadalafil + Cream hero + 1 at-home test + 2 GLP-1
(Semaglutide, Tirzepatide). The two `family` rows (`/testosterone`, `/weight-loss`) are non-buyable groupings, not
counted.

### Verbatim anchors

The footnotes / markers the Price column points at — they decide `published` (a per-plan ladder is shown) vs `partial`
(only a floor is shown, real number set later), plus the molecule-sourcing audit trail. Quoted exactly from the
captured pages.

- **The four `published` ladders (on each protocol's own PDP):** each shows three priced tiers verbatim —
  *"1 Month … 3-Month Plan **MOST POPULAR** … 12-Month Plan **BEST VALUE** …"* — with a spine restatement *"… starting
  at $X/mo"* and the footnote *"\*Pricing varies by dosage and plan length. May vary slightly by state."*
  (`testosterone-enclomiphene-only.md`, `testosterone-cream.md`, `testosterone-injectable-trt.md`,
  `testosterone-cream-and-enclomiphene.md`). The number for each plan length is visible → `published`.
- **The `partial` testosterone floors (category cards only):** Oral Testosterone *"Starting at$149.99/mo,"* Enclo +
  Oral *"Starting at$199.99/mo,"* Injectable + hCG *"Starting at$299.99/mo"* (`testosterone-category.md`). Only the
  floor shows; no per-page ladder was captured → `partial`.
- **The GLP-1 floors:** *"Personalized doses — from **$149.99**/mo ~~$229.99~~ — Save $80"* (Semaglutide) /
  *"…from **$249.99**/mo ~~$329.99~~…"* (Tirzepatide); FAQ *"We offer flat-rate monthly plans that include access to
  all dose tiers"* and *"Your dose, your plan. A licensed prescriber sets it."* The advertised number is a floor; the
  dose-set price is gated → `partial`.
- **Molecule sourcing (the page-attested-only rule, audited):**
  - **Enclomiphene → enclomiphene**, attested in PDP body: *"Strategically blocks estrogen receptors to increase
    testosterone… Up to 2x increase to testosterone without the testicular shutdown…"* (and the combo PDP names it
    explicitly).
  - **Semaglutide → semaglutide / GLP-1**, attested: *"Semaglutide, an FDA approved GLP-1 receptor agonist…"*; **base
    form**: *"Maximus uses only the base form of Semaglutide and Tirzepatide… Some pharmacies use salt forms… not
    equivalent."* **Tirzepatide → tirzepatide / GLP-1 + GIP**, attested: *"It's the only medication that activates
    both GLP-1 and GIP receptors."*
  - **hCG → hCG**, attested on the category card: *"Combines injectable TRT + hCG for testicular function."*
  - **Testosterone Cream / Oral / Injectable → "testosterone," no specific ester stated.** The PDP bodies say only
    "testosterone cream," "oral testosterone," "injectable testosterone." **Injectable: "cypionate" appears *only* in
    one image's alt-text** (`![buy testosterone cypionate online]`) — **not in any body copy** — so the ester is
    recorded **not stated**, not asserted "cypionate." (This corrects the seed draft, which inferred the ester from
    the image/URL.)
- **[anchor a] the patented hero is its own SKU.** The `testosterone-category.md` hero — *"PATENTED … The
  revolutionary testosterone plan you can only get at Maximus. … Starting at $189.99/mo"* — links **"Learn more"** to
  `/testosterone/enclomiphene-tadalafil-testosterone-cream`. That slug has **no product card and no captured PDP**;
  the same $189.99 floor also belongs to the *captured* `Testosterone-Cream-and-Enclomiphene` PDP (which has its own
  full ladder). Kept as two distinct rows, keyed by their own slugs; no claim that they are the same protocol or that
  $189.99 maps to the same plan length on both.

## Deep blocks

**None earned — the roster carries this company.** The four full price ladders and both GLP-1 floors live in the
roster's Price column; reproducing them as blocks would only restate roster cells (the explicit anti-pattern). The two
findings a roster cell can't fully hold — the *patented-hero-is-a-separate-uncaptured-SKU* disambiguation and the
*injectable "cypionate" is alt-text-only, ester not stated* call — are both resolved inline above under Verbatim
anchors (anchor a + the molecule-sourcing audit), where the verbatim string that decides them already sits. No gated
FAQ-only price and no "this isn't actually X" reversal needs a spine-plus-gold block here.

## Provenance

- **Pages read (8, all `captures/2026-06-03/`):** `testosterone-category.md` (/testosterone),
  `testosterone-enclomiphene-only.md`, `testosterone-cream.md`, `testosterone-injectable-trt.md`,
  `testosterone-cream-and-enclomiphene.md`, `weight-loss-category.md` (/weight-loss),
  `weight-loss-semaglutide-standard.md`, `weight-loss-tirzepatide-standard.md`. Also present in the capture set but
  used only for context, not enumerated: `homepage.md`, `labs-comprehensive.md`,
  `growth-hormone-peptides-category.md`. Context: `store/maximustribe-com/profile.md`.
- **Scope:** testosterone + weight-loss (GLP-1) only — the two lines with a per-SKU capture this run. Maximus's other
  lines (Growth Hormone Peptides, Oxytocin Calming Cream, Comprehensive Lab Testing, Hair Growth, Blood Flow,
  Building Blocks multivitamin) are real and noted in the overview but **not enumerated** — no per-protocol capture.
- **Gated / unreachable:** every protocol's actual dose-set, all-in monthly price (set during intake + physician
  review on `app.maximustribe.com`, and "Pricing varies by dosage and plan length"); the full 1-/3-/12-month ladders
  for the four `partial` testosterone protocols (Oral, Enclo + Oral, Injectable + hCG, and the patented
  Enclo + Tadalafil + Cream hero — captured as category-card / hero floors only, **no PDP**); the specific
  testosterone **ester** for the cream / oral / injectable protocols (not in body copy). The free **Tadalafil**
  add-on that rides the enclomiphene-based protocols ("Add Tadalafil to your protocol for free") is not a standalone
  buyable line in this scope and gets no row; Tadalafil's own ED line lives at
  `/vardenafil-tadalafil-sildenafil-bloodflow` (out of scope).
- **Point-in-time snapshot, not fixed:** Maximus runs a recurring **"50% OFF YOUR FIRST MONTH"** banner for new
  12-month customers and GLP-1 strike-through "Save $80" promos — prices here are the 2026-06-03 advertised values,
  not a contract. This module's own `captured_at` + a short freshness TTL are the guard; re-capture before trusting a
  price as current.
