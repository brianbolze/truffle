"""md — the dossier-markdown subset → HTML.

Why a subset and not a markdown engine: dossiers are written to SCHEMA conventions
(bold-led bullets, visibility tokens, confidence tags, anchor residue), so the renderer
understands those idioms natively and stays honest about everything else.
"""

from __future__ import annotations

import html as html_mod
import re

# ---------------------------------------------------------------- markdown (subset)

def esc(s: str) -> str:
    return html_mod.escape(str(s), quote=False)


def md_inline(s: str) -> str:
    s = esc(s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\s*\[anchor:[^\]]*\]", "", s)
    s = re.sub(r"\[(HIGH|MED|LOW)([^\]]*)\]",
               lambda m: f'<span class="conf conf-{m.group(1).lower()}">{m.group(1)}{esc(m.group(2))}</span>', s)

    def code(m: re.Match) -> str:
        c = m.group(1)
        vis = re.fullmatch(r"\[?\s*(published|partial|on-request)\s*\]?", c.strip())
        if vis:
            return f'<span class="vis vis-{vis.group(1)}">{vis.group(1)}</span>'
        return f"<code>{c}</code>"
    s = re.sub(r"`([^`]+)`", code, s)
    s = re.sub(r"\*\*\*([^*]+)\*\*\*", r"<strong><em>\1</em></strong>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w_])_([^_\n]+)_(?![\w_])", r"<em>\1</em>", s)
    return s


def _parse_table(lines: list[str]) -> tuple[list[str], list[list[str]]]:
    def cells(row: str) -> list[str]:
        return [c.strip() for c in row.strip().strip("|").split("|")]
    header = cells(lines[0])
    body = [cells(r) for r in lines[2:] if r.strip().startswith("|")]
    return header, body


def md_blocks(md: str) -> str:
    """The dossier's markdown subset → HTML: paragraphs, lists, tables, fences, quotes, h3/h4."""
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("```"):
            j = i + 1
            buf = []
            while j < len(lines) and not lines[j].startswith("```"):
                buf.append(lines[j])
                j += 1
            out.append("<pre>" + esc("\n".join(buf)) + "</pre>")
            i = j + 1
            continue
        if line.startswith("#"):
            out.append(f'<h4 class="subhead">{md_inline(line.lstrip("# "))}</h4>')
            i += 1
            continue
        if line.strip().startswith("|"):
            j = i
            buf = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                buf.append(lines[j])
                j += 1
            if len(buf) >= 2:
                header, body = _parse_table(buf)
                th = "".join(f"<th>{md_inline(h)}</th>" for h in header)
                trs = "".join("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in r) + "</tr>" for r in body)
                out.append(f'<div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')
            i = j
            continue
        if line.strip().startswith(">"):
            j = i
            buf = []
            while j < len(lines) and lines[j].strip().startswith(">"):
                buf.append(lines[j].strip().lstrip("> "))
                j += 1
            out.append("<blockquote>" + "<br>".join(md_inline(b) for b in buf) + "</blockquote>")
            i = j
            continue
        if re.match(r"^\s*-\s+", line):
            j = i
            items: list[tuple[int, str]] = []
            while j < len(lines) and (re.match(r"^\s*-\s+", lines[j]) or (lines[j].startswith("  ") and lines[j].strip() and items)):
                m = re.match(r"^(\s*)-\s+(.*)$", lines[j])
                if m:
                    items.append((len(m.group(1)), m.group(2)))
                else:
                    items[-1] = (items[-1][0], items[-1][1] + " " + lines[j].strip())
                j += 1
            out.append(_render_list(items))
            i = j
            continue
        j = i
        buf = []
        while j < len(lines) and lines[j].strip() and not re.match(r"^(\s*-\s+|#|```|\||>)", lines[j]):
            buf.append(lines[j].strip())
            j += 1
        para = md_inline(" ".join(buf))
        cls = ' class="callout"' if re.match(r"<strong>(Shape finding|Prominence)", para) else ""
        out.append(f"<p{cls}>{para}</p>")
        i = j
    return "\n".join(out)


def _render_list(items: list[tuple[int, str]]) -> str:
    out = ["<ul>"]
    prev = items[0][0] if items else 0
    base = prev
    for indent, text in items:
        if indent > prev:
            out.append("<ul>")
        elif indent < prev:
            out.append("</li></ul>" * max(1, (prev - indent) // 2))
            out.append("</li>")
        elif out[-1] != "<ul>":
            out.append("</li>")
        body = md_inline(text)
        cls = ' class="def"' if re.match(r"<strong>[^<]+:</strong>", body) else ""
        out.append(f"<li{cls}>{body}")
        prev = indent
    out.append("</li>" + "</ul>" * (1 + max(0, (prev - base) // 2)))
    return "".join(out)


def _truncate(s: str, n: int = 130) -> str:
    s = s.strip()
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0]
    return cut.rstrip(" ·,;") + " …"


def _peek(md: str, n: int = 120) -> str:
    """First plain-prose line of a section, stripped of markdown — the closed-state teaser."""
    for line in md.split("\n"):
        t = line.strip()
        if not t or t.startswith(("#", "```", "|", ">")):
            continue
        t = re.sub(r"\[anchor:[^\]]*\]", "", t)
        t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
        t = re.sub(r"[*_`]", "", t)
        if t.startswith("- "):
            t = t[2:]
        return esc(_truncate(t, n))
    return ""
