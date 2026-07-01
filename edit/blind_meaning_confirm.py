#!/usr/bin/env python3
"""blind_meaning_confirm.py — the deterministic BLINDING HARNESS for the /edit skill's leg-(d).

This is the OUT-OF-MODEL, structural half of the four-part gate's meaning-preservation leg
(leg-(d); see the Readability-Editing Methodology §6). The /edit skill is an optimizer; a
model that judges its OWN rewrite's faithfulness — or even reads a meaning-diff it produced —
is the gameable LLM-judge the gate exists to avoid. Testing proved it live: a generative
rewriter rationalized a `describes -> to describe` drift as
"equivalent" in its own diff; only a BLIND independent reader, re-deriving the claims cold,
caught it. So leg-(d) must be wired STRUCTURALLY outside the rewriting model's process — not as
an in-skill "I promise not to self-certify," which is recall-tier (the same model could skip it).

This harness is that structure. It takes the original text and the edited text and emits a
BLINDED BRIEF: the two texts relabeled "Text A" / "Text B", presented symmetrically, with the
A/B <-> original/edit MAPPING WITHHELD to a separate key file the confirming party never sees.
An independent blind cold-reader (a separate sonnet subagent, or a human) reads ONLY the brief
and re-derives the claim-by-claim diff COLD, not knowing which text is the edit. So:
  - the rewriting model does NOT produce the diff (the blind reader does), and
  - the confirming party does NOT see which text is the edit (this harness withheld it).
That is the non-forgeable boundary (methodology §6), wired in code.

WHY A HARNESS AND NOT A PROSE INSTRUCTION (the load-bearing design choice). "Construct a
symmetric blinded brief and don't reveal which is the edit," handed to the rewriting model as
prose, is itself recall-tier — the model could leak the mapping (deliberately or not). Doing the
blinding in deterministic code takes the leak out of the model's hands: the model passes the two
texts IN and hands the blind reader a brief FILE it did not author. The model's residual freedom
is reduced to "provide the two texts + consume the verdict"; it cannot bias the brief or reveal
the answer key. This is the meaning-side twin of readability_diag.py (the deterministic leg-(a)
half) — both push the non-forgeable part to code so the gate does not rest on a model's promise.

THE GATE DECISION IS ITSELF BLIND. The blind reader returns a `claim_deltas` list (claim-level
differences, quote-anchored) + an `uncertain` list; the skill's gate computes the verdict from
them WITHOUT the mapping — any claim that differs means the edit changed meaning, in either
direction (claim_deltas non-empty -> DRIFT; empty-but-uncertain -> escalate to the human read;
empty-and-certain -> CLEAN). The reader judges "claim-delta vs pure repackaging" (the irreducible,
out-of-model meaning call); the gate just rolls the lists up. The A/B <-> original/edit key is
needed ONLY to NAME a delta for the human report and the Step-2 return (which phrase the edit
changed), never for the pass/fail call. So even the consuming model never needs the mapping to gate.

Hard scope (the executor-fit split — do NOT violate):
  - NO model call. Pure stdlib. The JUDGMENT (the claim-diff) is the blind reader's, out-of-model.
    This harness does ONLY the deterministic blinding I/O: assign A/B, withhold the key, emit the
    brief. It never characterizes meaning.
  - The blind reader is NOT this harness — it is a separate model call (or a human) with no
    access to the rewrite's reasoning or to which text is the edit, spawned by the skill on
    --apply and pointed ONLY at the brief file.

Cross-platform: pure Python 3.8+ standard library. No pip install, no third-party deps.
  macOS / Linux:  python3 blind_meaning_confirm.py --original orig.txt --edited edit.txt \\
                      --brief-out brief.txt --key-out key.json
  Windows:        py -3   blind_meaning_confirm.py --original orig.txt --edited edit.txt ^
                      --brief-out brief.txt --key-out key.json
  inline text:    --text-original "..."  --text-edited "..."   (instead of the two file args)
  H1 diff brief:  add --diff  ->  the diff-anchored brief (word-level A/B diff + forced per-change
                  claim-vs-repackaging classify — the hardening for a drift BURIED among clean changes)
  reveal mapping: python3 blind_meaning_confirm.py --reveal --key key.json

Implements leg-(d) of the Readability-Editing Methodology (§6 the gate). The --diff (H1) mode
hardens the plain brief against a subtle qualifier drop BURIED among clean readability changes —
see the DIFF_BRIEF_TEMPLATE comment block below. The blind reader's output should be spot-checked
for form (every claim-delta carries a verbatim anchor present in the texts) without re-deriving
its substance — re-deriving the diff is the self-certification this harness exists to prevent.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
from collections import Counter

# ---------------------------------------------------------------------------
# The blind-reader brief — a FIXED, SYMMETRIC template (the model does not author it).
# It NEVER names which text is the original or the edit. It forces a bidirectional,
# quote-anchored claim-diff (quote-first grounding: every claim carries a verbatim anchor)
# so a "no drift" verdict cannot be a bare rubber-stamp and a drift claim cannot be fabricated.
# No literal { } braces below except the two .format placeholders {text_a} / {text_b}.
# ---------------------------------------------------------------------------
BRIEF_TEMPLATE = """\
# Blind meaning-preservation confirm — claim-by-claim cold read

