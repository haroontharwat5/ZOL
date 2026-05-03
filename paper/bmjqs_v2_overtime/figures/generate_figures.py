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
# FIGURE 1 — Staffing pyramid (step diagram)
# =============================================================================
fig, ax = plt.subplots(figsize=(7, 4))

times =  [8.0,  16.5, 16.5, 17.5, 17.5, 22.0, 22.0, 32.0]
rooms =  [25,   25,   8,    8,    4,    4,    1,    1   ]

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
ax.set_title('Staffing pyramid at Campus Genk')

tick_positions = [8, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26, 28, 30, 32]
tick_labels = ['08:00','10:00','12:00','14:00','16:00','17:00','18:00',
               '20:00','22:00','00:00','02:00','04:00','06:00','08:00']
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
# FIGURE 2 — Room-level overtime concentration (horizontal bar chart)
# =============================================================================

rooms_data = [
    ('GO10', 1743, 32.9, 154.2),
    ('GO09', 2637, 16.3, 71.6),
    ('GO13', 3298, 13.7, 61.3),
    ('GO08', 1777, 13.6, 68.5),
    ('GO12', 2884, 13.3, 59.4),
    ('GO05', 4886, 12.3, 54.8),
    ('GO11', 7482, 11.7, 55.1),
    ('GO02', 3502, 11.4, 52.1),
    ('GO04', 4518, 10.7, 57.4),
    ('GO03', 4094, 9.6, 45.0),
    ('GO06', 5217, 9.4, 58.6),
    ('GO16', 4098, 8.9, 36.9),
    ('GO15', 4323, 8.7, 46.6),
    ('GO07', 4658, 6.9, 38.0),
    ('GO17', 5480, 6.8, 44.2),
    ('GO18', 5293, 6.5, 41.6),
    ('GO01', 6577, 5.8, 57.8),
    ('GO14', 6885, 3.5, 31.4),
    ('GEX1', 634,  0.3, 0),
    ('GSE1', 2261, 0.0, 0),
    ('GEG1', 4498, 0.0, 0),
]

rooms_data.sort(key=lambda x: x[2])

names = [r[0] for r in rooms_data]
pcts = [r[2] for r in rooms_data]
mean_ot = [r[3] for r in rooms_data]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 7), sharey=True,
                                gridspec_kw={'width_ratios': [3, 2], 'wspace': 0.08})

colors = ['#c6dbef' if p < 8.4 else '#6baed6' if p < 15 else '#2171b5' if p < 30 else '#08306b'
          for p in pcts]

y_pos = np.arange(len(names))
ax1.barh(y_pos, pcts, color=colors, edgecolor='white', linewidth=0.5, height=0.7)
ax1.set_yticks(y_pos)
ax1.set_yticklabels(names, fontsize=9)
ax1.set_xlabel('Cases with overtime (%)')
ax1.set_title('Overtime rate by room')
ax1.axvline(8.4, color='#d62728', linestyle='--', linewidth=1, alpha=0.7)
ax1.text(8.4 + 0.5, len(names) - 0.5, 'Campus\naverage\n8.4%', fontsize=8,
         color='#d62728', va='top')

for i, (p, n) in enumerate(zip(pcts, [r[1] for r in rooms_data])):
    if p > 1:
        ax1.text(p - 0.3, i, f'{p:.1f}%', ha='right', va='center', fontsize=7.5,
                 fontweight='bold', color='white')
    ax1.text(max(pcts) + 1.5, i, f'n={n:,}', ha='left', va='center', fontsize=7.5,
             color='grey')

ax2.barh(y_pos, mean_ot, color=colors, edgecolor='white', linewidth=0.5, height=0.7)
ax2.set_xlabel('Mean overtime (min)')
ax2.set_title('Mean overtime duration')
for i, m in enumerate(mean_ot):
    if m > 0:
        ax2.text(m + 1, i, f'{m:.0f}', ha='left', va='center', fontsize=7.5, color='grey')

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

fig.suptitle('Figure 2. Room-level overtime concentration at Campus Genk',
             fontsize=12, fontweight='bold', y=1.01)

fig.tight_layout()
fig.savefig(f'{OUTDIR}/fig2_room_overtime.png')
fig.savefig(f'{OUTDIR}/fig2_room_overtime.pdf')
plt.close(fig)
print('Figure 2 done.')

# =============================================================================
# FIGURE 3 — Shift displacement mechanism (infographic)
# =============================================================================

