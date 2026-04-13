# BMJ Quality & Safety — Paper Outline

**Working title:** Do operating-room performance comparisons measure quality or structure? A 228,623-case natural experiment

**Article type:** Original Research
**Target word count:** ~3,800 words body text
**Abstract:** 250 words, structured (Objective / Design / Setting / Participants / Main outcome measures / Results / Conclusions)
**Reporting guideline:** STROBE (observational study)
**Reference style:** Vancouver (numbered superscript)

---

## Structured Abstract (~250 words)

**Objective:** To test whether commonly used operating-room performance metrics produce valid comparisons across sites with different operating models, and to quantify the share of between-site variation attributable to structural design rather than operational quality.

**Design:** Retrospective observational study using a progressive stratification method. We filtered administrative OR data through four sequential adjustment layers (weekday activity, day-shift hours, elective urgency, admission type) and measured the between-site performance spread at each level.

**Setting:** Four sites of a single Belgian hospital network (Ziekenhuis Oost-Limburg), sharing governance, electronic health records, and labor agreements but operating structurally different OR models: a 24/7 tertiary center, a weekday-only ambulatory facility, a hybrid campus, and a specialized cardiac catheterization lab.

**Participants:** 228,623 surgical and interventional procedures performed between January 2022 and May 2025.

**Main outcome measures:** After-hours rate (proportion of cases extending past shift end), room-level overtime variation, first-case-on-time-start concordance with stratified overtime, and duration-estimation coefficient of variation.

**Results:** Raw after-hours rates differed 16.8-fold across sites (0.5% to 8.4%). After full stratification, the spread fell to 3- to 4-fold; approximately four-fifths of the raw gap reflected operating-model structure. Within-site room-level variation exceeded between-site variation at two of four campuses, with a 44.5-fold spread between the best and worst rooms at one site. First-case punctuality did not predict stratified overtime across sites.

**Conclusions:** Standard OR performance metrics conflate structural design with operational quality. Multi-site comparisons based on unadjusted metrics risk misdirecting quality improvement resources. Stratified, room-level reporting provides a more valid basis for identifying actionable quality gaps.

---

## 1. Introduction (~600 words)

**Opening hook — the measurement problem as a quality and safety issue**

Hospital boards and regulators routinely compare operating-room performance across sites using metrics like overtime rates, utilization, and first-case-on-time starts. These comparisons drive resource allocation, staffing decisions, and quality improvement priorities. When the metrics are misleading, the decisions they inform can be counterproductive: improvement resources directed to the wrong problems, staff pressured to meet targets that reflect structure rather than performance, and patients affected by cancellations or rushed schedules that follow from misguided benchmarks.

**The validity gap in OR metrics**

Recent work has raised concerns about the validity of standard OR metrics for cross-site comparison. Zhang and Pandit (2023) demonstrated that NHS Model Hospital calculations produce misleading averages by selectively reporting subsets of operating lists. Schouten et al. (2023) found 47 distinct OR metrics in the literature with inconsistent definitions, and no studies accounting for interactions between quality and efficiency measures. The dominant single-metric approaches — Macario's scorecard (2006), Dexter's overutilization framework (2004) — were designed for within-site use. Their validity as between-site discriminators has not been systematically tested.

**Why this matters for quality and safety**

OR overtime is not merely an efficiency problem. Extended working hours are associated with increased medical errors (cite Landrigan et al., 2004). Cases pushed past shift boundaries create handover transitions, a well-documented source of adverse events (cite Nagpal et al., 2010). When benchmarks misidentify the source of overtime, they misdirect the improvement effort: resources flow toward closing between-site gaps that are largely structural, while room-level variation — which is under local control and directly affects patient exposure to overtime-related risks — goes unaddressed.

**Study questions**

Three questions:
1. When sites within a shared-governance network differ in operating model, how much of the raw performance spread survives progressive stratification?
2. Is within-site room-level variation a larger source of quality-relevant overtime than between-site variation?
3. Do standard efficiency levers (FCOTS, duration-prediction accuracy) explain the residual performance gaps?

---

## 2. Methods (~800 words)

### 2.1 Setting and data

- ZOL network description (four sites, shared governance, different operating models)
- Study period: Jan 2022–May 2025, 228,623 cases after quality filtering
- Site profiles: Table 1 (same as HCMS version)
- Cathlab labeling error disclosure (one sentence)
- STROBE compliance statement

### 2.2 Variables

Same derived variables as HCMS version:
- Shift label, start difference, overtime flag/minutes, gap time, room swap, duration deviation, shift-transition flag
- Definitions follow Bauer et al. (2020) German perioperative glossary

### 2.3 Progressive stratification

Same five-level ladder (L0–L4). Frame it as a diagnostic tool for metric validity: "At each level, we ask whether the between-site ranking changes, and how much of the spread is attributable to the structural confounder removed at that step."

### 2.4 Room-level decomposition

Same method. Frame the room-level spread as a measure of within-site equity of overtime exposure.

### 2.5 FCOTS and duration-estimation analyses

