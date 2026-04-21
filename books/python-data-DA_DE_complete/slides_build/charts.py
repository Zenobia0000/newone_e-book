"""Editorial-strict matplotlib charts. Output PNG 300dpi to _charts/."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from matplotlib.patches import Rectangle, FancyArrow

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


def line_chart_m2_s3(outfile: Path = None) -> Path:
    """M2-S3: refactor hours vs LOC, with/without class boundaries."""
    _editorial_style()
    x = [200, 400, 600, 800]
    a = [1.5, 3.2, 6.1, 9.8]
    b = [1.4, 2.1, 2.8, 3.5]

    fig, ax = plt.subplots(figsize=(11.7, 4.8))
    ax.plot(x, a, color=T.HEX_PRIMARY, linewidth=2.5, marker="o", markersize=5)
    ax.plot(x, b, color=T.HEX_CHARCOAL, linewidth=2.0, marker="o", markersize=5,
            linestyle="--")

    ax.axvline(x=200, color=T.HEX_GRAY_MID, linestyle="--", linewidth=1.2)
    ax.text(202, 11.0, "臨界點", color=T.HEX_GRAY_MID, fontsize=9, style="italic")

    ax.annotate("無 class 邊界", xy=(800, 9.8), xytext=(8, 0),
                textcoords="offset points", color=T.HEX_PRIMARY,
                fontsize=10, fontweight="bold", va="center")
    ax.annotate("有 class 邊界", xy=(800, 3.5), xytext=(8, 0),
                textcoords="offset points", color=T.HEX_CHARCOAL,
                fontsize=10, fontweight="bold", va="center")

    ax.set_xlim(150, 920)
    ax.set_ylim(0, 12)
    ax.set_xticks(x)
    ax.set_xlabel("程式碼行數 (LOC)", fontsize=10)
    ax.set_ylabel("重構所需工時 (小時)", fontsize=10)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m2s3_line.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def hbar_log_m3s2(outfile: Path = None) -> Path:
    """M3-S2: log-scale horizontal bar, Python loop vs NumPy vectorised."""
    _editorial_style()
    labels = ["Python for-loop", "NumPy 向量化"]
    values = [1800, 12]
    value_labels = ["1,800 ms", "12 ms (-99.3%)"]
    colors = [T.HEX_PRIMARY, T.HEX_CHARCOAL]

    fig, ax = plt.subplots(figsize=(10.5, 4.2))
    bars = ax.barh(labels, values, color=colors, height=0.55)
    ax.set_xscale("log")
    ax.set_xlim(1, 10000)
    ax.invert_yaxis()

    for bar, v, vl in zip(bars, values, value_labels):
        ax.text(v * 1.15, bar.get_y() + bar.get_height() / 2, vl,
                va="center", fontsize=10, color=T.HEX_CHARCOAL, fontweight="bold")

    ax.set_xlabel("耗時 (ms, log scale)", fontsize=10)
    ax.tick_params(axis="y", length=0, labelsize=10)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m3s2_hbar_log.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def datasaurus_dozen_m4s3(outfile: Path = None) -> Path:
    """M4-S3: 3x4 small-multiples, synthetic datasaurus-style distributions."""
    _editorial_style()
    rng = np.random.default_rng(42)
    n = 142
    mx, my, sx, sy = 54.0, 48.0, 16.0, 16.0

    def normalise(xs, ys):
        xs = (xs - xs.mean()) / (xs.std() + 1e-9) * sx + mx
        ys = (ys - ys.mean()) / (ys.std() + 1e-9) * sy + my
        return xs, ys

    def dino():
        t = np.linspace(0, 2 * np.pi, n)
        xs = 30 * np.cos(t) + rng.normal(0, 4, n)
        ys = 25 * np.sin(t) + 0.3 * xs + rng.normal(0, 5, n)
        return normalise(xs, ys)

    def star():
        t = np.linspace(0, 2 * np.pi, n)
        r = 20 + 10 * np.cos(5 * t)
        return normalise(r * np.cos(t), r * np.sin(t))

    def x_shape():
        s = rng.choice([-1, 1], n)
        xs = rng.uniform(-30, 30, n)
        ys = s * xs + rng.normal(0, 3, n)
        return normalise(xs, ys)

    def h_lines():
        ys = rng.choice([-20, 0, 20], n) + rng.normal(0, 1.2, n)
        xs = rng.uniform(-30, 30, n)
        return normalise(xs, ys)

    def v_lines():
        xs = rng.choice([-20, 0, 20], n) + rng.normal(0, 1.2, n)
        ys = rng.uniform(-30, 30, n)
        return normalise(xs, ys)

    def circle():
        t = rng.uniform(0, 2 * np.pi, n)
        r = 25 + rng.normal(0, 1.2, n)
        return normalise(r * np.cos(t), r * np.sin(t))

    def bullseye():
        t = rng.uniform(0, 2 * np.pi, n)
        r = np.where(rng.random(n) < 0.5, 10, 25) + rng.normal(0, 0.8, n)
        return normalise(r * np.cos(t), r * np.sin(t))

    def dots():
        cx = rng.choice([-20, 0, 20], n)
        cy = rng.choice([-20, 0, 20], n)
        return normalise(cx + rng.normal(0, 1.5, n), cy + rng.normal(0, 1.5, n))

    def away():
        xs = rng.uniform(-30, 30, n)
        ys = rng.uniform(-30, 30, n)
        return normalise(xs, ys)

    def wide_lines():
        ys = rng.choice([-22, 22], n) + rng.normal(0, 2, n)
        xs = rng.uniform(-30, 30, n)
        return normalise(xs, ys)

    def slant_up():
        xs = rng.uniform(-30, 30, n)
        ys = xs + rng.choice([-14, 0, 14], n) + rng.normal(0, 2, n)
        return normalise(xs, ys)

    def slant_down():
        xs = rng.uniform(-30, 30, n)
        ys = -xs + rng.choice([-14, 0, 14], n) + rng.normal(0, 2, n)
        return normalise(xs, ys)

    shapes = [
        ("dino", dino), ("star", star), ("x", x_shape), ("h-lines", h_lines),
        ("v-lines", v_lines), ("circle", circle), ("bullseye", bullseye),
        ("dots", dots), ("away", away), ("wide-lines", wide_lines),
        ("slant-up", slant_up), ("slant-down", slant_down),
    ]

    fig, axes = plt.subplots(3, 4, figsize=(11.5, 6.0))
    for ax, (name, fn) in zip(axes.flat, shapes):
        xs, ys = fn()
        ax.scatter(xs, ys, s=4, color=T.HEX_PRIMARY, alpha=0.75)
        ax.set_title(name, fontsize=9, color=T.HEX_CHARCOAL, pad=3)
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_color(T.HEX_LIGHT_GRAY)

    fig.suptitle("同 μ、同 σ、截然不同的形狀", fontsize=12,
                 color=T.HEX_CHARCOAL, fontweight="bold", y=0.995)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m4s3_datasaurus.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def before_after_truncated_axis_m4s6(outfile: Path = None) -> Path:
    """M4-S6: truncated vs full-zero y-axis bar pair."""
    _editorial_style()
    labels = ["A", "B"]
    values = [97.2, 98.1]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.8))

    for ax, ylim, title in [
        (ax1, (95, 100), "截斷 y 軸：誇大差異"),
        (ax2, (0, 100), "完整 0 起點：真實差異"),
    ]:
        bars = ax.bar(labels, values, color=T.HEX_PRIMARY, width=0.55)
        ax.set_ylim(*ylim)
        ax.set_title(title, loc="left", fontsize=10.5,
                     color=T.HEX_CHARCOAL, fontweight="bold", pad=8)
        for bar, v in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    v + (ylim[1] - ylim[0]) * 0.015,
                    f"{v}", ha="center", fontsize=10,
                    color=T.HEX_CHARCOAL, fontweight="bold")
        ax.tick_params(axis="x", labelsize=10)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m4s6_truncated.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def bar_vs_box_m4s9(outfile: Path = None) -> Path:
    """M4-S9: bar+error vs boxplot — same means, different distributions."""
    _editorial_style()
    rng = np.random.default_rng(7)
    # Three distributions: skewed / bimodal / uniform — all mean ~= 50
    g1 = rng.gamma(2.0, 10.0, 60)
    g1 = (g1 - g1.mean()) + 50
    g2 = np.concatenate([rng.normal(30, 4, 30), rng.normal(70, 4, 30)])
    g2 = (g2 - g2.mean()) + 50
    g3 = rng.uniform(20, 80, 60)
    g3 = (g3 - g3.mean()) + 50

    means = [50, 50, 50]
    se = [2, 2, 2]
    labels = ["A", "B", "C"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.8))

    bars = ax1.bar(labels, means, yerr=se, color=T.HEX_PRIMARY, width=0.55,
                   capsize=6, ecolor=T.HEX_CHARCOAL)
    ax1.set_ylim(0, 100)
    ax1.set_title("柱狀 + 誤差：均值相同", loc="left", fontsize=10.5,
                  color=T.HEX_CHARCOAL, fontweight="bold", pad=8)
    for bar, v in zip(bars, means):
        ax1.text(bar.get_x() + bar.get_width() / 2, v + 4, str(v),
                 ha="center", fontsize=10, color=T.HEX_CHARCOAL, fontweight="bold")

    bp = ax2.boxplot([g1, g2, g3], labels=labels, patch_artist=True,
                     widths=0.5)
    for patch in bp["boxes"]:
        patch.set_facecolor(T.HEX_PRIMARY)
        patch.set_edgecolor(T.HEX_CHARCOAL)
    for med in bp["medians"]:
        med.set_color("white")
        med.set_linewidth(1.8)
    for whisker in bp["whiskers"]:
        whisker.set_color(T.HEX_CHARCOAL)
    for cap in bp["caps"]:
        cap.set_color(T.HEX_CHARCOAL)
    for flier in bp["fliers"]:
        flier.set_marker("o")
        flier.set_markersize(3)
        flier.set_markerfacecolor(T.HEX_GRAY_MID)
        flier.set_markeredgecolor(T.HEX_GRAY_MID)
    ax2.set_ylim(0, 100)
    ax2.set_title("箱形圖：全貌立現", loc="left", fontsize=10.5,
                  color=T.HEX_CHARCOAL, fontweight="bold", pad=8)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m4s9_bar_vs_box.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def ci_shrink_loglog_m4s10(outfile: Path = None) -> Path:
    """M4-S10: CI width shrinks with sqrt(n) — semi-log with filled band."""
    _editorial_style()
    n = np.array([10, 30, 100, 300, 1000, 3000, 10000])
    # width at n=100 ~= 5 ; width = 50 / sqrt(n)
    w = 50.0 / np.sqrt(n)

    fig, ax = plt.subplots(figsize=(11.5, 5.2))
    ax.fill_between(n, -w, w, color=T.HEX_PRIMARY, alpha=0.18,
                    linewidth=0)
    ax.plot(n, w, color=T.HEX_PRIMARY, linewidth=2.4)
    ax.plot(n, -w, color=T.HEX_PRIMARY, linewidth=2.4)
    ax.axhline(y=0, color=T.HEX_CHARCOAL, linewidth=1.0)

    ax.set_xscale("log")
    ax.set_xlim(8, 13000)
    ax.set_ylim(-18, 18)
    ax.set_xlabel("樣本數 (log)", fontsize=10)
    ax.set_ylabel("誤差範圍 (±%)", fontsize=10)

    ax.annotate("1% 誤差門檻 (n≈2500)",
                xy=(2500, 1.0), xytext=(300, 12),
                color=T.HEX_CHARCOAL, fontsize=10, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=T.HEX_CHARCOAL, lw=1.3,
                                connectionstyle="arc3,rad=-0.2"))

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m4s10_ci_shrink.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def gil_dual_line_m5s12(outfile: Path = None) -> Path:
    """M5-S12: GIL dual-line chart, CPU vs I/O bound scaling."""
    _editorial_style()
    x = [1, 2, 4, 8, 16]
    cpu = [98, 102, 104, 101, 99]
    io = [95, 180, 340, 610, 720]

    fig, ax = plt.subplots(figsize=(10.5, 5.0))
    ax.plot(x, cpu, color=T.HEX_PRIMARY, linewidth=2.5, marker="o", markersize=5)
    ax.plot(x, io, color=T.HEX_CHARCOAL, linewidth=2.0, marker="o",
            markersize=5, linestyle="--")

    ax.axhline(y=100, color=T.HEX_GRAY_MID, linestyle=":", linewidth=1.2)
    ax.text(16.2, 100, "單核上限", color=T.HEX_GRAY_MID, fontsize=9,
            style="italic", va="center")

    ax.annotate("CPU bound", xy=(16, 99), xytext=(8, -6),
                textcoords="offset points", color=T.HEX_PRIMARY,
                fontsize=10, fontweight="bold", va="center")
    ax.annotate("I/O bound", xy=(16, 720), xytext=(8, 0),
                textcoords="offset points", color=T.HEX_CHARCOAL,
                fontsize=10, fontweight="bold", va="center")

    ax.set_xlim(0.5, 18.5)
    ax.set_ylim(0, 820)
    ax.set_xticks(x)
    ax.set_xlabel("執行緒數", fontsize=10)
    ax.set_ylabel("吞吐 (%, 8 核上限=800)", fontsize=10)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m5s12_gil.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def bar_chart_m6s2_dtype_ram(outfile: Path = None) -> Path:
    """M6-S2: dtype RAM footprint per 1M records, linear MB."""
    _editorial_style()
    labels = ["int64", "int32", "float32", "int8"]
    values = [8, 4, 4, 1]

    fig, ax = plt.subplots(figsize=(10.5, 4.0))
    bars = ax.barh(labels, values, color=T.HEX_PRIMARY, height=0.55)
    ax.invert_yaxis()
    ax.set_xlim(0, max(values) * 1.18)

    for bar, v in zip(bars, values):
        ax.text(v + 0.12, bar.get_y() + bar.get_height() / 2, f"{v} MB",
                va="center", fontsize=10, color=T.HEX_CHARCOAL, fontweight="bold")

    ax.set_xlabel("每百萬筆記錄的 RAM (MB)", fontsize=10)
    ax.tick_params(axis="y", length=0, labelsize=10)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m6s2_dtype_ram.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def bar_chart_m6s3_memory_hierarchy(outfile: Path = None) -> Path:
    """M6-S3: memory hierarchy latency, log ns."""
    _editorial_style()
    labels = ["L1", "L2", "L3", "RAM", "SSD", "Network"]
    values = [1, 4, 12, 100, 150_000, 10_000_000]
    vlabels = ["1 ns", "4 ns", "12 ns", "100 ns", "150 μs", "10 ms"]

    fig, ax = plt.subplots(figsize=(10.5, 4.5))
    bars = ax.barh(labels, values, color=T.HEX_PRIMARY, height=0.6)
    ax.set_xscale("log")
    ax.set_xlim(0.5, 5e7)
    ax.invert_yaxis()

    for bar, v, vl in zip(bars, values, vlabels):
        ax.text(v * 1.35, bar.get_y() + bar.get_height() / 2, vl,
                va="center", fontsize=10, color=T.HEX_CHARCOAL, fontweight="bold")

    ax.set_xlabel("延遲 (ns, log scale)", fontsize=10)
    ax.tick_params(axis="y", length=0, labelsize=10)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m6s3_memhier.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def bar_chart_m6s9_io_evolution(outfile: Path = None) -> Path:
    """M6-S9: I/O primitive evolution — max connections, log scale."""
    _editorial_style()
    labels = ["select", "poll", "epoll", "io_uring", "io_uring + SQ poll"]
    values = [1024, 10_000, 100_000, 500_000, 1_000_000]
    vlabels = [f"{v:,}" for v in values]

    fig, ax = plt.subplots(figsize=(10.5, 4.5))
    bars = ax.barh(labels, values, color=T.HEX_PRIMARY, height=0.6)
    ax.set_xscale("log")
    ax.set_xlim(500, 5e6)
    ax.invert_yaxis()

    for bar, v, vl in zip(bars, values, vlabels):
        ax.text(v * 1.25, bar.get_y() + bar.get_height() / 2, vl,
                va="center", fontsize=10, color=T.HEX_CHARCOAL, fontweight="bold")

    ax.set_xlabel("單機可承載連線數 (log)", fontsize=10)
    ax.tick_params(axis="y", length=0, labelsize=10)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m6s9_io_evolution.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def before_after_m6s10_dtype(outfile: Path = None) -> Path:
    """M6-S10: object vs category dtype RAM (linear)."""
    _editorial_style()
    labels = ["object dtype", "category dtype"]
    values = [900, 2]
    colors = [T.HEX_CHARCOAL, T.HEX_PRIMARY]

    fig, ax = plt.subplots(figsize=(9.0, 4.8))
    bars = ax.bar(labels, values, color=colors, width=0.5)
    ax.set_ylim(0, 1000)
    ax.set_ylabel("RAM (MB)", fontsize=10)

    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 18, f"{v} MB",
                ha="center", fontsize=10, color=T.HEX_CHARCOAL, fontweight="bold")

    # -99.8% annotation over right bar
    ax.annotate("-99.8%", xy=(1, 2), xytext=(1, 320),
                ha="center", color=T.HEX_PRIMARY, fontsize=12, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=T.HEX_PRIMARY, lw=1.5),
                bbox=dict(boxstyle="round,pad=0.3", fc="white",
                          ec=T.HEX_PRIMARY, lw=1.2))

    ax.tick_params(axis="x", labelsize=10)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m6s10_dtype_ba.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def tensor_vs_ndarray_bench_m7s7(outfile: Path = None) -> Path:
    """M7-S7: 10k×10k MatMul — NumPy CPU / PyTorch CPU / PyTorch GPU."""
    _editorial_style()
    labels = ["NumPy CPU", "PyTorch CPU", "PyTorch GPU"]
    values = [3.80, 3.50, 0.04]
    vlabels = ["3.80 s", "3.50 s", "0.04 s"]
    colors = [T.HEX_CHARCOAL, T.HEX_CHARCOAL, T.HEX_PRIMARY]

    fig, ax = plt.subplots(figsize=(11.5, 3.6))
    bars = ax.barh(labels, values, color=colors, height=0.55)
    ax.set_xscale("log")
    ax.set_xlim(0.01, 20)
    ax.invert_yaxis()

    for bar, v, vl in zip(bars, values, vlabels):
        ax.text(v * 1.25, bar.get_y() + bar.get_height() / 2, vl,
                va="center", fontsize=10, color=T.HEX_CHARCOAL, fontweight="bold")

    ax.set_xlabel("10k×10k MatMul 耗時 (s, log)", fontsize=10)
    ax.tick_params(axis="y", length=0, labelsize=10)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m7s7_bench.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile


def tool_scale_bands_m7s10(outfile: Path = None) -> Path:
    """M7-S10: tool operating ranges as horizontal bands on log-row axis."""
    _editorial_style()
    # Rows top→bottom
    rows = [
        ("NumPy",   1e3, 1e7,  False, False),
        ("pandas",  1e3, 1e7,  True,  False),   # dashed tail 1e7→1e9 "OOM 風險"
        ("Polars",  1e5, 1e9,  False, False),
        ("DuckDB",  1e5, 5e9,  False, False),
        ("Spark",   1e7, 1e11, False, True),    # right-open arrow
    ]

    fig, ax = plt.subplots(figsize=(11.5, 4.5))
    n = len(rows)
    h = 0.55
    for i, (name, lo, hi, dashed_tail, right_open) in enumerate(rows):
        y = n - 1 - i  # top→bottom
        # Solid supported range
        ax.add_patch(Rectangle((lo, y - h / 2), hi - lo, h,
                               facecolor=T.HEX_PRIMARY, edgecolor=T.HEX_CHARCOAL,
                               linewidth=0.8, alpha=0.85))
        # Dashed tail for pandas (OOM 風險)
        if dashed_tail:
            ax.plot([hi, 1e9], [y, y], color=T.HEX_CHARCOAL, linewidth=1.6,
                    linestyle="--")
            ax.text(3e8, y + 0.38, "OOM 風險", color=T.HEX_CHARCOAL,
                    fontsize=8.5, style="italic", ha="center")
        # Right-open arrow for Spark (interpret as extends beyond axis)
        if right_open:
            ax.annotate("", xy=(5e11, y), xytext=(hi, y),
                        arrowprops=dict(arrowstyle="->", color=T.HEX_PRIMARY,
                                        lw=2.0))
        # Label to left of band
        ax.text(lo / 2.2, y, name, ha="right", va="center",
                fontsize=10.5, color=T.HEX_CHARCOAL, fontweight="bold")

    ax.set_xscale("log")
    ax.set_xlim(1e2, 1e12)
    ax.set_ylim(-0.8, n - 0.2)
    ax.set_yticks([])
    ax.set_xlabel("資料筆數 (log)", fontsize=10)
    ax.spines["left"].set_visible(False)

    plt.tight_layout()
    outfile = outfile or T.CHART_CACHE / "m7s10_tool_bands.png"
    plt.savefig(outfile, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return outfile
