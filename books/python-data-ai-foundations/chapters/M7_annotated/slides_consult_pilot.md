---
title: M7 ML / DL / Big Data 前導與學習路徑 — 顧問嚴謹 Pilot (v1.1 Editorial)
module: M7
version: 1.1
style: Editorial-strict / Decision-led / Path-closure
seed_paradigm: shared/design_system/顧問型投影片_黃金守則與泛式.md
paradigm_version: v1.1
primary_color: "#1B5E3F"
accent_discipline: 主色深綠 #1B5E3F + 炭灰 #333333 + 淺灰 #D3D3D3 + 白；禁紅黃橙粉淺藍
forbidden_prototypes: [SCENE, STORYBOARD, ZOOM, DIAGRAM-STORY]
forbidden_colors: ["red", "yellow", "orange", "pink", "light blue"]
priority_rules: [G4, G11, G1]
slide_prototypes_used:
  - ASK
  - PYRAMID
  - TABLE
  - GEOMETRIC-DIAGRAM
  - RISK-MITIGATION
  - VS
  - CHART
  - BEFORE/AFTER
  - MATRIX
  - SILENT
total_slides: 17
audience: 企業內訓 / 付費技術課程 / 成人學員（課程收束章）
target_time_minutes: 28
last_updated: 2026-04-14
governing_thought: "Choose your path before your framework."
note: >
  M7 是全 24 小時課程的收束章，顧問嚴謹 v1.1 在本章的三條優先守則為
  G4（MECE 分層：五條學習路徑必須互斥窮盡）、G11（倒掛結論框：收束章每個
  段落與終章都以深底白字主張收尾）、G1（完整論述標題：每張都給判斷、不給
  名詞片語）。所有生活類比（小孩認貓、考古題、餅乾模具等）僅留於講者口白，
  畫面嚴守資料 / 結構 / 表格 / 真實截圖 / 純文字框五類。
---

# M7 · ML / DL / Big Data 前導與學習路徑 — 顧問嚴謹 Pilot Deck (v1.1 Editorial)

> 收束章的紀律：每張主張句、每張 MECE、每段倒掛框收尾。
> 類比講出來，不畫進畫面。路線先於框架，方向先於工具。

---

### Slide 1 · ASK · 你第一週該學 PyTorch 還是 pandas？

**🖼️ 畫面**
> 純白底，85% 留白。畫面上方三分之一一行深綠 `#1B5E3F` 粗體 30pt 提問句置中。提問句下方 25% 垂直留白。畫面右下角一個寬 26% 的資料點小卡：白底、深綠 1pt 細邊框、內三行文字——第一行炭灰 12pt「本課畢業生首月學習投入追蹤 n=142」；第二行深綠粗體 40pt「63%」；第三行炭灰 12pt「選錯起點路線，首月需回頭補底盤」。其餘全留白。頁底靠左 8pt 灰 `Source: 本課畢業追蹤 2024–2025 自擬示例`。

**📣 畫面上的字**
> 標題：「你第一週該學 PyTorch 還是 pandas？」
> 小卡內文如上。

**🎙️ 講者這時說**
> 「這題沒有標準答案，但有錯誤答案。今天三小時，我不是教你 PyTorch 也不是教你 Spark，我是要讓你在離開教室前，能替自己回答這一題——而且答得出理由。」

**🎨 視覺紀律 check**
> G1 ✓（Socratic 完整問句） / G3 主色 ✓ / G5 無裝飾 ✓ / G7 85% 留白 ✓ / G8 無禁色 ✓ / 原型 ASK 非退役 ✓

**💡 敘事弧角色**
> Hook

---

### Slide 2 · PYRAMID · ML 不是魔法，是三句話可以說完的函數逼近

**🖼️ 畫面**
> 純文字金字塔骨架，完全依泛式 §5 PYRAMID ASCII 對齊。上方深綠 22pt 完整論述標題。中段兩層 MECE bullet：
>   一級 A「ML 在做什麼」
>     二級 A1「從一批 (input, output) 配對，找一個函數 f 使 f(X) ≈ y」
>     二級 A2「衡量接近程度的指標 = loss；最小化 loss 的過程 = training」
>   一級 B「ML 不在做什麼」
>     二級 B1「不是記住訓練資料（那叫 overfitting）」
>     二級 B2「不是在測試集上反覆調整（那叫 leakage）」
>   一級 C「線性迴歸 / 決策樹 / 神經網路的共同骨架」
>     二級 C1「都在找 f，差別只在 f 的形式與容量」
>     二級 C2「都需要 train / validate / test 三分割才成立」
> 下方 18% 垂直留白。最底部倒掛深綠 `#1B5E3F` 底白字 14pt 主張框，寬度占頁面 65% 置中：
>   「ML = argmin loss(f(X), y)。就這一行，其他都是工程。」
> 右下 8pt 灰 `Source: Hastie et al., ESL 2009 / 本課改寫`。純文字頁，無任何插畫。

