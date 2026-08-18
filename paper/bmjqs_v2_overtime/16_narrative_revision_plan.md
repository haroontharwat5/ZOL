# Narrative revision plan (response to Niels's e-mail + review, v2 → v3)

## 1. Recommendation: adopt Niels's narrative

Reframe the contribution as *showing the potential of data-driven analyses, based on routinely recorded OR data, to support overtime management*, with the ZOL analysis as the case study. Reasons:

1. It converts the paper's two structural weaknesses into features. "We did not fit causal or inferential models" stops being a gap a reviewer pokes at and becomes appropriate scope: a monitoring case study describes and localises, it does not explain. The case-mix statements Niels flagged as overclaiming stop being conclusions and become an example of what monitoring surfaces for management attention: a hypothesis the hospital can now investigate, which is exactly what a dashboard is for.
2. It fits BMJ Quality & Safety better. Their readership is quality-improvement people; "what routine administrative data can tell OR management about overtime, demonstrated in one hospital" is a QI paper. "Descriptive epidemiology of overtime in one hospital" is a harder sell in exactly the ways Niels anticipates.
3. The findings survive intact. Concentration across rooms, the punctuality null result, and the urgent-elective load all remain the evidence; they are now evidence of what the approach reveals rather than freestanding claims.

Cost to accept: the dashboard mock-up becomes a real deliverable (Niels floated it; it strengthens the reframe and can be built entirely from the existing analyses), and the Introduction and Discussion need rewriting rather than editing. Results needs reordering but not new analysis.

## 2. Introduction storyline (per Niels's method: core message per paragraph first, then the build-up)

| ¶ | Core message | Content |
|---|--------------|---------|
| 1 | OR overtime is undesirable, and for patients the evidence links it to real harm | Define overtime immediately at first use (work continuing past the rostered shift end, in line with the staff-overtime literature). Then the patient side, integrated rather than listed: after-hours operating carries higher adjusted mortality risk (meta-analysis), higher morbidity with handovers and transfusions as part of the mechanism, and each intra-operative handover raises complication risk. Two or three sentences, not seven studies in sequence. |
| 2 | For staff, overtime erodes wellbeing and retention | Nurse workforce evidence: overtime linked to worse perceived quality and safety, burnout, intent to leave. Fatigue evidence (HSSIB/MDU) closes the loop back to patients. |
| 3 | Managing overtime requires knowing where and why it occurs in your own department, and aggregate numbers do not tell you | Standard theatre metrics mislead when aggregated (capped utilisation; site-level scoring; unreliable metrics in isolation). What overtime means operationally also differs between hospitals depending on staffing structure, so the site's own pattern is what management needs. |
| 4 | The data to answer this already exist: hospitals record it during day-to-day operations | Secondary use of administrative OR data can support overtime management without new data collection. Gap: prior work treats overtime as a site aggregate or a cost parameter; there is little demonstration of what routine data can reveal about overtime at the level where scheduling decisions are made. |
| 5 | This paper is a case study of that approach | One sentence of hospital context (Belgian tertiary centre, 18 ORs, steep staffing step-down at shift end) so the RQs do not arrive out of the blue. RQ1: how is overtime distributed across rooms and time. RQ2: which operational factors are associated with it. Contribution: demonstrating the potential (and limits) of data-driven overtime analysis for OR management, illustrated with a monitoring-dashboard mock-up. |

Cuts from the current intro: the overtime-taxonomy sentence ("can refer to several distinct phenomena", Niels: "will only lead to confusion"), the "broader programme" sentence (Niels: "not relevant"), and the block-time glossary contrast moves to Methods where the operationalisation lives.

## 3. Drafted Introduction (v3, for discussion)

Citations are given as author names; bracket numbers get assigned after the structure is agreed, since the citation order changes.

