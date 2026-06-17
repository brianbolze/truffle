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

    def test_explicit_tool_corroborated_by_env_is_env_trust(self) -> None:
        # marek/trt fix: --tool claude-code while CLAUDECODE is set must read as env-trust (the env
        # confirms it), not agent — so two identical Claude runs don't diverge on trust.
        rec = rr.build_record(
            verb="visual-evidence", status="complete", started_at=STARTED, ended_at=ENDED,
            tool="claude-code", model="claude-opus-4-8", artifacts=["visual.md"],
            env={"CLAUDECODE": "1"},
        )
        self.assertEqual(rec["tool"], "claude-code")
        self.assertEqual(rec["trust"], "env")

    def test_undetected_tool_writes_unknown_not_raises(self) -> None:
        # The footgun fix: no env signal and no --tool must still produce a record (tool "unknown",
        # trust "agent") rather than erroring and dropping the bookkeeping step.
        rec = rr.build_record(
            verb="research-company", status="complete", started_at=STARTED,
            model="gpt-5", artifacts=["profile.md"], env={},
        )
        self.assertEqual(rec["tool"], "unknown")
        self.assertEqual(rec["trust"], "agent")

    def test_artifacts_strip_store_slug_prefix(self) -> None:
        # One agent recorded the full repo path; normalize to the bare company-dir filename.
        self.assertEqual(rr.clean_artifacts(["store/directmeds-com/visual.md"]), ["visual.md"])
        self.assertEqual(rr.clean_artifacts(["profile.md"]), ["profile.md"])

    def test_codex_env_is_auto_detected(self) -> None:
        # Codex stamps deterministic env (CODEX_SHELL / CODEX_THREAD_ID / bundle id) — detect it like
        # Claude so a Codex agent needn't pass --tool, killing the "tool could not be detected" footgun.
        rec = rr.build_record(
            verb="visual-evidence", status="complete", started_at=STARTED, ended_at=ENDED,
            model="gpt-5", artifacts=["visual.md"],
            env={"CODEX_SHELL": "1", "CODEX_THREAD_ID": "019ed727", "__CFBundleIdentifier": "com.openai.codex"},
        )
        self.assertEqual(rec["tool"], "codex")
        self.assertEqual(rec["trust"], "env")

    def test_runrec_env_overrides_declare_model_and_effort(self) -> None:
        # Brian's session declaration via env is authoritative over the agent's --model/--effort guess.
        rec = rr.build_record(
            verb="research-company", status="complete", started_at=STARTED,
            model="gpt-5", effort="low", artifacts=["profile.md"],
            env={"CODEX_SHELL": "1", "RUNREC_MODEL": "gpt-5.5", "RUNREC_EFFORT": "high"},
        )
        self.assertEqual(rec["model"], "gpt-5.5")
        self.assertEqual(rec["effort"], "high")

    def test_model_defaults_unknown_when_unnamed(self) -> None:
        # No --model and no RUNREC_MODEL: record still lands with model "unknown", never an error.
        rec = rr.build_record(
            verb="research-company", status="complete", started_at=STARTED,
            artifacts=["profile.md"], env={"CODEX_SHELL": "1"},
        )
        self.assertEqual(rec["model"], "unknown")


if __name__ == "__main__":
    unittest.main(verbosity=2)
