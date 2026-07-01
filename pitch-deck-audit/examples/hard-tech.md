# Pitch deck lens — hard-tech / energy-infrastructure raise

**What this file is.** A filled sector lens for a hard-tech or energy-infrastructure company raising capital — specifically the type with physical assets (mining infrastructure, data centers, renewable energy generation, grid hardware, manufacturing facilities) where the unit of business is a physical-world metric (kWh, MW, tons, hectares, rack-units) rather than software metrics (ARR, MAU, NPS). The single most distinctive structural choice in a hard-tech deck is **leading with the physical unit, not the financial abstraction** — investors need to see the kWh economics, the PPA pricing, and the country energy macro before they can evaluate any revenue projection.

**Source.** Structurally abstracted from [hard-tech / Bitcoin-mining infrastructure exemplar (2022)], Series A pitch deck, 2022 (Bitcoin mining infrastructure, Paraguay/Brazil operations). The kWh-as-leading-unit convention, country-energy-macro framing, multi-round capital plan structure, and advisor-stack pattern are drawn from that deck. Agent-speed infrastructure cross-reference: playbook §29.

**How to use this file.** Sections 1–3 establish the company type and raise structure. Section 5 (country energy macro) and §6 (infrastructure cycle) are the sections most likely to be missing from a first-draft hard-tech deck — read them before running any audit. Section 11 (kWh-as-leading-unit slide) is the single highest-priority addition for most hard-tech decks.

**This is a living document.** The energy macro in §5 and §6 must be updated every six months — energy pricing, PPA availability, and grid policy change faster than most founders anticipate. Comparable raises (§10) become stale quickly in a sector where valuation multiples track energy-price and AI-demand volatility.

**See also.** [`playbook.md`](../playbook.md) §§3, 7, 10, 13, 14, 15, 25, 29 for methodology context. [`lens_template.md`](../lens_template.md) for the blank schema.

---

## 1. Company identity

```
Company: [a Bitcoin mining / energy infrastructure company — fill with your company name]
Sector: hard-tech, energy infrastructure, Bitcoin mining / [compute / manufacturing / grid]
Stage: pre-Series A / Series A (physical assets operational or pre-operational)
Geography: [country + region — e.g., Paraguay, Itaipu watershed; southern Brazil, Rio Grande do Sul]
Founded: 20XX
Physical asset base:
  - Capacity installed: [N] MW contracted / [N] MW operational
  - Energy source: [hydroelectric PPA / wind / solar / grid / hybrid]
  - PPA pricing: USD [N] / MWh (or R$ [N] / MWh)
  - Physical footprint: [N] hectares / [N] containers / [N] data-center rows
Headline metrics:
  - Hash rate (mining) or equivalent: [N] TH/s / EH/s
  - Revenue: USD [X]M (LTM or annualized)
  - EBITDA margin: [N]%
  - Mining cost per BTC: USD [N] (current) — vs network average USD [N]
Team: [N] people + [N] advisors
  - Core team: [N] (operations, engineering, finance)
  - Advisor stack: [list tier: strategic advisors / legal / energy procurement /
    capital markets / mining tech]
```

**The raise.** USD [X]M. [Describe the instrument: equity / convertible / project-finance debt / token]. [Describe the use: expand capacity from [N] MW to [N] MW; build data-center phase 2; acquire new PPA; fund multi-round capital plan]. See §2 for the multi-round framing that hard-tech investors require.

---

## 2. Raise framing

Hard-tech and energy-infrastructure raises differ from venture-equity raises in two fundamental ways: **the capital stack is larger and the return horizon is longer.** Infrastructure investors are not expecting a 10× return on a 5-year horizon; they are expecting yield + equity upside over an 8–12-year horizon with intermediate liquidity events at each phase.

**Multi-round capital plan framing.** Most hard-tech decks make the mistake of presenting one round as the entire funding path. Infrastructure investors need to see the full capital plan — not because they will fund all of it, but because they need to understand whether the current round is the one that de-risks the asset.

