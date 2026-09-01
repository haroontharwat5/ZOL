# Data-driven monitoring of operating-room overtime: a single-centre retrospective study

[Authors and affiliations removed for blinded review]

**Keywords:** operating room, overtime, scheduling, patient safety, staff wellbeing, quality improvement

Citations as [Author] pending final Vancouver renumbering. [TO CONFIRM] marks items awaiting external input.

---

## ABSTRACT

**Background.** Operating-room (OR) overtime, in which surgery continues beyond the end of the staffed shift, is associated with higher patient mortality and staff burnout, and it costs roughly twice as much per minute as underutilised time. Overtime is usually reported as a single figure for the whole OR department, which conceals where it arises and cannot direct improvement.

**Objective.** To show what analysis of routinely collected administrative data can contribute to overtime monitoring and management, by characterising overtime in one high-volume tertiary hospital: its distribution across rooms and time, and the operational factors associated with it.

**Design and setting.** Retrospective observational study using administrative OR data from a 24/7 tertiary hospital in Belgium with 18 surgical operating rooms.

**Participants.** 79,352 surgical cases performed between January 2022 and May 2025; a case is one patient's uninterrupted stay in one operating room, from entry to exit.

**Main outcome measures.** Overtime per case, analysed by room, weekday, shift, and urgency; start-time deviation, duration-estimation accuracy, inter-case gaps, and urgent-case disruption of the elective programme were examined as candidate contributing factors.

**Results.** Of 79,352 cases, 7,729 (9.7%) ran past the end of their assigned shift, with a mean overtime of 60.3 minutes and a 95th percentile of 197 minutes. Room-level overtime rates ranged from 3.5% to 32.9%; the highest-overtime room ran overtime on a third of its cases (mean 154 minutes). Urgent cases ran past the shift boundary at more than twice the elective rate (18.2% versus 8.3%). Nearly half of the overtime cases (45.7%) were already planned to end past the shift boundary, and these scheduled crossings carried 62.1% of all overtime minutes. Rooms with longer gaps between cases had higher overtime rates (Spearman rho = 0.89, p < 0.001), whereas start-time punctuality showed no association with room-level overtime (rho = −0.29, p = 0.24).

**Conclusions.** Routinely collected OR data located overtime precisely enough to direct management attention: it was concentrated in a small number of rooms, it divided into scheduled boundary-crossings and unplanned overruns with different management levers, and longer between-case gaps travelled with overtime, while start-time punctuality predicted little. Room-level monitoring built from these data may offer a more actionable basis for overtime management than department-wide averages.

## KEY MESSAGES

**What is already known on this topic**

- After-hours surgery is associated with higher patient mortality, and staff overtime with poorer reported care quality, safety, and retention; overtime is one route by which planned daytime work becomes after-hours work. Overtime is costly: staffing is planned in advance, so underutilised time is paid staff time that goes unused, and overutilised time costs roughly twice as much per minute. Prior work reports overtime as an aggregate for the whole OR department.

**What this study adds**

- In a single-centre retrospective analysis of 79,352 surgical cases, overtime concentrated in a few rooms, with a nearly ten-fold spread within one OR department (3.5% to 32.9%). Nearly half of overtime cases were already planned to end past the shift boundary, and these scheduled crossings carried most overtime minutes. Rooms with longer between-case gaps ran more overtime; start-time punctuality showed no association with room-level overtime.

**How this study might affect research, practice or policy**

- Hospitals seeking to reduce overtime should monitor individual rooms rather than department-wide averages, and should distinguish overtime that is scheduled into the programme from overtime that arises in execution, because the two call for different responses. Linking these operational patterns to patient and staff outcomes is a necessary next step.

## INTRODUCTION

Operating lists overrun. Surgical durations are inherently variable [Strum], and a list planned to end with the day shift often does not. When surgery continues past the end of the rostered shift, the list runs into overtime. We use the term in the same sense as the staff-overtime literature, where overtime is work beyond contracted hours [Griffiths]. The consequences reach patients as well as staff. Overtime pushes planned daytime surgery into the evening, and operating after hours carries documented risks: a meta-analysis found higher adjusted mortality for night and after-hours surgery (odds ratio 1.16, 95% CI 1.06 to 1.28, low-certainty evidence) [Cortegiani], and a multicentre cohort of more than 350,000 non-cardiac cases linked night surgery to increased morbidity, partly mediated by more frequent provider handovers during the case [Althoff]. Handovers are not incidental here: a case that crosses the shift boundary continues under staff who were not present at its start, and each additional intraoperative anaesthesia transition raises the incidence of major complications, from 8.8% with none to 21.2% with four or more [Saager].