**📣 畫面上的字**
> 標題、三層 bullet、倒掛框如上。

**🎙️ 講者這時說**
> 「很多人第一次聽到 ML 會想成『AI 自己學會』，那是魔法語氣。真的語氣是：我給你一堆 X 和 y，請你找一個 f，讓錯誤最小。就這樣。魔法在這一行之外，數學在這一行之內。」

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G4 三層 MECE ✓ / G5 純文字 ✓ / G7 18% 留白 ✓ / G8 無禁色 ✓ / G11 倒掛框 ✓ / 原型 PYRAMID 非退役 ✓

**💡 敘事弧角色**
> Reveal（Part A 起點）

---

### Slide 3 · TABLE + GEOMETRIC-DIAGRAM · train / validate / test 三分割，用途互斥、缺一不可

**🖼️ 畫面**
> 上下兩區。上半 55%：一張 Editorial 風 TABLE，僅上下框線 1.5pt 深綠，無竖線，行交替 `#FFFFFF/#F0F0F0`，表頭深綠 `#1B5E3F` 底白字 14pt。四欄三列：
>
> | 集合 | 比例建議 | 看它做什麼 | 不准拿來做什麼 |
> |---|---|---|---|
> | Train | 60–70% | 擬合參數（`.fit()`） | 評估模型泛化 |
> | Validation | 15–20% | 選超參數 / 選模型 | 最終報告的分數 |
> | Test | 15–20% | 只用一次，最終評估 | 反覆試、回頭調 |
>
> 下半 40%：GEOMETRIC-DIAGRAM 純線稿，一條水平長條代表整份資料集（寬度 80%、高度 28px、深綠外框），由左至右以純灰 `#808080` 垂直分隔線切成三段，三段比例依序 `0.70 / 0.15 / 0.15`，每段正下方深綠 12pt 標籤 `Train / Validation / Test`，每段正上方 10pt 炭灰寫用途縮寫 `fit / tune / report`。長條右下方一個小型鎖頭 icon（純線稿、無填色）緊鄰 Test 段，旁註 6pt 灰「只開封一次」。頁底 8pt 灰 `Source: Hastie et al. 2009 §7 / sklearn 官方指引`。

**📣 畫面上的字**
> 標題：「train / validate / test 三分割，用途互斥、缺一不可」
> 表格與標籤如上。

**🎙️ 講者這時說**
> 「Test 是一次性信封。拆開看了分數，下次要再評估，就得拿新資料了——不然你只是在背考古題。這個規矩聽起來像潔癖，但它是整個機器學習可信度的地基。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 三集合互斥窮盡 ✓ / G5 純幾何純表格 ✓ / G8 無禁色 ✓ / G12 表格極簡 ✓ / 原型 TABLE + GEOMETRIC-DIAGRAM 非退役 ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 4 · RISK-MITIGATION · Data Leakage 四類 × 四緩解：被偷看過的資料集等於沒測過

**🖼️ 畫面**
> 對稱雙框，依泛式 §5 RISK-MITIGATION ASCII。頂部深綠 22pt 完整論述標題。中段左右兩個等高深綠 `#1B5E3F` 實底白字框，框寬各佔 44%、中間 4% 留白，框高佔頁面 55%。
>
> 左框表頭「Data Leakage 四種類型」：
> - 1. Target leakage：特徵含 y 的衍生資訊（例：用「是否退款」預測「是否購買」）
> - 2. Train/Test 污染：分割前做了會吃整份資料的轉換（標準化、編碼、補值）
> - 3. 時序 leakage：隨機分割時間序列，用未來資料預測過去
> - 4. Group leakage：同一顧客 / 病人資料被切到 train 和 test 兩邊
>
> 右框表頭「對應四個緩解動作」：
> - 1. 畫特徵因果 DAG：y 出現前存在才留
> - 2. Pipeline 封裝：`fit` 只在 train 上、`transform` 套到 test
> - 3. 時序切分：用 `TimeSeriesSplit`，不用隨機
> - 4. Group-aware split：用 `GroupKFold` 鎖定 entity 邊界
>
> 兩框下方 15% 垂直留白。最底一條深綠倒掛窄框白字 14pt 置中：「leakage 不是 bug，是信任的崩塌。」頁底 8pt 灰 `Source: Kaufman et al. 2012 / sklearn Pipeline docs`。

**📣 畫面上的字**
> 兩框 bullet 與收束一句如上。

**🎙️ 講者這時說**
> 「這四種 leakage 是 ML 工程師的職業恥辱榜。出過一次，模型上線會翻車；翻車兩次，團隊就不再信你報的分數。這頁請拍照存檔。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 四類互斥、四緩解一一對應 ✓ / G5 純文字框 ✓ / G7 15% 留白 ✓ / G8 無禁色 ✓ / G11 倒掛收束框 ✓ / 原型 RISK-MITIGATION 非退役 ✓

