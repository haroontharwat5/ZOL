# Paper outline — for Niels and Maxim

**Working title:** Where does operating-room overtime come from, and who pays for it? A 96,044-case analysis of one tertiary centre.

**Target journal:** BMJ Quality & Safety. Original Research, ~3,500 words body. STROBE. Vancouver references. Up to **5 tables/figures in the main text**; anything additional goes to the online supplement.

**Frame agreed with Maxim (24 Apr meeting):**
The umbrella project is operating-theatre efficiency at ZOL. This paper zooms into one slice — overtime — because the literature ties overtime to staff harm (fatigue, burnout, intent to leave) and patient harm (after-hours mortality, handover errors). The data from Genk are then used to ask three questions: how much, where, and through what mechanism. The paper does not directly measure outcomes; it characterises exposure and references the harm literature for consequences.

**Statistical framing rule:** describe what the data show; avoid causal language. "Our data show that…" rather than "X causes Y." If reviewers ask for tests, we add CIs and p-values for the headline numbers; we do not run a full inferential model.

---

## How to read this document

Each section below lists:
- **Word target** for that section.
- **Story** in 2–3 sentences.
- **Numbers** with the source location (page, table, figure in the In-Depth or EDA file).
- **Figure or table proposal** with a status flag: **MAIN** (one of the five visual slots), **TEXT-ONLY** (mentioned in prose), **APPENDIX** (online supplement), or **SKIP**.
- **Citations** for that section.

The five MAIN visual slots are decided at the end of this document, after every candidate is laid out, so we can compare them side by side.

---

## 1. Introduction (~600 words)

**Story.** Operating-theatre efficiency is a well-studied operational concern, but inside a single hospital the literature still treats overtime as a single aggregate number. We motivate why overtime in particular is worth a closer look: it has documented consequences for staff and for patients. We then introduce the staffing-pyramid context that makes overtime in this hospital a sharper problem than the headline number suggests, and end with the three research questions.

### 1.1 The bigger picture (≈100 words)
ZOL is running a multi-phase OR-efficiency programme. Phase 1 = retrospective characterisation of scheduled-versus-observed performance. Phase 2 = link operational patterns to patient outcomes. Phase 3 = predictive scheduling. This paper sits in Phase 1 and points to Phase 2.

Reference: hospital kickoff slides 21–22 (already in `06_hospital_original_ask.md`).

### 1.2 Why overtime specifically (≈250 words)
Overtime as the binding economic and operational cost (Dexter 2004, McIntosh 2006). Then the harm framing:

- **Staff harm.** Long shifts and overtime are associated with poorer perceived care quality and higher patient-safety risk (Griffiths 2014, *Med Care*). Mandatory overtime is associated with intent-to-leave (**Cho/Bae 2024, *Int J Public Health***). Unpredictable overtime is more harmful than planned long shifts (Dall'Ora 2016, 2020). 12-hour shift studies link overtime to burnout and intent-to-leave (Dall'Ora 2015, *BMJ Open*).
- **Patient harm.** After-hours surgery is associated with elevated mortality (Cortegiani 2020, *BJA* — adjusted OR 1.16, 95% CI 1.06–1.28; meta-analysis). Replicated recently in a 281,717-patient propensity-matched South Korean cohort (**Oh 2025, *Anaesthesia***). Each intraoperative anaesthesia handover raises the odds of major composite complication (Saager 2014, *Anesthesiology* — incidence rises from 8.8% at 0 transitions to 21.2% at ≥4). Recent UK national patient-safety investigation explicitly names staff fatigue as a patient-safety problem (**HSSIB 2025**). Direct quantification of overtime hours and patient-safety indicators across 70 US hospitals (**Pittman 2025, *JAMA Network Open***).

### 1.3 The staffing-pyramid context (≈100 words)
At Campus Genk, 25 theatres run 08:00–16:30, dropping to 8 rooms 16:30–17:30, 4 rooms 17:30–22:00, and a single overnight room (kickoff slide 11; reproduced in `06_hospital_original_ask.md` §4). A case spilling past 16:30 is competing for one of a sharply diminishing set of staffed rooms. This is what makes "going past the shift end" a meaningful exposure category in this setting, not an arbitrary clock cut-off.

### 1.4 Research questions (≈80 words)
1. How is overtime distributed across rooms and time within one tertiary centre?
2. What mechanism — late starts, individual case overruns, or mid-day cascading — accounts for most of the overtime minutes?
3. How do urgent cases interact with the elective programme to produce spillover into staffed-down hours?

**Figure proposal — Figure 1 (Staffing pyramid).** Bar/step illustration of the four staffing tiers. Reproduced from the hospital kickoff with permission. **MAIN — slot 1.** This single figure carries the entire framing of why overtime matters at this site.

---

## 2. Methods (~700 words)

**Story.** Single-site retrospective. STROBE-compliant description of setting, data source, variables, definitions, and analyses.

### 2.1 Setting (≈100 words)
Campus Genk, ZOL network, Belgium. Tertiary, >50,000 procedures/year. 18 surgical theatres + 7 interventional + ambulatory anaesthesia (endoscopy, IVF/MKA). 90+ anaesthesiologists. All surgery except congenital cardiac and transplant. Staffing pyramid as in §1.3.

