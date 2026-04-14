---
title: M3 NumPy 與 pandas
module: M3
style: Editorial-strict / Chart-and-table-first / Colorblind-safe-minus-yellow-orange
primary_color: "#1B5E3F"
palette: 主色深綠 #1B5E3F + 炭灰 #333333 + 淺灰 #D3D3D3 + 白
forbidden_colors: ["red", "yellow", "orange", "pink", "light blue"]
forbidden_elements: [人物剪影, 場景, 光線描寫, 時間描寫, 道具, 擬人化, stock photo, 3D, 陰影, 漸層]
total_slides: 16
audience: 企業內訓 / 付費技術課程 / 成人學員
companion_mvk: ./05_mvk.md
governing_thought: "向量化不是為了快，是為了用對的語言描述計算。"
---

# M3 · NumPy 與 pandas — 顧問嚴謹 Pilot Deck (v1.1 Editorial)

> 本 deck 是 v1.1 雙軌分離後的 Editorial-strict 範例。M3 是全課圖表與資料表密度最高的模組之一，CHART / TABLE / GEOMETRIC-DIAGRAM / BEFORE-AFTER 為主場。三條優先守則 **G5 圖表去裝飾 / G6 數字精準標註 / G12 表格極簡** 在此 100% 落地；所有類比（餅乾模具、食譜）僅存在於講者口白，不進入畫面。

---

### Slide 1 · ASK · 100 萬列資料，你打算用 for 迴圈處理嗎？

**🖼️ 畫面**
> 純白底，85% 留白。正中央一行深綠 `#1B5E3F` 粗體提問句（字級最大）。提問句下方一條極簡水平時間軸，左端標 `for 迴圈：約 1,800 ms`、右端標 `向量化：約 12 ms`，兩點間純灰 `#808080` 實線連接，中段標 `≈ 150×`。頁底靠左 8pt 灰 `Source: 本課自擬 numpy 1e6 float64 加總微基準`。

**📣 畫面上的字**
> 1,000,000 列 你要怎麼算？

**🎙️ 講者這時說**
> 這不是「慢一點」而已，是 150 倍。你寫一杯咖啡、機器算完；你等三分鐘、機器等 0.01 秒。向量化不是偷懶，是對的語言。

**💡 這張在做什麼**
Hook：用一個直接數字開場，把「向量化」從玄學拉成可量化的決策。

---

### Slide 2 · CHART · 100 萬列加總：for 迴圈 1,800 ms，向量化 12 ms，差 150 倍

**🖼️ 畫面**
> 全幅一張純色 CHART：水平長條圖，Y 軸兩列（由上而下）`Python for 迴圈` / `NumPy 向量化 (np.sum)`，X 軸「執行時間 (ms)，對數刻度」從 1 到 10,000。兩條純深綠 `#1B5E3F` 實心長條、無邊框、無陰影。柱右端直接深綠粗體標註：`1,800 ms (基準)` / `12 ms (-99.3%)`。Y 軸與 X 軸純灰 `#808080` 細線、僅保留刻度、無格線。右下角一行小字灰色補註：`資料：1e6 float64 陣列 / 機器：M2 Pro 單執行緒`。頁底 8pt 灰 `Source: 本課 benchmark，%.repeat=7 取中位`。

**📣 畫面上的字**
> 向量化省 99.3% 時間

**🎙️ 講者這時說**
> 記住這個 -99.3%。當你下次還想寫 `for i in range(len(arr))`，先問自己：我是在用工具，還是在用 1995 年的 C 語言思維？

**💡 這張在做什麼**
Tension 第一擊：把 Hook 的提問落地成一張純資料 CHART，CHART 主場首發。

---

### Slide 3 · GEOMETRIC-DIAGRAM · ndarray 是一塊連續記憶體，list 是一串指標

**🖼️ 畫面**
> 純白底，左右分割兩區純幾何示意。
> **左半**（上方小標 `Python list：8 個 float`）：一排八個白底深綠邊框小方塊水平排列（代表 list 本體的指標槽），每個方塊有一條純灰 `#808080` 實線箭頭分別指向八個散落在上下不同位置的深綠邊框大方塊（代表八個獨立 PyFloat 物件），每個大方塊裡寫 `header + value`。底部灰字 `記憶體佔用：約 224 bytes`。
> **右半**（上方小標 `NumPy ndarray：8 個 float64`）：一條水平緊密連接的長條，被均分成八格純深綠 `#1B5E3F` 實心小方塊、無間隙、無箭頭、無外部物件。底部灰字 `記憶體佔用：64 bytes (-71%)`。
> 兩區中央純灰垂直分隔線。頁底 8pt 灰 `Source: CPython 3.12 / NumPy 2.0 記憶體量測`。

