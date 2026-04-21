# S1 — NumPy 與向量化思維｜Slides Design

> 23 張內容投影片（封面 + 23 + 版權）｜教學型七原型為主
> 對齊 `01_outline.md` 的 5 個 Learning Objectives × 5 個 Common Pitfalls
> 配色：主色 `#1B5E3F` + 錯誤紅 `#C62828`（僅 PITFALL 頁）+ 成功綠 `#2E7D32`

---

## S1 · MOTIVATION — 別再等 for-loop 跑完

- 🖼️ 畫面：全白底 / 大字痛點句 / 右下一張小數據卡（1e7 筆實測對比）
- 📣 畫面上的字：
  - 標題：「你還在等 for-loop 跑完？」
  - 副標：1,000 萬筆加總 · Python list: 3.2s · NumPy: 0.04s · **80×**
- 🎙️ 講者這時說：「在座有多少人寫過一個 for-loop 跑了五分鐘，然後才發現結果算錯？我們今天要把這件事情從『寫 for 開始，等它跑完，再除錯』，改成『一行寫完，眨一下眼就出結果』。不是讓 Python 變快，是換一種思維。」

---

## S2 · ASK — 同一台電腦，差在哪？

- 🖼️ 畫面：白底，中央大字問句，右下資料卡（80× caption）
- 📣 畫面上的字：
  - 「同一台電腦、同一個 Python——為什麼差 80 倍？」
  - 卡片提示：「不是 CPU，是運算在哪一層跑」
- 🎙️ 講者這時說：「線索給你們：不是 Python 變快，也不是 CPU 換了。差別在『運算發生的位置』。Python list 的 for-loop 每一輪都要進直譯器；NumPy 把整個運算丟給底下的 C 程式庫一次算完。記住這句話——它是整節課的地基。」

---

## S3 · SILENT — 一句話立論

- 🖼️ 畫面：全綠底 / 白色 HERO 大字置中
- 📣 畫面上的字：「NumPy 不是『加個 np. 就好』，是換一種語言想運算。」
- 🎙️ 講者這時說：「這頁我故意不給太多字。記住這句話——今天你離開教室如果只記得一件事，就是這個：向量化是一種思維，不是語法糖。」

---

## S4 · CONCEPT-CARD — ndarray 的本質

- 🖼️ 畫面：左欄文字定義 + 右欄 ndarray 記憶體佈局示意（真圖佔位）
- 📣 畫面上的字：
  - 標題：「ndarray ＝ 連續記憶體 + 一層 view」
  - 左：三個屬性（shape 形狀 / dtype 型別 / ndim 維度）各一句
  - 右：記憶體格子圖（連續一排 int64 + 上方覆蓋 shape label）
- 🎙️ 講者這時說：「把 ndarray 想成一塊『連續的記憶體』加上一層『眼鏡』。眼鏡告訴你這塊記憶體要被看成 (3,4) 還是 (12,)——資料完全沒動，只是詮釋方式換了。這就是 reshape 為什麼免費。」

---

## S5 · EXAMPLE-I/O — np.array() 三欄示範

- 🖼️ 畫面：三欄 Input | Process | Output，中間箭頭
- 📣 畫面上的字：
  - 欄1 Input：`[[1,2,3],[4,5,6]]`（Python list）
  - 欄2 Process：`a = np.array(lst)`（code panel）
  - 欄3 Output：`a.shape → (2,3)`、`a.dtype → int64`、`a.ndim → 2`
- 🎙️ 講者這時說：「三欄走一次：左邊給我們熟悉的 Python list；中間一行 np.array；右邊就有了 shape / dtype / ndim。這三個屬性是你之後每次 debug 的第一張牌。」

---

## S6 · CHECKPOINT — shape 快問快答

- 🖼️ 畫面：白底 / 標題「Check Point · shape 怎麼讀」/ 三題列點
- 📣 畫面上的字：
  - Q1：`(3,)` 是幾維？
  - Q2：`(3,1)` 與 `(1,3)` 差在哪？
  - Q3：`(2,3,4)` 有幾個元素？
