# Candidate figures and tables for each paper section

**Purpose.** For every section of the outline (`08_outline_for_niels_maxim.md`), this document proposes multiple candidate visuals from the Genk PDFs (`Exporative_Data_Analysis_Genk.pdf`, EDA, 22 pp.; `In-Depth_Analysis_Genk.pdf`, ID, 51 pp.). Each candidate has a brief description, source page, what it would carry in the paper, strengths, weaknesses, and a Haroon recommendation. The goal is for Niels and Maxim to pick the five MAIN slots together.

**Constraint.** BMJ Quality & Safety allows up to **5 tables/figures in the main text**; everything else goes to the online supplement.

**Convention.** EDA = Explorative Data Analysis. ID = In-Depth Analysis. References cited in this document have been verified in `02_existing_overtime_sources.md`, `03_new_literature.md`, and `07_recent_citations_verified.md`.

---

## §1 Introduction

### Candidate 1A — Staffing pyramid (kickoff slide 11) [RECOMMENDED]

**What it shows.** Step diagram: 25 rooms 08:00–16:30 → 8 rooms 16:30–17:30 → 4 rooms 17:30–22:00 → 1 overnight room. Reproduced from hospital kickoff with permission.

**Source.** Not in the EDA/ID PDFs. From `paper/bmjqs_v2_overtime/06_hospital_original_ask.md` §4 / kickoff slide 11.

**Role in the paper.** Carries the entire framing of why "16:30" is the meaningful threshold at this site. Without this figure the reader cannot understand why a case ending at 17:00 is in a fundamentally different operational context than a case ending at 15:30.

**Strengths.** Unique to our hospital. Immediately legible. No comparable figure in the published OR-efficiency literature for a Belgian site.

**Weaknesses.** Not a data figure — a reviewer might prefer data in the main body. Mitigation: pair it with Figure 3 (room-level overtime) so the reader gets both framing and data on facing pages.

**Citations to anchor it.** Bauer et al. (2020) for the shift-end definition; Zhang/Dunstan/Pandit (2024) for why aggregate utilisation hides what staffing-tier figures reveal.

**Recommendation: MAIN slot 1.**

### Candidate 1B — Start-hour distribution (EDA Figure 1, p.4)

**What it shows.** Number of surgeries by start hour. Sharp peak at 08:00 (~13,000 cases), gradual decline through afternoon, very low after 16:00.

**Role.** Could anchor the introduction by showing visually that the OR programme is a daytime operation. Sets up the "after-hours" framing.

**Strengths.** Data figure with a clear pattern.

**Weaknesses.** Doesn't carry the staffing-pyramid argument by itself. The reader sees activity declining but doesn't see the staffing cliff that gives the decline its meaning.

**Recommendation: SKIP — the staffing pyramid does the same job better.**

---

## §3.1 Sample and setting overview

No figure proposed. Headline cohort numbers (96,044 cases, 71,621 patients, 225 surgeons, 211 anaesthesiologists, 26 actual ORs, 1,327 procedure names) belong in prose plus a STROBE flow diagram if a reviewer asks for one.

If reviewers insist on a setting figure, the EDA Figure 2 (top 20 procedures, p.5) demonstrates the long-tail of procedure variety. **Default: APPENDIX.**

---

## §3.2 Planning vs reality (context block)

This is Maxim's first highlighted section — brief context, not the headline finding. Multiple candidates because Dieter flagged the CV analysis as analytically interesting.

### Candidate 2A — Planned vs Observed scatter (ID Figure 2, p.7)

**What it shows.** Scatter of every case: planned duration (y) vs observed duration (x), with the 1:1 diagonal in red. Heavy density along the diagonal, with substantial dispersion that widens for longer cases.

**Role.** Single-glance picture of planning accuracy across the entire 96,044-case cohort.

**Strengths.** Conventional, immediately legible. Shows two things at once — central tendency (the line) and variance growing with case length (the cone shape). Directly parallels the lognormal duration discussion in Strum, May & Vargas (2000).

