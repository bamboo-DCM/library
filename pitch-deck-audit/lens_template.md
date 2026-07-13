# Pitch deck lens — blank template

**What this file is.** A fillable template for the criteria a pitch deck audit runs against. You fill it once for your company, then point Claude at it every time you want feedback on the deck. The template has 13 sections derived from a real bespoke audit lens; the structure generalizes across sectors.

**How to use it.** Replace every `[YOUR COMPANY]`, `[FILL]`, and `[REPLACE WITH YOUR REALITY]` placeholder with your specifics. Keep the structure. The shape of the document — not the company-specific content — is what makes the audit consistent across iterations.

**This is a living document.** The first version takes 60–90 minutes to fill. The version that wins your round is the one you've edited 10 times — every real investor meeting surfaces an objection you didn't anticipate, and the lens gets sharper when you add it to Section 9.

**See also.** [`playbook.md`](playbook.md) for the methodology behind each section. [`cowork_workflow.md`](cowork_workflow.md) for the iteration loop. [`examples/`](examples/) for filled lenses you can use as a model — pick the one closest to your sector and replace the specifics.

---

## 1. Company identity

Tell Claude who you are. Anything Claude doesn't know from this section, it will guess at — and the guesses will be wrong.

```
Company: [YOUR COMPANY]
Sector: [ONE-PHRASE DESCRIPTION — name the sector + the buyer + the product class in one phrase]
Stage: [bootstrapped / pre-seed / seed / Series A / Series B+]
Geography: [country + region]
Founded: [YEAR]
Headline metrics ([month YEAR]): [3–5 numbers that tell your story today — revenue, customers, growth rate, key cohort]
Team: [N founders, one phrase per role]
Product today: [one sentence]
Roadmap: [3–4 product steps in order, with the logic of the order — not a list]
Vision: [one sentence — where this is going long-term]
```

**The raise:** [one sentence stating amount, instrument, and what the money does]. **Make this sentence land.** A vague raise sentence here means a vague raise slide later; sharpening it once at the lens level forces clarity across every iteration.

---

## 2. Raise framing

This is the section most founders under-invest in and that matters most. **What kind of raise is this — really?**

The default story is "we're raising growth equity." For most companies, that's right. For some, it's wrong, and pitching the default story when the actual structure is different is the single most common reason credit-instrument and structured-product raises miss.

Examples of where the raise framing differs:

- **Equity raise (default).** Investor buys equity, expects exit via acquisition or IPO. Most fundraise decks.
- **Credit-instrument equity wedge.** Investor buys equity that funds the first-loss layer of a debt vehicle (FIDC, ABS facility, sub-quota structure). Returns come from the leverage of senior tranches stacked on top of the equity. Different math, different audience.
- **Regulated structured-product distribution.** Not a raise at all in the venture sense — a product offering to qualified institutional investors under a regulator's marketing rules.
- **Strategic round.** Investor expects commercial integration, not just financial return.
- **Bridge.** Short-runway raise to a milestone before a larger round.

Write 3–5 sentences explaining what kind of raise this is, what the investor's return profile looks like, and what the investor is really buying. If the math is non-trivial (sub/senior ratios, deployable credit per equity dollar, leverage wedge), draft the math here so Claude has it for every audit.

```
[FILL — 3–5 sentences naming the raise type, the investor return profile, and what makes this raise different from a generic growth-equity check (if anything)]
```

If applicable, include a worked-numbers table. The example below is one shape — replace with your own:

| Layer | Amount | Source | Role |
|---|---|---|---|
| `[LAYER 1]` | `[$AMOUNT]` | `[SOURCE]` | `[ROLE]` |
| `[LAYER 2]` | `[$AMOUNT]` | `[SOURCE]` | `[ROLE]` |
| `[DEPLOYABLE]` | `[$TOTAL]` | | |

---

## 3. Sector-specific slide arc

The canonical 15-slide flow (Cover → Problem → Solution → Why now → Market → Product → Traction → Business model → Competition → Team → Financials → Ask → Use of funds → Roadmap → Close) is the right baseline for most equity raises. Some sectors need a different sequence.

**Does your sector require additional or differently-ordered slides?** Examples:

