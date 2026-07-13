# Pitch deck audit playbook

**Version 0.1.0-beta · 5 May 2026**

A methodology for auditing fundraise decks (and structurer-to-counterparty proposals, M&A teasers, and the VC investment memos that come back about you) using a sector-tuned lens. Synthesizes Founder Institute, Sequoia, McKinsey writing discipline, and patterns drawn from a working corpus of credit-fintech, regulated structured-product, hard-tech, and M&A teaser material — extended for the AI-era 2026 reality.

**About this playbook.** This is a methodology, not a slide-design tool. It assumes you already have a deck (or are sketching one) and want to audit it against a sector-tuned rubric. If you don't yet have a deck, start at [`field_guide.md`](field_guide.md) — it is the build-mode entry point for founders authoring their first deck, with slide-by-slide guidance and self-check questions. Once you have a v1, this playbook (audit-mode) and [`lens_template.md`](lens_template.md) (sector-tuned lens) take over. The kit's distinctive contribution is the *lens system* — see [`lens_template.md`](lens_template.md) and [`cowork_workflow.md`](cowork_workflow.md).

**Who it's for.** Founders raising rounds. Structurers writing commercial proposals. Advisors writing sell-side teasers. Operators inside firms who help portfolio companies sharpen pitches. Reading level: business-literate; no developer or finance-PhD prerequisites.

**Status.** Versioned beta. Narrow distribution while the substrate gets pressure-tested in the wild. Bug reports, disagreements, and pushback wanted — contacts at the bottom.

**The kit's distinctive pattern: lens-as-system.** Most public pitch deck guides ship as a static document. This kit ships two paired surfaces — the playbook (what to do) and the lens system (how to apply it iteratively to your specific company). The lens system is what makes the kit a tool, not just a document. See Part 8.

**v0.1-beta does not cover** marketplace / two-sided platform fundraises or fund / PE LP pitches. Both are deferred to a future release pending exemplar curation. Use [`lens_template.md`](lens_template.md) for these in the interim.

---

## Table of contents

**Part 1 — What you're producing**
1. Artifact classes
2. The two-decks rule
3. Framework selector

**Part 2 — Mechanical core (fundraise deck baseline)**
4. Slide-by-slide map
5. Cover and one-sentence pitch
6. Problem and solution
7. Why now
8. Market and sizing
9. Product / how it works
10. Traction and metrics
11. Business model and unit economics
12. Competition and positioning
13. Team
14. Financials and projections
15. Ask and use of funds

**Part 3 — Audit and quality gate**
16. Per-slide priority tiers
17. The 23-category rubric
18. The 5-criterion gap analysis
19. Pre-finalization quality gate
20. Slide writing discipline

**Part 4 — Stage-based de-risking**
21. Tottman risk types by stage
22. Rotman five-statement frame
23. Thiel's 10 questions (generic)
24. Hot vs cold round signals

**Part 5 — AI-era extension**
25. AI-native vs AI-applied
26. Service-as-Software (with the labor-budget caveat)
27. Why-now for the model wave
28. The Wave-1 copilot anti-pattern
29. Agent-speed infrastructure framings

**Part 6 — Process discipline**
30. Belenzon timeboxed running
31. LatAm and EU process variations
32. Data-room spine
33. Multi-term-sheet running

**Part 7 — Other artifact classes (compressed)**
34. Structurer-to-counterparty proposals
35. Sell-side M&A blind teasers
36. Reading a VC investment memo about you

**Part 8 — The lens system**
37. How to use the sector lens annexes
38. How to fill the blank lens template

---

# Part 1 — What you're producing

## 1. Artifact classes

Most pitch deck guides treat "pitch deck" as one artifact. It isn't. Before opening slide structure, determine which of four artifact classes you're producing — they have different conventions, different audiences, and different audit criteria.

| Class | Audience | Default length | Distinctive features |
|---|---|---|---|
| **Fundraise deck** | Investors (VC / PE / DFI / family office) | 10–14 slides (reading); 14–20 (listening) | The bulk of this playbook. Equity round, credit-instrument equity wedge, strategic round, bridge — all variants. |
| **Structurer-to-counterparty proposal** | Issuer evaluating a structuring firm to mandate | 12–25 slides | DCM / securitization / FIDC proposals. Process diagram + term sheet + events of default + garantias central; no TAM, no team bios at length. See §34. |
| **Sell-side M&A blind teaser** | Potential buyers screening anonymized targets | Sub-6 slides | Advisor-fronted, anonymized issuer, no team, no competition. See §35. |
| **VC investment memo (received)** | You, the founder, reading what the VC wrote about you | Prose, no slides | What VCs write internally about deals. Useful to read so you understand what comes back from a partnership meeting. See §36. |

The default for the rest of Parts 2–6 is the fundraise deck. The other three classes are covered in Part 7.

---

## 2. The two-decks rule

Every fundraise has two decks, even if the founder ships one and uses it for both:

- **The reading deck.** Sent over email, read by an investor in 4–7 minutes without the founder present. Denser. Self-contained slide titles that carry the thesis without narration. 10–14 slides.
- **The listening deck.** Presented in a meeting, narrated by the founder. Lighter on each slide; more whitespace; more slides (14–20) because each one supports a verbal beat rather than standing alone.

Most founders ship the reading deck and use it as the listening deck. Symptoms: dense slides, founder reads off the screen, investor disengages by slide 4. Or they ship the listening deck and email it. Symptoms: investor opens the PDF, sees half-empty slides, can't tell what the company does, doesn't reply.

**The fix:** maintain both. Same content, different density. The reading deck's slide titles are full assertions ("$X originated across N deals validates the underwriting model"); the listening deck's are short hooks the founder elaborates on ("Why we win"). The reading deck is the pre-meeting attachment; the listening deck is the in-meeting tool.

Founder Institute names this distinction explicitly. Most other guides skip it. Don't.

---

## 3. Framework selector

Three orthogonal axes determine what the deck looks like. Walk all three before opening slide structure:

