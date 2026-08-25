# Where operating-room overtime concentrates and why: a retrospective single-centre study

[Authors and affiliations removed for blinded review]

**Correspondence:** [removed for blinded review]

**Word count:** 3,094 (body text, excluding abstract, tables, and references)

**Keywords:** operating room, overtime, scheduling, patient safety, staff wellbeing, quality improvement

---

## ABSTRACT

**Background.** Operating-room overtime is associated with higher patient mortality and staff burnout, and it costs roughly twice as much per minute as underutilised time. Most studies report overtime as a hospital-wide aggregate, which can obscure where the problem concentrates and misdirect improvement efforts.

**Objective.** To characterise operating-room overtime within a high-volume tertiary hospital: its distribution across rooms and the operational factors associated with it.

**Design and setting.** Retrospective observational study using administrative operating-room data from a 24/7 tertiary hospital in Belgium with 18 surgical operating rooms.

**Participants.** 79,352 surgical procedures performed between January 2022 and May 2025.

**Main outcome measures.** Case-level overtime (time past the assigned shift end), by room, weekday, shift, and urgency. Start-time deviation, duration-estimation accuracy, and unplanned urgent-case disruption of the elective programme as candidate contributing factors.

**Results.** Of 79,352 cases, 7,729 (9.7%) ran past the end of their assigned shift, with a mean overtime of 60.3 minutes and a 95th percentile of 197 minutes. Overtime concentrated in a few rooms: OR10 ran overtime on 32.9% of its cases (mean 154 minutes), while OR14 ran 3.5%. Urgent cases ran after-hours at more than twice the elective rate (18.2% versus 8.3%). Unplanned urgent cases disrupted the elective programme on 68.8% of observation days, with a median difference of approximately 30 minutes in elective start times. Start-time punctuality showed no association with room-level overtime, whereas rooms with longer gaps between cases also had higher overtime rates.

**Conclusions.** Overtime was concentrated in a small number of rooms, driven by case-mix complexity and routine urgent-case disruption of the elective programme. Room-level monitoring and scheduling that accounts for urgent-case flow are more actionable targets than start-time punctuality.

---

## KEY MESSAGES

**What is already known on this topic**

- Operating-room overtime is associated with higher patient mortality and staff burnout, and overutilised time costs roughly twice as much per minute as underutilised time. Prior work has largely reported overtime as a hospital-wide aggregate, which can obscure where the problem actually resides.

**What this study adds**

- In a single-centre retrospective analysis of 79,352 surgical cases, overtime concentrated in a few rooms, with a nearly ten-fold spread within one hospital (3.5% to 32.9%). Case-mix complexity and unplanned urgent cases disrupting the elective programme were the factors most visibly associated with room-level overtime, and rooms with longer gaps between cases also ran more overtime; start-time punctuality was not associated with room-level overtime.

**How this study might affect research, practice or policy**

- Hospitals seeking to reduce overtime should monitor and target individual rooms rather than hospital-wide averages, and should treat urgent-case flow as a routine scheduling input rather than an exception. Linking these operational patterns to patient and staff outcomes is a necessary next step.

---

## INTRODUCTION

Operating rooms are among the most resource-intensive units in a hospital, and actual schedules routinely diverge from planned ones. Overtime in this setting can refer to several distinct phenomena: an individual case running longer than its booked duration, an operating list ending after its scheduled close, or surgery continuing into a period when different staff are rostered. These are different operational events with different consequences. Standardised glossaries of perioperative process times define overrun and utilisation relative to allocated operating-room capacity.[1] We instead define overtime against the staffing boundary, in line with the staff-overtime literature, where overtime is work beyond contracted hours;[2] the change of nursing staff at each shift end is the operational event that gives overtime its meaning at this site. Overutilised time costs roughly double what underutilised time does,[3] but overtime is more than a budget problem.

