# Writing effective instructions for Claude

*Consult when authoring or improving a prompt, task brief, CLAUDE.md, or sub-agent instruction. Condensed from Anthropic's prompting best-practices — cut to what applies to Claude Code / agent work (no API-parameter tuning).*

## Principles

**1. Be clear and direct.** Claude has no context on your norms — spell out what you want.
- *Golden rule:* show the instruction to someone with no context on the task. If they'd be confused, Claude will be too.
- Be specific about output format and constraints. Numbered steps when order or completeness matters.
- Want "above and beyond"? Ask for it explicitly — don't rely on inference.

**2. Explain the *why*.** Give the motivation behind an instruction, not just the rule — Claude generalizes from the reason and delivers more targeted output.
- *Instead of:* "Format dates as MM/DD/YYYY." *Try:* "Format dates as MM/DD/YYYY — they feed a US billing system that rejects other formats."

**3. Say what to do, not what not to do.**
- *Instead of:* "Don't use markdown." *Try:* "Write in smoothly flowing prose paragraphs."
- Match your prompt's style to the output you want — a markdown-heavy prompt produces markdown-heavy output.

**4. Give a role.** One sentence focuses tone and behavior. "You are a compliance reviewer for DTC health ads" beats a generic ask.

**5. Structure with XML tags.** Wrap distinct content types so they don't bleed together: `<instructions>`, `<context>`, `<input>`, `<example>`. Consistent, descriptive names; nest when there's a hierarchy.

**6. Examples — when they're worth it.** Powerful but expensive to hand-craft, so use them deliberately:
- **Worth it:** reusable formats (a note template, a SKU row, an ad frame) or fuzzy taste calls ("sound like *this*"). One example beats paragraphs of description.
- **Cheaper substitutes:** point at an artifact you already have ("match the format of `key-decisions.md`"); generate-then-correct (let Claude draft one, you fix it, that's your example); or skip it entirely for one-shot exploratory asks.

**7. Long inputs: data first, question last.** For large inputs (20k+ tokens), put the documents at the top and your question at the bottom — can improve answers by up to ~30%. For long-document tasks, ask Claude to quote the relevant parts before answering.

**8. Delegating to a sub-agent? Give the why + goal, not the how.** Hand it the objective, the decision it serves, and pointers to read — then trust it to find the steps. Don't micro-script or assume you know its domain better. Keep the brief short.

## Steering snippets (paste-ready)

**Keep it minimal — anti-over-engineering:**
```
Avoid over-engineering. Only make changes directly requested or clearly necessary:
- Scope: Don't add features, refactor, or make "improvements" beyond what was asked.
- Defensive coding: Don't add error handling/validation for scenarios that can't happen; only validate at system boundaries.
- Abstractions: Don't build helpers or design for hypothetical future needs. Minimum complexity for the current task.
- On edits: do a simplification pass — changes shouldn't be purely additive. Look for what to cut or consolidate, not just what to add.
```

**Take action by default** — or the inverse, hold off:
```
<default_to_action>
By default, implement changes rather than only suggesting them. If intent is unclear, infer the most useful likely action and proceed, using tools to find missing details instead of guessing.
</default_to_action>
```
```
<hold_off_until_asked>
Do not change files unless clearly instructed. When intent is ambiguous, default to research and recommendations rather than action. Only edit when explicitly requested.
</hold_off_until_asked>
```

**Don't answer from memory — investigate first:**
```
<investigate_before_answering>
Never speculate about a file you have not opened. If the user references a specific file, read it before answering. Investigate relevant files BEFORE making any claim — unless you are certain.
</investigate_before_answering>
```

**Frontend / brand visuals — avoid "AI slop":**
```
<frontend_aesthetics>
NEVER use generic AI aesthetics: overused fonts (Inter, Roboto, Arial, system fonts), cliché color schemes (especially purple gradients), predictable layouts, cookie-cutter design. Use unique fonts, cohesive color themes, and animation for micro-interactions.
</frontend_aesthetics>
```
Two things to know when generating designs:
- Claude's *default* house style is warm cream (`#F4F1EA`), serif display type, terracotta accent — great for editorial/hospitality, wrong for clinical/health/dashboard. Override with a **concrete** spec (exact palette + type), not "make it clean" — vague negatives just swap one default for another.
- Or: *"Before building, propose 4 distinct visual directions (bg hex / accent hex / typeface + one-line rationale); I'll pick one."* Breaks the default and hands you the control.

---

*Source: [Anthropic — Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). Trimmed to instruction-writing principles; API-parameter, thinking/effort, and migration sections omitted as not applicable to Claude Code usage.*
