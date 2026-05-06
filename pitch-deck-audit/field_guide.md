# Pitch Deck Field Guide

**For founders authoring a fundraise deck for the first time**
**Bamboo DCM · v0.1-beta · 6 May 2026**

*Working tools from an AI-native credit infrastructure firm. Shared early in v0.1-beta.*

A working playbook for building a fundraise deck from scratch. Slide-by-slide guidance, self-check questions, and the process discipline that makes a deck actually land.

---

## About this guide

This is a build-mode companion for founders authoring a fundraise deck from scratch. It synthesizes Founder Institute, Sequoia, and McKinsey writing discipline, extended for the 2026 reality of AI-native fundraising. Each slide gets a one-page treatment: what it answers, how to draft it, the red flags to avoid. Each part closes with self-check questions you can run as you build.

**How to use this document.** Read Part 1 in order before opening any slide template — artifact class, two-decks rule, and framework selector are upstream decisions that shape everything downstream. Part 2 is the slide-by-slide build (the canonical 15-slide flow). Part 3 turns the audit rubric into self-checks you run as you draft. Part 4 covers stage-based positioning and AI-era considerations. Part 5 closes with process discipline. If you only have an hour, read Part 1 and Part 2.

**Status.** Versioned beta. Bug reports, disagreements, and pushback welcome — contacts at the bottom.

**Companion tools.** Once you have a v1 deck, [`playbook.md`](playbook.md) (the audit-mode methodology) and [`lens_template.md`](lens_template.md) (the sector-tuned lens system) take over. The Field Guide builds; the audit kit reviews. See [`cowork_workflow.md`](cowork_workflow.md) for the iterative-audit loop in Claude.ai. Send us a v0.5 of your deck when you have one and we will run our tool against it — it is currently in beta and the feedback genuinely helps.

---

## Part 1 — Decide what you're building

Three decisions land before any slide gets drafted. Skipping them is the most common reason first decks get torn up after the first round of investor feedback — the founder built the wrong artifact, in the wrong density, on the wrong narrative arc.

### 1. The two-decks rule

- **The reading deck.** Sent over email. Read alone in 4-7 minutes without you present. Denser. Self-contained slide titles that carry the thesis without narration. 10-14 slides.
- **The listening deck.** Presented in a meeting, narrated. Lighter per slide; more whitespace; 14-20 slides. Each slide supports a verbal beat rather than standing alone.

Build the reading deck first. It forces you to state every claim as a complete assertion that stands without your narration. Once it is clean, stripping it into the listening deck takes half a day. Building the listening deck first tends to produce slides that depend on narrative and fall apart when emailed to a partner who missed the meeting.

### 2. Framework selector

Three axes shape the deck. Walk all three before opening slide structure:

- **Sector.** Generic / credit-fintech / regulated structured-product / hard-tech / sport-tech / your sector. Determines which red flags and unit-economics anchors apply.
- **Stage.** Pre-seed / seed / Series A / Series B+. Determines which risk type the round is selling down.
- **Instrument.** Equity / credit-instrument equity wedge / structured-product distribution / strategic round / bridge. Determines what the investor is actually buying.

For the equity-raise branch, Founder Institute's four-framework selector — pick exactly one as the lead arc:

| Framework | When to use | Lead slide after elevator |
|---|---|---|
| **Problem / Solution** | Solve a clear, evidenced problem for a paying customer. You have data to quantify the pain. | Problem → Solution |
| **Vision / Opportunity** | Creating a new market or a "why now" bet on a trend inflection. | Vision → Opportunity |
| **Team** | Founding team's credibility is the primary wedge; domain leaders that command attention. | Team immediately after elevator |
| **Traction** | Growth and metrics are top-tier for stage; progress over time is the story. | Traction immediately after elevator |

All slides that follow must serve the chosen arc. Don't mix frameworks — the deck reads as unfocused.

### 3. Common variants

Most rounds use the canonical 15-slide flow in Part 2. Two variants worth knowing: the 5-slide format (Elevator / Problem-Market / Solution-Traction / Team / Ask) for rapid screening conversations; the 30-slide format (full flow + appendix slides for diligence) for late-stage rounds. Sector overrides are real — credit-fintech adds a capital-stack slide; hard-tech adds a country-macro slide before market sizing; regulated structured-product replaces the entire flow with a three-pillar arc. If your sector is in that list, the sector lens annexes in [`examples/`](examples/) cover the variations.

---

## Part 2 — Slide-by-slide build

