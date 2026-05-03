# Detailed skeleton with figure assignments

**Working title:** Where does operating-room overtime come from, and who pays for it? A 96,044-case analysis of one tertiary centre

**Target:** BMJ Quality & Safety, Original Research, ~3,500 words body, STROBE, Vancouver numbered superscript, max 5 main figures/tables.

**How to use this document:** Each bullet below is written as a paragraph seed. Expanding it into prose should require only connecting sentences, not new research. Figures and tables are assigned in-line where they appear. References use the numbering from the full reference list at the end.

---

## Structured abstract (~250 words)

- **Objective.** Characterise where operating-room overtime originates within a high-volume tertiary hospital and connect the operational pattern to published evidence on staff and patient harms.
- **Design.** Retrospective observational study of administrative OR data.
- **Setting.** Campus Genk of the Ziekenhuis Oost-Limburg network, Belgium. A 24/7 tertiary hospital running 25 operating rooms across general, cardiac, and endoscopy blocks.
- **Participants.** 96,044 surgical and interventional procedures, January 2022 to May 2025.
- **Main outcome measures.** Case-level overtime flag and overtime minutes (time past the end of the case's assigned shift), by room, weekday, shift, and urgency. Shift-transition displacement, start-time deviation, and duration-estimation accuracy as candidate mechanisms.
- **Results (headline numbers).** 8,024 cases (8.4%) ran past the end of their assigned shift, mean overtime 59 min (among overtime cases), P95 194 min. Overtime was concentrated in a small number of rooms: GO10 ran overtime on 32.9% of its cases (mean 154 min), while three rooms had zero overtime. 4,786 cases (5%) were displaced into a different shift than planned, with a mean start delay of 352 min and a mean duration 22 min shorter than planned, indicating upstream cascading rather than individual overruns. Urgent-elective overlap occurred on 69.7% of observation days and added roughly 30 min to elective start times. First-case punctuality did not predict room-level overtime.
- **Conclusions.** Overtime at this centre was concentrated, cascading, and driven by mid-day displacement. Room-level and cascading-focused metrics offer a more actionable target for quality improvement than utilisation or first-case punctuality.

---

## 1. Introduction (~600 words)

### 1.1 The bigger picture (100 words)

- ZOL is running a multi-phase OR-efficiency programme: Phase 1 = retrospective characterisation of scheduled-versus-observed performance; Phase 2 = link operational patterns to patient outcomes; Phase 3 = predictive scheduling. This paper sits in Phase 1 and points forward to Phase 2.
- The clinical leadership framed the project question as linking the area under the curve of surgical activity past the day-shift staffing window to measurable consequences for patients and staff.
- 96,044 cases across 3.5 years provide the dataset for Phase 1.

### 1.2 Why overtime specifically (250 words)

- Overtime is the binding economic cost in OR operations, weighted 1.5-2× the cost of idle time [1a,2].
- **Staff harm.** Overtime and long shifts are associated with poorer perceived care quality and higher patient-safety risk in a 12-country European nurse workforce study [3]. The companion study found that 12-hour shifts were associated with burnout and intent to leave [4]. The most recent direct evidence links mandatory overtime to intent to leave in a 2024 cross-sectional study of 264 South Korean nurses [5]. Both long shifts and overtime are associated with worse performance and wellbeing [23]; high workload and low decision latitude are established burnout predictors [24].
- **Patient harm.** After-hours surgery carries elevated mortality in a 2020 meta-analysis (adjusted OR 1.16, 95% CI 1.06-1.28, low-certainty evidence) [6], recently replicated in a 281,717-patient propensity-matched South Korean cohort, although the effect size (OR 3.58) has been challenged on residual-confounding grounds [7,26]. Each intraoperative anaesthesia handover raises the odds of a major composite complication [8]. A 2025 UK national safety investigation (citing an MDU member survey of 481 doctors) named staff fatigue as a direct patient-safety problem [9]. Overtime hours above a breakpoint threshold were associated with a 2.09% increase in pressure ulcers across 70 US hospitals [10].
- Staff fatigue and handover transitions are the mechanisms that turn operational overtime into a clinical-safety problem.

### 1.3 The staffing-pyramid context (100 words)

- At Campus Genk, 25 theatres run 08:00-16:30 (day shift). Staffing drops to 8 rooms during 16:30-17:30, then 4 rooms during 17:30-22:00, and a single overnight room with 3 on-call nurses.
- A case spilling past 16:30 is not merely late; it is competing for one of a sharply diminishing set of staffed rooms, covered by different staff than those who started the day.
- The staffing change at the shift boundary is what gives overtime its operational meaning at this site, rather than an arbitrary clock cut-off.

> **Figure 1 (MAIN slot 1) — Staffing pyramid.** Step diagram showing the four staffing tiers: 25 rooms 08:00-16:30 → 8 rooms 16:30-17:30 → 4 rooms 17:30-22:00 → 1 room overnight. Reproduced from the hospital kickoff with permission. Anchors the entire framing.

### 1.4 Research questions (80 words)

- RQ1: How is overtime distributed across rooms and time within one tertiary centre?
- RQ2: Which mechanism (late starts, individual case overruns, or mid-day cascading) accounts for most of the overtime minutes?
- RQ3: How do urgent cases interact with the elective programme to produce spillover into staffed-down hours?

**References for §1:** [1a] Dexter/Macario/Traub 1999, [2] Dexter/Macario 2002, [3] Griffiths 2014, [4] Dall'Ora 2015, [5] Bae 2024, [6] Cortegiani 2020, [7] Oh 2025, [8] Saager 2014, [9] HSSIB 2025, [10] Pittman 2025, [23] Dall'Ora 2016, [24] Dall'Ora 2020, [26] Sakurai 2025.

---

## 2. Methods (~700 words)

### 2.1 Setting (100 words)

- Campus Genk, ZOL network, Belgium. Tertiary, >50,000 procedures/year.
- 18 surgical theatres, 7 interventional theatres, ambulatory anaesthesia unit (endoscopy, IVF/MKA sedation).
- 90+ anaesthesiologists (including trainees, fellows). All surgery except congenital cardiac and transplant.
- Staffing: 2-3 nurses per OR during day shift, dropping per the pyramid in §1.3. Weekends and bank holidays covered by back-up nurse rotation.

### 2.2 Data and inclusion (150 words)

- Administrative OR data, 1 January 2022 - 31 May 2025. 96,044 cases at Genk.
- 71,621 unique patients, 225 surgeons, 211 anaesthesiologists, 26 distinct actual ORs, 1,327 distinct procedure names.
- Admission mix: 51.0% ambulatory (DAG), 48.9% inpatient (HOS), 0.1% emergency (SPOED).
- Time-stamp reliability disclosure: the hospital clinical team confirmed that room-in and room-out are the only reliable data points in the registration pipeline. All timing analyses use room-in and room-out only; induction, recovery, and ward-transfer marks are recorded but not used.
- STROBE flow diagram if requested by reviewers.

### 2.3 Variables (80 words)

- Per Bauer et al. (2020) glossary [11]: planned duration, observed duration, planning deviation, scheduled start, actual start, start-time deviation, room-out time, overtime flag (room-out > assigned shift end), overtime minutes, planned room vs actual room (room-swap flag), urgency at planning (elective vs niet-electief), shift label (day 08:00-16:30; evening 16:30-22:00; night 22:00-08:00).
- Metric choice justified by the heterogeneity of OR performance metrics documented in a recent systematic review [12] and the argument that aggregate utilisation hides room-level reality [13].

### 2.4 Overtime definition (100 words)

- Each case was assigned to one of three shift buckets based on its actual room-in time: day (08:00-16:30), evening (16:30-22:00), or night (22:00-08:00). A case was flagged as after-hours if its room-out time fell after the end of its assigned shift. Overtime minutes equal the difference between room-out and shift end, floored at zero. A day-shift case ending at 17:00 has 30 minutes of overtime; an evening-shift case ending at 23:00 has 60 minutes; a night-shift case ending at 09:00 has 60 minutes. Cases finishing within their assigned shift have zero overtime, irrespective of which shift that is.
- Chosen because the staffing change at each shift boundary is the operational event that gives overtime its meaning at this site. Aligns with Bauer 2020 §3.4 [11] and the hospital's own "area under the curve" framing.

### 2.5 Overlap definition (80 words)

- An urgent case was deemed to overlap with an elective case when the urgent case's actual room matched the elective case's planned room and the urgent case's actual time interval (room-in to room-out) overlapped with the elective case's planned time interval (planned start to planned end). The day-level overlap metric counts the number of distinct calendar days on which at least one such overlap occurred. The case-level metric counts whether a given elective case's planned slot was overlapped by an urgent case in the same room.

### 2.6 Analyses (200 words)

- Descriptive throughout. No causal inferential modelling. Three analysis blocks:
- **Block 1 — Burden and concentration.** Case-level overtime rate, mean, median, P95. Distribution by room, weekday, year, shift. Room-level concentration is the primary analytic focus.
- **Block 2 — Mechanism.** Start-time deviation per case and per room. Duration-deviation by planned-duration bucket via coefficient of variation [14,15]. Shift displacement: cases performed in a different shift than originally planned, with mean start delay and mean planning deviation.
- **Block 3 — Daily disruptors.** Urgency mix and timing. Urgent-elective overlap in the same OR (per day, per room, per month). Effect of overlap on elective start delay.
- **Non-mechanism checks (text only).** Room swaps (1.1%) and idle time between cases (median 7 min) are reported as non-bottlenecks.

### 2.7 Ethics (30 words)

- Institutional approval. Fully de-identified administrative data. No patient interaction.

### 2.8 Software (30 words)

- Python / R. Versions specified on submission.

**References for §2:** [11] Bauer 2020, [12] Schouten 2023, [13] Zhang/Dunstan/Pandit 2024, [14] Strum 2000, [15] Eijkemans 2010.

---

## 3. Results (~1,000 words)

### 3.1 Sample and setting overview (80 words, no figure)

- 96,044 cases, 71,621 unique patients, 225 surgeons, 211 anaesthesiologists, 26 ORs, 1,327 procedure names.
- Weekday volume evenly distributed 18.7-20.9% Mon-Fri; weekends 1.5-1.7%.
- Year-on-year volume growth: 26,103 (2022) → 28,522 (2023) → 29,223 (2024) → 12,196 (2025 partial).
- Urgency mix: 87.5% elective, 12.5% non-elective.

### 3.2 Planning vs reality — context (150 words)

- 45.2% of cases run longer than planned, 54.8% shorter. Mean overrun 21 min (median 13); mean underrun 19.7 min (median 11). The planning system is roughly unbiased on average; the dispersion is the problem.
- Coefficient of variation by planned-duration bucket: <30 min CV 0.61, 31-60 min CV 0.46, 61-90 min CV 0.36, 91-180 min CV 0.35, >180 min CV 0.42. Planning-deviation CV follows the same pattern but more extreme: >180 min bucket has CV 1.86.
- Mid-length cases (61-180 min) are most predictable. Very long cases carry the largest planning noise. This matters because the same complex-cardiac and oncology procedures that drive planning variability are concentrated in the rooms with the most overtime.
- Weekend relative deviation is 23.1% (Saturday) and 23.4% (Sunday) vs 2.0-4.8% on weekdays. One sentence.
- Top deviation procedures: DEBULKING MET HIPEC (74.4 min), AVR (73.7), CABG OFF PUMP (60.4). These are the complex cardiac and oncology procedures concentrated in GO10.

> **Supplementary Table S1 — CV by planned-duration bucket.** Five rows, three columns (n, CV observed, CV planning deviation). Compact and analytically interesting, but not headline. APPENDIX.

### 3.3 Overtime: how often, where, when, how heavy (300 words)

**Headline numbers:**
- 96,044 cases, 8,024 ran past the end of their assigned shift (8.4%). Mean overtime 59 min (among overtime cases); median 38 min; P95 193.8 min.

**Weekday pattern:**
- Mon-Fri: 7.8-8.5% (Mon 8.0, Tue 8.2, Wed 8.5, Thu 7.8, Fri 8.0).
- Saturday 16.8%, Sunday 15.5%. Weekend rate roughly twice the weekday rate. Weekend volume is almost entirely non-elective.

**Year trend:**
- 2022 8.8% → 2023 8.6% → 2024 8.2% → 2025 (partial) 7.2%. Slow improvement, not a step change.

**End-time distribution:**
- Sharp peak immediately after 16:30 (~3,000 cases ending 16:30-17:30), rapid decay through 17:30-20:00, long thin tail past 22:00. Most overtime cases land in the window where staffing has just dropped from 25 to 8 rooms.

**Room-level concentration (the headline finding):**
- GO10: 32.9% overtime, mean 154 min, P95 327 min. One in every three cases runs into after-hours. GO10 handles complex cardiac surgery (CABG, aortic valve replacement, mitral valve repair, MIDCAB, mini-maze ablation).
- Tier 2 (GO08-GO13): 11-16%.
- Near-zero rooms: GEG1 0% (n=4,498), GSE1 0% (n=2,261), GEX1 0.3%.
- The within-campus spread (0-32.9%) exceeds the between-campus spread across the entire ZOL network (Lanaken 0.5%, Maaseik 2.8%, Cathlab 5.8%, Genk 8.4%).

> **Figure 2 (MAIN slot 2) — Room-level overtime concentration.** Horizontal bar chart, one bar per OR, ordered descending by overtime rate. GO10 at top (32.9%), descending to GEG1/GSE1 (0%). Secondary panel or annotation showing mean overtime minutes. Caption includes headline numbers (8.4%, mean 59 min, median 38 min, P95 194 min). Source: In-Depth Table 25 (pp.30-31).

> **Table 1 (MAIN slot 3) — Overtime summary by weekday and year.** Rows: Mon-Sun + Total. Columns: n cases, n overtime, overtime %, mean OT min. Second panel: year rows 2022-2025. Source: In-Depth Table 24 + Figures 16-17.

### 3.4 Cascading / shift displacement (150 words)

- 4,786 cases (5% of total) were performed in a different shift than originally planned.
- Mean start delay for these cases: 352 min (nearly 6 hours).
- Mean duration deviation vs plan: -22 min (they finish shorter than planned).
- Mean overtime for these cases: 9.2 min.
- The displaced cases do not run long. They finish on time or early. They land in a later shift because upstream cases pushed them there. This reframes the intervention target: the problem is mid-day flow, not end-of-list management.
- Monthly trend: 7-8% of cases displaced in early 2022, declining to 4-5% by 2024. Modest improvement, parallel to overall overtime trend.

> **Figure 3 (MAIN slot 4) — Shift displacement mechanism.** Annotated summary showing the four key numbers: 5% displaced, 352 min mean start delay, -22 min mean duration deviation, 9.2 min mean overtime. Custom design (infographic or annotated bar). Alternatively, a simple 4-row table if the infographic format gets pushback. Source: In-Depth Table 39 (p.47).

### 3.5 Urgent vs elective overtime (200 words)

**Per-case burden by urgency:**
- Elective: 84,028 cases, 7% after-hours, mean OT 4.1 min (all cases, including zeros), P95 18 min.
- Non-elective: 12,016 cases, 18% after-hours, mean OT 10.5 min (all cases, including zeros), P95 67.2 min.
- Urgent cases run after-hours at more than twice the rate. The 95th percentile of overtime minutes was longer for urgent cases (67.2 vs 18 min), indicating heavier tails. However, conditional on running over, the mean overrun length was similar in both groups (approximately 58-59 min). The difference in unconditional means (10.5 vs 4.1 min) reflects the higher overtime rate, not longer individual overruns. Elective cases are seven times more numerous, so the absolute pool of after-hours minutes is dominated by the elective programme.

**Daily overlap:**
- Urgent-elective overlap in the same OR occurred on 869 of 1,247 observation days = 69.7%. Daily, not exceptional.
- Elective cases affected by an urgent overlap started ~30 min later on average (~60 min in early 2022).
- GO11 carries the highest overlap burden: 485 overlap events, 15.5% of its elective cases affected. GO11 is the designated urgent-intake room.

> **Table 2 (MAIN slot 5) — Urgent vs elective overtime and overlap.** Combines: volume (84,028 elective vs 12,016 urgent), per-case overtime rate (7% vs 18%), mean OT, P95 OT, overlap days (869/1,247 = 69.7%), start-delay effect (+30 min), GO11 burden. Source: In-Depth Tables 33, 35, 37, 38.

### 3.6 Stability and turnover — text only (100 words, no figure)

- Room swaps: 1.1% of cases. Overtime 9.5% among swapped vs 8.3% among non-swapped. Room swaps are not a major overtime driver. One sentence. [Supplementary Table S3.]
- Idle time: mean 9.2 min, median 7 min, P95 25 min (gaps exceeding 60 min are excluded as planned downtime). Turnover is fast and consistent. Idle time between cases is not the bottleneck. One sentence. [Supplementary Figure S1.] [32]

### 3.7 Start-time delays — text only (80 words, no figure)

- GEG1 (endoscopy): 90% of cases start late, 0% overtime.
- GO10 (complex surgery): mid-pack on start punctuality (46.2% late), 32.9% overtime.
- This kills the first-case-on-time-start (FCOTS) narrative: the worst-late-start room has zero overtime, and the worst-overtime room is mid-pack on punctuality. Consistent with Pandit et al. (2012), who found R-squared values of 0.04 to 0.08 between start and finish times across more than 7,000 theatre lists in two UK hospitals [17]. [Supplementary Table S2.]

---

## 4. Discussion (~1,000 words)

### 4.1 Finding 1 — Concentration, not prevalence (250 words)

- The headline overtime rate of 8.4% is unremarkable. The finding is that nearly all of it sits in a handful of rooms. GO10 runs overtime in one of every three cases, with a mean overrun of 154 minutes. Three rooms at the other end of the same corridor have zero overtime. The within-campus spread (0-32.9%) exceeds the between-campus spread across the entire ZOL network (0.5-8.4%).
- **Operational implication.** Hospital-wide targets (e.g., "reduce overtime by 10%") will miss the problem unless decomposed by room. The overtime is already concentrated; the intervention should be too. This aligns with Zhang, Dunstan & Pandit (2024), who argue that aggregate utilisation metrics hide room-level operational reality [13].
- **FCOTS contrast.** The conventional view holds that first-case-on-time starts drive end-of-day performance [16]. Our data contradict this: GEG1 has the worst first-case punctuality (90% late) and zero overtime; GO10 is mid-pack on punctuality and worst on overtime. Pandit et al. (2012) showed the same disconnect across more than 7,000 theatre lists in two UK hospitals (R-squared 0.04-0.08 between start and finish times) [17]. FCOTS is a useful discipline metric but not a reliable lever for overtime reduction.

**References for §4.1:** [13] Zhang/Dunstan/Pandit 2024, [16] Dexter & Epstein 2009, [17] Pandit 2012, [18] Macario 2006.

### 4.2 Finding 2 — Cascading as the dominant mechanism (250 words)

- The 4,786 shift-displaced cases finish on time or early (mean duration deviation -22 min), yet they land in the evening shift because of a mean start delay of 352 min. This is not an individual-case-overrun problem. It is mid-day delay accumulation pushing cases across the shift boundary.
- **Literature parallel.** Wachtel and Dexter (2009) showed that tardiness per case grew larger as the day progressed, because the total duration of preceding cases increased; this is the classic cascade pattern [19]. Fugener et al. (2017) demonstrated systematic biases in surgeon duration estimates (planning fallacy, anchoring), which compound the cascade: each underestimated case pushes the next one later [20]. Our -22 min duration deviation is consistent with displaced cases being compressed or truncated to fit a shrinking window.
- **Reframing the intervention.** If the mechanism is cascading rather than long-running individual cases, the intervention point is earlier in the day: scheduling density, buffer placement, and urgent-case routing, rather than end-of-list management. Joseph et al. (2019) documented how minor flow disruptions cluster and escalate into major ones [21]. A systematic review of OR workflow disruptions estimated that roughly 20% of operating time involves disruptions, although the evidence for direct linkage to surgical outcomes is mixed [22].

**References for §4.2:** [19] Wachtel & Dexter 2009, [20] Fugener 2017, [21] Joseph 2019, [22] Koch 2020.

### 4.3 Finding 3 — Urgent-elective interaction (150 words)

- Urgent cases run after-hours at more than twice the rate of elective cases (18% vs 7%), with heavier tails (P95 67.2 vs 18 min). When overtime does occur, however, the mean overrun length is similar in both groups (~58-59 min). Elective cases are seven times more numerous, so the absolute pool of after-hours minutes is dominated by the elective programme. Overlap occurs on 70% of days, adding 30 min to elective start times.
- This is not an argument to restrict urgent access. It is an argument to protect the elective programme from predictable disruption, either through dedicated urgent rooms or through scheduling buffers on historically high-urgency days. GO11 already absorbs much of the overlap and functions as a de facto urgent-intake room.
- The unpredictability of the overlap is the staff-harm dimension: both long shifts and overtime are associated with worse performance and wellbeing, and the unpredictable nature of urgent-driven overtime compounds the effect [23].

**References for §4.3:** [23] Dall'Ora 2016.

### 4.4 The double-ended harm argument (200 words)

- The paper does not measure outcomes directly. It characterises an exposure (cases and staff pushed into understaffed hours) and draws on published evidence for consequences at both ends.
- **Staff harm.** Overtime and long shifts are associated with burnout, reduced perceived care quality, and intent to leave [3,4,5]. Both long shifts and overtime are risk factors for worse performance and wellbeing [23]; high workload and low decision latitude are established burnout predictors [24]. In two Belgian university hospitals, workload and unit-level nurse management were the strongest predictors of burnout and job outcomes [25]. The HSSIB 2025 investigation named staff fatigue as a patient-safety problem [9].
- **Patient harm.** After-hours surgery carries elevated mortality [6,7], though the effect size is debated [26]. Each intraoperative handover raises complication risk [8], though recent sub-specialty data are mixed [27]. Structured handover programmes reduce adverse events (the I-PASS paediatric inpatient study showed a 30% reduction in preventable adverse events) [28]. Reducing intern shifts from extended (>24 h) to intervention schedules produced 36% fewer serious medical errors [30]; extended-duration shifts were associated with 3.5- to 7.5-fold higher odds of fatigue-related significant medical errors in a prospective intern cohort [29]. A systematic review of physician fatigue found associations with physician health outcomes, with mixed evidence for direct effects on surgical patient outcomes [31]. Overtime hours above a breakpoint threshold were associated with increased pressure ulcers across 70 US hospitals [10].
- **Linking the two.** In a hospital where 25 rooms drop to 8, then 4, then 1, each case pushed past the shift boundary lands in a setting with fewer staff, more handovers, and a fatigued workforce. The exposure we document is the upstream condition for both classes of harm.

**References for §4.4:** [3] Griffiths 2014, [4] Dall'Ora 2015, [5] Bae 2024, [6] Cortegiani 2020, [7] Oh 2025, [8] Saager 2014, [9] HSSIB 2025, [10] Pittman 2025, [23] Dall'Ora 2016, [24] Dall'Ora 2020, [25] Van Bogaert 2017, [26] Sakurai 2025, [27] Guerra-Londono 2025, [28] Starmer/I-PASS 2014, [29] Barger 2006, [30] Landrigan 2004, [31] Gates 2018.

### 4.5 Limitations (150 words)

1. **Single-site retrospective.** Findings describe one Belgian tertiary centre. Generalisability to different staffing models is unknown.
2. **Administrative data.** Room-in and room-out only; no induction or recovery timestamps. Cannot decompose what happens inside the case.
3. **No direct outcome data.** The harm argument rests on published literature, not on patient outcomes in this cohort. Phase 2 will link operational patterns to complication and readmission data.
4. **Urgency classification.** The urgency flag is set at booking. Cannot distinguish truly emergent from semi-urgent from add-on elective.
5. **Confounding by case complexity.** GO10 handles complex cardiac surgery (CABG, valve procedures). Its high overtime may partly reflect irreducible procedural duration. We describe this but cannot adjust without procedure-level risk scores.
6. **After-hours mortality debate.** The effect size is contested [26]. We present the evidence as a measurable signal, not a settled question.

---

## 5. Conclusion (~200 words)

- Operating-room overtime at this tertiary centre is not a diffuse hospital-wide problem. It is concentrated in a small number of rooms, driven by mid-day cascading rather than individual case overruns, and amplified by daily urgent-elective overlap.
- The staffing pyramid (25 rooms dropping to 8, then 4, then 1) means every case pushed past the shift boundary lands in a setting with fewer staff and more handovers. Published evidence links both the staff exposure (fatigue, burnout, intent to leave) and the patient exposure (after-hours surgery, handover transitions) to measurable harm.
- These findings argue for room-level rather than hospital-level overtime targets, for scheduling interventions that address mid-day flow rather than first-case punctuality alone, and for prospective outcome linkage in Phase 2.
- No new references in §5. The conclusion restates findings; it does not introduce new evidence.

---

## Figure/table summary — 5 main slots

| Slot | Assignment | Section | Type |
|---|---|---|---|
| 1 | **Figure 1 — Staffing pyramid** | §1.3 | Diagram |
| 2 | **Figure 2 — Room-level overtime bar chart** | §3.3 | Bar chart |
| 3 | **Table 1 — Overtime summary (weekday + year)** | §3.3 | Table |
| 4 | **Figure 3 — Shift displacement mechanism** | §3.4 | Infographic/table |
| 5 | **Table 2 — Urgent vs elective overtime + overlap** | §3.5 | Table |

## Supplementary materials

| Label | Content | Source |
|---|---|---|
| Table S1 | CV by planned-duration bucket | In-Depth Table 13, p.13 |
| Table S2 | Per-room late-start share and overtime rate | In-Depth Table 21, p.24 |
| Table S3 | Room-swap rates and overtime impact | In-Depth Table 27+32 |
| Figure S1 | Idle time per OR | In-Depth Figure 32, p.50 |
| Figure S2 | Monthly shift-displacement trend | In-Depth Figure 30, p.48 |
| Figure S3 | End-time distribution histogram | In-Depth Figure 18, p.32 |
| Table S4 | Per-room overlap burden | In-Depth Table 38, p.46 |

---

## Full reference list (Vancouver numbered)

1. Dexter F, Abouleish AE, Epstein RH, et al. Use of operating room information system data to predict the impact of reducing turnover times on staffing costs. *Anesth Analg* 2003;97(4):1119-26.
1a. Dexter F, Macario A, Traub RD, Hopwood M, Lubarsky DA. An operating room scheduling strategy to maximize the use of operating room block time: computer simulation of patient scheduling and survey of patients' preferences for surgical waiting time. *Anesth Analg* 1999;89(1):7-20.
2. Dexter F, Macario A. Changing allocations of operating room time from a system based on historical utilization to one where the aim is to schedule as many surgical cases as possible. *Anesth Analg* 2002;94(5):1272-79.
3. Griffiths P, Dall'Ora C, Simon M, et al. Nurses' shift length and overtime working in 12 European countries. *Med Care* 2014;52(11):975-81.
4. Dall'Ora C, Griffiths P, Ball J, et al. Association of 12 h shifts and nurses' job satisfaction, burnout and intention to leave. *BMJ Open* 2015;5(9):e008331.
5. Bae S-H. Nurse staffing, work hours, mandatory overtime, and turnover in acute care hospitals affect nurse job satisfaction, intent to leave, and burnout. *Int J Public Health* 2024;69:1607068.
6. Cortegiani A, Ippolito M, Misseri G, et al. Association between night/after-hours surgery and mortality: a systematic review and meta-analysis. *Br J Anaesth* 2020;124(5):623-37.
7. Oh T-K, Song I-A. Outcomes of after-hours surgeries performed under general anaesthesia: a South Korean nationwide cohort study. *Anaesthesia* 2025. DOI: 10.1111/anae.16559.
8. Saager L, Hesler BD, You J, et al. Intraoperative transitions of anesthesia care and postoperative adverse outcomes. *Anesthesiology* 2014;121(4):695-706.
9. Health Services Safety Investigations Body (HSSIB). The impact of staff fatigue on patient safety. Investigation report, UK, 2025.
10. Pittman P, Tiunn H-L, et al. Increased utilization of overtime and agency nurses and patient safety. *JAMA Netw Open* 2025. PMID: 40172888.
11. Bauer M, Diemer M, Merkel M, et al. Glossary of perioperative process times and indicators. *Anaesthesist* 2020;69(Suppl 1):S5-17.
12. Schouten AEM, Flipse SM, van Nieuwenhuizen KE, et al. Operating room performance optimization metrics: a systematic review. *J Med Syst* 2023;47(1):19.
13. Zhang C, Dunstan C, Pandit JJ. A tutorial on "capped utilisation" as a metric in NHS England's Model Hospital operating theatres database. *Anesthesiol Perioper Sci* 2024. DOI: 10.1007/s44254-024-00073-3.
14. Strum DP, May JH, Vargas LG. Modeling the uncertainty of surgical procedure times: comparison of log-normal and normal models. *Anesthesiology* 2000;92(4):1160-7.
15. Eijkemans MJ, van Houdenhoven M, Nguyen T, et al. Predicting the unpredictable: a new prediction model for operating room times. *Anesthesiology* 2010;112(1):41-9.
16. Dexter F, Epstein RH. Typical savings from each minute reduction in tardy first case of the day starts. *Anesth Analg* 2009;108(4):1262-7.
17. Pandit JJ, Abbott T, Pandit M, et al. Is "starting on time" useful (or useless) as a surrogate measure for "surgical theatre efficiency"? *Anaesthesia* 2012;67(8):823-32.
18. Macario A. Are your hospital operating rooms "efficient"? *Anesthesiology* 2006;105(2):237-40.
19. Wachtel RE, Dexter F. Influence of the operating room schedule on tardiness from scheduled start times. *Anesth Analg* 2009;108(6):1889-1901.
20. Fugener A, Schiffels S, Kolisch R. Overutilization and underutilization of operating rooms: insights from behavioral health care operations management. *Health Care Manag Sci* 2017;20(1):115-28.
21. Joseph A, Khoshkenar A, Taaffe KM, et al. Minor flow disruptions, traffic-related factors and their effect on major flow disruptions in the operating room. *BMJ Qual Saf* 2019;28(4):276-83.
22. Koch A, Burns J, Catchpole K, Weigl M. Associations of workflow disruptions in the operating room with surgical outcomes: a systematic review and narrative synthesis. *BMJ Qual Saf* 2020;29(12):1033-1045.
23. Dall'Ora C, Ball J, Recio-Saucedo A, Griffiths P. Characteristics of shift work and their impact on employee performance and wellbeing: a literature review. *Int J Nurs Stud* 2016;57:12-27.
24. Dall'Ora C, Ball J, Reinius M, Griffiths P. Burnout in nursing: a theoretical review. *Hum Resour Health* 2020;18:41.
25. Van Bogaert P, Peremans L, Van Heusden D, et al. Predictors of burnout, work engagement and nurse reported job outcomes and quality of care. *BMC Nurs* 2017;16:5.
26. Sakurai T. Assessing the influence of after-hours surgery: concerns with the confounders and conclusion. *Anaesthesia* 2025. DOI: 10.1111/anae.16591.
27. Guerra-Londono JJ, et al. The impact of intraoperative anesthesiology provider handovers on postoperative complications after hepatopancreatobiliary surgery. *J Surg Oncol* 2025. PMID: 39388390.
28. Starmer AJ, Spector ND, Srivastava R, et al. Changes in medical errors after implementation of a handoff program. *N Engl J Med* 2014;371(19):1803-12.
29. Barger LK, Ayas NT, Cade BE, et al. Impact of extended-duration shifts on medical errors, adverse events, and attentional failures. *PLoS Med* 2006;3(12):e487.
30. Landrigan CP, Rothschild JM, Cronin JW, et al. Effect of reducing interns' work hours on serious medical errors in intensive care units. *N Engl J Med* 2004;351(18):1838-48.
31. Gates M, Wingert A, Featherstone R, et al. Impact of fatigue and insufficient sleep on physician and patient outcomes: a systematic review. *BMJ Open* 2018;8(9):e021967.
32. MacMillan L, et al. What affects operating room turnover time? A systematic review and mapping of the evidence. *Surgery* 2025. PMID: 40054053.
33. Zhang C, Pandit JJ. Getting operating theatre metrics right to underpin quality improvement. *Br J Anaesth* 2023;131(1):130-4.