Source: kickoff slides 3–4, slide 11.

### 2.2 Data and inclusion (≈150 words)
Administrative OR data, 1 January 2022 – 31 May 2025. **96,044 cases** at Genk. **71,621 unique patients**, **225 surgeons**, **211 anaesthesiologists**, **26 distinct actual ORs**, **1,327 distinct procedure names** (In-Depth Table 1, p.3).

Time-stamp reliability disclosure (kickoff slide 14): "**Room in and room out are the only reliable data available.**" All timing analyses use room-in and room-out only; induction, recovery and ward-transfer marks are recorded but not used.

**Admission mix:** 51.0 % ambulatory (DAG), 48.9 % inpatient (HOS), 0.1 % emergency-bed (SPOED) (In-Depth Table 4, p.5).

### 2.3 Variables (per Bauer 2020)
- Planned duration, observed duration, planning deviation.
- Scheduled start, actual start, start-time deviation.
- Room-out time → overtime flag and overtime minutes.
- Planned room vs actual room → room-swap flag.
- Urgency at planning (elective vs niet-electief).
- Shift label (day 08:00–16:30; evening 16:30–22:00; night 22:00–08:00).

### 2.4 Overtime definition (≈80 words)
Overtime = case still in the room past **16:30** on the calendar day, or any case ending in the evening or night shift. This is shift-based, not duration-based. We chose this definition because the staffing change at 16:30 is the operational event that gives overtime its meaning at this site (cf. §1.3). We follow Bauer 2020 §3.4 and align with how the hospital frames "area under the curve" past the day-shift staffing window (kickoff slide 18).

### 2.5 Analyses (≈200 words)
Descriptive throughout — no causal inferential modelling. Three blocks:

1. **Burden and concentration.** Case-level overtime rate, mean, median, P95. Distribution by room, weekday, year, shift.
2. **Mechanism.** Start-time deviation (per case and per room). Duration-deviation by planned-duration bucket via coefficient of variation. Shift-displacement: cases performed in a different shift than originally planned, with mean start delay and mean planning-deviation.
3. **Daily disruptors.** Urgency mix and timing. Urgent–elective overlap in the same OR (per day, per room, per month). Effect of overlap on elective start delay.

**Sensitivity / non-mechanism checks.** Room swaps (1.1 %) and idle time between cases (median 7 min) are reported as non-bottlenecks — covered in text without their own tables, per the meeting decision.

### 2.6 Ethics (≈30 words)
Institutional approval, fully de-identified administrative data, no patient interaction.

### 2.7 Software (≈30 words)
Python/R as used by the analysis pipeline. Specify versions on submission.

---

## 3. Results (~1,000 words)

The Results section follows the order Maxim highlighted in the In-Depth document: brief context on planning vs reality, then the overtime block, then the urgent-cases block, then a short stability paragraph.

### 3.1 Sample and setting overview (≈80 words)
Headline cohort numbers (already given in §2.2). One sentence on activity distribution: weekday volume even 18.7–20.9 % Mon–Fri, weekends 1.5–1.7 % (In-Depth Table 6, p.6). Year-on-year volume growth: 26,103 (2022) → 28,522 (2023) → 29,223 (2024) → 12,196 (2025 partial) (In-Depth Table 7, p.6). One sentence on urgency mix: **87.5 % elective vs 12.5 % non-elective** (Table 5, p.6). No table.

### 3.2 Planning vs reality — context (≈150 words)
This block answers Maxim's first highlighted section. Brief, not the headline finding.

**Aggregate planning accuracy.** 45.2 % of cases run longer than planned, 54.8 % shorter (In-Depth Table 8, pp.7–8). Mean overrun 21 min (median 13); mean underrun 19.7 min (median 11). The planning system is roughly unbiased on average; the dispersion is the problem.

**Coefficient of variation by planned-duration bucket** (In-Depth Table 13, p.13):
| Planned bucket | n | CV (observed) | CV (planning deviation) |
|---|---|---|---|
| <30 min | 19,511 | 0.61 | 1.25 |
| 31–60 min | 28,674 | 0.46 | 1.07 |
| 61–90 min | 19,921 | 0.36 | 1.06 |
| 91–180 min | 20,592 | 0.35 | 0.91 |
| >180 min | 7,343 | 0.42 | 1.86 |

Mid-length cases (61–180 min) are most predictable; very long cases carry the largest planning-deviation CV. Note: Dieter flagged the CV as analytically interesting, so we keep this in the body.

**Weekend vs weekday relative deviation** (In-Depth Figure 5, p.10): weekday relative deviation 2.0–4.8 %; **Saturday 23.1 %, Sunday 23.4 %.** One sentence in text.

**Procedures with the largest absolute deviation** (In-Depth Table 22, p.25 — actually Table 11 p.11 in In-Depth has duration-deviation per OR; the procedure-level table lives elsewhere): top deviators include CABG OFF PUMP, AVR, DEBULKING MET HIPEC. These are the complex cardiac and oncology procedures that we will see again in the GO10 finding. One sentence.

