# Market Read

## Question

If an agent is delegated a concrete buyer-facing brief — **compare the captured
compounded-GLP-1 telehealth brands across four ingredient *types*: entry price, offer /
continuity structure, trust / proof claims, and geographic availability**, restricted to
store-only cited evidence — what fraction of that brief is answerable with decision-grade
cited ingredients, and which ingredient *types* force the agent to flag "not captured" or
invent?

Mode: **calibration / system-test, store-only.** The deliverable is a typed grounding map
of the store as an agent substrate — where delegation is safe vs where it forces invention
— not a buyer's-guide ranking. Panel: 8 well-captured DTC weight-loss brands (henrymeds,
hims, ro, joinfound/Found, lifemd, ivimhealth, hellowisp/Wisp, remedymeds), purposively
selected from the ~57 store profiles that mention GLP-1/semaglutide. This is a **panel, not
a census** (L004).

## Result

**Grounding is ingredient-type-shaped, not brand-shaped. The store is a strong agent
substrate for two of the four types (offer structure, advertised entry price), a
*conditionally* safe one for proof (it grounds what the brand *claims*, faithfully flagged
as self-reported — safe only if the agent preserves that label), and a systematically weak
one for state-level availability (the agent is forced to abstain or invent for most
brands). The frontier is a source-scope boundary — what the marketing site exposes — not a
schema defect.**

The four ingredient types, strongest to weakest grounding:

**(1) Offer / continuity structure — decision-grade-cited, 8/8 (strongest).** Every panel
brand's revenue/commitment shape is captured legibly: membership-separate-from-medication
(hims: $39 first month → $149/mo, billed separately from the drug — `hims:18,78`),
all-in-bundle-no-separate-fee (henrymeds `:72`; remedymeds folds membership into a $299
sema / $399 tirz all-in `:120`), low-membership-front-door (lifemd $19/mo flagship →
$75 program `:78,85`; ivim ~$75/mo `:38`), and insurance-layered (joinfound $149/insured
vs $199/cash, 12-mo upfront `:60`). Continuity terms (auto-renew, 12-month upfront,
multi-month early-cancel balance, 365-day money-back) live in prose. A delegated agent can
answer "how does brand X charge and lock me in" from cited State.

**(2) Entry price (advertised) — decision-grade-cited *for the advertised figure*, 7-8/8,
with a well-flagged ceiling.** Seven of eight carry SCHEMA price-visibility tokens on
offerings (`ro:68-76`, `lifemd:73-80`, `joinfound:69-76`, `hellowisp:79-83`,
`ivim:69-75`, `remedymeds:59-62`, `henrymeds:65-70`); hims states floors in prose. But the
captured number is almost always a *"starting at" floor or membership fee* — the full
out-the-door / per-dose / all-in price is **intake-gated** across the board, and the store
says so honestly (henrymeds `unverified_fields:31`; joinfound `:35-36`; hims `:18`
"gated behind the per-condition intake quiz"). Pricing is also layered/insurance-dependent
(joinfound, lifemd) and promo-volatile (lifemd $39 vs $75 A/B `:77`; ro runs its own A/B
engine `:18,146`). So the agent can ground "advertised entry price" with a citation, but
**not** "what will I actually pay all-in" — and the store's own caveats make that boundary
legible rather than hidden (L005 working).

**(3) Trust / proof claims — split grade; grounds *the claim*, not *the truth*.** Two
sub-types behave differently:
- *Legitimacy / trust badges + ratings* (LegitScript, HIPAA, BBB, embedded Trustpilot
  score): captured 8/8 — but **self-reported / self-embedded**, and flagged as such
  (henrymeds 4.4 self-reported `:104`; remedymeds 4.7 badge-image `:106`; hellowisp 4.3/4
  widget `:140`). Per L003 the review *bodies* behind the score are uncaptured, so the
  agent gets a number, not the objection cluster.