A case that runs past its shift boundary continues into the next shift, when a different team is on duty. Most overtime at this site crosses the day-to-evening boundary, so the after-hours surgery literature is directly relevant. That literature defines the exposure by clock time rather than by a staffing boundary. Overtime and after-hours surgery are not identical, but overtime is one of the routes by which scheduled daytime work ends up being performed after hours, so the harms reported for after-hours surgery are relevant. After-hours surgery has been linked to higher patient mortality. A meta-analysis pooling 18 studies found an adjusted odds ratio of 1.16 (95% CI 1.06 to 1.28), graded as low-certainty evidence.[4] A propensity-matched cohort study of 281,717 South Korean patients found a larger effect for 90-day mortality (odds ratio 3.58), although that estimate has been challenged on residual-confounding grounds.[5,6] In a multicentre cohort of more than 350,000 non-cardiac surgical cases, night surgery was associated with increased morbidity (adjusted odds ratio 1.41), mediated partly by higher transfusion rates and provider handovers during the case.[7] A systematic review of elective non-cardiac surgery confirmed the direction: evening and night procedures carried higher mortality and morbidity than daytime procedures, although the quality of evidence was low.[8] Each intraoperative anaesthesia handover raises the odds of a major composite complication, with incidence rising from 8.8% at zero transitions to 21.2% at four or more.[9] A 2025 UK national patient-safety investigation into staff fatigue cited a Medical Defence Union survey of 481 doctors in which 22% reported daily sleep deprivation and 35% said tiredness had impaired their ability to treat patients, with long shifts and overtime among the contributing factors.[10] Overtime above a breakpoint threshold has been associated with a 2.09% increase in pressure ulcers across 70 US hospitals.[11]

The consequences for staff are also well documented. A 12-country European nurse workforce study linked overtime and long shifts to poorer perceived quality of care and higher patient safety risk.[2] The companion study tied 12-hour shifts to burnout and intent to leave.[12] Mandatory overtime was associated with intent to leave in a 2024 cross-sectional study of 264 South Korean nurses.[13] Both long shifts and overtime are associated with worse performance and well-being,[14] and the combination of high workload and low decision latitude is an established burnout predictor.[15]

The severity of these consequences depends on what happens at the shift boundary. In hospitals that step staffing down sharply at the end of the day shift, a case running past the boundary continues with fewer rooms open and with nursing staff who were not present at the start of the case.

Prior work on operating-room (OR) overtime has largely treated it as an aggregate site-level number.[16,17] Workflow disruptions consume a substantial share of operating time,[18] and minor disruptions can escalate into major ones.[19] Whether overtime concentrates in specific rooms within a single hospital, and which operational factors are associated with it, remain open questions. Without that granularity, quality improvement efforts risk targeting the wrong intervention point.

This study is part of a broader programme at the study hospital to improve OR performance. Using administrative data, we address two research questions:

1. How is overtime distributed across rooms and time within one tertiary hospital (RQ1)? This examines whether overtime is a diffuse, hospital-wide problem or concentrated in specific rooms, since the appropriate intervention point depends on its distribution.
2. Which operational factors (duration overruns, urgent-elective interaction, and start-time punctuality) are associated with overtime (RQ2)? This tests which candidate factors identified in the literature are visible in our data, to inform where scheduling interventions should be directed.

## METHODS

### Setting and data

The study hospital is a 24/7 tertiary centre in Belgium performing more than 22,000 surgical procedures per year. It operates 18 surgical operating rooms and 7 interventional operating rooms. The surgical staff includes 195 surgeons and 207 anaesthesiologists (including trainees and fellows), covering all surgical specialities except congenital cardiac surgery and organ transplantation. During the 08:00 to 16:30 day shift, each room is staffed with 2 to 3 nurses; at 16:30 the hospital reduces to 8 staffed rooms, at 17:30 to 4, and overnight to a single room.

