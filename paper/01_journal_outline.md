# Journal Submission Outline

**Target journal (primary):** *Health Care Management Science* (Springer)
**Target journal (backup):** *Anesthesia & Analgesia* (OR Economics, Education & Policy section)
**Target journal (safety):** *BMC Health Services Research*

**Working title:**
*One hospital, four operating-room models: a stratified 228,623-case benchmarking of a Belgian hospital network (2022–2025)*

**Authors (proposed order):** Haroon Tharwat · Maxim Riebus · Ben [surgeon co-author] · Dieter [surgeon co-author] · Niels Martin (corresponding)

**Length target:** 9,000–11,000 words (HCMS tolerates up to ~12,000 excluding references). Expect ~6 figures and ~4 tables.

---

## 1. Core argument (one paragraph)

Under a single governance umbrella, the four operating-room (OR) sites of Ziekenhuis Oost-Limburg (ZOL) run four structurally different operating models. Their raw overtime rates differ by a factor of 16.8 between the ambulatory-only site (Lanaken, 0.5%) and the 24/7 inpatient-heavy site (Genk, 8.4%). We show that progressive stratification — for weekday, shift window, elective status, and admission type — collapses this spread by roughly an order of magnitude, leaving a residual 3–4× difference that is almost entirely attributable to operating-model design rather than managerial effort. Within-site, room-level variation is *larger* than between-site variation at two of the four campuses, meaning the biggest performance lever is inside each hospital, not between hospitals. We argue that OR benchmarking must adjust for operating-model type, and that within-site room-level heterogeneity is a larger waste reservoir than any of the standard first-case-on-time-start interventions the literature recommends.

---

## 2. Structure (IMRaD with pre-registered robustness checks)

### Abstract (~250 words)

- One-sentence hook: 16.8× raw overtime spread across four sites of a single hospital network.
- Data: 228,623 procedures, Jan 2022–May 2025, 48 operating rooms.
- Method: progressive stratification (raw → weekday → day shift → elective → admission type), shift-aware overtime definition, room-level variance decomposition, cascade-vs-overrun quantification.
- Findings: (i) spread collapses with stratification; (ii) within-site room-level variation exceeds between-site variation at 2/4 campuses; (iii) first-case punctuality does not rank sites in the same order as stratified overtime; (iv) duration-estimation precision is similar across sites; (v) start-time cascades waste ≈4× more OR time than duration overruns; (vi) cases pushed across shift boundaries finish substantially shorter than planned.
- Implication: OR benchmarking must adjust for operating-model type; room-level heterogeneity is the larger lever.

### 1. Introduction (~1,200 words)

1.1 The OR is the most resource-intensive unit of the hospital; its efficiency metrics drive investment and staffing decisions.
1.2 Benchmarking at the site level is the standard, but often ignores case-mix and operating-model differences.
1.3 The dominant efficiency doctrine (Macario 2006; Dexter & Epstein 2009) centers on first-case-on-time starts, turnover, duration prediction, and contribution margin per OR hour.
1.4 Recent large-sample benchmarking efforts (Ernst et al. 2012; Schneider et al. 2024) have improved German multi-site comparability but (a) mostly emphasize a single case-mix adjustment layer and (b) seldom decompose variance into within- vs. between-site components.
1.5 Three open questions motivate this paper:
   - When a single hospital network runs multiple operating models under shared governance, how much of the raw between-site performance spread survives progressive stratification?
   - Is within-site, room-level variation a bigger lever than between-site ranking?
   - Does the FCOTS doctrine hold up empirically when tested on a large multi-site dataset with a proper overtime definition?
1.6 Contribution. We answer these three questions with 228,623 observations from four structurally different OR environments in a single Belgian hospital network, using a shift-aware overtime definition and a progressive-stratification methodology that, to our knowledge, has not been previously applied to multi-site OR benchmarking.

### 2. Setting and data (~800 words)

