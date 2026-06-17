#!/usr/bin/env python3
# ruff: noqa: I001
"""Tests for scripts/runrecord.py — the small JSON envelope that records which agent/model/effort
produced a capture. No real store, no network."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import runrecord as rr  # noqa: E402 — after the sys.path insert above


STARTED = "2026-06-17T15:30:12Z"
ENDED = "2026-06-17T16:12:48Z"


class RunRecordTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_claude_code_env_record(self) -> None:
        rec = rr.build_record(
            verb="research-company",
            status="complete",
            started_at=STARTED,
            ended_at=ENDED,
            model="claude-opus-4-8",
            artifacts=["profile.md"],
            env={"CLAUDECODE": "1", "CLAUDE_EFFORT": "xhigh"},
        )
        self.assertEqual(rec["record_version"], "0.1")
        self.assertEqual(rec["tool"], "claude-code")
        self.assertEqual(rec["effort"], "xhigh")
        self.assertEqual(rec["trust"], "env")
        self.assertNotIn("wall_seconds", rec)
        self.assertNotIn("run_id", rec)
        dest = rr.write_record("functionhealth.com", rec, root=self.root)
        self.assertEqual(dest.relative_to(self.root).as_posix(), "functionhealth-com/runs/20260617T153012Z-research-company.json")
        self.assertEqual(json.loads(dest.read_text()), rec)
        with self.assertRaises(ValueError):
            rr.write_record("functionhealth.com", rec, root=self.root)

    def test_codex_agent_record_omits_effort_when_absent(self) -> None:
        rec = rr.build_record(
            verb="research-company",
            status="complete",
            started_at=STARTED,
            ended_at=ENDED,
            tool="Codex",
            model="gpt-5.5",
            artifacts=["profile.md", "offerings.md"],
            env={},
        )
        self.assertEqual(rec["tool"], "codex")
        self.assertEqual(rec["trust"], "agent")
        self.assertNotIn("effort", rec)

    def test_claude_code_empty_effort_is_unknown(self) -> None:
        rec = rr.build_record(
            verb="visual-evidence",
            status="complete",
            started_at=STARTED,
            ended_at=ENDED,
            model="claude-opus-4-8",
            artifacts=["visual.md"],
            env={"CLAUDE_CODE_SESSION_ID": "abc"},
        )
        self.assertEqual(rec["effort"], "unknown")

    def test_components_are_llm_only_and_validated(self) -> None:
        components = rr.parse_components(
            '[{"tool":"codex","model":"gpt-5.5","role":"claim-audit"},'
            '{"tool":"claude-code","model":"sonnet","role":"visual-miner"}]'
        )
        rec = rr.build_record(
            verb="visual-evidence",
            status="complete",
            started_at=STARTED,
            ended_at=ENDED,
            tool="claude-code",
            model="claude-opus-4-8",
            artifacts=["visual.md"],
            components=components,
            env={},
        )
        self.assertEqual(len(rec["components"]), 2)
        with self.assertRaises(ValueError):
            rr.parse_components('[{"tool":"x","model":"y","count":4}]')

    def test_skipped_and_failed_are_not_status_values(self) -> None:
        for status in ("skipped", "failed", "aborted"):
            with self.assertRaises(ValueError):
                rr.build_record(
                    verb="research-company",
                    status=status,
                    started_at=STARTED,
                    model="gpt-5.5",
                    tool="codex",
                    artifacts=[],
                    env={},
                )

    def test_artifacts_must_be_relative_markdown(self) -> None:
        with self.assertRaises(ValueError):
            rr.clean_artifacts(["/tmp/profile.md"])
        with self.assertRaises(ValueError):
            rr.clean_artifacts(["profile.json"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