```
Phase 1 — Proof of concept (current / completed):
  Capital: USD [X]M (equity or convertible)
  Milestone: [N] MW operational, PPA signed, first revenue quarter
  De-risks: technology + energy-procurement assumptions

Phase 2 — Scaling (this round):
  Capital: USD [X]M (equity)
  Milestone: [N] MW operational, [N] TH/s hash rate, breakeven at USD [N]/BTC
  De-risks: operational scale, cost-per-kWh at production volume

Phase 3 — Institutional scale / pre-IPO:
  Capital: USD [X]–[X]M (project finance + equity)
  Milestone: [N] MW operational or IPO / strategic sale
  De-risks: project-finance close, institutional AUM comparable to listed peers
```

The IPO comp-set slide (§10) anchors Phase 3 valuation. Put it in the deck early — it tells the Series A investor what the Phase 3 exit looks like and why the current round is priced correctly relative to the fully-funded vision.

---

## 3. Sector-specific slide arc

| # | Slide | Purpose |
|---|---|---|
| 1 | Cover with tagline | A kWh-anchored claim, not a software claim. "[N]¢ / kWh in a market where the average is [N]¢" is a cover-level number if it holds. |
| 2 | Country energy macro | The single most important context slide. Where is energy cheapest on Earth, and why is this company in that geography? Grid policy, PPA availability, regulatory environment for energy-intensive industry. |
| 3 | Physical asset overview | What the company has built or contracted: MW capacity, PPA terms, physical footprint, current operational status. Photos of the actual facility matter more here than in any other sector. |
| 4 | The business model | Revenue per kWh or per BTC mined or per MW contracted. Not a flow diagram — worked economics at current operating parameters. |
| 5 | Market and macro | Why this moment in the energy-infrastructure cycle. Bitcoin hash rate trajectory (for mining), AI compute demand (for data centers), grid-demand growth (for energy storage). This is the "why now" slide. |
| 6 | Competitive positioning | Energy cost per kWh vs comparable facilities globally. The relevant 2×2 is energy cost × uptime, not product features. |
| 7 | Unit economics at current scale | Revenue per MWh, operating cost per MWh, EBITDA margin, energy cost as % of revenue. If mining: cost per BTC mined vs BTC price at various stress scenarios. |
| 8 | Multi-round capital plan | Phases 1, 2, and 3 with capital required, milestones achieved, and Phase 3 target (IPO / project finance / strategic sale). |
| 9 | Traction | Uptime %, MWh delivered, BTC mined or equivalent output, revenue trend, customer contracts (for data centers / energy services). See playbook §10. |
| 10 | IPO comp-set / public-company comparables | 3–5 publicly listed hard-tech or mining companies with their EV/MW or EV/hash-rate multiples. This is the exit anchor for Series A investors. |
| 11 | Team + advisor stack | Core team (operations + engineering + finance) + advisor stack. For hard-tech companies, the advisor stack is often more impressive than the employee count — show it, but balance it against operational evidence. |
| 12 | The ask + use of funds + milestones | Dollar amount, specific use (MW expansion, PPA acquisition, facility buildout, working capital), milestone cadence. |

Optional appendix: PPA term sheet summary, facility photos and engineering specs, energy macro data by country, hash-rate sensitivity analysis, legal + regulatory structure.

---

## 4. Cover and tagline

Hard-tech cover taglines should lead with the **physical unit that determines economic viability** — for mining, that's kWh cost; for data centers, that's watts per rack or PUE; for renewable energy, that's LCOE (levelized cost of energy).

Five candidates for a Bitcoin mining / energy infrastructure company:

