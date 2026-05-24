# Where does operating-room overtime come from? A retrospective single-center study

Haroon Tharwat, Maxim Riebus, [Ben surname], [Dieter surname], Niels Martin

[Affiliations]

**Correspondence:** [corresponding author details]

**Word count:** ~3,400 (body text)

**Keywords:** operating room, overtime, scheduling, patient safety, staff wellbeing, quality improvement

---

## ABSTRACT

**Objective.** To characterize operating-room overtime within a high-volume tertiary hospital: its distribution across rooms and the operational factors associated with it.

**Design.** Retrospective observational study of administrative operating-room data.

**Setting.** A 24/7 tertiary hospital in Belgium running 18 surgical operating rooms.

**Participants.** 79,352 surgical procedures performed between January 2022 and May 2025.

**Main outcome measures.** Case-level overtime (time past the assigned shift end), by room, weekday, shift, and urgency. Start-time deviation, duration-estimation accuracy, shift displacement, and urgent-elective overlap as candidate contributing factors.

**Results.** 7,729 cases (9.7%) ran past the end of their assigned shift, with a mean overtime of 60.3 minutes and a 95th percentile of 197 minutes. Overtime concentrated in a small number of rooms: OR10 ran overtime on 32.9% of its cases (mean 154 minutes), while OR14 ran overtime on 3.5%. Urgent cases ran after-hours at more than twice the elective rate (18.2% versus 8.3%). Urgent-elective overlap in the same room occurred on 68.8% of observation days and added roughly 30 minutes to elective start times. First-case punctuality and inter-case idle time showed no consistent association with room-level overtime.

**Conclusions.** At this tertiary hospital, overtime concentrated in a small number of rooms, with case-mix complexity and urgent-elective overlap as the most visible associated factors. Room-level overtime monitoring and scheduling that accounts for urgent-case flow are more practical targets for quality improvement than first-case punctuality alone.

---

## INTRODUCTION

Operating rooms are among the most resource-intensive units in a hospital, and their schedules rarely match what is planned. "Overtime" in this setting can refer to several distinct phenomena: an individual case running longer than its booked duration, an operating list ending after its scheduled close, or surgery continuing into a period when fewer staff are rostered. These are different operational events with different consequences. The glossary of Bauer et al. defines overtime in relation to the staffing window: time spent operating beyond the end of the assigned shift.[18] We adopt this shift-based definition because the staffing change at each boundary is the operational event that gives overtime its meaning. Overutilized time is approximately twice as expensive as underutilized time,[1] but overtime is more than a budget problem.

After-hours surgery has been linked to elevated patient mortality. A meta-analysis reported an adjusted odds ratio of 1.16 (95% CI 1.06 to 1.28), based on low-certainty evidence.[7] A propensity-matched cohort of 281,717 South Korean patients reported a larger effect (odds ratio 3.58), although that estimate has been challenged on residual-confounding grounds.[8,9] In a multicenter cohort of more than 350,000 non-cardiac surgical cases, night surgery was associated with increased morbidity (adjusted odds ratio 1.41), mediated partly by higher transfusion rates and provider handovers during the case.[13] Each intraoperative anesthesia handover raises the odds of a major composite complication, with incidence rising from 8.8% at zero transitions to 21.2% at four or more.[10] A 2025 UK national patient-safety investigation reported that 22% of surveyed doctors experienced daily sleep deprivation and 35% said tiredness had impaired their ability to treat patients.[11] Overtime above a breakpoint threshold has been associated with a 2.09% increase in pressure ulcers across 70 US hospitals.[12]

The same exposure carries documented consequences for staff. A 12-country European nurse workforce study linked overtime and long shifts to poorer perceived care quality and higher patient-safety risk.[2] The companion study tied 12-hour shifts to burnout and intent to leave.[3] Mandatory overtime was associated with intent to leave in a 2024 cross-sectional study of 264 South Korean nurses.[4] Both long shifts and overtime are associated with worse performance and wellbeing,[5] and the combination of high workload and low decision latitude is an established burnout predictor.[6]

