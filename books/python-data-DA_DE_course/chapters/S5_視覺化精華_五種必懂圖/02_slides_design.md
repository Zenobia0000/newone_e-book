---
session: S5
title: 視覺化精華：5 種必懂圖
track: teaching
palette: "#1B5E3F / #C62828 / #2E7D32"
n_content: 24
---

# S5 · 投影片設計稿（🖼️ 版面 · 📣 文案 · 🎙️ 講稿）

> 節奏：4 拍（SILENT／ASK／核心概念／PITFALL 或 CHECKPOINT）。每 4-5 張一次收束。

---

## S5-01 · SILENT — 數字不會說話。圖會。
- 🖼️ 深綠全版 + 白色 hero 句
- 📣 「數字不會說話。\n圖會。」
- 🎙️ 學員開場先冷震。S4 算出一堆數字，但老闆只會看圖。這節 2 小時，帶你把 5 張圖畫到簡報級。

## S5-02 · ASK — 老闆問「所以誰最好？」
- 🖼️ 白底大問題 + data card
- 📣 「老闆看完表格\n還是問『所以誰最好？』」；data card: 表格閱讀成本 37 秒 vs 圖 4 秒
- 🎙️ 問題不在資料，在呈現。表格是給你讀的、圖是給老闆看的。

## S5-03 · MATRIX 2×3 — 五個問題 → 五種圖
- 🖼️ 2×3 矩陣（第 6 格放「選圖心法」）
- 📣 趨勢→折線／比較→長條／關聯→散佈／分布→箱型／矩陣→熱力／心法：問題決定圖
- 🎙️ 這是本節最該背的一張。問句在前、圖在後。

## S5-04 · VS — 表格 vs 折線
- 🖼️ 左表格（12 列月銷售）／右折線縮圖
- 📣 左：12 列數字；右：一條折線；delta：「4 秒 vs 37 秒」
- 🎙️ 同一份資料，讀表 37 秒、看圖 4 秒。這就是為什麼我們要學畫圖。

## S5-05 · CODE — 環境三件套
- 🖼️ code panel
- 📣 `sns.set_theme(style='whitegrid')` + `rcParams['font.sans-serif']` + `axes.unicode_minus=False`
- 🎙️ 這三行寫在 notebook 最上面。之後不用再煩字型、網格、負號。

## S5-06 · SILENT — 圖 1 · 折線
- 🖼️ 深綠底
- 📣 「圖 1 · 折線\n看的是趨勢。」
- 🎙️ 進第一張圖。

## S5-07 · IMAGE+CODE — sns.lineplot 月度趨勢
- 🖼️ 左：折線圖佔位／右：code + bullets
- 📣 `sns.lineplot(data=df, x='month', y='sales', marker='o')`；bullets: 時間有序 / marker / hue 多條線 / xtick rotation
- 🎙️ 一行搞定。重點是 marker='o' 讓離散月份看得清楚。

## S5-08 · PITFALL — 折線常見坑
- 🖼️ risk/mitigation 雙欄
- 📣 風險：類別資料硬套折線 / x 軸過密 / 忘了 marker；對策：改長條 / rotation=45 / 一律加 marker='o'
- 🎙️ 學員最常犯第一條——把「地區」當 x 軸畫折線，那叫錯覺趨勢。

## S5-09 · IMAGE+CODE — sns.barplot 排序 + 標註
- 🖼️ 左：橫向長條（由大到小）／右：code
- 📣 `df.sort_values('sales').pipe(sns.barplot, ...)` + `plt.text()` 數字標註
- 🎙️ 排序是長條圖的靈魂。未排序 = 老闆不知道誰第一。

## S5-10 · PITFALL — 長條常見坑
- 🖼️ risk/mitigation
- 📣 風險：未排序 / seaborn 0.13 palette 警告 / 長標籤撞；對策：sort_values / hue=x,legend=False / vert=False 橫排
- 🎙️ seaborn 0.13 後 palette 必須搭 hue，這是學員必踩第一坑。

## S5-11 · IMAGE+CODE — sns.scatterplot hue + legend
- 🖼️ 左：散佈圖依品類上色／右：code
- 📣 `sns.scatterplot(x='price', y='qty', hue='category', alpha=0.6)` + `plt.legend(bbox_to_anchor=(1.02, 1))`
- 🎙️ hue 上色是散佈圖的超能力。legend 外移避免擋圖。

