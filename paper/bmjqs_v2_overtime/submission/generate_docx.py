#!/usr/bin/env python3
"""Generate BMJ-formatted Word document from manuscript markdown."""

import re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

doc = Document()

# --- Page setup: 2.5 cm margins ---
for section in doc.sections:
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

# --- Default font ---
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
font.color.rgb = RGBColor(0, 0, 0)
pf = style.paragraph_format
pf.space_after = Pt(0)
pf.space_before = Pt(0)
pf.line_spacing = Pt(24)  # double spacing
pf.alignment = WD_ALIGN_PARAGRAPH.LEFT


def add_paragraph(text, bold=False, italic=False, font_size=12, space_after=0,
                  space_before=0, alignment=WD_ALIGN_PARAGRAPH.LEFT, style_name='Normal'):
    p = doc.add_paragraph(style=style_name)
    p.alignment = alignment
    pf = p.paragraph_format
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(space_before)
    pf.line_spacing = Pt(24)
    add_formatted_runs(p, text, bold=bold, italic=italic, font_size=font_size)
    return p


def add_formatted_runs(paragraph, text, bold=False, italic=False, font_size=12):
    """Parse text for [N] references (make superscript), **bold**, and *italic* markers."""
    parts = re.split(r'(\*\*.*?\*\*|\*[^*]+?\*|\[\d+(?:[,––-]\d+)*\])', text)
    for part in parts:
        if not part:
            continue
        if part.startswith('**') and part.endswith('**'):
            inner = part[2:-2]
            run = paragraph.add_run(inner)
            run.bold = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(font_size)
        elif part.startswith('*') and part.endswith('*') and not part.startswith('**'):
            inner = part[1:-1]
            run = paragraph.add_run(inner)
            run.italic = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(font_size)
        elif re.match(r'^\[\d+(?:[,–—–-]\d+)*\]$', part):
            ref_text = part[1:-1]
            run = paragraph.add_run(ref_text)
            run.font.superscript = True
            run.font.name = 'Times New Roman'
            run.font.size = Pt(font_size)
        else:
            run = paragraph.add_run(part)
            run.bold = bold
            run.italic = italic
            run.font.name = 'Times New Roman'
            run.font.size = Pt(font_size)


def add_heading_caps(text, space_before=12):
    """BMJ Level 1: BOLD CAPS"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(6)
    pf.line_spacing = Pt(24)
    run = p.add_run(text.upper())
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p


def add_heading_lower(text, space_before=12):
    """BMJ Level 2: bold lower case"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(6)
    pf.line_spacing = Pt(24)
    run = p.add_run(text)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p


# ============================================================
# TITLE PAGE
# ============================================================
title_text = 'Where does operating-room overtime come from? A retrospective single-centre study'
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
pf = p.paragraph_format
pf.space_after = Pt(12)
pf.line_spacing = Pt(24)
run = p.add_run(title_text)
run.bold = True
run.font.name = 'Times New Roman'
run.font.size = Pt(14)

add_paragraph('Maxim Riebus, Haroon Tharwat, Niels Martin, Ben Van Bylen, Dieter Mesotten',
              space_after=6)
add_paragraph('[Affiliations]', space_after=6)
add_paragraph('**Correspondence:** [corresponding author details]', space_after=6)
add_paragraph('**Word count:** ~2,800 (body text)', space_after=6)
add_paragraph('**Keywords:** operating room, overtime, scheduling, patient safety, staff wellbeing, quality improvement',
              space_after=12)

# ============================================================
# ABSTRACT
# ============================================================
add_heading_caps('Abstract', space_before=18)

