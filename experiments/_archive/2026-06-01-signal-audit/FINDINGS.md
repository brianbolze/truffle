# Underused capture payload — signal audit

**$0 experiment** over 43 homepage rich-pass payloads + 304 total page payloads across the 44-company store (`store/*/captures/*/.payloads/`). No Firecrawl calls. Repro: [`audit.py`](audit.py) → [`probe2.py`](probe2.py) → [`probe3.py`](probe3.py), raw output in [`_out/`](_out/).

Question: per format (`html`, `rawHtml`, `links`, `images`, `branding`, `metadata`), what **unique** signal does it add *beyond* markdown + screenshot — and is it worth a routine enrichment read?

---

## The answer in one screen

**One payload is badly underused (`rawHtml`'s JSON-LD), two are dead weight for enrichment (`html`, `links`), the rest are roughly scoped right.** And the whole "Capture quality" backlog cluster collapses: nav, logos, and this audit are all *one* change — **read `rawHtml`'s structured layer (JSON-LD + `<header>`)** — not five.

| Format | Verdict | Unique signal beyond md+screenshot | Where it helps |
|---|---|---|---|
| **`rawHtml`** | **KEEP — and start reading it** | **JSON-LD schema.org graph** (32/43 homepages): legalName, alternateName, foundingDate, founders, HQ, contact, `medicalSpecialty`, self-reported `AggregateRating`. + `<header>`/`<nav>` flyout structure. + hreflang geo footprint. Already the framework SoT. | identity (`aliases`, `name`, canonical), Credibility (ratings, verbatim+flagged), **Nav structure**, proposed `specialties` |
| **`metadata`** | **KEEP (already used)** | Mostly already-read (verify: `sourceURL`/`statusCode`/`creditsUsed`; visual: `favicon`). New: **`price`/`priceCurrency`/`eligibleQuantity`** flattened from Product/Offer microdata on pricing pages. | verify (current), logo set (favicon/og:image), **pricing recovery on /pricing pages**, `og:site_name` name canon |
| **`branding`** | **KEEP as-is (hint-to-verify)** | exact hex + exact font-family names (unreadable off a screenshot) + inline logo SVG (`images.logo`). | `brand_colors`, `fonts`, `logo_url` — **status quo is correct** |
| **`images`** | **KEEP narrowly — reshape logo item** | The **partner/customer logo wall** (Microsoft, Slack, Brex, Linear…) — credibility proof that markdown flattens to nothing. *Not* a reliable source for the company's **own** logo. | Credibility (logo wall), SVG *fallback* for logo set |
| **`html`** | **CUT from routine read** (keep persisting — free) | None that reproduced. The "recovers JS-garbled prices" rationale is **0/43** in this corpus; both apparent hits were animation artifacts. | break-glass only, when markdown is visibly broken on a specific value |
| **`links`** | **CUT from routine read** (keep persisting — free) | Near-redundant with markdown anchors; its one niche (client-rendered sites) yields content noise (Airbnb `/rooms/*`), not IA, and it's flat — can't carry nav hierarchy anyway. | nothing routine; nav is `rawHtml`'s job, not this |

"Keep persisting" everywhere — they ride the single homepage credit (the all-formats rule), so cutting capture saves nothing. The verdicts are about what **enrichment should read**, not what to scrape.

---

## The headline: `rawHtml`'s JSON-LD is verified, verbatim, company-authored identity data we throw away

32/43 homepages (74%) ship a `<script type="application/ld+json">` block; 26 carry an Organization-family entity (`Organization` ×24, `Corporation`, `MedicalOrganization`), 4 a `SoftwareApplication`, 3 an `AggregateRating`. What's in them — and **verified absent from both `markdown` and the flattened `metadata`** ([`probe3.py`](probe3.py)):

- **honehealth** → `legalName: "Time Therapeutics, Inc."`, `medicalSpecialty: [Endocrinology, Menopause, Andrology]`, `foundingDate: 2021`, clean logo URL. *(Profile today has none of these — `grep "Time Therapeutics"` → NONE.)*
- **hims** → `alternateName: ["for hims","forhims","hims & hers"]`, `founders: [Andrew Dudum, Jack Abraham]`, `foundingDate: 2017`. *(Profile `aliases:` today = just `[www.hims.com]` — the real alias "hims & hers" was on offer and missed.)*
- **marekhealth** → `legalName: "Marek Health LLC"`, full HQ `PostalAddress` (Pontiac MI 48342), phone.
- **clari** → `applicationCategory` = their own 15-item category taxonomy, `AggregateRating: 9.2 / 5602 reviews`.
- **datadog** → `foundingDate: 2010-10-27`, `info@datadoghq.com`, `+1-866-…`.
- **usertesting** → `AggregateRating: 4.25 / 1034`, logo as clean `.svg`.

This is the strongest "leaving signal on the table" evidence in the audit: it's **machine-authored by the company** (high trust), **verbatim** (survives the grep rule), durable **state** (not events/judgments — clears the engine-owns-state line), and it traces to the capture (it's on the page). It maps directly onto existing/proposed schema surface: `aliases` ← `alternateName`; name canon ← `legalName`/`name`; Credibility ← `AggregateRating` (the SCHEMA already says capture self-reported proof **verbatim + flagged**); proposed `specialties` ← `medicalSpecialty`/`applicationCategory`.