**Sector** — generic / credit-fintech / regulated structured-product / hard-tech / banking-infra / vertical-fintech-workflow / sport-tech / biotech / [your sector]. Determines which sector lens applies. The kit ships five worked sector lenses and a blank template.

**Stage** — pre-seed / seed / Series A / Series B+ / growth. Determines which risk type the round is selling down (see §21) and what carries the narrative (founder story for early; metrics for Series A; scalability proof for Series B+).

**Instrument** — equity / credit-instrument equity wedge / structured-product distribution / debt facility / strategic round / bridge / acquisition. Determines what the investor is really buying. Most founders default to "equity" and miss that they're actually pitching a credit-instrument equity wedge or a structured-product distribution.

For the equity-raise branch specifically, Founder Institute's 4-framework selector is the next layer:

| Framework | When to use | Lead slide after elevator |
|---|---|---|
| **Problem / Solution** | Solve a clear, evidenced problem for a paying customer archetype. Have data to quantify the problem. | Problem → Solution |
| **Vision / Opportunity** | Creating a new market or a "why now" bet on a trend inflection. | Vision → Opportunity |
| **Team** | Founding team's credibility is the wedge; domain leaders that command attention. | Team (immediately after elevator) |
| **Traction** | Growth and metrics are top-tier for stage; progress over time is the story. | Traction (immediately after elevator) |

Pick exactly one. Don't mix. All slides that follow must serve the chosen arc.

---

# Part 2 — Mechanical core (fundraise deck baseline)

The slide-by-slide map below is the canonical baseline for fundraise decks. Sector lenses (Part 8) override or extend it; if your sector lens doesn't override a particular slide, the canonical version applies.

## 4. Slide-by-slide map

The canonical 15-slide flow:

| # | Slide | Purpose |
|---|---|---|
| 1 | Cover | Logo + tagline + sub-tagline (see §5) |
| 2 | Problem | Pain, quantified, for one customer archetype |
| 3 | Solution | Mirror the problem bullets — opposite outcomes |
| 4 | Why now | What changed in the last 18 months that opens this space (see §7) |
| 5 | Market | Bottom-up TAM, ending in your actual addressable customer base |
| 6 | Product / how it works | Show > tell. Screenshots or workflow in 3 frames |
| 7 | Traction | Time series of the metric that matters most for your stage |
| 8 | Business model | How money is made; CAC + LTV; not a pricing menu |
| 9 | Competition | 2×2 matrix or feature comparison; honest about what each plays well |
| 10 | Team | Why this team; one sentence per founder connecting background to a moat |
| 11 | Financials | Projections + path to next round milestones |
| 12 | Ask | Amount + use of funds + 12-month milestones |
| 13 | Use of funds | What the money does; quarterly milestones tied to ask |
| 14 | Roadmap | Where the company goes in 12–18 months and what unlocks the next round |
| 15 | Close | Vision + tagline + contact |

Common variants: 5-slide format (Elevator + Problem-Market + Solution-Traction + Team + Ask) for rapid screening; 30-slide format (full flow + appendix slides for diligence) for late-stage rounds.

Sector overrides: credit-fintech adds a capital-stack / leverage-wedge slide between Slides 8 and 9; hard-tech adds a country macro slide before Slide 5 and a multi-round capital plan after Slide 14; regulated structured-product replaces the entire flow with a three-pillar arc + disclaimer wall + cronograma.

## 5. Cover and one-sentence pitch

The cover earns the page turn. Logo + "Pitch Deck — Q2 2026" earns nothing.

The cover carries a tagline + sub-tagline that does three things in eight words or less:

1. States who you serve (specific, not "users")
2. Implies what's broken or what's unique
3. Earns the right to make the reader turn the page

The "only X for Y" formula works often: clean, memorable, claims a category. Sequoia's framing — "not just better, but different" — applies here.

Founder Institute's elevator pitch templates are the next layer:

**4-sentence elevator template** — fill each line:
1. *We help [customer]*
2. *do [specific job]*
3. *better, faster, or cheaper than [alternative]*
4. *because [unique advantage]*

**5-sentence one-minute pitch:**
1. Hook (one-liner)
2. Problem (quantified)
3. Solution (mirror to problem)
4. Why us / why now
5. Ask

**Common issues:**
- Average good investor sees ~100 decks per week and spends ~4:30 on a deck. Hook them in the first 2 slides.
- Always number slides for phone discussions and post-meeting follow-up.

## 6. Problem and solution

The Problem slide states one crisp problem in ≤10 words and supports it with ≤3 quantified bullets. The Solution slide mirrors the Problem bullets — exact opposites.

**Customer-confusion red flag.** Your customer is who pays. Founders often write the Problem slide for an end user who isn't the buyer. Fix: name who pays, then state the pain *they* feel.

**Unfocused red flag.** Founders pile pains onto the Problem slide because each one feels load-bearing. Pick one. The deck has 14 other slides for nuance.

**Mirror discipline.** Solution bullet 1 directly answers Problem bullet 1, and so on. If you need "and" to connect two ideas in a Solution bullet, you have two solutions and one of them belongs elsewhere.

Founder Institute's per-slide diagnostics for Problem and Solution are the canonical reference here.

## 7. Why now

The single most under-invested slide in early-stage decks. Most founders skip it or write a generic "AI is hot" gesture.

**The forcing function:** what changed in the last 18 months that makes this company possible (or necessary) now? Three classes of answer:

- **Technology shift.** New capability (modern foundation models, agentic workflows, real-time data infrastructure) that was unavailable or impractical 18 months ago.
- **Regulatory shift.** New rule, new license category, new disclosure regime, new resolution opening a market that was closed.
- **Market shift.** Customer behavior change (fintech-distribution maturity in LatAm, energy macro inflection, supply-chain re-shore) that opens a window.

The honest answer often combines two. The dishonest answer ("AI is having a moment") gets discounted as undifferentiated. The investor reads ~100 decks per week and most of them claim a why-now built on "AI." Specificity wins.

Cross-reference: Part 5 (AI-era extension) covers AI-specific why-now framings.

## 8. Market and sizing

