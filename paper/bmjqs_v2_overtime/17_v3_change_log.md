# v3 change log with evidence basis

Standing rule (Haroon, 25 Aug): every clarification, rewording, and adjustment must be traceable to evidence, literature, or facts — no unsourced assumptions. Evidence sources: (a) verified verbatim quotes in `submission/reference_quote_verification.md`, (b) hospital facts confirmed by the ZOL clinical team, (c) arithmetic on our own reported results. Each entry below names its basis.

## Locked decisions

### 1. Narrative (approved 25 Aug)
Adopt Niels's framing: contribution = showing the potential of data-driven analyses of routinely recorded OR data for overtime management; ZOL analysis is the case study; dashboard mock-up as illustration. Basis: Niels's e-mail; resolves his overclaim and "why no inferential models" objections structurally.

### 2. Title (approved)
"Data-driven monitoring of operating-room overtime: a single-centre retrospective study."
Note: "monitoring" is supported by the planned dashboard mock-up figure; revisit if the mock-up is dropped.

### 3. Abstract (locked)
- "hospital-wide aggregate" → "one number for the whole OR department". Basis: the cited prior work operates at OR-suite/department level (Macario: eight indicators scored for the OR suite, verified via citing sources; Zhang 2024: capped theatre utilisation reported per trust theatre department, verified quote). No source reports OR overtime for a hospital beyond the OR. Confirms Niels's reading; sweep later occurrences to match.
- OR14 removed from abstract; spread carried by the range "3.5% to 32.9%", only the top room characterised ("ran overtime on a third of its cases"). Basis: our Table/Figure 1 results. The heuristics-mislead point (OR14 starts late most, least overtime) stays in Results where the punctuality null is reported.
- 68.8% urgent-elective overlap sentence REMOVED from the abstract. Basis for removal: the link from elective start displacement to overtime is unmeasured in our data, and the cross-room punctuality null (Spearman rho = −0.29, p = 0.24) undercuts the displacement→overtime mechanism as a general rule. Finding stays in Results as a disruption observation with an explicit "overtime link untested" sentence, and in Discussion as a monitoring-surfaced item for investigation.
- Conclusions rewritten so every clause is a measured fact: concentration (room range), urgent 2× boundary-crossing rate (18.2% vs 8.3%), punctuality null. "Driven by case-mix complexity" and "accompanied by urgent-case disruption" removed from conclusions. Basis: Niels's overclaim comments; our own results tables.
- Optional reinstatement path (not yet requested): compute overtime on overlap vs non-overlap days from the xlsx data; if it shows a difference, the disruption finding returns with a measured link.

### 4. Key messages (locked)
- Underutilised-time cost clause: "staffing is planned in advance, so underutilised time is paid staff time that goes unused, and overutilised time costs roughly twice as much again." Basis: verified Wachtel & Dexter 2010 abstract: "OR managers must plan staffing in the face of uncertain demand... Planning too much staffing results in underutilized OR time. Planning too little staffing causes overutilized time, which is approximately twice as expensive as underutilized time." An earlier draft clause attributing the asymmetry to "premium pay" was dropped: mechanism not verbatim-verified.
- "factors most visibly associated with room-level overtime" → descriptive wording. "Associated" retained only where tested (punctuality, idle time: Spearman). Case-mix clause becomes observational: "The highest-overtime rooms were those handling long, complex procedures" (basis: our Results, procedure types per room from hospital records). Basis for the change: Niels's comment that "associated with" requires statistical tests.

## Traceability flags (claims needing care)

- Macario 2006 has no published abstract; the "suite-level scoring" characterisation is verified via citing sources only. Verify the exact indicator wording against the full PDF before quoting it directly.
- "The schedule is built such that no overtime occurs if all cases run as planned" (Niels wants this in Methods): NOT yet confirmed — requires Ben/Dieter confirmation before it enters the text.
- Pandit 2012 "7,096 lists": abstract says "more than 7000"; exact figure needs full-text check or use "more than 7,000".

## 5. Code and data audit (25 Aug, data + Rmds shared by Haroon)

Independent Python verification against genk_cleaned.xlsx (79,352 rows), cross-checked against Maxim's R console output in the previous-version Google Doc. Verification script: `verification/verify_results_numbers.py` (code in repo; data not in repo).

**Confirmed exactly:** all headline overtime stats; full 18-room table; start-delay stats; punctuality Spearman (rho −0.2920537, p 0.2388 — matches Maxim's R to 7 decimals); idle summary; swaps; urgency table incl. the Table 3A all-cases means (5.0/10.7); overlap 858/1,247 = 68.8%; OR11 475 events/15.2%. Stored overtime flag is 100% internally consistent, and an independent reconstruction matches it on 100.0000% of cases.

**Corrections applied to the manuscript:**
1. **Shift boundary:** day-shift assignment starts at room-in 07:30, not 08:00 (6,163 cases enter 07:30–07:59 and carry the day label). Methods now state room-in windows and shift ends explicitly. Rationale for 07:30 NOT yet confirmed clinically — ask Ben/Dieter (or check data_cleaning.R) before adding a "why".
2. **Idle-time correlation:** rho corrected to 0.91 (overtime rate over all cases per room, consistent with room rates reported elsewhere; Maxim's 0.89 used the gap-defined subset — both reproduced). The claim "Excluding OR10, the pattern did not hold" was never computed in any shared code and is false (excl GO10: rho 0.90/0.87, p < 10⁻⁵ in all variants); it originated as prose in an earlier draft ("idle time is not the bottleneck" notes tab). Replaced with the computed result: the association persists without OR10; idle time is now reported as a positive room-level association, interpreted as a plausible case-mix marker, causality untested. Abstract, Key Messages, Discussion opening, and Conclusion updated accordingly. **Confirm with Maxim which rate denominator to keep (0.91 recommended; his 0.89 equally defensible if the subset is described).**
3. **Overlap wording:** comparison is case-level (overlapped vs non-overlapped elective cases), not day-level; "median ≈30 minutes" was OR11's median gap (60 vs 28); "reaching 60 minutes in early 2022" was the monthly means trend (~70 vs ~30). Results now report each correctly; OR11 identified as the emergency-designated room (per In-Depth Rmd).
4. **Methods additions:** idle-time measurement rules (day shift; includes shift-start-to-first-case gap; excludes gaps > 60 min); overlap flag definition.

**v3 locked-section updates:** abstract Results sentence now "Start-time punctuality showed no association with room-level overtime, whereas rooms with longer gaps between cases also had higher overtime rates."; Key Messages adjusted to match.

## 6. data_cleaning.R audit (25 Aug, shared by Haroon)

Resolves ask-list Q2. The base shift boundaries ARE hospital policy at 08:00/16:30/22:00 (code comment: "op basis van beleid"). The 07:30 pattern is a deliberate reclassification ("Herclassificeer vroege starters"): cases entering 07:30-08:00 whose room-out falls after 08:00 are assigned to the day shift (6,153 cases; the 10 early entrants ending before 08:00 stay night). Methods rewritten accordingly; the earlier "07:30 assignment boundary" description was an approximation.

Second code-vs-prose fix: gap_time excludes the first case of each shift window (lag = NA), contradicting the Rmd prose "delay between shift start and the first case"; and it is computed within all three shift windows, not day-only. Methods corrected (code is ground truth). gap_time cutoff 60 min confirmed in data_cleaning.R (the quality-check variant uses 120 min and is not the shipped dataset).

Remaining Ben/Dieter questions: (1) zero-overtime-by-design schedule claim; (3) does anaesthesia also change at shift boundaries; (4) weekend staffing boundaries.
