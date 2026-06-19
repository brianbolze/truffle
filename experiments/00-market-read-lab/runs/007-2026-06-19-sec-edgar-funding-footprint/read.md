# Market Read

## Question

Among captured DTC telehealth brands, which show an SEC / Form-D funding footprint, and what
does that footprint (form type, filing date, name-match quality, existence-only flags) actually
tell you — and not tell you — about company funding/maturity?

## Direct Answer

**Of the 20 captured `sec_edgar` signals, only ~7 brand domains carry a credible SEC footprint, and
they collapse to 6 distinct legal issuers — because two brand domains share one CIK.** The captured
signal cleanly sorts brands into four buckets, and the *match quality* field is what makes it
trustworthy: half of the "hits" are name-collision noise, not funding.

| Bucket | Brands (captured) | What the SEC signal supports | Judgment |
|---|---|---|---|
| **Public issuer** (10-K/10-Q/8-K) | `hims-com` (CIK …3751); `niagenplus-com` + `truniagen-com` → **same** CIK …6570 (`registered_name` "Niagen Bioscience, Inc."; filer string "ChromaDex Corp. (CDXC)") | Periodic-reporting public company; material-filing cadence | Most mature. **3 domains = 2 issuers** — the issuer behind both Niagen brands is the public company ChromaDex Corp (ticker CDXC), now registered as Niagen Bioscience, Inc. |
| **Confirmed private Form D** | `eden-health` (3 D's, 2017→2021), `mylifeforce-com` (1 D, 2022), `agelessrx-com` (1 D, 2026), `waldo-fyi` (1 D, 2026) | An exempt private-placement *was filed* — existence only | Took outside capital at least once. Eden's 3-filing trail is the only serial-raise pattern in the cohort. |
| **Name-match only — NOT a funding signal** | `joinamble-com` (34 hits / 10 CIKs, vehicle), `maximustribe-com` (45 / 19, vehicle), `honehealth-com` (2 / 2) | Nothing. Common-word names collide with unrelated filers. | Must be read as *no usable signal*, not as funded. |
| **No SEC footprint found** | 10 brands incl. `marekhealth-com`, `trtnation-com`, `defymedical-com`, `sermorelin-com`, `getpetermd-com`, `gogeviti-com`, `joinfridays-com`, `directmeds-com`, `hydramed-com`, `struthealth-com` | Absence of a *found* Form-D / public filing under the matched name | "Not found" ≠ "never raised" — could be bootstrapped, raised without a Form D, or filed under a different legal name. |

**The load-bearing caveat:** every funding signal carries `amount: null` (Form-D events also flagged
`existence_only`; public periodic filings flagged `material_filing`). The captured signal answers
*"is there a filing footprint, and how confident is the name match?"* — it **does not** answer *how
much* was raised, *when relative to the brand*, or *from whom*.

## Evidence Used

All from captured local signal JSON (`store/<domain>/signals/sec_edgar/<latest>.json`, capture
clock 2026-06-15, waldo 2026-06-18) + `telehealth.md` frontmatter. No live SEC fetch. See
[`receipts/sec-edgar-footprint-panel.md`](receipts/sec-edgar-footprint-panel.md).

- **C1** — 20 domains captured; match split = 6 `confirmed`, 1 `no_issuer_form_d` (hims, public), 3
  `name_match_unconfirmed`, 10 `no_match`. *(derived from the 20 latest JSONs)*
- **C2** — `niagenplus-com` and `truniagen-com` both resolve to `cik: 0001386570` → **one issuer, two
  brand domains** (dedup confound). The JSON carries two names for that CIK: `state.registered_name`
  "Niagen Bioscience, Inc." (current) and the Form-D filer string "ChromaDex Corp. (CDXC)" — i.e. the
  public company ChromaDex (ticker CDXC) renamed to Niagen Bioscience; both Niagen brand domains sit under it.
- **C3** — Public issuers carry `forms:[10-K,10-Q,8-K]` + `flags:[…,material_filing]`: hims
  (CIK …3751) and Niagen Bioscience (CIK …6570). hims is `no_issuer_form_d` (public-market raiser,
  no exempt Form D), which is correct, not a gap.
- **C4** — Confirmed private Form-D issuers + dates: eden-health (2017-11-27, 2018-12-28, 2021-02-19);
  mylifeforce/"Lifeforce Digital Inc." (2022-02-17); agelessrx (2026-03-17); waldo-fyi/"Curiosities
  Inc." (2026-06-09).
- **C5** — `name_match_unconfirmed` rows have high `distinct_ciks` and `is_vehicle: true`
  (maximustribe 19 CIKs, joinamble 10 CIKs) — textbook common-name collisions, zero filings attached.
- **C6** — Every `funding_signals[]` entry has `amount: null` — **no captured SEC signal carries a
  raise amount.** The `flags` differ by event: `event_type: form_d` entries carry `existence_only`
  (Form-D filed, amount not captured); public `event_type: filing` entries (hims, Niagen) carry
  `material_filing`. So "presence, never amount" holds universally; `existence_only` specifically is
  the Form-D flag, not a flag on the public periodic filings.

## Companies Seen

20 captured `sec_edgar` domains, all `value_chain_role: DTC brand` except `waldo-fyi` (no
telehealth pack — captured as a general profile; legal name "Curiosities Inc."). By anchor category
the captured SEC slice skews **longevity/NAD** (agelessrx, gogeviti, honehealth, mylifeforce,
niagenplus, truniagen) and **TRT** (defymedical, getpetermd, marekhealth, maximustribe, trtnation),
with GLP-1 (eden, hims, directmeds, joinamble, joinfridays) and a few peptides/multi.

## Missing / Stale Coverage

- **Captured floor: 20 domains** with a `sec_edgar` signal vs 54 captured telehealth packs — the
  other ~34 telehealth brands have **no SEC signal captured at all** (not "no filing"). Any
  cohort-wide funding claim is over this ~20-brand slice only.
- Captures are 1–4 days old (2026-06-15/-18) — current.
- Public-issuer `filings` arrays cap at 10 rows → filing counts for hims/Niagen are **floors**, not totals.

## Source Gaps

- **No amount, ever.** Form D *does* disclose offering amounts in its primary doc, but the captured
  signal stores `existence_only` — so "raised $X" is unanswerable without re-fetching the filing
  body (out of scope, store-only).
- **No filing-vs-brand-age alignment.** A 2017 Eden Form D predates much of its current GLP-1 line;
  the signal dates the *entity's* raise, not the current product (same domain-history-≠-brand-history
  trap Run 006 hit with Wayback tenure).
