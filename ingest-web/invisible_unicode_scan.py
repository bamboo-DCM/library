#!/usr/bin/env python3
"""Detect invisible Unicode in explicitly named UTF-8 files before ingestion.

Flags printable Unicode tag payloads, bidi controls and context-sensitive
zero-width/format characters. Standard emoji subdivision flags and meaningful
script/emoji joiners are handled by the classifier. Reports rule, codepoint and
line without decoding hidden text by default.

Use --json or --quiet with an explicit file path. Exit 0: listed patterns absent
in the scanned representation (or stripped); 1: findings or coverage gap;
2: missing explicit target or internal error. Stripping is storage hygiene,
never clearance for agent consumption. Adjudicate findings before consumption.
--strip changes its target in place: use only an operator-approved working copy.
--reveal is deliberate incident analysis and must not feed a model by reflex.

Built and maintained by Bamboo DCM (https://bamboodcm.com), an independent
structurer and distributor of corporate and structured credit in Brazil.
CC-BY 4.0; see ../LICENSE. Public companion to SKILL.md.
"""
# capability: Detect or strip invisible Unicode used to smuggle instructions past a human reader into agent context
# capability-keywords: invisible characters, zero width, prompt injection, unicode, sanitize, hidden text
# capability-group: drafting
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import sys
import unicodedata

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

DEFAULT_INCLUDE = ("*.md", "*.txt", "*.rst", "*.adoc", "*.json", "*.yaml", "*.yml")

SKIP_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv",
    ".pytest_cache", ".mypy_cache", ".cache",
}

# --- character classes -------------------------------------------------------

# Severity HIGH: no legitimate use in this corpus. Always report; safe to strip.
TAG_BLOCK = range(0xE0000, 0xE0080)
BIDI_CONTROLS = frozenset(
    [0x202A, 0x202B, 0x202C, 0x202D, 0x202E, 0x2066, 0x2067, 0x2068, 0x2069]
)

# Severity MEDIUM: mundane individually, but used to fragment strings so a
# literal grep misses a banned term, or to pad an invisible payload.
ZERO_WIDTH_UNCONDITIONAL = frozenset(
    [
        0x200B,  # ZERO WIDTH SPACE
        0x2060,  # WORD JOINER
        0x00AD,  # SOFT HYPHEN
        0x180E,  # MONGOLIAN VOWEL SEPARATOR
        0x2061,  # FUNCTION APPLICATION
        0x2062,  # INVISIBLE TIMES
        0x2063,  # INVISIBLE SEPARATOR
        0x2064,  # INVISIBLE PLUS
        0x034F,  # COMBINING GRAPHEME JOINER — invisible, no rendering effect in
                 # normal text; a known filter-evasion filler
    ]
)

# ⚠️ INTRAWORD BY DESIGN — these must NEVER escalate to fragmentation.
# The whole POINT of a soft hyphen is to sit inside a word; invisible math
# operators sit between operands; the combining grapheme joiner sits between
# graphemes. Escalating them on intraword placement fires HIGH on every
# legitimately hyphenated word — and PT-BR typesetting uses them, so half this
# firm's corpus would halt ingestion. A control that screams on legitimate
# content gets disabled, which is a worse outcome than the miss it prevents.
# (Caught by the SECOND cross-vendor review, 12 Aug 2026, and reproduced against
# the code before the fix: 'estabe<SHY>lecimento' classified HIGH.)
INTRAWORD_BY_DESIGN = frozenset(
    [
        0x00AD,  # SOFT HYPHEN — discretionary hyphenation point
        0x034F,  # COMBINING GRAPHEME JOINER — collation-sensitive sequences
        0x2061, 0x2062, 0x2063, 0x2064,  # invisible mathematical operators
    ]
)

# The complete set of emoji tag sequences in actual use (UTS #51 Annex C —
# CLDR subdivision IDs with "regular" status). Three flags, and that is all.
# An allowlist rather than a grammar because a grammar exempts attacker-chosen
# strings that merely LOOK like subdivision IDs.
VALID_SUBDIVISION_TAGS = frozenset(["gbeng", "gbsct", "gbwls"])

# Context-sensitive: legitimate inside emoji sequences and Indic/Arabic scripts.
JOINERS = frozenset([0x200C, 0x200D])  # ZWNJ, ZWJ

# U+FEFF is a legitimate BOM at offset 0; anywhere else it is a zero-width
# no-break space and is treated as MEDIUM.
BOM = 0xFEFF