We used administrative OR data from 1 January 2022 to 31 May 2025 from the 18 surgical operating rooms. Endoscopy suites and catheterisation laboratory cases without an anaesthesiologist present were excluded. Cases with implausible timestamps (zero observed duration, planned duration exceeding 24 hours, or extreme deviations from the planned schedule) were also removed. The final cohort comprised 79,352 cases involving 60,895 unique patients and 1,276 distinct procedure types. The admission mix was 42.3% ambulatory and 57.7% inpatient (ambulatory patients are discharged on the day of surgery; inpatient patients are admitted overnight). Room-in and room-out times are the only procedural time markers confirmed as reliable by the hospital's clinical team; all timing analyses use these two time points. The administrative system also records planned duration, urgency (cases scheduled or performed within 24 hours of booking were classified as non-elective, hereafter referred to as urgent; all others were classified as elective), and room assignment. From these inputs we derived observed duration, planning deviation, and start-time deviation following standard perioperative process-time definitions,[1] and additionally defined an overtime flag and overtime minutes, a room-swap flag, and a shift label (defined below).

### Overtime definition and analyses

Each case was assigned to a shift based on its actual room-in time: day (room-in from 07:30 to 16:30, shift end 16:30), evening (room-in from 16:30 to 22:00, shift end 22:00), or night (room-in from 22:00 to 07:30, shift end 08:00). The same boundaries were applied on weekends. A case was flagged as overtime if its room-out fell after the end of its assigned shift; overtime minutes equal the positive difference between room-out and shift end. We chose this shift-based definition because the change of nursing staff at each boundary is the operational event that makes overtime consequential at this site. Room-level overtime was the primary metric because aggregate utilisation measures can misrepresent the performance of individual rooms[16] and published OR performance metrics lack standardised definitions.[20]

All analyses are descriptive; we did not fit causal or inferential models. For RQ1, we computed overtime rate, mean, median, and 95th percentile, stratified by room, weekday, year, and shift. For RQ2, we examined duration deviation by planned-duration bucket using coefficients of variation,[21,22] urgency mix and timing, urgent-elective interaction (defined and reported in Results), start-time deviation per room, inter-case idle time, and room swaps. Inter-case idle time was measured during the day shift as the gap between consecutive cases in the same room, including the gap from shift start to the first case and excluding gaps longer than 60 minutes as planned downtime. An urgent-elective overlap was flagged when an urgent case occupied a room during a window in which an elective case had been planned in that room; start-delay comparisons are made at case level between overlapped and non-overlapped elective cases. Spearman rank correlations across the 18 rooms were computed between room-level overtime rate and two candidate factors: late-start rate and mean inter-case idle time. Intermediate findings were reviewed with the clinical team and used to refine variable definitions and exclusions. The study is reported in accordance with the STROBE guidelines for observational studies.

### Ethics

This study used fully anonymised administrative data with institutional approval. No patient interaction occurred.

### Patient and public involvement

Given the retrospective use of fully anonymised administrative data, no patient or public involvement was sought.

## RESULTS

### Sample overview

The cohort comprised 79,352 surgical cases performed on 60,895 unique patients across 18 operating rooms between January 2022 and May 2025 (Table 1). Cases covered 1,276 distinct procedure types performed by 195 surgeons and 207 anaesthesiologists. The urgency mix was 85.4% elective and 14.6% urgent (non-elective); 42.3% of cases were ambulatory, and almost all activity (96.1%) fell on weekdays. Annual volume grew from 22,133 in 2022 to 23,738 in 2024, with 9,906 cases recorded through May 2025.

**Table 1. Study cohort characteristics.** (*2025 partial, January–May.)

| Characteristic | Value |
|----------------|-------|
| Surgical cases | 79,352 |
| Unique patients | 60,895 |
| Surgical operating rooms | 18 |
| Distinct procedure types | 1,276 |
| Surgeons | 195 |
| Anaesthesiologists | 207 |
| Study period | January 2022 – May 2025 |
| **Admission type**, n (%) | |
| Ambulatory (day surgery) | 33,566 (42.3) |
| Inpatient | 45,786 (57.7) |
| **Urgency**, n (%) | |
| Elective | 67,736 (85.4) |
| Urgent (non-elective) | 11,616 (14.6) |
| **Timing**, n (%) | |
| Weekday | 76,255 (96.1) |
| Weekend | 3,097 (3.9) |
| **Cases by year**, n | |
| 2022 | 22,133 |
| 2023 | 23,575 |
| 2024 | 23,738 |
| 2025* | 9,906 |

