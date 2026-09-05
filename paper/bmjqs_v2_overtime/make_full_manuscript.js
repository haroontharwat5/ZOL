const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, BorderStyle, ShadingType, ImageRun,
} = require('docx');
const fs = require('fs');

const SP = '/tmp/claude-0/-home-user-ZOL/0eab60bb-835d-5933-8a55-8388cc65e941/scratchpad';
const fig1 = fs.readFileSync(SP + '/Figure1_v3.png');
const fig2 = fs.readFileSync(SP + '/Figure2_candidate.png');

const F = { font: 'Times New Roman', size: 24 };
const FS = { font: 'Times New Roman', size: 22 };
const NONE = { style: BorderStyle.NONE, size: 0, color: 'auto' };
const THIN = { style: BorderStyle.SINGLE, size: 4, color: '000000' };
const THICK = { style: BorderStyle.SINGLE, size: 8, color: '000000' };

function t(text, extra = {}) { return new TextRun({ text, ...F, ...extra }); }
function s(num) { return new TextRun({ text: num, superScript: true, ...F }); }
function para(children) { return new Paragraph({ children, spacing: { after: 240, line: 360 } }); }
function heading(text, italics = false) {
  return new Paragraph({ children: [new TextRun({ text, bold: true, italics, ...F })], spacing: { after: 240, line: 360 } });
}
function caption(parts) { return new Paragraph({ children: parts, spacing: { before: 120, after: 120, line: 300 } }); }
function figure(data, width, height) {
  return new Paragraph({
    children: [new ImageRun({ type: 'png', data, transformation: { width, height } })],
    alignment: AlignmentType.CENTER, spacing: { before: 120, after: 120 },
  });
}
function bCell(text, { bold = false, width, align = AlignmentType.LEFT, top = NONE, bottom = NONE, span, shade = false, indent = false } = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    columnSpan: span,
    borders: { top, bottom, left: NONE, right: NONE },
    shading: shade ? { type: ShadingType.CLEAR, fill: 'F2F2F2' } : undefined,
    margins: { top: 60, bottom: 60, left: 80, right: 80 },
    children: [new Paragraph({
      children: [new TextRun({ text, bold, ...FS })],
      alignment: align,
      indent: indent ? { left: 240 } : undefined,
      spacing: { after: 0 },
    })],
  });
}
function bookTable(widths, rows) {
  const W = widths.reduce((a, b) => a + b, 0);
  return new Table({
    columnWidths: widths,
    width: { size: W, type: WidthType.DXA },
    borders: { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE },
    rows: rows.map(r => {
      if (r.kind === 'section') {
        return new TableRow({ children: [bCell(r.cells[0].text, { bold: true, width: W, span: widths.length, shade: true })] });
      }
      const isHeader = r.kind === 'header', isLast = r.kind === 'last', isTotal = r.kind === 'total';
      return new TableRow({
        tableHeader: isHeader,
        children: r.cells.map((c, j) => bCell(c.text, {
          bold: isHeader || isTotal,
          width: widths[j],
          align: j === 0 ? AlignmentType.LEFT : AlignmentType.RIGHT,
          top: isHeader ? THICK : (isTotal ? THIN : NONE),
          bottom: isHeader ? THIN : ((isLast || (isTotal && r.alsoLast)) ? THICK : NONE),
          indent: c.indent,
        })),
      });
    }),
  });
}

const table1 = bookTable([5400, 3600], [
  { kind: 'header', cells: [{ text: 'Characteristic' }, { text: 'Value' }] },
  { kind: 'body', cells: [{ text: 'Surgical cases, n' }, { text: '79,352' }] },
  { kind: 'body', cells: [{ text: 'Unique patients, n' }, { text: '60,895' }] },
  { kind: 'body', cells: [{ text: 'Surgical operating rooms, n' }, { text: '18' }] },
  { kind: 'body', cells: [{ text: 'Distinct procedure types, n' }, { text: '1,276' }] },
  { kind: 'body', cells: [{ text: 'Surgeons, n' }, { text: '195' }] },
  { kind: 'body', cells: [{ text: 'Anaesthesiologists, n' }, { text: '207' }] },
  { kind: 'body', cells: [{ text: 'Study period' }, { text: 'Jan 2022 – May 2025' }] },
  { kind: 'section', cells: [{ text: 'Admission type, n (%)' }] },
  { kind: 'body', cells: [{ text: 'Ambulatory (day surgery)', indent: true }, { text: '33,566 (42.3)' }] },
  { kind: 'body', cells: [{ text: 'Inpatient', indent: true }, { text: '45,786 (57.7)' }] },
  { kind: 'section', cells: [{ text: 'Urgency, n (%)' }] },
  { kind: 'body', cells: [{ text: 'Elective', indent: true }, { text: '67,736 (85.4)' }] },
  { kind: 'body', cells: [{ text: 'Urgent (non-elective)', indent: true }, { text: '11,616 (14.6)' }] },
  { kind: 'section', cells: [{ text: 'Timing, n (%)' }] },
  { kind: 'body', cells: [{ text: 'Weekday', indent: true }, { text: '76,255 (96.1)' }] },
  { kind: 'body', cells: [{ text: 'Weekend', indent: true }, { text: '3,097 (3.9)' }] },
  { kind: 'section', cells: [{ text: 'Cases by year, n' }] },
  { kind: 'body', cells: [{ text: '2022', indent: true }, { text: '22,133' }] },
  { kind: 'body', cells: [{ text: '2023', indent: true }, { text: '23,575' }] },
  { kind: 'body', cells: [{ text: '2024', indent: true }, { text: '23,738' }] },
  { kind: 'last', cells: [{ text: '2025*', indent: true }, { text: '9,906' }] },
]);

