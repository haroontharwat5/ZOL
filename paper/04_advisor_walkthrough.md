# How to present this paper to Niels and Maxim

A practical guide for your meeting. Read this 10 minutes before you walk in.

---

## Before the meeting

**Review these two files** (5 min):
- `00_framing_recommendation.md` — the full reasoning behind the framing choice
- This document — the pitch and Q&A below

**The one sentence you open with:**

> "I think we should frame the ZOL paper as a natural experiment in OR benchmarking: four sites share the same governance but run four different operating models, and the raw 16.8-fold overtime gap is mostly structural, not managerial."

---

## The pitch (5-7 minutes)

Walk them through it in this order. Keep it conversational. Don't read from a script.

**1. The dataset**
"We have 228,623 surgical cases across 4 ZOL sites from January 2022 to May 2025. That's 41 months of complete OR timestamp data. The sites share everything: same EHR, same governance, same labor agreements. What they don't share is their operating model."

**2. The four models**
Keep this brief. One sentence per site:
- "Genk is the big one: 96k cases, 26 rooms, 24/7, does everything, 42% ambulatory."
- "Lanaken is the opposite: 69k cases, weekdays only, 98% ambulatory, mean procedure 30 minutes."
- "Maaseik is a hybrid: it has MK rooms that look like Lanaken and MO rooms that look like Genk."
- "Cathlab is specialized cardiac interventions, 9k cases, mostly inpatient despite being almost all elective."

**3. The headline number**
"Raw overtime rates: Genk 8.4%, Cathlab 5.8%, Maaseik 2.8%, Lanaken 0.5%. That's a 16.8-fold spread. If you showed this to any hospital board, they'd conclude Lanaken is massively more efficient than Genk."

**4. The stratification collapse**
"But when we filter step by step: weekdays only, day shift only, elective only, then split by ambulatory versus inpatient, the gap shrinks from 16.8x down to 3-4x. Four-fifths of the apparent gap is structural. It's comparing apples to oranges."

If Niels asks "what exactly happens at each step?" you can say:
- L0 (raw): 16.8x spread
- L1 (weekdays): removes weekend emergency confound
- L2 (day shift): removes evening/night shift activity
- L3 (elective): removes urgent cases
- L4 (admission type split): separates ambulatory from inpatient within elective day-shift weekday cases
- After L4: residual ~3-4x

**5. The room-level finding**
"Here's the bigger finding. Within Maaseik alone, the worst room (MO03, 8.9% overtime) versus the best room (MK11, 0.2%) is a 44-fold spread. That's nearly triple the 16.8x spread between campuses. The waste isn't between hospitals. It's between rooms inside each hospital."

**6. Three things that contradict the literature**
- "First-case punctuality doesn't predict stratified overtime. Genk has the best first-case discipline but the worst overtime."
- "Duration-prediction accuracy is nearly identical across sites within each duration bucket. It's not about forecasting."
- "Start-time cascading wastes about 4x more OR time than duration overruns. The problem is delays stacking up, not surgeries running long."

**7. Why HCMS, not BJS**
"BJS wants clinical outcomes. We don't have any. Our paper is about operations, scheduling, and benchmarking methodology. That's Health Care Management Science territory. It's Q1, impact factor around 3. Schneider et al. published the German benchmarking dataset there in 2024, which is the closest precedent to our work."

---

## Anticipated questions from Niels

**"Why not BJS or another surgery journal?"**
We don't have morbidity, mortality, or readmission data. Surgery journals will ask "so what does this mean for patients?" and we can't answer that cleanly. HCMS is the right audience: people who make OR management decisions.

**"Is the progressive stratification method novel enough for a Q1 journal?"**
Yes. I checked the literature thoroughly. Ernst et al. (2012) use a single-layer case-mix adjustment. Nobody has published a step-by-step stratification showing how the between-site spread collapses at each level. The systematic review by Schouten et al. (2023) in J Med Syst explicitly identified inconsistent metric definitions and the lack of multi-layer adjustment as open problems. Our method directly addresses that gap.

**"What about causality? Isn't this just descriptive?"**
It is descriptive, and we're honest about that. The contribution is methodological: we show *how* to benchmark fairly, not *why* one site outperforms another. HCMS publishes observational benchmarking studies regularly. The German benchmarking papers (Ernst et al., Schneider et al.) are also descriptive.

**"Should we add a multilevel regression model?"**
We could, and it would strengthen the paper. But the simple variance partition already makes the point. I'd suggest flagging a full hierarchical Bayesian model as future work rather than delaying submission. If reviewers ask for it, we can add it in revision.

**"What about the Cathlab labeling error?"**
Our in-depth report for Cathlab says "ambulatory admissions represent 88.6%" but the data table shows HOS (inpatient) = 88.6%. The text is wrong; the table is right. I recommend we fix the original report and include a one-sentence note in the paper's methods section. It shows good practice to catch and disclose our own errors.

**"How long will this take to write up?"**
The first draft is already written. We need: (1) a round of internal review, (2) verification of all in-text numbers against the PDFs, (3) final formatting. Realistically 4-6 weeks to submission if we don't add new analyses.

**"What if HCMS rejects us?"**
BMC Health Services Research is the fallback. It's open access, Q2, higher acceptance rate. Our paper is stronger than most OR efficiency work published there, so chances are good. Anesthesia & Analgesia is another option if we want to reach the Dexter/Macario readership.

---

## The three decisions you need from them

Write these on a sticky note before you go in:

1. **Framing:** natural experiment in operating-model benchmarking. Are they on board, or do they want something different?
2. **Journal:** HCMS as primary target, BMC-HSR as fallback. Agreed?
3. **Cathlab labeling error:** fix the original report + disclose in the paper. OK?

---

## If they push back

**If Niels wants a different framing:**
Ask what specifically he'd change. Listen. The framing is flexible on the exact narrative wrapper, but the core results (stratification collapse, room-level variation, FCOTS paradox) are what they are. Any framing needs to accommodate all of them.

**If they want more analysis before writing:**
Push back gently. The analysis is done. Running more analyses delays submission without changing the story. If Niels insists on a multilevel model, ask if it can be added in revision rather than blocking submission.

**If they prefer BJS or a surgery journal:**
Explain that surgery journals need clinical outcome data (mortality, complications, length of stay as a patient outcome). We have length of stay as a number but not as a quality metric. The paper will be seen as "interesting but not surgical" by BJS reviewers. If they still want to try, HCMS is a better first submission with BJS as an unlikely plan B.

---

## Quick reference card

Glance at this during the meeting:

```
Total cases:          228,623  (Jan 2022 - May 2025)
Sites:                Genk 96k | Lanaken 69k | Maaseik 54k | Cathlab 9k
Raw OT spread:        16.8x    (Genk 8.4% vs Lanaken 0.5%)
After stratification: 3-4x     (four-fifths is structural)
Room spread Maaseik:  44.5x    (MO03 8.9% vs MK11 0.2%)
Room spread Lanaken:  17x      (LO03 1.7% vs LP01 0.1%)
FCOTS paradox:        Genk best discipline, worst overtime
Duration CV:          Similar across sites within buckets
Cascade:overrun:      ~4:1 ratio
Target journal:       HCMS (Q1, IF ~3.0)
Backup:               BMC Health Services Research
```
