# M3 三鏡頭分析：First Principles / Fundamentals / BoK

> **文件定位**：以三種審視鏡頭重新解構 M3，對應內部架構討論的三種語彙層次——物理層（第一性原理）、工程層（肌肉記憶 checklist）、學科層（知識體系對齊）。最後給出三鏡合流建議，作為講師教學決策的準則。
> **適用對象**：課程負責人、資深講師、課程架構師
> **配套文件**：01_on_page_annotation.md、03_bcg_narrative.md

---

## Lens 1：First Principles — 為什麼 NumPy/pandas 長這樣

回到物理與硬體，不看 API、不看生態，只問「為什麼必須是這樣」。

### 1.1 向量化的本質：批次 SIMD 與 cache 命中

**物理事實**：
- 現代 CPU 一個核心有多條 SIMD 管線（AVX2 = 256-bit、AVX-512 = 512-bit），一個指令可同時處理 4–16 個 float32。
- L1 cache 一次搬 64 byte（一個 cache line）。若資料連續擺放（C-contiguous），一次讀入 8 個 float64；若散落（Python list 的物件指標陣列），每個元素都要解引用，cache miss 率飆升。
- 主記憶體到 CPU 的延遲大約是 L1 cache 的 100 倍。

**推論**：
1. **同質 dtype 是必要條件**：異質容器無法利用 SIMD，因為每次運算都要先型別檢查。
2. **連續記憶體是必要條件**：stride 不均勻時 SIMD 無法啟用、cache 利用率崩潰。
3. **批次操作是必要條件**：把「每元素都要解釋一次」的成本攤平到一次配置上。

**結論**：NumPy 的設計不是為了「好用」，是為了讓 Python 能觸碰到 CPU 的真實性能。ndarray = 連續同質記憶體 + dtype 標記 + shape 與 strides 視圖。這四件事缺一不可。

### 1.2 BLAS / LAPACK：你從未直接呼叫的最底層

**物理事實**：
- `np.dot`、`np.matmul`、`@` 底層呼叫 BLAS（Basic Linear Algebra Subprograms）Level 3 routine（GEMM）。
- 實作通常是 OpenBLAS、Intel MKL、Apple Accelerate。這些函式庫為特定 CPU 微架構手工調校（block size、prefetching、register tiling）。
- 一個 $1000 \times 1000$ 矩陣乘法，naive triple-loop 在 Python 裡要 30 秒，用 BLAS 只要 5 ms。差距 6000 倍。

**推論**：
- NumPy 不是「用 C 重寫 Python」而已，是「Python 綁定了過去 50 年的線性代數工程累積」。
- 深度學習框架的 tensor 運算最終也是呼叫 cuBLAS（GPU 版 BLAS）。NumPy 是這條產業鏈的 onboarding 層。

### 1.3 Broadcasting 的零成本：view + stride 0

**物理事實**：
- `np.broadcast_to(a, (3, 4))` 不複製記憶體，而是回傳一個 strides 裡某一維為 0 的 view。
- stride = 0 的意思是「無論這個 index 變多少，實際讀取的記憶體位址不變」。
- 讀 10 次相同位址，CPU cache 命中率 100%。

**推論**：
- Broadcasting 不是「聰明地省記憶體」的 feature，是 stride 資料結構**天生能做到**的事。
- 這也解釋了為什麼 broadcasting 有嚴格規則——規則其實是「stride 能否正確偽裝成想要的 shape」的條件。

### 1.4 pandas 的 Index：為什麼不是 NumPy 就好

**物理事實**：
- NumPy 是 positional（按位置），pandas 是 labeled（按標籤）。
- `s1 + s2` 在 pandas 會自動對齊 index——若 s1 的 index 是 `[a, b, c]`、s2 是 `[b, c, d]`，結果 index 是 `[a, b, c, d]`，不在交集的位置填 NaN。
- 這個語意來源於**關聯代數**：資料的身份由 key 決定，不由位置決定。

**推論**：
- pandas 的 Index 不是「附加功能」，是**資料身份（identity）的表示**。MultiIndex 則是複合主鍵。
- merge / join 的正確性依賴 Index 的語意，而不是行號。

### 1.5 Copy-on-Write 的本質：reference-counted view 的寫入安全

