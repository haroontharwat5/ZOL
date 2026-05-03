# Definition and reference verification

This document checks (a) whether the overtime and overlap definitions in the outline and draft match what the R analysis code actually does, and (b) whether each cited reference exists and supports the specific claim we make. Verified against the source R files on 2 May 2026.

---

## Part 1 — Overtime definition

### What the R code actually does

Source: `data_cleaning.R` lines 89-145, 251-270.

The `bucket_to_shift()` function assigns each case to a shift based on its actual room-in time (`ORIn`):

- `ORIn` between 08:00 and 16:30 → shift "08:00-16:30" (day) → `shift_end` = same calendar day at 16:30
- `ORIn` between 16:30 and 22:00 → shift "16:30-22:00" (evening) → `shift_end` = same calendar day at 22:00
- `ORIn` between 22:00 and 08:00 → shift "22:00-08:00" (night) → `shift_end` = next calendar day at 08:00
- Special carve-out: if `ORIn` is between 07:30 and 08:00 AND `OROut` crosses 08:00, the case is reassigned to the day shift

Then:

```r
afterhours_flag = as.integer(OROut > shift_end)
overtime_minutes = pmax(0, as.numeric(difftime(OROut, shift_end, units = "mins")))
```

So a case is flagged as after-hours if its room-out time exceeded the end of the shift it was operating in. Overtime minutes equal `OROut − shift_end`, floored at zero.

### Examples that follow from this code

| Room-in | Room-out | Assigned shift | Shift end | After-hours? | Overtime min |
|---|---|---|---|---|---|
| 09:00 | 17:00 | 08:00-16:30 | 16:30 | YES | 30 |
| 14:00 | 16:25 | 08:00-16:30 | 16:30 | NO | 0 |
| 18:00 | 21:30 | 16:30-22:00 | 22:00 | NO | 0 |
| 18:00 | 23:00 | 16:30-22:00 | 22:00 | YES | 60 |
| 23:00 | 03:00 next day | 22:00-08:00 | 08:00 next day | NO | 0 |
| 23:00 | 09:00 next day | 22:00-08:00 | 08:00 next day | YES | 60 |

A case starting and ending fully within the evening or night shift is NOT flagged as overtime. The flag fires only when the case crosses its assigned shift's end boundary.

### What our outline and paper say

**Skeleton (`10_skeleton_with_figures.md`, §2.4):** *"Overtime = case still in the room past 16:30 on the calendar day, or any case ending in the evening or night shift. Shift-based, not duration-based."*

**Paper draft (`11_paper_draft.md`, Methods):** *"Overtime was defined as any case still in the room past 16:30 on the calendar day, or any case ending in the evening or night shift. This is a shift-based definition, not a duration-based one."*

### Verdict — INCORRECT

The clause "or any case ending in the evening or night shift" wrongly implies that all evening and night cases are flagged. They are not. A case fully inside the evening or night shift has overtime = 0.

### Suggested replacement wording

> Overtime was defined per-case using the case's actual room-in time. Each case was assigned to one of three shift buckets — day (08:00-16:30), evening (16:30-22:00), or night (22:00-08:00) — based on its room-in. A case was flagged as after-hours if its room-out time fell after the end of its assigned shift. Overtime minutes equal the time between shift end and room-out, floored at zero. A day-shift case ending at 17:00 has 30 minutes of overtime; an evening-shift case ending at 23:00 has 60 minutes of overtime; a night-shift case ending at 09:00 has 60 minutes of overtime. Cases starting and ending fully within their assigned shift have zero overtime, irrespective of which shift that is.

This definition needs to replace the current Methods paragraph and the corresponding skeleton bullet.

---

## Part 2 — A second methodological inconsistency in the source analysis

The "Mean Overtime" reported in different tables of the in-depth file uses different denominators. This is in the source analysis, not introduced by our paper, but our paper currently reports both numbers without flagging the difference.

### Table 24 (headline)