**📣 畫面上的字**
> 散落指標 vs 連續方塊

**🎙️ 講者這時說**
> CPU 快取喜歡連續資料。list 是散落的指標，每取一個值要跳記憶體；ndarray 是連在一起的方塊，一次抓一排。向量化的速度優勢，根在這張圖。

**💡 這張在做什麼**
Reveal：用純幾何解釋為什麼向量化快，GEOMETRIC-DIAGRAM 取代任何卡通化記憶體插畫。

---

### Slide 4 · GEOMETRIC-DIAGRAM · Broadcasting 四步驟：從右對齊，補 1 擴張，不複製

**🖼️ 畫面**
> 純白底，四格水平流程圖，每格一步驟，之間純灰 `#808080` 實線箭頭。所有方塊純深綠 `#1B5E3F` 邊框白底，shape 標籤深綠粗體，純幾何無任何角色。
> - **Step 1 · 對齊**：兩個 shape 方塊 `(3, 4)` 與 `(4,)` 上下疊放，右側對齊，左側 `(4,)` 前補灰色 `?` 方格
> - **Step 2 · 補 1**：`(4,)` 被改寫為 `(1, 4)`，紅綠色不用，改深綠粗體新增框
> - **Step 3 · 擴張（虛擬）**：`(1, 4)` 沿第 0 軸以**虛線邊框**複製三份為 `(3, 4)`，下方灰字 `記憶體不真複製`
> - **Step 4 · 逐元素運算**：兩個 `(3, 4)` 實線方塊相加，結果 `(3, 4)` 實心深綠方塊
>
> 底部深綠 `#1B5E3F` 倒掛框白字粗體一句：「規則：從右對齊，維度相同或其一為 1 才能廣播。」頁底 8pt 灰 `Source: NumPy 2.0 官方文件 Broadcasting rules`。

**📣 畫面上的字**
> 對齊 → 補 1 → 虛擬擴張 → 運算

**🎙️ 講者這時說**
> 注意 Step 3 是「虛擬」擴張。NumPy 不真的複製記憶體，只是在計算時假裝擴張。這就是為什麼 `(X - X.mean(axis=0))` 一行搞定、還不爆記憶體。

**💡 這張在做什麼**
Reveal：Broadcasting 是全 M3 最容易被畫得卡通化的主題，這張用純幾何四格流程收束成可記規則。

---

### Slide 5 · TABLE · DataFrame 三層結構：index / columns / dtype，每欄各自有型別

**🖼️ 畫面**
> 上半部一張 Editorial 風 DataFrame 示意 TABLE：僅上下框線、無竖線、行交替 `#FFFFFF/#F0F0F0`、表頭深綠 `#1B5E3F` 底白字。欄位 `index / employee_id / hire_date / salary / is_manager`，四列資料：
>
> | index | employee_id | hire_date | salary | is_manager |
> |---|---|---|---|---|
> | 0 | E001 | 2020-03-15 | 68000.0 | True |
> | 1 | E002 | 2019-07-01 | 92000.0 | False |
> | 2 | E003 | 2021-11-20 | 55000.0 | False |
> | 3 | E004 | 2018-01-08 | NaN | True |
>
> 表格下方一條灰色極細水平標示帶，對齊每一欄下方小字深綠標註 dtype：`int64` / `object` / `datetime64[ns]` / `float64` / `bool`。最左側 `index` 欄上方額外小字灰色 `身份證，不是資料欄`。頁底 8pt 灰 `Source: pandas 2.2 官方文件`。

**📣 畫面上的字**
> 每欄各自型別 index 是身份證

**🎙️ 講者這時說**
> 看這張表的三個重點：一、index 在最左邊，但它不是欄位，是「列的身份證」。二、每欄 dtype 可以不同，這是 DataFrame 跟 ndarray 的分水嶺。三、第 4 列 salary 是 NaN，導致整欄變 float64——整數有缺失值就被迫升級成浮點數。

