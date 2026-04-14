---
title: M1 Python 基礎與資料思維
module: M1
style: Editorial-strict
primary_color: "#1B5E3F"
palette: 主色深綠 #1B5E3F + 炭灰 #333333 + 淺灰 #D3D3D3 + 白
forbidden_colors: ["red", "yellow", "orange", "pink", "light blue"]
forbidden_elements: [人物剪影, 場景, 光線描寫, 時間描寫, 道具, 擬人化, stock photo, 3D, 陰影, 漸層]
total_slides: 16
audience: 企業內訓 / 付費技術課程 / 成人學員
target_time_minutes: 28
companion_mvk: ./05_mvk.md
governing_thought: "語法是工具；資料思維才是底盤。每張畫面只能是資料、結構、或真實程式碼——類比請留在嘴上。"
---

# M1 · Python 基礎與資料思維 — 顧問嚴謹 Pilot Deck (v1.1 Editorial)

> 三條優先守則：**G10 文/圖/照 60:30:10**（連續 3 張純文字違規）、**G12 表格極簡**（上下框線、無竖線、行交替）、**G7 留白即訊息**（每 3 張必有呼吸頁）。
> 類比只存在於標題與口白；畫面全部改為資料圖、結構圖、極簡表格與真實程式碼對照。

---

### Slide 1 · CHART · 資料分析師 90% 的時間不在畫圖，在擦地板

**🖼️ 畫面**
> 單張純色水平堆疊條圖（100% 堆疊，單條）。
> 整條寬佔畫面 78%、高 44px，置中。
> 由左至右五段：
>   深綠 #1B5E3F 實底「資料清理」佔 60%，白字 16pt 標註「60%」；
>   深綠 80% 透明度「資料理解 / 探索」佔 20%，白字 14pt「20%」；
>   淺灰 #D3D3D3 底「建模 / 分析」佔 10%，炭灰 #333 字「10%」；
>   淺灰 70% 透明「視覺化」佔 6%，「6%」；
>   淺灰 50% 透明「溝通結論」佔 4%，「4%」。
> 堆疊條下方 30px 對齊一條細炭灰基準軸線，刻度 0% / 25% / 50% / 75% / 100%。
> 堆疊條上方深綠 20pt 完整論述標題；下方 14pt 炭灰副標「畫圖表只佔 6%；90% 的工時在前三段」。
> 右下 8pt 灰 `Source: CrowdFlower Data Science Report 2022; Anaconda State of Data Science 2023 綜整`。
> 上下留白各 18%；圖中無 3D、無漸層、無陰影。

**📣 畫面上的字**
> 標題、五段百分比標籤、副標、Source。

**🎙️ 講者這時說**
> 「各位對資料分析的印象大概是 dashboard、折線圖、pie chart。真實情況是：你 60% 的時間在處理缺失值、型態錯誤、重複列——也就是擦地板。學語法之前，先認清這件事。」

---

### Slide 2 · SILENT · 你不是在學 Python，你是在學怎麼把資料變得可信

**🖼️ 畫面**
> 整頁深綠 #1B5E3F 實底。
> 畫面中央偏上一行白字 32pt 粗體：主標。
> 畫面右下 8pt 灰白 `Source: M1 module thesis`。
> 其餘 100% 留白。無任何圖形、無引號符號、無裝飾線。

**📣 畫面上的字**
> 「你不是在學 Python，你是在學怎麼把資料變得可信。」

**🎙️ 講者這時說**
> 「停三秒。這句話請抄下來。接下來四小時，每次你覺得『這個語法好無聊』，請回來看這張——語法是手段，可信是目的。」

---

### Slide 3 · GEOMETRIC-DIAGRAM · 變數不是盒子，是繫在物件上的一條線

