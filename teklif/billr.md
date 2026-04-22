# Billr — Go-to-Market Strategy Document

**Prepared:** April 2026
**Version:** v1 (draft for review)
**Scope:** Outbound lead generation + hypothesis-testing framework for early-stage ICP, offer, and positioning discovery
**Client:** Billr (billr.io)
**Service provider:** Tibexa

---

## 1. Executive Summary

Billr is a Vienna-based, 2024-founded startup building a **custom billing infrastructure platform** for companies whose pricing models don't fit off-the-shelf tools (Chargebee, Stripe Billing, Zuora). Two live references — **Quivo** (€50M European 3PL, 800+ customers) and **Ecomflow** (China-direct 3PL, 150+ brands, 25K+ daily shipments) — both land in the same vertical: **third-party logistics**. This is a strong signal, not yet a confirmed niche.

At this stage, Billr faces three open questions that any early-stage B2B infrastructure company must answer before scaling spend:

1. **ICP clarity** — Is 3PL the wedge, or a coincidence? What sub-segment of 3PL (European mid-market, Asia-Pacific D2C fulfillment, freight forwarders, warehouse SaaS verticals)?
2. **Offer clarity** — Is the pitch "custom billing infrastructure" (platform positioning), "replace your billing engineer" (cost-out), or "unlock pricing you can't bill today" (revenue-enabling)?
3. **Channel clarity** — Does cold outbound produce conversations with CFOs, Heads of Finance, or CTOs in 3PL / usage-based SaaS? At what response rate?

Rather than commit to a single ICP and message up front, **Tibexa proposes a 4-month sprint designed as a market experiment**. The sprint simultaneously generates pipeline and produces the data Billr needs to pick its wedge with evidence. Setup takes one month; the next three months exhaust the addressable market across up to three parallel ICP hypotheses.

We work with three layers of market sizing, deliberately:

- **TAM (Total Addressable Market):** the full universe of companies that *could* need custom billing infrastructure — **~430,000+ accounts globally** across the three hypotheses, with 3PL alone accounting for ~340,000 firms (IBISWorld / Speed Commerce 2024)
- **SAM (Serviceable Addressable Market):** the subset filtered by signals of acute pain and buying readiness (pricing complexity, tech maturity, billing-function hiring, growth signals) — **~35,000–45,000 accounts**
- **SOM (Serviceable Obtainable Market):** what we can realistically touch in a 3-month active sprint — scales with the package selected (see Section 8)

Because Billr is pre-wedge, **the real job of this sprint is to convert TAM into a defensible SAM** — to find the sub-segment of the universe where the pitch actually lands, then go back for depth. Outbound is the fastest, cheapest instrument to do this.

**A note on strategic focus, before the hypothesis section:** Tibexa's own recommendation is to treat **logistics as the primary vertical** and concentrate here. Section 2.4 explains why. The multi-hypothesis design is a concession to the founder's preference to test breadth — but the sprint is structured so that if logistics confirms its pull (as we expect), the remaining budget compounds there rather than fragmenting across verticals.

**Sprint funnel at 0.35% positive-reply baseline, scaled by package volume (3 active outreach months):**
- **Small — Discovery** (10,000 sends/month → 30,000 sends total, ~20,000 accounts): 105 positive replies → 50–70 meetings → 10–17 closed deals
- **Medium — Validation** (25,000 sends/month → 75,000 sends total, ~50,000 accounts): 262 positive replies → 125–175 meetings → 25–44 closed deals
- **Large — Market Sweep** (50,000 sends/month → 150,000 sends total, ~100,000 accounts): 525 positive replies → 250–350 meetings → 50–88 closed deals

**Timing note:** Custom billing infrastructure has a 3–6 month sales cycle (see Section 8.2.1). Most closed deals from a sprint land in months 5–10 after sprint start, not during the sprint itself. The sprint's month-4 deliverable is the **ICP evidence + pipeline in flight**; closed-won ARR materializes across the following two quarters.

At ARR of $10K per customer and a 3-year LTV of ~$27K per customer, even the Small package can return multiples of its own cost if conservative assumptions hold. The deeper value is the ICP evidence and objection dataset the sprint produces in month 4, well before most deals close.

---

## 2. Strategic Context — Why This Sprint Is Designed as an Experiment

### 2.1 The early-stage reality

Billr has 2 customers, both 3PLs, both sourced via network / founder-led sales. At this stage:

- **Conviction is higher than evidence.** Two references in the same vertical is suggestive but not conclusive. It could be a genuine niche or the artifact of who the founder happened to know.
- **Every wrong assumption costs a month.** Committing the whole sprint to the wrong ICP burns budget and time.
- **Outbound is the best research instrument available.** Unlike surveys or content marketing, outbound produces structured data: open rates, reply rates, objection patterns, the questions prospects ask before they'll take a meeting. These are the signals that tell you whether a wedge is real.

### 2.2 What we're optimizing for

Two outputs simultaneously:

1. **Pipeline** — booked meetings with qualified prospects, handed off to Billr for close.
2. **Evidence** — a dataset on which ICP sub-segment responds, which message angle resonates, what objections come up, and where the genuine pull is. This becomes Billr's Series A deck slide on ICP clarity.

### 2.3 The hypotheses