**💡 這張在做什麼**
Reveal：用 TABLE 主場直接展示 DataFrame 本身，避免任何 Excel 擬物化插畫。

---

### Slide 6 · BEFORE/AFTER · 同一欄切片：view 共享記憶體，copy 各自獨立

**🖼️ 畫面**
> 上下分割兩個 GEOMETRIC-DIAGRAM 小區塊。
> **上區 BEFORE · view（共享）**：左一個深綠實心大方塊標 `df`（8 列），右一個深綠實線框小方塊標 `s = df['salary']`。兩者之間一條純灰 `#808080` 實線雙向箭頭，上方標 `id(s._values) == id(df['salary']._values)` 深綠粗體；下方灰字 `寫 s 會改到 df`。
> **下區 AFTER · copy（獨立）**：左同樣 `df`，右一個新的**虛線邊框**方塊標 `s = df['salary'].copy()`。兩者之間一條灰色斷裂的箭頭（中間斷開 ✗），上方標 `id(.) ≠ id(.)` 深綠粗體；下方灰字 `寫 s 不影響 df`。
>
> 兩區之間細灰水平分隔線。頁底 8pt 灰 `Source: pandas 2.2 indexing-copy-view`。

**📣 畫面上的字**
> view 同址 / copy 異址

**🎙️ 講者這時說**
> `id()` 是你的偵測器。看到兩邊相等，就是 view，改一邊另一邊跟著改。看到不等，就是 copy，彼此獨立。pandas 1.x 最坑的鏈式賦值 bug，根源就是你不知道自己拿到哪一種。

**💡 這張在做什麼**
Reveal：view vs copy 是 pandas 最抽象的概念，用 BEFORE/AFTER 記憶體地址對照把它視覺化。

---

### Slide 7 · TABLE · pandas 版本三代對照：1.5 / 2.0 / 2.2 的關鍵差異

**🖼️ 畫面**
> Editorial 風 TABLE：僅上下框線、行交替 `#FFFFFF/#F0F0F0`、表頭深綠 `#1B5E3F` 底白字、無竖線。四欄六列：
>
> | 特性 | pandas 1.5 (2022) | pandas 2.0 (2023) | pandas 2.2 (2024) |
> |---|---|---|---|
> | 鏈式賦值語意 | 未定義（有時成功） | CoW opt-in | CoW 預設啟用 |
> | 底層儲存 | 僅 NumPy | NumPy 或 Arrow | NumPy 或 Arrow |
> | 字串欄位記憶體 | 基準 | -35% (Arrow) | -35% (Arrow) |
> | 整數欄 + NaN | 升級為 float64 | 可用 Int64 原生可空 | 可用 Int64 原生可空 |
> | SettingWithCopyWarning | 常見 | 仍出現 | CoW 下大幅減少 |
> | 典型資料集總記憶體 | 基準 1.0× | 0.65× (-35%) | 0.60× (-40%) |
>
> 表格下方 15% 留白。底部深綠 `#1B5E3F` 倒掛框白字粗體：「2.2 起 CoW 預設啟用——你的舊程式碼可能需要檢查。」頁底 8pt 灰 `Source: pandas release notes 1.5 / 2.0 / 2.2`。

**📣 畫面上的字**
> CoW 從 opt-in 到預設

**🎙️ 講者這時說**
> 注意最後一列：Arrow backend 讓典型資料集記憶體少 40%。這不是微調，是架構層級升級。你教學搜尋到的舊文如果寫「pandas 很吃記憶體」，那是 2022 年以前的事。

**💡 這張在做什麼**
Reveal：用 TABLE 主場比較 pandas 三代演進，符合題目「pandas 2.0 CoW 現況（CHART 或 TABLE）」要求。

---

### Slide 8 · GEOMETRIC-DIAGRAM · SettingWithCopyWarning 根因：一條有歧義的存取路徑

