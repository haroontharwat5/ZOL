"""
Figures and tables for the BMJ QS overtime paper.
All numbers verified against In-Depth_Analysis_Genk.pdf (Tables 24, 25, 33-40, Figures 16-20).
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
ax.set_title('Staffing pyramid at Campus Genk')

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
# Source: Table 25 (In-Depth Analysis pp.30-31), all 25 rooms (GIC7 excluded n=2)
# =============================================================================

rooms_data = [
    ('GO10', 1752, 32.9, 154.2),
    ('GO09', 2640, 16.3, 71.6),
    ('GO13', 3308, 13.8, 61.4),
    ('GO12', 2889, 13.4, 59.2),
    ('GO08', 2615, 12.5, 57.7),
    ('GO05', 4905, 12.3, 54.8),
    ('GO11', 7567, 11.7, 55.1),
    ('GO02', 3514, 11.3, 52.1),
    ('GO04', 4535, 10.7, 57.4),
    ('GO03', 4204, 9.4, 45.1),
    ('GO06', 5226, 9.4, 58.5),
    ('GO16', 4100, 8.9, 36.9),
    ('GO15', 4327, 8.7, 46.6),
    ('GO07', 4751, 6.8, 37.9),
    ('GO17', 5482, 6.8, 44.2),
    ('GO18', 5300, 6.6, 41.4),
    ('GO01', 6607, 5.8, 57.5),
    ('GO14', 6896, 3.6, 31.1),
    ('GOP2', 1316, 3.1, 24.4),
    ('GEE1', 2330, 2.4, 14.0),
    ('GEE2', 1646, 1.6, 16.1),
    ('GOP1', 2739, 1.6, 22.2),
    ('GEX1', 634,  0.3, 11.0),
    ('GEG1', 4498, 0.0, 0.0),
    ('GSE1', 2261, 0.0, 0.0),
]

rooms_data.sort(key=lambda x: x[2])
names = [r[0] for r in rooms_data]
ncases = [r[1] for r in rooms_data]
pcts = [r[2] for r in rooms_data]
mean_ot = [r[3] for r in rooms_data]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 8), sharey=True,
                                gridspec_kw={'width_ratios': [3, 2], 'wspace': 0.30})

colors = ['#c6dbef' if p < 8.4 else '#6baed6' if p < 15 else '#2171b5' if p < 30 else '#08306b'
          for p in pcts]

y_pos = np.arange(len(names))
ax1.barh(y_pos, pcts, color=colors, edgecolor='white', linewidth=0.5, height=0.7)
ax1.set_yticks(y_pos)
ax1.set_yticklabels(names, fontsize=9)
ax1.set_xlabel('Cases with overtime (%)')
ax1.set_title('A. Overtime rate by room', loc='left', fontweight='bold')
ax1.axvline(8.4, color='#d62728', linestyle='--', linewidth=1, alpha=0.7)
ax1.text(8.4 + 0.5, 0, 'Campus average 8.4%', fontsize=8, color='#d62728', va='center')
ax1.set_xlim(0, 36)

for i, (p, n) in enumerate(zip(pcts, ncases)):
    if p > 1.5:
        ax1.text(p - 0.3, i, f'{p:.1f}%', ha='right', va='center',
                 fontsize=7.5, fontweight='bold', color='white')
    else:
        ax1.text(p + 0.3, i, f'{p:.1f}%', ha='left', va='center',
                 fontsize=7.5, color='#555555')

ax2.barh(y_pos, mean_ot, color=colors, edgecolor='white', linewidth=0.5, height=0.7)
ax2.set_xlabel('Mean overtime (min)')
ax2.set_title('B. Mean overtime duration', loc='left', fontweight='bold')
ax2.set_xlim(0, 175)
for i, (m, n) in enumerate(zip(mean_ot, ncases)):
    if m > 5:
        ax2.text(m + 2, i, f'{m:.0f}', ha='left', va='center', fontsize=7.5, color='#333333')
    ax2.text(170, i, f'n={n:,}', ha='right', va='center', fontsize=7, color='grey')

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
# =============================================================================
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

ax.text(5, 4.5, 'Shift displacement: the dominant overtime mechanism',
        ha='center', va='center', fontsize=13, fontweight='bold')

boxes = [
    (1.25, 2.5, '4,786', 'cases displaced\ninto a different shift', '5.0% of total'),
    (3.75, 2.5, '352',   'minutes\nmean start delay', '≈ 5h 52min'),
    (6.25, 2.5, '−22',   'minutes\nduration deviation', 'shorter than planned'),
    (8.75, 2.5, '9.2',   'minutes\nmean overtime', 'modest overrun'),
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
# Sources: Table 24, Tables 33-34, Figures 16-17, Figures 19-20
# =============================================================================
print('\n' + '='*80)
print('TABLE 1 — Overtime summary by weekday and year')
print('='*80)

weekday = [
    ('Monday',     17938, 1435, 8.0, 57.8),
    ('Tuesday',    18489, 1516, 8.2, 57.4),
    ('Wednesday',  17943, 1525, 8.5, 59.1),
    ('Thursday',   18420, 1437, 7.8, 59.1),
    ('Friday',     20112, 1609, 8.0, 60.8),
    ('Saturday',    1680,  282, 16.8, 63.3),
    ('Sunday',      1462,  227, 15.5, 59.0),
]

print(f'\n{"Day":<12} {"n cases":>10} {"n overtime":>12} {"OT rate":>10} {"Mean OT":>10}')
print('-' * 60)
total_n = total_ot = 0
for day, n, ot, pct, mean in weekday:
    print(f'{day:<12} {n:>10,} {ot:>12,} {pct:>9.1f}% {mean:>9.1f} min')
    total_n += n
    total_ot += ot
print('-' * 60)
print(f'{"Total":<12} {total_n:>10,} {total_ot:>12,} {total_ot/total_n*100:>9.1f}% {59.0:>9.1f} min')

year = [
    ('2022',     26103, 2297, 8.8, 60.6),
    ('2023',     28522, 2453, 8.6, 57.7),
    ('2024',     29223, 2396, 8.2, 59.6),
    ('2025*',    12196,  878, 7.2, 57.0),
]
print(f'\n{"Year":<12} {"n cases":>10} {"n overtime":>12} {"OT rate":>10} {"Mean OT":>10}')
print('-' * 60)
for yr, n, ot, pct, mean in year:
    print(f'{yr:<12} {n:>10,} {ot:>12,} {pct:>9.1f}% {mean:>9.1f} min')
print('-' * 60)
print(f'{"Total":<12} {96044:>10,} {8024:>12,} {8.4:>9.1f}% {59.0:>9.1f} min')
print('* 2025 data through May only.')

# =============================================================================
# TABLE 2 — Urgent vs elective overtime and overlap
# Sources: Tables 33, 35, 37, 38
# =============================================================================
print('\n' + '='*80)
print('TABLE 2 — Urgent vs elective overtime and overlap')
print('='*80)

print('\nPanel A. Overtime by urgency')
print(f'{"Urgency":<15} {"n":>10} {"Share":>8} {"After-hrs":>12} {"OT rate":>10} {"Mean OT":>10} {"P95 OT":>10}')
print('-' * 80)
print(f'{"Elective":<15} {"84,028":>10} {"87.5%":>8} {"5,859":>12} {"7.0%":>10} {"4.1 min":>10} {"18 min":>10}')
print(f'{"Non-elective":<15} {"12,016":>10} {"12.5%":>8} {"2,165":>12} {"18.0%":>10} {"10.5 min":>10} {"67.2 min":>10}')
print(f'{"Total":<15} {"96,044":>10} {"100%":>8} {"8,024":>12} {"8.4%":>10} {"—":>10} {"—":>10}')

print('\nPanel B. Urgent-elective overlap in the same room')
print(f'{"Days with overlap":<35} 869 / 1,247 (69.7%)')
print(f'{"Mean elective start delay":<35} +30 min on overlap days vs no-overlap days')
print(f'{"Highest-burden room (GO11)":<35} 485 events affecting 15.5% of its elective cases')
print(f'{"Median start delay at GO11":<35} 29 min (no overlap) vs 60 min (overlap)')

# =============================================================================
# SUPPLEMENTARY TABLE S1 — CV by planned-duration bucket
# Source: Table 13, p.13
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

print('\nAll figures saved to:', OUTDIR)
