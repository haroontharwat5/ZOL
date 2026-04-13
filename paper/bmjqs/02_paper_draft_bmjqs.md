# Do operating-room performance comparisons measure quality or structure? A 228,623-case natural experiment

**Haroon Tharwat, Maxim Riebus, Ben [TBD], Dieter [TBD], Niels Martin**

Hasselt University, Faculty of Business Economics, Research Group Business Informatics

---

## Abstract

**Objective:** To test whether standard operating-room performance metrics produce valid comparisons across structurally different sites, and to quantify the share of between-site variation that reflects operating-model design rather than operational quality.

**Design:** Retrospective observational study using progressive stratification. We filtered administrative OR data through four sequential adjustment layers (weekday activity, day-shift hours, elective urgency, admission type) and measured the between-site performance spread at each level.

**Setting:** Four sites of a single Belgian hospital network (Ziekenhuis Oost-Limburg), sharing governance, electronic health records, and labour agreements but running structurally different OR models: a 24/7 tertiary centre (Genk), a weekday-only ambulatory facility (Lanaken), a hybrid campus (Maaseik), and a specialised cardiac catheterisation lab (Cathlab).

**Participants:** 228,623 surgical and interventional procedures, January 2022 to May 2025.

**Main outcome measures:** After-hours rate (cases extending past shift end), room-level overtime spread within each campus, concordance between first-case-on-time start rankings and stratified overtime rankings, duration-estimation coefficient of variation by planned-duration bucket.

**Results:** Raw after-hours rates differed 16.8-fold across sites (0.5% to 8.4%). After full stratification the spread fell to 3- to 4-fold; roughly four-fifths of the raw gap reflected operating-model structure rather than operational performance. Within-site room-level variation exceeded between-site variation at two of four campuses, with a 44.5-fold spread between the best and worst rooms at one campus. First-case punctuality did not predict stratified overtime.

**Conclusions:** Standard OR metrics conflate structural design with operational quality. Cross-site comparisons based on unadjusted metrics risk misdirecting improvement resources. Stratified, room-level reporting offers a more valid basis for identifying actionable quality gaps.

---

## 1. Introduction

Hospital boards and regulators compare operating-room performance across sites using overtime rates, utilisation figures, and first-case-on-time start percentages. These numbers inform resource allocation, staffing decisions, and quality improvement priorities. When they mislead, the decisions they drive can be counterproductive: improvement resources directed at problems that are structural rather than operational, staff held accountable for targets shaped by factors outside their control, and patients affected when schedules are cut or reorganised based on flawed comparisons.

The validity of these metrics for cross-site use has received surprisingly little scrutiny. Zhang and Pandit showed that NHS Model Hospital calculations selectively report subsets of operating lists, producing averages that distort site-level performance.(1) Schouten et al. identified 47 distinct OR metrics in the published literature with inconsistent definitions and no studies examining interactions between them.(2) The most widely used frameworks — Macario's eight-indicator scorecard(3) and Dexter's overutilisation-underutilisation cost model(4) — were developed for within-site decision-making. Whether they remain valid as between-site discriminators has not been systematically tested.

This gap matters beyond operational efficiency. OR overtime is associated with staff fatigue, a known risk factor for medical error.(5) Cases displaced past shift boundaries create handover transitions during or shortly after surgery, and handovers are among the most error-prone moments in perioperative care.(6) When benchmarks misidentify the source of overtime, improvement efforts target the wrong lever. Meanwhile, within-site variation at the room level — which directly determines whether a given patient's case runs into fatigued staff or a shift transition — can go unrecognised.

We studied 228,623 procedures across four sites of a single Belgian hospital network. The sites share governance, information systems, and labour agreements but operate structurally different OR models. This shared infrastructure creates a natural experiment: between-site differences in performance metrics cannot be attributed to management culture, IT quality, or contract terms. They reflect either the operating model or genuine operational differences. Our aim was to determine how much of the raw performance spread survives progressive stratification, whether room-level variation within a site exceeds variation between sites, and whether the standard levers recommended in the literature — first-case punctuality and duration-prediction accuracy — explain the residual gaps.

---

## 2. Methods

### 2.1 Setting

Ziekenhuis Oost-Limburg (ZOL) is a public hospital network in Limburg, Belgium, with three physical campuses and a cardiac catheterisation lab housed within the largest campus. All sites share a single electronic health record, unified governance, identical labour agreements, and a common clinical staff pool.

