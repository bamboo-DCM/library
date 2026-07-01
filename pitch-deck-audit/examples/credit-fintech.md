# Pitch deck lens — credit-fintech / credit-instrument raise

**What this file is.** A filled sector lens for a credit-fintech company raising a credit-instrument equity round — the structure where investor equity funds the first-loss layer of a debt vehicle (FIDC, ABS facility, sub-quota structure), with senior tranches stacked on top for capital efficiency. The single most important structural fact about this sector is that the deck is not pitching generic growth equity: it is pitching the equity that makes the leverage of senior tranches possible. Every slide either supports or undermines that thesis.

**Source.** Abstracted from a worked audit lens for an ag-fintech credit-instrument raise (Brazil, bootstrapped → Series A, three harvests of operating data). Sector-adjacent reference: Percent / Percent A55 ABS proposal structure (Source / Structure / Syndicate / Surveil framework; publicly available memo). Consumer-credit AI lender variant: see §11 sub-section below.

**How to use this file.** Read §§1–3 to understand the company type and raise structure. Jump to §7 (audit rubric) and §8 (red flags) before running your first audit. Treat §9 (objection bank) as a living document — add every hostile question you hear in real investor meetings.

**This is a living document.** The first fill takes 60–90 minutes. The version that closes a round has been edited after every investor conversation. The leverage-wedge framing in §2 and §11 is the section that compounds fastest — sharpen the math with actual numbers before you show the deck.

**See also.** [`playbook.md`](../playbook.md) §§2, 7, 8, 10, 11, 15, 25 for the methodology behind each section. [`cowork_workflow.md`](../cowork_workflow.md) for the iteration loop. [`lens_template.md`](../lens_template.md) for the blank version of this schema.

---

## 1. Company identity

```
Company: [a digital lender to mid-sized crop producers — fill with your company name]
Sector: Brazilian rural credit, ag-fintech, digital lending to small and mid-sized agricultural producers
Stage: Bootstrapped / pre-Series A (three full harvest cycles of operating data)
Geography: Brazil, five core producing regions
Founded: 20XX
Headline metrics: [N] active borrowers, R$[X]M credit portfolio, [N]% monthly portfolio growth,
  [N]x LTV/CAC, sub-2% cumulative default rate across three vintage cohorts,
  [R$XM] credit instrument already placed
Team: [N] founders — agricultural domain expertise (research institution background,
  field operations) + financial markets expertise (structured credit, fintech)
Product today: short-term working-capital loans to crop producers, digital app,
  automated underwriting, sub-24-hour approval, in-house regional sales in core geographies
Roadmap:
  (1) working capital (no collateral required) — current
  (2) custeio loans with crop collateral — 12-month horizon
  (3) higher-ticket land-collateral loans — 24-month horizon
  (4) authorized distributor of government-subsidized credit — 36-month horizon
Vision: the digital bank for Brazil's mid-sized crop producers
```

**The raise.** R$[X]M equity. R$[X]M for team expansion and credit infrastructure. R$[X]M to seed the subordinated quota of a Fiagro/FIDC structure that lets the company scale credit deployment without proportional dilution. This sentence must appear on slide 1. If it is buried in the appendix, the deck fails its primary job.

---

## 2. Raise framing

This is not a generic growth-equity raise. It is the equity wedge that unlocks a multi-turn senior debt facility through a structured credit vehicle. The framing difference is not cosmetic — it determines the audience, the math, and the risk story.

**Why this matters to investors.**

A Brazilian Fiagro/FIDC issues senior cotas (lower risk, fixed return, distributed to institutional allocators) and subordinated cotas (first-loss, higher return, held by the originator for incentive alignment). Sub/senior ratios for early-stage agricultural credit funds typically range from 15–25% sub, meaning a single real of subordinated capital supports four to seven reais of senior capital — and thus four to seven reais of deployable producer credit.

