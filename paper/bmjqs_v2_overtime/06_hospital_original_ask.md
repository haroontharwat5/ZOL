# Hospital's Original Ask (14 February 2025)

Source: `20250214 - UHasselt - OR - introduction (1).pdf`, 22 slides, delivered by the ZOL clinical team (Ben, Dieter and colleagues) at the project kickoff.

This file is important because it shows the original questions the hospital wanted answered. The overtime-centered framing of the paper is not a departure from that ask — it is a direct response to it. Several of the paper's central claims map onto specific questions the clinical team raised in this presentation.

---

## 1. Operating department profile (slides 3–4)

- **Campus St Jan (Genk):** 18 theatres (operating department) + 7 theatres (interventional department) + ambulatory anesthesia for endoscopy/sedation (IVF, MKA)
- **Campus St Barbara (Lanaken):** 5 theatres
- **Campus ZMK (Maaseik):** 6 theatres + ambulatory endoscopy
- Total annual procedures: more than 50,000
- Staff: more than 90 anesthesiologists (including trainees/fellows)
- Tertiary centre covering all surgery except congenital cardiac and transplant
- General anesthesia / locoregional anesthesia / local anesthesia

## 2. Risk stratification (slides 5–9)

The hospital team emphasised that they care about risk stratification as part of the study. The tools they named:
- ASA classification (categories 1–6)
- Charlson Comorbidity Index (CCI)
- Lee Revised Cardiac Risk Index (RCRI)
- Frailty Score
- EuroScore-II (cardiac surgery)
- Surgical procedure risk

**Implication for our paper:** we do not have patient-level ASA or CCI data in our current dataset. The paper acknowledges this as a limitation and positions a future Phase 2 analysis that would incorporate risk stratification. This is consistent with the original phased roadmap (see Section 8).

## 3. Surgical outcome (slide 10)

The hospital team said they track:
- Mortality and morbidity
- Cox regression analysis (proportional hazard)
- VLAD (Variable Life Adjusted Displays) — reference: https://www.ucl.ac.uk/clinical-operational-research-unit/sites/clinical_operational_research_unit/files/vladmethods.pdf

**Implication for our paper:** outcome data live in the hospital system. We do not analyse them in the current paper, but we can cite this slide to show the hospital themselves framed safety tracking as part of the study program.

## 4. Daily practice — the staffing pyramid (slide 11)

This is the single most important slide for the overtime paper.

| Time window | OR rooms staffed | Coverage |
|---|---|---|
| 08:00 – 16:30 | Full complement (25 at Genk) | 2–3 nurses per OR room |
| 16:30 – 17:30 | **Decrease to 8 OR rooms** | |
| 17:30 – 22:00 | **Decrease to 4 OR rooms** | |
| 22:00 – 08:00 | **3 nurses on call (max 1 OR room)** | |
| Weekend / bank holidays | Back-up nurses 24/7 | |

This is why overtime is not just "extra time" — it is cases competing for dramatically reduced capacity. A case running past 16:30 is not simply inconveniencing the team that would otherwise be heading home; it is claiming one of only eight rooms staffed for that hour window, pushing downstream cases into an even tighter four-room configuration at 17:30, and potentially into the single overnight room.

**Paper usage:** this pyramid should appear as Figure 0 or as a methods-box diagram. Every reviewer will then understand why concentrated overtime has disproportionate cost.

## 5. Data reliability caveat (slide 14)

Quoted from the hospital presentation:

> "Nurse-based for theatre in, doctor-based for theatre out"
>
> **"Room in and room out are the only reliable data available!"**

Other registration points (called for patient, patient in operating department, start/end induction, start/end operation, patient to recovery, patient to ward) exist but are not considered reliable by the hospital team.

**Paper usage:** this is the methodological justification for defining overtime as "case still in the room past 16:30" rather than using start-of-induction or end-of-operation markers. We cite this as received data-quality guidance from the hospital.

## 6. Planning inputs (slide 16)

When a surgery is planned, the system captures:
- Procedure code, acting surgeon, requested length of surgery
- Materials required (for case cart preparation)
- Priority (elective, urgent, emergent, salvage)
- Hospitalisation or day-care surgery
- ASA classification at planning
- Anticoagulant drug management

**Paper usage:** the "requested length of surgery" field is our `PlannedOR` variable. The urgency field matches our elective/non-elective split.

