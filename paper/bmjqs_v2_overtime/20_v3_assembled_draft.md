# v3 assembled draft — current approved state

Legend: [LOCKED] approved by Haroon. [PENDING] proposed, awaiting verdict. [TODO] chunk not yet reached. Citations as author names until final renumbering. This file is the single tracking view; chat shows any section on request.

---

## Title [LOCKED]
Data-driven monitoring of operating-room overtime: a single-centre retrospective study

## Abstract [LOCKED]

**Background.** Operating-room (OR) overtime, in which surgery continues beyond the end of the staffed shift, is associated with higher patient mortality and staff burnout, and it costs roughly twice as much per minute as underutilised time. Overtime is usually reported as a single figure for the whole OR department, which conceals where it arises and cannot direct improvement.

**Objective.** To show what analysis of routinely collected administrative data can contribute to overtime monitoring and management, by characterising overtime in one high-volume tertiary hospital: its distribution across rooms and time, and the operational factors associated with it.

**Design and setting.** Retrospective observational study using administrative OR data from a 24/7 tertiary hospital in Belgium with 18 surgical operating rooms.

**Participants.** 79,352 surgical cases performed between January 2022 and May 2025; a case is one patient's uninterrupted stay in one operating room, from entry to exit.

**Main outcome measures.** Overtime per case, analysed by room, weekday, shift, and urgency; start-time deviation, duration-estimation accuracy, inter-case gaps, and urgent-case disruption of the elective programme were examined as candidate contributing factors.

**Results.** Of 79,352 cases, 7,729 (9.7%) ran past the end of their assigned shift, with a mean overtime of 60.3 minutes and a 95th percentile of 197 minutes. Room-level overtime rates ranged from 3.5% to 32.9%; the highest-overtime room ran overtime on a third of its cases (mean 154 minutes). Urgent cases ran past the shift boundary at more than twice the elective rate (18.2% versus 8.3%). Nearly half of the overtime cases (45.7%) were already planned to end past the shift boundary, and these scheduled crossings carried 62.1% of all overtime minutes. Rooms with longer gaps between cases had higher overtime rates (Spearman rho = 0.89, p < 0.001), whereas start-time punctuality showed no association with room-level overtime (rho = −0.29, p = 0.24).

**Conclusions.** Routinely collected OR data located overtime precisely enough to direct management attention: it was concentrated in a small number of rooms, it divided into scheduled boundary-crossings and unplanned overruns with different management levers, and longer between-case gaps travelled with overtime, while start-time punctuality predicted little. Room-level monitoring built from these data may offer a more actionable basis for overtime management than department-wide averages.

## Key messages [LOCKED]

**What is already known on this topic** — After-hours surgery is associated with higher patient mortality, and staff overtime with poorer reported care quality, safety, and retention; overtime is one route by which planned daytime work becomes after-hours work. Overtime is costly: staffing is planned in advance, so underutilised time is paid staff time that goes unused, and overutilised time costs roughly twice as much per minute. Prior work reports overtime as an aggregate for the whole OR department.

**What this study adds** — In a single-centre retrospective analysis of 79,352 surgical cases, overtime concentrated in a few rooms, with a nearly ten-fold spread within one OR department (3.5% to 32.9%). The highest-overtime rooms were those handling long, complex procedures, and rooms with longer between-case gaps ran more overtime; start-time punctuality showed no association with room-level overtime.

**How this study might affect research, practice or policy** — Hospitals seeking to reduce overtime should monitor and target individual rooms rather than department-wide averages, and should treat urgent-case flow as a routine scheduling input. Linking these operational patterns to patient and staff outcomes is a necessary next step.

## Introduction [LOCKED]

Operating lists overrun. Surgical durations are inherently variable [Strum], and a list planned to end with the day shift often does not. When surgery continues past the end of the rostered shift, the list runs into overtime. We use the term in the same sense as the staff-overtime literature, where overtime is work beyond contracted hours [Griffiths]. The consequences reach patients as well as staff. Overtime pushes planned daytime surgery into the evening, and operating after hours carries documented risks: a meta-analysis found higher adjusted mortality for night and after-hours surgery (odds ratio 1.16, 95% CI 1.06 to 1.28, low-certainty evidence) [Cortegiani], and a multicentre cohort of more than 350,000 non-cardiac cases linked night surgery to increased morbidity, partly mediated by more frequent provider handovers during the case [Althoff]. Handovers are not incidental here: a case that crosses the shift boundary continues under staff who were not present at its start, and each additional intraoperative anaesthesia transition raises the incidence of major complications, from 8.8% with none to 21.2% with four or more [Saager].