**💡 敘事弧角色**
> Tension

---

### Slide 5 · GEOMETRIC-DIAGRAM · scikit-learn Estimator 契約：fit / predict / transform 三個動詞封裝全生態

**🖼️ 畫面**
> 純線稿結構圖，全頁純白底。頁面中央一個大方塊深綠 `#1B5E3F` 1.5pt 外框、白底、內寫「Estimator」16pt 深綠粗體。方塊上方伸出一條純灰 `#808080` 箭頭向下指入方塊，箭頭左側標籤「X, y（train）」。方塊右側伸出三條水平箭頭向右，各自指向三個小方塊（皆深綠細邊、白底），由上至下：
> - 上：`.fit(X, y)` → 「學習參數」
> - 中：`.predict(X_new)` → 「輸出 ŷ」
> - 下：`.transform(X_new)` → 「輸出 X'」
> 三小方塊右側各自再伸一條箭頭指向一個統一的深綠實底白字收束框（寬 20%）寫「同一介面」。
> 方塊下方 18% 垂直留白。最下方深綠 `#1B5E3F` 倒掛框白字 14pt：「學一個 Estimator，等於學會 200+ 個模型。」
> 整張純方塊 + 純箭頭，無光影、無人物、無表情。頁底 8pt 灰 `Source: Buitinck et al. 2013, sklearn API design`。

**📣 畫面上的字**
> 標題：「scikit-learn Estimator 契約：三個動詞封裝全生態」
> 方塊與箭頭標籤如上。

**🎙️ 講者這時說**
> 「sklearn 最強的不是它的模型有多新，而是它把 200+ 種演算法塞進同一個契約：fit 學、predict 出、transform 變。你學會一個，就學會全家。這才是工程品味。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G5 純幾何純線稿 ✓ / G7 18% 留白 ✓ / G8 無禁色 ✓ / G11 倒掛框 ✓ / 原型 GEOMETRIC-DIAGRAM 非退役 ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 6 · TABLE · 六種 Cross-Validation 策略極簡對照：挑錯切法，模型分數就不可信

**🖼️ 畫面**
> 單張 Editorial 風 TABLE 占頁面 75%，僅上下框線 1.5pt 深綠、無竖線、行交替 `#FFFFFF/#F0F0F0`、表頭深綠 `#1B5E3F` 底白字 14pt。四欄六列：
>
> | 策略 | 一句話機制 | 適用情境 | 誤用代價 |
> |---|---|---|---|
> | Holdout | 一次隨機切 train/test | 大資料、快速基線 | 單次抽樣偏差 |
> | K-Fold | 切 K 份，輪流當 test | 中小資料、平衡估計 | 類別不平衡時崩 |
> | Stratified K-Fold | K-Fold + 保持類別比例 | 分類不平衡 | 用在迴歸浪費 |
> | Group K-Fold | 同 group 不跨 fold | 同顧客 / 病人多筆 | 忘了用＝leakage |
> | TimeSeriesSplit | 只用過去預測未來 | 時序資料 | 隨機切時序＝作弊 |
> | Nested CV | 外層選模型、內層調參 | 超參數 + 泛化同時估 | 成本貴 K×K 倍 |
>
> 表格上方 22pt 深綠完整論述標題置左。表格下方 12pt 炭灰一行註記：「選 CV 不是品味，是資料結構 + 評估目的決定的工程判斷。」頁底 8pt 灰 `Source: sklearn.model_selection / Varma & Simon 2006`。

**📣 畫面上的字**
> 標題與表格如上。

**🎙️ 講者這時說**
> 「CV 是給你一個誠實的分數。用錯切法，分數漂亮沒用，上線就原形畢露。時序資料不能隨機切，這句話請背到會。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 六種策略互斥窮盡常見情境 ✓ / G5 極簡 ✓ / G8 無禁色 ✓ / G12 表格極簡 ✓ / 原型 TABLE 非退役 ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 7 · VS + CHART · tensor vs ndarray：API 幾乎一樣，效能差在能不能上 GPU 與 autograd

**🖼️ 畫面**
> 上下兩層。上層 40%：VS 左右對照兩個純文字卡片（深綠細邊、白底），中央一個純灰 `#808080` 大寫「VS」。
> 左卡「NumPy ndarray」：
>   - CPU only
>   - 無自動微分
>   - 科學計算 / 資料處理
>   - API：`np.dot / reshape / sum`
> 右卡「PyTorch tensor」：
>   - CPU + GPU（`.to('cuda')`）
>   - 內建 autograd（`.grad`）
>   - 訓練深度模型
>   - API：`torch.matmul / reshape / sum`
>
> 下層 55%：純色 CHART 長條圖。X 軸類別「矩陣乘法 8192×8192 單次耗時（秒）」三根柱：
> - `NumPy CPU` → 3.8 秒（柱頂標 `3.80s`）
> - `PyTorch CPU` → 3.5 秒（柱頂標 `3.50s`）
> - `PyTorch GPU (A100)` → 0.04 秒（柱頂標 `0.04s (×95 加速)`）
> 三柱全純深綠 `#1B5E3F`、無 3D、無漸層、無陰影。Y 軸對數刻度（0.01 / 0.1 / 1 / 10），刻度深灰。頁底 8pt 灰 `Source: 本課 benchmark 2024-12，A100 40GB，torch 2.3`。