fig, ax = plt.subplots(figsize=(8, 3.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

ax.text(5, 4.5, 'Shift displacement: the dominant overtime mechanism',
        ha='center', va='center', fontsize=13, fontweight='bold')

boxes = [
    (1.25, 2.5, '4,151', 'cases displaced\ninto a different shift', '5.2% of total'),
    (3.75, 2.5, '398', 'minutes\nmean start delay', '≈ 6.6 hours'),
    (6.25, 2.5, '−22', 'minutes\nduration deviation', 'shorter than planned'),
    (8.75, 2.5, '10.4', 'minutes\nmean overtime', 'modest overrun'),
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

ax.annotate('', xy=(2.5, 2.5), xytext=(2.75, 2.5),
            arrowprops=dict(arrowstyle='->', color='#2171b5', lw=1.5))
ax.annotate('', xy=(5.0, 2.5), xytext=(5.25, 2.5),
            arrowprops=dict(arrowstyle='->', color='#2171b5', lw=1.5))
ax.annotate('', xy=(7.5, 2.5), xytext=(7.75, 2.5),
            arrowprops=dict(arrowstyle='->', color='#2171b5', lw=1.5))

ax.text(5, 0.6,
        'Displaced cases finish on time or early. They run into overtime\n'
        'because upstream delays pushed them across the shift boundary.',
        ha='center', va='center', fontsize=9, color='#555555',
        style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff9e6', edgecolor='#f0c040',
                  linewidth=1))

fig.tight_layout()
fig.savefig(f'{OUTDIR}/fig3_shift_displacement.png')
fig.savefig(f'{OUTDIR}/fig3_shift_displacement.pdf')
plt.close(fig)
print('Figure 3 done.')

# =============================================================================
# TABLE 1 — Overtime summary by weekday and year (formatted text output)
# =============================================================================

print('\n' + '='*70)
print('TABLE 1 — Overtime summary by weekday and year')
print('='*70)
print('\nNote: Weekday percentages from Figure 16 in screenshots.')
print('Case counts and overtime counts not available from screenshots.')
print('Year percentages from Figure 17.\n')
print(f'{"Day":<12} {"OT rate (%)":<15}')
print('-' * 30)
for day, pct in [('Monday', 9.5), ('Tuesday', 9.5), ('Wednesday', 9.5),
                  ('Thursday', 8.8), ('Friday', 9.9),
                  ('Saturday', 16.8), ('Sunday', 15.5)]:
    print(f'{day:<12} {pct:<15.1f}')
print()
print(f'{"Year":<12} {"OT rate (%)":<15}')
print('-' * 30)
for year, pct in [('2022', 10.0), ('2023', 10.0), ('2024', 9.7), ('2025*', 8.0)]:
    print(f'{year:<12} {pct:<15.1f}')
print('* 2025 partial (through May)')
print('\n⚠ Paper draft uses different numbers (weekdays 7.8-8.5%, years 8.8-7.2%).')
print('  These may come from a different analysis run or inclusion criteria.')

# =============================================================================
# TABLE 2 — Urgent vs elective overtime and overlap
# =============================================================================

print('\n' + '='*70)
print('TABLE 2 — Urgent vs elective overtime and overlap')
print('='*70)

print('\nPanel A: Overtime by urgency (from Tables 33 + 35)')
print(f'{"Urgency":<15} {"Total n":<10} {"After-hrs n":<12} {"Rate (%)":<10} {"Mean OT":<10} {"P95 OT":<10}')
print('-' * 67)
print(f'{"Elective":<15} {"67,736":<10} {"5,620":<12} {"8.3":<10} {"5":<10} {"29":<10}')
print(f'{"Non-elective":<15} {"11,616":<10} {"2,109":<12} {"18.2":<10} {"10.7":<10} {"69":<10}')
print(f'{"Total":<15} {"79,352":<10} {"7,729":<12} {"9.7":<10} {"—":<10} {"—":<10}')

print('\nPanel B: Urgent-elective overlap (from Tables 37 + 38)')
print(f'  Overlap days:      858 / 1,247 = 68.8%')
print(f'  Top-burden room:   GO11 (475 events, 15.2% of its elective cases)')
print(f'  Start-delay effect: median 28 min (no overlap) vs 60 min (overlap) at GO11')

print('\n⚠ Paper draft uses slightly different numbers:')
print('  - 84,028 elective / 12,016 non-elective (total 96,044)')
print('  - 7% / 18% overtime rates')
print('  - 869/1,247 = 69.7% overlap days')
print('  - 485 overlap events at GO11')

# =============================================================================
# SUPPLEMENTARY: Table S1 — CV by planned-duration bucket
# =============================================================================

print('\n' + '='*70)
print('TABLE S1 — Coefficient of variation by planned-duration bucket')
print('='*70)
print('\nFrom paper text (Section 3.2):')
print(f'{"Duration bucket":<20} {"CV (observed)":<18}')
print('-' * 38)
for bucket, cv in [('<30 min', '0.61'), ('31-60 min', '0.46'),
                    ('61-90 min', '0.36'), ('91-180 min', '0.35'),
                    ('>180 min', '0.42')]:
    print(f'{bucket:<20} {cv:<18}')
print('\nPlanning-deviation CV for >180 min bucket: 1.86')
print('Note: Full data with n per bucket needed from In-Depth Table 13.')

print('\nAll figures saved to:', OUTDIR)
