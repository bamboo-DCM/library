# Pitch deck lens — regulated structured-product marketing

**What this file is.** A filled sector lens for a regulated structured-product marketing document — specifically the type used by Brazilian asset managers distributing regulated investment vehicles (FIDCs, Fiagros, CRIs, CRAs, FIIs) to qualified institutional investors under CVM Instrução 160 (CVM 160). The conventions of this artifact class are radically different from a fundraise deck. This is not a pitch to investors who need to be convinced the category is real; it is a regulated marketing document to institutional allocators who already understand the asset class and are evaluating whether this specific offering, from this specific manager, at this specific moment, deserves allocation.

**Source.** Structurally abstracted from Vinci Crédito Portfólio CDI+ FIDC (Vinci Partners, public CVM 160 marketing material). The three-pillar arc, mandatory disclaimer wall, cronograma format, risk-factor structure, and distribution syndicate conventions are drawn from that publicly-distributed material. Cited here with attribution per fair use of public regulated marketing material.

**How to use this file.** Sections 1–3 cover what this artifact is and how its arc differs from a fundraise deck. Section 7 (rubric) covers both content quality and CVM 160 compliance checkpoints. Section 8 (red flags) covers the compliance failures that get material pulled before distribution. Read §§1–3 before any audit run.

**This is a living document.** The cronograma and offering details require updating each time the fund opens a new window or issues a new series. CVM 160 disclaimer language must be reviewed with counsel each time the regulatory environment updates.

**See also.** [`playbook.md`](../playbook.md) §§1, 3, 10, 17 for methodology context. For the fundraise deck conventions that this artifact explicitly rejects, read [`playbook.md`](../playbook.md) §§2–15. [`lens_template.md`](../lens_template.md) for the blank schema.

---

## 1. Company identity

```
Fund / product: [FUND NAME] — [ASSET CLASS, e.g., FIDC / Fiagro / FII]
Manager: [ASSET MANAGER NAME]
Strategy: [one-sentence description of the credit strategy —
  e.g., "multi-originator credit receivables, CDI+ target return, CVM-rated senior cotas"]
Target return: CDI + [N]% a.a. (or fixed rate + spread, depending on structure)
Target AUM: R$[X]M (current round) / R$[X]M (total program)
Investor eligibility: qualified investors (investidores qualificados) as defined by
  CVM Resolução 30, minimum ticket R$[X]
Regulatory wrapper: CVM 160 regulated marketing material
Series: [Série N, ISIN: BRXXXXX]
Distribution: [N] qualified distributors listed (see §3 for arc)
Management team: [N] professionals; [describe portfolio management team briefly
  — seniority, relevant track record]
Key metrics (fund):
  - Track record: [N years / N series of prior issuances]
  - Volume managed: R$[X]M across [N] prior series
  - Investor base: [N] institutional allocators
  - Default history: [X]% portfolio-level loss across [N] series / zero credit events on prior series
  - Rating: [if rated — agency + rating level]
```

**What this is not.** This is not a venture capital raise. This is not a pitch to convert a skeptic. Qualified institutional investors receiving this material already know what an FIDC is. The job of the marketing material is to answer three questions: (1) is this asset class worth allocating to right now? (2) is this manager trustworthy with a mandate in this asset class? (3) does the timing of this offering match the portfolio construction context? See the three-pillar arc in §3.

---

## 2. Raise framing

Unlike a fundraise deck, a regulated structured-product marketing document is not pitching a round that the manager needs to close by a certain date in order to survive. The framing is therefore fundamentally different:

**The offer framing.** This is an offer of an investment vehicle to qualified institutional investors under CVM 160. The manager is the intermediary between the investor's capital and the underlying credit exposure — not the founder asking for growth equity. The investor is evaluating credit risk, manager risk, structure risk, and timing, in that order.