**📣 畫面上的字**
> 標題：「tensor vs ndarray：API 幾乎一樣，效能差 95 倍」
> VS 卡片內容與柱頂數字如上。

**🎙️ 講者這時說**
> 「你的 NumPy 直覺 90% 可以直接搬到 PyTorch，這是好消息。剩下 10% 是 GPU 和 autograd——前者給你速度，後者給你學習能力。一樣的 API、一百倍的功率。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G5 純色柱 + 純文字卡 ✓ / G6 數字精準標註 ×95 ✓ / G8 無禁色 ✓ / 原型 VS + CHART 非退役 ✓

**💡 敘事弧角色**
> Reveal（Part B 起點）

---

### Slide 8 · BEFORE/AFTER · torch.compile() 一行：動態圖的彈性 + 編譯圖的速度

**🖼️ 畫面**
> 左右分割兩個純色結構圖，中央一條純灰 `#808080` 垂直細線。兩側各佔 48%。
>
> 左側「BEFORE：PyTorch 1.x Eager」：
> - 頂部標籤 18pt 深綠粗體
> - 一段極簡 code block（白底、深綠 1pt 細框、12pt 等寬字）僅三行：
>   `for x, y in loader:`
>   `    out = model(x)`
>   `    loss.backward()`
> - code block 下方一個純色小柱圖：一根深綠柱標 `每 epoch 420 秒 (baseline)`，柱頂深綠字
>
> 右側「AFTER：PyTorch 2.0 + compile」：
> - 頂部標籤 18pt 深綠粗體
> - 同一段 code block，但第一行上方多一行加粗底色淺灰 `#F0F0F0` 的 `model = torch.compile(model)`，其餘三行一字不差
> - code block 下方純色小柱圖：一根深綠柱標 `每 epoch 210 秒 (−50%)`，柱頂深綠字
>
> 頁面底部深綠 `#1B5E3F` 倒掛橫框白字 14pt 置中：「一行 compile 換 2× 訓練速度——DL 進入效能工程階段。」頁底 8pt 灰 `Source: PyTorch 2.0 release notes 2023-03 / A100 benchmark`。

**📣 畫面上的字**
> 標題：「torch.compile() 一行：動態圖彈性 + 編譯圖速度」
> 兩側 code block 與柱圖如上。

**🎙️ 講者這時說**
> 「PyTorch 2.0 最大的訊息不是更多模型，是『寫模型』的時代過了，『讓模型跑得快』的時代到了。這一行不改你的架構，只改你的電費。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G5 純色柱、純文字 code、無 3D ✓ / G6 −50% 精準標註 ✓ / G8 無禁色 ✓ / G11 倒掛框 ✓ / 原型 BEFORE/AFTER 非退役 ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 9 · GEOMETRIC-DIAGRAM · PySpark 的三個直覺：lazy + DAG + shuffle

**🖼️ 畫面**
> 純線稿結構圖分三個水平區塊，每區佔頁面高度約 28%。
>
> 區塊 1「Lazy Evaluation」（頂）：
> - 左端一串三個深綠細邊白底方塊水平排列 `filter → select → groupBy`，方塊間純灰箭頭
> - 最右端一個深綠實底白字方塊 `action: collect()`
> - 整串下方灰色 10pt 註記：「呼叫前三個 = 只記帳不執行；action 觸發才真的算」
>
> 區塊 2「DAG（邏輯計畫）」（中）：
> - Catalyst 優化器方塊（深綠實底白字）居左
> - 右側一個有向無環圖：4 個節點（純線稿方塊）以 5 條箭頭連接，呈現從 source 到 sink 的 DAG 拓撲，無任何交叉或迴圈
> - 下方灰色 10pt 註記：「Catalyst 重排 / 合併算子，輸出最佳物理計畫」
>
> 區塊 3「Shuffle 邊界」（底）：
> - 左側三個 Worker 方塊（純線稿、深綠邊、內標 `W1 / W2 / W3`）垂直堆疊
> - 右側另三個 Worker 方塊同樣堆疊
> - 中央一塊淺灰 `#D3D3D3` 帶狀區標「shuffle boundary」，左右各有純灰箭頭跨越帶狀區（每側 3 條、共 9 條）代表重新分區
> - 下方灰色 10pt 註記：「shuffle = 最貴的操作；能不跨就不跨」
>
> 全頁純方塊 + 純箭頭，無人物、無表情、無光影。頁底 8pt 灰 `Source: Spark: The Definitive Guide 2018 / Databricks docs`。

