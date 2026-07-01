# Cowork workflow — running the kit without Claude Code

**For:** founders, advisors, and operators who don't run Claude Code (the developer CLI) but do use Claude.ai Pro or Team and want to run the same iterative pitch-deck audit loop in a Claude.ai Project.

**The premise:** instead of asking a friend to "look at your deck" once and then forgetting their feedback two days later, you build a system that gives you structured, repeatable feedback every time you make a change. The system gets sharper as you use it, because you teach it what your real investors actually push back on.

**~30 minutes to get the loop running for the first time.**

> **Step 0 — if you don't yet have a deck, start at [`field_guide.md`](field_guide.md).** The Cowork loop below is built around iterative *audits* of an existing deck. If you are still drafting your first version, the field guide is the build-mode entry point: slide-by-slide guidance, self-check questions, and the upstream decisions worth locking before you draft. Come back here once you have a v1.

---

## 1. About this guide

The pitch-deck-audit kit ships in two paths:

- **Claude Code path.** You install the kit as a skill (`/pitch-deck-audit`) and invoke it from the developer CLI. Faster for technical operators who already run Claude Code; supports automated iteration loops.
- **Cowork path (this guide).** You drop the kit's files into a Claude.ai Project and run audits from a chat. Identical methodology; no install, no terminal, no Node.js. This is the default path for non-developer founders.

The output of both paths is the same: structured audit reports, rewrite suggestions, and a prioritized fix list anchored to your sector lens. Pick the path that matches your environment.

This guide covers the Cowork path end-to-end. If you want to switch to Claude Code later, the kit's [`SKILL.md`](SKILL.md) has the install instructions and the audit logic is identical.

---

## 2. Setup (one-time, ~10 minutes)

### Step 1. Make sure you're on Claude Pro or Team

You need a paid Claude.ai account. The free tier doesn't give you enough usage or file size headroom for iterative deck work, and pitch deck work is exactly the use case where the paid tier pays for itself in the first hour. If your team is sharing the workflow, Claude Team is worth considering for shared project access.

### Step 2. Create a Claude.ai project

In Claude.ai, click **Projects** in the left sidebar, then **+ Create project**. Name it something concrete like **"`[YOUR COMPANY]` — Pitch Deck Audit"**.

The project is a persistent workspace: anything you upload stays loaded across every conversation you have inside the project. This is the difference between chat and Cowork — you stop re-pasting context every time, and Claude's responses get sharper because they're always anchored on the same source files.

In the project description field, paste this (replace the bracketed text):

> *`[YOUR COMPANY]` is a `[ONE-PHRASE DESCRIPTION]` raising `[$AMOUNT]` `[INSTRUMENT]` at `[STAGE]`. This project iteratively audits and improves our investor pitch deck. The lens file in this project contains the criteria Claude should use; the playbook contains the methodology; the deck PDF is the current artifact under audit.*

That description gets included in every conversation in the project, so Claude always remembers what `[YOUR COMPANY]` is.

### Step 3. Upload the kit files plus your deck

Inside the project, find the **Project knowledge** section (sometimes labeled "Knowledge base" or "Files"). Click **Add content** and upload:

1. **`playbook.md`** — the methodology
2. **`lens_template.md`** if your sector isn't covered, OR one of the worked examples from [`examples/`](examples/) (e.g., `credit-fintech.md`, `regulated-structured-product.md`, `hard-tech.md`, `m-and-a-teaser.md`, `structurer-proposal.md`)
3. **Your latest pitch deck PDF**

If you're using `lens_template.md`, fill the placeholders before uploading. If you're using one of the worked examples, treat it as a starting point — you'll edit it down to your specifics in the first session.

That's it. The project now has everything it needs.

---

## 3. First run (~15 minutes)

### Step 4. Start a new conversation in the project

Click **Start new chat** inside the project. Paste this exact text into the chat (adapt the lens-file name to whichever you uploaded):

> *Use the criteria in the lens file (`[YOUR LENS FILE NAME].md`) to audit the pitch deck PDF in this project. For each of the 12 rubric criteria in Section 7 of the lens, score the current deck 1–5 and give one specific reason for the score. After the table, give me a prioritized list of the top 3 highest-impact fixes — not the three lowest scores, but the three changes that would move the deck the most for the smallest amount of work. Be direct. Don't pad.*

Press enter. Wait ~30 seconds. Read what comes back.

### Step 5. Read the output critically

