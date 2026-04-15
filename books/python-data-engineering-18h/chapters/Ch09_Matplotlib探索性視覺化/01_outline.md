# Chapter 9：Matplotlib 探索性視覺化

**模組：** M4 視覺化與整合實戰  
**時數：** 1.5 小時  
**前置知識：** Ch7 NumPy、Ch8 Pandas  
**後續銜接：** Ch10（DataCleaner 整合 EDA 圖表）

---

## 一、章節定位

Matplotlib 是 Python 視覺化的底層基礎（Seaborn、Pandas plotting 都建立在它之上）。本章不教所有圖種，只教**EDA 工作流必備的 4 種圖**與**Figure/Axes 心智模型**。

---

## 二、學習目標

完成本章後，學生能夠：

1. 解釋 Figure 與 Axes 的雙層結構
2. 為四種典型 EDA 場景選對圖表（線圖 / 散佈 / 直方 / Box）
3. 客製化標題、軸線、圖例、配色
4. 用 `subplots` 排版多圖

---

## 三、章節結構

### 9-1. Figure 與 Axes 的雙層結構（20 分鐘）
- **比喻**：Figure 是畫布，Axes 是畫布上的座標系
- 兩種寫法：
  - **狀態式（pyplot）**：`plt.plot(...)` —— 上手快但容易混亂
  - **物件導向（OO）**：`fig, ax = plt.subplots(); ax.plot(...)` —— 推薦
- 為何業界推薦 OO 寫法：可預測、可組合、易擴充
- **Linus 觀點**：「明確 > 隱式」

### 9-2. EDA 必備四種圖（45 分鐘）

| 圖種 | 何時用 | API |
|------|--------|-----|
| 折線圖 | 趨勢、時間序列 | `ax.plot(x, y)` |
| 散佈圖 | 兩變數關係、離群偵測 | `ax.scatter(x, y)` |
| 直方圖 | 單變數分布 | `ax.hist(data, bins=N)` |
| Box plot | 分布比較、四分位數 | `ax.boxplot(data)` |

每種圖的教學內容：
1. 何時選它（資料特徵與問題）
2. 最小範例
3. 常見變化（多條線、分組著色）
4. 解讀重點

### 9-3. 客製化：標題、軸線、圖例、配色（15 分鐘）
- `ax.set_title()` / `set_xlabel` / `set_ylabel`
- `ax.legend()` 與 label 參數
- 配色：`color='C0'`、`cmap='viridis'`
- 中文字型設定：`plt.rcParams['font.family'] = 'Noto Sans CJK TC'`
- 儲存圖片：`fig.savefig('out.png', dpi=300, bbox_inches='tight')`

### 9-4. 多圖排版：subplots（10 分鐘）
- `fig, axes = plt.subplots(2, 2, figsize=(10, 8))`
- 用 `axes[0, 0]`、`axes[1, 1]` 取出個別子圖
- `fig.tight_layout()` 自動排版
- **EDA 工作流**：一張 2×2 包含「分布、趨勢、相關、離群」四圖

---

## 四、課後練習

1. **入門題**：用某 CSV 的銷售資料，畫出月度趨勢折線圖
2. **EDA 題**：對鳶尾花資料集，用 2×2 subplots 同時呈現 4 個特徵的直方圖
3. **進階題**：把散佈圖按類別著色，加上 trend line 與圖例

---

## 五、銜接下一章

資料能讀、能清、能畫，最後一步是「**收斂為一個可重用的工具**」。Ch10 將整合所有前序章節，完成 `DataCleaner` 端到端管線。