const table2 = bookTable([1750, 1250, 1050, 1400, 1300, 1250, 1000], [
  { kind: 'header', cells: [{ text: 'Urgency' }, { text: 'n' }, { text: 'Share' }, { text: 'Overtime n' }, { text: 'OT rate' }, { text: 'Mean OT (min)' }, { text: 'P95 (min)' }] },
  { kind: 'body', cells: [{ text: 'Elective' }, { text: '67,736' }, { text: '85.4%' }, { text: '5,620' }, { text: '8.3%' }, { text: '5.0' }, { text: '29' }] },
  { kind: 'body', cells: [{ text: 'Urgent' }, { text: '11,616' }, { text: '14.6%' }, { text: '2,109' }, { text: '18.2%' }, { text: '10.7' }, { text: '69' }] },
  { kind: 'total', alsoLast: true, cells: [{ text: 'Total' }, { text: '79,352' }, { text: '100%' }, { text: '7,729' }, { text: '9.7%' }, { text: '–' }, { text: '–' }] },
]);

const references = [
  'Strum DP, May JH, Vargas LG. Modeling the uncertainty of surgical procedure times: comparison of log-normal and normal models. Anesthesiology 2000;92(4):1160-7.',
  "Griffiths P, Dall'Ora C, Simon M, et al. Nurses' shift length and overtime working in 12 European countries: the association with perceived quality of care and patient safety. Med Care 2014;52(11):975-81.",
  'Cortegiani A, Ippolito M, Misseri G, et al. Association between night/after-hours surgery and mortality: a systematic review and meta-analysis. Br J Anaesth 2020;124(5):623-37.',
  'Althoff FC, Wachtendorf LJ, Rostin P, et al. Effects of night surgery on postoperative mortality and morbidity: a multicentre cohort study. BMJ Qual Saf 2021;30(8):678-88.',
  'Saager L, Hesler BD, You J, et al. Intraoperative transitions of anesthesia care and postoperative adverse outcomes. Anesthesiology 2014;121(4):695-706.',
  "Dall'Ora C, Ball J, Recio-Saucedo A, Griffiths P. Characteristics of shift work and their impact on employee performance and wellbeing: a literature review. Int J Nurs Stud 2016;57:12-27.",
  'Bae S-H. Nurse staffing, work hours, mandatory overtime, and turnover in acute care hospitals affect nurse job satisfaction, intent to leave, and burnout: a cross-sectional study. Int J Public Health 2024;69:1607068.',
  'Pittman P, Tiunn HL, Luo Q, et al. Increased utilization of overtime and agency nurses and patient safety. JAMA Netw Open 2025;8(4):e252875.',
  'Macario A. Are your hospital operating rooms "efficient"? A scoring system with eight performance indicators. Anesthesiology 2006;105(2):237-40.',
  'Schouten AM, Flipse SM, van Nieuwenhuizen KE, et al. Operating room performance optimization metrics: a systematic review. J Med Syst 2023;47(1):19.',
  'Zhang C, Dunstan C, Pandit JJ. A tutorial on "capped utilisation" as a metric and key performance target in NHS England’s Model Hospital operating theatres database: caution for international healthcare systems. Anesthesiol Perioper Sci 2024;2:35. DOI: 10.1007/s44254-024-00073-3.',
  'Wachtel RE, Dexter F. Review of behavioral operations experimental studies of newsvendor problems for operating room management. Anesth Analg 2010;110(6):1698-710.',
  'Bauer M, Auhuber TC, Kraus R, et al. The German perioperative procedural time glossary: a joint recommendation by the BDA, BDC, VOPM, VOPMÖ, ÖGARI and SFOPM (2020 edition). Anästh Intensivmed 2020;61:516-31. DOI: 10.19224/ai2020.516.',
  "Eijkemans MJ, van Houdenhoven M, Nguyen T, et al. Predicting the unpredictable: a new prediction model for operating room times using individual characteristics and the surgeon's estimate. Anesthesiology 2010;112(1):41-9.",
  'Dexter F, Epstein RH. Typical savings from each minute reduction in tardy first case of the day starts. Anesth Analg 2009;108(4):1262-7.',
  'Pandit JJ, Abbott T, Pandit M, et al. Is "starting on time" useful (or useless) as a surrogate measure for "surgical theatre efficiency"? Anaesthesia 2012;67(8):823-32.',
  'MacMillan L, Madura GM, Elliot M, et al. What affects operating room turnover time? A systematic review and mapping of the evidence. Surgery 2025;181:109263.',
  'Fügener A, Schiffels S, Kolisch R. Overutilization and underutilization of operating rooms: insights from behavioral health care operations management. Health Care Manag Sci 2017;20(1):115-28.',
  'Wachtel RE, Dexter F. Influence of the operating room schedule on tardiness from scheduled start times. Anesth Analg 2009;108(6):1889-901.',
  'Parmar D, Woodman M, Pandit JJ. A graphical assessment of emergency surgical list efficiency to determine operating theatre capacity needs. Br J Anaesth 2022;128(3):574-83.',
  'Charlesworth M, Pandit JJ. Rational performance metrics for operating theatres, principles of efficiency, and how to achieve it. Br J Surg 2020;107(2):e63-9.',
  'Zhang C, Pandit JJ. Getting operating theatre metrics right to underpin quality improvement. Br J Anaesth 2023;131(1):130-4.',
  'Dexter F, Wachtel RE, Epstein RH. Decreasing the hours that anesthesiologists and nurse anesthetists work late by making decisions to reduce the hours of over-utilized operating room time. Anesth Analg 2016;122(3):831-42.',
  'Ivers N, Jamtvedt G, Flottorp S, et al. Audit and feedback: effects on professional practice and healthcare outcomes. Cochrane Database Syst Rev 2012;2012(6):CD000259.',
  'Oh T-K, Song I-A. Outcomes of after-hours surgeries performed under general anaesthesia: a South Korean nationwide cohort study. Anaesthesia 2025;80(6):645-51.',
  'Sakurai K, Takeda C. Assessing the influence of after-hours surgery: concerns with the confounders and conclusion. Anaesthesia 2025;80(5):596-7.',
  'Meewisse AJG, Gribnau A, Thiessen SE, et al. Effect of time of day on outcomes in elective surgery: a systematic review. Anaesthesia 2024;79(12):1325-34.',
];