```
1. "Mining at [N]¢ / kWh in a market where viable operations start at [N]¢."
   Sub-tagline: [N] MW contracted. PPA signed. Phase 2 capital opens the scale.
   Test: does a mining-infrastructure investor immediately understand the moat?

2. "The infrastructure play in the lowest-cost energy corridor in South America."
   Sub-tagline: [country] hydroelectric power at [N]¢ / kWh. Series A scaling to [N] EH/s.
   Note: geography-first framing; works with investors who lead with macro thesis.

3. "Bitcoin mining at [N]% of North American average energy cost."
   Sub-tagline: [N] MW operational. PPA through [YEAR]. IPO comp set at [N]x EV/MW.
   Note: comparative framing; immediately positions vs listed peers.

4. "[N] MW. [N]¢ / kWh. [N] TH/s. The infrastructure that runs when the market
   corrects."
   Sub-tagline: Energy contracts structured for the bear market, not just the bull.
   Note: credibility play for investors who've been burned by high-cost operations.

5. "Phase 2: [N] MW → [N] MW. One PPA. One facility. One path to IPO-comparable scale."
   Sub-tagline: [N] MW operational. USD [X]M this round closes the gap.
   Note: milestone framing; works best when Phase 1 is visibly de-risked.
```

**How to choose.** Hard-tech taglines should contain a number — the energy cost or the scale. An energy-infrastructure tagline without a unit cost is as weak as a SaaS tagline without an ARR figure.

---

## 5. Sector framework

```
Underlying model: global energy cost arbitrage as a structural driver of hard-tech location
Our position: [country / region] — [describe the energy source and why it is structurally
  cheap and durable: hydroelectric base load / wind corridor / underutilized grid capacity]
The shift underway:
  - AI compute demand is creating a step-change in energy-intensive infrastructure demand
    globally; data centers, Bitcoin mining, and AI training facilities are competing for
    the same low-cost energy corridors
  - The [country] energy regulatory environment has [improved / stabilized] for
    energy-intensive foreign investment as of [year/policy change]
  - PPA availability in [region] at [N]¢ / kWh is structurally below global average;
    this is a geography-specific moat, not a technology moat
Why this position is durable: [explain why the energy cost advantage is not easily
  arbitraged — grid constraints, PPA term length, regulatory environment, infrastructure
  investment required to replicate]
Why incumbents don't already own this position: [geography / capital / regulatory
  relationships / timing — be specific]
```

**Country energy macro — the mandatory slide.** The most important context in a hard-tech deck is the energy macro for the operating geography. For Paraguay/southern Brazil: Itaipu hydroelectric base load provides below-market energy pricing not available elsewhere in South America without comparable infrastructure. For any geography, include: current grid tariff (USD/MWh), PPA market pricing (range + term availability), energy mix (% renewable), regulatory status for energy-intensive industry, and the sensitivity of the energy cost to grid policy changes.

See playbook §29 for the agent-speed infrastructure cross-reference: AI-native workloads create persistent infrastructure demand that doesn't behave like human-speed traffic — this structural demand shift is the "why now" argument that wasn't available in 2022 but is now.

---

## 6. Cycle / positioning framework

```
Where we are in the infrastructure cycle:
  - Early-institutional: physical assets built or contracted; proof-of-concept phase
    complete; scaling capital required to reach institutional-comparable scale
Where competitors are:
  - Listed mining companies (North American): operating at USD [N]–[N]¢ / kWh;
    institutional-scale but locked into higher-cost geographies
  - Private operators in same geography: [describe competitive dynamic —
    land competition, PPA competition, regulatory competition]
  - Hyperscaler data center expansion: competing for the same energy corridors but
    with longer lead times and larger minimum-scale requirements
Why now (energy and AI macro):
  - BTC mining economics: network hash rate at [N] EH/s, current difficulty at [N],
    post-halving economics require sub-[N]¢/kWh operations to be profitable at
    BTC price of USD [N]; our cost structure is [N]% below this floor
  - AI compute demand: [describe demand shift — inference workloads, model training,
    agentic workloads per playbook §29]
  - Grid policy: [country]'s [regulatory event] creates a window for PPAs at current
    pricing before [anticipated policy change or demand compression]
Why us:
  - PPA signed and in force through [YEAR] at [N]¢ / kWh — not a letter of intent
  - Phase 1 assets operational for [N] months with [N]% uptime — not prospective
  - Local regulatory relationships that took [N] years to build
```

---

## 7. Audit rubric (12 criteria, 1–5 scoring)