2.1 The ZOL network: four sites (Genk, Maaseik, Lanaken, Cathlab), shared EHR, governance, and labor agreements.
2.2 Description of each site's operating model:
- **Genk** — tertiary, 26 ORs, mixed elective/urgent, 24/7 emergency access, 85.4% elective, 42.3% ambulatory, 96,044 cases
- **Maaseik** — secondary, 8 ORs, hybrid MK/MO block structure, 94.3% elective, 83.9% ambulatory, 53,902 cases
- **Lanaken** — ambulatory-only, 7 ORs, paired-room flex (LP01↔LP02), no weekend activity, 99.6% elective, 98.1% ambulatory, 69,395 cases
- **Cathlab** — specialized interventional cardiology, 7 core rooms, 97.5% elective, 11.3% ambulatory (note: corrects a labeling error in our internal in-depth report), 9,282 cases
2.3 Study period: January 2022 – May 2025 (41 months).
2.4 Original export: 258,517 records on 21 variables; final analytic cohort after quality filtering: 228,623 cases.
2.5 Data quality: completeness by variable, missing-value audit, 28 records with duration >24h removed, 97 zero-duration removed, 65 unrealistic-long and 260 unrealistic-short after duration-group-specific thresholds, 102 elective cases with planned duration ≤1 min, 79 negative planned durations, 53 forgotten check-outs. (Full details in supplementary Data Quality Report.)
2.6 Standardized urgency definition: ZOL data manager defined non-elective as booked within 24h of surgery; network-wide non-elective rate is 6.4%. Cathlab subset: only procedures with anesthesiologist present retained, so as to compare to regular OR cases.

### 3. Methods (~1,500 words)

#### 3.1 Derived variables
- `shift_label`: which of the three shifts (08:00–16:30, 16:30–22:00, 22:00–08:00) contains the case's `ORIn` (effective shift, not planned shift).
- `planned_shift_label`: the shift that would have contained `PlannedStartDT` (used only for the cross-shift indicator).
- `moved_to_other_shift`: 1 if planned and effective shifts differ.
- `start_diff = ORIn − PlannedStartDT`, `end_diff = OROut − PlannedEndDT`, `duration_diff = DurationMinutes − PlannedDurationMinutes`.
- `overtime_flag`: 1 if `OROut > shift_end` (shift-aware, not naive 16:30).
- `overtime_minutes = max(0, OROut − shift_end)`.
- `planned_afterhours_minutes`: minutes of planned work that already fall after `shift_end`.
- `relative_overtime_minutes = overtime_minutes / planned_afterhours_minutes`, undefined if the denominator is ≤0.
- `gap_time`: idle minutes between consecutive cases in the same room, capped at 60 (periods above 60 min represent planned downtime, not inefficiency).
- `room_swap`: 1 if `ActualOR ≠ PlannedOR`.

#### 3.2 Progressive stratification ladder

We compute the overtime rate at five levels of stratification (L0–L4):
- **L0 (raw):** all cases.
- **L1 (weekdays):** Monday–Friday only — removes the weekend emergency confound.
- **L2 (day shift):** L1 ∩ cases whose effective shift is 08:00–16:30.
- **L3 (elective):** L2 ∩ urgency==elective.
- **L4 (planned within shift):** L3 ∩ `planned_afterhours_minutes ≤ 0` — the case was *supposed* to end within shift, so any overtime is unplanned.

We further split L4 by admission type (DAG, HOS) to isolate case-mix-driven differences from operating-model-driven differences.

#### 3.3 Room-level variance decomposition

For each campus, we compute the stratified-L4 overtime rate at the operating-room level, then report the ratio of max-room to min-room overtime rates and compare to the between-campus ratio. We also compute a simple variance partition between "between-campus" and "within-campus, between-room" components.

#### 3.4 Cascade vs overrun decomposition

Total daily OR time waste (in minutes) is the sum of
- **Start-time cascade waste:** cumulative minutes lost to `start_diff > 0` across all cases in a room-day.
- **Duration-overrun waste:** cumulative minutes from `duration_diff > 0` across all cases in a room-day.

We report the ratio of these two quantities at the network level.

#### 3.5 First-case-on-time start (FCOTS) audit

For each campus, we compute the first-case punctuality profile (mean `start_diff`, median `start_diff`, %>15 min late, %>30 min late). We test whether the ranking of sites by FCOTS matches the ranking by L4 overtime using Spearman's rank correlation.

#### 3.6 Shift-transition compression

For cases with `moved_to_other_shift == 1`, we report mean `duration_diff` and compare to the matched-plan baseline. A negative `duration_diff` would indicate compression (finish shorter than planned) when cases spill across a shift.