**Figure/table proposal — Table 2 (CV by planned-duration bucket).** Five rows, three columns. Compact. **MAIN — slot 2** *if* we want one analytical table on planning quality; otherwise demote to **APPENDIX**. Open question for Niels — see §6.

### 3.3 Overtime: how often, where, when, how heavy (≈300 words)
This is Maxim's main highlighted block (his check-mark on "Do surgeries stay within regular working hours?"). It carries the headline numbers and the room-level concentration.

**Headline (In-Depth Table 24, p.28):**
- 96,044 cases, **8,024 ran past 16:30 (8.4 %)**.
- Mean overtime 59 min; median 38 min; P95 193.8 min.

**By weekday (In-Depth Figure 16, p.29):**
- Mon–Fri 7.8–8.5 % (Mon 8.0, Tue 8.2, Wed 8.5, Thu 7.8, Fri 8.0).
- **Saturday 16.8 %, Sunday 15.5 %.** Weekend rate roughly twice the weekday rate.

**By year (In-Depth Figure 17, p.29):**
- 2022 8.8 % → 2023 8.6 % → 2024 8.2 % → 2025 (partial) 7.2 %. Slow improvement, not a step change.

**By end-time hour (In-Depth Figure 18, p.31):**
- Sharp peak immediately after 16:30 (~3,000 cases ending in 16:30–17:30).
- Rapid decay through 17:30–20:00.
- Long thin tail past 22:00.

