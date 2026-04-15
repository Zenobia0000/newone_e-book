# Ch09 · 02_slides_design — SOP §4.2

- 章節：Matplotlib 探索性視覺化（M4 · 1.5 hr · 17 張內容）
- Governing thought：圖不是漂亮，是問題的顯影 — 選對四種 EDA 圖、用 Figure/Axes 雙層結構 + subplots，讓資料自己開口說話。
- 配色：黑 + 灰 + 深綠（#1B5E3F）
- 每張格式：🖼️（視覺規格）/ 📣（文字骨架）/ 🎙️（口頭引導）

---

## S1 · SILENT — 開場第一口氣
- 🖼️ 深綠滿版，白字 hero。
- 📣 「圖不是漂亮，\n是問題的顯影。」
- 🎙️ Ch08 清完的 DataFrame，今天要變成眼睛看得見的訊號。我們不學美術，我們學「讓資料說話」。

## S2 · ASK — 為什麼大家 plot 完還要查文件
- 🖼️ 白底，大哉問 + 右下 data card。
- 📣 Q：「為什麼大家 plot 完還要查文件半小時？」
  Data card：label「Matplotlib 官方 Cheatsheet 下載量（2024）」· stat「4 M+」· caption「『用過就忘』是 Matplotlib 的常態 — 因為大家背 API，沒建心智模型」
- 🎙️ 因為大家把 Matplotlib 當畫筆，沒當作「Figure + Axes」的雙層建築。今天補上這塊心智模型。

## S3 · MATRIX 2×2 — EDA 四個問題 → 四種圖
- 🖼️ 2×2 方陣。
- 📣 標題「EDA 要回答的四個問題 → 四種必備圖」
  cells：
  - 「分布如何？」→ 直方圖 `ax.hist`（highlight）
  - 「有趨勢嗎？」→ 折線圖 `ax.plot`（highlight）
  - 「兩個變數有關係嗎？」→ 散佈圖 `ax.scatter`
  - 「有離群或分組差異嗎？」→ Box plot `ax.boxplot`
- 🎙️ 看圖前先問「我在回答什麼問題」— 問題決定圖，不是品味決定圖。

## S4 · IMAGE — Figure / Axes 雙層結構
- 🖼️ 滿版圖：Figure 大框 + 內含一至多個 Axes；標註 title / spines / ticks / legend 各歸屬。
- 📣 標題「Figure / Axes 雙層結構：畫布 + 座標系」
  下方 bullets：Figure = 整張畫布（可存檔的最小單位）／Axes = 畫布上的一個座標系／title、xlabel、ylabel 都屬於 Axes／一個 Figure 可以放多個 Axes（subplots）。
- 🎙️ 這張圖搞懂了，Matplotlib 所有 API 就都各就各位 — Figure 管畫布，Axes 管內容。

## S5 · VS-CODE — pyplot vs OO
- 🖼️ 上下兩個 code panel：BEFORE = 狀態式（易混）、AFTER = OO（推薦）。
- 📣 上 panel（label_dark=False）：`plt.plot(x,y); plt.title(...); plt.xlabel(...)` — 依賴「當前 Figure/Axes」的全域狀態。
  下 panel（label_dark=True）：`fig, ax = plt.subplots(); ax.plot(x,y); ax.set_title(...); ax.set_xlabel(...)` — 明確操作對象。
  bullets：狀態式上手快但多圖易亂／OO 可預測、可組合、易擴充／業界 99% 的程式碼用 OO／Linus 觀點「明確 > 隱式」。
- 🎙️ 狀態式像開車不看儀表板，OO 像開車看儀表板 — 短路顯得快，但出問題你連哪個 Axes 都找不到。

## S6 · CODE — 所有圖的共同骨架
- 🖼️ 滿版 code panel。
- 📣 code：`fig, ax = plt.subplots(figsize=(8,5)); ax.plot(x,y); ax.set_title(...); ax.set_xlabel(...); ax.set_ylabel(...); plt.show()`，註明「之後所有圖都從這裡開始」。
  bullets：記住這 5 行、所有圖只換中間 `ax.plot`／`ax.scatter`／`ax.hist`／`ax.boxplot` 一行／figsize 單位是英吋／`plt.show()` 只在 script 需要，Notebook 自動顯示。