### Overtime burden and room-level concentration (RQ1)

Of 79,352 cases, 7,729 (9.7%) ran past the end of their assigned shift. Among overtime cases, the mean was 60.3 minutes, the median was 39 minutes, and the 95th percentile (P95) was 197 minutes (Table 2A). Weekday rates were similar (8.8 to 9.9%) but roughly 1.7 times higher on weekends (Saturday 16.8%, Sunday 15.5%), when the elective programme does not run and volume is almost entirely urgent surgery. The overtime rate declined gradually over the study period: 10.0% in 2022, 10.0% in 2023, 9.7% in 2024, and 8.6% in the first five months of 2025 (Table 2B).

**Table 2A. Overtime by weekday.** (OT, overtime; rates and means among overtime cases.)

| Day | n cases | n overtime | OT rate (%) | Mean OT (min) |
|-----|--------:|-----------:|------------:|--------------:|
| Monday | 14,232 | 1,395 | 9.8 | 58.5 |
| Tuesday | 14,750 | 1,416 | 9.6 | 60.1 |
| Wednesday | 15,814 | 1,502 | 9.5 | 59.7 |
| Thursday | 15,844 | 1,394 | 8.8 | 60.5 |
| Friday | 15,615 | 1,546 | 9.9 | 62.4 |
| Saturday | 1,654 | 278 | 16.8 | 63.4 |
| Sunday | 1,443 | 224 | 15.5 | 59.1 |
| **Total** | **79,352** | **7,729** | **9.7** | **60.3** |

**Table 2B. Overtime trend by year.** (OT, overtime; *2025 partial, January–May.)

| Year | OT rate (%) | Mean OT (min) | Median OT (min) |
|------|------------:|--------------:|----------------:|
| 2022 | 10.0 | 61.8 | 40 |
| 2023 | 10.0 | 58.8 | 38 |
| 2024 | 9.7 | 61.3 | 39 |
| 2025* | 8.6 | 58.2 | 37 |

Room-level overtime rates ranged from 3.5% to 32.9% across the 18 rooms (Figure 1). OR10, which handles complex cardiac surgery (coronary artery bypass grafting, aortic valve replacement, mitral valve repair), ran overtime on 32.9% of its 1,743 cases, with a mean of 154 minutes and a 95th percentile of 328 minutes. A second tier (OR08 through OR13) clustered at 11–16%. At the other end, OR14 ran 3.5% across 6,885 cases and OR01 ran 5.8% across 6,577. Rates spanned nearly an order of magnitude within a single hospital.

[Insert Figure 1 about here]

Most overtime cases ended shortly after the shift boundary. More than half of overtime completions fell in the 16:30 to 17:30 window, immediately after the day-shift handover. The distribution decayed through the evening, with a thin tail past 22:00 (Supplementary Figure S1).

### Contributing factors (RQ2)

*Planning accuracy.* Of all cases (not only those with overtime), 45.7% ran longer than planned and 54.3% ran shorter. The mean overrun was 22.6 minutes (median 14) and the mean underrun was 21.2 minutes (median 12). Overruns and underruns were similar in both size and frequency, so the planning system showed no systematic bias: bookings were not consistently too tight or too generous, and no fixed padding factor would correct the schedule. The problem was variability. Two cases booked for the same duration could finish well apart, and that spread, rather than a tendency to under-book, is what pushes a list past its boundary.

We measured this spread with the coefficient of variation (CV), the standard deviation of duration divided by its mean, which places cases of different lengths on a comparable scale. Observed-duration CV was highest for short cases (0.54 for procedures under 30 minutes), lowest for mid-length cases (about 0.35 for 61 to 180 minutes), and intermediate for the longest cases (0.42 for over 180 minutes); short cases are proportionally the most variable because a few extra minutes is a large fraction of a brief booking. The CV of the planning error itself was higher still, reaching 1.84 in the over-180-minute bucket, where the spread of the booking error was nearly twice its own average. The schedule was therefore least able to predict the finishing time of the longest cases. These procedures, mainly complex cardiac and oncology cases, clustered in the rooms with the highest overtime, so the rooms that were hardest to plan were also the ones that most often ran late.