**Return profile.** Target return of CDI + [N]% a.a., with [description of senior/subordinated structure if applicable]. Distribution: [monthly / quarterly]. Liquidity window: [N months / maturity date]. Tax treatment: [exempt / [N]% IR on gains].

**The capital stack (if multi-tranche).**

| Tranche | Amount | Target return | Rating | Priority |
|---|---|---|---|---|
| Senior cotas | R$[X]M | CDI + [N]% | [Agency, rating] | First payment |
| Mezanino (if applicable) | R$[X]M | CDI + [N]% | — | Second |
| Subordinated cotas (originator) | R$[X]M | Equity-like upside | — | Last |

**Why this offering, now.** The "why now" for a regulated structured product is a market-conditions argument, not a team narrative: credit spreads at current levels, the specific regulatory window this series qualifies under, the pipeline of receivables already committed at formation. See §6.

---

## 3. Sector-specific slide arc

Regulated CVM 160 marketing material follows a different structure from any fundraise deck. The arc has three mandatory structural sections plus two mandatory compliance sections. Total length: 40–60 pages for a full offering document (not slides — pages, or "lâminas").

| Section | Content | Notes |
|---|---|---|
| **Disclaimer wall (mandatory)** | CVM 160 required language: "This is not a public offering"; qualified-investor eligibility statement; past-performance disclaimer; risk disclosure header; contact for prospectus; ANBIMA code of conduct declaration | 3–6 pages. Required by regulation. Must appear before any fund information. |
| **Manager credentials** | Manager AUM, strategy history, team tenure, regulatory standing, ANBIMA classification | This is the "team" section equivalent. Institutional allocators need to know the manager before the product. |
| **Three-pillar arc** | Pillar 1: the asset class (why credit receivables / agricultural credit / real-estate receivables deserve allocation in the current cycle); Pillar 2: the manager (why this manager has a structural edge in originating, structuring, and surveilling this asset class); Pillar 3: the timing (why this series, at this moment, offers a better risk-adjusted return than the alternatives) | This is the core analytical argument. Each pillar answers one of the three allocator questions. |
| **Product specifics** | Series name, ISIN, target AUM, target return, distribution frequency, liquidity terms, minimum ticket, tax treatment, subscription periods | The term sheet equivalent. Must be fully populated; no placeholders. |
| **Cronograma** | Subscription window, credit analysis window, allocation window, first distribution date, maturity or next liquidity event, key dates in the operational calendar | Brazilian institutional allocators have portfolio construction cadences; the cronograma must align with Q-end or month-end cycles. |
| **Eligibility criteria** | Who can invest: investidores qualificados per CVM Resolução 30 (minimum R$1M financial assets); investment restrictions if any (e.g., concentrated-portfolio exclusion for some pension funds); know-your-customer requirements | Missing eligibility criteria is a distribution-blocking compliance failure. |
| **Risk factors** | Mandatory list: credit risk, concentration risk, liquidity risk, regulatory risk, operational risk, manager risk. Each with a description of the risk and the mitigation in the structure | CVM 160 material must enumerate risks. Omitting any category is a compliance failure, not a stylistic choice. |
| **Portfolio and strategy detail** | For an active-management vehicle: originator selection criteria, maximum concentration per originator, minimum credit criteria, surveillance cadence, default resolution mechanics | Institutional allocators will ask these questions in diligence; the document must anticipate them. |
| **Distribution syndicate** | List of qualified distributors authorized to sell this product to end investors; contact persons and cutoff dates per distributor | |
| **Regulatory compliance block** | ANBIMA code reference, CVM authorization number, registration date, prospectus availability statement, complaints channel | Must appear on every page footer in most CVM 160-registered materials. |

---

## 4. Cover and tagline

The cover of a CVM 160 regulated marketing document is constrained by ANBIMA style rules and CVM disclosure requirements. The format is institutional, not persuasive.

**Typical cover structure:**