For staff, the evidence concerns overtime itself rather than its after-hours consequences. In a survey of 31,627 nurses across 12 European countries, working overtime was associated with poorer nurse-reported quality of care and worse patient safety [Griffiths]. A review of shift-work studies linked overtime to decreased job performance [Dall'Ora], and mandatory overtime was associated with intention to leave in Korean acute-care hospitals [Bae].

An OR department that wants to reduce overtime first has to know where it occurs, and the numbers usually available to management do not say. Established efficiency scoring operates at the level of the whole OR suite [Macario], published performance metrics lack standardised definitions [Schouten], and aggregation can actively mislead: NHS England's capped-utilisation metric ignores operating time in late finishes, which is precisely the time overtime consists of [Zhang, Dunstan and Pandit]. Prior analyses of overtime itself treat it as a department-level number or as a cost parameter in staffing models [Wachtel and Dexter]. Where overtime sits within a department, room by room, and which operational factors are associated with it, the literature does not answer. The records needed to answer it already exist in routine registration: OR information systems log room entry and exit times, planned durations, and urgency classifications in the course of daily operations [Bauer].

This paper uses those records to study overtime at a Belgian tertiary centre with 18 surgical ORs and a steep staffing step-down at each shift end. Using only routinely recorded administrative data covering three and a half years and 79,352 cases, we address two research questions. First, how is overtime distributed across rooms and time, and to what extent is it scheduled rather than unplanned (RQ1)? Second, which of four operational factors are associated with it: duration overruns, urgent-elective interaction, start-time punctuality, and inter-case gaps (RQ2)? The aim is to show what data-driven analysis of routine OR records can contribute to overtime management, and where its limits lie.

## Methods [PENDING — full chunk awaiting verdict]

### Setting and data [PENDING]
Hospital paragraph (unchanged facts) + data paragraph with Table 1 moved here from Results + derived-variables paragraph with inline definitions (observed duration; planning deviation; start-time deviation; overtime flag; room-swap flag; shift label).

### Overtime definition and analyses [PENDING]
Terminology passage ("reference point" version, quotes around each term; Dexter clause pending full-text verification). Shift assignment per hospital policy (08:00/16:30/22:00) with the 07:30-early-starter reclassification (n = 6,153). Zero-overtime-by-design sentence [pending Ben/Dieter]. Room-level measurement rationale (aggregate misrepresents rooms [Zhang]; explicit definitions because metrics lack standardisation [Schouten; Morton pending verification]). Descriptive-by-design sentence tied to monitoring aim. Analysis paragraph incl. CV definition (moved from Results), idle-time rules per code, overlap flag, late-start rate, Spearman correlations, STROBE.

### Ethics / PPI [LOCKED as in v2]

## Results [BASELINE APPROVED + decomposition APPROVED by Maxim meeting 27 Aug]

Structure: opens with general overtime statistics (no sample-overview section); every subsection ends with its explicit conclusion for overtime; Table 3B deleted (values in prose); room swaps section removed.

### New RQ1 block: Scheduled and unplanned overtime [APPROVED]

> Not all overtime was unplanned. For 5,812 cases (7.3%), the schedule itself placed the planned end past the shift boundary (6.4% of elective and 12.8% of urgent cases; median 40 planned minutes past it). Of these planned crossings, 60.8% did run past the boundary, against 5.7% of cases planned to fit. The 7,729 overtime cases therefore divide into 3,532 scheduled crossings (45.7%) and 4,197 unplanned overruns (54.3%). Scheduled crossings ran longer (mean 82 versus 42 overtime minutes) and carried 62.1% of all overtime minutes. The balance differed by room: in OR10, 81.5% of overtime cases were scheduled crossings. For monitoring, overtime risk is therefore largely visible at planning time.

Planning-accuracy subsection now opens: "For the unplanned component of overtime, lists planned to finish inside the shift that did not, the first candidate explanation is systematic underbooking: if cases routinely needed more time than the schedule gave them, the shortfall would accumulate over the list and push its end past the boundary. The data show no such pattern." Idle correlation reported as rho = 0.89 (gap-subset denominator, Maxim's computation), robust excluding OR10 (rho = 0.90).

## Discussion [TODO - one block APPROVED]

### Approved passage: the scheduled component as a capacity decision

> The scheduled component reframes part of the overtime problem as a capacity decision rather than an execution failure. Booking a long case across the boundary uses staffed evening capacity that would otherwise sit idle, and idle staffed time is itself costly: overutilised time costs roughly twice as much as underutilised time, which is the trade-off OR managers weigh when staffing cannot match uncertain demand [Wachtel and Dexter]. Whether the observed volume of scheduled crossings reflects deliberate use of the evening tier could not be determined from administrative data and is a question for the clinical team. The two components call for different responses: scheduled crossings are a planning and capacity question, while unplanned overruns, concentrated where duration variability is highest, are a duration-risk question. Room-level monitoring can report both from routine data alone.

Remaining TODO: what-the-case-study-showed opening (9.7% re-explained); FCOTS paragraph fixes; dashboard paragraph [Ivers, Anhøj pending verification]; limitations rewrite.

## Conclusion [TODO]

## Back matter [TODO]
Data availability per Niels's wording; AI disclosure sentence (wording with Niels); funding/acknowledgements; reference renumbering last.

---

## Open questions for Ben/Dieter
1. Are schedules constructed so no case would cross its shift boundary if all cases ran as planned?
2. Does the anaesthesia team also change at shift boundaries, or only nursing?
3. Does weekend staffing follow the same shift boundaries?

## Open decisions for Maxim
- Idle correlation denominator: 0.91 (all cases per room) vs his 0.89 (gap-defined subset).
