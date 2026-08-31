# Meeting brief — Haroon + Maxim (27 Aug)

Purpose: align on (1) verification results, (2) the scheduled-crossing finding, (3) the analysis decisions that are ours to make before involving Niels. Niels's comments are handled separately (triage below): only ~7 of 63 depend on what we decide here.

## 1. Where the revision stands

- Narrative: adopting Niels's data-driven-monitoring framing (his e-mail proposal). Title updated: "Data-driven monitoring of operating-room overtime: a single-centre retrospective study."
- Abstract, Key Messages, Introduction: rewritten and internally locked (tracking file: 20_v3_assembled_draft.md).
- Methods: rewritten (definitions inline, terminology passage, shift rule per data_cleaning.R, idle/overlap definitions per code).
- Results/Discussion: comment fixes drafted; assembly awaiting the decisions below.
- Every number in the manuscript reproduced independently from genk_cleaned.xlsx; your two Spearman outputs reproduced to 7 decimals (verification/verify_results_numbers.py — runs in one command).

## 2. Two corrections found during verification (already applied)

1. "Excluding OR10, the pattern did not hold" (idle time) was never computed anywhere and the data refute it: rho = 0.90 without GO10 (p < 1e-5). Rewritten: gap-overtime association is robust; idle time is now a positive finding, plausibly a case-mix marker.
2. The Methods said day shift 08:00-16:30; data_cleaning.R reclassifies 07:30-08:00 entrants that cross 08:00 into the day shift (6,153 cases). Methods now describe the actual rule.

## 3. The scheduled-crossing finding (new; needs your reproduction + sign-off)

Trigger: Niels asked whether schedules are composed so that no overtime occurs if all runs as planned. Checked in data (PlannedEndDT vs planned_shift_end - variables your cleaning script builds; never analysed in any report):

| Funnel | n |
|---|---|
| All cases | 79,352 |
| Planned to cross the boundary | 5,812 (7.3%; electives 6.4%; median 40 min over, P95 246; 4,921 are day bookings past 16:30) |
| ...of which actually crossed | 3,532 (60.8%) |
| Actual overtime cases | 7,729 = 3,532 scheduled (45.7%) + 4,197 unplanned (54.3%) |

- Scheduled crossings carry 62.1% of all overtime minutes (mean 82 vs 42 min).
- Overtime risk visible at planning time: 5.7% (planned to fit) vs 60.8% (planned to cross).
- GO10: 31.6% of cases booked past the boundary; 81.5% of its overtime cases were scheduled crossings.

R reproduction snippets: 21_note_to_maxim_niels_decomposition.md.

Proposed consequences (our recommendation, for Niels after we align):
- Definition unchanged (boundary-crossing = same staffing exposure either way).
- RQ1 gains the decomposition as a headline; RQ2 analyses interpreted as explaining the unplanned component.
- Answers Niels's case-mix objection with a booking fact instead of an inference.
- Compiled Ben/Dieter question: is booking past the boundary deliberate use of the evening tier?

## 4. Decisions for this meeting (ours to make)

1. Reproduce the decomposition in R - does it hold for you?
2. Idle correlation to report: 0.91 (per-room overtime rate over all cases, consistent with Figure 1 rates) vs your 0.89 (gap-defined subset). Recommendation: 0.91.
3. Concentration shares: OR10 = 19.0% of all overtime minutes from 2.2% of cases; top three rooms 36.4%. Newly computed; include?
4. Per-room decomposition (scheduled vs unplanned rate per room) - compute and make Figure 1 a stacked bar?
5. RQ2 correlations: keep total-overtime versions as primary (recommendation), optionally add unplanned-scoped sensitivity?
6. Optional: compute overtime for overlapped vs non-overlapped elective cases (would settle Niels's "conclusion on overtime?" for the overlap section with a measured link).
7. Room swaps: recommend removing the subsection (not an RQ2 factor; direction undeterminable; no swap-cause field).

## 5. Niels-comment triage (all 63)

- RESOLVED, decomposition-independent: ~48 - includes the full Introduction storyline set, abstract clarity set, terminology/definition set, both table caption/footnote repairs, idle correction, punctuality rewrites, data availability wording, PPI answer, derived-variable explanations.
- RESOLVABLE TODAY, independent: ~8 - Discussion clarity items (9.7% re-explanation, "both observations" referent, FCOTS logic, QI-metrics sentence), Limitations rewrite, figure-legend check.
- ENTANGLED with this meeting's decisions: ~7 - zero-overtime comment (answered by finding), case-mix comments (better answered by finding), "bold statements"/limitations-narrative pair, RQ1 subsection text, abstract/key-message amendments.

## 6. Compiled Ben/Dieter list (ask once, when we are ready)

1. Is booking past the shift end deliberate use of the evening staffing tier, and is its scale known?
2. Does anaesthesia change over at shift boundaries, or only nursing?
3. Does weekend staffing follow the same shift boundaries?
