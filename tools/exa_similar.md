# exa_similar.py — Exa /findSimilar neighbor discovery

Give it ONE anchor company (URL or domain); it asks [Exa](https://exa.ai)'s `/findSimilar` "what
pages are most similar to this one" and emits a **ranked list of neighbor companies**. Parsed JSON
to stdout — no store write, no cohort dedupe, no vertical baked in. The caller decides where it
lands and what to match.

```bash
python3 tools/exa_similar.py ro.co                                   # 10 neighbors, category=company
python3 tools/exa_similar.py https://ro.co --num-results 25
python3 tools/exa_similar.py hims.com --exclude-domains hims.ca forhims.co.uk   # mirror/i18n hygiene
python3 tools/exa_similar.py acme.com --category ""                  # drop Exa's company filter
```

Auth: `EXA_API_KEY` from the environment, falling back to a `.env` at the repo root (gitignored).

## The match-free line (what this tool refuses to do)

One anchor in, a ranked neighbor list out. Everything that makes a *discovery run* — looping over
many anchors, folding `api.`/`en.`/i18n mirrors back to an apex, deduping across anchors, scoring
multi-anchor overlap, matching neighbors against a tracked set — is the **caller's**
orchestration, not this tool's. The experiment this was distilled from baked all of it in (Notion
dedupe, a hard-coded shortlist, a B2B supply-side mission); the promote stripped it to the generic
core. Two artifacts of that line show up live and are *correct*: run `hims.com` and you'll get
`forhims.co.uk` twice (a mirror the caller folds) and — with `--category ""` — `en.wikipedia.org`
(an aggregator the caller drops). The tool hands over raw neighbors; the cleanup is downstream.

## What it does now vs. what it could grow into

**Now — `/findSimilar` only.** One anchor → ranked neighbors. That's the whole scope of *this* file.

**Sibling endpoints are their own tools** — Exa exposes more endpoints behind the same key, UA, and
HTTP shape, but each maps 1:1 to its own `source_type`, so it lives in its own `tools/<source_type>.py`
(the way `scripts/signals.py` resolves `tools/{tool}.py`), not folded in here:

| Endpoint | Tool | Status |
|---|---|---|
| `/search` | [`exa_search.py`](exa_search.py) (`tool: exa_search`) — query→companies, `type` pinned to `neural` | **shipped 2026-06-20** |
| `/contents` | (future) page text / LLM `summary` per URL — a latent enrichment | not built |

Keep the boundary deliberate: a new endpoint is a new sibling tool, **not** a second path wedged into
this file. `exa_search.py` duplicates the small Exa plumbing (UA, POST, `_domain_of`) on purpose, the
way every tool is self-contained; extract a shared `_exa.py` only if a *third* endpoint lands.

## The gotchas (most of the value)

These cost a probe or a real bug to learn. Carry them forward; don't relitigate them live.

- **User-Agent MUST be `curl/8.4.0`.** The default `urllib` UA is Cloudflare-blocked at Exa's edge —
  a ~30-min debugging trap on first deploy. (Or use `requests`, which sets a real UA.) Carried from
  agent-workflows/INVARIANTS, 2026-05-06.
- **`score` is dropped — `rank` is the signal.** Exa returns a `score` per result, but it's a
  synthetic, near-rank-derived value (originally documented as `(10 - rank) / 9`; live it reads as a
  small ~0.0–0.05 float), useless as an *absolute* relevance score. The tool emits ordinal `rank`
  only. If you ever need raw scores back, they're one field away in the response — but don't treat
  them as relevance.
- **findSimilar is ALWAYS neural — there's no mode to pin.** The auto-vs-neural flip warning from
  INVARIANTS applies to `/search`, **not** here: `costDollars` reports under `search.neural`, and the
  `type` param is *silently ignored* on findSimilar (a bogus `type:"banana"` still returns 200,
  verified 2026-06-08). So the tool sends no `type` — adding one would falsely imply it does
  something. Pin `type:"neural"` only when/if this grows into `/search`.