**Genk** is the largest site: 26 rooms, 96,044 cases, a mix of inpatient (57.7%) and ambulatory (42.3%) work, 14.6% non-elective activity, and 24/7 emergency access. **Lanaken** operates seven rooms on weekdays only, handling almost exclusively ambulatory day surgery (98.1% DAG, 99.6% elective) with a mean planned duration of 30 minutes. Two rooms (LP01, LP02) function as a paired-room flex system, swapping cases bidirectionally in real time. **Maaseik** has eight rooms split into two blocks: short ambulatory procedures in the MK rooms and longer inpatient work in the MO rooms. **Cathlab** performs cardiac catheterisation procedures across seven rooms; despite a 97.5% elective profile, 88.6% of its patients are admitted as inpatients because cardiac procedures typically require overnight observation. We note that our own internal analysis report for the Cathlab contained a labelling error, describing this 88.6% as "ambulatory" when the underlying data showed it was inpatient. We corrected this for the present study.

### 2.2 Data

The dataset covers all procedures recorded between January 2022 and May 2025 (41 months). After quality filtering — removing zero-duration cases, implausible timestamps, endoscopy-room procedures, and Cathlab cases without an anaesthesiologist — 228,623 cases remained. Variables include anonymised patient and staff identifiers, planned and actual timestamps, room assignments, admission type (ambulatory/inpatient/emergency), and urgency classification (elective or non-elective, defined as booked within 24 hours).

### 2.3 Variables

We derived performance variables from the raw timestamps following the German perioperative glossary.(7) Each case was assigned a shift label based on actual start time: day (07:00–16:29), evening (16:30–21:59), or night (22:00–06:59). Start difference was computed as actual minus planned start time in minutes. An overtime flag was set when actual end time exceeded the shift boundary, with overtime minutes recording the excess. Gap time measured the interval between consecutive cases in the same room. Duration deviation recorded actual minus planned duration. A shift-transition flag identified cases performed in a different shift window than planned.

### 2.4 Progressive stratification

The analytic core is a sequential filtering approach applied in five levels:

- **L0 (raw):** All 228,623 cases.
- **L1 (weekday):** Monday through Friday only. Removes the weekend effect (Lanaken has no weekend activity; Genk has 4%).
- **L2 (day shift):** Cases starting between 07:00 and 16:29 on weekdays. Removes evening and night activity.
- **L3 (elective):** Elective cases at L2. Removes the non-elective volume (0.4% at Lanaken, 14.6% at Genk).
- **L4 (admission split):** L3 separated into ambulatory (DAG) and inpatient (HOS) subgroups.

At each level we recalculated overtime rates and the between-site spread ratio.

### 2.5 Room-level decomposition

For each room with at least 100 cases, we computed the room-specific overtime rate and the ratio of the highest to lowest rate within each campus. This within-site spread is directly comparable to the between-site spread from the stratification ladder.

### 2.6 First-case and duration analyses

First-case-on-time start was computed for the first case of each room-day. Duration-estimation precision was assessed via the coefficient of variation (CV) of observed duration within five planned-duration buckets (<30, 31–60, 61–90, 91–180, >180 minutes), separately by campus.

This study follows the STROBE guideline for observational research.

---

## 3. Results

### 3.1 The between-site spread collapses under stratification

At L0, after-hours rates range from 0.5% at Lanaken to 8.4% at Genk, a 16.8-fold spread. Maaseik sits at 2.8% and the Cathlab at 5.8%. A naive reading of these numbers places Lanaken as the best performer and Genk as the worst.

This ranking conflates at least four structural differences. Lanaken has no weekend activity; Genk operates seven days a week. Lanaken has almost no evening or night cases; Genk's 24/7 mandate generates them by design. Only 0.4% of Lanaken's volume is non-elective; Genk's non-elective share is 14.6%. And 98.1% of Lanaken's cases are ambulatory, compared with 42.3% at Genk.

At L1 (weekday only), the spread narrows modestly. At L2 (day shift), it compresses further as evening and night activity is removed. At L3 (elective, day shift, weekday), the between-site spread falls to roughly 4- to 5-fold. At L4, splitting by admission type, the residual gap is approximately 3- to 4-fold. Each layer removes one structural confounder; each removal narrows the spread. Roughly four-fifths of the L0 gap is attributable to operating-model design rather than operational quality.