## 7. What the hospital asked us to investigate — efficiency (slide 18)

Four questions verbatim from the slide:

1. **Does scheduled OR time reflect observed OR time?** → our duration-estimation analysis (CV by bucket, Table 13 in the in-depth file)

2. **Does observed OR time correspond with current working schedule?**
   - *"Determining area under the curve"* → **this is exactly our overtime analysis**. The hospital framed overtime from day one as "area under the curve" — a continuous measure of how much activity spills beyond the staffing pyramid.

3. **Can we improve OR scheduling efficiency?**
   - *"Efficient use of emergency theatre?"* → our urgent-elective overlap analysis (69.7% of days, Table 37)
   - *"Creating gaps for non-elective surgery?"* → our finding that GO11 absorbs overlap events, and that overlap cases delay elective starts by ~30–60 min

4. **Can we predict OR scheduling?** → future work, Phase 3

## 8. What the hospital asked us to investigate — safety (slide 19)

Three questions verbatim from the slide:

1. **Does predicted mortality correspond with observed mortality?** → future work (needs patient-level outcome data)

2. **Does OR staffing/efficient use of OR time correspond with mortality/outcome?**
   - *"Linking AUC and mortality?"* → **this is exactly the double-ended argument of our paper**. The hospital itself asked whether overtime (AUC past 16:30) has mortality implications. Our paper answers the first half (how big and where) and points to the literature for the second half (does after-hours activity affect outcomes), leaving the ZOL-local answer to Phase 2.

3. **Can we predict mortality more accurately using patient and surgery variables?** → future work, Phase 2

## 9. Project phasing (slides 21–22)

The hospital team proposed a three-phase plan:

- **Phase 1 — Retrospective analysis.** Scheduled vs observed timing. Existing data. **Calculating area under the curve.** Specific questions: *does scheduled operating time correspond with the real situation?* and *added value of "swapping theatres"?* (We answer both. Room swap = 1.1 %, not a major overtime driver.)
- **Phase 2 — Prospective study** with patient variables (CCI, ASA, type of surgery). Does predicted mortality reflect observed mortality? Using VLAD curves.
- **Phase 3 — Prediction of operating room scheduling.**

**Implication for our paper:** this is Phase 1. The paper should explicitly position itself as delivering on the Phase 1 questions and handing off to Phase 2 for the patient-outcome link.

---

## 10. What this changes for the paper

| Element of the paper | Connection to the original ask |
|---|---|
| Overtime as central concept | "Area under the curve" (efficiency slide, Phase 1) |
| Room-level concentration (GO10, GEG1) | Not explicitly asked, but directly relevant to "staffing pyramid" reasoning — concentrated overtime is what collapses a 25-room daytime complex into 8/4/1 at night |
| Cascading / shift displacement | "Added value of swapping theatres" and "efficient use of emergency theatre" (Phase 1) |
| Urgent–elective overlap | "Creating gaps for non-elective surgery" (efficiency slide) |
| FCOTS does not predict overtime | Extension of "does scheduled OR time reflect observed OR time?" |
| Staff harm (fatigue, burnout) | Not in the ask — added by Niels — but aligns with hospital's wider concern about overtime being undesirable for staff |
| Patient harm (after-hours outcomes) | "Linking AUC and mortality?" (safety slide) — the hospital itself raised this question, we answer through literature |
| Phased program positioning | Slides 21–22 — positioning the paper as Phase 1 is exactly what the hospital asked for |

The paper is now better framed as: *responding to the hospital's Phase 1 research questions, with a safety framing motivated by the hospital's own Phase 2 ambition, and with the limitations (no patient-level outcome data) explicitly pointing to Phase 2 as the next step.*

## 11. Quotes worth using directly in the paper

- On the staffing drop: "During daytime surgery, 2-3 nurses per OR room. From 16:30-17:30, decrease to 8 OR rooms. From 17:30-22:00, decrease to 4 OR rooms. From 22:00-08:00, 3 nurses on call, maximum 1 OR room."
- On data reliability: "Room in and room out are the only reliable data available."
- On the safety-efficiency link: the hospital explicitly asked "Does OR staffing/efficient use of OR time correspond with mortality/outcome? Linking AUC and mortality?"

These can appear in the Methods (for the staffing and data-reliability notes) and in the Introduction (for the safety-efficiency link).