```r
`Mean Overtime` = round(mean(overtime_minutes[overtime_minutes > 0], na.rm = TRUE), 1)
```

The filter `[overtime_minutes > 0]` restricts the calculation to cases that actually ran overtime. The reported 59 minutes is the mean among the 8,024 overtime cases.

### Table 35 (urgency breakdown)

```r
MeanOvertime = round(mean(overtime_minutes, na.rm = TRUE), 1)
```

No filter. The reported 4.1 minutes (elective) and 10.5 minutes (non-elective) are means across ALL cases in each urgency group, including the cases with zero overtime.

### Why this matters

If you compute the mean overtime per overtime case for each urgency group:
- Elective: 4.1 min × 84,028 cases / 5,859 overtime cases ≈ 58.8 minutes per overtime case
- Non-elective: 10.5 min × 12,016 cases / 2,165 overtime cases ≈ 58.3 minutes per overtime case

When an elective case runs overtime, its average overrun is roughly the same as when an urgent case runs overtime (~58-59 minutes). What differs is how often each group runs overtime (7% vs 18%). Our paper currently writes "with a mean overtime of 10.5 versus 4.1 minutes" in a way that implies urgent cases have longer overruns. That is misleading. The longer 95th percentile (67.2 min vs 18 min) is a more accurate reflection of urgent cases having a heavier tail.

### Suggested correction in the paper

Replace: *"Per case, urgent surgery ran after-hours at more than twice the rate of elective surgery: 18% versus 7%, with a mean overtime of 10.5 versus 4.1 minutes."*

With: *"Per case, urgent surgery ran after-hours at more than twice the rate of elective surgery (18% versus 7%). The 95th percentile of overtime minutes was longer for urgent cases (67.2 versus 18 minutes), suggesting heavier tails. The mean overrun length, conditional on running over, was similar in the two groups (approximately 58 minutes)."*

---

## Part 3 — Overlap definition

### What the R code actually does

Source: `In-Depth_Analysis_Genk.Rmd` lines 1761-1775.

```r
is_overlap <- function(start1, end1, start2, end2) {
  (start1 < end2) & (end1 > start2)
}

ne_cases <- genk %>% filter(grepl("(niet|non)", tolower(UrgencyType))) %>%
  select(NE_ID = PatientID, NE_OR = ActualOR, NE_start = ORIn, NE_end = OROut)

e_cases <- genk %>% filter(!grepl("(niet|non)", tolower(UrgencyType))) %>%
  select(E_ID = PatientID, E_OR = PlannedOR, E_start = PlannedStartDT, E_end = PlannedEndDT)

overlaps <- ne_cases %>%
  inner_join(e_cases, by = c("NE_OR" = "E_OR")) %>%
  filter(is_overlap(NE_start, NE_end, E_start, E_end))
```

Three points worth noting in this definition:

1. **Asymmetry between the two sides.** The non-elective case is described by its ACTUAL room (`ActualOR`) and its ACTUAL time interval (`ORIn` to `OROut`). The elective case is described by its PLANNED room (`PlannedOR`) and its PLANNED time interval (`PlannedStartDT` to `PlannedEndDT`). The match is on the urgent case actually being placed where, and when, the elective case was supposed to be.

2. **Time-interval overlap, not same-day overlap.** The function `is_overlap()` is the standard interval overlap check: two intervals overlap when one starts before the other ends and ends after the other starts. Two cases in the same OR on the same day but at different times of day do NOT count as an overlap.

3. **Day-level metric (the 69.7%).** Table 37 counts the number of distinct calendar days on which at least one such time-interval overlap occurred anywhere in the OR complex. 869 out of 1,247 days = 69.7%.

### What our outline and paper say

**Skeleton:** *"Urgent-elective overlap in the same OR occurred on 869 of 1,247 observation days = 69.7%"*

**Paper draft:** *"Urgent-elective overlap in the same operating room occurred on 869 of 1,247 observation days, or 69.7%. This was daily rather than exceptional."*