## S5-12 · PITFALL — 散佈常見坑
- 🖼️ risk/mitigation
- 📣 風險：重疊不用 alpha / legend 擋圖 / hue 類別 > 7；對策：alpha=0.4-0.6 / bbox_to_anchor / 分面 facet
- 🎙️ hue 超過七類 = 彩虹災難，改 facet 或換圖。

## S5-13 · IMAGE+CODE — sns.boxplot 解讀
- 🖼️ 左：三地區箱型圖（含離群）／右：code + 解剖圖註解
- 📣 box=IQR、線=中位數、whisker=1.5×IQR、點=離群
- 🎙️ 這是學員最不熟的圖。先教「怎麼看」再教「怎麼畫」。

## S5-14 · PITFALL — 箱型常見坑
- 🖼️ risk/mitigation
- 📣 風險：兩組用 box 沒比較價值 / 把離群點當錯誤丟掉 / y 軸起點被壓扁；對策：兩組改 hist / 先問為何離群 / sharey=False
- 🎙️ 離群點不是垃圾，它是訊號。先問為什麼。

## S5-15 · IMAGE+CODE — sns.heatmap 矩陣視覺
- 🖼️ 左：地區×品類 熱力圖／右：code
- 📣 `sns.heatmap(pivot, annot=True, fmt=',.0f', cmap='Greens')`
- 🎙️ 熱力圖是 S3 pivot_table 的視覺化版。annot=True 把數字補上、fmt 擋科學記號。

## S5-16 · PITFALL — 熱力常見坑
- 🖼️ risk/mitigation
- 📣 風險：類別>15 格子擠 / 數字跑科學記號 / cmap 誤選發散色；對策：先 groupby.nlargest / fmt=',.0f' / 單向用 sequential、雙向用 diverging
- 🎙️ cmap 選錯 = 資訊反效果。正負值才用 diverging（紅-白-藍）。

## S5-17 · TABLE — 五圖速查
- 🖼️ editorial table
- 📣 問題｜圖｜一行 API｜常見誤用
- 🎙️ 這張截圖放工作桌布。

## S5-18 · CODE — plt.subplots(2, 3) 骨架
- 🖼️ code panel
- 📣 `fig, axes = plt.subplots(2, 3, figsize=(15, 8))` + `axes[0, 0]` 索引
- 🎙️ 進儀表板環節。axes 是 2D numpy array，用 [i, j] 取。

## S5-19 · IMAGE+CODE — Q4 Sales Dashboard
- 🖼️ 左：2×3 儀表板大圖／右：code + bullets
- 📣 六格：月趨勢 / 地區排名 / 品類散佈 / 地區箱型 / 熱力矩陣 / KPI 區塊
- 🎙️ 這張畫出來放履歷。DA 面試就是比你會不會整合。

## S5-20 · PITFALL — 儀表板常見坑
- 🖼️ risk/mitigation
- 📣 風險：axes[0][1] vs axes[0, 1] 混用 / 沒 tight_layout 撞版 / plt.show() 在 savefig 前；對策：統一 [i, j] / tight_layout() / savefig → show
- 🎙️ 存檔空白是十人九坑。記順序：先存再顯示。

## S5-21 · VS — seaborn vs matplotlib
- 🖼️ 兩欄 VS
- 📣 左 seaborn：一行、統計預設、palette 友善；右 matplotlib：精修軸、雙 y、annotation；delta：「打底 vs 微調」
- 🎙️ 分工明確：90% 場景 seaborn 搞定，極度客製才切 matplotlib。

## S5-22 · PRACTICE-PROMPT — Electronics 迷你儀表板
- 🖼️ prompt + 評分 rubric
- 📣 題目：用 Electronics 品類資料畫 2×2（趨勢/地區排名/單價散佈/金額箱型），10 分鐘；rubric：選圖正確/排序/標題/字型
- 🎙️ 30 分鐘：前 10 寫、後 20 互看。強調「能放履歷」。

## S5-23 · FLOW — 選圖工作流
- 🖼️ 4 節點 flow chain
- 📣 問題 → 圖種 → 排版 → 交付（savefig dpi=300）
- 🎙️ 遇到新需求時照這個流程走，不會卡。

## S5-24 · PYRAMID — S5 收束 + S6 預告
- 🖼️ thesis hierarchy
- 📣 左：5 圖速查；右：4 紀律（先 subplots / sort 是靈魂 / hue+legend=False / savefig→show）；thesis：S6 加「互動」——讓老闆自己點
- 🎙️ 下節 Plotly + Capstone，把 5 圖搬上網頁讓老闆自己篩。
