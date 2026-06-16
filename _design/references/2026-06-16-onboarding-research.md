# OSS onboarding research — findings & best practices

Context: research pass (2026-06-16) on making web-research friendly for **both new humans and new AI agents** as it goes fully public OSS. 32 sources, 25 claims adversarially verified, 23 survived. Raw report was in ephemeral `/tmp`; this file preserves the verified findings + citations for the redesign. Confidence tags reflect evidence strength, not vibes.

## The core thesis

**Humans and agents are two different onboarding jobs — solve them with two barely-overlapping layers.**

- **Humans** need to *get it fast*: a 30-second "what is this / why not just use the generic tool," then a quick first win. Hook first, depth on demand.
- **Agents** need the *opposite*: a short list of exact commands, nothing else. The more you write for an agent, the worse it follows you (it's "too obedient" and drowns in noise).

Don't duplicate human prose into agent files. Agent files should *point to* human docs, not copy them.

---

## Verified findings (act on these)

### 1. Agent files: less is more — strongest finding in the report `[HIGH]`
ETH study (arXiv 2602.11988, Feb 2026; measured on real bug-fix tasks across 12 repos) found bloated agent-context files *reduce* task success and add >20% inference cost. The one category that reliably helps: **concrete, non-obvious, repo-specific tooling commands.** A named tool (`uv`) was invoked ~160× more often when the file mentioned it.
- **→ web-research:** `AGENTS.md` should be exact commands only — how to run a capture, query the store, run the linters/tests, the pyenv `env: bash` gotcha. **Not** the farm analogy, not a restatement of the README.
- Caveat: this evidence is for agent *task completion* on existing repos, not human onboarding. Do **not** apply "ruthlessly prune" to the human README/CONTRIBUTING — those want progressive disclosure, not aggressive cutting.

### 2. AGENTS.md is the real cross-tool standard `[HIGH]`
Released by OpenAI Aug 2025 (collaborative — Sourcegraph's Amp team authored), now stewarded by the Linux Foundation's Agentic AI Foundation; 60k+ repos; native support in Cursor, Copilot, Codex, Gemini CLI, Devin, Windsurf, VS Code, Zed.
- **→ web-research:** Adopt `AGENTS.md` as the primary "README-for-robots." (`CLAUDE.md` stays as the Claude-Code-specific file.)
- Calibration: "de facto standard" is partly promoter framing — an independent academic study (arXiv 2511.12884) declines to call it a standard, citing fragmentation. But "broadly adopted cross-tool convention" is solid.

### 3. CLAUDE.md: keep it thin, push domain knowledge into Skills `[HIGH]`
Anthropic's official docs: `./CLAUDE.md` (committed, team) loads at the start of *every* conversation, so bloat actively degrades adherence — "Bloated CLAUDE.md files cause Claude to ignore your actual instructions." Rule: for each line ask "would removing this cause mistakes?" If not, cut. Put sometimes-relevant knowledge in Skills (`SKILL.md`), loaded on demand.
- **→ web-research:** The thin `CLAUDE.md` + rich `SKILL.md` split this repo already uses *is* Anthropic's recommended structure. Keep it; don't fatten CLAUDE.md.

### 4. Skip llms.txt `[HIGH on what it is; efficacy weak]`
A `/llms.txt` markdown file (H1 name → blockquote summary → H2 link sections) gives LLMs curated entry points at inference time. Well-specified, but adoption/payoff is contested: one analysis of ~137K sites found 97% of llms.txt files were never read; Google reportedly rejected it. Aimed at hosted docs *sites*, not code repos.
- **→ web-research:** Skip it. `AGENTS.md` + `CLAUDE.md` carry the agent load.

### 5. Zero-to-first-success: linear setup ending in a concrete success signal `[HIGH]`
Canonical exemplar: Google's Gemini API quickstart README — a numbered `## Setup` sequence (install → clone → venv → `pip install -r requirements.txt` → `cp .env.example .env` → add key → `flask run`) ending in an exact success signal ("…at http://localhost:5000!"). Secrets handled by a committed `.env.example` you copy and fill — never make the user author config from scratch.
- **→ web-research:** No app to run, so the quickstart's terminal state is *"run `/research-company stripe.com`, watch a cited dossier appear."* (`.env.example` already added — good.)

### 6. Demo media for a no-GUI tool: charmbracelet/vhs `[HIGH]`
Write the terminal recording *as code* — a `.tape` script (`Type`, `Enter`, `Sleep`, `Set`, `Output`) renders to GIF/MP4/WebM. Version-controllable and reproducible, so it doesn't rot like a one-off screen capture. A CLI's demo *is* its terminal output.
- **→ web-research:** A ~15s GIF of one slash-command producing a cited dossier = the hero visual. Highest-leverage "make it look compelling" move. Alternatives: asciinema (raw casts), terminalizer — but VHS's as-code model wins for staying current.

### 7. Badges: assessment-signal only, not decoration `[HIGH, but correlational + 8 yrs old]`
Peer-reviewed (ICSE 2018, ~295K npm repos): badges that *run a real analysis* (build status, test coverage, dependency freshness) empirically correlate with quality. Static/lookup badges are "cheap to produce, therefore easy to fake" — clutter. Caveat: badges *signal* quality, they don't *cause* it, and the effect can decay.
- **→ web-research:** A couple of honest CI/coverage badges > a wall of shields. (Needs CI to exist first.)

### 8. Custom Open Graph / social-preview image `[HIGH]`
GitHub auto-generates a generic OG card until you upload one (Settings → Social preview). Produce it by rendering an HTML/CSS template and screenshotting with a headless browser (Puppeteer/Playwright) or `vercel/og`.
- **→ web-research:** A one-line value-prop card on a branded background. Prime real estate to land a non-obvious pitch.

### 9. Community-health files: 3 auto-detected locations `[HIGH]`
GitHub surfaces `CONTRIBUTING` / `CODE_OF_CONDUCT` / `SECURITY` / `SUPPORT` / `FUNDING` from the repo root, `.github/`, **or** `docs/`. Exception: issue templates **must** live in `.github/ISSUE_TEMPLATE/`.
- **→ web-research:** Put the set in `.github/` to keep root uncluttered.
- Note: the attempt to enumerate an "exact canonical finite set" of health files was *refuted* — don't treat any single checklist as authoritative; only the three-locations rule is solid.

### 10. Information architecture: route by need, not by file tree (Diátaxis) `[HIGH]`
Diátaxis (diataxis.fr; used by Django, Canonical, Cloudflare): four needs → four doc types — tutorials (*learn*), how-to guides (*do*), reference (*information*), explanation (*understand*). Organize around the reader's need, not your internal taxonomy.
- **→ web-research:** README becomes a hub routing by intent — *learn* (quickstart) / *do* (skill playbooks) / *reference* (SCHEMA) / *understand* (design docs). Wrap the existing rich docs in a "start here" router; don't physically reshuffle every file. Caveat: Diátaxis itself warns against forcing rigid one-doc-one-mode buckets.

### 11. The farm analogy is a legitimate cognitive aid `[HIGH on mechanism; single older source + consensus]`
Metaphor transfers structure from a familiar domain to an unfamiliar one, letting readers build a correct new mental model. But the risk is symmetric: vague, implicit, or *mixed* metaphors actively mislead.
- **→ web-research:** Keep the farm analogy, but keep it explicit and bounded — map it cleanly (farm = cited store that persists/compounds; foraging = generic search that discards each run). Don't let it sprawl into mixed metaphors.

---

## Honest gaps (not verified this run — "not found," not "no best practice")

The verifier capped at 25 claims; these fell below the line and need judgment or a follow-up pass:
- **README section-ordering specifics + named exemplar READMEs** — raw blog sources exist (awesome-readme, freecodecamp guide); fill from established practice, flag as medium-confidence.
- **Launch playbook** (Show HN / Reddit / Product Hunt / awesome-lists) + **discoverability/SEO** (name, description, topics/tags) — genuinely uncertain for a niche dev-tool. Defer until actually launching.
- **Docs-site threshold** — when GitHub Pages / Docusaurus / mkdocs beats in-repo markdown (likely overkill here, since markdown *is* the product).
- **License choice** — not verified; Apache-2.0 already chosen (good for adoption + patent grant).

## Two claims that were refuted (don't repeat them)
1. "AGENTS.md *reduces* agent success" — the blunt version was killed; the nuanced "minimal + tooling-focused helps" survived.
2. "GitHub has a defined finite set of community-health files" — the set is less crisply bounded than asserted.

---

## Suggested redesign order (for the other agent)

| Tier | What | Status / note |
|---|---|---|
| **0 — Unblock** | `LICENSE`, `requirements.txt`, `.env.example`, `.python-version` | ✅ done 2026-06-16 |
| **1 — Human on-ramp** | README rewrite: 30-sec pitch + bounded farm analogy + golden-path quickstart ending in a real cited dossier; VHS demo GIF | the main event |
| **2 — Agent layer** | minimal, commands-only `AGENTS.md` (finding #1) | keep CLAUDE.md thin |
| **3 — Polish + launch infra** | OG social card, `.github/` health files, Diátaxis README routing, honest CI badges | needs CI for badges |
| **4 — Launch** | discoverability + launch playbook | research gap — revisit at launch |

## Sources (verified findings)
- Agent files / minimalism: arXiv 2602.11988 (ETH SRI Lab, Feb 2026); arXiv 2511.12884
- AGENTS.md standard: linuxfoundation.org press release (Dec 9, 2025)
- CLAUDE.md: code.claude.com/docs/en/best-practices + /memory
- llms.txt: llmstxt.org
- Onboarding/quickstart: github.com/google-gemini/gemini-api-quickstart
- Demo media: github.com/charmbracelet/vhs
- Badges: cmustrudel.github.io/papers/icse18badges.pdf (ICSE 2018)
- OG images: github.blog/open-source/git/framework-building-open-graph-images
- Community-health files: docs.github.com (.../creating-a-default-community-health-file)
- IA: diataxis.fr
- Metaphor: journals.openedition.org/asp/4136