An equity investor in this round is not funding operating runway. They are funding the first-loss layer of a credit machine that, once built, deploys multiples of their capital into the loan book and earns net interest margin on the spread between the senior cotas' coupon and the loan yield. This is a fundamentally different risk/return profile than a SaaS Series A. Investors who understand structured credit (private credit funds, family offices with credit exposure, agro-focused PE, DFI windows) will respond to the leverage math. Investors pitched as though this is a generic growth round will be confused or will pass.

**The math the deck must make explicit.**

| Layer | Amount | Source | Role |
|---|---|---|---|
| Subordinated quota (this raise) | R$[X]M | Equity investors | First loss, aligned with originator |
| Senior quota (Fiagro/FIDC) | R$[4X–7X]M | Institutional allocators | Fixed return, CDI + spread |
| Total deployable credit | R$[5X–8X]M | | |
| Loan book yield | [N]%/month | | |
| Net interest margin (target) | [REPLACE WITH YOUR REALITY]% | | |

Fill in the actual numbers before showing to any investor. The structure of the math is the contribution of this section; the specific figures must be yours.

See §11 for the draft leverage wedge slide.

---

## 3. Sector-specific slide arc

The generic 15-slide Sequoia arc is built for SaaS. A credit-instrument raise needs a different sequence because the questions investors ask are different. Sixteen slides, in this order:

| # | Slide | Purpose |
|---|---|---|
| 1 | Cover with tagline | Hook in eight words. No "Pitch Deck — [Month YEAR]." |
| 2 | Vision + one-liner | Where this is going + what we are today. Move vision forward — it currently lives at the end of most decks. |
| 3 | The credit cycle frame | Where in the producer's annual cycle the company plugs in, and why that point is structurally underserved. Missing from most lender decks. |
| 4 | Problem (cycle-anchored) | The specific pain at that cycle point, with one quantified bullet per pain. Not "credit is slow and bureaucratic" — anchor it to the cycle. |
| 5 | Solution (mirrors the problem) | The opposite outcome for each pain, plus one product screenshot. |
| 6 | Product | App screenshots or workflow, the user journey in three frames. |
| 7 | Market (anchored, not generic TAM) | Not "$215B Brazil agriculture." Instead: addressable cycle-point × addressable producer count × current spend on credit. End with the wedge: "we serve N of M today; here is the path to all M." See playbook §8. |
| 8 | Competitive landscape | Positioning matrix: speed × collateral requirement, or digital × cycle stage. Place the company alongside legacy banks, cooperatives, trading-house barter, and digital-native competitors honestly. |
| 9 | Business model + unit economics | Per-loan: gross yield, cost of funds, expected loss, opex per loan, contribution margin. Annualized into net interest margin. Not a flow diagram. |
| 10 | Capital stack and leverage wedge | The missing slide in most lender decks. Diagram of equity → sub quota → senior quota → deployable credit, with worked numbers. See §11. |
| 11 | Traction — cohort view | Three vintage cohorts side-by-side: disbursements, loss curve, average ticket, retention. The headline is the trend, not the latest number. |
| 12 | Traction — portfolio growth | Monthly bar chart with annotations for deliberate events (credit structure placement, drawdown periods, harvest seasonality). |
| 13 | GTM | How producers find the company today, channel-level CAC, conversion, the path from current scale to 10× origination. In-house sales + digital + referral mechanics. See playbook §9. |
| 14 | Moats that compound | Cycle position + proprietary borrower dataset + repeat-harvest network effects. Reorder so the structural moats come first; aspirational items go last. |
| 15 | Team | One sentence per founder connecting background to a specific moat or capability. See playbook §13. |
| 16 | Ask + use of funds + milestones | Amount, the explicit sub-quota framing, the leverage math, milestones tied to the next 12 months, what the next round looks like and when. |

Optional appendix: detailed cohort tables, regulatory wrapper (CVM, BCB, securitizadora), CRA/CRI deal terms, hiring plan, full financial projections, comparable raises.

---

## 4. Cover and tagline

The cover has one job: make the next slide irresistible.