**Weaknesses.** Doesn't pull apart short-versus-long cases the way the CV table does. With 96K dots it can look like a blob.

**Citations.** Strum DP, May JH, Vargas LG (2000). *Anesthesiology* 92(4):1160–7 — lognormal distribution foundation. Eijkemans MJ, et al. (2010). *Anesthesiology* 112(1):41–9 — surgeon-estimate dominance.

**Recommendation: APPENDIX. Strong as supplementary, not strong enough for a main slot.**

### Candidate 2B — CV by planned-duration bucket (ID Table 13, p.13) [RECOMMENDED if we want one analytical table]

**What it shows.** Five rows (<30, 31–60, 61–90, 91–180, >180 min) with n, CV of observed duration, and CV of planning deviation.

**Role.** Compact analytical statement: mid-length cases (61–180 min) are most predictable; very long cases (>180 min) carry the largest planning-deviation CV (1.86). Justifies why complex cardiac procedures concentrated in GO10 are a planning-noise problem, not just a duration-length problem.

**Strengths.** Compact (5 × 5). Quantitative. Dieter has already flagged this as the analytical anchor.

**Weaknesses.** A table, not a figure — visually less arresting than a chart.

**Citations.** Strum 2000 (lognormal); Eijkemans 2010.

**Recommendation: MAIN slot 2 *if* we want planning quality represented in the main body. Otherwise APPENDIX.**

### Candidate 2C — Relative deviation by weekday (ID Figure 5, p.10)

**What it shows.** Bar chart, weekday relative deviation 2.0–4.8 % Mon–Fri, then jumps to **23.1 % Saturday and 23.4 % Sunday.**

**Role.** Striking visual of weekend planning unreliability. Complements the weekend-overtime figure later (after-hours rate is 16.8 % Sat, 15.5 % Sun, double the weekday rate).

**Strengths.** Strong visual contrast. Carries the "weekends are emergency-driven" point in one image.

**Weaknesses.** Not the headline of the paper. Could clutter the planning section.

**Recommendation: APPENDIX. Mention in prose alongside the weekend-overtime numbers in §3.3.**

### Candidate 2D — SD vs mean operative time scatter (ID Figure 9, p.20)

**What it shows.** Each dot = a procedure type. SD of operative time grows linearly with mean operative time.

**Role.** Confirms the scaling property: longer procedures have proportionally similar variability, so the absolute spread grows with mean duration. Sets up why mid-length procedures are "best planned" in absolute minutes.

**Strengths.** Methodologically clean visual.

**Weaknesses.** Audience likely doesn't need this depth. More appropriate for the methods supplement.

**Recommendation: APPENDIX.**

### Candidate 2E — CV vs mean operative time scatter (ID Figure 10, p.20)

**What it shows.** CV decreases as mean duration increases. Inverse pattern to 2D.

**Role.** Same conceptual content as 2D from a different angle.

**Recommendation: APPENDIX (pick 2D or 2E if a methodological reviewer asks).**

### Candidate 2F — Monthly CV by duration group (ID Figure 7, p.14)

**What it shows.** Monthly CV time series for each planned-duration bucket. Short (<30 min) shows highest CV; mid-range (61–180 min) lowest; long (>180 min) intermediate but volatile.

**Role.** Confirms the bucket-CV finding holds over time, not just on average.

**Recommendation: APPENDIX.**

---

## §3.3 Overtime: how often, where, when, how heavy

Maxim's main highlighted block. Carries the headline numbers and the room-level concentration. Multiple strong candidates here.

### Candidate 3A — Room-level overtime bar chart (built from ID Table 25, pp.30–31) [STRONGLY RECOMMENDED]

**What it shows.** Horizontal bar chart, one bar per OR, ordered descending by overtime rate. GO10 at the top (32.9 %), then GO09 (16.3 %), GO13 (13.8 %), GO12 (13.4 %), GO08 (12.5 %), descending to GEG1 (0 %), GSE1 (0 %). A second-axis or paired-panel showing mean overtime minutes.