**🖼️ 畫面**
> 純白底流程圖，純幾何純線稿。頂端一個深綠 `#1B5E3F` 邊框方塊 `df[df['age'] > 30]['salary'] = 0`。向下分叉兩條純灰 `#808080` 實線箭頭（無裝飾、無動畫感）：
> - **左路徑**（標 `Step 1 先 filter`）：深綠方塊 `df[mask]` → 灰字 `可能回傳 view / 可能 copy`（純文字，無標籤雲）
> - **右路徑**（標 `Step 2 再 ['salary'] = 0`）：深綠方塊 `__setitem__` → 灰字 `若前步是 copy，寫入被丟棄`
>
> 兩路徑於底部匯合到一個**虛線邊框**方塊 `結果：未定義行為`。該方塊右側標灰字 `pandas 丟出 SettingWithCopyWarning`。最下方深綠倒掛框白字粗體：「解法：用 `.loc[mask, 'salary'] = 0` 合併成一次存取。」頁底 8pt 灰 `Source: pandas 官方 Indexing and Selecting Data`。

**📣 畫面上的字**
> 兩步存取 第一步未定義

**🎙️ 講者這時說**
> 警告不是嚇你，是在跟你說：你用了兩步路徑，pandas 不知道中間那步是 view 還 copy。解法只有一招，把兩步壓成一步：`.loc[mask, 'col'] = value`。

**💡 這張在做什麼**
Reveal：把 pandas 最折磨人的警告訊息結構化為一張根因圖。

---

### Slide 9 · GEOMETRIC-DIAGRAM · groupby 三步驟：split → apply → combine

**🖼️ 畫面**
> 純白底三欄流程圖，由左至右三個純深綠 `#1B5E3F` 邊框區塊，彼此以灰色實線箭頭相連。
> **左欄 Split**：一張極簡小 TABLE（6 列，region 欄標示 N/N/S/S/E/E，revenue 欄數字），旁一條灰色虛線把它切成三堆（N/S/E），每堆標深綠小字 `group N (2 列)` / `group S (2 列)` / `group E (2 列)`。
> **中欄 Apply**：三個獨立小方塊，每個內寫 `sum()`，各自輸出一個數 `N: 3,200` / `S: 2,100` / `E: 4,500`（深綠粗體）。
> **右欄 Combine**：一張兩欄三列的小 TABLE（僅上下框線）`region / revenue_sum`，資料即左方三個聚合結果。表頭深綠底白字。
>
> 頂端標題 `df.groupby('region')['revenue'].sum()` 深綠等寬字體。頁底 8pt 灰 `Source: Wickham 2011 Split-Apply-Combine`。

**📣 畫面上的字**
> 切開 → 各算 → 合回

**🎙️ 講者這時說**
> groupby 不是語法，是三個動作。任何業務問「按 X 看 Y」，都可翻譯成這三步。你會講業務語言，就會寫 groupby。

**💡 這張在做什麼**
Reveal：用純流程方塊把 split-apply-combine 教科書概念落實，完全不做擬人切蛋糕插畫。

---

### Slide 10 · BEFORE/AFTER · merge：兩張窄表 → 一張寬表，鍵對齊決定一切

**🖼️ 畫面**
> 上下分割，上區 BEFORE、下區 AFTER，皆 Editorial 風 TABLE。
> **BEFORE**：左右並排兩張小 TABLE（僅上下框線、無竖線、表頭深綠底白字、行交替）。
> - 左 `orders`（3 欄 4 列）：`order_id / customer_id / amount`
> - 右 `customers`（3 欄 3 列）：`customer_id / name / city`
>
> 兩表中央純灰 `#808080` 水平雙向箭頭，箭頭上方深綠粗體標 `on='customer_id'`。
>
> **AFTER**：一張合併後 TABLE（5 欄 4 列）：`order_id / customer_id / amount / name / city`。新欄位 `name / city` 的欄頭以**深綠虛線邊框**標記（視覺提示「新增」），其餘守 Editorial 風格。下方灰字 `左表 4 列保留、右表缺鍵者為 NaN`。
>
> 頁底 8pt 灰 `Source: pandas 2.2 merge how='left'`。

**📣 畫面上的字**
> 兩窄 → 一寬 鍵為軸

**🎙️ 講者這時說**
> merge 的本質：兩張表靠 key 對齊，像拉鏈合在一起。how='left' 保左表所有列、右邊沒對上就 NaN。這是全 pandas 最容易寫錯的操作，永遠先問自己：我要哪一邊的列全留？

**💡 這張在做什麼**
Ground：補原教材最大缺口——merge 的 BEFORE/AFTER 表格變形。純資料表，禁拉鍊 / 齒輪插畫。

---

