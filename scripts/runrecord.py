#!/usr/bin/env python3
"""Write per-company run records for capture verbs.

Run records answer the operational question "what produced this capture?" without
putting engine telemetry into company State. They are small JSON envelopes under
`store/<slug>/runs/<UTC-compact-Z>-<verb>.json`; see modules/RUNS.md for the contract.

CLI:
  python3 scripts/runrecord.py now
  python3 scripts/runrecord.py write --slug <slug> --verb research-company \
    --started-at <ISO-Z> --model claude-opus-4-8 --artifact profile.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

RECORD_VERSION = "0.1"
VERBS = {"research-company", "deepen-offerings", "visual-evidence"}
STATUSES = {"complete", "partial"}
TRUST = {"env", "agent"}

ROOT = Path(__file__).resolve().parents[1]
STORE = ROOT / "store"


def utc_now() -> str:
    """Current UTC instant, second precision, in the contract's ISO-Z shape."""
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_iso_z(value: str) -> dt.datetime:
    """Parse an ISO-Z instant and normalize to UTC. Raises ValueError on bad input."""
    raw = value.strip()
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    parsed = dt.datetime.fromisoformat(raw)
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include a timezone, preferably trailing Z")
    return parsed.astimezone(dt.timezone.utc).replace(microsecond=0)


def compact_stamp(value: str) -> str:
    """ISO-Z instant -> compact filename stamp, e.g. 20260617T153012Z."""
    return parse_iso_z(value).strftime("%Y%m%dT%H%M%SZ")


def normalize_tool(value: str | None) -> str | None:
    """Tool labels are query keys, so normalize common spellings to stable slugs."""
    if not value:
        return None
    token = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    if token in {"claudecode", "claude-code", "claude"}:
        return "claude-code"
    return token or None


def detect_tool(env: dict[str, str] | None = None) -> tuple[str | None, bool]:
    """(tool, env_trusted). Both Claude Code and Codex stamp deterministic env signatures."""
    e = env if env is not None else os.environ
    if e.get("CLAUDECODE") or e.get("CLAUDE_CODE_SESSION_ID"):
        return "claude-code", True
    if e.get("CODEX_SHELL") or e.get("CODEX_THREAD_ID") or e.get("__CFBundleIdentifier") == "com.openai.codex":
        return "codex", True
    if tool := normalize_tool(e.get("AI_AGENT")):
        return tool, True
    return None, False


def parse_components(raw: str | None) -> list[dict[str, str]] | None:
    """Validate the optional LLM component list. Omit when absent."""
    if raw is None:
        return None
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"--components-json is not valid JSON: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError("--components-json must be a JSON list")
    allowed = {"tool", "model", "role"}
    out: list[dict[str, str]] = []
    for i, item in enumerate(data, 1):
        if not isinstance(item, dict):
            raise ValueError(f"component {i} is not an object")
        extra = set(item) - allowed
        if extra:
            raise ValueError(f"component {i} has unsupported keys: {sorted(extra)}")
        if not item.get("tool") or not item.get("model"):
            raise ValueError(f"component {i} must include tool and model")
        out.append({k: str(v) for k, v in item.items() if v not in (None, "")})
    return out


def clean_artifacts(items: list[str]) -> list[str]:
    """Artifacts are bare, company-dir-relative markdown filenames (e.g. `profile.md`).

    Normalize to that form: a `store/<slug>/…` prefix (one agent recorded the full repo-relative
    path) is stripped to the bare filename, so the slug — already the record's location — isn't
    duplicated and the column stays joinable across runs. Empty list is valid.
    """
    out: list[str] = []
    for item in items:
        path = item.strip()
        if not path:
            continue
        if path.startswith("/") or ".." in Path(path).parts:
            raise ValueError(f"artifact must be a repo-relative path: {item!r}")
        parts = Path(path).parts
        if len(parts) >= 3 and parts[0] == "store":
            path = Path(*parts[2:]).as_posix()  # store/<slug>/profile.md -> profile.md
        if not path.endswith(".md"):
            raise ValueError(f"artifact must be a markdown file: {item!r}")
        out.append(path)
    return out


