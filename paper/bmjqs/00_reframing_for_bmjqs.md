# Reframing the ZOL Paper for BMJ Quality & Safety

**Purpose:** This document explains why and how we're reframing the paper from an operations management contribution (HCMS) to a quality and safety contribution (BMJ QS). The original HCMS versions are preserved in the parent `paper/` directory.

---

## Why change the framing?

BMJ Quality & Safety (IF 5.7, Q1) is a higher-impact journal than HCMS (IF ~3.0). But it publishes from a different angle. HCMS asks: "How do we run hospitals more efficiently?" BMJ QS asks: "How do we make healthcare safer and higher quality?"

Our data answers both questions. The findings are identical. The difference is which implication we lead with.

| | HCMS framing | BMJ QS framing |
|---|---|---|
| **Opening question** | "How should we benchmark ORs fairly?" | "Do current OR metrics mislead decision-makers in ways that affect care quality?" |
| **Central claim** | Progressive stratification is a better benchmarking method | Standard OR benchmarks are a measurement validity problem — and flawed measurement is a quality and safety risk |
| **Who cares** | OR managers, operations researchers | Clinical leaders, safety officers, hospital boards, policymakers |
| **"So what?"** | Better benchmarking → smarter resource allocation | Better benchmarking → fewer wrong decisions → fewer cancelled patients, less staff fatigue, more equitable care |
| **Room-level finding** | "This is where the efficiency gains are" | "This is where patients face unequal safety exposure" |
| **FCOTS finding** | "FCOTS is a weak efficiency proxy" | "Over-reliance on FCOTS diverts safety improvement resources to the wrong lever" |
| **Cascading finding** | "Cascading wastes more time than overruns" | "Cascading pushes cases into shift handovers, a known error-prone transition" |

---

## What BMJ QS actually publishes on OR topics

Every OR-related paper in BMJ QS connects to patient safety:

- **Abdelfattah et al. (2020)** — Systematic review finding 20.5% of OR time lost to flow disruptions; examined links to surgical outcomes
- **Joseph et al. (2019)** — Minor flow disruptions cluster and escalate into major ones (cascading — relevant to our finding)
- **Armstrong et al. (2022)** — Surgical safety checklist effects on provider and patient outcomes
- **Lingard et al. (2004)** — Communication failures in ORs, classified by type and effect
- **Schmidtke et al. (2023)** — Why strong surgical trial evidence doesn't change practice (implementation gap)

Pattern: safety culture, communication, flow disruptions, checklists, implementation science. No pure operations/scheduling papers.

Our paper enters this space through the **measurement validity** door: "The metrics hospitals use to compare OR performance are broken. Broken metrics lead to wrong decisions. Wrong decisions affect patients."

---

## The five safety connections in our data

These are not invented connections. They follow directly from the findings.

### 1. Misleading benchmarks → wrong resource allocation → patient impact

When Hospital A's overtime rate looks 16.8x worse than Hospital B's, boards redirect resources toward "fixing" Hospital A. But if 80% of that gap is structural, 80% of that effort is wasted. Meanwhile, the real problems (room-level variation within each hospital) go unaddressed. Misallocated improvement resources have opportunity costs for patients.

### 2. Overtime → staff fatigue → known safety risk

The link between extended working hours and medical errors is well documented (Landrigan et al., 2004, NEJM; Barger et al., 2006, PLOS Medicine). Our finding that cascading delays — not FCOTS — drive most overtime tells safety leaders where to intervene. Fixing first-case starts addresses maybe 4-8% of the cascading problem (Pandit et al., 2012). Fixing mid-day flow addresses the rest.

### 3. Cascading delays → shift-boundary transitions → handover risk

Cases pushed from day shift into evening shift create handover moments. Handovers are among the most error-prone transitions in healthcare (WHO, 2007; Nagpal et al., 2010, Annals of Surgery). Our data show that at Genk, 5% of cases are displaced into a later shift window, with a mean start delay of +352 minutes. These patients are the ones most likely to experience a shift handover during or shortly after their procedure.

### 4. Room-level variation → unequal safety exposure

At Maaseik, a patient scheduled in room MO03 faces an 8.9% chance of their case going overtime. A patient in MK11 faces a 0.2% chance. That is a 44.5-fold difference in exposure to overtime-related risks (fatigued staff, rushed closure, shift handover). Both patients are in the same hospital. This is an equity-of-care finding, not just an efficiency finding.

### 5. Metric validity → decision quality → system safety

BMJ QS has published extensively on measurement in healthcare. If a metric systematically misleads decision-makers, it is a system safety problem. Our paper shows that three widely used OR metrics (overtime rate, FCOTS, utilization) fail as between-site discriminators because they conflate operating-model structure with operational performance. This is a measurement validity contribution.

---

## What changes in the paper

### Structure

BMJ QS uses BMJ Publishing Group conventions:

- **Word limit:** ~3,000-4,000 words body text (our HCMS draft is ~7,100 — needs cutting roughly in half)
- **Abstract:** 250 words, structured with headings: Objective / Design / Setting / Participants / Main Outcome Measures / Results / Conclusions
- **Reference style:** Vancouver (numbered superscript), not author-year
- **Reporting guideline:** STROBE checklist for observational studies (our study is a retrospective cross-sectional analysis of administrative data)
- **Figures/tables:** No fixed limit, but editorial preference is restraint

### What stays identical

- All data (228,623 cases, four sites, Jan 2022–May 2025)
- Progressive stratification method and results
- Room-level variance decomposition
- FCOTS analysis
- Duration CV analysis
- Cascading analysis
- All tables and figures

### What changes

1. **Title** — Shifts from benchmarking methodology to measurement validity / quality implications
2. **Introduction** — Opens with the patient safety angle, not the cost angle
3. **Discussion** — Leads with safety implications (fatigue, handovers, misallocated resources), not operations management implications
4. **Abstract** — Restructured to BMJ format
5. **Word count** — Cut from 7,100 to ~3,800
6. **References** — Add safety/quality literature (Landrigan, WHO handover guidelines, Nagpal), keep core OR references

---

## Risk assessment

| Risk | Likelihood | Mitigation |
|---|---|---|
| Desk rejection ("this is an operations paper") | Medium | Strong safety framing in abstract and cover letter; cite BMJ QS precedents (Abdelfattah, Joseph) |
| Reviewer asks for patient outcome data | Medium-High | Acknowledge as limitation; argue measurement validity contribution stands on its own; point to room-level safety exposure as indirect outcome |
| Reviewer says "resubmit to HCMS" | Medium | Cover letter explicitly argues why this is a quality/safety paper, not just an operations paper |
| Word count too tight for our content | Low | The tighter format actually helps — forces us to cut repetition and make every sentence earn its place |

---

## Fallback plan

If BMJ QS desk-rejects or rejects after review:
1. **HCMS** — Paper is already written in that format (files in parent directory)
2. **BMJ Open Quality** — BMJ's open-access sister journal, publishes more operational QI work, lower bar
3. **International Journal for Quality in Health Care** — Broader scope, accepts efficiency studies

---

## Decision for the meeting with Niels

Present both options:
1. **BMJ QS** — Higher prestige (IF 5.7), broader audience, but needs safety framing and carries desk-rejection risk
2. **HCMS** — Natural fit (IF 3.0), paper is nearly ready, high confidence of getting past the desk

Ask Niels which strategic priority matters more: prestige or certainty. Both are legitimate. A reasonable strategy is to submit to BMJ QS first (takes 2-3 weeks to reframe) and have HCMS as a ready fallback.
