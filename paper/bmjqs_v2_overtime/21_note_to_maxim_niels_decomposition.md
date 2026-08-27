# Draft note to Maxim and Niels — scheduled-crossing decomposition

(To send from Haroon; edit freely.)

---

Hi Maxim, hi Niels,

While working through the review comments, Niels's question "is it stated somewhere that the schedule is composed so that no overtime would happen if everything runs as planned?" prompted us to check this in the data rather than assume it. The answer changes part of our story, and I want your view before anything enters the manuscript.

The check uses two variables our own cleaning script already builds (PlannedEndDT vs planned_shift_end; data_cleaning.R also computes planned_afterhours_minutes, which none of our reports ever used). The finding:

- 5,812 cases (7.3% of 79,352; 6.4% of electives) were already PLANNED to end past their shift boundary. This is not marginal squeezing: median 40 planned minutes over, and a third are planned more than an hour over. Almost all are day-programme bookings past 16:30.
- Of the 7,729 overtime cases, 3,532 (45.7%) were these scheduled crossings. They run heavier than unplanned overruns (mean 82 vs 42 overtime minutes) and carry 62.1% of all overtime minutes.
- Overtime risk is visible at planning time: 5.7% of cases planned to fit ran overtime, versus 60.8% of cases planned to cross.
- OR10, our highest-overtime room, books 31.6% of its cases past the boundary; 81.5% of its overtime cases were scheduled crossings. Its overtime is mostly written into the schedule, not lost during execution.

What we think this means for the paper, pending your view:
1. The overtime definition stays as it is (crossing the boundary carries the same staffing exposure either way), but RQ1 gains a decomposition: scheduled crossings vs unplanned overruns.
2. The RQ2 analyses (planning accuracy, punctuality, gaps) become explanations of the unplanned component; the scheduled component is a capacity/rostering question.
3. This strengthens the data-driven monitoring narrative: the routine record distinguishes the two kinds per room, and they have different remedies.
4. One question for Ben and Dieter: is booking past the shift end deliberate use of the evening staffing tier (8 rooms remain staffed after 16:30), and is its scale known to them?

Maxim, could you reproduce the numbers in R? Starting from genk_cleaned.xlsx:

    genk %>%
      mutate(planned_over = PlannedEndDT > planned_shift_end) %>%
      summarise(n = sum(planned_over, na.rm = TRUE),
                pct = mean(planned_over, na.rm = TRUE))          # 5812, 7.3%

    genk %>% filter(afterhours_flag == 1) %>%
      group_by(planned_over = PlannedEndDT > planned_shift_end) %>%
      summarise(n = n(), mean_ot = mean(overtime_minutes),
                total_min = sum(overtime_minutes))
    # FALSE: 4197, ~42 min ; TRUE: 3532, ~82 min (62.1% of minutes)

    genk %>% filter(afterhours_flag == 1, ActualOR == "GO10") %>%
      summarise(sched_share = mean(PlannedEndDT > planned_shift_end))   # 0.815

Nothing goes into the manuscript before you have both confirmed. If you agree it belongs, I will draft the Results subsection and the adjusted abstract sentences for review.

Best,
Haroon