abstract_parts = [
    ('Background.', ' Operating-room overtime exposes patients and staff to increased risks, but how overtime distributes within a hospital and which operational factors are associated with it is not well characterised.'),
    ('Objective.', ' To characterise operating-room overtime within a high-volume tertiary hospital: its distribution across rooms and the operational factors associated with it.'),
    ('Design and setting.', ' Retrospective observational study of administrative data from a 24/7 tertiary hospital in Belgium running 18 surgical operating rooms.'),
    ('Participants.', ' 79,352 surgical procedures performed between January 2022 and May 2025.'),
    ('Main outcome measures.', ' Case-level overtime (time past the assigned shift end), by room, weekday, shift, and urgency. Start-time deviation, duration-estimation accuracy, shift displacement, and unplanned urgent-case disruption of the elective programme as candidate contributing factors.'),
    ('Results.', ' 7,729 cases (9.7%) ran past the end of their assigned shift, with a mean overtime of 60.3 minutes and a 95th percentile of 197 minutes. Overtime concentrated in a small number of rooms: OR10 ran overtime on 32.9% of its cases (mean 154 minutes), while OR14 ran overtime on 3.5%. Urgent cases ran after-hours at more than twice the elective rate (18.2% versus 8.3%). Unplanned urgent-case disruption of the elective programme occurred on 68.8% of observation days and was associated with a median difference of approximately 30 minutes in elective start times. First-case punctuality and inter-case idle time showed no consistent association with room-level overtime.'),
    ('Conclusions.', ' At this tertiary hospital, overtime concentrated in a small number of rooms, with case-mix complexity and unplanned urgent-case disruption of the elective programme as the most visible associated factors. Room-level overtime monitoring and scheduling that accounts for urgent-case flow are more practical targets for quality improvement than first-case punctuality alone.'),
]

for label, content in abstract_parts:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.space_after = Pt(3)
    pf.line_spacing = Pt(24)
    run = p.add_run(label)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run = p.add_run(content)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)

# ============================================================
# KEY MESSAGES
# ============================================================
add_heading_caps('Key messages', space_before=18)

add_paragraph('**What is already known on this topic**', space_after=3)
add_paragraph('• Operating-room overtime increases staffing costs and is associated with poorer patient and staff outcomes.', space_after=2)
add_paragraph('• Most hospitals monitor overtime at the aggregate hospital or site level.', space_after=2)
add_paragraph('• First-case punctuality is widely promoted as a lever for reducing end-of-day overruns.', space_after=6)

add_paragraph('**What this study adds**', space_after=3)
add_paragraph('• Within a single hospital, room-level overtime rates ranged from 3.5% to 32.9%, a ten-fold spread hidden by aggregate metrics.', space_after=2)
add_paragraph('• Unplanned urgent-case disruption of the elective programme occurred on more than two-thirds of observation days and was associated with delayed elective start times.', space_after=2)
add_paragraph('• First-case punctuality showed no consistent association with room-level overtime, suggesting it may not be an effective intervention target in all settings.', space_after=6)

# ============================================================
# INTRODUCTION
# ============================================================
add_heading_caps('Introduction', space_before=18)