- Credit-instrument raises: capital stack + leverage wedge slide
- Hard-tech / energy: country macro + multi-round capital plan + advisor stack
- Regulated structured-product: disclaimer wall + cronograma + risk factors + eligibility criteria
- M&A teasers: anonymized issuer card + advisor contact (no team, no competition, sub-6 slides)
- Structurer-to-counterparty proposals: process diagram + term sheet + events of default + garantias (no TAM, no team bios at length)

```
Target slide count: [N]
Sector-specific additions: [list any slides beyond the canonical 15 — e.g., "leverage wedge, cohort vintage curves, capital stack diagram"]
Sector-specific removals: [list any canonical slides that don't apply — e.g., "no TAM, no team bios" for a structurer proposal]
Order changes: [if you're moving canonical slides — e.g., "vision moves from slide 19 to slide 2"]
```

---

## 4. Cover and tagline

The cover has one job: make the next slide irresistible. A logo + "Pitch Deck — March 2026" earns nothing.

**The cover should carry a tagline + sub-tagline that does three things in eight words or less:**

1. States who you serve (specific, not "users")
2. Implies what is broken (or what is unique)
3. Earns the right to make the reader turn the page

The "only X for Y" formula works often: clean, memorable, makes a category claim. Sequoia's framing is "not just better, but different" — the cover should claim a category, not a feature.

**Five candidate taglines for `[YOUR COMPANY]`:**

```
1. "[FILL — most natural option]"
   Sub-tagline: [FILL — 8–14 words]
   Test: does it survive being said out loud at a coffee meeting without sounding ridiculous?

2. "[FILL — alternative emphasizing mission]"
   Sub-tagline: [FILL]

3. "[FILL — alternative emphasizing infrastructure / category claim]"
   Sub-tagline: [FILL]

4. "[FILL — Portuguese-first if Brazilian-led round]"
   Sub-tagline: [FILL]

5. "[FILL — proof-led, risky-if-numbers-slip]"
   Sub-tagline: [FILL]
```

**How to choose:** Test each against three filters. (a) Does it earn the page turn? (b) Does it survive being said out loud? (c) Does it still feel right after 30 days of use?

---

## 5. Sector framework

Every sector has an underlying model — a cycle, a macro force, a regulatory schema, a network structure. The investor expects you to articulate what that model is and where you sit inside it.

Generic TAM funnels do not answer the "why this point in this market" question. The sector framework does.

```
Underlying model in our sector: [cycle / macro force / regulatory schema / network structure / supply-chain stage / lifecycle phase]
Our position in it: [FILL — be specific about what slice of the model is yours]
The shift the sector is undergoing: [FILL — what changed in the last 18 months that opens this space]
Why this position is underserved by incumbents: [FILL — be honest about why they don't already do this]
```

**Optional diagram.** If your sector has a natural visual representation (a cycle, a stack, a flow, a 2×N grid showing where each player operates), describe it here. Claude can sketch markdown-renderable versions on request.

```
[ASCII diagram or prose description]
```

---

## 6. Cycle / positioning framework

Closely related to §5 but specifically about timing and competitive position:

```
Where we are in the cycle: [FILL — early / scaling / mature; pre-product-market-fit / post-PMF / pre-scale]
Where competitors are: [FILL — name 3–5 competitors with their cycle position]
Why now (sector-specific, not generic AI-is-hot): [FILL — what changed in your sector in the last 18 months that makes the company necessary or possible now]
Why us (not why-not-them): [FILL — the wedge that's specifically yours]
```

The "why now" answer here gets cross-referenced into Slide 4 (Why Now) of your deck. If you can't write a good "why now" here, you can't write a good "why now" slide later.

---

## 7. Audit rubric (12 criteria, 1–5 scoring)

When Claude runs an audit, it scores your deck against these 12 criteria. **5 = best in class; 3 = passable; 1 = problematic.** The scores are diagnostic — the point is the prioritized fix list, not the score.

The 12 criteria below are a starting point. Customize them to your sector — replace any that don't apply, add sector-specific ones (e.g., default rate cohort discipline for lenders; energy macro for hard-tech).

