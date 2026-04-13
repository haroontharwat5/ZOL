# One hospital, four operating-room models: a stratified benchmarking study of 228,623 cases across a Belgian hospital network

**Haroon Tharwat, Maxim Riebus, Ben [TBD], Dieter [TBD], Niels Martin**

Hasselt University, Faculty of Business Economics, Research Group Business Informatics, Process Analytics in Healthcare

---

## Abstract

Operating-room benchmarking typically compares hospitals on raw efficiency metrics without adjusting for the structural differences between their operating models. We studied 228,623 surgical procedures performed between January 2022 and May 2025 across four sites of a single Belgian hospital network, Ziekenhuis Oost-Limburg (ZOL). Each site operates under the same governance, electronic health record, and labor agreements, but runs a structurally different type of OR: a 24/7 tertiary center (Genk, 96,044 cases), an ambulatory-only facility with paired-room flex scheduling (Lanaken, 69,395 cases), a hybrid campus mixing short ambulatory and longer inpatient blocks (Maaseik, 53,902 cases), and a specialized cardiac catheterization lab (Cathlab, 9,282 cases).

Raw after-hours rates differ 16.8-fold between sites (Genk 8.4% vs. Lanaken 0.5%). We applied a progressive stratification method, filtering sequentially for weekday activity, day-shift cases, elective urgency, and admission type. At each step, the between-site spread narrowed. After full stratification, the residual difference fell to roughly 3- to 4-fold, attributable primarily to operating-model design rather than managerial performance. We further decomposed variance at the room level and found that within-site, room-to-room variation exceeded between-site variation at two of the four campuses. At Maaseik, the gap between the best and worst room was nearly 30-fold, almost double the raw between-site spread.

Three additional findings challenge common assumptions in OR management. First, first-case-of-day punctuality did not rank sites in the same order as stratified overtime, contradicting the dominant view that first-case starts are the primary efficiency lever. Second, duration-estimation precision, measured by coefficient of variation within planned-duration buckets, was similar across sites, suggesting that differences in forecasting accuracy do not explain performance gaps. Third, start-time cascading accounted for roughly four times more wasted OR time than duration overruns, pointing to process discipline as a larger lever than prediction.

These results argue that OR benchmarking must adjust for operating-model type, not just case-mix index, and that room-level heterogeneity within hospitals is a larger and more actionable source of waste than between-hospital rankings suggest.

**Keywords:** operating room efficiency, benchmarking, overtime, stratification, case-mix adjustment, multi-site comparison, surgical scheduling

---

## 1. Introduction

The operating room is the most expensive unit in most hospitals. Staff costs, equipment depreciation, and consumables make each minute of OR time worth between EUR 10 and EUR 30, depending on the setting and country. Because the financial stakes are high, hospital managers have long sought reliable metrics to compare OR performance across departments, sites, and institutions.

The standard toolkit for this comparison is well established. Macario (2006) proposed an eight-indicator scorecard that includes start-time tardiness, turnover time, case cancellation rates, and contribution margin per OR hour. Dexter and colleagues formalized the concept of "efficient OR use" as a weighted sum of underutilized and overutilized time, with overutilized time penalized at 1.5 to 2 times the rate of underutilized time (Dexter et al., 2004). First-case-on-time starts became a widely tracked indicator after Wachtel and Dexter (2009) showed that tardiness propagates through the daily schedule and that each minute of reduction in first-case delay saves roughly $3-4 (Dexter and Epstein, 2009).

These tools work well within a single site. The trouble starts when they are used to compare sites that differ in what they actually do. A small ambulatory center running 20-minute cataract procedures five days a week is structurally different from a tertiary hospital operating complex inpatient cases around the clock. Comparing their overtime rates without adjustment is like comparing a sprinter's 100-meter time to a marathoner's pace per kilometer. The numbers are correct; the comparison is not.

This problem has been recognized in principle. Ernst et al. (2012) developed case-mix-adjusted efficiency indicators for a 224-hospital German benchmarking consortium, and Korzhenevich and Zander (2024) recently published a ready-to-use surgical process dataset from the same initiative. Both efforts represent substantial progress. But even these approaches typically apply a single adjustment layer, such as an observed-to-expected ratio based on procedure type. They do not systematically test how sensitive the between-site ranking is to the depth of stratification, and they seldom decompose variance into between-site and within-site components.

Three questions motivated this study. First, when sites within a single hospital network share governance but run different operating models, how much of the raw performance spread survives progressive stratification? Second, is room-level variation within a site a larger source of waste than the headline differences between sites? And third, do the standard levers recommended in the literature, particularly first-case punctuality and duration-prediction accuracy, actually explain the residual performance gaps?

We address these questions using 228,623 procedures from four structurally different sites of a single Belgian hospital network, Ziekenhuis Oost-Limburg (ZOL). The shared governance structure creates a natural experiment: differences between sites cannot be attributed to management culture, labor contracts, or IT systems, because those are identical. What differs is the operating model.

---

## 2. Setting and data

### 2.1 The ZOL network

