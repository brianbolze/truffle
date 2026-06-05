---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: gogeviti.com          # company key; each offering's slug (its relative url) is its key *within* Geviti
captured_at: 2026-06-03       # own freshness; captures/2026-06-03/ holds the source pages
---

## Portfolio overview

Geviti (gogeviti.com; legal entity Geviti Health Inc.) is a **Flagship + companions** telehealth-longevity
platform whose *product is the membership*. One recurring tier — **Plus** — unlocks everything; every test,
prescription, and supplement is a **companion** bought *through* the membership ("a membership is required to
access Geviti's services," FAQ). So this is not a card-grid catalog like Hims/Hone — the roster is **3
membership tiers + a thin à-la-carte diagnostics shelf + an entirely price-opaque Rx clinic + a custom
supplement line + the Blueprint deliverable**. The whole thing is **Next.js marketing + an app wall**: ordering,
per-Rx pricing, and the à-la-carte catalog live in `app.gogeviti.com` behind intake; the marketing host only
exposes the ~7 feature pages enumerated here.

**Shape finding — three visibility regimes, by layer:**
- **Memberships are `published`** (flat, self-contained): Free `$0/mo`; Plus shown two ways — `$150/mo`
  (billed $899 every 6 months) on /pricing and `$127/mo` (billed annually $1,529.99) on the homepage; Infinite
  is `on-request` ("Inquire about pricing," "Coming Soon").
- **Diagnostics are `published`** where a number shows — Genomics and Microbiome carry real member/non-member
  add-on prices and Genomics is orderable *without* a membership. The flagship **Longeviti Panel is `partial`**:
  it's bundled into Plus (membership shown) but its standalone à-la-carte price is app-walled this capture.
- **The Rx clinic is `on-request`, by design** — /clinic shows **zero** prices; HRT, peptides, GLP-1s, and
  thyroid are "compounded and shipped," priced only in-app behind Plus + bloodwork + intake.

**Visibility rule (stated, applied consistently below).** `published` = the number shown is the full,
self-contained price you actually pay. `partial` = the real all-in isn't fully shown — a mandatory separate
cost (the Plus membership), a price that's only a self-valuation, or a standalone number that's hidden.
`on-request` = no price shown (inquire / app-walled / quote). `—` = a non-SKU `family` row. The mandatory
mechanics that decide a call (membership-on-top, app-wall, cross-page price divergence) are captured verbatim
in the Price cell or a `### Verbatim anchor`, so a cross-brand comparison stays recoverable.

**Two new slug columns** key to the Notion vocab: **Form** = the page-attested **Delivery Mechanism** slug for
*medication* SKUs; `n/a` for non-drug SKUs (memberships, diagnostics, the Blueprint — a drug-route doesn't
apply); `not stated` where a med's route isn't bound on the page. **Category** = the SKU's best-fit **Product
Category**, slugified; `[?]` flags a SKU with no clean single fit (Geviti's gender-neutral "HRT" line spans
three Notion categories; memberships/Blueprint are platform layers, not therapeutic verticals).

**Prominence (calibrated).**
- **Plus is the singular flagship [HIGH]** — the homepage carries **only the Plus card**, under the company's
  own **"Most Popular"** badge; Free and Infinite appear only on /pricing.
- **Membership-as-the-product is the whole model [HIGH]** — every companion line repeats "included with your
  membership" / "Plus membership unlocks…"; the FAQ states the membership is required.
- **Rx is deliberately price-opaque [HIGH]** — /clinic is the one feature page with no number anywhere; the
  catalog is gated behind intake + labs and lives in the app.
- **Genetics is getting the marketing push [MED]** — Longeviti Genomics is the *only* SKU with its own rich
  PDP (/genetics) and a limited-time pre-order promo ("Save $250… through July 1st").
- **Nav/section order [MED]:** the Features menu runs Custom Supplements → Routine Bloodwork → Longevity Clinic
  → Testing Shop → Longevity Blueprint, identical across pages. Card order within /pricing and the rotating
  Father's-Day promo bar left **[LOW]** — not used for ranking.

## Roster

Complete **at the level Geviti indexes on its public site** — membership tiers, the three named test
categories, and the therapy *categories* of the Rx clinic — never the per-drug leaves, which the site does not
expose (they're app-walled; see Provenance). Within-company key = **Slug** (relative URL, quoted exactly).
Price quoted verbatim with its on-page markers; **Form**/**Category** keyed to the Notion vocab; molecule in
**What** is page-attested only, never inferred from the brand. An offering here is never asserted equal to a
same-molecule offering at another brand.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | Form | Category | What (molecule · access) |
|---|---|---|---|---|---|---|---|---|
| **Membership** | family | — | `/pricing` | — | — | — | — | The access layer — a required subscription that gates every test, Rx, and supplement. "A membership is required to access Geviti's services." |
| Free | buyable | Membership | `/pricing` | `$0/mo` | published | n/a | other [?] | not a drug — free tier: app + Personalized Health Blueprint + custom-supplement-blend access + specialty-testing marketplace; labs/supplements pay-per-use (app-priced). "No card needed." |
| Plus | buyable | Membership | `/pricing` | `$150/mo` ("Billed $899 every 6 months", /pricing) · `$127/mo` ("Or From $4/day", "Billed annually at $1,529.99", homepage) | published | n/a | other [?] | not a drug — **the flagship; "Most Popular."** 100+ biomarker panel 2×/yr, at-home draws, provider & coaching visits, **full Rx catalog access**, blueprint, member pricing on supplements/tests. Two cadences: semi-annual $150/mo vs annual $127/mo ("Annually -15%"). [anchor: plus-price] |
| Infinite | buyable | Membership | `/pricing` | `Inquire about pricing` ("Coming Soon" / "Join Waitlist") | on-request | n/a | other [?] | not a drug — concierge top tier (unreleased): dedicated physician, **all therapies/supplements/Rx included**, quarterly testing, "Genomics, gut health & cancer screening," 48hr priority concierge. [anchor: infinite] |
| **Testing Shop (Diagnostics)** | family | — | `/testing` | — | — | — | — | À-la-carte at-home tests, ordered in-app ("Three Core Test Categories"). Results feed the Blueprint. |
| Longeviti Panel — Bloodwork | buyable | Testing Shop (Diagnostics) | `/bloodwork` | Included w/ Plus (annual) & Infinite (quarterly); self-valued `over $2,200` if bought independently; Free = "Add-on" (app-priced) | partial | n/a | labs-diagnostics | not a drug — 100+ biomarker blood panel (≈104: hormones incl. total/free/bioavailable testosterone, estradiol, thyroid; metabolic, cardiovascular, inflammation, nutrients, kidney/liver) + PhenoAge; at-home draw or Quest walk-in. Standalone à-la-carte price app-walled this capture. [anchor: panel] |
| Longeviti Genomics — Genetics | buyable | Testing Shop (Diagnostics) | `/genetics` | /testing: `Add-On (member pricing): $300` · `Add-On (free pricing): $500`. /genetics: `$349 for Geviti members` · `$599 non-member` · `Save $250` (pre-order "through July 1st") | published | n/a | labs-diagnostics | not a drug — one-time DNA **cheek swab** (~80 gene variants / ~160 insights / 23 categories; APOE, MTHFR, etc.); "No subscription required to order the genetics kit." **Two pages quote different prices.** [anchor: genomics-price] |
| Longeviti Microbiome — Gut Health | buyable | Testing Shop (Diagnostics) | `/testing` | `Add-On (member pricing): $500` · `Add-On (free pricing): $600` | published | n/a | labs-diagnostics | not a drug — **Mosaic GI360** gut-microbiome test (diversity, pathogen/parasite screen, SCFA); "Quarterly Add-On." No dedicated PDP — lives on /testing. |
| **Longevity Clinic (Rx)** | family | — | `/clinic` | — | — | — | — | Clinician-prescribed, **compounded-and-shipped** Rx; "Plus membership unlocks clinic access." **No prices anywhere on-site** — member pricing set in-app behind intake + bloodwork. Indexed at the therapy-category level (no per-drug PDPs). [anchor: rx-gating] |
| Peptide therapy | buyable | Longevity Clinic (Rx) | `/clinic` | none on site — member pricing in-app | on-request | not stated | peptides | **BPC-157, Sermorelin, GHK-Cu, GLP-1s** "and more" (page-attested, /clinic Peptide Protocols pillar) · compounded, shipped, "monitored by twice annual or quarterly bloodwork." Per-peptide route not page-bound (hero shows injection vial + troche). [anchor: rx-molecule] |
| GLP-1 / weight loss | buyable | Longevity Clinic (Rx) | `/clinic` | none on site — member pricing in-app | on-request | not stated | glp-1-medical-weight-loss | **GLP-1s** (category named on /clinic + the /genetics "Rx catalog (HRT, peptides, GLP-1s, thyroid)" table + FAQ). Specific molecule **not stated** this capture — semaglutide/tirzepatide appear only in blog, not the catalog. [anchor: rx-molecule] |
| Hormone therapy (HRT) | buyable | Longevity Clinic (Rx) | `/clinic` | none on site — member pricing in-app | on-request | not stated | trt [?] | **HRT** (gender-neutral; named in the /genetics Rx-catalog table). **Enclomiphene Citrate** page-attested in the /clinic hero product image; testosterone/estrogen/progesterone per profile, not named in this capture's /clinic text. One site line spanning TRT + women's HRT + fertility-preserving — no clean single category. [anchor: rx-molecule] |
| Thyroid | buyable | Longevity Clinic (Rx) | `/clinic` | none on site — member pricing in-app | on-request | not stated | longevity-rx-non-nad [?] | thyroid Rx — "thyroid" named only in the /genetics Rx-catalog table ("HRT, peptides, GLP-1s, thyroid"); no molecule/form stated. No clean Notion category (thyroid-hormone Rx). |
| Aesthetic / skin Rx | buyable | Longevity Clinic (Rx) | `/clinic` | none on site — member pricing in-app | on-request | topical-gel | aesthetics-dermatology | "**Skin Rejuvenation Cream**" (page-attested, /clinic hero product image; blog also: "Radiance Cream" for acne) · topical cream · molecule not stated. |
| Hair-loss Rx | buyable | Longevity Clinic (Rx) | `/clinic` | none on site — member pricing in-app | on-request | not stated | hair-loss | "**Follicle Fix**" dropper (page-attested, /clinic hero product image; blog also: "Cedar hair growth capsules") · form not bound (a dropper ⇒ topical, capsules ⇒ oral; both appear) · molecule not stated. |
| Custom Supplements (Longeviti Blend) | buyable | — | `/supplements` | none on site — member/wholesale pricing ("Wholesale pricing on supplements (~`$80/mo` saved)", /genetics) | on-request | pill | supplements | not Rx — blood-based custom supplement blend in **AM/PM capsule packs**, **Xymogen** pharmaceutical-grade, re-optimized every 6 months; no published unit price. |
| Longevity Blueprint | buyable | — | `/blueprint` | Included (Free + Plus) — no separate price | published | n/a | other [?] | not a drug — the personalized optimization **plan** that fuses blood + genetics + gut + wearables into a protocol; included on Free and Plus. |

**Buyable count (in scope): 13** — 3 membership tiers + 3 diagnostics + 6 Rx therapy-category lines + Custom
Supplements + Blueprint. The 3 `family` rows (Membership, Testing Shop, Longevity Clinic) are non-buyable
groupings, not counted. **Not enumerated** (app-walled, not on the public site): the per-molecule Rx SKUs and
every Rx price (see Provenance).

### Verbatim anchors

The footnotes the Price/Visibility columns point at — they decide `published`/`partial`/`on-request` and carry
the molecule-sourcing audit. Quoted exactly from the cited 2026-06-03 captures.

- **[anchor: plus-price] Plus is shown two ways (cadence, not contradiction).** /pricing (default tab "Every 6
  Months", toggle "Annually -15%"): *"Plus · Most Popular · **$150/mo** · Billed **$899** every 6 months."*
  Homepage card: *"Plus · Most Popular · **$127/mo** · Or From **$4/day** … Includes $10,000+ in testing & care
  · Billed annually at **$1,529.99**."* → the semi-annual cadence is $899 twice a year; the annual cadence is
  billed $1,529.99/yr (the advertised −15%). Both are full, self-contained membership prices → `published`. The
  /pricing annual *number* itself sits behind the toggle and wasn't in the captured markdown (only the
  homepage's $1,529.99 is).
- **[anchor: infinite] Infinite = a coming-soon concierge tier, not a price.** /pricing: *"Infinite · **Inquire
  about pricing** · Your dedicated physician, every therapy, and full concierge service — one flat rate."* with
  *"Coming Soon · Join Waitlist."* Included list (verbatim): *"Quarterly testing and advanced panels · Dedicated
  physician. Same doctor always · All therapies, supplements, and Rx included · Genomics, gut health & cancer
  screening · 48hr priority fulfillment & concierge."* → `on-request`. (The profile flagged this tier as
  possibly stale; it is now an explicit, named, unreleased tier.)
- **[anchor: panel] Longeviti Panel — bundled, with a self-valuation, standalone price hidden.** /testing badge:
  *"Most Ordered · Included · Plus & Infinite … Tested annually with Plus, quarterly with Infinite."* FAQ:
  *"It's valued at **over $2,200** if ordered independently — included free twice yearly with your membership."*
  The $2,200 is a *self-valuation*, not a transaction price, and the Free-tier à-la-carte number is app-walled
  this run → `partial`. (The old profile's "$399 / from $349" pay-per-test figures did **not** reappear on any
  2026-06-03 page — treated as stale CRO-variant pricing and omitted.)
- **[anchor: genomics-price] The genetics price diverges across two pages — captured both.** /testing card:
  *"One-Time Add-On · Add-On (member pricing): **$300** · Add-On (free pricing): **$500**."* /genetics PDP hero:
  *"**$349** for Geviti members · **$599** non-member · **Save $250** limited time savings"* + *"Pre-order
  pricing available through July 1st."* Read as: /testing = steady-state add-on price; /genetics = a limited-time
  pre-order promo on the same SKU. Both `published`; not reconciled (a snapshot of a live promo). *(Capture note:
  Firecrawl's markdown glued the `$300` badge to the next label as "`$300Add-On`"; repaired to "`$300 Add-On`"
  in `captures/2026-06-03/testing.md` to match the rawHtml's discrete `$300</span>` element — the price is
  rawHtml-attested, not invented.)*
- **[anchor: rx-gating] The Rx clinic shows no price — the gate is the finding.** /clinic: *"Plus membership
  unlocks clinic access"*; *"When clinically indicated, your practitioner can prescribe medications through
  Geviti's licensed compounding network"*; *"Legally compounded by licensed pharmacies · Shipped directly to
  your door · Managed in the app."* FAQ: *"Your Geviti care team includes licensed providers who can prescribe
  as part of your protocol — peptides, HRT, GLP-1s, and more."* No figure anywhere → every Rx line `on-request`.
- **[anchor: rx-molecule] Molecule sourcing (page-attested-only, audited).**
  - **Peptides → "BPC-157, GLP-1s, Sermorelin, GHK-Cu"** attested verbatim on /clinic: *"BPC-157, GLP-1s,
    Sermorelin, GHK-Cu, and more."* (Peptide Protocols pillar.) Recorded as named.
  - **GLP-1s → category only.** "GLP-1s" is named (/clinic, /genetics Rx-catalog table, FAQ) but **no specific
    GLP-1 molecule is stated** on any captured page — *semaglutide*/*tirzepatide* appear only in blog titles,
    which are content, not catalog. Recorded **"not stated"** rather than inferred.
  - **HRT → category; enclomiphene the only attested molecule.** "HRT" is named in the /genetics Rx-catalog
    table; **"Enclomiphene Citrate"** is page-attested as a /clinic hero product-image label. Testosterone /
    estrogen / progesterone are in the warm profile but **not named in this capture's /clinic text** — left as
    the category, not asserted per-SKU.
  - **Aesthetic / hair → product names, not molecules.** "Skin Rejuvenation Cream" and "Follicle Fix" are
    page-attested /clinic hero product-image labels (corroborated by blog posts); their molecules are **not
    stated**, so recorded as product names only.
- **The mandatory membership (the cross-cutting separate cost).** FAQ (verbatim): *"Yes, a membership is
  required to access Geviti's services."* Every companion price above sits *on top of* a Plus membership unless
  the SKU is explicitly orderable without one (only Longeviti Genomics is). Mobile phlebotomy is **"included
  with your membership"** (FAQ) — no standalone draw fee shown this capture (the profile's "$79 add-on" did not
  reappear; omitted as stale).

## Deep blocks

Three blocks earn their place — they span the three visibility regimes and three categories, and each teaches a
PDP shape a roster cell can't carry: the **Plus membership** (the flagship bundle), **Longeviti Genomics** (the
only true rich PDP, and the price-divergence SKU), and the **Longevity Clinic** (the price-opaque Rx layer).
Quoted, not paraphrased.