*Urgent-elective interaction.* Urgent cases accounted for 14.6% of the volume (11,616 of 79,352) and ran past the shift boundary at more than twice the elective rate (18.2% versus 8.3%, Table 3A), with heavier tails (P95: 69 versus 29 minutes). Because elective cases outnumbered urgent cases nearly six to one, the absolute volume of overtime minutes was still dominated by the elective programme.

To assess whether urgent cases disrupt the elective programme, we flagged elective cases whose planned room and time window were occupied by an urgent case. Such overlap occurred on 858 of 1,247 observation days (68.8%, Table 3B). Elective cases affected by an overlap started later than unaffected elective cases: at OR11, the emergency-designated room that absorbed the highest overlap burden (475 events, 15.2% of its elective cases), the median start delay was 60 minutes with overlap versus 28 minutes without. In monthly terms, mean start delays for overlapped elective cases exceeded 70 minutes in early 2022, against roughly 30 minutes for unaffected cases, and the gap narrowed over the study period.

**Table 3A. Volume and overtime by urgency.**

| Urgency | n | Share | Overtime n | Overtime rate | Mean OT (min) | P95 OT (min) |
|---------|------:|------:|--------------:|-----------------:|--------------:|-------------:|
| Elective | 67,736 | 85.4% | 5,620 | 8.3% | 5.0 | 29 |
| Non-elective (urgent) | 11,616 | 14.6% | 2,109 | 18.2% | 10.7 | 69 |
| **Total** | **79,352** | **100%** | **7,729** | **9.7%** | – | – |

*OT, overtime. Mean and P95 overtime in this table are computed across all cases in each row, including cases without overtime; Table 2 reports means among overtime cases only.*

**Table 3B. Urgent–elective overlap in the same room.**

| Metric | Value |
|--------|-------|
| Days with at least one urgent–elective overlap | 858 of 1,247 (68.8%) |
| Highest-burden room (OR11) | 475 events; 15.2% of OR11 elective cases |
| Median start delay at OR11 (no overlap) | 28 min |
| Median start delay at OR11 (overlap) | 60 min |

*Start-time punctuality.* A common assumption is that punctual starts, and the first case of the day in particular (first-case-on-time-start, FCOTS), protect the end of the list. Across all cases and rooms, 67.4% started later than planned, with a mean delay of 74.6 minutes and a median of 28 minutes among late cases. We tested a broad version of this hypothesis by correlating each room's late-start rate, computed across all scheduled cases rather than first cases alone, with its overtime rate. The two were not associated (Spearman rho = −0.29, p = 0.24), and the direction was, if anything, negative. OR10 had the lowest late-start rate of all 18 rooms (46.1%) but the highest overtime rate (32.9%), while OR14 started late more often (78.7%) yet ran the least overtime (3.5%). Start-time punctuality therefore did not track where overtime accumulated.

*Inter-case idle time.* Across all 18 rooms, inter-case idle time (the gap between one case's room-out and the next case's room-in, akin to turnover time[23]) had a median of 8 minutes and a mean of 9.9 minutes. At the room level, mean idle time was positively correlated with overtime rate (Spearman rho = 0.91, p < 0.001), and the association was not an artefact of the extreme room: it persisted when OR10, which had both the highest mean idle time (22.6 minutes) and the highest overtime rate (32.9%), was excluded (rho = 0.90, p < 0.001). Rooms with longer gaps between cases therefore also ran more overtime. Both are plausibly markers of case-mix complexity, since complex procedures require longer preparation between cases as well as longer operating times; these cross-sectional correlations cannot separate that account from a turnover effect.