**Bottom-up beats top-down.** Top-down ("$365B Brazilian private credit market") is a wallpaper number. Bottom-up ("addressable customers × annual spend per customer × geography count = a specific addressable spend pool, of which we serve N today") is a thesis. Replace the bracketed elements with your real numbers.

The bottom-up math:

- **Buyer count** — how many actual addressable customers
- **Annual spend per buyer** — what they pay today for the closest existing alternative
- **TAM** — buyer count × annual spend
- **SAM / SOM** — constrain by geography, segment, channel

**Vanity-sizing red flag.** "Brazilian agriculture is a $215B market." That's the wallpaper. Your TAM is a slice of that wallpaper, anchored to your specific addressable wedge.

**Credit Suisse pyramid trap.** TAM funnels that look like the Credit Suisse global wealth pyramid (broad-to-narrow, with each layer roughly an order of magnitude smaller) read as canned. Build your funnel from your actual unit economics, not from a template.

## 9. Product / how it works

Show > tell. Screenshots, demo, or a workflow in three frames. Multi-slide section if needed.

**Customer-confusion red flag.** Don't bury the lead. The first product slide should land the core "what does it do for the buyer" message in the headline, not require the investor to read three slides to understand the value proposition.

**Demo-vs-screenshots trade-off.** Live demos fail and waste meeting time. Screenshots are reliable. Most listening decks should use screenshots; the demo, if any, comes later in diligence.

## 10. Traction and metrics

Progress over time. Timeline or metric chart. Highlight the standout proof point.

**Sector-tuned metric:** the headline metric varies by sector. Default rate (lenders) / ARR (SaaS) / volume-through-platform (vertical-fintech) / kWh-as-leading-unit (hard-tech) / deals-structured-volume (DCM). Match the metric to the audience.

**Vanity-metrics red flag.** "10,000 signups" without conversion economics; "viral growth" without retention. Investors discount metrics that don't tie to revenue or sustained engagement.

**Don't bury the lead.** If you have one standout proof point, lead with it. Don't make the investor scan four bullets to find it.

## 11. Business model and unit economics

How money is made. CAC + LTV at minimum. For credit-fintech: per-loan gross yield, cost of funds, expected loss, opex per loan, contribution margin, NIM annualized — not a flow diagram. For SaaS: ARR, gross margin, payback period, NRR. For hard-tech: PPA pricing, kWh-cost economics, asset utilization.

**Common issues:**
- Too complex — simple beats complex
- Unfocused — one or two revenue streams maximum
- Missing CAC + LTV — table stakes for most rounds

The math should be cell-pasteable: a sophisticated investor wants to plug your numbers into a model in five minutes.

## 12. Competition and positioning

Name real companies. Use a 2×2 matrix or a feature-comparison table. Nothing else.

**2×2 axes:** customer outcomes that matter (speed × ticket size; quality × price; coverage × specialization). Place real competitor logos honestly. Put yourself in the top-right.

**Matrix:** rows are competitors; columns are buyer-relevant capabilities; ✓ / – per cell; end with one sentence on why you win.

**Bad-competitor-choices red flag.** Listing tangential companies as competitors signals you don't understand the market. Listing only direct competitors and ignoring substitutes signals the same.

For vertical-fintech-workflow patterns: a vs-DIY / vs-incumbents pricing comparison table is often more load-bearing than a 2×2 — investors want to see how a buyer choosing between you and the incumbent justifies the switch on price + capability.

## 13. Team

Photos + accomplishments. One sentence per founder connecting background to a specific capability or moat.

**Why-this-team-now framing.** Don't list bios; explain why each founder's background is load-bearing for this specific company at this specific moment. "Ex-McKinsey, MBA from Insper" is a bio. "Built the regional ag-credit risk model at [bank] before founding this; the underwriting model we use today is the third version of that thesis" is a wedge.

**Advisor-stack inflation red flag.** Long advisor lists with no evidence of advisory contribution read as compensation for thin core team. If you don't have a strong founding team, fix that before fundraising; don't paper over it with advisors.

Don't include advisors unless they're truly needle-moving. One to three brief bullets per person, or a single key bullet per person.

## 14. Financials and projections

The reading deck and listening deck have different financials density.

**Reading deck:** revenue + growth rate + 12-month forward + key sensitivity. Investor can take it or leave it; full model goes in the data room.

**Listening deck:** same numbers, less dense, narrated. Founder talks through the path; the slide carries 3–5 bullets, not a full P&L.

**Realistic-stretch ratio.** Projections should be defensible-realistic in years 1–2 and stretch-but-attainable in years 3–5. Hockey-stick projections that show flat in year 1 and 100× in year 4 read as fabricated. Year 1 is what you'll actually do; year 5 is the case for what's possible.

Standard format:

| Metric | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Target market | … | … | … | … | … |
| Total customers | … | … | … | … | … |
| Paying customers | … | … | … | … | … |
| Market penetration | … | … | … | … | … |
| Gross revenue | … | … | … | … | … |
| EBITDA | … | … | … | … | … |
| EBITDA margin | … | … | … | … | … |

Sanity check: market-penetration rate reasonable? Compare public companies and recent acquisitions in the sector for margin benchmarks.

## 15. Ask and use of funds

Amount + the milestones the round enables. **Avoid donut "use of proceeds"** charts — they read as filler. Investors want to know what the money does, in milestones tied to dates.

Template:

> Raising $`[N]`M to achieve `[Milestone A]`, `[Milestone B]`, `[Milestone C]` within `[N]` months.
> Runway: `[N]` months.
> Readiness for next round: `[benchmarks you'll hit]`.

**Common issues:**
- Don't mention amounts already raised, deadlines, or terms in materials sent broadly (securities-law constraints in most jurisdictions; check counsel).
- Focus on milestones, not use of proceeds. "$2M to hire 4 engineers" is filler. "$2M unlocks the regulatory licensing milestone that opens the senior-tranche structure" is a thesis.