```
[MANAGER LOGO]

[FUND NAME]
[Fundo de Investimento em Direitos Creditórios / Fiagro / FII — full legal name]

Material destinado a investidores qualificados, conforme definição da
Resolução CVM nº 30.

Versão [N] · [Month YEAR]

Este material foi elaborado em conformidade com o Código ANBIMA de Regulação e
Melhores Práticas para Administração de Recursos de Terceiros.
```

**Notes.** There is no marketing tagline on the cover of a CVM 160 document — the cover is a compliance artifact. The persuasive work is done in the three-pillar arc (§3), not on the cover. A cover that leads with a slogan rather than the full legal fund name and mandatory eligibility statement will not pass ANBIMA review.

**The equivalent of a tagline** is the one-sentence strategy description that appears on the "fundos em destaque" distribution lists: "[FUND NAME] — [asset class] — CDI + [N]% target — qualified investors." This must be accurate, precise, and ANBIMA-compliant.

---

## 5. Sector framework

```
Underlying model: Brazilian private credit market — the gap between what regulated
  bank credit covers and what institutional-quality borrowers actually need
Our position: [e.g., multi-originator FIDC focused on agricultural receivables /
  corporate credit receivables / real-estate receivables — fill per your fund]
The structural gap: the Brazilian private credit market is structurally underdeveloped
  relative to capital markets depth; spreads to CDI remain attractive because
  the institutional infrastructure for originating and surveilling credit at scale
  is not widely distributed
The shift underway: Fiagro and FIDC regulatory reforms (post-2021) opened new
  structures; institutional investor appetite for private credit alternatives to
  CDI-only fixed income has increased as CDI normalizes to lower levels over
  multi-year horizon; ANBIMA infrastructure improvements reduce operational friction
  for smaller distributors
Why this position: [manager-specific — the origination edge, the surveillance
  infrastructure, the originator relationships that are not replicable at entry]
```

**What CVM 160 requires here.** The "asset class education" section (the first pillar) must explain why this asset class exists, what its return-risk profile is relative to comparable instruments, and where it fits in a QI institutional portfolio. Write for an investment committee that includes at least one member who is skeptical of the asset class — not for one that already believes.

---

## 6. Cycle / positioning framework

```
Where we are in the private credit cycle: [describe current spread environment,
  CDI trajectory, historical allocation by institutional investors to FIDC/Fiagro]
Where competitors are: [list comparable vehicles in the same asset class — by
  AUM, target return, originator concentration, distribution track record]
Why now (market-conditions argument, not team narrative):
  - Credit spreads to CDI are currently [X]% above their 5-year historical average
    in this asset class, offering better risk-adjusted returns than [comparable
    instruments]
  - The [specific regulatory event or market condition] creates a window before
    [expected compression or structural change]
  - The originator pipeline committed at formation reduces vintage-concentration
    risk for first-call subscribers
Why this manager: [the operational edge — surveillance infrastructure, originator
  relationships, workout track record, credit-committee composition]
```

The "why now" in a regulated-product document is a **market-conditions argument**, not a "why this company" narrative. Institutional allocators evaluate timing relative to the credit cycle, not relative to the manager's funding needs. The cronograma (§3) must be consistent with the "why now" argument — if the offering window doesn't align with a credible market-conditions case, allocators will wait for the next series.

---

## 7. Audit rubric (12 criteria, 1–5 scoring)