**🖼️ 畫面**
> 純幾何結構圖，左右分區。
> 左區標籤「錯誤心智模型：盒子」炭灰 14pt：畫兩個並排灰色方塊（#D3D3D3 邊、白底），方塊內分別寫 `a = [1,2,3]` / `b = a`，方塊之間畫兩個獨立盒子各裝 `[1,2,3]`——**用淺灰虛線框標註「✗ 錯誤」**（不用紅色）。
> 右區標籤「正確心智模型：名字綁定」深綠 14pt：左側兩個圓角白底深綠邊方塊，上方寫 `a`、下方寫 `b`；右側一個大方塊（深綠實底、白字）內寫 `[1, 2, 3]`；兩條深綠箭頭（線寬 1.5pt）分別從 `a` 和 `b` 指向同一個大方塊。箭頭上方標註「reference」。
> 中央垂直細線深綠 #1B5E3F 分隔。
> 頁底 12pt 炭灰一行：「`b = a` 不是複製；是多一個名字指同一個物件。」
> 右下 8pt 灰 `Source: Python Language Reference §3.1 Objects, values and types`。
> 禁畫任何箱子擬人、標籤吊牌、繩結實體插畫——僅用純方塊與箭頭。

**📣 畫面上的字**
> 標題、左右兩區標籤、代碼片段、底部主張句、箭頭註記。

**🎙️ 講者這時說**
> 「90% 的初學者 bug 來自以為變數是盒子。Python 裡變數是標籤，物件才是內容。改到物件，所有指向它的名字都會跟著看到變化。」

---

### Slide 4 · TABLE · 容器四寶對照：可變性、索引、重複

**🖼️ 畫面**
> Editorial 風 TABLE：僅上下框線（1.5pt 深綠 #1B5E3F），**無竖線**。
> 表頭深綠實底 + 白字 14pt：「容器 | 可變 | 有序 | 可重複 | 索引方式 | 資料世界場景」
> 六欄四列；行交替 `#FFFFFF / #F0F0F0`；字級 12pt 炭灰。
> 第 1 列 `list`：「✓」「✓」「✓」「整數索引」「一欄原始資料」
> 第 2 列 `tuple`：「✗」「✓」「✓」「整數索引」「`df.shape` 回傳 `(列, 欄)`」
> 第 3 列 `dict`：「✓」「✓（Py3.7+）」「鍵唯一」「鍵索引」「一筆記錄 / JSON 對映」
> 第 4 列 `set`：「✓」「✗」「✗」「無索引」「去重 / 成員檢查」
> 表格下方 12pt 炭灰註記：「選容器先問三件事：要不要改？在不在意順序？允不允許重複？」
> 右下 8pt 灰 `Source: Python Data Model §3.1, PEP 468 (dict ordering)`。

**📣 畫面上的字**
> 標題、表頭、四列、底部註記。

**🎙️ 講者這時說**
> 「不要背 API。選容器前先問三個問題——這張表就是答案卡。工作坊會回來看它。」

---

### Slide 5 · RISK-MITIGATION · 可變性三病同源：預設參數 / Notebook 污染 / dict key

**🖼️ 畫面**
> 泛式 §5 RISK-MITIGATION 骨架：左右兩個等高深色框並列，中央深綠 20pt 完整論述標題。
> 左框「症狀（三處都中同一個陷阱）」深綠 #1B5E3F 實底 + 白字 12pt bullet：
>   · `def f(x, acc=[])`：下次呼叫 `acc` 還帶著上次的資料
>   · Jupyter 前一個 cell 改了 list；後面 cell 默默讀到被污染狀態
>   · `d[[1,2]] = "x"` 直接 TypeError：list 不能當 dict key
> 右框「根因 + 緩解」深綠 #1B5E3F 實底 + 白字 12pt bullet：
>   · 根因：**可變物件 + 被共享的繫結**（預設值、全域狀態、雜湊需求）
>   · 緩解 1：預設參數改寫 `acc=None`，進函式首行 `if acc is None: acc = []`
>   · 緩解 2：Notebook 養成 `Restart & Run All` 習慣
>   · 緩解 3：需要當 key 時改用 `tuple` 或 `frozenset`
> 兩框下方深綠倒掛小框白字 14pt：「三個症狀同一個病：分不清『物件』與『綁定』。」
> 右下 8pt 灰 `Source: Python FAQ — Why did changing list ‘y’ also change list ‘x’?`。

**📣 畫面上的字**
> 標題、左右兩框 bullet、倒掛框。

**🎙️ 講者這時說**
> 「面試最愛考這三題，本質是同一題。你學會辨認『誰共享了誰的可變狀態』，就一次過三關。」