### Plus membership — the flagship bundle (published, two cadences)

- **Parent:** Membership · **slug:** `/pricing` (+ homepage card) · **price:** `$150/mo` ($899/6mo) | `$127/mo`
  ($1,529.99/yr) · **visibility:** `published` · the homepage's *only* pricing card, badged "Most Popular."

> **Anatomy (/pricing), in order —**
> **Hero:** "One Membership. · **# Your Entire Protocol. Handled.** · Testing, specialist analysis,
> prescriptions, and ongoing care — all in one plan. Pick the tier that fits where you are." Trust row:
> "HSA/FSA Eligible · 47 States · Clinical-grade Labs · $10,000+ in diagnostics, Rx & ongoing care."
> **Toggle:** "Every 6 Months | Annually **-15%**."
> **Price + contents (verbatim):** "**Plus · Most Popular · $150/mo · Billed $899 every 6 months** · Your
> personal health team, full testing panels, and complete Rx access, all included." Included list: "**100+
> biomarker panels (2x/year)** · At-home blood draws included* · Personalized health blueprint · Provider &
> coaching visits · **Full Rx catalog: peptides, HRT, GLP-1s** · Member pricing on supplements & specialty
> testing." Footnotes: "*Rx access subject to state availability · Includes $10,000+ in testing & care ·
> HSA/FSA Eligible."
> **Homepage card (the annual cadence):** "Plus · Most Popular · **$127/mo · Or From $4/day** … Full Rx catalog
> access · Personalized Health Blueprint · Discounts on supplements & specialty tests … **Billed annually at
> $1,529.99** · HSA/FSA Accepted · Secure checkout · HIPAA compliant."
> **FAQ (gating/value, verbatim):** "Does insurance cover this? We accept HSA and FSA payments on all plans…
> most members find Geviti costs less than the separate labs, supplements, and specialist visits they were
> already paying for." · "Is there a long-term commitment? No. You can cancel anytime."

