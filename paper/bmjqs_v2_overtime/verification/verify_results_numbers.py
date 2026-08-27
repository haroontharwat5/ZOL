"""Independent verification of the Results numbers in the ZOL overtime manuscript.

Reproduces every reported statistic from the cleaned Genk extract
(genk_cleaned.xlsx, 79,352 rows). The data file is NOT in this repository;
set DATA_PATH before running. Verified 25 Aug 2026: all checks pass, and the
overtime flag reconstruction matches the stored flag on 100.0000% of cases.

Key definitional facts confirmed against the data:
- Shift assignment by room-in time: day = from 07:30 (not 08:00 as an early
  draft said), evening = from 16:30, night = from 22:00. Shift ends: 16:30,
  22:00, 08:00. Overtime = room-out after assigned shift end.
- Inter-case idle time (gap_time) is day-shift only, includes the gap from
  shift start to the first case, and excludes gaps > 60 min.
- Idle-vs-overtime correlation: Spearman rho = 0.913 (all cases per room) or
  0.891 on the gap-defined subset (matches Maxim's R output 0.8906089).
  Excluding GO10 the association persists (rho = 0.90 / 0.87), refuting the
  earlier draft claim that it "did not hold".
"""

import os
import pandas as pd
from scipy.stats import spearmanr

DATA_PATH = os.environ.get("DATA_PATH", "genk_cleaned.xlsx")


def main() -> None:
    df = pd.read_excel(DATA_PATH)
    assert len(df) == 79352, len(df)

    # 1. Overtime flag reconstruction (day boundary 07:30)
    d = df.dropna(subset=["ORIn", "OROut"]).copy()
    d["ORIn"] = pd.to_datetime(d["ORIn"])
    d["OROut"] = pd.to_datetime(d["OROut"])
    t = d["ORIn"].dt.hour * 60 + d["ORIn"].dt.minute
    day = (t >= 450) & (t < 990)
    eve = (t >= 990) & (t < 1320)
    night = ~(day | eve)
    base = d["ORIn"].dt.normalize()
    end = pd.Series(pd.NaT, index=d.index)
    end[day] = base[day] + pd.Timedelta(minutes=990)
    end[eve] = base[eve] + pd.Timedelta(minutes=1320)
    late_n = night & (t >= 1320)
    early_n = night & (t < 450)
    end[late_n] = base[late_n] + pd.Timedelta(days=1, minutes=480)
    end[early_n] = base[early_n] + pd.Timedelta(minutes=480)
    flag = (d["OROut"] > end).astype(int)
    agree = (flag == d["afterhours_flag"]).mean()
    print(f"flag reconstruction agreement: {agree:.4%}")
    assert agree == 1.0

    # 2. Headline stats
    ot = df.loc[df["afterhours_flag"] == 1, "overtime_minutes"]
    print(f"overtime: n={len(ot)} rate={len(ot)/len(df):.1%} "
          f"mean={ot.mean():.1f} median={ot.median():.0f} P95={ot.quantile(.95):.0f}")
    assert len(ot) == 7729

    # 3. Punctuality correlation (all cases per room)
    rooms = df.groupby("ActualOR").agg(
        late=("start_diff", lambda s: (s > 0).mean()),
        rate=("afterhours_flag", "mean"),
        gap=("gap_time", "mean"),
        n=("afterhours_flag", "size"),
    )
    main18 = rooms[rooms["n"] > 500]
    rho, p = spearmanr(main18["late"], main18["rate"])
    print(f"punctuality: rho={rho:.2f} p={p:.2f}")   # -0.29, 0.24

    # 4. Idle correlation, full-sample rates, with and without GO10
    rho_a, p_a = spearmanr(main18["gap"], main18["rate"])
    no10 = main18.drop("GO10")
    rho_b, p_b = spearmanr(no10["gap"], no10["rate"])
    print(f"idle vs overtime: rho={rho_a:.2f} (p={p_a:.2g}); "
          f"excl GO10 rho={rho_b:.2f} (p={p_b:.2g})")

    # 5. Idle correlation on the gap-defined subset (Maxim's variant)
    sub = df[df["gap_time"].notna()].groupby("ActualOR").agg(
        gap=("gap_time", "mean"), rate=("afterhours_flag", "mean"),
        n=("afterhours_flag", "size"))
    rho_m, _ = spearmanr(sub["gap"], sub["rate"])
    print(f"idle (gap-defined subset): rho={rho_m:.7f}  # Maxim's R: 0.8906089")


if __name__ == "__main__":
    main()


def decomposition() -> None:
    """Scheduled-crossing vs unplanned overtime decomposition (26 Aug).

    New analysis completed from variables data_cleaning.R already builds
    (PlannedEndDT vs planned_shift_end). Awaiting team sign-off before the
    numbers enter the manuscript.
    """
    df = pd.read_excel(DATA_PATH)
    d = df.dropna(subset=["PlannedEndDT", "planned_shift_end"]).copy()
    d["PlannedEndDT"] = pd.to_datetime(d["PlannedEndDT"])
    d["planned_shift_end"] = pd.to_datetime(d["planned_shift_end"])
    d["planned_over"] = d["PlannedEndDT"] > d["planned_shift_end"]
    po = d["planned_over"]
    print(f"planned to cross: {po.sum()} of {len(d)} ({100*po.mean():.1f}%)")       # 5812, 7.3%
    ot = d[d["afterhours_flag"] == 1]
    print(f"overtime cases planned to cross: {ot['planned_over'].sum()} of {len(ot)}"
          f" ({100*ot['planned_over'].mean():.1f}%)")                                # 3532, 45.7%
    for name, g in [("scheduled", ot[ot.planned_over]), ("unplanned", ot[~ot.planned_over])]:
        m = g["overtime_minutes"]
        print(f"  {name}: n={len(g)} mean={m.mean():.1f} median={m.median():.0f} "
              f"minutes={m.sum():.0f} ({100*m.sum()/ot['overtime_minutes'].sum():.1f}%)")
    # conversion: planned-to-fit 5.7% -> planned-to-cross 60.8%
    fit = d[~po]
    print(f"overtime risk: planned-to-fit {100*fit['afterhours_flag'].mean():.1f}% vs "
          f"planned-to-cross {100*d.loc[po,'afterhours_flag'].mean():.1f}%")
    go10 = ot[ot["ActualOR"] == "GO10"]
    print(f"GO10 overtime cases scheduled share: {100*go10['planned_over'].mean():.1f}%")  # 81.5%