**The "only X for Y" formula.** Clean, memorable, makes a category claim. Sequoia's framing: "not just better, but different" — the cover should claim a category, not a feature.

Five candidates for a digital agricultural lender:

```
1. "The only digital bank built for Brazil's mid-sized crop producers."
   Sub-tagline: Profitable from day one. Three harvests, sub-2% lifetime loss.
   Test: does it earn the page turn? Does it survive being said out loud?

2. "Banking the producers who feed Brazil — and the world."
   Sub-tagline: Digital credit infrastructure for the farmers legacy banks won't serve.
   Note: mission-framing works better with impact-aligned investors and DFIs.

3. "The credit operating system for Brazilian agriculture."
   Sub-tagline: Working capital today. The full credit cycle tomorrow.
   Note: infrastructure framing; plays well with "picks and shovels" investors.

4. "Crédito rural sem burocracia. Em 24 horas."
   Sub-tagline: O banco digital para o produtor que os bancos tradicionais ignoram.
   Note: Portuguese-first for Brazilian institutional allocators.

5. "[N] harvests. Sub-2% loss. R$[X]M deployed. One bank rebuilt from scratch."
   Sub-tagline: [Company] is the digital credit infrastructure for Brazil's crop producers.
   Note: proof-led; strongest if numbers hold, problematic if they slip.
```

**How to choose.** Test against three filters: (a) does it earn the page turn? (b) does it survive being said out loud at a coffee meeting? (c) does it still feel right after 30 days of use? If two candidates pass all three, pick the one that names the specific segment rather than the generic mission.

---

## 5. Sector framework

Every credit-fintech sector has an underlying model — a cycle, a macro force, a regulatory schema. In Brazilian rural credit, the underlying model is the **producer's annual crop cycle**, and the company's position in it determines everything: which products are possible, which competitors are relevant, which regulatory wrapper applies, and what the "why now" is.

```
Underlying model: the annual crop cycle of a grain or coffee producer
  (pre-plantio → plantio/custeio → growing → colheita → comercialização → reinvestimento)
Our position: working-capital gap in the pre-plantio and early-plantio window
  (the period when producers need liquidity before the main custeio structures open)
The structural gap: legacy banks and cooperatives focus on custeio (the large, collateralized
  window); tradings finance their own input sales; no digital-native player owns the
  pre-plantio working-capital window at scale
The shift underway: digital underwriting reduces the information asymmetry that historically
  made sub-collateral rural credit uneconomical for institutional lenders;
  three-harvest borrower datasets enable model-driven approval where physical appraisal
  was previously required
Why this position is underserved by incumbents: minimum ticket size economics don't work
  for legacy banks; tradings only finance producers who buy their inputs; cooperatives
  have geographic concentration and member-ownership constraints
```

**Optional cycle diagram.** Draw a horizontal timeline with crop-cycle stages along the x-axis, lenders layered as bars per stage, and your company's current and future products highlighted. This becomes slide 3 in the recommended arc (§3) and answers the "where do you play in the cycle" question before the investor asks it.

---

## 6. Cycle / positioning framework

```
Where we are in the cycle: scaling — post product-market-fit, pre-institutional-scale
  (the company has proven the underwriting model across multiple harvest cohorts;
  the constraint is now capital efficiency, not credit performance)
Where competitors are:
  - Legacy banks (BB, cooperatives): dominate custeio with government-subsidized rates;
    not competing for the pre-plantio working-capital window
  - Trading-house barter: input financing only, tied to the trading's own sales
  - Digital ag-credit competitors: most are at similar scale or Series B+;
    differentiation is on cycle position and geographic focus, not tech stack alone
Why now (sector-specific):
  - Three years of operating data from the first wave of digital ag lenders have proved
    the model is scalable; institutional allocators now understand the asset class
  - The Fiagro/FIDC regulatory wrapper (post-2021 CVM reform) provides a viable
    structure for raising senior capital from institutional allocators
  - Brazil's 5M+ small and mid-sized producers remain 90%+ underserved by digital credit
Why us:
  - [N] harvest cycles of proprietary underwriting data (no digital competitor has a
    longer track record in this specific cycle position)
  - Profitability at current scale (the company is not burning cash while proving the model)
  - The regulatory wrapper is structured — existing CRA places capital already in market
```