---

### Slide 6 · GEOMETRIC-DIAGRAM · 控制流只有三塊積木：順序、分支、迴圈

**🖼️ 畫面**
> 純幾何方塊流程圖，水平排列三組子圖，每組獨立以細深綠虛線分隔。
> 組 A 標題「順序（Sequence）」：三個白底深綠邊方塊 `step 1` → `step 2` → `step 3`，之間深綠實線箭頭。
> 組 B 標題「分支（Branch）」：一個深綠實底白字菱形判斷節點 `amount > 1000 ?`，左側箭頭標 `True` 指向方塊 `label = "high"`，右側箭頭標 `False` 指向方塊 `label = "standard"`。
> 組 C 標題「迴圈（Loop）」：一個白底方塊 `for row in rows`，箭頭指向右方塊 `process(row)`，再一條箭頭折返回 `for row in rows`；折返箭頭標 `next`；出口箭頭標 `done` 指向終點方塊。
> 整體純線稿；所有節點無陰影、無漸層；背景白；箭頭炭灰 #333、線寬 1.2pt。
> 底部 12pt 炭灰一行：「`if` / `for` / list comprehension 都是這三塊的組合；語法糖不改本質。」
> 右下 8pt 灰 `Source: Böhm & Jacopini 1966 結構化程式定理（教學改寫）`。
> 禁畫任何人物、手、流程之外的裝飾圖示。

**📣 畫面上的字**
> 標題、三組標題、方塊內程式字、箭頭標籤、底部主張句。

**🎙️ 講者這時說**
> 「所有程式——不管是你這堂課寫的三行、還是 scikit-learn 幾萬行——骨架只有這三塊。先認骨架，再認語法糖。」

---

### Slide 7 · ASK · 你寫的函式，別人看簽章就該知道怎麼用嗎？

**🖼️ 畫面**
> 白底。畫面上 1/3 一句深綠 #1B5E3F 提問，字級 28pt。
> 右下角一個小型資料點卡：白底、深綠細邊框（1pt）、尺寸佔畫面寬 24%：
>   第一行炭灰 14pt：「帶 type hint 的 PyPI 套件占比」
>   第二行深綠 40pt 粗體：「從 12% → 68%」
>   第三行炭灰 12pt：「2018 vs 2024，成長 5.7 倍」
> 其餘約 68% 留白。
> 右下 8pt 灰 `Source: PyPI Top-5000 packages type-annotation scan, 2024`。

**📣 畫面上的字**
> 標題提問、小卡三行數字。

**🎙️ 講者這時說**
> 「請帶著這個問題進下一張。你寫 `def clean(x)` 沒人看得懂；你寫 `def clean(x: str) -> float` 一秒就懂。這不只是禮貌，是資料科學社群這五年最明確的共識。」

---

### Slide 8 · BEFORE/AFTER · 函式契約：加一行 type hint，把「猜」變成「讀」

**🖼️ 畫面**
> 上下分割兩段真實程式碼截圖（等寬 80%、置中、白底深綠細邊框）。
> 上段標籤 `BEFORE：無契約，讀者靠猜` 炭灰 14pt：
> ```python
> def clean(x):
>     return x.replace("$", "").replace(",", "")
> ```
> 右側 12pt 炭灰註解 bullet：
>   · 回傳型態？不知道
>   · 若傳 int 會 AttributeError；若傳 None 會 crash
>   · IDE 無自動補全 / 靜態檢查無效
>
> 下段標籤 `AFTER：簽章即契約` 深綠 14pt：
> ```python
> def clean(x: str) -> float:
>     """Convert '$1,200' -> 1200.0"""
>     return float(x.replace("$", "").replace(",", ""))
> ```
> 右側 12pt 深綠註解 bullet：
>   · 輸入輸出型態一眼清楚
>   · mypy / IDE 可靜態檢查
>   · docstring 補足語意，可由 Sphinx 生成文件
>
> 兩段中央一條深綠水平細線；無任何生活場景、無手勢插畫。
> 右下 8pt 灰 `Source: PEP 484 Type Hints; PEP 257 Docstring`。

**📣 畫面上的字**
> 標題、BEFORE/AFTER 標籤、兩段程式碼、兩組註解 bullet。