For staff, the evidence concerns overtime itself rather than its after-hours consequences. In a survey of 31,627 nurses across 12 European countries, working overtime was associated with poorer nurse-reported quality of care and worse patient safety [Griffiths]. A review of shift-work studies linked overtime to decreased job performance [Dall'Ora], and mandatory overtime was associated with intention to leave in Korean acute-care hospitals [Bae].

An OR department that wants to reduce overtime first has to know where it occurs, and the numbers usually available to management do not say. Established efficiency scoring operates at the level of the whole OR suite [Macario], published performance metrics lack standardised definitions [Schouten], and aggregation can actively mislead: NHS England's capped-utilisation metric ignores operating time in late finishes, which is precisely the time overtime consists of [Zhang, Dunstan and Pandit]. Prior analyses of overtime itself treat it as a department-level number or as a cost parameter in staffing models [Wachtel and Dexter]. Where overtime sits within a department, room by room, and which operational factors are associated with it, the literature does not answer. The records needed to answer it already exist in routine registration: OR information systems log room entry and exit times, planned durations, and urgency classifications in the course of daily operations [Bauer].

This paper uses those records to study overtime at a Belgian tertiary centre with 18 surgical ORs and a steep staffing step-down at each shift end. Using only routinely recorded administrative data covering three and a half years and 79,352 cases, we address two research questions. First, how is overtime distributed across rooms and time, and to what extent is it scheduled rather than unplanned (RQ1)? Second, which of four operational factors are associated with it: duration overruns, urgent-elective interaction, start-time punctuality, and inter-case gaps (RQ2)? The aim is to show what data-driven analysis of routine OR records can contribute to overtime management, and where its limits lie.

## METHODS

### Setting and data

The study hospital is a 24/7 tertiary centre in Belgium performing more than 22,000 surgical procedures per year. It operates 18 surgical operating rooms and 7 interventional operating rooms. The surgical staff includes 195 surgeons and 207 anaesthesiologists (including trainees and fellows), covering all surgical specialities except congenital cardiac surgery and organ transplantation. During the 08:00 to 16:30 day shift, each room is staffed with 2 to 3 nurses; at 16:30 the hospital reduces to 8 staffed rooms, at 17:30 to 4, and overnight to a single room.

We used administrative OR data from 1 January 2022 to 31 May 2025 from the 18 surgical operating rooms. Endoscopy suites and catheterisation laboratory cases without an anaesthesiologist present were excluded, as were cases with implausible timestamps (zero observed duration, planned duration exceeding 24 hours, or extreme deviations from the planned schedule). The final cohort comprised 79,352 cases involving 60,895 unique patients and 1,276 distinct procedure types; annual volume grew from 22,133 cases in 2022 to 23,738 in 2024, with 9,906 recorded through May 2025 (Table 1). The admission mix was 42.3% ambulatory and 57.7% inpatient, and 85.4% of cases were elective (cases scheduled or performed within 24 hours of booking were classified as urgent; all others as elective). Room-in and room-out times are the only procedural time markers confirmed as reliable by the hospital's clinical team; all timing analyses use these two time points.

The unit of analysis is the case: one uninterrupted occupancy of one operating room by one patient, from room-in to room-out, recorded with one procedure code. A case is distinct from an admission, which may span days around it, and from a patient: some of the 60,895 patients appear repeatedly over the study period. From these inputs we derived, for each case: observed duration (room-in to room-out), planning deviation (observed minus planned duration, positive when a case ran longer than booked), and start-time deviation (actual minus planned room-in, positive when a case started late), following standard perioperative process-time definitions [Bauer]. We additionally defined an overtime flag and overtime minutes, and a shift label, as set out below.

### Overtime definition and analyses

Time beyond plan goes by different names in the literature, depending on the reference point. Measured against the room's allocated block time, it is "overutilisation" [Bauer]. Measured against the clock, it is "after-hours surgery" [Cortegiani]. Measured against the staff roster, it is "overtime": work beyond contracted hours [Griffiths]. This study uses the roster as the reference point, applied at room level, because the change of nursing staff at each shift end is the operational event that makes a late-running case consequential at this site.

Each case was assigned to a shift by its actual room-in time, following the hospital's shift boundaries: day (08:00 to 16:30), evening (16:30 to 22:00), and night (22:00 to 08:00). One reclassification was applied: cases entering the room between 07:30 and 08:00 and remaining in the room past 08:00 (n = 6,153) were treated as day-shift cases, since these represent early starts of the day programme rather than night activity. The same rules were applied on weekends. A case was flagged as overtime if its room-out fell after the end of its assigned shift; overtime minutes equal the positive difference between room-out and shift end. A case was classified as a scheduled crossing when its planned end time already fell after the end of its planned shift; overtime cases that were not scheduled crossings are referred to as unplanned overruns.

We measured overtime at room level because aggregate utilisation measures can misrepresent the performance of individual rooms [Zhang, Dunstan and Pandit]. Because published OR performance metrics lack standardised definitions [Schouten], each metric used in this study is defined explicitly here.

In line with the study's aim of showing what routinely recorded data can contribute to overtime monitoring, all analyses are descriptive; we did not fit causal or inferential models, and we interpret associations accordingly. For RQ1, we computed overtime rate, mean, median, and 95th percentile, stratified by room, weekday, year, and shift, and the split between scheduled crossings and unplanned overruns. For RQ2, we examined duration deviation by planned-duration bucket using the coefficient of variation (the standard deviation of duration divided by its mean, which places cases of different lengths on a comparable scale) [Strum; Eijkemans], urgency mix and timing, urgent-elective interaction, start-time deviation per room, and inter-case idle time. Inter-case idle time was measured as the gap between consecutive cases in the same room within the same shift window; the first case in a window has no defined gap, overlapping room times count as zero, and gaps longer than 60 minutes were excluded as planned downtime. An urgent-elective overlap was flagged when an urgent case occupied a room during a window in which an elective case had been planned in that room; start-delay comparisons are made at case level between overlapped and non-overlapped elective cases. Spearman rank correlations across the 18 rooms were computed between room-level overtime rate and two candidate factors: late-start rate (the share of cases starting after their planned time) and mean inter-case idle time; for the idle-time correlation, each room's overtime rate was computed among the cases contributing gap data. Intermediate findings were reviewed with the clinical team and used to refine variable definitions and exclusions. The study is reported in accordance with the STROBE guidelines for observational studies.

### Ethics

This study used fully anonymised administrative data with institutional approval. No patient interaction occurred.

### Patient and public involvement

Given the retrospective use of fully anonymised administrative data, no patient or public involvement was sought.

## RESULTS

### Overtime burden, composition, and room-level concentration (RQ1)

Of 79,352 cases, 7,729 (9.7%) ran past the end of their assigned shift. Among overtime cases, the mean was 60.3 minutes, the median 39 minutes, and the 95th percentile (P95) 197 minutes (Table 2A). Weekday rates were stable (8.8 to 9.9%) and roughly 1.7 times higher at weekends (Saturday 16.8%, Sunday 15.5%), when the elective programme does not run and the caseload is largely urgent. The overtime rate declined slightly over the study period, from 10.0% in 2022 to 8.6% in the first five months of 2025 (Table 2B).

Not all overtime was unplanned. For 5,812 cases (7.3%), the schedule itself placed the planned end past the shift boundary (6.4% of elective and 12.8% of urgent cases; median 40 planned minutes past it). Of these planned crossings, 60.8% did run past the boundary, against 5.7% of cases planned to fit. The 7,729 overtime cases therefore divide into 3,532 scheduled crossings (45.7%) and 4,197 unplanned overruns (54.3%). Scheduled crossings ran longer (mean 82 versus 42 overtime minutes) and carried 62.1% of all overtime minutes. For monitoring, overtime risk is therefore largely visible at planning time.

Room-level overtime rates ranged from 3.5% to 32.9% across the 18 rooms (Figure 1). OR10, which handles complex cardiac surgery (coronary artery bypass grafting, aortic valve replacement, mitral valve repair), ran overtime on 32.9% of its 1,743 cases, with a mean of 154 minutes and a P95 of 328 minutes; 81.5% of its overtime cases were scheduled crossings. At the other end, OR14 ran 3.5% across 6,885 cases and OR01 5.8% across 6,577. Overtime minutes were strongly concentrated: OR10 alone, with 2.2% of the caseload, generated 19.0% of all overtime minutes, and the three largest contributors together generated 36.4%.

Most overtime cases ended shortly after the shift boundary: more than half of overtime completions fell between 16:30 and 17:30, immediately after the day-shift handover, with the distribution decaying through the evening (Supplementary Figure S1). For monitoring purposes, the department-wide rate is therefore the wrong unit: overtime at this hospital is a property of particular rooms and of particular scheduling decisions, and both are identifiable from routine data alone.

### Candidate operational factors (RQ2)

*Planning accuracy.* For the unplanned component of overtime, lists planned to finish inside the shift that did not, the first candidate explanation is systematic underbooking: if cases routinely needed more time than the schedule gave them, the shortfall would accumulate over the list and push its end past the boundary. The data show no such pattern. Cases were almost as likely to run long as to run short (45.7% versus 54.3% of all cases), and the typical deviation was similar in both directions (median 14 minutes when longer than planned, 12 minutes when shorter). The schedule's problem is not bias but unpredictability: two cases booked for the same duration often finished far apart.

This unpredictability was unevenly distributed. The coefficient of variation of observed duration was highest for short procedures (0.54 below 30 minutes) and between 0.35 and 0.42 for longer ones, but the variability of the planning error rose with planned duration, reaching 1.84 for procedures planned above 180 minutes: the longest cases were the hardest to book accurately. These long, hard-to-book procedures, mainly complex cardiac and oncological surgery, were performed in the rooms with the highest overtime rates. For overtime, the conclusion is that no uniform padding of bookings would fix the schedule, because duration risk is concentrated in particular rooms and procedure types.

*Urgent-elective interaction.* Urgent cases related to overtime through two channels. Directly, they generated it: urgent cases crossed the shift boundary at more than twice the elective rate (18.2% versus 8.3%, Table 3), with heavier tails (P95: 69 versus 29 minutes); because electives outnumber urgent cases six to one, elective cases still supplied most overtime volume. Indirectly, urgent arrivals compressed the elective day: an urgent case occupied a room planned for elective use on 858 of 1,247 observation days (68.8%), and affected elective cases started later than unaffected ones. At OR11, the emergency-designated room carrying the highest overlap burden (475 events, 15.2% of its elective cases), the median start delay was 60 minutes with overlap versus 28 without. Whether these later starts translated into additional elective overtime was not measured here.

*Start-time punctuality.* A common assumption in OR management is that punctual starts, and the first case of the day in particular (first-case on-time start, FCOTS), keep the list on schedule so that it finishes within its shift. Late starts were common: 67.4% of cases started after their planned time, by a mean of 74.6 minutes and a median of 28 among late cases. To test the assumption, we correlated each room's late-start rate with its overtime rate. Across the 18 rooms there was no association (Spearman rho = −0.29, p = 0.24); if anything the direction was negative: OR10 had the lowest late-start rate yet the highest overtime rate, while OR14 started late most often yet ran the least overtime. Start-time punctuality therefore does not indicate which rooms accumulate overtime.

*Inter-case idle time.* Across the 18 rooms, inter-case idle time (akin to turnover time [MacMillan]) had a median of 8 minutes and a mean of 9.9 minutes. At room level, mean idle time was positively correlated with overtime rate (Spearman rho = 0.89, p < 0.001), and the association was not an artefact of the extreme room: it persisted when OR10, which had both the highest mean idle time (22.6 minutes) and the highest overtime rate, was excluded (rho = 0.90, p < 0.001). Rooms with longer gaps between cases therefore also ran more overtime. Both are plausibly markers of case-mix complexity, since complex procedures require longer preparation between cases as well as longer operating times; these cross-sectional correlations cannot separate that account from a turnover effect.

## DISCUSSION

In this analysis of 79,352 cases at one tertiary centre, one case in ten ran past the end of its staffed shift, but that department-wide figure concealed the two facts that matter for management. First, overtime was concentrated: room-level rates spanned 3.5% to 32.9%, and one cardiac room with 2.2% of the caseload generated 19.0% of all overtime minutes. Second, overtime was heterogeneous: nearly half of the cases that crossed the boundary were planned to cross it, and these scheduled crossings carried 62.1% of the overtime minutes. Neither fact is visible in the aggregate number, and both came out of records the hospital already keeps.

### Two kinds of overtime, two levers

The scheduled component reframes part of the overtime problem as a capacity decision rather than an execution failure. Booking a long case across the boundary uses staffed evening capacity that would otherwise sit idle, and idle staffed time is itself costly: overutilised time costs roughly twice as much as underutilised time, which is the trade-off OR managers weigh when staffing cannot match uncertain demand [Wachtel and Dexter]. Whether the volume of scheduled crossings at this hospital reflects deliberate use of the evening tier could not be determined from administrative data and is a question for the clinical team. What the data do show is that the exposure is the same either way: a case that crosses the boundary is completed after the nursing handover, with fewer rooms open, whether or not the crossing was planned. The two components nonetheless call for different responses. Scheduled crossings are a planning and capacity question: whether the evening tier is sized for what is booked into it. Unplanned overruns are a duration-risk question, and they concentrated exactly where duration variability was highest.

### The factors that did and did not travel with overtime

Duration risk, not systematic underbooking, characterised the unplanned component. Overruns and underruns were balanced overall, but the planning error grew most variable for the longest procedures, and surgeons' duration estimates are known to show systematic deviations under uncertainty [Fugener]. Tardiness also accumulates over a list as the scheduled time preceding each case grows [Wachtel and Dexter, tardiness]. Both observations fit the pattern we describe, in which the rooms hosting long, hard-to-book cases were the rooms that ran late, although our descriptive design cannot test the cumulative mechanism directly.

Start-time punctuality, the most commonly monitored discipline marker, told management nothing about overtime here. The premise behind first-case on-time starts, that each minute of tardiness propagates to the end of the day at measurable cost [Dexter and Epstein], did not translate into a room-level association: the correlation between late-start rate and overtime rate was absent, and its direction, if anything, negative. Pandit and colleagues reached a compatible conclusion across more than 7,000 UK operating lists, where start time explained only 4 to 8% of the variance in finish time [Pandit]. We do not conclude that punctuality is unimportant, only that at this hospital it does not indicate where overtime accumulates.

Urgent flow related to overtime through a measured channel, urgent cases crossing the boundary at twice the elective rate, and a documented but unquantified one, the routine displacement of elective starts. Overlap between urgent and elective work occurred on two-thirds of days despite dedicated urgent rooms, so protecting the elective programme is likely to require scheduling buffers or capacity reallocation rather than reactive rescheduling; graphical methods for judging emergency capacity from delay and utilisation patterns could support such decisions [Parmar].

### Monitoring at the level where decisions are made

These findings argue for room-level, composition-aware monitoring rather than department-wide targets. A target such as "reduce overtime by 10%" cannot be acted on when room rates differ ninefold and half the overtime is scheduled: the highest-overtime room needs a capacity discussion, not a punctuality campaign, and the punctuality campaign would in any case address a factor with no measured relation to overtime. Aggregate theatre metrics have been criticised on exactly these grounds: capped utilisation discards the late-finish operating time that overtime consists of [Zhang, Dunstan and Pandit], and standard metrics mislead in isolation [Charlesworth and Pandit]. Quality improvement work needs metrics that are valid at the level where decisions are made, and for overtime that level is the room and the schedule. All the quantities used here, room rates, the scheduled and unplanned components, and the planning-time risk signal, derive from timestamps that OR information systems record in daily operation, so a monitoring instrument built on them requires no new data collection.

### Limitations

This study has several limitations. It is a single-site analysis, and the concentration and composition patterns reflect one hospital's staffing structure and scheduling practice; what generalises is the approach, not the numbers. The administrative record contains only room-in and room-out times, so nothing can be said about events within a case. The analyses are descriptive by design: associations are reported without causal claims, and the account linking case complexity to gaps, duration risk, and overtime remains an interpretation consistent with the data rather than a tested mechanism. Whether scheduled boundary-crossings reflect deliberate policy could not be determined from these data. We did not measure patient or staff outcomes; the harm argument rests on published literature in which effect sizes vary widely and some estimates are contested on residual-confounding grounds [Oh; Sakurai; Meewisse]. Readers should weigh the after-hours evidence with that uncertainty in mind.

## CONCLUSION

Operating-room overtime at this tertiary hospital was concentrated in a small number of rooms and divided into two components with different management levers: scheduled crossings, written into the programme and carrying most overtime minutes, and unplanned overruns, driven by duration risk rather than late starts. All of this was extracted from routinely recorded administrative data, and most of the overtime risk was visible at planning time. The findings support room-level, composition-aware monitoring of overtime as a practical instrument for OR management, and linking these operational patterns to patient and staff outcomes is the necessary next step.

---

## DATA AVAILABILITY

The dataset cannot be made publicly available, consistent with contractual agreements with the hospital.

## ACKNOWLEDGEMENTS / FUNDING / COMPETING INTERESTS

[TO CONFIRM: AI-assistance disclosure wording with Niels; funding statement; competing interests: none declared.]

## DISPLAY ITEMS

- Table 1. Study cohort characteristics (moved to Methods).
- Table 2A/2B. Overtime by weekday / by year (captions short; explanatory footnotes below tables).
- Table 3. Volume and overtime by urgency (renamed from 3A; footnote on denominators; Table 3B deleted).
- Figure 1. Room-level overtime, stacked scheduled/unplanned components [figure to regenerate].
- Supplementary Figure S1. Timing of overtime completions.
- Supplementary Table S1. Cited literature summary (updated; absorbs references no longer cited in main text).