**Why it earns a block:** the flagship *is* a membership, and its price renders **two different ways depending
on the page/toggle** ($150/mo semi-annual vs $127/mo annual) — a roster cell can flag both but can't show that
they're cadences of one SKU. It's the bundle every other row is gated by, so the verbatim "Full Rx catalog:
peptides, HRT, GLP-1s" is the load-bearing link from the published membership to the on-request clinic.

### Longeviti Genomics — the one true PDP (published, price-divergent)

- **Parent:** Testing Shop · **slug:** `/genetics` · **price:** `$349`/`$599` (/genetics) vs `$300`/`$500`
  (/testing) · **visibility:** `published` · **Form:** n/a (DNA cheek swab) · **Category:** labs-diagnostics.

> **Anatomy (/genetics), in order —**
> **Eyebrow + hero:** "Pre-order pricing available through July 1st · Clinical-grade · CLIA-certified labs ·
> 47 states · **# One Swab. A Lifetime Of You, Decoded.** · A one-time cheek swab that adds permanent genetic
> insights on top of your bloodwork."
> **Price block (verbatim):** "**$349 for Geviti members · $599 non-member · Save $250 limited time savings**"
> + CTA "Order my DNA panel" + "HSA/FSA reimbursable · Free shipping both ways · Results in 4-6 weeks · DNA data
> never sold."
> **Stats:** "~160 personalized insights · ~80 gene variants analyzed · 23 health categories."
> **How-it-works (verbatim):** "Order your kit … Swab & mail back … CLIA-certified lab runs your panel …
> Insights unlock in your protocol … Makor AI updates your health blueprint automatically."
> **Contents (gene examples, verbatim):** "MTHFR · C677T · A1298C — Folate methylation… · FADS1 · rs174537 —
> Omega-3 conversion efficiency · APOE 3/3 — the agricultural genotype · GSTM1 null — reduces mercury
> clearance · ACTN3 RR — power-athlete potential · CYP1A2 fast metabolizer."
> **Member-vs-non-member table (verbatim):** non-member gets the test only; "Member + Genetics" adds
> "104-biomarker Longeviti Panel · 2× a year · Dedicated Longevity Specialist · Makor AI protocol integration ·
> Wholesale pricing on supplements (~$80/mo saved) · **Rx catalog (HRT, peptides, GLP-1s, thyroid)**."
> **Gating note (verbatim):** "**No subscription required to order the genetics kit**" · "Pick Longeviti
> Genomics → checkout at $349."