- 🎙️ 講者這時說：「不看投影片，舉手答——(3,) 是一維還是二維？(3,1) 是列向量還是行向量？為什麼這重要？因為等下 broadcasting 出錯你第一件事就是看 shape。」

---

## S7 · MECHANISM-FLOW — 索引三件套

- 🖼️ 畫面：三個方塊橫排 + 箭頭：基本切片 → 布林遮罩 → fancy indexing
- 📣 畫面上的字：
  - 方塊1「基本切片 a[1:3]」sub：view、零複製
  - 方塊2「布林遮罩 a[a>0]」sub：篩選、像 WHERE
  - 方塊3「fancy index a[[0,2,5]]」sub：copy、任意取
- 🎙️ 講者這時說：「三種索引語意完全不同。切片是借鏡——沒複製；遮罩像 SQL 的 WHERE；fancy indexing 是『我點名要哪幾個』，這個會 copy。等下每個都做一次。」

---

## S8 · PITFALL — and 不能用，要用 &

- 🖼️ 畫面：VS 兩欄，左紅邊「✗ 錯」右綠邊「✓ 對」，下方一句 why
- 📣 畫面上的字：
  - 左欄：`a[a>0 and a<10]` → `ValueError: truth value ambiguous`
  - 右欄：`a[(a>0) & (a<10)]` → `array([...])`
  - 下方：「為什麼：and/or 期待單一 bool，但遮罩是整個陣列」
- 🎙️ 講者這時說：「這是本節最常見 bug——你可能一輩子都會踩一次。and 期待一個 True/False，可是遮罩給它的是一整排。記住：元素級運算用 & | ~，而且『每一塊括號都不能省』。」

---

## S9 · EXAMPLE-I/O — 布林遮罩篩分數

- 🖼️ 畫面：三欄 Input | Process | Output
- 📣 畫面上的字：
  - Input：`scores = np.array([45,72,88,51,99,100,38])`
  - Process：`scores[(scores>=60) & (scores<=100)]`
  - Output：`array([72, 88, 99, 100])`
- 🎙️ 講者這時說：「用 for-if 寫要四行，用布林遮罩一行。重點是括號——少一個 () 就噴 ValueError。」

---

## S10 · PITFALL — 切片是 view 不是 copy

- 🖼️ 畫面：VS 兩欄，左紅「以為是 copy」右綠「其實是 view」
- 📣 畫面上的字：
  - 左：`b = a[:3]; b[0] = 99` → `a` 也變了（紅色驚嘆）
  - 右：`b = a[:3].copy(); b[0] = 99` → `a` 不動
  - 下方：「為什麼：切片共用記憶體，NumPy 預設不 copy，是為了省記憶體」
- 🎙️ 講者這時說：「這個坑很深——你在做特徵工程時改了『子集』，結果發現原資料也動了。記住：需要獨立副本就 .copy()。這跟 Python list 的 [:] 不一樣！」

---

## S11 · CONCEPT-CARD — 向量化的本質

- 🖼️ 畫面：左欄「for-loop 在 Python 層」右欄「向量化在 C 層」，下方一行小字
- 📣 畫面上的字：
  - 左：每次迴圈進直譯器 / 每個值包 PyObject / 慢
  - 右：整個運算送進 C / 連續記憶體走 SIMD / 快
  - 下方：「向量化 ≠ 加 np.；是讓整塊運算一次離開 Python」
- 🎙️ 講者這時說：「注意副標那句——『加 np. 不等於向量化』。如果你在 for 裡面呼叫 np.sum，還是慢。關鍵是讓 Python 層『一次都不要進入迴圈』。」

---

## S12 · CHART / CHECKPOINT — 1e7 實測對比

- 🖼️ 畫面：上半 bar chart（list 3.2s / NumPy 0.04s）+ 下半一句 takeaway
- 📣 畫面上的字：
  - 標題：「1,000 萬筆加總實測」
  - Bar：Python list 3.20 s ｜ NumPy 0.04 s
  - 徽章：**80×**（右上角 delta badge）
  - 下方：「而且 NumPy 那行，只有 12 個字」