You are an INDEPENDENT reader. Below are two texts, **Text A** and **Text B** — two versions of
the same passage. You are NOT told which came first or which was edited; that is deliberate, and
you must not guess or assume it. Treat them symmetrically.

YOUR JOB: enumerate every CLAIM-LEVEL difference between the two texts, in BOTH directions, COLD.
A "claim" is something a text asserts about the world: a fact, a qualifier or hedge, a condition,
a quantity, a date, a named entity, a citation, a causal / temporal / modal / purposive relation,
or an existence / novelty assertion. You are checking ONE thing only — do the two texts assert
the SAME claims? Not which is better, clearer, or easier. Only same-claims, yes or no, per claim.

WHAT IS A CLAIM-DELTA (list it):
  - a claim, qualifier, hedge, or condition ADDED on one side or DROPPED on the other;
  - a changed quantity, date, name, or citation;
  - a definite -> indefinite / existence shift: "the X" -> "a new X" ADDS a novelty/existence
    claim (the second asserts the X is *new*; the first does not) — this IS a delta;
  - a factual -> purposive / aspectual / modal shift: "X describes Y" -> "X to describe Y"
    (asserts a fact vs states a purpose), "may" -> "will", "is" -> "should" — these ARE deltas;
  - a claim present on one side, absent on the other.

WHAT IS NOT A CLAIM-DELTA (do NOT list it, and do NOT put it under "uncertain"): pure SYNTACTIC
REPACKAGING that preserves every claim — clause reordering, active <-> passive, a participial
clause <-> a finite clause, splitting or joining sentences, fronting a time phrase, or a synonym
with identical denotation. A readability edit is SUPPOSED to repackage; repackaging that keeps all
claims is exactly what must pass clean. Reporting it is the over-flagging failure — do not.

QUOTE-FIRST (mandatory): for EACH claim-delta, quote the exact phrase from Text A and from Text B,
verbatim, with a little surrounding context. A delta with no verbatim anchor will be rejected. If
a claim is genuinely on only one side, quote that side and write "(absent in the other text)".

THINK BEFORE YOU CONCLUDE. Walk both texts claim by claim. Do NOT return "equivalent" just because
they read similarly — a fluent rewrite that quietly changed a claim is the exact failure this read
exists to catch (a real edit once shifted "the language describes" to "a new language to describe"
and the writer called it equivalent; it was not — "a new" added a novelty claim and "to describe"
turned a fact into a purpose). Hold that bar.

--- TEXT A ---
{text_a}

--- TEXT B ---
{text_b}

RETURN your findings in EXACTLY this structure (so they can be consumed mechanically):

claim_deltas:
  - kind: <added|dropped|altered|qualifier-changed|number-or-name-changed|modal-or-purposive-shift|definite-indefinite-or-novelty-shift>
    text_a: "<verbatim quote from Text A, or (absent in Text A)>"
    text_b: "<verbatim quote from Text B, or (absent in Text B)>"
    note: <one line — which claim changed>
  - ...    (leave this list EMPTY if the two texts assert exactly the same claims)
uncertain:
  - <a claim you suspect MAY have changed but genuinely cannot resolve from the two texts alone;
     do NOT put pure syntactic repackaging here. Leave empty if none.>