| # | Criterion | What 5/5 looks like |
|---|---|---|
| 1 | Disclaimer wall is complete and first | CVM 160 mandatory language appears before any fund information. ANBIMA code reference, QI eligibility statement, past-performance disclaimer — all present in correct order. |
| 2 | Three-pillar arc is explicit | Distinct sections for (1) asset class case, (2) manager credentials, and (3) timing/opportunity. An allocator reading only the section headers can follow the argument. |
| 3 | Manager credentials are specific, not generic | Track record in this specific asset class (not AUM-under-management alone): number of series, volume, default history, workout outcomes. |
| 4 | Risk factors are enumerated, not summarized | Each risk category (credit, concentration, liquidity, regulatory, operational, manager) has its own paragraph with a mitigation mechanism named. No "risks exist" summaries. |
| 5 | Cronograma aligns with distribution calendar | Subscription window, credit-analysis window, allocation, first distribution, and liquidity events are all populated with specific dates that align with Q-end and month-end cycles. |
| 6 | Eligibility criteria are complete | CVM Resolução 30 QI definition, minimum ticket, and any fund-specific investment restrictions are stated. No ambiguity about who can subscribe. |
| 7 | Product specifics are fully populated | Target return, distribution frequency, liquidity terms, minimum ticket, tax treatment, ISIN — none can be placeholder. |
| 8 | Target return is defensible | The CDI + [N]% target is backed by the originator pipeline yield, cost of structure, and historical NIM on comparable series. An allocator asking "where does this number come from" gets an answer in the document. |
| 9 | Distribution syndicate is listed | All authorized distributors named with contact persons. Allocators routed to the correct channel. |
| 10 | Regulatory compliance block is on every page footer | Fund name, CVM authorization, ANBIMA code, "past performance is not a guarantee of future results" — per CVM 160 and ANBIMA requirements. |
| 11 | Portfolio strategy is specific enough to diligence | For active management: originator selection criteria, maximum concentration per originator, minimum credit criteria, surveillance cadence, default resolution. |
| 12 | Version and date are current | No prior-version dates visible. No series-specific data from a previous window still in the document. |

---

## 8. Sector-specific red flags

```
1. Missing or incomplete disclaimer wall.
   Any CVM 160 marketing material distributed without the mandatory qualified-investor
   eligibility statement and past-performance disclaimer is non-compliant. ANBIMA
   members distributing the material are also in violation. This is a pull-the-document
   failure, not a stylistic flag.

2. Target return without backing math.
   CDI + [N]% stated without a worked example of how the originator pipeline yield,
   structural costs, and NIM produce that number. Institutional investment committees
   will reverse-engineer this in diligence; the document should survive the calculation.

3. Cronograma not aligned to institutional calendar.
   A subscription window that ends on a random mid-month date, or a first distribution
   that doesn't align with month-end, signals operational immaturity to institutional
   allocators who are managing month-end portfolio construction.

4. Eligibility criteria buried or incomplete.
   Many pension funds and insurers have internal allocation restrictions (maximum
   concentration in a single issuer or asset class, minimum credit rating for non-
   sovereign instruments). The eligibility section must be complete enough for a
   compliance officer at the allocator to sign off without calling the distributor.

5. Three-pillar arc absent or collapsed.
   A document that jumps from cover to product specifics without the asset-class
   education and manager-credentials sections has not answered the two prior questions
   the allocator is asking before they read the term sheet.

6. Risk factors listed without mitigations.
   "Credit risk exists" is not a risk factor disclosure. Each risk requires a paragraph
   describing the specific exposure in this structure and the mechanism (collateral,
   concentration limits, originator covenant, manager surveillance) that mitigates it.

7. Past performance presented as guarantee.
   Any framing that implies prior series' performance predicts future series' performance
   is a CVM 160 violation. Prior track record may be presented for informational purposes
   only, with the mandated disclaimer.

8. Series-specific details from prior windows still in the document.
   Prior-vintage ISIN, prior cronograma dates, or prior AUM targets remaining in an
   updated offering document undermine credibility and may constitute misrepresentation.

9. Comparable fund analysis absent.
   Institutional allocators are comparing this offering against three or four alternatives
   in their pipeline at the same time. A document that does not address "why this fund
   vs [comparable FIDC]" forces the allocator to do the comparison themselves — and they
   will do it less favorably to the fund.
```

---

## 9. Investor objection bank

Qualified institutional investors in CVM 160 material are primarily portfolio managers, treasurers, and investment committees at pension funds, insurance companies, and family offices. Their objections are analytical, not emotional.

