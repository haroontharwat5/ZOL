# Where does operating-room overtime come from, and who pays for it? A 96,044-case analysis of one tertiary centre

Haroon Tharwat, Maxim Riebus, [Ben surname], [Dieter surname], Niels Martin

[Affiliations]

**Correspondence:** [corresponding author details]

**Word count:** ~3,500 (body text)

**Keywords:** operating room, overtime, scheduling, patient safety, staff wellbeing, quality improvement

---

## Abstract

**Objective.** To characterise where operating-room overtime originates within a high-volume tertiary hospital and to connect the operational pattern to published evidence on staff and patient harms.

**Design.** Retrospective observational study of administrative operating-room data.

**Setting.** Campus Genk of the Ziekenhuis Oost-Limburg network, Belgium, a 24/7 tertiary hospital running 25 operating rooms across general, cardiac, and endoscopy blocks.

**Participants.** 96,044 surgical and interventional procedures performed between January 2022 and May 2025.

**Main outcome measures.** Case-level overtime flag and overtime minutes (time past the 16:30 scheduled shift end), by room, weekday, shift, and urgency. Shift-transition displacement, start-time deviation, and duration-estimation accuracy as candidate mechanisms.

**Results.** 8,024 cases (8.4%) ran past the scheduled shift end, with a mean overtime of 59 minutes and a 95th percentile of 194 minutes. Overtime was concentrated in a small number of rooms: one room (GO10) ran overtime on 32.9% of its cases with a mean overrun of 154 minutes, while three rooms never ran overtime. 4,786 cases (5%) were performed in a different shift than originally planned, with a mean start delay of 352 minutes and a mean duration 22 minutes shorter than planned, indicating upstream displacement rather than individual overruns. Urgent-elective overlap in the same operating room occurred on 69.7% of observation days and added roughly 30 minutes to elective start times. First-case punctuality did not predict room-level overtime.

**Conclusions.** At this high-volume tertiary centre, overtime was concentrated, cascading, and driven by mid-day displacement rather than by late starts or individual case overruns. Room-level and cascading-focused metrics offer a more actionable target for quality improvement than utilisation or first-case punctuality.

---

## Introduction

Ziekenhuis Oost-Limburg (ZOL) is running a multi-phase programme to improve operating-theatre performance across its hospital network. Phase 1 of the programme characterises scheduled-versus-observed performance from administrative data. Phase 2 will link the operational patterns to patient outcomes. Phase 3 will build predictive scheduling tools. This paper reports Phase 1 findings for one specific aspect of OR performance: overtime.

Overtime is the binding economic cost in operating-room operations, weighted 1.5 to 2 times the cost of idle time in established costing models.^1,2^ But its consequences extend beyond staffing budgets. Two bodies of evidence make overtime a quality-and-safety concern rather than a purely financial one.

On the staff side, overtime and long shifts are associated with poorer perceived care quality and higher patient-safety risk in a 12-country European nurse workforce study.^3^ The companion study linked 12-hour shifts to burnout and intent to leave.^4^ More recently, mandatory overtime was significantly associated with intent to leave in a cross-sectional study of 397 US nurses.^5^ The distinction between planned and unplanned overtime matters: unplanned overtime is more harmful than planned long shifts.^23,24^

On the patient side, after-hours surgery carries elevated mortality. A 2020 meta-analysis reported an adjusted odds ratio of 1.16 (95% CI 1.06 to 1.28).^6^ This was recently replicated in a 281,717-patient propensity-matched cohort from South Korea.^7^ Each intraoperative anaesthesia handover raises the odds of a major composite complication, with incidence rising from 8.8% at zero transitions to 21.2% at four or more.^8^ A 2025 UK national patient-safety investigation named staff fatigue as a direct patient-safety problem, reporting that 22% of surveyed doctors experienced daily sleep deprivation and 35% said tiredness had impaired their ability to treat patients.^9^ Overtime hours have also been directly associated with patient-safety indicators across 70 US hospitals.^10^

