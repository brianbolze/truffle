# web-research

**Fresh, cited company intelligence — captured once, then queried forever, by you or any agent.**

Generic AI research forages the open web — paraphrased, undated, often bot-blocked — and discards it after every question. **web-research is a farm instead:** it captures a company's real pages *once* — verbatim, cited, dated — and keeps them. So every later answer is built from fresh primary sources, not reheated scraps.

The payoff: ask *"how do a dozen telehealth brands price semaglutide?"* and get a complete, cited answer in one shot — the thing generic Claude + web search can't cheaply rebuild.

<!-- TODO: hero demo GIF — /research-company producing a cited dossier (record with VHS) -->

## What you get

- **A cited dossier per company** — what it sells, how it's priced, who's behind it, its visual identity — drawn from the company's *own* pages, every claim traceable to a captured source.
- **A queryable store** — ask across one company or a whole cohort; answers come from local files, not a fresh crawl, so they're complete and ~free to re-ask.
- **Human briefs** — render any company into a one-page HTML brief that wears its own captured brand.

## How it works

web-research is a set of **Claude Code skills** plus a **file store**. You drive it by typing slash-commands *inside Claude Code* (CLI, desktop, or IDE) — not in a plain terminal. Two verbs do most of the work:

| Command | What it does |
|---|---|
| `/research-company <domain>` | Capture a company into the store (spends a Firecrawl credit; a warm company is ~free) |
| `/query-companies <question>` | Answer from the store — cited, no re-scraping |

Captured once, a company stays warm for every future question, in any project. The only metered cost is the initial capture; reasoning rides your Claude subscription.

## Quickstart

**Setup (one-time):**

1. **Clone** this repo.
2. **Point Claude Code at it** — add to `~/.claude/settings.json`:
   ```json
   {
     "env": {
       "WEB_RESEARCH_HOME": "/absolute/path/to/Web Research",
       "FIRECRAWL_API_KEY": "fc-..."
     }
   }
   ```
   (Or `cp .env.example .env` and put the key there. Grab a key at [firecrawl.dev](https://firecrawl.dev).)
3. **Install deps:** `pip install -r requirements.txt` (Python 3.11). For the visual layer: `playwright install chromium`.
4. **Link the verbs** so Claude Code sees them:
   ```bash
   export WEB_RESEARCH_HOME="/absolute/path/to/Web Research"
   mkdir -p ~/.claude/skills
   for s in research-company query-companies deepen-offerings visual-evidence; do
     ln -s "$WEB_RESEARCH_HOME/skills/$s" ~/.claude/skills/"$s"
   done
   ```

**Your first capture:**

5. In Claude Code, type **`/research-company stripe.com`** → it maps the site, reads the key pages, and writes a cited dossier to `store/stripe-com/profile.md`.
6. Ask about it: **`/query-companies what does Stripe charge?`** → answered from the store, cited, no new web hit.
7. *(Optional)* Render a brief: `python scripts/render.py stripe.com` → `_out/briefs/stripe-com.html`.

## Find your way around

| You want to… | Start here |
|---|---|
| **Use it** — capture & query companies | the two verbs above |
| **Read the store** — query recipes | [`QUERYING.md`](QUERYING.md) |
| **Capture external signals** — SERP, funding, reviews over time | [`SIGNALS.md`](SIGNALS.md) |
| **Understand why it exists** — the design | [`_design/2026-05-29-frame.md`](_design/2026-05-29-frame.md) |
| **Build on the engine** — contracts, rules, agent routing | [`SCHEMA.md`](SCHEMA.md) · [`MAINTAINING.md`](MAINTAINING.md) · [`CLAUDE.md`](CLAUDE.md) |

*New to the vocabulary (cohort, signals, warm, module)? A short glossary is coming next.*

## Status

A working tool, used daily, now being smoothed for a handful of trusted users — open-sourcing in progress. macOS-first today (the visual layer shells out to `sips` + ImageMagick). Licensed under [Apache-2.0](LICENSE).
