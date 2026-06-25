# Writing Guidelines

Works at two zoom levels — a **quick skim** and a **drill**. The skim must stand on its own.

## Patterns

- **Open with the frame.** Goal, clearly articulated + plain english problem statement, or locating sentence as the first line. No *"this doc covers…"* preamble.
- **Consider your audience.** Is this doc for an agent -> see `.claude/docs/effective-prompts.md`  Is it for a human? Consider using `/humanize-comms`. Always ask yourself - would a _fresh_ reader understand every sentence quickly?
- **Distill your key points**: What are the ~1-3 things you want the reader to walk away thinking/understanding? Can we ladder the other details up to those?
- **Vary length. Blank lines are fine.** Uniform bullets get skipped wholesale. A one-liner next to a paragraph is a *feature*.
- **Bold sparingly — it's the skim layer.** Lead clause of weighted bullets, the one phrase that matters. If everything's bold, nothing is.
- **Keep tables narrow.** General rule of thumb — 3–5 columns. Wider → split, or convert to a list.

### For Markdown:
- **YAML Frontmatter** (for Markdown artifacts): Often helpful to have a few structured fields at the very top of the file, like created & last_updated (as YYYY-MM-DD HH:MM), authors (agent, brian, both), etc.

### For Markdown + Notion
- **Use progressive disclosure.** Key point at the top; detail hidden or below. Mix freely with plain bullets — use a plain bullet when nothing's worth hiding. `<detail>` blocks (for Markdown) or `<toggle>` blocks (for Notion), or child / sub-pages that you link out to can be helpful for this.
- **Callouts are load-bearing.** Callouts for goals, warnings, *Read Next* — not decoration. If you need section sub-headlines / descriptions, often good to *italicize*.

## Prefer vs. Avoid

| **PREFER**                      | **AVOID**               |
|---------------------------------|-------------------------|
| Bolded lead + short prose       | Wall of paragraphs      |
| Collapsible sections for depth  | Everything at top level |
| Varied bullet length            | Uniform bullets         |
| Narrow tables                   | 7+ column tables        |
| Color that encodes an axis      | Decorative color        |
| Direct voice                    | Hedged, anodyne prose   |

## Anti-patterns

- **Same density everywhere.** Eye has nowhere to land.
- **No hierarchy on a long page.** Almost certainly wrong — depth should be navigable.
- **Sources at full weight.** Move to smaller links, footnotes, or the bottom of the page.
- **Discussion leakage.** Don't let specific quotes / details from a thread drift into a deliverable intended to outlive the session.