> Operating-room (OR) overtime, surgery that continues past the end of the rostered shift, is common in practice and undesirable in principle. For patients, the concern is that care delivered after hours is riskier care. A meta-analysis of night and after-hours surgery found higher adjusted mortality (OR 1.16, 95% CI 1.06 to 1.28, low-certainty evidence) [Cortegiani], and a multicentre cohort of over 350,000 non-cardiac cases linked night surgery to higher morbidity, partly through more transfusions and more provider handovers during the case [Althoff]. Handovers matter in their own right: the incidence of major complications rises from 8.8% with no intraoperative anaesthesia transitions to 21.2% with four or more [Saager]. A case that crosses the shift boundary is finished by a team that did not start it, at an hour when the hospital runs on reduced staffing.
>
> For staff, the costs of overtime accumulate more quietly. In a twelve-country European survey, nurses working overtime reported poorer quality of care and worse patient safety on their units [Griffiths], and the same programme of work tied long shifts to burnout and intention to leave [Dall'Ora]. Mandatory overtime predicted intention to leave in Korean acute-care hospitals [Bae]. Fatigue closes the circle back to patients: in a survey cited by the UK national investigation into staff fatigue, 22% of doctors felt sleep-deprived daily and 35% said tiredness had impaired their ability to treat patients [HSSIB].
>
> A hospital that wants to reduce overtime first has to know where it occurs, and the numbers usually available to management do not say. Site-level utilisation figures aggregate away the variation between rooms, and the aggregation itself can mislead: NHS England's capped-utilisation metric discards operating time that runs past the scheduled finish, so the theatres with the worst overruns can look acceptable [Zhang, Dunstan and Pandit]. Standard theatre metrics are unreliable in isolation more generally [Charlesworth and Pandit], and established efficiency scoring operates at the level of the whole OR suite [Macario]. What overtime means also depends on local staffing structure: in a hospital that steps staffing down sharply at the end of the day shift, a case running fifteen minutes past the boundary has different consequences than in one with overlapping shifts. Overtime management therefore needs the hospital's own pattern, at the level where scheduling decisions are made.
>
> The data required for this already exist. ORs log room entry and exit times, planned durations, and urgency classifications as part of routine operations, and this administrative record can be analysed without any new data collection. Prior work has used such data mainly to estimate cost parameters or site-level averages; what routine data can reveal about the structure of overtime within a single department has received little attention.
>
> This paper presents a case study of that approach at a Belgian tertiary centre with 18 surgical ORs and a steep staffing step-down at each shift end. Using three and a half years of administrative data, we ask two questions. First, how is overtime distributed across rooms and time (RQ1)? Second, which operational factors, duration overruns, urgent-elective interaction, and start-time punctuality, are associated with it (RQ2)? The aim is to show what data-driven analysis of routinely recorded OR data can contribute to overtime management, and where its limits lie.

(≈430 words against the current intro's ≈600, which also answers the "laundry list" comment: Oh/Sakurai, Meewisse, Pittman, Koch, Joseph, Dall'Ora 2016/2020 move to the Discussion or drop to supplementary Table S1.)

## 4. Results transformation (Niels: "make explicit which conclusion we draw and how it relates to overtime")

Pattern for every subsection: numbers first, then one sentence of interpretation that names overtime. Worked example, inter-case idle time:

Current ending: *"Inter-case turnover was therefore not identified as an independent contributor to room-level overtime."*

Revised ending: *"For overtime management, this means faster turnover is unlikely to reduce overtime at this site: rooms did not run late because they idled between cases, and the one room where idle time and overtime were both high is the room whose complex cases require long changeovers."*

Also in Results:
- Move the Sample overview paragraph and Table 1 to Methods (Niels; he expects "general overtime statistics" to open Results instead — the current RQ1 opening paragraph already is that, so this is mostly a lift-and-shift).
- Delete the two passages Niels marked as repetition of Methods.
- Define room swap at first mention; re-explain 9.7%/32.9% where reused in the Discussion.
- Table cull: Niels says one table can go, Maxim suggests appendix. Candidate: Table 2B (year trend, four rows, fully stated in text). Confirm with Niels which one he meant.

## 5. Discussion reframe

Structure under the new narrative:
1. What the case study showed (restate findings with the percentages re-explained).
2. What this means for data-driven overtime management: monitoring at room level changes the intervention question; punctuality dashboards would target the wrong thing at this site; urgent-elective load is quantifiable from routine data alone.
3. What monitoring cannot do: it localises, it does not explain. The concentration in OR10 is *consistent with* a case-mix account, which is a hypothesis these data cannot test — this is where the current "case-mix complexity most likely accounts for..." claims get softened to Niels's comfort level.
4. Dashboard implication: the analyses map onto a monitoring instrument (mock-up figure).
5. Limitations, rewritten for the case-study narrative: single site is inherent to a case study; what generalises is the approach, not the numbers; room-in/room-out only; no outcome linkage.

## 6. Title options (new narrative)

1. "Using routinely collected data to support operating-room overtime management: a single-centre case study"
2. "Data-driven monitoring of operating-room overtime: a case study in a tertiary hospital"
3. "What routine operating-room data reveal about overtime: a single-centre case study"

## 7. Quick wins from the comment digest to fold into the same revision

- Data availability sentence: use Niels's wording (dataset cannot be made public, consistent with contractual agreements with the hospital).
- Add to Methods: schedules are constructed such that no overtime occurs if all cases run as planned (confirm with Ben/Dieter that this is true).
- Define "case" at first use; clarify "hospital-wide" as OR-department-wide.
- "underutilised time" cost logic: one clause explaining that staffed-but-unused time still costs wages, which is why its cost is nonzero and why overutilised time costs about double.
- Replace "associated with" in Key Messages where no test backs it ("was concentrated in", "occurred alongside").
- Drop OR14 from the abstract's concentration sentence or reword ("rates ranged from 3.5% to 32.9% across rooms").
- Reference renumbering: redo after the restructure settles (citation order changes); the Vancouver script run is mechanical.

## 8. Dashboard mock-up

Can be built from existing outputs, no new analysis: room-level overtime ranking (Figure 1 content), trend tile (Table 2B content), boundary-completion histogram (Figure S1), urgent-elective overlap counter, and a punctuality tile deliberately marked as "not predictive of overtime at this site". One figure, presented as an illustration of how the analyses become a management instrument.
