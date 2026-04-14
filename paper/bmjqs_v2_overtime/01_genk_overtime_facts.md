# Genk Overtime — Complete Fact Sheet

All numbers below come from `Exporative_Data_Analysis_Genk.pdf` (22 pages, October 2025) and `In-Depth_Analysis_Genk.pdf` (51 pages, October 2025). Page references point to the in-depth file unless marked (EDA).

Definition used throughout: overtime = case extends past the scheduled shift end of the operating team. Day shift runs 08:00–16:30. After-hours = 16:30 onward on weekdays, plus weekends.

---

## Headline numbers

| Metric | Genk | Source |
|---|---|---|
| Cases analysed | 96,044 | Table 24, p.28 |
| Cases with overtime | 8,024 | Table 24, p.28 |
| Overtime rate | **8.4 %** | Table 24, p.28 |
| Mean overtime (minutes) | 59 | Table 24, p.28 |
| Median overtime (minutes) | 38 | Table 24, p.28 |
| P95 overtime (minutes) | 193.8 | Table 24, p.28 |

For context only, the cross-campus comparison (Table 26, p.34):

| Campus | Cases | Overtime rate | Mean OT | P95 OT |
|---|---|---|---|---|
| Genk | 96,044 | 8.4 % | 59 | 193.8 |
| Cathlab | 9,282 | 5.8 % | 41.8 | 108.3 |
| Maaseik | 53,902 | 2.8 % | 42 | 129 |
| Lanaken | 69,395 | 0.5 % | 15.7 | 48.5 |

---

## Time patterns

**By year (p.29, Fig.17):**
- 2022: 8.8 %
- 2023: 8.6 %
- 2024: 8.2 %
- 2025 (partial): 7.2 %
  - Slow downward trend, no step change.

**By weekday (p.29, Fig.16):**
- Weekdays: 7.8–8.5 % (Mon 8.0, Tue 8.2, Wed 8.5, Thu 7.8, Fri 8.0)
- Saturday: 16.8 %
- Sunday: 15.5 %

**By end-time hour (p.31, Fig.18):**
- Sharp peak immediately after 16:30 (~3,000 cases ending in the 16:30–17:30 window)
- Rapid decay through 17:30–20:00
- Small residual tail past 22:00, very few past midnight

**Mean overtime by weekday (p.32, Fig.19):**
- Mon–Fri mean: 57.4–60.8 minutes; median 34–38 minutes
- Sat: mean 63.3, median 44.5
- Sun: mean 59, median 46

**By shift type (p.33, Fig.21):**
- Day shift 08:00–16:30 has the widest overtime distribution (volume effect)
- Evening 16:30–22:00: narrower spread
- Night 22:00–08:00: concentrated near zero with a few long outliers

---

## Room-level concentration

**Room-by-room overtime rate, ranked (Table 25, pp.30–31):**

| Room | Cases | Overtime % | Mean OT | Median OT | P95 OT |
|---|---|---|---|---|---|
| GIC7 | 2 | 50 | 10 | 10 | 10 |
| **GO10** | **1,752** | **32.9** | **154.2** | **142.5** | **327.5** |
| GO09 | 2,640 | 16.3 | 71.6 | 53 | 204 |
| GO13 | 3,308 | 13.8 | 61.4 | 39 | 173.2 |
| GO12 | 2,889 | 13.4 | 59.2 | 40.5 | 176 |
| GO08 | 2,615 | 12.5 | 57.7 | 32 | 220.1 |
| GO05 | 4,905 | 12.3 | 54.8 | 39 | 160.8 |
| GO11 | 7,567 | 11.7 | 55.1 | 39.5 | 156.6 |
| GO02 | 3,514 | 11.3 | 52.1 | 38 | 149.6 |
| GO04 | 4,535 | 10.7 | 57.4 | 40 | 155.8 |
| GO03 | 4,204 | 9.4 | 45.1 | 33 | 142.6 |
| GO06 | 5,226 | 9.4 | 58.5 | 41 | 174.6 |
| GO16 | 4,100 | 8.9 | 36.9 | 26 | 101.8 |
| GO15 | 4,327 | 8.7 | 46.6 | 34 | 130.2 |
| GO07 | 4,751 | 6.8 | 37.9 | 28 | 103.6 |
| GO17 | 5,482 | 6.8 | 44.2 | 27 | 138.5 |
| GO18 | 5,300 | 6.6 | 41.4 | 27.5 | 127.3 |
| GO01 | 6,607 | 5.8 | 57.5 | 36 | 193.9 |
| GO14 | 6,896 | 3.6 | 31.1 | 19 | 87 |
| GOP2 | 1,316 | 3.1 | 24.4 | 17 | 75 |
| GEE1 | 2,330 | 2.4 | 14 | 10.5 | 37.2 |
| GEE2 | 1,646 | 1.6 | 16.1 | 12 | 36 |
| GOP1 | 2,739 | 1.6 | 22.2 | 18 | 69 |
| GEX1 | 634 | 0.3 | 11 | 11 | 17.3 |
| **GEG1** | 4,498 | **0** | (no OT cases beyond 1 sample at 52.5) | — | — |
| GSE1 | 2,261 | 0 | — | — | — |

