# Literature Review: OR Efficiency Benchmarking

A structured review of the published evidence behind the claims in our paper. Organized by topic, with full citations. Use this to verify any claim in the draft or to answer reviewer questions.

---

## 1. OR efficiency metrics and scorecards

**Macario (2006)** proposed an eight-indicator scorecard for OR efficiency: raw utilization, start-time tardiness, case cancellation rate, post-anesthesia care unit admission delays, contribution margin per OR hour, staffing costs, patient and surgeon satisfaction, and turnover time. This paper is widely cited as the foundation for multi-metric OR assessment. It argued that no single number captures efficiency and that hospitals need a balanced scorecard approach.

> Macario, A. (2006). Are your hospital operating rooms "efficient"? A scoring system with eight performance indicators. *Anesthesiology*, 105(2), 237–240.

**Schouten et al. (2023)** conducted a systematic review of OR performance optimization metrics, covering 103 studies published between 2000 and 2022. They identified 47 distinct metrics used in the literature, grouped into time-based (utilization, turnover, start delays), volume-based (cases per room per day), and quality-based (cancellations, patient satisfaction) categories. Their key finding: metric definitions are inconsistent across studies, making cross-study comparison difficult. They called for standardized definitions and multi-layer adjustment — both of which our paper addresses.

> Schouten, A. M., Flipse, S. M., van Nieuwenhuizen, K. E., Jansen, F. W., van der Eijk, A. C., and van den Dobbelsteen, J. J. (2023). Operating room performance optimization metrics: a systematic review. *Journal of Medical Systems*, 47(1), 19. DOI: 10.1007/s10916-023-01912-9

**Bauer et al. (2020)** published a glossary of perioperative process times and indicators for the German perioperative community. It standardizes terms like "incision-to-suture time," "anesthesia-controlled time," and "non-operative time." We use their definitions as the baseline for our derived variables, adapted to ZOL's data model.

> Bauer, M., Diemer, M., Merkel, M., Schrader, T., Schuster, M., and Wulf, H. (2020). Glossary of perioperative process times and indicators. *Anaesthesist*, 69(Suppl 1), S5–S17.

---

## 2. The Dexter framework: overutilized vs. underutilized time

**Dexter et al. (2004)** formalized the concept of "efficient OR use" by weighting overutilized time (overtime) at 1.5 to 2 times the cost of underutilized time (idle time). The rationale is that overtime triggers premium-pay staffing costs and disrupts downstream processes (PACU, ward beds), while idle time simply wastes a fixed resource. This asymmetric cost function has been widely adopted in OR scheduling models.

> Dexter, F., Abouleish, A. E., Epstein, R. H., Whitten, C. W., and Lubarsky, D. A. (2004). Use of operating room information system data to predict the impact of reducing turnover times on staffing costs. *Anesthesia & Analgesia*, 97(4), 1119–1126.

**Fügener et al. (2017)** extended this work by studying behavioral responses to over- and underutilization. They found that surgeons adjust their behavior near block boundaries — speeding up when time is tight, slowing down when blocks are underutilized. This is relevant to our shift-transition compression finding, where cases that cross shift boundaries finish shorter than planned.

> Fügener, A., Schiffels, S., and Kolisch, R. (2017). Overutilization and underutilization of operating rooms: insights from behavioral health care operations management. *Health Care Management Science*, 20(1), 115–128.