**Source.** ID Table 25 (pp.30–31) — needs to be plotted; the table itself does not yet exist as a figure in the PDF.

**Role.** The single most powerful visual the paper has. Shows the 0–32.9 % spread inside one corridor in one glance.

**Strengths.** Headline finding. Immediately answers "where does the overtime live?" with a name. Reframes the entire paper from "8.4 % overtime rate" (boring) to "GO10 runs overtime 1 in 3 cases" (compelling).

**Weaknesses.** Needs an annotation explaining what GO10 specialism is — pending hospital confirmation.

**Citations.** Pandit JJ, et al. (2012). *Anaesthesia* 67(8):823–32 — start time poorly predicts end time, so room-level concentration is the right unit. Zhang/Dunstan/Pandit (2024) — aggregate utilisation hides room-level reality.

**Recommendation: MAIN slot 3.**

### Candidate 3B — After-hours rate by weekday (ID Figure 16, p.29)

**What it shows.** Bar chart, Mon–Fri 7.8–8.5 %, Saturday 16.8 %, Sunday 15.5 %.

**Role.** Weekend rate is twice weekday rate. Sets up the "weekends are emergency-driven" point.

**Strengths.** Clear and clean.

**Weaknesses.** Already published in the ID PDF. Adds weekend context but not the headline finding.

**Citations.** Cortegiani A, et al. (2020). *Br J Anaesth* 124(5):623–37 — after-hours surgery and mortality, the framing this figure supports. Oh T-K, et al. (2025). *Anaesthesia* — recent Korean cohort.

**Recommendation: APPENDIX. Cite weekend numbers in prose alongside §3.3.**

### Candidate 3C — Year trend (ID Figure 17, p.30)

**What it shows.** Line plot 8.8 % (2022) → 7.2 % (2025 partial). Slow downward trend.

**Role.** Shows modest improvement over the study period.

**Strengths.** Useful framing for "the problem is not getting worse, but it is not solved either."

**Weaknesses.** Modest visual. Slope is gentle.

**Recommendation: APPENDIX. One sentence in prose.**

### Candidate 3D — End-time distribution histogram (ID Figure 18, p.32) [STRONG ALTERNATIVE]

**What it shows.** When overtime cases end. Sharp peak at 16:30–17:30 (~3,000 cases), rapid decline through 17:30–20:00, long thin tail past 22:00.

**Role.** Vivid picture of the overtime "shape." Directly visualises the staffing-tier crisis: most overtime cases land in the 16:30–17:30 window when staffing has just dropped from 25 rooms to 8.

**Strengths.** Pairs naturally with Figure 1 (staffing pyramid) — the histogram shows where in time the cases land that the pyramid says are now competing for fewer rooms.

**Weaknesses.** Descriptive, not analytical.

**Citations.** Cortegiani 2020, Oh 2025 (after-hours mortality). Saager L, et al. (2014). *Anesthesiology* 121(4):695–706 — handover risk in late-running cases.

**Recommendation: MAIN slot candidate. Strong second-choice for slot 3 if Niels prefers it over the room-level bar chart, OR pair them as Figure 3a and 3b.**

### Candidate 3E — Mean and median overtime by weekday (ID Figure 19, p.32)

**What it shows.** Stacked-bar chart, mean and median overtime in minutes per weekday.

**Role.** Shows that conditional on running overtime, weekend cases are not dramatically longer than weekday cases. Useful for the urgency argument.

**Recommendation: APPENDIX.**

### Candidate 3F — Year trend mean and median (ID Figure 20, p.33)

**What it shows.** Mean and median OT minutes per year. Mean ~57–60 min, median ~36–39 min, stable.

**Role.** Confirms that improvement is in *frequency* not *duration*.

**Recommendation: APPENDIX.**

### Candidate 3G — Violin plot of overtime by shift type (ID Figure 21, p.34)

**What it shows.** Three violin plots. Day shift = widest spread. Evening = narrower. Night = concentrated near zero.

**Role.** Shows that overtime distribution is shaped by shift volume rather than by shift fatigue per se.

**Strengths.** Conceptually clean.

