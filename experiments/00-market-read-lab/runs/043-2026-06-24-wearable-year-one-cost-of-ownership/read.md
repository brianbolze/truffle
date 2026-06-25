# Market Read

## Question

For a buyer choosing a connected sleep/recovery device (Oura, Whoop, Eight Sleep,
Peloton, Apple Watch), what is the **year-one total cost of ownership** — device plus
required-vs-optional subscription — and the lock-in, and can the store deliver an
apples-to-apples year-one number per brand **from captured State alone**?

## Result

**Buyer answer (year-one total cost of ownership, from captured State):**

| Brand | Device (one-time) | Subscription | Sub required? | **Year-one TCO** | Lock-in shape |
|---|---|---|---|---|---|
| **Whoop** | $0 — device bundled into membership | $199 / $239 / $359 per **yr** (tier floors, "Starts at") | **Yes — by construction** (device-as-a-service; you join, you don't buy) | **$199–$359** | Membership IS the product; 12-mo term, device included |
| **Oura** | Ring $244–$499 (Ring 5 $399/$499; Ring 4 from $244) | $5.99/mo **or** $69.99/yr (first month free) | **For value, yes** — ring functions without it but insights "much more limited"; framed inseparable | **~$314–$569** (≈ ring + $70) | Buy ring once, then pay to keep the scores |
| **Peloton** | Bike from $1,695 · refurb Original Bike from $695 · Tread+ to $6,695 | All-Access **$49.99/mo** ($599.88/yr), required for owners | **Yes** for hardware owners | **~$1,295 (refurb) → ~$7,295 (Tread+)** | Hardware-as-entry → mandatory monthly content sub |
| **Eight Sleep** | Pod 5 Core **$2,749** (Queen; Ultra & other sizes not captured) | Autopilot **required first 12 mo**, annual: $199 / $299 / $399 | **Yes — mandatory first 12 mo** | **~$2,948–$3,148** (or **rent $169/mo ≈ $2,028/yr** all-in) | One-time device + mandatory recurring software; rental fully subscription-izes it |
| **Apple Watch** | **Not captured at the Watch-SKU grain** (profile is company/catalog-level; only Mac entry prices quoted inline) | No required sub for the Watch; Fitness+ optional | **No** | **Cannot deliver from State** (device price absent) | Hardware one-time + optional services overlay |

**Foil / contrast set (pure one-time recovery hardware, no required subscription):**

| Brand | Device range | Subscription | Year-one TCO |
|---|---|---|---|
| Therabody | $84.99–$1,249.99 (Theragun, JetBoots, Therm, TheraFace…) | None shown | = device price |
| Hyperice | $99–$1,548 (Hypervolt, Normatec, Venom…) | None shown | = device price |
| Nike (recovery line) | $30–$999.97 (Hyperboot, Normatec Elite, Hypervolt…) | Membership is **free** loyalty | = device price |

**Can the store deliver an apples-to-apples year-one number? Mostly yes for 4/5 as an
honestly-caveated *range*, but NOT as a clean single comparable number — and not at all
for Apple Watch.** Every component a buyer needs — device price, subscription price,
billing cadence, and the required-vs-optional status — is present in captured State for
Oura/Whoop/Eight Sleep/Peloton, with capture clocks and point-in-time flags. The
buyer's hardest composite fact (year-one TCO + "is the recurring cost mandatory") **is
assemblable from State**. It just isn't in a single scannable column, and four structural
frictions block a true apples-to-apples sort (see Gap Map).

This directly pressure-tests **run-037's hybrid-revenue schema finding (G1/CR1)**: the
single-valued `business_model` lossiness is **real but not decision-blocking for a human
buyer** — prose + the per-offering price tokens carry the composite cost fine. It would
block only an *automated* apples-to-apples filter/sort, which sharpens run-037 W1 (a
ranked multi-select matters only if a consumer needs to *filter*, not merely read).

## Gap Map

**Where Truffle answered cleanly:**
- Per-offering device and subscription prices, with `[published]`/`[partial]` visibility
  tokens, capture clocks, and point-in-time sale flags — strong for all four connected
  DTC brands and all three foils.
- The required-vs-optional subscription distinction *is captured* — but in prose/`STRAIN:`
  comments, not a structured field (Whoop "you join, you don't buy"; Eight Sleep "required
  for the first 12 months"; Oura "the only way to unlock… insights"; Peloton "must hold an
  All-Access Membership").

**Where it fell short of a clean apples-to-apples number:**
1. **No structured required-vs-optional flag.** A buyer must read paragraphs to learn
   whether the recurring cost is mandatory (Eight Sleep, Whoop, Peloton) or only
   value-gating (Oura). Buyer-lens instance of run-037 G1/CR1.
2. **The "year-one" unit is structurally non-uniform.** Whoop bundles the device *into*
   the subscription (year-one = sub only, $0 device); the others separate them. Billing
   cadence differs (Whoop/Eight Sleep annual; Oura/Peloton monthly). Normalizing to one
   "year-one $" needs per-brand judgment, not a field — cousin of run-023's GLP-1 price
   incomparability, now on devices.
3. **Every device number is a point-in-time sale snapshot**, honestly flagged
   (Oura flash sale + same-day price disagreement $279 vs $399; Eight Sleep "4th July
   Sale"; Peloton "limited-time" refurb). A year-one TCO inherits that volatility.
4. **Apple Watch can't be answered from State at all** — Apple is captured at
   company/catalog grain (a multi-product giant), with no Watch-SKU price. A
   single-product buyer question hits an entity-grain mismatch.

For a `value-read`, the honest deliverable is a **caveated per-brand TCO range a human
buyer can act on**, not a single sortable comparable. That distinction is the result.

## Evidence Used

All evidence is local captured State (`store/<domain>/profile.md`), store-only, no
external sources. Claim IDs map to receipt `R1`.

- `C1` Whoop year-one = membership only ($199/$239/$359/yr, device included): whoop-com/profile.md:35,40,63,65–67,75.
- `C2` Oura ring $244–$499 + $5.99/mo ($69.99/yr) membership, value-gating: ouraring-com/profile.md:41,48,71–74,81.
- `C3` Eight Sleep Pod $2,749 + mandatory Autopilot $199–$399/yr (rent $169/mo): eightsleep-com/profile.md:37,44,67–68,75,79.
- `C4` Peloton device $695–$6,695 + required All-Access $49.99/mo: onepeloton-com/profile.md:36,43,64,67–80,87.
- `C5` Apple Watch SKU price absent; catalog-grain capture: apple-com/profile.md:33,40,59.
- `C6` Foils (Therabody/Hyperice/Nike) one-time only, no required sub: therabody-com/profile.md:51,72–79; hyperice-com/profile.md:51,84; nike-com/profile.md:49,88–94.

## Companies Seen

**Cohort (connected sleep/recovery, device + recurring):** ouraring-com, whoop-com,
eightsleep-com, onepeloton-com, apple-com (Apple Watch).
**Foil set (one-time recovery hardware):** therabody-com, hyperice-com, nike-com.

Drawn deliberately by entity-shape (connected device with a recurring layer), **not** by
`primary_industry` — which scatters this cohort and would pull in unrelated companies
(the n=4 `denominator-reconciliation` pattern; not re-litigated here, just respected in
the draw).

## Missing / Stale Coverage

- **Apple Watch SKU pricing** — not captured (catalog-grain profile).
- **Eight Sleep** Pod 5 Ultra price and non-Queen sizes — not rendered at capture.
- **Whoop** all-in checkout total — gated behind join.whoop.com, not captured (tier
  floors only).
- **Oura** Ring 4 base price and Ceramic price — client-rendered / same-day disagreement.
- All device prices are 2026-06-24-era sale snapshots; a refresh would move the numbers.

## Source Gaps

No external source family was needed for the buyer answer itself — this is a store-only
value-read and the store carried it. The one genuinely unreachable fact (Whoop's all-in
gated checkout, Apple Watch SKU price) sits **behind a funnel or below the captured
grain**, not in a missing external panel. (This is the *positive* face of the recurring
"decision-grade fact lives off the captured surface" pattern: here, for the price
ingredient on DTC device makers, it mostly lives *on* the captured surface.)

## Raw Learning to Preserve

See `run-notes.md` Observations: **S1** (buyer's composite TCO is assemblable from State —
a positive), **G1** (required-vs-optional flag is prose/STRAIN-only), **S2** (year-one
unit structurally non-uniform across the cohort), **G2** (Apple Watch entity-grain
mismatch — catalog company can't answer a SKU buyer question), **S3** (every device
number is a point-in-time sale snapshot), **W1** (lightest graduation path only if a
*filtering* consumer appears), **S4** (foils confirm `business_model` accurate for
single-leg; clean contrast).

## External Completeness Check

Not run — completeness of the *market* denominator is not load-bearing for this read
(the question is "for these brands," a buyer's consideration set, not "all wearables").
The cohort is an explicitly partial, entity-shape-selected set; "not captured" ≠ "not
on the market."

## Market Pattern

Connected sleep/recovery hardware has converged on **device-as-entry → recurring
revenue**, but along a spectrum of how hard the lock-in is bolted on:

- **Pure device-as-a-service** (Whoop): no device sale at all — you rent access; year-one
  cost is the subscription.
- **Mandatory bundled sub** (Eight Sleep, Peloton): buy the hardware, but it's inert
  without the required recurring sub; both also offer a rental path that fully
  subscription-izes the big-ticket device.
- **Value-gating sub** (Oura): you own a working device; the sub unlocks the insights
  that are the actual reason to buy it.
- **Optional overlay** (Apple Watch): device stands alone; services are an upsell.
- **No recurring layer** (Therabody, Hyperice, Nike recovery): one-time purchase, no
  lock-in — the contrast that proves the model is a choice, not a category inevitability.

The buyer takeaway: **year-one cost is dominated by the subscription structure, not the
sticker price.** A $0-device Whoop ($199–$359/yr) and a $2,749 Eight Sleep Pod live in
the same "you will keep paying" category; a $549 Theragun does not.

## What Would Change This Answer

- A returning capture (prices are sale snapshots; numbers will move).
- Capturing Apple at the Apple-Watch-SKU grain (would complete the 5th cohort member).
- A real downstream consumer who needs to **filter or sort** brands by composite year-one
  cost programmatically — that, and only that, is when run-037 W1's ranked-multi-select
  `business_model` (or a structured required-vs-optional flag) would earn its place. A
  human buyer reading the profiles does **not** need it; prose carries the decision today.