- **Name-match is the integrity gate.** Without `form_d.match` + `distinct_ciks` + `is_vehicle`, the
  raw `total_hits` (maximustribe 45) would massively over-state footprint.

## External Completeness Check

Not run — would require live SEC/EDGAR fetching (disallowed this run). The internal `match` field is
the completeness proxy: `no_match` is an honest "no filing found under the resolved name," and the
tool already self-grades match confidence, so an external denominator isn't load-bearing for the
*shape* of the answer (only for converting "not found" → "confirmed never raised").

## Market Pattern

- **Funding footprint is thin and lumpy, not a cohort norm.** Across the captured slice, only ~6
  distinct issuers show any credible SEC trace; the rest are bootstrapped-or-invisible to EDGAR. SEC
  presence is a *minority* signal in DTC telehealth — most of these brands raise privately without a
  retrievable Form-D match, or don't raise institutionally at all.
- **Two maturity tiers are visible:** public reporters (hims; ChromaDex/Niagen Bioscience) vs single/serial
  private-placement filers (Eden's 3-filing trail being the standout). Everyone else is dark.
- **The signal's real value is the dedup + integrity layer, not a leaderboard.** Its two sharpest
  outputs are (a) *one CIK behind two brand domains* (Niagen) — a relation/entity fact a domain-keyed
  store can't see on its own — and (b) *match-quality triage* that strips 3 false-positive "funded"
  reads. A naive `total_hits` ranking would have crowned maximustribe (45 hits) #1; it has zero real filings.

## What Would Change This Answer

- **Capturing the remaining ~34 telehealth packs' SEC signal** — could surface more confirmed issuers
  and move "no footprint" brands into buckets.
- **Re-fetching Form-D primary docs** to attach offering *amounts* — would turn an existence map into
  a sizing read (needs live fetch / approval).
- **A CIK-keyed entity join** — would automatically catch the Niagen two-domains-one-issuer case (and
  any other shared-parent filers) instead of relying on a human spotting the matching CIK.
