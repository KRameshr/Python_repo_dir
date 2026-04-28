# """
# =======================================================
#   India Listed Hospital Stocks — Analysis Dashboard
#   Tools: pandas, numpy, matplotlib, seaborn, tabulate
# =======================================================
# """

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# import seaborn as sns
# from tabulate import tabulate
# import warnings
# warnings.filterwarnings("ignore")

# # ─────────────────────────────────────────────
# # 1. LOAD DATA
# # ─────────────────────────────────────────────
# def load_data():
#     data = {
#         "Name": [
#             "Apollo Hospitals", "Max Healthcare", "Fortis Healthcare",
#             "Aster DM Healthcare", "Narayana Hrudayalaya", "Global Health (Medanta)",
#             "KIMS", "Dr. Agarwal Health Care", "Rainbow Children's",
#             "Park Medi World", "HCG", "Jupiter Life Line",
#             "Yatharth Hospital", "Kovai Medical Center", "Nephrocare Health",
#             "Indraprastha Medical", "Dr Agarwal Eye Hospital", "Shalby Ltd"
#         ],
#         "Ticker": [
#             "APOLLOHOSP","MAXHEALTH","FORTIS","ASTERDM","NH","MEDANTA",
#             "KIMS","AGARWALEYE","RAINBOW","PARKHOSPS","HCG","JLHL",
#             "YATHARTH","KOVAI","NEPHROPLUS","INDRAMEDCO","DRAGARWQ","SHALBY"
#         ],
#         "MarketCap_Cr": [
#             111181,97261,70158,36457,35914,29700,
#             26057,13886,12602,10051,8501,8177,
#             6921,6169,5354,3726,2305,1670
#         ],
#         "Metro_pct": [78,95,92,65,45,85,60,70,80,75,70,90,55,20,60,100,65,40],
#         "NonMetro_pct": [22,5,8,35,55,15,40,30,20,25,30,10,45,80,40,0,35,60],
#         "ARPOB_day": [
#             63569,77000,66300,44000,43600,64000,
#             39200,28000,38500,26206,44500,60000,
#             30800,20173,18000,55000,22000,39000
#         ],
#         "ALOS_days": [3.06,3.20,3.40,3.50,3.80,3.30,3.60,1.50,2.80,3.20,4.00,3.50,4.20,3.80,4.50,3.20,1.00,3.50],
#         "Occupancy_pct": [67,74,69,65,51,65,50,55,62,62,60,65,61,60,58,68,52,47],
#         "EBITDA_Cr": [3022,1884,1570,808,1308,840,783,280,270,268,230,280,185,180,90,210,70,120],
#         "EV_EBITDA": [30,42,35,28,27,38,17,32,25,22,30,32,16,14,20,22,28,18],
#         "NetDebt_EBITDA": [0.4,-0.3,0.8,0.5,0.2,0.3,0.1,0.6,0.2,0.5,1.2,0.3,0.4,0.1,1.5,0.0,0.4,0.8],
#         "Capex_Cr": [2701,1100,1200,900,800,1500,600,500,350,400,350,500,250,150,120,200,150,180],
#     }
#     df = pd.DataFrame(data)
#     # Derived columns
#     df["ARPOB_annual_Cr"] = (df["ARPOB_day"] * 365 / 10_000_000).round(2)   # in Crores/bed/yr
#     df["MarketCap_Tier"] = pd.cut(
#         df["MarketCap_Cr"],
#         bins=[0, 10000, 50000, np.inf],
#         labels=["Small Cap (<10K Cr)", "Mid Cap (10K-50K Cr)", "Large Cap (>50K Cr)"]
#     )
#     df["Focus"] = df.apply(
#         lambda r: "Metro-Heavy" if r["Metro_pct"] >= 70 else ("Non-Metro-Heavy" if r["NonMetro_pct"] >= 50 else "Balanced"),
#         axis=1
#     )
#     return df

# # ─────────────────────────────────────────────
# # 2. PRINT FULL TABLE
# # ─────────────────────────────────────────────
# def print_full_table(df):
#     display = df[[
#         "Name","Ticker","MarketCap_Cr","Metro_pct","NonMetro_pct",
#         "ARPOB_day","ALOS_days","Occupancy_pct","EBITDA_Cr","EV_EBITDA","NetDebt_EBITDA","Capex_Cr"
#     ]].copy()
#     display.columns = [
#         "Hospital","Ticker","MktCap(Cr)","Metro%","NonMetro%",
#         "ARPOB(₹/d)","ALOS(d)","Occ%","EBITDA(Cr)","EV/EBITDA","NetDbt/EBITDA","Capex(Cr)"
#     ]
#     print("\n" + "═"*110)
#     print("  INDIA HOSPITAL STOCKS — FULL METRICS TABLE (FY25)")
#     print("═"*110)
#     print(tabulate(display, headers="keys", tablefmt="fancy_grid", showindex=False,
#                    floatfmt=".2f", numalign="right"))