The severity of these consequences depends on what happens at the shift boundary. In hospitals that step staffing down sharply at the end of the day shift, a case running past the boundary competes for a diminishing set of staffed rooms, often covered by different personnel from those who started the case.

Prior work on OR overtime has largely treated it as an aggregate site-level number,[16,17] and OR workflow disruptions are known to cluster and escalate.[14,15] Whether overtime concentrates in specific rooms within one hospital, and which operational factors are associated with it, has received less attention. Without that granularity, quality improvement efforts risk targeting the wrong intervention point.

This study is part of a multi-phase program at a Belgian tertiary hospital to improve OR performance. Phase 1 characterizes scheduled-versus-observed performance from administrative data. Phase 2 will link the operational patterns to patient outcomes. Phase 3 will build predictive scheduling tools. In this Phase 1 analysis, we address two questions:

1. **How is overtime distributed across rooms and time within one tertiary hospital?** This examines whether overtime is a diffuse hospital-wide problem or concentrates in specific rooms, since the appropriate intervention point depends on that distribution.
2. **Which operational factors (duration overruns, shift displacement, urgent-elective interaction, and first-case punctuality) are associated with overtime?** This tests which candidate factors identified in the literature are visible in our data, to inform where scheduling interventions should be directed.

## METHODS

### Setting and data

The study hospital is a 24/7 tertiary center in Belgium performing more than 22,000 surgical procedures per year. It operates 18 surgical operating rooms and 7 interventional operating rooms. The surgical staff includes 195 surgeons and 207 anesthesiologists (including trainees and fellows), covering all surgery except congenital cardiac and organ transplantation. Nursing staffing runs 2 to 3 per room during the 08:00 to 16:30 day shift; at 16:30 the number of staffed rooms drops to 8, at 17:30 to 4, and overnight a single room remains staffed.

We used administrative OR data from 1 January 2022 to 31 May 2025, covering 79,352 cases in the 18 surgical operating rooms, 60,895 unique patients, and 1,276 distinct procedure types. The admission mix was 42.3% ambulatory and 57.7% inpatient. Room-in and room-out times are the only time markers confirmed as reliable by the hospital's clinical team; all timing analyses use these two time points. Following the glossary of Bauer et al.,[18] the extracted variables include planned and observed duration, planning deviation, start-time deviation, overtime flag and overtime minutes, room-swap flag, urgency (elective versus non-elective), and shift label.

### Analytic framework

We organized the work along the phases of the CRISP-DM process model.[28] Business and data understanding came from scoping conversations with the hospital's clinical team and an exploratory pass over the registration. Data preparation covered consolidation of records across campuses and validity checks against the clinical team's disclosure that room-in and room-out are the only reliable time markers in the pipeline. The modeling phase was descriptive rather than predictive: room-level overtime statistics and the figures that follow. Evaluation took the form of structured reviews of intermediate findings with the clinical team. Deployment falls outside the present analysis and is the subject of Phases 2 and 3.

### Overtime definition and analyses

Each case was assigned to a shift based on its actual room-in time: day (08:00 to 16:30), evening (16:30 to 22:00), or night (22:00 to 08:00). A case was flagged as overtime if its room-out fell after the end of its assigned shift; overtime minutes equal the positive difference between room-out and shift end. We chose this shift-based definition because the staffing change at each boundary is the operational event that makes overtime consequential at this site, and because it aligns with Bauer et al.[18] Room-level overtime, rather than aggregate utilization, was used as the primary metric, since aggregate measures can mask room-level operational problems.[16,19]

All analyses are descriptive; we did not fit causal or inferential models. For RQ1, we computed overtime rate, mean, median, and 95th percentile, stratified by room, weekday, year, and shift. For RQ2, we examined duration deviation by planned-duration bucket using coefficients of variation,[20,21] shift displacement (cases performed in a different shift than originally planned), urgency mix and timing, urgent-elective interaction (defined and reported in Results), first-case start-time deviation per room, inter-case idle time, and room swaps. This study is reported following the STROBE guidelines for observational studies.