- *Clinical / efficacy proof*: present at decision grade **only where the brand publishes
  it** — ivimhealth is the outlier (two peer-reviewed Obesity Pillars studies, n=1,131 +
  1,166, verbatim 27%/22% TBWL, flagged not-RCT — `:119`); hims cites NEJM + Lancet and a
  named clinical bench (`:118,120`); ro claims "100s of published studies" + triple-board
  CMO (`:136`); lifemd attributes 15-20% to third-party "clinical studies," not its own
  outcomes (`:130`). henrymeds, remedymeds, hellowisp, joinfound offer **no** independent
  efficacy proof — only "Proven" marketing, named care teams, or batch-quality testing
  (remedymeds "four independent tests" `:112`).

  The store faithfully captures presence/absence and labels self-reported status. The
  **risk** is not absence — it is *relay*: a delegated agent that surfaces a captured
  self-reported claim (remedymeds "250,000+ members," internally inconsistent across pages
  `:108,139`; ivim "470K+ patients" `:118`; "27% TBWL") *without* carrying its
  self-reported flag launders marketing into apparent fact. The flag is the guardrail; it
  lives in prose, so its protection depends on the agent reading and preserving it.

**(4) Geographic availability — systematically invention-forcing (weakest).** The *binary*
"broadly available / all-50 claim" is captured for some (hims 400+ providers all 50
`:116`; lifemd all 50 `:127`; hellowisp all 50 `:119`). But the buyer's real question —
**"can I get this in MY state?"** — is mostly **not** answerable: henrymeds explicitly
doesn't enumerate states (`unverified_fields:33`, KYZATREX not in CA); joinfound's
~40-state list is behind a gated picker (CA "No plans available" `:36`); remedymeds "states
served… not on captured pages" (`:27,127`); ivimhealth surfaces no availability line at
all. The one strong exception proves the rule: hellowisp's `/provider-credentials` page
lists per-state license numbers and names the 8 states requiring video visits (AR, DC, DE,
KS, MS, RI, VT, WV — `:93,137`). For ~6/8 the agent must abstain or invent — and crucially
this is an **intake-gating** boundary (the data isn't on the marketing site), so even a
refresh capture wouldn't recover it without entering the funnel. Per L004/L005, "not
captured" is **not** "not available."

**Bottom line for the delegation job:** of the four ingredient types, an agent can safely
ground **two** (offer, advertised price) outright, a **third** (proof) only if it preserves
the store's self-reported labels, and is **forced to abstain** on the **fourth** (state
availability) for most of the panel. The store earns the "make AI safe to delegate to" job
on structural facts and loses it on per-jurisdiction and independent-efficacy facts — both
because those live off the marketing site, not because the schema can't hold them.

## Gap Map

- **Answered cleanly (store-only):** per-brand offer/continuity structure and advertised
  entry price, each cited to frontmatter + body with the intake-gated ceiling flagged;
  *which* brands publish independent efficacy proof vs only marketing; the presence and
  self-reported status of trust badges/ratings.
- **Fell short (source-scope, not schema):** (a) all-in / per-dose actual price — intake-
  gated; (b) state-level availability — intake-gated for ~6/8; (c) independent verification
  of self-reported ratings, scale, and outcome claims — the store holds the claim, not the
  audit; (d) review *bodies* behind the scores (L003).
- **What would have changed the answer:** a non-marketing source panel — intake-flow
  capture (for price + state lists), or filings/IR for audited scale (hims/lifemd are public
  cos) — would ground types (2-tail) and (4). None is a schema or field gap; all are
  capture-scope/source-family gaps, and all are spend/approval-gated.

## Evidence Used