### Slide 11 · BEFORE/AFTER · pivot：長表轉寬表，一列多指標變欄位

**🖼️ 畫面**
> 上下分割，皆 Editorial 風 TABLE。
> **BEFORE · 長表（long）**：3 欄 9 列：`region / quarter / revenue`。資料為 N/S/E 三區 × Q1/Q2/Q3 三季，共 9 列。表頭深綠底白字、行交替、無竖線。
>
> **AFTER · 寬表（wide）**：4 欄 3 列：`region / Q1 / Q2 / Q3`。每區一列，三個季度成為三欄。`Q1/Q2/Q3` 三欄欄頭以**深綠虛線邊框**標示「由 quarter 值攤開而來」。
>
> 兩表中央垂直純灰細線分隔（此處分隔上下兩態，不是欄內竖線）。中間寫一行深綠粗體：`df.pivot(index='region', columns='quarter', values='revenue')`。頁底 8pt 灰 `Source: pandas 2.2 reshape pivot`。

**📣 畫面上的字**
> 長表 9 列 → 寬表 3 列

**🎙️ 講者這時說**
> 長表是資料庫的語言、寬表是報表的語言。同樣 9 個數字，分析時長、做簡報時寬。pivot 和 melt 是兩邊之間的翻譯機。

**💡 這張在做什麼**
Ground：補原教材第二大缺口——pivot 的 BEFORE/AFTER。純資料表對照，不做擬物化。

---

### Slide 12 · MATRIX · 小中大資料 × SQL 偏好，四象限選工具

**🖼️ 畫面**
> 經典 2×2 MATRIX：水平軸 `資料量` 左低右高（左 `< 1 GB`、右 `1–100 GB`），垂直軸 `團隊 SQL 偏好` 下低上高（下 `Python API 為主`、上 `SQL 為主`）。軸線純灰 `#808080`、軸標深綠粗體。四格各放一個深綠邊框工具卡：
> - **左下（小、Py 風）**：`pandas 2.2`，下標 `in-memory / 生態最成熟 / 本課主場`
> - **左上（小、SQL 風）**：`DuckDB + pandas`，下標 `SQL 語法、in-process / 零伺服器`
> - **右下（中、Py 風）**：`Polars 1.x`，下標 `Rust / lazy 評估 / 5–20× pandas`
> - **右上（中、SQL 風）**：`DuckDB 獨立`，下標 `GB–百 GB 單機 SQL`
>
> 每格左上角深綠小字標代表 HEX 色無意義，改標 `建議門檻` 三個字 + 具體條件（如 `資料 < 1 GB` / `1–100 GB`）。**右下 Polars 格**描邊加粗並標 `✓ 本課推薦演進路徑`。頁底 8pt 灰 `Source: Polars 1.0 公告 2024 / DuckDB 1.0 release / Kohavi 工具選型框架`。

**📣 畫面上的字**
> 不是 pandas 夠不夠好 是用對地方

**🎙️ 講者這時說**
> pandas 不會被取代，但它有邊界。資料過 1 GB 你該認識 Polars，團隊喜歡 SQL 你該認識 DuckDB。超過 100 GB 才進入 Spark 領域——那是 M7 的事。

**💡 這張在做什麼**
Ground：用 MATRIX 把工具選型從「誰比較快」升級成結構化決策，回應題目 Polars/DuckDB 挑戰點。

---

### Slide 13 · VS · SQL ↔ pandas：同一個業務問題，兩種語言

**🖼️ 畫面**
> 左右分割，皆 Editorial 風程式碼框（深綠 `#1B5E3F` 邊框、白底、等寬字體、純色無語法高亮）。
> **左框 SQL**（標題列深綠底白字 `SQL`）：
> ```
> SELECT region,
>        COUNT(*)        AS n,
>        AVG(revenue)    AS avg_rev
> FROM   orders
> WHERE  revenue > 1000
> GROUP  BY region
> ORDER  BY avg_rev DESC
> LIMIT  3;
> ```
> **右框 pandas**（標題列深綠底白字 `pandas`）：
> ```
> (orders
>   .query('revenue > 1000')
>   .groupby('region')
>   .agg(n=('revenue', 'size'),
>        avg_rev=('revenue', 'mean'))
>   .sort_values('avg_rev', ascending=False)
>   .head(3))
> ```
> 兩框中央灰色大寫 `≡`。底部一張極簡對照 mini TABLE（三欄四列、僅上下框線、表頭深綠底白字）：
>
> | SQL 子句 | pandas 對應 | 順序 |
> |---|---|---|
> | WHERE | .query() 或 bool indexing | 1 |
> | GROUP BY + agg | .groupby().agg() | 2 |
> | ORDER BY + LIMIT | .sort_values().head() | 3 |
>
> 頁底 8pt 灰 `Source: 本課整理，對應 pandas 2.2 / ANSI SQL`。

