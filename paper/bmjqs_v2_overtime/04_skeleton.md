# Paper Skeleton — Overtime at Genk

**Working title:** Where does operating-room overtime come from, and who pays for it? A 96,044-case analysis of one tertiary centre

**Target journal:** BMJ Quality & Safety
**Article type:** Original Research
**Reporting guideline:** STROBE
**Reference style:** Vancouver (numbered superscript)
**Target length:** 3,500–4,000 words body text

---

## Structured abstract (~250 words)

**Objective.** To characterise where operating-room overtime originates within a high-volume tertiary hospital, and to connect the operational pattern to recognised staff and patient harms.

**Design.** Retrospective observational study of administrative OR data.

**Setting.** Campus Genk of the Ziekenhuis Oost-Limburg network, Belgium — a 24/7 tertiary hospital running 25 operating rooms across general, cardiac, and endoscopy blocks.

**Participants.** 96,044 surgical and interventional procedures performed between January 2022 and May 2025.

**Main outcome measures.** Case-level overtime flag and overtime minutes (time past the 16:30 scheduled shift end), by room, weekday, shift, and urgency. Shift-transition displacement, start-time deviation, and duration-estimation accuracy as candidate mechanisms.

**Results.** 8,024 cases (8.4 %) ran past the scheduled shift end, with a mean overtime of 59 minutes and a 95th percentile of 194 minutes. Overtime concentrated in a small number of rooms: one room (GO10) ran overtime on 32.9 % of cases with a mean overrun of 154 minutes, while three rooms never ran overtime. 4,786 cases (5 %) were performed in a different shift than originally planned, with a mean start delay of 352 minutes and a mean duration shorter than planned by 22 minutes — indicating displacement rather than overrun. Urgent–elective overlap in the same OR occurred on 69.7 % of observation days and was associated with a doubling of elective start delay. First-case punctuality did not predict room-level overtime.

**Conclusions.** At a high-volume tertiary OR, overtime is concentrated, cascading, and driven by mid-day displacement rather than by late starts or individual case overruns. The cases that spill into after-hours carry the documented risks of fatigue and handover transitions for staff and patients. Room-level and cascading metrics offer a more actionable target for quality improvement than utilisation or first-case punctuality.

---

## 1. Introduction (~600 words)

### 1.1 Opening
Operating-room overtime is widely tracked as an operational indicator. Less widely examined is where it comes from inside a single hospital and what it costs the people involved.