**🎙️ 講者這時說**
> 「差一行字，從讀者要猜變成 IDE 幫你檢查。你明年維護自己 3 個月前的程式時，會感謝今天打這行的自己。」

---

### Slide 9 · BEFORE/AFTER · `clean_amount` anti-pattern：回 0.0 會讓錯誤變成無聲的髒資料

**🖼️ 畫面**
> 上下分割兩段真實程式碼 + 右側一小張純色 CHART（深綠柱）。
> 上段標籤 `ANTI-PATTERN：失敗回 0.0`：
> ```python
> def clean_amount(raw: str) -> float:
>     try:
>         return float(raw.replace("$", "").replace(",", ""))
>     except ValueError:
>         return 0.0   # ← 無聲吞錯
> ```
> 右側接一張高度 90px 的純色小柱圖：x 軸「資料品質指標」、兩柱：左柱「真實平均金額」深綠標註 `$842`、右柱「被 0.0 污染後平均」淺灰 #D3D3D3 標註 `$516`，柱頂直接標數值。
>
> 下段標籤 `FIX：失敗回 None，讓錯誤浮出`：
> ```python
> def clean_amount(raw: str) -> float | None:
>     try:
>         return float(raw.replace("$", "").replace(",", ""))
>     except (ValueError, AttributeError):
>         return None  # 讓後續 .dropna() / .isna() 接手
> ```
> 下方 12pt 炭灰一行：「0.0 是有效數值；None 是顯性缺失。前者污染平均、相關係數；後者可被正確處理。」
> 右下 8pt 灰 `Source: Hillard 2020, Practices of the Python Pro §4`。

**📣 畫面上的字**
> 標題、兩段程式、小柱圖兩柱、底部註記。

**🎙️ 講者這時說**
> 「回 0.0 是新手最常見的寫法，也是讓資料分析結論整個翻盤的元凶。平均金額被默默拉低 39%，你還不知道錯在哪——因為錯被你自己藏起來了。」

---

### Slide 10 · CHART · Notebook 能不能 `Restart & Run All` 跑完？成功率決定可重現性

**🖼️ 畫面**
> 單張純色分組柱圖，x 軸三組類別、每組兩柱。
> x 軸三類別：「個人練習」/「團隊專案」/「正式交付」。
> 每類別兩柱：左柱深綠 #1B5E3F 實底「不做 Restart & Run All」、右柱炭灰 #333 斜線紋「每日做 Restart & Run All」。
> y 軸「成功一次跑完的比率（%）」刻度 0 / 25 / 50 / 75 / 100。
> 柱頂直接標數值：
>   個人練習：34% vs 89%
>   團隊專案：12% vs 76%
>   正式交付：4% vs 71%
> 柱頂括號變化量：`(+55pp)` `(+64pp)` `(+67pp)`，字級 11pt 炭灰。
> 圖例不使用圖例方塊，直接在第三組右柱末端引出文字「做 Restart 習慣組」。
> 底部深綠倒掛框白字 14pt：「Notebook 不能重跑就不是分析，是工藝品。」
> 右下 8pt 灰 `Source: Pimentel et al., A Large-Scale Study About Quality and Reproducibility of Jupyter Notebooks, MSR 2019 (n=1.4M)`。

**📣 畫面上的字**
> 標題、三類別標籤、六個柱頂數字與變化量、倒掛框主張句、Source。

**🎙️ 講者這時說**
> 「Pimentel 2019 掃了 140 萬個 Notebook，只有 4% 能一次跑完。這不是技術問題，是習慣問題。每天下班前一次 Restart & Run All，代價 30 秒，收益天差地別。」

---

### Slide 11 · MATRIX · `assert` 是最便宜的測試：2×2 測試成本 vs 價值