**Caveat (same discipline as `branding`):** self-authored ⇒ seed-to-verify, never blind-trust. It can be marketing-shaped (hims folds in the combined "hims & hers" brand), stale, or absent (11/43 have none), and `@type` varies. Treat it like the branding payload: a hint Opus confirms against the page, not a source of truth.

### Update — probe 4 (the enrichment-delta check, [`probe4_jsonld.py`](probe4_jsonld.py))

Ran the actual delta on 6 profiles. It **tempers this headline**: the recently re-enriched profiles *already* capture most identity basics (founders, HQ, description, parent) from the about page, so JSON-LD's marginal value there is **confirmation + structuring, not new facts**. What's genuinely net-new and JSON-LD-only:

- **`sameAs` social/Wikipedia URLs — 0/6 profiles have a socials field; all 6 JSON-LDs carry them.** The standout; ties to the discoverability item's `linkedin`/`x`/`wikipedia` external-links hook.
- **Self-reported `AggregateRating`** — clari `9.2 (5602)`, usertesting `4.25 (1034)`, both verified absent → clean Credibility fill (verbatim + flagged).
- **Verbatim `legalName` / exact `foundingDate` / `medicalSpecialty`** where prose enrichment skipped or fuzzed them — honehealth `Time Therapeutics, Inc.` + `[Endocrinology, Menopause, Andrology]` confirmed absent (exact grep).

Correction to the examples above: hims' "hims & hers" *is* captured — in `parent:` and prose — but the queryable **`aliases:` field is just `[www.hims.com]`**, so JSON-LD's `alternateName` would still populate the structured field. Net: the case for reading JSON-LD is **reliability + queryable structure + socials/ratings**, less "buried facts" than the headline implied.

Implementation note: `<header>` extracts cleanly 4/6, hims needs a `<nav>` fallback, **marek has neither** (nav in a div) — so the nav-slice selector isn't just `<header>`; fall back to `<nav>`/`role=banner`, and validate against the screenshot (as the nav item already says).

---

## Per-format detail

### `rawHtml` — KEEP, and it's the underused one
Beyond the framework read (already in SCHEMA) and the JSON-LD above, two more lower-value but real slices:
- **`<header>`/`<nav>` flyout structure** — `aria-controls` / `aria-haspopup` counts track real mega-nav depth (twilio 51 `aria-controls`, cloudflare 26, upwork 25, apple 23). Markdown flattens these; this is exactly the **nav-structure** item below.
- **hreflang alternates** — invisible in markdown, a clean read on geo/market footprint (Uber 173 locales, Apple 136, Stripe 87 vs Datadog 4, Gong 3). Minor, but free and unique. `canonical` present 43/43 (identity/dedup).
- **Cost:** median 27× markdown bytes. Don't dump the whole thing into context — the read is *targeted*: extract the `ld+json` blocks + the `<header>` region, not the 2 MB blob.

### `metadata` — KEEP (already read); one new use
Already load-bearing for verify (`sourceURL`, `statusCode`, `creditsUsed`, body-md5 inputs) and the favicon fallback. The long tail (300+ distinct keys: analytics buckets, CMS constants, site-verification tokens, Sentry traces) is **noise — don't mine it.** The one genuinely new find: Firecrawl flattens **Product/Offer microdata** into `metadata` on commerce/pricing pages — `cloudflare/plans` came back with a full `price[]` × `eligibleQuantity[]` table ("$0.30", "100k/day"…), `cartier` product pages with `priceCurrency` arrays. That's a real **pricing-recovery surface on exactly the pages where pricing hides** (and the Cloudflare/Datadog map-noise item flags pricing pages as hard to reach). `generator` (CMS self-report) exists but is weak (9/43) and `rawHtml` is already the framework SoT — skip it.

### `branding` — KEEP exactly as scoped today
SCHEMA already nails this: hint-to-verify for `brand_colors`/`fonts`/`color_scheme`/`logo_url`. Unique-beyond-screenshot slice is real and narrow: **exact hex values + exact font-family names** (you cannot reliably read "Söhne" off a screenshot) + the **inline logo SVG** in `branding.images.logo` (Stripe/Upwork/Apple all ship their wordmark as a usable data-URI SVG here). The `personality` field is shallow LLM boilerplate — nearly every company is `{tone: professional, energy: medium}` — low value; SCHEMA correctly relegates it to a `brand.md` seed. `typography.fontSizes` is unreliable (rolex "h2: 99px"); `confidence` is 0 on some (honehealth, mylifeforce). No change warranted.

