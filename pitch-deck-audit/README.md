# Pitch Deck Audit — kit contents

Audit a fundraise deck (or a structurer proposal, an M&A teaser, or the VC investment memo that comes back about you) against a **sector-tuned lens** — and, if you don't have a deck yet, build a v1 from scratch.

The kit's distinctive contribution is the **lens system**: you fill a lens once for your company, then point Claude at it every time the deck changes. Feedback stays consistent across iterations, and the lens gets sharper every time a real investor surfaces an objection you hadn't anticipated.

**`v0.1.0-beta`** — versioned beta, narrow distribution while the substrate gets pressure-tested. Comments and corrections welcome; see [Contact](../README.md#contact).

## Where to start

**No deck yet?** → [`field_guide.md`](field_guide.md)
**Have a deck, want it audited?** → [`playbook.md`](playbook.md), then [`lens_template.md`](lens_template.md)
**Not a Claude Code user?** → [`cowork_workflow.md`](cowork_workflow.md)

## The files

| File | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The Claude Code skill itself — drop this folder into your skills directory and invoke it. Wraps the playbook and lens system into a runnable audit. |
| [`playbook.md`](playbook.md) | **The methodology** (38 sections, 8 parts). Audit-mode: how to evaluate a deck that already exists. Synthesizes Founder Institute, Sequoia and McKinsey writing discipline against a working corpus of credit-fintech, regulated structured-product, hard-tech and M&A material, extended for the 2026 AI-era reality. Business-literate reading level; no developer or finance-PhD prerequisites. |
| [`field_guide.md`](field_guide.md) | **Build-mode entry point** for founders authoring a fundraise deck for the first time. Slide-by-slide guidance, self-check questions, and the upstream decisions worth locking before you draft. Start here if you're pre-v1, then hand off to the playbook. |
| [`lens_template.md`](lens_template.md) | **The blank lens** — a fillable 13-section template for the criteria your audits run against. First fill takes 60–90 minutes; the version that wins your round is the one you've edited ten times. The structure, not the company-specific content, is what keeps audits consistent. |
| [`cowork_workflow.md`](cowork_workflow.md) | Running the same iterative loop **without Claude Code** — in a Claude.ai Project, for founders, advisors and operators who don't use the developer CLI. About 30 minutes to get the loop running the first time. |
| [`examples/`](examples/) | **Five filled sector lenses** to copy from — pick the one closest to your sector and replace the specifics. See that folder's own index. |

## How the pieces fit

```
field_guide.md      →  you have no deck yet; build a v1
      │
      ▼
lens_template.md    →  fill the lens once for your company
   (or examples/)      (or start from the closest worked example)
      │
      ▼
playbook.md         →  the methodology each audit section runs against
      │
      ▼
SKILL.md            →  run it in Claude Code
cowork_workflow.md  →  ...or run the same loop in a Claude.ai Project
```

The lens is the part that compounds. Add every hostile question you hear in a real meeting to its objection bank, and the next audit catches it before the investor does.