# # ─────────────────────────────────────────────
# # 3. METRO vs NON-METRO COMPARISON TABLE
# # ─────────────────────────────────────────────
# def metro_nonmetro_comparison(df):
#     print("\n" + "═"*80)
#     print("  METRO vs NON-METRO FOCUS — GROUP COMPARISON")
#     print("═"*80)

#     groups = df.groupby("Focus").agg(
#         Count=("Name","count"),
#         Avg_ARPOB=("ARPOB_day","mean"),
#         Avg_Occupancy=("Occupancy_pct","mean"),
#         Avg_EBITDA=("EBITDA_Cr","mean"),
#         Avg_EV_EBITDA=("EV_EBITDA","mean"),
#         Avg_ALOS=("ALOS_days","mean"),
#         Total_MktCap=("MarketCap_Cr","sum"),
#     ).reset_index()
#     groups = groups.round(1)
#     print(tabulate(groups, headers="keys", tablefmt="fancy_grid", showindex=False, numalign="right"))

#     # Metro vs Non-Metro hospitals listing
#     print("\n  Metro-Heavy Hospitals (Metro% ≥ 70%):")
#     metro = df[df["Metro_pct"] >= 70][["Name","Metro_pct","ARPOB_day","Occupancy_pct","EV_EBITDA"]]
#     print(tabulate(metro, headers=["Hospital","Metro%","ARPOB(₹/d)","Occ%","EV/EBITDA"],
#                    tablefmt="simple", showindex=False, numalign="right"))

#     print("\n  Non-Metro-Heavy Hospitals (NonMetro% ≥ 50%):")
#     nonmetro = df[df["NonMetro_pct"] >= 50][["Name","NonMetro_pct","ARPOB_day","Occupancy_pct","EV_EBITDA"]]
#     print(tabulate(nonmetro, headers=["Hospital","NonMetro%","ARPOB(₹/d)","Occ%","EV/EBITDA"],
#                    tablefmt="simple", showindex=False, numalign="right"))

# # ─────────────────────────────────────────────
# # 4. KEY INSIGHTS (NUMPY STATS)
# # ─────────────────────────────────────────────
# def key_insights(df):
#     print("\n" + "═"*80)
#     print("  KEY STATISTICAL INSIGHTS (numpy)")
#     print("═"*80)

#     metrics = {
#         "ARPOB (₹/day)":    df["ARPOB_day"],
#         "Occupancy %":      df["Occupancy_pct"],
#         "EBITDA (₹ Cr)":   df["EBITDA_Cr"],
#         "EV/EBITDA (x)":   df["EV_EBITDA"],
#         "ALOS (days)":      df["ALOS_days"],
#     }
#     rows = []
#     for label, series in metrics.items():
#         rows.append([
#             label,
#             f"{np.mean(series):.1f}",
#             f"{np.median(series):.1f}",
#             f"{np.std(series):.1f}",
#             f"{np.min(series):.1f}",
#             f"{np.max(series):.1f}",
#         ])
#     print(tabulate(rows, headers=["Metric","Mean","Median","Std Dev","Min","Max"],
#                    tablefmt="fancy_grid", numalign="right"))

#     # Pearson correlation
#     corr = np.corrcoef(df["ARPOB_day"], df["Occupancy_pct"])[0,1]
#     print(f"\n  Correlation — ARPOB vs Occupancy:   r = {corr:.3f}")
#     corr2 = np.corrcoef(df["Metro_pct"], df["ARPOB_day"])[0,1]
#     print(f"    Correlation — Metro% vs ARPOB:       r = {corr2:.3f}")
#     corr3 = np.corrcoef(df["EV_EBITDA"], df["Occupancy_pct"])[0,1]
#     print(f"    Correlation — EV/EBITDA vs Occupancy: r = {corr3:.3f}")

#     top_arpob  = df.loc[df["ARPOB_day"].idxmax(), "Name"]
#     top_occ    = df.loc[df["Occupancy_pct"].idxmax(), "Name"]
#     top_margin = df.loc[df["EBITDA_Cr"].idxmax(), "Name"]
#     print(f"\n   Highest ARPOB:     {top_arpob}")
#     print(f"     Highest Occupancy: {top_occ}")
#     print(f"     Highest EBITDA:    {top_margin}")

