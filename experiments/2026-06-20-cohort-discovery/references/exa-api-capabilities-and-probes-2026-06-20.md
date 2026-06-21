# Exa API — capabilities + probe findings (2026-06-20)

**What this is.** A dated reference on Exa's API for the cohort-discovery probe, written after
run-030 (Market Read Lab) found `exa_similar.py` returns name-collisions, not competitors. Two
sources: Exa's docs (`exa.ai/docs/reference/*`, scraped 2026-06-20) and 5 live API probes that day.
Doc facts are tagged **[doc]**; probe-confirmed facts **[probe]**. Exa ships fast — re-verify
before relying on anything here past ~Q3 2026.

## TL;DR for cohort-discovery

- **`/findSimilar` (what our `exa` technique uses) is anchor-name-bound, low precision.** It returns
  pages *semantically/name-similar to one URL* — for short/common brand names that's mirrors,
  link-shorteners, and letter-collisions, not competitors. The FINDINGS smoke-test hunch (midihealth →
  generic-health neighbors) is the rule, not bad luck. **[probe]**
- **`/findSimilar`'s filter params are silently ignored.** With `category` set, `includeText`,
  `excludeText`, and `excludeDomains` do nothing (same class as the long-known `type`-ignored gotcha).
  You cannot topic-constrain findSimilar. **[probe + doc]**
- **`/search` by *function description* + `category:company` is the usable Exa mode** — it returns
  real companies, not junk. But it surfaces a **long tail of small players** and has low recall of a
  *curated/known* brand set, so it's a **net-new discovery** input, not a "find the obvious cohort"
  tool. **[probe]**
- **Net for the bake-off:** expect `exa` (findSimilar) to lose the recall race on precision. If you
  want Exa in the field at all, run it as **`/search`-by-description**, treat its output as net-new
  candidates, and verify hard. It will not beat `websearch`/`listicle`; it may add a few long-tail
  uniques.

## Endpoints [doc]

`POST https://api.exa.ai/{search, findSimilar, contents, answer}` (confirmed in the coding-agents
guide). Relevant to discovery:

| Endpoint | Input | Use |
|---|---|---|
| `/search` | a **query string** (+ `type`, `category`, `contents`, filters) | find companies by *what they do* — the discovery workhorse |
| `/findSimilar` | **one URL** (+ filters, mostly ignored) | "pages like this page" — name/embedding similarity; weak for competitors |
| `/contents` | URLs | pull `text`/`highlights`/`summary`/`subpages`/`livecrawl` per page — enrichment/post-filter |
| `/answer` | a question | RAG-style answer; not used here |

## Parameters that matter [doc unless tagged]

- **`category`** — values seen in docs: `company`, `research paper`, `news`, `personal site`,
  `financial report`, `people`. `company` is the right filter for cohort work. **Caveat [doc, ×2 pages]:**
  with `category: company` (and `people`), Exa does **not** support `excludeDomains` or the date
  filters (`start/endPublishedDate`, `start/endCrawlDate`) — they're silently dropped.
- **`type`** (`/search` only) — `neural | keyword | auto` (and a `fast` mode referenced elsewhere).
  Pin `neural` for semantic discovery; on `/search` the auto↔neural choice genuinely changes results,
  so don't leave it to `auto` if you diff runs. On `/findSimilar`, `type` is silently ignored.
- **`includeText` / `excludeText`** — substring filters on result page text. **Limits unknown:** doc
  extraction was self-contradictory (one page "≤50 words," another "≤1200 strings") — do **not** code
  to a specific limit without a live check. **[probe]:** *ignored on `/findSimilar` when `category`
  is set* (see gotchas); behavior on `/search` not yet probed.
- **`includeDomains` / `excludeDomains`** — domain allow/deny lists. `excludeDomains` is void with
  `category:company` (above). `includeDomains` is honored.
- **`contents`** — request `text`, `highlights`, `summary`, `subpages`, `livecrawl`, `extras:[links]`
  inline. Tip [doc]: prefer `highlights`/`summary` over full `text` for precision + cost. A `summary`
  per candidate is the natural **post-filter** for "is this actually in-cohort?".