You'll get a scored table and a top-3 fix list. **Do not accept it blindly.** Some of what Claude says will be exactly right. Some will be wrong because Claude doesn't know things you know — your real numbers, your investor relationships, your regulatory situation. Some will be a useful provocation that makes you defend a choice you'd been making on instinct.

Three rules for reading Claude's output well:

1. **Trust the structural critique.** When Claude says "your vision slide is at slide 19 and should be at slide 2," that's a pattern observation Claude is good at. Take it seriously.
2. **Pressure-test the specifics.** When Claude says "your default rate of 0% is implausibly low," that's worth investigating but it might not be true given your actual cohort. You know more than Claude here.
3. **Don't optimize for the score.** The score is a diagnostic, not a goal. A 60/60 deck that bores investors is worse than a 45/60 deck that wins meetings. Use the rubric to find the *meaningful* gaps, not to chase points.

### Step 6. Pick ONE thing to fix this week

Look at the top-3 list. Pick the one that's both **highest-impact** (would move the deck the most) and **most concrete** (you know exactly how to do it). Resist the temptation to fix all three. Resist the temptation to fix something easy that isn't on the list.

If the top recommendation is "add a sector-specific slide that's missing" (e.g., a leverage-wedge slide for a credit raise, a kWh-as-leading-unit slide for hard-tech), draft that next. Section 11 of your lens has a placeholder for the sector-specific slide draft — point Claude at it: *"Use Section 11 of the lens to draft `[SLIDE NAME]` for `[YOUR COMPANY]`."*

### Step 7. Make the fix in your design tool

Take Claude's output and adapt it in PowerPoint, Figma, Canva, or whatever you use. Don't paste Claude's words verbatim. Read what it wrote, understand the *point* it was making, then write the slide in your own voice. The lens file's Section 12 has voice guidance — point Claude at it if you want to keep the register consistent.

Save the new version of the deck as **v2** (then v3, v4, etc.). Version your work — it's cheap and it lets you compare.

---

## 4. The iteration loop (every 1–2 weeks until the round closes)

Once setup is done, the recurring loop is fast. ~20 minutes per cycle.

1. **Re-upload** the new PDF to the project. Delete the old one first (otherwise Claude gets confused about which is current). Click into project knowledge, remove the old PDF, drag the new one in.

2. **Run a focused audit, not always a full one.** If you just rewrote the cover, ask Claude to score against criterion 1 ("cover earns the page turn") only. If you just added the leverage-wedge slide, ask to score against criterion 7. Spot checks beat full audits when you're iterating fast.

3. **Run a red-team once a week**, even if nothing has changed. Paste this:

   > *Play a hostile institutional investor on `[YOUR SECTOR]`. Walk through the questions in Section 9 of the lens, but ask the hardest version of each — the one a skeptical LP would ask. Don't be polite.*

   Claude will surface objections you didn't think of, and the lens file gets sharper as you add the new ones to Section 9.

4. **After every real investor meeting**, paste in the questions the investor asked and ask Claude to update the lens:

   > *I just had a meeting with `[INVESTOR TYPE]` who asked these three questions: `[Q1, Q2, Q3]`. Add them to Section 9 of the lens, drafted with the answer I'd want to give next time. If any of them indicate a gap in the deck itself (not just my preparation), flag that.*

   This is the most valuable habit. Within a month, the lens file contains a custom Q&A tailored to the investors you're actually pitching, and Claude's red-teams start to feel like the meetings themselves.

---

## 5. Rules for using AI feedback well

This part matters more than the mechanics.

### Pressure-test specifics, trust structural critique

Claude is good at:

- Narrative flow and slide order
- Prose tightening and removing filler
- Spotting internal contradictions and inconsistent numbers
- Generating multiple options to react to (taglines, headlines, slide titles)
- Comparing your deck against patterns in other decks
- Playing hostile investor and surfacing questions you haven't thought through
- Translating between languages with register awareness

Push back on Claude when:

- It quotes a specific regulatory rule (CVM, SEC, BCB, ESMA) — verify with counsel
- It invents numbers you didn't give it (cohort default rates, NIM, cost of funds, CAC) — these have to come from your books
- It generalizes about "the `[YOUR SECTOR]` market" — you and your team know more
- It writes copy that sounds clever but doesn't sound like you — rewrite in your own voice
- It says "this slide is fine" on something you have a nagging feeling about — your nagging feeling is probably right
- It tells you what you want to hear — that's the most dangerous failure mode

### The single most important rule