# # ─────────────────────────────────────────────
# # 5. PLOTS
# # ─────────────────────────────────────────────
# def make_plots(df):
#     sns.set_theme(style="whitegrid", palette="muted")
#     fig = plt.figure(figsize=(22, 26))
#     fig.patch.set_facecolor("#F7F9FC")
#     fig.suptitle("India Hospital Stocks — Analytical Dashboard (FY25)",
#                  fontsize=18, fontweight="bold", color="#1F4E79", y=0.98)

#     colors_focus = {"Metro-Heavy": "#1F77B4", "Balanced": "#FF7F0E", "Non-Metro-Heavy": "#2CA02C"}
#     col_map = df["Focus"].map(colors_focus)

#     # ── Plot 1: ARPOB Bar Chart
#     ax1 = fig.add_subplot(4, 2, 1)
#     sorted_df = df.sort_values("ARPOB_day", ascending=True)
#     bars = ax1.barh(sorted_df["Name"], sorted_df["ARPOB_day"] / 1000,
#                     color=[colors_focus[f] for f in sorted_df["Focus"]], edgecolor="white")
#     ax1.set_xlabel("ARPOB (₹ '000 / day)", fontsize=9)
#     ax1.set_title("ARPOB by Hospital", fontweight="bold")
#     ax1.tick_params(axis="y", labelsize=7)
#     for bar, val in zip(bars, sorted_df["ARPOB_day"] / 1000):
#         ax1.text(val + 0.5, bar.get_y() + bar.get_height()/2, f"₹{val:.0f}K", va="center", fontsize=6.5)

#     # ── Plot 2: Occupancy Bar Chart
#     ax2 = fig.add_subplot(4, 2, 2)
#     sorted_occ = df.sort_values("Occupancy_pct", ascending=True)
#     bars2 = ax2.barh(sorted_occ["Name"], sorted_occ["Occupancy_pct"],
#                      color=[colors_focus[f] for f in sorted_occ["Focus"]], edgecolor="white")
#     ax2.set_xlabel("Occupancy (%)", fontsize=9)
#     ax2.set_title("Occupancy Rate by Hospital", fontweight="bold")
#     ax2.tick_params(axis="y", labelsize=7)
#     ax2.axvline(df["Occupancy_pct"].mean(), color="red", linestyle="--", linewidth=1, label=f"Avg {df['Occupancy_pct'].mean():.1f}%")
#     ax2.legend(fontsize=7)

#     # ── Plot 3: Metro vs Non-Metro Scatter (ARPOB vs Occupancy)
#     ax3 = fig.add_subplot(4, 2, 3)
#     for focus, grp in df.groupby("Focus"):
#         ax3.scatter(grp["ARPOB_day"]/1000, grp["Occupancy_pct"],
#                     label=focus, color=colors_focus[focus], s=80, edgecolors="white", linewidths=0.8)
#         for _, row in grp.iterrows():
#             ax3.annotate(row["Ticker"], (row["ARPOB_day"]/1000, row["Occupancy_pct"]),
#                          fontsize=6, xytext=(3, 3), textcoords="offset points")
#     ax3.set_xlabel("ARPOB (₹ '000 / day)", fontsize=9)
#     ax3.set_ylabel("Occupancy %", fontsize=9)
#     ax3.set_title("ARPOB vs Occupancy (Metro/Non-Metro)", fontweight="bold")
#     ax3.legend(fontsize=7)

#     # ── Plot 4: EV/EBITDA vs Market Cap
#     ax4 = fig.add_subplot(4, 2, 4)
#     scatter = ax4.scatter(df["MarketCap_Cr"]/1000, df["EV_EBITDA"],
#                           c=df["Occupancy_pct"], cmap="YlOrRd", s=df["EBITDA_Cr"]/20,
#                           edgecolors="gray", linewidths=0.5, alpha=0.85)
#     plt.colorbar(scatter, ax=ax4, label="Occupancy %")
#     for _, row in df.iterrows():
#         ax4.annotate(row["Ticker"], (row["MarketCap_Cr"]/1000, row["EV_EBITDA"]),
#                      fontsize=6, xytext=(3, 3), textcoords="offset points")
#     ax4.set_xlabel("Market Cap (₹ '000 Cr)", fontsize=9)
#     ax4.set_ylabel("EV/EBITDA (x)", fontsize=9)
#     ax4.set_title("Valuation vs Market Cap\n(bubble = EBITDA size, color = Occupancy)", fontweight="bold")