**Table 1.** Campus-level characteristics and performance (L0, all cases).

| | Genk | Cathlab | Maaseik | Lanaken |
|---|---|---|---|---|
| Cases | 96,044 | 9,282 | 53,902 | 69,395 |
| Operating rooms | 26 | 7 | 8 | 7 |
| Ambulatory (%) | 42.3 | 11.3 | 83.9 | 98.1 |
| Elective (%) | 85.4 | 97.5 | 94.3 | 99.6 |
| Mean planned duration (min) | 94 | 94 | 40 | 30 |
| After-hours rate (%) | 8.4 | 5.8 | 2.8 | 0.5 |
| Mean overtime (min) | 59.0 | 41.8 | 42.0 | 15.7 |
| P95 overtime (min) | 193.8 | 108.3 | 129.0 | 48.5 |
| Room swap (%) | 1.1 | 1.2 | 0.8 | 7.5 |
| Median gap time (min) | 7 | 4 | 2 | 0 |

### 3.2 Within-site room-level variation exceeds between-site variation

Maaseik's aggregate overtime rate of 2.8% conceals a 44.5-fold spread at the room level. Room MO03 runs overtime in 8.9% of cases; room MK11 in 0.2%. This internal gap is 2.6 times larger than the 16.8-fold raw gap between the best and worst campus.

The pattern holds at every site. At Lanaken, room-level rates range from 0.1% (LP01 and LP02, the paired-flex rooms) to 1.7% (LO03), a 17-fold spread. At Genk, room GO10 has an overtime rate of 32.9% while several rooms sit near 0%. At the Cathlab, the range is 4.5% to 17.6%, a roughly fourfold spread within a single specialised unit.

Patients assigned to high-overtime rooms face systematically different conditions from those in low-overtime rooms within the same hospital: greater exposure to fatigued staff near shift end, higher probability that their case spans a shift transition, and more time pressure on the surgical team. This variation is not random. It reflects which procedures are assigned to which rooms, how blocks are allocated, and how cases are sequenced through the day — all factors under local management control.

### 3.3 First-case punctuality does not predict stratified overtime

At Genk, 68.2% of first cases started late, with a mean net delay of 25.1 minutes. At Lanaken, 57% started late, with a net delay of 3.8 minutes. Maaseik fell between them (65.3% late, 16.0 min net delay). The Cathlab had 58.3% late starts and a 17.2-minute net delay.

On raw punctuality, the ranking mirrors the overtime ranking. But this match is driven by the same structural confounders: Lanaken's first cases are short ambulatory procedures with simple setups; Genk's are complex inpatient operations requiring longer preparation. The Cathlab's net delay (17.2 min) is close to Maaseik's (16.0 min), yet its overtime rate (5.8%) is more than double Maaseik's (2.8%). If first-case punctuality were the primary driver, these two sites should have similar overtime profiles. They do not.

Pandit et al. found that start times and finish times were poorly correlated across 7,000 theatre lists (R² = 0.04–0.08), concluding that "starting on time" is a weak surrogate for overall efficiency.(8) Our cross-site data support this conclusion. First-case punctuality tracks raw overtime because both correlate with operating-model complexity. It adds no independent explanatory power once the operating model is accounted for.

### 3.4 Duration estimation is similar across sites

**Table 2.** Coefficient of variation of observed duration by planned-duration bucket.

| Planned duration | Genk | Lanaken | Maaseik | Cathlab |
|---|---|---|---|---|
| <30 min | 0.61 | 0.52 | 1.03 | 0.61 |
| 31–60 min | 0.16 | 0.39 | 0.47 | 0.43 |
| 61–90 min | 0.36 | 0.34 | 0.36 | 0.39 |
| 91–180 min | 0.20 | 0.32 | 0.35 | 0.35 |
| >180 min | 0.42 | 0.69 | 0.37 | 0.59 |

For the three middle buckets that contain the bulk of surgical volume (31–180 min), CVs are comparable across campuses. No site is consistently more or less accurate. The scheduling teams share the same EHR and historical data, and this similarity in estimation quality is consistent with that shared infrastructure. Duration-estimation differences do not explain the between-site overtime gaps.

### 3.5 Cascading delays dominate duration overruns

