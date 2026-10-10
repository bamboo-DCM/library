#!/usr/bin/env python3
"""Fail closed on high-confidence exposure hazards in this public repository.

Blocks credential-shaped content, secret-bearing filenames, absolute user-home
paths, symlinks, binary files and oversized files in the proposed tree. It is a
deterministic floor, narrower than a human confidentiality review: passing it
does not mean a change is fit to publish. Python standard library only.

Usage:
    python3 .github/exposure_check.py --self-test
    python3 .github/exposure_check.py [ROOT]
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


MAX_BYTES = 1_000_000
FORBIDDEN_EXACT_NAMES = {".env", "id_rsa", "id_ed25519", "credentials.json"}
FORBIDDEN_SUFFIXES = {".pem", ".key", ".p12", ".pfx"}
# Patterns are split so this file never matches itself.
HOME_PATH_PATTERNS = [
    ("macOS user path", re.compile(rb"/" + rb"Users/[^/\s]+/")),
    # One backslash as written in prose, two as escaped in JSON or code.
    ("Windows user path", re.compile(rb"[A-Za-z]:\\{1,2}" + rb"Users\\{1,2}[^\\\s]+\\")),
]
SECRET_PATTERNS = [
    ("private key", re.compile(rb"-----" + rb"BEGIN (?:RSA |OPENSSH |EC |DSA |PGP )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(rb"(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,})")),
    ("Slack token", re.compile(rb"xox[baprs]-[A-Za-z0-9-]{20,}")),
    ("AWS access key", re.compile(rb"AKIA[0-9A-Z]{16}")),
    ("OpenAI-style key", re.compile(rb"sk-[A-Za-z0-9_-]{32,}")),
    ("xAI-style key", re.compile(rb"xai-[A-Za-z0-9_-]{20,}")),
]


def tracked_files(root: Path) -> list[Path]:
    proc = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        check=False,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8", errors="replace").strip())
    return [root / item.decode("utf-8") for item in proc.stdout.split(b"\0") if item]


def scan_bytes(label: str, data: bytes) -> list[str]:
    return [f"{label}: {name}" for name, pattern in SECRET_PATTERNS + HOME_PATH_PATTERNS
            if pattern.search(data)]


def scan(root: Path) -> list[str]:
    findings: list[str] = []
    for path in tracked_files(root):
        rel = path.relative_to(root).as_posix()
        if path.name.lower() in FORBIDDEN_EXACT_NAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            findings.append(f"{rel}: secret-bearing filename")
            continue
        if path.is_symlink():
            findings.append(f"{rel}: symlink is not admitted")
            continue
        try:
            data = path.read_bytes()
        except OSError as exc:
            findings.append(f"{rel}: unreadable ({exc})")
            continue
        if len(data) > MAX_BYTES:
            findings.append(f"{rel}: exceeds {MAX_BYTES} bytes")
            continue
        if b"\0" in data:
            findings.append(f"{rel}: binary content is not admitted")
            continue
        findings.extend(scan_bytes(rel, data))
    return findings


def self_test() -> int:
    samples = {
        "clean": b"portable public text\n",
        "private-key": b"-----" + b"BEGIN OPENSSH PRIVATE KEY-----\n",
        "mac-user-path": b"/" + b"Users/example/notes.md\n",
        "windows-user-path": b"C:\\" + b"Users\\example\\notes.md\n",
        "escaped-windows-user-path": b"C:\\\\" + b"Users\\\\example\\\\notes.md\n",
        "github-token": b"ghp" + b"_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcd\n",
        "slack-token": b"xox" + b"b-0123456789-abcdefghijklmnop\n",
    }
    assert scan_bytes("clean", samples["clean"]) == [], "scanner flagged clean text"
    for name in ("private-key", "mac-user-path", "windows-user-path", "escaped-windows-user-path",
                 "github-token", "slack-token"):
        assert scan_bytes(name, samples[name]), f"scanner missed {name}"
    # The checkout must keep local environment files and Finder metadata out of a PR.
    root = Path(__file__).resolve().parents[1]
    for name in (".env", ".DS_Store", "nested/.DS_Store"):
        result = subprocess.run(
            ["git", "-C", str(root), "check-ignore", "--quiet", "--no-index", "--", name],
            check=False, capture_output=True,
        )
        assert result.returncode == 0, f".gitignore does not ignore {name}"
    print("exposure self-test: pass")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    if args.self_test:
        return self_test()
    root = Path(args.root).resolve()
    try:
        findings = scan(root)
    except RuntimeError as exc:
        print(f"::error::cannot enumerate tracked files: {exc}")
        return 2
    if findings:
        for finding in findings:
            print(f"::error::{finding}")
        print(f"exposure: fail ({len(findings)} finding(s))")
        return 1
    print(f"exposure: pass ({len(tracked_files(root))} tracked files scanned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