- 🎙️ 講者這時說：「我剛才在電腦現場跑的，不是投影片騙你。80 倍不是理論值，是你的筆電今天就能複現的。把這個數字記下來——下次你老闆問『這可不可以更快』，你就知道答案在這裡。」

---

## S13 · CONCEPT-CARD — Broadcasting 兩條規則

- 🖼️ 畫面：左規則文字 + 右 shape 對齊示意圖（真圖佔位）
- 📣 畫面上的字：
  - 規則1：「從右往左對齊每個維度」
  - 規則2：「該維度相等，或其中一個是 1 → 可擴展；否則報錯」
  - 右圖：`(3,1)` + `(1,4)` → `(3,4)` 的網格擴展
- 🎙️ 講者這時說：「Broadcasting 只有兩條規則。從右邊開始對齊，相等 OK，一邊是 1 也 OK，其它通通報錯。畫一張圖比我講 10 分鐘有用——看著這張網格圖把它記下來。」

---

## S14 · PITFALL — (3,) vs (3,1) 不是同一件事

- 🖼️ 畫面：VS 左「(3,) + (3,) → (3,)」右「(3,1) + (3,) → (3,3)」
- 📣 畫面上的字：
  - 左：一維 + 一維 = 逐元素加總
  - 右：列向量 + 一維 = broadcasting 成 3×3 矩陣（意外！）
  - 下方：「shape 看起來像，結果完全不同；不確定就先 .shape 印出來」
- 🎙️ 講者這時說：「這是 broadcasting 第二大坑——你以為在做逐元素，結果做出一個矩陣。記得 debug 時第一件事：`print(a.shape, b.shape)`。」

---

## S15 · EXAMPLE-I/O — 電商：總庫存價值

- 🖼️ 畫面：三欄 Input | Process | Output
- 📣 畫面上的字：
  - Input：`price = np.array([199, 599, 1299, 89])`、`stock = np.array([120, 45, 8, 300])`
  - Process：`(price * stock).sum()`
  - Output：`total_value = 77,215`
- 🎙️ 講者這時說：「過去你用 Excel SUMPRODUCT，現在一行。注意——price × stock 是逐元素乘，不是矩陣乘。這就是 broadcasting 在 (4,) + (4,) 的最單純情況。」

---

## S16 · EXAMPLE-I/O — 電商：低庫存商品數

- 🖼️ 畫面：三欄 + 下方一句商業解讀
- 📣 畫面上的字：
  - Input：同上 stock
  - Process：`(stock < 10).sum()`
  - Output：`1`（表示庫存 < 10 的商品有 1 個）
  - 下方：「布林的 True = 1 / False = 0，sum 就是 count-if」
- 🎙️ 講者這時說：「這個招式我叫它『布林加總 = 計數』——凡是 SQL 的 COUNT(WHERE…) 通通可以這樣寫。今天帶走這招就值回票價。」

---

## S17 · PITFALL — for-loop 的反模式

- 🖼️ 畫面：VS 左紅「for-loop 版」右綠「向量化版」
- 📣 畫面上的字：
  - 左：`total = 0`\n`for x in data:`\n`    total += x * 2`（紅標：慢 50×）
  - 右：`total = (data * 2).sum()`（綠標：一行、快、可讀）
  - 下方：「看到 for + 數字運算 = 先問自己『這能不能向量化』」
- 🎙️ 講者這時說：「這是寫 NumPy 的第一反射：看到 for 處理數字，立刻停手，問自己『這能不能用陣列運算』。80% 的情況都可以。」

---

## S18 · CHECKPOINT — 中段驗收

- 🖼️ 畫面：白底，三題列點
- 📣 畫面上的字：
  - Q1：`a[:3]` 是 copy 還是 view？
  - Q2：`(4,) * (4,1)` 結果 shape 是什麼？
  - Q3：`data[(data>0) and (data<10)]` 會發生什麼？
- 🎙️ 講者這時說：「30 秒——不看講義，口頭回答。三題都答得出來就繼續往下；有一題卡住就回頭翻 S8 / S10 / S14。」

---

## S19 · PITFALL — 浮點比較的陷阱

