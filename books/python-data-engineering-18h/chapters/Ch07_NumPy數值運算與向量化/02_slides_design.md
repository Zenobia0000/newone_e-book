# Ch07 · 02_slides_design — SOP §4.2

- 章節：NumPy 數值運算與向量化（M3 · 2.0 hr · 19 張內容）
- Governing thought：NumPy 不是讓你算快一點，而是讓你用 shape × broadcasting 的語言描述計算問題。
- 配色：黑 + 灰 + 深綠（#1B5E3F）
- 每張格式：🖼️（視覺規格）/ 📣（文字骨架）/ 🎙️（口頭引導）

---

## S1 · SILENT — 思維換檔的第一口氣
- 🖼️ 深綠滿版，白字 hero。
- 📣 「別再寫 for 算數字。\n換一種語言想這件事。」
- 🎙️ Ch02–Ch06 我們都是「一個一個處理」。今天開始進入資料工程層，第一件事就是把大腦從迴圈思維切換到向量化思維。

## S2 · ASK — 效能落差的震撼教育
- 🖼️ 白底大哉問 + 右下 data card。
- 📣 Q：「同樣加總一億個數字，list vs ndarray 差多少？」
  Data card：label「1e8 筆 float64 加總實測」· stat「80×」· caption「Python list comprehension vs np.sum 的平均時間比」
- 🎙️ 差距不是 2 倍、不是 10 倍，是 80 倍。這不是優化，是換了一種計算方式。為什麼？接下來三十分鐘會講清楚。

## S3 · MATRIX 2×3 — 為什麼 list 不夠用
- 🖼️ 2×3 方陣，左欄 list 的問題、右欄 ndarray 的對應解決方案。
- 📣 標題「為什麼 list 不夠用：ndarray 的六個差別」
  cells（row-major）：
  - `list 混型別`（highlight）— 一個 list 可裝 int / str / obj，每格都是 PyObject
  - `ndarray 統一 dtype` — 整塊相同型別，`float64` 就是 `float64`
  - `list 記憶體散落` — pointer 四散於 heap，CPU 無法預測
  - `ndarray 連續記憶體`（highlight）— 一整條，CPU cache 友善
  - `list 無向量化` — 必須 Python level for loop
  - `ndarray 向量化 + SIMD` — 底層 C，一次處理多筆
- 🎙️ list 是「萬能容器」，ndarray 是「數值專用高速公路」。

## S4 · CODE — shape / dtype / ndim 三件套
- 🖼️ 滿版 code panel，標題 label「描述一個 ndarray，只需三個屬性」
- 📣 code：
  ```python
  import numpy as np
  a = np.array([[1, 2, 3], [4, 5, 6]])
  a.shape    # (2, 3)
  a.dtype    # dtype('int64')
  a.ndim     # 2
  a.size     # 6 總元素數
  ```
  bullets：
  - `shape`：每個維度長度，是 tuple
  - `dtype`：所有元素的統一型別
  - `ndim = len(shape)`
  - 看到 ndarray 先問這三個
- 🎙️ 做資料工程時，99% 的 bug 都先用這三個屬性 print 出來就破案了。

## S5 · IMAGE-CODE — 連續記憶體的物理原因
- 🖼️ 左側圖：Python list（pointer 散落）vs ndarray（連續 block）；右側 code 印 shape/dtype/itemsize/nbytes。
- 📣 image 說明 list pointer 散落 heap、ndarray 是一整條連續 float64 格子；code：
  ```python
  a = np.zeros(1_000_000, dtype=np.float64)
  a.itemsize   # 8 bytes
  a.nbytes     # 8_000_000 = 8 MB
  ```
  bullets：
  - 連續記憶體 → CPU cache 可預讀
  - 單一 dtype → SIMD 一次處理多筆
  - 無 PyObject header → 純數字沒包裝
  - 這就是 Ch1 CPU/RAM 的現實投影
- 🎙️ NumPy 快的根本理由不在「Python 程式碼」，而在「記憶體長什麼樣子」。

## S6 · CODE — 建立 ndarray 的六種常用方式
- 🖼️ 滿版 code panel。
- 📣 code：`np.array` / `np.zeros` / `np.ones` / `np.arange` / `np.linspace` / `np.random.randn`；bullets：哪種情境用哪一個。
- 🎙️ 這六個 API 蓋掉 95% 的建立需求。其他忘了也沒關係。

## S7 · CODE — 多維切片
- 🖼️ 滿版 code panel。
- 📣 code：`arr[行, 列]` / `arr[:, 0]` / `arr[1:3, ::2]` 三種寫法 + 輸出示意；bullets：逗號切割維度、slice 與 list 一致、省略維度補 `:`。
- 🎙️ 從「arr[1][2]」進化到「arr[1, 2]」，不是語法糖，是告訴 NumPy 一次性下手。

## S8 · CODE — 布林索引
- 🖼️ 滿版 code panel。
- 📣 code：`arr[arr > 0]` / `arr[(arr > 0) & (arr < 10)]`；bullets：條件回傳 bool array、`&` `|` `~` 不是 `and`/`or`、輸出一維攤平、最重要的過濾工具。
- 🎙️ 這是資料工程每天用最多次的一招。

## S9 · CODE — Fancy Indexing
- 🖼️ 滿版 code panel。
- 📣 code：`arr[[0, 2, 5]]` / `arr[[0, 1], [1, 2]]` 取指定元素；bullets：整數陣列當索引、可抽不連續、可重排、回傳 copy。
- 🎙️ 當你需要「按某個 id 清單取資料」時，不用 for，一行搞定。

