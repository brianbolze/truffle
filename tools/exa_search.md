# exa_search.py — Exa /search (query → ranked companies/pages)

Give it ONE natural-language **query** (a description of what you're looking for); it asks
[Exa](https://exa.ai)'s `/search` and emits a **ranked list of results**. Parsed JSON to stdout —
no store write, no cohort dedupe, no vertical baked in. Sibling to [`exa_similar.py`](exa_similar.py)
(Exa `/findSimilar`); they share Exa's auth/UA/envelope but are separate tools because each maps 1:1
to its own `source_type` (`exa_search` vs `exa_similar`), the way `scripts/signals.py` resolves
`tools/<source_type>.py`.

```bash
python3 tools/exa_search.py "telehealth TRT & hormone optimization clinic: labs, membership" --num-results 25
python3 tools/exa_search.py "menopause / HRT telehealth brand" --category company
python3 tools/exa_search.py "..." --include-domains a.com b.com          # restrict (honored with category)
python3 tools/exa_search.py "..." --category "" --exclude-domains reddit.com   # excludeDomains only honored w/o category
```

Auth: `EXA_API_KEY` from the environment, falling back to a `.env` at the repo root (gitignored).

## When to use this vs. exa_similar.py

| You have… | Use | Why |
|---|---|---|
| a known company **URL** whose neighbors you want | `exa_similar.py` | `/findSimilar` ranks pages similar to that page |
| a **description** of what you're looking for | `exa_search.py` | `/search` matches your query against the index |

**They are not interchangeable** (probe-confirmed 2026-06-20). `/findSimilar` is anchor-**name**-bound:
short/common brand names return name-collisions, mirrors, and link-shorteners (`hims` → `bit.ly`,
"HMS Holdings"; "Honey Health" for "Hone Health"), and its `includeText`/`excludeText` are silently
ignored, so it has no topic knob. `/search` by a function/description query returns **real companies**
instead. **But `/search` is a DISCOVERY tool, not a cross-shop tool** — it surfaces a long tail of
small players and has *low recall of a curated/known set* (a Hone-description search recovered **1/16**
of run-017's known neighbor set). Treat results as net-new candidates and corroborate; for "who do
buyers cross-shop a known brand," use owned `/vs` pages + review co-shopping, not Exa. Full evidence:
`experiments/2026-06-20-cohort-discovery/references/exa-api-capabilities-and-probes-2026-06-20.md`.

## The match-free line (what this tool refuses to do)

One query in, a ranked result list out. Pooling many queries, folding `api.`/`en.`/i18n mirrors to an
apex, deduping, scoring, and matching results against a tracked cohort is the **caller's**
orchestration (`_match.py` + consumers), never this tool's. **Grain note:** `/search` output is
**query/cohort-grain** (a description, not a company), so — like a SERP panel — it is *not* a
company-keyed signal and usually lives in an experiment/cohort, not `store/<domain>/signals/`.

## Gotchas (search-specific; shared Exa gotchas live in [`exa_similar.md`](exa_similar.md))

- **`type` defaults to `neural`; never leave it `auto`.** On `/search` the mode genuinely flips
  neural↔keyword between runs, which breaks any diff/repeatability — so the tool pins `neural` and
  exposes `--type` for the rare keyword/fast case. (`/findSimilar` has no such knob — it's always
  neural.)
- **`excludeDomains` is unsupported when `category` is `company`/`people`** (Exa silently drops it,
  per its docs and confirmed on `/findSimilar`). The tool only sends `excludeDomains` to the API when
  no category is set, and **always enforces the exclude list caller-side** (results filtered before
  ranking) — so `--exclude-domains` works regardless of category, but `result_count` can fall below
  `--num-results` when hosts are removed. **`includeDomains` IS honored** with a category — use it to
  pin a curated allow-list.
- **`includeText`/`excludeText` are honored here** (unlike `/findSimilar`), sent as a one-element
  list. Exa wants a short phrase (a few words); exact limits are undocumented/contradictory as of
  2026-06-20, so don't lean on a hard cap — if Exa rejects it you'll get an exit-2 HTTP error.
- **`category="company"` keeps results to operating companies**; `--category ""` drops it and lets
  aggregators/news/wikipedia leak in (the same trade-off as `exa_similar.py`).
- **`score` is dropped; `rank` is the signal** — Exa's per-result `score` is synthetic/near-rank-derived
  (carried from the sibling tool's prior art).

## Output shape

The shared **envelope** keys lead; the payload sits beside them, uniform across `tools/` (see the
library README's Conventions). No `parser_version` (stable JSON API), and **`cost` is in dollars**
(Exa meters `costDollars`).

```jsonc
{
  "tool": "exa_search",                  // = source_type (sibling to exa_similar)
  "source": "exa.ai",                    // external system hit (via api.exa.ai/search)
  "captured_at": "2026-06-20T20:00:00Z", // this invocation's wall-clock (UTC) — NOT a source date
  "ok": true,
  "input": { "query": "...", "num_results": 25, "type": "neural", "category": "company",
             "include_domains": [], "exclude_domains": [], "include_text": null, "exclude_text": null },
  "schema_drift": [],                    // always [] — stable API, kept for envelope uniformity
  "cost": { "usd": 0.007 },
  "results": [                           // ranked by Exa; [] is valid (a signal, not a bug)
    { "rank": 1, "title": "Acme Health", "url": "https://acme.com", "domain": "acme.com" }
  ],
  "result_count": 1
}
```

## Exit codes

- `0` — clean capture (**including** an empty `results` list).
- `2` — fetch error: network, auth (`401`), an Exa HTTP error (e.g. a rejected `includeText`), or a
  `200` whose body is missing `results`.
- `3` — unused (no version-pinned parser to drift); `schema_drift` stays `[]` for envelope uniformity.