GIC7 has two cases, so we exclude it from interpretation.

**Take-away:** the room-level spread within a single Genk OR complex runs from 0 % to 32.9 % — more than thirty-fold from floor to ceiling, wider than the between-campus gap between Maaseik and Genk. GO10 carries the heaviest overtime both in frequency and magnitude (mean 154 min, P95 of five and a half hours). The next tier (GO08–GO13) sits at 12–16 %. Three rooms (GEG1, GSE1, GEX1) essentially never overrun.

---

## Cascading — shift-boundary displacement

From Table 39, p.47: **4,786 cases (5 %) at Genk were performed in a different shift than originally planned.**

| Metric for mismatched-shift cases | Value |
|---|---|
| Number of cases | 4,786 |
| Share of total | 5 % |
| Mean start delay | **352.2 minutes** (≈ 5 h 52 min) |
| Mean duration diff vs plan | **−22 minutes** (shorter than planned) |
| Mean overtime for these cases | 9.2 minutes |

This is the central cascading fact. The displaced cases do not run long on their own. They finish on time or early. What makes them land in a different shift is the accumulation of upstream delays. They then become the cases exposed to fatigued late-shift staff or handover transitions.

Monthly trend (Fig.30, p.48): 7–8 % of cases in early 2022 → stabilised around 4–5 % by 2024. Modest improvement, not a solved problem.

---

## Start-time delays

From Table 19, p.21:

| Direction | % of cases | Mean (min) | Median (min) | P99 (min) |
|---|---|---|---|---|
| Late start | 68.2 % | 70 | 30 | 847 |
| Early start | 31.8 % | 33.7 | 12 | 350.2 |

Start-delay patterns by weekday (Table 20, p.23): Mon–Fri mean delay 34.8–38.9 min, Sat 47.2 min, Sun 44.5 min.

By room (Table 21, p.23): late-start share ranges from 42.5 % (GSE1) to 90 % (GEG1). GO11 stands out with mean late-start delay of 320.3 min — driven by extreme outliers in this high-volume room that runs both planned lists and urgent intake.

First-case punctuality alone therefore does not define who runs late. The rooms with the worst start-time discipline (GEG1, GO11) are not the rooms with the worst overtime (GEG1: 0 % overtime; GO11: 11.7 %, mid-tier).

---

## Urgent cases and overlap with elective activity

From Table 33, p.41: urgent (niet-electief) cases = 12,016, **12.5 %** of Genk volume. 

Urgent-case timing (p.41, Fig.25): concentrated 13:00–15:00 with a secondary evening peak around 18:00. Weekdays carry about 10.5–11.3 % urgent share; Saturdays 65 %; Sundays 60 %.

From Table 35, p.43 — **do urgent cases drive overtime?**

| Urgency | n | After-hours share | Mean OT | P95 OT |
|---|---|---|---|---|
| Elective | 84,028 | 7 % | 4.1 | 18 |
| Non-elective | 12,016 | 18 % | 10.5 | 67.2 |