Each hypothesis gets a dedicated segment, message angle, and contact volume. See Section 4 for the full ICP breakdown. Note the weighting: H1 is the primary hypothesis, H2 is a validated secondary, H3 is available as an exploration slot only in the larger packages.

| # | Hypothesis | Role in sprint | Why worth testing |
|---|---|---|---|
| H1 | **Logistics vertical — 3PL, fulfillment, warehousing, freight** | **Primary, always included** | Two reference customers already; pricing complexity (storage × volume × SKU × carrier) is the sharpest pain; global TAM of ~340K firms is more than sufficient for multi-year scaling |
| H2 | **Usage-based SaaS, infrastructure, and AI** | **Secondary, always included** | Category where "usage-based billing" is an acknowledged problem; Metronome / Orb / Lago validate the narrative; Billr's custom flexibility needs testing against self-serve configurable platforms |
| H3 | **Complex vertical B2B SaaS (healthtech, energy, telco, construction, etc.)** | **Exploration slot — Package 3 only** | Broad and noisy; only worth testing once H1 and H2 signal is solid, as a "could we expand?" probe |

By month 3, one hypothesis will visibly outperform. The remaining budget flows there.

### 2.4 Tibexa's strategic recommendation: logistics-first

Tibexa's professional opinion — offered alongside the experimental structure — is that Billr should concentrate the next 18–24 months in the **logistics vertical** and treat horizontal expansion (usage-based SaaS, vertical SaaS) as deliberate, later-stage moves rather than a parallel GTM. The reasoning:

**1. Market size is already more than sufficient.** Global 3PL firms number ~340,000 (IBISWorld / Speed Commerce 2024). The US alone hosts ~73,000. The global 3PL market is $1.41T in 2025, projected $1.54T in 2026. Even capturing 0.1% of the signal-filtered SAM in 3PL produces Series-B-grade revenue. There is no revenue-scalability reason to go horizontal early.

**2. Operational complexity compounds non-linearly.** Serving logistics + usage-based SaaS + vertical SaaS simultaneously means:
- Three distinct ICP languages, objection libraries, case studies, and trust anchors
- Three distinct sales motions (CFO-led ops buying vs. CTO-led infra buying vs. product-led commercial buying)
- Three distinct implementation patterns (batch-heavy logistics vs. real-time SaaS events vs. regulated vertical compliance)
- Marketing, content, and event presence fragmented across three unrelated communities

At 2–10 employees, this is a fatal distraction. A focused 3PL positioning lets Billr *own* one conversation before entering a second.

**3. The logistics vertical has defensible moats that horizontal usage-based doesn't.** In usage-based SaaS, Billr competes with Metronome ($100M+ raised), Orb, Lago, Togai, and Stripe Billing — all well-funded, all with configurable products. In logistics billing, the incumbents are Extensiv Billing Manager, Hopstack, 3PL Central, and spreadsheets. **That's a more winnable field.** Two case studies (Quivo, Ecomflow) already position Billr credibly; a third and fourth logistics logo close the loop on category leadership.

**4. Language and pain-specificity are a sales unlock.** Logistics CFOs and COOs speak about pallets, pick fees, carrier accessorials, peak-season surcharges, storage-day math, and DIM-weight gotchas. A billing vendor who uses this language in the first email has a massive advantage over a generic "usage-based billing infrastructure" pitch. Tibexa's operating thesis is that **vertical language beats horizontal positioning** for any early-stage infrastructure vendor.

**5. The horizontal option stays open later.** Logistics-first doesn't close off usage-based SaaS — it just sequences it. Once Billr has 15–25 logistics customers and a clear playbook, the operational and commercial structures are in place to expand into an adjacent vertical without duress.

**What this means for the sprint:** Tibexa will run the three-hypothesis test as designed (because we agreed to test, not assume). But the sprint is pre-weighted toward H1 logistics, and the month-2 / month-3 decision gates will pass final budget toward logistics unless H2 shows *unusually* strong signal. H3 only runs in Package 3 as a probe.

---

## 3. Value Proposition — What We'll Actually Say

Based on the website and the two case studies, Billr's strongest positioning rests on four pillars. Each maps to a different buyer psychology and message angle. We'll test them across segments.

| # | Angle | Core promise | Best-fit buyer |
|---|---|---|---|
| 1 | **Escape the middleware tax** | "Chargebee/Stripe Billing forces you to build a middleware layer to handle your real pricing. We replace that entire layer." | CTO / VP Eng at scaling startup |
| 2 | **Stop the revenue leak** | "If a price isn't entered, you silently lose money. We flag it in real time, not at month-end." (Quivo angle) | CFO at mid-market operating company |
| 3 | **Billing in hours, not days** | "Monthly billing runs take 12+ hours and require overnight test runs. Billr compresses to 1 hour with zero test runs." (Quivo + Ecomflow angle) | Head of Finance / Operations at high-volume ops company |
| 4 | **Price anything you can imagine** | "Volume tiers, customer-specific overrides, mixed models, currency conversion — model it, don't build it." | Product / commercial leadership launching a new pricing model |

Note: angles 2 and 3 are the **most concrete** (numbers attached, competitor comparison embedded). Angles 1 and 4 are the most **aspirational** (broader appeal, thinner proof). Early A/B testing will tell us which converts.

---

## 4. Ideal Customer Profile — Three Hypotheses, TAM → SAM Framework

