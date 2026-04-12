# Glossary of terms

Quick reference for all technical terms used in the ZOL OR efficiency paper. Alphabetical order. Each definition is self-contained.

**Admission type (DAG / HOS / SPOED)** — How the patient enters the hospital. DAG (dagopname) means they go home the same day. HOS (hospitalisatie) means they stay overnight or longer. SPOED means emergency admission. In our dataset, Lanaken is 98% DAG while Genk is 58% HOS.

**After-hours / overtime** — Any OR activity that continues past the end of the assigned shift. We define this relative to the shift the case actually started in, not a fixed clock time. So a case starting in the evening shift (16:30-22:00) that runs past 22:00 counts as overtime, even though it started after the standard day.

**Ambulatory surgery / day case** — Surgery where the patient arrives and leaves the same day. No overnight stay. Cataract removal and arthroscopic knee surgery are common examples. Lanaken runs almost entirely on ambulatory cases.

**Benchmarking** — Comparing performance metrics across sites, departments, or hospitals to identify who is doing better or worse. Our paper argues that raw benchmarking without adjusting for operating model is misleading.

**Block time** — A reserved time window in the OR schedule, typically assigned to a specific surgeon or specialty. If a surgeon has a "Tuesday morning block," that OR is theirs from 08:00 to 12:30 whether or not they fill it.

**Case mix** — The composition of procedures a site performs. A hospital doing mostly hip replacements has a different case mix than one doing mostly cataract surgeries. Case mix drives most of the raw performance differences between sites.

**Cascade / cascading delay** — When one surgery starts late, it pushes the next one later, which pushes the one after that later still. By the end of the day, a 10-minute first-case delay can become a 60-minute delay for the last case. Our data shows cascading delays waste about 4 times more OR time than surgeries simply running longer than expected.

**Catheterization lab (Cathlab)** — A specialized procedural suite for heart-related interventions like ablations, stent placements, and valve replacements. Different from a regular OR because the equipment and layout are specific to cardiac work. At ZOL, the Cathlab is physically inside the Genk campus but analyzed separately.

**Coefficient of variation (CV)** — Standard deviation divided by the mean. It tells you how variable something is relative to its average. A CV of 0.3 means the spread is about 30% of the mean. For surgical durations, routine procedures have CVs around 0.3, while highly variable procedures can exceed 1.0.

**Contribution margin** — Revenue from a case minus the variable costs of running it. Higher contribution margin per OR hour means the OR is generating more net revenue. We do not have cost data in our study, so we use minutes as our currency instead.

**Duration deviation (duration_diff)** — Actual duration minus planned duration, in minutes. Positive means the surgery took longer than planned. Negative means it finished early. Across our dataset, about 55-60% of cases finish earlier than planned.

**Elective vs non-elective** — Elective surgery is planned in advance. Non-elective (urgent or emergency) surgery is booked within 24 hours of the procedure. At ZOL, 6.4% of all cases are non-elective. The distinction matters because non-elective cases disrupt the planned schedule.

**First-case-on-time start (FCOTS)** — Whether the first surgery of the day in each room began at its scheduled time. The OR management literature has long considered this the single most important efficiency metric. Our data challenges that view: Genk has the best FCOTS discipline but the worst overtime.

**Gap time / idle time** — Minutes between one patient leaving the OR and the next entering. We cap this at 60 minutes; anything longer is likely a planned break, not inefficiency. Lanaken's median gap time is 0 minutes. Genk's is 7 minutes.

**Inpatient surgery** — Surgery where the patient stays in the hospital at least one night. Typically more complex, longer, and less predictable than ambulatory cases.

**Natural experiment** — A research setting where groups differ because of circumstances, not because a researcher assigned them. Our four ZOL sites share governance but differ in operating model, creating a natural experiment in OR design.