At Genk, 5.0% of cases (4,786 procedures) were displaced into a later shift window than planned, with a mean start delay of +352 minutes. These displaced cases — the ones most likely to cross a shift handover boundary — are generated primarily by delays accumulating through the day rather than by individual procedures running long. Start-time cascading accounted for roughly four times more displaced OR time than duration overruns alone. At Lanaken, by contrast, only 0.8% of cases shifted windows, and the direction was reversed: cases were pulled forward into empty slots (mean delay −143 minutes), consistent with a high-throughput ambulatory model that absorbs slack rather than generating cascades.

---

## 4. Discussion

### 4.1 OR benchmarks as a measurement validity problem

The central finding of this study is not a performance number. It is a measurement problem. Raw overtime rates, the most commonly tracked OR efficiency indicator, produced a 16.8-fold spread across four sites of a single network. Progressive stratification reduced that spread to 3- to 4-fold. Four-fifths of the headline number reflected operating-model structure — weekend coverage, shift patterns, urgency mix, admission type — not operational quality.

This result has direct consequences for how OR performance data are used. When a hospital board sees a 16.8-fold gap, the natural response is to investigate the worst-performing site. Resources move toward closing that gap. Staff face pressure to improve their numbers. But if four-fifths of the gap is structural, four-fifths of that effort is directed at a target that cannot be moved without redesigning the site's mission. The improvement resources are not merely wasted; they are unavailable for the room-level quality gaps where intervention would actually change patient experience.

Zhang and Pandit raised a parallel concern for NHS theatre metrics, showing that selective reporting of operating-list subsets produces misleading averages.(1) Zhang, Dunstan, and Pandit extended this to the 85% "capped utilisation" target, arguing that it penalises certain hospitals unfairly.(9) Our findings complement theirs: even when metrics are calculated correctly, they fail as between-site discriminators if the sites differ in structural design. The problem is not arithmetic. It is validity.

### 4.2 Room-level variation and equity of patient exposure

The room-level decomposition reframes the improvement agenda. At Maaseik, the gap between MO03 (8.9% overtime) and MK11 (0.2%) is 44.5-fold — nearly triple the raw between-site spread. This variation sits within a single campus, under a single management team, using shared staff and scheduling systems. It is addressable.

It is also a quality concern. A patient whose procedure is scheduled in MO03 faces a meaningfully different probability of encountering overtime conditions — later finishes, staff working past their shift, compressed post-operative transitions — than a patient scheduled in MK11 on the same day. Whether this translates into different complication rates is beyond the scope of our data. But the differential exposure is real, and it arises from scheduling decisions rather than patient characteristics.

### 4.3 Rethinking standard efficiency levers

Two findings challenge common assumptions. First, first-case-on-time start did not rank sites in the same order as stratified overtime, and the Cathlab demonstrated that similar first-case punctuality can coexist with very different overtime rates. Pandit et al. reached a similar conclusion from different data.(8) FCOTS remains useful as a within-room daily management tool. It should not be treated as a quality indicator for cross-site comparison.

Second, duration-estimation precision was comparable across sites once cases were grouped by planned duration. The between-site overtime gap is not caused by one campus predicting surgical times less accurately than another. The dominant mechanism is cascading: delays accumulating through the day, each one compressing the window for subsequent cases and increasing the probability that the final case spills past the shift boundary. Process flow through the room-day, not the accuracy of any single time estimate, is the operative lever.

### 4.4 Implications for quality leaders

These results point to four changes in how OR performance data are used.

First, cross-site comparisons should report results at multiple stratification levels. An unadjusted number invites misinterpretation. At minimum, reports should separate elective from non-elective, ambulatory from inpatient, and day-shift from after-hours activity before comparing sites.

Second, room-level performance reports should become standard. They identify where patients face unequal overtime exposure and where scheduling interventions will yield the greatest return. Campus-level averages obscure both.

Third, FCOTS should be tracked as one indicator among many, not as a headline metric that drives resource allocation for cross-site quality improvement.

Fourth, cascading-delay analysis should complement or replace FCOTS as a diagnostic for overtime risk, since cascading is the dominant mechanism and it operates at the room-day level where managers can actually intervene.

### 4.5 Limitations

