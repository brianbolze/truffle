#!/usr/bin/env python3
"""Build blind A/B review packets from the two final candidate sets.

Why this exists: the judge passes must (a) read the *current* gpt55_v11 set, not
the stale logo-less gpt55 dir, and (b) never see model identity. Doing the copy
by hand risks grabbing the wrong source or leaking the model name (the Claude
RUN_NOTES header literally says "Model: Claude (Opus 4.8)"). This script makes the
pairing deterministic and reproducible, randomizes A/B per sample via a stable
hash (no RNG state to persist), and scrubs identity tokens from every copied file.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

EXPERIMENT = Path(__file__).resolve().parents[1]
SAMPLES = json.loads((EXPERIMENT / "sample.json").read_text(encoding="utf-8"))
BLIND = EXPERIMENT / "_out" / "blind"

# The two final V1.1 candidate sets under comparison. gpt55 (no suffix) is the
# stale pre-logo set and is deliberately excluded.
GPT_MODEL = "gpt55_v11"
CLAUDE_MODEL = "claude"

# Stable salt so A/B assignment is reproducible run-to-run but not guessable from
# the sample name alone.
SALT = "bakeoff-2026-06-13"

# Identity tokens scrubbed from copied files so prose/RUN_NOTES can't de-blind the
# judge. None of these appear in the sampled companies' legitimate content.
IDENTITY_RE = re.compile(
    r"(claude|opus\s*4\.8|gpt-?5\.5|gpt-?5|codex|anthropic|openai|comparator side of the bakeoff)",
    re.IGNORECASE,
)


def gpt_is_a(sample_id: str) -> bool:
    """Deterministically decide whether GPT is side A for this sample."""
    digest = hashlib.sha256(f"{SALT}:{sample_id}".encode()).hexdigest()
    return int(digest, 16) % 2 == 0


def scrub(text: str) -> str:
    """Redact model-identity tokens; keep everything else byte-for-byte."""
    return IDENTITY_RE.sub("[model]", text)


def copy_candidate(src_dir: Path, dst_dir: Path) -> None:
    """Copy a candidate dir into a blind slot, scrubbing identity from text files."""
    if dst_dir.exists():
        shutil.rmtree(dst_dir)
    dst_dir.mkdir(parents=True)
    for src in sorted(src_dir.rglob("*")):
        rel = src.relative_to(src_dir)
        dst = dst_dir / rel
        if src.is_dir():
            dst.mkdir(parents=True, exist_ok=True)
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix == ".md":
            dst.write_text(scrub(src.read_text(encoding="utf-8", errors="replace")), encoding="utf-8")
        else:
            shutil.copy2(src, dst)


def main() -> int:
    if BLIND.exists():
        shutil.rmtree(BLIND)
    BLIND.mkdir(parents=True)

    model_map: dict[str, dict[str, str]] = {}
    for sample in SAMPLES:
        sample_id = sample["sample_id"]
        gpt_src = EXPERIMENT / "_out" / GPT_MODEL / sample_id
        claude_src = EXPERIMENT / "_out" / CLAUDE_MODEL / sample_id
        if not gpt_src.exists() or not claude_src.exists():
            print(f"{sample_id}: missing candidate ({GPT_MODEL}={gpt_src.exists()}, "
                  f"{CLAUDE_MODEL}={claude_src.exists()})")
            return 1

        a_model, b_model = (GPT_MODEL, CLAUDE_MODEL) if gpt_is_a(sample_id) else (CLAUDE_MODEL, GPT_MODEL)
        a_src = gpt_src if a_model == GPT_MODEL else claude_src
        b_src = claude_src if b_model == CLAUDE_MODEL else gpt_src
        copy_candidate(a_src, BLIND / sample_id / "A")
        copy_candidate(b_src, BLIND / sample_id / "B")
        model_map[sample_id] = {"A": a_model, "B": b_model}

    (BLIND / "model_map.json").write_text(json.dumps(model_map, indent=2) + "\n", encoding="utf-8")
    print(f"blind packets built for {len(model_map)} samples at {BLIND}")
    print("model_map.json written (keep private — do not show judges)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