# NEVER touched — makes emoji render as emoji rather than as text glyphs.
NEVER_STRIP = frozenset([0xFE0F, 0xFE0E])

SEVERITY_HIGH = "HIGH"
SEVERITY_MEDIUM = "MEDIUM"

RULE_TAG_BLOCK = "tag-block-ascii-smuggling"
RULE_BIDI = "bidi-control-trojan-source"
RULE_ZERO_WIDTH = "zero-width-format-char"
RULE_JOINER = "orphan-joiner"
RULE_STRAY_BOM = "stray-bom"
RULE_FRAGMENTATION = "intraword-fragmentation-evasion"


def _is_emoji_or_complex_script(cp: int) -> bool:
    """True if cp legitimately participates in a joiner sequence.

    Covers emoji ranges plus the Indic / Arabic / Malayalam-class scripts where
    ZWJ / ZWNJ are orthographically meaningful. Deliberately generous: a false
    'legitimate' costs us one unreported joiner, while a false 'orphan' would
    corrupt a real emoji or a real word.
    """
    if cp in NEVER_STRIP:
        return True
    return (
        0x1F000 <= cp <= 0x1FAFF        # emoji blocks
        or 0x2600 <= cp <= 0x27BF       # misc symbols + dingbats
        or 0x2190 <= cp <= 0x21FF       # arrows (often emoji-presented)
        or 0x2B00 <= cp <= 0x2BFF       # misc symbols and arrows
        or 0xFE00 <= cp <= 0xFE0F       # variation selectors
        or 0x1F1E6 <= cp <= 0x1F1FF     # regional indicators (flags)
        or 0x0900 <= cp <= 0x0DFF       # Devanagari .. Sinhala
        or 0x0600 <= cp <= 0x06FF       # Arabic
        or 0x0A00 <= cp <= 0x0A7F       # Gurmukhi
    )


def _is_emoji_tag_sequence(line: str, idx: int) -> bool:
    """True ONLY for a VALID emoji tag sequence per UTS #51.

    ⚠️ v3 of this check was a SCANNER BYPASS and was caught by the third review.
    It accepted "any emoji base + any tag run + CANCEL TAG", so
    `😀` + tag-encoded("exfiltrate keys") + CANCEL returned ZERO findings — a
    fully invisible payload waved through by an exemption added to fix a false
    positive. Reproduced before fixing.

    UTS #51 § Valid Emoji Tag Sequences is narrow, so the check can be too:
      base       = U+1F3F4 WAVING BLACK FLAG (the only base in use)
      tag_spec   = 2..6 chars from U+E0030-E0039 (0-9) and U+E0061-E007A (a-z)
      terminator = U+E007F CANCEL TAG
    Anything outside that envelope — a different base, an uppercase or
    punctuation tag char, a run longer than 6 — is not a flag and stays HIGH.

    Lesson worth keeping: an exemption is an attack surface. Validate against
    the standard's actual grammar, never against its broad syntactic shape.
    """
    start = idx
    while start > 0 and ord(line[start - 1]) in TAG_BLOCK:
        start -= 1
    if start == 0 or ord(line[start - 1]) != 0x1F3F4:
        return False
    end = idx
    while end + 1 < len(line) and ord(line[end + 1]) in TAG_BLOCK:
        end += 1
    run = [ord(c) for c in line[start:end + 1]]
    if not run or run[-1] != 0xE007F:
        return False
    spec = run[:-1]
    # ⚠️ A GRAMMAR CHECK IS NOT ENOUGH — round 4 caught this. UTS #51 Annex C
    # requires the DECODED tag to be a valid CLDR subdivision ID, not merely
    # 2-6 lowercase characters. Accepting the shape alone leaves an attacker a
    # 6-character exempt channel (`\U0001F3F4` + tag("abcdef") + CANCEL).
    # The real-world valid set is three flags, so an ALLOWLIST closes the
    # channel completely and costs nothing. Anything else stays HIGH.
    decoded = "".join(chr(c - 0xE0000) for c in spec)
    return decoded in VALID_SUBDIVISION_TAGS