| # | Criterion | What 5/5 looks like |
|---|---|---|
| 1 | Cover earns the page turn | Tagline + sub-tagline that names segment + wedge in <12 words. Reader can quote it back after one viewing. |
| 2 | First three slides answer "what is this" | By slide 3, an investor who has never heard of `[YOUR COMPANY]` can describe in one sentence what it does, who it serves, and why it's different. |
| 3 | Sector positioning is explicit | A diagram or sentence that shows exactly where in the sector framework `[YOUR COMPANY]` plugs in and why that point is underserved. |
| 4 | Market is anchored, not generic | TAM funnel ends in a number that matches `[YOUR COMPANY]`'s actual addressable customer base, not a wallpaper figure. |
| 5 | Competitive positioning is comparative, not declarative | A 2×2 or matrix that places `[YOUR COMPANY]` next to real competitors and is honest about what each does well. |
| 6 | Unit economics are present and credible | Per-customer (or per-loan / per-transaction): gross yield, cost, margin, NIM. Not a flow diagram. |
| 7 | `[SECTOR-SPECIFIC CRITERION — e.g., capital stack visible]` | `[FILL]` |
| 8 | Traction is shown in cohorts, not headlines | `[FILL — sector-specific anchor: vintage curves for lenders, MoM cohorts for SaaS, etc.]` |
| 9 | GTM is explicit and quantified | How customers find `[YOUR COMPANY]` today, channel-level CAC, conversion rates, the path from current scale to next milestone. |
| 10 | Team slide carries the wedge each founder represents | One sentence per founder that connects their background to a specific moat or capability. |
| 11 | The ask is matched to the instrument | The raise amount is broken down with the instrument math made explicit. The reader knows what 12 months of progress looks like and what the next round looks like. |
| 12 | No filler slides | Every slide earns its place. Vision is up front. No mid-deck "where are we" interludes. |

When Claude returns audit results, it should also flag the **top 3 highest-impact fixes** — not the three lowest scores, but the three changes that would move the deck the most for the smallest amount of work.

---

## 8. Sector-specific red flags

Generic deck red flags (vanity metrics, top-down TAM, undifferentiated team bios) apply to every deck. **Sector-specific red flags are the ones a generalist auditor would miss.**

5–10 patterns Claude should explicitly check for and call out when present:

```
1. [FILL — sector-specific red flag #1, with what it looks like and why it's a problem]
2. [FILL]
3. [FILL]
4. [FILL]
5. [FILL]
[Add as many as your sector needs — start at 5, grow toward 10 over iterations]
```

Examples by sector to anchor against:

- **Credit-fintech:** headline default rate without cohort curves; LTV/CAC presented like SaaS; capital stack omitted; market sized in dollars not customers
- **Hard-tech / energy:** PPA economics undisclosed; advisor stack heavier than evidence base; multi-round capital plan presented as one round
- **Regulated structured-product:** missing risk-factor section; cronograma not aligned to legal calendar; eligibility criteria buried
- **M&A teaser:** issuer-identifying details leak through; advisor contact buried; sub-6-slide promise broken
- **Structurer-to-counterparty:** TAM included where there shouldn't be one; team bios where there shouldn't be team

---

## 9. Investor objection bank

When Claude red-teams your deck, it plays a hostile investor and asks the hardest version of these questions. **This is the section that compounds.** Add to it after every real investor meeting that surfaces a question you didn't anticipate.

The starter list below is sector-agnostic. Add 10–20 sector-specific objections in the first sitting; grow from there.

**On the business:**

```
1. [FILL — the question a hostile investor asks first]
2. [FILL]
3. [FILL]
```

**On unit economics:**

```
4. [FILL]
5. [FILL]
```

**On capital structure (if applicable):**

```
6. [FILL]
7. [FILL]
```

**On GTM and growth:**

```
8. [FILL]
9. [FILL]
```

**On team:**

```
10. [FILL]
```

**On market and timing:**

```
11. Why now? What changed in the last 36 months that makes [YOUR COMPANY] possible today and impossible three years ago?
12. [FILL — sector-specific timing question]
```

**On the exit:**

```
13. What's a realistic exit for [YOUR COMPANY]? Strategic acquisition by which acquirer? IPO? Continuation as an independent?
14. What's the comparable transaction you'd point to as the model?
```

---

## 10. Comparable raises

Anchor your positioning against 3–5 sector-comparable raises. Update at least once a month — comparable raises are a moving target.

| Company | Latest raise | Stage | Lead | Notes |
|---|---|---|---|---|
| `[NAME]` | `[$AMOUNT, DATE]` | `[STAGE]` | `[LEAD]` | `[1–2 sentences on what they pitched and what they got]` |
| `[NAME]` | `[$AMOUNT, DATE]` | `[STAGE]` | `[LEAD]` | `[1–2 sentences]` |
| `[NAME]` | `[$AMOUNT, DATE]` | `[STAGE]` | `[LEAD]` | `[1–2 sentences]` |

