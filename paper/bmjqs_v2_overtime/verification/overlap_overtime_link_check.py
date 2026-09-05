"""Exploratory check: do overlap-affected elective cases run more overtime?

STATUS: approximation, NOT a manuscript number. The overlap flag here is an
interval-intersection reconstruction (urgent case's actual room occupancy
intersecting an elective case's planned window in its planned room). It comes
close to but does not exactly match the flag used for the manuscript's overlap
statistics (this script: 854/1,247 days, 401 GO11 events; manuscript: 858 and
475), so the manuscript keeps the sentence that the overlap-to-overtime link
was not measured.

Ask for Maxim: rerun this comparison with the exact overlap flag from the
original R analysis. Approximate results with this flag:
  overlapped elective 11.3% overtime vs 8.2% unaffected;
  excluding GO11: 10.9% vs 8.2%;
  restricted to electives planned to fit their shift: 8.4% vs 4.5%.

Set DATA_PATH to genk_cleaned.xlsx before running.
"""

import os

import numpy as np
import pandas as pd

DATA_PATH = os.environ.get("DATA_PATH", "genk_cleaned.xlsx")


def main() -> None:
    df = pd.read_excel(DATA_PATH)
    for c in ["PlannedStartDT", "PlannedEndDT", "ORIn", "OROut"]:
        df[c] = pd.to_datetime(df[c])

    ele = df[df["UrgencyType"] == "electief"].copy()
    urg = df[df["UrgencyType"] == "niet-electief"].copy()

    urg_by_room = {r: g[["ORIn", "OROut"]].to_numpy() for r, g in urg.groupby("ActualOR")}
    flags = np.zeros(len(ele), dtype=bool)
    for room, g in ele.groupby("PlannedOR"):
        if room not in urg_by_room:
            continue
        ui, uo = urg_by_room[room][:, 0], urg_by_room[room][:, 1]
        idx = ele.index.get_indexer(g.index)
        s, e = g["PlannedStartDT"].to_numpy(), g["PlannedEndDT"].to_numpy()
        ov = (ui[None, :] < e[:, None]) & (uo[None, :] > s[:, None])
        flags[idx] = ov.any(axis=1)
    ele["overlap"] = flags

    ov_days = ele.loc[ele["overlap"], "ORIn"].dt.normalize().nunique()
    print(f"days with overlap (approx flag): {ov_days}/1247")
    g11 = ele[ele["PlannedOR"] == "GO11"]
    print(f"GO11 events (approx flag): {int(g11['overlap'].sum())} ({100 * g11['overlap'].mean():.1f}%)")

    ov, no = ele[ele["overlap"]], ele[~ele["overlap"]]
    print(f"overtime rate overlapped {100 * ov['afterhours_flag'].mean():.1f}% "
          f"vs unaffected {100 * no['afterhours_flag'].mean():.1f}%")
    sub = ele[ele["PlannedOR"] != "GO11"]
    print(f"excluding GO11: {100 * sub.loc[sub['overlap'], 'afterhours_flag'].mean():.1f}% "
          f"vs {100 * sub.loc[~sub['overlap'], 'afterhours_flag'].mean():.1f}%")
    ele["sched"] = ele["PlannedEndDT"] > ele["planned_shift_end"]
    unp = ele[~ele["sched"]]
    print(f"planned-to-fit electives: {100 * unp.loc[unp['overlap'], 'afterhours_flag'].mean():.1f}% "
          f"vs {100 * unp.loc[~unp['overlap'], 'afterhours_flag'].mean():.1f}%")


if __name__ == "__main__":
    main()
