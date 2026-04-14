# Reference Strategy: HCMS vs BMJ Quality & Safety

A side-by-side guide for the meeting with Niels and Maxim. Shows which references serve which journal and why.

---

## Shared references (both journals)

| # | Reference | Role | Verified? |
|---|---|---|---|
| 1 | Macario A. (2006). OR efficiency scorecard. *Anesthesiology* 105:237–40. | The standard metrics we're testing | [V] |
| 2 | Dexter F, et al. (2004). Turnover times and staffing costs. *Anesth Analg* 97:1119–26. | The dominant cost model we're critiquing | [V] |
| 3 | Dexter F, Epstein RH. (2009). Savings from FCOTS reduction. *Anesth Analg* 108:1262–7. | Quantifies the FCOTS value claim | [V] |
| 4 | Pandit JJ, et al. (2012). "Starting on time" is useless as surrogate. *Anaesthesia* 67:823–32. | Supports our FCOTS finding (R² = 0.04–0.08) | [V] |
| 5 | Schouten AM, et al. (2023). OR metrics systematic review. *J Med Syst* 47:19. | 47 metrics, no consistency, no interaction studies | [V] |
| 6 | Ernst C, et al. (2012). German OR management tools. *Anesth Analg* 115:671–7. | Best existing single-layer adjustment | [V] |
| 7 | Bauer M, et al. (2020). Perioperative glossary. *Anaesthesist* 69(S1):S5–17. | Variable definitions | [V] |
| 8 | Strum DP, et al. (2000). Lognormal surgical times. *Anesthesiology* 92:1160–7. | Statistical basis for duration analysis | [V] |
| 9 | Eijkemans MJ, et al. (2010). Predicting OR times. *Anesthesiology* 112:41–9. | Explains scheduling buffer pattern | [V] |

---

## HCMS-only references (operations research audience)

| # | Reference | Role | Verified? |
|---|---|---|---|
| 10 | Korzhenevich G, Zander A. (2024). German OR benchmarking dataset. *Health Care Manag Sci* 27:328–51. | Closest precedent, published in the target journal | [V] |
| 11 | Fügener A, et al. (2017). Behavioral responses to over/underutilization. *Health Care Manag Sci* 20:115–28. | Explains shift-transition compression; published in HCMS | [V] |
| 12 | Wachtel RE, Dexter F. (2009). Block time capacity planning. *Anesth Analg* 108:1215–20. | Technical scheduling reference | [V] |
| 13 | Munnich EL, Parente ST. (2014). ASCs complete procedures 30% faster. *Health Aff* 33:764–9. | Operating-model effect from economics angle | [?] |
| 14 | Brovman EY, et al. (2019). ASC vs hospital matched cohorts. *J Clin Anesth* 57:51–7. | Confirms ASC-hospital gap | [?] |
| 15 | Baumgart A, et al. (2017). Benchmarking program didn't improve. *J Med Syst* 41:126. | Benchmarking data alone doesn't help | [V] |
| 16 | Merlo J, et al. (2006). Multilevel analysis tutorial. *J Epidemiol Community Health* 60:290–7. | Framework for our room-level variance decomposition | [V] |
| 17 | Ligthart-Melis GC, et al. (2022). Dutch hospital between-site variance. *Br J Anaesth* 129:387–95. | Precedent: within > between variation | [?] |

---

## BMJ QS-only references (quality and safety audience)