The "why now" answer here must match the "Why Now" slide (slide 7 in the canonical arc, or slide 4 in the lender-specific arc). If you cannot write a clean "why now" here, the slide will also fail. See playbook §7.

---

## 7. Audit rubric (12 criteria, 1–5 scoring)

When Claude runs an audit, it scores the deck against these 12 criteria. **5 = best in class; 3 = passable; 1 = problematic.** The scores are diagnostic — the point is the prioritized fix list.

| # | Criterion | What 5/5 looks like |
|---|---|---|
| 1 | Cover earns the page turn | Tagline + sub-tagline names the segment and the wedge in under 12 words. Reader can quote it back after one viewing. |
| 2 | First three slides answer "what is this" | By slide 3, an investor who has never heard of the company can describe in one sentence what it does, who it serves, and why it is different. |
| 3 | Credit cycle positioning is explicit | A diagram or sentence shows exactly where in the producer's annual cycle the company plugs in and why that point is underserved by legacy lenders. |
| 4 | Market is anchored, not generic TAM | TAM funnel ends in a number matching the actual addressable customer base — not a "total agricultural finance market" wallpaper figure. Anchored to cycle position. |
| 5 | Competitive positioning is comparative, not declarative | A 2×2 or matrix places the company next to legacy banks, cooperatives, trading-house barter, and digital-native competitors honestly, showing what each does well. |
| 6 | Unit economics are present and credible | Per-loan: gross yield, cost of funds, expected loss, opex, contribution margin, NIM. Not a revenue-flow diagram. Sector-agnostic LTV/CAC framing is insufficient for a credit business. |
| 7 | Capital stack and leverage wedge are visible | A diagram shows equity → sub quota → senior quota → deployable credit, with worked numbers. Investor understands what their capital is doing. This is the highest-priority missing slide in most lender decks. |
| 8 | Traction is shown in cohorts, not headlines | Three vintage cohorts side-by-side with loss curves, average ticket, and retention. The headline is the trend, not the latest single-period number. |
| 9 | GTM is explicit and quantified | How producers find the company today, channel-level CAC, conversion rates, and a credible path from current scale to the next order of magnitude. |
| 10 | Team slide carries the wedge each founder represents | One sentence per founder connects their background to a specific moat or capability — not "ten years of experience in X" but "built the underwriting model at [prior firm], which produced the dataset this company runs on." |
| 11 | The ask is matched to the instrument | The raise amount is broken down with the leverage math explicit. Reader knows what 12 months of progress looks like and what the next round looks like. See playbook §15. |
| 12 | No filler slides | Every slide earns its place. Vision is up front. No mid-deck "where are we" interludes. Appendix handles diligence detail, not the main flow. |

When Claude returns audit results, it should flag the **top 3 highest-impact fixes** — not the three lowest scores, but the three changes that move the deck the most for the smallest amount of work.

---

## 8. Sector-specific red flags

Generic red flags (vanity metrics, top-down TAM, undifferentiated team bios) apply to every deck. **These are the red flags a generalist auditor would miss on a lender deck.**