For credit-instrument raises: the ask is in deployable-credit terms, not operating-runway terms. The equity that funds the first-loss layer of a structured-credit vehicle (sub-quota / first-loss tranche / equity wedge) supports a senior tranche stacked on top, and the deployable-credit total is the multiple — typically 4–7× the equity, depending on the structure and the credit-quality assumptions priced into the senior. The deck's ask should reflect the deployable-credit math, not just the equity check size.

---

# Part 3 — Audit and quality gate

## 16. Per-slide priority tiers

Every deck must address these questions. Flag any missing or weak.

| Priority | # | Slide | Core question |
|---|---|---|---|
| **Critical** | 1 | Executive summary / elevator | Why should I keep reading? |
| **Critical** | 2 | Problem | What pain exists and for whom? |
| **Critical** | 3 | Solution | How do you solve this pain? |
| **Critical** | 4 | Market size | Is this worth pursuing? |
| **Critical** | 5 | Product | What does the user actually experience? |
| **Critical** | 6 | Business model | How do you make money? |
| **Critical** | 7 | Traction | Is this working? |
| **Critical** | 8 | Team | Can you execute? |
| **Critical** | 9 | Ask / use of funds | What do you need and why? |
| **Important** | 10 | Why now | Why is this the right moment? |
| **Important** | 11 | Go-to-market | How will you acquire customers? |
| **Important** | 12 | Competition | Why will you win? |
| **Important** | 13 | Customer profile | Who exactly is the target buyer? |
| **Important** | 14 | Unit economics | Is growth sustainable? |
| **Important** | 15 | Roadmap | What will you do with the money? |
| **Nice-to-Have** | 16 | Testimonials / social proof | Do customers endorse you? |
| **Nice-to-Have** | 17 | Partnerships | Who validates / accelerates you? |
| **Nice-to-Have** | 18 | Global precedent / comparables | Has this worked elsewhere? |
| **Nice-to-Have** | 19 | Vision | Where does this go long-term? |

A Critical slide that's missing or weak is a structural hole the audit must surface. A Nice-to-Have slide that's missing is a stylistic choice.

## 17. The 23-category rubric

A diagnostic tool from review-pattern analysis of multiple decks against multiple investor types. Each category gets a color (green / yellow / red / missing) and a "what good looks like" anchor.

The categories:

1. Cover slide — earns the page turn
2. Tagline — survives without context
3. Problem — quantified, one customer archetype
4. Solution — mirrors problem bullets
5. Why now — specific, not generic
6. Market — bottom-up, anchored to your addressable
7. Product — show > tell
8. Traction — sector-tuned headline metric
9. Cohort discipline — vintage / cohort views, not headlines
10. Business model — CAC + LTV minimum
11. Unit economics — credible, sector-appropriate
12. Capital structure (if applicable) — visible for credit-instrument raises
13. Competition — comparative, not declarative
14. Positioning — 2×2 or matrix, real names
15. Team — wedge per founder
16. Advisor stack — proportionate, not compensation
17. Why-this-team-now — tied to current company moment
18. Financials — realistic-stretch ratio
19. Ask — milestone-tied, not use-of-proceeds
20. Use of funds — quarterly milestones
21. Roadmap — sequential logic, not list
22. Vision — anchored, not aspirational
23. Filler — every slide earns its place

Score each: green (5), yellow (3), red (1), missing (0). The total score is diagnostic — the point is the prioritized fix list, not the score.

Sector lenses replace specific categories with sector-tuned versions. A credit-fintech lens swaps category 11 for "default rate cohort discipline"; a hard-tech lens swaps category 11 for "PPA economics + asset utilization"; a regulated structured-product lens swaps multiple categories for CVM-160-equivalent disclaimer wall, cronograma, and risk factor list discipline.

## 18. The 5-criterion gap analysis

For each slide present in the deck, evaluate on five criteria:

| Criterion | Question | Red flag |
|---|---|---|
| **Completeness** | Does it fully answer the core question from the priority tier table? | Slides that state a topic but don't make an argument |
| **Evidence** | Are claims supported by data, not assertions? | "Large market" without a number; "strong traction" without a chart |
| **Clarity** | Is the message immediately clear to a non-expert? | Jargon-heavy, multi-concept slides requiring re-reading |
| **Credibility** | Will sophisticated investors believe this? | Unattributed market data, unrealistic projections, vague competitive claims |
| **Consistency** | Does it align with the narrative of other slides? | Problem slide describes pain that Solution slide doesn't address |

Output structure for each slide: one line per criterion, ✓ / ⚠ / ✗ flag, plus a short note on what's missing or weak.

## 19. Pre-finalization quality gate

Run this checklist before sending any deck version externally.

**Headlines.** Every headline is a complete sentence with a clear assertion. The takeaway is stated, not just a topic label. Most important information is front-loaded. Two lines or fewer. Specific data where relevant. Reading only headlines tells the full thesis.

**Body content.** Every bullet directly supports its slide headline. Each bullet is two lines or fewer. Five or fewer bullets per slide. Filler words removed. Active voice throughout. No banned phrases (see §20).

**Data integrity.** Every number is contextualized with a comparison or benchmark. Notation formats are consistent (currency, large numbers, percentages, ratios — see §20.6). External data sources attributed. Numbers appropriately rounded (no false precision). Financial projections pass sanity check.

**Narrative coherence.** Problem → Solution bullets mirror each other. Traction directly demonstrates Solution claims. Market size connects to Business model revenue math. Competition is honest about competitor strengths. Ask milestones tied to specific metrics, not use-of-proceeds.

**Investor litmus tests.** Would this convince a skeptical institutional investor? Anything unsubstantiated or hand-wavy? Does every slide pass the "so what?" test? Could a non-expert understand the thesis in one read-through? If an investor reads only the first 5 slides, do they stay?

## 20. Slide writing discipline

Discipline rules for *how* to write slide content once structure is locked.

**Pyramid principle.** Lead with the answer, then support it. The reader should understand your point from the first line. Everything after is evidence.

**One slide, one message.** Each slide makes exactly one claim. If you need "and" to connect two ideas, you need two slides.

**Assertion, not description.** Slides are arguments, not topics.