This is a single-network study. The shared governance structure is an analytic strength but limits generalisability. We lack patient-level acuity scores (ASA classification) and cannot adjust for patient complexity beyond procedure type and admission type. The stratification ladder is descriptive, not causal; it reveals how much of the spread is structural but does not identify the mechanisms by which operating-model design translates into overtime. We do not have safety outcome data (errors, adverse events) and therefore measure exposure to overtime-related conditions rather than the outcomes themselves. The study period includes the tail end of COVID-19 disruptions, though exploratory checks suggested that the main findings hold when 2022 is excluded.

---

## 5. Conclusion

Operating-room performance metrics are treated as quality indicators, but their validity for cross-site comparison has not been tested. In 228,623 cases across four structurally different sites sharing a single governance structure, progressive stratification showed that four-fifths of the raw 16.8-fold between-site performance spread was attributable to operating-model design, not operational quality. Within-site room-level variation was larger than between-site variation at half the campuses, creating unequal patient exposure to overtime-related conditions based on room assignment rather than clinical need.

Quality leaders should treat unadjusted OR benchmarks with the same scepticism they apply to unadjusted clinical outcome comparisons. Stratified reporting and room-level analysis provide a more valid foundation for directing improvement resources where they will make the most difference for patients.

---

## References

1. Zhang C, Pandit JJ. Getting operating theatre metrics right to underpin quality improvement: understanding limitations of NHS Model Hospital calculations. *Br J Anaesth* 2023;131:130–4.
2. Schouten AM, Flipse SM, van Nieuwenhuizen KE, et al. Operating room performance optimization metrics: a systematic review. *J Med Syst* 2023;47:19.
3. Macario A. Are your hospital operating rooms "efficient"? A scoring system with eight performance indicators. *Anesthesiology* 2006;105:237–40.
4. Dexter F, Abouleish AE, Epstein RH, et al. Use of operating room information system data to predict the impact of reducing turnover times on staffing costs. *Anesth Analg* 2004;97:1119–26.
5. Landrigan CP, Rothschild JM, Cronin JW, et al. Effect of reducing interns' work hours on serious medical errors in intensive care units. *N Engl J Med* 2004;351:1838–48.
6. Nagpal K, Vats A, Ahmed K, et al. An evaluation of information transfer through the continuum of surgical care: a feasibility study. *Ann Surg* 2010;252:402–7.
7. Bauer M, Diemer M, Merkel M, et al. Glossary of perioperative process times and indicators. *Anaesthesist* 2020;69(Suppl 1):S5–17.
8. Pandit JJ, Abbott T, Pandit M, et al. Is "starting on time" useful (or useless) as a surrogate measure for "surgical theatre efficiency"? *Anaesthesia* 2012;67:823–32.
9. Zhang C, Dunstan C, Pandit JJ. A tutorial on 'capped utilisation' as a metric and key performance target in NHS England's Model Hospital operating theatres database. *Anesthesiol Perioper Sci* 2024. doi:10.1007/s44254-024-00073-3.
10. Ernst C, Szczesny A, Soderstrom N, et al. Success of commonly used operating room management tools in reducing tardiness of first case of the day starts. *Anesth Analg* 2012;115:671–7.
11. Korzhenevich G, Zander A. Leveraging the potential of the German operating room benchmarking initiative for planning: a ready-to-use surgical process data set. *Health Care Manag Sci* 2024;27:328–51.
12. Dexter F, Epstein RH. Typical savings from each minute reduction in tardy first case of the day starts. *Anesth Analg* 2009;108:1262–7.
13. Eijkemans MJ, van Houdenhoven M, Nguyen T, et al. Predicting the unpredictable: a new prediction model for operating room times. *Anesthesiology* 2010;112:41–9.
14. Strum DP, May JH, Vargas LG. Modeling the uncertainty of surgical procedure times. *Anesthesiology* 2000;92:1160–7.
15. Wachtel RE, Dexter F. Tactical increases in operating room block time for capacity planning should not be based on utilization. *Anesth Analg* 2009;108:1215–20.
16. Abdelfattah E, et al. Associations of workflow disruptions in the operating room with surgical outcomes: a systematic review. *BMJ Qual Saf* 2020;29:1009–17.
17. Joseph A, et al. Minor flow disruptions, traffic-related factors and their effect on major flow disruptions in the operating room. *BMJ Qual Saf* 2019;28:276–83.
18. Merlo J, Chaix B, Ohlsson H, et al. A brief conceptual tutorial of multilevel analysis in social epidemiology. *J Epidemiol Community Health* 2006;60:290–7.