- **`excludeSourceDomain` is always on; mirrors still leak.** Exa drops the anchor's *exact* domain,
  but the anchor's i18n/vanity mirrors (`forhims.co.uk`, `hims.to`) are different domains and come
  back as neighbors. Pass them via `--exclude-domains`; apex-folding the rest is the caller's job.
- **findSimilar SILENTLY IGNORES its filter params when `category` is set — `excludeDomains`,
  `includeText`, `excludeText` all do nothing** (probe-confirmed 2026-06-20: two calls differing only
  in `includeText` returned byte-identical results; Exa's docs also list `excludeDomains` as
  unsupported for `category:company`/`people`). Only `excludeSourceDomain` / `numResults` / `category`
  are honored. Consequences: (1) `--exclude-domains` is now enforced **caller-side** in the tool
  (results filtered before ranking), so it works regardless of `category` — but `neighbor_count` can
  fall below `--num-results` when mirrors are removed; (2) **there is no API-side topic filter** on
  findSimilar, so its quality is anchor-name-bound (short/common brand names → name-collisions,
  link-shorteners, letter-matches, not competitors). For topic/function discovery, use Exa **`/search`**
  with a description query + `category:company` (probe-confirmed to return real companies) — that's
  the "could grow into `/search`" path below, not a findSimilar tweak. Full write-up:
  `experiments/2026-06-20-cohort-discovery/references/exa-api-capabilities-and-probes-2026-06-20.md`.
- **An empty neighbor list is data.** Exa returning zero similar pages is a real signal (obscure or
  brand-new anchor), not a failure — `neighbors: []`, `ok: true`, exit 0.
- **`category="company"` matters.** It's an Exa-native filter that keeps the list to operating
  companies; drop it (`--category ""`) and aggregators/wikipedia/news leak in (live-confirmed). The
  default is `company` because this tool *is* company discovery; override it for a wider sweep.

## Output shape

The shared **envelope** keys lead; exa_similar's payload sits beside them. The envelope is uniform
across every tool in `tools/` — see the library README's Conventions. Note: **no `parser_version`**
(Exa is a stable, documented JSON API — no version-pinned parser, so no schema-drift path), and
**`cost` is in dollars** (Exa meters `costDollars`, not credits).

```jsonc
{
  // --- shared envelope ---
  "tool": "exa_similar",
  "source": "exa.ai",                    // external system hit (via api.exa.ai/findSimilar)
  "captured_at": "2026-06-08T17:25:20Z", // this invocation's wall-clock (UTC) — NOT a source date
  "ok": true,                            // transport failures exit 2 before this; no drift path
  "input": { "anchor": "https://ro.co", "num_results": 10, "category": "company", "exclude_domains": [] },
  "schema_drift": [],                    // always [] — stable API, kept for envelope uniformity
  "cost": { "usd": 0.007 },              // Exa meters dollars (costDollars.total)
  // --- payload ---
  "neighbors": [                         // ranked by Exa similarity; [] is valid (a signal, not a bug)
    { "rank": 1, "title": "Roon", "url": "https://roon.com", "domain": "roon.com" }
  ],
  "neighbor_count": 1
}
```

`domain` is a convenience (bare host, `www.` stripped) — **not** an apex fold. Collapsing
`api.`/`en.`/i18n mirrors and deduping across anchors is the caller's discovery logic, kept out on
purpose.

## Exit codes

- `0` — clean capture (**including** an empty `neighbors` list).
- `2` — fetch error: network, auth (`401`), an Exa HTTP error, or a `200` whose body is missing
  `results` (surfaced loud rather than parsed-on).
- `3` — unused. There's no version-pinned parser to drift, so this never fires; the
  `schema_drift`→exit-3 wiring is kept only to stay uniform with the drift-prone tools.
