#!/usr/bin/env python3
"""Generate BMJ-formatted Word document from manuscript markdown."""

import re
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn

FIGURES_DIR = '/home/user/ZOL/paper/bmjqs_v2_overtime/figures'

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
    parts = re.split(r'(\*\*.*?\*\*|\*[^*]+?\*|\[\d+(?:,\d+)*\])', text)
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
        elif re.match(r'^\[\d+(?:,\d+)*\]$', part):
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


def add_image(filename, width_inches=6.0, caption_text=None, caption_label=None):
    """Insert a centered image with an optional bold caption."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(12)
    pf.space_after = Pt(6)
    pf.line_spacing = Pt(14)
    run = p.add_run()
    run.add_picture(f'{FIGURES_DIR}/{filename}', width=Inches(width_inches))
    if caption_text is not None:
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
        cpf = cap.paragraph_format
        cpf.space_after = Pt(12)
        cpf.line_spacing = Pt(14)
        if caption_label:
            rl = cap.add_run(caption_label)
            rl.bold = True
            rl.font.name = 'Times New Roman'
            rl.font.size = Pt(11)
        rt = cap.add_run(' ' + caption_text)
        rt.font.name = 'Times New Roman'
        rt.font.size = Pt(11)


def add_table(headers, rows, header_color='2171b5', bold_last_row=False,
              col_widths_inches=None, caption_label=None, caption_text=None):
    """Insert a native Word table with a colored header row and an optional caption.

    headers: list of column header strings
    rows: list of row lists (strings)
    """
    if caption_label:
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
        cpf = cap.paragraph_format
        cpf.space_before = Pt(12)
        cpf.space_after = Pt(4)
        cpf.line_spacing = Pt(14)
        rl = cap.add_run(caption_label)
        rl.bold = True
        rl.font.name = 'Times New Roman'
        rl.font.size = Pt(11)
        if caption_text:
            rt = cap.add_run(' ' + caption_text)
            rt.font.name = 'Times New Roman'
            rt.font.size = Pt(11)

    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.style = 'Light Grid Accent 1'

    # Header row
    for j, h in enumerate(headers):
        cell = table.rows[0].cells[j]
        cell.text = ''
        para = cell.paragraphs[0]
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = para.add_run(h)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shading = f'<w:shd {{}} w:fill="{header_color}"/>'.format
        from docx.oxml import OxmlElement
        tcPr = cell._tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), header_color)
        tcPr.append(shd)

    # Data rows
    for i, row in enumerate(rows, start=1):
        is_bold = bold_last_row and i == len(rows)
        for j, val in enumerate(row):
            cell = table.rows[i].cells[j]
            cell.text = ''
            para = cell.paragraphs[0]
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = para.add_run(str(val))
            run.bold = is_bold
            run.font.name = 'Times New Roman'
            run.font.size = Pt(10)
            if is_bold:
                tcPr = cell._tc.get_or_add_tcPr()
                from docx.oxml import OxmlElement
                shd = OxmlElement('w:shd')
                shd.set(qn('w:val'), 'clear')
                shd.set(qn('w:color'), 'auto')
                shd.set(qn('w:fill'), 'DEEBF7')
                tcPr.append(shd)

    # Column widths
    if col_widths_inches:
        for j, w in enumerate(col_widths_inches):
            for row in table.rows:
                row.cells[j].width = Inches(w)

    # Spacing after table
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(6)
    spacer.paragraph_format.line_spacing = Pt(14)


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
title_text = 'Where does operating-room overtime come from? A retrospective single-center study'
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
pf = p.paragraph_format
pf.space_after = Pt(12)
pf.line_spacing = Pt(24)
run = p.add_run(title_text)
run.bold = True
run.font.name = 'Times New Roman'
run.font.size = Pt(14)

add_paragraph('Haroon Tharwat, Maxim Riebus, [Ben surname], [Dieter surname], Niels Martin',
              space_after=6)
add_paragraph('[Affiliations]', space_after=6)
add_paragraph('**Correspondence:** [corresponding author details]', space_after=6)
add_paragraph('**Word count:** ~3,400 (body text)', space_after=6)
add_paragraph('**Keywords:** operating room, overtime, scheduling, patient safety, staff wellbeing, quality improvement',
              space_after=12)

# ============================================================
# ABSTRACT
# ============================================================
add_heading_caps('Abstract', space_before=18)

abstract_parts = [
    ('Objective.', ' To characterize operating-room overtime within a high-volume tertiary hospital: its distribution across rooms and the operational factors associated with it.'),
    ('Design.', ' Retrospective observational study of administrative operating-room data.'),
    ('Setting.', ' A 24/7 tertiary hospital in Belgium running 18 surgical operating rooms.'),
    ('Participants.', ' 79,352 surgical procedures performed between January 2022 and May 2025.'),
    ('Main outcome measures.', ' Case-level overtime (time past the assigned shift end), by room, weekday, shift, and urgency. Start-time deviation, duration-estimation accuracy, and urgent-elective overlap as candidate contributing factors.'),
    ('Results.', ' 7,729 cases (9.7%) ran past the end of their assigned shift, with a mean overtime of 60.3 minutes and a 95th percentile of 197 minutes. Overtime concentrated in a small number of rooms: OR10 ran overtime on 32.9% of its cases (mean 154 minutes), while OR14 ran overtime on 3.5%. Urgent cases ran after-hours at more than twice the elective rate (18.2% versus 8.3%). Urgent-elective overlap in the same room occurred on 68.8% of observation days and added roughly 30 minutes to elective start times. First-case punctuality and inter-case idle time showed no consistent association with room-level overtime.'),
    ('Conclusions.', ' At this tertiary hospital, overtime concentrated in a small number of rooms, with case-mix complexity and urgent-elective overlap as the most visible associated factors. Room-level overtime monitoring and scheduling that accounts for urgent-case flow are more practical targets for quality improvement than first-case punctuality alone.'),
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
# INTRODUCTION
# ============================================================
add_heading_caps('Introduction', space_before=18)

intro_paras = [
    'Operating rooms are among the most resource-intensive units in a hospital, and their schedules rarely match what is planned. Overtime in this setting can refer to several distinct phenomena: an individual case running longer than its booked duration, an operating list ending after its scheduled close, or surgery continuing into a period when fewer staff are rostered. These are different operational events with different consequences. The glossary of Bauer et al. defines overtime in relation to the staffing window: time spent operating beyond the end of the assigned shift.[18] We adopt this shift-based definition because the staffing change at each boundary is the operational event that gives overtime its meaning. Overutilized time is approximately twice as expensive as underutilized time,[1] but overtime is more than a budget problem.',

    'After-hours surgery has been linked to elevated patient mortality. A meta-analysis reported an adjusted odds ratio of 1.16 (95% CI 1.06 to 1.28), based on low-certainty evidence.[7] A propensity-matched cohort of 281,717 South Korean patients reported a larger effect (odds ratio 3.58), although that estimate has been challenged on residual-confounding grounds.[8,9] In a multicenter cohort of more than 350,000 non-cardiac surgical cases, night surgery was associated with increased morbidity (adjusted odds ratio 1.41), mediated partly by higher transfusion rates and provider handovers during the case.[13] Each intraoperative anesthesia handover raises the odds of a major composite complication, with incidence rising from 8.8% at zero transitions to 21.2% at four or more.[10] A 2025 UK national patient-safety investigation reported that 22% of surveyed doctors experienced daily sleep deprivation and 35% said tiredness had impaired their ability to treat patients.[11] Overtime above a breakpoint threshold has been associated with a 2.09% increase in pressure ulcers across 70 US hospitals.[12]',

    'The same exposure carries documented consequences for staff. A 12-country European nurse workforce study linked overtime and long shifts to poorer perceived care quality and higher patient-safety risk.[2] The companion study tied 12-hour shifts to burnout and intent to leave.[3] Mandatory overtime was associated with intent to leave in a 2024 cross-sectional study of 264 South Korean nurses.[4] Both long shifts and overtime are associated with worse performance and wellbeing,[5] and the combination of high workload and low decision latitude is an established burnout predictor.[6]',

    'The severity of these consequences depends on what happens at the shift boundary. In hospitals that step staffing down sharply at the end of the day shift, a case running past the boundary competes for a diminishing set of staffed rooms, often covered by different personnel from those who started the case.',

    'Prior work on OR overtime has largely treated it as an aggregate site-level number,[16,17] and OR workflow disruptions are known to cluster and escalate.[14,15] Whether overtime concentrates in specific rooms within one hospital, and which operational factors are associated with it, has received less attention. Without that granularity, quality improvement efforts risk targeting the wrong intervention point.',

    'This study is part of a multi-phase program at a Belgian tertiary hospital to improve OR performance. Phase 1 characterizes scheduled-versus-observed performance from administrative data. Phase 2 will link the operational patterns to patient outcomes. Phase 3 will build predictive scheduling tools. In this Phase 1 analysis, we address two questions:',
]
for para in intro_paras:
    add_paragraph(para, space_after=6)

numbered_qs = [
    '1. **How is overtime distributed across rooms and time within one tertiary hospital?** This examines whether overtime is a diffuse hospital-wide problem or concentrates in specific rooms, since the appropriate intervention point depends on that distribution.',
    '2. **Which operational factors (duration overruns, urgent-elective interaction, and first-case punctuality) are associated with overtime?** This tests which candidate factors identified in the literature are visible in our data, to inform where scheduling interventions should be directed.',
]
for q in numbered_qs:
    add_paragraph(q, space_after=3)

# ============================================================
# METHODS
# ============================================================
add_heading_caps('Methods', space_before=18)

add_heading_lower('Setting and data')
add_paragraph('The study hospital is a 24/7 tertiary center in Belgium performing more than 22,000 surgical procedures per year. It operates 18 surgical operating rooms and 7 interventional operating rooms. The surgical staff includes 195 surgeons and 207 anesthesiologists (including trainees and fellows), covering all surgery except congenital cardiac and organ transplantation. Nursing staffing runs 2 to 3 per room during the 08:00 to 16:30 day shift; at 16:30 the number of staffed rooms drops to 8, at 17:30 to 4, and overnight a single room remains staffed.', space_after=6)
add_paragraph('We used administrative OR data from 1 January 2022 to 31 May 2025, covering 79,352 cases in the 18 surgical operating rooms, 60,895 unique patients, and 1,276 distinct procedure types. The admission mix was 42.3% ambulatory and 57.7% inpatient. Room-in and room-out times are the only time markers confirmed as reliable by the hospital\'s clinical team; all timing analyses use these two time points. Following the glossary of Bauer et al.,[18] the extracted variables include planned and observed duration, planning deviation, start-time deviation, overtime flag and overtime minutes, room-swap flag, urgency (elective versus non-elective), and shift label.', space_after=6)

add_heading_lower('Overtime definition and analyses')
add_paragraph('Each case was assigned to a shift based on its actual room-in time: day (08:00 to 16:30), evening (16:30 to 22:00), or night (22:00 to 08:00). A case was flagged as overtime if its room-out fell after the end of its assigned shift; overtime minutes equal the positive difference between room-out and shift end. We chose this shift-based definition because the staffing change at each boundary is the operational event that makes overtime consequential at this site, and because it aligns with Bauer et al.[18] Room-level overtime, rather than aggregate utilization, was used as the primary metric, since aggregate measures can mask room-level operational problems.[16,19]', space_after=6)
add_paragraph('All analyses are descriptive; we did not fit causal or inferential models. For RQ1, we computed overtime rate, mean, median, and 95th percentile, stratified by room, weekday, year, and shift. For RQ2, we examined duration deviation by planned-duration bucket using coefficients of variation,[20,21] urgency mix and timing, urgent-elective interaction (defined and reported in Results), first-case start-time deviation per room, inter-case idle time, and room swaps. Intermediate findings were reviewed with the clinical team and used to refine variable definitions and exclusions. The study is reported following the STROBE guidelines for observational studies.', space_after=6)

add_heading_lower('Ethics')
add_paragraph('This study used fully de-identified administrative data with institutional approval. No patient interaction occurred.', space_after=6)

# ============================================================
# RESULTS
# ============================================================
add_heading_caps('Results', space_before=18)

add_heading_lower('Sample overview')
add_paragraph('The cohort comprised 79,352 cases across 18 surgical operating rooms, involving 60,895 unique patients, 195 surgeons, and 207 anesthesiologists performing 1,276 distinct procedure types. Weekday volume was evenly distributed (17.9 to 20.0% Monday through Friday); weekends accounted for 1.8 to 2.1%. Year-on-year volume grew from 22,133 in 2022 to 23,738 in 2024, with 9,906 recorded through May 2025. The urgency mix was 85.4% elective and 14.6% non-elective.', space_after=6)

add_heading_lower('Overtime burden and room-level concentration (RQ1)')
add_paragraph('Of 79,352 cases, 7,729 (9.7%) ran past the end of their assigned shift. Among overtime cases, the mean was 60.3 minutes, the median 39, and the 95th percentile 197 (Table 1). Weekday rates were similar (8.8 to 9.9%) but roughly 1.7 times higher on weekends (Saturday 16.8%, Sunday 15.5%), when volume is almost entirely non-elective. The year-on-year trend showed gradual improvement: 10.0% in 2022, 10.0% in 2023, 9.7% in 2024, and 8.6% in the partial 2025 data.', space_after=6)

add_table(
    headers=['Day', 'n cases', 'n overtime', 'OT rate (%)', 'Mean OT (min)'],
    rows=[
        ['Monday',    '14,232', '1,395',  '9.8',  '58.5'],
        ['Tuesday',   '14,750', '1,416',  '9.6',  '60.1'],
        ['Wednesday', '15,814', '1,502',  '9.5',  '59.7'],
        ['Thursday',  '15,844', '1,394',  '8.8',  '60.5'],
        ['Friday',    '15,615', '1,546',  '9.9',  '62.4'],
        ['Saturday',   '1,654',   '278', '16.8',  '63.4'],
        ['Sunday',     '1,443',   '224', '15.5',  '59.1'],
        ['Total',     '79,352', '7,729',  '9.7',  '60.3'],
    ],
    bold_last_row=True,
    caption_label='Table 1A.',
    caption_text='Overtime by weekday.',
)
add_table(
    headers=['Year', 'OT rate (%)', 'Mean OT (min)', 'Median OT (min)'],
    rows=[
        ['2022',  '10.0', '61.8', '40'],
        ['2023',  '10.0', '58.8', '38'],
        ['2024',   '9.7', '61.3', '39'],
        ['2025*',  '8.6', '58.2', '37'],
    ],
    caption_label='Table 1B.',
    caption_text='Overtime trend by year. * 2025 partial (Jan–May).',
)

add_paragraph('Room-level overtime rates ranged from 3.5% to 32.9% across the 18 rooms (Figure 1). OR10, which handles complex cardiac surgery (CABG, aortic valve replacement, mitral valve repair), ran overtime on 32.9% of its 1,743 cases, with a mean of 154 minutes and a 95th percentile of 328 minutes. A second tier (OR08 through OR13) clustered at 11 to 16%. At the other end, OR14 ran 3.5% across 6,885 cases and OR01 ran 5.8% across 6,577. Rates therefore spanned nearly an order of magnitude across rooms in the same hospital.', space_after=6)

add_image(
    'fig2_room_overtime.png',
    width_inches=6.3,
    caption_label='Figure 1.',
    caption_text='Room-level overtime concentration. Panel A: percentage of cases with overtime per operating room, ordered ascending. Panel B: mean overtime duration per room (minutes). Overall: 7,729 of 79,352 cases (9.7%), mean 60.3 min, median 39 min, P95 197 min.',
)

add_paragraph('Most overtime cases ended shortly after the shift boundary. The majority of completions fell in the 16:30 to 17:30 window, right after the day-shift handover when most of the rooms had already closed. The distribution decayed through the evening, with a thin tail past 22:00 (Supplementary Figure S1).', space_after=6)

add_heading_lower('Contributing factors (RQ2)')

add_paragraph('*Planning accuracy.* Of all cases, 45.7% ran longer than planned and 54.3% ran shorter. The mean overrun was 22.6 minutes (median 14); the mean underrun was 21.2 minutes (median 12). On average, the planning system was roughly unbiased. The problem was dispersion. The coefficient of variation of observed duration was lowest for mid-length cases (0.35 to 0.36 for 61 to 180 minutes), moderate for short cases (0.61 for under 30 minutes), and intermediate for very long cases (0.42 for over 180 minutes). Planning-deviation CV was more extreme: the over-180-minute bucket had a CV of 1.86 (Supplementary Table S1). The procedures with the largest absolute deviations (complex cardiac and oncology cases) were concentrated in the rooms with the highest overtime.', space_after=6)

add_paragraph('*Urgent-elective interaction.* Urgent cases constituted 14.6% of volume (11,616 of 79,352). Per case, urgent surgery ran past the shift boundary at more than twice the elective rate (18.2% versus 8.3%, Table 2), with heavier tails (P95 69 versus 29 minutes). Because elective cases outnumbered urgent cases nearly six to one, the absolute volume of overtime minutes was still dominated by the elective program.', space_after=6)

add_paragraph('To assess whether urgent cases disrupt the elective program, we counted days on which an urgent case ran in a room while an elective case had been planned in the same room over an overlapping time window (urgent case\'s actual room and room-in to room-out interval matched the elective case\'s planned room and planned start-to-end interval). Such overlap occurred on 858 of 1,247 observation days (68.8%). On days with overlap, elective cases started roughly 30 minutes later than on days without, a gap that reached 60 minutes in early 2022 before narrowing. OR11 absorbed the highest overlap burden, with 475 events affecting 15.2% of its elective cases (Supplementary Table S2).', space_after=6)

add_table(
    headers=['Urgency', 'n', 'Share', 'After-hours n', 'After-hours rate', 'Mean OT (min)', 'P95 OT (min)'],
    rows=[
        ['Elective',     '67,736', '85.4%', '5,620',  '8.3%',  '5',    '29'],
        ['Non-elective', '11,616', '14.6%', '2,109', '18.2%', '10.7',  '69'],
        ['Total',        '79,352', '100%',  '7,729',  '9.7%', '–',    '–'],
    ],
    bold_last_row=True,
    caption_label='Table 2A.',
    caption_text='Volume and overtime by urgency.',
)
add_table(
    headers=['Metric', 'Value'],
    rows=[
        ['Days with at least one urgent–elective overlap', '858 of 1,247 (68.8%)'],
        ['Highest-burden room (OR11)',                     '475 events; 15.2% of OR11 elective cases'],
        ['Median start delay at OR11 (no overlap)',        '28 min'],
        ['Median start delay at OR11 (overlap)',           '60 min'],
    ],
    caption_label='Table 2B.',
    caption_text='Urgent–elective overlap in the same room.',
)

add_paragraph('*Factors not associated with overtime.* Inter-case idle time had a median of 8 minutes and a mean of 9.9 minutes, with a 95th percentile of 25 minutes; turnover was not the bottleneck.[22]', space_after=6)

add_paragraph('First-case punctuality showed no consistent association with room-level overtime. OR10 had the lowest late-start rate (46.1% of first cases late) yet the highest overtime (32.9% of cases past the shift boundary). OR14 had a substantially higher late-start rate (78.7%) yet the lowest overtime (3.5%), and OR11 had the highest late-start rate (82.4%) with mid-pack overtime (11.7%). This is consistent with Pandit et al., who reported R-squared values of 0.04 to 0.08 between start and finish times across more than 7,000 operating room lists.[23]', space_after=6)

# ============================================================
# DISCUSSION
# ============================================================
add_heading_caps('Discussion', space_before=18)

add_paragraph('In this single-center analysis of 79,352 cases, overtime was not a diffuse hospital-wide phenomenon. The aggregate rate (9.7%) hid a near ten-fold spread across rooms (3.5 to 32.9%). The factors most visibly associated with the room-level pattern were case-mix complexity and routine urgent-elective overlap; first-case punctuality and inter-case idle time were not.', space_after=6)

add_heading_lower('Concentration, not prevalence')
add_paragraph('A 9.7% hospital-wide overtime rate is unremarkable on its own. The distribution, however, is uneven: OR10 ran overtime in roughly one of every three cases, while OR14 ran 3.5%. Hospital-wide targets such as "reduce overtime by 10%" will not reach the problem unless decomposed by room. Zhang, Dunstan and Pandit made the same point: aggregate metrics hide room-level operational reality.[16] Valid room-level metrics are a prerequisite for quality improvement.[24]', space_after=6)

add_heading_lower('Factors associated with overtime')
add_paragraph('The procedures with the largest planning deviations (complex cardiac and oncology cases) clustered in the rooms with the highest overtime. This concentration suggests that case-mix complexity, rather than scheduling inefficiency alone, accounts for much of the room-level variation. Wachtel and Dexter described, in a large operational dataset, how tardiness grows as duration uncertainty accumulates through the day,[26] and Fugener et al. documented systematic biases in surgeons\' duration estimates that compound across a list.[27] Both observations are consistent with the room-level pattern we describe, although our data cannot test the cumulative-delay account directly.', space_after=6)

add_paragraph('Urgent-elective overlap occurred on more than two-thirds of observation days and added roughly 30 minutes to elective start times. This makes urgent arrivals a routine scheduling factor rather than an exception. Protecting the elective program from this disruption, through dedicated urgent rooms or scheduling buffers, may be more effective than reactive rescheduling.', space_after=6)

add_paragraph('A common assumption is that first-case-on-time-start (FCOTS) drives end-of-day performance, with each minute of tardiness carrying a marginal cost.[25] At the room level, our data do not show that relationship: the room with the lowest late-start rate (OR10, 46.1%) had the highest overtime (32.9%), while a room with one of the highest late-start rates (OR14, 78.7%) had the lowest overtime (3.5%). Pandit et al. reported a similar disconnect across more than 7,000 operating room lists.[23] We do not conclude that FCOTS is unimportant; it remains a reasonable discipline marker. In this dataset, however, it does not predict where overtime accumulates.', space_after=6)

add_heading_lower('Implications')
add_paragraph('Operational implication. Room-level monitoring should sit ahead of hospital-wide overtime targets, and scheduling should treat urgent-case flow as a routine planning input rather than as an exception.', space_after=6)
add_paragraph('Clinical implication. The overtime we document is the same exposure that other studies have linked to staff fatigue and to elevated after-hours mortality and complication risk (Introduction; references 2-13). Whether those associations hold in this cohort is the question Phase 2 of this program will address by linking the operational patterns we describe to outcome data.', space_after=6)

add_heading_lower('Limitations')
add_paragraph('This study has several limitations. It is a single-site retrospective analysis, so whether the concentration pattern holds in hospitals with different staffing models is unknown. The administrative data provide room-in and room-out times only, so we cannot decompose what happens inside the case. We do not measure patient or staff outcomes directly; the harm argument rests on published literature, not on complications or burnout scores from this cohort. The urgency flag is set at booking, and we cannot distinguish truly emergent cases from semi-urgent or add-on elective cases. OR10 handles complex cardiac surgery, and its high overtime may partly reflect irreducible procedural duration rather than schedulable inefficiency; we describe this but cannot adjust for it without procedure-level risk scores. The link between after-hours surgery and patient harm rests on observational mortality studies whose effect sizes range widely (adjusted odds ratio 1.16[7] to 3.58[8]) and whose estimates have been questioned on residual-confounding grounds.[9] Readers should weigh the after-hours mortality evidence with this uncertainty in mind.', space_after=6)

# ============================================================
# CONCLUSION
# ============================================================
add_heading_caps('Conclusion', space_before=18)
add_paragraph('Operating-room overtime at this tertiary hospital concentrated in a small number of rooms, with case-mix complexity and urgent-elective overlap as the most visible associated factors. First-case punctuality and inter-case idle time were not associated with room-level overtime. The findings support room-level rather than hospital-level overtime monitoring and scheduling interventions that account for urgent-case flow. Phase 2 of this research program will link the operational patterns to patient outcome data.', space_after=6)

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
add_paragraph('The dataset contains de-identified administrative hospital data. Requests for access should be directed to the hospital\'s research office.', space_after=6)

add_heading_caps('Patient and public involvement', space_before=12)
add_paragraph('Patients were not involved in the design, conduct, or reporting of this study.', space_after=6)

# ============================================================
# REFERENCES
# ============================================================
add_heading_caps('References', space_before=18)

references = [
    'Wachtel RE, Dexter F. Review of behavioral operations experimental studies of newsvendor problems for operating room management. Anesth Analg 2010;110(6):1698-1710.',
    'Griffiths P, Dall’Ora C, Simon M, et al. Nurses’ shift length and overtime working in 12 European countries: the association with perceived quality of care and patient safety. Med Care 2014;52(11):975-81.',
    'Dall’Ora C, Griffiths P, Ball J, et al. Association of 12 h shifts and nurses’ job satisfaction, burnout and intention to leave: findings from a cross-sectional study of 12 European countries. BMJ Open 2015;5(9):e008331.',
    'Bae S-H. Nurse staffing, work hours, mandatory overtime, and turnover in acute care hospitals affect nurse job satisfaction, intent to leave, and burnout: a cross-sectional study. Int J Public Health 2024;69:1607068.',
    'Dall’Ora C, Ball J, Recio-Saucedo A, Griffiths P. Characteristics of shift work and their impact on employee performance and wellbeing: a literature review. Int J Nurs Stud 2016;57:12-27.',
    'Dall’Ora C, Ball J, Reinius M, Griffiths P. Burnout in nursing: a theoretical review. Hum Resour Health 2020;18:41.',
    'Cortegiani A, Ippolito M, Misseri G, et al. Association between night/after-hours surgery and mortality: a systematic review and meta-analysis. Br J Anaesth 2020;124(5):623-37.',
    'Oh T-K, Song I-A. Outcomes of after-hours surgeries performed under general anaesthesia: a South Korean nationwide cohort study. Anaesthesia 2025. DOI: 10.1111/anae.16559.',
    'Sakurai T. Assessing the influence of after-hours surgery: concerns with the confounders and conclusion. Anaesthesia 2025. DOI: 10.1111/anae.16591.',
    'Saager L, Hesler BD, You J, et al. Intraoperative transitions of anesthesia care and postoperative adverse outcomes. Anesthesiology 2014;121(4):695-706.',
    'Health Services Safety Investigations Body (HSSIB). The impact of staff fatigue on patient safety. Investigation report. London: HSSIB, 2025.',
    'Pittman P, Tiunn H-L, et al. Increased utilization of overtime and agency nurses and patient safety. JAMA Netw Open 2025. PMID: 40172888.',
    'Althoff FC, Wachtendorf LJ, Rostin P, et al. Effects of night surgery on postoperative mortality and morbidity: a multicentre cohort study. BMJ Qual Saf 2021;30(8):678-688.',
    'Joseph A, Khoshkenar A, Taaffe KM, et al. Minor flow disruptions, traffic-related factors and their effect on major flow disruptions in the operating room. BMJ Qual Saf 2019;28(4):276-83.',
    'Koch A, Burns J, Catchpole K, Weigl M. Associations of workflow disruptions in the operating room with surgical outcomes: a systematic review and narrative synthesis. BMJ Qual Saf 2020;29(12):1033-1045.',
    'Zhang C, Dunstan C, Pandit JJ. A tutorial on “capped utilisation” as a metric and key performance target in NHS England’s Model Hospital operating theatres database: caution for international healthcare systems. Anesthesiol Perioper Sci 2024. DOI: 10.1007/s44254-024-00073-3.',
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