**Operating model** — The structural design of how an OR suite runs. This includes what types of cases it handles, whether it runs on weekends, how many rooms it has, whether rooms are interchangeable, and whether it has emergency capacity. Our paper argues this is the main thing you need to adjust for when benchmarking.

**Overtime flag (afterhours_flag)** — A yes/no indicator: did this case extend past the end of its shift? 1 = yes, 0 = no. Defined relative to the effective shift (based on when the case actually started), not the planned shift.

**Overtime minutes** — How many minutes past the shift end the case actually ran. Calculated as max(0, OROut - shift_end). Never negative by definition.

**Paired-room flex** — Lanaken's system where rooms LP01 and LP02 are fully interchangeable. Cases swap freely between them based on real-time availability. 100% of LP01's room swaps go to LP02 and vice versa. This absorbs scheduling pressure without extending hours.

**Percentage deviation** — (Actual duration - Planned duration) / Planned duration, times 100. Expresses the error as a percentage of the plan. A 30-minute case that takes 39 minutes has a percentage deviation of +30%.

**Planning ratio** — Actual duration divided by planned duration. A ratio of 1.0 means the plan was exactly right. Above 1.0 means the case ran long. Below 1.0 means it finished early.

**Planned afterhours minutes** — How many minutes of a case were already scheduled to run past the shift end. If a case was fully planned within the shift, this is zero. We use this to separate planned overtime (the schedule intended it) from unplanned overtime (the schedule didn't).

**Progressive stratification** — Our method: filter the data step by step to make comparisons fairer. Step 1: weekdays only. Step 2: day shift only. Step 3: elective only. Step 4: split by admission type. At each step, the between-site spread shrinks, revealing how much of the raw gap was structural rather than managerial.

**Relative overtime minutes** — Actual overtime divided by planned afterhours minutes. A value of 1.0 means the case had exactly as much overtime as planned. Above 1.0 means more overtime than expected. Only defined for cases that had planned afterhours activity.

**Room swap** — When a case is performed in a different OR than originally planned. At Lanaken this happens 7.5% of the time (by design, via paired-room flex). At Genk it happens 1.1% of the time.

**Shift** — One of three staffing windows at ZOL. Day shift: 08:00-16:30. Evening shift: 16:30-22:00. Night shift: 22:00-08:00. Each case is assigned to a shift based on when the patient actually entered the OR, not when the case was planned.

**Shift-transition compression** — Our term for a new finding: when a case gets bumped from one shift to another (e.g., from day to evening), it tends to finish faster than planned. At Cathlab, bumped cases finished 88 minutes shorter on average. The mechanism is unclear but may involve behavioral pressure near shift boundaries.

**Start deviation (start_diff)** — The difference between when the patient actually entered the OR and when they were planned to enter, in minutes. Positive = late start. Negative = early start. Across the network, about 60-68% of cases start late.

**Stratification** — Breaking data into subgroups to control for things that might confuse a comparison. If you compare overtime rates between a hospital that does emergencies and one that doesn't, the emergency hospital will always look worse. Stratifying by urgency type removes that confusion.

**Turnover time** — Time from one patient leaving the OR to the next patient entering. Similar to gap time but sometimes defined more narrowly (cleanup + setup only, excluding scheduling gaps). We use gap_time in our analysis.

**Underutilized OR time** — Staffed OR time that goes unused. If a room is staffed until 16:30 but the last case ends at 14:00, those 2.5 hours are underutilized. We focus on overutilized time (overtime) rather than underutilized time in this paper.

**Urgency type** — Whether a case is elective (planned) or non-elective (urgent). At ZOL, non-elective is defined as booked within 24 hours of surgery. Network-wide, 6.4% of cases are non-elective.

**Variance decomposition** — Splitting the total variation in a metric into the part that comes from differences between groups (e.g., between hospitals) and the part from differences within groups (e.g., between rooms inside one hospital). Our key finding is that within-site room-level variation is larger than between-site variation at 2 of 4 campuses.