intro_paras = [
    'Operating-room (OR) overtime can refer to several distinct phenomena: a procedure running longer than its estimated duration, a case finishing after its planned end time, or a case extending past a staffing-shift boundary and requiring a personnel handover during or after the procedure. These definitions capture different problems — planning accuracy, schedule adherence, and workforce exposure — and the choice of definition shapes what is measured and what intervention follows. In this study, we define overtime as a case whose room-out time falls after the end of its assigned staffing shift, because the nursing handover at each shift boundary is the operational event that makes overtime consequential. Overutilised time is approximately twice as expensive as underutilised time,[1] but overtime is more than a budget problem.',

    'On the patient side, after-hours surgery carries elevated mortality. A meta-analysis reported an adjusted odds ratio of 1.16 (95% CI 1.06 to 1.28), based on low-certainty evidence.[2] A propensity-matched cohort of 281,717 South Korean patients reported a larger effect (odds ratio 3.58), although that estimate has been challenged on residual-confounding grounds.[3,4] Each intraoperative anaesthesia handover raises the odds of a major composite complication, with incidence rising from 8.8% at zero transitions to 21.2% at four or more.[5] At the study hospital, anaesthesiologists are not subject to shift-based handovers; they remain with the case until it is complete. The nursing team, however, changes at each shift boundary regardless of whether a procedure is in progress. A 2025 UK national patient-safety investigation reported that 22% of surveyed doctors experienced daily sleep deprivation and 35% said tiredness had impaired their ability to treat patients.[6] Overtime above a breakpoint threshold has been associated with a 2.09% increase in hospital-acquired pressure ulcers — skin injuries that develop during prolonged immobility — across 70 US hospitals.[7] In a multicentre cohort of more than 350,000 non-cardiac surgical cases, night surgery was associated with increased morbidity (adjusted odds ratio 1.41), mediated partly by higher blood-transfusion rates and provider handovers during the case.[8]',

    'On the staff side, overtime and long shifts are associated with poorer perceived care quality and higher patient-safety risk in a 12-country European nurse workforce study.[9] The companion study linked 12-hour shifts to burnout and intent to leave.[10] Mandatory overtime was significantly associated with intent to leave in a 2024 cross-sectional study of 264 South Korean nurses.[11] Both long shifts and overtime are associated with worse performance and wellbeing,[12] and high workload combined with low decision latitude is an established burnout predictor.[13]',

    'The severity of these consequences depends on what happens at the shift boundary. At the study hospital, 25 rooms (18 surgical, 7 interventional) are staffed during the 08:00 to 16:30 day shift, with 2 to 3 nurses per room. At 16:30, capacity drops to 8 rooms. At 17:30, it drops to 4. Overnight, a single room remains staffed. A case running past the shift boundary competes for a diminishing set of staffed rooms. The nursing team hands over at the boundary regardless of whether a procedure is in progress; surgeons and anaesthesiologists remain with the case until completion.',

    'Workflow disruptions in the OR cluster and escalate,[14] and a systematic review estimated that approximately 20% of operating time involves disruptions, although evidence for direct effects on patient outcomes remains mixed.[15] Prior work on OR overtime has largely treated it as an aggregate site-level number.[16,17] Whether overtime concentrates in specific rooms, and which operational factors are associated with it, has received less attention. Without that granularity, quality improvement efforts risk targeting the wrong intervention point.',

    'This study is part of a broader quality-improvement effort at a Belgian tertiary hospital. The present analysis characterises scheduled-versus-observed performance from administrative data. We address two questions:',
]
for para in intro_paras:
    add_paragraph(para, space_after=6)

numbered_qs = [
    '1. How is overtime distributed across rooms and time within one tertiary hospital?',
    '2. Which operational factors — including duration overruns, shift displacement, unplanned urgent-case disruption of the elective programme, and first-case punctuality — are associated with overtime?',
]
for q in numbered_qs:
    add_paragraph(q, space_after=3)

add_paragraph('The first question examines whether overtime is a diffuse hospital-wide problem or whether it concentrates in specific rooms. The second asks which candidate mechanisms identified in the literature are visible in our data, to inform where interventions should be directed.', space_after=6, space_before=3)

# ============================================================
# METHODS
# ============================================================
add_heading_caps('Methods', space_before=18)

add_heading_lower('Setting')
add_paragraph('The study hospital is a 24/7 tertiary centre in Belgium performing more than 22,000 surgical procedures per year. It operates 18 surgical theatres and 7 interventional theatres. The surgical staff includes 195 surgeons and 207 anaesthesiologists (including trainees and fellows), covering all surgery except congenital cardiac and organ transplantation. During the day shift, 2 to 3 nurses staff each room. At 16:30, the number of staffed rooms drops from 25 to 8; at 17:30, to 4; overnight, a single room remains staffed.', space_after=6)

add_heading_lower('Data and inclusion')
add_paragraph('We used administrative OR data from 1 January 2022 to 31 May 2025, covering 79,352 cases in the 18 surgical operating rooms, involving 60,895 unique patients and 1,276 distinct procedure types. By admission type, 42.3% of cases were ambulatory and 57.7% inpatient (this classification reflects the admission pathway and does not correspond to the elective/non-elective urgency split reported below). The urgency mix was 85.4% elective and 14.6% non-elective. Annual volume grew from 22,133 cases in 2022 to 23,738 in 2024, with 9,906 recorded through May 2025. Room-in and room-out times are the only time markers confirmed as reliable by the hospital\'s clinical team; all timing analyses use these two time points.', space_after=6)

