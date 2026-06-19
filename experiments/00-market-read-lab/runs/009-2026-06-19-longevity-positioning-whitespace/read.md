# Market Read

## Question

In the longevity/NAD telehealth cohort, what **positioning wedge** does each brand anchor on
(NAD+ precursor supply vs rapamycin/senolytics vs biomarker-diagnostic-first vs hormone-optimization),
what **proof devices** do they lead with, and where is the **sameness vs real whitespace**?

Store-only, captured-State read. All claims below are from captured marketing-page State on disk
(capture dates per brand, 2026-05-31…06-18); several heroes are flagged point-in-time (A/B-live).
Judgments are labeled `[J]` and tied to the State they rest on.

## Direct Answer

**The cohort does not split into four wedges — it splits along one axis: _sell me the molecule_ vs
_measure me, then prescribe a protocol_.** [J] Every brand's positioning lands somewhere on a
**supply-access ↔ diagnostic-first** spectrum, and the proof devices follow the position:

- **Supply-access pole** (the molecule *is* the product; proof = ingredient science + quality/heritage):
  **truniagen**, **niagenplus**, **prohealth** — all NAD+/NMN-precursor-led, no required labs, no
  membership (niagenplus is the odd Rx-but-no-labs middle).
- **Catalog-under-a-banner** (a broad à-la-carte longevity catalog flying a longevity flag; proof =
  research identity): **agelessrx**.
- **Diagnostic-first pole** (a biomarker panel is the mandatory front door; proof = panel size +
  named clinicians + personalization; mostly membership-gated — gogeviti / mylifeforce / honehealth are
  membership-required, gethealthspan is à-la-carte/both with only HRT/GLP-1/TRT behind membership):
  **gogeviti**, **mylifeforce**, **gethealthspan**, **honehealth**.

**The load-bearing finding [J]:** the diagnostic-first pole is **crowded and same-y** — four brands all
lead with "measure 50–100+ biomarkers → personalized protocol," and **all four**
(**honehealth, mylifeforce, gethealthspan, gogeviti**, plus straddler **getopt**) quietly run **Schedule-III
testosterone/HRT** behind the longevity banner. **"Longevity clinic" in this cohort frequently means
"hormone-optimization clinic wearing a longevity coat."** That connects directly to run 008's
"price-posture tracks business model" thread: the diagnostic-first longevity brands *are* the
membership/clinic business model, and the NAD-supply brands *are* the publish-and-sell model.

## Evidence Used

State only — no external/current/news claims; no snippets. Each claim ties to a brand's captured
`telehealth.md` / `profile.md` / `offerings.md` on disk. Receipt:
[`receipts/longevity-positioning-panel.md`](receipts/longevity-positioning-panel.md) (`C1` = the
per-brand positioning/proof panel; `C2` = the supply↔diagnostic axis assignment; `C3` = the
Schedule-III-behind-longevity-banner tell).

## Companies Seen

**Core cohort (8)** — `anchor_category: longevity/NAD` per `telehealth.md`:

| Brand | Captured | Position on axis [J] | Hero / positioning (verbatim State) | Lead proof device (State) | Labs | Access | Rx grain |
|---|---|---|---|---|---|---|---|
| **truniagen** | 06-16 | Supply (OTC) | NAD+ / "cellular health" / healthy aging; Niagen® NR | Science pedigree: advisory board w/ **Nobel laureates** + NR discoverer **Dr. Charles Brenner**; NSF/GRAS/NDI/ISO/CoA seals | none | à-la-carte / Subscribe&Save, no membership | OTC supplement |
| **niagenplus** | 06-04 | Supply (Rx) | "A new way to access **Niagen®**… the science of cellular health" | Single-molecule Rx access; **$299 one-time kit** (consult bundled) | none | per-visit, no membership | Rx, non-scheduled (Niagen only) |
| **prohealth** | 06-07 | Supply (+Rx arm) | **NMN/NAD+** hero front door; GLP-1/pharma secondary | Heritage: **BBB A+, 35 consecutive years**; named Rx clinician (Beluga/Jonah Mink MD) | optional (DNA bio-age test) | à-la-carte / Subscribe&Save, no membership | non-scheduled (NMN supplement + compounded GLP-1/sermorelin/NAD) |
| **agelessrx** | 05-31 | Catalog-under-banner | "Harness the power of **longevity science**" + 4 co-equal tiles (longevity/weight/heart/energy) | Research identity: **XPRIZE Healthspan semi-finalist**, "5,200+ participants," "70,000+ NAD+ users"; named 6-person team; Rapamycin+Metformin as credibility molecules | per-Rx (rapamycin gated) | à-la-carte, no membership | non-scheduled (no TRT SKU) |
| **gethealthspan** | 06-04 | Diagnostic-first *(by positioning)* | "**1st digital longevity clinic**" / rapamycin-senescence front door | Named **MD/PhD advisory board** ("150+ published works"); "Trusted by 12K Patients"; 70+ biomarkers, labs incl. in protocols | optional (incl. in protocols) | à-la-carte/both; HRT/GLP-1/TRT need membership $99–129/mo | **Schedule-III testosterone** (via membership) |
| **mylifeforce** | 06-04 | Diagnostic-first | "**America's largest longevity medicine program**" | **50+ biomarker Lifeforce Diagnostic** ($599) as mandatory entry; named clinicians; LegitScript | required-step | membership $149/mo | **Schedule-III testosterone** |
| **honehealth** | 06-18 | Diagnostic-first | "Longevity **engineered around your biology**" / "Death to Midlife" | **$65 biomarker panel** entry wedge; Trustpilot **4.8/11,677**; named physician group | required-step | membership $25 / $155/mo | **Schedule-III testosterone** (flagship treatment line) |
| **gogeviti** | 06-04 | Diagnostic-first | "We **map your body** / longevity" (data-stream unification) | **100+ biomarker Longeviti Panel** 2×/yr; SOC2/HIPAA/CLIA (no named clinician roster) | required-step (in Plus) | membership-required | **Schedule-III testosterone/HRT + enclomiphene** (app-walled) |

**Straddlers inspected, scored separately:**
- **getopt-com** (`anchor_category: TRT`) — front door is a *concierge longevity/optimization membership*
  ("Opt into a Better You," "Be 55. Feel 35.," Opt Performance Score) but the foregrounded vertical is
  **TRT**. The clearest example of the longevity-coat-over-hormones pattern; correctly *not* counted in
  the core 8 (its anchor is TRT, not NAD).
- **joinfridays-com** (`anchor_category: GLP-1`) — runs a longevity line but is a GLP-1 brand; out of cohort.

## Missing / Stale Coverage

- **Captures span 05-31…06-18 (≤19 days old).** honehealth (06-18) and truniagen (06-16) are freshest;
  agelessrx (05-31) oldest. All within a normal capture window for a positioning read.
- **Point-in-time heroes:** agelessrx (rotating coupon instrumentation), honehealth (Optimizely A/B live),
  mylifeforce/gethealthspan heroes are positioning snapshots. Hero *copy* itself was not observed rotating
  for niagenplus/truniagen (stable single-molecule front door). Read positions as captured-floor, not
  durable doctrine.
- **gogeviti Rx grain is app-walled** — per-molecule Rx/route/price live behind the member app, not on
  marketing pages; the Schedule-III read is from page-attested catalog references, not a PDP.

## Source Gaps

- **No proof of the actual promise.** Every brand leads with *mechanism* (NAD+/rapamycin), *measurement*
  (biomarker panels), or *access* (buy the molecule) — **none leads with outcome evidence** of lifespan/
  healthspan extension, because none can. This is a real category-level whitespace, not a store gap. [J]