**Why it earns a block:** it's the only SKU on the whole site with a dedicated, full-anatomy PDP — and the
**price contradicts the /testing card** ($349/$599 promo vs $300/$500 add-on), the exact "which number is real"
ambiguity a cross-brand price comparison must see. It's also the one companion **orderable without a
membership**, so it's the cleanest `published` diagnostic. The member-table verbatim "Rx catalog (HRT, peptides,
GLP-1s, thyroid)" is the best single attestation of the clinic's therapy categories.

### Longevity Clinic — the price-opaque Rx layer (on-request, app-walled)

- **Parent:** — (family) · **slug:** `/clinic` · **price:** none anywhere · **visibility:** `on-request` ·
  the structural opposite of the two blocks above: a full feature page with **no price and no per-drug PDP**.

> **Anatomy (/clinic), in order —**
> **Hero:** "Longevity Clinicians · 39 States · HIPAA Compliant · Functionally Trained · **# Real Clinicians.
> Evidence-Based Protocols Built Around You.** · Board-certified longevity practitioners, personalized peptide
> protocols, and a dedicated care team — all coordinated through your Geviti membership." CTAs: "Get My
> Protocol" / "View Plans." Hero product images (alt text): "Troche medication · Injection vial · **Enclomiphene
> Citrate** · **Skin Rejuvenation Cream** · **Follicle Fix dropper**."
> **Four Pillars of Clinical Care (verbatim):** "**01. Peptide Protocols** — Clinician-prescribed peptide
> programs tailored to your biomarkers… **BPC-157, GLP-1s, Sermorelin, GHK-Cu, and more.** · Prescribed by
> licensed clinicians · Compounded and shipped to your door · Monitored by twice annual or quarterly
> bloodwork." · "**02. Longevity Practitioners** … endocrinology, and functional medicine." · "**03. Dedicated
> Care Team** — Medical Director: Oversees protocols and Rx · Longevity Specialist: Monthly check-ins · Member
> Support." · "**04. Prescriptions & Rx** — When clinically indicated, your practitioner can prescribe
> medications through Geviti's licensed compounding network · Legally compounded by licensed pharmacies ·
> Shipped directly to your door · Managed in the app."
> **Funnel (verbatim):** "Choose a Plan — **Plus membership unlocks clinic access** · Schedule Bloodwork —
> Your labs will guide your protocol · Get Protocol — Personalized plan + any Rx · Track & Adjust — Quarterly
> labs + monthly check-ins." Footer disclaimer: "GEVITI IS A HEALTHCARE TECHNOLOGY COMPANY AND NOT A LABORATORY
> OR MEDICAL PROVIDER… THESE… PROVIDERS SET THEIR OWN PRICING."