Urgent cases run into after-hours at more than twice the rate of elective cases, but elective cases still contribute the larger absolute volume of after-hours minutes because they are seven times more numerous.

From Table 37, p.44: **urgent–elective overlap in the same OR occurred on 69.7 % of 1,247 observation days (869 days with at least one overlap).** Daily rather than exceptional.

From Fig.29, p.45: elective cases affected by an urgent overlap start about 30 minutes later than elective cases without overlap; in early 2022 this gap reached 60 minutes.

From Table 38, p.46: GO11 carries the highest absolute number of overlaps (485 events, 15.5 % of its elective cases) — the designated urgent-intake room absorbs the overlap pressure.

---

## Duration estimation variability

From Table 13, p.13 — CV of observed duration by planned-duration bucket:

| Planned bucket | n | CV (observed duration) | CV (planning deviation) |
|---|---|---|---|
| < 30 min | 19,511 | 0.61 | 1.25 |
| 31–60 min | 28,674 | 0.46 | 1.07 |
| 61–90 min | 19,921 | 0.36 | 1.06 |
| 91–180 min | 20,592 | 0.35 | 0.91 |
| > 180 min | 7,343 | 0.42 | 1.86 |

Mid-length procedures (61–180 min) are the best-planned. Short cases are proportionally noisy because small absolute errors are large percentages. Very long cases carry the highest planning-deviation CV, which matters for cascading risk.

From Table 22, p.25 — procedures with the largest absolute duration deviations at Genk: DEBULKING MET HIPEC (mean abs dev 74.4 min), AVR (73.7), DEBULKING (72.2), FEMUR FRAKTUUR LFN (68.5), TROMBECTOMIE (66.7), CABG OFF PUMP (60.4). These are the complex-cardiac and complex-oncology cases concentrated in GO10, GO11, and the cardiac rooms.

---

## Room swaps

From Table 27, p.35: **1,066 cases swapped rooms (1.1 %).** Weekday rates 0.5–1.3 %; weekend rates 3.5–4.8 %.

Impact on overtime (Table 32, p.39): swapped 9.5 % after-hours vs non-swapped 8.3 %. Small effect. Swapping is not a major overtime driver.

---

## Other structural features

- **71,621 unique patient IDs** across 225 surgeons and 211 anesthesiologists (p.4)
- **1,327 distinct procedure names**, heavy concentration in top 20 (p.5, EDA)
- **Admission mix at Genk**: 51 % ambulatory (DAG), 49 % inpatient (HOS), 0.1 % emergency (SPOED) (p.5)
- **Urgency mix**: 87.5 % elective, 12.5 % non-elective (p.6)
- **Weekday volume**: evenly split 18.7–20.9 % Mon–Fri; Sat 1.7 %; Sun 1.5 % (p.6)
- **Mean idle time between cases**: 9.2 min; median 7 min (Table 40, p.48). Idle time is not the bottleneck.
- **Surgeon-level duration deviation**: ranges from 30.4 to 68.1 minutes mean absolute deviation across 15 highest-volume surgeons (Tables 23, pp.26–27). Not uniform.

---

## What the facts support for the new paper

1. **Overtime is concentrated, not distributed.** GO10 alone runs overtime in roughly one in three cases and averages over two and a half hours of overrun. A handful of rooms carry the weight.
2. **Cascading dominates the mechanism.** 4,786 cases get shifted into a later shift with an average delay of nearly six hours — and then finish early relative to plan. The problem is upstream displacement, not individual cases running long.
3. **Urgent–elective overlap is the main daily disruptor.** 70 % of days see at least one overlap, and overlap doubles the start delay for elective cases in the affected room.
4. **First-case punctuality does not predict overtime.** GEG1 (endoscopy) has the worst late-start share (90 %) and zero overtime. GO10 has moderate start-time performance and the worst overtime.
5. **Duration estimation is cleanest for 60–180 min cases.** Short cases and very long complex cases carry the most planning noise.
6. **Weekend overtime is twice weekday rates.** Emergency-driven.
7. **The trend is slowly improving** (8.8 % → 7.2 %) but still far from a solved problem.