### Ethics

This study used fully de-identified administrative data with institutional approval. No patient interaction occurred.

## RESULTS

### Sample overview

The cohort comprised 79,352 cases across 18 surgical operating rooms, involving 60,895 unique patients, 195 surgeons, and 207 anesthesiologists performing 1,276 distinct procedure types. Weekday volume was evenly distributed (17.9 to 20.0% Monday through Friday); weekends accounted for 1.8 to 2.1%. Year-on-year volume grew from 22,133 in 2022 to 23,738 in 2024, with 9,906 recorded through May 2025. The urgency mix was 85.4% elective and 14.6% non-elective.

### Overtime burden and room-level concentration (RQ1)

Of 79,352 cases, 7,729 (9.7%) ran past the end of their assigned shift. Among overtime cases, the mean was 60.3 minutes, the median 39, and the 95th percentile 197 (Table 1). Weekday rates were similar (8.8 to 9.9%) but roughly 1.7 times higher on weekends (Saturday 16.8%, Sunday 15.5%), when volume is almost entirely non-elective. The year-on-year trend showed gradual improvement: 10.0% in 2022, 10.0% in 2023, 9.7% in 2024, and 8.6% in the partial 2025 data.

**[Table 1. Overtime summary by weekday and year. Cases, overtime count, overtime percentage, and mean overtime minutes by weekday (Monday-Sunday) and year (2022-2025).]**

Room-level overtime rates ranged from 3.5% to 32.9% across the 18 rooms (Figure 1). OR10, which handles complex cardiac surgery (CABG, aortic valve replacement, mitral valve repair), ran overtime on 32.9% of its 1,743 cases, with a mean of 154 minutes and a 95th percentile of 328 minutes. A second tier (OR08 through OR13) clustered at 11 to 16%. At the other end, OR14 ran 3.5% across 6,885 cases and OR01 ran 5.8% across 6,577. Rates therefore spanned nearly an order of magnitude across rooms in the same hospital.

[Insert Figure 1 about here]

Most overtime cases ended shortly after the shift boundary. The majority of completions fell in the 16:30 to 17:30 window, right after the day-shift handover when most of the rooms had already closed. The distribution decayed through the evening, with a thin tail past 22:00 (Supplementary Figure S1).

### Contributing factors (RQ2)

*Planning accuracy.* Of all cases, 45.7% ran longer than planned and 54.3% ran shorter. The mean overrun was 22.6 minutes (median 14); the mean underrun was 21.2 minutes (median 12). On average, the planning system was roughly unbiased. The problem was dispersion. The coefficient of variation of observed duration was lowest for mid-length cases (0.35 to 0.36 for 61 to 180 minutes), moderate for short cases (0.61 for under 30 minutes), and intermediate for very long cases (0.42 for over 180 minutes). Planning-deviation CV was more extreme: the over-180-minute bucket had a CV of 1.86 (Supplementary Table S1). The procedures with the largest absolute deviations (complex cardiac and oncology cases) were concentrated in the rooms with the highest overtime.

*Shift displacement.* A total of 4,151 cases (5.2%) were performed in a different shift than originally planned. These cases started on average 398 minutes later than planned (roughly six and a half hours) and ran 22.3 minutes shorter than planned. We report these figures descriptively; the data do not let us determine whether displacement was a cause of, or a response to, delays elsewhere in the day.

*Urgent-elective interaction.* Urgent cases constituted 14.6% of volume (11,616 of 79,352). Per case, urgent surgery ran past the shift boundary at more than twice the elective rate (18.2% versus 8.3%, Table 2), with heavier tails (P95 69 versus 29 minutes). Because elective cases outnumbered urgent cases nearly six to one, the absolute volume of overtime minutes was still dominated by the elective program.