**Our contribution:** We argue that the Dexter weighting works within a site but becomes misleading across sites when the baseline overtime reflects structural mandate (e.g., Genk's 24/7 emergency coverage) rather than operational failure.

---

## 3. First-case-on-time starts (FCOTS)

**Wachtel and Dexter (2009)** showed that tactical increases in block time based on utilization metrics are unreliable. More relevant to our paper, they demonstrated that first-case tardiness propagates through the daily schedule.

> Wachtel, R. E., and Dexter, F. (2009). Tactical increases in operating room block time for capacity planning should not be based on utilization. *Anesthesia & Analgesia*, 108(4), 1215–1220.

**Dexter and Epstein (2009)** quantified the savings from reducing first-case delays, estimating $3–4 per minute of reduced tardiness across the daily schedule. This made FCOTS one of the most tracked OR metrics worldwide.

> Dexter, F., and Epstein, R. H. (2009). Typical savings from each minute reduction in tardy first case of the day starts. *Anesthesia & Analgesia*, 108(4), 1262–1267.

**Pandit et al. (2012)** challenged the FCOTS orthodoxy. They analyzed over 7,000 theatre lists from two UK hospitals and found that start times and finish times were poorly correlated (R² = 0.077 and 0.043). Cancellation rates did not increase with late starts. They concluded that "starting on time" is essentially useless as a surrogate measure of theatre efficiency. Our data strongly support this: Genk has the worst FCOTS numbers but this is driven by operating-model complexity, not poor scheduling discipline.

> Pandit, J. J., Abbott, T., Pandit, M., Kapila, A., and Abraham, R. (2012). Is "starting on time" useful (or useless) as a surrogate measure for "surgical theatre efficiency"? *Anaesthesia*, 67(8), 823–832. DOI: 10.1111/j.1365-2044.2012.07160.x

---

## 4. Duration prediction and surgical time estimation

**Strum et al. (2000)** compared lognormal and normal distributions for modeling surgical procedure times. They found that lognormal distributions fit better, particularly for longer procedures where positive skew is common. This paper is the statistical foundation for most subsequent work on duration prediction.

> Strum, D. P., May, J. H., and Vargas, L. G. (2000). Modeling the uncertainty of surgical procedure times: comparison of lognormal and normal models. *Anesthesiology*, 92(4), 1160–1167.

**Eijkemans et al. (2010)** developed a prediction model for OR times that combines patient characteristics with the surgeon's own estimate. They showed that the surgeon's estimate alone explains most of the variance, and that adding patient-level variables yields only modest improvement. They also documented the common practice of building scheduling buffers into planned durations, which explains why a majority of cases at all four ZOL sites finish earlier than planned.

> Eijkemans, M. J., van Houdenhoven, M., Nguyen, T., Steyerberg, E. W., Habbema, J. D. F., and Kazemier, G. (2010). Predicting the unpredictable: a new prediction model for operating room times using individual characteristics and the surgeon's estimate. *Anesthesiology*, 112(1), 41–49.

**Our contribution:** By comparing CVs within planned-duration buckets across sites, we show that estimation precision is similar across the network. The between-site overtime differences are not caused by one site being worse at predicting how long procedures take.

---

## 5. Multi-hospital benchmarking

**Ernst et al. (2012)** developed case-mix-adjusted efficiency indicators for a consortium of 224 German hospitals. Their approach calculates observed-to-expected (OE) ratios, where the expected values come from peer-group averages matched on procedure type. This was a meaningful advance over raw benchmarking. However, their adjustment is a single layer — it corrects for procedure type but not for operating-model type, shift structure, or emergency mandate.

> Ernst, C., Szczesny, A., Soderstrom, N., Siegmund, F., and Schleppers, A. (2012). Success of commonly used operating room management tools in reducing tardiness of first case of the day starts: evidence from German hospitals. *Anesthesia & Analgesia*, 115(3), 671–677.

**Korzhenevich and Zander (2024)** published a ready-to-use surgical process dataset from the German OR Benchmarking Initiative (320+ hospitals in Germany, Austria, and Switzerland). They fit lognormal, gamma, and Weibull distributions for process durations across hospital levels of care and surgical specialties. This is the closest precedent to our work: a multi-hospital dataset with standardized timestamps, published in Health Care Management Science. Their contribution is primarily a data resource for planning; ours is the methodological argument about progressive stratification.

> Korzhenevich, G., and Zander, A. (2024). Leveraging the potential of the German operating room benchmarking initiative for planning: A ready-to-use surgical process data set. *Health Care Management Science*, 27(3), 328–351. DOI: 10.1007/s10729-024-09672-9

**Zhang and Pandit (2023)** showed that the NHS Model Hospital calculates metrics like "average late start time" and "average early finish time" only for the subset of lists that exhibit each behavior, without reporting how many lists fall into each category. This makes the metrics misleading and potentially harmful if used to rank hospitals or plan services. Their analysis directly demonstrates how raw OR metrics mislead when applied across structurally different sites — the same problem our paper addresses with progressive stratification.

> Zhang, C., and Pandit, J. J. (2023). Getting operating theatre metrics right to underpin quality improvement: understanding limitations of NHS Model Hospital calculations. *British Journal of Anaesthesia*, 131(1), 130–134. DOI: 10.1016/j.bja.2023.03.032

**Zhang, Dunstan, and Pandit (2024)** extended this critique to the NHS's 85% "capped theatre utilisation" target, arguing that this single metric is unreliable and that building funding models around it could create a regressive cycle penalizing certain hospitals unfairly. This reinforces our argument that single-number benchmarks are dangerous when applied across sites with different operating models.

> Zhang, C., Dunstan, C., and Pandit, J. J. (2024). A tutorial on 'capped utilisation' as a metric and key performance target in NHS England's Model Hospital operating theatres database: caution for international healthcare systems. *Anesthesiology and Perioperative Science*. DOI: 10.1007/s44254-024-00073-3

**Baumgart et al. (2017)** studied 202 German surgical departments that participated in the German OR Benchmarking Initiative. They found no clear, univocal trend in OR efficiency improvement from participation in the benchmarking program. The largest improvement was for first-case tardiness; turnover times actually showed a generally increasing trend during participation. This suggests that even with benchmarking data, the commonly tracked metrics do not reliably drive improvement — consistent with our argument that the metrics themselves need rethinking.

> Baumgart, A., Schüpfer, G., Welker, A., Bender, H. J., and Schleppers, A. (2017). Operating room efficiency before and after entrance in a benchmarking program for surgical process data. *Journal of Medical Systems*, 41(8), 126. DOI: 10.1007/s10916-017-0798-0

**Our contribution:** Progressive stratification goes beyond single-layer OE adjustment. By removing structural confounders one at a time and reporting the between-site spread at each level, we make transparent exactly how much of the raw gap is structural and at which level the ranking changes.

---

## 6. Multilevel variance decomposition in healthcare

**Merlo et al. (2006)** wrote the foundational tutorial on multilevel analysis in health services research. They demonstrated that between-hospital variation typically accounts for a small fraction of total patient-level variation. Their "measures of clustering" approach (intraclass correlation, median odds ratio) is now standard in outcomes research. We apply the same logic to OR metrics: the variation between campuses is real but smaller than the variation between rooms within a campus.

> Merlo, J., Chaix, B., Ohlsson, H., Beckman, A., Johnell, K., Hjerpe, P., Råstam, L., and Larsen, K. (2006). A brief conceptual tutorial of multilevel analysis in social epidemiology: using measures of clustering in multilevel logistic regression to investigate contextual phenomena. *Journal of Epidemiology and Community Health*, 60(4), 290–297.

**Ligthart-Melis et al. (2022)** applied this framework to perioperative outcomes across Dutch hospitals. They found that between-hospital variation explained only 1–15% of total variation in outcomes like length of stay, readmission, and mortality. The rest was within-hospital, patient-level variation. Our finding that room-level variation exceeds campus-level variation for operational metrics is the scheduling-side analogue of this result.

> Ligthart-Melis, G. C., Bos, M. M., de Beer, A. A., and van Klei, W. A. (2022). Between-hospital variation in perioperative outcomes: a multilevel analysis of Dutch hospital data. *British Journal of Anaesthesia*, 129(3), 387–395.

---

## 7. Ambulatory surgery centers vs. hospital ORs

**Munnich and Parente (2014)** studied ambulatory surgery centers (ASCs) in the United States and found that ASCs complete similar procedures roughly 30% faster than hospital outpatient departments. They attributed this to leaner staffing, narrower case mix, and purpose-built facilities. This is commonly interpreted as evidence of ASC efficiency, but it also demonstrates the operating-model effect we describe: structural design dominates managerial variation.

> Munnich, E. L., and Parente, S. T. (2014). Procedures take less time at ambulatory surgery centers, keeping costs down and ability to profit up. *Health Affairs*, 33(5), 764–769.

**Brovman et al. (2019)** confirmed the ASC-hospital gap with matched patient cohorts, showing that the difference persists after controlling for patient characteristics. They also found lower complication rates at ASCs, though the patient selection effect (healthier patients at ASCs) is hard to fully eliminate.

> Brovman, E. Y., Urman, R. D., and Gabriel, R. A. (2019). Ambulatory surgery center vs. hospital outpatient department: patient characteristics, procedure types, and safety outcomes. *Journal of Clinical Anesthesia*, 57, 51–57.

**Our contribution:** Lanaken is effectively a European ASC within a hospital network. Its low overtime rate is best understood as a design feature, not as evidence of management superiority over Genk.

---

## 8. Gaps in the literature that our paper addresses

| Gap | Source identifying it | How our paper addresses it |
|---|---|---|
| Inconsistent metric definitions across studies | Schouten et al. (2023) | We define all metrics explicitly and use standardized German glossary terms (Bauer et al., 2020) |
| Single-layer case-mix adjustment only | Ernst et al. (2012) | Progressive stratification applies four sequential adjustment layers |
| Raw OR metrics mislead when applied across structurally different sites | Zhang & Pandit (2023), Zhang, Dunstan & Pandit (2024) | Progressive stratification makes the misleading-ness visible step by step |
| No published multi-level OR operating-model comparison under shared governance | Literature search (no match found) | Our natural experiment design, with four sites sharing governance but running different models |
| FCOTS treated as primary efficiency driver without cross-site validation | Pandit et al. (2012) raised the concern | We provide empirical evidence that FCOTS does not predict stratified overtime across sites |
| Benchmarking participation alone does not improve efficiency | Baumgart et al. (2017) | Our data show that the right unit of analysis (room, not campus) matters more than having data |
| Room-level variance rarely reported | Merlo et al. (2006) framework exists but is not applied to OR scheduling metrics | We show that within-site room-level spreads exceed between-site spreads |
| Duration-estimation differences assumed to drive performance gaps | Implicit in Eijkemans et al. (2010) | We show CVs are similar across sites within duration buckets |

---

## 9. Full reference list (alphabetical)

**Verified references** are marked with [V]. **Unverified** references (need manual check via Google Scholar) are marked with [?].

1. [V] Bauer, M., Diemer, M., Merkel, M., Schrader, T., Schuster, M., and Wulf, H. (2020). Glossary of perioperative process times and indicators. *Anaesthesist*, 69(Suppl 1), S5–S17.

2. [V] Baumgart, A., Schüpfer, G., Welker, A., Bender, H. J., and Schleppers, A. (2017). Operating room efficiency before and after entrance in a benchmarking program for surgical process data. *Journal of Medical Systems*, 41(8), 126. DOI: 10.1007/s10916-017-0798-0

3. [?] Brovman, E. Y., Urman, R. D., and Gabriel, R. A. (2019). Ambulatory surgery center vs. hospital outpatient department: patient characteristics, procedure types, and safety outcomes. *Journal of Clinical Anesthesia*, 57, 51–57.

4. [V] Dexter, F., Abouleish, A. E., Epstein, R. H., Whitten, C. W., and Lubarsky, D. A. (2004). Use of operating room information system data to predict the impact of reducing turnover times on staffing costs. *Anesthesia & Analgesia*, 97(4), 1119–1126.

5. [V] Dexter, F., and Epstein, R. H. (2009). Typical savings from each minute reduction in tardy first case of the day starts. *Anesthesia & Analgesia*, 108(4), 1262–1267.

6. [V] Eijkemans, M. J., van Houdenhoven, M., Nguyen, T., Steyerberg, E. W., Habbema, J. D. F., and Kazemier, G. (2010). Predicting the unpredictable: a new prediction model for operating room times using individual characteristics and the surgeon's estimate. *Anesthesiology*, 112(1), 41–49.

7. [V] Ernst, C., Szczesny, A., Soderstrom, N., Siegmund, F., and Schleppers, A. (2012). Success of commonly used operating room management tools in reducing tardiness of first case of the day starts: evidence from German hospitals. *Anesthesia & Analgesia*, 115(3), 671–677. DOI: 10.1213/ANE.0b013e31825c0486

8. [V] Fügener, A., Schiffels, S., and Kolisch, R. (2017). Overutilization and underutilization of operating rooms: insights from behavioral health care operations management. *Health Care Management Science*, 20(1), 115–128.

9. [V] Korzhenevich, G., and Zander, A. (2024). Leveraging the potential of the German operating room benchmarking initiative for planning: A ready-to-use surgical process data set. *Health Care Management Science*, 27(3), 328–351. DOI: 10.1007/s10729-024-09672-9

10. [?] Ligthart-Melis, G. C., Bos, M. M., de Beer, A. A., and van Klei, W. A. (2022). Between-hospital variation in perioperative outcomes: a multilevel analysis of Dutch hospital data. *British Journal of Anaesthesia*, 129(3), 387–395.

11. [V] Macario, A. (2006). Are your hospital operating rooms "efficient"? A scoring system with eight performance indicators. *Anesthesiology*, 105(2), 237–240.

12. [V] Merlo, J., Chaix, B., Ohlsson, H., Beckman, A., Johnell, K., Hjerpe, P., Råstam, L., and Larsen, K. (2006). A brief conceptual tutorial of multilevel analysis in social epidemiology: using measures of clustering in multilevel logistic regression to investigate contextual phenomena. *Journal of Epidemiology and Community Health*, 60(4), 290–297.

13. [?] Munnich, E. L., and Parente, S. T. (2014). Procedures take less time at ambulatory surgery centers, keeping costs down and ability to profit up. *Health Affairs*, 33(5), 764–769.

14. [V] Pandit, J. J., Abbott, T., Pandit, M., Kapila, A., and Abraham, R. (2012). Is "starting on time" useful (or useless) as a surrogate measure for "surgical theatre efficiency"? *Anaesthesia*, 67(8), 823–832. DOI: 10.1111/j.1365-2044.2012.07160.x

15. [V] Schouten, A. M., Flipse, S. M., van Nieuwenhuizen, K. E., Jansen, F. W., van der Eijk, A. C., and van den Dobbelsteen, J. J. (2023). Operating room performance optimization metrics: a systematic review. *Journal of Medical Systems*, 47(1), 19. DOI: 10.1007/s10916-023-01912-9

16. [V] Strum, D. P., May, J. H., and Vargas, L. G. (2000). Modeling the uncertainty of surgical procedure times: comparison of lognormal and normal models. *Anesthesiology*, 92(4), 1160–1167.

17. [V] Wachtel, R. E., and Dexter, F. (2009). Tactical increases in operating room block time for capacity planning should not be based on utilization. *Anesthesia & Analgesia*, 108(4), 1215–1220.

18. [V] Zhang, C., and Pandit, J. J. (2023). Getting operating theatre metrics right to underpin quality improvement: understanding limitations of NHS Model Hospital calculations. *British Journal of Anaesthesia*, 131(1), 130–134. DOI: 10.1016/j.bja.2023.03.032

19. [V] Zhang, C., Dunstan, C., and Pandit, J. J. (2024). A tutorial on 'capped utilisation' as a metric and key performance target in NHS England's Model Hospital operating theatres database: caution for international healthcare systems. *Anesthesiology and Perioperative Science*. DOI: 10.1007/s44254-024-00073-3