A note on numbers: early-stage ICP work fails when the TAM is defined too narrowly — we disqualify before we've observed. In each hypothesis below we define the **full TAM** (anyone who plausibly fits), then a **Serviceable Addressable Market (SAM)** filter based on buying-readiness signals. The sprint targets SAM; the hypothesis-testing logic lets us expand back into TAM if SAM underperforms.

We deliberately **do not filter tightly on employee count** at the TAM stage. A 30-person usage-based startup, a 900-person mid-market SaaS, and a 5,000-person logistics group can all have the same billing pain — the differentiator is pricing complexity, not headcount. The sprint will tell us which company size converts.

### 4.1 Hypothesis 1 (primary): 3PL, fulfillment, warehousing, and freight

| Criterion | Definition |
|---|---|
| Industry | Third-party logistics, e-commerce fulfillment, warehousing, freight forwarding, parcel networks, cold-chain logistics, contract logistics |
| Size (TAM) | Any operator with multi-customer billing complexity — no hard employee ceiling |
| Signal for SAM | Runs variable pricing (per pallet, per pick, per order, per storage day, per shipment); visible online pricing page OR "request quote" model; job postings for billing / revenue ops / WMS roles; tech-forward signals (ERP, WMS, API integrations); active investment in software/platform; growth signals (new warehouses, new geographies, funding) |
| Decision maker | CFO, Head of Finance, COO, VP Operations, CTO — varies by company maturity |
| **TAM (global)** | **~340,000 accounts** (Speed Commerce 2024 global 3PL count; US ~73K per IBISWorld 2024; Asia-Pacific ~40% share; Europe ~25%; North America ~28%. Global 3PL market: $1.41T in 2025, $1.54T projected 2026) |
| **SAM (signal-filtered)** | **~20,000–25,000 accounts** — operators with multi-tier pricing, tech stack maturity, and buying-readiness signals |

**Why this is the primary hypothesis and the recommended long-term focus:** Two existing references. Pain is extreme and well-documented (Quivo had 1,170 active price sheets). The TAM is large enough that Billr can scale for years without leaving the vertical. Competitive field in logistics billing is weaker than in horizontal usage-based billing — the incumbents are Extensiv, Hopstack, and spreadsheets rather than well-funded Metronome-class competitors.

**What we don't yet know:** which sub-vertical (pure-play fulfillment vs. freight forwarder vs. cold-chain vs. contract logistics vs. parcel networks) has the sharpest pain — and in which geography. The sprint will reveal both.

**Why this is the strongest hypothesis:** Two existing references. Pain is extreme and well-documented (Quivo had 1,170 active price sheets). Customers of 3PLs increasingly demand real-time visibility that legacy billing can't provide — a genuine forcing function.

**What we don't yet know:** which sub-vertical (pure-play fulfillment vs. freight forwarder vs. cold-chain vs. contract logistics) actually has the sharpest pain. The sprint will reveal this.

### 4.2 Hypothesis 2 (secondary): Usage-based SaaS, infrastructure, AI, and data platforms

| Criterion | Definition |
|---|---|
| Industry | API platforms, developer tools, AI/ML inference, cloud infrastructure, data infra, observability, FinOps, vertical API products |
| Size (TAM) | Any usage-based-pricing product past seed stage |
| Signal for SAM | Public pricing page shows tokens / requests / GB / events / credits / seats+usage hybrid; raised funding in last 36 months; current stack = Stripe Billing / Chargebee / in-house (identifiable via BuiltWith, job postings, GitHub repos, engineering blog posts); visible "billing engineer" or "revenue ops" hire |
| Decision maker | CTO, VP Engineering, Head of Platform, Head of Revenue Ops, CFO |
| **TAM (global)** | **~45,000–55,000 accounts** (Crunchbase identifies >45K SaaS companies with usage-based pricing components across US, EU, Israel, India, LATAM) |
| **SAM (signal-filtered)** | **~7,000–9,000 accounts** — post-Series A, publicly usage-based, identified billing stack |

**Why this matters as a test:** This is the category where "usage-based billing" is already a named, understood problem. Competitors (Metronome, Orb, Lago, Togai) raised significant rounds on this narrative. Billr's positioning difference — "we build it around your model vs. you configure ours" — needs to be tested for whether it's a real preference or a niche quirk, given the crowded and well-funded competitive field.

**What we don't yet know:** whether Billr's "custom-built per client" story reads as superior craftsmanship or as slow and expensive compared to self-serve configurable platforms. Section 2.4 explains why Tibexa recommends treating this as a test rather than a co-equal GTM track.

### 4.3 Hypothesis 3 (exploration only, Package 3): Complex B2B vertical / industry-specific platforms

| Criterion | Definition |
|---|---|
| Industry | Vertical software in healthtech, energy, utilities, telco, construction tech, proptech, fintech-adjacent, IoT platforms, industrial SaaS *(logistics SaaS is excluded here — it lives in H1)* |
| Size (TAM) | Any vertical SaaS with non-standard pricing past product-market fit |
| Signal for SAM | Pricing page is "contact sales" OR shows complex feature/usage hybrid; public finance-team pain signals (LinkedIn posts, Reddit, G2 reviews mentioning billing); recent pricing-page changes; hiring for billing/revenue operations; regulatory complexity (healthcare claims, utility meters, telco CDRs) |
| Decision maker | CFO, COO, Head of Revenue Operations, VP Product (pricing owner) |
| **TAM (global)** | **~45,000–55,000 accounts** |
| **SAM (signal-filtered)** | **~6,000–8,000 accounts** — filtered by revenue >€2M, pricing complexity, buying-readiness signals |