**What `[YOUR COMPANY]` can learn from each:**

```
- From [NAME]: [FILL — the framing that worked, and why]
- From [NAME]: [FILL]
- From [NAME]: [FILL]
```

**What `[YOUR COMPANY]` should *not* do:** position as "the next `[NAME]`" or "the better `[NAME]`." The investor's question is *why does this market need a fourth player*, and the answer has to be about your specific wedge — not about being a clone with better tech.

---

## 11. Draft slide for the sector-specific moment

Most decks have one slide that the canonical 15-slide flow doesn't include and that, once added, makes the rest of the deck snap into place. Examples:

- Credit-instrument raises: the **leverage wedge slide** (equity → sub quota → senior quota → deployable credit, with worked numbers)
- Hard-tech: the **kWh-as-leading-unit slide** (physical asset specifics + country macro)
- Regulated structured-product: the **three-pillar arc slide** (asset class / manager / timing)
- M&A teasers: the **anonymized issuer card** (sector + scale + one differentiator, no name)
- Structurer-to-counterparty: the **process diagram + term sheet** slide

Draft your sector-specific slide here. The deck draft inherits this content; the lens version is the source of truth.

```
Slide title: [FILL]
Headline (one sentence): [FILL]
Body: [FILL — the slide content, in markdown]
```

---

## 12. Style and voice guidance

When Claude rewrites slides or generates new copy, apply these:

- **Short sentences. Active voice.** No more than 15 words per slide bullet.
- **Numbers over adjectives.** Replace "rapid growth" with "4.4×." Replace "low default" with "sub-2% lifetime loss across three vintage cohorts."
- **Specific over generic.** Name the addressable customer count and the geography in one phrase — abstract numbers ("a large opportunity") read as filler.
- **Match the language to the audience.** English for international investors; Portuguese (or the local language) for local institutional investors. The deck should be available in both. If the round is led locally, lead with the local language.
- **No AI vocabulary.** Avoid: leverage, robust, comprehensive, holistic, synergy, actionable, impactful, cutting-edge, best-in-class, paradigm, revolutionize. Use plain words.
- **No filler.** Every slide should pass the test: *if I deleted this slide, would the deck be worse?* If the answer is no, delete it.

**Voice rules specific to `[YOUR COMPANY]`:**

```
- [FILL — phrases you always want Claude to avoid]
- [FILL — phrases or terminology you specifically use]
- [FILL — register: founder-voice / institutional / regulated]
- [FILL — language priority: English-first / Portuguese-first / bilingual parity]
```

---

## 13. What Claude should NOT do

Final guardrails so Claude doesn't drift outside the lens:

- Claude should **not invent numbers** `[YOUR COMPANY]` hasn't shared. If a slide needs a number Claude doesn't know, leave a `[REPLACE WITH YOUR REALITY]` placeholder.
- Claude should **not pretend to know regulatory specifics** it isn't sure of. For sector-specific regulatory rules (CVM 161, Resolution 4,656, FIDC structure rules, ABS securities-act exemptions, etc.), answer with explicit uncertainty and recommend verification with counsel.
- Claude should **not optimize for what sounds clever**. Optimize for what an investor actually wants to know.
- Claude should **not give 12 pieces of feedback when 3 would do**. The point of the rubric is prioritization, not exhaustiveness.
- `[FILL — additional guardrails specific to YOUR COMPANY: e.g., "Don't reference Competitor X by name unless I've explicitly asked"; "Don't suggest English-language taglines until the Portuguese ones are settled"; "Don't speculate on the regulatory wrapper"]`

---

**End of lens.** Save this file, drop it into your Claude project (or load it via the `/pitch-deck-audit` skill), and run your first audit. See [`cowork_workflow.md`](cowork_workflow.md) for the iteration loop and [`playbook.md`](playbook.md) for the methodology behind each section.

---

**Authored by Bamboo DCM** ([bamboodcm.com](https://bamboodcm.com)) — the independent infrastructure for Brazil's corporate and structured credit market, with an intelligence layer on top.

Comments, improvements, or questions:

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

License: [CC-BY 4.0](https://github.com/bamboo-DCM/library/blob/main/LICENSE) — free to share and adapt with attribution.

Version 0.1.0-beta · 5 May 2026