- 🖼️ 畫面：VS 左紅 `==` 右綠 `np.isclose`
- 📣 畫面上的字：
  - 左：`0.1 + 0.2 == 0.3` → `False`（紅色 ✗）
  - 右：`np.isclose(0.1 + 0.2, 0.3)` → `True`（綠色 ✓）
  - 下方：「浮點是近似值；任何浮點相等比較都要用 np.isclose()」
- 🎙️ 講者這時說：「最後一個坑——這不只是 NumPy 的問題，是整個計算機的問題。浮點沒辦法精確表示 0.1。做金融、做科學計算，這行一定要變成肌肉記憶。」

---

## S20 · PRACTICE-PROMPT — 🟡 核心練習

- 🖼️ 畫面：白底 / 大字題目 / 底部計時器
- 📣 畫面上的字：
  - 標題：「練習時間 · 3 分鐘 · 各自動手」
  - 題目：給定 price / stock / category 三個陣列，用一行分別寫出：
    1. 總庫存價值
    2. 低庫存商品數（stock < 10）
    3. 平均售價
  - 提示：Think-Pair-Share / 完成後與鄰座對答案
- 🎙️ 講者這時說：「三分鐘——現在就打開 Notebook。不要看講義，就看你剛剛學的 (price*stock).sum() 夠不夠用。三分鐘後我們對答案。」

---

## S21 · PRACTICE-PROMPT — 🔴 雙 11 折扣挑戰

- 🖼️ 畫面：白底 / 情境敘述 / shape 提示
- 📣 畫面上的字：
  - 標題：「挑戰題 · 10 分鐘 · Broadcasting 實戰」
  - 情境：3C/服飾/食品 三品類各自折扣 `discounts = [0.9, 0.8, 0.95]`（shape (3,)），商品價格矩陣 `prices` shape (3, 5) 每品類 5 個商品
  - 任務：一行算出折後價矩陣（shape 應為 (3,5)）
  - 提示：哪個要 reshape 成 (3,1)？
- 🎙️ 講者這時說：「這題測的是 broadcasting——discounts 要 reshape 成 (3,1) 才能跟 prices (3,5) 對齊。十分鐘，卡住的可以跟旁邊討論。」

---

## S22 · PYRAMID — 三層 takeaway

- 🖼️ 畫面：四層金字塔 / 左右 cross-cut（What / Why）+ 底部 inverted thesis box
- 📣 畫面上的字：
  - 最頂：思維（向量化：整塊運算一次離開 Python）
  - 第二：語言（broadcasting：從右對齊 + 維度為 1 擴展）
  - 第三：地基（ndarray：連續記憶體 + shape/dtype/ndim）
  - 底：「會了這三層，Pandas 只是加了欄名的 ndarray」
- 🎙️ 講者這時說：「三層把今天收掉：最底下是 ndarray 這塊積木；中間 broadcasting 是語言；最上面是向量化思維。三層會了，下節課 Pandas 你會發現它就長在這塊地基上。」

---

## S23 · SILENT — 銜接下一節

- 🖼️ 畫面：全綠底 / 白色 HERO 大字
- 📣 畫面上的字：「學會 NumPy，Pandas 只是加了欄名的 ndarray。」
- 🎙️ 講者這時說：「下一節 S2 Pandas I/O，你會發現 DataFrame 的底層就是 ndarray，groupby / merge 其實都是 shape 運算。今天的 shape 直覺是明天的地基。下課十分鐘。」

---

**節奏檢查**：
- 動機（S1-3） → 概念（S4-5） → 檢核（S6） → 機制（S7） → 例子（S9） → 陷阱（S8,10） → 概念（S11） → 檢核/實測（S12） → 機制（S13） → 陷阱（S14） → 例子（S15-16） → 陷阱（S17） → 檢核（S18） → 陷阱（S19） → 練習（S20-21） → 收束（S22-23）
- 5 個 PITFALL 頁（S8 P2 / S10 P3 / S14 P4 / S17 P1 / S19 P5）全數對應 teacher_notes §4
- 3 個 CHECKPOINT（S6 / S12 / S18）落在 5/12/18 位置，符合 T10「每 5 張插一張」