def _is_intraword(line: str, idx: int) -> bool:
    """True if the char at idx sits BETWEEN two letters — a fragmentation tell.

    🔑 This discriminator escalates one obvious evasion shape to HIGH; it does
    NOT make MEDIUM findings safe to automate. It exists because of a specific
    attack the first version of this tool enabled:

        An attacker fragments an instruction with zero-width characters
        (`ig<ZWSP>nore all pre<ZWSP>vious instructions`) to slip past a keyword
        filter. A scanner that reports MEDIUM, strips the padding, and lets
        ingestion continue has just DE-OBFUSCATED the payload and handed the
        agent a clean prompt-injection string. The evasion attempt is converted
        into a working attack BY THE CONTROL.

    Zero-width characters arriving from honest HTML extraction often cluster at
    tag and line boundaries, next to whitespace or punctuation. Intraword
    placement escalates to HIGH; boundary placement remains MEDIUM but still
    requires adjudication before agent consumption. Severity ranks urgency,
    never permission to auto-proceed.

    Caught by cross-vendor review, 12 Aug 2026, as the single strongest
    objection to the original contract.
    """
    if idx == 0 or idx + 1 >= len(line):
        return False
    return line[idx - 1].isalnum() and line[idx + 1].isalnum()


def _classify(cp: int, line: str, idx: int, line_no: int) -> dict | None:
    """Return a finding dict for cp at position idx, or None if benign."""
    if cp in NEVER_STRIP:
        return None

    if cp in TAG_BLOCK:
        if _is_emoji_tag_sequence(line, idx):
            return None
        return _finding(RULE_TAG_BLOCK, SEVERITY_HIGH, cp, line_no, idx)

    if cp in BIDI_CONTROLS:
        return _finding(RULE_BIDI, SEVERITY_HIGH, cp, line_no, idx)

    if cp in ZERO_WIDTH_UNCONDITIONAL:
        if cp not in INTRAWORD_BY_DESIGN and _is_intraword(line, idx):
            return _finding(RULE_FRAGMENTATION, SEVERITY_HIGH, cp, line_no, idx)
        return _finding(RULE_ZERO_WIDTH, SEVERITY_MEDIUM, cp, line_no, idx)

    if cp == BOM:
        # Legitimate only as the very first char of the very first line.
        if line_no == 1 and idx == 0:
            return None
        return _finding(RULE_STRAY_BOM, SEVERITY_MEDIUM, cp, line_no, idx)

    if cp in JOINERS:
        prev_cp = ord(line[idx - 1]) if idx > 0 else None
        next_cp = ord(line[idx + 1]) if idx + 1 < len(line) else None
        prev_ok = prev_cp is not None and _is_emoji_or_complex_script(prev_cp)
        next_ok = next_cp is not None and _is_emoji_or_complex_script(next_cp)
        if prev_ok or next_ok:
            return None  # load-bearing inside an emoji / script cluster
        if _is_intraword(line, idx):
            # A joiner between two Latin letters is fragmentation, not orthography.
            return _finding(RULE_FRAGMENTATION, SEVERITY_HIGH, cp, line_no, idx)
        return _finding(RULE_JOINER, SEVERITY_MEDIUM, cp, line_no, idx)

    return None


def _finding(rule: str, severity: str, cp: int, line_no: int, col: int) -> dict:
    try:
        name = unicodedata.name(chr(cp))
    except ValueError:
        name = "<unnamed>"
    return {
        "rule": rule,
        "severity": severity,
        "codepoint": f"U+{cp:04X}",
        "name": name,
        "line": line_no,
        "col": col + 1,
    }


def scan_text(text: str) -> list[dict]:
    """Scan a string. Returns findings; never raises on content."""
    findings: list[dict] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        for idx, ch in enumerate(line):
            cp = ord(ch)
            # Fast path: everything we care about is non-ASCII and non-printing.
            if cp < 0x80:
                continue
            hit = _classify(cp, line, idx, line_no)
            if hit:
                findings.append(hit)
    return findings


def strip_text(text: str) -> tuple[str, int]:
    """Remove every character this tool would report. Returns (clean, removed)."""
    out: list[str] = []
    removed = 0
    for line_no, line in enumerate(text.split("\n"), start=1):
        kept: list[str] = []
        for idx, ch in enumerate(line):
            cp = ord(ch)
            if cp < 0x80:
                kept.append(ch)
                continue
            if _classify(cp, line, idx, line_no) is None:
                kept.append(ch)
            else:
                removed += 1
        out.append("".join(kept))
    return "\n".join(out), removed