- **Reviews/forums are not in the store as State.** The "do longevity buyers trust this?" question
  (objection mining, distrust of compounded NAD, churn complaints) needs live reviews/Reddit/Trustpilot
  bodies — a `live-external-needs-approval` source ingredient this read cannot reach. Trustpilot *ratings*
  appear in some `profile.md` Credibility blocks but the review *content* does not.

## External Completeness Check

Completeness is **not** load-bearing here — this is a positioning read over a named, store-resident
cohort, not a market-share or census claim. The 8-brand set is the store's current `longevity/NAD`-anchored
population (grep of `telehealth.md` frontmatter); a fuller external census (e.g. Novos, Tally Health,
Healthspan.io, Modern Age, Blueprint/Bryan Johnson) would add brands but would not change the **axis** or the
**sameness** finding — the supply↔diagnostic spectrum and the crowded diagnostic-first pole are structural,
not artifacts of which 8 are captured. [J] Flagged as a partial cohort, not a market map.

## Market Pattern

**Sameness / table stakes (State across the cohort):**
- **NAD+ as the category totem** — even diagnostic-first clinics carry an NAD line; "cellular health,"
  "biological age," "healthy aging," "optimize" are universal vocabulary.
- **Cash-pay, no insurance; HSA/FSA eligibility** is the near-universal payment posture (truemed partnerships
  at prohealth/truniagen; HSA/FSA badges at agelessrx/gethealthspan/mylifeforce/gogeviti).
- **Cancel-anytime** and a **trust seal** (LegitScript *or* product-quality certs *or* BBB/Trustpilot) are
  table stakes.
- **Diagnostic-first brands are nearly interchangeable on the surface:** biomarker-panel-count one-upmanship
  (40+ → 50+ → 70+ → 100+) + named clinicians + "personalized protocol" + membership. [J]

**Real differentiation / whitespace [J]:**
- **truniagen owns science pedigree** (Nobel laureates + the NR discoverer) more credibly than any peer — a
  moat the compounded-NAD sellers can't copy.
- **niagenplus occupies a genuinely odd lane** — Rx-gated single-molecule NAD with *no labs and no membership*;
  differentiated but strategically awkward (Rx friction without the clinical wrapper that justifies it).
- **agelessrx's research identity** (XPRIZE, in-house studies, "we read the trials so you don't have to") is
  the cohort's strongest *narrative* differentiator and the only one leaning into anti-gatekeeping populism.
- **Open whitespace:** (1) an **honest-outcomes** lane — nobody leads with proof, so credible
  outcome/biomarker-improvement evidence is unclaimed; (2) a **clinician-backed protocol without the
  membership tax** — gethealthspan is closest but still $99+/mo; (3) the diagnostic-first pole is so crowded
  that a *new entrant should avoid it* and either go pure-supply-with-pedigree or own the outcomes lane.

**The cross-cohort tell (ties to run 008) [J]:** the four diagnostic-first "longevity" brands are the same
**membership/clinic business model** that gated pricing in the GLP-1/TRT reads, and **all four** sell
**Schedule-III testosterone/HRT behind the longevity banner**. The longevity coat is, for much of this cohort, a
**category-acceptable wrapper over hormone optimization** — a positioning-vs-substance gap a strategist
should name before building a brief. Supply-access brands (truniagen/niagenplus/prohealth) are the
publish-and-sell model; positioning posture tracks business model, again.

## What Would Change This Answer

- A brand in the cohort leading with **outcome/longitudinal-biomarker proof** would open the closed
  "promise/proof" lane and break the "everyone sells mechanism/measurement" finding.
- Capturing the **Rx grain behind gogeviti's app** (and honehealth/mylifeforce TRT PDPs) could show the
  hormone business is even larger than the marketing front door admits — strengthening the longevity-coat tell.
- A **live reviews/forums** layer could confirm or refute whether the diagnostic-first sameness actually
  costs trust/conversion, which this State-only read cannot see.
- A broader external census could add brands but, per the completeness check, is unlikely to move the
  **axis** or **crowded-pole** findings.