To assess whether urgent cases disrupt the elective program, we counted days on which an urgent case ran in a room while an elective case had been planned in the same room over an overlapping time window (urgent case's actual room and room-in to room-out interval matched the elective case's planned room and planned start-to-end interval). Such overlap occurred on 858 of 1,247 observation days (68.8%). On days with overlap, elective cases started roughly 30 minutes later than on days without, a gap that reached 60 minutes in early 2022 before narrowing. OR11 absorbed the highest overlap burden, with 475 events affecting 15.2% of its elective cases (Supplementary Table S2).

**[Table 2. Urgent versus elective overtime and overlap. Panel A: volume, after-hours rate, mean overtime, and P95 overtime by urgency. Panel B: overlap frequency (858/1,247 days = 68.8%), mean start-delay effect (+30 min), and OR11 burden.]**

*Factors not associated with overtime.* Room swaps affected 0.7% of cases (519 of 79,352). Swapped cases had a higher overtime rate than non-swapped (14.8% versus 9.7%). Because the data cannot tell us whether the swap caused the overtime or the anticipated overrun prompted the swap, we report the association without interpreting its direction. Inter-case idle time had a median of 8 minutes and a mean of 9.9 minutes, with a 95th percentile of 25 minutes; turnover was not the bottleneck.[22]

First-case punctuality showed no consistent association with room-level overtime. OR10 had the lowest late-start rate (46.1% of first cases late) yet the highest overtime (32.9% of cases past the shift boundary). OR14 had a substantially higher late-start rate (78.7%) yet the lowest overtime (3.5%), and OR11 had the highest late-start rate (82.4%) with mid-pack overtime (11.7%). This is consistent with Pandit et al., who reported R-squared values of 0.04 to 0.08 between start and finish times across more than 7,000 operating room lists.[23]

## DISCUSSION

In this single-center analysis of 79,352 cases, overtime was not a diffuse hospital-wide phenomenon. The aggregate rate (9.7%) hid a near ten-fold spread across rooms (3.5 to 32.9%). The factors most visibly associated with the room-level pattern were case-mix complexity and routine urgent-elective overlap; first-case punctuality and inter-case idle time were not. We discuss each in turn against the existing literature, draw out the implications for quality improvement, and end with the study's limitations.

### Concentration, not prevalence

A 9.7% hospital-wide overtime rate is unremarkable on its own. The distribution, however, is uneven: OR10 ran overtime in roughly one of every three cases, while OR14 ran 3.5%. Hospital-wide targets such as "reduce overtime by 10%" will not reach the problem unless decomposed by room. Zhang, Dunstan and Pandit made the same point: aggregate metrics hide room-level operational reality.[16] Valid room-level metrics are a prerequisite for quality improvement.[24]

### Factors associated with overtime

The procedures with the largest planning deviations (complex cardiac and oncology cases) clustered in the rooms with the highest overtime. This concentration suggests that case-mix complexity, rather than scheduling inefficiency alone, accounts for much of the room-level variation. Wachtel and Dexter described, in a large operational dataset, how tardiness grows as duration uncertainty accumulates through the day,[26] and Fugener et al. documented systematic biases in surgeons' duration estimates that compound across a list.[27] Both observations are consistent with the room-level pattern we describe, although our data cannot test the cumulative-delay account directly.

Urgent-elective overlap occurred on more than two-thirds of observation days and added roughly 30 minutes to elective start times. This makes urgent arrivals a routine scheduling factor rather than an exception. Protecting the elective program from this disruption, through dedicated urgent rooms or scheduling buffers, may be more effective than reactive rescheduling.

A common assumption is that first-case-on-time-start (FCOTS) drives end-of-day performance, with each minute of tardiness carrying a marginal cost.[25] At the room level, our data do not show that relationship: the room with the lowest late-start rate (OR10, 46.1%) had the highest overtime (32.9%), while a room with one of the highest late-start rates (OR14, 78.7%) had the lowest overtime (3.5%). Pandit et al. reported a similar disconnect across more than 7,000 operating room lists.[23] We do not conclude that FCOTS is unimportant; it remains a reasonable discipline marker. In this dataset, however, it does not predict where overtime accumulates.

### Implications

