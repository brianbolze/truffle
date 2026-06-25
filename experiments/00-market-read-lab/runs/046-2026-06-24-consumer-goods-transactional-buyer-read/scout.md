# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L001–L006 read. L005 (query-time grouping enough only when corpus carries the cut) and
  L006 (price-visibility token reports buyer-reachability, not intermediary take-rate) are
  the live conventions most relevant to a price/offer read. Observations through run 045.
- `scout-context.md`: two-test selection (value/reach + design), value jobs, design
  uncertainties, evidence-mode rules. Optimize the slate for reader value + reach +
  source-family diversity, not store-answerability.
- Last 3 `run-notes.md` files: 043 (wearable year-one cost of ownership), 044 (usage-based
  pricing comparability), 045 (agency services schema fit). Plus `question_history.py` map
  of all 045 prior selected questions.
- Current run artifacts, if resuming: none (fresh scaffold 046).

## History read — what is saturated vs under-tested

- **Saturated:** schema-edge entity-type fit (035 investors / 036 marketplaces / 037
  wearables / 042 deep-tech / 045 agencies); telehealth cohort price-visibility &
  offer-ladder (008/010/013/023); denominator-reconciliation (recurs almost everywhere);
  freshness/change-pulse just run (032/041).
- **Under-tested:** the **consumer-goods transactional slice** (only 033 watches has had a
  dedicated read); a buyer-facing **physical-retail** comparison where the purchase is a
  one-time catalog buy, not a subscription; the "compare a whole field" value job applied
  outside telehealth/SaaS.

## Candidate Questions

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| C1. For a shopper comparing premium consumer-hardware/apparel/eyewear DTC brands that sell one-time catalog products (Warby Parker, Nike, Therabody, Hyperice), how does the store represent a **transactional** purchase — catalog breadth, price visibility, offer structure — and does the telehealth-subscription-shaped State frame leave a physical-retail buyer able to comparison-shop, or blind? | value-read | yes | store-only | A real shopper comparison; the transactional consumer-goods corner is barely touched since the watch run (033). | Whether durable State built around subscription-DTC generalizes to **one-time physical-retail commerce** — does `price_visibility` / `business_model` / `offerings` carry a catalog buyer's decision? | Reaches the transactional (not subscription) commerce shape; tests whether `offerings.md` captures catalog breadth a shopper needs. | Each brand's `profile.md` + `offerings.md`; the `price_visibility` token; clean read of `business_model: Transactional`. | Concluding "store handles it" from 4 brands that all happen to publish prices — over-generalizing from an easy cohort. |
| C2. Across the captured store, for the "cold-start a single unfamiliar company" job, does a one-company profile actually stand alone as a 5-second handoff — or does a first-contact reader have to cross-read offerings/signals/visual to trust it? Calibrate on 3–4 mid-depth profiles. | calibration | yes | store-only | Tests the First-Contact persona's core value job directly; most runs are cohort reads, not single-profile depth. | Profile self-sufficiency: does one `profile.md` carry the cold-start, or is the unit of value actually the whole `store/<domain>/` folder? | Reaches profile-grain completeness vs folder-grain; a persistence/packaging-boundary question. | 3–4 profiles read end-to-end against the brief-render lens. | Grading depth as a proxy for hand-off readiness; conflating "complete" with "lands in 5s." |
| C3. For a buyer choosing recovery/percussion devices (Therabody vs Hyperice), can the store support a head-to-head on product line, price tier, and positioning wedge — a true two-brand duel? | value-read | yes | store-only | Narrow real buyer decision; tests duel-grain rather than cohort-grain. | Whether two deep profiles can be diffed into a buyer's table without a relation primitive. | Reaches two-company head-to-head readability. | Both `offerings.md` + `profile.md`. | Too narrow; n=2 may not teach a general lesson (overlaps 043's device focus). |
| C4. In the captured GLP-1 / compounded-semaglutide cohort, what do third-party best-of listicles + SERPs name as the default brands vs the store's captured set — re-run of the coverage-radar with a fresh source panel to test whether L001 still holds at a later capture date. | gap-probe | yes (bounded plan) | bounded-live | Coverage radar is a graduated lesson (L001); a re-run tests its durability. | Source-panel: does the listicle→intersection→store-diff recipe still hold months later? | Reaches the external denominator the store can't see. | SERP + ≥2 listicles, capture-dated; store token-match. | bounded-live spend block (cf. 040 → needs-human-review); broadening into a crawl. |
| C5. Across the consumer-goods + telehealth slices, does the `business_model` token cleanly separate **subscription** from **transactional** from **hybrid** revenue — or do the STRAIN-flagged hybrids (Oura, Peloton) reveal a token that collapses a buyer-relevant distinction? | calibration | yes | store-only | Tests a live SCHEMA token's expressiveness across two slices; ties to L006's token-grain family. | `business_model` token grain: does one enum value hide hybrid hardware+subscription economics a buyer must know? | Reaches token-expressiveness on hybrid revenue; cousin to L006. | `business_model` + STRAIN markers across ~10 brands. | Re-treading 037 (wearable hybrid revenue schema fit) without a new edge. |
| C6. For a returning reader, can the store tell what changed in a brand's **own** State (price/offer/positioning) since last look? | gap-probe | yes | store-only | The "trust the cache over time" job. | Append-only State-history boundary. | Reaches the un-versioned State frontier. | 2+ dated captures per domain. | Direct repeat of 041 (state-change-pulse) — just run. |