add_heading_lower('Definitions')
add_paragraph('Each case was assigned to a shift based on its actual room-in time: day (08:00 to 16:30), evening (16:30 to 22:00), or night (22:00 to 08:00). A case was flagged as overtime if its room-out fell after the end of its assigned shift. Overtime minutes equal the positive difference between room-out and shift end. This operationalises the conceptual definition stated in the Introduction and aligns with the framework in Bauer et al.[18]', space_after=6)
add_paragraph('An unplanned urgent case was deemed to disrupt the elective programme when the urgent case\'s actual room matched the elective case\'s planned room and their time intervals (actual for urgent, planned for elective) overlapped.', space_after=6)

add_heading_lower('Variables')
add_paragraph('We followed the glossary of Bauer et al.[18] Variable definitions include planned and observed duration, planning deviation, start-time deviation, overtime flag and minutes, room-swap flag, urgency (elective versus non-elective), and shift label. We chose room-level overtime as the primary metric rather than aggregate utilisation, which can mask room-level operational problems.[16,19]', space_after=6)

add_heading_lower('Analyses')
add_paragraph('Analyses are primarily descriptive; we did not fit causal or multivariable models. For RQ1 (distribution), we computed overtime rate, mean, median, and 95th percentile, stratified by room, weekday, year, and shift. For RQ2 (contributing factors), we assessed duration deviation by planned-duration bucket using coefficients of variation,[20,21] shift displacement (cases performed in a different shift than planned), urgency mix and timing, unplanned urgent-case disruption per day and per room, first-case start-time deviation per room, inter-case idle time, and room swaps. To test whether first-case punctuality and inter-case idle time were associated with room-level overtime rates, we computed Spearman rank correlations across the 18 rooms. This study is reported following the STROBE guidelines for observational studies.', space_after=6)

add_heading_lower('Ethics')
add_paragraph('This study used fully anonymised administrative data with institutional approval. No patient interaction occurred.', space_after=6)

# ============================================================
# RESULTS
# ============================================================
add_heading_caps('Results', space_before=18)

add_heading_lower('Overtime burden and room-level concentration (RQ1)')
add_paragraph('Of 79,352 cases, 7,729 (9.7%) ran past the end of their assigned shift. Among overtime cases, the mean was 60.3 minutes, the median 39, and the 95th percentile 197 (Table 1). Weekday rates were similar (8.8 to 9.9%) but roughly 1.7 times higher on weekends (Saturday 16.8%, Sunday 15.5%), when volume is almost entirely non-elective. The year-on-year trend showed gradual improvement: 10.0% in 2022, 10.0% in 2023, 9.7% in 2024, and 8.6% in the partial 2025 data.', space_after=6)

add_paragraph('[Table 1. Overtime summary by weekday and year. Cases, overtime count, overtime percentage, and mean overtime minutes by weekday (Monday-Sunday) and year (2022-2025).]', italic=True, space_after=6, space_before=6)

add_paragraph('Room-level overtime rates ranged from 3.5% to 32.9% across the 18 rooms (Figure 1). OR10, which handles complex cardiac surgery (CABG, aortic valve replacement, mitral valve repair), ran overtime on 32.9% of its 1,743 cases, with a mean of 154 minutes and a 95th percentile of 328 minutes. A second tier (OR08 through OR13) clustered at 11 to 16%. At the other end, OR14 ran 3.5% across 6,885 cases and OR01 ran 5.8% across 6,577. The within-hospital spread (nearly ten-fold) exceeded the between-campus spread across the hospital network (0.5 to 9.7%).', space_after=6)

