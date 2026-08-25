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