**Room-level concentration (In-Depth Table 25, pp.30–31):** spread runs from **0 % to 32.9 %** within one OR complex.
- **GO10: 32.9 % overtime, mean 154 min, P95 327 min.** GO10 is the headline outlier. (Per Maxim's note: confirm with hospital what specialism GO10 carries — best guess from EDA Table 9, p.12: cardiac complex surgery, six procedures performed >50 times each include AORTAKLEP VIA MINI-STERNOTOMIE, COR.AORTA BYPASS GRAFT V., MITRALISKLEP PORT ACCES.)
- Tier 2: GO09 16.3 %, GO13 13.8 %, GO12 13.4 %, GO08 12.5 %, GO05 12.3 %, GO11 11.7 %, GO02 11.3 %, GO04 10.7 %.
- Near-zero rooms: GEG1 0 % (n=4,498), GSE1 0 % (n=2,261), GEX1 0.3 %.

The headline finding is that the spread inside one campus exceeds the spread between campuses (Genk 8.4 %, Cathlab 5.8 %, Maaseik 2.8 %, Lanaken 0.5 % — In-Depth Table 26, p.34, optional one-sentence cross-site context).

**Figure/table proposal — Figure 3 (Room-level overtime concentration).** Horizontal bar chart of room overtime rate, ordered descending, with mean overtime min in a secondary panel. **MAIN — slot 3.** This is the strongest single visual the paper has.

**Figure/table proposal — Table 3 (Overtime headline).** Headline numbers (8.4 %, mean, median, P95) plus weekday and year breakdowns. **MAIN — slot 4.** Or merge with Figure 3 panel — see §6.

### 3.4 Cascading / shift displacement (≈150 words)
This is the mechanism finding from In-Depth §6 ("How stable is the surgical schedule?", pp.40–41). Maxim highlighted "How often are surgeries moved to another shift?"

From In-Depth Table 39, p.47:

| Metric | Value |
|---|---|
| Cases performed in a different shift than planned | 4,786 |
| Share of total | 5 % |
| Mean start delay | **352.2 min (≈5 h 52 min)** |
| Mean duration difference vs plan | **−22 min (shorter than planned)** |
| Mean overtime for these cases | 9.2 min |

Interpretation in one sentence: the displaced cases do not run long. They finish on time or early. They land in a later shift because upstream cases pushed them there. This reframes the intervention target away from individual case overrun and toward mid-day flow.

Monthly trend (Figure 30, p.48): 7–8 % in early 2022 → 4–5 % through 2023–2024. Modest improvement, parallel to overall overtime trend.

**Figure/table proposal — Figure 4 (Shift displacement summary).** Either (a) a single bar showing the four key numbers (5 %, 352 min, −22 min, 9.2 min) with annotation, or (b) Figure 30 (monthly trend) reproduced. **MAIN — slot 5** *if* this is the visual we want for the cascading mechanism. Alternative: keep this as a text-only paragraph and use slot 5 for §3.5 below. Open question for §6.

### 3.5 Urgent vs elective overtime (≈200 words)
This is the second-most-cited block in Maxim's notes (his highlight on "Do urgent cases drive overtime?", In-Depth pp.34–37). It also captures the volume-versus-intensity argument Maxim flagged.

**Urgency volume (In-Depth Table 33, p.41):** 84,028 elective, 12,016 non-elective (12.5 %).

**Per-case overtime by urgency (In-Depth Table 35, p.43):**
| Urgency | n | After-hours rate | Mean OT (min) | P95 OT (min) |
|---|---|---|---|---|
| Elective | 84,028 | **7 %** | 4.1 | 18 |
| Non-elective | 12,016 | **18 %** | 10.5 | 67.2 |

So the per-case picture: urgent cases run after-hours at more than twice the rate, with longer overruns. **But because elective cases are 7× more numerous, the absolute pool of after-hours minutes is dominated by elective cases.** This is the framing Maxim wants — both per-case and total.

**Daily overlap (In-Depth Table 37, p.44):** urgent and elective in the same OR on **869 of 1,247 observation days = 69.7 %.** Daily, not exceptional.

**Effect on elective start (In-Depth Figure 29, p.45):** elective cases affected by an urgent overlap start **~30 min later** on average (~60 min in early 2022). Persistent across 2022–2025.

**Per-room overlap burden (In-Depth Table 38, p.46):** GO11 carries the highest absolute number — 485 overlap events affecting 15.5 % of its elective cases. GO11 absorbs the urgent-intake pressure (consistent with the kickoff description of GO11 as the 24/7 emergency room).

**Caveat to flag with the hospital:** Maxim noted Dieter said urgent cases may not be planned in advance. We should confirm how the urgency flag is captured. Working assumption: priority field set at booking (kickoff slide 16).

**Figure/table proposal — Table 4 (Urgent vs elective overtime + overlap).** Combines Tables 33, 35, 37, 38 into one compact summary. **MAIN — candidate for slot 5.**

### 3.6 Stability and turnover — text-only (≈100 words)
This block answers two of Maxim's smaller highlights without using a figure slot.

**Room swaps (In-Depth pp.27–32 / EDA pp.18–19).** **1.1 %** of cases performed in a room different from the planned room. Overtime rate 9.5 % among swapped vs 8.3 % among non-swapped. **Conclusion: room swaps are not a major overtime driver.** One sentence in text. **APPENDIX** for the per-room swap table.

**Idle time (In-Depth Table 40, p.48).** Mean 9.2 min between consecutive cases, median 7 min, P95 25 min. Turnover is fast and consistent. **Idle time between cases is not the bottleneck.** One sentence in text. **APPENDIX** for the per-room idle-time figure (Figure 32, p.49).

### 3.7 Start-time delays — text-only (≈80 words)
Maxim highlighted "How large are start-time delays, and when do they happen?" but during the meeting we agreed start delays are interesting only as the link to Pandit 2012's argument that first-case start does not predict end-time performance.

From EDA Table 11, p.13: elective cases start on average 25.1 min late (median 9); non-elective 125.7 min late (median 27). **GEG1: 90 % of cases start late, 0 % overtime. GO10: mid-pack on start punctuality, 32.9 % overtime.** One paragraph with this contrast. **APPENDIX** for the per-room late-start table.

---

## 4. Discussion (~1,000 words)

**Story.** Three findings, each with a literature anchor and an implication. Then the double-ended harm framing: staff first, patient second, bridged by the staffing-pyramid argument. End with limitations and a forward look to Phase 2.

### 4.1 Finding 1 — Concentration, not prevalence (≈250 words)

The headline overtime rate of 8.4 % is unremarkable on its own. The finding is that nearly all of it sits in a handful of rooms. GO10 runs overtime in one of every three cases, with a mean overrun of 154 minutes. Three rooms at the other end of the same corridor have zero overtime. The within-campus spread (0–32.9 %) exceeds the between-campus spread across the entire ZOL network (0.5–8.4 %).

**Why this matters operationally.** Hospital-wide targets (e.g., "reduce overtime by 10 %") will miss the problem unless they are decomposed by room. The overtime is already concentrated; the intervention should be too. This aligns with Zhang, Dunstan & Pandit (2024), who argue that aggregate utilisation metrics hide room-level operational reality.

**Contrast with FCOTS literature.** The conventional view holds that first-case-on-time starts drive end-of-day performance (Dexter & Epstein 2009). Our data contradict this: GEG1 has the worst first-case punctuality (90 % late) and zero overtime; GO10 is mid-pack on punctuality and worst on overtime. Pandit et al. (2012) showed the same disconnect (R² = 0.04–0.08 between start and finish times). The implication is that FCOTS is a useful discipline metric but not a reliable lever for overtime reduction.

**Citations for §4.1:**
- Zhang, Dunstan & Pandit 2024 (capped utilisation tutorial)
- Dexter & Epstein 2009 (FCOTS cost claim — the reference we challenge)
- Pandit et al. 2012 (start time ≠ finish time)
- Macario 2006 (historical OR scorecard context, brief)

### 4.2 Finding 2 — Cascading as the dominant mechanism (≈250 words)

The 4,786 shift-displaced cases finish on time or early (mean duration deviation −22 min), yet they land in the evening shift because of a mean start delay of 352 minutes. This is not an individual-case-overrun problem. It is mid-day delay accumulation pushing cases across the shift boundary.

**Literature parallel.** Wachtel & Dexter (2009) described the same phenomenon — first-case tardiness propagating through the day — in a theoretical OR model. Fügener et al. (2017) added a behavioural dimension: surgeons compress their work when they sense they are approaching a boundary. Our −22 min duration deviation is consistent with that compression effect.

**What this reframes.** If the mechanism is cascading rather than individual long-running cases, the intervention point is earlier in the day: scheduling density, buffer placement, and urgent-case routing, not end-of-list management. Joseph et al. (2019, *BMJ Qual Saf*) documented the same escalation pattern — minor flow disruptions compounding into major ones — in a different OR context.

**Citations for §4.2:**
- Wachtel & Dexter 2009 (cascading through the day)
- Fügener et al. 2017 (behavioural compression near boundaries)
- Joseph et al. 2019 (*BMJ Qual Saf* — minor-to-major disruption escalation)
- Abdelfattah et al. 2020 (*BMJ Qual Saf* — workflow disruptions and outcomes)

### 4.3 Finding 3 — Urgent–elective interaction (≈150 words)

Urgent cases run after-hours at more than twice the rate of elective cases (18 % vs 7 %). But elective cases are seven times more numerous, so the absolute pool of after-hours minutes is dominated by the elective programme. Overlap between urgent and elective in the same room occurs on 70 % of observation days, adding roughly 30 minutes to elective start times.

This is not an argument to restrict urgent access. It is an argument to protect the elective programme from predictable disruption — either through dedicated urgent rooms (GO11 already absorbs much of this) or through scheduling buffers on days with historically high urgent volume.

**Citations for §4.3:**
- Dall'Ora et al. 2016 (unplanned overtime more harmful than planned long shifts — the unpredictability framing)

### 4.4 The double-ended harm argument (≈200 words)

The paper does not measure outcomes directly. It characterises an exposure — cases and staff pushed into understaffed hours — and then draws on published evidence to argue that this exposure has documented consequences at both ends.

**Staff harm.** Overtime and long shifts are associated with burnout, reduced perceived care quality, and intent to leave (Griffiths et al. 2014; Dall'Ora et al. 2015; Cho/Bae 2024). Unpredictable overtime is worse than planned long hours (Dall'Ora et al. 2016, 2020). In a Flemish nursing workforce, workload and schedule control dominate burnout predictors (Van Bogaert et al. 2017). The HSSIB 2025 national investigation explicitly names staff fatigue as a patient-safety problem, bridging the two sides.

**Patient harm.** After-hours surgery carries elevated mortality (Cortegiani 2020 meta-analysis, adjusted OR 1.16; Oh 2025 Korean cohort, 281K matched). Each intraoperative handover raises complication risk (Saager 2014), though recent sub-specialty data are mixed (Guerra-Londono 2025 found no association in HPB surgery). Shifts exceeding 24 hours produce 36 % more serious errors (Barger et al. 2006). Overtime hours have been directly associated with patient-safety indicators across 70 US hospitals (Pittman 2025, *JAMA Network Open*).

**The bridge.** In a hospital where 25 rooms drop to 8, then 4, then 1, each case pushed past 16:30 lands in a setting with fewer staff, more handovers, and a fatigued workforce. The exposure we document is the upstream condition for both classes of harm.

**Citations for §4.4:**
- Griffiths et al. 2014, Dall'Ora et al. 2015, 2016, 2020, Van Bogaert et al. 2017 (staff harm)
- Cho/Bae 2024 (intent to leave)
- HSSIB 2025 (bridge: fatigue = patient safety issue)
- Cortegiani 2020, Oh 2025 (after-hours mortality)
- Saager 2014, Guerra-Londono 2025 (handover — positive and negative)
- Barger et al. 2006, Landrigan et al. 2004, Gates et al. 2018 (fatigue–error chain)
- Pittman 2025 (overtime hours → patient-safety indicators)

### 4.5 Limitations (≈150 words)

1. **Single-site retrospective.** Findings describe one Belgian tertiary centre. Generalisability to different staffing models is unknown.
2. **Administrative data.** Room-in and room-out only; no induction or recovery timestamps. We cannot decompose what happens inside the case.
3. **No direct outcome data.** The harm argument rests on published literature, not on patient outcomes measured in this cohort. Phase 2 of the research programme will link these operational patterns to complication and readmission data.
4. **Urgency classification.** The urgency flag is set at booking. We cannot distinguish truly emergent from semi-urgent from add-on elective.
5. **Confounding by case complexity.** GO10 likely handles the most complex cardiac surgery. Its high overtime may partly reflect irreducible procedural duration rather than schedulable inefficiency. We describe this but cannot adjust for it without procedure-level risk scores.
6. **After-hours mortality debate.** The effect size remains contested (Sakurai 2025 critique of Oh 2025). We present the evidence as "a measurable signal, not a settled question."

---

## 5. Conclusion (~200 words)

Operating-room overtime at this tertiary centre is not a diffuse, hospital-wide problem. It is concentrated in a small number of rooms, driven primarily by mid-day cascading rather than individual case overruns, and amplified by daily urgent–elective overlap. The staffing pyramid — 25 rooms dropping to 8, then 4, then 1 — means that every case pushed past the shift boundary lands in a setting with fewer staff and more handovers. Published evidence links both the staff exposure (fatigue, burnout, intent to leave) and the patient exposure (after-hours surgery, handover transitions) to measurable harm.

These findings argue for room-level rather than hospital-level overtime targets, for scheduling interventions that address mid-day flow rather than first-case punctuality alone, and for prospective outcome linkage in Phase 2 of this research programme.

**No new citations in §5.** The conclusion restates findings; it does not introduce new evidence.

---

## 6. Five figure-slot decision table

BMJ Quality & Safety allows up to **5 tables or figures in the main text**. Everything else goes to an online supplement. Below is a side-by-side comparison of all candidates identified in §§1–3, with a recommended allocation.

### All candidates

| Slot | Candidate | Type | Section | What it shows | Strength | Weakness |
|---|---|---|---|---|---|---|
| — | Figure 1: Staffing pyramid | Diagram | §1.3 | Four-tier staffing drop-off (25→8→4→1) | Carries the entire framing of why overtime matters at this site; unique to our setting; immediately legible | Not a data figure — a reviewer might prefer data in the main body |
| — | Table 2: CV by planned-duration bucket | Table | §3.2 | Five rows × three columns showing planning variability | Compact; analytically interesting (Dieter flagged it) | Supporting context, not the headline finding; could go to supplement without weakening the story |
| — | Figure 3: Room-level overtime bar chart | Bar chart | §3.3 | Overtime rate per room, ordered descending, with mean OT minutes | The single strongest visual — shows the 0–32.9 % spread in one glance | Needs annotation to explain GO10's specialism |
| — | Table 3: Overtime headline numbers | Table | §3.3 | 8.4 %, mean, median, P95, weekday breakdown, year trend | Compact summary of the overtime burden | Could merge into Figure 3 as a panel or caption table |
| — | Figure 4: Shift displacement summary | Annotated bar or infographic | §3.4 | The four cascading numbers: 5 %, 352 min delay, −22 min duration, 9.2 min OT | Captures the mechanism finding in one visual | Not a conventional chart — needs design work |
| — | Table 4: Urgent vs elective + overlap | Table | §3.5 | Per-case overtime by urgency, overlap frequency, start-delay effect | Carries the urgent–elective interaction story | Dense; might need splitting |
| — | Figure 30 (monthly shift-displacement trend) | Line chart | §3.4 | Monthly % of cases displaced, 2022–2025 | Shows improvement over time | Less impactful than the four-number summary |
| — | Figure 18 (end-time distribution) | Histogram | §3.3 | When overtime cases actually end (peak at 16:30–17:30, long tail) | Vivid picture of the overtime shape | Descriptive, not analytical |
| — | Per-room late-start table | Table | §3.7 | GEG1 90 % late / 0 % OT vs GO10 mid-pack / 32.9 % OT | Kills the FCOTS narrative | The contrast can be stated in one sentence of text |

### Recommended allocation

| Main slot | Assigned to | Rationale |
|---|---|---|
| **Slot 1** | **Figure 1 — Staffing pyramid** | Non-negotiable framing figure. Without it, the reader cannot understand why 16:30 is the threshold that matters. No other paper has published this pyramid for a Belgian OR. |
| **Slot 2** | **Figure 3 — Room-level overtime bar chart** | The headline finding. The 0–32.9 % spread is more powerful as a visual than as a sentence. Merge the headline numbers (8.4 %, mean, median, P95) into a caption table below the chart, eliminating the need for a separate Table 3. |
| **Slot 3** | **Table 3 — Overtime headline numbers (weekday + year)** | If the merge with Figure 3 works, this slot is freed. If not, keep it here as a standalone table with weekday and year breakdown rows. |
| **Slot 4** | **Figure 4 — Shift displacement summary** | The mechanism finding. Design as an annotated diagram: one bar showing 4,786 cases, four callout numbers. This is the finding that reframes the intervention target from individual overruns to mid-day flow. |
| **Slot 5** | **Table 4 — Urgent vs elective overtime + overlap** | The daily-disruptor finding. Combine urgency rates (7 % vs 18 %), overlap frequency (69.7 % of days), and start-delay effect (~30 min) into one table. |

### What goes to the online supplement

| Item | Supplement label |
|---|---|
| Table 2 (CV by planned-duration bucket) | Supplementary Table S1 |
| Per-room late-start table (§3.7) | Supplementary Table S2 |
| Room-swap table (§3.6) | Supplementary Table S3 |
| Idle-time per-room figure (§3.6) | Supplementary Figure S1 |
| Figure 30 (monthly shift-displacement trend) | Supplementary Figure S2 |
| Figure 18 (end-time distribution histogram) | Supplementary Figure S3 |
| Per-room overlap burden table (Table 38) | Supplementary Table S4 |

### Open questions for Niels

1. **Slot 3 freed?** If the headline numbers merge cleanly into Figure 3's caption, we have a spare slot. Options: (a) promote the CV table (Table 2) back into the main body; (b) promote the end-time histogram (Figure 18); (c) leave the slot unused and keep the paper tighter.
2. **Figure 4 format.** An annotated infographic is unusual for BMJ QS. Alternative: present the four cascading numbers as a small table (Table 4a) and use slot 4 for something else. Niels's preference?
3. **GO10 specialism.** We need hospital confirmation before we can annotate Figure 3. If GO10 is cardiac complex, the annotation should say so; if not, we describe it generically.

---

## 7. Complete reference mapping

Every reference the paper will cite, organised by the section where it first appears. References that recur in later sections are marked (→ also §X). Vancouver numbered superscript style per BMJ QS format.

### Introduction (§1)

| # | Reference | Role in §1 |
|---|---|---|
| 1 | Dexter F, Abouleish AE, Epstein RH, et al. (2004). *Anesth Analg* 97(4):1119–26. | Overtime as the binding OR cost (1.5–2× idle-time cost). |
| 2 | McIntosh C, Dexter F, Epstein RH. (2006). *Anesth Analg* 103(6):1499–516. | Overtime as primary operational KPI. |
| 3 | Griffiths P, Dall'Ora C, Simon M, et al. (2014). *Med Care* 52(11):975–81. | European nurse workforce: overtime → poorer perceived care quality. |
| 4 | Dall'Ora C, Griffiths P, et al. (2015). *BMJ Open* 5(9):e008331. | 12-h shifts → burnout and intent to leave (companion to Griffiths 2014). |
| 5 | Cho (Bae) J, et al. (2024). *Int J Public Health* 69:1607068. | Mandatory overtime → intent to leave. |
| 6 | Cortegiani A, et al. (2020). *Br J Anaesth* 124(5):623–37. | After-hours surgery mortality meta-analysis (adj OR 1.16). |
| 7 | Oh T-K, et al. (2025). *Anaesthesia*, DOI: 10.1111/anae.16559. | 281K-matched cohort replicating after-hours mortality signal. |
| 8 | Saager L, et al. (2014). *Anesthesiology* 121(4):695–706. | Intraoperative handover → complication risk. |
| 9 | HSSIB. (2025). *The impact of staff fatigue on patient safety.* UK investigation report. | Staff fatigue = patient-safety problem (bridge citation). |
| 10 | Pittman P, et al. (2025). *JAMA Netw Open*. PMID: 40172888. | Overtime hours → patient-safety indicators (70 US hospitals). |

### Methods (§2)

| # | Reference | Role in §2 |
|---|---|---|
| 11 | Bauer M, et al. (2020). *Anaesthesist* 69(Suppl 1):S5–17. | Definitions of overtime minutes, turnover, start-time deviation. |
| 12 | Schouten AEM, et al. (2023). *J Med Syst* 47:19. | OR metric inconsistency — justifies anchoring on Bauer 2020. |
| 13 | Zhang J, Dunstan M, Pandit JJ. (2024). *Anesthesiol Perioper Sci*, DOI: 10.1007/s44254-024-00073-3. | Capped utilisation hides overtime — justifies room-level metric. |
| 14 | Strum DP, May JH, Vargas LG. (2000). *Anesthesiology* 92(4):1160–7. | Lognormal duration distributions — statistical foundation. |
| 15 | Eijkemans MJ, et al. (2010). *Anesthesiology* 112(1):41–9. | Surgeon estimate dominates duration prediction. |

### Results (§3) — no new references

Results is descriptive. All numbers come from the In-Depth and EDA analyses. No references are cited in the Results section.

### Discussion (§4)

| # | Reference | Role in §4 |
|---|---|---|
| 13 | Zhang, Dunstan & Pandit 2024 (→ also §2) | Aggregate metrics hide room-level reality. |
| 16 | Dexter F, Epstein RH. (2009). *Anesth Analg* 108(4):1262–7. | FCOTS cost claim ($3–4/min) — the reference we challenge. |
| 17 | Pandit JJ, et al. (2012). *Anaesthesia* 67(8):823–32. | R² = 0.04–0.08 between start and finish times. |
| 18 | Macario A. (2006). *Anesthesiology* 105(2):237–40. | Historical OR scorecard context (brief). |
| 19 | Wachtel RE, Dexter F. (2009). *Anesth Analg* 108(4):1215–20. | Cascading through the day — theoretical parallel. |
| 20 | Fügener A, et al. (2017). *Health Care Manag Sci* 20(1):115–28. | Behavioural compression near block boundaries. |
| 21 | Joseph A, et al. (2019). *BMJ Qual Saf* 28(4):276–83. | Minor disruptions escalate to major (BMJ QS precedent). |
| 22 | Abdelfattah E, et al. (2020). *BMJ Qual Saf* 29:1009–17. | Workflow disruptions → outcomes (BMJ QS precedent). |
| 23 | Dall'Ora C, et al. (2016). *Int J Nurs Stud* 57:12–27. | Unplanned overtime more harmful than planned long shifts. |
| 24 | Dall'Ora C, et al. (2020). *Hum Resour Health* 18:41. | Unpredictable workload as burnout driver. |
| 25 | Van Bogaert P, et al. (2017). *BMC Nurs* 16:5. | Flemish nurse burnout: workload and schedule control. |
| 3 | Griffiths et al. 2014 (→ also §1) | Staff-harm evidence. |
| 4 | Dall'Ora et al. 2015 (→ also §1) | Burnout and intent to leave. |
| 5 | Cho/Bae 2024 (→ also §1) | Mandatory overtime → intent to leave. |
| 9 | HSSIB 2025 (→ also §1) | Bridge: fatigue = patient safety. |
| 6 | Cortegiani 2020 (→ also §1) | After-hours mortality. |
| 7 | Oh 2025 (→ also §1) | Recent large cohort replication. |
| 26 | Sakurai T. (2025). *Anaesthesia*, DOI: 10.1111/anae.16591. | Critique of Oh 2025 — balanced reading. |
| 8 | Saager 2014 (→ also §1) | Handover risk — positive finding. |
| 27 | Guerra-Londono JJ, et al. (2025). *J Surg Oncol*. PMID: 39388390. | Handover risk — negative finding in HPB (balanced reading). |
| 28 | Starmer AJ, et al. (I-PASS). (2014). *N Engl J Med* 371(19):1803–12. | Structured handover reduced adverse events by 30 %. |
| 29 | Barger LK, et al. (2006). *PLoS Med* 3(12):e487. | Shifts >24 h → 36 % more serious errors. |
| 30 | Landrigan CP, et al. (2004). *N Engl J Med* 351(18):1838–48. | Shorter shifts reduced serious errors by 36 %. |
| 31 | Gates M, et al. (2018). *BMJ Open* 8(9):e021967. | Fatigue and insufficient sleep → physician/patient outcomes (synthesis). |
| 10 | Pittman 2025 (→ also §1) | Overtime hours → patient-safety indicators. |
| 32 | MacMillan C, et al. (2025). *Surgery*. PMID: 40054053. | Turnover-time systematic review — our data show turnover is not the bottleneck. |
| 33 | Zhang C, Pandit JJ. (2023). *Br J Anaesth* 131(1):130–4. | Ties overtime metrics to quality-improvement framing. |

### References available but probably not cited

These are in our literature files but are unlikely to appear in the final paper. Kept here so we can pull them back in if a reviewer asks.

| Reference | Why it is on standby |
|---|---|
| Kelz RR, et al. (2008). *Ann Surg* 247(3):544–52. | After-hours morbidity. Replaced by the stronger Cortegiani 2020 meta-analysis + Oh 2025 cohort unless a reviewer wants individual-study depth. |
| van Zaane B, et al. (2015). *Eur J Anaesthesiol* 32(7):477–85. | European after-hours mortality. Same logic — Cortegiani pools it. Keep in reserve for a "European data" argument. |
| Turrentine FE, et al. (2010). *J Trauma* 69(2):313–19. | Non-emergent after-hours complications. Cortegiani pools it. |
| Rothschild JM, et al. (2009). *JAMA* 302(14):1565–72. | Next-day performance after nighttime surgery — overall null, subgroup positive. Cite only if a reviewer asks about next-day effects. |
| Stimpfel AW, et al. (2012). *Health Aff* 31(11):2501–9. | Shift length and burnout dose-response. Replaced by Dall'Ora 2015/2016 which are closer to our setting. |
| Shanafelt TD, et al. (2019). *Mayo Clin Proc* 94(9):1681–94. | Physician burnout longitudinal. Too broad for our focused argument. |
| Dimou FM, et al. (2016). *J Am Coll Surg* 222(6):1230–9. | Surgeon burnout systematic review. Same — too broad. |
| Sinsky CA, et al. (2021). *Mayo Clin Proc Innov Qual Outcomes* 5(6):1165–73. | COVID-era intention to leave. Topical but tangential. |
| Caruso CC. (2014). *Rehabil Nurs* 39(1):16–25. | NIOSH fatigue synthesis. Covered by Gates 2018. |
| Scott SD, et al. (2009). *Qual Saf Health Care* 18(5):325–30. | Second-victim framework. Only relevant if we discuss adverse-event aftermath — not in scope for this paper. |
| Segall N, et al. (2012). *Anesth Analg* 115(1):102–15. | Postoperative handover failure rates. Covered by Saager 2014 + Starmer 2014. |
| Nagpal K, et al. (2010). *Ann Surg* 252(1):171–76. | Handover information loss. Same — covered by the above. |
| Wahr JA, et al. (2013). *Circulation* 128(10):1139–69. | AHA statement on cardiac OR safety. Could add weight but the paper is already long on citations. |
| Korzhenevich A, Zander B. (2024). *HCMS* 27(3). | Cross-campus benchmarking — story dropped. |

---

## 8. Total reference count

**Expected: 28–33 references in the final Vancouver list.** Of these:
- 15 from the existing literature (operational core, §2 existing sources)
- 9 from the new patient-harm / staff-harm literature (§3 new literature)
- 9 recent (2023–2025) citations verified in this session (§7 recent citations)

Some references overlap across these files. After de-duplication the unique count should land at **28–33**, well within BMJ QS norms for an Original Research paper.

---

## 9. Next steps

1. **Confirm GO10 specialism with Ben/Dieter.** Needed for Figure 3 annotation.
2. **Share this outline with Niels and Maxim** for feedback on figure-slot allocation and Discussion emphasis.
3. **Niels decision on slot 3.** If headline numbers merge into Figure 3, what fills the freed slot?
4. **Draft the full manuscript** once the outline is approved.
5. **Phase 2 scoping.** Begin linking overtime exposure to complication/readmission data — referenced in §4.5 limitation 3.