**Weaknesses.** The cross-campus comparison (also referenced on p.34) was dropped in the pivot. The violin uses the Genk-only data, so it stays usable, but the message is subtler.

**Recommendation: APPENDIX.**

### Candidate 3H — Headline overtime numbers table (ID Table 24, p.28 + Tables 6–7 reordered)

**What it shows.** Compact table with headline cohort and overtime numbers (96,044 cases, 8,024 with OT, 8.4 %, mean 59 min, median 38 min, P95 193.8 min) plus weekday breakdown plus year breakdown.

**Role.** Replaces three figures (3B, 3C, 3E) with one compact data table.

**Strengths.** Frees figure slots. Reviewers often appreciate one well-designed table over multiple histograms.

**Weaknesses.** Less visually striking than a histogram.

**Recommendation: MAIN slot 4 — combines weekday/year breakdowns into one place. Or merge into Figure 3's caption to save the slot.**

---

## §3.4 Cascading / shift displacement

Mechanism finding. The 4,786-case shift-displacement number is the paper's mechanistic anchor.

### Candidate 4A — Shift displacement summary infographic (built from ID Table 39, p.47) [RECOMMENDED]

**What it shows.** Custom design: one large bar showing 4,786 cases (5 % of 96,044), with four annotated callout numbers: mean start delay 352 min, mean duration deviation −22 min, mean overtime 9.2 min, share 5 %.

**Source.** ID Table 39 numbers; needs a custom visual.

**Role.** The mechanism finding in one visual. Reframes the intervention target away from individual case overrun and toward mid-day flow.

**Strengths.** Communicates four key numbers in one frame. Directly shows that displaced cases finish *early* relative to plan, killing the "they ran long" hypothesis.

**Weaknesses.** Not a conventional chart — needs design work. Reviewers used to standard plots may push back.

**Citations.** Wachtel RE, Dexter F (2009). *Anesth Analg* 108(4):1215–20 — cascading propagation through the day. Fügener A, et al. (2017). *Health Care Manag Sci* 20:115–28 — behavioural compression near boundaries (explains the −22 min). Joseph A, et al. (2019). *BMJ Qual Saf* 28:276–83 — minor disruptions escalate (BMJ QS precedent).

**Recommendation: MAIN slot 5 candidate. Niels's call on the unconventional format.**

### Candidate 4B — Monthly shift-displacement trend (ID Figure 30, p.48)

**What it shows.** Monthly time series, 7–8 % in early 2022 declining to 4–5 % through 2023–2024.

**Role.** Shows modest improvement parallel to overall overtime trend.

**Strengths.** Conventional time series. Reviewer-friendly format.

**Weaknesses.** Monthly trend is the *less* interesting cut of the cascading story. The 352 / −22 / 9.2 numbers are the substance.

**Citations.** Same as 4A.

**Recommendation: APPENDIX. Use 4A in the main slot.**

### Candidate 4C — Plain table version of 4A

**What it shows.** Same four numbers as a 5-row table.

**Role.** Conservative alternative if the infographic format gets pushback.

**Recommendation: Backup option for slot 5. Default to 4A.**

---

## §3.5 Urgent vs elective overtime

Maxim's second-most-cited block. Captures the volume-versus-intensity argument.

### Candidate 5A — Urgent vs elective summary table (built from ID Tables 33, 35, 37, 38) [RECOMMENDED]

**What it shows.** Compact table combining: volume (84,028 elective vs 12,016 urgent), per-case after-hours rate (7 % vs 18 %), mean OT (4.1 vs 10.5 min), P95 OT (18 vs 67.2 min), overlap days (869/1,247 = 69.7 %), elective start-delay effect (+30 min on overlap days), GO11 burden (485 overlaps, 15.5 % of its elective load).

**Role.** Carries the "urgent cases per-case worse but elective volume dominates" finding plus the overlap context plus the GO11-as-emergency-room observation. One table replaces four figures.

**Strengths.** Compact. Directly reportable. Forces the reader to confront the volume math.

