# Meeting Prep — Haroon + Maxim, 24 April 2026

**Purpose:** Decide which Genk overtime results go into the paper, align on structure and next steps before the May 4 meeting with Niels.

---

## 1. What changed since last time

After the meeting with Niels (mid-April), the paper direction shifted:

- **Before:** Cross-campus comparison (Genk vs Lanaken vs Maaseik vs Cathlab) with progressive stratification as the methodological centerpiece. Target: BMJ Quality & Safety via measurement-validity angle.
- **Now:** Single-campus deep dive into overtime at Genk. Central concept = overtime. Double argument: bad for staff (fatigue, burnout, turnover) AND bad for patients (after-hours outcome risk, handover errors). Still targeting BMJ Quality & Safety.

The skeleton, literature, and fact extraction are done. Files are in `paper/bmjqs_v2_overtime/`.

---

## 2. The paper skeleton (for discussion)

**Title:** Where does operating-room overtime come from, and who pays for it? A 96,044-case analysis of one tertiary centre

**Structure:**

| Section | Words | Content |
|---|---|---|
| Introduction | ~600 | Why overtime matters: staff harm (burnout, intent-to-leave) + patient harm (after-hours mortality, handover risk). Gap: nobody has mapped overtime *within* a hospital at the room level. Three research questions. |
| Methods | ~700 | Setting (Genk, 25 ORs, 96,044 cases, Jan 2022–May 2025). Variables per Bauer 2020. Descriptive + mechanism analyses. |
| Results | ~1,000 | Six findings (see Section 3 below). |
| Discussion | ~1,000 | Concentration, cascading mechanism, staff/patient implications, what to do, limitations. |
| Conclusion | ~200 | Overtime is concentrated and cascading-driven; room-level metrics are the actionable target. |
| **Total** | **~3,500** | |

---

## 3. Proposed results — which findings to include?

These are the candidates from the exploratory and in-depth Genk analyses. We need to decide together which ones earn a table/figure and which get a sentence.

### Finding 1: Overall overtime burden
- 8,024 of 96,044 cases (8.4%) ran past shift end.
- Mean overtime 59 min; median 38 min; P95 194 min.
- Weekday rate 7.8–8.5%; weekend 15.5–16.8%.
- Year trend: 8.8% (2022) → 7.2% (2025). Slow improvement, not solved.
- **Proposed:** Table 1 (overtime by weekday and year). Sets the scene.

### Finding 2: Room-level concentration ← probably the strongest finding
- GO10: 32.9% overtime, mean 154 min, P95 328 min (complex surgery).
- GO09: 16.3%; GO13: 13.8%; GO12: 13.4%.
- GEG1, GSE1, GEX1: near-zero overtime.
- Spread within one campus: 0% to 32.9% — wider than the between-campus gap.
- **Proposed:** Table 2 (room-by-room overtime) + Figure 1 (dot plot). This is the headline finding.

### Finding 3: Cascading / shift displacement ← the mechanism story
- 4,786 cases (5%) performed in a different shift than planned.
- Mean start delay: **352 minutes** (≈ 6 hours).
- Mean duration difference: **−22 min** (shorter than planned!).
- Mean overtime for these cases: only 9.2 min.
- **Interpretation:** These cases don't run long. They get displaced by upstream delays. The problem is cascading, not overruns.
- **Proposed:** Figure 2 (illustrative cascaded day) + key numbers in text. This is the mechanism finding.

### Finding 4: Urgent–elective overlap ← the daily disruptor
- 12.5% of Genk cases are non-elective.
- Urgent–elective overlap in same OR on **69.7% of observation days** (869/1,247 days).
- Elective cases with overlap start ~30 min later (up to 60 min in 2022).
- GO11 absorbs most overlap: 485 events, 15.5% of elective activity.
- Non-elective cases: 18% after-hours rate vs 7% for elective.
- **Proposed:** Table 3 (overtime by urgency + overlap effect). Shows the main daily mechanism.