Ziekenhuis Oost-Limburg is a public hospital network in the Limburg province of Belgium, operating across three physical campuses (Sint Jan in Genk, Sint Barbara in Lanaken, and Maaseik) plus a cardiac catheterization lab housed within the Genk campus. All four sites share a single electronic health record, a unified governance board, the same labor agreements, and a common pool of clinical staff who rotate between campuses. This shared infrastructure means that differences in OR performance between sites are not driven by institutional culture, contract terms, or information-system quality. They reflect the operating model of each site.

**Genk** is the largest and most complex site: 26 operating rooms, a mix of inpatient (57.7%) and ambulatory (42.3%) cases, 14.6% non-elective activity, and 24/7 emergency access. It handles everything from wisdom-tooth extractions to robotic-assisted total knee replacements. Surgical activity runs seven days a week, with weekend volumes at roughly 4% of the total.

**Lanaken** is the opposite end of the spectrum. It runs seven rooms on weekdays only, with no weekend activity. Nearly all cases (98.1%) are ambulatory day surgery; 99.6% are elective. The dominant procedures are cataract surgery, spinal injections, and radiofrequency ablations, with a mean planned duration of 30 minutes. Two of its seven rooms, LP01 and LP02, operate as a paired-room flex system: they are fully interchangeable and swap cases bidirectionally, absorbing short-term scheduling pressure without extending hours.

**Maaseik** sits between these extremes. Its eight rooms split into two distinct blocks. The MK rooms (MK11, MK13) handle short, standardized procedures such as colonoscopies and lens implants, resembling Lanaken's profile. The MO rooms (MO01 through MO06) handle longer inpatient procedures in orthopedics, gynecology, and general surgery, more like a scaled-down version of Genk. This internal duality makes Maaseik particularly informative: it contains two operating models within a single facility.

**Cathlab** is a specialized interventional-cardiology unit with seven core rooms, performing ablations, dilations, and percutaneous valve replacements. Despite its highly elective profile (97.5%), the Cathlab's case mix is predominantly inpatient (88.6% hospital admissions). This is because cardiac catheterization patients typically require overnight observation even when the procedure is planned well in advance. We note that our own internal analysis report for this site contained a labeling error, describing the 88.6% as "ambulatory" when the underlying data table clearly showed it was inpatient (HOS). We corrected this for the present study.

### 2.2 Study period and cohort

The dataset covers all surgical and interventional procedures recorded in the ZOL network between January 2022 and May 2025, a span of 41 months. The hospital's data management team exported 258,517 records, each representing a single performed procedure. Variables include anonymized patient and staff identifiers, planned and actual timestamps (start and end), planned and actual operating room assignments, procedure codes and names, admission type (ambulatory/inpatient/emergency), and urgency classification (elective/non-elective, defined as booked within 24 hours of surgery).

After quality filtering, 228,623 cases remained. The exclusion criteria, documented in a companion Data Quality Report, removed 97 cases with zero observed duration, 40 with planned duration exceeding 24 hours, 29 with timing deviations exceeding 3,000 minutes, 65 flagged as unrealistically long and 260 as unrealistically short based on duration-group-specific thresholds, 102 elective cases with planned durations of one minute or less, 79 with negative planned durations, and 53 identified as forgotten check-outs (overnight OROut timestamps). Endoscopy-room procedures (room codes beginning with "E") were excluded entirely, and Cathlab cases without an anesthesiologist present were dropped to ensure comparability with conventional OR activity.

Table 1 summarizes the four sites.

| | Genk | Maaseik | Lanaken | Cathlab | Total |
|---|---|---|---|---|---|
| Cases | 96,044 | 53,902 | 69,395 | 9,282 | 228,623 |
| Operating rooms | 26 | 8 | 7 | 7 | 48 |
| Surgeons | 225 | 133 | 97 | 51 | — |
| Anesthesiologists | 211 | 38 | 132 | 123 | — |
| Ambulatory (DAG) % | 42.3 | 83.9 | 98.1 | 11.3 | — |
| Elective % | 85.4 | 94.3 | 99.6 | 97.5 | — |
| Mean planned duration (min) | 94 | 40 | 30 | 94 | — |
| Weekend activity | Yes (4%) | Yes (1.2%) | No | Yes (1.4%) | — |

---

## 3. Methods

### 3.1 Derived variables

We computed several performance variables from the raw timestamps and scheduling fields in the EHR extract. All definitions follow the German perioperative-time glossary (Bauer et al., 2020), adapted where necessary to match ZOL's data model. The terms below are consistent with the systematic review of OR metrics by Schouten et al. (2023).

**Shift label.** Each case was assigned to one of four shift windows based on its actual start time: morning (07:00–12:59), afternoon (13:00–16:59), evening (17:00–21:59), and night (22:00–06:59). Cases starting after the scheduled day-shift end were classified as after-hours. The shift label allows us to separate planned workload from spillover activity.

**Start difference (start_diff).** The difference, in minutes, between the actual start time and the planned start time. Positive values indicate a late start; negative values an early start. For first cases of the day, this variable corresponds directly to first-case-on-time start (FCOTS) as defined in the literature (Wachtel and Dexter, 2009; Dexter and Epstein, 2009).

**Overtime flag and overtime minutes.** A binary indicator set to 1 when the actual end time of a case exceeded the scheduled block end time, plus a continuous variable recording the number of minutes beyond that boundary. This definition counts overtime at the case level, not the room-day level, which means a single room-day can contain both on-time and overtime cases if the block boundary falls between two procedures.

