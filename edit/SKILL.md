---
name: edit
description: >-
  Refine an existing draft to read as easily as its ideas allow — at the grade
  the content earns, never below the floor your audience expects, never inflated
  above it. Runs a diagnose→propose→refine→gate-check methodology: shells out to
  the deterministic readability_diag.py for the countable flags (does NOT
  recompute them), judges intrinsic-vs-extraneous load, proposes refine moves
  with a floor/ceiling check, and on --apply runs the gate it can't game
  (meaning-preservation held outside the rewriter). Read-only default; --apply
  refines + gates. Voice-neutral; composes with a defect/AI-pattern linter and a
  content-drafting skill. TRIGGER when: user says "edit this for readability",
  "make this read easier", "reduce reading effort", "tighten this prose",
  "readability pass", "refine for clarity". DO NOT TRIGGER when: user wants a
  defect / AI-pattern / brand check (use a linter); to draft net-new content (use
  a content-authoring approach); a named-recipient message; or a literal file
  edit (use the editor directly).
version: 0.4.0-share
updated: 1 Jul 2026
attribution: Bamboo DCM (https://bamboodcm.com)
contact: [arthur@bamboodcm.com, felipe@bamboodcm.com, urian@bamboodcm.com]
license: CC-BY-4.0
public-source: https://github.com/bamboo-DCM/library/tree/main/edit
user-invocable: true
allowed-tools: [Read, Bash, Edit, Grep, Agent]
---

## About this skill

Built and maintained by **Bamboo DCM** ([bamboodcm.com](https://bamboodcm.com)) — the independent infrastructure for Brazil's corporate and structured credit market, with an intelligence layer on top. We use this skill (and the broader knowledge-systems framework around it) to edit our own writing — memos, board material, investor letters, public posts — at the grade each piece earns.

**First public packaging.** The methodology and the skill have been used and pressure-tested internally; this is their first release outside the firm. The leg-(d) meaning gate assumes your runtime can spawn independent (blind) reader calls — see § The gate. Bug reports and pushback are wanted.

Comments, improvements, or questions:

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

License: [CC-BY 4.0](https://github.com/bamboo-DCM/library/blob/main/LICENSE) — free to share and adapt with attribution.

---

# /edit — the readability editor

Refine an existing draft so it reads as easily as its ideas allow — and **prove the edit helped via a gate it can't game.** Where a defect/AI-pattern **linter** *lints for defects* and a content skill *drafts in a brand voice*, `/edit` *refines an existing draft to lower reading effort* without changing what it says, at a grade the content earns. Voice-**neutral**: it refines anyone's draft (yours, a colleague's, a counterparty's), not toward one voice.

> **This skill EXECUTES a published methodology — it does not restate it.** The canon is the **Readability-Editing Methodology**, published alongside this skill in the same library: [`../readability-editing-methodology/readability_editing_methodology.md`](../readability-editing-methodology/readability_editing_methodology.md). Read it once on first encounter; this SKILL.md is the runnable orchestration layer on top of it.

> **Install note.** This skill **shells out to two deterministic tools** — **`readability_diag.py`** (the countable-flags diagnostic) and **`blind_meaning_confirm.py`** (leg-(d)'s blinding + diff harness) — both **co-located in this directory**. The skill does not function without them. Both are **stdlib-only Python 3.8+** (no `pip`; standard library only). Install them alongside this SKILL.md — or copy them to the path your shell-out uses — and invoke:
> - **macOS / Linux:** `python3 readability_diag.py --json <file>`
> - **Windows:** `py -3 readability_diag.py --json <file>` (or `python readability_diag.py ...`)
>
> This canonical ships the two tools **co-located**, so the shell-out paths below read `readability_diag.py` / `blind_meaning_confirm.py`. Point them wherever you install the two files.

---

## The executor-fit contract (load-bearing — read first)

This skill is a **mix** of work-classes, split by the cheapest-executor-per-part principle:

- **Deterministic, countable** → **`readability_diag.py` (no model).** The skill **SHELLS OUT** to it for the countable flags — readability scores (FK/Fog), sentence-length **variance** (the Lever-4 rhythm/monotone flag), nominalization density, term-frequency surface, whole-piece antithesis count, subject-verb-gap estimate. **The skill does NOT recompute these in-model.** Run it:

  ```bash
  python3 readability_diag.py --json <file>          # or:  --json --text "..."
  ```

- **Irreducible judgment** → **the model (this skill).** Intrinsic-vs-extraneous discrimination (methodology §4); the information-density / recovery read (model-assisted, NOT in the tool); the generative rewrite; floor/ceiling calibration; the meaning read it *surfaces* but never self-certifies.

- **Adaptive recovery loop** → **not needed → not an agent.** A single-pass edit + the gate. The one out-of-skill handoff — leg-(d), §The gate — wires as **`blind_meaning_confirm.py --diff` (code, the deterministic blinding + diff-anchoring) + three blind out-of-model readers whose verdicts are combined by a consensus rule (the claim-diff judgment)**, the meaning-side twin of the `readability_diag.py` split. A structured handoff, **not** an agent loop.

**The withheld-verdict contract — respect `parse_confidence` / `withheld`.** The tool emits a `parse_confidence` and a `sentence_segmentation` status (`trusted` / `low_confidence` / `degenerate`). When a sentence-dependent flag is **withheld** (listed in the tool's `withheld` array, value `"unmeasured"`), the deterministic verdict is unavailable — **the model judgment carries; NEVER fabricate the number.** A naive splitter already produced a false "harder" verdict in testing; withholding is the tool refusing to emit a confident wrong number. On a withheld leg-(a), the rhythm half abstains and §4 judgment decides (see § The gate, leg (a)).

---

## Mode

- `/edit <text|file>` — **default: diagnose + propose, read-only.** Outputs the lever diagnosis (intrinsic-vs-extraneous split + the dominant 2–3 load sources + per-lever findings) and the proposed refine moves, each with its two-sided floor/ceiling check, plus the *predicted* gate result. **Changes nothing.** Includes the **STOP / NO-EDIT verdict** when the difficulty is intrinsic-only or the prose is at-floor — restraint is a first-class output. (= methodology Steps 1–2.)
- `/edit --apply <file>` — **apply + gate.** Applies the refine moves and runs the four-part gate. Outputs the refined text + the gate result, with meaning-preservation handed to the blocking-blind-independent confirm (§ The gate, leg (d)). (= methodology Steps 3–4.)

`/edit` mirrors a read-only-default / write-on-flag UX for consistency with a linter run in the same pipeline. Both run *around* this editor in the pipeline below; neither replaces it.

### Pipeline position (the invariant)

The editor is the **middle** of a fixed order; it does not run alone:

```
draft (a content skill or a human)
  → linter CRITICAL pre-screen   (Pass 1: confidentiality + capability-disclosure short-circuits)
  → /edit  (this skill)          (the generative readability refine)
  → linter FULL                  (Pass 1 + Pass 2: catch any AI-tell the rewrite introduced)
  → publish
```

- **Linter-critical FIRST** — a confidentiality leak or capability-disclosure must be caught *before* a voice-neutral, confidentiality-blind generative rewriter touches the text (a rewrite can paraphrase a leak past a regex; this skill has no such machinery).
- **`/edit` MIDDLE** — the generative refine.
- **Linter-full LAST** — a generative rewrite can *introduce* fresh AI-tells (a new synonym-cycle, an accidental rule-of-three); a full defect/style pass back-stops the output.

> The linter is a separate defect / AI-pattern / style pass, run before and after this skill. It is not part of this package; substitute whatever defect linter your workflow uses. (Internally we pair `/edit` with a skill we call `/review`.)

---

## Process — the runnable sequence (methodology §5)

> The deterministic measures come from `readability_diag.py`; the judgment is the model's. **A tool output is a flag to adjudicate, never a target to optimize** (methodology §1 — the metric-trap).

### Step 0 — Calibrate the floor AND ceiling

Name the **audience** and **content class** → read off the target grade *band* (a ceiling-and-floor pair, not a single target) + the **home-vocabulary** keep-list (the exact terms a specialist reader uses with peers). Everything downstream edits *toward the band* — never below its floor (dumb-down), never above its ceiling (inflation).

- **If audience is unstated, infer it from content class and STATE the inference.** A wrong floor is a dumb-down risk; a wrong ceiling an inflation risk — the band is never silently assumed.
- **Set the band + keep-list to YOUR audience.** Pick a grade band for the content class and audience, and keep the audience's home vocabulary — the words a peer would actually use, not signaling. *Worked example (the firm's own bands): a private-credit desk sets an investor-grade floor across audiences — board memos sit higher (grade ~12–14), shareholder letters ~11–13, LinkedIn ~10–11, press ~9–10 (external floor) — but nothing drops below an institutional-investor reading level. The home vocabulary survives: "covenant," "FIDC," "debênture," "tranche" are grade-11+ terms a credit investor uses daily, so they stay; "sub-linear," "intelligence-heavy services layer" are signaling and get cut. The test: would the reader use this exact word telling a peer what you do? Keep precision; cut signaling.* Set your own bands and keep-list for your audience — the numbers above are an example, not a default.
- **Language (EN/PT).** The six levers are language-general; the calibration is language-specific. *Worked example for a second language:* Portuguese runs **~1 grade above** English at the same register (gerúndios, subjunctive, heavier natural nominalization) — don't fight it; an institutional-Portuguese vocabulary (e.g. CVM 161, ANBIMA, FIDC sênior, debênture incentivada, CRA, alocador) is grade-11+ *by nature* and is the reader's home, and the density tell shifts to **-ção chains**. Pass `--lang pt` to the tool, or let it auto-detect.

### Step 1 — Diagnose, then decide whether to edit at all

1. **Run the tool** on the input. Read the flag list; respect `parse_confidence` / `withheld`.
2. **The core split (methodology §4):** for each hard passage, is it hard because the **idea** is hard (*intrinsic* — leave it, maybe anchor or rest it) or because the **prose** is hard (*extraneous* — fix it)? This is the irreducible judgment a score cannot make.
3. **Scan the six levers** (§ The six levers) and **name the dominant 2–3 load sources** — do not try to fix all six everywhere.
4. **Diagnostic unit per lever.** Declare the unit and refuse whole-piece legs on a fragment:
   - **Levers 1–4** (abstraction, concreteness, cohesion, sentence-variation/recovery) are **section-local** — diagnosable on a passed-in snippet.
   - **Levers 5–6** (structural variation, term-glossing) are **whole-piece** — device-repetition counts across the whole article (6 antitheses ÷ sections = 2–3 each, fine locally); glossing happens at a term's first load-bearing use, which a non-first-use section lacks.
   - **On a fragment input, mark Levers 5–6 `unassessed (whole-piece required)` and do NOT fire leg-(a)'s device-count or leg-(c)'s gloss-screen on them** — preventing false device/gloss verdicts in both directions.

**STOP / NO-EDIT terminal.** If the difficulty is **intrinsic-only** OR the prose is **already at floor**, STOP — emit a NO-EDIT verdict + a short rejected-move log (what you considered and why you left it). Restraint is the right answer often; do **not** proceed to Step 2 to manufacture an edit. (In the methodology's validation, two of four pieces correctly stopped here.)

```
=== /edit: NO-EDIT VERDICT ===
verdict:  NO EDIT — {intrinsic-only difficulty | already at floor}
why:      {1–2 lines}
rejected-move log:
  - {move considered} → rejected: {floor / ceiling / net-of-cost reason}
  - ...
```

### Step 2 — Propose

For each dominant lever, pick the refine move and **attach its two-sided floor/ceiling check** — *"does this drop content/precision the audience expects (below floor)?"* AND *"does this raise register, ceremony, or glossing above the audience (above ceiling)?"* If either fires, reject the move.

**Net-of-cost, per move.** A refine move enters only if its readability gain exceeds its meaning/precision/voice cost. A move that buys variance by deleting a causal connective (the tree-bark trap) **fails net-of-cost and is rejected here**, before it ships. **Propose, don't yet apply** — a proposal you can inspect is one you can reject before it costs meaning. (The default mode stops here: a diagnosis + proposed moves, read-only.)

### Step 3 — Refine (`--apply` only)

Apply the moves. The mantra: **same ideas, same sophistication — paced for a reader, not compressed for a writer.** You move load *off the prose*, not *out of the content*.

### Step 4 — Gate-check (`--apply` only)

Run the four-part gate (§ The gate). **Re-run `readability_diag.py` on the refined output** for leg-(a)'s deterministic deltas — code, not the rewriter's say-so. If (b), (c), or (d) fails, return to Step 2. If leg-(a) flags but your §4 judgment disagrees, **adjudicate — do not auto-fail, do not re-propose a real fix to chase a number.** Ship only when (b)/(c)/(d) clear *and* the blocking, blind, independent meaning-confirm returns clean — leg-(d) is wired **out-of-model** (the code-blinded **diff-anchored** brief → **three** blind readers → the mechanical **consensus** roll-up; see § Leg-(d) wiring). The rewriting model never produces the meaning-diff nor sees which text is the edit.

---

## The gate it can't game (methodology §6 — made executable)

The editor is an optimizer; give it a weak gate and it will satisfy the gate without doing the work. **The hard-AND is on legs (b), (c), (d). Leg (a) is a computed flag adjudicated against judgment, never a ship-blocking veto.** An edit ships only after the blocking, blind, independent meaning-confirm (d) returns clean.

| Leg | Condition | Executor in this skill | Gate role |
|---|---|---|---|
| **(a) measurably easier** | Extraneous-load sources from Step 1 are reduced. | **Two instruments, not one**: **variance** = the tool's rhythm/monotone flag (code, non-forgeable *but narrow* — high variance ≠ easy; carries `parse_confidence`); **recovery/information-density** = a **model-assisted** read (NOT in the tool); + the FK/Fog score delta as a flag. All computed on the *output*, outside the rewriter's say-so. | **Adjudicated flag — NEVER a veto.** A leg-(a)/judgment disagreement routes to adjudication against §4 (methodology §5), not auto-fail. **On `parse_confidence` < threshold the rhythm half ABSTAINS** (the tool withheld it) and §4 judgment carries. |
| **(b) not dumbed down** | No content/precision the audience expects dropped; no grade fell *below* the band floor; no home-vocabulary term stripped. | Below-floor grade alarm (tool FK vs band floor) + home-vocabulary term-diff (keep-list) + content-drop check (model). | **HARD-AND (blocking).** |
| **(c) on-floor + under-ceiling** | Passes the jargon screen (signaling out, precision kept), stays at the audience's grade, *and* is not register-inflated above the audience. | Jargon screen (keep-list match + new-signaling detection, model) + a register-inflation check (model). | **HARD-AND (blocking).** |
| **(d) meaning preserved** | The edited version asserts exactly what the original did — no claim added, none lost, no qualifier dropped, no drift. | **Wired:** `blind_meaning_confirm.py --diff` (code) blinds the two texts → A/B (mapping withheld) and emits a **diff-anchored** brief (word-level A/B diff + forced per-change classify); **three readers blind to which is the edit** each re-derive the claim-deltas *cold* in separate contexts (out-of-model). The skill emits `PENDING`, then **consumes** their lists under a **consensus rule** (unanimous-flag → DRIFT, unanimous-clean → CLEAN, split → ESCALATE) — it **never produces the diff it is judged against and never self-certifies.** | **HARD-AND, BLOCKING. The edit is `PENDING` — not shipped — until the blind consensus returns clean.** |

**The non-forgeable boundary, in one rule:** *the skill that does the rewriting neither produces the meaning-diff it is judged against nor sees which text is the edit.* That independence is what makes the whole gate non-forgeable — not "one leg is code." An in-skill "I promise to emit PENDING and not self-certify" is a recall-tier control the same model could skip; the **structural** form is that the blind confirm runs **outside the rewriting model's process** (a held-out party — a human read, or a separate model call with no access to which text is the edit).

### Leg-(d) output contract (the frozen interface; § Leg-(d) wiring consumes it)

On `--apply`, after Steps 3–4, the skill emits exactly this block:

```
=== /edit --apply: GATE RESULT (PENDING) ===
leg (a) measurably easier   [ADJUDICATED FLAG — never a veto]
  variance delta:    {tool, on the output; "ABSTAINED — low-confidence parse (withheld)" if parse_confidence < threshold}
  recovery/density:  {model-assisted read — did a lower-density sentence follow the high-density one?}
  score delta:       {FK/Fog flag, direction only}
  adjudication:      {corroborates §4 judgment | DISAGREES → adjudicated against §4 → {keep edit / revisit}}
leg (b) not dumbed down     [HARD-AND]:  {✅ PASS | 🔴 FAIL — reason}
  below-floor grade alarm:  {tool FK vs band floor}
  home-vocab term-diff:     {keep-list — any term stripped?}
  content-drop:             {model — any claim/precision lost?}
leg (c) on-floor+ceiling    [HARD-AND]:  {✅ PASS | 🔴 FAIL — reason}
  jargon screen:            {keep-list match + new-signaling (model)}
  register-inflation:       {model — manufactured formality / over-glossing?}
leg (d) meaning preserved   [HARD-AND, BLOCKING]:  PENDING
  --- HELD-OUT TEXT A ---
  {one of the two texts}
  --- HELD-OUT TEXT B ---
  {the other text}
  (the A/B ↔ original/edit mapping is WITHHELD from the confirming party — see boundary rule above)
STATUS:   PENDING — edit NOT shipped.   ⚠️ HUMAN-READ-REQUIRED
OVERALL:  ✅ CLEAN (apply) / 🟡 DRIFT (re-diagnose → Step 2) / ⚠️ ESCALATE (human read)   — set by --rollup
NEXT:     leg-(d) blind independent confirm (diff-anchored, 3-reader consensus — § Leg-(d) wiring) → unanimous-clean = ✅ CLEAN; unanimous-drift = 🟡 DRIFT; a split = ⚠️ ESCALATE.
```

> **Gate glyphs.** Legs read `✅ PASS` / `🔴 FAIL`; the overall verdict reads `✅ CLEAN (apply)` / `🟡 DRIFT (re-diagnose)` / `⚠️ ESCALATE (human read)`. The gate summary sits ABOVE the refined text (never tokenizes it); the read-only NO-EDIT terminal is unchanged.

**If (b) or (c) FAILS**, the skill does not emit the held-out texts — it returns to Step 2 with the failing leg named. Leg-(d)'s `PENDING` is reached only when (b)/(c) clear.

### Leg-(d) wiring — the out-of-model blind confirm

**The mechanism — code blinds + diff-anchors, three out-of-model readers judge, the skill rolls up by consensus.** On `--apply`, after (b)/(c) clear and the `PENDING` block is emitted:

1. **Blind (code, non-forgeable) — emit the DIFF-ANCHORED brief.** Write the original and the refined text to two files, then run with `--diff`:
   ```bash
   python3 blind_meaning_confirm.py --original <orig> --edited <edit> --diff \
       --brief-out <scratch>/confirm_brief.txt --key-out <scratch>/confirm_key.json
   ```
   The harness assigns the two texts to **Text A / Text B** (content-hash order — the edit is not always the same slot), writes a **symmetric, diff-anchored brief** — a mechanically-computed word-level A/B diff (order-preserving **PART 1** opcodes + an order-independent **PART 2** residue) that forces the reader to classify **every** numbered change as claim-change vs repackaging — and **withholds** the A/B↔original/edit mapping to `confirm_key.json`. *The `--diff` mode is the fix for a silent-ship failure mode: a subtle qualifier dropped inside a reworded/reordered clause is an **enumerated item the reader must adjudicate**, not something to catch by holistic re-reading (blind readers went **0/3 → 3/3** on that case). Doing the blinding AND the diff in CODE is the load-bearing choice — a prose brief handed to the rewriting model is recall-tier (it could leak the mapping); the harness takes the leak out of the model's hands.*

2. **Judge (THREE blind out-of-model readers — the consensus panel).** Spawn **three** independent readers (a separate mid-tier model call — e.g. Claude Sonnet — or human readers), each with the brief *only*: "Read **only** `confirm_brief.txt`; do **not** open any other file (there is an answer key you must not see); classify every numbered diff item and return the structured findings." Each runs in a **separate context**, blind to which text is the edit, and returns `change_classifications` (one line per numbered item) + `claim_deltas` (quote-anchored) + `uncertain`. *Three readers, not one, because the diff-anchored brief's forcing-function — classify EVERY item — makes a lone reader occasionally over-classify a borderline near-synonym or a subordination↔coordination swap as a claim-change, and a single reader cannot tell its own spurious flag from a real one. Consensus (step 3) routes that disagreement to the human read instead of a spurious bounce.*

3. **Roll up (mechanical CONSENSUS rule — the skill never re-derives the diff).** The skill computes the verdict from the three readers' lists, **without** reading the key. Let a reader "flag" iff its `claim_deltas` is non-empty:
   - **all three CLEAN** (every reader: empty `claim_deltas` **and** empty `uncertain`) → **CLEAN** → apply the edit to the file.
   - **all three FLAG** (unanimous non-empty `claim_deltas`) → **DRIFT** → do **not** ship; return to **Step 2** with each delta named (read `confirm_key.json` only now, to map A/B → which phrase the *edit* changed).
   - **anything else** — the readers **SPLIT** (one or two flag), or **any** reader is `uncertain` → **ESCALATE** → route to the **human read** (the methodology's ground truth) before shipping. Never auto-clean and **never auto-bounce on a split.**

   *Why unanimous-consensus and not pure-OR. Pure-OR (any one reader's `claim_deltas` non-empty → DRIFT) amplifies the lone-reader over-flag: a clean readability reword that stresses the synonym / causal-connective boundary drew a spurious flag from 1–2 of 3 readers → a false DRIFT that bounces a clean edit. The consensus rule converts that into an ESCALATE (a human dismisses it), while a real buried drop — which the `--diff` brief makes salient to **all** readers — still goes 3/3 → DRIFT. It never silent-ships (any reader catching a real drift forces at least an ESCALATE).*

**Why this is genuinely out-of-model + non-rubber-stampable (not theater):** (a) the reader's **separate context** is the structural out-of-model boundary — it cannot see the rewrite reasoning; (b) the **code-blinded** symmetric brief means the reader cannot tell which text is the edit, and the rewriting model cannot leak it; (c) the rewriting model **produces neither the diff nor the verdict** — each reader enumerates the deltas, the skill only applies the consensus rule over the three lists; (d) the brief forbids "reads equivalent" hand-waving — it forces a **bidirectional, quote-anchored** claim enumeration that distinguishes a claim-change from pure syntactic repackaging.

**The verification contract — applied WITHOUT breaking blindness.** The reader's verdict gates an apply, so it is an execution-party verdict. But "re-verify against the source at the moment of action" must **not** be read as *the orchestrator re-deriving the diff* — that is the self-certification the gate forbids. The blindness-preserving application:
- **Pre-dispatch:** the skill picks the exact two texts (gather-vs-judge split — the reader never chooses what to compare); the brief is the fixed symmetric template; the anti-fabrication + quote-first rules are baked in by the harness.
- **Form-verification (orchestrator-safe):** confirm the verdict is well-formed — every claim-delta carries a verbatim anchor that is actually present in the texts, and the pass was bidirectional. This checks the verdict's *form*, never re-derives its *substance*.
- **Substance defense-in-depth (out-of-model, never the orchestrator):** the **three-reader consensus** is the default (a lone reader's verdict never decides); on top of that the retained **human read** (ground truth, below) is owed for publication.

**The human read stays the publication ground truth.** The wired reader panel is the *routine, automated* front-stop — it catches gross-to-moderate drift cheaply and escalates the subtle. An LLM reader is a **proxy**, not a held-out *human* read. For anything published, the `HUMAN-READ-REQUIRED` flag still owes a human cold read; the wiring front-stops it, it does not replace it.

---

## The six levers (operational reference)

The *real* levers of reading difficulty — what a score can't see and the editor moves. Each is **diagnostic signal → refine move → floor/ceiling check**. Full science + citations: methodology §3 — do not re-derive here.

| # | Lever | Unit | Diagnostic signal | Refine move | Floor/ceiling check |
|---|---|---|---|---|---|
| 1 | **Abstraction density** | section-local | Stacked abstract nouns (-tion/-ment/-ção), *esp. in the subject slot*; >~3–4 unresolved abstractions before a concrete anchor | De-nominalize → finite verb + real actor; split an over-loaded sentence | Keep the nominalization that names a known concept; don't over-spell what an expert already chunks (ceiling) |
| 2 | **Concreteness & anchoring** | section-local | Abstract runs with no concrete instance; the anchor arriving *after* the abstraction, or not at all | Add **one** concrete instance/example **landed before (or with)** the abstraction | Keep anchors precise (real mechanism/number), not folksy (floor); don't anchor what didn't need it (ceiling) |
| 3 | **Cohesion & flow** *(highest-yield)* | section-local | Sentences opening with new/abstract material; main idea buried mid-sentence; long subject-verb gaps (>~8–10 words); a concept renamed across sentences | Start each sentence with old/given info (echo prior end); move the key idea to the stress position (before the period); close S-V gaps; one term per concept | *Don't over-link for experts* (gaps can aid them); **formal-legal register: a long intercalated S-V clause may be a register marker, not load — a CHECK, not a ban** |
| 4 | **Sentence-length variation & recovery** | section-local | **Two signals:** near-zero variance = monotone (the **tool's deterministic flag**); a high-density sentence with no lower-density one after it = no recovery (**model-assisted**, NOT the variance number) | Engineer rest-then-load cadence; after a dense sentence give a low-density **recovery** sentence (example/restatement) | A *recovery* sentence is productive; a *redundant* one is cuttable. **Chopping into uniform short sentences LOWERS variance — the symmetric trap** |
| 5 | **Structural variation** | **whole-piece** | The same device (antithesis, tricolon, "not X but Y") past ~2–3 instances *across the whole piece*; a wall of paragraphs with no headings | Keep the two strongest instances, rewrite the rest plainly; add headings; lead with the main idea | Devices are load-bearing in small doses (don't sterilize, floor); don't impose scaffolding a short piece doesn't need (ceiling) |
| 6 | **Term-glossing** | **whole-piece** | A necessary technical term used load-bearingly on first appearance with no half-second gloss; jargon where a plain word exists | *Keep* the necessary term + add an inline gloss on first use; *strip* non-necessary jargon | Gloss only terms new to the *intended* audience — glossing what every specialist knows is inflation (ceiling) |

---

## Inputs & outputs

**Inputs:** text or a file path; audience/register (sets the floor band *and* ceiling — Step 0); language (EN/PT). Audience unstated → infer from content class and *state the inference*.

**Outputs:**
- **default (`/edit`):** a diagnosis report — a findings list of readability levers — + the proposed moves + the *predicted* gate result; **or** the NO-EDIT verdict + rejected-move log when restraint is the answer.
- **`--apply`:** the refined text + the **GATE RESULT (PENDING)** block above (legs (b)/(c)/(d) pass/fail; leg-(a) an adjudicated flag with `parse_confidence`; leg-(d) the two held-out texts + `PENDING` + `HUMAN-READ-REQUIRED`).

---

## Gotchas

- **The score is a flag, never a target (the metric-trap).** Every formula (FK, Fog, SMOG…) is a function of word length + sentence length *only* — blind to cohesion, abstraction, order. You can satisfy a formula and make the text *harder* (the tree-bark proof: chopping a sentence deletes the causal link the reader needed). Never optimize to a number.
- **High variance ≠ easy.** The variance flag is *narrow* — a piece can have healthy variance and still read as "constant maximum load." Variance catches monotone; it does **not** certify ease. That's why leg-(a) is a flag, not a veto.
- **Never fabricate a withheld number.** When the tool withholds a verdict (low `parse_confidence`), the model judgment carries — do not invent the variance/score figure. Emit "ABSTAINED — low-confidence parse."
- **Don't fire whole-piece legs on a fragment.** On a snippet, Levers 5–6 are `unassessed`; don't count antithesis or screen glossing on it.
- **The rewriter must never produce the diff it's judged against (leg-d).** A model judging its own rewrite — *or reading a diff it produced* — is the gameable LLM-judge the gate exists to avoid. Leg-(d) is structurally outside the rewriter, blind, and blocking (wired via `blind_meaning_confirm.py --diff` + **three** blind readers under a consensus rule — § Leg-(d) wiring). The *mechanical* word-level diff is code-computed and symmetric — it is not the rewriter's diff.
- **The wired blind confirm is a proxy, not the ground truth (leg-d).** The three-reader consensus catches gross-to-moderate drift and *escalates* the subtle or the split (→ human read); it does **not** replace the held-out **human** read a publication piece owes. And the diff-anchored brief must define a delta as a **claim/precision** change, not any surface difference — the forcing-function (classify every diff item) fixes the buried-drop silent-ship but makes a *lone* reader over-classify a borderline synonym / connective swap, which is exactly why the **consensus rule** (unanimous-flag → DRIFT, split → ESCALATE) is load-bearing, not just best-of-N. Each reader enumerates `claim_deltas`; the **gate applies the consensus rule** — no single reader editorializes a verdict.
- **Two symmetric failures, not one.** *Below floor* (dumb-down): stripping content/precision an expert reader expects. *Above ceiling* (inflation): manufactured formality, over-glossing — on expert-grade prose this is the **more common** real failure. Every move carries both checks.
- **Restraint is an output.** NO-EDIT on intrinsic-only / at-floor prose is correct, not a failure to act. Manufacturing an edit to "do something" is the failure.

## Edge cases

- **Fragment / snippet input** → Levers 5–6 `unassessed (whole-piece required)`; leg-(a) device-count + leg-(c) gloss-screen do not fire on it.
- **Low `parse_confidence` / `degenerate` segmentation** → the sentence-dependent flags are withheld; leg-(a)'s rhythm half abstains, §4 judgment carries; report the abstention, never a fabricated figure.
- **Portuguese text** → shift the band ~1 grade up; run an institutional-Portuguese home-vocabulary set; apply the Lever-3 formal-legal register check with *extra* force (a closed S-V gap can read *less* formal). Pass `--lang pt`.
- **Already-at-floor or intrinsic-only difficulty** → NO-EDIT verdict + rejected-move log (Step 1 STOP).
- **`--apply` reaches `PENDING` → leg-(d) runs** → the skill runs the out-of-model blind confirm (§ Leg-(d) wiring): `blind_meaning_confirm.py --diff` blinds the two texts + emits the diff-anchored brief → **three** blind readers each re-derive `claim_deltas` cold → the skill applies the **consensus** rule. **Unanimous non-empty `claim_deltas` → DRIFT** (return to Step 2); **a split (1–2 flag) or any `uncertain` → ESCALATE** to the human read; **unanimous clean → apply.** The edit is **never** auto-applied before leg-(d) returns unanimous-clean, and a **publication** piece still owes the `HUMAN-READ-REQUIRED` ground-truth human read on top of the automated confirm.
- **Markdown input** → the tool strips formatting and excludes fenced code blocks before measuring; pass `--raw` to measure literally.

## See also

- [`../readability-editing-methodology/readability_editing_methodology.md`](../readability-editing-methodology/readability_editing_methodology.md) — the published methodology this skill executes (§3 levers, §5 sequence, §6 the gate). Published alongside this skill in the same library.
- [`readability_diag.py`](readability_diag.py) — the deterministic executor the skill shells out to, **co-located** (`--json` contract: `flags`, `parse_confidence`, `sentence_segmentation`, `withheld`).
- [`blind_meaning_confirm.py`](blind_meaning_confirm.py) — leg-(d)'s out-of-model **blinding harness**, **co-located** (`--diff` mode): blinds the two texts → A/B with the mapping withheld and emits the diff-anchored brief, feeding the **three** blind readers whose verdicts the consensus rule combines (§ Leg-(d) wiring).
- **A defect / AI-pattern linter** — the composes-with sibling that runs *around* `/edit` in the pipeline (`linter`-critical → `/edit` → `linter`-full). Substitute whatever defect/style linter your workflow uses. A brand-voice content-drafting skill is the other composes-with sibling: it drafts; `/edit` refines readability of *any* draft, voice-neutral.

---

*This skill is part of an internal knowledge-systems framework Bamboo DCM has been building for AI-native execution in regulated finance. If the broader framework is interesting, get in touch — we're publishing more as we package them.*