- 🎙️ 把這 5 行肌肉記憶化，之後你只需要想「今天畫哪種圖」。

## S7 · SILENT — 分節氣口
- 🖼️ 深綠滿版，白字 hero。
- 📣 「選對圖，\n資料就會自己說故事。」
- 🎙️ 接下來四張 — 每張對應 EDA 必問的一個問題。

## S8 · IMAGE + CODE — 折線圖
- 🖼️ 左：折線圖範例 placeholder（2024 月度銷售趨勢）；右：code panel。
- 📣 code：`ax.plot(df['month'], df['sales'], marker='o', color=C.PRIMARY)` + 多條線 `ax.plot(..., label='2023'); ax.plot(..., label='2024'); ax.legend()`。
  bullets：時間或有序類別／多條線要加 label + legend／marker 幫離散點看得更清楚／X 軸類別過密時用 `fig.autofmt_xdate()`。
- 🎙️ 看到「隨時間／序列變化」— 直覺反應：折線圖。

## S9 · IMAGE + CODE — 散佈圖
- 🖼️ 左：散佈圖範例（身高 vs 體重，1 個離群）；右：code panel。
- 📣 code：`ax.scatter(df['height'], df['weight'], alpha=0.6, c=df['gender_code'], cmap='viridis')`；說明 alpha 處理重疊、c + cmap 做第三維著色。
  bullets：兩連續變數用 scatter／alpha 降透明 → 看密度／第三維用顏色（c + cmap）／離群點從 scatter 一眼看出。
- 🎙️ 兩變數畫成 scatter — 「關係」與「離群」兩個問題一張圖就有答案。

## S10 · IMAGE + CODE — 直方圖
- 🖼️ 左：直方圖範例（考試成績分布，右偏）；右：code panel。
- 📣 code：`ax.hist(df['score'], bins=20, color=C.PRIMARY, edgecolor='white')`；說明 bins 太少（失真）/ 太多（鋸齒）；用 `density=True` 變機率密度。
  bullets：單變數分布、看鐘形／偏態／多峰／bins 是唯一關鍵參數／預設 10 常常不夠、先試 20~30／要比較分布就用 `alpha=0.5` 疊圖。
- 🎙️ 拿到一欄數值 — 先 hist 一下，你才知道它「長什麼樣」。

## S11 · IMAGE + CODE — Box plot
- 🖼️ 左：三城市房價 box plot 範例；右：code panel。
- 📣 code：`ax.boxplot([df[df.city==c]['price'] for c in cities], labels=cities)`；說明 box = IQR、線 = 中位數、whisker = 1.5×IQR、點 = 離群。
  bullets：分組比較／離群點一眼可見／比 hist 更節省空間（N 個分布一張圖）／`vert=False` 轉橫式更利閱讀長標籤。
- 🎙️ 要比較多組分布 — box plot 是空間效率王，一張圖比十張 hist 更有用。

## S12 · TABLE — 四圖速查表
- 🖼️ Editorial table，4 欄（圖種／何時用／API／常見誤用）。
- 📣 rows：
  - 折線 / 時間或有序序列 / `ax.plot` / 「類別資料硬套折線 → 錯覺趨勢」
  - 散佈 / 兩連續變數關係 / `ax.scatter` / 「大量重疊不用 alpha → 看起來只有一坨」
  - 直方 / 單變數分布 / `ax.hist(bins=N)` / 「bins 沒調 → 失真」
  - Box / 多組分布比較、離群偵測 / `ax.boxplot` / 「只兩組可以，但三組以上才真正體現價值」
  下方補 1 行：「選圖 = 選問題，不是選品味。」
- 🎙️ 實戰中 90% 的 EDA 就這四張 — 其他圖（heatmap / violin / pair）是進階選項。