**物理事實**：
- CoW 的實作：所有衍生 DataFrame 共享底層 array。寫入時檢查 refcount，>1 就 clone。
- 這與 PyTorch 的 `.clone()` vs `.detach()` 哲學一致。與 Rust 的 `Cow<T>` 概念同源。
- pandas 1.x 的歧義源於 BlockManager 有時 return view、有時 return copy，取決於運算是否跨越 block。

**推論**：
- CoW 不是「新 feature」，是把「view/copy 的二選一」從 user 移到 runtime。user 不再需要知道底層是哪種，runtime 保證語意。
- 這是**語意正確性優先於效能**的工程決策。

---

## Lens 2：Fundamentals — NumPy 10 招 + pandas 10 招 checklist

不是把所有 API 都學一次，而是把「你必須在盲打等級熟練」的操作列出來。熟練標準：閉眼寫出語法、說得出 shape/dtype 結果、知道一個替代寫法。

### 2.1 NumPy 10 招

| # | 招式 | 關鍵 API | 盲打檢驗 |
|---|------|----------|----------|
| 1 | 建立陣列 | `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`, `np.random.default_rng()` | 能從 `(3,4,5)` shape 產生對應的全零陣列 |
| 2 | 形狀操作 | `reshape`, `.T`, `ravel`, `flatten`, `np.expand_dims`, `np.squeeze` | 知道 `reshape` 是 view、`flatten` 是 copy |
| 3 | 索引切片 | basic slicing、fancy indexing、boolean mask | 知道 fancy indexing 永遠 copy，slice 是 view |
| 4 | Broadcasting | shape 對齊、`None`/`np.newaxis`、`np.broadcast_to` | 能徒手算 `(3,1,5) * (4,5)` 的結果 shape |
| 5 | reduction | `sum`, `mean`, `std`, `min/max`, `argmin/argmax`，都帶 `axis=` | 知道 `axis` 是「壓縮掉的維度」 |
| 6 | 線性代數 | `@`, `np.dot`, `np.linalg.solve`, `np.linalg.inv`, `np.linalg.eig`, `np.linalg.svd` | 知道 `X.T @ X` 是 Gram matrix |
| 7 | 條件邏輯 | `np.where`, `np.select`, `np.clip`, `np.isnan`, `np.isfinite` | 能用 `np.where` 寫 ReLU |
| 8 | 隨機 | `rng = np.random.default_rng(seed)`, `rng.normal/uniform/choice` | 知道 legacy `np.random.seed` 是 global state（勿用） |
| 9 | 合併分割 | `concatenate`, `stack`, `vstack`/`hstack`, `split` | 知道 `stack` 增加一維、`concatenate` 不加 |
| 10 | dtype 與記憶體 | `dtype`, `astype`, `.itemsize`, `.nbytes`, `.flags['C_CONTIGUOUS']` | 能徒手算 `(1000, 1000) float32` 佔 4MB |

### 2.2 pandas 10 招

| # | 招式 | 關鍵 API | 盲打檢驗 |
|---|------|----------|----------|
| 1 | 讀檔偵察 | `read_csv`（帶 `dtype`, `parse_dates`, `na_values`）, `.head`, `.info`, `.describe`, `.dtypes` | 能從 `info()` 一眼看出型別與缺失 |
| 2 | 選取 | `[]`, `.loc[]`, `.iloc[]`, `.at[]`, `.query()` | 知道三者的索引語意差異 |
| 3 | 布林篩選 | `df[cond]`, 多條件 `&` / `|`，括號包住 | 不用 `and`/`or` |
| 4 | 排序與 rank | `sort_values`, `sort_index`, `rank` | 知道 `sort_values` 非 in-place |
| 5 | groupby | `groupby().agg/transform/apply`, `as_index=False`, `observed=True` | 能說出 agg vs transform 的差異 |
| 6 | 缺失值 | `isna`, `dropna`, `fillna`, `ffill`, `bfill`, `interpolate` | 知道 `pd.NA` vs `np.nan` |
| 7 | 合併 | `merge` (`how`, `on`, `left_on/right_on`, `validate`), `concat`, `join` | 能說出 inner/left/outer/right 的語意 |
| 8 | 重塑 | `pivot_table`, `melt`, `stack`, `unstack`, `wide_to_long` | 知道 pivot vs pivot_table 的差異（重複值處理） |
| 9 | 時間序列 | `pd.to_datetime`, `dt` accessor, `resample`, `rolling`, `shift` | 能做「近 7 天平均」 |
| 10 | 型別與後端 | `astype`, `convert_dtypes`, `dtype_backend='pyarrow'`, `pd.options.mode.copy_on_write` | 知道何時切 Arrow backend |