def build_record(
    *,
    verb: str,
    status: str,
    started_at: str,
    artifacts: list[str],
    model: str | None = None,
    tool: str | None = None,
    effort: str | None = None,
    trust: str | None = None,
    ended_at: str | None = None,
    components: list[dict[str, str]] | None = None,
    note: str | None = None,
    env: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Build a contract-conformant run record. The caller writes it with write_record()."""
    if verb not in VERBS:
        raise ValueError(f"verb must be one of {sorted(VERBS)}")
    if status not in STATUSES:
        raise ValueError(f"status must be one of {sorted(STATUSES)}")
    parse_iso_z(started_at)
    if ended_at:
        parse_iso_z(ended_at)

    e = env if env is not None else os.environ
    # An explicit --tool is a self-report; honor its VALUE over env detection (which can leak — a
    # Codex run inside a Claude Code shell still carries CLAUDECODE). But `trust` reflects whether the
    # environment independently CORROBORATES that value: env-detected, or an explicit tool the env
    # confirms, is "env"; an explicit tool the env can't back (Codex self-report, or a leaked override)
    # is "agent". Undetected + unnamed ⇒ never lose the record — stamp tool "unknown" / trust "agent"
    # (a hard error here made agents abandon the bookkeeping step and drop the record entirely).
    explicit_tool = normalize_tool(tool)
    env_tool, env_trusted = detect_tool(e)
    if explicit_tool:
        final_tool = explicit_tool
        default_trust = "env" if (env_trusted and env_tool == explicit_tool) else "agent"
    elif env_tool:
        final_tool, default_trust = env_tool, ("env" if env_trusted else "agent")
    else:
        final_tool, default_trust = "unknown", "agent"
    final_trust = trust or default_trust
    if final_trust not in TRUST:
        raise ValueError(f"trust must be one of {sorted(TRUST)}")

    # model: a RUNREC_MODEL env override (Brian's session declaration) is authoritative; else the
    # agent's --model (best-known); else "unknown" — never block the write on a model nobody named.
    final_model = (e.get("RUNREC_MODEL") or model or "").strip() or "unknown"
    # effort: a RUNREC_EFFORT declaration (authoritative, like RUNREC_MODEL) wins over the agent's
    # --effort guess; else Claude Code's CLAUDE_EFFORT; else omit.
    final_effort = e.get("RUNREC_EFFORT") or effort
    if final_effort is None and final_tool == "claude-code":
        final_effort = e.get("CLAUDE_EFFORT") or "unknown"

    record: dict[str, Any] = {
        "record_version": RECORD_VERSION,
        "verb": verb,
        "status": status,
        "tool": final_tool,
        "model": final_model,
        "trust": final_trust,
        "started_at": utc_now_from(started_at),
        "artifacts": clean_artifacts(artifacts),
    }
    if final_effort is not None:
        record["effort"] = final_effort.strip() or "unknown"
    if ended_at:
        record["ended_at"] = utc_now_from(ended_at)
    if components:
        record["components"] = components
    if note:
        record["note"] = note.strip()
    return record


def utc_now_from(value: str) -> str:
    """Normalize an accepted timestamp to canonical ISO-Z."""
    return parse_iso_z(value).isoformat().replace("+00:00", "Z")


def record_path(slug: str, record: dict[str, Any], root: Path | None = None) -> Path:
    """Destination path for a record. run_id is path-only, never a JSON field."""
    from store import canon  # sibling module — the store's one domain-folding rule, so no local copy can drift

    store_root = root or STORE
    run_id = f"{compact_stamp(record['started_at'])}-{record['verb']}"
    return store_root / canon(slug) / "runs" / f"{run_id}.json"


def write_record(slug: str, record: dict[str, Any], root: Path | None = None) -> Path:
    """Write one JSON record and return its path."""
    dest = record_path(slug, record, root)
    if dest.exists():
        raise ValueError(f"run record already exists: {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as handle:
        json.dump(record, handle, indent=2)
        handle.write("\n")
    return dest


def cmd_write(args: argparse.Namespace) -> int:
    components = parse_components(args.components_json)
    ended_at = None if args.no_ended_at else (args.ended_at or utc_now())
    record = build_record(
        verb=args.verb,
        status=args.status,
        started_at=args.started_at,
        ended_at=ended_at,
        tool=args.tool,
        model=args.model,
        effort=args.effort,
        trust=args.trust,
        artifacts=args.artifact or [],
        components=components,
        note=args.note,
    )
    dest = write_record(args.slug, record)
    print(dest.relative_to(ROOT))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("now", help="print an ISO-Z UTC timestamp for RUN_STARTED_AT")

    write = sub.add_parser("write", help="write one store/<slug>/runs/*.json record")
    write.add_argument("--slug", required=True)
    write.add_argument("--verb", required=True, choices=sorted(VERBS))
    write.add_argument("--status", choices=sorted(STATUSES), default="complete")
    write.add_argument("--started-at", required=True)
    write.add_argument("--ended-at", help="defaults to now; mostly for deterministic tests/replays")
    write.add_argument("--no-ended-at", action="store_true", help="omit ended_at (rare; normal completed runs stamp it)")
    write.add_argument("--tool", help="tool slug when env cannot detect it, e.g. codex")
    write.add_argument("--model", help="stable lead-model id, e.g. claude-opus-4-8; or set RUNREC_MODEL in the session. Falls back to 'unknown'.")
    write.add_argument("--effort", help="raw per-tool effort string; or set RUNREC_EFFORT. Claude Code auto-reads CLAUDE_EFFORT.")
    write.add_argument("--trust", choices=sorted(TRUST), help="defaults to env when tool was env-detected, else agent")
    write.add_argument("--artifact", action="append", default=[], help="repo-relative markdown artifact, repeatable")
    write.add_argument("--components-json", help='optional JSON list, e.g. \'[{"tool":"codex","model":"gpt-5.5","role":"claim-audit"}]\'')
    write.add_argument("--note", help="optional one-line run note")

    args = parser.parse_args()
    if args.cmd == "now":
        print(utc_now())
        return 0
    if args.cmd == "write":
        return cmd_write(args)
    raise AssertionError(args.cmd)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ValueError as exc:
        sys.exit(f"runrecord: {exc}")
