# tools — shared capture utilities

> Small, generic scripts that pull signal from an external source (a SERP API, the Wayback CDX, Trustpilot, …). One home for the capture tools that were scattered across projects, so they're findable and reusable.

Early days — this dir will grow and the conventions will shift as we learn. What's below is starting intent, not a fixed spec.

## Principles (for now)

- **Generic, not project-bound.** No Notion, cohort, or vertical baked in — pass those as inputs. A tool should run from a bare shell.
- **Capture, not judgment.** Fetch, parse, emit. Classifying or synthesizing the result is the caller's job, not the tool's.
- **Print, don't write.** A tool emits JSON / "vanilla" output to stdout; the caller decides _where_ the capture lands (the store, a project overlay, wherever). To accumulate captures for the `signal_delta.py` comparator, the company-grain home is `store/<domain>/signals/<source_type>/<captured_at>.json` (the [architecture](../_design/2026-05-30-architecture.md)'s convention — a path, not a writer).
- **Keep the gotchas with the code.** The hard-won API quirks (rate limits, schema drift, auth headers) live in each tool's docstring or companion markdown doc — that's most of the value.
- **Stay small.** One source per tool; extend an existing one before adding a new one.

`tools/` is for getting external signal *in*; `scripts/` is for managing the store. Different jobs.

## What's here

Five tools live; the last two deferred on purpose — see [`BACKLOG.md`](BACKLOG.md) for why:

| Tool | Source | Auth | Status |
|---|---|---|---|
| [`serpapi.py`](serpapi.py) · [docs](serpapi.md) | Google SERP (AI Overview + organic) | `SERP_API_KEY` | **live** |
| [`wayback.py`](wayback.py) · [docs](wayback.md) | Internet Archive CDX + replay (tenure / content diff) | none | **live** |
| [`trends.py`](trends.py) · [docs](trends.md) | Google Trends (pytrends) | none | **live** |
| [`trustpilot.py`](trustpilot.py) · [docs](trustpilot.md) | Trustpilot reviews (Firecrawl-stealth) | `FIRECRAWL_API_KEY` | **live** |
| [`exa_similar.py`](exa_similar.py) · [docs](exa_similar.md) | Exa /findSimilar | `EXA_API_KEY` | **live** |
| [`ads_transparency.py`](ads_transparency.py) · [docs](ads_transparency.md) | Google Ads Transparency Center (paid-ads presence/recency) | `SERP_API_KEY` | **live** |
| `ad_library.py` | Meta Ad Library (Apify) | `APIFY_API_KEY` | deferred |
| `reddit.py` | Reddit JSON search | none | deferred |

Consumer helpers live here too when they make repeated use of captured envelopes boring without
turning into project judgment:

| Consumer | Inputs | Status |
|---|---|---|
| [`serp_match.py`](serp_match.py) | one `serpapi.py` envelope + cohort JSON | **live bridge** |
| [`serp_intent_panel.py`](serp_intent_panel.py) · [docs](serp_intent_panel.md) | query set + cohort JSON + captured `serpapi.py` envelopes | **live** |
| [`signal_delta.py`](signal_delta.py) · [docs](signal_delta.md) | two captures/runs of the same source (the comparator) | **live** |

## Conventions (the reference shape)

[`serpapi.py`](serpapi.py) + [`serpapi.md`](serpapi.md) are the worked example — copy their shape. The load-bearing rules, so tool #N doesn't reinvent them:

- **Exit codes.** `0` clean · `2` transport/auth error · `3` schema drift. Universal across the library.
- **Keys.** `from _env import load_key` → `load_key("SERP_API_KEY")`. Env first, repo-root `.env` fallback, fail loud. One strategy ([`_env.py`](_env.py)) — never re-roll it per tool.
- **Output envelope.** Print one JSON *object* to stdout (never a bare list — list-y tools hold their list in a named payload field). Reserved top-level keys, identical across every tool so a caller reads provenance + freshness the same way:
  - **required:** `tool` · `source` (the external system hit, e.g. `serpapi.com` / `web.archive.org/cdx`) · `captured_at` (UTC ISO) · `ok` (bool — did it complete cleanly) · `input` (object echoing the args) · `schema_drift` (list; non-empty ⇒ exit 3).
  - **optional:** `parser_version` (only on versionable/drift-prone upstreams — skip it on frozen feeds like CDX) · `cost` (only where the source meters credits/$).
  - then the tool's **payload as named field(s) beside** these (`organic_results`, `snapshots`, `neighbors`, `reviews`…) — never nested under a generic `payload`/`data`.
  - **`captured_at` is *this invocation's* wall-clock, not a source-reported date.** Source dates that are themselves the signal (Wayback timestamps, review dates, ad first-seen) live *inside payload items* under their own names. Conflating the two is the trap. Lock these keys; leave payload naming to each tool (a loose spine, not a frozen schema).
- **Match-free.** Capture tools emit raw signal; matching results to a cohort/brand list is a separate composable step (`_match.py` plus consumers like `serp_match.py` and `serp_intent_panel.py`), never baked into a capture tool. Keeps every capture generic — `serpapi` does this; the legacy scripts that baked matching in are what we're undoing.
- **Avoid wrapper sprawl.** `_match.py` is the shared importable matcher; don't add one `*_match.py` CLI per source. A one-off bridge can exist while a workflow proves itself, but repeated matching/orchestration should graduate to a generic recipe or batch runner outside the capture-tool surface.
- **Drift-prone upstream → fail loud.** If the source reshapes (Google AIO, Apify, Trustpilot HTML): pin a `PARSER_VERSION`, ship `validate_<x>_shape_<ver>()` returning a complaint list, route it through `schema_drift[]`, **suppress the parsed fields** (no parse-on into plausible-but-wrong output), exit 3. Stable sources (Wayback CDX) skip this — don't cargo-cult a validator onto a frozen feed.
- **CLI shape.** Single-verb → flat `main()` (serpapi). Multi-verb → subparsers + `DISPATCH = {cmd: fn}` (the `fc.py` pattern, per [`python.md`](../.claude/rules/python.md)).
- **Docstring vs companion `.md`.** Docstring = scope + exit codes + auth + terse maintainer invariants (stays with the code). `.md` = the dated gotcha catalog + output-shape example + credits + growth table. Terse-in-code, detailed-in-doc; don't repeat verbatim.
- **House style** is [`.claude/rules/python.md`](../.claude/rules/python.md): type hints everywhere, `from __future__ import annotations`, why-first docstrings, stdlib-first (earn every dep).
- **Extract a shared helper only on the second caller.** [`_env.py`](_env.py) earned its place because *every* tool loads a key. Don't pre-extract a `_firecrawl.py` / `_http.py` for a single user — inline it, lift it when the second tool needs it.

## Keys & discovery

Found via `$WEB_RESEARCH_HOME/tools/`. Keys read from a `.env` at the repo root (gitignored), via [`_env.py`](_env.py). Run any tool standalone: `python3 tools/<name>.py …`.
