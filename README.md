<p align="center">
  <img src="assets/truffle.webp" alt="Truffle" width="220">
</p>

<h1 align="center">Truffle</h1>

<p align="center">
  <strong>Fresh, cited company intelligence — captured once, then queried forever, by you or any agent.</strong>
</p>

---

Generic AI research forages the open web — paraphrased, undated, often bot-blocked — and tosses the scraps the moment it answers. Truffle goes to the source instead: it takes a company's real pages whole — verbatim, cited, dated — and keeps them. Every later answer draws on the real thing, not a reheated summary.

Ask *"how do a dozen telehealth brands price semaglutide?"* and get one complete, cited answer — what generic Claude + web search can't cheaply rebuild.

## What you get

- **A cited dossier per company** — what it sells, how it's priced, who's behind it, its visual identity — drawn from the company's *own* pages, every claim traceable to a captured source.
- **A queryable store** — ask across one company or a whole cohort; answers come from local files, not a fresh crawl, so they're complete and ~free to re-ask.
- **Human briefs** — render any company into a one-page HTML brief that wears its own captured brand.

<p align="center">
  <img src="assets/ro-co-brief.webp" alt="Scrolling through Truffle's rendered brief for Ro" width="760">
  <br>
  <sub><em>A real capture, rendered — <a href="https://ro.co">ro.co</a> wearing its own brand. To explore the full interactive page, open <code>assets/ro-co.html</code> from your clone in any browser — one self-contained file, no setup.</em></sub>
</p>

<!-- TODO: capture-process demo GIF — /research-company producing a cited dossier (record with VHS) -->

## How it works

Truffle is a set of **Claude Code skills** plus a **file store**. You drive it by typing slash-commands *inside Claude Code* (CLI, desktop, or IDE) — not in a plain terminal. Two verbs do most of the work:

| Command | What it does |
|---|---|
| `/research-company <domain>` | Capture a company into the store (spends a Firecrawl credit; a warm company is ~free) |
| `/query-companies <question>` | Answer from the store — cited, no re-scraping |

Captured once, a company stays warm for every future question, in any project. The only metered cost is the initial capture; reasoning rides your Claude subscription.

## Quickstart

**Setup (one-time):**

1. **Clone** the repo:
   ```bash
   git clone https://github.com/brianbolze/truffle
   ```
2. **Point Claude Code at it** — add to `~/.claude/settings.json` (`WEB_RESEARCH_HOME` is the engine's internal name):
   ```json
   {
     "env": {
       "WEB_RESEARCH_HOME": "/absolute/path/to/truffle",
       "FIRECRAWL_API_KEY": "fc-..."
     }
   }
   ```
   (Or `cp .env.example .env` and put the key there. Grab a key at [firecrawl.dev](https://firecrawl.dev).)
3. **Install deps:** `pip install -r requirements.txt` (Python 3.11). For the visual layer: `playwright install chromium`.
4. **Link the verbs** so Claude Code sees them:
   ```bash
   export WEB_RESEARCH_HOME="/absolute/path/to/truffle"
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

---

<sub>Truffle is the brand; **web-research** is the engine's internal name — you'll see it in `WEB_RESEARCH_HOME` and across the design docs.</sub>