```
1. Headline default rate without cohort vintage curves.
   "Sub-2% default this harvest" reads as either heroic or naive depending on the
   maturity of the book. Show three vintage cohorts side-by-side so investors can see
   whether the model holds as the portfolio scales. A single-period default number
   without vintage context is unauditable.

2. LTV/CAC presented using SaaS mechanics.
   Lending LTV is dominated by net interest margin × duration × renewal rate, not
   by retention curves. An LTV/CAC multiple without showing how it was computed will
   be questioned immediately by any credit-fund investor.

3. Capital stack absent on a credit-instrument raise.
   The single biggest credibility gap in most lender decks. If the company is raising
   sub-quota equity and the deck doesn't show the senior tranche structure, sophisticated
   investors assume either (a) the structure hasn't been designed yet, or (b) the
   founders don't understand what they're selling.

4. Market sized in dollars, not in customers.
   "$215B Brazilian agriculture" is a wallpaper number. "[N]K producers in five regions
   with [R$X]K average annual credit demand, of which [N] are served today" is a thesis.
   See playbook §8 on bottom-up TAM.

5. GTM described as "we have an in-house sales team."
   That is an org structure, not a GTM. GTM is how the producer first hears about
   the company, what makes them apply, what makes them come back next harvest,
   and what the CAC is by channel.

6. Roadmap that reads as a list.
   Products 1, 2, 3, 4 without logic for the sequence looks arbitrary. The credit
   cycle framework (§5) gives the sequence its logic — each product deepens the
   company's position along the cycle as trust compounds.

7. "AI" mentioned as a feature, not a structural moat.
   In 2026, AI claims without a proprietary dataset are discounted as thin wrappers.
   Either show the proprietary borrower dataset that the model compounds on — vintage
   curves, behavioral signals, repayment timing by cycle stage — or don't lead with AI.

8. Regulatory wrapper absent.
   Credit-fund investors will ask: is this company a securitizadora, an SCD,
   a correspondente bancário? What is the role of the CRA emissora? Address it
   in the deck before they ask.

9. Mismatched register across slides.
   A deck that opens in a whisper ("Pitch Deck — March 2026") and ends with a shout
   ("Build the go-to digital bank for Brazil's farmers") has an inconsistency investors
   notice even if they can't name it. Calibrate the energy across all slides before
   finalizing.

10. Vague use of funds.
    "R$5M for hiring, R$10M for capital structure" is the seed of a good slide.
    Make it specific: which roles, which quarters, which milestones unlock the next
    capital event. The milestones tied to the ask determine whether the round story
    is coherent. See playbook §15.
```

---

## 9. Investor objection bank

When Claude red-teams the deck, it plays a hostile credit-fund LP and asks the hardest version of these questions. Add to this list after every real investor meeting.

**On credit performance:**

```
1. Your current harvest shows sub-2% default but the harvest isn't closed. What does
   the cohort look like at 50% maturity? At 80%?
2. Your sample is [N] borrowers. What's the statistical confidence on the underwriting
   model at this book size?
3. What's the worst loan you've made and what did you learn from it? If the answer is
   "we haven't had one," investors conclude you haven't been tested.
4. How does your default rate reconcile with the broader Brazilian rural credit default
   rate, which runs 4–7% depending on the cohort?
```

**On unit economics:**

```
5. What's your cost of funds on your placed credit instrument? What's the spread to
   your gross loan yield?
6. What's your fully-loaded contribution margin per loan, including allocated origination
   cost, servicing, collections, and provisioning?
7. What does the unit economic picture look like at 10× current borrower count?
```

**On capital structure:**

```
8. What's your target sub/senior ratio and who's lined up for the senior tranche?
9. If the senior tranche doesn't materialize, what does the company look like?
   Is this raise contingent on the structure or independent of it?
10. What's the duration mismatch between your loan book and your funding structure?
```

**On GTM and growth:**

```
11. Your sales force covers [N] regions. What's the CAC by region? Which region has
    the best unit economics and why?
12. Brazilian rural credit is relationship-driven. How do you scale a relationship
    business 10× without breaking the trust that makes it work?
13. What happens when a large state bank decides to compete on speed? They have the
    brand, the regulatory cost-of-funds advantage, and the existing relationships.
```

**On team:**

```
14. Who's your credit committee? Who do you call when you're looking at a deal you
    don't know how to underwrite?
15. Who handles regulatory — the relationship with CVM, BCB, and the CRA emissora?
```

**On market and timing:**

```
16. Why now? What changed in the last 36 months that makes this company possible
    today and harder to replicate three years from now?
17. The Brazilian digital ag-credit sector has seen multiple well-funded raises.
    Why does the market need another entrant and why is this company the one that wins?
18. What's the path to a R$1B loan book? At current growth, when does the company
    get there, and what breaks first?
```