### `images` — KEEP narrowly; this reshapes the logo item
A substring scan for "logo" in `images[]` mostly returns the **partner/customer logo wall**, not the company's own mark: delighted → Google/Slack/Squarespace; upwork → Microsoft/Airbnb/BambooHR; granola → Replit/PostHog/Brex/Linear; apple → product promo logos. That's a **credibility signal** (who they integrate with / who their customers are) that markdown drops entirely because logos are images. For the company's **own** logo, `images[]` is unreliable — the clean sources are JSON-LD `logo`, `og:image`, `branding.images.logo`, and `metadata.favicon`. SVG harvest from `images[]` is a *fallback*, not the primary.

### `html` — CUT from routine enrichment
The rationale on record (playbook §3: "linear's `$` prices were scrambler artifacts in markdown, clean in html") **did not reproduce in this corpus.** Across 43 homepages the price-divergence scan found 2 candidates, and [`probe3.py`](probe3.py) shows both are noise, not recovery:
- functionhealth `$42`/`$499` → `data-oldval` attributes (the counter's *pre-animation* value); the real prices `$365`/`$1/day` are correctly in markdown.
- honehealth `$164056755` → concatenated animated-counter digit columns.

So `html` (median 9× markdown) is a **break-glass tool for the occasional scrambled page, not a routine signal source.** Keep capturing it (free, write-once, replay-able); consult it only when markdown is visibly broken on a specific value.

### `links` — CUT from routine enrichment
`md-link` paths ≥ `links[]` paths on most sites — markdown's own link syntax already carries the anchors. Where `links[]` adds entries (JS-rendered sites: Airbnb +96, Audemars +10) the surplus is **content noise** (Airbnb `/rooms/<id>` listings), not IA. And `links[]` is a flat list — it carries no hierarchy, so it can't reconstruct nav even where it has the anchors. The nav fix belongs to `rawHtml`'s `<header>` region, not here.

---

## Downstream backlog items this resolves or reshapes

This audit was meant to make three other "Capture quality" items informed instead of blind. It does — and it **consolidates them into one enrichment change**:

- **"Nav-structure capture is lossy" → RESOLVED (direction confirmed).** The audit confirms the backlog's own hypothesis — read `rawHtml`'s `<header>`/`<nav>` region incl. `aria-controls` flyout targets — and **rules out the `links` alternative** (flat + redundant + noisy). This stops being a separate item: it's one slice of "read `rawHtml`'s structured layer." Still validate completeness against the homepage screenshot (ground truth), per the item.
- **"Multi-ratio logo set" → RESHAPED.** Redirect the primary sources from "cleanest SVG from `images[]`" to **JSON-LD `logo` + `og:image` + `branding.images.logo` + `metadata.favicon`** (cleaner, higher-trust, multi-ratio by construction: favicon=square, og:image=rectangle, JSON-LD/branding=mark). `images[]` becomes the SVG *fallback* and the source for the separate partner-wall credibility read.
- **"Light cleaning pass on payload markdown" → UNBLOCKED, scope held to markdown.** This audit confirms enrichment should read `markdown` (+ the targeted `rawHtml` slices), *not* `html`/`links` — so the cleaning pass stays **markdown-only**; `html`/`links` don't need cleaning because they shouldn't be routinely read. Bonus: the `data-oldval` / concatenated-counter noise that fooled the html scan is the same animated-counter family the cleaning item already targets in markdown — consistent signal.
- **Bonus — proposed `specialties` field.** JSON-LD `medicalSpecialty` (honehealth) and `applicationCategory` (clari) are literal, verbatim feedstock for the proposed `specialties` field — capture it for free if/when that field lands.

**Net consolidation:** the codified follow-up is essentially **one** thing — *teach enrichment to read `rawHtml`'s JSON-LD + `<header>` region* (Opus reads it directly; no reducer/Haiku/Pydantic — borrow Doro's insight, not its machinery) — plus two small source-list tweaks (logo sources; pricing-page `metadata.price`). Not five parallel efforts.

---

## Scope — what this session did NOT do

Findings only, per the brief. **No** edit to `SCHEMA.md` / `TAXONOMIES.md` / the capture playbook, and **no** new enrichment step codified — that's the gated next step (and a parallel session may be touching the playbook). The concrete next move, when it's taken up: a `rawHtml`-read probe that extracts JSON-LD + `<header>` on a handful of profiles and shows the enrichment delta (e.g. honehealth gains `legalName` + specialties; hims gains the real alias), before any contract change.