The canonical 15-slide flow for fundraise decks. Build in this order.

### 1. Cover and one-sentence pitch

The cover earns the page turn. Logo + "Pitch Deck — Q2 2026" earns nothing. The cover carries a tagline + sub-tagline that does three things in eight words or less: states who you serve (specific, not "users"), implies what is broken or unique, earns the right to make the reader turn the page. The "only X for Y" formula works often. Use Founder Institute's four-sentence elevator: *We help [customer] do [specific job] better/faster/cheaper than [alternative] because [unique advantage]*. An average investor sees ~100 decks per week and spends ~4:30 on a deck — the first two slides are the filter. Always number slides for phone discussions and post-meeting follow-up.

### 2. Problem

One crisp problem in ≤10 words, supported by ≤3 quantified bullets. Your customer is who pays — not who uses the product. Founders often write the Problem slide for the end user when the buyer is someone else. Pick one pain. The deck has 14 other slides for nuance. **Red flag:** piling pains onto the slide because each one feels load-bearing.

### 3. Solution

Mirror the Problem bullets — exact opposites. Solution bullet 1 directly answers Problem bullet 1, and so on. If you need "and" to connect two ideas in a Solution bullet, you have two solutions and one of them belongs elsewhere. **Red flag:** Solution slide describes a product capability instead of an outcome for the customer named on the Problem slide.

### 4. Why now

The single most under-invested slide in early-stage decks. Most founders skip it or write a generic "AI is hot" gesture, which gets discounted. Three classes of answer: **technology shift** (new capability that was unavailable 18 months ago); **regulatory shift** (new rule, new license category, new market that was previously closed); **market shift** (customer behavior change that opens a window). The honest answer often combines two. The dishonest answer ("AI is having a moment") gets discounted as undifferentiated. See Part 4 for AI-specific framings.

### 5. Market and sizing

Bottom-up beats top-down. "$365B Brazilian private credit market" is a wallpaper number. Bottom-up math: *buyer count × annual spend per buyer × geography count = TAM*. Then constrain by geography, segment, and channel for SAM and SOM. **Red flags:** vanity-sizing (broad industry number, not your actual wedge); the Credit Suisse pyramid trap (templated funnels not built from your actual unit economics).

### 6. Product / how it works

Show > tell. Screenshots, demo, or a workflow in three frames. The first product slide should land the core "what does it do for the buyer" message in the headline — not require the investor to read three slides to understand the value proposition. Live demos fail and waste meeting time; screenshots are reliable. Save the demo for diligence.

### 7. Traction and metrics

Progress over time. Timeline or metric chart. Highlight the standout proof point. The headline metric varies by sector: default rate by vintage cohort (lenders); ARR + NRR (SaaS); volume-through-platform (vertical-fintech); kWh or MW deployed (hard-tech); ticket / fan revenue (sport-tech / events). Match the metric to the audience. **Red flags:** vanity metrics ("10,000 signups" without conversion economics); burying the lead under four bullets before the standout number.

### 8. Business model and unit economics

How money is made. CAC + LTV at minimum. The math should be cell-pasteable — a sophisticated investor wants to plug your numbers into a model in five minutes. Sector-specific unit economics matter: gross yield + cost of funds + expected loss + NIM annualized for credit; ARR + payback + NRR for SaaS; PPA pricing + asset utilization for hard-tech; revenue per club + sponsorship attach rate + platform take rate for sport-tech. **Red flags:** too complex (simple beats complex); flow diagrams instead of unit-economics math; missing CAC or LTV.

### 9. Competition and positioning

Name real companies. Use a 2×2 matrix or a feature-comparison table — nothing else. Choose 2×2 axes that reflect customer outcomes that matter (speed × ticket size; quality × price; coverage × specialization). Place real competitor logos honestly. Put yourself in the top-right. **Red flag:** listing tangential companies as competitors signals you don't understand the market; listing only direct competitors and ignoring substitutes signals the same.

### 10. Team

Photos + accomplishments. One sentence per founder connecting background to a specific capability or moat. **Why-this-team-now framing:** "Ex-McKinsey, MBA from Insper" is a bio. "Built the regional ag-credit risk model at [bank] before founding this; the underwriting model we use today is the third version of that thesis" is a wedge. **Red flag:** long advisor lists with no evidence of advisory contribution read as compensation for thin core team. If you don't have a strong founding team, fix that before fundraising; don't paper over it with advisors.

### 11. Financials and projections