#### 3.7 Software

All analyses in R 4.x using tidyverse, lubridate, and custom shift-aware scripts. Code and derived variable definitions are published with the paper.

### 4. Results (~3,500 words, 6 figures, 4 tables)

#### 4.1 Network-level descriptive statistics (Table 1)
Cases, ORs, surgeons, admission-type mix, urgency mix, weekday distribution, year distribution — per site and total.

#### 4.2 Progressive stratification (Figure 1, Table 2)
- Bar chart showing L0 → L4 overtime rate for each site.
- Genk 8.4% → ~4% at L4 (remaining unplanned elective overtime in day-shift cases).
- Lanaken 0.5% stays ≈0.4%.
- Maaseik 2.8% → ~1.6%.
- Cathlab 5.8% → ~3.8%.
- Spread collapses from 16.8× to ~10× at L4, then to 3–4× after admission-type split.

#### 4.3 Within-site room-level variation (Figure 2, Table 3)
- For each campus, show the distribution of L4 overtime rate across rooms.
- Headline: at Maaseik, MK13 is 0.3% and MO03 is 8.9% — a within-campus spread of ~30× — which is nearly double the 16.8× between-campus spread.
- Lanaken: LP01 0.1% to LO03 1.7% (17×).
- Cathlab: KO06–KO03 range is ~4×.
- Genk: GSE1/GEG1 ~0% to GO10 32.9%.
- Variance partitioning: within-site, between-room variance exceeds between-site variance at 2/4 sites.

#### 4.4 First-case punctuality does not explain between-site variation (Figure 3, Table 4)
- Genk first-case mean delay +56 min; Lanaken +30 min; Cathlab +49; Maaseik +31 (from PDF digests).
- Ranking by FCOTS does not match ranking by stratified overtime.
- Spearman's ρ between FCOTS rank and L4 overtime rank is not monotone across the four sites.
- Interpretation: the dominant FCOTS doctrine (Dexter & Epstein 2009; Wachtel & Dexter 2009) is not the sole lever.

#### 4.5 Duration-estimation precision is similar across sites (Figure 4)
- Plot CV of actual duration within each planned-duration bucket, stratified by site.
- 0–30 min bucket: Genk 0.61, Lanaken 0.52, Maaseik 0.59, Cathlab 0.61.
- 31–60 min bucket: Genk 0.16, Lanaken 0.39, Maaseik 0.41, Cathlab 0.43.
- 61–90 min bucket: Genk 0.36, Lanaken 0.34, Maaseik 0.30, Cathlab 0.39.
- 91–180 min bucket: Genk 0.20, Lanaken 0.32, Maaseik 0.32, Cathlab 0.35.
- >180 min bucket: Genk 0.42, Lanaken 0.69, Maaseik 0.37, Cathlab 0.59 (sparse).
- Interpretation: duration prediction is *not* the differentiator; the gap is in process discipline and operating model, not forecasting accuracy.

#### 4.6 Cascade > overrun (Figure 5)
- Aggregate waste (minutes) from start-time cascade vs from duration overruns, network-wide.
- Ratio ~4:1 in favor of cascade — start-time drift matters more than forecasting errors.

#### 4.7 Shift-transition compression (Figure 6)
- For cases with `moved_to_other_shift==1`, `duration_diff` is systematically negative.
- Cathlab mean duration_diff for moved cases: −87.6 min (note: this value should be re-verified against the source data before final submission as the effect size is large).
- Lanaken moved cases: −11.7 min.
- Maaseik moved cases: −0.2 min.
- Genk moved cases: −22 min.
- Interpretation: the very act of pushing into a later shift compresses execution, likely through case-swap, rescheduling, or staff effort. This is a behavioral-OM phenomenon that to our knowledge has not been reported in the OR literature.

### 5. Discussion (~2,000 words)

#### 5.1 Principal findings
Restate the six headline results; anchor each against the closest published result.

#### 5.2 Why raw benchmarking misleads
Tie to Schneider et al. (2024) and Ernst et al. (2012). Argue that single-layer case-mix adjustment is insufficient; operating model is the deeper covariate.