- **`numResults`** — up to 100 on `/search`. **`excludeSourceDomain`** (`/findSimilar`) — honored
  (the anchor's own exact domain is dropped) **[probe]**.
- **`score`** — synthetic, ~rank-derived; ordinal `rank` is the only trustworthy relevance signal
  (carried from our tool's prior art).

## Confirmed gotchas [probe, 2026-06-20]

1. **`/findSimilar` silently ignores `includeText`/`excludeText` (with `category`).** Probes A1 and
   A2 — identical body except `includeText=["telehealth"]` vs `["mens health treatment"]` on
   `hims.com` — returned **byte-identical** result lists, both full of `bit.ly`, `mailchi.mp`,
   `hms.com`, "HMS Holdings Corp" (an unrelated IT firm sharing the letters). No topic filtering
   occurred.
2. **`excludeDomains` is void with `category:company`** [doc, corroborated]. Our tool was passing it
   together with `category:company` → the mirror-exclusion never took effect API-side.
3. **`excludeSourceDomain` works** — `hims.com` itself was absent from its own neighbor list (only
   mirrors `forhims.com`/`hims-inc.com` leaked, which is the separate mirror-fold problem).
4. **Dropping `category` makes `includeText` bite — but floods aggregators.** Probe D (`findSimilar`
   on `honehealth.com`, no `category`, `includeText=["hormone"]`) returned hormone-themed results but
   dominated by B2B directories (`ventureradar`, `linkedin`, `cbinsights`, `leadiq`, `doccafe`). You
   trade name-collisions for directory-noise. Not a clean win.

## Probe log (anchor = our run-030 worst cases)

| # | Call | Result | Cost |
|---|---|---|---|
| A1 | `findSimilar hims.com` + `category:company` + `includeText:["telehealth"]` | name-collision junk (bit.ly, HMS Holdings…) | $0.011 |
| A2 | same, `includeText:["mens health treatment"]` | **identical to A1** → includeText ignored | $0.011 |
| B | `search` q="telehealth for men: ED/hair/testosterone/weight loss, subscription" + `type:neural` + `category:company` | **real** men's-health cos: Nu Image, **Strut Health** (in store), Revibe, Everyman, Vital Men's Health | $0.011 |
| C | `search` q=Hone's job description + `category:company`, n=25 | **real** hormone/longevity cos (trtkingdom, hormonesynergy, 1stOptimal, TruForm…) but **1/16 recall** of run-017's curated Hone DTC neighbor set; a small-clinic long tail | $0.022 |
| D | `findSimilar honehealth.com` **no category** + `includeText:["hormone"]` | hormone-themed but aggregator-dominated (ventureradar/linkedin/cbinsights/leadiq) | $0.011 |

Cost is trivial ($0.011 `/findSimilar` & small `/search`; $0.022 for n=25). Not the constraint.

## Implications for the cohort-discovery bake-off

- **Re-run `exa` as `/search`-by-description, not `/findSimilar`-from-seeds.** findSimilar from seed
  brands will reproduce the name-collision failure; `/search` with the cohort *description* +
  `category:company` is the mode that returns real companies (Probe B/C). Build the query from the
  cohort description, not the seed domains. **Now shipped as `tools/exa_search.py`** (2026-06-20) —
  `python3 tools/exa_search.py "<cohort description>" --num-results 25`.
- **Expect Exa to lose to `websearch`/`listicle` on the curated cohort but add long-tail net-new.**
  Probe C's 1/16 recall of a known set, alongside real-but-obscure clinics, says Exa's lane is
  *novelty* (small players the listicles miss), bought at low precision → it **needs the verify
  stage hard** (cf. the "payers aren't platforms" trap).
- **Use `/contents` `summary` as the verify/post-filter**, not a second discovery pass — one batched
  `/contents` call over the candidate pool to confirm in-cohort beats per-domain agents (also
  addresses FINDINGS issue #4, signal-stage cost).
- **The mirror double-count** (FINDINGS #2, `hers.com`/`forhers.com`) is the same apex-fold gap Exa
  exposes (`forhims.com` etc.) — a caller-side fold, not an Exa feature.

## Untested / open (for a future probe)

- `includeText`/`excludeText` behavior + exact limits on `/search` (only findSimilar tested).
- Whether `/search` `type:keyword` or `fast` changes the precision/long-tail mix.
- `/contents summary` schema-extraction as an automated in-cohort classifier.
- `includeDomains` to pin a known authoritative set (e.g. restrict to a curated TLD list).

## Pointers

- Run-030 read (the failure that started this): `experiments/00-market-read-lab/runs/030-2026-06-20-external-cross-shop-neighbor-map/read.md`.
- Tools: `tools/exa_similar.py` (findSimilar) + **`tools/exa_search.py`** (search — shipped 2026-06-20 from these probes); both have `.md` companions with the gotchas.
- Backlog: `BACKLOG.md` "Fix / improve Exa findSimilar tool".