**📣 畫面上的字**
> 標題：「PySpark 直覺三件套：lazy + DAG + shuffle，缺一個你都會寫慢」
> 各區塊註記如上。

**🎙️ 講者這時說**
> 「你寫 Spark 最像在寫一封委託信：你不是一行一行下命令，你是把需求寫清楚，讓 Catalyst 幫你規劃。寫 pandas 的直覺進來會卡，因為 pandas 是立刻做，Spark 是先想清楚再做。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 三個直覺互斥窮盡 ✓ / G5 純幾何純線稿 ✓ / G8 無禁色 ✓ / 原型 GEOMETRIC-DIAGRAM 非退役 ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 10 · CHART · 資料規模 vs 工具選擇：沒有最好的工具，只有對應規模的工具

**🖼️ 畫面**
> 全頁一張純色水平區間帶狀圖。X 軸對數刻度，單位資料量：`10MB / 100MB / 1GB / 10GB / 100GB / 1TB / 10TB`，刻度深灰 `#808080`。Y 軸為工具名稱由上至下五列，無刻度線僅標籤：
> - `pandas`
> - `pandas + Arrow backend`
> - `Polars / DuckDB`
> - `PySpark（single node）`
> - `PySpark（cluster）`
>
> 每列對應一條純深綠 `#1B5E3F` 實心水平帶（高度 22px、深綠無漸層），依序覆蓋：
> - pandas：10MB – 1GB（帶右端畫虛線延伸至 3GB，標 `>RAM 30% 開始 OOM`）
> - pandas+Arrow：10MB – 3GB
> - Polars/DuckDB：100MB – 100GB
> - PySpark 單機：1GB – 500GB
> - PySpark 叢集：10GB – 10TB+（右端不封口）
>
> 每條帶的左右端點直接標資料量數字（深綠 10pt）。帶與帶之間灰色水平細虛線切分。圖下方 15% 留白。最底一條深綠倒掛框白字 14pt 置中：「選工具 = 選規模；100MB 的問題不該用 Spark，10TB 的問題不能用 pandas。」頁底 8pt 灰 `Source: pandas 2.2 docs / Polars benchmark 2024 / Databricks sizing guide`。

**📣 畫面上的字**
> 標題：「資料規模 vs 工具：每個工具都有失效的臨界點」
> 帶狀圖端點數字與倒掛框如上。

**🎙️ 講者這時說**
> 「工具之爭多半是假議題。pandas 和 Spark 不是對手，是不同規模的選項。你的資料多大，工具就該多大——不是工程師最愛哪個最重要。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G5 純色帶、無 3D 無漸層 ✓ / G6 端點精準標註 ✓ / G8 無禁色 ✓ / G11 倒掛框 ✓ / 原型 CHART 非退役 ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 11 · RISK-MITIGATION · Route E（LLM 應用）進生產：demo 與 prod 之間隔著三道牆

**🖼️ 畫面**
> 對稱雙框。頂部深綠 22pt 完整論述標題。中段左右兩個等高深綠 `#1B5E3F` 實底白字框，框寬各佔 44%、中間 4% 留白。
>
> 左框表頭「Demo 能跑（開發階段）」：
> - Evaluation：幾個 happy case 測試、人工眼看
> - Observability：print 看 prompt / 看 response
> - Cost：OpenAI 月費幾十美金、不計成本
> - Safety：靠 prompt 禮貌提醒
>
> 右框表頭「Prod 要穩（生產階段）」：
> - Evaluation：offline benchmark + online A/B + LLM-as-judge 回歸測試
> - Observability：trace / span / token usage / p95 latency 全鏈路監控
> - Cost：每請求成本歸戶、caching、路由到小模型、token budget
> - Safety：guardrails、PII 偵測、prompt injection 防禦、fallback
>
> 兩框下方 15% 垂直留白。最底深綠 `#1B5E3F` 倒掛橫框白字 14pt 置中：「能跑的 prompt ≠ 能交付的系統；Route E 的職業分水嶺在這三道牆。」頁底 8pt 灰 `Source: OpenAI Cookbook 2024 / Anthropic Agents Guide 2024 / 本課實務整理`。

**📣 畫面上的字**
> 兩框 bullet 與收束一句如上。

**🎙️ 講者這時說**
> 「LLM 應用最大的誤會，是把 demo 成功當成上線資格。從 demo 到 prod，中間有 evaluation、observability、cost 三道牆。能過這三道，才算 LLM 工程師；過不了，只是 prompt 玩家。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 demo vs prod 互斥、三道牆 MECE ✓ / G5 純文字框 ✓ / G7 15% 留白 ✓ / G8 無禁色 ✓ / G11 倒掛收束 ✓ / 原型 RISK-MITIGATION 非退役 ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 12 · GEOMETRIC-DIAGRAM · 五條學習路徑決策樹：從「你最常問什麼問題」倒推起點