| # | Criterion | What 5/5 looks like |
|---|---|---|
| 1 | Cover leads with a physical-unit claim | The tagline contains an energy cost, hash rate, or physical scale number — not a market-size abstraction. |
| 2 | Country energy macro is the second or third slide | The geographic energy-cost advantage is framed before unit economics. Investors who don't understand why this geography is cheap cannot evaluate anything that follows. |
| 3 | PPA terms are disclosed | Energy cost per MWh, PPA duration, counterparty, whether contracted or LOI-stage. A hard-tech deck without PPA specifics is unauditable. |
| 4 | Unit economics at operational scale | Revenue per MWh (or per BTC, per rack), operating cost per MWh, EBITDA margin at current scale and at Phase 2 scale. Not revenue projections alone. |
| 5 | Multi-round capital plan is explicit | Phases 1, 2, and 3 with capital required, milestones, and Phase 3 target. Investors need to see the full path even if they're only funding one phase. |
| 6 | IPO comp-set is current and credible | 3–5 publicly listed peers with EV/MW or EV/hash-rate multiples drawn from recent market data (specify the date). Shows the Series A investor what the Phase 3 valuation looks like. |
| 7 | Advisor stack is balanced against operational evidence | Advisory roles are named alongside operational proof points. An advisor stack heavier than the employee team raises questions about the company's ability to build independently. |
| 8 | Stress scenario analysis is present | What does the unit economic picture look like at BTC USD [N] / energy cost [N]¢ / [relevant stress variable]? Hard-tech investors are evaluating bear-scenario viability, not just bull-scenario upside. |
| 9 | Traction is physical, not projected | MWh delivered, BTC mined, uptime %, customer contracts signed — actual operational data, not pro forma. |
| 10 | Competition framing uses physical-unit comparisons | Competitive positioning is "our energy cost vs theirs" not "our product features vs theirs." |
| 11 | Team has operational hard-tech credibility | At least one founder has either built physical infrastructure at comparable scale or has deep relationships with the energy counterparties that matter. Operators from pure software backgrounds without hard-tech advisors are a flag. |
| 12 | Regulatory and legal structure is addressed | Operating licenses, energy import/export regulations (for cross-border operations), entity structure, and tax treatment of operations in the geography. |

---

## 8. Sector-specific red flags

```
1. PPA economics undisclosed.
   "We have low-cost energy" without naming the cost and the contract term is not
   a moat claim — it's a promise. Any experienced hard-tech investor will ask for the
   PPA in the first diligence meeting. Front-load it in the deck.

2. Advisor stack heavier than the evidence base.
   Multiple named advisors (legal, energy, capital markets, mining tech, strategic)
   with a core team of 3 and no operational history raises the question of who is
   actually building this. Advisors validate; they don't substitute for operational
   capability.

3. Multi-round capital plan presented as a single round.
   "We're raising USD [X]M" with no Phase 2 or Phase 3 framing implies this is the
   only capital needed. Infrastructure investors know that is not true. The absence of
   a multi-round plan reads as either naivety or deliberate concealment.

4. Bull-scenario-only economics.
   A hard-tech deck that only shows unit economics at BTC USD 100K (or full-capacity
   occupancy, or peak grid prices) doesn't pass basic stress testing. Show the economics
   at a realistic bear scenario and explain what makes the company viable in that scenario.

5. IPO comp-set absent or stale.
   Without listed comparable companies and their current trading multiples, investors
   cannot price the Series A. A comp-set with data older than 12 months in a sector
   where Bitcoin price, hash rate, and energy prices all shift is misleading.

6. Energy cost advantage framed as "lowest in the world" without sourcing.
   Superlatives require data. The energy cost claim must be paired with a specific
   number (USD [N]/MWh), a source (PPA contract, grid tariff schedule), and a
   comparison (global average, nearest competing jurisdiction).

7. Regulatory risk unaddressed.
   Cross-border operations (Paraguay/Brazil, El Salvador, Kazakhstan) have specific
   energy-import, currency, and foreign-investment regulations. The deck must address
   whether operating licenses are in place, what the exposure to a regulatory change is,
   and what the company's contingency is.

8. Technology risk dismissed.
   Hard-tech equipment (ASIC miners, cooling infrastructure, power distribution)
   has failure rates, obsolescence curves, and supply-chain risk. A deck that
   presents the equipment as risk-free will be challenged in diligence.
```

