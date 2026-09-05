"""Candidate Figure 2: room-level correlates of overtime (RQ2).

Panel A: mean inter-case gap vs overtime rate (Spearman rho = 0.89, p < 0.001).
Uses Maxim's denominator: each room's overtime rate computed among the cases
contributing gap data (gap_time not NA).
Panel B: late-start rate vs overtime rate (rho = -0.29, p = 0.24), overtime rate
over all cases per room, as reported elsewhere in the paper.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_pickle("/tmp/claude-0/-home-user-ZOL/0eab60bb-835d-5933-8a55-8388cc65e941/scratchpad/genk.pkl")

g = df.groupby("ActualOR")
rooms = pd.DataFrame({
    "late_rate": 100 * g.apply(lambda x: (x["start_diff"] > 0).mean(), include_groups=False),
    "ot_rate_all": 100 * g["afterhours_flag"].mean(),
    "mean_gap": g.apply(lambda x: x.loc[x["gap_time"].notna(), "gap_time"].mean(), include_groups=False),
    "ot_rate_gapsub": 100 * g.apply(
        lambda x: x.loc[x["gap_time"].notna(), "afterhours_flag"].mean(), include_groups=False),
})
rooms.index = [f"OR{ix[2:]}" for ix in rooms.index]

rho_gap, p_gap = stats.spearmanr(rooms["mean_gap"], rooms["ot_rate_gapsub"])
rho_late, p_late = stats.spearmanr(rooms["late_rate"], rooms["ot_rate_all"])
print(f"gap:  rho={rho_gap:.4f} p={p_gap:.2e}")
print(f"late: rho={rho_late:.4f} p={p_late:.4f}")

BLUE = "#256abf"
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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.5), dpi=300)

label_rooms = {"OR10", "OR14", "OR11", "OR09"}

for ax, xcol, ycol, rho, p, xlabel in (
    (ax1, "mean_gap", "ot_rate_gapsub", rho_gap, p_gap, "Mean inter-case gap (min)"),
    (ax2, "late_rate", "ot_rate_all", rho_late, p_late, "Cases starting late (%)"),
):
    ax.scatter(rooms[xcol], rooms[ycol], s=42, color=BLUE,
               edgecolors="white", linewidths=0.8, zorder=3)
    for name, row in rooms.iterrows():
        if name in label_rooms:
            dx, dy = (5, -10) if (ax is ax2 and name == "OR10") else (5, 4)
            ax.annotate(name, (row[xcol], row[ycol]),
                        xytext=(dx, dy), textcoords="offset points",
                        fontsize=7.5, color=MUTED)
    ptxt = "p < 0.001" if p < 0.001 else f"p = {p:.2f}"
    xy = (0.03, 0.97) if ax is ax1 else (0.03, 0.06)
    va = "top" if ax is ax1 else "bottom"
    ax.text(*xy, f"Spearman rho = {rho:.2f}, {ptxt}",
            transform=ax.transAxes, ha="left", va=va, fontsize=8.5, color=INK)
    ax.set_xlabel(xlabel)
    ax.grid(color=MUTED, alpha=0.2, linewidth=0.6)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)

ax1.set_ylabel("Cases with overtime (%)")
ax1.set_title("A  Inter-case gaps", loc="left", fontsize=10, fontweight="bold", pad=8)
ax2.set_title("B  Start-time punctuality", loc="left", fontsize=10, fontweight="bold", pad=8)

fig.tight_layout()
fig.savefig("/tmp/claude-0/-home-user-ZOL/0eab60bb-835d-5933-8a55-8388cc65e941/scratchpad/Figure2_candidate.png",
            bbox_inches="tight", facecolor="white")
fig.savefig("/tmp/claude-0/-home-user-ZOL/0eab60bb-835d-5933-8a55-8388cc65e941/scratchpad/Figure2_candidate.pdf",
            bbox_inches="tight", facecolor="white")
print("saved")