"""


def assignment(original: str, edited: str, seed=None):
    """Return (text_a, text_b, mapping).

    Deterministic: same inputs (+ same seed) -> same assignment, so tests and re-runs are
    reproducible. Content-hash default (sha256, NOT Python's per-process-salted hash()) so the
    edit does not always land in the same slot across different pieces — that defeats a blind
    reader's positional / acquiescence bias ("the second one is always the edit"). A --seed
    override forces a specific assignment for tests / smoke runs.
    """
    if seed is None:
        h = hashlib.sha256((original + "\x00" + edited).encode("utf-8")).hexdigest()
        parity = int(h, 16) % 2
    else:
        parity = int(seed) % 2
    if parity == 0:
        return original, edited, {"A": "original", "B": "edited"}
    return edited, original, {"A": "edited", "B": "original"}


def build_brief(text_a: str, text_b: str) -> str:
    return BRIEF_TEMPLATE.format(text_a=text_a.strip(), text_b=text_b.strip())


# ---------------------------------------------------------------------------
# THE DIFF-ANCHORED BRIEF (H1) — the hardening against a drop BURIED among clean changes.
#
# The plain brief (above) asks the reader to notice claim-drift by holistic re-reading. Testing
# proved that fails on a subtle qualifier drop BURIED among clean readability changes (a dropped
# "up to" cap-qualifier lost among 6 legit repackagings — best-of-3 blind readers 0/3, a SILENT
# ship; the misses correlate, so best-of-N does not rescue it). H1 removes the failure mode
# STRUCTURALLY: it hands the reader a mechanically-computed, word-level enumeration of the exact
# differences and FORCES a per-change "claim-change vs repackaging" classification — a dropped
# qualifier that is one of the enumerated items cannot be skipped by holistic attention loss.
#
# An earlier prototype validated the forcing function on a COARSE, phrase-level difflib pass
# (split-on-whitespace, whole-opcode chunks). Its honest edge: when a drift sits INSIDE a large
# reworded/reordered chunk, the coarse diff bracketed it with its neighbors and the reader had to
# spot it WITHIN the chunk — the weakness this word-level build fixes.
#
# The fix is a TWO-VIEW word-level diff, both computed deterministically and SYMMETRICALLY (Text A /
# Text B — the original<->edit mapping is never revealed; the diff cannot tell which side is the edit):
#   * PART 1 — order-preserving word+punctuation opcodes (difflib), with local context. Catches a
#     reorder that CHANGES the claim ("more common in A than in B" -> "...in B than in A": same words,
#     reversed claim — PART 2 is blind to it because the multiset is unchanged; PART 1 is not).
#   * PART 2 — the ORDER-INDEPENDENT net residue: words present in Text A but net-absent in Text B
#     (dropped) and vice-versa (added), grouped into contiguous phrase-runs. THIS is the fine-grained
#     isolation: a "up to" dropped inside a heavily reworded+reordered clause still surfaces here as a
#     discrete run «up to», because a multiset difference does not care that difflib bracketed it into
#     a coarse chunk. The two views are complementary — PART 1 gives position + catches meaning-bearing
#     reorders; PART 2 guarantees a buried/moved drop cannot hide.
#
# Blinding is preserved end-to-end: tokenization + difflib + multiset are pure functions of the two
# (already-blinded) texts; nothing in the diff references "original"/"edit". Cross-platform stdlib only.
# ---------------------------------------------------------------------------
DIFF_BRIEF_TEMPLATE = """\
# Blind meaning-preservation confirm — DIFF-ANCHORED claim-by-claim cold read

You are an INDEPENDENT reader. Below are two texts, **Text A** and **Text B** — two versions of the
same passage. You are NOT told which came first or which was edited; that is deliberate, and you must
not guess or assume it. Treat them symmetrically.

Below the two texts is a NUMBERED, mechanically-computed enumeration of the EXACT differences between
Text A and Text B (you did NOT author it). YOUR JOB: for EVERY numbered item, decide whether it is a
CLAIM-CHANGE or pure REPACKAGING — then list every claim-change. You MUST classify EVERY numbered item
(PART 1 and PART 2); do not skip any, however small.

A CLAIM-CHANGE (list it): a claim, qualifier, hedge, condition, quantity, date, name, citation, or
causal / temporal / modal / purposive relation ADDED, DROPPED, or ALTERED between the two texts.
  - Dropping or adding a HEDGE or QUALIFIER changes the assertion and IS a claim-change: "in large
    part X" vs "X" (partial vs absolute), "up to N" vs "N" (a ceiling vs a fixed amount), "more common
    in A than in B" vs "more common in A" (a comparison vs an unanchored claim), "sufficiently capable"
    vs "capable" (a threshold vs none), "may" vs "will", "the X" vs "a new X" (novelty added).
  - A changed quantity / date / name / citation IS a claim-change.
  - A REORDER that CHANGES the assertion IS a claim-change: "more common in A than in B" vs "more
    common in B than in A" uses the same words but reverses the claim — PART 1 (order-preserving) is
    where you catch these; PART 2 will look empty for them because the word-set did not change.

PURE REPACKAGING (NOT a claim-change, and NOT "uncertain"): a clause reorder that PRESERVES the
assertion, active <-> passive, participial <-> finite, splitting or joining sentences, fronting a time
phrase, punctuation, or a synonym with identical denotation. A readability edit is SUPPOSED to
repackage; repackaging that keeps every claim is what must pass clean. Do not report it.

--- TEXT A ---
{text_a}

--- TEXT B ---
{text_b}

--- THE EXACT DIFFERENCES (Text A <-> Text B) — you MUST classify EVERY numbered item ---
{diff_block}

RETURN in EXACTLY this structure (so it can be consumed mechanically):

change_classifications:
  - <item id, e.g. P1.1 or D2 or A1>: <claim-change | repackaging> — <one-line reason>
  - ...    (one line for EVERY numbered item in PART 1 and PART 2 above)
claim_deltas:
  - kind: <added|dropped|altered|qualifier-changed|number-or-name-changed|modal-or-purposive-shift|definite-indefinite-or-novelty-shift|reorder-changes-claim>
    text_a: "<verbatim quote from Text A, or (absent in Text A)>"
    text_b: "<verbatim quote from Text B, or (absent in Text B)>"
    note: <one line — which claim changed>
  - ...    (leave EMPTY if every numbered item is pure repackaging)
uncertain:
  - <an item you genuinely cannot resolve; do NOT put pure repackaging here. Empty if none.>
"""

# Word OR single punctuation char. Unicode-aware (\w matches ç/á/… for PT). Splitting punctuation off
# words ("transaction." -> "transaction", ".") is load-bearing: it lets difflib recognize a shared word
# whose only difference is an attached comma/period, so a genuine dropped qualifier next to it falls out
# as a discrete opcode instead of being fused into a coarse replace.
_TOKEN_RE = re.compile(r"\w+|[^\w\s]", re.UNICODE)


def _tokenize(text: str):
    """Return (display_tokens, match_keys). Display keeps original case for quoting; keys are casefolded
    so alignment is not fooled by a capitalization change from fronting ("Annually," vs "annually")."""
    disp = _TOKEN_RE.findall(text)
    keys = [t.casefold() for t in disp]
    return disp, keys


def _has_word(run: str) -> bool:
    """A phrase-run worth surfacing contains at least one word token — drop bare-punctuation residue
    (a moved comma/period is never a claim-change and only adds noise)."""
    return bool(re.search(r"\w", run, re.UNICODE))


def _context(disp, i1, i2, width=4) -> str:
    """A short window around disp[i1:i2] with the changed span marked ⟦…⟧, for the reader to locate it."""
    lo, hi = max(0, i1 - width), min(len(disp), i2 + width)
    before = " ".join(disp[lo:i1])
    span = " ".join(disp[i1:i2])
    after = " ".join(disp[i2:hi])
    ell_l = "…" if lo > 0 else ""
    ell_r = "…" if hi < len(disp) else ""
    mid = f"⟦{span}⟧" if span else "⟦∅⟧"
    return " ".join(p for p in (f"{ell_l}{before}".strip(), mid, f"{after}{ell_r}".strip()) if p)


def _residue_runs(disp, keys, residual: Counter):
    """Walk the token stream; group maximal consecutive tokens still 'owed' by the residual multiset
    into contiguous phrase-runs (raw display text). Consuming from the counter handles duplicates
    correctly (two "the"s in A, one in B -> exactly one "the" is net-dropped)."""
    owed = Counter(residual)
    runs, cur = [], []
    for tok, key in zip(disp, keys):
        if owed.get(key, 0) > 0:
            owed[key] -= 1
            cur.append(tok)
        elif cur:
            runs.append(" ".join(cur))
            cur = []
    if cur:
        runs.append(" ".join(cur))
    return [r for r in runs if _has_word(r)]


def fine_diff(text_a: str, text_b: str) -> dict:
    """Word-level, fine-granularity, SYMMETRIC diff of two texts. Returns a structured dict:
      positional  — order-preserving opcodes: [{kind: removed|added|substituted, a, b, a_ctx, b_ctx}]
      dropped_runs — phrase-runs present in Text A, net-absent in Text B (order-independent residue)
      added_runs   — phrase-runs present in Text B, net-absent in Text A

    The residue lists are the H1 hardening: a qualifier dropped INSIDE a reworded/reordered clause is
    a discrete run here even when the positional view brackets it into a coarser chunk. Deterministic
    (pure difflib + multiset over deterministic tokenization); symmetric (swapping A/B swaps
    dropped<->added and mirrors the opcodes) — nothing distinguishes original from edit."""
    disp_a, keys_a = _tokenize(text_a)
    disp_b, keys_b = _tokenize(text_b)
    sm = difflib.SequenceMatcher(a=keys_a, b=keys_b, autojunk=False)
    _KIND = {"delete": "removed", "insert": "added", "replace": "substituted"}
    positional = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        positional.append({
            "kind": _KIND[tag],
            "a": " ".join(disp_a[i1:i2]),
            "b": " ".join(disp_b[j1:j2]),
            "a_ctx": _context(disp_a, i1, i2) if i2 > i1 else "",
            "b_ctx": _context(disp_b, j1, j2) if j2 > j1 else "",
        })
    dropped = Counter(keys_a) - Counter(keys_b)   # multiset diff: keys net-present in A
    added = Counter(keys_b) - Counter(keys_a)
    return {
        "positional": positional,
        "dropped_runs": _residue_runs(disp_a, keys_a, dropped),
        "added_runs": _residue_runs(disp_b, keys_b, added),
    }


def render_diff(text_a: str, text_b: str) -> str:
    """Render fine_diff() as the numbered PART 1 / PART 2 block the diff-anchored brief embeds."""
    d = fine_diff(text_a, text_b)
    lines = ["PART 1 — word-level changes in reading order (⟦…⟧ marks the changed span):"]
    if d["positional"]:
        for n, c in enumerate(d["positional"], 1):
            if c["kind"] == "removed":
                lines.append(f"  P1.{n}. REMOVED — in Text A, not Text B: «{c['a']}»")
                lines.append(f"          Text A: \"{c['a_ctx']}\"")
            elif c["kind"] == "added":
                lines.append(f"  P1.{n}. ADDED — in Text B, not Text A: «{c['b']}»")
                lines.append(f"          Text B: \"{c['b_ctx']}\"")
            else:
                lines.append(f"  P1.{n}. SUBSTITUTED — Text A «{c['a']}» ↔ Text B «{c['b']}»")
                lines.append(f"          Text A: \"{c['a_ctx']}\"    Text B: \"{c['b_ctx']}\"")
    else:
        lines.append("  (no order-preserving changes)")
    lines.append("")
    lines.append("PART 2 — net word-level residue (ORDER-INDEPENDENT): a word or qualifier dropped/added")
    lines.append("INSIDE a reworded or reordered clause surfaces here as a DISCRETE item even when PART 1")
    lines.append("bundles it into a larger chunk. Classify each.")
    lines.append("  dropped — present in Text A, net-absent in Text B:")
    if d["dropped_runs"]:
        for n, r in enumerate(d["dropped_runs"], 1):
            lines.append(f"        D{n}. «{r}»")
    else:
        lines.append("        (none)")
    lines.append("  added — present in Text B, net-absent in Text A:")
    if d["added_runs"]:
        for n, r in enumerate(d["added_runs"], 1):
            lines.append(f"        A{n}. «{r}»")
    else:
        lines.append("        (none)")
    return "\n".join(lines)


def build_diff_brief(text_a: str, text_b: str) -> str:
    """The diff-anchored (H1) brief: the two blinded texts + the numbered word-level diff + the forced
    per-change claim-vs-repackaging classification. Symmetric; never names which text is the edit."""
    return DIFF_BRIEF_TEMPLATE.format(
        text_a=text_a.strip(), text_b=text_b.strip(), diff_block=render_diff(text_a, text_b))


def build_key(original: str, edited: str, mapping: dict, seed) -> dict:
    return {
        "mapping": mapping,  # which of A/B is the original vs the edit
        "seed": seed,
        "sha_original": hashlib.sha256(original.encode("utf-8")).hexdigest()[:16],
        "sha_edited": hashlib.sha256(edited.encode("utf-8")).hexdigest()[:16],
        "WARNING": "The blind reader must NEVER see this file. It is the A/B answer key, used "
                   "only to NAME a drift for the human report / the Step-2 return — the pass/fail "
                   "call (computed from the reader's claim_deltas list) does not need it.",
    }


def reveal(key: dict) -> str:
    m = key["mapping"]
    return (
        "blind-confirm reveal — A/B answer key\n"
        f"  Text A = {m['A']}\n"
        f"  Text B = {m['B']}\n"
        "(Map the blind reader's Text-A / Text-B references through this to name which text "
        "is the edit. The claim_deltas-based drift decision did NOT use this key.)"
    )


def _read_source(file_arg, text_arg, label):
    """Resolve a text from either a file path ('-' = stdin) or an inline --text arg."""
    if text_arg is not None:
        return text_arg
    if file_arg is None:
        sys.exit(f"error: provide --{label} <file> or --text-{label} \"...\"")
    if file_arg == "-":
        return sys.stdin.read()
    with open(file_arg, encoding="utf-8") as fh:
        return fh.read()


def main(argv):
    p = argparse.ArgumentParser(
        description="Deterministic blinding harness for the /edit skill's out-of-model "
                    "blind meaning-confirm (leg-(d)). Emits a blinded brief + a withheld key.",
    )
    p.add_argument("--original", help="path to the ORIGINAL text ('-' for stdin)")
    p.add_argument("--edited", help="path to the EDITED text ('-' for stdin)")
    p.add_argument("--text-original", dest="text_original", help="inline original text")
    p.add_argument("--text-edited", dest="text_edited", help="inline edited text")
    p.add_argument("--brief-out", dest="brief_out",
                   help="write the blinded brief here (the blind reader reads ONLY this). "
                        "Default: stdout.")
    p.add_argument("--key-out", dest="key_out",
                   help="write the withheld A/B key here (the blind reader must NEVER see it).")
    p.add_argument("--seed", type=int, default=None,
                   help="force the A/B assignment parity (default: content-hash, reproducible).")
    p.add_argument("--diff", action="store_true",
                   help="emit the DIFF-ANCHORED (H1) brief — a word-level A/B diff + a forced per-change "
                        "claim-vs-repackaging classify (the hardening for a subtle drift buried among "
                        "clean changes). Default: the holistic-read brief.")
    p.add_argument("--reveal", action="store_true",
                   help="reveal mode: print the A/B<->original/edit mapping from --key.")
    p.add_argument("--key", help="(reveal mode) path to the key file to reveal.")
    args = p.parse_args(argv[1:])

    if args.reveal:
        if not args.key:
            sys.exit("error: --reveal requires --key <keyfile>")
        with open(args.key, encoding="utf-8") as fh:
            print(reveal(json.load(fh)))
        return 0

    original = _read_source(args.original, args.text_original, "original")
    edited = _read_source(args.edited, args.text_edited, "edited")

    if original.strip() == edited.strip():
        sys.stderr.write(
            "warning: original and edited texts are identical — no edit to confirm; "
            "the blind read will return 'no drift' trivially.\n"
        )

    text_a, text_b, mapping = assignment(original, edited, args.seed)
    brief = build_diff_brief(text_a, text_b) if args.diff else build_brief(text_a, text_b)
    key = build_key(original, edited, mapping, args.seed)

    if args.brief_out:
        with open(args.brief_out, "w", encoding="utf-8") as fh:
            fh.write(brief)
        sys.stderr.write(f"blinded brief -> {args.brief_out}\n")
    else:
        print(brief)

    if args.key_out:
        with open(args.key_out, "w", encoding="utf-8") as fh:
            json.dump(key, fh, ensure_ascii=False, indent=2)
        sys.stderr.write(f"withheld key  -> {args.key_out}  (do NOT show this to the blind reader)\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