const children = [
  heading('Data-driven monitoring of operating-room overtime: a single-centre retrospective study'),
  para([t('[Authors and affiliations removed for blinded review]')]),
  para([t('Keywords: ', { bold: true }), t('operating room, overtime, scheduling, patient safety, staff wellbeing, quality improvement')]),

  heading('ABSTRACT'),
  para([t('Background. ', { bold: true }), t('Operating-room (OR) overtime occurs when surgery continues beyond the end of the staffed shift. It is associated with poorer staff wellbeing, displaces surgery into after-hours periods linked to higher patient risk, and costs roughly twice as much per minute as underutilised time. It is usually reported as one figure for the whole OR department, concealing where it arises.')]),
  para([t('Objective. ', { bold: true }), t('To show what routinely collected administrative data can contribute to overtime monitoring and management, by characterising its distribution, its scheduled and unplanned components, and associated operational factors in one high-volume tertiary hospital.')]),
  para([t('Design and setting. ', { bold: true }), t('Retrospective observational study using administrative OR data from a 24/7 Belgian tertiary hospital with 18 surgical operating rooms.')]),
  para([t('Participants. ', { bold: true }), t('79,352 surgical cases (January 2022 to May 2025); a case is one patient’s uninterrupted stay in one operating room.')]),
  para([t('Main outcome measures. ', { bold: true }), t('Overtime per case by room, weekday, shift, and urgency; start-time deviation, duration-estimation accuracy, inter-case gaps, and urgent-case disruption as candidate factors.')]),
  para([t('Results. ', { bold: true }), t('Of 79,352 cases, 7,729 (9.7%) ran past the end of their assigned shift (mean 60.3 minutes among overtime cases; 95th percentile 197 minutes). Room-level rates ranged from 3.5% to 32.9%; the highest-overtime room ran overtime in a third of its cases (mean 154 minutes). Urgent cases crossed the boundary at more than twice the elective rate (18.2% versus 8.3%). Nearly half of overtime cases (45.7%) had been planned to end past the boundary; these scheduled crossings carried 62.1% of overtime minutes. Rooms with longer gaps between cases ran more overtime (Spearman rho = 0.89, p < 0.001); start-time punctuality showed no association (rho = −0.29, p = 0.24).')]),
  para([t('Conclusions. ', { bold: true }), t('Routinely collected OR data located overtime precisely enough to direct management attention: it was concentrated in a few rooms and divided into scheduled crossings and unplanned overruns, which call for different responses. Room-level monitoring built from these data may offer a more actionable basis than a department-wide average.')]),

  heading('KEY MESSAGES'),
  heading('What is already known on this topic', true),
  para([t('After-hours surgery is associated with higher patient mortality, and working overtime is associated with poorer nurse-reported quality and safety of care. The two are connected: a case that runs past the end of the day shift is completed in the evening, so overtime turns planned daytime surgery into after-hours surgery. Overtime is also costly: staffing is planned in advance, so underutilised time is paid staff time that goes unused, and overutilised time costs roughly twice as much per minute. Prior work reports overtime as an aggregate for the whole OR department, which can obscure where it arises.')]),
  heading('What this study adds', true),
  para([t('In a single-centre retrospective analysis of 79,352 surgical cases, overtime was concentrated in a few rooms, with a nearly ten-fold spread within one OR department (3.5% to 32.9%). Nearly half of overtime cases had been planned to end past the shift boundary, and these scheduled crossings carried most of the overtime minutes. Rooms with longer intervals between cases ran more overtime; start-time punctuality showed no association with room-level overtime.')]),
  heading('How this study might affect research, practice or policy', true),
  para([t('Hospitals seeking to reduce overtime could monitor individual rooms rather than a department-wide average, and could distinguish overtime that is scheduled into the programme from overtime that arises on the day, because the two call for different responses. Linking these operational patterns to patient and staff outcomes is a necessary next step.')]),

  heading('INTRODUCTION'),
  para([
    t('Operating lists overrun. Surgical durations are inherently variable,'), s('1'),
    t(' and a list planned to end with the day shift often does not. When surgery continues past the end of the rostered shift, the list runs into overtime. We use the term in the same sense as the staff-overtime literature, where overtime is work beyond contracted hours.'), s('2'),
  ]),
  para([
    t('The consequences reach patients as well as staff. Overtime pushes planned daytime surgery into the evening, and operating after hours carries documented risks: a meta-analysis found higher adjusted mortality for night and after-hours surgery (odds ratio 1.16, 95% CI 1.06 to 1.28, low-certainty evidence),'), s('3'),
    t(' and a multicentre cohort of more than 350,000 non-cardiac cases linked night surgery to increased morbidity, partly mediated by more frequent provider handovers during the case.'), s('4'),
    t(' Handovers carry risk of their own: a case that crosses the shift boundary continues under staff who were not present at its start, and for the best-studied type of intraoperative handover, anaesthesia transitions, the incidence of major complications rises from 8.8% with none to 21.2% with four or more.'), s('5'),
  ]),
  para([
    t('For staff, the evidence concerns overtime itself rather than its after-hours consequences. In a survey of 31,627 nurses across 12 European countries, working overtime was associated with poorer nurse-reported quality of care and worse patient safety.'), s('2'),
    t(' A review of shift-work studies linked overtime to decreased job performance,'), s('6'),
    t(' and mandatory overtime was associated with intention to leave in Korean acute-care hospitals.'), s('7'),
    t(' In 70 US hospitals, nursing overtime above a safety threshold was also associated with more pressure ulcers, one of the safety indicators most sensitive to nursing care.'), s('8'),
  ]),
  para([
    t('An OR department that wants to reduce overtime first has to know where it occurs, and the figures routinely available to management seldom show this. Established efficiency scoring operates at the level of the whole OR suite,'), s('9'),
    t(' published performance metrics lack standardised definitions,'), s('10'),
    t(' and aggregation can mislead: NHS England’s capped-utilisation metric ignores operating time in late finishes, which is precisely the time overtime consists of.'), s('11'),
    t(' Prior analyses of overtime itself treat it as a department-level number or as a cost parameter in staffing models.'), s('12'),
    t(' Where overtime sits within a department, room by room, and which operational factors are associated with it, the literature does not answer. The records needed to answer these questions already exist: OR information systems log room entry and exit times, planned durations, and urgency classifications in the course of daily operations.'), s('13'),
  ]),
  para([t('This paper uses those records to study overtime at a Belgian tertiary centre with 18 surgical ORs and a steep staffing step-down at each shift end. Drawing only on routinely recorded administrative data covering three and a half years and 79,352 cases, we address two research questions. First, how is overtime distributed across rooms and time, and to what extent is it scheduled rather than unplanned (RQ1)? Second, which of four operational factors are associated with it: duration overruns, urgent-elective interaction, start-time punctuality, and inter-case gaps (RQ2)? The aim is to show what data-driven analysis of routine OR records can contribute to overtime management, and where its limits lie.')]),

  heading('METHODS'),
  heading('Setting and data', true),
  para([t('The study hospital is a 24/7 tertiary centre in Belgium performing more than 22,000 surgical procedures per year. It operates 18 surgical operating rooms and 7 interventional operating rooms. The surgical staff includes 195 surgeons and 207 anaesthesiologists (including trainees and fellows), covering all surgical specialities except congenital cardiac surgery and organ transplantation. During the 08:00 to 16:30 day shift, each room is staffed with 2 to 3 nurses; at 16:30 the hospital reduces to 8 staffed rooms, at 17:30 to 4, and overnight to a single room.')]),
  para([t('We used administrative OR records from 1 January 2022 to 31 May 2025 for the 18 surgical operating rooms. Endoscopy suites and catheterisation laboratory cases without an anaesthesiologist present were excluded, as were cases with implausible timestamps (zero observed duration, planned duration exceeding 24 hours, or extreme deviations from the planned schedule). The final cohort comprised 79,352 cases involving 60,895 unique patients and 1,276 distinct procedure types; annual volume grew from 22,133 cases in 2022 to 23,738 in 2024, with 9,906 recorded through May 2025 (Table 1). The admission mix was 42.3% ambulatory and 57.7% inpatient, and 85.4% of cases were elective; cases scheduled or performed within 24 hours of booking were classified as urgent, all others as elective. Room-in and room-out times are the only procedural time markers confirmed as reliable by the hospital’s clinical team, and all timing analyses use these two time points.')]),
  caption([new TextRun({ text: 'Table 1. Study cohort characteristics. ', bold: true, ...F }), t('*2025 covers January to May.')]),
  table1,
  para([]),
  para([
    t('The unit of analysis is the case: one uninterrupted occupancy of one operating room by one patient, from room-in to room-out, recorded with one procedure code. A case is distinct from an admission, which may span days around it, and from a patient, since some of the 60,895 patients appear repeatedly over the study period. From these inputs we derived, for each case, the observed duration (room-in to room-out), the planning deviation (observed minus planned duration, positive when a case ran longer than booked), and the start-time deviation (actual minus planned room-in, positive when a case started late), following standard perioperative process-time definitions.'), s('13'),
    t(' We additionally derived an overtime flag, overtime minutes, and a shift label, as defined below.'),
  ]),
  heading('Overtime definition and analyses', true),
  para([
    t('Time beyond plan goes by different names in the literature, depending on the reference point. Measured against the room’s allocated block time, it is overutilisation.'), s('13'),
    t(' Measured against the clock, it is after-hours surgery.'), s('3'),
    t(' Measured against the staff roster, it is overtime: work beyond contracted hours.'), s('2'),
    t(' This study uses the roster as the reference point, applied at room level: at this hospital, the shift end is when the nursing team changes and the number of staffed rooms falls, so that is the line a late-running case actually crosses.'),
  ]),
  para([t('Each case was assigned to a shift by its actual room-in time, following the hospital’s shift boundaries: day (08:00 to 16:30), evening (16:30 to 22:00), and night (22:00 to 08:00). Cases entering between 07:30 and 08:00 and remaining past 08:00 (n = 6,153) were assigned to the day shift, as early starts of the day programme. The same rules applied on weekends. A case was flagged as overtime if its room-out fell after the end of its assigned shift, and its overtime minutes equal the positive difference between room-out and shift end. A case was classified as a scheduled crossing when its planned end time already fell after the end of its planned shift; overtime cases that were not scheduled crossings are referred to as unplanned overruns.')]),
  para([
    t('We measured overtime at room level because aggregate utilisation measures can misrepresent the performance of individual rooms.'), s('11'),
    t(' Because published OR performance metrics lack standardised definitions,'), s('10'),
    t(' each metric used in this study is defined explicitly.'),
  ]),
  para([
    t('In line with the study’s aim of showing what routinely recorded data can contribute to overtime monitoring, the analyses are descriptive apart from two rank correlations: we report rates, distributions, and shares as observed, we fitted no regression or causal models, and we draw no causal conclusions from the associations reported. For RQ1, we computed the overtime rate, mean, median, and 95th percentile, stratified by room, weekday, year, and shift, together with the split between scheduled crossings and unplanned overruns. For RQ2, we examined duration deviation by planned-duration bucket using the coefficient of variation, defined as the standard deviation of duration divided by its mean, which places cases of different lengths on a comparable scale.'), s('1,14'),
    t(' We further examined urgency mix and timing, urgent-elective interaction, start-time deviation per room, and inter-case idle time. Inter-case idle time was measured as the gap between consecutive cases in the same room within the same shift window; the first case in a window has no defined gap, overlapping room times count as zero, and gaps longer than 60 minutes were excluded as planned downtime. An urgent-elective overlap was flagged when an urgent case occupied a room during a window in which an elective case had been planned in that room, and start-delay comparisons were made at case level between overlapped and non-overlapped elective cases. Spearman rank correlations across the 18 rooms were computed between the room-level overtime rate and two candidate factors: the late-start rate, defined as the share of cases starting after their planned time, and the mean inter-case idle time; for the idle-time correlation, each room’s overtime rate was computed among the cases contributing gap data. Intermediate findings were reviewed with the clinical team and used to refine variable definitions and exclusions. The study is reported in accordance with the STROBE guidelines for observational studies.'),
  ]),
  heading('Ethics', true),
  para([t('This study used fully anonymised administrative data with institutional approval. No patient interaction occurred.')]),
  heading('Patient and public involvement', true),
  para([t('Given the retrospective use of fully anonymised administrative data, no patient or public involvement was sought.')]),

  heading('RESULTS'),
  heading('Overtime burden, composition, and room-level concentration (RQ1)', true),
  para([t('Of 79,352 cases, 7,729 (9.7%) ran past the end of their assigned shift. Among overtime cases, the mean was 60.3 minutes, the median 39 minutes, and the 95th percentile (P95) 197 minutes. Weekday rates were stable, between 8.8% and 9.9%, and roughly 1.7 times higher at weekends (Saturday 16.8%, Sunday 15.5%), when the elective programme does not run and the caseload is largely urgent. The overtime rate declined slightly over the study period, from 10.0% in 2022 to 8.6% in the first five months of 2025.')]),
  para([t('Not all of this overtime was unplanned. For 5,812 cases (7.3% of the cohort; 6.4% of elective and 12.8% of urgent cases), the schedule itself placed the planned end past the shift boundary, by a median of 40 planned minutes. Of these planned crossings, 60.8% did run past the boundary, against 5.7% of the cases planned to fit within their shift. The 7,729 overtime cases therefore divide into 3,532 scheduled crossings (45.7%) and 4,197 unplanned overruns (54.3%). Scheduled crossings ran longer, with a mean of 82 overtime minutes against 42 for unplanned overruns, and carried 62.1% of all overtime minutes. Much of the overtime was therefore already visible in the schedule before the day began.')]),
  para([t('Room-level differences were large, in both size and composition. Figure 1 shows each room’s overtime rate divided into its scheduled and unplanned components (panel A), together with its mean overtime duration (panel B). Rates ranged from 3.5% (OR14) to 32.9% (OR10). OR10, which handles complex cardiac surgery (coronary artery bypass grafting, aortic valve replacement, mitral valve repair), ran overtime in a third of its 1,743 cases, ran it longest (mean 154 minutes against a hospital mean of 60, panel B; P95 328 minutes), and ran it by design more than by accident: 81.5% of its overtime cases were scheduled crossings. The composition was reversed in OR11, the emergency-designated room, where 76.7% of overtime cases were unplanned overruns, consistent with a largely urgent caseload that enters the schedule at short notice. Overtime minutes were strongly concentrated: OR10 alone, with 2.2% of the caseload, generated 19.0% of all overtime minutes, and the three largest contributors together generated 36.4%.')]),
  figure(fig1, 580, 531),
  caption([new TextRun({ text: 'Figure 1. ', bold: true, ...F }), t('Room-level overtime, ranked by overtime rate. Panel A: percentage of cases with overtime per operating room, divided into scheduled crossings (planned end past the shift boundary) and unplanned overruns. Panel B: mean overtime duration per room in minutes, among overtime cases, with the hospital mean (60 min) marked. Overall: 7,729 of 79,352 cases (9.7%); 45.7% of overtime cases were scheduled crossings, carrying 62.1% of overtime minutes.')]),
  para([t('Most overtime cases ended shortly after the shift boundary: more than half of overtime completions fell between 16:30 and 17:30, immediately after the day-shift handover, and the distribution decayed through the evening. A department-wide rate therefore gives management little to act on. Overtime at this hospital is a property of particular rooms and of particular scheduling decisions, and both are identifiable from routine records.')]),
  heading('Candidate operational factors (RQ2)', true),
  para([
    t('Planning accuracy. ', { italics: true }),
    t('For the unplanned component of overtime, lists that were planned to finish inside the shift but did not, the first candidate explanation is systematic underbooking: if cases routinely needed more time than the schedule allotted, the shortfall would accumulate over a list and push its end past the boundary. The data show no such pattern. Of all cases, 45.7% ran longer than booked and 54.3% ran shorter, and the typical miss was nearly the same size on both sides: a median of 14 minutes over when a case ran long, and 12 minutes under when it ran short. The schedule’s weakness is not bias but unpredictability: two cases booked for the same duration often finished far apart.'),
  ]),
  para([t('This unpredictability was unevenly distributed. The coefficient of variation of observed duration was highest for short procedures (0.54 below 30 minutes) and between 0.35 and 0.42 for longer ones, but the variability of the planning error rose with planned duration, reaching 1.84 for procedures planned above 180 minutes: the longest cases were the hardest to book accurately. These long, hard-to-book procedures, mainly complex cardiac and oncological surgery, were performed in the rooms with the highest overtime rates. No uniform padding of bookings would therefore correct the schedule, because duration risk, the chance that a case runs well past its booked time, is concentrated in particular rooms and procedure types.')]),
  para([
    t('Urgent-elective interaction. ', { italics: true }),
    t('Urgent cases related to overtime through two channels. Directly, they generated it: urgent cases crossed the shift boundary at more than twice the elective rate (18.2% versus 8.3%, Table 2), and the worst cases ran further past it (P95 of 69 versus 29 minutes); because elective cases outnumber urgent cases six to one, elective work still supplied most of the overtime volume. Indirectly, urgent arrivals compressed the elective day: an urgent case occupied a room planned for elective use on 858 of 1,247 observation days (68.8%), and the affected elective cases started later than unaffected ones. At OR11, the emergency-designated room carrying the highest overlap burden (475 events, 15.2% of its elective cases), the median start delay was 60 minutes with overlap versus 28 minutes without. Whether the delayed cases themselves went on to run more overtime was not measured in this study.'),
  ]),
  caption([new TextRun({ text: 'Table 2. Volume and overtime by urgency. ', bold: true, ...F }), t('OT, overtime. Mean and P95 overtime are averaged over all cases in each row, including cases with zero overtime; the means reported in the text average over overtime cases only.')]),
  table2,
  para([]),
  para([
    t('Start-time punctuality. ', { italics: true }),
    t('A common assumption in OR management is that punctual starts, and the first case of the day in particular (first-case on-time start, FCOTS), keep a list on schedule so that it finishes within its shift.'), s('15,16'),
    t(' Late starts were common: 67.4% of cases started after their planned time, by a mean of 74.6 minutes and a median of 28 minutes among late cases. To test the assumption, we correlated each room’s late-start rate with its overtime rate. Across the 18 rooms there was no association (Spearman rho = −0.29, p = 0.24). Figure 2 (panel B) shows why: the rooms form a cloud with no gradient, and the extremes run against the assumption, with OR10 combining the lowest late-start rate with the highest overtime rate and OR14 starting late most often while running the least overtime. Start-time punctuality therefore does not indicate which rooms accumulate overtime.'),
  ]),
  para([
    t('Inter-case idle time. ', { italics: true }),
    t('Across the 18 rooms, inter-case idle time, a quantity akin to turnover time,'), s('17'),
    t(' had a median of 8 minutes and a mean of 9.9 minutes. At room level, mean idle time was positively correlated with the overtime rate (Spearman rho = 0.89, p < 0.001). In Figure 2 (panel A) the association appears as a gradient across the full span of rooms rather than a product of one outlier, and it persisted when OR10, which had both the highest mean idle time (22.6 minutes) and the highest overtime rate, was excluded (rho = 0.90, p < 0.001). Rooms with longer gaps between cases therefore also ran more overtime. Both quantities are plausibly markers of case-mix complexity, since complex procedures require longer preparation between cases as well as longer and less predictable operating times; the correlations cannot tell that explanation apart from a direct effect of slow turnover.'),
  ]),
  figure(fig2, 580, 280),
  caption([new TextRun({ text: 'Figure 2. ', bold: true, ...F }), t('Room-level correlates of overtime across the 18 operating rooms. Panel A: mean inter-case gap against the room’s overtime rate, computed among the cases contributing gap data (Spearman rho = 0.89, p < 0.001). Panel B: share of cases starting late against the room’s overall overtime rate (rho = −0.29, p = 0.24). Each point is one operating room.')]),

  heading('DISCUSSION'),
  para([t('In this analysis of 79,352 cases at one tertiary centre, one case in ten ran past the end of its staffed shift, but that department-wide figure concealed the two findings that matter most for management. First, overtime was concentrated: room-level rates spanned 3.5% to 32.9%, and a single cardiac room with 2.2% of the caseload generated 19.0% of all overtime minutes. Second, overtime was heterogeneous: nearly half of the cases that crossed the boundary had been planned to cross it, and these scheduled crossings carried 62.1% of the overtime minutes. Among the candidate operational factors, the most widely monitored one, start-time punctuality, carried no room-level signal, while inter-case gaps tracked overtime closely. None of these patterns is visible in the aggregate figure, and all were obtained from records the hospital already keeps.')]),
  heading('Two kinds of overtime, two levers', true),
  para([
    t('The scheduled component reframes part of the overtime problem as a capacity decision rather than a failure to run the day as planned. Booking a long case across the boundary uses staffed evening capacity that would otherwise stand idle, and idle staffed time is itself costly: overutilised time costs roughly twice as much as underutilised time, which is the trade-off OR managers weigh when staffing cannot match uncertain demand.'), s('12'),
    t(' Whether the volume of scheduled crossings at this hospital reflects a deliberate policy of using the evening tier could not be determined from administrative data. What the data do show is that planned and unplanned crossings put the case in the same position: it is completed after the nursing handover and with fewer rooms open either way. The two components nonetheless call for different responses. Scheduled crossings raise a planning and capacity question, namely whether the evening tier is sized for the work booked into it. Unplanned overruns raise a duration-risk question instead: whether the durations of the cases booked into a room can be predicted well enough to plan around. The components also separated by room: 81.5% of overtime cases in the cardiac room were scheduled crossings, while 76.7% in the emergency-designated room were unplanned overruns (Figure 1), so the lever that matters differs from room to room.'),
  ]),
  heading('Factors that did and did not accompany overtime', true),
  para([
    t('Unplanned overruns came from unpredictable durations, not from a schedule that was systematically too tight. Overruns and underruns were balanced overall, but the planning error grew most variable for the longest procedures, and surgeons’ duration estimates are known to show systematic biases when durations are uncertain.'), s('18'),
    t(' Delays have also been shown to build up over an operating list as the scheduled time before each case grows.'), s('19'),
    t(' Both findings, the estimation biases and the build-up of delay, are consistent with our observation that the rooms hosting long, hard-to-book cases were the rooms that ran late, although the descriptive design cannot test this cumulative mechanism directly.'),
  ]),
  para([
    t('Start-time punctuality, the most widely monitored discipline marker, was uninformative about overtime at this hospital. The premise behind first-case on-time starts is that each minute of tardiness carries through to the end of the day at measurable cost.'), s('15'),
    t(' That premise did not translate into a room-level association: the correlation between late-start rate and overtime rate was absent, and its direction, if anything, negative. Pandit and colleagues reached a compatible conclusion across more than 7,000 UK operating lists, in which start time explained only 4 to 8% of the variance in finish time.'), s('16'),
    t(' We do not conclude that punctuality is unimportant, only that at this hospital it does not indicate where overtime accumulates.'),
  ]),
  para([t('Inter-case gaps showed the opposite pattern: a strong positive room-level association with overtime where punctuality had none. We read long gaps as a reflection of the rooms’ case mix rather than as a cause of overtime, since complex procedures need longer preparation between cases as well as longer and less predictable operating times, and a cross-sectional correlation cannot show that shortening gaps would reduce overtime. Its value is as a signal: mean gap length is computable from the same two timestamps as overtime itself, and at this site it indicated the high-overtime rooms far more reliably than the more widely monitored start-time measures.')]),
  para([
    t('Urgent cases related to overtime in two ways: one measured, crossing the shift boundary at more than twice the elective rate, and one documented but not quantified, the routine delaying of elective start times. Overlap between urgent and elective work occurred on more than two-thirds of observation days despite dedicated urgent rooms, so protecting the elective programme is likely to require building slack into the schedule or reallocating room capacity, rather than rescheduling on the day; graphical methods for judging emergency capacity from delay and utilisation patterns could support such decisions.'), s('20'),
  ]),
  heading('Monitoring at the level where decisions are made', true),
  para([
    t('These findings support monitoring that reports each room separately and distinguishes scheduled from unplanned overtime, in preference to department-wide targets. A target such as “reduce overtime by 10%” offers no guidance when room rates differ ninefold and nearly half of overtime cases are scheduled into the programme: the highest-overtime room raises a capacity discussion rather than a punctuality campaign, and a punctuality campaign would in any case address a factor with no measured relation to overtime at this site. Aggregate theatre metrics have been criticised on precisely these grounds: capped utilisation discards the late-finish operating time that overtime consists of,'), s('11'),
    t(' and standard metrics mislead when used in isolation.'), s('21'),
    t(' Quality improvement requires metrics that are valid at the level where decisions are taken,'), s('22'),
    t(' and for overtime that level is the individual room and the schedule. This matches how overtime is reduced in practice: the decisions that most influence late running are taken shortly before and on the day of surgery, by identifying the specific rooms expected to run over and acting on them.'), s('23'),
    t(' Every quantity used in this study, the room-level rates, the scheduled and unplanned components, and the overtime risk visible at booking, derives from timestamps that OR information systems record in daily operation, so monitoring built on these quantities requires no new data collection. Feeding such data back to the teams involved is itself an evidence-supported improvement strategy, most effective when the feedback is repeated and linked to explicit targets and an action plan.'), s('24'),
  ]),
  heading('Limitations', true),
  para([
    t('This study has several limitations. It is a single-site analysis, and the concentration and composition patterns reflect one hospital’s staffing structure and scheduling practice; what may generalise is the approach rather than the numbers. The administrative record contains only room-in and room-out times, so events within a case cannot be examined. Beyond two rank correlations, the analyses are descriptive, and associations are reported without causal claims. The account linking case complexity to inter-case gaps, unpredictable durations, and overtime is an interpretation consistent with the data rather than a tested mechanism: the record contains no procedure-level complexity or risk scores, so case-mix differences between rooms could not be formally adjusted for. Whether scheduled boundary-crossings reflect deliberate policy could not be determined from these data. Weekend cases were classified with the same shift rules as weekday cases, and weekend staffing patterns were not separately verified. Finally, we did not measure patient or staff outcomes; the harm argument rests on published literature in which effect sizes vary widely and some estimates are contested on grounds of residual confounding.'), s('25-27'),
    t(' Readers should weigh the after-hours evidence with that uncertainty in mind.'),
  ]),

  heading('CONCLUSION'),
  para([t('Operating-room overtime at this tertiary hospital was concentrated in a small number of rooms and consisted of two components with different management levers: scheduled crossings, written into the programme and carrying most of the overtime minutes, and unplanned overruns, which reflected unpredictable case durations rather than late starts. All of these findings were obtained from routinely recorded administrative data, and much of the overtime risk was visible at the moment of planning. The findings support room-by-room monitoring of overtime, separated into its scheduled and unplanned components, as a practical tool for OR management; linking these operational patterns to patient and staff outcomes is the necessary next step.')]),

  heading('CONTRIBUTORSHIP STATEMENT'),
  para([t('[To complete with the co-authors before submission.]')]),
  heading('COMPETING INTERESTS'),
  para([t('None declared.')]),
  heading('FUNDING'),
  para([t('This study was supported by the Special Research Fund (BOF) of Hasselt University under Grant No. BOF24OWB10 and BOF24TT02 and Research Foundation Flanders (FWO) under Grant Number G0A4524N.')]),
  heading('DATA AVAILABILITY'),
  para([t('The dataset cannot be made publicly available, consistent with contractual agreements with the hospital.')]),

  heading('REFERENCES'),
  ...references.map((r, i) => para([t(`${i + 1}. ${r}`)])),
];

const doc = new Document({
  styles: { default: { document: { run: F } } },
  sections: [{ properties: { page: { size: { width: 11906, height: 16838 } } }, children }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(SP + '/Manuscript_v3_final.docx', buf);
  console.log('written');
});