## S10 · VS-CODE — view vs copy 陷阱
- 🖼️ 上下兩個 code panel（BEFORE / AFTER）。
- 📣 上：切片共享記憶體，改 view 改到原 array；下：Fancy Indexing 是 copy，修改不影響原 array。bullets 歸納判斷法則、`.copy()` 的用時機。
- 🎙️ 這是「為什麼我的資料莫名其妙被改了」的頭號嫌犯。

## S11 · ASK — Broadcasting 的大哉問
- 🖼️ 白底大問句 + data card。
- 📣 Q：「兩個形狀不同的 ndarray，為什麼能直接相乘？」data card：label「Broadcasting 規則」stat「3 步」caption「右對齊 → 缺維補 1 → 大小 1 可拉伸」
- 🎙️ Broadcasting 不是 NumPy 的特異功能，是一種讓資料形狀自動對齊的語法。

## S12 · IMAGE-CODE — Broadcasting 三步規則
- 🖼️ 左圖：shape 對齊步驟示意（A (2,1) + B (3,) → (2,3)）；右 code：三步 shape 計算。
- 📣 code：展示 shape 變化；bullets：右對齊、補 1、大小 1 拉伸、不符合會 ValueError。
- 🎙️ 規則只有三步，但能解決 80% 的「我不想寫 for」的場景。

## S13 · CODE — Broadcasting 經典範例
- 🖼️ 滿版 code panel。
- 📣 code：
  ```python
  prices   = np.array([100, 200, 300])        # (3,)
  discount = np.array([[0.9], [0.8]])          # (2, 1)
  (prices * discount)                          # (2, 3)
  ```
  bullets：shape 對齊過程、不需要 reshape、三次促銷方案一行算完。
- 🎙️ 這就是資料工程的真實場景：把一行定價、多個折扣組合一次算出。

## S14 · CODE — z-score 標準化實戰
- 🖼️ 滿版 code panel。
- 📣 code：
  ```python
  X = np.random.randn(100, 5)           # 100 筆 × 5 特徵
  z = (X - X.mean(axis=0)) / X.std(axis=0)
  ```
  bullets：`(100,5) - (5,)` broadcasting 成功、`(100,5) / (5,)` 同理、ML preprocessing 的骨架、Ch8 會換成 sklearn StandardScaler。
- 🎙️ 這行程式碼 90% 的 ML pipeline 裡都有。廠商付錢的 pipeline，底層就是這兩個運算子。

## S15 · VS-CODE — for 迴圈 vs 向量化
- 🖼️ 上下兩個 code panel。
- 📣 上（BEFORE）：Python for 迴圈平方加總 1e7 筆，約 4.2 秒；下（AFTER）：`(a ** 2).sum()`，約 0.05 秒。bullets：80× 差距、原因三件套（C 實作 / SIMD / 無 PyObject 包裝）。
- 🎙️ 這不是優化，是換語言。同樣一件事，NumPy 用「一句話」描述，CPython 就能把它交給底層 C。

## S16 · TABLE — 內建統計函式
- 🖼️ 編輯式表格。
- 📣 標題「NumPy 內建統計函式：一行搞定聚合」
  header：`函式` / `做什麼` / `常用 axis` / `Pandas 對應`
  rows：
  - `mean` / 平均 / `axis=0/1` / `.mean()`
  - `std` / 標準差 / `axis=0/1` / `.std()`
  - `min/max` / 極值 / `axis=0/1` / `.min()/.max()`
  - `argmax/argmin` / 極值座標 / `axis=0/1` / `.idxmax()/.idxmin()`
  - `percentile` / 分位數 / `axis=0/1` / `.quantile()`
  - `cumsum` / 累加 / `axis=0/1` / `.cumsum()`
- 🎙️ 學這六個，就能做完 EDA 階段 80% 的描述統計。

## S17 · IMAGE-CODE — axis 方向圖
- 🖼️ 左圖：3×4 矩陣配 axis=0（上下箭頭穿欄）/ axis=1（左右箭頭穿列）；右 code 示範。
- 📣 code：
  ```python
  arr = np.arange(12).reshape(3, 4)
  arr.mean(axis=0)   # shape (4,)  每欄一個值
  arr.mean(axis=1)   # shape (3,)  每列一個值
  ```
  bullets：axis=k 就是「把第 k 維摺掉」、axis=0 = 沿列 = 每欄聚合、axis=1 = 沿欄 = 每列聚合、記熟輸出 shape 就不會錯。
- 🎙️ axis 是新手最常搞錯的地方。記住一句話：axis=k 就是把第 k 維吃掉。

## S18 · VS-CODE — axis=0 vs axis=1
- 🖼️ 上下兩個 code panel，同一個矩陣、兩種 axis、兩種輸出 shape。
- 📣 上（axis=0）：`arr.mean(axis=0)` → shape (4,)；下（axis=1）：`arr.mean(axis=1)` → shape (3,)。bullets：輸出 shape 是最好的 debug 工具、實務上 axis=0 更常用（每欄的統計量）、搞不清就 print shape。
- 🎙️ 遇到 axis bug 不要硬看資料，先 print shape，半秒鐘破案。

## S19 · PYRAMID — Ch07 收束
- 🖼️ 兩欄階層 + 底部深綠 thesis box。
- 📣 兩欄：
  - 「四件套」：shape / dtype / broadcasting / axis
  - 「三個為什麼快」：連續記憶體 + SIMD + C 實作無 PyObject 包裝
  thesis：「Ch08 Pandas 的 Series/DataFrame 底層就是 ndarray —— 本章的 shape × broadcasting × axis 直接在表格上複用。」
- 🎙️ 今天學的不是一個函式庫，是資料工程的共同語言。Ch08 只是把這個語言套上欄位名稱。