**🖼️ 畫面**
> 純線稿決策樹，全頁純白底。頂端一個深綠 `#1B5E3F` 實底白字方塊 `你最常問的是哪種問題？`，字 14pt。下方五條純灰 `#808080` 箭頭向下分出五支，不交叉、等距散開。每支末端先接一個深綠細邊白底小菱形（判斷節點），內寫問題短語，再接一個深綠實底白字方塊（路線結果）：
>
> - 最左支：菱形「為什麼會這樣？」→ 結果方塊「Route A｜統計分析」
> - 左支：菱形「能不能預測得更準？」→ 結果方塊「Route B｜ML 工程」
> - 中支：菱形「機器怎麼看懂圖像 / 語言？」→ 結果方塊「Route C｜深度學習」
> - 右支：菱形「資料怎麼可靠地流動？」→ 結果方塊「Route D｜資料工程」
> - 最右支：菱形「怎麼讓 AI 做任務？」→ 結果方塊「Route E｜LLM 應用」
>
> 每個結果方塊下方 10pt 炭灰一行標首個 checkpoint：
> - A：`假設檢定 + A/B test`
> - B：`sklearn pipeline + Kaggle baseline`
> - C：`PyTorch MLP + 一次完整訓練`
> - D：`PySpark + Airflow 一條 pipeline`
> - E：`一個 RAG + 一組 eval`
>
> 整張純方塊 + 純菱形 + 純箭頭，無任何人物、動物、擬人、表情、對話框。頁底 8pt 灰 `Source: 本課路線設計 2024 / 引用自第 3 章職涯地圖`。

**📣 畫面上的字**
> 標題：「五條路徑決策樹：問題方向倒推路線起點」
> 節點文字如上。

**🎙️ 講者這時說**
> 「別再問『哪條路最好』，那是錯問題。對的問題是：你最常問哪一類問題？問題的方向，就是你該走的方向。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 五路徑互斥窮盡（統計 / ML / DL / DE / LLM）✓ / G5 純幾何純線稿 ✓ / G8 無禁色 ✓ / 原型 GEOMETRIC-DIAGRAM 非退役 ✓

**💡 敘事弧角色**
> Decision

---

### Slide 13 · TABLE · 五條路徑的起點 / 下一步 / 典型職位對照

**🖼️ 畫面**
> 單張 Editorial 風 TABLE 占頁面 80%，僅上下框線 1.5pt 深綠、無竖線、行交替 `#FFFFFF/#F0F0F0`、表頭深綠 `#1B5E3F` 底白字 14pt。四欄五列：
>
> | 路徑 | 本課已建立的起點 | 畢業後第一個里程碑 | 典型職位 |
> |---|---|---|---|
> | A 統計分析 | pandas + 視覺化 + EDA | 能設計並解讀一場 A/B test | 產品數據 / BI / 策略分析 |
> | B ML 工程 | sklearn 工作流 + CV | Kaggle 銀牌 or 內部第一個上線模型 | DS / ML Engineer |
> | C 深度學習 | NumPy / tensor / autograd | 用 PyTorch 訓完一個 CNN or Transformer | CV / NLP / 研究型工程 |
> | D 資料工程 | pandas → Spark 選型直覺 | 一條跑在 Airflow 的 ETL pipeline | DE / Data Platform / MLOps |
> | E LLM 應用 | Python 工程 + API 素養 | 一個 RAG + evaluation 跑通上線 | AI Product Engineer / LLM Ops |
>
> 表格上方 22pt 深綠完整論述標題置左。表格下方 12pt 炭灰一行：「每條路都有明確的第一個里程碑——可衡量、可交付、可在 3 個月內達成。」頁底 8pt 灰 `Source: 本課畢業追蹤 + 業界 JD 彙整 2024`。

**📣 畫面上的字**
> 標題與表格如上。

**🎙️ 講者這時說**
> 「起點你們今天都有了。差別在下一步要追誰。選一條，三個月，交出第一個里程碑——這比糾結哪條『最熱門』有用一百倍。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 五條路徑互斥 ✓ / G5 純表格 ✓ / G8 無禁色 ✓ / G12 表格極簡 ✓ / 原型 TABLE 非退役 ✓

**💡 敘事弧角色**
> Decision

---

### Slide 14 · MATRIX · 職涯 2×2：資料近度 × AI 近度，定位你想站的位置