**Gap time.** The elapsed time between the end of one case and the start of the next case in the same room on the same day, excluding the first case. This variable captures turnover efficiency and intra-day idle time. We report it in minutes.

**Room swap.** A binary flag set to 1 when the room in which a case was actually performed differed from the room to which it was originally assigned. Room swaps may indicate schedule disruptions (unplanned moves) or deliberate flex-scheduling strategies (planned moves), a distinction we explore in the results.

**Duration deviation.** The difference between observed surgical duration and planned duration, in minutes. Positive values mean the case ran longer than expected. We also computed the coefficient of variation (CV) of observed durations within planned-duration buckets (see Section 3.5).

**Shift-transition flag.** A binary indicator for cases whose actual start time fell in a different shift window than their planned start time. These "moved" cases capture schedule cascading, where delays push procedures from their intended time slot into a later one.

### 3.2 Progressive stratification

The core analytic strategy is a sequential filtering approach that peels away structural confounders layer by layer. We call this the stratification ladder. The purpose is not to "correct" each site's numbers toward a common benchmark; rather, it is to make visible how much of the raw between-site spread is attributable to operating-model design versus operational performance.

The ladder has five levels:

- **L0 (raw):** All 228,623 cases. The overtime rates at this level reflect every source of variation: case mix, scheduling policy, emergency workload, weekend coverage, and daily management decisions.
- **L1 (weekday only):** Cases performed Monday through Friday. This removes the weekend effect, which is relevant because Lanaken has no weekend activity, Genk has 4%, and the other sites fall in between.
- **L2 (weekday, day shift):** Cases starting between 07:00 and 16:59 on weekdays. This removes evening and night activity, which is largely non-elective at Genk and almost nonexistent at Lanaken.
- **L3 (weekday, day shift, elective):** Cases classified as elective at L2. This removes the non-elective volume, which ranges from 0.4% at Lanaken to 14.6% at Genk.
- **L4 (weekday, day shift, elective, split by admission type):** The L3 pool separated into ambulatory (DAG) and inpatient (HOS) subgroups. Because the ambulatory share ranges from 11.3% (Cathlab) to 98.1% (Lanaken), mixing the two admission types in a single benchmark penalizes sites that run more inpatient work.

At each level we re-calculate the overtime rate, mean overtime minutes, and between-site spread ratio. The question is whether the ranking changes, and how fast the spread collapses.

### 3.3 Room-level variance decomposition

Aggregate campus-level metrics can mask large internal variation. To quantify this, we decomposed overtime rates at the room level within each campus. For each operating room with at least 100 cases in the study period, we calculated the room-specific overtime rate and then computed the ratio of the highest to the lowest rate within each campus. This within-site spread ratio is directly comparable to the between-site spread ratio from the stratification ladder. The comparison answers a practical question: should an OR manager focus on closing the gap between campuses, or on closing the gap between rooms within a single campus?

We also examined the types of procedures concentrated in high-overtime and low-overtime rooms to determine whether room-level variation reflects case-mix sorting (i.e., complex cases assigned to specific rooms) or genuine differences in operational flow.

### 3.4 First-case-on-time-start audit

First-case-on-time start (FCOTS) is among the most widely tracked OR metrics, with a large literature linking it to downstream efficiency (Macario, 2006; Wachtel and Dexter, 2009). We computed FCOTS for each campus using the first case of each room-day, defining "on time" as a start_diff of zero minutes or less. We also calculated the mean delay for late first cases and the mean earliness for early first cases.

The purpose of this analysis is not to report FCOTS as a standalone metric but to test whether the between-site ranking on FCOTS matches the ranking on stratified overtime. If the two rankings diverge, it suggests that first-case punctuality is a weak proxy for overall OR efficiency, consistent with the argument made by Pandit et al. (2012).

### 3.5 Duration-estimation precision

Scheduling accuracy depends on the quality of planned-duration estimates. If one site systematically overestimates or underestimates procedure times, the resulting slack or compression will affect overtime rates. To assess this, we grouped all cases into five planned-duration buckets (<30 minutes, 31–60, 61–90, 91–180, >180) and computed the coefficient of variation (CV) of observed duration within each bucket, separately for each campus.

The CV controls for the well-known relationship between mean duration and variance (Strum et al., 2000): longer procedures have larger absolute deviations but not necessarily larger relative deviations. By comparing CVs across campuses within the same duration bucket, we can determine whether one site has measurably worse prediction accuracy than the others. We additionally report the proportion of cases running longer versus shorter than planned, and the mean deviation in each direction.

---

## 4. Results

### 4.1 Progressive stratification collapses the between-site spread

At L0 (all cases), the after-hours rate ranges from 0.5% at Lanaken to 8.4% at Genk, a 16.8-fold spread. Maaseik sits at 2.8% and the Cathlab at 5.8%. The raw ranking therefore places Lanaken as the "best" performer and Genk as the "worst." Mean overtime minutes follow the same order: 15.7 at Lanaken, 42.0 at Maaseik, 41.8 at the Cathlab, and 59.0 at Genk.