def _iter_files(paths: list[str], include: tuple[str, ...],
                unscanned: list[tuple[str, str]] | None = None):
    """Yield files to scan; record glob-excluded ones as UNSCANNED coverage.

    A file excluded by the include globs is not 'not our problem' — it is a
    file the caller pointed us at and we did not read. Recording it is what
    keeps a folder of PDFs from producing a confident 'clean'.
    """
    for path in paths:
        if os.path.isfile(path):
            yield path          # an explicitly-named file bypasses the globs
            continue
        for root, dirnames, filenames in os.walk(path):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in sorted(filenames):
                if any(fnmatch.fnmatch(fn, pat) for pat in include):
                    yield os.path.join(root, fn)
                elif unscanned is not None and not fn.startswith("."):
                    unscanned.append(
                        (os.path.join(root, fn), "excluded by --include globs")
                    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Detect/strip invisible Unicode used to smuggle instructions."
    )
    ap.add_argument("paths", nargs="*", default=None,
                    help="explicit files or directories to scan")
    ap.add_argument("--include", default=",".join(DEFAULT_INCLUDE),
                    help="comma-separated glob patterns for directory walks")
    ap.add_argument("--strip", action="store_true",
                    help="remove offending characters in place")
    ap.add_argument("--stdin", action="store_true",
                    help="read from stdin; with --strip, write clean text to stdout")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--quiet", action="store_true",
                    help="hook mode: no per-finding output, exit 1 if any found")
    ap.add_argument("--reveal", action="store_true",
                    help="INCIDENT ANALYSIS ONLY: decode tag-block payloads to text")
    args = ap.parse_args(argv)

    try:
        if args.stdin:
            text = sys.stdin.read()
            if args.strip:
                clean, removed = strip_text(text)
                sys.stdout.write(clean)
                if removed and not args.quiet:
                    print(f"[invisible-unicode] stripped {removed} char(s)",
                          file=sys.stderr)
                return 0
            findings = scan_text(text)
            _report({"<stdin>": findings}, args)
            return 1 if findings else 0

        include = tuple(p.strip() for p in args.include.split(",") if p.strip())
        if not args.paths:
            print("[invisible-unicode] no explicit scan path; control did NOT run", file=sys.stderr)
            return 2
        paths = args.paths
        results: dict[str, list[dict]] = {}
        total_removed = 0
        scanned = 0
        unscanned: list[tuple[str, str]] = []

        for path in paths:
            if not os.path.exists(path):
                unscanned.append((path, "path does not exist"))

        # A file the caller NAMED but the include globs exclude is unscanned
        # coverage, not an absent file. Point this at a folder of PDFs and every
        # one of them lands here.
        for fp in _iter_files(paths, include, unscanned):
            try:
                with open(fp, "r", encoding="utf-8", errors="strict") as fh:
                    text = fh.read()
            except UnicodeDecodeError:
                unscanned.append((fp, "not UTF-8 text (binary?)"))
                continue
            except OSError as exc:
                unscanned.append((fp, f"unreadable: {exc.__class__.__name__}"))
                continue
            scanned += 1

            if args.strip:
                clean, removed = strip_text(text)
                if removed:
                    with open(fp, "w", encoding="utf-8") as fh:
                        fh.write(clean)
                    total_removed += removed
                    results[fp] = [{"rule": "stripped", "count": removed}]
            else:
                findings = scan_text(text)
                if findings:
                    results[fp] = findings

        if scanned == 0:
            unscanned.append(("<selection>", "zero files scanned"))

        if args.strip:
            if not args.quiet:
                print(f"[invisible-unicode] stripped {total_removed} char(s) "
                      f"across {len(results)} file(s)")
            if unscanned:
                _report(results, args, scanned, unscanned)
            return 1 if unscanned else 0

        _report(results, args, scanned, unscanned)
        # Unscanned coverage is a FINDING, not a footnote: exiting 0 here is
        # exactly how "clean" gets asserted over files nobody read.
        return 1 if (results or unscanned) else 0

    except Exception as exc:  # noqa: BLE001
        # EXIT 2 = "the control did not run" — distinct from 0 (clean) and
        # 1 (findings). This used to return 0, which made scanner MALFUNCTION
        # indistinguishable from SUCCESS to any hook or CI step: the single
        # strongest objection of the second cross-vendor review, and precisely
        # the false-assurance shape this tool exists to prevent.
        #
        # It still fails OPEN in the sense that matters — a caller ignoring exit
        # codes proceeds, so the guard cannot wedge a pipeline. But a caller that
        # CHECKS can now distinguish "clear" from "never ran", and `if ! cmd`
        # reads 2 as failure, which is the correct default.
        print(f"[invisible-unicode] INTERNAL ERROR — control did NOT run "
              f"(exit 2; this is NOT a clean result): {exc}", file=sys.stderr)
        return 2