**On the asset class:**

```
1. Our ALM doesn't allow illiquid exposure above [N]% of AUM. Where does this vehicle sit
   on the liquidity spectrum and how does the cronograma interact with our reporting calendar?
2. This is a private credit vehicle. How does your originator-selection process ensure we're
   not taking concentrated exposure to a sector already overrepresented in our book?
3. CDI + [N]% sounds attractive today. What does the return look like in a stress scenario
   where CDI rises 200bps and the originator's borrowers refinance elsewhere?
```

**On the manager:**

```
4. Your track record across [N] series is [N years]. What is the worst single-series outcome
   you've had and how did you manage the workout?
5. What's the turnover in your portfolio management team over the last three years? Who
   is personally responsible for credit decisions on this vehicle?
6. You manage R$[X]B in similar strategies. Is this vehicle competing for the same
   originator relationships as your flagship fund?
```

**On structure:**

```
7. What's your maximum single-originator concentration and what covenant triggers a forced
   reduction?
8. If the senior cotas go to 90%+ of NAV (stress scenario), what is your playbook?
   Who calls it, how fast, and what happens to the subordinated quota holders?
9. What's the legal opinion on the enforceability of your receivables? Which counsel
   and what's the structure?
```

**On timing and allocation:**

```
10. We already have [N]% in private credit. What's the portfolio construction case for
    adding another [N]% in this vehicle versus extending duration in our existing
    private credit book?
11. The subscription window closes [date]. We have an investment committee meeting
    [date]. Can we get the full prospectus and legal opinion five business days before
    the committee date?
```

---

## 10. Comparable raises

For a regulated structured product, "comparable raises" means prior series of the same fund or comparable vehicles from competing managers. Update quarterly — the private credit market moves faster than most founders realize.

| Fund | Series / vintage | Target return | AUM | Notes |
|---|---|---|---|---|
| **Vinci Crédito Portfólio CDI+ FIDC** (Vinci Partners, public CVM 160 material) | Multiple series | CDI+ | Disclosed in offering material | Three-pillar arc model. Asset class / manager / timing structure is the clearest public example of the form. |
| [Comparable FIDC from competing manager] | [Series, year] | CDI + [N]% | R$[X]M | [One sentence on what differentiated their offering] |
| [Prior series of this fund] | [Series N-1] | CDI + [N]% | R$[X]M target / R$[X]M raised | [Track record summary — return delivered vs target, credit events if any] |

**What to take from Vinci's structure.** The three-pillar arc (asset class → manager → timing) is the load-bearing structure of any well-authored regulated marketing document. Each pillar has a distinct job and a distinct audience: the asset class section converts a generalist allocator; the manager section converts a specialist; the timing section converts a decision-ready allocator who needs a reason to subscribe now rather than next quarter.

---

## 11. Draft slide for the sector-specific moment

The three-pillar arc summary is the slide that collapses the investment case into one page for an investment committee presentation. This is the equivalent of the fundraise deck's cover tagline: a single artifact that earns the reader's investment of 40 more pages.

```
Slide title: "[FUND NAME] — investment case in three sentences"

Sentence 1 (asset class):
"Brazilian private credit receivables continue to offer CDI + [N]–[N]% risk-adjusted
returns as institutional infrastructure deepens and bank credit remains structurally
rationed for mid-market originators."

Sentence 2 (manager):
"[MANAGER NAME] has originated and surveilled R$[X]B in [asset class] across [N]
series with [zero credit events / sub-[N]% loss rate], giving this vehicle a
surveillance infrastructure that a first-time issuer cannot replicate."

Sentence 3 (timing):
"This series opens a [N]-month subscription window with [N] originators pre-committed,
targeting first distribution on [DATE] — aligned with institutional Q[N] portfolio
construction cycles."

Supporting table:
| | This series | Prior series average |
|---|---|---|
| Target return | CDI + [N]% | CDI + [N]% |
| Realized return (prior series) | — | CDI + [N]% (range: CDI+[N]% to CDI+[N]%) |
| Loss rate | — | [N]% |
| AUM | R$[X]M target | R$[X]M avg. |
```

