# Ch09 · Minimum Viable Knowledge

**章節**：Matplotlib 探索性視覺化（M4 · 1.5 hr）
**Governing thought**：圖不是漂亮，是問題的顯影 — 選對四種 EDA 圖、用 Figure/Axes 雙層結構 + subplots，讓資料自己開口說話。

---

## Figure / Axes 雙層結構（心智模型）

- **Figure** = 整張畫布（存檔、列印的最小單位）
- **Axes** = 畫布上的一個座標系（title / xlabel / ylabel / spines / legend 都屬 Axes）
- 一個 Figure 可以有多個 Axes（subplots）
- **pyplot（狀態式）vs OO（物件導向）** — 業界 99% 用 OO，本課程只教 OO

---

## 所有圖的共同骨架（5 行，背下來）

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y)                # ← 只有這行會換（hist/scatter/boxplot）
ax.set_title("..."); ax.set_xlabel("..."); ax.set_ylabel("...")
plt.show()
```

---

## EDA 必備四種圖

| 問題 | 圖 | API | 關鍵參數 |
|------|-----|-----|----------|
| 分布如何？ | 直方 | `ax.hist(x, bins=N)` | `bins`, `density` |
| 有趨勢嗎？ | 折線 | `ax.plot(x, y, label=...)` | `marker`, `label` |
| 兩變數有關係嗎？ | 散佈 | `ax.scatter(x, y, alpha=...)` | `alpha`, `c`, `cmap` |
| 有離群 / 分組差？ | Box | `ax.boxplot([g1, g2, g3])` | `labels`, `vert` |

---

## 客製化三件套

```python
ax.set_title("標題", fontsize=14, pad=12)
ax.set_xlabel("月份"); ax.set_ylabel("金額 (千元)")
ax.legend(loc="upper left", frameon=False)
ax.plot(..., color="#1B5E3F")      # 具名色 'C0'~'C9' 或 hex
# 連續著色：cmap='viridis'
```

---

## 中文字型 + 高解析存檔（台灣必備）

```python
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Noto Sans CJK TC"
plt.rcParams["axes.unicode_minus"] = False    # 負號修正
# ...畫圖...
fig.savefig("out.png", dpi=300, bbox_inches="tight")
```

⚠ **負號變方塊**是 CJK 使用者第一個坑，`axes.unicode_minus=False` 擋掉。

---

## subplots 多圖排版

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].hist(df["score"], bins=20)
axes[0, 1].plot(df["month"], df["sales"])
axes[1, 0].scatter(df["h"], df["w"], alpha=0.6)
axes[1, 1].boxplot([df[df.city == c]["price"] for c in cities])
fig.tight_layout()
```

- `axes` 是 2D numpy array，用 `[i, j]` 取子圖
- `tight_layout` 解決標題 / 軸重疊
- 2×2 就是經典 EDA 儀表板：分布 / 趨勢 / 相關 / 離群

---

## 學生離開教室時應能

1. 畫出 Figure / Axes 雙層結構圖，並說明 title / xlabel 屬 Axes
2. 用 OO API 寫出 5 行共同骨架，並套用到四種圖
3. 為 EDA 四個典型問題各選對一種圖
4. 客製化標題、軸、圖例、配色
5. 設定中文字型並正確顯示負號
6. 用 `fig, axes = plt.subplots(2, 2)` 完成一張 EDA 儀表板
7. 用 `savefig(dpi=300, bbox_inches='tight')` 輸出交付級圖

---

## 本章刻意不深教（留給後續或進階）

- Seaborn / Plotly / Altair（建議另課）
- `rcParams` 全域樣式系統
- 3D / 極座標 / 地理投影
- 動畫 / `FuncAnimation`
- Matplotlib 內部 Artist / Renderer 架構

---

## 銜接

- **Ch10 OOP × Pandas 整合**：把 Ch08 清洗 + Ch09 視覺化，封裝成 `DataCleaner.plot_*()` 方法 — 端到端資料工程物件。