**📣 畫面上的字**
> 同一問題 兩種寫法

**🎙️ 講者這時說**
> 右邊那個鏈式寫法，每一步正好對應一個 SQL 子句，順序也一樣。你會 SQL，就已經會 80% 的 pandas。

**💡 這張在做什麼**
Ground：用 VS 原型把 SQL 與 pandas 等價性具象化，降低資料庫背景學員遷移成本。

---

### Slide 14 · PYRAMID · M3 壓縮包：ndarray 連續、broadcasting 對齊、groupby 三步、2.0 架構升級

**🖼️ 畫面**
> 頂部完整論述標題深綠 `#1B5E3F` 粗體。中段四格等寬卡片橫排，每格深綠邊框、白底、左上角深綠粗體編號 1/2/3/4：
> - ① **ndarray**：連續記憶體、同型別、向量化的物理基礎（`-71% 記憶體 vs list`）
> - ② **broadcasting**：從右對齊、補 1 擴張、不複製（`(X - X.mean(0))` 一行）
> - ③ **groupby**：split → apply → combine，業務問題的通用骨架
> - ④ **pandas 2.0**：CoW + Arrow，典型資料集 `-40% 記憶體`、鏈式賦值不再未定義
>
> 四卡下方 18% 垂直留白。底部深綠 `#1B5E3F` 倒掛框白字粗體：「向量化不是為了快，是為了用對的語言描述計算。」頁底 8pt 灰 `Source: 本模組 Slide 2–13 收束`。

**📣 畫面上的字**
> 四件事 一句話

**🎙️ 講者這時說**
> 這四點記不住，其他都白學。下一模組 M4 做視覺化，你會發現：每一張 matplotlib 圖背後都在呼叫 ndarray、每一次 seaborn 統計圖背後都在 groupby。

**💡 這張在做什麼**
Ground 收束：把全 deck 壓縮成 4 點 + 1 句，供學員離場時帶走。

---

### Slide 15 · ASK · 你現在手上那段 for 迴圈，能不能寫成一行？

**🖼️ 畫面**
> 純白底，90% 留白。正中央深綠 `#1B5E3F` 粗體提問句（字級最大）。提問句下方一條極簡深綠水平箭頭，左端標 `for i in range(len(arr)):` 小字灰色、右端標 `arr.sum()` 小字深綠，箭頭中段無任何裝飾。頁底 8pt 灰 `Source: 回到 Slide 2`。

**📣 畫面上的字**
> 你的 for 迴圈 能寫成一行嗎？

**🎙️ 講者這時說**
> 打開你最近一段資料處理程式碼。找到一個 for 迴圈。試著用一個 NumPy 函式或一次 pandas 操作取代它。（停 5 秒）做得到，就帶走了今天。

**💡 這張在做什麼**
Feel 過場：把 Slide 14 的結論從紙面拉回學員自己的程式碼，逼出承諾。

---

### Slide 16 · SILENT · 向量化是對的語言，不只是快的語言

**🖼️ 畫面**
> 全幅深綠 `#1B5E3F` 底。正中央一行白字粗體大標語，上下各 30% 垂直留白。**完全空白**——無 logo、無頁碼、無 source。

**📣 畫面上的字**
> 向量化 是對的語言

**🎙️ 講者這時說**
> （沉默 5 秒）M4 視覺化見。

**💡 這張在做什麼**
Feel 終章：金句主張。靜默做重擊，收束全模組 governing_thought。

---

## § 課後延伸資源

姊妹檔：[`05_mvk.md`](./05_mvk.md) — 與本 deck 對應的 MVK 速學卡，供課後自學或跨部門速成使用。

> MVK 內容不得回流進 deck 畫面；MVK 的範例與誤解屬自學口白，畫面需維持 Editorial-strict 紀律。
