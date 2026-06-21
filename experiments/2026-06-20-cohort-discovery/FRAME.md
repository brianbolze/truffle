# Frame: cohort discovery

## 30-second skim / Problem statement

Truffle keys on **one company at a time**. We can profile a brand deeply, but we have no
way to answer the prior question: **"who is even in this market?"** Today a cohort gets
assembled by hand — a person guesses the brands, captures them one by one, and hopes the
list is complete. It usually isn't.

**The problem:** given a plain-language market — *"menopause telehealth / compounded-Rx
D2C brands"* — reliably identify the **top-K most relevant and formidable companies in it**,
store-first, so we know which ones we already have and which net-new ones are worth adding.

A cohort is only as trustworthy as its membership. **If we can't name the field, every
cross-field answer is quietly bounded by what we happened to capture.**

## Why this matters — the strategy ladder

This is the build-out of one named roadmap row, and the unlock for three more.

- **Discovery tools** *(Coverage · Planned)* — the row this *is*: "scripts, recipes, and/or
  skills to discover companies not yet in the store." [↗](https://app.notion.com/p/58c416b2bd5049dc9d540c4e1e1062e8)
- **Automatic store expansion** *(Coverage · Considering)* — discovery is its prerequisite: you
  can't auto-add the right companies on a budget until you can *rank* who's worth adding. [↗](https://app.notion.com/p/38284b6d1f49805887b8c43fe5a16c88)
- **Category / Cohort "profiles"** *(Depth · Considering)* — "to really understand a company you
  need its neighborhood." A profile needs a *complete* membership first. [↗](https://app.notion.com/p/38384b6d1f498024a436d9597ce20382)
- **Category / cohort monitoring** *(Freshness · Considering)* — you can only watch a cohort
  over time once its boundary is drawn and maintained. [↗](https://app.notion.com/p/38384b6d1f4980778905f2833b830239)

**Value-prop tie:** the system Frame's bet is *capture once, read back forever*, and its
litmus is *"materially better than generic Claude + web search for a cold start."* The job
this serves is **"Compare a whole field at once"** (Beekeeper-Brian; *Synthesis · Coverage*) —
a complete, cited field, "without hand-collating tabs." That job is bounded *before any query
runs* by who's in the store. Cohort discovery is how the field gets complete.
[System Frame ↗](https://app.notion.com/p/38284b6d1f4980ec8a4ed45dcdbe30d7) · [Value & JtbD ↗](https://app.notion.com/p/8f94edca56cd4d95822089e488a1d00c)

## What makes it hard

- **Discovery is open-ended.** No fixed list to check against — you don't know what you don't
  know, and "did we find them all?" has no clean stopping signal.
- **"Formidable" is a judgment, not a field.** Relevance and strength (scale, traction, brand,
  funding, breadth) are read-time calls, and *most relevant* can pull against *most formidable*.
- **The field is noisy.** Payers, pharmacies, retailers, content sites, defunct brands, and
  adjacent-but-different businesses all masquerade as cohort members. Junk in the roster is
  worse than a short roster.
- **Same company, many faces.** One brand can wear two domains; a parent can span several. Our
  domain key can't see that — and the anti-Doro line forbids heavy entity-resolution to fix it.
- **It costs real money and time.** Searching, verifying, and (optionally) capturing all spend.
  A discovery pass has to be worth more than it costs.

## Long-term / capability goal

A reusable, **generic** `cohort-discovery` verb: feed it any market description, get back a
ranked, cited candidate roster (in-store vs net-new) — and, on request, fill the cohort by
capturing the top net-new brands. It becomes the front door to *automatic store expansion*
and the membership layer under *cohort profiles* and *monitoring*. Menopause telehealth is
just the validation cohort; the verb must not be vertical-bound.

## Primary use cases

- **Fill out a cohort** — go from a half-captured market to a complete, ranked one (the live
  need: the menopause segment the store under-resolves).
- **Cold-start a market** — point at a category we've never touched and get the formidable set
  to seed it.
- **Feed the capture queue** — hand a prioritized "what to research next" worklist to a human
  or to the auto-expansion routine (propose-first).

## Non-goals

- **Not** a market graph, a relations engine, or minted category/cohort objects in the store.
- **Not** entity-resolution machinery (the anti-Doro line holds).
- **Not** the monitoring or profile layers themselves — discovery is upstream of both.
- **Not** the production verb yet — this experiment chooses the *recipe*; graduation is later
  and human-gated.

## Constraints & principles

- **Anti-heavy / file-first.** No graph DB, embeddings, served API, or standing service.
  Conventions over infrastructure.
- **Generic, not project-bound.** The vertical is an input; the engine owns no taxonomy.
- **Spend is bounded and visible.** Discovery is light; capture spends Firecrawl and is an
  explicit, budgeted step — propose before it writes.
- **The litmus governs.** If a pass isn't materially better than a human with Claude + web
  search, it isn't worth maintaining.

## Rough scoping

- **Must** — given a market, return a verified, ranked roster (relevant + formidable),
  store-first, separating in-store from net-new. Validate on menopause telehealth.
- **Should** — keep cost honest; show it generalizes beyond telehealth.
- **Could** — auto-capture the top net-new brands to fill the cohort end-to-end.
- **Cut / later** — graduating a production verb; auto-expansion scheduling; cohort
  profiles & monitoring.

## Related references

- This experiment's method + results: [`README.md`](README.md) · [`FINDINGS.md`](FINDINGS.md).
- Upstream demand: the Market Read Lab's repeatedly-confirmed *selection-bias* blind spot —
  the store can't see a market it never captured (MRL-001 / MRL-013, menopause worklist).
- Strategy: [System Frame](https://app.notion.com/p/38284b6d1f4980ec8a4ed45dcdbe30d7) ·
  [Value & JtbD](https://app.notion.com/p/8f94edca56cd4d95822089e488a1d00c) ·
  [Roadmap DB](https://app.notion.com/p/2362eca6edf441c18aaa7c0105c4cc23).