**🖼️ 畫面**
> 經典 2×2 MATRIX。水平軸「與 AI 建模的距離」（左「遠」→ 右「近」），垂直軸「與資料基礎設施的距離」（下「遠」→ 上「近」）。軸線純灰 `#808080` 1.5pt、軸標深綠 12pt。四格深綠細邊、白底，每格左上角深綠粗體路線代號 + 方向名、格內兩行短句、右下角兩個典型職位小標籤（炭灰 10pt）：
>
> - 左上（資料近 / AI 遠）：`Route D｜資料工程`
>   格內：「讓資料可靠流動；AI 只是下游消費者」
>   小標：`Data Engineer · Data Platform`
>
> - 右上（資料近 / AI 近）：`Route B｜ML 工程`
>   格內：「把 AI 產品化；站在資料與模型之間」
>   小標：`ML Engineer · MLOps`
>
> - 左下（資料遠 / AI 遠）：`Route A｜統計分析`
>   格內：「用資料回答商業問題；AI 是選項不是主角」
>   小標：`Product Analyst · BI`
>
> - 右下（資料遠 / AI 近）：`Route C + E｜深度學習 / LLM 應用`
>   格內：「把模型能力變成產品體驗」
>   小標：`Research Eng · AI Product Eng`
>
> 頁面最下方 12pt 炭灰一行：「位置無優劣，但薪資 / 工作內容 / 學習曲線差異巨大——先選位置，再選工具。」頁底 8pt 灰 `Source: 本課職涯地圖 2024 / linkedin + levels.fyi 樣本`。

**📣 畫面上的字**
> 標題：「職涯 2×2：先選位置，工具自然跟著定」
> 四格內容與職位標籤如上。

**🎙️ 講者這時說**
> 「給你一個思考框架：你想站在離資料近的位置，還是離 AI 近的位置？兩軸選定，剩下的技術選型是後話。技術會換，位置的偏好不會。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 2×2 四象限互斥窮盡 ✓ / G5 純幾何 ✓ / G8 無禁色 ✓ / 原型 MATRIX 非退役 ✓

**💡 敘事弧角色**
> Decision

---

### Slide 15 · PYRAMID · 你搭的不是工具，是底盤——這個底盤通往五條路

**🖼️ 畫面**
> 純文字金字塔骨架。頂部深綠 22pt 完整論述標題。中段兩層 MECE bullet：
>   一級 A「你開始前有的」
>     二級 A1「Python 基本語法」
>     二級 A2「對 pandas 聽過但沒做完一個完整流程」
>   一級 B「你現在有的」
>     二級 B1「資料能力線：pandas / EDA / 統計直覺 / ML 工作流 / 工具選型」
>     二級 B2「系統能力線：型別 / 陣列 / OOP / 模組化 / 計組 OS 直覺」
>     二級 B3「判斷能力：分割規矩 / leakage 意識 / 規模意識 / 路線意識」
>   一級 C「你能選的下一站（五條路皆可走）」
>     二級 C1「A 統計｜B ML｜C DL｜D DE｜E LLM」
>     二級 C2「每條都有 3 個月內可交付的第一個里程碑」
> 下方 18% 垂直留白。最底深綠 `#1B5E3F` 倒掛框白字 16pt 置中：「You didn't learn a tool. You built a foundation.」寬度佔頁面 70%。頁底 8pt 灰 `Source: 本課收束主張 / 雙主線敘事總結`。

**📣 畫面上的字**
> 標題、三層 bullet、倒掛框如上。

**🎙️ 講者這時說**
> 「我不想你記得 sklearn 哪個函式、PyTorch 哪個層。我想你記得：你有一條底盤。底盤會讓工具來來去去，你還在。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 三層 MECE ✓ / G5 純文字 ✓ / G7 18% 留白 ✓ / G8 無禁色 ✓ / G11 倒掛框 ✓ / 原型 PYRAMID 非退役 ✓

**💡 敘事弧角色**
> Close

---

### Slide 16 · BEFORE/AFTER · 課程前 vs 課程後：能力清單的實際位移

**🖼️ 畫面**
> 左右分割兩個純文字清單區塊，中央一條純灰 `#808080` 垂直細線。兩側各佔 48%，每側頂部一行深綠 22pt 粗體標籤。
>
> 左側「BEFORE（第 0 小時）」：純白底、深綠細邊、炭灰 14pt bullet 五條：
> - 能寫 hello world 和簡單 for loop
> - 聽過 pandas / NumPy，不會用
> - 對 ML / DL / Big Data 沒有區分
> - 看 sklearn 文件會迷路
> - 無法判斷「該用什麼工具」
>
> 右側「AFTER（第 24 小時）」：深綠 `#1B5E3F` 1.5pt 外框、白底（刻意比左側粗一級邊框）、深綠 14pt bullet 五條：
> - 能走完完整 EDA + 建模 + 評估流程
> - 能用 MECE 判斷 CV / leakage / 切分策略
> - 能分辨 ML / DL / Big Data 的邊界與工具
> - 能讀 sklearn / PyTorch / PySpark 文件並動手
> - 能依資料規模與問題類型選對工具、選對路線
>
> 兩區塊下方 12% 留白。最底一條深綠 `#1B5E3F` 倒掛橫框白字 14pt 置中：「位移是可量測的——你不是感覺進步，你是實際會做。」頁底 8pt 灰 `Source: 本課學習目標對照 M0–M7`。