## Selected Question(s)

1. **C1** — the transactional consumer-goods read. Highest reader value (a real shopper),
   genuine reach (the physical-retail commerce shape, under-tested since 033), and a clean
   builder lens (does subscription-shaped State generalize to one-time catalog commerce).
   Store-only and autonomous-safe.

Runner-up: C2 (profile self-sufficiency calibration) — strong, but C1 has clearer reader
value and a sharper generalizability edge. C4 is the most reach-y but carries the
bounded-live spend-block risk that sent 040 to needs-human-review; held for an attended run.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: >
  For a shopper comparing premium DTC brands that sell one-time catalog products
  (Warby Parker, Nike, Therabody, Hyperice), how does the captured store represent a
  transactional purchase — catalog breadth, price visibility, and offer structure — and
  does Truffle's telehealth-subscription-shaped State frame leave a physical-retail buyer
  able to comparison-shop, or blind?
selected_slug: consumer-goods-transactional-buyer-read
run_type: mixed
question_mode: value-read
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: >
  The store's transactional / one-time physical-product brands. Seed set: warbyparker,
  nike, therabody, hyperice (all business_model: Transactional / One-time per frontmatter).
  Treat as partial; check for other Transactional brands at read time (casio, swatch are
  candidates; rolex/patek covered separately in 033's luxury read).
likely_source_panel: >
  store/<domain>/profile.md + offerings.md for the seed brands; business_model and
  price_visibility frontmatter tokens; no external sources.
builder_lens: >
  Whether durable State built around subscription-DTC telehealth generalizes to one-time
  physical-retail commerce — does the price_visibility / business_model / offerings frame
  carry a catalog buyer's decision (breadth, price, offer), or is it silent on
  retail-specific concerns (catalog depth, in-store channel, returns/warranty)?
reach_reason: >
  Reaches the transactional commerce shape rather than the subscription default the schema
  was built around; the consumer-goods slice has had no dedicated buyer read since the
  luxury-watch run (033), and that one focused on gated-vs-published luxury pricing, not
  mass/premium catalog comparison-shopping.
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/learning/"
disallowed_actions:
  - "live browsing / external search / Firecrawl"
  - "store/ mutation or write-back"
  - "durable primitive or field creation"
  - "lesson proposal or graduation"
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: >
  Answerable entirely from local store files and lab artifacts; store-only; no spend; no
  write-back; no durable-primitive creation.
loop1_failure_mode: >
  Over-generalizing from a small, convenient cohort whose members all happen to publish
  catalog prices — claiming "the frame handles transactional retail" when the sample can't
  see gated/quote-only physical-product cases. Say "not found," not "not there"; flag
  retail concerns the schema has no field for (returns, warranty, channel) as gaps, not
  proof.
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. C1 clears both tests: a downstream
shopper would recognize it (value/reach), and it probes a real generalizability frontier —
does subscription-shaped State carry a one-time-purchase buyer (design). It deliberately
avoids the saturated schema-edge "does the schema fit entity type X" framing by being a
**buyer-value read first**, with the schema-generalizability question as the builder lens
rather than the headline. Store-only keeps the autonomous cycle clean and avoids the
bounded-live spend block that sent 040 to needs-human-review.