**Weaknesses.** Dense — may need splitting into two stacked sub-tables.

**Citations.** Dall'Ora C, et al. (2016). *Int J Nurs Stud* 57:12–27 — unplanned overtime is more harmful than planned long shifts (the unpredictability framing). Cho/Bae 2024 — mandatory overtime to intent-to-leave. Pittman P, et al. (2025). *JAMA Netw Open* — overtime hours and patient-safety indicators.

**Recommendation: MAIN slot 5 candidate (alternative to 4A).**

### Candidate 5B — Urgent timing density curve (ID Figure 25, p.41)

**What it shows.** Density of non-elective surgery start times. Sharp peak 13:00–15:00. Secondary evening peak ~18:00.

**Role.** Shows that urgent cases hit the OR programme at exactly the time when elective rooms are still busy — i.e., the overlap is structural, not random.

**Strengths.** Visually distinctive. Argues directly for scheduled-buffer interventions.

**Weaknesses.** Could be merged into supplementary discussion.

**Recommendation: APPENDIX. Mention the 13:00–15:00 peak in prose.**

### Candidate 5C — Hourly urgent–elective overlaps (ID Figure 28, p.45)

**What it shows.** Bar chart, hour of day vs number of overlaps. Heavy peak 13:00–15:00 (>300 overlaps each hour), much smaller outside that window.

**Role.** Same operational story as 5B but counts overlaps directly.

**Recommendation: APPENDIX. Pick 5B or 5C if reviewers want urgency timing in main body.**

### Candidate 5D — Elective start delay by overlap status over time (ID Figure 29, p.45)

**What it shows.** Two lines, monthly mean start delay for elective cases — one for "overlapped" days, one for "not overlapped." The overlapped line consistently runs 20–60 min higher; the gap was largest in early 2022 (60 min) and narrowed to ~30 min later.

**Role.** Direct quantification: urgent overlap costs the elective programme ~30 min of start-delay per affected case.

**Strengths.** Strong argument-supporting visual. Recurring pattern over 3+ years.

**Weaknesses.** Time series with two lines is busier than a single bar.

**Citations.** Wachtel & Dexter 2009 — cascading propagation. Pandit 2012 — start delays and end-time independence.

**Recommendation: MAIN slot 5 alternative. If we want urgency to occupy slot 5 visually rather than as a table, use this.**

### Candidate 5E — Urgent start hour by weekday ridge plot (ID Figure 26, p.42)

**What it shows.** Seven density curves stacked, one per weekday. Mon–Fri all peak ~13:00–15:00; Sat–Sun flatten out across the day.

**Role.** Shows that the urgent-elective collision is a weekday-elective phenomenon. Weekends are entirely urgent-driven.

**Strengths.** Visually elegant.

**Weaknesses.** Niche finding for our argument.

**Recommendation: APPENDIX.**

---

## §3.6 Stability and turnover (text-only by default)

Not headline findings; included to refute the alternative explanations (room swaps, slow turnovers).

### Candidate 6A — Idle time per OR (ID Figure 32, p.50)

**What it shows.** Horizontal bar chart, mean and median idle time between cases per OR. Max ~22 min in GO10, most rooms 5–15 min, GEG1 ~3 min.

**Role.** Refutes "turnover time is the bottleneck." Median idle time across all rooms is 7 min — fast and consistent.

**Strengths.** Direct rebuttal to a likely reviewer question.

**Weaknesses.** Eats a slot for a *non-finding*.

**Citations.** MacMillan C, et al. (2025). *Surgery* — turnover-time systematic review. Our data show turnover is not the bottleneck at Genk; this figure demonstrates that.

**Recommendation: APPENDIX. State in prose: "Median idle time between cases is 7 min; turnover is not the bottleneck (Supplementary Figure S1)."**

### Candidate 6B — Room swap by weekday (ID Figure 22, p.35)

**What it shows.** Bar chart, weekday swap rate 0.5–1.3 %, weekend Sat 4.8 %, Sun 3.5 %.