### 2.3 20 招的共通心法

- 每一招都有「shape / dtype / index 會怎麼變」的三問。做完操作，腦中能重現結果。
- 90% 的 bug 來自不知道自己在操作 view 還是 copy、index 對齊還是位置對齊。
- 每一招都有「if it's slow, what's the escalation path」——是 dtype 太貴？是觸發 copy？是 groupby-apply 走了 Python 路徑？

---

## Lens 3：BoK — 對齊 Data Science 知識體系

用學科地圖檢視 M3 的覆蓋，找出缺口與重疊。參考 EDISON、ACM Data Science Task Force 2021、以及 DAMA DMBoK。

### 3.1 Data Wrangling（資料整備）

BoK 定義：從原始資料到可分析資料的整個路徑，涵蓋收集、清理、轉換、整合、品質保證。

| BoK 子領域 | M3 覆蓋 | 缺口 |
|------------|---------|------|
| 資料讀取 | B2（read_csv） | Parquet、JSON、資料庫連線未提 |
| 型別修正 | B2、練習 C | `convert_dtypes()` 自動化未提 |
| 缺失值處理 | B5（四種策略） | MCAR/MAR/MNAR 機制未提 |
| 離群值處理 | B5（IQR、Z-score） | MAD、Isolation Forest、業務判準未提 |
| 資料整合 | （無） | **merge/join/concat 完全缺席**，這是最大缺口 |
| 重塑 | （無） | **pivot/melt/stack 完全缺席** |
| 品質保證 | 練習 C 隱含 | Great Expectations、pandera 等工具未提 |

**判斷**：M3 覆蓋 Wrangling 約 60%，缺口集中在**多表整合**與**資料品質框架**。merge/melt 的缺席是最嚴重問題——實務上任何分析都從多表 join 開始。

### 3.2 Computational Statistics（計算統計）

BoK 定義：用計算方法執行統計推論，包含描述統計、抽樣、假設檢定、貝氏計算。

| BoK 子領域 | M3 覆蓋 | 缺口 |
|------------|---------|------|
| 描述統計 | A5（向量化）、B2（describe）、B5（summary） | `scipy.stats` 補充未提 |
| 抽樣 | （無） | bootstrap、train_test_split 未提（留給 M5？） |
| 機率分布 | A 側 `np.random` 淺提 | 分布 API 未系統化 |
| 假設檢定 | （無） | 留給 M4 / M5 |
| 向量化統計 | A5 | axis 語意、weighted stats 未提 |

**判斷**：M3 不是 stat 模組，覆蓋薄是合理的。但 `np.random.default_rng` 的新 API（對比 legacy `np.random.seed`）應在 A 側更明確。

### 3.3 Linear Algebra（線性代數）

| BoK 子領域 | M3 覆蓋 |
|------------|---------|
| 向量、矩陣基本操作 | A1–A3 |
| 矩陣乘法 | A6（`@` 運算子） |
| 轉置 | 練習 A |
| 特徵分解、SVD、線性方程求解 | 未提 |

**判斷**：M3 不做線性代數課，但對 `X.T @ X`、`np.linalg.solve` 等 ML 高頻操作應至少列入「10 招」清單，避免學生誤以為 NumPy 只能做基本運算。

### 3.4 Software Engineering for Data（資料工程化）

| BoK 子領域 | M3 覆蓋 | 缺口 |
|------------|---------|------|
| 可重現性 | （無） | seed 固定、環境鎖定未提 |
| 版本意識 | A7、B6 | 很好，保留 |
| 效能意識 | A5 輕提 | profiling 工具（`%timeit`、`line_profiler`）未提 |
| 測試 | （無） | pandera、unittest 未提（留給 M5+） |