Same methods. Frame as testing whether commonly recommended quality levers explain residual gaps.

---

## 3. Results (~1,200 words)

### 3.1 Stratification collapses the between-site spread

- L0: 16.8x → L4: ~3-4x
- Four-fifths structural
- Table 2: Campus-level metrics at L0

### 3.2 Room-level variation exceeds between-site variation

- Maaseik: 44.5x room spread (MO03 8.9% vs MK11 0.2%)
- Lanaken: 17x (LO03 1.7% vs LP01 0.1%)
- Genk: GO10 at 32.9%, some rooms at 0%
- Frame as unequal patient exposure to overtime-related risks

### 3.3 FCOTS does not predict stratified overtime

- Genk worst FCOTS, worst overtime — but confounded by structure
- Cathlab similar FCOTS to Maaseik, double the overtime
- Pandit et al. (2012) found R² = 0.04-0.08 between start and finish times; our data confirm this across sites

### 3.4 Duration estimation is similar across sites

- Table 3: CV by planned-duration bucket
- Middle buckets (31-180 min) show comparable CVs
- Not the differentiator

### 3.5 Cascading as the dominant mechanism

- Genk: 5% of cases displaced to later shift (mean delay +352 min)
- Cascade waste ~4x duration-overrun waste
- Frame: these displaced cases are the ones crossing shift handover boundaries

---

## 4. Discussion (~1,000 words)

### 4.1 Measurement validity: why this is a quality problem

Standard OR metrics fail the basic validity test for cross-site comparison. A metric that conflates structure with performance does not measure what it claims to measure. When hospitals act on invalid metrics, the consequences are real: misallocated improvement resources, pressure on staff to meet structural benchmarks, and neglect of the room-level variation where actionable quality gaps actually live.

Zhang and Pandit (2023, 2024) raised this concern for NHS metrics. Our data provide the first systematic quantification: four-fifths of the raw between-site spread is structural artifact.

### 4.2 Room-level variation as a safety equity issue

Patients in high-overtime rooms face systematically different conditions: more fatigued staff, more shift-boundary transitions, more time pressure. This is not random variation — it reflects scheduling, block allocation, and case-sequencing decisions that are under local management control. Addressing room-level variation is both a quality improvement and a safety improvement.

### 4.3 Implications for quality leaders

1. Multi-site OR benchmarks should report stratified results, not raw numbers
2. Room-level performance reporting should be standard practice — it identifies where patients face unequal overtime exposure
3. FCOTS should not be treated as a headline quality indicator for cross-site comparison
4. Cascading delays, not individual case overruns, are the dominant driver of cases crossing shift boundaries

### 4.4 Limitations

- Single network (shared governance is an advantage but limits generalizability)
- No patient-level acuity (ASA) data
- No direct safety outcome data (errors, complications) — we measure exposure to overtime-related risks, not the outcomes themselves
- Case-level overtime definition may overstate room-day frequency
- COVID-19 tail effects in 2022

---

## 5. Conclusion (~200 words)

Operating-room performance metrics are treated as quality indicators, but their validity for cross-site comparison has not been established. In this 228,623-case study across four structurally different sites sharing a single governance structure, progressive stratification showed that four-fifths of the raw between-site performance spread was attributable to operating-model design, not operational quality. Within-site room-level variation — which directly determines patient exposure to overtime-related risks — was larger than between-site variation at half the campuses studied.

These findings suggest that quality leaders should treat unadjusted OR benchmarks with the same skepticism they would apply to unadjusted clinical outcome comparisons. Stratified reporting and room-level analysis offer a more valid basis for identifying where quality improvement resources will have the greatest impact on patient care.

---

## References (~20 references)

Core OR literature (verified): Macario 2006, Dexter et al. 2004, Dexter & Epstein 2009, Pandit et al. 2012, Ernst et al. 2012, Korzhenevich & Zander 2024, Schouten et al. 2023, Bauer et al. 2020, Strum et al. 2000, Eijkemans et al. 2010, Wachtel & Dexter 2009

Quality/safety additions (to verify): Landrigan et al. 2004 (NEJM, work hours and errors), Nagpal et al. 2010 (Annals of Surgery, handovers), WHO 2007 (handover guidelines), Zhang & Pandit 2023 (BJA, NHS metrics), Zhang Dunstan & Pandit 2024 (capped utilisation)

BMJ QS precedents: Abdelfattah et al. 2020 (workflow disruptions), Joseph et al. 2019 (flow disruption escalation)

---

## Figures and Tables

- **Table 1:** Cross-campus structural summary (cases, rooms, ambulatory %, elective %, mean planned duration, weekend activity)
- **Table 2:** Campus-level performance metrics at L0 (overtime %, mean OT minutes, median, P95, room swap %, gap time)
- **Table 3:** CV of observed duration by planned-duration bucket and campus
- **Figure 1:** Progressive stratification — overtime rate by site at each level (line chart or waterfall)
- **Figure 2:** Room-level overtime rates within each campus (dot plot or bar chart)