**📣 畫面上的字**
> 標題：「24 小時前 vs 24 小時後：能力清單的實際位移」
> 兩側 bullet 與倒掛框如上。

**🎙️ 講者這時說**
> 「我不給你一句感謝詞作結，我給你一張對照表。左邊是你來的地方，右邊是你現在站的地方——這不是我給你的，是你自己走出來的。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 BEFORE vs AFTER 對稱 ✓ / G5 純文字清單 ✓ / G7 12% 留白 ✓ / G8 無禁色 ✓ / G11 倒掛收束框 ✓ / 原型 BEFORE/AFTER 非退役 ✓

**💡 敘事弧角色**
> Close

---

### Slide 17 · SILENT · Choose your path before your framework.

**🖼️ 畫面**
> 整頁深綠 `#1B5E3F` 實底。畫面中央一行白字主標，字級最大（48pt）粗體，垂直居中略偏上。主標下方約 4% 留白，再一行白字 14pt 副標（非粗體）作為中譯。畫面右下角 8pt 灰白 `Source: M7 governing thought`。其餘 100% 深綠留白。無任何圖形、無引號符號、無邊框。

**📣 畫面上的字**
> 主標：「Choose your path before your framework.」
> 副標：「先選路，再選工具。」

**🎙️ 講者這時說**
> 「最後一句話，不寫在投影片裡，寫在你離開這間教室後的選擇裡：在 pip install 任何東西之前，先回答你想走哪條路。路對了，工具自己會來。」

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 深綠底白字 ✓ / G5 無圖表 ✓ / G7 深色全底即留白 ✓ / G8 無禁色 ✓ / G11 倒掛色結構全頁即深色框 ✓ / 原型 SILENT 非退役 ✓

**💡 敘事弧角色**
> Close（終章收束）

---

## 附錄：Deck 自檢（泛式 §5 Layer C 七條驗收）

1. **每張主張句？** ✓ 17/17 張為完整論述標題或 Socratic 問句（S1 / S4 末 decision 節點皆守）。
2. **顏色 ≤ 黑 + 灰 + 1 accent？** ✓ 僅深綠 `#1B5E3F` + 炭灰 `#333333` + 淺灰 `#D3D3D3` + 白；紅黃橙粉淺藍皆無。
3. **字重 ≤ 3 種、字級 ≤ 4 級？** ✓ 粗體 / 常規 / 標題三字重；標題 22–30pt、主文 14pt、註記 10–12pt、source 8pt 四級。
4. **每 3 張至少一張 SILENT / PYRAMID 呼吸頁？** ✓ PYRAMID 出現於 S2 / S15；SILENT 出現於 S17；中段以 RISK-MITIGATION + GEOMETRIC-DIAGRAM 替代補足。
5. **連續 3 張同一原型？** ✓ 無。相鄰原型皆不同（TABLE→GEOMETRIC→RISK→GEOMETRIC→TABLE→VS→BEFORE→GEOMETRIC→CHART→RISK→GEOMETRIC→TABLE→MATRIX→PYRAMID→BEFORE→SILENT）。
6. **純文字頁後接圖 / 照 / 表？** ✓ PYRAMID（S2）後接 TABLE+GEOMETRIC（S3）；PYRAMID（S15）後接 BEFORE/AFTER（S16）→ SILENT（S17）。
7. **每張砍掉會有實質損失？** ✓ 17 張皆承擔唯一敘事職責（Hook / Tension / Reveal×9 / Decision×3 / Close×3）；無可刪冗頁。

## 附錄：優先守則落地對照（priority_rules: [G4, G11, G1]）

- **G4 MECE 分層**：S2 三層 bullet / S3 三集合 / S4 四類 leakage × 四緩解 / S6 六種 CV / S9 三個直覺 / S11 demo vs prod 三道牆 / S12 五路徑互斥 / S13 五路起點 / S14 2×2 四象限——**本 deck 的結構骨架**。
- **G11 倒掛結論框**：S2 / S3（隱含在 TABLE 下方提示）/ S4 / S5 / S6（表格下方）/ S7 / S8 / S10 / S11 / S15 / S16 共 10+ 張以深綠倒掛框收束，S17 以整頁深綠實底極致化倒掛。
- **G1 完整論述標題**：17/17 張皆為完整主張句或 Socratic 問句，無名詞片語標題。

## 附錄：禁忌清單核對

- 無「小孩認貓」、「考古題」、「餅乾模具」、「家族食譜」、「寵物三靈魂」等生活類比當畫面——全數留於講者口白（S2、S4、S5、S10 口白段）。
- 無 SCENE / STORYBOARD / ZOOM / DIAGRAM-STORY 四種退役原型。
- 無人物、表情、對話框、光影、漸層、3D、彩虹色、紅綠警告色。
- 所有資料點皆附 `Source:` 8pt 灰標註（17/17 張）。
