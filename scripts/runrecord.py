#!/usr/bin/env python3
"""Write per-company run records for capture verbs.

Run records answer the operational question "what produced this capture?" without
putting engine telemetry into company State. They are small JSON envelopes under
`store/<slug>/runs/<UTC-compact-Z>-<verb>.json`; see RUNS.md for the contract.

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


def canon_slug(value: str) -> str:
    """Store-dir slug fallback: lowercase, strip scheme/www, dots -> dashes."""
    s = value.strip().lower()
    s = re.sub(r"^https?://", "", s).rstrip("/")
    s = re.sub(r"^www\.", "", s)
    return s.replace(".", "-")


def normalize_tool(value: str | None) -> str | None:
    """Tool labels are query keys, so normalize common spellings to stable slugs."""
    if not value:
        return None
    token = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    if token in {"claudecode", "claude-code", "claude"}:
        return "claude-code"
    return token or None


def detect_tool(env: dict[str, str] | None = None) -> tuple[str | None, bool]:
    """(tool, env_trusted). Claude Code exposes deterministic env; Codex usually does not."""
    e = env or os.environ
    if e.get("CLAUDECODE") or e.get("CLAUDE_CODE_SESSION_ID"):
        return "claude-code", True
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
    """Artifacts are bare, repo-relative markdown paths. Empty list is valid."""
    out: list[str] = []
    for item in items:
        path = item.strip()
        if not path:
            continue
        if path.startswith("/") or ".." in Path(path).parts:
            raise ValueError(f"artifact must be a repo-relative path: {item!r}")
        if not path.endswith(".md"):
            raise ValueError(f"artifact must be a markdown file: {item!r}")
        out.append(path)
    return out


def build_record(
    *,
    verb: str,
    status: str,
    started_at: str,
    model: str,
    artifacts: list[str],
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
    if not model.strip():
        raise ValueError("model is required")

    e = env or os.environ
    env_tool, env_trusted = detect_tool(e)
    final_tool = env_tool or normalize_tool(tool)
    if not final_tool:
        raise ValueError("tool could not be detected; pass --tool")
    final_trust = trust or ("env" if env_trusted else "agent")
    if final_trust not in TRUST:
        raise ValueError(f"trust must be one of {sorted(TRUST)}")

    final_effort = effort
    if final_effort is None and final_tool == "claude-code":
        final_effort = e.get("CLAUDE_EFFORT") or "unknown"

    record: dict[str, Any] = {
        "record_version": RECORD_VERSION,
        "verb": verb,
        "status": status,
        "tool": final_tool,
        "model": model.strip(),
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
    store_root = root or STORE
    run_id = f"{compact_stamp(record['started_at'])}-{record['verb']}"
    return store_root / canon_slug(slug) / "runs" / f"{run_id}.json"


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
    write.add_argument("--model", required=True, help="stable lead-model id, e.g. claude-opus-4-8")
    write.add_argument("--effort", help="raw per-tool effort string; Claude Code uses CLAUDE_EFFORT when omitted")
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