What connects the two sides is the staffing context. At the study hospital, Campus Genk runs 25 operating rooms during the 08:00 to 16:30 day shift. At 16:30, capacity drops to 8 rooms. At 17:30, it drops again to 4. Overnight, a single room remains staffed with three on-call nurses (Figure 1). A case that runs past 16:30 is not merely a few minutes late. It is competing for one of a sharply diminishing set of staffed rooms, covered by different staff than those who started the day. This staffing cliff is what makes overtime at this site a meaningful exposure category rather than an arbitrary clock cut-off.

**[Figure 1. Staffing pyramid at Campus Genk. Step diagram showing the four staffing tiers: 25 rooms during the 08:00-16:30 day shift, 8 rooms during 16:30-17:30, 4 rooms during 17:30-22:00, and 1 room overnight. Reproduced with permission from the hospital's project-launch materials.]**

Prior work on OR overtime has largely treated it as an aggregate site-level number.^13,18^ Little existing literature examines how overtime is distributed within a single hospital: which rooms, which mechanisms, and which cases spill into after-hours. Without that distribution, quality improvement efforts cannot target the right lever. We asked three questions:

1. How is overtime distributed across rooms and time within one tertiary centre?
2. What mechanism — late starts, individual case overruns, or mid-day cascading — accounts for most of the overtime?
3. How do urgent cases interact with the elective programme to produce spillover into staffed-down hours?

## Methods

### Setting

Campus Genk is a tertiary centre within the ZOL network in Limburg, Belgium, performing more than 50,000 procedures per year. It operates 18 surgical theatres, 7 interventional theatres, and an ambulatory anaesthesia unit covering endoscopy, IVF, and MKA sedation. More than 90 anaesthesiologists, including trainees and fellows, cover all surgery except congenital cardiac surgery and organ transplantation. Staffing runs 2 to 3 nurses per operating room during the day shift, with the stepwise reductions described above.

### Data and inclusion

We used administrative OR data from 1 January 2022 to 31 May 2025, covering 96,044 cases involving 71,621 unique patients, 225 surgeons, 211 anaesthesiologists, 26 operating rooms, and 1,327 distinct procedure names. The admission mix was 51.0% ambulatory, 48.9% inpatient, and 0.1% emergency-bed. The hospital's clinical team confirmed that room-in and room-out are the only reliable time markers in the registration pipeline. All timing analyses therefore use those two time points. Induction, recovery, and ward-transfer marks are recorded in the electronic health record but were not used.

### Variables

We followed the glossary of Bauer et al.^11^ for variable definitions: planned duration, observed duration, planning deviation, scheduled start, actual start, start-time deviation, room-out time, overtime flag (room-out after 16:30), overtime minutes, room-swap flag (actual room differs from planned room), urgency at planning (elective versus non-elective), and shift label (day 08:00-16:30, evening 16:30-22:00, night 22:00-08:00). We chose room-level overtime as the primary metric rather than aggregate utilisation, following the argument that utilisation figures hide room-level operational problems when interpreted without staffing context.^12,13^

### Overtime definition

Overtime was defined as any case still in the room past 16:30 on the calendar day, or any case ending in the evening or night shift. This is a shift-based definition, not a duration-based one. We chose it because the staffing change at 16:30 is the operational event that gives overtime its meaning at this site. The definition aligns with the overtime framework in Bauer et al.^11^ and with the hospital's own framing of surgical activity past the day-shift staffing window.

### Analyses

All analyses are descriptive. We did not fit causal or inferential models. Three blocks of analysis address the three research questions:

First, burden and concentration. We computed case-level overtime rate, mean, median, and 95th percentile, stratified by room, weekday, year, and shift. Room-level concentration is the primary analytic focus.

Second, mechanism. We assessed start-time deviation per case and per room, duration deviation by planned-duration bucket using coefficients of variation,^14,15^ and shift displacement (cases performed in a different shift than originally planned, with mean start delay and mean planning deviation).

Third, daily disruptors. We calculated the urgency mix and its timing, urgent-elective overlap in the same operating room per day and per room, and the effect of overlap on elective start delay.

Room swaps (1.1% of cases) and idle time between cases (median 7 minutes) were assessed separately and are reported as non-bottlenecks in the results text, with full data in the online supplement.

### Ethics

This study used fully de-identified administrative data with institutional approval. No patient interaction occurred.

## Results

### Sample overview

The cohort comprised 96,044 cases. Weekday volume was evenly distributed (18.7 to 20.9% Monday through Friday); weekends accounted for 1.5 to 1.7% of cases. Year-on-year volume grew from 26,103 cases in 2022 to 29,223 in 2024, with 12,196 recorded in 2025 through May. The urgency mix was 87.5% elective and 12.5% non-elective.

### Planning accuracy

Of all cases, 45.2% ran longer than planned and 54.8% ran shorter. The mean overrun was 21 minutes (median 13); the mean underrun was 19.7 minutes (median 11). On average, the planning system was roughly unbiased. The problem was dispersion. The coefficient of variation of observed duration was lowest for mid-length cases (0.35 to 0.36 for 61 to 180 minutes), moderate for short cases (0.61 for cases under 30 minutes), and intermediate for very long cases (0.42 for cases over 180 minutes). Planning-deviation CV followed the same pattern but was more extreme: the over-180-minute bucket had a CV of 1.86 (Supplementary Table S1). The procedures with the largest absolute deviations included complex cardiac cases (AVR, CABG off-pump) and oncology procedures (debulking with HIPEC), the same procedure types concentrated in the rooms with the highest overtime.

### Overtime burden

Of 96,044 cases, 8,024 (8.4%) ran past the 16:30 shift end. Mean overtime was 59 minutes, median 38 minutes, and the 95th percentile was 194 minutes (Table 1). The rate was stable across weekdays (7.8 to 8.5%) but roughly doubled on weekends (Saturday 16.8%, Sunday 15.5%), when volume is almost entirely non-elective. The year-on-year trend showed slow improvement: 8.8% in 2022, 8.6% in 2023, 8.2% in 2024, and 7.2% in the partial 2025 data. This was a gradual decline, not a step change.

**[Table 1. Overtime summary by weekday and year. Rows: Monday through Sunday, plus yearly breakdown (2022-2025). Columns: number of cases, number with overtime, overtime percentage, mean overtime minutes. Source: In-Depth Analysis Table 24, Figures 16-17.]**

### Room-level concentration

The within-campus spread in overtime rates ran from 0% to 32.9% (Figure 2). GO10, which handles complex cardiac surgery, ran overtime on 32.9% of its 1,752 cases, with a mean overrun of 154 minutes and a 95th percentile of 327 minutes. In this room, one in every three cases ran into after-hours. A second tier of rooms (GO08 through GO13) clustered at 11 to 16%. At the other end, GEG1 (endoscopy, 4,498 cases), GSE1 (2,261 cases), and GEX1 (634 cases) had overtime rates at or near zero. This within-campus spread exceeded the between-campus spread across the entire ZOL network, where overtime rates ranged from 0.5% at Lanaken to 8.4% at Genk.

**[Figure 2. Room-level overtime concentration at Campus Genk. Horizontal bar chart with one bar per operating room, ordered descending by overtime rate. A secondary panel shows mean overtime minutes per room. GO10 (32.9%) and GEG1/GSE1 (0%) anchor the extremes. Caption table includes headline numbers: 8,024 of 96,044 cases (8.4%), mean 59 min, median 38 min, P95 194 min. Source: In-Depth Analysis Table 25.]**

Most overtime cases ended shortly after the shift boundary. Roughly 3,000 cases ended between 16:30 and 17:30, the window in which staffing had just dropped from 25 to 8 rooms. The distribution decayed rapidly through the evening, with a thin tail past 22:00 (Supplementary Figure S3).

### Cascading as the dominant mechanism

A total of 4,786 cases (5.0%) were performed in a different shift than originally planned (Figure 3). These displaced cases had a mean start delay of 352 minutes, nearly six hours. Yet their mean duration was 22 minutes shorter than planned, and their mean overtime was only 9.2 minutes. The displaced cases did not run long. They finished on time or early. They landed in a later shift because upstream cases pushed them there.

This finding reframes the intervention target. The overtime problem is not about individual cases overrunning their scheduled time. It is about delay accumulating through the morning and early afternoon, pushing end-of-list cases across the 16:30 boundary. The monthly trend showed modest improvement, declining from 7 to 8% of cases displaced in early 2022 to 4 to 5% by 2024 (Supplementary Figure S2).

**[Figure 3. Shift displacement as the overtime mechanism. Summary of 4,786 cases (5.0% of total) displaced into a different shift than planned. Four annotated numbers: mean start delay 352 minutes, mean duration deviation -22 minutes (shorter than planned), mean overtime 9.2 minutes, share of total 5%. Source: In-Depth Analysis Table 39.]**

### Urgent-elective interaction

Urgent cases constituted 12.5% of volume (12,016 of 96,044). Per case, urgent surgery ran after-hours at more than twice the rate of elective surgery: 18% versus 7%, with a mean overtime of 10.5 versus 4.1 minutes (Table 2). But elective cases outnumbered urgent cases seven to one. In absolute terms, the elective programme contributed the larger share of after-hours minutes.

Urgent-elective overlap in the same operating room occurred on 869 of 1,247 observation days, or 69.7%. This was daily rather than exceptional. On days with overlap, elective cases started roughly 30 minutes later than on days without, a gap that reached 60 minutes in early 2022 before narrowing. GO11 absorbed the highest absolute overlap burden, with 485 overlap events affecting 15.5% of its elective cases. This room functioned as a de facto urgent-intake room (Supplementary Table S4).

**[Table 2. Urgent versus elective overtime and overlap. Panel A: volume, after-hours rate, mean overtime, and P95 overtime by urgency. Panel B: overlap frequency (869/1,247 = 69.7% of days), mean start-delay effect (+30 min), and GO11 burden. Source: In-Depth Analysis Tables 33, 35, 37, 38.]**

### Non-mechanisms

Room swaps affected 1.1% of cases. The overtime rate among swapped cases was 9.5% versus 8.3% among non-swapped cases. Room swaps were not a meaningful overtime driver (Supplementary Table S3). Idle time between consecutive cases had a median of 7 minutes and a mean of 9.2 minutes. Turnover was fast and consistent across rooms. Idle time was not the bottleneck (Supplementary Figure S1).^32^

First-case punctuality did not predict overtime. GEG1 had the worst start-time performance, with 90% of cases starting late, yet had zero overtime. GO10 was mid-pack on start punctuality (46.2% late) and worst on overtime (32.9%). This is consistent with Pandit et al., who found that start time explained only 4 to 8% of the variance in finish time.^17^

## Discussion

### Concentration, not prevalence

A campus-wide overtime rate of 8.4% is unremarkable. What stands out is how uneven its distribution is. GO10 ran overtime in one of every three cases, with a mean overrun of more than two and a half hours. Three rooms at the other end of the same corridor had zero overtime. The spread within this single campus (0 to 32.9%) was wider than the spread between campuses across the entire ZOL network (0.5 to 8.4%).

Hospital-wide targets such as "reduce overtime by 10%" will miss the problem unless they are decomposed by room. The overtime is already concentrated; the intervention should be too. Zhang, Dunstan, and Pandit made the same point in their tutorial on capped utilisation: aggregate metrics hide room-level operational reality.^13^ The broader argument that getting OR metrics right is a prerequisite for quality improvement has been made separately.^33^

The data also challenge the first-case-on-time-start (FCOTS) narrative. The conventional view holds that first-case punctuality drives end-of-day performance, and that each minute of tardiness carries a marginal cost.^16^ Our data show the opposite pattern: the room with the worst start-time discipline (GEG1, 90% late) had zero overtime, and the room with the worst overtime (GO10, 32.9%) was mid-pack on punctuality. Pandit et al. demonstrated the same disconnect, reporting R-squared values of 0.04 to 0.08 between start and finish times across 17 operating rooms.^17^ FCOTS may be a useful discipline marker, but it is not a reliable lever for reducing overtime.

### Cascading as the dominant mechanism

The 4,786 shift-displaced cases finished on time or early (mean duration deviation of minus 22 minutes), yet they landed in the evening shift because of a mean start delay of 352 minutes. This was not an individual-case problem. It was mid-day delay accumulating through the schedule and pushing cases across the shift boundary.

The cascading pattern has been described before. Wachtel and Dexter modelled first-case tardiness propagating through the day in a theoretical OR framework.^19^ Fugener et al. added a behavioural dimension: surgeons compress their work when they sense they are approaching a block boundary.^20^ The minus-22-minute duration deviation we observed is consistent with that compression effect. Joseph et al. documented a similar escalation pattern in a different OR context, showing how minor flow disruptions compound into major ones.^21^ Abdelfattah et al. linked workflow disruptions directly to patient outcomes.^22^

If the mechanism is cascading rather than individual long-running cases, the intervention point is earlier in the day. The targets are scheduling density, buffer placement, and urgent-case routing, not end-of-list management.

### Urgent-elective interaction

Urgent cases ran after-hours at more than twice the rate of elective cases (18% versus 7%). But because elective cases were seven times more numerous, the absolute volume of after-hours minutes was dominated by the elective programme. Overlap between urgent and elective cases in the same room occurred on 70% of observation days, adding roughly 30 minutes to elective start times.

This is not an argument to restrict urgent access. It is an argument to protect the elective programme from predictable disruption, either through dedicated urgent rooms or through scheduling buffers on days with historically high urgent volume. GO11 already absorbs a large share of the overlap, functioning as the designated urgent-intake room. The unpredictability of the overlap has a workforce dimension: unplanned overtime is more harmful than planned long shifts.^23^

### Staff and patient consequences

This paper does not measure outcomes directly. It characterises an exposure: cases and staff pushed into understaffed hours. Published evidence documents consequences at both ends.

On the staff side, overtime and long shifts are associated with burnout, reduced perceived care quality, and intent to leave.^3,4,5^ Unpredictable overtime is worse than planned long hours.^23,24^ In a Flemish nursing workforce, workload and schedule control dominated burnout predictors.^25^ The HSSIB 2025 national investigation named staff fatigue as a patient-safety problem, bridging the two sides of the argument.^9^

On the patient side, after-hours surgery carries elevated mortality in meta-analytic and cohort data,^6,7^ though the effect size is debated.^26^ Each intraoperative handover raises complication risk,^8^ though recent sub-specialty data have produced mixed results.^27^ Structured handover programmes can reduce adverse events.^28^ Shifts exceeding 24 hours are associated with a 36% increase in serious medical errors,^29^ and shorter intern shifts reduced serious errors by a similar magnitude in an ICU setting.^30^ A systematic review of the fatigue-to-error pathway confirmed these patterns across physician and patient outcomes.^31^ Overtime hours have been directly associated with patient-safety indicators across 70 US hospitals.^10^

In a hospital where 25 rooms drop to 8, then 4, then 1, each case pushed past 16:30 lands in a setting with fewer staff, more handovers, and a fatigued workforce. The exposure we document is the upstream condition for both classes of harm.

### Limitations

This study has several limitations. First, it is a single-site retrospective analysis of one Belgian tertiary centre. Whether the concentration and cascading patterns hold in hospitals with different staffing models is unknown. Second, the administrative data provide room-in and room-out times only. We cannot decompose what happens inside the case. Third, we do not measure patient outcomes or staff outcomes directly. The harm argument rests on published literature, not on complications or burnout scores from this cohort. Phase 2 of the research programme will link these operational patterns to complication and readmission data. Fourth, the urgency flag is set at booking, and we cannot distinguish truly emergent cases from semi-urgent or add-on elective cases. Fifth, GO10 likely handles the most complex cardiac surgery, and its high overtime may partly reflect irreducible procedural duration rather than schedulable inefficiency. We describe this but cannot adjust for it without procedure-level risk scores. Sixth, the after-hours mortality signal, while replicated across studies, has been questioned on confounder grounds.^26^ We present the evidence as a measurable signal rather than a settled question.

## Conclusion

Operating-room overtime at this tertiary centre is not a diffuse hospital-wide problem. It is concentrated in a small number of rooms, driven primarily by mid-day cascading rather than individual case overruns, and amplified by daily urgent-elective overlap. The staffing pyramid, with 25 rooms dropping to 8, then 4, then 1, means every case pushed past the shift boundary lands in a setting with fewer staff and more handovers. Published evidence links both the staff exposure (fatigue, burnout, intent to leave) and the patient exposure (after-hours surgery, handover transitions) to measurable harm.

These findings argue for room-level rather than hospital-level overtime targets, for scheduling interventions that address mid-day flow rather than first-case punctuality alone, and for prospective outcome linkage in Phase 2 of this research programme.

---

## Acknowledgements

[To be completed]

## Funding

[To be completed]

## Competing interests

None declared.

## Data availability

The dataset contains de-identified administrative hospital data. Requests for access should be directed to the Ziekenhuis Oost-Limburg research office.

## Patient and public involvement

Patients were not involved in the design, conduct, or reporting of this study.

---

## References

1. Dexter F, Abouleish AE, Epstein RH, et al. Use of operating room information system data to predict the impact of reducing turnover times on staffing costs. *Anesth Analg* 2004;97(4):1119-26.
2. McIntosh C, Dexter F, Epstein RH. The impact of service-specific staffing, case scheduling, turnovers, and first-case starts on anesthesia group and operating room productivity. *Anesth Analg* 2006;103(6):1499-516.
3. Griffiths P, Dall'Ora C, Simon M, et al. Nurses' shift length and overtime working in 12 European countries: the association with perceived quality of care and patient safety. *Med Care* 2014;52(11):975-81.
4. Dall'Ora C, Griffiths P, Ball J, et al. Association of 12 h shifts and nurses' job satisfaction, burnout and intention to leave: findings from a cross-sectional study of 12 European countries. *BMJ Open* 2015;5(9):e008331.
5. Cho (Bae) J, Cho HJ, et al. Nurse staffing, work hours, mandatory overtime, and turnover in acute care hospitals affect nurse job satisfaction, intent to leave, and burnout: a cross-sectional study. *Int J Public Health* 2024;69:1607068.
6. Cortegiani A, Ippolito M, Misseri G, et al. Association between night/after-hours surgery and mortality: a systematic review and meta-analysis. *Br J Anaesth* 2020;124(5):623-37.
7. Oh T-K, Jo Y-Y, Song I-A. Outcomes of after-hours surgeries performed under general anaesthesia: a South Korean nationwide cohort study. *Anaesthesia* 2025. DOI: 10.1111/anae.16559.
8. Saager L, Hesler BD, You J, et al. Intraoperative transitions of anesthesia care and postoperative adverse outcomes. *Anesthesiology* 2014;121(4):695-706.
9. Health Services Safety Investigations Body (HSSIB). The impact of staff fatigue on patient safety. Investigation report. London: HSSIB, 2025.
10. Pittman P, Tiunn H-L, et al. Increased utilization of overtime and agency nurses and patient safety. *JAMA Netw Open* 2025. PMID: 40172888.
11. Bauer M, Diemer M, Merkel M, et al. Glossary of perioperative process times and indicators. *Anaesthesist* 2020;69(Suppl 1):S5-17.
12. Schouten AEM, Flipse SM, van Nieuwenhuizen KE, et al. Operating room performance optimization metrics: a systematic review. *J Med Syst* 2023;47(1):19.
13. Zhang J, Dunstan M, Pandit JJ. A tutorial on "capped utilisation" as a metric and key performance target in NHS England's Model Hospital operating theatres database. *Anesthesiol Perioper Sci* 2024. DOI: 10.1007/s44254-024-00073-3.
14. Strum DP, May JH, Vargas LG. Modeling the uncertainty of surgical procedure times: comparison of log-normal and normal models. *Anesthesiology* 2000;92(4):1160-7.
15. Eijkemans MJ, van Houdenhoven M, Nguyen T, et al. Predicting the unpredictable: a new prediction model for operating room times using individual surgeon-specific historical data. *Anesthesiology* 2010;112(1):41-9.
16. Dexter F, Epstein RH. Typical savings from each minute reduction in tardy first case of the day starts. *Anesth Analg* 2009;108(4):1262-7.
17. Pandit JJ, Abbott T, Pandit M, et al. Is "starting on time" useful (or useless) as a surrogate measure for "surgical theatre efficiency"? *Anaesthesia* 2012;67(8):823-32.
18. Macario A. Are your hospital operating rooms "efficient"? A scoring system with eight performance indicators. *Anesthesiology* 2006;105(2):237-40.
19. Wachtel RE, Dexter F. Tactical increases in operating room block time for capacity planning should not be based on utilization. *Anesth Analg* 2009;108(4):1215-20.
20. Fugener A, Schiffels S, Kolisch R. Overutilization and underutilization of operating rooms: insights from behavioral health care operations management. *Health Care Manag Sci* 2017;20(1):115-28.
21. Joseph A, Khoshkenar A, Taaffe KM, et al. Minor flow disruptions, traffic-related factors and their effect on major flow disruptions in the operating room. *BMJ Qual Saf* 2019;28(4):276-83.
22. Abdelfattah E, et al. Workflow disruptions and surgical outcomes. *BMJ Qual Saf* 2020;29:1009-17.
23. Dall'Ora C, Ball J, Recio-Saucedo A, Griffiths P. Characteristics of shift work and their impact on employee performance and wellbeing: a literature review. *Int J Nurs Stud* 2016;57:12-27.
24. Dall'Ora C, Ball J, Reinius M, Griffiths P. Burnout in nursing: a theoretical review. *Hum Resour Health* 2020;18:41.
25. Van Bogaert P, Peremans L, Van Heusden D, et al. Predictors of burnout, work engagement and nurse reported job outcomes and quality of care: a survey among hospital nurses in Belgium. *BMC Nurs* 2017;16:5.
26. Sakurai T. Assessing the influence of after-hours surgery: concerns with the confounders and conclusion. *Anaesthesia* 2025. DOI: 10.1111/anae.16591.
27. Guerra-Londono JJ, et al. The impact of intraoperative anesthesiology provider handovers on postoperative complications after hepatopancreatobiliary surgery. *J Surg Oncol* 2025. PMID: 39388390.
28. Starmer AJ, Spector ND, Srivastava R, et al. Changes in medical errors after implementation of a handoff program. *N Engl J Med* 2014;371(19):1803-12.
29. Barger LK, Ayas NT, Cade BE, et al. Impact of extended-duration shifts on medical errors, adverse events, and attentional failures. *PLoS Med* 2006;3(12):e487.
30. Landrigan CP, Rothschild JM, Cronin JW, et al. Effect of reducing interns' work hours on serious medical errors in intensive care units. *N Engl J Med* 2004;351(18):1838-48.
31. Gates M, Wingert A, Featherstone R, et al. Impact of fatigue and insufficient sleep on physician and patient outcomes: a systematic review. *BMJ Open* 2018;8(9):e021967.
32. MacMillan C, et al. What affects operating room turnover time? A systematic review and mapping of the evidence. *Surgery* 2025. PMID: 40054053.
33. Zhang C, Pandit JJ. Getting operating theatre metrics right to underpin quality improvement. *Br J Anaesth* 2023;131(1):130-4.