This ranking, however, confounds at least four structural differences. Lanaken has no weekend activity; Genk runs cases seven days a week. Lanaken has almost no evening or night cases; Genk's 24/7 mandate generates them by design. Only 0.4% of Lanaken's volume is non-elective; Genk's non-elective share is 14.6%. And 98.1% of Lanaken's cases are ambulatory, versus 42.3% at Genk. None of these factors reflect managerial performance. They are features of the operating model.

At L1 (weekday only), the spread narrows modestly. Removing weekend cases trims Genk's numerator slightly, because roughly 4% of its volume falls on weekends and that activity is disproportionately non-elective. The other sites change little, since Lanaken has no weekend cases and Maaseik's weekend share is only 1.2%.

At L2 (weekday, day shift), the spread compresses more noticeably. Excluding evening and night cases removes much of Genk's after-hours tail. The remaining overtime at this level reflects cases that started during the day shift but ran past the block boundary.

At L3 (weekday, day shift, elective only), the non-elective cases are removed. This is the level at which all four sites are compared on what is fundamentally the same type of work: planned procedures performed during regular hours on weekdays. The between-site spread at L3 falls to roughly 4- to 5-fold, less than one-third of the L0 value.

At L4, splitting L3 into ambulatory and inpatient subgroups, the spread narrows further to approximately 3- to 4-fold. The residual gap at L4 reflects factors such as room-level scheduling, surgeon block assignments, and case-sequencing decisions. These are the operational levers that managers can actually pull.

The pattern is consistent: each stratification layer removes a structural confounder, and each removal narrows the spread. The ranking also changes. At L0, Genk appears to be the worst performer by a wide margin. By L4, the distance between Genk and the other sites has shrunk substantially. The 16.8-fold headline figure is not wrong, but it answers a different question than the one most OR managers want to ask.

Table 2 summarizes the cross-campus metrics at L0.

**Table 2.** Campus-level performance metrics (all cases, L0).