---

## 9. Investor objection bank

Hard-tech investors fall into two categories: infrastructure-first (yield + stability + long-horizon) and venture-infrastructure (equity upside in a hard asset that behaves asymmetrically). The objections differ but the underlying scrutiny is the same: are the physical economics real?

**On energy and operations:**

```
1. What's your PPA counterparty's credit rating? What happens if Itaipu [or your
   energy supplier] changes pricing or access conditions mid-term?
2. What's your uptime over the last 12 months? What caused the downtime?
3. What's your all-in operating cost per MWh including cooling, maintenance, and
   infrastructure CAPEX amortization — not just the PPA tariff?
4. What is the replacement cost per MW if your ASICs [or core equipment] reach
   end of life in [N] years?
```

**On the market:**

```
5. BTC price is the single biggest variable in your economics. Walk me through your
   P&L at BTC USD 30K vs USD 60K vs USD 120K.
6. The network hash rate has tripled in the last 24 months. What's your projection
   for the next 24 months and how does that affect your cost per BTC?
7. AI compute demand is real, but the hyperscalers are also moving into the same
   low-cost energy corridors. What happens when [hyperscaler] signs a PPA for
   [N] MW in your geography?
```

**On capital and structure:**

```
8. You're in Phase 2. What conditions trigger Phase 3 capital, and who has
   committed to lead it?
9. What's your exit timeline and who are the realistic acquirers? Strategic sale
   to a mining company or listed infrastructure player? IPO at [N] MW scale?
10. The Phase 3 capital requirement is USD [X]M. Your current team has raised
    USD [X]M to date. What gives you conviction you can raise [N]x the current
    round in the next [N] years?
```

**On team:**

```
11. Your CEO has a software background. Who on the team has built physical
    infrastructure at this scale before?
12. Your advisor stack is impressive on paper. Who actually shows up for
    the hard operational decisions?
```

**On timing:**

```
13. Bitcoin mining is a commodity business at scale. What's your structural
    moat two years from now when every large operator has access to the same
    PPA pricing you have today?
14. Why Paraguay / [geography] specifically, and why this year rather than
    three years ago or three years from now?
```

---

## 10. Comparable raises

Hard-tech comparable raises must include both private rounds (for Series A pricing anchoring) and listed public-company multiples (for Phase 3 exit anchoring). Update at least quarterly.

| Company | Round / listing | Scale | Multiple / price | Notes |
|---|---|---|---|---|
| [Listed Bitcoin mining company A — NASDAQ/TSX-listed] | Public | [N] EH/s / [N] MW | EV/hash-rate: [N]x | Primary IPO comp-set anchor. Use the most recent EV/MW or EV/hash-rate multiple. |
| [Listed Bitcoin mining company B] | Public | [N] EH/s | EV/hash-rate: [N]x | Second IPO comp-set anchor. Range gives the Series A investor a floor and ceiling. |
| [Private infrastructure comparable — recent Series A] | Series A — [Year] | [N] MW | [N]x revenue / [N]x EBITDA | Most recent private-market comparable for this round's pricing. |
| [Data center / AI infrastructure comparable] | [Recent round] | [N] MW | [N]x EBITDA | Cross-sector anchor; shows that energy-intensive compute infrastructure is valued on MW, not on pure software multiples. |

**What the comp-set demonstrates.** Infrastructure companies are valued on physical-unit multiples (EV/MW, EV/hash-rate, EV/kWh-capacity) — not on revenue or ARR multiples. If the current round's implied valuation is disconnected from these multiples, explain why (earlier stage, different risk profile, geography discount / premium). If it's in line, say so explicitly.

---

## 11. Draft slide for the sector-specific moment