| Wrong (descriptive) | Right (assertive) |
|---|---|
| "Market size" | "The addressable mid-market segment is $4.2B and growing 18% annually" |
| "Our team" | "Founding team built and exited two infrastructure businesses in the last decade" |
| "Traction" | "$X originated across N deals across three vintages with sub-2% lifetime loss" |
| "Business model" | "Three revenue streams converging on software-margin economics by Y3" |

**Headline rules.**
- Complete sentences with a standalone assertion
- Front-load the insight — most important information first
- Quantify where possible — specificity builds credibility
- Maximum two lines — if longer, tighten
- Use parallel structure across listed items

**Headline formulas that work:**

| Formula | Example |
|---|---|
| "[Metric] proves [conclusion]" | "N deals × sub-2% lifetime loss proves underwriting model durability" |
| "[Company] does [X], resulting in [Y]" | "We compress diligence from 3 weeks to 48 hours, opening a buyer segment incumbents can't serve" |
| "[Number] [things] demonstrate [point]" | "Three vintage cohorts demonstrate underwriting model durability" |
| "[Insight]: [evidence]" | "The mid-market is structurally uneconomical for incumbents: per-deal analyst cost consumes a third of fees" |
| "[Claim] — [proof]" | "Regulatory moats compound — license takes 3+ years to replicate" |

**Body copy.**
- 3–5 bullet points maximum per slide
- 1–2 lines per bullet maximum
- Under 40 words per bullet
- Each bullet is a mini-argument: assertion first, evidence after
- Active voice, no passive
- Eliminate filler

**Banned phrases.**

| Category | Banned |
|---|---|
| **Empty superlatives** | "Innovative," "best-in-class," "world-class," "cutting-edge," "game-changing," "unique" |
| **Buzzword fog** | "Synergy," "leverage," "holistic," "robust," "paradigm shift," "end-to-end," "disrupt," "revolutionize" |
| **Hedging** | "We believe," "helping to," "scalable solution" (say what scales and by how much) |
| **Unearned claims** | "First-mover advantage" (unless proven with data), "conservative estimates," "huge market" |

**Tone.**
- Confident, not arrogant. State facts clearly without hedging or overstating.
- Precise, not vague. Every claim specific enough to verify.
- Active, not passive. Subject does the action.
- Investor-centric. Frame in returns, risk, scalability, defensibility.

**Data presentation standards.**

| Format | Use | Don't use |
|---|---|---|
| Currency | $2M, R$300M | $2 million, R$300 million |
| Large numbers | 1,800+ issuances, 4M users | 1800 issuances, 4,000,000 users |
| Percentages | 15%, 2.15% | 15 percent, 2.15 per cent |
| Ratios | 4.1x LTV/CAC | 4.1 times LTV to CAC |
| Growth | 4x YoY, 2x QoQ | 300% year-over-year |
| Rounding | $90M+ (not $91.3M) | Excessive precision undermines credibility |

Always contextualize numbers with comparisons or benchmarks. Attribute external data with source and date. Prefer multiples (4x YoY) for large changes, percentages for small (<100%).

---

# Part 4 — Stage-based de-risking

## 21. Tottman risk types by stage

Chris Tottman: "Fundraising is not about raising money — it's about systematically removing the reasons for investors to say 'no.'"

| Stage | Dominant risk | Objective | Key actions |
|---|---|---|---|
| **Pre-Seed** | Technical risk | Prove you can build it | MVP, early users, proof of feasibility |
| **Seed** | Market risk | Prove it solves a real pain | Customer engagement, retention, early revenue |
| **Series A** | Go-to-market risk | Show repeatable, efficient customer acquisition | One scalable channel, CAC/LTV, conversion funnel |
| **Series B** | Scalability / TAM risk | Prove it can scale into a large market | Expand TAM, new geos / verticals, ops systems, exec team |
| **Series C+** | Culture / people risk | Sustain culture under rapid scaling | Codify mission and values, leadership systems, retention |

**Trapdoor questions by stage:**
- Pre-Seed: "Can you build it?"
- Seed: "Will anyone pay for it?"
- Series A: "Can you sell it repeatably?"
- Series B: "Can this become huge?"
- Series C: "Can your people sustain this?"

The deck should obviously address the stage's dominant risk. A Series A deck that emphasizes technical execution while ducking GTM economics signals the founder doesn't understand what's being underwritten.

## 22. Rotman five-statement frame

Frank Rotman's complement to Tottman: every startup makes assertions in five categories, and the round depends on generating proof (or anti-proof) of each.

| Statement class | What you assert | What investors test |
|---|---|---|
| **Problem** | This pain exists for this customer | Is the customer real? Does the pain quantify? |
| **Solution** | This product addresses the pain | Does it work? At what cost? |
| **GTM** | We can find and convert these customers repeatably | Channel CAC, conversion %, sales cycle |
| **Financial** | This produces durable economics | Margin, payback, retention, NIM |
| **Team** | We can execute this | Background fit, prior wins, key gaps |

Tottman names risk types; Rotman names assertion classes. Use both. The audit looks for evidence (or anti-evidence) per assertion class, mapped to stage-appropriate proof points.

## 23. Thiel's 10 questions (generic)

From *Zero to One*. Every startup answers these implicitly; the deck should answer them explicitly enough that the investor doesn't have to interrogate.

| # | Question | What it means |
|---|---|---|
| 1 | **Engineering** | Can you create breakthrough technology (10x better) instead of incremental improvements? |
| 2 | **Timing** | Is now the right time? Are market conditions favorable? |
| 3 | **Monopoly** | Are you starting with a big share of a small market? |
| 4 | **People** | Do you have the right team? |
| 5 | **Distribution** | Do you have a way to deliver, not just create? |
| 6 | **Durability** | Will your market position be defensible 10–20 years from now? |
| 7 | **Secret** | Have you identified a unique opportunity others don't see? |
| 8 | **Alignment** | Is the team deeply aligned on vision and incentives? |
| 9 | **Political moat** | Do you benefit from regulations or political conditions that shield you? |
| 10 | **Narrative control** | Can you shape the narrative of your industry to your advantage? |