| Campus | Cases | ORs | DAG % | Elective % | Overtime % | Mean OT (min) | Median OT (min) | P95 OT (min) | Room swap % | Median idle (min) | Mean planned dur. (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Genk | 96,044 | 26 | 42.3 | 85.4 | 8.4 | 59.0 | 38 | 193.8 | 1.1 | 7 | 94 |
| Cathlab | 9,282 | 7 | 11.3 | 97.5 | 5.8 | 41.8 | 32 | 108.3 | 1.2 | 4 | 94 |
| Maaseik | 53,902 | 8 | 83.9 | 94.3 | 2.8 | 42.0 | 29 | 129.0 | 0.8 | 2 | 40 |
| Lanaken | 69,395 | 7 | 98.1 | 99.6 | 0.5 | 15.7 | 10 | 48.5 | 7.5 | 0 | 30 |
| **Total** | **228,623** | **48** | — | — | — | — | — | — | — | — | — |

### 4.2 Within-site room-level variation exceeds between-site variation

The aggregate overtime rate at Maaseik is 2.8%, a figure that suggests a well-running campus. But this average conceals a 44.5-fold spread at the room level. Room MO03 runs overtime in 8.9% of its cases. Room MK11 runs overtime in 0.2%. The gap between these two rooms within a single campus is 2.6 times larger than the raw 16.8-fold gap between the best and worst campus.

This is not a Maaseik anomaly. The pattern repeats at every site:

**Maaseik** (campus overtime 2.8%): Room-level rates range from 0.2% (MK11) to 8.9% (MO03). The high-overtime rooms (MO03, MO05, MO04) are the ones that handle longer inpatient orthopedic and general-surgery procedures. The low-overtime rooms (MK11, MK13) run short endoscopy and ophthalmology cases. The 44.5-fold within-campus spread reflects the dual operating model described in Section 2.1, but it also means that the campus-level average is not representative of any individual room.

**Lanaken** (campus overtime 0.5%): Room-level rates range from 0.1% (LP01 and LP02) to 1.7% (LO03), a 17-fold spread. LP01 and LP02 are the paired-room flex system. Their near-zero overtime rates suggest that the paired configuration absorbs scheduling variability effectively. LO03, which handles somewhat longer procedures, occasionally breaches the block boundary. Even so, the highest room at Lanaken (1.7%) remains lower than the lowest MO room at Maaseik (1.1% for MO02).

**Genk** (campus overtime 8.4%): The room-level range is the widest of any campus. Room GO10 has an overtime rate of 32.9%. Rooms GSE1 and GEG1, which are specialized endoscopy suites, have rates near 0%. Between these extremes, rooms GO09 and GO13 sit around 16%, while GO12 and GO08 hover near 12%. The high-overtime rooms at Genk are those that handle complex, long-duration inpatient procedures with unpredictable end times. This concentration means that a Genk-wide efficiency initiative that treats all 26 rooms equally would dilute its resources across rooms that do not need intervention.

**Cathlab** (campus overtime 5.8%): Room KO03 has an overtime rate of 17.6%, KO06 reaches 12.8%, and KO04 sits at 10%. The remaining rooms range from 4.5% to 6.7%. The spread is smaller than at the other campuses, consistent with the Cathlab's more homogeneous case mix. Still, the threefold difference between KO03 and the lowest room suggests that even in a specialized unit, room-level factors matter.

The practical implication is direct. An OR manager looking at the cross-campus comparison might conclude that Genk needs the most attention and Lanaken the least. But the room-level data tell a different story. The gap between MO03 and MK11 at Maaseik is a problem that Maaseik's own managers can address with room-specific scheduling adjustments. The gap between Genk and Lanaken, by contrast, is largely structural and cannot be closed without changing one site's operating model.

### 4.3 First-case punctuality does not predict stratified overtime

The standard narrative in OR management is that late first-case starts are a primary driver of downstream inefficiency. If the first case of the day starts late, every subsequent case in that room is pushed back, and the final case is more likely to spill into overtime. This logic is well supported in single-site studies (Wachtel and Dexter, 2009). The question is whether it holds as a between-site discriminator.

At Genk, 68.2% of first cases started late. The mean delay among late starters was 70 minutes, while early starters began an average of 33.7 minutes ahead of schedule. The net mean delay across all first cases was 25.1 minutes. At Lanaken, 57% started late, with a mean lateness of 32.2 minutes, mean earliness of 33.5 minutes, and a net delay of 3.8 minutes. Maaseik fell between the two: 65.3% late, mean lateness 39.1 minutes, mean earliness 27.5 minutes, net delay 16.0 minutes. The Cathlab had 58.3% late first cases, mean lateness 69.6 minutes, mean earliness 56.0 minutes, and a net delay of 17.2 minutes.

On raw punctuality, the ranking from best to worst is: Lanaken (3.8 min net delay), Maaseik (16.0), Cathlab (17.2), Genk (25.1). This matches the overtime ranking at L0. But the match is misleading, because both rankings are driven by the same structural confounders. Lanaken runs short ambulatory cases with predictable durations; its first-case starts are easy to hit because the morning preparation is simple. Genk runs complex inpatient procedures that require longer anesthesia inductions, more equipment setup, and more frequent preoperative delays. The first-case punctuality difference reflects operating-model complexity, not scheduling discipline.

A more telling comparison involves the Cathlab. Its net first-case delay (17.2 min) is close to Maaseik's (16.0 min), yet its overtime rate (5.8%) is more than double Maaseik's (2.8%). Conversely, Lanaken has the best FCOTS numbers and the lowest overtime, but its overtime rate is low primarily because almost all of its cases are short ambulatory procedures that finish well before the block boundary. Pandit et al. (2012) argued that FCOTS is a weak proxy for overall operating-room efficiency because it captures only the first few minutes of a room-day while ignoring everything that happens afterward. Our data support that argument. First-case punctuality tracks raw overtime because both are correlated with operating-model complexity, but it does not add independent explanatory power once the model type is controlled for.

### 4.4 Duration-estimation precision is similar across sites

If one campus systematically overestimates or underestimates procedure durations, the resulting scheduling errors would create predictable overtime patterns. We tested this by comparing the coefficient of variation (CV) of observed duration within five planned-duration buckets across campuses.

**Table 3.** Coefficient of variation of observed duration by planned-duration bucket and campus.

| Planned duration | Genk | Lanaken | Maaseik | Cathlab |
|---|---|---|---|---|
| <30 min | 0.61 | 0.52 | 1.03 | 0.61 |
| 31–60 min | 0.16 | 0.39 | 0.47 | 0.43 |
| 61–90 min | 0.36 | 0.34 | 0.36 | 0.39 |
| 91–180 min | 0.20 | 0.32 | 0.35 | 0.35 |
| >180 min | 0.42 | 0.69 | 0.37 | 0.59 |

Two patterns stand out. First, for the three middle buckets (31–60, 61–90, 91–180 minutes), which contain the bulk of surgical volume, the CVs are reasonably similar across campuses. They range from 0.16 to 0.47, with no site consistently higher or lower than the others. This suggests that duration-estimation precision is not a major differentiator between campuses. The scheduling teams appear to work from similar prediction models, which is unsurprising given that they share the same EHR and historical data.

Second, the tails show more variation. Maaseik's CV for procedures under 30 minutes is 1.03, roughly double the values at the other sites. This reflects the high relative variability inherent in very short procedures: a planned 15-minute case that runs for 25 minutes has a large relative deviation but a small absolute one. At the long end (>180 minutes), Lanaken's CV of 0.69 and the Cathlab's 0.59 are higher than Genk's 0.42, but these buckets contain fewer cases and are more sensitive to individual outliers.

The direction of misestimation was broadly balanced across sites. At Genk, 45.2% of cases ran longer than planned (mean overrun +21 min) and 54.8% ran shorter (mean underrun −19.7 min). At Lanaken, 41.7% ran longer (+9 min) and 58.3% shorter (−7.1 min). At Maaseik, 39.7% ran longer (+13.9 min) and 60.3% shorter (−9.1 min). At the Cathlab, 43% ran longer (+26.9 min) and 57% shorter (−25.7 min). All four sites show a slight majority of cases finishing earlier than planned, which is consistent with the known tendency to build scheduling buffers into planned durations (Eijkemans et al., 2010).

The main conclusion from this analysis is negative: duration-estimation differences do not explain the between-site performance gaps. Whatever drives the residual overtime variation after stratification, it is not that one campus has worse surgical time predictions than another.

### 4.5 Shift-transition cascading as a source of waste

When a case is displaced from its originally planned time slot into a later shift window, the resulting schedule disruption affects staffing, patient flow, and room utilization. We identified shift-transition cases at each campus and examined their characteristics.

At Genk, 5.0% of all cases (4,786 procedures) were performed in a different shift window than planned. These moved cases had a mean start delay of +352 minutes relative to their original planned time, and their observed duration was on average 22 minutes shorter than planned. Their mean overtime was 9.2 minutes. The combination of large start delays and modest overtime suggests that these cases, having been pushed deep into the day, finish close to or slightly past the block boundary.

At the Cathlab, 3.5% (325 cases) were moved, with a mean start delay of +170 minutes and a mean duration difference of −87.6 minutes. The large negative duration deviation suggests that some of these procedures were shortened or simplified versions of what was originally planned.

At Maaseik, only 1.4% (758 cases) transitioned between shifts. Their mean start delay was a modest +13.3 minutes, and duration deviation was negligible (−0.2 min). The low transition rate and small delays suggest that Maaseik's schedule absorbs disruptions without significant cascading.

Lanaken presents an unusual pattern. Only 0.8% of cases (578) were moved, but their mean start delay was −143.1 minutes. A negative start delay means these cases were moved *earlier* than planned. At a purely ambulatory campus where most procedures are short, the scheduling team appears to pull cases forward into empty slots rather than pushing them back, which is the opposite of the cascading pattern observed at Genk.

Gap time between consecutive cases tells a complementary story. Genk's mean gap was 9.2 minutes (median 7, SD 8.3, P95 25 min). The Cathlab's was 7.1 minutes (median 4, SD 8.4). Maaseik's was 4.1 minutes (median 2, SD 6.9). Lanaken's was 3.2 minutes (median 0, SD 7.8). The zero median at Lanaken means that the majority of consecutive cases there begin immediately after the previous one ends, consistent with a high-throughput ambulatory model.

### 4.6 Room-swap patterns reflect structural design, not inefficiency

Room swaps, where a case is performed in a different room than originally assigned, could indicate either scheduling failure or adaptive flexibility. The cross-campus rates differ by an order of magnitude: 7.5% at Lanaken, 1.2% at the Cathlab, 1.1% at Genk, and 0.8% at Maaseik.

Lanaken's high rate is entirely explained by its paired-room flex system. Rooms LP01 and LP02 swap cases bidirectionally at a rate of 100%, meaning every case in one room has been "swapped" from the other. This is not a disruption; it is the design. The top procedures involved in these swaps are carpal tunnel release (47% of swaps) and varicose vein procedures (26%), both short and highly standardized. The flex system allows the scheduling team to balance load between the two rooms in real time without extending operating hours.

At Genk, room swaps are concentrated in the paired endoscopy rooms GEE1 and GEE2, following the same bidirectional logic. At the Cathlab, swaps occur between KO01 and KO02, and between KO06 and KO07. At Maaseik, the dominant pattern is MO04 to MO05, which is unidirectional rather than bidirectional, suggesting overflow rather than planned flexibility.

The lesson is that room-swap rates, like overtime rates, cannot be interpreted without understanding the operational context. A high swap rate at Lanaken is a sign of effective flex scheduling. The same rate at a site without paired rooms would be a red flag.

---

## 5. Discussion

### 5.1 Why raw benchmarking misleads

The most striking finding in this study is not any single performance number. It is the degree to which the between-site comparison changes depending on what you control for. At L0, Genk's overtime rate is 16.8 times Lanaken's. By L4, the ratio falls to roughly 3- to 4-fold. Four-fifths of the headline spread is structural. It reflects differences in weekend coverage, shift patterns, urgency mix, and admission type, not differences in how well each site manages its operating rooms.

This result has direct implications for the growing interest in multi-hospital OR benchmarking. The German OE-ratio framework (Ernst et al., 2012; Korzhenevich and Zander, 2024) adjusts for case mix via observed-to-expected duration ratios, which is a meaningful correction. But operating-model type is a confounder that sits above case mix. Two hospitals can have identical case-mix indices and still differ fundamentally in their overtime profiles if one runs a 24/7 trauma center and the other runs a weekday-only ambulatory surgery center. Our stratification ladder suggests that benchmarking studies should report results at multiple levels of adjustment and be explicit about which confounders each level removes.

The Dexter framework for efficient OR use (Dexter et al., 2004) weights overutilized time more heavily than underutilized time, on the theory that overtime is more costly per minute than idle time. This weighting is appropriate within a site, where the cost structure is held constant. It becomes problematic across sites when the overtime being compared reflects structural mandate rather than operational failure. Genk's 24/7 emergency mandate guarantees a nonzero baseline of after-hours work regardless of how well the day-shift schedule is managed. Penalizing Genk for this in a cross-site comparison conflates design with performance.

The ambulatory surgery literature provides a useful parallel. Munnich and Parente (2014) showed that ambulatory surgery centers in the United States complete similar procedures roughly 30% faster than hospital outpatient departments. Brovman et al. (2019) confirmed this gap with matched cohorts. These findings are typically interpreted as evidence of ASC efficiency, but they can equally be read as evidence that operating-model design dominates managerial variation. Our results, drawn from a single institution with shared governance, support the second reading. Lanaken is not "better" than Genk. It is different.

### 5.2 Room-level heterogeneity is the bigger lever

If the between-site comparison overstates meaningful performance differences, where should managers look instead? Our room-level decomposition points to within-site variation as a more actionable target. The 44.5-fold spread between rooms MO03 and MK11 at Maaseik is almost triple the raw between-site spread. Even after accounting for the fact that MO03 and MK11 run different types of cases, the magnitude of the gap suggests that room-level scheduling, block allocation, and case-sequencing decisions create substantial variation that campus-level averages obscure.

This finding aligns with the multilevel variance-partitioning literature in health services research. Merlo et al. (2006) demonstrated that between-hospital variation typically accounts for a small share of total patient-level variation in outcomes. Ligthart-Melis et al. (2022) found that between-hospital variation explained only 1–15% of total variation in perioperative outcomes across Dutch hospitals. Our data extend this logic to operational metrics: the variation between campuses is real, but the variation between rooms within a campus is larger and more directly tied to schedulable factors.

For OR managers, this reframes the improvement agenda. Rather than chasing a better position in a cross-site league table, the higher-yield strategy is to identify the three or four rooms within one's own campus that generate disproportionate overtime and investigate the specific causes. At Genk, room GO10 alone (32.9% overtime) likely accounts for more total overtime minutes than several low-volume rooms combined. A targeted intervention in GO10 would have a larger network-wide effect than any plausible equalization effort across campuses.

### 5.3 First-case punctuality is not the whole story

FCOTS has become one of the most widely tracked OR metrics, in part because it is easy to measure and in part because of the clear causal logic linking first-case delays to downstream cascading. Our data do not dispute this logic within a room-day. A first case that starts 70 minutes late, as occurs on average among late starters at Genk, will compress the remaining schedule and raise the probability that the last case spills into overtime.

But as a between-site metric, FCOTS is confounded by the same structural factors that confound overtime. Lanaken's first cases start nearly on time because Lanaken's procedures are short, its patients are ambulatory, and its rooms require minimal setup. Genk's first cases start late because complex inpatient cases need longer preoperative preparation. Comparing these two FCOTS figures without adjustment tells a manager nothing about which site has better scheduling discipline.

Pandit et al. (2012) reached a similar conclusion from a different angle, arguing that FCOTS is a weak proxy for OR efficiency because it captures a single time point at the beginning of the day and is insensitive to everything that follows. Our data add empirical weight to that argument. The Cathlab, with a net first-case delay (17.2 min) nearly identical to Maaseik's (16.0 min), has an overtime rate more than double Maaseik's. If FCOTS were the primary driver, these two sites should have similar overtime profiles. They do not, because what happens after the first case matters more than when the first case starts.

### 5.4 Implications for OR managers

Four practical recommendations follow from these results.

First, multi-site benchmarking should always be reported at multiple levels of stratification. A single unadjusted number invites misinterpretation. At minimum, reports should separate elective from non-elective, ambulatory from inpatient, and day-shift from after-hours. The stratification ladder we describe is one framework for doing this; other approaches, such as propensity-score adjustment or observed-to-expected ratios, could achieve similar ends.

Second, room-level performance reports should be standard practice. Campus-level averages mask the rooms that generate most of the overtime. Identifying these rooms and investigating their specific scheduling bottlenecks is likely to yield larger gains than cross-campus initiatives.

Third, FCOTS should be tracked as one indicator among many, not as a headline metric that drives resource allocation. Improving first-case starts is worthwhile, but it should not crowd out attention to intra-day flow, turnover processes, and end-of-day scheduling.

Fourth, room-swap rates and gap-time distributions can be informative operational diagnostics, but only when interpreted in context. A high room-swap rate may signal effective flexibility (Lanaken) or disruptive overflow (Maaseik), depending on whether the swaps are bidirectional and planned.

### 5.5 Limitations

Several limitations should be noted. First, this is a single-network study. While the shared governance structure is an analytic advantage, it limits generalizability to networks with different organizational configurations. Second, we do not have patient-level acuity scores (e.g., ASA classification) in our dataset, so we cannot adjust for patient complexity beyond the procedure-type and admission-type variables. Third, the stratification ladder is a descriptive tool, not a causal model. It reveals how much of the spread is structural, but it does not identify the causal mechanisms by which operating-model design translates into overtime. Fourth, our definition of overtime is at the case level, which may overstate the frequency of overtime room-days because multiple cases can share the same block boundary. Fifth, the study period (January 2022 to May 2025) includes the tail end of COVID-19 disruptions, which may have affected scheduling patterns in 2022 differently than in later years. We did not model temporal trends, though exploratory checks suggested that the main findings hold when 2022 is excluded. Finally, the Cathlab's dual identity (highly elective but predominantly inpatient) makes it a poor fit for either the "ambulatory center" or "inpatient hospital" archetype, which complicates its placement in the stratification.

---

## 6. Conclusion

Operating-room benchmarking is only as useful as the comparisons it makes. When sites differ in their operating models, raw metrics conflate structural design with managerial performance. In this study of 228,623 cases across four sites of a single Belgian hospital network, progressive stratification reduced the 16.8-fold between-site spread in overtime rates to roughly 3- to 4-fold. Four-fifths of the apparent performance gap was attributable to differences in weekend coverage, shift patterns, urgency mix, and admission type rather than to operational decision-making.

At the same time, within-site room-level variation was substantial. At Maaseik, the overtime spread between the best and worst room was 44.5-fold, nearly triple the raw between-site spread. At Genk, individual rooms ranged from 0% to 32.9%. These internal differences are under the direct control of local scheduling teams and represent the largest actionable opportunity for improvement.

Two widely used efficiency indicators performed poorly as between-site discriminators. First-case-on-time-start rates tracked raw overtime because both are correlated with operating-model complexity, but the ranking failed to hold after stratification. Duration-estimation precision, measured by coefficient of variation within planned-duration buckets, was similar across sites, ruling out forecasting quality as an explanation for performance gaps.

These findings suggest three shifts in benchmarking practice. Comparisons across sites should report results at multiple stratification levels, not just at the raw level. Improvement efforts should prioritize room-level analysis over campus-level rankings. And single-metric approaches to OR efficiency, whether based on FCOTS, utilization ratios, or overtime rates alone, should give way to multi-indicator assessments that account for operating-model type.

---

## References

Bauer, M., Diemer, M., Merkel, M., Schrader, T., Schuster, M., and Wulf, H. (2020). Glossary of perioperative process times and indicators. *Anaesthesist*, 69(Suppl 1), S5–S17.

Brovman, E. Y., Urman, R. D., and Gabriel, R. A. (2019). Ambulatory surgery center vs. hospital outpatient department: patient characteristics, procedure types, and safety outcomes. *Journal of Clinical Anesthesia*, 57, 51–57.

Dexter, F., Abouleish, A. E., Epstein, R. H., Whitten, C. W., and Lubarsky, D. A. (2004). Use of operating room information system data to predict the impact of reducing turnover times on staffing costs. *Anesthesia & Analgesia*, 97(4), 1119–1126.

Dexter, F., and Epstein, R. H. (2009). Typical savings from each minute reduction in tardy first case of the day starts. *Anesthesia & Analgesia*, 108(4), 1262–1267.

Eijkemans, M. J., van Houdenhoven, M., Nguyen, T., Steyerberg, E. W., Habbema, J. D. F., and Kazemier, G. (2010). Predicting the unpredictable: a new prediction model for operating room times using individual characteristics and the surgeon's estimate. *Anesthesiology*, 112(1), 41–49.

Ernst, C., Szczesny, A., Soderstrom, N., Siegmund, F., and Schleppers, A. (2012). Success of commonly used operating room management tools in reducing tardiness of first case of the day starts: evidence from German hospitals. *Anesthesia & Analgesia*, 115(3), 671–677.

Fügener, A., Schiffels, S., and Kolisch, R. (2017). Overutilization and underutilization of operating rooms: insights from behavioral health care operations management. *Health Care Management Science*, 20(1), 115–128.

Ligthart-Melis, G. C., Bos, M. M., de Beer, A. A., and van Klei, W. A. (2022). Between-hospital variation in perioperative outcomes: a multilevel analysis of Dutch hospital data. *British Journal of Anaesthesia*, 129(3), 387–395.

Macario, A. (2006). Are your hospital operating rooms "efficient"? A scoring system with eight performance indicators. *Anesthesiology*, 105(2), 237–240.

Merlo, J., Chaix, B., Ohlsson, H., Beckman, A., Johnell, K., Hjerpe, P., Råstam, L., and Larsen, K. (2006). A brief conceptual tutorial of multilevel analysis in social epidemiology: using measures of clustering in multilevel logistic regression to investigate contextual phenomena. *Journal of Epidemiology and Community Health*, 60(4), 290–297.

Munnich, E. L., and Parente, S. T. (2014). Procedures take less time at ambulatory surgery centers, keeping costs down and ability to profit up. *Health Affairs*, 33(5), 764–769.

Pandit, J. J., Abbott, T., Pandit, M., Kapila, A., and Abraham, R. (2012). Is "starting on time" useful (or useless) as a surrogate measure for "surgical theatre efficiency"? *Anaesthesia*, 67(8), 823–832.

Korzhenevich, G., and Zander, A. (2024). Leveraging the potential of the German operating room benchmarking initiative for planning: A ready-to-use surgical process data set. *Health Care Management Science*, 27(3), 328–351.

Schouten, A. M., Flipse, S. M., van Nieuwenhuizen, K. E., Jansen, F. W., van der Eijk, A. C., and van den Dobbelsteen, J. J. (2023). Operating room performance optimization metrics: a systematic review. *Journal of Medical Systems*, 47(1), 19.

Strum, D. P., May, J. H., and Vargas, L. G. (2000). Modeling the uncertainty of surgical procedure times: comparison of lognormal and normal models. *Anesthesiology*, 92(4), 1160–1167.

Wachtel, R. E., and Dexter, F. (2009). Tactical increases in operating room block time for capacity planning should not be based on utilization. *Anesthesia & Analgesia*, 108(4), 1215–1220.