Operational implication. Room-level monitoring should sit ahead of hospital-wide overtime targets, and scheduling should treat urgent-case flow as a routine planning input rather than as an exception.

Clinical implication. The overtime we document is the same exposure that other studies have linked to staff fatigue and to elevated after-hours mortality and complication risk (Introduction; references 2–13). Whether those associations hold in this cohort is the question Phase 2 of this program will address by linking the operational patterns we describe to outcome data.

### Limitations

This study has several limitations. It is a single-site retrospective analysis, so whether the concentration pattern holds in hospitals with different staffing models is unknown. The administrative data provide room-in and room-out times only, so we cannot decompose what happens inside the case. We do not measure patient or staff outcomes directly; the harm argument rests on published literature, not on complications or burnout scores from this cohort. The urgency flag is set at booking, and we cannot distinguish truly emergent cases from semi-urgent or add-on elective cases. OR10 handles complex cardiac surgery, and its high overtime may partly reflect irreducible procedural duration rather than schedulable inefficiency; we describe this but cannot adjust for it without procedure-level risk scores. The link between after-hours surgery and patient harm rests on observational mortality studies whose effect sizes range widely (adjusted odds ratio 1.16[7] to 3.58[8]) and whose estimates have been questioned on residual-confounding grounds.[9] Readers should weigh the after-hours mortality evidence with this uncertainty in mind.

## CONCLUSION

Operating-room overtime at this tertiary hospital concentrated in a small number of rooms, with case-mix complexity and urgent-elective overlap as the most visible associated factors. First-case punctuality and inter-case idle time were not associated with room-level overtime. The findings support room-level rather than hospital-level overtime monitoring and scheduling interventions that account for urgent-case flow. Phase 2 of this research program will link the operational patterns to patient outcome data.

---

## ACKNOWLEDGEMENTS

[To be completed]

## COMPETING INTERESTS

None declared.

## FUNDING

[To be completed]

## DATA AVAILABILITY

The dataset contains de-identified administrative hospital data. Requests for access should be directed to the hospital's research office.

## PATIENT AND PUBLIC INVOLVEMENT

Patients were not involved in the design, conduct, or reporting of this study.

---

## REFERENCES