---

## 12. Style and voice guidance

- **Institutional, not persuasive.** CVM 160 marketing material is not allowed to be persuasive in the sense a startup pitch deck is. The register is: factual, precise, disclosure-complete.
- **Numbers over narratives.** Every return claim, concentration limit, and credit criterion must be a number, not a description.
- **Bilingual.** Brazilian institutional allocators work in Portuguese; international co-investors may need English. If distributing to both audiences, produce parallel versions rather than a mixed-language document. ANBIMA review is in Portuguese.
- **No superlatives.** "Best," "leading," "largest" require substantiation in a CVM 160 document. If you can't cite the source and date for the claim, drop it.
- **No AI vocabulary.** Avoid: robust, comprehensive, holistic, synergy, paradigm, impactful. In a regulated document, these words flag a marketing overlay on what should be a disclosure document.
- **ANBIMA vocabulary.** Preferred terms: "veículo de investimento regulado," "cotas seniores," "cotas subordinadas," "cedente," "cedido," "direitos creditórios," "patente de originação" — use the vocabulary an ANBIMA compliance reviewer expects to find.

**Voice rules specific to regulated structured product:**

```
- Never "raise" — the correct term is "oferta" or "captação"
- "Investidores qualificados" per CVM Resolução 30 — never "accredited investors" (US term)
- Always include the ANBIMA disclaimer block in every version; it is not optional
- If a comparable is named, include the source and date ("per Relatório de Gestão,
  [MANAGER], [DATE]") — unsourced competitive comparisons are a CVM 160 violation
- Regulatory regime citations: CVM Resolução 175 (FIDCs post-2023),
  Lei 14,130/2021 (Fiagro), CVM 160 (marketing material) — cite by current number
```

---

## 13. What Claude should NOT do

- Claude should **not generate CVM 160 disclaimer language** from memory. Mandatory regulatory text changes with regulatory updates. Always copy from the current ANBIMA template and have it reviewed by compliance counsel before distribution.
- Claude should **not invent fund metrics** — AUM, return history, loss rates, or ISIN — that haven't been provided. Placeholder fund metrics in a CVM 160 document are a compliance risk if the document circulates before they are replaced with actual data.
- Claude should **not optimize for persuasiveness at the expense of disclosure completeness.** A regulated marketing document that omits a required risk factor to keep the reader's attention is non-compliant. Completeness takes priority over narrative flow.
- Claude should **not give feedback using fundraise-deck criteria.** A regulated product document has no "problem slide," no "why now" in the startup sense, no team bios in the founder sense. Audit it against the rubric in §7, not against playbook §§2–15.
- Claude should **not compare this offering to equity raises** in its suggestions. The audience, the instrument, and the disclosure regime are all different. The benchmark is "what does a best-practice CVM 160 offering document from a first-tier Brazilian asset manager look like" — not "what would a16z want to see."

---

**Authored by Bamboo DCM** ([bamboodcm.com](https://bamboodcm.com)) — an AI-native private credit infrastructure platform in São Paulo, Brazil.

Comments, improvements, or questions:

- **Arthur O'Keefe** — [arthur@bamboodcm.com](mailto:arthur@bamboodcm.com)
- **Felipe Grassi de Moraes** — [felipe@bamboodcm.com](mailto:felipe@bamboodcm.com)
- **Urian Inhauser** — [urian@bamboodcm.com](mailto:urian@bamboodcm.com)

License: [CC-BY 4.0](https://github.com/bamboo-DCM/library/blob/main/LICENSE) — free to share and adapt with attribution.

Version 0.1.0-beta · 5 May 2026