**Role.** Refutes "room swaps cause overtime." Overtime rate among swapped cases is 9.5 % vs 8.3 % unswapped — barely different.

**Recommendation: APPENDIX.**

---

## §3.7 Start-time delays (text-only by default)

The contrast between GEG1 (90 % late, 0 % overtime) and GO10 (mid-pack starts, 32.9 % overtime) carries the "FCOTS does not predict overtime" point in one paragraph, no figure needed.

### Candidate 7A — Start delay by weekday (ID Figure 13, p.23)

**What it shows.** Bar chart, mean start delay Mon 35.7 min → Fri 34.8 min, Sat 47.2 min, Sun 44.5 min.

**Role.** Mild weekday/weekend contrast in start punctuality.

**Strengths.** Clean.

**Weaknesses.** Not the angle that matters for our paper. The room-level contrast is what kills the FCOTS claim.

**Recommendation: APPENDIX.**

### Candidate 7B — Per-room start-delay table (ID Table 21, p.24)

**What it shows.** Per-OR late-start share and mean delay. GEG1 90 % late / 60.7 min mean; GO10 46.2 % late / 63 min mean / 32.9 % overtime; GO11 82.4 % late / 320.3 min mean (extreme outliers).

**Role.** Carries the FCOTS rebuttal in one table. Direct contrast: the worst-late-start room (GEG1) has zero overtime, the worst-overtime room (GO10) is mid-pack on punctuality.

**Strengths.** Hard data behind the rebuttal.

**Weaknesses.** Long table (26 rows). Not strong enough for main body.

**Citations.** Pandit JJ, et al. (2012). *Anaesthesia* 67(8):823–32 — R² = 0.04–0.08 between start and finish times. Dexter F, Epstein RH (2009). *Anesth Analg* 108(4):1262–7 — the FCOTS cost claim we rebut.

**Recommendation: APPENDIX. Carry the GEG1-vs-GO10 contrast in prose only.**

---

## §4 Discussion

No new figures. Discussion is prose only, with all evidence already shown in §3.

If a reviewer wants a "summary of mechanisms" diagram, we can add a small conceptual figure (rooms × shifts × cascading × urgency) in the supplement, but this should not occupy a main slot.

---

## §5 Conclusion

No figure.

---

## Summary table — recommended five MAIN slots vs alternatives

| Slot | First choice | Alternative | Notes |
|---|---|---|---|
| **1** | **1A — Staffing pyramid** | none | Non-negotiable framing figure. Pair with Figure 3 for impact. |
| **2** | **2B — Table: CV by planned-duration bucket** | demote to APPENDIX | Open question — keep or drop? Dieter wants it; 5-slot constraint argues against. |
| **3** | **3A — Room-level overtime bar chart** | 3D end-time histogram | The headline finding. Strongest visual the paper has. |
| **4** | **3H — Headline overtime table (combined w/ weekday + year)** | merge into Fig 3 caption | If we merge, slot 4 frees up for 4A or 5A. |
| **5** | **4A — Shift displacement infographic** | 5A urgent vs elective table OR 5D start-delay-by-overlap line plot | Open question — mechanism (cascading) or daily disruptor (urgency)? |

### Open questions for Niels and Maxim

1. **Slot 2 — keep CV table or move to appendix?** The CV-by-bucket finding is interesting (Dieter flagged it) but supporting context, not headline. With only 5 slots, demoting opens space.
2. **Slots 4 vs 5 — do we want both cascading (4A) and urgency (5A)?** They are the two mechanism findings. With only one slot left after 1, 2, 3 are taken, we choose one. My recommendation: cascading (4A) — it is more novel.
3. **Figure 3 design — bar chart only, or paired panel with end-time histogram (3D)?** A two-panel Figure 3 (a: room concentration, b: end-time histogram) gives the most powerful single page.
4. **GO10 specialism annotation — confirmed?** Pending hospital reply. EDA Table 9 (p.12) suggests cardiac complex (AORTAKLEP, COR.AORTA BYPASS, MITRALISKLEP). Need Ben/Dieter confirmation before annotation.

---

## Full inventory of available figures (for reference)