**On exit:**

```
19. What's a realistic exit? Strategic acquisition by which acquirer? IPO?
    Continuation as an independent credit institution?
20. What's the comparable transaction you'd point to as the model exit?
```

---

## 10. Comparable raises

Anchor positioning against sector-comparable raises. Update at least monthly — comparable raises move fast.

| Company | Latest raise | Stage | What they pitched | What to take |
|---|---|---|---|---|
| Percent (US, ABS infrastructure) | Series B (2022); public memo available | Series B | "Source / Structure / Syndicate / Surveil" — a four-step infrastructure workflow for private credit. Pitched standardization of the private credit market, not just a lender. | The four-step framework is an explicit moat claim. If your company has a comparable workflow differentiation, name it with the same clarity. |
| [Brazilian digital ag-credit comparable] | [Recent equity + credit vehicle round] | Series A–C | Raised equity and a parallel credit vehicle simultaneously; proved the structure is fundable for institutional allocators. | Use this as a precedent that the sub-quota equity + senior-tranche structure is a known pattern LPs understand. |
| [Consumer-credit AI lender comparable] | [Recent round] | Series A–B | Led with AI underwriting model as structural moat (model-version history, feature-level differentiation, proprietary default dataset). | AI moat works only if tied to a proprietary dataset. The underwriting model is the asset; the AI stack is what it runs on. |

**What to avoid.** Do not position as "the next [comparable]" or "the better [other digital lender]." The investor's question is *why does this market need another entrant*, and the answer must be about cycle position and proprietary moat — not about being a clone with better technology.

---

## 11. Draft slide for the sector-specific moment

The leverage wedge slide is the missing slide in almost every lender deck. It is also the slide with the single highest return on investment for the time spent writing it.

```
Slide title: "The math of this round"

Headline: R$[X]M of equity → R$[4X–7X]M of deployable producer credit over 12 months.

Body:

[N] harvest cycles of underwriting data. Sub-2% lifetime loss. R$[X]M credit instrument
already in market. The engine works.

This round does two things. R$[X]M scales the team and credit infrastructure.
R$[X]M seeds the first-loss layer of a Fiagro/FIDC structure that lets every real
of this raise's equity support four to seven reais of senior cota capital from
institutional allocators.

| Layer | Amount | Source | Role |
|---|---|---|---|
| Subordinated quota (this raise) | R$[X]M | Equity investors | First loss, aligned with originator |
| Senior quota (Fiagro/FIDC) | R$[4X–6X]M | Institutional allocators | CDI + spread |
| Total deployable credit | R$[5X–7X]M | | |

At [N]%/month loan yield and a stress-tested [N]% default scenario, this structure
produces [REPLACE WITH YOUR REALITY]% NIM on the senior cotas and
[REPLACE WITH YOUR REALITY]% return on the subordinated layer.

Ask: investors in this round buy the leverage wedge — and the credit performance
that makes the wedge financeable.
```

**Notes on this slide.** Fill in the actual numbers. The structure of the math is right; every figure above is a placeholder. The NIM and return-on-subordinated calculations must be yours, verified with your structuring counsel. Do not show a worked example to an investor with [REPLACE WITH YOUR REALITY] still in it.

### Consumer-credit AI lender variant

If the company is a **consumer-credit AI lender** rather than a producer-credit fintech, the pattern differences are:

- **Leverage-wedge logic applies** but the vehicle changes (ABS facility, revolving line from a bank rather than Fiagro/FIDC). The math — equity funds first-loss, senior capital stacks on top — is structurally identical.
- **Default rate vs market benchmark is the headline metric**, not vintage crops. Replace "sub-2% across three harvest cohorts" with "sub-[N]% lifetime loss vs [N]% market rate" and show both numbers prominently.
- **AI model version history functions as the moat narrative.** Each model generation upgrade is a compound interest step in underwriting accuracy — if the company has three generations of model with documented performance improvements, show all three in a timeline. This is the "proprietary dataset that the AI compounds on" argument in its most concrete form.
- **Feature-level deep-dives demonstrate AI-nativeness.** A single behavioral signal that predicts repayment (time-of-day app usage patterns, SMS response timing, income-cycle triangulation) narrated as a worked example converts "we use AI" into "our model does something a human underwriter cannot replicate at scale." See playbook §25 (AI-native vs AI-applied).
- **Slide arc adjusts.** Drop the crop-cycle frame (§3, slide 3); replace with the **consumer-credit lifecycle frame** (acquisition → first loan → repayment → second loan → credit limit expansion → churn). The structural story is compound trust, not seasonal cycle.
- **MoM cohort compounding replaces harvest-vintage framing.** Show 12+ cohorts of monthly borrowers with identical axis scales so the compounding is visible without narration.

---

## 12. Style and voice guidance

- **Short sentences. Active voice.** No more than 15 words per slide bullet.
- **Numbers over adjectives.** Replace "rapid growth" with the actual growth rate. Replace "low default" with "sub-[N]% lifetime loss across [N] vintage cohorts."
- **Specific over generic.** Name the addressable customer count and the geography in one phrase. Abstract numbers ("a large opportunity") read as filler to credit-fund investors.
- **Match the language to the audience.** English for international investors; Portuguese for local institutional allocators. If the round is Brazil-led, lead with Portuguese.
- **Register: institutional-but-direct.** Lender decks that try to read like SaaS decks lose credibility with credit-fund LPs. The right register is the one a CFO of a private credit fund recognizes immediately as professionally prepared — precise, numerical, no hype.
- **No AI vocabulary.** Avoid: robust, comprehensive, holistic, utilize, paradigm, impactful, revolutionize. Use plain words.

**Voice rules specific to this company type:**

```
- Never "capital-light business model" — credit businesses hold the book;
  the capital efficiency story is in the leverage structure, not in pretending
  credit is software
- Never "growing rapidly" — show the MoM/harvest-over-harvest number
- Never lead with AI as a stand-alone claim — always pair with the proprietary
  dataset and a specific model output (default prediction at a specific accuracy)
- "Leverage wedge" is the correct technical term for the sub/senior structure;
  use it, it is not on the banned list
- Prefer Portuguese for regulatory terms: cota sênior / cota subordinada /
  fiagro / FIDC / cedente / cedido rather than English translations
```

---

## 13. What Claude should NOT do

- Claude should **not invent credit metrics** the company hasn't shared. If a slide needs a default rate, a NIM, or a CAC that Claude doesn't have, leave a `[REPLACE WITH YOUR REALITY]` placeholder.
- Claude should **not pretend to know Brazilian regulatory specifics** it isn't sure of. For CVM 88, Resolution BCB 4,656, Fiagro structure rules, CRA/CRI exemption limits, ask Claude to flag uncertainty and recommend verification with structured-finance counsel.
- Claude should **not substitute SaaS metrics for credit metrics.** Gross margin, ARR, and NRR are useful secondary signals for a credit-fintech but are not the primary underwriting story. The primary story is default rate, NIM, and capital efficiency.
- Claude should **not give 12 pieces of feedback when 3 would do.** The rubric's job is prioritization, not exhaustiveness. Top-3 highest-impact fixes first.
- Claude should **not flatten the leverage-wedge story into generic growth equity.** If the deck reads like a SaaS Series A, the audit failed. The leverage structure is the deck's most distinctive feature — every audit pass should check whether it is visible, correctly sized, and correctly framed for a credit-fund audience.

---

**Authored by Bamboo DCM** ([bamboodcm.com](https://bamboodcm.com)) — the independent infrastructure for Brazil's corporate and structured credit market, with an intelligence layer on top.

Comments, improvements, or questions:

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

License: [CC-BY 4.0](https://github.com/bamboo-DCM/library/blob/main/LICENSE) — free to share and adapt with attribution.

Version 0.1.0-beta · 5 May 2026