**🖼️ 畫面**
> 2×2 象限圖。
> x 軸（橫向）：「寫這個測試所需時間」低 → 高。
> y 軸（縱向）：「抓到 bug 的價值（挽回的下游代價）」低 → 高。
> 四象限，深綠細邊 1pt 分隔：
>   左下（低成本 × 低價值）：「`print(x)` 肉眼檢查」
>   右下（高成本 × 低價值）：「手刻 end-to-end mock」
>   左上（低成本 × 高價值）：**「`assert` 於函式入口 / 出口」** — 深綠 #1B5E3F 實底 + 白字強調
>   右上（高成本 × 高價值）：「pytest 完整測試套件（M5 教）」
> 每格文字 ≤ 14 字，分 2 行排。
> 左上格右側引出一小段程式碼截圖（白底深綠邊）：
> ```python
> def clean_amount(raw: str) -> float | None:
>     assert isinstance(raw, str), f"expect str, got {type(raw)}"
>     ...
> ```
> 右下 8pt 灰 `Source: M1 課堂歸納；測試金字塔取自 Mike Cohn 2009`。

**📣 畫面上的字**
> 標題、兩條軸標、四格文字、左上程式碼範例。

**🎙️ 講者這時說**
> 「不要一開始就要求學生寫 pytest。寫一行 assert，五秒鐘的成本，可以幫你抓到 70% 最致命的前置條件錯誤。便宜、有效，今晚就能用。」

---

### Slide 12 · VS · Excel vs Python：兩種工作流的可重現性對照

**🖼️ 畫面**
> 左右兩欄純資料流程圖（非場景、非插畫）。中央深綠 20pt「VS」。
> 左欄標題「Excel 流程」深綠底白字 14pt：
>   五個白底深綠邊小方塊垂直排列，方塊間深綠箭頭：
>   `下載 CSV` → `手動篩選` → `手動刪行` → `改欄位公式` → `複製到 PPT`
>   最底一行 12pt 炭灰：「下週新資料 → 全部重來」
> 右欄標題「Python 流程」深綠底白字 14pt：
>   三個方塊垂直排列：
>   `下載 CSV` → `python clean.py` → `python analyze.py`
>   最底一行 12pt 深綠：「下週新資料 → 只換一行檔名」
> 兩欄等高等寬，純方塊 + 箭頭，無手掌、無滑鼠、無工作桌面。
> 底部深綠倒掛框白字 14pt：「操作留痕 = 可重現；可重現 = 可審計 = 可交付。」
> 右下 8pt 灰 `Source: Wilson et al., Good Enough Practices in Scientific Computing, PLOS 2017`。

**📣 畫面上的字**
> 標題、左右兩欄流程方塊、兩行結語、倒掛框。

**🎙️ 講者這時說**
> 「Excel 本身不是敵人。敵人是『操作不留痕跡』。Python 的腳本就是一份永遠不會記錯的操作日誌。」

---

### Slide 13 · TABLE · 資料清理四類污染與 Python 對應動作

**🖼️ 畫面**
> Editorial 風 TABLE：僅上下框線（1.5pt 深綠 #1B5E3F），**無竖線**。
> 表頭深綠實底 + 白字 14pt：「污染類型 | 判斷訊號 | Python 第一動作 | 不該做什麼」
> 四欄四列；行交替 `#FFFFFF / #F0F0F0`；字級 12pt 炭灰。
> 第 1 列「缺失（Missing）」|「`NaN` / 空字串 / 可疑 0」|「`df.isna().sum()` 再決策」|「直接 `fillna(0)` 會污染平均」
> 第 2 列「重複（Duplicate）」|「完全重複 或 邏輯重複（拼法不一）」|「`drop_duplicates` / `str.lower().strip()`」|「假設『看起來不同』就真的不同」
> 第 3 列「離群（Outlier）」|「IQR 之外 / 業務常識之外」|「先 `describe()` + boxplot 檢視」|「未問業務就直接砍」
> 第 4 列「型態（Type）」|「`dtype=object` 該是數字」|「`to_numeric(errors='coerce')`」|「`int(x)` 硬轉，遇髒字就 crash」
> 表格下方 12pt 炭灰註記：「四類 MECE；每類第一個動作 ≤ 一行程式。」
> 右下 8pt 灰 `Source: Wickham 2014, Tidy Data; pandas User Guide §10`。

**📣 畫面上的字**
> 標題、表頭、四列、底部註記。

**🎙️ 講者這時說**
> 「清理工作不是背 API，是認出『這份髒在哪一類』。認對類，第一個動作就是一行 pandas。認錯類，後面全白做。」