#     # ── Plot 5: Metro% vs NonMetro% Grouped Bar
#     ax5 = fig.add_subplot(4, 2, 5)
#     x = np.arange(len(df))
#     w = 0.4
#     ax5.bar(x - w/2, df["Metro_pct"], width=w, label="Metro %", color="#1F77B4", alpha=0.85)
#     ax5.bar(x + w/2, df["NonMetro_pct"], width=w, label="Non-Metro %", color="#2CA02C", alpha=0.85)
#     ax5.set_xticks(x)
#     ax5.set_xticklabels(df["Ticker"], rotation=45, ha="right", fontsize=7)
#     ax5.set_ylabel("Revenue Mix (%)", fontsize=9)
#     ax5.set_title("Metro vs Non-Metro Revenue Mix", fontweight="bold")
#     ax5.legend(fontsize=8)

#     # ── Plot 6: EBITDA vs Capex
#     ax6 = fig.add_subplot(4, 2, 6)
#     ax6.scatter(df["Capex_Cr"], df["EBITDA_Cr"],
#                 color=col_map, s=90, edgecolors="white", linewidths=0.8)
#     for _, row in df.iterrows():
#         ax6.annotate(row["Ticker"], (row["Capex_Cr"], row["EBITDA_Cr"]),
#                      fontsize=6, xytext=(4, 4), textcoords="offset points")
#     z = np.polyfit(df["Capex_Cr"], df["EBITDA_Cr"], 1)
#     p = np.poly1d(z)
#     xline = np.linspace(df["Capex_Cr"].min(), df["Capex_Cr"].max(), 100)
#     ax6.plot(xline, p(xline), "r--", linewidth=1, label="Trend")
#     ax6.set_xlabel("Capex (₹ Cr)", fontsize=9)
#     ax6.set_ylabel("EBITDA (₹ Cr)", fontsize=9)
#     ax6.set_title("Capex vs EBITDA", fontweight="bold")
#     ax6.legend(fontsize=7)

#     # ── Plot 7: ALOS by Focus Group Box Plot
#     ax7 = fig.add_subplot(4, 2, 7)
#     focus_groups = [df[df["Focus"] == f]["ALOS_days"].values for f in ["Metro-Heavy","Balanced","Non-Metro-Heavy"]]
#     bp = ax7.boxplot(focus_groups, labels=["Metro-Heavy","Balanced","Non-Metro-Heavy"],
#                      patch_artist=True, notch=False)
#     for patch, color in zip(bp["boxes"], ["#1F77B4","#FF7F0E","#2CA02C"]):
#         patch.set_facecolor(color)
#         patch.set_alpha(0.7)
#     ax7.set_ylabel("ALOS (days)", fontsize=9)
#     ax7.set_title("ALOS Distribution by Focus Group", fontweight="bold")

#     # ── Plot 8: Net Debt / EBITDA
#     ax8 = fig.add_subplot(4, 2, 8)
#     colors_debt = ["#D32F2F" if v > 1 else ("#FF9800" if v > 0 else "#388E3C") for v in df["NetDebt_EBITDA"]]
#     ax8.bar(df["Ticker"], df["NetDebt_EBITDA"], color=colors_debt, edgecolor="white")
#     ax8.axhline(0, color="black", linewidth=0.8)
#     ax8.axhline(1, color="red", linewidth=0.8, linestyle="--", label="Leverage Warning (1x)")
#     ax8.set_xticklabels(df["Ticker"], rotation=45, ha="right", fontsize=7)
#     ax8.set_ylabel("Net Debt / EBITDA", fontsize=9)
#     ax8.set_title("Leverage Profile", fontweight="bold")
#     ax8.legend(fontsize=7)
#     red_p = mpatches.Patch(color="#D32F2F", label=">1x (High)")
#     ora_p = mpatches.Patch(color="#FF9800", label="0-1x (Moderate)")
#     grn_p = mpatches.Patch(color="#388E3C", label="<0 (Net Cash)")
#     ax8.legend(handles=[red_p, ora_p, grn_p], fontsize=7)

#     plt.tight_layout(rect=[0, 0, 1, 0.97])
#     out = "DTTXHospitals_analysis.csv"
#     plt.savefig("hospital_dashboard.png", dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
#     plt.close()
#     print(f"\n   Dashboard saved → hospital_dashboard.png")

# # ─────────────────────────────────────────────
# # 6. EXPORT SUMMARY CSV
# # ─────────────────────────────────────────────
# def export_csv(df):
    
