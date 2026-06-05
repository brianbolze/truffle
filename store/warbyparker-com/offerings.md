---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: warbyparker.com      # company key; each offering's slug (its relative url) is its key *within* Warby Parker
captured_at: 2026-06-04      # own freshness; captures/2026-06-04/ holds the source pages
site_notes: "Catalog shape — NOT enumerated to the SKU. Hundreds of frame styles live under /eyeglasses & /sunglasses (the /map returns ~466 URLs, ~90% individual PDPs at /eyeglasses/<style>/<color>); roster grain here is LINE + pricing tier + a few flagship exemplars. No /pricing page — house-frame prices ($95, some $145) sit on the category/PDP pages; the PDP 'Everything included for $95' box is the bundle truth. Contacts are RESOLD third-party brands (Acuvue, Air Optix, Biofinity, Biotrue, Dailies, MyDay…) + Warby's own Scout; per-box prices are behind brand/Rx selection (not on the category page). Eye-exam fee is behind the booking flow. PDP hero renders lazy-load (AIR_ASSETS blanks; i.warbycdn /s/f/ = color swatches) — flagship renders were cropped from PDP full-page screenshots into images/."
---

## Portfolio overview

Warby Parker is a **Catalog** seller, so this file captures **shape + exemplars, not the SKU list** — the eyewear
catalog runs to hundreds of styles × colors. The shape: a small set of **lines** — **Eyeglasses, Sunglasses,
Contacts, Accessories** (products) plus **Eye exams** (a service) and the pre-launch **Intelligent Eyewear** — sitting
on top of a **flat, legible price**: virtually every house frame is **$95 with prescription lenses included**, a
handful of premium styles **$145**. The two non-eyewear lines break the pattern: **Contacts are resold** (major
third-party brands + Warby's own **Scout**), and **Eye exams** are an in-store optometry service. Price is the headline,
not the individual SKU — which is exactly why a per-frame roster would be noise.

**Visibility rule (stated once, applied to every row).**
- **`published`** — the displayed price is the complete cost: every house frame is "$95, lenses included" (or $145),
  self-contained. Coatings (anti-reflective, scratch-resistant) and single-vision lenses are *in* the price (PDP box).
- **`on-request`** — no price shown until you act: **contacts** (per-box price behind brand/Rx selection),
  **eye exams** (behind the booking flow), **lens upgrades** beyond single-vision (progressives etc., priced at
  checkout), and **Intelligent Eyewear** (pre-launch, sign-up only).
- *No `partial` rows* — Warby's shown frame price genuinely is the all-in for that frame (insurance/FSA only lowers it).

**Prominence (calibrated).**
- **Eyeglasses + the $95 price are the lead [HIGH]** — "Premium eyewear, starting at $95" rides the top bar and the
  first nav slot; $95 repeats across the homepage and every PDP.
- **Sunglasses are co-headlined [HIGH]** — the homepage hero is "The sunglasses of the season" (Boaz), and Sunglasses
  is nav slot 2.
- **Contacts are promo-pushed [MED]** — "25% off your first contacts order" sits in the top bar; nav slot 3.
- **Eye exams + Insurance are foregrounded as a funnel [MED]** — a "Four ways to use your vision benefits" homepage
  module and dedicated nav/booking entries.
- **Intelligent Eyewear is seeded, not sold [MED→LOW]** — own nav + footer entry, but pre-launch (email sign-up only).

## Roster

Complete at the level Warby **indexes** (its lines + pricing tiers + the flagships it foregrounds), **not** the SKU.
The three exemplar frames are the ones with captured hero renders. Prices quoted verbatim from the captures; `—` marks
a family/umbrella row. `What` leads with a plain descriptor (no telehealth `molecule·form·access` — this is eyewear).

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What |
|---|---|---|---|---|---|---|
| **Eyeglasses** | family | — | `/eyeglasses` | — | — | In-house-designed prescription frames — the catalog core (hundreds of styles × colors). |
| **$95 frames** | buyable | `/eyeglasses` | `/eyeglasses?prices=95` | "Starting at **$95**, including prescription lenses" | published | The default tier: most house frames. Single-vision Rx + polycarbonate lenses + AR & scratch-resistant coatings included (see Deep block). |
| **Premium frames** | buyable | `/eyeglasses` | `/eyeglasses` | **$145** | published | Higher-tier styles (e.g. Melva) — same bundle, dearer frame. |
| **Durand** *(exemplar)* | buyable | `/eyeglasses` | `/eyeglasses/durand/whiskey-tortoise` | **$95** | published | Flagship round-square acetate; 4.5★ (326). Hero render captured. |
| **Percey** *(exemplar)* | buyable | `/eyeglasses` | `/eyeglasses/percey/chestnut-crystal` | **$95** | published | Iconic keyhole round; 4.5★ (307). Hero render captured. |
| **Sunglasses** | family | — | `/sunglasses` | — | — | Same frame catalog with tinted / prescription lenses; from **$95**. |
| **Boaz** *(exemplar)* | buyable | `/sunglasses` | `/sunglasses/boaz/jet-black` | **$95** | published | Homepage hero "sunglasses of the season." Hero render captured. |
| **Lens upgrades** | family | `/eyeglasses` | `/eyeglasses/lenses` | — | — | Treatments layered on any frame above single-vision. |
| **Progressives** | buyable | `/eyeglasses/lenses` | `/eyeglasses/progressives` | (priced at checkout) | on-request | "Turn any pair into a progressives pair." |
| **Blue-light / Light-responsive / Anti-fatigue** | buyable | `/eyeglasses/lenses` | `/eyeglasses/lenses` | (priced at checkout) | on-request | Optional lens treatments (`/eyeglasses/blue-light`, `/light-responsive`, `/anti-fatigue-lenses`). |
| **Contacts** | family | — | `/contacts` | — | — | **Resold** third-party brands — Acuvue, Air Optix, Biofinity, Biotrue, Dailies, Clariti, MyDay, Precision7, Avaira, Total30… Per-box price behind brand/Rx selection. |
| **Scout by Warby Parker** | buyable | `/contacts` | `/contacts/scout/scout-90-pack-1000020` | (per-box; not shown on category page) | on-request | Warby's **own** daily-disposable contact, sold in 90-packs (the low-cost end of the "$400–$1,000/yr" daily range). |
| **Eye exams** | buyable | — | `/appointments/eye-exams/booking` | (behind booking; "Save **$40** on average") | on-request | Comprehensive in-store optometry "at most of our stores." |
| **Accessories** | family | — | `/accessories` | (not captured) | on-request | Cases, chains, clip-ons, lens kits (line noted; not enumerated). |
| **Intelligent Eyewear** | buyable | — | `/intelligent-eyewear` | (no price — pre-launch) | on-request | AI smart glasses built with Google (AI) + Samsung (hardware); "launching this fall." Email sign-up only. |

### Verbatim anchors

The footnotes the Price/visibility column points at, quoted exactly from the captures:

- **The $95 anchor (`/eyeglasses`):** "Starting at $95, including prescription lenses with scratch-resistant,
  anti-reflective coatings. After choosing your eyeglasses, pick from a variety of prescription types and lens options
  to meet your vision needs. Each pair of eyeglasses also ships free!"
- **Contacts cost framing (`/contacts`, Warby's own buying guide, NOT a SKU price):** "plan on spending roughly
  **$400–$1,000 per year**" for daily disposables ("You can keep to the lower end… [with] Scout by Warby Parker in
  90-packs"); "Biweekly contact lenses might run you **$150–$600** annually, and monthly contacts, around **$200–$600**."
- **Insurance savings + contacts credit (`/insurance`):** "Save **$100** on average" (glasses), "Save **$115** on
  average" (contacts), "Save **$40** on average" (eye exams); "if you buy a year's supply, we'll give you a **$50**
  credit for new prescription glasses!"
- **Bundle (PDP "Everything included for $95"):** "Single-vision prescriptions · Polycarbonate lenses ·
  Anti-reflective and scratch-resistant lens coatings · Free scratched lens replacement · FSA, HSA, and insurance accepted."

No molecule audit applies — this is eyewear, so the telehealth `molecule · form · access` lead is dropped from `What`
(the seven spine columns are unchanged, so `offeringscheck.py` holds).

## Deep blocks

One earned — the **$95 bundle**, because the roster's `published` tokens can't carry *what is and isn't* in the
headline price, and "lenses included" is the whole Warby pitch:

**What "$95, lenses included" actually includes.** Verbatim from the flagship PDPs ("Everything included for $95"):
*"Single-vision prescriptions · Polycarbonate lenses · Anti-reflective and scratch-resistant lens coatings · Free
scratched lens replacement · FSA, HSA, and insurance accepted."* So at $95 a single-vision wearer pays nothing extra
for the lens, the standard coatings, or a scratch replacement — the upcharges are the *frame* ($145 premium styles) and
*lens upgrades* (progressives, light-responsive, blue-light, high-index, etc.), priced at checkout. This is why every
house frame is `published` (the shown number is self-contained for a single-vision Rx) while the lens-upgrade rows are
`on-request`.

**Hero renders (opt-in design-reference assets).** Clean isolated frame renders for the three exemplars, cropped from
the PDP full-page screenshots (the CDN render URLs were lazy-load blanks / color swatches):
- **Durand — Whiskey Tortoise:** `captures/2026-06-04/images/durand-whiskey-tortoise.png` (3/4 angle, "WARBY PARKER" on temple)
- **Percey — Chestnut Crystal:** `captures/2026-06-04/images/percey-chestnut-crystal.png`
- **Boaz — Jet Black (sunglasses):** `captures/2026-06-04/images/boaz-jet-black.png`

No per-SKU deep-dives earned beyond these — a Catalog company's roster carries the shape, and a per-frame quota would
manufacture padding. No PDP-template anatomy block (not requested this run); the raw PDPs sit in `captures/`.

## Provenance

- **Pages read:** `/eyeglasses`, `/sunglasses`, `/contacts` (category backbones, captured rich for the prominence read),
  `/insurance`, homepage, and the 3 flagship PDPs (`/eyeglasses/durand/whiskey-tortoise`,
  `/eyeglasses/percey/chestnut-crystal`, `/sunglasses/boaz/jet-black`) — all in `store/warbyparker-com/captures/2026-06-04/`.
  Every `$` in this file greps to one of them.
- **Scope:** enumerated — the lines, the price tiers, the flagship exemplars, Scout, the lens-upgrade options, eye
  exams, and Intelligent Eyewear. **Noted but NOT enumerated (by design — Catalog):** the hundreds of individual frame
  styles/colors under `/eyeglasses` & `/sunglasses`, the full third-party contacts brand list, and the accessories line.
- **Gated/unreachable:** per-box contacts prices (brand/Rx selection), the eye-exam fee (booking flow), and lens-upgrade
  prices (checkout) — all `on-request`.
- **Snapshot caveat:** pricing/IA is point-in-time — promos run ("25% off first contacts," "buy one save 20%"), and the
  homepage merchandising rotates; the $95/$145 frame anchors are the stable part.
- **Run profile:** non-vanilla — **Catalog-shape offerings** (shape + exemplars, not SKUs) **with hero product images**
  (3 flagship renders, cropped from PDP screenshots since the CDN renders were uncapturable). Standard 7-column spine +
  closed visibility set retained, so `offeringscheck.py` holds. First non-telehealth + first Catalog `offerings.md` of
  this shape in the store.