### 1.2 Why overtime matters for quality and safety
Two lines of evidence.
- **Patient side.** After-hours surgery is associated with elevated mortality and morbidity (Cortegiani 2020, BJA; Kelz 2008, Ann Surg; van Zaane 2015, Eur J Anaesthesiol). Intraoperative handovers raise the odds of major complications (Saager 2014, Anesthesiology). Structured handover programmes reduce errors (I-PASS, NEJM 2014).
- **Staff side.** Overtime and long shifts are associated with burnout, intent-to-leave, and measurable performance decrement in OR staff (Griffiths 2014, Med Care; Stimpfel 2012, Health Aff; Barger 2006, PLOS Med; Rothschild 2009, JAMA). Unplanned overtime is more harmful than planned long shifts (Dall'Ora 2016, 2020).

### 1.3 The gap
Prior OR-overtime work treats overtime as an aggregate site-level number. Little existing literature examines how overtime is distributed within a single hospital — which rooms, which mechanisms, which cases spill into after-hours. Without that distribution, quality improvement efforts cannot target the right lever.

### 1.4 Research questions
1. How is overtime distributed across rooms and time within a single tertiary centre?
2. What mechanism — late starts, duration overruns, or mid-day cascading — accounts for most of the overtime minutes?
3. How do urgent cases interact with the elective schedule to produce spillover?

---

## 2. Methods (~700 words)

### 2.1 Setting
Campus Genk (ZOL), single tertiary hospital, 25 OR rooms covering general surgery, cardiac surgery, endoscopy, and ambulatory. Shared EHR, shared governance. Day shift 08:00–16:30.

### 2.2 Data
Administrative OR data, January 2022 – May 2025, 96,044 cases. STROBE flow diagram of inclusion.

### 2.3 Variables
Per Bauer et al. (2020) glossary: shift label, planned duration, observed duration, start-time deviation, end-time, overtime flag (end-time > shift end), overtime minutes, room swap flag, urgency classification.

### 2.4 Analyses
Descriptive:
- Overtime rate and distribution by room, weekday, year, shift.
- Start-time deviation by room and weekday.
- Duration deviation by planned-duration bucket (<30, 31–60, 61–90, 91–180, >180 min).

Mechanism:
- Shift-displacement analysis: cases performed in a different shift than originally scheduled.
- Urgent–elective overlap frequency and its effect on elective start delay.
- Decomposition of late-start effect versus cascading effect.

### 2.5 Ethics
Institutional approval, de-identified administrative data.

---

## 3. Results (~1,000 words)

### 3.1 Overall overtime burden
- 8,024 cases (8.4 %) ran past 16:30.
- Mean overtime 59 min; median 38 min; P95 194 min.
- Year trend: 8.8 % (2022) → 7.2 % (2025 partial). Slow improvement.
- Weekend rate twice the weekday rate (16.8 % Sat / 15.5 % Sun vs 7.8–8.5 % Mon–Fri).
- **Table 1.** Overtime by weekday and year.

### 3.2 Overtime concentrates in a small set of rooms
- GO10 runs overtime on 32.9 % of cases, mean 154 min, P95 327 min.
- Tier 2 (GO08, GO09, GO11, GO12, GO13): 11–16 %.
- Three rooms (GEG1, GSE1, GEX1): near-zero overtime.
- **Table 2.** Room-by-room overtime rate, mean, P95.
- **Figure 1.** Dot plot of overtime rate by room.

### 3.3 Cascading, not overruns, dominates the mechanism
- 4,786 cases (5 %) were performed in a different shift than planned.
- Mean start delay for these cases: **352 minutes**.
- Mean duration diff: **−22 minutes** (shorter than planned).
- Mean overtime for these cases: 9.2 minutes.
- **Interpretation:** the displaced cases do not run long — they arrive in a later shift because upstream cases pushed them there.
- **Figure 2.** Illustrative day showing start delays accumulating through the morning and pushing cases past 16:30.

### 3.4 Urgent–elective overlap is the primary daily disruptor
- Urgent cases = 12.5 % of volume.
- Urgent–elective overlap in the same OR occurred on **69.7 % of observation days**.
- Elective cases affected by an overlap started ~30 min later on average than elective cases without overlap; ~60 min in early 2022.
- GO11 absorbs most of the overlap burden: 485 overlap events, 15.5 % of its elective cases affected.
- **Table 3.** Overtime and start delay by urgency and overlap status.

### 3.5 First-case punctuality does not predict overtime
- GEG1 (endoscopy): 90 % late starts, 0 % overtime.
- GO10 (complex surgery): mid-pack on start punctuality, worst on overtime.
- Consistent with Pandit et al. (2012): R² = 0.04–0.08 between start and finish.
- **Figure 3.** Scatter: room-level late-start share vs overtime rate.

### 3.6 Duration estimation is not uniform
- CV of observed duration lowest for 61–180 min cases (CV 0.33–0.36).
- Higher CV for <30 min (0.61) and >180 min (0.42).
- Top 20 procedures by deviation are concentrated in complex cardiac/oncology categories — the same procedure types that sit in GO10.
- **Table 4.** CV by planned-duration bucket.

---

## 4. Discussion (~1,000 words)

### 4.1 Overtime is concentrated, not distributed
The most actionable finding. One room runs overtime six times more often than the campus average; three rooms never do. Campus-average overtime rates obscure this. Quality improvement targeted at the campus mean under-invests in the rooms that carry the weight.

### 4.2 Cascading is the dominant mechanism
The displaced cases finish slightly shorter than planned. They are not individually over-running; they are arriving in the wrong shift. This reframes the intervention target: mid-day flow, not case-by-case duration prediction.

### 4.3 Staff harm
Cascading-driven overtime is exactly the unpredictable overtime pattern that Dall'Ora (2016, 2020) links to higher burnout relative to planned long shifts. Griffiths et al. (2014) showed associations with intent-to-leave across 12 European health systems. The rooms at Genk that run late are the same rooms, week after week — the staff exposure is not random across the workforce but concentrated on specific teams. This is a workforce sustainability concern, not only a wellbeing one.

### 4.4 Patient harm
Cortegiani et al. (2020) reported elevated mortality for after-hours surgery across a meta-analysis. Saager et al. (2014) showed that each intraoperative handover raises the odds of a major complication. The mechanism linking our operational finding to patient outcomes is documented: cases that cross shift boundaries are more likely to involve a fatigued team or a handover transition, both of which are associated with worse outcomes. We do not measure complications directly — this is a limitation — but the exposure is real and documented.

### 4.5 What to do
- Room-level reporting of overtime should replace or supplement campus-average reporting.
- Mid-day flow instruments (dynamic scheduling, urgent-slot reservation) should be prioritised over first-case-start initiatives.
- Urgent-absorber rooms (GO11) deserve scheduling protection rather than sustained overload.
- The rooms that never run overtime (GEG1, GSE1) can serve as an internal benchmark rather than a peer hospital.

### 4.6 Limitations
- Single-centre design. External validity needs testing in other hospital networks.
- No patient outcome data. We measure exposure to overtime conditions, not the outcomes themselves.
- No staff outcome data (burnout score, turnover). We cite published dose-response relationships rather than measuring locally.
- No ASA acuity stratification at the case level.
- COVID-19 tail effects in 2022 and partial 2025 data.
- Overtime defined at case level; room-day frequency may differ.

---

## 5. Conclusion (~200 words)

At one tertiary hospital across more than 96,000 cases, overtime was concentrated in a small number of rooms and driven primarily by mid-day cascading rather than late starts or individual case overruns. The cases that ran past scheduled shift end carried documented exposure to both staff harms — burnout, turnover intent, fatigue — and patient harms — handover error risk, time-of-day mortality gradient. Room-level and cascading-focused metrics offer a more actionable target for quality improvement than the utilisation or punctuality measures currently emphasised. Treating overtime as a quality indicator with dual staff and patient consequences changes what counts as a successful OR improvement programme.

---

## Figures and tables

- **Table 1.** Overtime rate by weekday and year (from Fig.16, Fig.17 in the in-depth file).
- **Table 2.** Room-by-room overtime rate, mean, median, P95 (from Table 25 in the in-depth file).
- **Table 3.** Overtime and start-delay by urgency and overlap status (from Tables 35, 38).
- **Table 4.** CV of observed duration by planned-duration bucket (from Table 13).
- **Figure 1.** Dot plot — room-level overtime rates at Genk.
- **Figure 2.** Illustrative cascaded day — how a 9 AM 20-minute delay compounds into a 17:30 post-shift case.
- **Figure 3.** Scatter — room-level late-start share vs overtime rate (with Pandit 2012 R² anchor).

---

## Reference set (~22–28 total, Vancouver numbered)

Core operational (from prior drafts):
- Dexter 2004; McIntosh 2006; Dexter & Epstein 2009; Wachtel & Dexter 2009; Fügener 2017; Pandit 2012; Strum 2000; Eijkemans 2010; Bauer 2020; Schouten 2023

Patient-harm layer (new):
- Cortegiani 2020; Kelz 2008; van Zaane 2015; Rothschild 2009; Landrigan 2004; Barger 2006; Gates 2018; Saager 2014; Starmer/I-PASS 2014; Segall 2012; Nagpal 2010; Wahr 2013

Staff-harm layer (new):
- Stimpfel 2012; Griffiths 2014; Dall'Ora 2016; Dall'Ora 2020; Caruso 2014; Shanafelt 2019; Dimou 2016; Van Bogaert 2017

BMJ QS precedents (from prior drafts):
- Abdelfattah 2020; Joseph 2019

Framing bridge (from prior drafts):
- Zhang & Pandit 2023

Trim to final 24 in the writing stage.

---

## Writing order

1. Methods (already well-specified from prior draft — port over).
2. Results (port room-level and cascading numbers directly from `01_genk_overtime_facts.md`).
3. Introduction (new — leads with the dual harm argument).
4. Discussion (new — four-part structure as above).
5. Abstract and title last.
6. Apply humanizer pass per CLAUDE.md rules.
