# Where does operating-room overtime come from, and who pays for it? A 79,352-case analysis of one tertiary centre

Haroon Tharwat, Maxim Riebus, [Ben surname], [Dieter surname], Niels Martin

[Affiliations]

**Correspondence:** [corresponding author details]

**Word count:** ~3,500 (body text)

**Keywords:** operating room, overtime, scheduling, patient safety, staff wellbeing, quality improvement

---

## Abstract

**Objective.** To characterise where operating-room overtime originates within a high-volume tertiary hospital and to connect the operational pattern to published evidence on staff and patient harms.

**Design.** Retrospective observational study of administrative operating-room data.

**Setting.** Campus Genk of the Ziekenhuis Oost-Limburg network, Belgium, a 24/7 tertiary hospital running 18 surgical operating rooms.

**Participants.** 79,352 surgical procedures performed between January 2022 and May 2025.

**Main outcome measures.** Case-level overtime flag and overtime minutes (time past the end of the case's assigned shift), by room, weekday, shift, and urgency. Shift-transition displacement, start-time deviation, and duration-estimation accuracy as candidate mechanisms.

**Results.** 7,729 cases (9.7%) ran past the end of their assigned shift, with a mean overtime of 60.3 minutes (calculated among overtime cases) and a 95th percentile of 197 minutes. Overtime was concentrated in a small number of rooms: one room (GO10) ran overtime on 32.9% of its cases with a mean overrun of 154 minutes, while the lowest-overtime room (GO14) ran overtime on 3.5%. 4,151 cases (5.2%) were performed in a different shift than originally planned, with a mean start delay of 398 minutes and a mean duration 22 minutes shorter than planned, indicating upstream displacement rather than individual overruns. Urgent-elective overlap in the same operating room occurred on 68.8% of observation days and added roughly 30 minutes to elective start times. First-case punctuality did not predict room-level overtime.

**Conclusions.** At this tertiary centre, overtime was concentrated, cascading, and driven by mid-day displacement rather than by late starts or individual case overruns. Room-level and cascading-focused metrics offer a more actionable target for quality improvement than utilisation or first-case punctuality.

---

## Introduction

Ziekenhuis Oost-Limburg (ZOL) is running a multi-phase programme to improve operating-theatre performance across its hospital network. Phase 1 of the programme characterises scheduled-versus-observed performance from administrative data. Phase 2 will link the operational patterns to patient outcomes. Phase 3 will build predictive scheduling tools. This paper reports Phase 1 findings for one specific aspect of OR performance: overtime.

Overtime is the binding economic cost in operating-room operations; overutilised time is approximately twice as expensive as underutilised time.^1^ Its consequences extend beyond staffing budgets. Two bodies of evidence make overtime a quality-and-safety concern as well as a financial one.

On the staff side, overtime and long shifts are associated with poorer perceived care quality and higher patient-safety risk in a 12-country European nurse workforce study.^2^ The companion study linked 12-hour shifts to burnout and intent to leave.^3^ More recently, mandatory overtime was significantly associated with intent to leave in a 2024 cross-sectional study of 264 South Korean nurses.^4^ Both long shifts and overtime are associated with worse performance and wellbeing,^22^ and high workload combined with low decision latitude is an established burnout predictor.^23^

On the patient side, after-hours surgery carries elevated mortality. A 2020 meta-analysis reported an adjusted odds ratio of 1.16 (95% CI 1.06 to 1.28), based on low-certainty evidence.^5^ A 2024 propensity-matched cohort of 281,717 South Korean patients reported a much larger effect (OR 3.58), although that estimate has been challenged on residual-confounding grounds, given a four-fold imbalance in emergency procedures even after matching.^6,25^ Each intraoperative anaesthesia handover raises the odds of a major composite complication, with incidence rising from 8.8% at zero transitions to 21.2% at four or more.^7^ A 2025 UK national patient-safety investigation, citing a Medical Defence Union member survey of 481 doctors, reported that 22% experienced daily sleep deprivation and that 35% said tiredness had impaired their ability to treat patients.^8^ Overtime hours above a breakpoint threshold have been associated with a 2.09% increase in pressure ulcers across 70 US hospitals.^9^

The staffing context is what links the two sides. At the study hospital, Campus Genk runs 25 operating rooms during the 08:00 to 16:30 day shift. At 16:30, capacity drops to 8 rooms. At 17:30, it drops again to 4. Overnight, a single room remains staffed with three on-call nurses (Figure 1). A case that runs past 16:30 is not merely a few minutes late; it is competing for one of a sharply diminishing set of staffed rooms, covered by different staff than those who started the day. The staffing change at the shift boundary is what gives overtime its operational meaning at this site, rather than an arbitrary clock cut-off.

**[Figure 1. Staffing pyramid at Campus Genk. Step diagram showing the four staffing tiers: 25 rooms during the 08:00-16:30 day shift, 8 rooms during 16:30-17:30, 4 rooms during 17:30-22:00, and 1 room overnight. Reproduced with permission from the hospital's project-launch materials.]**

Prior work on OR overtime has largely treated it as an aggregate site-level number.^12,17^ Less attention has been paid to how overtime is distributed within a single hospital: which rooms, which mechanisms, and which cases spill into after-hours. Without that distribution, quality improvement efforts cannot target the right point of intervention. We asked three questions:

1. How is overtime distributed across rooms and time within one tertiary centre?
2. Which mechanism (late starts, individual case overruns, or mid-day cascading) accounts for most of the overtime?
3. How do urgent cases interact with the elective programme to produce spillover into staffed-down hours?

## Methods

### Setting

Campus Genk is a tertiary centre within the ZOL network in Limburg, Belgium, performing more than 22,000 surgical procedures per year. It operates 18 surgical theatres, 7 interventional theatres, and an ambulatory anaesthesia unit covering endoscopy, IVF, and MKA sedation. The surgical staff includes 195 surgeons and 207 anaesthesiologists (including trainees and fellows), covering all surgery except congenital cardiac surgery and organ transplantation. Staffing runs 2 to 3 nurses per operating room during the day shift, with the stepwise reductions described above.

### Data and inclusion

We used administrative OR data from 1 January 2022 to 31 May 2025, covering 79,352 cases in the 18 surgical operating rooms, involving 60,895 unique patients, 195 surgeons, 207 anaesthesiologists, and 1,276 distinct procedure names. The admission mix was 42.3% ambulatory and 57.7% inpatient. The hospital's clinical team confirmed that room-in and room-out are the only reliable time markers in the registration pipeline. All timing analyses therefore use those two time points. Induction, recovery, and ward-transfer marks are recorded in the electronic health record but were not used.

### Variables

We followed the glossary of Bauer et al.^10^ for variable definitions: planned duration, observed duration, planning deviation, scheduled start, actual start, start-time deviation, room-out time, overtime flag (room-out after the assigned shift end), overtime minutes, room-swap flag (actual room differs from planned room), urgency at planning (elective versus non-elective), and shift label (day 08:00-16:30, evening 16:30-22:00, night 22:00-08:00). We chose room-level overtime as the primary metric rather than aggregate utilisation, following the argument that utilisation figures hide room-level operational problems when interpreted without staffing context.^11,12^

### Overtime definition

Each case was assigned to one of three shift buckets based on its actual room-in time: day (08:00 to 16:30), evening (16:30 to 22:00), or night (22:00 to 08:00). A case was flagged as after-hours if its room-out time fell after the end of its assigned shift. Overtime minutes equal the difference between room-out and shift end, floored at zero. A day-shift case ending at 17:00 has 30 minutes of overtime; an evening-shift case ending at 23:00 has 60 minutes; a night-shift case ending at 09:00 has 60 minutes. Cases finishing within their assigned shift have zero overtime, regardless of which shift that is. We chose this shift-based definition because the staffing change at each shift boundary is the operational event that gives overtime its meaning at this site. The definition aligns with the overtime framework in Bauer et al.^10^ and with the hospital's own framing of surgical activity past the day-shift staffing window.

### Overlap definition

An urgent case was deemed to overlap with an elective case when the urgent case's actual room matched the elective case's planned room and the urgent case's actual time interval (room-in to room-out) overlapped with the elective case's planned time interval (planned start to planned end). The day-level overlap metric counts the number of distinct calendar days on which at least one such overlap occurred. The case-level metric counts whether a given elective case's planned slot was overlapped by an urgent case in the same room.

### Analyses

All analyses are descriptive; we did not fit causal or inferential models. Analysis was organised into three blocks corresponding to the three research questions.

For burden and concentration, we computed case-level overtime rate, mean, median, and 95th percentile, stratified by room, weekday, year, and shift, with room-level concentration as the primary analytic focus.

For mechanism, we assessed start-time deviation per case and per room, duration deviation by planned-duration bucket using coefficients of variation,^13,14^ and shift displacement (cases performed in a different shift than originally planned, with mean start delay and mean planning deviation).

For daily disruptors, we calculated the urgency mix and its timing, urgent-elective overlap in the same operating room per day and per room, and the effect of overlap on elective start delay.

Room swaps (0.7% of cases) and idle time between cases (median 8 minutes, with gaps exceeding 60 minutes excluded as planned downtime) were assessed separately and are reported as non-bottlenecks in the results text, with full data in the online supplement.

### Ethics

This study used fully de-identified administrative data with institutional approval. No patient interaction occurred.

## Results

### Sample overview

The cohort comprised 79,352 cases across 18 surgical operating rooms at Campus Genk, involving 60,895 unique patients, 195 surgeons, and 207 anaesthesiologists performing 1,276 distinct procedure types. Weekday volume was evenly distributed (17.9 to 20.0% Monday through Friday); weekends accounted for 1.8 to 2.1% of cases. Year-on-year volume grew from 22,133 cases in 2022 to 23,738 in 2024, with 9,906 recorded in 2025 through May. The urgency mix was 85.4% elective and 14.6% non-elective.

### Planning accuracy

Of all cases, 45.7% ran longer than planned and 54.3% ran shorter. The mean overrun was 22.6 minutes (median 14); the mean underrun was 21.2 minutes (median 12). On average, the planning system was roughly unbiased. The problem was dispersion. The coefficient of variation of observed duration was lowest for mid-length cases (0.35 to 0.36 for 61 to 180 minutes), moderate for short cases (0.61 for cases under 30 minutes), and intermediate for very long cases (0.42 for cases over 180 minutes). Planning-deviation CV followed the same pattern but was more extreme: the over-180-minute bucket had a CV of 1.86 (Supplementary Table S1). The procedures with the largest absolute deviations included complex cardiac cases (AVR, CABG off-pump) and oncology procedures (debulking with HIPEC), the same procedure types concentrated in the rooms with the highest overtime.

### Overtime burden

Of 79,352 cases, 7,729 (9.7%) ran past the end of their assigned shift. Among overtime cases, the mean overtime was 60.3 minutes, the median 39 minutes, and the 95th percentile 197 minutes (Table 1). The rate was similar across weekdays (8.8 to 9.9%) but roughly 1.7 times higher on weekends (Saturday 16.8%, Sunday 15.5%), when volume is almost entirely non-elective. The year-on-year trend showed slow improvement: 10.0% in 2022, 10.0% in 2023, 9.7% in 2024, and 8.6% in the partial 2025 data, a gradual decline rather than a step change.

**[Table 1. Overtime summary by weekday and year. Rows: Monday through Sunday, plus yearly breakdown (2022-2025). Columns: number of cases, number with overtime, overtime percentage, mean overtime minutes. Source: In-Depth Analysis Table 24, Figures 16-17, 19.]**

### Room-level concentration

The within-campus spread in overtime rates ran from 3.5% to 32.9% across the 18 surgical rooms (Figure 2). GO10, which handles complex cardiac surgery (CABG, aortic valve replacement, mitral valve repair, MIDCAB, mini-maze ablation), ran overtime on 32.9% of its 1,743 cases, with a mean overrun of 154 minutes and a 95th percentile of 328 minutes. In this room, one in every three cases ran into after-hours. A second tier of rooms (GO08 through GO13) clustered at 11 to 16%. At the other end, GO14 had an overtime rate of 3.5% across 6,885 cases, and GO01 ran 5.8% across 6,577 cases. The within-campus spread (nearly ten-fold, from 3.5% to 32.9%) exceeded the between-campus spread across the entire ZOL network, where overtime rates ranged from 0.5% at Lanaken to 9.7% at Genk.

**[Figure 2. Room-level overtime concentration at Campus Genk. Horizontal bar chart with one bar per operating room, ordered descending by overtime rate. A secondary panel shows mean overtime minutes per room. GO10 (32.9%) and GO14 (3.5%) anchor the extremes. Caption: 7,729 of 79,352 cases (9.7%), mean 60.3 min, median 39 min, P95 197 min. Source: In-Depth Analysis Table 25.]**

Most overtime cases ended shortly after the shift boundary. The majority of overtime completions fell in the 16:30 to 17:30 window, when staffing had just dropped from 25 to 8 rooms. The distribution decayed rapidly through the evening, with a thin tail past 22:00 (Supplementary Figure S2).

### Shift displacement and its link to overtime

A total of 4,151 cases (5.2%) were performed in a different shift than originally planned (Figure 3). These displaced cases had a mean start delay of 398 minutes, roughly six and a half hours. Yet their mean duration was 22.3 minutes shorter than planned, and their mean overtime was only 10.4 minutes. The displaced cases did not run long. They finished on time or early. They landed past the shift boundary because upstream cases pushed them there.

Shift displacement matters for overtime because of the staffing pyramid. A case displaced past 16:30 arrives in a setting where 25 rooms have dropped to 8, covered by different staff than those who started the day. Even if the displaced case itself barely overruns, it is consuming after-hours staffing capacity and exposing its team to the handover and fatigue risks that the staffing change creates. Displacement is the mechanism by which daytime scheduling failures become overtime problems.

The monthly trend showed modest improvement, declining from 7 to 8% of cases displaced in early 2022 to 3 to 5% by 2024 (Supplementary Figure S2).

**[Figure 3. Shift displacement as the overtime mechanism. Summary of 4,151 cases (5.2% of total) displaced into a different shift than planned. Four annotated numbers: mean start delay 398 minutes, mean duration deviation -22.3 minutes (shorter than planned), mean overtime 10.4 minutes, share of total 5.2%. Source: In-Depth Analysis Table 39.]**

### Urgent-elective interaction

Urgent cases constituted 14.6% of volume (11,616 of 79,352). Per case, urgent surgery ran after-hours at more than twice the rate of elective surgery (18.2% versus 8.3%, Table 2). The 95th percentile of overtime minutes was longer for urgent cases (69 versus 29 minutes), indicating heavier tails. The unconditional mean overtime, calculated across all cases including those with zero overtime, was 10.7 versus 5 minutes. Because elective cases outnumbered urgent cases nearly six to one, the absolute volume of after-hours minutes was still dominated by the elective programme.

Urgent-elective overlap in the same operating room occurred on 858 of 1,247 observation days (68.8%), making it a daily occurrence rather than an exceptional one. On days with overlap, elective cases started roughly 30 minutes later than on days without overlap, a gap that reached 60 minutes in early 2022 before narrowing. GO11 absorbed the highest absolute overlap burden, with 475 overlap events affecting 15.2% of its elective cases, and functioned as a de facto urgent-intake room (Supplementary Table S4).

**[Table 2. Urgent versus elective overtime and overlap. Panel A: volume, after-hours rate, mean overtime, and P95 overtime by urgency. Panel B: overlap frequency (858/1,247 = 68.8% of days), mean start-delay effect (+30 min), and GO11 burden. Source: In-Depth Analysis Tables 33, 35, 37, 38.]**

### Non-mechanisms

Room swaps affected 0.7% of cases (519 of 79,352). The overtime rate among swapped cases was 14.8% versus 9.7% among non-swapped cases. Swapped cases were associated with a higher overtime rate, but whether swaps contribute to overtime (through disruption) or result from it (through reactive rescheduling) cannot be determined from these data. At 0.7% of total volume, their absolute contribution to overtime was small in either case (Supplementary Table S3). Idle time between consecutive cases had a median of 8 minutes and a mean of 9.9 minutes, with a 95th percentile of 25 minutes. Turnover was fast and consistent across rooms. Idle time was not the bottleneck (Supplementary Figure S1).^31^

First-case punctuality was not associated with room-level overtime. GO10 had the best start-time punctuality among the 18 surgical rooms (46.1% late) yet the worst overtime (32.9%). GO14 had the second-worst punctuality (78.7% late) yet the lowest overtime (3.5%). GO11 had the worst punctuality (82.4% late, with a mean delay of 319 minutes driven by its role as the urgent-intake room) yet mid-pack overtime (11.7%). Across the 18 rooms, late-start frequency showed no consistent association with overtime rate (Supplementary Table S2). This is consistent with Pandit et al., who reported R-squared values of 0.04 to 0.08 between start and finish times across more than 7,000 theatre lists in two UK hospitals.^16^

## Discussion

### Concentration, not prevalence

A campus-wide overtime rate of 9.7% is unremarkable. What is unusual is how uneven the distribution is. GO10 ran overtime in one of every three cases, with a mean overrun of more than two and a half hours. GO14, in the same building, ran overtime on 3.5% of cases. The spread within this single campus (3.5 to 32.9%, nearly ten-fold) was wider than the spread between campuses across the ZOL network (0.5 to 9.7%).

Hospital-wide targets such as "reduce overtime by 10%" will miss the problem unless they are decomposed by room. The overtime is already concentrated; the intervention should be too. Zhang, Dunstan, and Pandit made the same point in their tutorial on capped utilisation: aggregate metrics hide room-level operational reality.^12^ A separate argument that valid OR metrics are a prerequisite for quality improvement has been made elsewhere.^32^

The data also do not support the first-case-on-time-start (FCOTS) narrative. The conventional view holds that first-case punctuality drives end-of-day performance, and that each minute of tardiness carries a marginal cost.^15^ In our data, room-level start-time punctuality was not associated with overtime rate. The room with the best punctuality (GO10, 46.1% late) had the worst overtime (32.9%), while a room with among the worst punctuality (GO14, 78.7% late) had the lowest overtime (3.5%). Pandit et al. reported a similar disconnect, with R-squared values of 0.04 to 0.08 between start and finish times across more than 7,000 theatre lists in two UK hospitals.^16^ FCOTS may be a useful discipline marker, but on its own it does not appear to be a reliable lever for reducing overtime.

### Cascading as the dominant mechanism

The 4,151 shift-displaced cases finished on time or early (mean duration deviation of minus 22.3 minutes), yet they were pushed past the shift boundary by a mean start delay of 398 minutes. If overtime were primarily caused by individual cases running long, displaced cases would show positive duration deviations. Instead, they ran shorter than planned while starting nearly seven hours late. This pattern points to upstream delay accumulation rather than the displaced cases themselves overrunning.

The cascading pattern has been described before. Wachtel and Dexter showed in a large operational dataset that tardiness per case grew larger as the day progressed, because the total duration of preceding cases increased.^18^ Fugener et al. demonstrated systematic biases in surgeons' duration estimates (planning fallacy, anchoring), which compound the cascade: each underestimated case pushes the next one later.^19^ Our minus-22.3-minute duration deviation is consistent with displaced cases being compressed or truncated to fit a shrinking window. Joseph et al. documented how minor flow disruptions cluster and escalate into major ones.^20^ A systematic review of operating-room workflow disruptions estimated that approximately 20% of operating time involves disruptions, although the evidence for direct linkage to surgical outcomes is mixed.^21^

If the mechanism is cascading rather than individual long-running cases, the intervention point is earlier in the day. The targets are scheduling density, buffer placement, and urgent-case routing, rather than end-of-list management.

### Urgent-elective interaction

Urgent cases ran after-hours at more than twice the rate of elective cases (18.2% versus 8.3%), with heavier tails (P95 69 versus 29 minutes). Because elective cases were nearly six times more numerous, the absolute volume of after-hours minutes was dominated by the elective programme. Overlap between urgent and elective cases in the same room occurred on 68.8% of observation days, adding roughly 30 minutes to elective start times.

This is not an argument to restrict urgent access. It is an argument to protect the elective programme from predictable disruption, either through dedicated urgent rooms or through scheduling buffers on days with historically high urgent volume. GO11 already absorbs a large share of the overlap and functions as the designated urgent-intake room. The unpredictability of the overlap has a workforce dimension, since both long shifts and overtime are associated with worse performance and wellbeing.^22^

### Staff and patient consequences

This paper does not measure outcomes directly. It characterises an exposure: cases and staff pushed into understaffed hours. Published evidence documents consequences at both ends.

On the staff side, overtime and long shifts are associated with burnout, reduced perceived care quality, and intent to leave.^2,3,4^ Both long shifts and overtime are associated with worse performance and wellbeing,^22^ and high workload combined with low decision latitude is an established burnout predictor.^23^ In two Belgian university hospitals, workload and unit-level nurse management were the strongest predictors of burnout and job outcomes.^24^ The HSSIB 2025 national investigation named staff fatigue as a patient-safety problem, linking the two sides of the argument.^8^

On the patient side, after-hours surgery carries elevated mortality in meta-analytic and cohort data,^5,6^ although the effect size is contested.^25^ Each intraoperative handover raises complication risk,^7^ although recent sub-specialty data have produced mixed results.^26^ Structured handover programmes can reduce adverse events: in the I-PASS paediatric inpatient resident-handoff trial, preventable adverse events dropped by 30%.^27^ Reducing intern shifts from extended (longer than 24 hours) to intervention schedules produced 36% fewer serious medical errors in an ICU setting.^29^ Extended-duration shifts were associated with 3.5- to 7.5-fold higher odds of fatigue-related significant medical errors in a prospective intern cohort.^28^ A systematic review of physician fatigue confirmed associations with physician health outcomes, with mixed evidence for direct effects on surgical patient outcomes.^30^ Overtime hours above a breakpoint threshold have been associated with a 2.09% increase in pressure ulcers across 70 US hospitals.^9^

In a hospital where 25 rooms drop to 8, then 4, then 1, each case pushed past the shift boundary lands in a setting with fewer staff, more handovers, and a fatigued workforce. The exposure we document is the upstream condition for both classes of harm.

### Limitations

This study has several limitations. It is a single-site retrospective analysis of one Belgian tertiary centre, so whether the concentration and cascading patterns hold in hospitals with different staffing models is unknown. The administrative data provide room-in and room-out times only, so we cannot decompose what happens inside the case. We do not measure patient or staff outcomes directly; the harm argument rests on published literature, not on complications or burnout scores from this cohort. Phase 2 of the research programme will link the operational patterns to complication and readmission data. The urgency flag is set at booking, and we cannot distinguish truly emergent cases from semi-urgent or add-on elective cases. GO10 handles complex cardiac surgery, and its high overtime may partly reflect irreducible procedural duration rather than schedulable inefficiency; we describe this but cannot adjust for it without procedure-level risk scores. Finally, the link between after-hours surgery and patient harm rests partly on observational mortality studies whose effect sizes range widely (adjusted OR 1.16 in the 2020 meta-analysis^5^ to 3.58 in the 2024 South Korean cohort^6^) and whose estimates have been questioned on residual-confounding grounds.^25^ Our paper does not measure patient outcomes directly; readers should weigh the after-hours mortality evidence with this uncertainty in mind.

## Conclusion

Operating-room overtime at this tertiary centre is not a diffuse hospital-wide problem. It is concentrated in a small number of rooms, driven primarily by mid-day cascading rather than individual case overruns, and amplified by daily urgent-elective overlap. The staffing pyramid, with 18 rooms dropping to 8, then 4, then 1, means every case pushed past the shift boundary lands in a setting with fewer staff and more handovers. Published evidence links both the staff exposure (fatigue, burnout, intent to leave) and the patient exposure (after-hours surgery, handover transitions) to measurable harm.

The findings argue for room-level rather than hospital-level overtime targets, for scheduling interventions that address mid-day flow rather than first-case punctuality alone, and for prospective outcome linkage in Phase 2 of this research programme.

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

1. Wachtel RE, Dexter F. Review of behavioral operations experimental studies of newsvendor problems for operating room management. *Anesth Analg* 2010;110(6):1698-1710.
2. Griffiths P, Dall'Ora C, Simon M, et al. Nurses' shift length and overtime working in 12 European countries: the association with perceived quality of care and patient safety. *Med Care* 2014;52(11):975-81.
3. Dall'Ora C, Griffiths P, Ball J, et al. Association of 12 h shifts and nurses' job satisfaction, burnout and intention to leave: findings from a cross-sectional study of 12 European countries. *BMJ Open* 2015;5(9):e008331.
4. Bae S-H. Nurse staffing, work hours, mandatory overtime, and turnover in acute care hospitals affect nurse job satisfaction, intent to leave, and burnout: a cross-sectional study. *Int J Public Health* 2024;69:1607068.
5. Cortegiani A, Ippolito M, Misseri G, et al. Association between night/after-hours surgery and mortality: a systematic review and meta-analysis. *Br J Anaesth* 2020;124(5):623-37.
6. Oh T-K, Song I-A. Outcomes of after-hours surgeries performed under general anaesthesia: a South Korean nationwide cohort study. *Anaesthesia* 2025. DOI: 10.1111/anae.16559.
7. Saager L, Hesler BD, You J, et al. Intraoperative transitions of anesthesia care and postoperative adverse outcomes. *Anesthesiology* 2014;121(4):695-706.
8. Health Services Safety Investigations Body (HSSIB). The impact of staff fatigue on patient safety. Investigation report. London: HSSIB, 2025.
9. Pittman P, Tiunn H-L, et al. Increased utilization of overtime and agency nurses and patient safety. *JAMA Netw Open* 2025. PMID: 40172888.
10. Bauer M, Diemer M, Merkel M, et al. Glossary of perioperative process times and indicators. *Anaesthesist* 2020;69(Suppl 1):S5-17.
11. Schouten AEM, Flipse SM, van Nieuwenhuizen KE, et al. Operating room performance optimization metrics: a systematic review. *J Med Syst* 2023;47(1):19.
12. Zhang C, Dunstan C, Pandit JJ. A tutorial on "capped utilisation" as a metric and key performance target in NHS England's Model Hospital operating theatres database: caution for international healthcare systems. *Anesthesiol Perioper Sci* 2024. DOI: 10.1007/s44254-024-00073-3.
13. Strum DP, May JH, Vargas LG. Modeling the uncertainty of surgical procedure times: comparison of log-normal and normal models. *Anesthesiology* 2000;92(4):1160-7.
14. Eijkemans MJ, van Houdenhoven M, Nguyen T, et al. Predicting the unpredictable: a new prediction model for operating room times using individual surgeon-specific historical data. *Anesthesiology* 2010;112(1):41-9.
15. Dexter F, Epstein RH. Typical savings from each minute reduction in tardy first case of the day starts. *Anesth Analg* 2009;108(4):1262-7.
16. Pandit JJ, Abbott T, Pandit M, et al. Is "starting on time" useful (or useless) as a surrogate measure for "surgical theatre efficiency"? *Anaesthesia* 2012;67(8):823-32.
17. Macario A. Are your hospital operating rooms "efficient"? A scoring system with eight performance indicators. *Anesthesiology* 2006;105(2):237-40.
18. Wachtel RE, Dexter F. Influence of the operating room schedule on tardiness from scheduled start times. *Anesth Analg* 2009;108(6):1889-1901.
19. Fugener A, Schiffels S, Kolisch R. Overutilization and underutilization of operating rooms: insights from behavioral health care operations management. *Health Care Manag Sci* 2017;20(1):115-28.
20. Joseph A, Khoshkenar A, Taaffe KM, et al. Minor flow disruptions, traffic-related factors and their effect on major flow disruptions in the operating room. *BMJ Qual Saf* 2019;28(4):276-83.
21. Koch A, Burns J, Catchpole K, Weigl M. Associations of workflow disruptions in the operating room with surgical outcomes: a systematic review and narrative synthesis. *BMJ Qual Saf* 2020;29(12):1033-1045.
22. Dall'Ora C, Ball J, Recio-Saucedo A, Griffiths P. Characteristics of shift work and their impact on employee performance and wellbeing: a literature review. *Int J Nurs Stud* 2016;57:12-27.
23. Dall'Ora C, Ball J, Reinius M, Griffiths P. Burnout in nursing: a theoretical review. *Hum Resour Health* 2020;18:41.
24. Van Bogaert P, Peremans L, Van Heusden D, et al. Predictors of burnout, work engagement and nurse reported job outcomes and quality of care: a survey among hospital nurses in Belgium. *BMC Nurs* 2017;16:5.
25. Sakurai T. Assessing the influence of after-hours surgery: concerns with the confounders and conclusion. *Anaesthesia* 2025. DOI: 10.1111/anae.16591.
26. Guerra-Londono JJ, et al. The impact of intraoperative anesthesiology provider handovers on postoperative complications after hepatopancreatobiliary surgery. *J Surg Oncol* 2025. PMID: 39388390.
27. Starmer AJ, Spector ND, Srivastava R, et al. Changes in medical errors after implementation of a handoff program. *N Engl J Med* 2014;371(19):1803-12.
28. Barger LK, Ayas NT, Cade BE, et al. Impact of extended-duration shifts on medical errors, adverse events, and attentional failures. *PLoS Med* 2006;3(12):e487.
29. Landrigan CP, Rothschild JM, Cronin JW, et al. Effect of reducing interns' work hours on serious medical errors in intensive care units. *N Engl J Med* 2004;351(18):1838-48.
30. Gates M, Wingert A, Featherstone R, et al. Impact of fatigue and insufficient sleep on physician and patient outcomes: a systematic review. *BMJ Open* 2018;8(9):e021967.
31. MacMillan L, et al. What affects operating room turnover time? A systematic review and mapping of the evidence. *Surgery* 2025. PMID: 40054053.
32. Zhang C, Pandit JJ. Getting operating theatre metrics right to underpin quality improvement. *Br J Anaesth* 2023;131(1):130-4.