#     out = "DTTXHospitals_analysis.csv"
#     df.to_csv(out, index=False)
#     print(f"   Analysis CSV saved → DTTXHospitals_analysis.csv")

# # ─────────────────────────────────────────────
# # MAIN
# # ─────────────────────────────────────────────
# if __name__ == "__main__":
#     df = load_data()
#     print_full_table(df)
#     metro_nonmetro_comparison(df)
#     key_insights(df)
#     make_plots(df)
#     export_csv(df)
#     print("\n   All done!\n")

"""
=======================================================
  India Listed Hospital Stocks — Analysis Dashboard
  Tools: pandas, numpy, matplotlib, seaborn, tabulate
=======================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from tabulate import tabulate
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────────
def load_data():
    data = {
        "Name": [
            "Apollo Hospitals", "Max Healthcare", "Fortis Healthcare",
            "Aster DM Healthcare", "Narayana Hrudayalaya", "Global Health (Medanta)",
            "KIMS", "Dr. Agarwal Health Care", "Rainbow Children's",
            "Park Medi World", "HCG", "Jupiter Life Line",
            "Yatharth Hospital", "Kovai Medical Center", "Nephrocare Health",
            "Indraprastha Medical", "Dr Agarwal Eye Hospital", "Shalby Ltd"
        ],
        "Ticker": [
            "APOLLOHOSP","MAXHEALTH","FORTIS","ASTERDM","NH","MEDANTA",
            "KIMS","AGARWALEYE","RAINBOW","PARKHOSPS","HCG","JLHL",
            "YATHARTH","KOVAI","NEPHROPLUS","INDRAMEDCO","DRAGARWQ","SHALBY"
        ],
        "MarketCap_Cr": [
            111181,97261,70158,36457,35914,29700,
            26057,13886,12602,10051,8501,8177,
            6921,6169,5354,3726,2305,1670
        ],
        "Metro_pct": [78,95,92,65,45,85,60,70,80,75,70,90,55,20,60,100,65,40],
        "NonMetro_pct": [22,5,8,35,55,15,40,30,20,25,30,10,45,80,40,0,35,60],
        "ARPOB_day": [
            63569,77000,66300,44000,43600,64000,
            39200,28000,38500,26206,44500,60000,
            30800,20173,18000,55000,22000,39000
        ],
        "ALOS_days": [3.06,3.20,3.40,3.50,3.80,3.30,3.60,1.50,2.80,3.20,4.00,3.50,4.20,3.80,4.50,3.20,1.00,3.50],
        "Occupancy_pct": [67,74,69,65,51,65,50,55,62,62,60,65,61,60,58,68,52,47],
        "EBITDA_Cr": [3022,1884,1570,808,1308,840,783,280,270,268,230,280,185,180,90,210,70,120],
        "EV_EBITDA": [30,42,35,28,27,38,17,32,25,22,30,32,16,14,20,22,28,18],
        "NetDebt_EBITDA": [0.4,-0.3,0.8,0.5,0.2,0.3,0.1,0.6,0.2,0.5,1.2,0.3,0.4,0.1,1.5,0.0,0.4,0.8],
        "Capex_Cr": [2701,1100,1200,900,800,1500,600,500,350,400,350,500,250,150,120,200,150,180],
    }
    df = pd.DataFrame(data)
    df["ARPOB_annual_Cr"] = (df["ARPOB_day"] * 365 / 10_000_000).round(2)
    df["MarketCap_Tier"] = pd.cut(
        df["MarketCap_Cr"],
        bins=[0, 10000, 50000, np.inf],
        labels=["Small Cap (<10K Cr)", "Mid Cap (10K-50K Cr)", "Large Cap (>50K Cr)"]
    )
    df["Focus"] = df.apply(
        lambda r: "Metro-Heavy" if r["Metro_pct"] >= 70 else ("Non-Metro-Heavy" if r["NonMetro_pct"] >= 50 else "Balanced"),
        axis=1
    )
    return df

# ─────────────────────────────────────────────
# 2. PRINT FULL TABLE
# ─────────────────────────────────────────────
def print_full_table(df):
    display = df[[
        "Name","Ticker","MarketCap_Cr","Metro_pct","NonMetro_pct",
        "ARPOB_day","ALOS_days","Occupancy_pct","EBITDA_Cr","EV_EBITDA","NetDebt_EBITDA","Capex_Cr"
    ]].copy()
    display.columns = [
        "Hospital","Ticker","MktCap(Cr)","Metro%","NonMetro%",
        "ARPOB(Rs/d)","ALOS(d)","Occ%","EBITDA(Cr)","EV/EBITDA","NetDbt/EBITDA","Capex(Cr)"
    ]
    print("\n" + "="*110)
    print("  INDIA HOSPITAL STOCKS — FULL METRICS TABLE (FY25)")
    print("="*110)
    print(tabulate(display, headers="keys", tablefmt="fancy_grid", showindex=False,
                   floatfmt=".2f", numalign="right"))

# ─────────────────────────────────────────────
# 3. METRO vs NON-METRO COMPARISON TABLE
# ─────────────────────────────────────────────
def metro_nonmetro_comparison(df):
    print("\n" + "="*80)
    print("  METRO vs NON-METRO FOCUS — GROUP COMPARISON")
    print("="*80)

    groups = df.groupby("Focus").agg(
        Count=("Name","count"),
        Avg_ARPOB=("ARPOB_day","mean"),
        Avg_Occupancy=("Occupancy_pct","mean"),
        Avg_EBITDA=("EBITDA_Cr","mean"),
        Avg_EV_EBITDA=("EV_EBITDA","mean"),
        Avg_ALOS=("ALOS_days","mean"),
        Total_MktCap=("MarketCap_Cr","sum"),
    ).reset_index()
    groups = groups.round(1)
    print(tabulate(groups, headers="keys", tablefmt="fancy_grid", showindex=False, numalign="right"))

    print("\n  Metro-Heavy Hospitals (Metro% >= 70%):")
    metro = df[df["Metro_pct"] >= 70][["Name","Metro_pct","ARPOB_day","Occupancy_pct","EV_EBITDA"]]
    print(tabulate(metro, headers=["Hospital","Metro%","ARPOB(Rs/d)","Occ%","EV/EBITDA"],
                   tablefmt="simple", showindex=False, numalign="right"))

    print("\n  Non-Metro-Heavy Hospitals (NonMetro% >= 50%):")
    nonmetro = df[df["NonMetro_pct"] >= 50][["Name","NonMetro_pct","ARPOB_day","Occupancy_pct","EV_EBITDA"]]
    print(tabulate(nonmetro, headers=["Hospital","NonMetro%","ARPOB(Rs/d)","Occ%","EV/EBITDA"],
                   tablefmt="simple", showindex=False, numalign="right"))

# ─────────────────────────────────────────────
# 4. KEY INSIGHTS (NUMPY STATS)
# ─────────────────────────────────────────────
def key_insights(df):
    print("\n" + "="*80)
    print("  KEY STATISTICAL INSIGHTS (numpy)")
    print("="*80)

    metrics = {
        "ARPOB (Rs/day)":  df["ARPOB_day"],
        "Occupancy %":     df["Occupancy_pct"],
        "EBITDA (Rs Cr)":  df["EBITDA_Cr"],
        "EV/EBITDA (x)":  df["EV_EBITDA"],
        "ALOS (days)":     df["ALOS_days"],
    }
    rows = []
    for label, series in metrics.items():
        rows.append([label,
                     f"{np.mean(series):.1f}",
                     f"{np.median(series):.1f}",
                     f"{np.std(series):.1f}",
                     f"{np.min(series):.1f}",
                     f"{np.max(series):.1f}"])
    print(tabulate(rows, headers=["Metric","Mean","Median","Std Dev","Min","Max"],
                   tablefmt="fancy_grid", numalign="right"))

    corr  = np.corrcoef(df["ARPOB_day"],  df["Occupancy_pct"])[0,1]
    corr2 = np.corrcoef(df["Metro_pct"],  df["ARPOB_day"])[0,1]
    corr3 = np.corrcoef(df["EV_EBITDA"],  df["Occupancy_pct"])[0,1]
    print(f"\n  Correlation — ARPOB vs Occupancy:    r = {corr:.3f}")
    print(f"  Correlation — Metro% vs ARPOB:        r = {corr2:.3f}")
    print(f"  Correlation — EV/EBITDA vs Occupancy: r = {corr3:.3f}")
    print(f"\n  Highest ARPOB:     {df.loc[df['ARPOB_day'].idxmax(), 'Name']}")
    print(f"  Highest Occupancy: {df.loc[df['Occupancy_pct'].idxmax(), 'Name']}")
    print(f"  Highest EBITDA:    {df.loc[df['EBITDA_Cr'].idxmax(), 'Name']}")

# ─────────────────────────────────────────────
# 5. INDIVIDUAL CHARTS — 8 separate PNG files
# ─────────────────────────────────────────────
def save_chart(fig, filename):
    fig.savefig(filename, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  Saved --> {filename}")

def make_plots(df):
    sns.set_theme(style="whitegrid", palette="muted")
    colors_focus = {
        "Metro-Heavy":     "#1F77B4",
        "Balanced":        "#FF7F0E",
        "Non-Metro-Heavy": "#2CA02C"
    }
    col_map = df["Focus"].map(colors_focus)

    # ── Chart 1: ARPOB Bar Chart ──────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("#F7F9FC")
    sorted_df = df.sort_values("ARPOB_day", ascending=True)
    bars = ax.barh(sorted_df["Name"], sorted_df["ARPOB_day"] / 1000,
                   color=[colors_focus[f] for f in sorted_df["Focus"]], edgecolor="white")
    for bar, val in zip(bars, sorted_df["ARPOB_day"] / 1000):
        ax.text(val + 0.3, bar.get_y() + bar.get_height()/2,
                f"Rs{val:.0f}K", va="center", fontsize=7)
    ax.set_xlabel("ARPOB (Rs '000 / day)", fontsize=10)
    ax.set_title("Chart 1 — ARPOB by Hospital", fontweight="bold", fontsize=13)
    ax.tick_params(axis="y", labelsize=8)
    patches = [mpatches.Patch(color=v, label=k) for k, v in colors_focus.items()]
    ax.legend(handles=patches, fontsize=8)
    save_chart(fig, "chart1_ARPOB.png")

    # ── Chart 2: Occupancy Rate ───────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("#F7F9FC")
    sorted_occ = df.sort_values("Occupancy_pct", ascending=True)
    ax.barh(sorted_occ["Name"], sorted_occ["Occupancy_pct"],
            color=[colors_focus[f] for f in sorted_occ["Focus"]], edgecolor="white")
    ax.axvline(df["Occupancy_pct"].mean(), color="red", linestyle="--", linewidth=1.2,
               label=f"Avg {df['Occupancy_pct'].mean():.1f}%")
    ax.set_xlabel("Occupancy (%)", fontsize=10)
    ax.set_title("Chart 2 — Occupancy Rate by Hospital", fontweight="bold", fontsize=13)
    ax.tick_params(axis="y", labelsize=8)
    ax.legend(fontsize=8)
    save_chart(fig, "chart2_Occupancy.png")

    # ── Chart 3: ARPOB vs Occupancy Scatter ──────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor("#F7F9FC")
    for focus, grp in df.groupby("Focus"):
        ax.scatter(grp["ARPOB_day"]/1000, grp["Occupancy_pct"],
                   label=focus, color=colors_focus[focus],
                   s=90, edgecolors="white", linewidths=0.8)
        for _, row in grp.iterrows():
            ax.annotate(row["Ticker"], (row["ARPOB_day"]/1000, row["Occupancy_pct"]),
                        fontsize=7, xytext=(4, 4), textcoords="offset points")
    ax.set_xlabel("ARPOB (Rs '000 / day)", fontsize=10)
    ax.set_ylabel("Occupancy %", fontsize=10)
    ax.set_title("Chart 3 — ARPOB vs Occupancy (Metro / Non-Metro)", fontweight="bold", fontsize=13)
    ax.legend(fontsize=9)
    save_chart(fig, "chart3_ARPOB_vs_Occupancy.png")

    # ── Chart 4: EV/EBITDA vs Market Cap Bubble ───────────────────────────
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor("#F7F9FC")
    sc = ax.scatter(df["MarketCap_Cr"]/1000, df["EV_EBITDA"],
                    c=df["Occupancy_pct"], cmap="YlOrRd",
                    s=df["EBITDA_Cr"]/20, edgecolors="gray",
                    linewidths=0.5, alpha=0.85)
    plt.colorbar(sc, ax=ax, label="Occupancy %")
    for _, row in df.iterrows():
        ax.annotate(row["Ticker"], (row["MarketCap_Cr"]/1000, row["EV_EBITDA"]),
                    fontsize=7, xytext=(4, 4), textcoords="offset points")
    ax.set_xlabel("Market Cap (Rs '000 Cr)", fontsize=10)
    ax.set_ylabel("EV/EBITDA (x)", fontsize=10)
    ax.set_title("Chart 4 — Valuation vs Market Cap\n(bubble = EBITDA size, color = Occupancy)",
                 fontweight="bold", fontsize=13)
    save_chart(fig, "chart4_Valuation_Bubble.png")

    # ── Chart 5: Metro vs Non-Metro Revenue Mix ───────────────────────────
    fig, ax = plt.subplots(figsize=(13, 6))
    fig.patch.set_facecolor("#F7F9FC")
    x = np.arange(len(df))
    w = 0.4
    ax.bar(x - w/2, df["Metro_pct"],    width=w, label="Metro %",     color="#1F77B4", alpha=0.85)
    ax.bar(x + w/2, df["NonMetro_pct"], width=w, label="Non-Metro %", color="#2CA02C", alpha=0.85)
    ax.set_xticks(x)
    ax.set_xticklabels(df["Ticker"], rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Revenue Mix (%)", fontsize=10)
    ax.set_title("Chart 5 — Metro vs Non-Metro Revenue Mix", fontweight="bold", fontsize=13)
    ax.legend(fontsize=9)
    save_chart(fig, "chart5_Metro_vs_NonMetro.png")

    # ── Chart 6: Capex vs EBITDA ──────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor("#F7F9FC")
    ax.scatter(df["Capex_Cr"], df["EBITDA_Cr"],
               color=col_map, s=90, edgecolors="white", linewidths=0.8)
    for _, row in df.iterrows():
        ax.annotate(row["Ticker"], (row["Capex_Cr"], row["EBITDA_Cr"]),
                    fontsize=7, xytext=(4, 4), textcoords="offset points")
    z = np.polyfit(df["Capex_Cr"], df["EBITDA_Cr"], 1)
    xline = np.linspace(df["Capex_Cr"].min(), df["Capex_Cr"].max(), 100)
    ax.plot(xline, np.poly1d(z)(xline), "r--", linewidth=1.2, label="Trend")
    ax.set_xlabel("Capex (Rs Cr)", fontsize=10)
    ax.set_ylabel("EBITDA (Rs Cr)", fontsize=10)
    ax.set_title("Chart 6 — Capex vs EBITDA", fontweight="bold", fontsize=13)
    ax.legend(fontsize=9)
    save_chart(fig, "chart6_Capex_vs_EBITDA.png")

    # ── Chart 7: ALOS Box Plot ────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor("#F7F9FC")
    focus_groups = [df[df["Focus"] == f]["ALOS_days"].values
                    for f in ["Metro-Heavy", "Balanced", "Non-Metro-Heavy"]]
    bp = ax.boxplot(focus_groups, labels=["Metro-Heavy", "Balanced", "Non-Metro-Heavy"],
                    patch_artist=True, notch=False)
    for patch, color in zip(bp["boxes"], ["#1F77B4", "#FF7F0E", "#2CA02C"]):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    ax.set_ylabel("ALOS (days)", fontsize=10)
    ax.set_title("Chart 7 — ALOS Distribution by Focus Group", fontweight="bold", fontsize=13)
    save_chart(fig, "chart7_ALOS_Boxplot.png")

    # ── Chart 8: Leverage Profile ─────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(13, 6))
    fig.patch.set_facecolor("#F7F9FC")
    colors_debt = ["#D32F2F" if v > 1 else ("#FF9800" if v > 0 else "#388E3C")
                   for v in df["NetDebt_EBITDA"]]
    ax.bar(df["Ticker"], df["NetDebt_EBITDA"], color=colors_debt, edgecolor="white")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axhline(1, color="red",   linewidth=1,   linestyle="--")
    ax.set_xticks(range(len(df["Ticker"])))
    ax.set_xticklabels(df["Ticker"], rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Net Debt / EBITDA", fontsize=10)
    ax.set_title("Chart 8 — Leverage Profile (Net Debt / EBITDA)", fontweight="bold", fontsize=13)
    patches = [
        mpatches.Patch(color="#D32F2F", label=">1x  High Leverage"),
        mpatches.Patch(color="#FF9800", label="0-1x Moderate"),
        mpatches.Patch(color="#388E3C", label="<0   Net Cash"),
    ]
    ax.legend(handles=patches, fontsize=8)
    save_chart(fig, "chart8_Leverage.png")

# ─────────────────────────────────────────────
# 6. EXPORT SUMMARY CSV
# ─────────────────────────────────────────────
def export_csv(df):
    out = "DTTXHospitals_analysis.csv"
    df.to_csv(out, index=False)
    print(f"  Saved --> {out}")

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    df = load_data()
    print_full_table(df)
    metro_nonmetro_comparison(df)
    key_insights(df)
    print("\n  Saving 8 individual charts...")
    make_plots(df)
    export_csv(df)
    print("\n  All done! 8 PNG charts + 1 CSV saved in your project folder.\n")