The kWh-as-leading-unit slide is the equivalent of the credit-fintech leverage wedge slide: it is the one slide that collapses the entire investment case into a number the investor can hold in their head.

```
Slide title: "The energy math"

Headline: [N]¢ / kWh. In a sector where operations above [N]¢ / kWh are
structurally marginal, we run at [N]% of viable cost.

Body:

| Parameter | Our operations | North American average | Global average |
|---|---|---|---|
| Energy cost | USD [N]/MWh | USD [N]/MWh | USD [N]/MWh |
| All-in mining cost (BTC) | USD [N] | USD [N] | USD [N] |
| Breakeven BTC price | USD [N] | USD [N] | USD [N] |
| EBITDA margin at BTC USD [X] | [N]% | [N]% | [N]% |

Source: [PPA contract for our figures; public filings / Hashrate Index for comparables; date]

Why this is durable: PPA contracted through [YEAR] at fixed USD [N]/MWh.
The counterparty is [Itaipu / grid operator / renewable developer].
[N] MW operational. Phase 2 brings [N] MW on the same contract terms.

The moat is not the technology stack. The moat is [N] years of
energy-procurement relationships that took [N] years to build.
```

---

## 12. Style and voice guidance

- **Lead with units, not abstractions.** "kWh" and "MW" and "TH/s" are the language of this sector. Replacing them with "scalable infrastructure" or "energy solutions" tells investors the founders don't know the sector.
- **Physical before financial.** Describe what the company has built physically before describing the financial model. A photo of the facility before slide 3 signals operational reality.
- **Engineering precision over marketing vagueness.** "Our state-of-the-art facility" means nothing. "[N] MW of S19 Pro ASICs in [N] containers at 95% uptime" means something.
- **Stress-test in the document.** Hard-tech investors will stress-test the model in the meeting. If the deck doesn't pre-answer the bear scenario, the meeting will be dominated by that question.
- **No AI vocabulary.** Avoid: robust, holistic, comprehensive, synergy, impactful, revolutionize. In hard-tech, these words signal a software marketing mindset in a physical-asset business.

**Voice rules specific to hard-tech:**

```
- Never "energy solutions" — name the specific energy source and its cost
- Never "scalable infrastructure" — name the MW capacity and the expansion path
- "kWh," "MW," "TH/s," "EH/s," "ASIC" — use the vocabulary, not the euphemism
- English for international investors; local language for regulatory filings
  and energy-counterparty relationships
- Stress scenarios should use round numbers for readability
  (BTC at $30K, $60K, $100K — not $47,238)
```

---

## 13. What Claude should NOT do

- Claude should **not invent energy pricing, PPA terms, or hash-rate data** the company hasn't provided. These are the foundational facts of the investment case — a placeholder energy cost is worse than a missing slide.
- Claude should **not treat Bitcoin mining as a software business.** The audit criteria for hard-tech are physical and financial (energy cost, uptime, multi-round capital plan, IPO comp-set multiples), not software-sector metrics (ARR, NRR, LTV/CAC in the SaaS sense).
- Claude should **not overlook the regulatory and legal structure questions.** Cross-border energy operations have regulatory exposure that belongs in the deck, not just the data room.
- Claude should **not audit hard-tech decks against software-company criteria.** The playbook's 15-slide canonical arc is a starting point; the hard-tech arc (§3 above) overrides it in sequencing and emphasis.
- Claude should **not dismiss the advisor stack as vanity.** In hard-tech, advisors often provide access to energy counterparties, regulatory networks, and capital-markets channels that the core team doesn't have. The audit should evaluate whether the advisor relationships are operational (do they show up for specific problems?) or decorative (logo-on-the-deck). Both are worth noting.

---

**Authored by Bamboo DCM** ([bamboodcm.com](https://bamboodcm.com)) — the independent infrastructure for Brazil's corporate and structured credit market, with an intelligence layer on top.

Comments, improvements, or questions:

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

License: [CC-BY 4.0](https://github.com/bamboo-DCM/library/blob/main/LICENSE) — free to share and adapt with attribution.

Version 0.1.0-beta · 5 May 2026