*Room swaps.* Room swaps affected 0.7% of cases (519 of 79,352). Swapped cases had a higher overtime rate (14.8% versus 9.7%), but whether swaps contribute to or result from overtime cannot be determined.

## DISCUSSION

In this single-centre analysis of 79,352 cases, overtime was not a diffuse hospital-wide phenomenon. The aggregate rate (9.7%) hid a near ten-fold spread across rooms (3.5 to 32.9%). The factors most visibly associated with the room-level pattern were case-mix complexity, routine urgent-elective overlap, and longer inter-case gaps; start-time punctuality was not.

### Concentration, not prevalence

A 9.7% hospital-wide overtime rate is unremarkable on its own, but the distribution behind it is uneven: OR10 ran overtime in roughly one of every three cases, while OR14 ran 3.5%. A hospital-wide target such as "reduce overtime by 10%" will not reach the problem unless it is decomposed by room. Zhang, Dunstan and Pandit reached a similar conclusion about NHS England's capped-utilisation target, which discards operating time that runs past the scheduled finish and so misrepresents what individual theatres actually deliver.[16] Charlesworth and Pandit showed more broadly that standard theatre metrics, including start-time compliance and utilisation, are unreliable in isolation because they ignore list composition and scheduling uncertainty.[24] Quality improvement work needs metrics that are valid at the level where decisions are made.[25]

### Factors associated with overtime

Because the procedures with the largest planning deviations and longest planned durations were concentrated in the highest-overtime rooms, case-mix complexity rather than scheduling inefficiency alone most likely accounts for much of the room-level variation. Using a large operational dataset, Wachtel and Dexter showed that tardiness per case grows through the day as the scheduled time preceding each case accumulates,[26] and Fügener et al. documented systematic biases in surgeons' duration estimates under uncertainty.[27] Both observations are consistent with the room-level pattern we describe, although our data cannot test the cumulative-delay account directly.

Urgent-elective overlap occurred on more than two-thirds of observation days and was associated with later elective starts (at the emergency-designated room OR11, a median of 60 versus 28 minutes), making urgent arrivals a routine scheduling factor rather than an exception. The hospital already operates dedicated rooms for urgent cases, yet overlap persists, so protecting the elective programme may require additional scheduling buffers or capacity reallocation rather than reactive rescheduling alone. Parmar et al. proposed a graphical method for identifying when emergency capacity is insufficient from the pattern of delays and utilisation, which could inform such decisions.[28]

The absence of a link between per-room punctuality and overtime runs against the assumption that first-case-on-time-start (FCOTS) drives end-of-day performance, with each minute of tardiness carrying a marginal cost.[29] Pandit et al. found the same disconnect across more than 7,000 operating lists, where start time explained only 4 to 8% of the variance in finish time.[30] We do not conclude that FCOTS is unimportant; it remains a reasonable marker of scheduling discipline. In this hospital, however, it does not predict where overtime accumulates.

### Implications

*Operational implication.* Room-level monitoring should take precedence over hospital-wide overtime targets, because an intervention aimed at the average will miss the rooms that generate most of the overtime. For the highest-overtime rooms, where long complex cases dominate, scheduling systems could assign wider duration margins to procedures with high expected variability rather than applying a uniform padding factor. Urgent-case flow belongs in the schedule itself: given how often urgent and elective work collide, dedicating additional capacity or buffering the elective programme against predictable disruption is more realistic than reactive rescheduling. Start-time compliance, while reasonable to pursue on other grounds, should not be expected to reduce overtime.

*Clinical implication.* The overtime documented here produces the same exposure that other studies have linked to staff fatigue, higher after-hours mortality, and increased complication risk.[2,4–7,9–15] Whether those harms are present at this hospital cannot be determined from administrative data alone. Linking room-level overtime to patient and staff outcomes is a necessary next step.

### Limitations

