# External-Event Panel — captured 2026-06-19

Tiny live panel (Firecrawl search, ~8 credits) to stress-test Run 000's three
time-sensitive assumptions: compounding legality, branded cash-pay price, and whether
public floors reflect a real access path. **Not** a broad GLP-1 news digest — only
sources that could *invalidate the stored read*.

> Post-run source-rigor note: this receipt is direction-finding, not citation-grade.
> It relied too heavily on search/news snippets. Before using the read as a decision
> input, re-pull primary FDA/manufacturer sources, record exact URLs and capture dates,
> and separate primary evidence from secondary commentary.

## Panel (source type → what it governs → what it said)

### 1. FDA compounding status — governs "compounded sema/tirz is the category floor"

- **FDA proposes to exclude semaglutide, tirzepatide, liraglutide from the 503B Bulks
  List** (~May 2026) — would permanently bar large-scale outsourcing-facility
  compounding, not just the shortage-era 503A path.
  - pharmacytimes.com/view/fda-moves-to-permanently-close-the-door-on-compounded-glp-1s
  - medpagetoday.com/publichealthpolicy/fdageneral/121044
- **FDA warning letter to 503B facility ProRx for producing tirzepatide after shortage
  ended** (May 18 2026). safemedicines.org/2026/05/may-18-2026.html
- **FDA clarification on which compounded GLP-1s still qualify** (Apr 2026) — personalized
  exceptions only. natlawreview.com/article/not-joking-around-fda-offers-additional-clarification-compounded-glp-1-policy-april

Read: the legal default has flipped. Mass-compounded sema/tirz is no longer a stable
"floor of the category"; it is a winding-down, enforcement-targeted exception path.

### 2. Manufacturer direct cash-pay — governs the branded price assumption

- **NovoCare (Wegovy):** self-pay **$199/mo intro → $349/mo** (price guide PDF; $199 for
  first 2 fills through Jun 30 2026, then $349). Down from a $499 launch.
  - novocare.com/.../Wegovy_Price_Guide.pdf ; novocare.com/pharmacy.html
  - prnewswire: "Novo Nordisk launches introductory self-pay offer for Wegovy and Ozempic
    for $199/month" (intro through Mar 31 2026; standard $349).
- **LillyDirect (Zepbound single-dose vials):** **$299–$499/mo** cash, lowest dose $349;
  Dec 1 2025 cut to $299–$449; Walmart retail pickup added Oct 2025.
  - pricinginfo.lilly.com/zepbound ; investor.lilly.com (vial price cut) ;
    cnbc.com/2025/12/01/eli-lilly-prices-zepbound-weight-loss-drug-vials.html
- Branded **list** price still ~$1,000–$1,350/mo (mattioli/insurance context) — but that
  is the insurance-billed number, not the access path a cash patient takes.

Read: manufacturer-direct cash-pay branded is now **~$349–$499/mo**, often at or below
compounded program pricing — a direct inversion of Run 000's "$900–$1,900/mo, on-request"
branded tier.

### 3. Brand-pivot news — governs "compounded-led DTC menu" framing

- **Hims & Hers ↔ Novo Nordisk partnership/settlement** (Mar 2026, stock +~50%): move most
  patients to branded Wegovy/Ozempic, keep compounded "at limited scale"; plus a $1.15B
  Eucalyptus acquisition.
  - yahoo: "The era of $199 copycat weight loss drugs is ending"
  - financialcontent: "HIMS 2026 Deep Dive: the $1.15B Eucalyptus deal and the branded pivot"
- **Noom** pivoted to smaller-dose compounded as the regulatory window closed (Reuters,
  May 2025) — the microdose tier Run 000 flagged is partly a compliance maneuver.

## Staleness delta vs Run 000 (dated same day, 2026-06-19)

| Run 000 assumption | June-2026 external reality | Verdict |
|---|---|---|
| Compounded sema/tirz = "the price floor of the category" | 503A path closed; FDA moving to bar 503B too; warning letters live | **Inverted / eroding** |
| Branded tier = $900–$1,900/mo, `on-request`/insurance-set | Manufacturer-direct cash-pay $349–$499/mo (NovoCare, LillyDirect) | **Stale by ~3–5×** |
| Branded is the gated *up-tier* above a compounded floor | Branded direct-pay now rivals/undercuts compounded; brands signing with manufacturers | **Story flipped** |

Important nuance: the store's DTC-telehealth captures are *not necessarily wrong* — those
brands genuinely quote branded SKUs at retail/"+ insurance." The **manufacturer-direct
channel (NovoCare, LillyDirect) is a separate, cheaper path the cohort capture never
sees**, because Novo/Lilly direct-pay aren't "telehealth companies" in the cohort. The
cheapest real branded access path is structurally invisible to a cohort read built from
DTC-brand pages.

## Minimal monitor spec (the system-test deliverable)

Three source types, narrow and datable, would have caught all three shifts:

| Watch | Canonical source(s) | Cadence | Why |
|---|---|---|---|
| Compounding legality | FDA shortage list + 503A/503B bulks-list actions + warning letters | event-driven (~monthly check) | High-consequence, low-frequency upstream switch |
| Branded cash-pay floor | NovoCare Wegovy/Ozempic price guide PDF; LillyDirect/pricinginfo.lilly.com Zepbound terms | monthly | Two structured pages set the real branded floor |
| Brand-channel pivots | one news query: "GLP-1 telehealth branded partnership / compounding" | monthly | Catches Hims-style channel realignments |

All three are **category/non-company** signals. None is a single `store/<domain>/`. The
FDA switch has no company home at all. That is the engine-relevant finding (see run-notes).