| # | Reference | Role | Verified? |
|---|---|---|---|
| 10 | Zhang C, Pandit JJ. (2023). NHS OR metrics are misleading. *Br J Anaesth* 131:130–4. | Establishes metric validity as a real problem | [V] |
| 11 | Zhang C, Dunstan C, Pandit JJ. (2024). Capped utilisation critique. *Anesthesiol Perioper Sci*. doi:10.1007/s44254-024-00073-3 | Extends to utilisation targets | [V] |
| 12 | Landrigan CP, et al. (2004). Work hours and serious medical errors. *N Engl J Med* 351:1838–48. | Connects overtime → fatigue → patient harm | [?] Needs verification |
| 13 | Nagpal K, et al. (2010). Surgical handover evaluation. *Ann Surg* 252:402–7. | Connects shift transitions → information loss | [?] Needs verification |
| 14 | Abdelfattah E, et al. (2020). Workflow disruptions and outcomes. *BMJ Qual Saf* 29:1009–17. | Published IN the target journal; OR flow disruptions | [V] |
| 15 | Joseph A, et al. (2019). Minor disruptions escalate. *BMJ Qual Saf* 28:276–83. | Published IN BMJ QS; parallels our cascading finding | [V] |
| 16 | WHO. (2007). Communication during patient hand-overs. Patient Safety Solutions vol 1, solution 3. | Institutional authority on handover risk | [?] Needs verification |
| 17 | Merlo J, et al. (2006). Multilevel analysis tutorial. *J Epidemiol Community Health* 60:290–7. | Relevant to both, but especially equity framing | [V] |

---

## What each journal's reviewers will ask — and which references answer

### HCMS reviewer questions

| Question | Answer | Key reference |
|---|---|---|
| "Is progressive stratification methodologically sound?" | Each layer removes one confounder; the spread narrows monotonically | Ernst et al. (2012) did single-layer; we extend to four |
| "How does this compare to existing benchmarking approaches?" | OE-ratio is single-layer; we show multi-layer is needed | Korzhenevich & Zander (2024), Ernst et al. (2012) |
| "Is the natural experiment design valid?" | Shared governance eliminates institutional confounders | Original contribution; no direct precedent found |
| "Why not a multilevel regression?" | Could add; simple variance partition already makes the point | Merlo et al. (2006), Ligthart-Melis et al. (2022) |

### BMJ QS reviewer questions

| Question | Answer | Key reference |
|---|---|---|
| "Why should quality/safety leaders care about this?" | Invalid metrics → wrong decisions → wasted improvement resources → patients affected | Zhang & Pandit (2023), Zhang et al. (2024) |
| "Where's the patient safety data?" | We measure exposure to overtime conditions (fatigue, handovers), not outcomes directly. Limitation acknowledged. | Landrigan et al. (2004), Nagpal et al. (2010) |
| "Has BMJ QS published anything like this before?" | Yes — workflow disruptions in ORs, flow disruption escalation | Abdelfattah et al. (2020), Joseph et al. (2019) |
| "Is FCOTS really not useful?" | Useless as between-site comparator; useful within a room-day | Pandit et al. (2012), R² = 0.04–0.08 |
| "What should quality leaders do differently?" | Stratify before comparing; report room-level; track cascading not just FCOTS | Our recommendations §4.4 |

---

## References still needing verification

Before submission, these must be checked on Google Scholar:

1. **Landrigan et al. (2004)** — "Effect of reducing interns' work hours on serious medical errors in intensive care units." *NEJM* 351:1838–48. Search: `Landrigan work hours medical errors NEJM 2004`

2. **Nagpal et al. (2010)** — Surgical handover evaluation. *Ann Surg* 252:402–7. Search: `Nagpal surgical handover information transfer Annals Surgery 2010`

3. **Munnich & Parente (2014)** — ASC procedures faster. *Health Affairs* 33:764–9. Search: `Munnich Parente ambulatory surgery center Health Affairs 2014`

4. **Brovman et al. (2019)** — ASC vs hospital. *J Clin Anesth* 57:51–7. Search: `Brovman ambulatory surgery center hospital outpatient Journal Clinical Anesthesia 2019`

5. **Ligthart-Melis et al. (2022)** — Dutch hospital variation. *Br J Anaesth* 129:387–95. Search: `Ligthart-Melis between-hospital variation perioperative British Journal Anaesthesia 2022`

6. **WHO (2007)** — Patient Safety Solutions, handovers. Search: `WHO patient safety solutions communication hand-overs 2007`
