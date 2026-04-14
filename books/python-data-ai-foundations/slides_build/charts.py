"""Editorial-strict matplotlib charts. Output PNG 300dpi to _charts/."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams

from . import theme as T


def _editorial_style():
    # CJK-capable font, fallback chain
    rcParams["font.sans-serif"] = [
        "Noto Sans CJK TC", "Noto Sans TC",
        "Microsoft JhengHei", "DejaVu Sans",
    ]
    rcParams["font.family"] = "sans-serif"
    rcParams["axes.unicode_minus"] = False
    rcParams["axes.spines.top"] = False
    rcParams["axes.spines.right"] = False
    rcParams["axes.grid"] = False
    rcParams["axes.edgecolor"] = T.HEX_CHARCOAL
    rcParams["xtick.color"] = T.HEX_CHARCOAL
    rcParams["ytick.color"] = T.HEX_CHARCOAL
    rcParams["axes.labelcolor"] = T.HEX_CHARCOAL
    rcParams["font.size"] = 10


def line_chart_s3(outfile: Path = None) -> Path:
    """S3: three-line usage chart 2019-2025 with 2023 reference line."""
    _editorial_style()
    years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
    ai_ml = [41, 48, 54, 62, 69, 74, 78]
    ds = [52, 58, 63, 68, 71, 73, 75]
    de = [28, 34, 40, 46, 52, 58, 63]

    fig, ax = plt.subplots(figsize=(10.5, 5.0))
    ax.plot(years, ai_ml, color=T.HEX_PRIMARY, linewidth=2.5, marker="o",
            markersize=5, label="AI / ML")
    ax.plot(years, ds, color=T.HEX_CHARCOAL, linewidth=2.0, marker="o",
            markersize=5, label="Data Science")
    ax.plot(years, de, color=T.HEX_LIGHT_GRAY, linewidth=2.0, linestyle="--",
            marker="o", markersize=5, label="Data Engineering")

    # End-of-line labels (no legend box)
    ax.annotate("AI / ML", xy=(2025, 78), xytext=(6, 0), textcoords="offset points",
                color=T.HEX_PRIMARY, fontsize=10, fontweight="bold",
                va="center")
    ax.annotate("Data Science", xy=(2025, 75), xytext=(6, -2),
                textcoords="offset points",
                color=T.HEX_CHARCOAL, fontsize=10, fontweight="bold", va="center")
    ax.annotate("Data Engineering", xy=(2025, 63), xytext=(6, 0),
                textcoords="offset points",
                color=T.HEX_GRAY_MID, fontsize=10, fontweight="bold", va="center")

    # Direct value labels on key points
    for x, y in zip(years, ai_ml):
        ax.text(x, y + 2.5, str(y), color=T.HEX_PRIMARY, fontsize=8,
                ha="center", fontweight="bold")

    # 2023 reference line (dividing rule — Visual Grammar §10.2 time_split)
    ax.axvline(x=2023, color=T.HEX_GRAY_MID, linestyle="--", linewidth=1.3)
    ax.text(2023, 90, "分水嶺 · pandas 2.0 / PyTorch 2.0 釋出",
            color=T.HEX_GRAY_MID, fontsize=8.5, ha="center", style="italic")

    # Guidance layer: call-out arrow pointing to AI/ML 2025 terminal + thesis
    ax.annotate(
        "已跨越 75% 基礎設施門檻",
        xy=(2025, 78), xytext=(2023.3, 35),
        color=T.HEX_PRIMARY, fontsize=10, fontweight="bold",
        ha="left",
        arrowprops=dict(arrowstyle="->", color=T.HEX_PRIMARY, lw=1.5,
                        connectionstyle="arc3,rad=-0.15"),
    )
    # Insight badge: +37pp since 2019
    ax.text(2019.1, 46, "AI/ML 2019→2025\n+37pp", color=T.HEX_PRIMARY,
            fontsize=9, fontweight="bold", va="center",
            bbox=dict(boxstyle="round,pad=0.35", fc="white",
                      ec=T.HEX_PRIMARY, lw=1.2))

    ax.set_xlim(2018.5, 2026.8)
    ax.set_ylim(0, 92)
    ax.set_ylabel("企業工作場景使用率 (%)", fontsize=10)
    ax.set_xlabel("")
    ax.set_xticks(years)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "s3_line.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close()
    return outfile


def before_after_bars_s6(outfile: Path = None) -> Path:
    """S6: two horizontal bar charts stacked vertically."""
    _editorial_style()
    skills = ["Python", "SQL", "R", "Excel"]
    before = [64, 58, 22, 19]
    after = [87, 71, 9, 8]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10.5, 5.2), sharex=True)

    for ax, data, title in [(ax1, before, "Before（2023 Q2）"),
                             (ax2, after, "After（2025 Q4）")]:
        bars = ax.barh(skills, data, color=T.HEX_PRIMARY, height=0.55)
        ax.set_xlim(0, 100)
        ax.invert_yaxis()
        for bar, val in zip(bars, data):
            ax.text(val + 1.5, bar.get_y() + bar.get_height() / 2, f"{val}%",
                    va="center", fontsize=9, color=T.HEX_CHARCOAL, fontweight="bold")
        ax.set_title(title, loc="left", fontsize=10, color=T.HEX_CHARCOAL,
                     fontweight="bold", pad=6)
        ax.tick_params(axis="y", length=0)

    ax2.set_xlabel("AI 相關職缺要求率 (%)", fontsize=9, color=T.HEX_CHARCOAL)

    # Delta annotation between (Insight layer — inverted emphasis pill)
    fig.text(0.52, 0.50, "Python +23pp     R + Excel 合計 -24pp",
             fontsize=11, color="white", fontweight="bold", ha="center",
             bbox=dict(boxstyle="round,pad=0.5", fc=T.HEX_PRIMARY,
                       ec="none"))

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "s6_before_after.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close()
    return outfile


def stacked_bar_m1s1(outfile: Path = None) -> Path:
    """M1-S1: single 100% horizontal stacked bar of data analyst time split."""
    _editorial_style()
    segments = [
        ("資料清理", 60, T.HEX_PRIMARY, "#FFFFFF"),
        ("資料理解 / 探索", 20, "#498F6F", "#FFFFFF"),
        ("建模 / 分析", 10, T.HEX_LIGHT_GRAY, T.HEX_CHARCOAL),
        ("視覺化", 6, "#E5E5E5", T.HEX_CHARCOAL),
        ("溝通結論", 4, "#EFEFEF", T.HEX_CHARCOAL),
    ]

    fig, ax = plt.subplots(figsize=(11.0, 2.8))
    left = 0
    for label, val, color, txtcolor in segments:
        ax.barh([0], [val], left=left, color=color, height=0.55, edgecolor="white",
                linewidth=0.8)
        ax.text(left + val / 2, 0, f"{label}\n{val}%", ha="center", va="center",
                color=txtcolor, fontsize=9, fontweight="bold")
        left += val

    # Guidance layer: arrow + call-out pointing to 60% 資料清理 segment
    ax.annotate(
        "主戰場 · 60% 工時在此",
        xy=(30, 0.35), xytext=(30, 0.78),
        color=T.HEX_PRIMARY, fontsize=11, fontweight="bold",
        ha="center",
        arrowprops=dict(arrowstyle="->", color=T.HEX_PRIMARY, lw=1.5),
    )

    ax.set_xlim(0, 100)
    ax.set_ylim(-0.8, 1.0)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"], fontsize=8,
                       color=T.HEX_CHARCOAL)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color(T.HEX_CHARCOAL)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m1s1_stacked.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close()
    return outfile


def grouped_bar_m1s10(outfile: Path = None) -> Path:
    """M1-S10: Restart & Run All success rate — 3 categories × 2 bars."""
    _editorial_style()
    import numpy as np
    cats = ["個人練習", "團隊專案", "正式交付"]
    without = [34, 12, 4]
    with_rra = [89, 76, 71]
    deltas = ["(+55pp)", "(+64pp)", "(+67pp)"]

    x = np.arange(len(cats))
    w = 0.36

    fig, ax = plt.subplots(figsize=(10.5, 4.8))
    b1 = ax.bar(x - w/2, without, w, color=T.HEX_LIGHT_GRAY,
                 label="不做 Restart & Run All", edgecolor=T.HEX_CHARCOAL,
                 linewidth=0.6)
    b2 = ax.bar(x + w/2, with_rra, w, color=T.HEX_PRIMARY,
                 label="每日做 Restart & Run All")

    for bars in [b1, b2]:
        for bar in bars:
            v = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, v + 2, f"{int(v)}%",
                    ha="center", fontsize=9, color=T.HEX_CHARCOAL,
                    fontweight="bold")

    for i, d in enumerate(deltas):
        ax.text(x[i], max(with_rra[i], without[i]) + 9, d,
                fontsize=10, color=T.HEX_PRIMARY, fontweight="bold",
                ha="center",
                bbox=dict(boxstyle="round,pad=0.25", fc="white",
                          ec=T.HEX_PRIMARY, lw=1.0))

    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=10, color=T.HEX_CHARCOAL)
    ax.set_ylim(0, 100)
    ax.set_ylabel("成功一次跑完的比率 (%)", fontsize=9, color=T.HEX_CHARCOAL)
    ax.legend(loc="upper left", frameon=False, fontsize=9)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m1s10_grouped.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close()
    return outfile


def notebook_run_all_chart_m1s10(outfile: Path = None) -> Path:
    """M1-S10: small chart of notebook Restart & Run All success rate (illustrative)."""
    _editorial_style()
    labels = ["未加紀律", "加 seed + 相對路徑", "加 requirements.txt", "三項全加"]
    rates = [34, 58, 72, 91]

    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    bars = ax.barh(labels, rates, color=T.HEX_PRIMARY, height=0.55)
    ax.set_xlim(0, 100)
    ax.invert_yaxis()
    for bar, val in zip(bars, rates):
        ax.text(val + 1.5, bar.get_y() + bar.get_height() / 2, f"{val}%",
                va="center", fontsize=10, color=T.HEX_CHARCOAL, fontweight="bold")
    ax.set_xlabel("Restart & Run All 成功率 (%)", fontsize=9, color=T.HEX_CHARCOAL)
    ax.tick_params(axis="y", length=0, labelsize=10)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m1s10_notebook.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close()
    return outfile