**Why this is an exploration slot and not a core hypothesis:** Broadest pool, highest noise, lowest prior evidence. Worth probing only once H1 and H2 have given signal — hence its inclusion only in Package 3. If a sub-vertical (e.g., healthtech claims billing, energy usage billing, telco CDR-based billing) responds disproportionately, that's a directional input for Billr's 2027 roadmap, not a wedge to pursue this year.

**What we don't yet know:** which vertical is under-served by existing billing tools because the legacy verticals (telco, energy) already have entrenched billing systems and the newer verticals (healthtech, proptech) may not yet feel the pain sharply enough.

### 4.4 Summary: TAM → SAM → Sprint SOM

| Hypothesis | TAM | SAM (buying-ready) | SOM at Small Pkg | SOM at Medium Pkg | SOM at Large Pkg |
|---|---:|---:|---:|---:|---:|
| H1 — Logistics (3PL / fulfillment / freight) | ~340,000 | ~22,000 | 2,900 | 5,800 | 10,000 |
| H2 — Usage-based SaaS / infra / AI | ~50,000 | ~8,000 | 1,900 | 3,800 | 5,500 |
| H3 — Vertical SaaS / industry platforms | ~50,000 | ~7,000 | — | — | 2,500 |
| **Total** | **~440,000** | **~37,000** | **4,800** | **9,600** | **18,000** |

Notes on the math:
- SOM = accounts we actually touch in the 3 active outreach months
- Packages 1 and 2 test only the two core hypotheses (H1 + H2); H3 is introduced as an exploration slot only in Package 3
- Within each package, H1 gets the larger share of volume reflecting its role as the primary hypothesis (~60% H1 / ~40% H2 in Packages 1 and 2; ~55% H1 / ~30% H2 / ~15% H3 in Package 3)
- After the month-2 decision gate, the weaker hypothesis loses volume and the stronger gains
- Contact-per-account multiplier: ~1.5 (decision maker + one adjacent influencer), so monthly contact volume = SOM × 1.5 ÷ 3

### 4.5 Explicit choices we are NOT making up front

- **No employee-count filter at the TAM stage.** The sprint tests this — if 2,000-person logistics groups convert better than 200-person ones, we learn it. Pre-committing narrows the field prematurely.
- **No geography filter in the primary sprint.** English-language outreach globally; the heat map from replies tells us where the wedge lives (EU mid-market vs. US enterprise vs. APAC, etc.)
- **No "SaaS-only" or "non-SaaS-only" bias.** Both Quivo (non-SaaS operator) and Ecomflow (3PL-as-service) work — we test both revenue-model types.

### 4.6 Explicitly out of scope for this sprint

- **Pre-seed / <$500K ARR startups** — cannot afford custom infrastructure; better served by Stripe Billing defaults. Removing this filter alone would bloat TAM by ~200K meaningless accounts.
- **Consumer subscription businesses** (streaming, meal kits, fitness apps) — Stripe / Recurly dominate and pricing isn't complex enough to justify custom.
- **Heavily regulated banking / payment processing / core fintech** — compliance bar too high for a 2024-founded vendor to clear in a 4-month sales cycle.
- **Public-sector billing** (utilities government contracts, Medicare claims directly) — RFP-driven, multi-year sales cycles, wrong channel for outbound.

---

## 5. Message Matrix — Angle × Segment

Each segment gets 2–3 message variants mapping to value-prop angles from Section 3. One primary touch + one follow-up per contact.

| Segment | Primary angle | Secondary angle | CTA |
|---|---|---|---|
| European 3PLs (H1) | Angle 3 — billing in hours, not days | Angle 2 — stop revenue leak | "15-min call to see the Quivo setup" |
| US/Global 3PLs (H1) | Angle 2 — revenue leak at scale | Angle 4 — price anything | "See the Ecomflow 150-brand architecture" |
| Usage-based infra/AI (H2) | Angle 1 — escape middleware | Angle 4 — price anything | "How we replaced Chargebee for Quivo" |
| Usage-based dev tools (H2) | Angle 4 — model any pricing | Angle 1 — escape middleware | "15-min architecture review" |
| Vertical SaaS — healthtech, logtech (H3) | Angle 3 — billing in hours | Angle 2 — revenue leak | "Show me your current billing flow" |
| Vertical SaaS — energy, telco (H3) | Angle 4 — price anything | Angle 3 — billing in hours | "Case study walkthrough" |

The CTAs escalate by segment: where we have case-study fit, we offer the case study directly; where we don't, we offer a discovery-format call.

---

## 6. Operational Model

### 6.1 Monthly workflow