**Why it earns a block:** it's the proof that Geviti's Rx visibility is `on-request` *by construction* — a
clinician-prescribed protocol, not a shelf. The page names its therapy categories and a handful of peptide
molecules but **binds no price and no per-SKU PDP** to any of them; the catalog and every figure live behind
Plus + intake + labs in the app. That's why the roster's Rx rows stop at the therapy-category level and every
Rx price is app-walled — the page anatomy *is* the explanation a roster cell can only gesture at.

## Provenance

- **Pages read (9 fresh, all `captures/2026-06-03/`):** `homepage`, `pricing`, `clinic`, `testing`,
  `bloodwork`, `genetics`, `supplements`, `blueprint`, `faq` — each a rich `--homepage` scrape (`maxAge:0`,
  `location:US`, `waitFor:3500`, `onlyMainContent:false` + full-page screenshot + rawHtml). Context:
  `store/gogeviti-com/profile.md` (2026-06-02). All 9 verified — sourceURLs match, all body md5s unique (no
  geo/cache contamination).
- **Sources reconciled for completeness:** (1) the **rendered catalog** (the 9 feature pages); (2) a **no-search
  `/v2/map` census** and (3) **`sitemap.xml` (202 `<loc>`)** — both reconcile to the *same* ~7 product/feature
  paths (`/pricing`, `/clinic`, `/testing`, `/bloodwork`, `/supplements`, `/genetics`, `/blueprint`), the rest
  being `/blog` + `/es` locale dupes + influencer landers (`/allie`, `/brettcooper`, …) + legal/seasonal pages.
  Geviti is **Next.js on Vercel with no public product CMS/REST endpoint** (no `wp-json`, no `products.json`);
  the catalog backend is the authenticated app. So the three census methods agree the marketing host exposes no
  hidden SKUs — the roster is complete *at the public-site indexed level*.
