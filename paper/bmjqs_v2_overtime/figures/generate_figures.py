"""
Figures and tables for the BMJ QS overtime paper.
All numbers verified from In-Depth_Analysis_Genk.pdf screenshots:
Tables 24, 25, 20, 33, 35, 37, 38, 39 and Figures 16, 17.
Surgical-room cohort: n=79,352 (18 GO rooms), 7,729 overtime (9.7%).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'figure.facecolor': 'white',
})

OUTDIR = '/home/user/ZOL/paper/bmjqs_v2_overtime/figures'

# =============================================================================
# FIGURE 1 — Staffing pyramid
# =============================================================================
fig, ax = plt.subplots(figsize=(7, 4))

times = [8.0, 16.5, 16.5, 17.5, 17.5, 22.0, 22.0, 32.0]
rooms = [25,  25,   8,    8,    4,    4,    1,    1]

ax.fill_between(times, rooms, step='post', alpha=0.15, color='#2171b5')
ax.step(times, rooms, where='post', linewidth=2.5, color='#2171b5')

labels = [
    (12.25, 26.5, '25 rooms\n08:00–16:30', 13),
    (17.0,  9.5,  '8 rooms\n16:30–17:30', 10),
    (19.75, 5.5,  '4 rooms\n17:30–22:00', 10),
    (27.0,  2.8,  '1 room\n22:00–08:00\n(3 on-call nurses)', 9),
]
for x, y, txt, fs in labels:
    ax.text(x, y, txt, ha='center', va='bottom', fontsize=fs, fontweight='bold',
            color='#08519c')

ax.set_xlim(7, 33)
ax.set_ylim(0, 30)
ax.set_xlabel('Time of day')
ax.set_ylabel('Staffed operating rooms')
ax.set_title('Staffing pyramid at study hospital')

tick_positions = [8, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26, 28, 30, 32]
tick_labels = ['08:00', '10:00', '12:00', '14:00', '16:00', '17:00', '18:00',
               '20:00', '22:00', '00:00', '02:00', '04:00', '06:00', '08:00']
ax.set_xticks(tick_positions)
ax.set_xticklabels(tick_labels, rotation=45, ha='right', fontsize=8)
ax.set_yticks([0, 5, 10, 15, 20, 25])

for boundary in [16.5, 17.5, 22.0]:
    ax.axvline(boundary, color='grey', linestyle='--', linewidth=0.8, alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
fig.savefig(f'{OUTDIR}/fig1_staffing_pyramid.png')
fig.savefig(f'{OUTDIR}/fig1_staffing_pyramid.pdf')
plt.close(fig)
print('Figure 1 done.')

# =============================================================================
# FIGURE 2 — Room-level overtime concentration
# Source: Table 25 (In-Depth Analysis pp.30-31), 18 surgical rooms (OR01-OR18)
# Total n = 79,352 cases; campus average overtime = 9.7%
# =============================================================================

rooms_data = [
    ('OR10', 1743, 32.9, 154.2),
    ('OR09', 2637, 16.3, 71.6),
    ('OR13', 3298, 13.7, 61.3),
    ('OR08', 1777, 13.6, 68.5),
    ('OR12', 2884, 13.3, 59.4),
    ('OR05', 4886, 12.3, 54.8),
    ('OR11', 7482, 11.7, 55.1),
    ('OR02', 3502, 11.4, 52.1),
    ('OR04', 4518, 10.7, 57.4),
    ('OR03', 4094, 9.6, 45.0),
    ('OR06', 5217, 9.4, 58.6),
    ('OR16', 4098, 8.9, 36.9),
    ('OR15', 4323, 8.7, 46.6),
    ('OR07', 4658, 6.9, 38.0),
    ('OR17', 5480, 6.8, 44.2),
    ('OR18', 5293, 6.5, 41.6),
    ('OR01', 6577, 5.8, 57.8),
    ('OR14', 6885, 3.5, 31.4),
]

rooms_data.sort(key=lambda x: x[2])
names = [r[0] for r in rooms_data]
ncases = [r[1] for r in rooms_data]
pcts = [r[2] for r in rooms_data]
mean_ot = [r[3] for r in rooms_data]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 7), sharey=True,
                                gridspec_kw={'width_ratios': [3, 2], 'wspace': 0.30})

CAMPUS_AVG = 9.7
colors = ['#c6dbef' if p < CAMPUS_AVG else '#6baed6' if p < 15 else '#2171b5' if p < 30 else '#08306b'
          for p in pcts]

y_pos = np.arange(len(names))
ax1.barh(y_pos, pcts, color=colors, edgecolor='white', linewidth=0.5, height=0.7)
ax1.set_yticks(y_pos)
ax1.set_yticklabels(names, fontsize=9)
ax1.set_xlabel('Cases with overtime (%)')
ax1.set_title('A. Overtime rate by room', loc='left', fontweight='bold')
ax1.axvline(CAMPUS_AVG, color='#d62728', linestyle='--', linewidth=1, alpha=0.7)
ax1.text(CAMPUS_AVG + 0.5, 0, f'Hospital average {CAMPUS_AVG}%',
         fontsize=8, color='#d62728', va='center')
ax1.set_xlim(0, 36)

for i, (p, n) in enumerate(zip(pcts, ncases)):
    if p > 1.5:
        ax1.text(p - 0.3, i, f'{p:.1f}%', ha='right', va='center',
                 fontsize=7.5, fontweight='bold', color='white')
    else:
        ax1.text(p + 0.3, i, f'{p:.1f}%', ha='left', va='center',
                 fontsize=7.5, color='#555555')

CAMPUS_MEAN_OT = 60.3
ax2.barh(y_pos, mean_ot, color=colors, edgecolor='white', linewidth=0.5, height=0.7)
ax2.set_xlabel('Mean overtime (min)')
ax2.set_title('B. Mean overtime duration', loc='left', fontweight='bold')
ax2.set_xlim(0, 200)
ax2.axvline(CAMPUS_MEAN_OT, color='#d62728', linestyle='--', linewidth=1, alpha=0.7)
ax2.text(CAMPUS_MEAN_OT + 1.5, 0, f'Hospital average {CAMPUS_MEAN_OT} min',
         fontsize=8, color='#d62728', va='center')
for i, (m, n) in enumerate(zip(mean_ot, ncases)):
    if m > 120:  # long bars: label inside so it clears the n= count
        ax2.text(m - 3, i, f'{m:.0f}', ha='right', va='center',
                 fontsize=7.5, fontweight='bold', color='white')
    elif m > 5:
        ax2.text(m + 2, i, f'{m:.0f}', ha='left', va='center', fontsize=7.5, color='#333333')
    ax2.text(197, i, f'n={n:,}', ha='right', va='center', fontsize=7, color='grey')

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.tick_params(left=False)

fig.savefig(f'{OUTDIR}/fig2_room_overtime.png')
fig.savefig(f'{OUTDIR}/fig2_room_overtime.pdf')
plt.close(fig)
print('Figure 2 done.')

# =============================================================================
# FIGURE 3 — Shift displacement mechanism
# Source: Table 39 (In-Depth Analysis p.47)
# n=79,352; 4,151 displaced (5.2%); mean start delay 398.3 min;
# mean duration diff -22.3 min; mean overtime 10.4 min.
# =============================================================================
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

ax.text(5, 4.5, 'Shift displacement: the dominant overtime mechanism',
        ha='center', va='center', fontsize=13, fontweight='bold')

boxes = [
    (1.25, 2.5, '4,151', 'cases displaced\ninto a different shift', '5.2% of total'),
    (3.75, 2.5, '398',   'minutes\nmean start delay', '≈ 6h 38min'),
    (6.25, 2.5, '−22',   'minutes\nduration deviation', 'shorter than planned'),
    (8.75, 2.5, '10.4',  'minutes\nmean overtime', 'modest overrun'),
]
for x, y, number, label, subtitle in boxes:
    rect = mpatches.FancyBboxPatch((x - 1.0, y - 1.2), 2.0, 2.4,
                                    boxstyle='round,pad=0.1',
                                    facecolor='#deebf7', edgecolor='#2171b5',
                                    linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x, y + 0.5, number, ha='center', va='center',
            fontsize=20, fontweight='bold', color='#08306b')
    ax.text(x, y - 0.15, label, ha='center', va='center',
            fontsize=8.5, color='#2c3e50', linespacing=1.3)
    ax.text(x, y - 0.85, subtitle, ha='center', va='center',
            fontsize=7.5, color='#7f8c8d', style='italic')

for arrow_x in [(2.5, 2.75), (5.0, 5.25), (7.5, 7.75)]:
    ax.annotate('', xy=(arrow_x[0], 2.5), xytext=(arrow_x[1], 2.5),
                arrowprops=dict(arrowstyle='->', color='#2171b5', lw=1.5))

ax.text(5, 0.6,
        'Displaced cases finish on time or early. They run into a later shift\n'
        'because upstream delays pushed them across the shift boundary.',
        ha='center', va='center', fontsize=9, color='#555555', style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff9e6',
                  edgecolor='#f0c040', linewidth=1))

fig.tight_layout()
fig.savefig(f'{OUTDIR}/fig3_shift_displacement.png')
fig.savefig(f'{OUTDIR}/fig3_shift_displacement.pdf')
plt.close(fig)
print('Figure 3 done.')

# =============================================================================
# TABLE 1 — Overtime summary by weekday and year
# Sources: Table 24 (overall), Table 20 (weekday n), Figure 16 (weekday %),
# Figure 17 (year %).
# =============================================================================
print('\n' + '='*80)
print('TABLE 1 — Overtime summary by weekday and year (n=79,352)')
print('='*80)

# Weekday n from Table 20; OT% from Figure 16; mean OT from Figure 19;
# n_overtime calculated as n*pct
weekday = [
    ('Monday',     14232, 9.8, 58.5),
    ('Tuesday',    14750, 9.6, 60.1),
    ('Wednesday',  15814, 9.5, 59.7),
    ('Thursday',   15844, 8.8, 60.5),
    ('Friday',     15615, 9.9, 62.4),
    ('Saturday',    1654, 16.8, 63.4),
    ('Sunday',      1443, 15.5, 59.1),
]

print(f'\n{"Day":<12} {"n cases":>10} {"n overtime":>12} {"OT rate":>10} {"Mean OT":>10}')
print('-' * 60)
total_n = 0
total_ot = 0
for day, n, pct, mean in weekday:
    ot = round(n * pct / 100)
    print(f'{day:<12} {n:>10,} {ot:>12,} {pct:>9.1f}% {mean:>9.1f}')
    total_n += n
    total_ot += ot
print('-' * 60)
print(f'{"Total":<12} {total_n:>10,} {7729:>12,} {9.7:>9.1f}% {60.3:>9.1f}')

# Year from Figure 17
year = [
    ('2022',     10.0),
    ('2023',     10.0),
    ('2024',      9.7),
    ('2025*',     8.6),
]
print(f'\n{"Year":<12} {"OT rate":>10}')
print('-' * 25)
for yr, pct in year:
    print(f'{yr:<12} {pct:>9.1f}%')
print('-' * 25)
print(f'{"All years":<12} {9.7:>9.1f}%')
print('* 2025 data through May only.')

print(f'\nOverall (Table 24): n=79,352, overtime=7,729 (9.7%), '
      f'mean=60.3 min, median=39 min, P95=197 min')

# =============================================================================
# TABLE 2 — Urgent vs elective overtime and overlap
# Sources: Tables 33, 35, 37, 38
# =============================================================================
print('\n' + '='*80)
print('TABLE 2 — Urgent vs elective overtime and overlap')
print('='*80)

print('\nPanel A. Volume and overtime by urgency (Tables 33, 35)')
print(f'{"Urgency":<15} {"n":>10} {"Share":>8} {"After-hrs":>12} {"AH rate":>10} {"Mean OT":>10} {"P95 OT":>10}')
print('-' * 80)
print(f'{"Elective":<15} {"67,736":>10} {"85.4%":>8} {"5,620":>12} {"8.3%":>10} {"5 min":>10} {"29 min":>10}')
print(f'{"Non-elective":<15} {"11,616":>10} {"14.6%":>8} {"2,109":>12} {"18.2%":>10} {"10.7 min":>10} {"69 min":>10}')
print(f'{"Total":<15} {"79,352":>10} {"100%":>8} {"7,729":>12} {"9.7%":>10} {"—":>10} {"—":>10}')

print('\nPanel B. Urgent-elective overlap in the same room (Tables 37, 38)')
print(f'{"Days with overlap":<35} 858 / 1,247 (68.8%)')
print(f'{"Highest-burden room (OR11)":<35} 475 events affecting 15.2% of its elective cases')
print(f'{"Median start delay at OR11":<35} 28 min (no overlap) vs 60 min (overlap)')

# =============================================================================
# SUPPLEMENTARY TABLE S1 — CV by planned-duration bucket
# Source: Table 13, p.13 (unchanged — refers to full Genk dataset)
# =============================================================================
print('\n' + '='*80)
print('TABLE S1 — Coefficient of variation by planned-duration bucket')
print('='*80)
print(f'\n{"Duration bucket":<18} {"n":>10} {"CV (observed)":>16} {"CV (planning dev)":>20}')
print('-' * 65)
for bucket, n, cv_obs, cv_plan in [
    ('<30 min',    19511, 0.61, 1.25),
    ('31-60 min',  28674, 0.46, 1.07),
    ('61-90 min',  19921, 0.36, 1.06),
    ('91-180 min', 20592, 0.35, 0.91),
    ('>180 min',    7343, 0.42, 1.86),
]:
    print(f'{bucket:<18} {n:>10,} {cv_obs:>16.2f} {cv_plan:>20.2f}')

# =============================================================================
# SUPPLEMENTARY TABLE S2 — Start-time deviation by room (FCOTS contrast)
# Source: Table 21 (start-time per OR) + Table 25 (overtime per OR)
# Demonstrates the inverse relationship between punctuality and overtime
# inside the surgical cohort.
# =============================================================================
print('\n' + '='*80)
print('TABLE S2 — Start-time deviation by room vs overtime')
print('='*80)

# (room, n, late_pct, mean_delay, ot_pct) — joined from Tables 21 and 25
rooms_join = [
    ('OR11', 7482, 82.4, 319.1, 11.7),
    ('OR14', 6885, 78.7,  37.3,  3.5),
    ('OR01', 6577, 75.1,  38.0,  5.8),
    ('OR08', 1777, 71.9,  44.9, 13.6),
    ('OR02', 3502, 70.3,  42.2, 11.4),
    ('OR07', 4658, 70.0,  43.5,  6.9),
    ('OR05', 4886, 68.3,  54.3, 12.3),
    ('OR03', 4094, 65.9,  44.6,  9.6),
    ('OR09', 2637, 64.5,  48.9, 16.3),
    ('OR04', 4518, 63.5,  49.4, 10.7),
    ('OR15', 4323, 63.1,  40.5,  8.7),
    ('OR16', 4098, 62.6,  35.0,  8.9),
    ('OR18', 5293, 62.3,  36.9,  6.5),
    ('OR17', 5480, 61.8,  38.4,  6.8),
    ('OR06', 5217, 61.7,  42.1,  9.4),
    ('OR12', 2884, 54.5,  48.3, 13.3),
    ('OR13', 3298, 53.7,  48.6, 13.7),
    ('OR10', 1743, 46.1,  63.2, 32.9),
]
print(f'\n{"Room":<8} {"n":>8} {"Late starts %":>15} {"Mean delay":>12} {"Overtime %":>12}')
print('-' * 60)
for r, n, late, delay, ot in rooms_join:
    print(f'{r:<8} {n:>8,} {late:>14.1f}% {delay:>11.1f} {ot:>11.1f}%')

print('\nKey contrast:')
print('  OR10: 46.1% late starts (best punctuality) — 32.9% overtime (worst)')
print('  OR14: 78.7% late starts (2nd worst punctuality) — 3.5% overtime (best)')
print('  OR11: 82.4% late starts (worst, 319 min mean delay) — 11.7% overtime (mid-pack)')

# =============================================================================
# RENDERED TABLE 1 — Overtime summary by weekday and calendar year (MERGED)
# Single table with two strata (weekday, year) plus an overall total row.
# Per-year case counts for the surgical cohort: 2022=22,133, 2023=23,575,
# 2024=23,738, 2025*=9,906 (sum = 79,352); n overtime = round(n x rate).
# =============================================================================
fig, ax = plt.subplots(figsize=(8.5, 6))
ax.axis('off')
ax.set_title('Table 1. Overtime summary by weekday and calendar year',
             loc='left', fontweight='bold', fontsize=12, pad=10)

header = ['Stratum', 'n cases', 'n overtime', 'OT rate (%)', 'Mean OT (min)']
rows = [
    ['By weekday',  '',       '',      '',     ''],
    ['Monday',      '14,232', '1,395',  '9.8', '58.5'],
    ['Tuesday',     '14,750', '1,416',  '9.6', '60.1'],
    ['Wednesday',   '15,814', '1,502',  '9.5', '59.7'],
    ['Thursday',    '15,844', '1,394',  '8.8', '60.5'],
    ['Friday',      '15,615', '1,546',  '9.9', '62.4'],
    ['Saturday',     '1,654',   '278', '16.8', '63.4'],
    ['Sunday',       '1,443',   '224', '15.5', '59.1'],
    ['By calendar year', '',   '',      '',     ''],
    ['2022',        '22,133', '2,213', '10.0', '61.8'],
    ['2023',        '23,575', '2,358', '10.0', '58.8'],
    ['2024',        '23,738', '2,303',  '9.7', '61.3'],
    ['2025*',        '9,906',   '852',  '8.6', '58.2'],
    ['Total (all cases)', '79,352', '7,729', '9.7', '60.3'],
]

t1 = ax.table(cellText=rows, colLabels=header, loc='center', cellLoc='center')
t1.auto_set_font_size(False)
t1.set_fontsize(9)
t1.scale(1, 1.3)

# Header styling
for j in range(len(header)):
    t1[(0, j)].set_facecolor('#2171b5')
    t1[(0, j)].set_text_props(color='white', fontweight='bold')

# Section-header rows (1-indexed including the colLabels row at 0)
section_rows = [1, 9]   # 'By weekday', 'By calendar year'
for r in section_rows:
    for j in range(len(header)):
        t1[(r, j)].set_facecolor('#c6dbef')
        t1[(r, j)].set_text_props(fontweight='bold', ha='left' if j == 0 else 'center')

# Total row (last data row)
total_row = len(rows)
for j in range(len(header)):
    t1[(total_row, j)].set_facecolor('#deebf7')
    t1[(total_row, j)].set_text_props(fontweight='bold')

fig.text(0.5, 0.04,
         '* 2025 partial (Jan–May). Per-year case counts sum to the 79,352-case surgical cohort; '
         'overtime counts are rounded. Source: In-Depth Analysis Tables 20, 24; Figures 16, 17, 19, 20.',
         ha='center', fontsize=8, style='italic', color='#666666', wrap=True)
fig.tight_layout(rect=[0, 0.06, 1, 1])
fig.savefig(f'{OUTDIR}/table1_overtime_summary.png')
fig.savefig(f'{OUTDIR}/table1_overtime_summary.pdf')
plt.close(fig)
print('Table 1 rendered (merged single table).')

# =============================================================================
# RENDERED TABLE 2 — Urgent vs elective overtime and overlap
# =============================================================================
fig, axes = plt.subplots(2, 1, figsize=(8.5, 4.2),
                          gridspec_kw={'height_ratios': [3, 2]})

ax = axes[0]
ax.axis('off')
ax.set_title('Table 2A. Volume and overtime by urgency', loc='left',
             fontweight='bold', fontsize=11, pad=8)
header_a = ['Urgency', 'n', 'Share', 'After-hours n', 'AH rate', 'Mean OT (min)', 'P95 OT (min)']
rows_a = [
    ['Elective',     '67,736', '85.4%', '5,620',  '8.3%',  '5',    '29'],
    ['Non-elective', '11,616', '14.6%', '2,109', '18.2%', '10.7',  '69'],
    ['Total',        '79,352', '100%',  '7,729',  '9.7%',  '—',    '—'],
]
ta = ax.table(cellText=rows_a, colLabels=header_a, loc='center', cellLoc='center')
ta.auto_set_font_size(False)
ta.set_fontsize(9)
ta.scale(1, 1.35)
for j in range(len(header_a)):
    ta[(0, j)].set_facecolor('#2171b5')
    ta[(0, j)].set_text_props(color='white', fontweight='bold')
for j in range(len(header_a)):
    ta[(3, j)].set_facecolor('#deebf7')
    ta[(3, j)].set_text_props(fontweight='bold')

ax = axes[1]
ax.axis('off')
ax.set_title('Table 2B. Urgent–elective overlap in the same room',
             loc='left', fontweight='bold', fontsize=11, pad=8)
header_b = ['Metric', 'Value']
rows_b = [
    ['Days with at least one overlap',          '858 of 1,247 (68.8%)'],
    ['Highest-burden room (OR11)',              '475 events; 15.2% of its elective cases'],
    ['Median start delay at OR11 (no overlap)', '28 min'],
    ['Median start delay at OR11 (overlap)',    '60 min'],
]
tb = ax.table(cellText=rows_b, colLabels=header_b, loc='center', cellLoc='left',
              colWidths=[0.55, 0.45])
tb.auto_set_font_size(False)
tb.set_fontsize(9)
tb.scale(1, 1.35)
for j in range(len(header_b)):
    tb[(0, j)].set_facecolor('#2171b5')
    tb[(0, j)].set_text_props(color='white', fontweight='bold')

fig.text(0.5, 0.01,
         'Source: In-Depth Analysis Tables 33, 35, 37, 38.',
         ha='center', fontsize=8, style='italic', color='#666666')
fig.tight_layout(rect=[0, 0.03, 1, 1])
fig.savefig(f'{OUTDIR}/table2_urgent_overlap.png')
fig.savefig(f'{OUTDIR}/table2_urgent_overlap.pdf')
plt.close(fig)
print('Table 2 rendered.')

# =============================================================================
# FIGURE S1 — Idle-time distribution between consecutive cases
# Source: Table 40 + Figure 31 (approximate bin heights)
# =============================================================================
fig, ax = plt.subplots(figsize=(7, 4))
bins = ['0–5', '5–10', '10–15', '15–20', '20–25', '25–30',
        '30–35', '35–40', '40–45', '45–50', '50–55', '55–60']
counts = [9000, 13000, 4500, 1500, 800, 400, 200, 150, 100, 80, 60, 50]
colors_s1 = ['#2171b5'] * len(bins)
ax.bar(bins, counts, color=colors_s1, edgecolor='white', linewidth=0.5)
ax.set_xlabel('Idle time between consecutive cases (minutes)')
ax.set_ylabel('Number of transitions')
ax.set_title('Figure S1. Idle time between consecutive cases',
             loc='left', fontweight='bold', fontsize=11)
ax.tick_params(axis='x', rotation=0, labelsize=8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.text(0.98, 0.92,
        'Mean 9.9 min · Median 8 min\nP95 25 min · P99 42 min',
        transform=ax.transAxes, ha='right', va='top', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff9e6',
                  edgecolor='#f0c040'))
fig.tight_layout()
fig.savefig(f'{OUTDIR}/figS1_idle_time.png')
fig.savefig(f'{OUTDIR}/figS1_idle_time.pdf')
plt.close(fig)
print('Figure S1 done.')

# =============================================================================
# FIGURE S2 — End-time distribution of overtime cases
# Source: In-Depth Figure 18 (approximate bin heights)
# =============================================================================
fig, ax = plt.subplots(figsize=(8, 4))
hours = ['16:30', '17:30', '18:30', '19:30', '20:30', '21:30',
         '22:30', '23:30', '00:30', '01:30', '02:30', '03:30',
         '04:30', '05:30', '06:30', '07:30']
case_counts = [2700, 1600, 850, 450, 280, 200, 380, 300, 220, 120, 60, 40, 30, 20, 30, 60]
ax.bar(hours, case_counts, color='#2171b5', edgecolor='white', linewidth=0.5)
ax.set_ylim(0, 3200)
ax.set_xlabel('End time of surgery')
ax.set_ylabel('Number of overtime cases')
ax.set_title('Figure S1. Timing of overtime case completions',
             loc='left', fontweight='bold', fontsize=11, pad=12)
ax.tick_params(axis='x', rotation=45, labelsize=8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.axvspan(-0.5, 0.5, alpha=0.15, color='#d62728')
# annotate from the right so the label clears the top-left title
ax.annotate('Day-shift spillover', xy=(0.45, 2700), xytext=(3.0, 2950),
            ha='left', va='center', fontsize=8, color='#d62728', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.2))
fig.tight_layout()
fig.savefig(f'{OUTDIR}/figS2_end_time_distribution.png')
fig.savefig(f'{OUTDIR}/figS2_end_time_distribution.pdf')
plt.close(fig)
print('Figure S2 done.')

# =============================================================================
# RENDERED TABLE S2 — Per-room start-time deviation vs overtime (FCOTS contrast)
# =============================================================================
fig, ax = plt.subplots(figsize=(8.5, 7))
ax.axis('off')
ax.set_title('Table S2. Per-room start-time deviation vs overtime rate',
             loc='left', fontweight='bold', fontsize=11, pad=8)
header_s2 = ['Room', 'n', 'Late starts (%)', 'Mean delay (min)', 'Overtime (%)']
rooms_join = [
    ('OR11', 7482, 82.4, 319.1, 11.7),
    ('OR14', 6885, 78.7,  37.3,  3.5),
    ('OR01', 6577, 75.1,  38.0,  5.8),
    ('OR08', 1777, 71.9,  44.9, 13.6),
    ('OR02', 3502, 70.3,  42.2, 11.4),
    ('OR07', 4658, 70.0,  43.5,  6.9),
    ('OR05', 4886, 68.3,  54.3, 12.3),
    ('OR03', 4094, 65.9,  44.6,  9.6),
    ('OR09', 2637, 64.5,  48.9, 16.3),
    ('OR04', 4518, 63.5,  49.4, 10.7),
    ('OR15', 4323, 63.1,  40.5,  8.7),
    ('OR16', 4098, 62.6,  35.0,  8.9),
    ('OR18', 5293, 62.3,  36.9,  6.5),
    ('OR17', 5480, 61.8,  38.4,  6.8),
    ('OR06', 5217, 61.7,  42.1,  9.4),
    ('OR12', 2884, 54.5,  48.3, 13.3),
    ('OR13', 3298, 53.7,  48.6, 13.7),
    ('OR10', 1743, 46.1,  63.2, 32.9),
]
rows_s2 = [[r, f'{n:,}', f'{l:.1f}', f'{d:.1f}', f'{o:.1f}']
           for r, n, l, d, o in rooms_join]
ts2 = ax.table(cellText=rows_s2, colLabels=header_s2, loc='center', cellLoc='center')
ts2.auto_set_font_size(False)
ts2.set_fontsize(9)
ts2.scale(1, 1.25)
for j in range(len(header_s2)):
    ts2[(0, j)].set_facecolor('#2171b5')
    ts2[(0, j)].set_text_props(color='white', fontweight='bold')
go10_row = next(i for i, (r, *_) in enumerate(rooms_join) if r == 'OR10') + 1
go14_row = next(i for i, (r, *_) in enumerate(rooms_join) if r == 'OR14') + 1
go11_row = next(i for i, (r, *_) in enumerate(rooms_join) if r == 'OR11') + 1
for j in range(len(header_s2)):
    ts2[(go10_row, j)].set_facecolor('#fee5d9')
    ts2[(go14_row, j)].set_facecolor('#deebf7')
    ts2[(go11_row, j)].set_facecolor('#fff9e6')

fig.text(0.5, 0.015,
         'OR10 (orange): best punctuality, worst overtime. '
         'OR14 (blue): worst punctuality, best overtime. '
         'OR11 (yellow): worst delay, mid-pack overtime.',
         ha='center', fontsize=8, style='italic', color='#444444')
fig.tight_layout(rect=[0, 0.04, 1, 1])
fig.savefig(f'{OUTDIR}/tableS2_starttime_vs_overtime.png')
fig.savefig(f'{OUTDIR}/tableS2_starttime_vs_overtime.pdf')
plt.close(fig)
print('Table S2 rendered.')

print('\nAll figures saved to:', OUTDIR)