1. **List building** — Accounts matching ICP filters are pulled from a combination of Apollo / LinkedIn Sales Nav / Crunchbase / BuiltWith / job-posting signals. Weekly batches of ~600 contacts.
2. **Enrichment** — Decision-maker email, company pricing page, recent funding, signals of billing pain (e.g., "hiring billing engineer," "migrating from X").
3. **Personalization** — Segment template + 2–3 company-specific lines per email.
4. **Send** — Primary email + one follow-up 4–6 days later.
5. **Reply classification** — Four levels:
   - L1: Interest / curiosity
   - L2: Information request (case study, architecture deep dive)
   - L3: Meeting-scheduling conversation
   - L4: Meeting booked
6. **Handoff** — L3+ replies handed to Billr within 30 minutes. Founder or sales lead takes it from there.
7. **Weekly report** — Volume, replies, level distribution, meetings booked, **objection themes** (this is the research output).

### 6.2 Why "objection themes" matter for a startup

A typical lead-gen agency reports on volume and replies. For an early-stage company, the **objections are the gold**. Examples of what we'll surface:

- "We tried Chargebee, it works fine" — signals the middleware pain isn't felt yet at that scale
- "We built it in-house" — tells us where the build-vs-buy line is
- "Your pricing is too opaque" — tells us Billr's sales-cycle friction points
- "We're locked in with Stripe Billing for 18 months" — tells us the switching cost story

We build a structured objection log. After month 2, Billr has a far clearer picture of who's ready to buy and what story unlocks them.

### 6.3 Handoff SLA

| Action | Timing | Owner |
|---|---|---|
| L3+ reply detected → Billr notified | 30 min | Tibexa |
| First reply to prospect | 2h (business hours) | Billr |
| Meeting confirmation / calendar | 24h | Billr |
| Post-meeting outcome logged | 48h after meeting | Billr |

Meetings where Billr response exceeds 48h are logged but excluded from Tibexa's KPI accounting — transparency measure.

---

## 7. KPI Framework

### 7.1 Volume KPIs by package (steady state, months 2–4)

All numbers below are **steady-state monthly** figures for active outreach months (2, 3, 4). Setup month 1 has no outbound volume.

**Small Package — Discovery Sprint**

| Metric | Monthly target | 3-month total |
|---|---:|---:|
| Accounts touched | ~6,700 | ~20,000 |
| Contacts sent (primary + follow-up) | 10,000 | 30,000 |
| Positive replies (L1+) at 0.35% | 35 | 105 |
| Qualified replies (L2+) | 17 | 52 |
| Booked meetings | 17–23 | 50–70 |

**Medium Package — Validation Sprint** *(recommended)*

| Metric | Monthly target | 3-month total |
|---|---:|---:|
| Accounts touched | ~16,700 | ~50,000 |
| Contacts sent | 25,000 | 75,000 |
| Positive replies (L1+) at 0.35% | 87 | 262 |
| Qualified replies (L2+) | 44 | 131 |
| Booked meetings | 42–58 | 125–175 |

**Large Package — Market Sweep**

| Metric | Monthly target | 3-month total |
|---|---:|---:|
| Accounts touched | ~33,300 | ~100,000 |
| Contacts sent | 50,000 | 150,000 |
| Positive replies (L1+) at 0.35% | 175 | 525 |
| Qualified replies (L2+) | 87 | 262 |
| Booked meetings | 83–117 | 250–350 |

**Response-rate assumption:** 0.35% positive-reply-to-contact ratio is our conservative baseline for high-volume segmented B2B outbound. Observed range for comparable operations in 2026 sits at 0.35%–0.80%. If the sprint outperforms, actual numbers scale linearly — a 0.55% rate on the Medium package produces ~412 positive replies instead of 262.

### 7.2 Conversion KPIs (Billr-side, tracked jointly)

- Meeting → qualified opportunity rate
- Qualified opportunity → closed-won rate
- Average deal size (ARR)
- Sales cycle length

### 7.3 Reporting rhythm

- **Weekly:** 1-page dashboard (volume, replies, handoffs, top 3 objections, blockers)
- **Monthly:** Performance review + segment comparison + message-angle performance + ICP hypothesis scorecard
- **End of sprint (month 4):** Wedge recommendation deck — which ICP/message/angle combination to scale on

### 7.4 Decision gates

**End of Month 2:** First hypothesis-ranking checkpoint. If one ICP is clearly underperforming (<50% of target replies), reallocate its contact budget to the strongest one for month 3.

**End of Month 3:** Wedge lock. Remaining month-4 volume concentrates on the winning ICP. Message variants narrow from 6 to 2–3.

**End of Month 4:** Strategy document delivered: recommended ICP, positioning, 3-angle message framework, and a plan for sprint 2 (either double-down on winning ICP, or expand adjacent segment).

---

## 8. Packages, Outcomes, and ROI Model

### 8.1 Three packages, one methodology

All three packages run the same 4-month structure (1 setup + 3 active), the same three ICP hypotheses, the same weekly reporting cadence. **What changes is volume and therefore signal strength.**

The small package is enough to know whether outbound works for Billr at all and produce first directional ICP evidence. The medium package produces enough signal to confidently pick a wedge and book meaningful pipeline. The large package attacks the full signal-filtered SAM and treats the sprint as a market-share grab.

Because the unit economics of lead-gen operations don't scale linearly (the setup, strategy, copy, infrastructure, and reporting are roughly fixed), **package pricing will not scale linearly with volume** — the medium and large packages offer better economics per contact. Commercial terms follow separately.

### 8.2 Package definitions

