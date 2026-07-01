#!/usr/bin/env python3
"""readability_diag.py — the deterministic, no-model readability diagnostic for the /edit skill.

This is the DETERMINISTIC EXECUTOR half of the /edit skill's executor-fit split (see the
Readability-Editing Methodology §3): the countable signals a model should NOT be trusted to
compute go here, in plain stdlib code. The judgment half (intrinsic-vs-extraneous, the
generative rewrite, information-density/recovery) stays model-side in the skill. This tool
emits a FLAG LIST — never a verdict to optimize toward (methodology §1: a score is a flag
that says "look here", never the target).

What it emits (methodology §3):
  - Readability scores (Flesch-Kincaid grade, Gunning Fog) — FLAGS ONLY, never targets.
  - Sentence-length variance (mean/SD/variance/CV) — the Lever-4 RHYTHM/MONOTONE flag.
    NOT the recovery/information-density signal, which is model-assisted and lives in the
    skill (methodology §3 Lever 4: "two distinct signals, two distinct instruments — do
    not conflate them"). This tool computes ONLY the deterministic rhythm half.
  - Nominalization density (-tion EN / -ção PT per 100 words) — Lever-1 HINT (weak both ways).
  - Term-frequency surface — input to the model-side synonym-cycling judgment (Lever 3/6).
  - Repeated-device (antithesis / negation-assertion) count — Lever-5, WHOLE-PIECE.
  - Subject-verb gap estimate — Lever-3, a low-precision heuristic ESTIMATE.

THE LOAD-BEARING REQUIREMENT (B4). Every sentence-segmentation-dependent signal carries a
`parse_confidence`. A naive sentence splitter already produced a FALSE "harder" verdict in
testing — a period-inside-closing-quote (`leakage."`) merged two
sentences and inflated the length stats. So below a confidence threshold this tool WITHHOLDS
the deterministic verdict ("unmeasured") rather than emit a confident wrong number. Leg-(a)
of the gate is non-forgeable ONLY on a high-confidence parse; on a low-confidence parse it
abstains and the model's §4 judgment carries.

Hard scope (the executor-fit split — do NOT violate):
  - NO model call. Pure stdlib. This is the deterministic executor; that is the whole point.
  - NOT the meaning-preservation gate (leg-d) — that is structurally out-of-model, wired
    separately (see blind_meaning_confirm.py). This tool does the leg-(a)-style countables only.

Cross-platform: pure Python 3.8+ standard library. No pip install, no third-party deps.
  macOS / Linux:  python3 readability_diag.py path/to/file.md
  Windows:        py -3   readability_diag.py path\\to\\file.md
  (also reads --text "..." or piped stdin; --json for the skill-consumable contract)

Implements the deterministic leg of the Readability-Editing Methodology (§3 the levers,
§6 the gate). Emits flags for the model to adjudicate; it never characterizes meaning.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass, field, asdict

# ---------------------------------------------------------------------------
# Tunables (all flags, never targets — methodology §1)
# ---------------------------------------------------------------------------
PARSE_CONFIDENCE_THRESHOLD = 0.75   # below this, sentence-based VERDICTS are withheld (B4)
MONOTONE_CV_MAX = 0.30              # CV below this on >=4 sentences => possible monotone (rhythm flag)
MIN_SENTENCES_FOR_RHYTHM = 4        # below this, rhythm/variance is not reliably assessable
SV_GAP_WORDS = 8                    # an intercalation longer than this before the verb => candidate (Lever 3)
LONG_SENTENCE_WORDS = 60            # a "sentence" longer than this is suspicious => parse penalty
TERM_FREQ_REPEAT_THRESHOLD = 5      # a content word repeated >= this is surfaced for the cycling judgment

# Vowel sets for the syllable heuristic (FK/Fog are EN-calibrated; PT is approximate-by-design).
VOWELS_EN = set("aeiouy")
VOWELS_PT = set("aeiouyáàâãéêíóôõúü")

# Abbreviations whose trailing period is NOT a sentence boundary. A period after one of these
# that is FOLLOWED BY A CAPITAL is genuinely ambiguous => it costs parse_confidence.
ABBREV = {
    # EN
    "mr", "mrs", "ms", "dr", "prof", "st", "jr", "sr", "vs", "etc", "eg", "ie",
    "inc", "ltd", "co", "no", "vol", "fig", "al", "approx", "dept", "est",
    # PT
    "nº", "art", "arts", "inc", "sra", "dra", "ltda", "cia", "av", "esq", "fls",
    "res", "resol", "cf", "pág", "p", "ed", "nos", "obs",
}

# -tion-family suffixes (broad nominalization hint — Lever 1). The PRIMARY metric matches the
# primary column (-tion EN / -ção PT per 100w); the broad set is a secondary signal.
EN_NOMINAL_SUFFIXES = ("tion", "tions", "sion", "sions", "ment", "ments",
                       "ance", "ances", "ence", "ences", "ity", "ities", "ness", "nesses")
PT_NOMINAL_SUFFIXES = ("ção", "ções", "mento", "mentos", "dade", "dades",
                       "ância", "ância", "ência", "ências", "agem", "agens")

EN_STOPWORDS = set("""a an the and or but nor for so yet of to in on at by with from as is are was
were be been being it its this that these those he she they them his her their we us our you your i
me my not no do does did has have had will would can could should may might must than then there here
which who whom whose what when where why how all any each few more most other some such only own same
into over under again further out up down off above below between through during before after about
""".split())
PT_STOPWORDS = set("""o a os as um uma uns umas de do da dos das em no na nos nas por para com sem sob
sobre que e ou mas nem se ao aos à às pelo pela pelos pelas como quando onde porque já não sim seu sua
seus suas este esta esse essa aquele aquela isto isso aquilo ser estar ter haver foi são é era
aqui ali lá entre até desde após antes durante muito mais menos também""".split())


# ---------------------------------------------------------------------------
# Result containers
# ---------------------------------------------------------------------------
@dataclass
class Flag:
    """One diagnostic flag. `value` is the measurement; `verdict` interprets it (or 'unmeasured')."""
    name: str
    lever: int | None
    instrument: str
    value: object
    verdict: str
    confidence_gated: bool      # does this flag depend on sentence segmentation?
    note: str = ""


@dataclass
class DiagResult:
    language: str = "en"
    language_source: str = "auto"
    words: int = 0
    sentences: int = 0
    parse_confidence: float = 0.0
    parse_confidence_threshold: float = PARSE_CONFIDENCE_THRESHOLD
    sentence_segmentation: str = "trusted"      # trusted | low_confidence | degenerate
    parse_notes: list = field(default_factory=list)
    excluded: dict = field(default_factory=dict)
    flags: list = field(default_factory=list)
    withheld: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# Markdown -> prose (light, conservative; --raw skips it)
# ---------------------------------------------------------------------------
_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+", re.MULTILINE)
_BLOCKQUOTE_RE = re.compile(r"^\s{0,3}>\s?", re.MULTILINE)
_LIST_RE = re.compile(r"^\s{0,3}(?:[-*+]\s+|\d+[.)]\s+)", re.MULTILINE)
_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_EMPH_RE = re.compile(r"(\*\*|\*|__|_|`)")


def strip_markdown(text: str) -> tuple[str, int]:
    """Strip markdown formatting while preserving sentence text. Returns (prose, code_blocks_dropped)."""
    code_blocks = len(_FENCE_RE.findall(text))
    text = _FENCE_RE.sub(" ", text)
    text = _LINK_RE.sub(r"\1", text)
    text = _HEADING_RE.sub("", text)
    text = _BLOCKQUOTE_RE.sub("", text)
    text = _LIST_RE.sub("", text)
    text = _EMPH_RE.sub("", text)
    return text, code_blocks


# ---------------------------------------------------------------------------
# Tokenization — the load-bearing part (B4)
# ---------------------------------------------------------------------------
_WORD_RE = re.compile(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'’-]*")
# A boundary candidate: terminal punct, optional closing quote/paren, whitespace.
# This is the CAREFUL splitter — it knows the closing-quote case that broke the naive measure.py.
_BOUNDARY_RE = re.compile(r'([.!?…]+)(["”’\')\]]*)(\s+|$)')
_ALNUM_PERIOD_ALNUM = re.compile(r"\w\.\w")          # decimals, thousands sep, code tokens (conftest.py)


def words_of(text: str) -> list[str]:
    return _WORD_RE.findall(text)


def _naive_sentence_count(text: str) -> int:
    """A deliberately NAIVE splitter (split on terminal punct + space). Used only to detect
    divergence from the careful splitter — large divergence => the text has tokenization traps."""
    parts = re.split(r"[.!?]+\s+", text.strip())
    return len([p for p in parts if p.strip()])


def split_sentences(text: str) -> tuple[list[str], float, list[str]]:
    """Careful sentence segmentation with a parse_confidence (B4).

    Returns (sentences, parse_confidence, notes). The confidence falls on RESIDUAL, unresolved
    ambiguity (abbreviation-before-capital, ellipses, degenerate ultra-long sentences, missing
    terminal punctuation, and large naive/careful divergence) — NOT on traps the splitter
    resolves cleanly (decimals, code tokens, closing-quote boundaries), which are handled and
    therefore confident.
    """
    notes: list[str] = []
    ambiguous = 0.0

    sentences: list[str] = []
    start = 0
    for m in _BOUNDARY_RE.finditer(text):
        punct_start = m.start()
        # Is the period part of an alnum.alnum token (decimal / thousands / code)? Not a boundary.
        ctx = text[max(0, punct_start - 1):punct_start + 2]
        if _ALNUM_PERIOD_ALNUM.search(ctx) and m.group(1) == ".":
            continue
        # Token immediately before the punctuation, lowercased, stripped of nº-style tails.
        before = text[start:punct_start]
        last_tok = (before.split() or [""])[-1].strip("\"'([{").lower()
        last_tok_alpha = re.sub(r"[^a-zà-ÿº]", "", last_tok)
        nxt = text[m.end():m.end() + 1]
        # Dotted initialism / corporate form: "S.A.", "U.S.", "Ph.D", "e.g" — the internal periods
        # are not sentence ends. (This caught a false split of a statutory legal sentence at "S.A.".)
        is_initialism = bool(re.match(r"^([a-zà-ÿ]\.){1,}[a-zà-ÿ]?$", last_tok))

        if (last_tok_alpha in ABBREV or is_initialism) and m.group(1) == ".":
            # Abbreviation / initialism. If followed by a capital it's genuinely ambiguous (could be
            # a real sentence end, e.g. "...made in the U.S. The next..."). Treat as NON-boundary
            # but pay a confidence cost — the safe direction (B4: discount, don't confidently split).
            if nxt and (nxt.isupper() or nxt.isdigit()):
                ambiguous += 1.0
            continue

        if "…" in m.group(1) or m.group(1).count(".") >= 3:
            # Ellipsis: ambiguous as a terminal. Take the boundary but flag it.
            ambiguous += 0.5

        # A real boundary requires the next char to start a new sentence (capital / digit / quote
        # / end). Lowercase next => suspicious (likely an unlisted abbreviation) — non-boundary + cost.
        if nxt and nxt.islower():
            ambiguous += 1.0
            continue

        seg = text[start:m.end()].strip()
        if seg:
            sentences.append(seg)
        start = m.end()

    tail = text[start:].strip()
    if tail:
        sentences.append(tail)
        if not re.search(r"[.!?…]\s*$", tail) and len(words_of(tail)) > 3:
            # Trailing prose with no terminal punctuation — could be a dropped boundary.
            ambiguous += 0.5
            notes.append("input ends without terminal punctuation")

    n = len(sentences)
    if n == 0:
        return [], 0.0, ["no sentences found"]

    # Degenerate ultra-long "sentences" suggest a missed split.
    over_long = [s for s in sentences if len(words_of(s)) > LONG_SENTENCE_WORDS]
    if over_long:
        # One genuinely-long statutory sentence (compliance 3a) is legitimate, so penalize lightly
        # and only note it; many over-long => stronger signal of merge errors.
        ambiguous += 0.5 * len(over_long)
        notes.append(f"{len(over_long)} sentence(s) over {LONG_SENTENCE_WORDS} words (possible missed split or intrinsic length)")

    # Divergence between the careful and a naive splitter => the text contains traps the careful
    # splitter had to resolve. Surfacing this is conservative: even when we're probably right,
    # heavy resolution work raises the risk, so we discount confidence (B4 belt-and-suspenders).
    naive_n = _naive_sentence_count(text)
    divergence = abs(naive_n - n)
    if divergence:
        ambiguous += min(divergence, 4) * 0.5
        notes.append(f"naive splitter would see {naive_n} sentences vs {n} careful (tokenization traps present)")

    confidence = max(0.0, 1.0 - 0.12 * ambiguous)
    confidence = min(1.0, confidence)
    return sentences, round(confidence, 3), notes


# ---------------------------------------------------------------------------
# Language detection
# ---------------------------------------------------------------------------
def detect_language(words: list[str]) -> str:
    if not words:
        return "en"
    lw = [w.lower() for w in words]
    pt_hits = sum(1 for w in lw if w in PT_STOPWORDS)
    en_hits = sum(1 for w in lw if w in EN_STOPWORDS)
    # PT diacritics / ç are a strong tell.
    diacritic = sum(1 for w in lw if re.search(r"[áàâãéêíóôõúüç]", w))
    return "pt" if (pt_hits + 2 * diacritic) > en_hits else "en"


# ---------------------------------------------------------------------------
# Syllables + readability scores (FLAGS ONLY)
# ---------------------------------------------------------------------------
def count_syllables(word: str, lang: str) -> int:
    w = word.lower()
    w = re.sub(r"[^a-zà-ÿ]", "", w)
    if not w:
        return 0
    vowels = VOWELS_PT if lang == "pt" else VOWELS_EN
    count = 0
    prev_vowel = False
    for ch in w:
        is_v = ch in vowels
        if is_v and not prev_vowel:
            count += 1
        prev_vowel = is_v
    if lang == "en" and w.endswith("e") and count > 1:
        count -= 1  # silent trailing e
    return max(1, count)


def flesch_kincaid_grade(n_words: int, n_sentences: int, n_syllables: int) -> float:
    if n_words == 0 or n_sentences == 0:
        return 0.0
    return 0.39 * (n_words / n_sentences) + 11.8 * (n_syllables / n_words) - 15.59


def gunning_fog(n_words: int, n_sentences: int, n_complex: int) -> float:
    if n_words == 0 or n_sentences == 0:
        return 0.0
    return 0.4 * ((n_words / n_sentences) + 100.0 * (n_complex / n_words))


def is_complex(word: str, lang: str) -> bool:
    """Gunning-Fog complex word: 3+ syllables, discounting common inflectional suffixes (EN)."""
    syl = count_syllables(word, lang)
    if lang == "en":
        w = word.lower()
        for suf in ("es", "ed", "ing"):
            if w.endswith(suf) and count_syllables(w[: -len(suf)], lang) < 3:
                return False
    return syl >= 3


# ---------------------------------------------------------------------------
# Lever metrics
# ---------------------------------------------------------------------------
def length_stats(sentences: list[str]) -> dict:
    lens = [len(words_of(s)) for s in sentences]
    lens = [l for l in lens if l > 0]
    if not lens:
        return {}
    n = len(lens)
    mean = sum(lens) / n
    variance = sum((l - mean) ** 2 for l in lens) / n   # POPULATION variance (matches measure.py)
    sd = math.sqrt(variance)
    cv = sd / mean if mean else 0.0
    return {
        "n": n,
        "mean": round(mean, 1),
        "sd": round(sd, 1),
        "variance": round(variance, 1),
        "cv": round(cv, 3),
        "longest": max(lens),
        "shortest": min(lens),
    }


def nominalization_density(words: list[str], lang: str) -> dict:
    n = len(words)
    if n == 0:
        return {}
    lw = [w.lower() for w in words]
    if lang == "pt":
        primary_suf, primary_label = ("ção", "ções"), "-ção"
        broad = PT_NOMINAL_SUFFIXES
    else:
        primary_suf, primary_label = ("tion", "tions"), "-tion"
        broad = EN_NOMINAL_SUFFIXES
    primary = sum(1 for w in lw if w.endswith(primary_suf))
    broad_ct = sum(1 for w in lw if w.endswith(broad))
    return {
        "suffix": primary_label,
        "primary_count": primary,
        "primary_per_100w": round(100.0 * primary / n, 2),
        "broad_count": broad_ct,
        "broad_per_100w": round(100.0 * broad_ct / n, 2),
    }


# Negation-assertion / antithesis family (Lever 5, whole-piece). Provost's "not X — it is Y".
_ANTITHESIS_RES = [
    re.compile(r"\bis\s+not\b[^.!?;—–]{1,70}?[.;:—–]\s*[Ii]t['’]?s?\s+(?:is\s+)?", re.IGNORECASE),
    re.compile(r"\bnot\s+(?:an?|the)\b[^.!?;—–]{1,70}?[.;:—–]\s*[Ii]t['’]?s?\s+", re.IGNORECASE),
    re.compile(r"\b(?:is|are|was|were)\s+not\b[^.!?]{1,60}?\bbut\b", re.IGNORECASE),
    re.compile(r"\bnão\s+é\b[^.!?;—–]{1,70}?[.;:—–]\s*[ÉéeE]", re.IGNORECASE),  # PT "não é X. É Y"
]


def antithesis_scan(text: str) -> dict:
    spans: list[tuple[int, int]] = []
    examples: list[str] = []
    for rgx in _ANTITHESIS_RES:
        for m in rgx.finditer(text):
            s, e = m.span()
            if any(not (e <= a or s >= b) for a, b in spans):
                continue  # overlaps an already-counted device
            spans.append((s, e))
            if len(examples) < 6:
                snippet = re.sub(r"\s+", " ", m.group(0)).strip()
                examples.append(snippet[:80])
    return {"count": len(spans), "examples": examples}


def term_frequency(words: list[str], lang: str, top: int) -> dict:
    stop = PT_STOPWORDS if lang == "pt" else EN_STOPWORDS
    counts: dict[str, int] = {}
    for w in words:
        lw = w.lower()
        if lw in stop or len(lw) < 3:
            continue
        counts[lw] = counts.get(lw, 0) + 1
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    repeated = [[w, c] for w, c in ordered if c >= TERM_FREQ_REPEAT_THRESHOLD]
    return {"top": [[w, c] for w, c in ordered[:top]], "repeated": repeated}


def subject_verb_gaps(sentences: list[str]) -> dict:
    """Low-precision heuristic ESTIMATE of long subject-verb interruptions (Lever 3).

    Detects an early comma/dash-bounded intercalation longer than SV_GAP_WORDS that sits between
    a short capitalized subject and the continuation — the textbook "O Diretor, que ..., terá"
    / "The language emerging ..., describes" shape. Deliberately conservative; reported as an
    estimate, never a verdict.
    """
    candidates = []
    pat = re.compile(r"^\W*([A-ZÀ-Ý][\wÀ-ÿ'’-]*(?:\s+[\wÀ-ÿ'’-]+){0,5}?)\s*([,—–])(.+?)\2\s*(\S+)")
    for s in sentences:
        m = pat.match(s.strip())
        if not m:
            continue
        intercalation = m.group(3)
        gap_words = len(words_of(intercalation))
        if gap_words >= SV_GAP_WORDS:
            candidates.append({
                "subject": re.sub(r"\s+", " ", m.group(1)).strip()[:40],
                "gap_words": gap_words,
                "resumes": re.sub(r"\s+", " ", m.group(4)).strip()[:24],
            })
    return {"count": len(candidates), "candidates": candidates[:8]}


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------
def diagnose(text: str, lang: str | None = None, strip_md: bool = True,
             threshold: float = PARSE_CONFIDENCE_THRESHOLD, top: int = 12) -> DiagResult:
    res = DiagResult(parse_confidence_threshold=threshold)
    code_blocks = 0
    if strip_md:
        text, code_blocks = strip_markdown(text)
    res.excluded = {"code_blocks": code_blocks}

    words = words_of(text)
    res.words = len(words)
    if lang:
        res.language, res.language_source = lang, "forced"
    else:
        res.language, res.language_source = detect_language(words), "auto"

    sentences, confidence, notes = split_sentences(text)
    res.sentences = len(sentences)
    res.parse_confidence = confidence
    res.parse_notes = notes

    # Segmentation status (B4): trusted / low_confidence / degenerate.
    trusted = confidence >= threshold and res.sentences >= 1 and res.words > 0
    if res.words == 0 or res.sentences == 0:
        res.sentence_segmentation = "degenerate"
        trusted = False
    elif not trusted:
        res.sentence_segmentation = "low_confidence"
    else:
        res.sentence_segmentation = "trusted"

    def gate(flag: Flag, value_when_trusted, verdict_when_trusted):
        """Apply B4: emit the value+verdict only on a trusted parse; else 'unmeasured'."""
        if trusted:
            flag.value = value_when_trusted
            flag.verdict = verdict_when_trusted
        else:
            flag.value = "unmeasured"
            flag.verdict = "unmeasured"
            res.withheld.append(flag.name)
        return flag

    # --- Syllable-dependent scores (need a sentence count => gated) ---
    n_syll = sum(count_syllables(w, res.language) for w in words)
    n_complex = sum(1 for w in words if is_complex(w, res.language))
    fk = round(flesch_kincaid_grade(res.words, max(1, res.sentences), n_syll), 1)
    fog = round(gunning_fog(res.words, max(1, res.sentences), n_complex), 1)

    res.flags.append(gate(
        Flag("readability_score_fk", None, "Flesch-Kincaid grade (FLAG ONLY, never a target)",
             None, "", True,
             "A score is a flag, never optimize to it (methodology §1). Breaks on long single sentences."),
        fk, "flag"))
    res.flags.append(gate(
        Flag("readability_score_fog", None, "Gunning Fog index (FLAG ONLY, never a target)",
             None, "", True, "Flag only; word+sentence length, blind to cohesion/abstraction/order."),
        fog, "flag"))

    # --- Lever 4: sentence-length variance = the RHYTHM/MONOTONE flag (deterministic half only) ---
    stats = length_stats(sentences)
    if not trusted:
        rhythm_verdict = "unmeasured"
    elif res.sentences < MIN_SENTENCES_FOR_RHYTHM:
        rhythm_verdict = f"unmeasured (n<{MIN_SENTENCES_FOR_RHYTHM}; rhythm needs more sentences)"
    elif stats.get("cv", 1.0) < MONOTONE_CV_MAX:
        rhythm_verdict = "possible_monotone (low variance)"
    else:
        rhythm_verdict = "no_monotone (healthy variance)"
    var_flag = Flag(
        "sentence_length_variance", 4, "rhythm/monotone — DETERMINISTIC (Lever 4 first instrument)",
        stats if trusted else "unmeasured", rhythm_verdict, True,
        "Rhythm only. High variance does NOT imply easy prose; the recovery/information-density "
        "half is model-assisted and lives in the skill, NOT here (methodology §3 Lever 4).")
    if not trusted:
        res.withheld.append(var_flag.name)
    res.flags.append(var_flag)

    # --- Lever 3 (estimate): subject-verb gap. Depends on segmentation => gated. ---
    sv = subject_verb_gaps(sentences)
    res.flags.append(gate(
        Flag("subject_verb_gap", 3, "intercalation heuristic — LOW-PRECISION ESTIMATE",
             None, "", True,
             "An estimate, not a verdict: long interruption between subject and verb (Lever 3)."),
        sv, "estimate"))

    # --- Word-level signals (robust to sentence-segmentation; NOT gated) ---
    nom = nominalization_density(words, res.language)
    res.flags.append(Flag(
        "nominalization_density", 1, "suffix-count HINT (weak in both directions)",
        nom, "hint", False,
        "Lever-1 hint only. Mis-fires on plain-worded-but-abstract and on proper-noun-dense "
        "regulated prose — the intrinsic/extraneous judgment gates it, not the count."))

    anti = antithesis_scan(text)
    res.flags.append(Flag(
        "repeated_device_antithesis", 5, "negation-assertion regex count — WHOLE-PIECE",
        anti, "hint", False,
        "Lever-5 whole-piece property: count devices across the whole piece, not a fragment "
        "(B5). 2-3 per section reads fine; the skill gates the fragment-vs-whole-piece scope."))

    tf = term_frequency(words, res.language, top)
    res.flags.append(Flag(
        "term_frequency", None, "content-word frequency SURFACE (input to a model judgment)",
        tf, "surface", False,
        "Synonym-cycling / elegant variation (Lever 3/6) is a MODEL-side judgment; this frequency "
        "surface is its deterministic input, not a cycling verdict."))

    return res


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def render_text(res: DiagResult) -> str:
    out = []
    out.append("readability_diag — deterministic flag list (flags, NOT targets)")
    out.append("=" * 64)
    out.append(f"language: {res.language} ({res.language_source})   words: {res.words}   sentences: {res.sentences}")
    seg = res.sentence_segmentation.upper()
    out.append(f"parse_confidence: {res.parse_confidence}  (threshold {res.parse_confidence_threshold})  -> {seg}")
    for n in res.parse_notes:
        out.append(f"  · {n}")
    if res.excluded.get("code_blocks"):
        out.append(f"  · excluded {res.excluded['code_blocks']} fenced code block(s) from prose")
    if res.withheld:
        out.append(f"WITHHELD (low-confidence parse — B4, model judgment carries): {', '.join(res.withheld)}")
    out.append("-" * 64)
    for f in res.flags:
        lev = f"L{f.lever}" if f.lever else "  "
        out.append(f"[{lev}] {f.name}  ->  {f.verdict}")
        out.append(f"      {f.instrument}")
        if f.value != "unmeasured":
            out.append(f"      value: {json.dumps(f.value, ensure_ascii=False)}")
        if f.note:
            out.append(f"      note: {f.note}")
    return "\n".join(out)


def render_json(res: DiagResult) -> str:
    d = asdict(res)
    return json.dumps(d, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _read_input(args) -> str:
    if args.text is not None:
        return args.text
    if args.path and args.path != "-":
        with open(args.path, encoding="utf-8") as fh:
            return fh.read()
    return sys.stdin.read()


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description="Deterministic readability diagnostic (the /edit skill's no-model executor). "
                    "Emits a flag list with parse_confidence — flags, never targets.")
    p.add_argument("path", nargs="?", help="file to diagnose ('-' or omitted = stdin)")
    p.add_argument("--text", help="diagnose this literal string instead of a file")
    p.add_argument("--lang", choices=("en", "pt"), help="force language (default: auto-detect)")
    p.add_argument("--json", action="store_true", help="emit the skill-consumable JSON contract")
    p.add_argument("--raw", action="store_true", help="do NOT strip markdown formatting first")
    p.add_argument("--threshold", type=float, default=PARSE_CONFIDENCE_THRESHOLD,
                   help=f"parse_confidence floor below which verdicts are withheld (default {PARSE_CONFIDENCE_THRESHOLD})")
    p.add_argument("--top", type=int, default=12, help="how many top content words to surface (default 12)")
    args = p.parse_args(argv)

    try:
        text = _read_input(args)
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    res = diagnose(text, lang=args.lang, strip_md=not args.raw,
                   threshold=args.threshold, top=args.top)
    print(render_json(res) if args.json else render_text(res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