add_paragraph('[Insert Figure 1 about here]', italic=True, space_after=6, space_before=6)

add_paragraph('Most overtime cases ended shortly after the shift boundary. The majority of completions fell in the 16:30 to 17:30 window, when staffing had dropped from 25 to 8 rooms. The distribution decayed through the evening, with a thin tail past 22:00 (Supplementary Figure S1).', space_after=6)

add_heading_lower('Contributing factors (RQ2)')

add_paragraph('*Planning accuracy.* Across all 79,352 cases (not only those with overtime), 45.7% ran longer than planned and 54.3% ran shorter. The mean overrun was 22.6 minutes (median 14); the mean underrun was 21.2 minutes (median 12). On average, the planning system was roughly unbiased. The problem was dispersion. The coefficient of variation of observed duration was lowest for mid-length cases (0.35 to 0.36 for 61 to 180 minutes), moderate for short cases (0.61 for under 30 minutes), and intermediate for very long cases (0.42 for over 180 minutes). Planning-deviation CV was more extreme: the over-180-minute bucket had a CV of 1.86, meaning the standard deviation of the planning error was nearly twice the mean — an indication that duration estimates for the longest cases are unreliable (Supplementary Table S1). The procedures with the largest absolute deviations — complex cardiac and oncology cases — were concentrated in the rooms with the highest overtime.', space_after=6)

add_paragraph('*Shift displacement.* A total of 4,151 cases (5.2%) were performed in a different shift than originally planned. These cases started on average 398 minutes later than planned (roughly six and a half hours) and took 22.3 minutes less than planned. Whether displacement contributed to overtime or resulted from it cannot be determined from these data.', space_after=6)

add_paragraph('*Unplanned urgent-case disruption.* Urgent cases constituted 14.6% of volume (11,616 of 79,352). Per case, urgent surgery ran after-hours at more than twice the elective rate (18.2% versus 8.3%, Table 2), with heavier tails (P95 69 versus 29 minutes). Because elective cases outnumbered urgent cases nearly six to one, the absolute volume of after-hours minutes was still dominated by the elective programme.', space_after=6)

add_paragraph('Unplanned urgent-case disruption of the elective programme occurred on 858 of 1,247 observation days (68.8%). On days with disruption, elective cases started approximately 30 minutes later than on days without, a gap that reached 60 minutes in early 2022 before narrowing. OR11 absorbed the highest disruption burden, with 475 events affecting 15.2% of its elective cases (Supplementary Table S2).', space_after=6)

add_paragraph('[Table 2. Urgent versus elective overtime and urgent-case disruption. Panel A: volume, after-hours rate, mean overtime, and P95 overtime by urgency. Panel B: disruption frequency (858/1,247 days = 68.8%), mean start-delay effect (+30 min), and OR11 burden.]', italic=True, space_after=6, space_before=6)

add_paragraph('*First-case punctuality.* Room swaps affected 0.7% of cases (519 of 79,352). Swapped cases had a higher overtime rate (14.8% versus 9.7%), but whether swaps contribute to or result from overtime cannot be determined.', space_after=6)

add_paragraph('First-case punctuality showed no significant correlation with room-level overtime (Spearman rho = −0.29, p = 0.24). OR10 had the best punctuality (46.1% late) yet the worst overtime (32.9%). OR14 had the second-worst punctuality (78.7% late) yet the lowest overtime (3.5%). OR11 had the worst punctuality (82.4% late) yet mid-pack overtime (11.7%). This is consistent with Pandit et al., who reported R-squared values of 0.04 to 0.08 between start and finish times across more than 7,000 theatre lists.[23]', space_after=6)

add_paragraph('*Inter-case idle time.* Mean idle time between consecutive same-room cases had a median of 8 minutes and a mean of 9.9 minutes, with a 95th percentile of 25 minutes; turnover was not a bottleneck.[22] The Spearman correlation between mean inter-case idle time and overtime rate across the 18 rooms was 0.89 (p < 0.001). This association was driven almost entirely by OR10, which combined high idle time with high overtime. After excluding OR10, the pattern did not hold. The high idle time in OR10 most likely reflects complex cardiac cases with long setup and preparation rather than avoidable turnover delay; idle time in this context is a marker of case-mix complexity, not an independent contributor to overtime.', space_after=6)