### Explorative Data Analysis (EDA), 22 pages

| Fig # | Page | Title | Used here? |
|---|---|---|---|
| 1 | 4 | Distribution of surgery start times | Mentioned (1B); not selected |
| 2 | 5 | Top 20 most frequent surgical procedures | APPENDIX option for §3.1 |
| 3 | 7 | Distribution of hospital stay duration | Out of scope |
| 4 | 7 | Length of stay by urgency | Out of scope |
| 5 | 8 | Distribution of planned surgery durations | Out of scope (use ID Fig 1 instead) |
| 6 | 10 | Number of planned surgeries per planned OR | Out of scope (volume, not overtime) |
| 7 | 11 | Number of actual surgeries per actual OR | Out of scope |
| 8 | 13 | Distribution of actual surgery durations | APPENDIX option for §3.2 |
| 9 | 14 | Start time deviations grouped per 10 min | APPENDIX for §3.7 |
| 10 | 16 | End time deviations grouped per 10 min | APPENDIX |
| 11 | 20 | Percentage deviation grouped per 10 % | APPENDIX |
| 12 | 20 | Top 20 procedures with highest relative deviation | APPENDIX |
| 13 | 21 | Average relative deviation per weekday | APPENDIX |

### In-Depth Analysis (ID), 51 pages

| Fig # | Page | Title | Used here? |
|---|---|---|---|
| 1 | 4 | Histogram of surgery duration | Out of scope |
| 2 | 7 | Planned vs Observed duration scatter | Candidate 2A, APPENDIX |
| 3 | 8 | Distribution of relative deviation | APPENDIX |
| 4 | 10 | Relative duration deviation by year | APPENDIX |
| 5 | 10 | Relative deviation by weekday | Candidate 2C, APPENDIX |
| 6 | 12 | Monthly CV planning deviation | APPENDIX |
| 7 | 14 | Monthly CV (observed) by group | APPENDIX |
| 8 | 14 | Monthly CV (planning dev) by group | APPENDIX |
| 9 | 20 | SD vs mean operative time | Candidate 2D, APPENDIX |
| 10 | 20 | CV operative duration vs mean | Candidate 2E, APPENDIX |
| 11 | 21 | CV planning deviation vs mean | APPENDIX |
| 12 | 22 | Start time deviations grouped per 10 min | APPENDIX |
| 13 | 23 | Mean start delay by weekday | Candidate 7A, APPENDIX |
| 14 | 26 | Procedure volume vs mean deviation | APPENDIX |
| 15 | 28 | Distribution of overtime duration | Could replace 3D in slot 3 alternative |
| 16 | 29 | Share of after-hours surgeries by weekday | Candidate 3B, APPENDIX |
| 17 | 30 | Evolution of after-hours activity over time | Candidate 3C, APPENDIX |
| 18 | 32 | Timing of overtime surgeries (end-time histogram) | **Candidate 3D, MAIN alternative** |
| 19 | 32 | Average and median overtime by weekday | Candidate 3E, APPENDIX |
| 20 | 33 | Average and median overtime per surgery by year | APPENDIX |
| 21 | 34 | Relative overtime per shift type (violin) | Candidate 3G, APPENDIX |
| 22 | 35 | Share of relocated surgeries by weekday | Candidate 6B, APPENDIX |
| 23 | 35 | Monthly percentage of surgeries with room swap | APPENDIX |
| 24 | 40 | Distribution of overtime duration for relocated surgeries | APPENDIX |
| 25 | 41 | Daily distribution of non-elective surgery start times | Candidate 5B, APPENDIX |
| 26 | 42 | Hourly distribution of non-elective by weekday | Candidate 5E, APPENDIX |
| 27 | 44 | Monthly share of elective surgeries affected by overlaps | APPENDIX |
| 28 | 45 | Hourly frequency of urgent–elective overlaps | Candidate 5C, APPENDIX |
| 29 | 45 | Average start delay of elective by overlap status | **Candidate 5D, MAIN alternative** |
| 30 | 48 | Monthly percentage of surgeries moved to another shift | Candidate 4B, APPENDIX |
| 31 | 49 | Distribution of idle time between surgeries | APPENDIX |
| 32 | 50 | Mean and median idle time per OR | Candidate 6A, APPENDIX |