1. Wachtel RE, Dexter F. Review of behavioral operations experimental studies of newsvendor problems for operating room management. *Anesth Analg* 2010;110(6):1698-1710.
2. Griffiths P, Dall'Ora C, Simon M, et al. Nurses' shift length and overtime working in 12 European countries: the association with perceived quality of care and patient safety. *Med Care* 2014;52(11):975-81.
3. Dall'Ora C, Griffiths P, Ball J, et al. Association of 12 h shifts and nurses' job satisfaction, burnout and intention to leave: findings from a cross-sectional study of 12 European countries. *BMJ Open* 2015;5(9):e008331.
4. Bae S-H. Nurse staffing, work hours, mandatory overtime, and turnover in acute care hospitals affect nurse job satisfaction, intent to leave, and burnout: a cross-sectional study. *Int J Public Health* 2024;69:1607068.
5. Dall'Ora C, Ball J, Recio-Saucedo A, Griffiths P. Characteristics of shift work and their impact on employee performance and wellbeing: a literature review. *Int J Nurs Stud* 2016;57:12-27.
6. Dall'Ora C, Ball J, Reinius M, Griffiths P. Burnout in nursing: a theoretical review. *Hum Resour Health* 2020;18:41.
7. Cortegiani A, Ippolito M, Misseri G, et al. Association between night/after-hours surgery and mortality: a systematic review and meta-analysis. *Br J Anaesth* 2020;124(5):623-37.
8. Oh T-K, Song I-A. Outcomes of after-hours surgeries performed under general anaesthesia: a South Korean nationwide cohort study. *Anesthesia* 2025. DOI: 10.1111/anae.16559.
9. Sakurai T. Assessing the influence of after-hours surgery: concerns with the confounders and conclusion. *Anesthesia* 2025. DOI: 10.1111/anae.16591.
10. Saager L, Hesler BD, You J, et al. Intraoperative transitions of anesthesia care and postoperative adverse outcomes. *Anesthesiology* 2014;121(4):695-706.
11. Health Services Safety Investigations Body (HSSIB). The impact of staff fatigue on patient safety. Investigation report. London: HSSIB, 2025.
12. Pittman P, Tiunn H-L, et al. Increased utilization of overtime and agency nurses and patient safety. *JAMA Netw Open* 2025. PMID: 40172888.
13. Althoff FC, Wachtendorf LJ, Rostin P, et al. Effects of night surgery on postoperative mortality and morbidity: a multicentre cohort study. *BMJ Qual Saf* 2021;30(8):678-688.
14. Joseph A, Khoshkenar A, Taaffe KM, et al. Minor flow disruptions, traffic-related factors and their effect on major flow disruptions in the operating room. *BMJ Qual Saf* 2019;28(4):276-83.
15. Koch A, Burns J, Catchpole K, Weigl M. Associations of workflow disruptions in the operating room with surgical outcomes: a systematic review and narrative synthesis. *BMJ Qual Saf* 2020;29(12):1033-1045.
16. Zhang C, Dunstan C, Pandit JJ. A tutorial on "capped utilisation" as a metric and key performance target in NHS England's Model Hospital operating theatres database: caution for international healthcare systems. *Anesthesiol Perioper Sci* 2024. DOI: 10.1007/s44254-024-00073-3.
17. Macario A. Are your hospital operating rooms "efficient"? A scoring system with eight performance indicators. *Anesthesiology* 2006;105(2):237-40.
18. Bauer M, Diemer M, Merkel M, et al. Glossary of perioperative process times and indicators. *Anaesthesist* 2020;69(Suppl 1):S5-17.
19. Schouten AEM, Flipse SM, van Nieuwenhuizen KE, et al. Operating room performance optimization metrics: a systematic review. *J Med Syst* 2023;47(1):19.
20. Strum DP, May JH, Vargas LG. Modeling the uncertainty of surgical procedure times: comparison of log-normal and normal models. *Anesthesiology* 2000;92(4):1160-7.
21. Eijkemans MJ, van Houdenhoven M, Nguyen T, et al. Predicting the unpredictable: a new prediction model for operating room times using individual surgeon-specific historical data. *Anesthesiology* 2010;112(1):41-9.
22. MacMillan L, et al. What affects operating room turnover time? A systematic review and mapping of the evidence. *Surgery* 2025. PMID: 40054053.
23. Pandit JJ, Abbott T, Pandit M, et al. Is "starting on time" useful (or useless) as a surrogate measure for "surgical theatre efficiency"? *Anaesthesia* 2012;67(8):823-32.
24. Zhang C, Pandit JJ. Getting operating theatre metrics right to underpin quality improvement. *Br J Anaesth* 2023;131(1):130-4.
25. Dexter F, Epstein RH. Typical savings from each minute reduction in tardy first case of the day starts. *Anesth Analg* 2009;108(4):1262-7.
26. Wachtel RE, Dexter F. Influence of the operating room schedule on tardiness from scheduled start times. *Anesth Analg* 2009;108(6):1889-1901.
27. Fugener A, Schiffels S, Kolisch R. Overutilization and underutilization of operating rooms: insights from behavioral health care operations management. *Health Care Manag Sci* 2017;20(1):115-28.
28. Wirth R, Hipp J. CRISP-DM: towards a standard process model for data mining. In: *Proceedings of the 4th International Conference on the Practical Applications of Knowledge Discovery and Data Mining (PADD-00)*. Manchester: Practical Application Company, 2000:29-39.

---

## FIGURE LEGENDS

**Figure 1.** Room-level overtime concentration. Horizontal bar chart with one bar per operating room, ordered descending by overtime rate. A secondary panel shows mean overtime minutes per room. OR10 (32.9%) and OR14 (3.5%) anchor the extremes. Overall: 7,729 of 79,352 cases (9.7%), mean 60.3 min, median 39 min, P95 197 min.