This study has several limitations. It is a single-site retrospective analysis, so whether the concentration pattern holds across hospitals with different staffing models is unknown. The administrative data provide only room-in and room-out times, so we cannot infer what happens inside the case. We do not measure patient or staff outcomes directly; the harm argument rests on published literature, not on complications or burnout scores from this cohort. OR10 handles complex cardiac surgery, and its high overtime may partly reflect irreducible procedural duration rather than schedulable inefficiency; we describe this but cannot adjust for it without procedure-level risk scores. The link between after-hours surgery and patient harm rests on observational studies whose effect sizes vary widely (adjusted odds ratios of 1.16[4] to 3.58[5]) and whose estimates have been questioned on residual-confounding grounds.[6] Readers should weigh the after-hours mortality evidence with this uncertainty in mind.

## CONCLUSION

Operating-room overtime at this tertiary hospital was concentrated in a small number of rooms. Case-mix complexity, unplanned urgent-case disruption of the elective programme, and longer inter-case gaps were the most visibly associated factors; start-time punctuality was not. The findings support room-level rather than hospital-level overtime monitoring and scheduling interventions that account for urgent-case flow.

---

## ACKNOWLEDGEMENTS

[To be completed]

## COMPETING INTERESTS

None declared.

## FUNDING

[To be completed]

## DATA AVAILABILITY

The dataset contains anonymised administrative hospital data. Requests for access should be directed to the hospital's research office.

---

## REFERENCES