#### 5.3 Where the waste actually lives
Argue that within-site, room-level heterogeneity is the larger lever; cite Merlo et al. (2006) on variance partitioning. Connect to Ligthart-Melis et al. (2022) on between-hospital variation in Dutch cohort.

#### 5.4 FCOTS is not the whole story
Anchor against Pandit et al. (2012, *Anaesthesia*), Wachtel & Dexter (2009), Dexter & Epstein (2009). Argue that the FCOTS doctrine is not *wrong* but *incomplete*, and that the cascade structure matters more than the first-case indicator.

#### 5.5 Shift-transition compression — a new phenomenon
Frame as a behavioral-OM finding. Connect to Fügener et al. (2017) in HCMS. Hypothesize three mechanisms: case de-selection, skill upgrading at the boundary, or scheduling adjustment pressure.

#### 5.6 Implications for OR managers
Three specific recommendations:
1. Benchmark after stratifying for operating model, not just case-mix index.
2. Invest in room-level improvement before between-site improvement.
3. Measure cascade waste explicitly; treat FCOTS as one factor among several.

#### 5.7 Limitations
- Single hospital network, single country — generalizability?
- No cost data — we cannot compute contribution margin or ROI.
- No staff-level data — we cannot disentangle surgeon vs anesthesia vs nursing effects.
- The shift-transition compression finding needs replication and mechanism work.
- The Cathlab labeling error in our own in-depth report (now corrected) is a reminder that OR benchmarking is sensitive to variable labeling.

#### 5.8 Future work
Multilevel hierarchical model, staff-level covariates, multi-network replication, behavioral-OR experimental follow-up on shift-transition compression.

### 6. Conclusion (~250 words)

One hospital network, four operating models, 228,623 cases. Raw overtime rates differ 16.8-fold. Stratification collapses this to 3–4×. Within-site room-level variation is bigger than between-site variation at half the sites. FCOTS doesn't rank sites by stratified overtime. Duration prediction is not the differentiator. Start-time cascading wastes ≈4× more OR time than duration overruns. And cases pushed across shift boundaries finish systematically shorter than planned — a behavioral-OM phenomenon worth investigating in its own right. OR benchmarking needs stratification by operating model, not just case mix, and the biggest improvement opportunity lies inside each hospital.

### References

~60–80 citations, see `06_literature_review.md`.

### Supplementary materials

- **Data Quality Report** (existing, 7 pages)
- **Project Goals and Variable Definitions** (existing, 8 pages)
- **Per-site in-depth reports** (existing, ~50 pages each)
- **R analysis scripts** (`data_cleaning.R`, `data_cleaning_quality.R`)
- **Derived variable specifications** (with example computations)

---

## 3. Timeline (rough)

| Milestone | Content | Notes |
|---|---|---|
| Week 1–2 | Finalize framing with Niels & Maxim | Discuss this outline |
| Week 3–4 | Full paper draft v1 | Using the existing PDFs; no new analyses needed |
| Week 5 | Internal review (Niels, Maxim, Ben, Dieter) | Round 1 revisions |
| Week 6 | Verify all in-text numbers against PDFs | Including re-verifying the shift-transition compression effect sizes |
| Week 7 | Final draft v2 | Ready for circulation |
| Week 8 | Final spelling/formatting/cover letter | HCMS submission |

## 4. Risks and how we manage them

1. **Reviewer objection: "This is just descriptive."** Mitigation: the progressive-stratification method *is* the contribution. Emphasize methodology.
2. **Reviewer objection: "You haven't shown causation."** Mitigation: we're explicit that this is a natural experiment, not an RCT. Our claims are observational.
3. **Reviewer objection: "Without cost data, how can you rank importance?"** Mitigation: cite Dexter & Epstein (2009) cost-per-minute estimates as an external anchor; be honest that we use minutes as our currency.
4. **Reviewer objection: "Why not a multilevel regression?"** Mitigation: we present a simple variance partition and flag the multilevel model as future work. A full hierarchical Bayesian model is out of scope.
5. **Reviewer objection: "Cathlab is not comparable to conventional ORs."** Mitigation: we explicitly include Cathlab as its own operating-model type and do not force it into between-OR comparisons without caveats.
6. **Our own Cathlab labeling error.** We flag and fix it transparently in the methods section.