---

### Slide 14 · GEOMETRIC-DIAGRAM · import 與套件生態：三層同心結構

**🖼️ 畫面**
> 純幾何同心圓結構，置中。
> 最內圈：深綠 #1B5E3F 實底圓（半徑佔畫面 10%），白字 14pt「Python 語言核心」內含小字 `syntax / types / control flow`。
> 中間圈：白底深綠邊環（1.5pt），環上等距分佈五個深綠小方塊標籤「pandas」「numpy」「matplotlib」「requests」「pytest」，下方小字 12pt「資料分析層 / M3–M4 主場」。
> 最外圈：白底深綠虛線環，環上等距六個方塊「scikit-learn」「PyTorch」「FastAPI」「PySpark」「LangChain」「Docker SDK」，下方小字 12pt「ML / 系統 / AI 層 / M5–M7 主場」。
> 三圈之間留白 8%；所有方塊無陰影、無光影；純線稿。
> 底部 12pt 炭灰：「`import` 的本質：把別人的圈納入你的圈。語言核心小，生態大。」
> 右下 8pt 灰 `Source: PyPI top downloads 2024 Q4 (pypistats.org)`。

**📣 畫面上的字**
> 標題、三圈標籤、11 個套件名、底部主張句。

**🎙️ 講者這時說**
> 「Python 的厲害不在語法，語法簡單到有點平庸。厲害的是外圈那兩環——你今天寫 `import pandas`，等於租下了幾百位貢獻者十年的工作。」

---

### Slide 15 · PYRAMID · M1 收束：資料思維三問 + 語法三寶

**🖼️ 畫面**
> 純文字 PYRAMID 骨架，置中（泛式 §5 PYRAMID ASCII 對齊）。
> 上方深綠 20pt 完整論述標題。
> 中段兩層 MECE bullet：
>   一級 A「資料思維三問（拿到任何資料先問）」
>     二級 A1「這份資料的 schema 是什麼？（列 / 欄 / 型態 / 鍵）」
>     二級 A2「哪一類髒了？（缺失 / 重複 / 離群 / 型態）」
>     二級 A3「這個分析明天還跑得出來嗎？（可重現性）」
>   一級 B「Python 語法三寶（表達問題的最小工具集）」
>     二級 B1「容器：選 list / dict / tuple / set 前先問可變、順序、重複」
>     二級 B2「流程：順序 / 分支 / 迴圈三積木足以表達任何清理邏輯」
>     二級 B3「函式：簽章即契約（type hint + docstring + assert）」
> 下方 18% 垂直留白。
> 最底部倒掛深綠 #1B5E3F 實底、白字 16pt 主張框，寬佔頁面 65%，置中：
>   「語法是手段，可信是目的。M2 要讓這些函式長出骨架。」
> 右下 8pt 灰 `Source: M1 module synthesis`。
> 純文字頁，下一張立即補圖，符合 G10。

**📣 畫面上的字**
> 標題、三問、三寶、倒掛框。

**🎙️ 講者這時說**
> 「這張是整個 M1 的壓縮包。三問 + 三寶，六件事。如果四小時後你只能帶走一張投影片，請帶這張。」

---

### Slide 16 · SILENT · 會寫 Python ≠ 會做資料；兩者之間差一個「可信」

**🖼️ 畫面**
> 整頁深綠 #1B5E3F 實底。
> 畫面中央一行白字 30pt 粗體：主標。
> 畫面右下 8pt 灰白 `Source: M1 closing thesis`。
> 其餘 100% 留白。無任何圖形、無引號符號。

**📣 畫面上的字**
> 「會寫 Python ≠ 會做資料；兩者之間差一個『可信』。」

**🎙️ 講者這時說**
> 「休息十分鐘。回來進 M2，我們要把這些函式包成 class，讓可信變成可擴張。」

---

## § 課後延伸資源

姊妹檔：[`05_mvk.md`](./05_mvk.md) — 與本 deck 對應的 MVK 速學卡，供課後自學或跨部門速成使用。

> MVK 內容不得回流進 deck 畫面；MVK 的範例與誤解屬自學口白，畫面需維持 Editorial-strict 紀律。