**Test against one real human investor before you incorporate a major change.** Claude is a sparring partner, not a substitute for actual market feedback. Show your v4 deck to one friendly investor, ask them the same question Claude flagged, and see what they actually say. If the human and Claude agree, ship the change. If they disagree, the human wins.

---

## 6. Extending the lens

The lens file is yours to edit. You don't need permission. Specific things to add over time:

- **Your real unit economics.** Replace every `[REPLACE WITH YOUR REALITY]` placeholder in the lens with actual numbers from your books.
- **New investor objections.** Every time a real investor asks a question that surprises you, add it to Section 9.
- **New comparables.** When a competitor raises, add them to Section 10 with what they pitched and what they got. Update at least once a month.
- **New rubric criteria.** If you find yourself wishing Claude would check for X and X isn't in Section 7, add X as criterion 13 with a "what 5/5 looks like" anchor.
- **Your voice rules.** As you discover phrases you always want Claude to avoid (or always use), add them to Section 12.

The point of a living lens is that the system learns alongside you. Don't treat the seed as gospel. Treat it as the starting board state.

---

## 7. Sharing with co-founders

Inside the Claude project, click the share icon and add your co-founders by email. They'll see the same project knowledge and conversations. Use the project as the team's shared memory: when one of you runs an audit and finds something useful, the others can read the conversation thread without redoing the work.

One caveat: only one person should be editing the lens file at a time. If multiple people edit in parallel you'll lose changes. Pick a "lens owner" (probably whoever is closest to the deck this week) and route lens edits through them.

The lens file is the team's source of truth — not the deck. Disagreements about what should be in the lens are productive (they surface real strategic disagreements about the raise). Disagreements about deck slides without lens grounding are not (they devolve into taste arguments).

---

## 8. Troubleshooting

**Claude seems to have forgotten the deck.** Re-upload the PDF. Sometimes project knowledge needs a refresh after a long conversation. Or start a new chat — the project files persist but the chat memory doesn't carry over between conversations.

**Claude is being too gentle.** Add this to the end of your prompt: *"Be ruthless. The point is to find what's broken, not to make me feel good. If I'm wrong, say so."*

**Claude is being too generic.** It's probably not reading the lens carefully enough. Start your prompt with: *"Before answering, re-read Sections `[X, Y, Z]` of the lens file and use those criteria specifically."*

**You're hitting usage limits.** Upgrade to Claude Pro or Team. For pitch deck work, the cost is trivial relative to the value.

**The output is too long to read.** Add to your prompt: *"Maximum 300 words. Be direct."*

**You want to compare two versions of a slide.** Upload both PDFs (rename them clearly, e.g., `deck_v3.pdf` and `deck_v4.pdf`) and ask Claude to compare them slide-by-slide.

**You want a fresh perspective and worry Claude is anchored on previous conversations.** Start a new chat in the project. Project knowledge persists; chat history doesn't.

**The lens template doesn't fit your sector.** Use the closest worked example in `examples/` as a starting point and edit aggressively. The 13-section schema is the structure; the company-specific content is replaceable.

**The audit returns generic findings.** The lens is too sparse. Fill more `[FILL]` placeholders, especially in Sections 5 (sector framework), 8 (sector red flags), and 9 (investor objection bank). The audit gets sharper as the lens gets sharper.

---

## 9. What "done" looks like

You'll know the system is working when:

- You stop re-explaining `[YOUR COMPANY]` to Claude every conversation
- The audit scores stop being interesting because the deck is actually good
- The red-team starts surfacing the same 3–4 questions every time, and you have crisp answers to all of them
- You can run a full audit and the only top-3 fixes are nuance, not structure
- A real investor asks you a hard question and you find yourself thinking *I prepared for this with my lens file last week*

When you get there, the deck is ready and the lens has done its job.

---

## Final note

This is a starter kit. The lens templates ship loaded with criteria, frameworks, rubrics, and starter content. The real value compounds over the next 30–60 days as you adapt the lens to your actual investors, your actual numbers, and your actual round dynamics. The first audit is the *least* valuable use of this system. The tenth audit, after you've taught the lens what your investors really care about, is what wins the round.

If something breaks or you have a question, get in touch — contacts below.

---

**Authored by Bamboo DCM** ([bamboodcm.com](https://bamboodcm.com)) — the independent infrastructure for Brazil's corporate and structured credit market, with an intelligence layer on top.

Comments, improvements, or questions:

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

License: [CC-BY 4.0](https://github.com/bamboo-DCM/library/blob/main/LICENSE) — free to share and adapt with attribution.

Version 0.1.0-beta · 5 May 2026