## S13 · CODE — 客製化三件套
- 🖼️ 滿版 code panel。
- 📣 code 含三段：
  1. 標題與軸：`ax.set_title(..., fontsize=14, pad=12); ax.set_xlabel(...); ax.set_ylabel(...)`
  2. 圖例：`ax.plot(..., label='2024'); ax.legend(loc='upper left', frameon=False)`
  3. 配色：`color='#1B5E3F'` / `color='C0'` / `cmap='viridis'`
  bullets：`set_title` vs `plt.title` — 永遠選 `ax.*` 版／label 要在 plot 時就指定，legend 才有內容／類別色用具名 `'C0'~'C9'`，連續用 cmap。
- 🎙️ 這三件套吃掉 80% 客製化需求 — 再有一點就進 `rcParams` 調全域。

## S14 · CODE — 中文字型 + savefig
- 🖼️ 滿版 code panel。
- 📣 code：
  ```
  import matplotlib.pyplot as plt
  plt.rcParams['font.family'] = 'Noto Sans CJK TC'
  plt.rcParams['axes.unicode_minus'] = False
  fig, ax = plt.subplots()
  ax.plot(...)
  fig.savefig('out.png', dpi=300, bbox_inches='tight')
  ```
  bullets：中文字型一次設定全域／`axes.unicode_minus=False` 才不會負號變方塊／savefig 放在 show 前／dpi=300 + bbox_inches='tight' 是交付標配／PDF/SVG 向量檔同指令即可。
- 🎙️ 負號變方塊是台灣/日本/韓國 Matplotlib 新手踩過的第一個坑，這一行擋掉。

## S15 · IMAGE + CODE — subplots 2×2
- 🖼️ 左：subplots 2×2 EDA 儀表板 placeholder（hist / plot / scatter / box 四圖）；右：code panel。
- 📣 code：
  ```
  fig, axes = plt.subplots(2, 2, figsize=(10, 8))
  axes[0,0].hist(df['score'], bins=20)
  axes[0,1].plot(df['month'], df['sales'])
  axes[1,0].scatter(df['height'], df['weight'], alpha=0.6)
  axes[1,1].boxplot([df[df.city==c]['price'] for c in cities])
  fig.tight_layout()
  ```
  bullets：`axes` 是 2D array，用 `[i,j]` 取子圖／`tight_layout` 解決標題軸重疊／不同子圖可獨立設 `set_title`／一張 2×2 = EDA 儀表板。
- 🎙️ 真實 EDA 幾乎都以 2×2 開場 — 一次回答四個問題。

## S16 · FLOW — EDA 四圖工作流
- 🖼️ 四節點 flow chain：分布 → 趨勢 → 相關 → 離群。
- 📣 標題「EDA 四圖工作流」
  nodes：
  1. 分布（hist） — sub「每欄先 hist 一下」（highlight）
  2. 趨勢（plot） — sub「時間欄畫 plot」
  3. 相關（scatter） — sub「兩欄配對 scatter」（highlight）
  4. 離群（box） — sub「分組 box 找異常」
  bottom note：「四個問題 → 四張圖 → 一張 2×2 subplots 封裝。」
- 🎙️ 這個順序不是教條，是拿到新資料 30 分鐘內一定要跑完的例行公事。

## S17 · PYRAMID — 收束
- 🖼️ 兩欄 thesis hierarchy + 底部深綠 thesis box。
- 📣 左欄「四圖速查（一輩子夠用）」：
  - 分布 → hist
  - 趨勢 → plot
  - 相關 → scatter
  - 離群 → box
  右欄「今天該帶走的四條紀律」：
  - 先建 `fig, ax`，再畫
  - 用 OO API（`ax.set_*`）不要混 pyplot
  - 中文字型 + 負號修正放在專案啟動時設定
  - savefig dpi=300 + bbox_inches='tight' 是交付預設
  底部 thesis：「Ch10 把 Ch08 的清洗與 Ch09 的視覺化封裝進 DataCleaner — 端到端的資料工程物件。」
- 🎙️ 你今天帶走 5 行骨架 + 4 種圖 + 4 條紀律，剩下的 Matplotlib 文件你只會在寫進階圖時才需要查。