Reading deck: revenue + growth rate + 12-month forward + key sensitivity. Full model goes in the data room. Listening deck: same numbers, less dense, narrated. **Realistic-stretch ratio:** years 1-2 should be defensible-realistic; years 3-5 should be stretch-but-attainable. Hockey-stick projections that show flat in year 1 and 100× in year 4 read as fabricated. Year 1 is what you'll actually do; year 5 is the case for what's possible. Sanity check: is your year-3 market-penetration rate reasonable against public companies and recent acquisitions in the sector?

### 12. Ask

Amount + the milestones the round enables. Avoid donut "use of proceeds" charts — they read as filler. Investors want to know what the money does, in milestones tied to dates.

> *Template: Raising \$[N]M to achieve [Milestone A], [Milestone B], [Milestone C] within [N] months. Runway: [N] months. Readiness for next round: [benchmarks you'll hit].*

"\$2M to hire 4 engineers" is filler. "\$2M unlocks the regulatory licensing milestone that opens the senior-tranche structure" is a thesis. Don't mention amounts already raised, deadlines, or terms in materials sent broadly — securities-law constraints apply in most jurisdictions; check counsel.

### 13. Use of funds

Quarterly milestones tied to the ask. What does the money do, in sequence, with what gating decisions? The investor reads this slide to verify that the ask amount is calibrated to the milestones — not picked because it sounded right. **Red flag:** use of funds reads as a hiring plan rather than a milestone plan.

### 14. Roadmap

Where the company goes in 12-18 months and what unlocks the next round. Sequential logic, not a list. The roadmap slide answers the implicit investor question: "if I write this check, what does the round-after-this look like, and what evidence will exist by then?" **Red flag:** roadmap is a feature backlog rather than a sequence of milestones with associated risk types being retired.

### 15. Close

Vision + tagline + contact. The Close slide is what investors screenshot when they share your deck internally. One line of vision (anchored, not aspirational), the tagline from the cover, and your contact details. Keep it clean — this slide is the last impression.

---

## Part 3 — Self-checks as you build

Four quality gates worth running as you draft, not after you've finished. The first scores 12 dimensions across the deck. The second is the question set investors will ask — anticipate them on the slides. The third scores 5 questions per individual slide. The fourth is a checkbox quality gate to run before the deck goes anywhere external. All four turn the audit rubric into something you can apply to your own work.

### 1. Twelve dimensions worth scoring yourself on

Score each dimension green / yellow / red as you draft. The score is diagnostic — the point is the prioritized fix list, not the number. If a dimension is yellow or red after the draft, that is what to work on next.

| # | Dimension | What good looks like |
|---|---|---|
| 1 | Cover earns the page turn | Tagline does three things in eight words; not just the company name |
| 2 | Problem is quantified for one archetype | One pain, ≤10 words, ≤3 supporting bullets, named buyer |
| 3 | Solution mirrors the Problem bullets | Solution bullet 1 answers Problem bullet 1; no "and" connectors |
| 4 | Why now is specific, not generic | Names the technology / regulatory / market shift in your sector |
| 5 | Market is bottom-up | Buyer count × annual spend × geography, not industry-total wallpaper |
| 6 | Product shows > tells | Screenshot or workflow in three frames; headline lands the value |
| 7 | Traction has the right metric | Sector-tuned headline metric with cohort/vintage discipline |
| 8 | Business model has CAC + LTV | Cell-pasteable math; not a flow diagram |
| 9 | Competition names real companies | 2×2 matrix or feature table; honest about competitor strengths |
| 10 | Team has a why-this-team-now wedge | One sentence per founder connecting background to current moat |
| 11 | Financials pass the realistic-stretch ratio | Years 1-2 defensible; years 3-5 stretch; not a 100× hockey stick |
| 12 | Ask is milestone-tied | Amount + 12-month milestones; not a donut chart |

### 2. Questions to anticipate

A working investor — VC partner, family-office principal, DFI officer — will walk into the meeting with a standing question set. The deck does not need to answer all of them on the slide; it needs to make the founder's answer easy to find or easy to volunteer. Build the deck assuming these questions get asked; if your deck doesn't address one, the meeting will.

**Company questions.** What is the history of the company — when did you start operating, and why did you start it? How did you find your team, and why are you the right people to execute? What is your target market size, and what is your projected market penetration in year five? What is your traction to date — MVP done, user growth, revenue, key milestones? Why will you fail — what are your biggest challenges? Why will you succeed — what are your unfair, sustainable competitive advantages? Show me LTV > CAC.

**Capital-raising questions.** What is the capital-raising history — how much, at what terms? When did you start raising this round? What investors have hard-committed versus soft-committed? Have you invested any of your own money? Are your advisors or board members investing? What are your terms — valuation, structure? How much cash is in the bank, what is your monthly burn rate, and how much runway does that give you? What are the use of proceeds and the expected milestones?

If a question on this list cannot be answered in two sentences without reaching for a separate document, that is the next thing to fix on the deck.

### 3. Five questions to ask yourself per slide

Run these on every slide as you draft it. Anything that fails a check is a structural hole.

| Check | Question | Red flag |
|---|---|---|
| **Completeness** | Does the slide fully answer the question its position implies? | States a topic but doesn't make an argument |
| **Evidence** | Are claims supported by data, not assertions? | "Large market" with no number; "strong traction" with no chart |
| **Clarity** | Is the message clear to a non-expert on first read? | Jargon-heavy, multi-concept slides requiring re-reading |
| **Credibility** | Will a sophisticated investor believe this? | Unattributed market data, unrealistic projections, vague competitive claims |
| **Consistency** | Does it align with the narrative of other slides? | Problem describes a pain that the Solution doesn't address |

### 4. Pre-finalization quality gate

Run this checklist before sending any deck version externally. The checks complement the rubric in subsection 1; the rubric scores structure, this gate verifies craft.

**Headlines.**

- [ ] Every headline is a complete sentence with a clear assertion.
- [ ] Takeaway is stated, not just a topic label.
- [ ] Most important information is front-loaded.
- [ ] Two lines or fewer.
- [ ] Includes specific data where relevant.
- [ ] Reading only headlines tells the full investment thesis.

**Body content.**

- [ ] Every bullet directly supports its slide headline.
- [ ] Each bullet is two lines or fewer.
- [ ] Five or fewer bullets per slide.
- [ ] Filler words removed.
- [ ] Active voice throughout.
- [ ] No banned phrases present (see subsection 5).

**Data integrity.**

- [ ] Every number is contextualized with a comparison or benchmark.
- [ ] Notation formats are consistent throughout (currency, large numbers, percentages, ratios).
- [ ] External data sources are attributed.
- [ ] Numbers are appropriately rounded — no false precision.
- [ ] Financial projections pass a sanity check against public comparables.

**Narrative coherence.**

- [ ] Problem → Solution bullets mirror each other.
- [ ] Traction evidence directly demonstrates Solution claims.
- [ ] Market size connects to Business Model revenue math.
- [ ] Competition slide is honest about competitor strengths.
- [ ] Ask milestones are tied to specific metrics, not use-of-proceeds.

**Investor litmus tests.**

- [ ] Would this convince a skeptical institutional investor?
- [ ] Is anything unsubstantiated or hand-wavy?
- [ ] Does every slide pass the "so what?" test?
- [ ] Could a non-expert understand the thesis in one read-through?
- [ ] If an investor reads only the first five slides, do they stay?

If a category has more than two unchecked boxes, treat that category as a gating issue — fix before sending.

### 5. Slide writing discipline

**Assertion, not description.** Slides are arguments, not topics. "Market size" is a topic. "The addressable mid-market segment is \$4.2B and growing 18% annually" is an assertion. Headlines should be complete sentences with a clear claim — reading only headlines should tell the full thesis.

**Banned phrases:** empty superlatives (innovative, best-in-class, world-class, cutting-edge, game-changing, unique); buzzword fog (synergy, holistic, robust, paradigm shift, end-to-end, disrupt, revolutionize); hedging ("we believe," "helping to," "scalable solution" — say what scales and by how much); unearned claims ("first-mover advantage" unless proven; "conservative estimates").

**Data standards:** Currency: \$2M, R\$300M. Large numbers: 1,800+. Percentages: 15%. Growth: 4× YoY. Always contextualize numbers with comparisons or benchmarks. Attribute external data with source and date.

---

## Part 4 — Stage and AI-era considerations

Two cross-cutting layers worth running over the draft once Part 2 lands: which risk type your stage is selling down, and which AI-era framings apply to your slides.

### 1. Tottman risk types by stage

Fundraising is not about raising money — it's about systematically removing the reasons for investors to say no. Each stage has a dominant risk the deck must address head-on.

| Stage | Dominant risk | Objective | Proof points |
|---|---|---|---|
| **Pre-Seed** | Technical risk | Prove you can build it | MVP, early users, feasibility evidence |
| **Seed** | Market risk | Prove it solves a real pain | Customer engagement, retention, early revenue |
| **Series A** | GTM risk | Repeatable, efficient customer acquisition | One scalable channel, CAC/LTV, conversion funnel |
| **Series B** | Scalability / TAM risk | Scale into a large market | New geos / verticals, ops systems, exec team |
| **Series C+** | Culture / people risk | Sustain culture under rapid scaling | Mission codification, leadership systems, retention |

A Series A deck that emphasizes technical execution while ducking GTM economics signals the founder doesn't understand what's being underwritten. Trapdoor questions: pre-seed "can you build it?"; seed "will anyone pay?"; Series A "can you sell it repeatably?"; Series B "can this become huge?"; Series C "can your people sustain this?"

### 2. AI-native vs AI-applied

Investors reward AI-native; AI-applied gets discounted as a thin wrapper. The discount is not about using AI — it's about whether the company *requires* the model wave to exist. **AI-native tells:** model-version history as moat; proprietary dataset that compounds with use; features that are impossible without modern foundation models. **AI-applied tells:** "we use AI to..." framings that could be replaced with "we use better software" without changing the thesis; AI as a feature rather than a structural moat.

### 3. Why-now for the model wave

Articulate why-now in your sector specifically, not generically. Three classes: capability unavailable 18 months ago; cost curve crossed a buyer threshold; compound effect of capability + data + regulatory or distribution change. The strongest why-now combines two of these. The weakest is a hand-wave at "the model wave" — investors read ~50 of these per week.

### 4. Wave-1 copilot anti-pattern

Wave 1 (2023-24) sold copilots — "10× productivity," seat-based pricing. Wave 2 (2025-26) sells outcomes — "AI does the job; you sell finished work," outcomes-based pricing. The standalone copilot has become a platform feature. Founders pitching Wave-1 in a Wave-2 market read as undifferentiated. Flag on Solution and Product slides: "saves time," "copilot for [role]," "augments expertise" → Wave-1 tells. "Delivers [outcome]," "ships finished [artifact]" → Wave-2 tells. Productivity gains are real — the flag is that productivity-only pitches sit in a category investors are now discounting.

### 5. Service-as-Software (with the labor-budget caveat)

Companies sell outcomes, not tools. The artifact looks like services to the customer but operates as software internally (AI executes; humans QC). **Honest caveat:** labor budgets don't always migrate to AI vendors — they sometimes evaporate as the price of the underlying outcome falls with automation diffusion. A strong pitch has an explicit theory of where the labor budget goes and why the buyer's reservation price stays elevated for years before competition compresses.

---

## Part 5 — Process discipline

A great deck is necessary but not sufficient. The process around the deck — how you run the round once the deck exists — determines outcomes more than most first-time founders expect. This is one short section because the deck is your current focus; once you ship a v1, [`playbook.md`](playbook.md) Part 6 covers running the round in detail.

### 1. Compress, then warm the funnel

Fundraises that drag past 6 weeks lose momentum. Investors smell desperation in slow rounds. The discipline: compress to 3-4 weeks of meeting density (LatAm and EU cadence; NA can compress to 2-3 weeks). Pre-warm the funnel the four weeks before "officially raising" — intro pings, not formal meetings. When the round opens, all meetings happen in a tight window and partners feel the heat.

### 2. Have the data room ready before the first partner meeting

A hot first meeting triggers a diligence request the same week. The data room should already exist before you send the first deck — not assembled reactively. Twelve sections to have ready: executive summary; pitch deck; financials (3-year historical P&L + 5-year model + cohort analysis); cap table; customer / contract data; competitive landscape; product / architecture; team (bios + hiring plan + comp); legal / corporate structure; references; risk factors; use-of-funds detail. For credit-instrument and structured-product raises, add securitizadora structure docs, term sheets, custodian and trustee letters, regulatory filings, and prior-deal-performance data.

### 3. Read hot vs cold signals

| Signal | Hot round | Cold round |
|---|---|---|
| First meeting | Partner joins last minute; vision/future questions; next steps discussed immediately | Associate handles full meeting; deep dive into current metrics; "great to learn more" |
| Follow-up | Same-day; direct partner contact; specific next steps | "Will update next week"; communication via associates; vague timeline |
| Diligence | Parallel checks; quick reference calls; expansion focus | Sequential requests; extensive customer calls; risk focus |
| Term sheet | Terms before full diligence; clean docs; short expiration | "Post-diligence terms"; complex docs; open-ended timeline |

> *Rule: if you're wondering whether your round is hot or cold, it's cold.*

### 4. Multi-term-sheet running

Once you have one term sheet, the others compress. Don't lie. Do communicate state: "We're in late-stage diligence with three other partners" is honest and creates competitive tension. Set a clear close date with a specific reason (board meeting, signing date, regulatory window). Use the first term sheet's 7-14 day expiration as a forcing function for the others. Beyond 3 active term sheets, marginal benefit drops fast and your time cost rises sharply.

---

## Where to start

Three steps from a blank page to a v1 deck.

**Step 1 — Lock the upstream decisions (30 minutes).** Read Part 1 and write down three answers before opening any slide template: (a) reading deck or listening deck first (always reading deck first); (b) which of the four Founder Institute frameworks leads your arc — Problem/Solution, Vision/Opportunity, Team, or Traction; (c) which sector flags apply. These answers shape slide order, metric priority, and competitive framing. Getting them wrong at the start costs two rounds of revision downstream.

**Step 2 — Draft the canonical 15 slides (one focused day).** Work through Part 2 in order. Draft the Cover, Problem, and Solution first — they are upstream of everything else. Then Why now, Market, Product, Traction in sequence. Business model, Competition, Team, Financials, Ask, Use of funds, Roadmap, Close round it out. Each slide gets a complete sentence as a headline, ≤5 bullets, no banned phrases. The first draft should take six hours of focused work, not three weeks.

**Step 3 — Run the self-checks (45 minutes).** Run Part 3's twelve dimensions across the whole deck, the questions-to-anticipate set against your standing answers, the five questions across each slide, and the pre-finalization quality gate before anything goes external. Anything yellow, red, or unchecked is what to work on in the second pass. The goal is not a perfect deck on first draft — it is a deck that fails the right checks on first draft, so the second pass fixes the structural holes rather than re-litigating tone.

**Once you have a v1 — send it back.** [`playbook.md`](playbook.md) (audit-mode methodology) and [`lens_template.md`](lens_template.md) (the sector-tuned lens system) take over from here; [`cowork_workflow.md`](cowork_workflow.md) walks the iteration loop in Claude.ai. Send us a v0.5 of your deck and we will run our tool against it — it is currently in beta, the feedback genuinely helps us improve the kit, and you get a sector-tuned audit at the same time.

**A note on the two-decks rule for your raise.** Start with the reading deck. It forces every claim to stand without your narration. Once the reading deck is clean, stripping it into the listening deck takes half a day. The reverse direction — building the listening deck first — tends to produce slides that depend too heavily on narrative and don't stand alone when emailed to a partner who missed the meeting. Every slide in the reading deck should pass the test: does the headline alone, without the body copy, tell the investor something concrete?

---

## Companion tools

The Field Guide is the Step 0 of the kit — for founders pre-deck. Once you have a v1, the rest of the kit takes over:

- [`playbook.md`](playbook.md) — the audit methodology, 38 numbered sections in 8 parts. Standalone-readable.
- [`lens_template.md`](lens_template.md) — the fillable 13-section sector-tuned lens schema.
- [`cowork_workflow.md`](cowork_workflow.md) — how to run the iterative-audit loop in Claude.ai (no Claude Code required).
- [`SKILL.md`](SKILL.md) — the Claude Code orchestration skill if you run the developer CLI.
- [`examples/`](examples/) — five worked sector lenses (credit-fintech, regulated structured-product, hard-tech, M&A teaser, structurer-to-counterparty proposal).

Send us a v0.5 of your deck once you have one and we will run our tool against it.

## Contacts

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

---

*Pitch Deck Field Guide · v0.1-beta · 6 May 2026*
*Authored by Bamboo DCM · [bamboodcm.com](https://bamboodcm.com) · São Paulo, Brazil*
*License: [CC-BY 4.0](https://github.com/bamboo-DCM/library/blob/main/LICENSE) — free to share and adapt with attribution.*

Sources synthesized: Founder Institute Pitch Structure Guide; J. Skyler Fernandes "The Best Startup Pitch Deck"; Chris Tottman "The Reasons Why Investors Say No"; Frank Rotman five-statement framework; Aaron Dinin "Why Most Fundraising Pitches Fail"; Peter Thiel *Zero to One*; Liran Belenzon "How to Get Multiple Term Sheets in Three Weeks"; a16z Big Ideas 2026; Bessemer Venture Partners ServiceTitan investment memo (publicly published).