**判斷**：作為入門模組這樣的覆蓋可接受，但可重現性（seed）是低成本高價值的補充。

### 3.5 Tool Ecosystem（工具生態）

- B7 的 Polars / DuckDB / Spark 對齊 BoK 的工具地圖維度。
- 缺少 Modin、Dask、Vaex 等「盡量兼容」系的工具。
- 完全沒提 scikit-learn pipeline、Arrow ecosystem（pyarrow, ADBC）。

**判斷**：B7 方向對，深度不足，可以做一張完整的工具象限圖。

---

## 三鏡合流建議

將三鏡頭的發現匯合，給出可執行的教學策略。

### 合流結論 1：把「記憶體佈局」升為一級主題

- First Principles 告訴我們，向量化、broadcasting、CoW 的根源都是記憶體佈局。
- Fundamentals 檢驗發現 view/copy/stride 沒進入 10 招 checklist，會導致學生無法辨識自己的效能 bug。
- BoK 對齊發現，Data Wrangling 的品質控制也依賴對記憶體語意的掌握。

**建議**：在 A2 和 A3 之間插入一張「記憶體佈局專頁」，或至少在 A2 擴充 200 字，強制帶到 stride / view / copy / contiguity。

### 合流結論 2：把「SQL 等價性」做成 pandas 的副線

- First Principles 告訴我們 pandas 本質是關聯代數的 Python 綁定。
- Fundamentals 的 groupby、merge、pivot 與 SQL 的 GROUP BY、JOIN、PIVOT 一一對應。
- BoK 對齊發現 Computational Statistics 與 BI 的橋樑就是 SQL 語意。

**建議**：在 B3、B4、B7 三處各放一小塊 SQL 對照表。Closing 時用一頁總結：「你學會的 pandas 操作，都是 SQL 能做的事。反之亦然。」

### 合流結論 3：merge/pivot 的缺席必須補上

- Fundamentals 20 招裡 pandas 的 7、8 條（merge、pivot）沒有對應投影片。
- BoK 對齊顯示這是 Data Wrangling 最大缺口。
- 實務上，任何真實分析第一步就是 merge。

**建議**：新增一張 B3.5「多表合併：pandas 的 JOIN」，放 merge 四種 how + validate + indicator。pivot/melt 可放在練習 B 擴展或作為額外補充。

### 合流結論 4：效能實測要進教案

- First Principles 講了物理原因，但沒有數字支撐會讓學生當作信仰。
- Fundamentals 的 10 招每一招都有「效能熱點」可實測。

**建議**：準備一個 `M3_benchmark.ipynb` 補充材料，用 `%timeit` 跑 5 組對照：
1. Python loop vs NumPy vectorized（dot product, $n=10^6$）
2. `apply_along_axis` vs vectorized
3. `df.iterrows` vs vectorized column op
4. Object dtype string vs Arrow string
5. BlockManager vs Arrow backend 的 memory footprint

### 合流結論 5：工具規模感升級為「資料工程成熟度」

- BoK 的工具生態維度比 M3 目前的「小中大」更多元（streaming、lakehouse、catalog 等）。
- 但 M3 是入門，不需要全講，可以預告 M7 會回來談。

**建議**：B7 保留現有內容，在結尾多一行「工具規模感的完整地圖在 M7」的指向。

---

## 附：三鏡頭檢驗表（給講師備課用）

| 問題 | 如果答不出 | 就該回到 |
|------|-----------|----------|
| 為什麼 ndarray 比 list 快？ | 背了結論沒理解 | Lens 1：連續記憶體 + SIMD + cache |
| 為什麼 `arr.T` 不會複製記憶體？ | 不懂 view | Lens 1：stride 視圖 |
| 什麼時候該用 `transform`、什麼時候該用 `agg`？ | 混用兩者 | Lens 2：招式 5 |
| pandas 和 SQL 怎麼對應？ | 各學一套 | Lens 3：Data Wrangling |
| 為什麼 Polars 比 pandas 快？ | 只會說「用 Rust」 | Lens 1 + 3：expression + lazy + Arrow |
| CoW 會影響我的哪些程式碼？ | 含糊帶過 | Lens 1：reference-counted view |