### Finding 5: First-case punctuality does NOT predict overtime
- GEG1: 90% of cases start late → 0% overtime.
- GO10: mid-pack on start punctuality → 32.9% overtime.
- Consistent with Pandit et al. (2012): R² = 0.04–0.08 between start and finish.
- **Proposed:** Figure 3 (scatter: late-start % vs overtime % by room). Challenges the FCOTS orthodoxy.

### Finding 6: Duration estimation variability
- CV by planned-duration bucket: <30 min = 0.61; 31–60 = 0.46; 61–90 = 0.36; 91–180 = 0.35; >180 = 0.42.
- Mid-length procedures (61–180 min) are most predictable.
- Very long cases (>180 min) have highest planning-deviation CV (1.86) — these cluster in GO10.
- Top deviating procedures: DEBULKING MET HIPEC (74.4 min), AVR (73.7), CABG OFF PUMP (60.4).
- **Proposed:** Table 4 (CV by bucket). Explains why GO10 carries the heaviest overtime — case-mix effect.

### Findings we could cut if space is tight
- Room swap analysis (1.1% rate, minimal overtime effect — probably a sentence, not a table).
- Surgeon-level duration deviation (interesting but might distract from the room-level story).
- Idle time between cases (median 7 min — confirms turnover is not the bottleneck, one sentence).

---

## 4. Discussion questions for tomorrow

1. **Which findings earn a table/figure vs. a sentence?** I propose Findings 1–5 get tables/figures; Finding 6 gets a compact table; room swaps, surgeon variation, and idle time get one sentence each.

2. **Is the Maxim-updated in-depth file ready?** Numbers may shift slightly after data correction. If it's not ready yet, we can write with current numbers and swap later.

3. **Do we want to include any cross-campus context?** Niels said to drop the comparison as the main story, but one compact table showing Genk 8.4% vs Cathlab 5.8% vs Maaseik 2.8% vs Lanaken 0.5% as background context might still be useful. In or out?

4. **Room names in the paper?** Do we use GO10, GO11, etc., or anonymise them? If reviewers want to know about the hospital, room codes identify the site. Discuss with Ben/Dieter.

5. **Do we split Results into subsections or use a continuous flow?** BMJ QS often uses subsection headers in Results. I propose six subsections matching the six findings above.

---

## 5. Literature status

### Already compiled and tagged
- **14 existing references** from prior drafts, each tagged to a specific overtime claim (`02_existing_overtime_sources.md`).
- **22 new references** from targeted literature search, split by staff-harm and patient-harm (`03_new_literature.md`).

### Top 5 new references (verification in progress)
1. **Cortegiani 2020, BJA** — after-hours surgery mortality meta-analysis (patient side, flagship)
2. **Saager 2014, Anesthesiology** — intraoperative handover raises complication odds
3. **Griffiths 2014, Medical Care** — European nurse overtime → burnout (RN4CAST, 12 countries)
4. **Rothschild 2009, JAMA** — post-call attending complications
5. **Kelz 2008, Annals of Surgery** — NSQIP time-of-day morbidity

### Still need from Ben/Dieter
- Any clinical papers they know on OR overtime and patient outcomes.
- Any internal ZOL data on staff satisfaction or turnover related to overtime (for the Discussion, not the analysis).

---

## 6. Timeline

| Date | Milestone |
|---|---|
| 24 April (tomorrow) | Haroon + Maxim: agree on which results, review skeleton |
| Week of 28 April | Haroon writes Methods + Results draft; Maxim finalises in-depth Genk file |
| 4 May at 11:00 | Meeting with Niels: walk through skeleton + early draft |
| Mid-May | Complete draft ready for internal review |
| Before summer | Submit to BMJ Quality & Safety |

---

## 7. Files to share with Maxim

All in the GitHub repo at `paper/bmjqs_v2_overtime/`:
- `00_pivot_decision.md` — explains the pivot (share this first for context)
- `01_genk_overtime_facts.md` — all overtime numbers from the PDFs
- `04_skeleton.md` — the paper structure
- `03_new_literature.md` — new staff + patient harm references
