# Market Read

## Question

Across the captured SaaS/Technology slice (~24 companies), what is the pricing-visibility
and business-model landscape — business model, price visibility (published vs
"contact sales"/quote-gated), and entry offer — and **can the read recipes that worked on
the telehealth cohort actually run on this substrate?** (calibration + value-read)

## Result

**Two clean answers, one for the reader and one for the builder.**

**Reader (market read): the SaaS price-visibility split tracks go-to-market motion, the
same way telehealth's split tracked Rx control.** Of 24 profiled Tech companies:

- **business_model** is filled **24/24** and splits cleanly on the closed set: **~15
  Subscription, 6 Usage-based/Consumption, 2 Transactional (apple, casio), 1 Marketplace
  (upwork)** [C1]. No `Other`, no strain on the model axis (one `# STRAIN` note on waldo
  is a capture-fidelity branding note, not a model misfit — same orthogonal-layer pattern
  as run 027's S/O3).
- **Price visibility (read from prose, see builder answer):** ~**14 publish** a real
  price / rate card (cloudflare $0–$250/mo, datadog/posthog/snowflake/aws/twilio metered
  rate cards, linear $10–16/user, notion $8–10/mo, typeform $28–379/mo, airtable
  $120–150/mo, delighted $19–249/mo, openai, upwork, apple/casio retail); ~**6 are
  quote-/sales-gated** with no public price (clari "quote-priced", alpha-sense "no public
  pricing / contact us", gong "quote", qualtrics "custom/tailored per suite", usertesting
  "quote / contact us", listenlabs "no public pricing") [C2]. Most published brands still
  gate their **top tier** behind "contact sales" (cloudflare, delighted, dovetail,
  airtable, posthog Enterprise) — a `partial` shape.
- **Pattern:** the **published** cluster is product-led / self-serve (PLG) and
  infra/usage-metered; the **on-request** cluster is enterprise **sales-led** —
  revenue-intelligence (clari, gong), research/experience-management (alpha-sense,
  qualtrics, usertesting). "Can I even get a price?" answers *yes* for self-serve and
  *no* for sales-led — the SaaS analog of telehealth's published-vs-intake-gated axis.

**Builder (gap-probe): the read-recipe family is NOT telehealth-overfit — but the cheap,
structured path off it is unbackfilled.** Three distinct recipe ingredients, three
verdicts:

| Recipe ingredient | Telehealth substrate | Runs on SaaS? | Why |
|---|---|---|---|
| **Enum-grep cut** (here `business_model`) | `anchor_category`/`audience` grep | **Yes, cleanly** | `business_model` filled 24/24, closed-set, greppable. Generalizes (confirms 027 on a *read* axis, not just a classification audit). |
| **Structured price-visibility grep** (`[published\|partial\|on-request]` token; offerings.md `Visibility` col) | profile.md token + offerings.md | **No — substrate empty** | Token present in only **3/24** profiles (airtable, notion, waldo); offerings.md in only **4/24** (airtable, notion, posthog, waldo). A telehealth-style `rg '\[on-request\]'` returns near-nothing → would falsely read as "SaaS doesn't gate prices." |
| **Prose-read** (run-010 "prose-surface variant") | `site_notes` / Overview prose | **Yes** | Price-visibility signal lives in `What they offer` / Overview prose for ~all 24 (posthog "published end-to-end"; snowflake "consumption-based, per credit by edition"; clari "quote-priced"). Read-prose-then-classify, not field-lookup. |

So the engine's "universal fields + reusable cuts" claim holds for **reading**, not just
classifying — but only the **enum** and **prose** paths carry it. The **structured
price-visibility convention is universal by design** (SCHEMA 2.3 token: *"the one pricing
axis that generalizes,"* spec even uses a jeweller example [C3]) yet the token is
**populated for 3/24** of this slice (offerings.md for 4/24) — a **capture-era /
depth-backfill gap**, not a recipe or schema defect.

## Gap Map

- **Answered cleanly:** business-model landscape (greppable); price-visibility landscape
  (from prose); the recipe-generalizability verdict.
- **Fell short (and why):** no one-grep price-visibility tally — the structured token/
  offerings substrate is unpopulated, so the read had to drop to prose-reading 24
  profiles by hand. Entry-offer (free-tier vs trial vs demo) is only partially
  separable from prose (free-tier/trial mentioned for ~10; not consistently captured).
- **What would change the answer:** backfilling the SCHEMA-2.3 price-visibility token on
  the 21 token-less `What they offer` lines would convert this from a prose read into a
  one-grep structured read — and is the *intended* convention, not new schema.

## Evidence Used

- **C1 — business_model split (24/24 filled):** `grep -m1 '^business_model:'
  store/<tech>/profile.md` → 15 Subscription / 6 Usage-based / 2 Transactional / 1
  Marketplace. Store clock: profiles captured 2026-05-31 (19) and 2026-06-04…06-18 (5).
  Source grade: primary (own-site capture). Receipt: `receipts/tech-slice-fields.md`.
- **C2 — price-visibility from prose:** per-profile `What they offer` / Overview prose,
  classified published / partial / on-request (≈14 / mixed / 6). Primary (own-site).
  Receipt: `receipts/tech-slice-fields.md`.
- **C3 — universal token convention:** `SCHEMA.md:99,142,147` (price-visibility token
  `[published | partial | on-request]`, explicitly vertical-agnostic, "wraps the price").
  Token presence in slice: 3/24 (airtable, notion, waldo). offerings.md: 4/24 (airtable,
  notion, posthog, waldo) — corrected from 5/24 by Loop-2 verifier (the prior "+1" double-
  counted; stripe/clerky/airbnb carry offerings.md but are filed under Finance/Consulting/
  Hospitality, not Technology).
- No external/current/news claims; all evidence is local store State. No snippets used.

## Companies Seen

24 profiled Tech companies: airtable, alpha-sense, apple, aws-amazon, casio, clari,
cloudflare, datadoghq, delighted, dovetail, gong, granola-ai, linear-app, listenlabs-ai,
notion, openai, posthog, qualtrics, snowflake, twilio, typeform, upwork, usertesting,
waldo-fyi.

## Missing / Stale Coverage

- **Denominator is partial** (per MRL-001 run-027 directory-vs-profiled flavor): the
  count is industry-grep on `primary_industry: Technology` over `profile.md` files. It
  may miss tech-adjacent companies filed under other industries (e.g. fintech SaaS under
  Finance) and excludes capture-only stubs. Count is a **floor**, not a census.
- 19/24 captured in the 2026-05-31 batch; price points may be stale but the *visibility
  posture* (published vs quote-gated) is structurally stable.

## Source Gaps

None requiring external panels for this question — the read is store-only by design. The
only "gap" is internal: the structured price-visibility token is uncaptured for 21/24, so
the cheap query path is unavailable until backfill.

## Raw Learning to Preserve

See `run-notes.md` Discovery ledger IDs **O1, O2, O3, S1, G1, W1, F1, V-trap** for
append to `discovery-ledger.md` in Loop 2.

## External Completeness Check

Not run (store-only; completeness of the SaaS universe is not load-bearing for the
recipe-generalizability verdict — the verdict holds on the captured slice regardless of
how many SaaS companies exist outside it).

## Market Pattern

1. **Price visibility is a GTM tell.** Self-serve / product-led SaaS publishes rate
   cards (often $0 free tier → metered/per-seat); enterprise sales-led SaaS gates price
   behind "contact sales"/quote. The on-request cluster is exactly the
   revenue/experience/research-intelligence sales-led set.
2. **The "can I get a price?" axis is genuinely universal** — it separated telehealth
   (published labs vs intake-walled GLP-1) and now separates SaaS (PLG vs sales-led) on
   the same three-value scale. This is positive calibration for the SCHEMA-2.3 token's
   design intent.
3. **Usage-based is the cloud/AI-infra signature** (aws, snowflake, twilio, datadog,
   posthog, waldo) — a 6-company sub-cluster that all publish granular metered rate
   cards; "published" and "usage-based" co-occur strongly.

## What Would Change This Answer

- Backfilling the price-visibility token on the 21 token-less profiles → turns the prose
  read into a one-grep structured read (and would let a future cross-vertical price-
  visibility read run without hand-reading prose).
- A wider/cleaner denominator (tech-adjacent cos under other industries) could shift the
  published/on-request ratio but not the **recipe-generalizability verdict**, which is
  substrate-level, not count-level.
