# Readability-Editing Methodology

A standalone framework, published open-source by [Bamboo DCM](https://bamboodcm.com). It's the process we use internally to edit our own writing.

| File | What it is |
|---|---|
| [`readability_editing_methodology.md`](readability_editing_methodology.md) | **The framework itself.** A runnable diagnose → refine process for making a piece as easy to read as its ideas allow — at the grade level the content earns, never below the floor your audience expects and never inflated above it. |

## What it actually does

It fixes the **real levers of reading difficulty** — abstraction density, concreteness, cohesion, sentence variation, structural variation, term-glossing — rather than a readability score. Scores are a symptom; chasing one produces short choppy sentences that are harder to read, not easier.

The part worth stealing even if you use nothing else is the **gate the editor cannot game**: meaning-preservation is verified *outside* the rewriter, via a blind, diff-anchored claim check. An editor asked "did you preserve the meaning?" always says yes.

Grounded in reading science — Gopen & Swan, Williams, cognitive-load research, the plain-language movement — with an explicit floor and ceiling, a **no-edit (restraint) terminal** for pieces that are already right, and bilingual awareness.

## How to use it

Readable straight off the page, paste-ready into a Claude.ai project, or printable. It pairs naturally with a human editor running it by hand and with a separate defect / AI-pattern linter that runs after — but it stands alone.

For the executable version, see [`/edit`](../edit/) — a Claude Code skill that applies this process, shells out to a deterministic diagnostic for the countable flags, and enforces the meaning-preservation gate on `--apply`.