# ============================================================
# DISCUSSION
# ============================================================
add_heading_caps('Discussion', space_before=18)

add_heading_lower('Concentration, not prevalence')
add_paragraph('A hospital-wide overtime rate of 9.7% is unremarkable. The distribution, however, is strikingly uneven. OR10 ran overtime in one of every three cases; OR14, in the same hospital, ran 3.5%. The ten-fold within-hospital spread was wider than the between-campus spread across the hospital network (0.5 to 9.7%). Hospital-wide targets such as “reduce overtime by 10%” will not reach the problem unless decomposed by room. Zhang, Dunstan, and Pandit made the same point: aggregate metrics hide room-level operational reality.[16] Valid room-level metrics are a prerequisite for quality improvement.[24]', space_after=6)

add_heading_lower('Factors associated with overtime')
add_paragraph('The procedures with the largest planning deviations and the highest planned durations — complex cardiac and oncology cases — clustered in the rooms with the highest overtime. This concentration suggests that case-mix complexity, rather than scheduling inefficiency alone, explains much of the room-level variation. Wachtel and Dexter showed in a large operational dataset that cumulative delay grows as duration uncertainty accumulates through the day.[26] Fugener et al. documented systematic biases in surgeons\' duration estimates — planning fallacy, anchoring — that compound across a list.[27] Both findings are consistent with the pattern observed here: high-complexity rooms generate more overtime because their cases carry wider duration uncertainty.', space_after=6)

add_paragraph('Unplanned urgent-case disruption of the elective programme occurred on more than two-thirds of observation days and was associated with a median difference of approximately 30 minutes in elective start times. This makes urgent arrivals a routine scheduling factor rather than an exception. The study hospital already designates rooms for urgent cases, yet disruption still occurred on the majority of days, suggesting that current allocation does not fully absorb urgent-case demand. Additional scheduling buffers or capacity reallocation may be needed.', space_after=6)

add_paragraph('The conventional view holds that first-case punctuality drives end-of-day performance, with each minute of late start carrying a marginal cost.[25] In our data, the Spearman correlation between first-case late-start rate and room-level overtime rate was −0.29 (p = 0.24), indicating no significant association. The room with the best start-time punctuality had the worst overtime, while a room with among the worst punctuality had the lowest. Pandit et al. reported a similar disconnect.[23] This does not prove that first-case punctuality is unrelated to overtime — case-mix complexity may explain the apparent dissociation — but it does suggest that the relationship is not straightforward and that first-case punctuality may not be an effective intervention target in all settings.', space_after=6)

add_heading_lower('Implications')
add_paragraph('The overtime documented here is operationally comparable to the exposure that other studies have linked to staff fatigue, elevated after-hours mortality, and increased complication risk.[2–13] Whether these harms are present in this cohort cannot be determined from administrative data alone; direct measurement of patient and staff outcomes associated with room-level overtime remains an important next step for future research. At a hospital where 25 staffed rooms drop to 8, then 4, then 1, each case past the shift boundary lands in a setting with fewer staff and more handovers. Room-level monitoring — decomposing aggregate metrics into per-room overtime rates — is a practical first step toward identifying where interventions would have the greatest effect.', space_after=6)

add_heading_lower('Limitations')
add_paragraph('This study has several limitations. It is a single-site retrospective analysis, so whether the concentration pattern holds in hospitals with different staffing models is unknown. We do not measure patient or staff outcomes directly; the harm argument rests on published literature, not on complications or burnout scores from this cohort. OR10 handles complex cardiac surgery, and its high overtime may partly reflect irreducible procedural duration rather than schedulable inefficiency; we describe this but cannot adjust for it without procedure-level risk scores. The link between after-hours surgery and patient harm rests on observational mortality studies whose effect sizes range widely (adjusted odds ratio 1.16[2] to 3.58[3]) and whose estimates have been questioned on residual-confounding grounds.[4] Readers should weigh the after-hours mortality evidence with this uncertainty in mind.', space_after=6)