- **Completeness verdict — HIGH for the public surface, with a known app wall.** Confident the membership tiers
  (3), the named test categories (3), and the Rx therapy categories are the complete public roster. The
  **per-molecule Rx SKUs and every Rx price are app-walled** (`app.gogeviti.com`, behind intake + the $150/mo
  Plus membership + bloodwork) and were **not reached** — by design, the marketing site never lists them.
- **Couldn't reach / app-walled:** the per-drug Rx catalog + all Rx unit prices; the Longeviti Blend supplement
  unit price; the Free-tier standalone pay-per-test panel price; the Infinite tier price; the `/pricing` annual
  *number* (behind the "Annually -15%" toggle — only the homepage's $1,529.99 was rendered). The clinic's
  HRT/GLP-1/thyroid molecules beyond what /clinic + /genetics name in rendered text (blog titles excluded as
  content, not catalog).
- **Point-in-time snapshot, not fixed.** The profile flags a live **CRO / A-B variant** on /pricing
  (`utm_content=pricing-cro_c`) and run-to-run price flicker — borne out here: Plus reads **$150/mo (/pricing)**
  vs **$127/mo (homepage)**, and Longeviti Genomics reads **$300/$500 (/testing)** vs **$349/$599 (/genetics
  pre-order, ends July 1)**. A site-wide **Father's-Day promo** ("20% OFF Gift Cards · code HISTURN") rides the
  top bar. This module's own `captured_at` + a short TTL are the guard; re-capture before trusting a price.
- **Credits:** 10 (1 map + 9 rich scrapes, 1 each; no enhanced-proxy/PDF add-ons). Screenshots + raw JSON
  persisted to `captures/2026-06-03/.payloads/`.