1. Bauer M, Auhuber TC, Kraus R, et al. The German perioperative procedural time glossary: a joint recommendation by the BDA, BDC, VOPM, VOPMÖ, ÖGARI and SFOPM (2020 edition). *Anästh Intensivmed* 2020;61:516-31. DOI: 10.19224/ai2020.516.
2. Griffiths P, Dall'Ora C, Simon M, et al. Nurses' shift length and overtime working in 12 European countries: the association with perceived quality of care and patient safety. *Med Care* 2014;52(11):975-81.
3. Wachtel RE, Dexter F. Review of behavioral operations experimental studies of newsvendor problems for operating room management. *Anesth Analg* 2010;110(6):1698-710.
4. Cortegiani A, Ippolito M, Misseri G, et al. Association between night/after-hours surgery and mortality: a systematic review and meta-analysis. *Br J Anaesth* 2020;124(5):623-37.
5. Oh T-K, Song I-A. Outcomes of after-hours surgeries performed under general anaesthesia: a South Korean nationwide cohort study. *Anaesthesia* 2025;80(6):645-51. DOI: 10.1111/anae.16559.
6. Sakurai K, Takeda C. Assessing the influence of after-hours surgery: concerns with the confounders and conclusion. *Anaesthesia* 2025;80(5):596-7. DOI: 10.1111/anae.16591.
7. Althoff FC, Wachtendorf LJ, Rostin P, et al. Effects of night surgery on postoperative mortality and morbidity: a multicentre cohort study. *BMJ Qual Saf* 2021;30(8):678-88.
8. Meewisse AJG, Gribnau A, Thiessen SE, et al. Effect of time of day on outcomes in elective surgery: a systematic review. *Anaesthesia* 2024;79(12):1325-34. DOI: 10.1111/anae.16395.
9. Saager L, Hesler BD, You J, et al. Intraoperative transitions of anesthesia care and postoperative adverse outcomes. *Anesthesiology* 2014;121(4):695-706.
10. Health Services Safety Investigations Body (HSSIB). The impact of staff fatigue on patient safety. Investigation report. London: HSSIB, 2025.
11. Pittman P, Tiunn HL, Luo Q, et al. Increased utilization of overtime and agency nurses and patient safety. *JAMA Netw Open* 2025;8(4):e252875. PMID: 40172888.
12. Dall'Ora C, Griffiths P, Ball J, et al. Association of 12 h shifts and nurses' job satisfaction, burnout and intention to leave: findings from a cross-sectional study of 12 European countries. *BMJ Open* 2015;5(9):e008331.
13. Bae S-H. Nurse staffing, work hours, mandatory overtime, and turnover in acute care hospitals affect nurse job satisfaction, intent to leave, and burnout: a cross-sectional study. *Int J Public Health* 2024;69:1607068.
14. Dall'Ora C, Ball J, Recio-Saucedo A, Griffiths P. Characteristics of shift work and their impact on employee performance and wellbeing: a literature review. *Int J Nurs Stud* 2016;57:12-27.
15. Dall'Ora C, Ball J, Reinius M, Griffiths P. Burnout in nursing: a theoretical review. *Hum Resour Health* 2020;18:41.
16. Zhang C, Dunstan C, Pandit JJ. A tutorial on "capped utilisation" as a metric and key performance target in NHS England's Model Hospital operating theatres database: caution for international healthcare systems. *Anesthesiol Perioper Sci* 2024. DOI: 10.1007/s44254-024-00073-3.
17. Macario A. Are your hospital operating rooms "efficient"? A scoring system with eight performance indicators. *Anesthesiology* 2006;105(2):237-40.
18. Koch A, Burns J, Catchpole K, Weigl M. Associations of workflow disruptions in the operating room with surgical outcomes: a systematic review and narrative synthesis. *BMJ Qual Saf* 2020;29(12):1033-45.
19. Joseph A, Khoshkenar A, Taaffe KM, et al. Minor flow disruptions, traffic-related factors and their effect on major flow disruptions in the operating room. *BMJ Qual Saf* 2019;28(4):276-83.
20. Schouten AM, Flipse SM, van Nieuwenhuizen KE, et al. Operating room performance optimization metrics: a systematic review. *J Med Syst* 2023;47(1):19.
21. Strum DP, May JH, Vargas LG. Modeling the uncertainty of surgical procedure times: comparison of log-normal and normal models. *Anesthesiology* 2000;92(4):1160-7.
22. Eijkemans MJ, van Houdenhoven M, Nguyen T, et al. Predicting the unpredictable: a new prediction model for operating room times using individual characteristics and the surgeon's estimate. *Anesthesiology* 2010;112(1):41-9.
23. MacMillan L, Madura GM, Elliot M, et al. What affects operating room turnover time? A systematic review and mapping of the evidence. *Surgery* 2025;181:109263. PMID: 40054053.
24. Charlesworth M, Pandit JJ. Rational performance metrics for operating theatres, principles of efficiency, and how to achieve it. *Br J Surg* 2020;107(2):e63-9. PMID: 31903597.
25. Zhang C, Pandit JJ. Getting operating theatre metrics right to underpin quality improvement. *Br J Anaesth* 2023;131(1):130-4.
26. Wachtel RE, Dexter F. Influence of the operating room schedule on tardiness from scheduled start times. *Anesth Analg* 2009;108(6):1889-901.
27. Fügener A, Schiffels S, Kolisch R. Overutilization and underutilization of operating rooms: insights from behavioral health care operations management. *Health Care Manag Sci* 2017;20(1):115-28.
28. Parmar D, Woodman M, Pandit JJ. A graphical assessment of emergency surgical list efficiency to determine operating theatre capacity needs. *Br J Anaesth* 2022;128(3):574-83. PMID: 34865827.
29. Dexter F, Epstein RH. Typical savings from each minute reduction in tardy first case of the day starts. *Anesth Analg* 2009;108(4):1262-7.
30. Pandit JJ, Abbott T, Pandit M, et al. Is "starting on time" useful (or useless) as a surrogate measure for "surgical theatre efficiency"? *Anaesthesia* 2012;67(8):823-32.

---

## FIGURE LEGENDS

**Figure 1.** Room-level overtime concentration. Panel A: percentage of cases with overtime per operating room, ranked from lowest to highest. Panel B: mean overtime duration per room (minutes), with the hospital average marked for reference. Overall: 7,729 of 79,352 cases (9.7%), mean 60.3 min, median 39 min, P95 197 min.

---

## SUPPLEMENTARY FIGURES

**Supplementary Figure S1.** Timing of overtime case completions. Distribution of room-out times for the 7,729 overtime cases. More than half of completions fall in the 16:30 to 17:30 window immediately after the day-shift handover, with a long tail decaying through the evening and overnight.

[Insert Supplementary Figure S1 about here]