# ============================================================
# CONCLUSION
# ============================================================
add_heading_caps('Conclusion', space_before=18)
add_paragraph('Operating-room overtime at this tertiary hospital concentrated in a small number of rooms, with case-mix complexity and unplanned urgent-case disruption of the elective programme as the most visible associated factors. First-case punctuality showed no significant correlation with room-level overtime (Spearman rho = −0.29, p = 0.24), and the association between inter-case idle time and overtime was driven by a single high-complexity room. The findings support room-level rather than hospital-level overtime monitoring and scheduling interventions that account for urgent-case flow.', space_after=6)

# ============================================================
# END MATTER
# ============================================================
add_heading_caps('Acknowledgements', space_before=18)
add_paragraph('[To be completed]', space_after=6)

add_heading_caps('Competing interests', space_before=12)
add_paragraph('None declared.', space_after=6)

add_heading_caps('Funding', space_before=12)
add_paragraph('[To be completed]', space_after=6)

add_heading_caps('Data availability', space_before=12)
add_paragraph('The dataset contains anonymised administrative hospital data. Requests for access should be directed to the hospital\'s research office.', space_after=6)

add_heading_caps('Patient and public involvement', space_before=12)
add_paragraph('Given the retrospective use of fully anonymised administrative data, no patient or public involvement in the design, conduct, or reporting of this study was applicable.', space_after=6)

# ============================================================
# REFERENCES
# ============================================================
add_heading_caps('References', space_before=18)

