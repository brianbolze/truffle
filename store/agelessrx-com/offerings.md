---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: agelessrx.com       # company key; each offering's slug (its relative url) is its key *within* AgelessRx
captured_at: 2026-06-03     # own freshness; captures/2026-06-03/ holds the source pages
---

## Portfolio overview

AgelessRx is the **broad-catalog generalist** of the longevity-telehealth cohort — **~51 distinct customer-facing
offerings** across nine therapeutic groupings (core longevity Rx, GLP-1/weight, NAD+, glutathione, peptides,
biological-age testing & monitoring, skin/hair, supplements, women's hormone) plus a paid consult. Nearly
everything is a clinician-gated, auto-refill **subscription** fulfilled by 503A compounding pharmacies; the
testing layer is one-time. The catalog is **flat with two cross-cutting nav axes** (by treatment family *and* by
need) rather than a clean hierarchy — so this roster enumerates at the SKU level and uses `Parent` to mark the
five families that have their own category page (GLP-1, NAD+, GSH, BioAge Tests, Core Longevity); peptides,
skin/hair, supplements and women's-hormone have no family page and sit at top level.

**The shape finding — almost everything is `published`, two patterns aren't:**
- **Most SKUs show a concrete "Starting at $X" subscription floor** (often with a quarterly-billing detail, e.g.
  Metformin "$25/month, billed $75 quarterly") → **`published`**. The number is real and public; the *all-in*
  can still move with dose ("a medical professional may recommend a different dose"), and checkout + rotating
  coupon codes resolve in the `customer.agelessrx.com` portal — so treat every price as a point-in-time floor.
- **The three brand-name GLP-1 access SKUs are `[partial]`.** Wegovy® (pill + injection) and Zepbound® show a
  **"$50/month + cost of medication"** access-and-monitoring fee where the medication is bought *separately* from
  NovoCare®/LillyDirect® at tiered, conditional prices ($149–$449/mo). The $50 is real but never the all-in —
  the AgelessRx-vs-brand split is the gotcha.
- **Two SKUs are `[on-request]`:** **BPC-157** has a live PDP but its body is **password-protected** ("Starting
  at $X" placeholder — not publicly buyable), and the paid **Longevity Consultation** is **"fully booked,"
  waitlist-only**.

**Prominence (calibrated).**
- **NAD+ is the flagship line [HIGH].** Three corroborating *own* signals: NAD+ Injection gets the company's
  **newest, most-invested PDP template** (see Deep blocks), the site claims **"70,000+ NAD+ users supported,"**
  and its XPRIZE Healthspan entry is explicitly *"studying NAD+."* It also leads the `/treatments/` "Featured" sort.
- **Metformin & Rapamycin are the credibility anchors [HIGH].** They head the curated "Find the right solution"
  set on the General-Longevity page and carry the heaviest science framing (Metformin's "Gatekeeping is so
  traditional healthcare" citation wall + its own 101 video); the profile's read holds.
- **Sermorelin is being actively promoted [HIGH].** A **sitewide promo bar** reads *"Boost energy, lean muscle,
  and focus | Save $50 on Sermorelin"* — the company's own current campaign (coupon `SERINJ50`).
- **GLP-1/weight is a featured volume line [MED]** — its own top-nav category, a dedicated landing, and the
  widest single lineup (6 SKUs), but priced as one family among several.
- Card sort-order within a page beyond the Featured lead, and the "In Stock" stock tags, are **[LOW]** / not
  emphasis — excluded from ranking.

## Roster

Complete at the indexed level (the `/treatments/` grid + the `agelessrx_product` registry; the 16 ad-experiment /
shopping-feed / direct-to-triage duplicate URLs are *not* separate offerings and are excluded). Within-company
key = **Slug**. Price quoted verbatim with its on-page markers; molecule/form is page-attested only (audit under
Verbatim anchors). An offering here is never asserted equal to a same-molecule offering at another brand.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Core Longevity Rx** | family | — | `/products-longevity/` | — | — | The flagship Rx grouping (no single SKU page); credibility anchors live here. |
| Metformin | buyable | Core Longevity Rx | `/metformin/` | `Starting at $25` · `$25 / month, billed $75 quarterly · shipped quarterly` | published | metformin · pill, once-daily · Rx subscription; 1,000mg/day or as prescribed. |
| Rapamycin | buyable | Core Longevity Rx | `/rapamycin/` | `Starting at $65` · `$65 / month, free shipping · free medical visit` | published | rapamycin · pill · Rx; "ongoing monitoring and blood work included." |
| Acarbose | buyable | Core Longevity Rx | `/acarbose/` | `Starting at $55` | published | acarbose · pill · Rx subscription. |
| Methylene Blue | buyable | Core Longevity Rx | `/methylene-blue/` | `Starting at $43` · `$43 / month, billed $129 quarterly` | published | methylene blue · pill · Rx subscription. |
| Low Dose Naltrexone (LDN) | buyable | Core Longevity Rx | `/ldn/` | `Starting at $25` | published | naltrexone (low-dose) · pill · Rx subscription. |
| Brenzavvy® | buyable | Core Longevity Rx | `/brenzavvy/` | `Starting at $125` · `$125/month after` | published | bexagliflozin (SGLT2 inhibitor) · pill, once-daily · Rx. |
| Invokana® | buyable | Core Longevity Rx | `/invokana/` | `Starting at $449` · `$449/month after` | published | canagliflozin (SGLT2 inhibitor) · pill, once-daily · Rx. |
| Atorvastatin | buyable | Core Longevity Rx | `/atorvastatin/` | `Starting at $30` · `$30 / month, billed $90 quarterly · free shipping` | published | atorvastatin · pill, once-daily · Rx subscription. |
| Telmisartan | buyable | Core Longevity Rx | `/telmisartan/` | `Starting at $30` · `$30 / month, billed quarterly` | published | telmisartan · pill · Rx subscription. |
| Tadalafil (Daily) | buyable | Core Longevity Rx | `/tadalafil-daily/` | `Starting at $60` · `$70/mo monthly` / `$60/mo billed $180 quarterly` | published | tadalafil · pill, daily · Rx subscription. |
| Tadalafil (As Needed) | buyable | Core Longevity Rx | `/tadalafil-as-needed/` | `Starting at $45` · `$50/mo monthly` / `$45/mo billed $135 quarterly` | published | tadalafil · pill, as-needed · Rx subscription. |
| **GLP-1 Support** | family | — | `/semaglutide-glp-1s/` | `Starting at $139` | — | The weight/GLP-1 line; gates the SKUs below behind a BMI-screened intake. |
| Injectable GLP-1 Treatments | buyable | GLP-1 Support | `/glp-1-injections/` | `Starting at $139` | published | semaglutide (compounded) · injection, weekly · Rx subscription. |
| Microdosing GLP-1 | buyable | GLP-1 Support | `/microdosing-glp1/` | `$99 / month` (semaglutide) · `$249 / month` (tirzepatide) | published | tirzepatide *or* semaglutide (compounded, low-dose) · injection · Rx; two molecule tiers. |
| Compounded Liraglutide | buyable | GLP-1 Support | `/compounded-liraglutide/` | `Starting at $149` · `$289/month after` | published | liraglutide (compounded, + B12) · injection, daily · Rx subscription. |
| Wegovy® Pill Access & Monitoring | buyable | GLP-1 Support | `/wegovy-pill-access-monitoring/` | `$50 + cost of medication` | partial | semaglutide (Wegovy®, oral) · pill · $50 access fee + separate NovoCare® med cost (tiered $149→$299 / $199→$349). |
| Wegovy® Access & Monitoring | buyable | GLP-1 Support | `/wegovy-access-monitoring/` | `$50 + cost of medication` | partial | semaglutide (Wegovy®, injection) · injection, weekly · $50 access fee + separate NovoCare® med cost ($199 first two months → $349). |
| Zepbound® Access & Monitoring | buyable | GLP-1 Support | `/zepbound-consultation/` | `$50 + cost of medication` | partial | tirzepatide (Zepbound®) · injection, weekly · $50 access fee + separate LillyDirect® introductory med cost ($299/$399/$449). |
| **NAD+ Support** | family | — | `/all-nad-support/` | — | — | Four delivery forms of NAD+; the flagship line (own newest PDP template). |
| NAD+ Injection | buyable | NAD+ Support | `/nad-injection/` | `Starting at $99/mo` | published | NAD+ (nicotinamide adenine dinucleotide) · injection, subcutaneous, 1–3×/wk · Rx, compounded; 2.5ml/5ml vials. |
| NAD+ Patches | buyable | NAD+ Support | `/nad-patch/` | `Starting at $160` | published | NAD+ · patch, iontophoresis, once-weekly · Rx, compounded. |
| NAD+ Nasal Spray | buyable | NAD+ Support | `/nad-nasal-spray/` | `Starting at $125` · `$125 / month, billed monthly` | published | NAD+ · nasal spray · Rx, compounded. |
| NAD+ Face Cream | buyable | NAD+ Support | `/nad-cream/` | `Starting at $95` · `$95 / month, billed monthly` | published | NAD+ · topical cream · Rx, compounded; targets aging skin. |
| **GSH Support** | family | — | `/all-gsh-support/` | — | — | Three delivery forms of glutathione, "at a fraction of the cost of IV therapy." |
| Glutathione Injection | buyable | GSH Support | `/gsh-injection/` | `Starting at $99` | published | glutathione (GSH, 100mg/0.5mL inj) · injection · Rx, compounded. |
| Glutathione Nasal Spray | buyable | GSH Support | `/gsh-nasal-spray/` | `Starting at $100` · `$100 / month, billed monthly` | published | glutathione · nasal spray · Rx, compounded. |
| Glutathione Patches | buyable | GSH Support | `/gsh-patch/` | `Starting at $190` | published | glutathione · patch, iontophoresis, once-weekly · Rx, compounded. |
| Sermorelin Injection | buyable | — | `/sermorelin/` | `Starting at $99` | published | sermorelin (GHRH analog peptide) · injection, subcutaneous, nightly · Rx, compounded. |
| Sermorelin Nasal Spray | buyable | — | `/sermorelin-nasal-spray/` | `Starting at $199` · `$199 / month, billed monthly` | published | sermorelin · nasal spray · Rx, compounded; needle-free. |
| PT-141 Injection | buyable | — | `/pt-141-injection/` | `Starting at $199` · `$199 / month, billed monthly` | published | PT-141 (peptide) · injection · Rx, compounded; libido/arousal. |
| PT-141 Nasal Spray | buyable | — | `/pt-141-nasal-spray/` | `Starting at $199` · `$199 / month, billed monthly` | published | PT-141 (peptide) · nasal spray · Rx, compounded. |
| GHK-Cu Cream | buyable | — | `/ghk-cu-cream/` | `Starting at $199` · `$199 / month, shipped monthly` | published | GHK-Cu (copper peptide) · topical cream · Rx, compounded; skin regeneration. |
| BPC-157 | buyable | — | `/bpc-157/` | `Starting at $X` (no price — page password-protected) | on-request | BPC-157 (peptide) · injection · gated; PDP body is password-protected, not publicly buyable. |
| **Testing & Monitoring** | family | — | `/biological-age-test/` | — | — | The measurement layer — two site families: BioAge Tests (`/biological-age-test/`, one-time) + Health Monitoring (`/health-monitoring/`, CGM/coaching). |
| At-Home Methylation Saliva Test (TruMe™) | buyable | Testing & Monitoring | `/trume/` | `Starting at $170` | published | DNA-methylation epigenetic test (TruMe™) · saliva test kit · one-time. |
| TruDiagnostic At-Home BioAge Blood Test | buyable | Testing & Monitoring | `/trudiagnostic/` | `Starting at $495` | published | epigenetic methylation test, 900,000+ biomarkers (TruDiagnostic) · at-home blood test · one-time. |
| Lab-Based Phenotypic Blood Test | buyable | Testing & Monitoring | `/pheno-age-blood-test/` | `Starting at $75` | published | phenotypic age, 9 blood markers (at Quest) · lab blood draw · one-time. |
| iollo Advanced At-Home Metabolic Test | buyable | Testing & Monitoring | `/iollo-advanced-at-home-metabolic-test/` | `Starting at $399` | published | metabolomic test, 600+ biomarkers (iollo) · at-home test kit · one-time. |
| Core Longevity Panel | buyable | Testing & Monitoring | `/core-longevity-panel/` | `Starting at $95` | published | 40+ biomarker longevity blood panel · lab blood draw · one-time, report in 2 weeks. |
| Galleri Multi-Cancer Early Detection Test | buyable | Testing & Monitoring | `/galleri-multi-cancer-early-detection-test/` | `Starting at $949` | published | cfDNA multi-cancer detection, 50+ cancers (Galleri) · blood draw · one-time. |
| Online Phenotypic Calculator | buyable | Testing & Monitoring | `/biological-age-calculator/` | `FREE` | published | biological-age calculator, 9 markers · online tool · free (needs recent bloodwork). |
| Glucose Biosensors (CGM) | buyable | Testing & Monitoring | `/cgm-sensor/` | `Starting at $99` · `$99 / month, billed monthly · six month commitment · free shipping` | published | glucose biosensor (Stelo / Nutrisense CGM) · wearable sensor · subscription. |
| Nutrisense (dietitian coaching) | buyable | Testing & Monitoring | `/nutrisense/` | `Free with insurance` (`$0 out-of-pocket` for "most clients") | published | nutrition coaching (partner; registered dietitian) · service · partner referral for GLP-1 patients. |
| Tretinoin | buyable | — | `/tretinoin/` | `Starting at $70` · `$85/mo monthly` / `$70/mo billed $210 quarterly` | published | tretinoin · topical cream · Rx, compounded; wrinkles/sun damage. |
| DMAE Firming Gel | buyable | — | `/dmae/` | `Starting at $68` · `$85/mo monthly` / `$68/mo billed $205 quarterly` | published | DMAE 3% (Rx-strength) · topical gel · Rx, compounded; AgelessRx exclusive. |
| Powers Hair Solution v5.1 | buyable | — | `/powers-hair-solution/` | `Starting at $95` · `$120/month after` | published | minoxidil + dutasteride (+9 ingredients) · topical solution · Rx, compounded. |
| Infinite Longevity Support | buyable | — | `/infinite-longevity-support/` | `Starting at $65` · `$75/mo monthly` / `$65/mo billed $195 quarterly` | published | multi-ingredient longevity supplement (carnosine, AKG, glucosamine, astaxanthin, pterostilbene…) · pill/packet · subscription (OTC). |
| Heart Health Pack | buyable | — | `/heart-health-pack/` | `Starting at $55` · `$75/mo monthly` / `$55/mo billed quarterly` | published | berberine + aged garlic + black garlic + GSE + ALA · pill pack · subscription (OTC). |
| Glucose Control Supplement | buyable | — | `/glucose-control-supplement/` | `Starting at $25` · `$30/mo monthly` / `$25/mo billed quarterly` | published | inositol · pill, daily · subscription (OTC). |
| Tran-Q Sleep | buyable | — | `/tran-q-sleep/` | `Starting at $43` · `$49/mo monthly` / `$43/mo billed $129 quarterly` | published | not stated — all-natural GABA-supporting sleep blend · pill · subscription (OTC). |
| Trazodone | buyable | — | `/trazodone/` | `Starting at $33` · `$49/mo monthly` / `$33/mo billed $99 quarterly` | published | trazodone · pill · Rx subscription; sleep. |
| B12 Injection | buyable | — | `/b12-injection/` | `Starting at $75` | published | vitamin B12 · injection · subscription. |
| B12/MIC Injection | buyable | — | `/b12-mic-injection/` | `Starting at $110` | published | B12 + methionine, inositol, choline (MIC) · injection · subscription. |
| Women's Hormone Care | buyable | — | `/womens-hormone-care/` | `Starting at $50` (consult) · `$70/month for the first month, then $95/month per prescription` | published | estradiol, micronized progesterone, and/or DHEA · cream/patch/pill · consult-led, compounded. |
| Longevity Consultation | buyable | — | `/longevity-consultation/` | none shown — "**fully booked**," waitlist only | on-request | paid 1:1 longevity consult · service · currently paused (Typeform waitlist). |

### Verbatim anchors

The footnotes the Price column points at — the strings that *decide* `partial`/`on-request`, and the
molecule-sourcing audit. Quoted exactly from the cited captures.

- **GLP-1 brand access → `[partial]` (the AgelessRx-fee-vs-brand-med split):** all three brand SKUs show the
  AgelessRx fee as **"$50 / month + cost of medication"** with the drug bought separately:
  - Wegovy® injection: *"The cost of Wegovy® is $199 for the first two months … $349/month for all doses. The
    cost of the medication is separate and paid directly to [NovoCare]."*
  - Wegovy® Pill: med tiers *"$149/month for first two months, $299/month after for all doses"* and
    *"$199/month first two months, $349/month after."*
  - Zepbound®: *"introductory prices from LillyDirect®… only available for the first order and refills made
    within 45 days,"* med tiers `$299` / `$399` / `$449`/month. → the $50 is real but access-only; all-in = $50 + brand med.
- **BPC-157 → `[on-request]`:** the PDP renders a product hero ("BPC-157," peptide description) then
  *"Starting at **$X**"* and *"This content is password-protected. To view it, please enter the password below."* —
  a live but **non-public** SKU (no real price exists to quote).
- **Longevity Consultation → `[on-request]`:** *"Our longevity consult is fully booked (for now)… we've
  temporarily paused new bookings… you can join the waitlist."*
- **Molecule sourcing (page-attested-only audit):**
  - **Brenzavvy® → bexagliflozin · Invokana® → canagliflozin** — attested: *"Invokana® (Canagliflozin) and
    Brenzavvy® (Bexagliflozin) are both oral medications, taken by mouth once per day."*
  - **Wegovy® → semaglutide** — *"Wegovy® contains Semaglutide."* **Zepbound® → tirzepatide** — *"Zepbound®
    contains the active ingredient Tirzepatide."*
  - **Microdosing GLP-1 → tirzepatide *or* semaglutide** — *"Microdosing GLP-1 is a low-dose Injectable GLP-1
    prescription (Tirzepatide or Semaglutide)."* (Both tiers attested; not inferred.)
  - **Powers Hair → minoxidil + dutasteride** — *"this exclusive formula features minoxidil and dutasteride,
    with 9 other synergistic ingredients."*
  - **Glutathione Injection → "100mg of GSH"** — *"Each injection (0.5mL/cc) contains 100mg of GSH."*
  - **Heart Health Pack → berberine + aged garlic (+ black garlic, GSE, ALA)**; **Glucose Control → inositol**
    (*"A daily dose of inositol"*); **B12/MIC → "B12 + methionine, inositol, choline (MIC)"** — all attested in product copy.
  - **Women's Hormone Care → estradiol, micronized progesterone, DHEA** — attested via the FDA disclaimer:
    *"The FDA has not approved or reviewed Estradiol, Micronized Progesterone, and/or DHEA…"*
  - **PT-141 → "PT-141 (peptide)"**, *not* "bremelanotide": the PDP states *"targeted peptide therapy"* but
    never names bremelanotide — recorded as the page names it.
  - **Rapamycin → "rapamycin"** (the page never says "sirolimus"); **Tran-Q Sleep → not stated** (an "all-natural"
    blend, no single molecule named) — both kept page-literal rather than inferred.

## Deep blocks

Three earn their place — the three PDPs you asked to dissect (Sermorelin, Metformin, NAD+ Injection). They earn
it beyond restating roster cells because together they expose a finding a row can't carry: **AgelessRx is
mid-redesign and runs three PDP template generations at once**, and the newest one's price layout is a live
misattribution trap. Each block: the PDP's section anatomy, then verbatim gold.

### The PDP template generations (the cross-cutting finding)

AgelessRx serves **three distinct PDP templates** simultaneously, and which one a SKU gets is itself a prominence
signal — the flagship gets the new build, legacy Rx the old one:

1. **Legacy template — `/metformin/`:** hero ("Starting at $X") → **"Other treatments to consider"** cross-sell →
   benefits → background → stat tiles → testimonials → how-it-works → **a detailed pricing box**
   ("$25 / month, billed $75 quarterly") → 101 video → FAQs → ISI → a numbered **citation table**.
2. **Mid / peptide template — `/sermorelin/`:** hero → **"What is X?"** → benefits → **"QUALITY TESTED"** lab panel
   (Potency / Sterility / Endotoxicity — Passed) → "The science of" → "Why AgelessRx?" → Trustpilot → FAQs → ISI →
   citation table. **No detailed pricing box** — just the hero floor + a coupon.
3. **Newest redesign — `/nad-injection/`:** teal rebrand + new nav, **image carousel**, inline trust bullets and an
   early FAQ, **"What is X? (chemical name)"**, a **"How X works" Day-1→1-Year timeline**, **"Results you can feel"**
   stat tiles, an **XPRIZE/research** block ("70,000+ NAD+ users"), "Made for your biology," how-it-works,
   a **cross-sell carousel**, an **expert-reviewer bio** (Dr. Stefanie Morgan, PhD), an FAQ accordion, and an
   11-entry citation list.

### Sermorelin Injection — the mid/peptide template

- **Parent:** — (peptides, no family page) · **slug:** `/sermorelin/` · **price:** `Starting at $99` (coupon
  `SERINJ50`, the sitewide "Save $50" promo) · **visibility:** `published`

> **H1:** "Sermorelin Injection"  (form tag: "Injection")
> **Hero (verbatim):** "Sermorelin has shown to boost energy, lean muscle mass, and strength by encouraging your
> body to replenish its own growth hormone safely and gradually, **without the risks and side effects of
> synthetic HGH therapy**."
> **What-is (verbatim):** "Unlike other synthetic options that override your system, Sermorelin works *with* your
> body, stimulating natural HGH production from the brain…"; "After age 30, human growth hormone (HGH) levels
> decline by up to 15% per decade."
> **Molecule (verbatim, page-attested):** "Sermorelin is an analog of growth hormone-releasing hormone (GHRH)…
> Sermorelin signals the pituitary gland to release human growth hormone (HGH) in a pulsed, physiological rhythm."
> **Not-a-steroid (FAQ verbatim):** "No, Sermorelin has a different mechanism of action than steroids. Sermorelin
> is a peptide that mimics growth hormone-releasing hormone (GHRH)…"
> **QUALITY TESTED panel (verbatim):** "Potency Test — Passed… Sterility Test — Passed (USP 71)… Endotoxicity —
> Passed (USP 85)."
> **Gating (verbatim):** "Sermorelin is only for patients who are at least 30 years old." · every CTA is "Start
> online visit" / "Get started," routing to the intake.
> **Compliance (verbatim):** "Sermorelin has not been approved by the FDA for these or any uses, but there are
> multiple studies that have shown these benefits."

**Why this block earns its place:** Sermorelin is the line the company is *actively promoting this week* (the
"Save $50" banner), and its template is the cleanest example of the mid-generation PDP — benefit-led, lab-panel
trust, **no pricing box** (the hero "$99" floor is the only price on the page; the all-in resolves in the portal).
The molecule is page-attested as a GHRH-analog peptide, not inferred.

### Metformin — the legacy template (the only one with a real pricing box)

- **Parent:** Core Longevity Rx · **slug:** `/metformin/` · **price:** `Starting at $25`, box `$25 / month, billed
  $75 quarterly | shipped quarterly` · **visibility:** `published`

> **H1:** "Metformin"  (form tag: "Pill")
> **Hero (verbatim):** "Metformin—a simple, once-daily medication originally used to treat diabetes—may also help
> support glucose control, encourage weight loss, and reduce the risk of certain age-related diseases."
> **The pricing box (verbatim — this is the legacy template's signature):** "$25 / month, billed $75 quarterly |
> shipped quarterly — 3-month supply per shipment — 1,000mg/day or as prescribed — Lab tested for purity — Free
> shipping. CODE **MET20**: $20 off first quarter & FREE medical evaluation."
> **Dose caveat (verbatim):** "A medical professional may recommend a different dose during medical intake
> process… You can request daily dose adjustments between refills."
> **Self-reported efficacy (verbatim):** "82% of patients felt improvement by their second check-in… 74% saw
> improvement in blood sugar levels… 75% felt better appetite control… 70% noticed reduced cravings" (n=1,412).
> **Safety / NDMA (verbatim):** "AgelessRx is not impacted by this recall, since we exclusively use Metformin
> manufactured by Tagi Pharma, which was found not to contain NDMA."
> **Science framing (verbatim H1, lower page):** "Gatekeeping is so traditional healthcare — We read the clinical
> trials so you don't have to." (followed by a 7-row citation table)

**Why this block earns its place:** Metformin is the anchor molecule and the *only* deep-dive PDP that still
carries the legacy **detailed pricing box** — the most concrete price on the whole site ("$25/month, billed $75
quarterly"), which is why its visibility is unambiguously `published`. The "Gatekeeping" citation wall is the
brand's credibility signature.

### NAD+ Injection — the newest redesign (and a price-misattribution trap)

- **Parent:** NAD+ Support · **slug:** `/nad-injection/` · **price:** **`Starting at $99/mo`** · **visibility:**
  `published`

> **H1:** "NAD+ Injection Rx"
> **Hero price (verbatim):** "Starting at **$99/ mo**" — with bullets "US-licensed pharmacies · High potency
> formula · 30 or 90-day supply options · Pause or cancel anytime."
> **What-is (verbatim):** "NAD+ (nicotinamide adenine dinucleotide) … is a vital coenzyme essential for everything
> from energy metabolism to DNA repair. As we age, levels decline."; "NAD+ levels drop up to 90% from age 30 to 60."
> **Dose (verbatim):** "Our NAD+ formulation contains 200mg/ml. A total 2.5ml vial totals 500mg NAD+, and a 5ml
> vial totals 1,000mg NAD+ total… 0.1ml = 20mg; 0.25ml = 50mg; 0.5ml = 100mg NAD+."
> **Results tiles (verbatim):** "89% felt benefits by second check-in · 83% felt more energized · 77% had more
> physical endurance · 75% reported better mental clarity" (n=1,412).
> **Flagship signals (verbatim):** "With **70,000+ NAD+ users supported** and multiple peer-reviewed clinical
> trials…"; "one of 40 global teams competing in the … XPRIZE Healthspan competition, **studying NAD+**…"

**The misattribution trap (why this earns a block):** this newest template renders the hero price as plain text
("Starting at" / "$99/ mo", *not* bolded) and then shows a **cross-sell carousel** whose first bolded price is
**"NAD+ Nasal Spray — Starting at $125."** A naïve grep for the first `**$…**` on the page returns **$125 and
misattributes it to NAD+ Injection** — the exact misattribution this module's lint guards against. The injection's
true floor is **$99/mo**, corroborated three ways (hero text, the General-Longevity card, and the page's own
"$99/mo"). The other carousel prices (Sermorelin $99, NAD+ Patches $160, B12 $75, LDN $25) are cross-sells, not
this SKU's.

## Provenance

- **Pages read — 57 fresh captures, all `captures/2026-06-03/`:** the `/treatments/` index (rich pass, for the
  Featured order); **51 product PDPs** (every distinct customer-facing offering — the full roster above; the 3
  deep-dive PDPs `/sermorelin/`, `/metformin/`, `/nad-injection/` captured with full formats + screenshot); **6
  family/category pages** (`cat-products-longevity`, `cat-semaglutide-glp-1s`, `cat-all-nad-support`,
  `cat-all-gsh-support`, `cat-biological-age-test`, `cat-health-monitoring`) for prices, comparison tables and
  prominence; plus a `/wp-json` REST read of the `agelessrx_product` registry. Context: `store/agelessrx-com/profile.md`
  + the prior 2026-05-31 captures. **Verify:** 59/59 sourceURL-matched, all bodies md5-unique (no geo/cache
  contamination). **Credits this run: 60** (1 index + 1 map + 2 REST + 51 PDPs + 6 family pages, 1 credit each).
- **Completeness:** enumerated at the indexed level off the `/treatments/` grid **and** the WordPress
  `agelessrx_product` registry (the authoritative source). The rendered grid showed **47 cards / "48 results"**;
  the registry's 69 entries resolved to **~51 distinct offerings** once the **16 duplicate leaves were excluded**
  (ad-experiment `*-mexp###` landing pages, `shopping-*` Google-feed dupes, `*-direct-to-triage` funnel variants,
  `nad-injection-2`, `semaglutide-glp-1s-ns` Black-Friday, `wegovy-pill-…-monthly`) — these are the same SKUs at
  marketing URLs, not separate offerings. The registry surfaced **4 offerings the visible grid omitted**: BPC-157,
  TruDiagnostic, Nutrisense, and the Longevity Consultation.
- **Gated / unreachable:** BPC-157 PDP body (password-protected — no public price); Longevity Consultation
  (waitlist, paused); the final all-in price for every SKU (checkout + dose-specific pricing + rotating coupon
  codes resolve inside `customer.agelessrx.com`; PDPs show "Starting at $X" floors only); the separate
  brand-medication cost for Wegovy®/Zepbound® (paid to NovoCare®/LillyDirect®, tiered and conditional).
- **Point-in-time snapshot, not fixed:** prices are "Starting at" floors; CTA deep-links bake in rotating coupon
  codes (`MET20`, `SERINJ50`, `NADINJ50`, `GLP100`, …) and the GLP-1 brand med prices are flagged "introductory."
  This module's own `captured_at` + a short TTL are the guard — re-capture before trusting a price as current.
