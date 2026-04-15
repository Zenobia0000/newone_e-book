# S5 · MVK（最小可帶走知識）

## 0. 一句話
> 5 張圖吃掉 90% DA 場景：**問題決定圖**，seaborn 打底、matplotlib 微調。

## 1. 五圖速查表（背下來）

| 問題 | 圖 | 一行 API | 關鍵參數 |
|---|---|---|---|
| 趨勢（時間） | 折線 | `sns.lineplot(data, x, y, marker='o')` | marker / hue |
| 比較（誰大） | 長條 | `sns.barplot(data, x, y, hue=x, legend=False)` | sort_values |
| 關聯（兩數值） | 散佈 | `sns.scatterplot(x, y, hue, alpha=0.6)` | alpha / hue |
| 分布（離群） | 箱型 | `sns.boxplot(x, y)` | 看 median / IQR / 離群 |
| 矩陣（交叉） | 熱力 | `sns.heatmap(pivot, annot=True, fmt=',.0f')` | fmt / cmap |

## 2. 環境三件套（notebook 首行）

```python
import seaborn as sns, matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]   # Win
plt.rcParams["axes.unicode_minus"] = False
```

## 3. 儀表板骨架（2×3）

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes[0, 0].plot(...)          # 月趨勢
axes[0, 1].barh(...)          # 地區排名
axes[0, 2].scatter(...)       # 品類散佈
sns.boxplot(..., ax=axes[1, 0])
sns.heatmap(..., ax=axes[1, 1])
axes[1, 2].text(...)          # KPI
fig.suptitle("Q4 Sales Dashboard", fontsize=16)
fig.tight_layout()
fig.savefig("q4_dashboard.png", dpi=300, bbox_inches="tight")
plt.show()    # 永遠 savefig 在前、show 在後
```

## 4. 四條紀律（帶走）

1. **先 `fig, ax = plt.subplots()` 再畫** — 物件導向、不混 pyplot。
2. **排序是長條圖的靈魂** — `sort_values` 永遠在 barplot 之前。
3. **seaborn 0.13+ palette 必搭 hue** — `hue=x, legend=False` 避警告。
4. **savefig → show** — 順序反了 → 存檔空白。

## 5. 選圖決策樹（30 秒判圖）

```
問：看什麼？
 ├─ 時間／有序 → 折線
 ├─ 誰比誰大 → 長條（排序！）
 ├─ 兩個數值有關嗎 → 散佈
 ├─ 分布 / 離群 → 箱型
 └─ 兩類別交叉 → 熱力
```

## 6. 常見坑（一句話解法）
- 長條圖未排序 → `sort_values()` 先行。
- palette 警告 → 加 `hue=x, legend=False`。
- 中文變方框 → `rcParams['font.sans-serif']` + `unicode_minus=False`。
- 散佈點看成一坨 → 加 `alpha=0.5`。
- 熱力圖科學記號 → `fmt=',.0f'`。
- 儀表板撞版 → `fig.tight_layout()`。
- 存檔空白 → `savefig` 永遠在 `show` 前。

## 7. 銜接 S6
S6 把這 5 張圖換成 Plotly：靜態 → 互動（hover、篩選、下鑽），交付改為 HTML/Dash。