All store-only; no external or current-event claims. Prices are captured point-in-time
snapshots (most under active promos / A-B engines per each profile's `site_notes`) and are
used as *structure* illustration, not live magnitudes.

- `C1` — panel denominator: 8 brands purposively selected from the 57 `store/*/profile.md`
  that mention GLP-1/semaglutide/tirzepatide (`grep -ril`), chosen for capture richness and
  DTC weight-loss focus. **Not** the GLP-1 universe — a panel (L004).
- Price tokens: ro `:68-76`, lifemd `:73-80`, joinfound `:69-76`, hellowisp `:79-83`,
  ivimhealth `:69-75`, remedymeds `:59-62`, henrymeds `:65-70`; hims floors in prose `:18`.
- Offer/continuity: hims `:18,78`; henrymeds `:72,76`; remedymeds `:120`; lifemd `:78,85`;
  ivim `:38`; joinfound `:60,82`.
- Proof: ivimhealth `:119`; hims `:118,120`; ro `:136`; lifemd `:130`; remedymeds
  `:106,108,112,139`; hellowisp `:137,140`; henrymeds `:104`; joinfound `:123`.
- Availability: hims `:116,120`; lifemd `:127`; hellowisp `:93,119,137`; henrymeds
  `unverified_fields:33`; joinfound `:35-36`; remedymeds `:27,127`; ivimhealth (no line).
- Contract: `SCHEMA.md` price-visibility token; `TAXONOMIES.md` business_model.

## Companies Seen

Panel (8): **henrymeds, hims, ro, joinfound (Found), lifemd, ivimhealth, hellowisp (Wisp),
remedymeds.** Cohort draw is a query-time judgment (GLP-1/semaglutide mention ∧ DTC
weight-loss focus ∧ capture richness), not a structured field — `anchor_category` /
offering prose carry it. The broader GLP-1-mentioning set is ~57 profiles; this panel is
the well-captured DTC core, deliberately bounded so each of the 4 ingredient types could be
judged per-brand without sampling the tail.

## Missing / Stale Coverage

- Prices are promo-period / A-B snapshots across the panel; fine for structure, not live
  magnitudes.
- Intake-gated facts (all-in price, per-dose price, enumerated state lists) are uncaptured
  by design — they sit behind the funnel, flagged in each profile.
- Self-reported ratings, scale, and outcome figures are captured verbatim but **not**
  independently verified; remedymeds's scale figures are internally inconsistent across its
  own pages (`:108,139`).

## Source Gaps

The two grounding shortfalls (state-level availability; independent verification of
price/scale/proof) both require a **non-marketing source family** the store does not hold:
the **intake flow** (price + state eligibility) and **filings/IR** (audited scale for the
public cos hims/lifemd). The SEC tool captures funding *existence*, not these. This is the
delegation-job analogue of run-036 G2 / run-037 Source Gaps (decision-grade economics live
off the marketing site). Spend/approval-gated; not attempted.

## Raw Learning to Preserve

See `run-notes.md` Observations: **G1** (state-level availability is the systematically
invention-forcing ingredient type — intake-gated, not a capture miss), **R1** (self-
reported proof/scale claims are captured *with* honest flags, but the flag is prose-grade —
a delegated agent that relays the claim without it launders marketing into fact;
delegation-relay grain of L002), **S1** (grounding is ingredient-*type*-shaped, not
brand-shaped — the same brand grounds strongly on offer and weakly on availability), **G2**
(the two shortfalls share one root: decision-grade facts live off the marketing site —
delegation analogue of run-036 G2 / run-037 source gap), **W1** (if anything graduates, the
lightest path is a read/relay convention — "carry the self-reported flag and the intake-
gated caveat into delegated output" — not a new field or capture mandate; "no new primitive
needed" stays live).

## External Completeness Check

Completeness is load-bearing only for the panel-denominator claim (`C1`), and that is named
as a **purposive panel, not a census** — the read makes no "these are the only / all GLP-1
brands" claim. The grounding verdicts are per-brand and per-ingredient-type, each cited; no
outside denominator is needed to support "type X grounds well / type Y forces invention,"
which is a statement about *captured evidence grain*, not market universe. Per L004, "not
captured outside this store," not "not there."

## Market Pattern

DTC GLP-1 telehealth converges on a recognizable shape the store grounds well —
async-first or intake-gated care, a membership-or-all-in cash model, compounded-plus-FDA
catalogs, and a "transparent/affordable" pitch — but the two facts a real buyer most needs
to *act* (the all-in price and "can I get it in my state") are exactly the two the category
**withholds until intake**. That is a market-structure finding, not a Truffle defect: the
store is as transparent as the marketing sites are, and honestly flags where they go dark.
For the delegation job, the lesson is that the store's grounding frontier mirrors the
*industry's* disclosure frontier — strong on structure and positioning, dark on
personalized price and eligibility.

## What Would Change This Answer

- A **real delegated consumer** who needs per-state eligibility or audited all-in price
  (not just structure) would raise whether an **intake-flow capture** source family is
  worth the spend — but that is a capture-worklist / source-panel decision, not a schema
  change, and stays gated. (W1; G1/G2.)
- If a future capture **dropped** a self-reported flag (e.g. stored "4.7 rating" without
  "self-reported"), R1 would harden from a relay-discipline observation into a provenance
  defect — the flag is currently doing real work and must travel with the claim.
- A second cohort (e.g. TRT or longevity) showing the *same* type-shaped grounding
  frontier (strong offer/price, weak availability/independent-proof) would suggest the
  pattern is telehealth-wide, not GLP-1-specific — but that is a learning-pass call, not
  this run's.