### Verdict — Numerically correct, but underspecified

The 69.7% figure is correctly cited. What our paper does not say is what counts as an overlap at the case level. A reviewer reading our Methods will not know that overlap means "an urgent case was actually placed in the room and time interval where an elective case was scheduled" rather than "an urgent case and an elective case happened to share a room on the same day."

### Suggested addition to Methods

> An urgent case was deemed to overlap with an elective case when the urgent case's actual room (`ActualOR`) matched the elective case's planned room (`PlannedOR`) and the urgent case's actual time interval (room-in to room-out) overlapped with the elective case's planned time interval (planned start to planned end). The day-level overlap metric counts the number of distinct calendar days on which at least one such overlap occurred. The case-level metric, used to assess elective start-delay effects, counts whether a given elective case's planned slot was overlapped by the actual operation of an urgent case in the same room.

---

## Part 4 — A few other things the R code clarifies

### The 4,786 shift-displaced cases

Source: `data_cleaning.R` lines 313-321. The flag is `moved_to_other_shift = (planned_shift_label != shift_label)`. Both labels are derived from the same shift bucketer, but applied to `PlannedStartDT` for the planned shift and to `ORIn` for the actual shift. So a case is "displaced" when the shift its actual room-in falls into differs from the shift its planned start time fell into. This matches the PDF text and our paper.

### GO10 specialism

Confirmed cardiac. EDA Table 9 (p.12) shows GO10's six most frequent procedures (each performed >50 times) are all cardiac:
- COR.AORTA BYPASS GRAFT V.
- AORTAKLEP VIA MINI-STERNOTOMIE
- PORT ACCES MITRALISKLEP
- RAL MIDCAB
- THORACOSCOPISCHE ABLATIE MINI MAZE
- MVR

Our paper can therefore state "GO10, which handles complex cardiac surgery" without the "to be confirmed with hospital" caveat. Hospital sign-off is still good practice but the data itself supports the description.

### "GO11 is the urgent intake room"

Source: `In-Depth_Analysis_Genk.Rmd` line 1910 calls GO11 "the emergency-designated room." Our paper's "GO11 is the designated urgent-intake room" is accurate.

### "Median idle time 7 minutes"

Source: `data_cleaning.R` lines 324-353. Idle time is computed only for consecutive cases in the same room within the same gap-shift window, capping any gap > 60 minutes as NA (treated as planned downtime, not idle time). The reported 7-minute median therefore excludes long gaps that might represent block transitions or planned breaks. This is a sensible operational measure but we should mention the 60-min cap if reviewers ask.

---

## Part 5 — Reference verification

Each reference cited in the paper is being checked against PubMed, the publisher, or the issuing body. The check has two parts:
- Does the paper exist with the bibliographic details as cited? (title, authors, journal, year, DOI/PMID)
- Does the specific claim we make match what the paper actually reports?

The verification report follows in `13_reference_verification.md` once the four parallel verification passes complete. Findings will be folded back into this document and into the paper itself.

---

## Summary of recommended edits

1. **Methods §2.4 (overtime definition).** Replace the current wording with the shift-based definition described in Part 1. The "or any case ending in the evening or night shift" clause is wrong as written.

2. **Methods (overlap definition).** Add the case-level overlap definition described in Part 3 so a reviewer can reproduce the 69.7% number.

3. **Results §3.5 (urgent vs elective overtime).** Reframe the "10.5 vs 4.1 min" comparison to make clear these are means across all cases in each group (with zeros), not means among overtime cases. The conditional mean overrun is similar in the two groups.

4. **Results §3.3 (GO10 description).** Drop the "to be confirmed with hospital" language for GO10 = cardiac. The data already support it. Hospital confirmation can still be obtained but does not gate the writing.

5. **Methods (idle-time note).** Mention the 60-minute cap on gap times if a reviewer queries the 7-minute median.