references = [
    'Wachtel RE, Dexter F. Review of behavioral operations experimental studies of newsvendor problems for operating room management. Anesth Analg 2010;110(6):1698-1710.',
    'Cortegiani A, Ippolito M, Misseri G, et al. Association between night/after-hours surgery and mortality: a systematic review and meta-analysis. Br J Anaesth 2020;124(5):623-37.',
    'Oh T-K, Song I-A. Outcomes of after-hours surgeries performed under general anaesthesia: a South Korean nationwide cohort study. Anaesthesia 2025. DOI: 10.1111/anae.16559.',
    'Sakurai T. Assessing the influence of after-hours surgery: concerns with the confounders and conclusion. Anaesthesia 2025. DOI: 10.1111/anae.16591.',
    'Saager L, Hesler BD, You J, et al. Intraoperative transitions of anesthesia care and postoperative adverse outcomes. Anesthesiology 2014;121(4):695-706.',
    'Health Services Safety Investigations Body (HSSIB). The impact of staff fatigue on patient safety. Investigation report. London: HSSIB, 2025.',
    'Pittman P, Tiunn H-L, et al. Increased utilization of overtime and agency nurses and patient safety. JAMA Netw Open 2025. PMID: 40172888.',
    'Althoff FC, Wachtendorf LJ, Rostin P, et al. Effects of night surgery on postoperative mortality and morbidity: a multicentre cohort study. BMJ Qual Saf 2021;30(8):678-688.',
    'Griffiths P, Dall\'Ora C, Simon M, et al. Nurses\' shift length and overtime working in 12 European countries: the association with perceived quality of care and patient safety. Med Care 2014;52(11):975-81.',
    'Dall\'Ora C, Griffiths P, Ball J, et al. Association of 12 h shifts and nurses\' job satisfaction, burnout and intention to leave: findings from a cross-sectional study of 12 European countries. BMJ Open 2015;5(9):e008331.',
    'Bae S-H. Nurse staffing, work hours, mandatory overtime, and turnover in acute care hospitals affect nurse job satisfaction, intent to leave, and burnout: a cross-sectional study. Int J Public Health 2024;69:1607068.',
    'Dall\'Ora C, Ball J, Recio-Saucedo A, Griffiths P. Characteristics of shift work and their impact on employee performance and wellbeing: a literature review. Int J Nurs Stud 2016;57:12-27.',
    'Dall\'Ora C, Ball J, Reinius M, Griffiths P. Burnout in nursing: a theoretical review. Hum Resour Health 2020;18:41.',
    'Joseph A, Khoshkenar A, Taaffe KM, et al. Minor flow disruptions, traffic-related factors and their effect on major flow disruptions in the operating room. BMJ Qual Saf 2019;28(4):276-83.',
    'Koch A, Burns J, Catchpole K, Weigl M. Associations of workflow disruptions in the operating room with surgical outcomes: a systematic review and narrative synthesis. BMJ Qual Saf 2020;29(12):1033-1045.',
    'Zhang C, Dunstan C, Pandit JJ. A tutorial on “capped utilisation” as a metric and key performance target in NHS England\'s Model Hospital operating theatres database: caution for international healthcare systems. Anesthesiol Perioper Sci 2024. DOI: 10.1007/s44254-024-00073-3.',
    'Macario A. Are your hospital operating rooms “efficient”? A scoring system with eight performance indicators. Anesthesiology 2006;105(2):237-40.',
    'Bauer M, Diemer M, Merkel M, et al. Glossary of perioperative process times and indicators. Anaesthesist 2020;69(Suppl 1):S5-17.',
    'Schouten AEM, Flipse SM, van Nieuwenhuizen KE, et al. Operating room performance optimization metrics: a systematic review. J Med Syst 2023;47(1):19.',
    'Strum DP, May JH, Vargas LG. Modeling the uncertainty of surgical procedure times: comparison of log-normal and normal models. Anesthesiology 2000;92(4):1160-7.',
    'Eijkemans MJ, van Houdenhoven M, Nguyen T, et al. Predicting the unpredictable: a new prediction model for operating room times using individual surgeon-specific historical data. Anesthesiology 2010;112(1):41-9.',
    'MacMillan L, et al. What affects operating room turnover time? A systematic review and mapping of the evidence. Surgery 2025. PMID: 40054053.',
    'Pandit JJ, Abbott T, Pandit M, et al. Is “starting on time” useful (or useless) as a surrogate measure for “surgical theatre efficiency”? Anaesthesia 2012;67(8):823-32.',
    'Zhang C, Pandit JJ. Getting operating theatre metrics right to underpin quality improvement. Br J Anaesth 2023;131(1):130-4.',
    'Dexter F, Epstein RH. Typical savings from each minute reduction in tardy first case of the day starts. Anesth Analg 2009;108(4):1262-7.',
    'Wachtel RE, Dexter F. Influence of the operating room schedule on tardiness from scheduled start times. Anesth Analg 2009;108(6):1889-1901.',
    'Fugener A, Schiffels S, Kolisch R. Overutilization and underutilization of operating rooms: insights from behavioral health care operations management. Health Care Manag Sci 2017;20(1):115-28.',
]

for i, ref in enumerate(references, 1):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.space_after = Pt(2)
    pf.line_spacing = Pt(24)
    run = p.add_run(f'{i}. ')
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run = p.add_run(ref)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)

# ============================================================
# FIGURE LEGENDS
# ============================================================
add_heading_caps('Figure legends', space_before=18)

fig_legends = [
    ('Figure 1.', ' Room-level overtime concentration. Horizontal bar chart with one bar per operating room, ordered descending by overtime rate. A secondary panel shows mean overtime minutes per room. OR10 (32.9%) and OR14 (3.5%) anchor the extremes. Overall: 7,729 of 79,352 cases (9.7%), mean 60.3 min, median 39 min, P95 197 min.'),
]

for label, text in fig_legends:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.space_after = Pt(6)
    pf.line_spacing = Pt(24)
    run = p.add_run(label)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)

# Save
output_path = '/home/user/ZOL/paper/bmjqs_v2_overtime/submission/manuscript.docx'
doc.save(output_path)
print(f'Saved to {output_path}')
