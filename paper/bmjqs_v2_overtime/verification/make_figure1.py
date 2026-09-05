"""Figure 1 for the v3 manuscript: room-level overtime, scheduled vs unplanned.

Panel A: stacked bar of room-level overtime rate (unplanned base, scheduled on top),
rooms ranked lowest to highest total rate.
Panel B: mean overtime minutes per room (among overtime cases), same room order,
hospital average marked.

Scheduled crossing: PlannedEndDT > planned_shift_end (same rule as the
verification scripts). Overtime: afterhours_flag == 1.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

df = pd.read_pickle("/tmp/claude-0/-home-user-ZOL/0eab60bb-835d-5933-8a55-8388cc65e941/scratchpad/genk.pkl")
df["sched_cross"] = df["PlannedEndDT"] > df["planned_shift_end"]

g = df.groupby("ActualOR")
per_room = pd.DataFrame({
    "n": g.size(),
    "ot_rate": 100 * g["afterhours_flag"].mean(),
    "sched_rate": 100 * g.apply(lambda x: ((x["afterhours_flag"] == 1) & x["sched_cross"]).mean(), include_groups=False),
    "unpl_rate": 100 * g.apply(lambda x: ((x["afterhours_flag"] == 1) & ~x["sched_cross"]).mean(), include_groups=False),
    "mean_ot": g.apply(lambda x: x.loc[x["afterhours_flag"] == 1, "overtime_minutes"].mean(), include_groups=False),
}).sort_values("ot_rate")
per_room.index = [f"OR{ix[2:]}" for ix in per_room.index]  # GO10 -> OR10

hosp_mean_ot = df.loc[df["afterhours_flag"] == 1, "overtime_minutes"].mean()

DARK = "#184f95"   # scheduled crossings
LIGHT = "#86b6ef"  # unplanned overruns
INK = "#1a1a19"
MUTED = "#6b6a63"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": INK,
    "text.color": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.linewidth": 0.8,
})

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(7.2, 6.4), dpi=300, sharex=True,
    gridspec_kw={"height_ratios": [1.25, 1], "hspace": 0.28},
)

x = np.arange(len(per_room))

# Panel A: stacked rates. Unplanned at the base, scheduled on top; white linewidth
# gives the 2px-equivalent gap between segments and bars.
ax1.bar(x, per_room["unpl_rate"], width=0.72, color=LIGHT,
        edgecolor="white", linewidth=0.8, label="Unplanned overruns")
ax1.bar(x, per_room["sched_rate"], width=0.72, bottom=per_room["unpl_rate"],
        color=DARK, edgecolor="white", linewidth=0.8, label="Scheduled crossings")

for i, (total, sched, unpl) in enumerate(zip(per_room["ot_rate"], per_room["sched_rate"], per_room["unpl_rate"])):
    ax1.text(i, total + 0.6, f"{total:.1f}", ha="center", va="bottom",
             fontsize=7.5, color=INK)

ax1.set_ylabel("Cases with overtime (%)")
ax1.set_ylim(0, 36)
ax1.yaxis.set_major_locator(mticker.MultipleLocator(10))
handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles[::-1], labels[::-1], loc="upper left", frameon=False, fontsize=8.5)
ax1.grid(axis="y", color=MUTED, alpha=0.25, linewidth=0.6)
ax1.set_axisbelow(True)
for s in ("top", "right"):
    ax1.spines[s].set_visible(False)
ax1.set_title("A  Overtime rate per operating room, by component", loc="left",
              fontsize=10, fontweight="bold", pad=10)

# Panel B: mean overtime minutes among overtime cases.
ax2.bar(x, per_room["mean_ot"], width=0.72, color=DARK, edgecolor="white", linewidth=0.8)
ax2.axhline(hosp_mean_ot, color=MUTED, linewidth=1.0, linestyle=(0, (4, 3)))
ax2.text(-0.45, 162, f"Dashed line: hospital mean, {hosp_mean_ot:.0f} min",
         ha="left", va="top", fontsize=8, color=MUTED)
for i, m in enumerate(per_room["mean_ot"]):
    ax2.text(i, m + 3, f"{m:.0f}", ha="center", va="bottom", fontsize=7.5, color=INK)

ax2.set_ylabel("Mean overtime (min)")
ax2.set_ylim(0, 175)
ax2.yaxis.set_major_locator(mticker.MultipleLocator(50))
ax2.grid(axis="y", color=MUTED, alpha=0.25, linewidth=0.6)
ax2.set_axisbelow(True)
for s in ("top", "right"):
    ax2.spines[s].set_visible(False)
ax2.set_title("B  Mean overtime duration per operating room (overtime cases)",
              loc="left", fontsize=10, fontweight="bold", pad=10)

ax2.set_xticks(x)
ax2.set_xticklabels(per_room.index, rotation=45, ha="right", fontsize=8)
ax2.set_xlim(-0.6, len(per_room) - 0.4)

fig.savefig("/tmp/claude-0/-home-user-ZOL/0eab60bb-835d-5933-8a55-8388cc65e941/scratchpad/Figure1_v3.png",
            bbox_inches="tight", facecolor="white")
fig.savefig("/tmp/claude-0/-home-user-ZOL/0eab60bb-835d-5933-8a55-8388cc65e941/scratchpad/Figure1_v3.pdf",
            bbox_inches="tight", facecolor="white")

print(per_room.round(1).to_string())
print("hospital mean OT:", round(hosp_mean_ot, 1))