Bill Gross's research: timing accounts for ~42% of success/failure variance. Question 2 is load-bearing.

## 24. Hot vs cold round signals

Liran Belenzon's signal taxonomy. Founders should read these signals before walking into a meeting.

| Signal | Hot | Cold |
|---|---|---|
| **First meeting** | Partner joins call last minute; questions about vision/future; discussing next steps instantly | Associate handles full meeting; deep dive into current metrics; "great to learn more" |
| **Follow-up** | Same-day follow-up; direct partner messages; specific next steps | "Will update next week"; communication via associates; vague timeline |
| **Diligence** | Parallel checks; quick reference calls; focus on expansion | Sequential requests; extensive customer calls; focus on risks |
| **Partner dynamic** | Multiple partners engage; weekend availability; proactive intros | Single point of contact; standard hours; you chase next steps |
| **Term sheet** | Terms before full diligence; clean docs; short expiration | "Post-diligence terms"; complex docs; open-ended |
| **Temperature** | They respond in hours; you set the timeline; terms get better | You wait days; they control process; terms get worse |

Rule: if you're wondering whether your round is hot or cold, it's cold.

---

# Part 5 — AI-era extension

The 2026 model wave changes what investors expect on certain slides — particularly Why now, Product, Competition, and the Moat narrative. This part covers what's mature enough to bake into a deck today and what's still too speculative for a versioned-beta playbook.

**Out of scope for v0.1-beta:**

- Specific multiples / valuations / "AI premium" math — too volatile, founders should look at current market data when they raise, not at a kit dated 2026.
- Model-economics deep-dives (training costs, inference unit economics) — infrastructure-specific topic, not generic deck content.
- Detailed "pitching to a16z vs Sequoia" prescriptive framings — too prescriptive; the lens system teaches founders to read VC theses themselves rather than memorize them.

## 25. AI-native vs AI-applied

The distinction matters in 2026. **AI-native** companies are structurally impossible without modern foundation models — agentic workflows, semantic search at scale, model-driven underwriting. **AI-applied** companies are traditional businesses that use AI as a tool.

Investors reward AI-native; AI-applied gets discounted as "thin wrapper." The discount is not about using AI — it's about whether the company *requires* the model wave to exist.

How the audit checks this:

- **AI-native tells:** model-version history as moat (how the company uses successive model generations); proprietary dataset that compounds (the data the AI learns from is unique to the company); product features that would be impossible without modern models (e.g., real-time semantic underwriting on heterogeneous documents).
- **AI-applied tells:** "we use AI to" framings without showing what's structurally different; AI claims that could be replaced with "we use better software" without changing the thesis; model-as-feature rather than model-as-moat.

Cross-references: credit-fintech lens (consumer-credit AI lender variant); hard-tech lens (agent-speed infrastructure).

## 26. Service-as-Software (with the labor-budget caveat)

a16z framing: companies sell outcomes, not tools. The artifact looks like a services firm to the customer (finished work delivered) but operates internally as a software company (AI does execution; humans do QC). Margin profile reframes service-firm economics: $6 services revenue per $1 software revenue, AI captures the labor budget.

**The honest caveat.** When machines do the work, work gets repriced at machine rates. Labor budgets don't always migrate to AI vendors — they sometimes evaporate as the price of the underlying outcome falls. The bullish framing assumes labor budgets transfer; the skeptical framing assumes they collapse. Both happen depending on the industry and the structure of the buying decision.

How the audit checks this:

- **Strong Service-as-Software pitch:** explicit theory of where the labor budget goes (which buyer pays the new margin, why they pay it, what alternative they're choosing against). Often: a regulated or specialized labor pool whose existing rate is above the new automation cost; the savings accrue to the buyer for years before competition compresses.
- **Weak Service-as-Software pitch:** assumes 1:1 transfer of labor budget to the company. Doesn't address why the buyer's reservation price stays elevated as automation diffuses.

## 27. Why-now for the model wave

Most decks claim a why-now anchored on "AI is hot." This gets discounted heavily — the investor reads ~50 of these per week.

The discipline: articulate why-now in *your sector specifically*, not generically. What changed in your sector — not in AI broadly — that opens this window? Three classes of sector-specific why-now:

- **Capability that wasn't possible 18 months ago.** Specific model capability (long-context retrieval, agentic workflows, multimodal understanding) that solves your specific problem in a way that didn't work before. Show the prior-attempt graveyard if it exists.
- **Cost curve crossed a threshold.** The unit cost of the AI execution dropped below the buyer's reservation price for the outcome. Specific numbers help.
- **Compound effect just hit.** The combination of (a) modern model capability + (b) accumulated data + (c) regulatory or distribution change creates a window that closes for late entrants.

The strongest why-now combines two of these. The weakest is a hand-wave at "the model wave."

## 28. The Wave-1 copilot anti-pattern

Wave 1 (2023–24) generative-AI startups sold copilots — "tool that makes your worker more productive." Wave 2 (2025–26) sells outcomes — "AI does the worker's job; you sell finished work." The standalone copilot has become a feature, not a company.

Founders pitching as Wave-1 in a Wave-2 market read as undifferentiated. The deck audit should flag Wave-1 framings on the Solution and Product slides:

- **Wave-1 tells:** "saves time," "10x productivity," "your team's AI assistant," "augments expertise," "copilot for `[role]`."
- **Wave-2 tells:** "delivers `[outcome]`," "replaces `[manual workflow]`," "ships finished `[artifact]`," outcomes-based pricing rather than seat-based pricing.

This isn't a rule against productivity claims — productivity gains are real. It's a flag that productivity-only pitches sit in a category investors are now discounting because the standalone-copilot outcome has been bundled into platform features.

## 29. Agent-speed infrastructure framings

The biggest infrastructure shock of 2026 comes from inside companies — the shift from human-speed traffic (predictable, low concurrency) to agent-speed (recursive, bursty, massive). Energy / manufacturing / logistics / industrial AI-native infrastructure is back in focus.

For hard-tech and infrastructure raises specifically, the agent-speed framing matters:

- **Energy:** demand for compute (training + inference) materially shifts grid composition. PPAs, hyperscaler load curves, and renewable-firmness arguments land differently in 2026 than 2022.
- **Industrial automation:** the unit of work moves from humans-with-software to agents-with-tools. Vertical applications that took human teams to scale now run as agent fleets.
- **Logistics / supply chain:** real-time multi-agent coordination becomes possible at scales that were academic two years ago.

For hard-tech decks, the why-now slide should land at least one of these. Cross-reference: hard-tech lens annex.

---

# Part 6 — Process discipline

A great deck is necessary but not sufficient. The process around the deck — how you run the round — determines outcomes more than most founders expect.

## 30. Belenzon timeboxed running

Liran Belenzon's discipline for running a round in three weeks instead of three months:

- **Compress to 14–21 days.** Fundraises that drag past 6 weeks lose momentum. Investors smell desperation in slow rounds.
- **5 first-meetings per day × 14 days = 70 first meetings.** That funnel becomes ~7 partner meetings, ~3 term sheets at a 10:1 ratio (depending on stage and round heat).
- **Pre-warm the funnel.** Spend the four weeks before "officially raising" doing intro pings, not formal meetings. When the round opens, all 70 meetings happen in a 2–3 week window.
- **Close fast.** Once you have one term sheet, the others compress. The first term sheet's expiration window is your second round of leverage.

This is North America cadence. See §31 for the LatAm / EU adjustments.

## 31. LatAm and EU process variations

Belenzon's NA-cadence assumes:
- Partners take Monday morning meetings as the default
- Term sheets move in days, not weeks
- "Hot rounds" happen frequently enough that 10:1 conversion holds
- Network density is high enough that 70 first meetings is achievable

In LatAm and EU, the cadence shifts:

- **Slower default.** Most VC partner cycles run weeks, not days. A 14-day calendar window is unusual; 6–8 weeks is normal.
- **Warmer intros required.** Cold pitches under-perform; intros from portfolio CEOs or known LPs carry more weight than NA defaults.
- **Lower meeting density.** 70 first meetings is hard outside the largest LatAm financial centers (São Paulo) or EU hubs (London / Paris / Berlin / Stockholm). Plan for 30–40.
- **Lower conversion to term sheet.** 10:1 may stretch to 15:1 or 20:1.

Adjust the timebox accordingly. A 6-week LatAm round with 35 meetings and 2 term sheets is the equivalent shape of a 3-week NA round with 70 meetings and 3 term sheets.

## 32. Data-room spine

Belenzon's 12-section data room. This is what diligence will actually request after a hot first meeting:

1. **Executive summary.** Two pages: what the company is, the round, the asks-and-answers.
2. **Pitch deck.** The reading deck.
3. **Financials.** Historical P&L (3 years if available), 5-year forward model, cohort analysis.
4. **Cap table.** Current and post-round.
5. **Customer / contract data.** Top contracts, ARR breakdown, retention by cohort.
6. **Competitive landscape.** Detailed comp set, pricing comparison, win/loss analysis.
7. **Product.** Architecture overview, roadmap, key technical differentiators.
8. **Team.** Bios, hiring plan, comp plan, equity policy.
9. **Legal / corporate structure.** Cap structure, options pool, IP, key contracts, regulatory licenses.
10. **References.** Customer / partner / employee references, available on request.
11. **Risk factors.** What could go wrong, and the mitigation logic.
12. **Use of funds detail.** Quarterly milestones, hiring waterfall, spend categories.

For credit-instrument and structured-product raises, the spine adds: securitizadora structure documentation, CRA / FIDC term sheets, custodian and trustee letters, regulatory filings, prior-deal-performance data.

## 33. Multi-term-sheet running

Once you have one term sheet, the others compress. Mechanics:

- **Don't lie.** Investors compare notes more than founders expect. "We have other term sheets" is a question they will verify.
- **Do communicate state.** "We're in late-stage diligence with three other partners" is honest and creates competitive tension.
- **Set a clear close date.** Not "next week" — a specific Tuesday with a clear reason (board meeting, signing date, regulatory window).
- **Use the first term sheet's expiration as forcing function.** Most term sheets carry 7–14 day expiration. That's the window for the others to step up.
- **Don't over-shop.** Beyond 3 active term sheets, marginal benefit drops fast and the time cost on the founder rises sharply.

A clean multi-term-sheet process closes 2–3 weeks after the first one lands. A messy one drags to 6+ weeks and signal-degrades.

---

# Part 7 — Other artifact classes (compressed)

## 34. Structurer-to-counterparty proposal

DCM / securitization / FIDC / ABS proposals from a structuring firm to a potential issuer. Different artifact, different audience, different conventions.

**What's different from a fundraise deck:**

- **No TAM.** The audience is one issuer evaluating one proposal — not a market opportunity.
- **No team bios at length.** A short credentials section, then move to the structure.
- **The process diagram is central.** A 3–5 step diagram of what the structurer does (originate / structure / distribute / monitor / report) is often the single most important slide.
- **Term sheet inline.** Pricing, fees, tenor, events of default, garantias — the proposal includes the actual proposed terms, not just a generic capability deck.
- **Tail and exclusivity language.** What happens if the issuer goes elsewhere mid-process. Specific to structurer mandate work.

For a worked example with abstracted placeholders, see [`examples/structurer-proposal.md`](examples/structurer-proposal.md) (ships in v0.1.0-beta as part of Phase 3b).

## 35. Sell-side M&A blind teaser

Advisor-fronted blind teaser to potential acquirers. Format is radically different from fundraise decks.

**Conventions:**

- **Anonymized issuer.** Sub-6 slides identify the company by sector + scale + one differentiator, with a project codename. The buyer requests an NDA to learn the issuer's identity.
- **No team.** The seller's team isn't relevant at the teaser stage.
- **No competition.** Competition is a fundraise discussion; in M&A, the relevant comparison is the buyer's strategic alternatives.
- **Advisor-fronted contact.** All inquiries route through the advisor; the issuer is not directly contactable until NDA.
- **Market tailwinds + market sizing brief.** Why this sector now, what the addressable buyer set looks like.

Common audit failures: issuer-identifying details leak through (specific city, specific revenue figure that uniquely identifies); advisor contact buried in fine print; sub-6-slide promise broken (advisors over-author).

For a worked example, see [`examples/m-and-a-teaser.md`](examples/m-and-a-teaser.md).

## 36. Reading a VC investment memo about you

After a partnership meeting, the investor often writes an internal memo about your deal. Sometimes they share it with you. Sometimes they don't. Either way, knowing what these documents look like shapes how you interpret what comes back.

A canonical investment memo (the publicly available Bessemer Venture Partners memo on ServiceTitan is a strong reference point) carries:

- **Bottom-line recommendation up front.** Invest / pass / monitor, with confidence level.
- **Diligence apprehensions and how we resolved them.** A section explicitly walking through risks, what was tested, and what the residual concern is.
- **Customer / expert call synthesis.** Often the longest section. Quotes, sentiment patterns, what users actually do.
- **Market sizing — bottom-up.** With the math shown.
- **Competition.** With internal honesty about competitor strengths.
- **GTM.** What the company does well, where the channel stress-tests yet to land.
- **Financials.** Including sensitivity analysis and downside cases.
- **Team.** Including key gaps the investor would help fill.
- **Risks named explicitly with mitigation logic.** Not hidden in footnotes.
- **Outcomes analysis.** Best case / base case / downside, with the math on each.
- **Redaction conventions** for sensitive material (`$X.Xk` placeholders).

The memo is **prose, not slides.** It's 8–25 pages typically. It's written for a partnership vote, not for the founder.

**How to use this knowledge:**

- If you receive a memo back, read it for the apprehensions section first. The decision usually turns on what was *not* fully resolved.
- If you don't receive a memo, the structure tells you what was probably discussed. The "we passed because…" email is usually a one-line summary of the apprehensions paragraph.
- If you write your own memo against your own deck (a pre-mortem), you find the apprehensions before the investor does.

This section is read-only — there's no "fillable" lens for a memo you receive. It's context for interpreting what the partnership-meeting outcome means.

---

# Part 8 — The lens system

The kit's distinctive contribution. Most public pitch deck guides ship as a static document. This kit ships two paired surfaces: the playbook (what to do) and the lens system (how to apply it iteratively to your specific company).

## 37. How to use the sector lens annexes

Five worked sector lenses ship in v0.1.0-beta:

- **`examples/credit-fintech.md`** — credit-instrument raises, ag-fintech, consumer-credit AI lenders, lending businesses
- **`examples/regulated-structured-product.md`** — FIDC, ABS, regulated structured-product marketing material
- **`examples/hard-tech.md`** — energy infrastructure, mining, capital-intensive hardware
- **`examples/m-and-a-teaser.md`** — sell-side blind teasers, advisor-fronted M&A material
- **`examples/structurer-proposal.md`** — structurer-to-counterparty commercial proposals

Pick the lens closest to your company. Read it end-to-end. The lens has 13 sections following the schema in [`lens_template.md`](lens_template.md), filled with the sector-specific content (sector framework, sector red flags, sector-specific audit rubric criteria, sector-specific objection bank).

**You don't have to use the lens as-is.** Two patterns work:

- **Direct use.** If the lens fits your company well, point Claude at it and run audits. Edit Section 1 (company identity), Section 9 (objection bank with your real investors' questions), Section 10 (your real comparables) — keep the rest.
- **Edit-down.** If the lens fits structurally but the specifics are wrong, save a copy as `[your-company]_lens.md` and edit aggressively. The 13-section schema is the structure; the company-specific content is replaceable.

## 38. How to fill the blank lens template

If none of the worked sector lenses fits, use [`lens_template.md`](lens_template.md). It has the same 13-section schema, with `[FILL]` placeholders instead of sector-specific content.

The first sitting takes 60–90 minutes. The lens that wins your round is the one you've edited 10 times — every real investor meeting surfaces an objection you didn't anticipate, and the lens gets sharper when you add it.

See [`cowork_workflow.md`](cowork_workflow.md) for the full iteration loop.

---

# Closing

This is a methodology, not a slide-design tool. The deck is the artifact; the lens is the source of truth. The audit is the diagnostic; the prioritized fix list is the action.

The first audit is the *least* valuable use of this system. The tenth audit, after you've taught the lens what your investors really care about, is what wins the round.

Found a bug? Disagreement? Open an issue at [github.com/bamboo-DCM/library](https://github.com/bamboo-DCM/library) or email any of the contacts below. Pushback wanted.

---

**Authored by Bamboo DCM** ([bamboodcm.com](https://bamboodcm.com)) — the independent infrastructure for Brazil's corporate and structured credit market, with an intelligence layer on top.

Comments, improvements, or questions:

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

License: [CC-BY 4.0](https://github.com/bamboo-DCM/library/blob/main/LICENSE) — free to share and adapt with attribution.

*This playbook is part of an internal knowledge-systems framework Bamboo DCM has been building for AI-native execution in regulated finance. If the broader framework is interesting, get in touch — we're publishing more as we package them.*

Sources synthesized: Founder Institute Pitch Structure Guide; J. Skyler Fernandes "The Best Startup Pitch Deck"; Chris Tottman "The Reasons Why Investors Say No"; Frank Rotman five-statement framework (X / Twitter, Jul 2023); Aaron Dinin "Why Most Fundraising Pitches Fail Within the First 5 Minutes"; Peter Thiel *Zero to One*; Liran Belenzon "How to Get Multiple Term Sheets in Three Weeks"; pitch.guide review framework; a16z Big Ideas 2026 (Parts 1–2); Linas Beliūnas "What to Build in 2026"; GTMnow Jennifer Li interview on AI infrastructure investment; Bessemer Venture Partners ServiceTitan investment memo (publicly published).

Version 0.1.0-beta · 5 May 2026