### Tables we may use as MAIN

| Table # | Page | Title | Used here? |
|---|---|---|---|
| ID Table 13 | 13 | CV by planned-duration bucket | **Candidate 2B, MAIN slot 2 (open)** |
| ID Table 24 | 28 | Headline overtime numbers | **Candidate 3H, MAIN slot 4** |
| ID Table 25 | 30–31 | OT rate by OR | Source for **Candidate 3A bar chart, MAIN slot 3** |
| ID Table 39 | 47 | Shift displacement summary | Source for **Candidate 4A infographic, MAIN slot 5 (option A)** |
| ID Tables 33+35+37+38 | 41, 43, 44, 46 | Urgency volume + per-case OT + overlap days + per-room overlaps | Source for **Candidate 5A composite table, MAIN slot 5 (option B)** |

---

## References cited in this document

All references below are verified — see `02_existing_overtime_sources.md`, `03_new_literature.md`, and `07_recent_citations_verified.md` for full bibliographic detail and verification status.

| Section | Reference | What it supports |
|---|---|---|
| §1 | Bauer M, et al. (2020). *Anaesthesist* 69(Suppl 1):S5–17 | Shift-end definition |
| §1 | Zhang J, Dunstan M, Pandit JJ (2024). *Anesthesiol Perioper Sci* | Aggregate utilisation hides reality |
| §3.2 | Strum DP, May JH, Vargas LG (2000). *Anesthesiology* 92(4):1160–7 | Lognormal duration foundation |
| §3.2 | Eijkemans MJ, et al. (2010). *Anesthesiology* 112(1):41–9 | Surgeon-estimate dominance |
| §3.3 | Pandit JJ, et al. (2012). *Anaesthesia* 67(8):823–32 | Start time poorly predicts end time |
| §3.3 | Cortegiani A, et al. (2020). *Br J Anaesth* 124(5):623–37 | After-hours mortality (meta-analysis) |
| §3.3 | Oh T-K, et al. (2025). *Anaesthesia*, DOI: 10.1111/anae.16559 | After-hours mortality (recent cohort) |
| §3.3 | Saager L, et al. (2014). *Anesthesiology* 121(4):695–706 | Handover risk in long cases |
| §3.4 | Wachtel RE, Dexter F (2009). *Anesth Analg* 108(4):1215–20 | Cascading propagation |
| §3.4 | Fügener A, et al. (2017). *Health Care Manag Sci* 20:115–28 | Behavioural compression |
| §3.4 | Joseph A, et al. (2019). *BMJ Qual Saf* 28:276–83 | Minor disruptions escalate |
| §3.5 | Dall'Ora C, et al. (2016). *Int J Nurs Stud* 57:12–27 | Unplanned overtime more harmful |
| §3.5 | Cho (Bae) J, et al. (2024). *Int J Public Health* 69:1607068 | Overtime → intent to leave |
| §3.5 | Pittman P, et al. (2025). *JAMA Netw Open*. PMID: 40172888 | Overtime → patient-safety indicators |
| §3.6 | MacMillan C, et al. (2025). *Surgery*. PMID: 40054053 | Turnover time systematic review |
| §3.7 | Dexter F, Epstein RH (2009). *Anesth Analg* 108(4):1262–7 | FCOTS cost claim (rebutted) |

---

## Next steps

1. Niels and Maxim review this document and pick the five MAIN slots collaboratively.
2. Confirm GO10 specialism with Ben or Dieter — required for Figure 3 annotation.
3. Confirm preference on Figure 4A (infographic) versus Figure 4B (line trend) versus Figure 4C (table). Niels's call.
4. Confirm slot 5 — cascading (4A) vs urgency (5A) vs the overlap-effect line plot (5D).
5. After slot decisions, generate publication-quality versions of the chosen figures.