**Package 1 — Discovery Sprint — €2,500/month**
- 3-month active send volume: **10,000 sends/month** (30,000 total, ~20,000 accounts touched)
- Hypothesis coverage: **H1 logistics + H2 usage-based SaaS** (roughly 60/40 split)
- Purpose: "Is outbound viable for Billr? Does logistics confirm as the wedge, or does H2 surprise?"
- Best for: Billr wants a low-risk first engagement, ICP clarity weighted over pipeline volume
- Expected booked meetings: 50–70 across 3 months
- Expected closed deals (20% meeting-to-deal): 10–14
- Note on close timing: sprint ends month 4; expect 2–3 deals to close during the sprint and the remainder to close in months 5–10 per the sales cycle below

**Package 2 — Validation Sprint — €3,500/month** *(recommended)*
- 3-month active send volume: **25,000 sends/month** (75,000 total, ~50,000 accounts touched)
- Hypothesis coverage: **H1 logistics + H2 usage-based SaaS** (roughly 60/40 split, rebalanced post month-2 gate)
- Purpose: "Validate and scale the winning hypothesis inside a single engagement"
- Best for: Billr is ready to commit to learning *and* producing pipeline; the best signal-per-spend package
- Expected booked meetings: 125–175 across 3 months
- Expected closed deals: 25–35 (4–6 during sprint, remainder spread across months 5–12)

**Package 3 — Market Sweep — €4,500/month**
- 3-month active send volume: **50,000 sends/month** (150,000 total, ~100,000 accounts touched)
- Hypothesis coverage: **H1 logistics + H2 usage-based SaaS + H3 vertical SaaS** (roughly 55/30/15 split)
- Purpose: "Talk to a large portion of the serviceable market in H1 and H2; probe H3 for 2027 directional insight."
- Best for: Billr is ready to treat the sprint as a category-capture move and has capacity to onboard new customers steadily across the following 12 months
- Expected booked meetings: 250–350 across 3 months
- Expected closed deals: 50–70 (8–12 during sprint, remainder spread across months 5–15)
- **Implementation-capacity note:** With Billr's 4-week implementation cycle, 50–70 deals cannot be onboarded simultaneously. The sales-cycle timing below spreads closes naturally across 12+ months — see Section 8.2.1.

**Pricing summary:**

| Package | Monthly retainer | 3-month active cost | Setup fee | 4-month total |
|---|---:|---:|---:|---:|
| Small — Discovery | €2,500 | €7,500 | (included in Month 1) | €10,000 |
| Medium — Validation | €3,500 | €10,500 | (included in Month 1) | €14,000 |
| Large — Market Sweep | €4,500 | €13,500 | (included in Month 1) | €18,000 |

Month 1 is the setup month — list build, infrastructure, copy, warmup — and is billed at the same monthly rate as active months. No outbound volume is produced in Month 1, but the setup carries the full cost of getting the operation production-ready.

### 8.2.1 Sales cycle and close cadence

Custom billing infrastructure is a **considered B2B purchase**, not an impulse buy. Realistic timing assumptions:

| Stage | Typical duration |
|---|---|
| Positive reply → first meeting | 1–3 weeks |
| First meeting → qualified opportunity | 2–4 weeks |
| Qualified opportunity → signed contract | 4–12 weeks (CFO buy-in, technical eval, security review, SOC2 questions) |
| Contract → kickoff → go-live (Billr's 4-week implementation) | 4–6 weeks |
| **Total: cold contact → live customer** | **3–6 months** |

Implications for the packages:
- **Most closed deals from a sprint land in months 5–10 after sprint start**, not during the sprint itself
- The monthly report distinguishes pipeline-in-flight (opportunities progressing) from closed-won — both are tracked
- For Package 3 specifically: 9–15 deals spread across months 5–12 averages ~1–2 onboardings per month, which comfortably fits Billr's 4-week implementation model without requiring parallel ramp

This timing also means the **sprint's ICP evidence and objection dataset arrive in month 4, well before most deals close** — giving Billr time to refine positioning and onboarding for the deals landing mid-year.

### 8.3 Conversion assumptions (held constant across packages)

| Variable | Value | Note |
|---|---|---|
| Contact-to-account multiplier | 1.5 | Decision maker + 1 adjacent |
| Positive reply rate (L1+) | 0.5% conservative baseline | 0.5–1.2% observed range for strong B2B outbound |
| Qualified reply rate (L2+) | 50% of L1+ | |
| Meeting conversion from qualified | 75% | Warm, pre-qualified |
| Meeting-to-deal conversion | 15–25% | Early-stage B2B SaaS with strong case study |
| Average ARR per closed deal | $10,000 | Billr indication ($8–12K midpoint) |
| 3-year LTV per deal | ~$27,000 | $10K Y1 + $9K Y2 + $8.1K Y3 at 90% gross retention |

### 8.4 Outcome matrix — conservative baseline (0.35% reply, 20% meeting-to-deal)

| Metric | Small Pkg | Medium Pkg | Large Pkg |
|---|---:|---:|---:|
| Sends over 3 months | 30,000 | 75,000 | 150,000 |
| Positive replies (L1+) | 105 | 262 | 525 |
| Qualified replies (L2+) | 52 | 131 | 262 |
| Booked meetings | 50–70 | 125–175 | 250–350 |
| Closed deals (at 20%) | 10–14 | 25–35 | 50–70 |
| **Year-1 ARR** | **$100K–140K** | **$250K–350K** | **$500K–700K** |
| **3-year LTV** | **$270K–378K** | **$675K–945K** | **$1.35M–1.89M** |

### 8.5 Outcome matrix — upside scenario (0.55% reply, 22% close)

| Metric | Small Pkg | Medium Pkg | Large Pkg |
|---|---:|---:|---:|
| Positive replies | 165 | 412 | 825 |
| Qualified replies | 82 | 206 | 412 |
| Booked meetings | 82–115 | 206–288 | 412–577 |
| Closed deals (at 22%) | 18–25 | 45–63 | 90–127 |
| **Year-1 ARR** | **$180K–250K** | **$450K–630K** | **$900K–1.27M** |
| **3-year LTV** | **$486K–675K** | **$1.22M–1.70M** | **$2.43M–3.43M** |

### 8.6 ROI framing

| Package | 4-month cost | Conservative Year-1 ROI | Upside Year-1 ROI | Conservative 3yr LTV ROI |
|---|---:|---:|---:|---:|
| Small — Discovery | €10,000 | ~$100K–140K on €10K = **9–13×** | ~$180K–250K = **16–23×** | ~$270K–378K = **25–35×** |
| Medium — Validation | €14,000 | ~$250K–350K = **17–24×** | ~$450K–630K = **30–43×** | ~$675K–945K = **46–65×** |
| Large — Market Sweep | €18,000 | ~$500K–700K = **27–38×** | ~$900K–1.27M = **49–69×** | ~$1.35M–1.89M = **74–104×** |

These returns are intentionally striking — and they reflect why outbound remains the most capital-efficient GTM motion for an early-stage B2B infrastructure company *if it converts at all*. The critical uncertainty is reply rate and close rate, not the math once those land. The Small package is designed precisely to de-risk both.

**What to hold against these numbers:** Billr's actual close rate may start below 20% in the first sprint as positioning and objection-handling find their groove. We've modeled 20% because that's achievable with case-study-backed sales into a qualified pipeline; month-2 and month-3 replies refine this expectation in real time.

### 8.7 What the sprint delivers beyond closed deals

Equally valuable for a 2024-founded startup:

1. **Structured objection database** — tens to hundreds of documented objections, tagged by ICP and angle
2. **Wedge recommendation** — which ICP to double down on in months 5–12, with supporting evidence
3. **Message library** — proven copy, tested angles, ready to reuse or hand to future inbound content
4. **Logo collection** — even 1–2 additional logos materially strengthens Billr's sales and fundraising narrative
5. **Founder conversation volume** — months of customer-discovery quality input in a compressed 3-month window

For an early-stage company, the **second-order value** (ICP clarity, pitch iteration, category evidence) typically exceeds the first-order value (closed deals). The sprint is deliberately designed to produce both.

---

## 9. Implementation Timeline

### Month 1 — Setup & Calibration (no active outreach yet)

- **Week 1:** Kickoff, deep ICP workshop across all three hypotheses, review of both case studies, buyer persona interviews (if possible with Quivo/Ecomflow contacts)
- **Week 2:** Sending infrastructure setup — dedicated domains (at least 2 for deliverability buffer), DNS / SPF / DKIM / DMARC, warmup starts
- **Week 3:** Message copy finalization across 6 variants (3 angles × 2 segments each), Billr approval, initial list builds for H1/H2/H3
- **Week 4:** Pilot send — 150–300 contacts to calibrate deliverability, tone, and early reply signal before going to full volume

### Month 2 — Full-volume launch

- Volume per selected package (4,800 / 9,600 / 18,000 accounts across the 3 active months — month 2 sees 1/3 of that volume)
- Reply classification and objection log live
- First decision gate (mid-month 2): which hypothesis is leading
- Weekly Billr sync calls to review handoffs and messaging

### Month 3 — Optimization & rebalancing

- Budget reallocates toward leading ICP
- Message variants narrow (drop the worst 2, double the best 2)
- Mid-month 3 wedge lock conversation

### Month 4 — Concentration & wrap

- Full volume on winning ICP + best-angle message combination
- Final objection-database synthesis
- Wedge recommendation and sprint-2 strategy deck delivered end of month 4

---

## 10. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Low deliverability (new domains, Vienna-based sender, unknown to inbox providers) | Multiple sending domains warmed in parallel; gradual volume ramp; quality-over-quantity bias on list |
| Billr founder bandwidth — can't respond to replies in <24h | Pre-built reply templates for L1/L2; founder only handles L3+; optional inside-sales support module |
| All three hypotheses underperform (real risk for early-stage positioning) | Month-2 checkpoint built explicitly to catch this; fallback is to expand messaging-angle tests within strongest hypothesis rather than add a fourth ICP |
| Language / region — Billr is Austrian; US prospects may read "Vienna startup" as risk | Lead with Quivo (German-language European credibility) for EU; lead with Ecomflow (global-scale 3PL) for US; customer testimonials carry the geography |
| Compliance — GDPR for EU outbound, CAN-SPAM for US | B2B legitimate-interest basis; unsubscribe on every email; opt-out suppression list maintained centrally |
| Attribution — closed deals take 2–6 months; sprint ends before full conversion data lands | Joint pipeline-tracking spreadsheet from day 1; month-4 report includes pipeline in flight, not just closed deals |

---

## 11. Assumptions to Validate With Billr

Listed separately so you can correct or refine each:

1. **Pricing model:** ARR of ~$10K per customer (midpoint of $8–12K). Confirm this is net of implementation fees.
2. **Implementation capacity:** Billr's 4-week implementation model assumes dev involvement. With the sales-cycle timing in Section 8.2.1, deals land spread across months 5–12 rather than concentrated. Confirm 1–2 parallel onboardings per month is the right ceiling, or let us know if capacity is lower so we throttle volume accordingly.
3. **Founder availability:** Dominik (or sales lead) is available for 4–20 meetings per month starting month 2 (scales with package). ~1–5 hours per week on qualified meetings alone.
4. **Case-study usage:** Are Quivo and Ecomflow case studies approved for direct use in outbound? (Both are already on the public site, so we assume yes — confirming for anonymization preferences.)
5. **Geographic preference:** Any geography we should deprioritize (e.g., no Asia-Pacific given Vienna timezone, or no US until legal entity setup)?
6. **Pricing-model preference for ICP:** Do you want to bias toward companies already doing usage-based billing (validated pain, lower sales friction), or also pursue companies on flat/subscription pricing (larger TAM, higher conversion friction)?
7. **Channel scope:** Email-first is the assumption. Any strong preference for LinkedIn outreach in parallel (increases cost, adds 20–40% reply lift typically)?

## 11B. Open Questions — Decisions We Need Billr's Input On

These are the decisions that materially shape sprint setup. We can propose defaults for each, but early alignment saves weeks in month 1.

### 11B.1 On SAM filters and buying-readiness signals

Our draft SAM filter uses: multi-tier pricing, job postings for billing/revenue-ops roles, funding in last 36 months, public pricing complexity, tech stack signals (BuiltWith, GitHub, engineering blogs), hiring for WMS/ERP roles.

**Questions for Billr:**

- **Is there a specific ERP / WMS / billing tool on a prospect's stack that signals strong fit?** (E.g., "anyone on Manhattan WMS is a great fit because X" or "anyone on Extensiv Billing Manager is actively frustrated.") Founder-specific knowledge here is gold.
- **Are there specific titles beyond CFO / COO / CTO that convert?** (E.g., "Billing Operations Lead," "Head of Customer Success Engineering," "VP Revenue Operations.")
- **Events, conferences, or communities where your buyer shows up?** (E.g., Manifest, Shoptalk, SaaStr, MicroConf, PTAK Forum.) Prospects who attended recent events = a signal we can mine.
- **Podcasts, newsletters, Slack/Discord communities where the billing-pain conversation happens?** (E.g., Pricing I/O, Price Intelligently content, Logistics of Logistics podcast.)
- **Any "anti-signals"** — patterns where you've seen a prospect look great on paper but turn out to be a bad fit? (E.g., companies that just raised and are deep in M&A, or companies with a single-product simple pricing.)
- **What does a "dream customer" Billr wins in month 6 look like?** Describe one real company name you'd want on your website, and we'll reverse-engineer the SAM filter from there.
- **Is there a recent pricing-page or billing-stack change on competitors of your existing customers that we could use as a trigger?** (E.g., "if they just changed from flat to usage-based, they're prime.")

### 11B.2 On competitive positioning

- **How do you want Billr positioned against Metronome / Orb / Lago** when the prospect brings them up? "More custom" is not a strong answer alone — is there a sharper differentiator (speed to go-live? price? ownership of the code? EU data residency?)
- **How do you want to handle Chargebee / Zuora objections** ("we already use X")? Is your pitch "rip and replace," "middleware removal," or "complement for the hard cases"?

### 11B.3 On the H3 exploration slot (Package 3 only)

- If Package 3 is selected, which 2–3 verticals inside H3 are you **most** curious about? (e.g., healthtech billing, telco CDR, energy usage, construction project billing, IoT device billing.) We'd focus the H3 budget on those rather than spread thinly across all.

### 11B.4 On Tibexa's logistics-first recommendation

Section 2.4 makes the case for concentrating in logistics for the next 18–24 months. The multi-hypothesis sprint is designed to serve the founder's stated preference to test breadth, but:

- **If the sprint confirms H1 logistics is outperforming, are you philosophically open to dropping H2 from sprint 2 onwards** and going vertical-focused? Or is horizontal positioning a non-negotiable long-term identity for Billr?
- The answer to this shapes how aggressively the month-2 / month-3 decision gates rebalance budget. If logistics-only is a live option, the gate cuts harder toward H1; if horizontal is permanent, the gate rebalances more gently.

---

## 12. Next Steps

1. Review this document end-to-end; flag sections that need correction
2. Confirm or refine the three ICP hypotheses (add, remove, re-weight)
3. Confirm assumptions in Section 11
4. Agree on sprint pricing (Tibexa to send commercial terms separately)
5. Kickoff workshop scheduled for week 1 of month 1
6. Sprint start target: **May 2026**

---

*This document is a strategic starting point, not a contract. The numbers are modeled on conservative B2B outbound benchmarks for 2026 and will be recalibrated against real data from month 1 pilot sends. The point of this sprint is to replace assumptions with evidence — including the assumptions in this document.*
