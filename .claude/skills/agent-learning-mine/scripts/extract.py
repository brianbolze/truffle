#!/usr/bin/env python3
"""Distill this project's Claude Code transcripts into small, mineable digests.

Step 1 of the /agent-learning-mine skill — the deterministic half. It turns the
raw session transcripts (an undocumented Claude Code internal: ~/.claude/projects/
<slug>/*.jsonl, often 1+ GB) into one small markdown digest per session, holding
the high-signal parts a human/AI judge needs: the verbatim human turns (where
corrections, redirects, and /overwhelmed firings live) plus a coarse friction-flag
on assistant text. The judging — deciding what is a real observation — is the
skill's job, not this script's. This file proposes nothing and writes no observation.

FENCED: the transcript format is not a supported API. If it drifts (we parse files
but find zero human turns), we fail loud rather than emit empty digests.

Usage: python3 extract.py [--since YYYY-MM-DD] [--out DIR] [--exclude SESSION_ID ...] [PROJECT_DIR]
Digests are SCRATCH (they contain transcript content) — written outside the repo; never commit them.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import tempfile

# --- coarse friction flashlight (NOT a rule) -------------------------------
# Only decides which assistant lines *surface* to the judge; the judge + the
# no-fix observation contract are the real gates, so a miss here costs recall,
# never correctness. Tune freely; keep it small.
LEX = re.compile(
    r"\b(surpris|unexpected|turns out|i was wrong|i assumed|"
    r"didn'?t realize|mislead|misled|brittle|confusing|silently|"
    r"i wish|would be nice|no way to|inflat|double[- ]count|"
    r"stale|drift|overstated|footgun|by hand again|toil)\b",
    re.I,
)


def project_dir_from_cwd() -> str:
    """Claude Code stores a project's transcripts under ~/.claude/projects/<slug>,
    where <slug> is the cwd with every non-alphanumeric char turned into '-'."""
    slug = re.sub(r"[^A-Za-z0-9]", "-", os.getcwd())
    return os.path.join(os.path.expanduser("~/.claude/projects"), slug)


def human_text(content: object) -> str:
    return content.strip() if isinstance(content, str) else ""


def is_plumbing(text: str) -> bool:
    s = text.lstrip()
    return (
        s.startswith("<command-name>")
        or s.startswith("<local-command")
        or s.startswith("Caveat:")
        or s.startswith("<system-reminder>")
        or s.startswith("[Request interrupted")
        or s.startswith("<task-notification>")
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("project_dir", nargs="?", default=None, help="transcript dir (default: derived from cwd)")
    ap.add_argument("--since", help="only sessions on/after this YYYY-MM-DD")
    ap.add_argument("--out", help="digest output dir (default: a fresh temp dir)")
    ap.add_argument("--exclude", action="append", default=[], help="session id(s) to skip, e.g. the current session")
    args = ap.parse_args()

    proj = args.project_dir or project_dir_from_cwd()
    if not os.path.isdir(proj):
        sys.exit(f"FAIL: transcript dir not found: {proj}\n(This tool reads a local Claude Code internal; a cloud clone won't have it.)")
    out = args.out or tempfile.mkdtemp(prefix="learning-mine-")
    os.makedirs(out, exist_ok=True)
    exclude = set(args.exclude)

    files = sorted(glob.glob(os.path.join(proj, "*.jsonl")))
    rows, total_humans, scanned = [], 0, 0
    for fp in files:
        sid = os.path.splitext(os.path.basename(fp))[0]
        if sid in exclude:
            continue
        title = branch = first_ts = last_ts = None
        humans, hits, overwhelmed = [], [], 0
        try:
            with open(fp, encoding="utf-8", errors="replace") as transcript:
                for line in transcript:
                    try:
                        d = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    t = d.get("type")
                    if t == "ai-title":
                        title = d.get("aiTitle") or title
                        continue
                    if d.get("isSidechain"):  # subagent transcript noise
                        continue
                    ts = d.get("timestamp")
                    if ts:
                        first_ts = first_ts or ts
                        last_ts = ts
                    msg = d.get("message")
                    if not isinstance(msg, dict):
                        continue
                    branch = d.get("gitBranch") or branch
                    if t == "user":
                        txt = human_text(msg.get("content"))
                        if txt and not is_plumbing(txt):
                            humans.append((ts, txt))
                            if "/overwhelmed" in txt or "<command-message>overwhelmed" in txt:
                                overwhelmed += 1
                    elif t == "assistant":
                        c = msg.get("content")
                        if isinstance(c, list):
                            for b in c:
                                if isinstance(b, dict) and b.get("type") == "text":
                                    tx = b.get("text", "")
                                    if LEX.search(tx):
                                        hits.append(tx.strip())
        except OSError:
            continue
        scanned += 1
        if not humans:
            continue
        date = (first_ts or "")[:10]
        if args.since and date and date < args.since:
            continue
        total_humans += len(humans)
        rows.append(
            dict(
                sid=sid,
                title=title,
                branch=branch,
                date=date,
                last=(last_ts or "")[:10],
                humans=humans,
                hits=hits,
                overwhelmed=overwhelmed,
                kb=os.path.getsize(fp) // 1024,
            )
        )

    # FENCE: parsed files but found no human turns anywhere → format likely drifted.
    if scanned and total_humans == 0:
        sys.exit(
            "FAIL: scanned transcripts but found zero human turns — the JSONL "
            "format may have changed. Stopping rather than emitting empty digests."
        )

    rows.sort(key=lambda r: r["date"] or "")
    for r in rows:
        L = [
            f"# {r['title'] or '(untitled)'}",
            f"session: {r['sid']}  |  date: {r['date']}→{r['last']}  |  branch: {r['branch']}  "
            f"|  human_turns: {len(r['humans'])}  |  overwhelmed_firings: {r['overwhelmed']}  "
            f"|  friction_flags: {len(r['hits'])}  |  ~{r['kb']}KB",
            "",
            "## Human turns (verbatim, ordered)",
            "",
        ]
        for i, (ts, txt) in enumerate(r["humans"], 1):
            snip = txt if len(txt) <= 1200 else txt[:1200] + " …[truncated]"
            L += [f"**H{i} [{(ts or '')[:16]}]:** {snip}", ""]
        if r["hits"]:
            L += ["## Assistant lines that tripped the friction flashlight (coarse — judge them)", ""]
            for h in r["hits"][:12]:
                snip = h if len(h) <= 600 else h[:600] + " …"
                L.append(f"- {snip.replace(chr(10), ' ')}")
            L.append("")
        with open(os.path.join(out, f"{r['date']}_{r['sid'][:8]}.md"), "w", encoding="utf-8") as digest:
            digest.write("\n".join(L))

    idx = [
        f"# Session digest index ({len(rows)} sessions" + (f", since {args.since}" if args.since else "") + ")\n",
        "date · human_turns · overwhelmed · friction_flags · KB · title\n",
    ]
    for r in rows:
        idx.append(
            f"- `{r['date']}` · {r['sid'][:8]} · {len(r['humans'])}t · "
            f"{r['overwhelmed']}o · {len(r['hits'])}f · {r['kb']}KB · "
            f"{(r['title'] or '(untitled)')[:80]}"
        )
    with open(os.path.join(out, "INDEX.md"), "w", encoding="utf-8") as index:
        index.write("\n".join(idx))

    print(f"digests: {out}")
    print(f"sessions_distilled: {len(rows)}  (scanned {scanned} transcripts)")
    print(f"total_human_turns: {total_humans}  overwhelmed_firings: {sum(r['overwhelmed'] for r in rows)}")
    if rows:
        print(f"date_range: {rows[0]['date']} .. {rows[-1]['date']}")
    print("NOTE: digests contain transcript content — scratch only, do not commit.")


if __name__ == "__main__":
    main()