def _decode_tag_block(findings: list[dict]) -> str:
    """Reconstruct the ASCII a tag-block payload mirrors.

    INCIDENT ANALYSIS ONLY (--reveal). Each U+E00xx tag char mirrors the ASCII
    char at (cp - 0xE0000), which is the whole point of the smuggling vector:
    the payload is readable ASCII wearing an invisible costume. Off by default
    because printing it re-injects the quarantined content into the transcript.
    """
    chars = []
    for f in findings:
        if f.get("rule") != RULE_TAG_BLOCK:
            continue
        try:
            cp = int(f["codepoint"].removeprefix("U+"), 16)
        except (KeyError, ValueError):
            continue
        ascii_cp = cp - 0xE0000
        if 0x20 <= ascii_cp <= 0x7E:
            chars.append(chr(ascii_cp))
    return "".join(chars)


def _report(results: dict[str, list[dict]], args,
            scanned: int = 0, unscanned: list[tuple[str, str]] | None = None) -> None:
    unscanned = unscanned or []
    if args.json:
        print(json.dumps(
            {"findings": results,
             "scanned": scanned,
             "unscanned": [{"file": f, "reason": r} for f, r in unscanned]},
            indent=2, ensure_ascii=False))
        return
    if args.quiet:
        return

    # ⚠️ The word "clean" is reserved for a scan with FULL coverage. Anything
    # unread is reported as a coverage gap, never absorbed into a pass — a
    # scanner that says "clean" over files it could not open is worse than no
    # scanner, because it converts "I don't know" into "checked, clear".
    if not results:
        if unscanned:
            print(f"[invisible-unicode] NOT CLEAN — no listed patterns in "
                  f"{scanned} file(s) scanned, but {len(unscanned)} file(s) "
                  f"were NOT SCANNED:")
            _print_unscanned(unscanned)
            print("\n  A scan that could not read the content is not evidence "
                  "of its absence.\n  For PDFs/DOCX: scan the EXTRACTED TEXT, "
                  "not the container.")
        else:
            print(f"[invisible-unicode] clean — no listed patterns found "
                  f"across {scanned} file(s) scanned, 0 unscanned")
        return

    high = sum(1 for f in results.values() for x in f
               if x.get("severity") == SEVERITY_HIGH)
    print(f"[invisible-unicode] {sum(len(v) for v in results.values())} finding(s) "
          f"across {len(results)} file(s) — {high} HIGH "
          f"({scanned} scanned, {len(unscanned)} NOT scanned)")
    print("  (payload text is deliberately NOT printed; see --reveal)")
    print("  ⚠️ NO severity authorizes auto-proceed. Severity ranks URGENCY, not")
    print("     safety: stripping removes obfuscation, which is exactly what an")
    print("     evasion payload wants. A human adjudicates before this content")
    print("     reaches an agent. Strip is for STORAGE.\n")
    for fp, findings in sorted(results.items()):
        rel = os.path.relpath(fp, REPO_ROOT) if fp != "<stdin>" else fp
        print(f"  {rel}")
        for f in findings[:20]:
            print(f"    {f['severity']:<6} {f['rule']:<28} "
                  f"{f['codepoint']} ({f['name']}) line {f['line']}:{f['col']}")
        if len(findings) > 20:
            print(f"    … and {len(findings) - 20} more")
        if args.reveal:
            payload = _decode_tag_block(findings)
            if payload:
                print(f"    [--reveal] decoded tag-block payload: {payload!r}")

    if unscanned:
        print(f"\n  ⚠️ {len(unscanned)} file(s) NOT SCANNED — coverage gap, "
              f"not a pass:")
        _print_unscanned(unscanned)


def _print_unscanned(unscanned: list[tuple[str, str]], cap: int = 10) -> None:
    for fp, reason in unscanned[:cap]:
        rel = os.path.relpath(fp, REPO_ROOT)
        print(f"    UNSCANNED  {rel} — {reason}")
    if len(unscanned) > cap:
        print(f"    … and {len(unscanned) - cap} more unscanned")


if __name__ == "__main__":
    sys.exit(main())
