# M3 逐頁批註：NumPy 與 pandas

> **文件定位**：內部技術審閱用。針對 `M3_NumPy與pandas.md` 逐投影片進行三層批註：宏觀（定位與論述價值）、細部（技術細節精確性）、reviewer 提問（留給講師補強的空白）。語氣為 code review 式，不客氣但就事論事。
> **審閱日期**：2026-04-14
> **審閱對象**：M3 主線 14 張投影片 + 3 個練習 + 2 張里程碑卡
> **引用慣例**：A1–A7 為 NumPy 側、B1–B7 為 pandas 側

---

## A1 — 你以為在學工具，其實在學模型的底層語言

- 🎯 **宏觀**：作為模組開場，先把 NumPy 定位為「ML 的語言」而非「加速器」，方向正確。這頁的野心不是教語法，是建立心理模型，值得保留。
- 🔬 **細部**：
  - 「tensor 的概念與操作幾乎直接繼承自 NumPy」措辭略軟。精確說法：PyTorch tensor API 與 NumPy 陣列 API 高度同構（broadcasting 規則、indexing 語意一致），但 autograd、device 語意是 tensor 獨有。建議補一句避免學生以為「tensor = NumPy」。
  - `y = Xw + b`：b 在實作上是 scalar 或 `(n,)` 向量，依靠 broadcasting 加到 `Xw` 上，這裡其實已經用到 A4 的概念，可預告。
- ⚠️ **reviewer 提問**：
  1. 為何不在這一頁就揭示「向量化 → SIMD → BLAS」的因果鏈？留到 A5 才講，前三頁缺了為什麼快的物理解釋。
  2. 「快只是副作用」這句漂亮但容易誤導，向量化帶來的「快」其實是對的語言選擇的必然結果，不是副作用。建議改措辭。

---

## A2 — ndarray：為科學計算設計的資料結構

- 🎯 **宏觀**：用「同質 vs 異質」切入 list/ndarray 差異是標準教法，但這頁對**記憶體佈局**的交代太淺，沒有 stride、view、copy 等關鍵詞，後面 reshape/transpose 就無法深入。
- 🔬 **細部**：
  - 「ndarray 讓所有元素緊密排列在連續記憶體」此描述在 C-contiguous 情況下成立，但 transposed view 不是連續的，`arr.T` 回傳的是 stride 不同的 view。這一點如果不提，學生之後會在 `arr.T.reshape(...)` 遇到 `cannot reshape, non-contiguous` 錯誤時當作 bug。
  - 「記憶體約是 list 的 1/8」，對 int64 成立（Python int 物件頭 + 值 ≈ 28 bytes vs NumPy 8 bytes），應明確前提。
- ⚠️ **reviewer 提問**：
  1. 沒有提 `ndarray.strides`、`ndarray.flags['C_CONTIGUOUS']`，後續 broadcasting 與 reshape 的「view vs copy」會懸空。建議至少在講者筆記補一段。
  2. 是否準備好回答「`arr.view()` 和 `arr.copy()` 的差別、以及 slice 預設是哪一個」？這是面試高頻題，學生會問。
  3. `np.array([1, "hello"])` 會發生什麼？（答：dtype 變 `<U`，整個陣列被轉字串）這個 demo 比純講「同質性」強 10 倍，為何沒放？

---

## A3 — shape / axis / dtype：三個你必須看懂的概念

- 🎯 **宏觀**：三件事合講合理，但份量不對稱——shape 和 axis 可以合成一組概念，dtype 值得獨立一頁處理記憶體與精度權衡。
- 🔬 **細部**：
  - 「axis 是你要壓縮掉的那個維度」這個記憶法很好，但只對 reduction 類操作成立（sum、mean、max）。對 concat、stack、cumsum 這類操作，axis 是「沿著哪個方向走」，語意不同。建議補上「reduction 類 vs along 類」兩種 axis 語意。
  - dtype 部分漏掉：（1）`np.float16` 在 CV/DL 量化的角色；（2）`bfloat16` 與 `float16` 差異（指數位 vs 尾數位）；（3）`object` dtype 是陷阱——它是 Python 物件指標陣列，效能退化到 list 等級。
- ⚠️ **reviewer 提問**：
  1. `(100, 28, 28)` vs `(100, 28, 28, 1)` 的差別在 CNN 裡致命，為何不舉這個例子？
  2. `arr.reshape(-1, 4)` 的 -1 是什麼語意？為何是「資料沒動，只是視角換了」？能用 strides 解釋嗎？
  3. dtype promotion（`int32 + float32 → float64`）這個坑值得三行字，現在完全沒提。

---

## A4 — Broadcasting：讓資料自己跑起來

- 🎯 **宏觀**：這是 NumPy 最核心的 mental model，現在的三條規則描述**不夠完整**，而且順序會讓學生誤會。建議改用官方的四步驟版本。
- 🔬 **細部**：
  - 標準 broadcasting 規則（NumPy 官方）應該是：
    1. 若兩陣列 ndim 不同，在較少維的陣列 shape 前補 1。
    2. 從右往左對齊每一維。
    3. 若某一維兩者相等，或其中之一為 1，則相容。
    4. 若某一維兩者都不為 1 且不等，ValueError。
  - 目前文件只講了第 2、3、4 條，漏掉「自動補 1」那條，會讓學生在 `(3,4) + (4,)` 為何成立時卡住。
  - 「NumPy 實際上不複製記憶體，只是虛擬地廣播」這句很重要但沒深入——可以提 `np.broadcast_to` 回傳的是唯讀 view，stride 裡某一維是 0。這是 broadcasting 零成本的物理解釋。
- ⚠️ **reviewer 提問**：
  1. `a[:, None] + b[None, :]` 這個「外積式 broadcasting」技巧沒提，KNN、pairwise distance 都靠這個。
  2. Broadcasting 會隱性放大記憶體嗎？答案是：通常不會（因為是 view），但運算結果會實體化。這點要講清楚，否則學生會以為 broadcasting 免費到可以無限套。

---

## A5 — 向量化思維：不是快，是對的

- 🎯 **宏觀**：標題的哲學主張我支持，但這頁論據薄弱——只用「哪個更清楚」作為訴求，沒有 SIMD/BLAS 的第一性解釋，學生會當作風格問題。
- 🔬 **細部**：
  - 真正的效能來源：（1）CPU SIMD 指令（AVX2、AVX-512）一次處理 4–16 個 float；（2）連續記憶體帶來的 cache line（64 byte）利用率；（3）BLAS（OpenBLAS/MKL）對矩陣運算的多執行緒最佳化。這三層沒一個提到。
  - 「反例：遞歸依賴」這段好，值得擴充。Kalman filter、ARIMA 的狀態更新就是典型案例。
  - `np.apply_along_axis` 內部其實是 Python for 迴圈，效能與手寫迴圈接近。文件已經提醒「謹慎」但沒說為什麼，應明說。
- ⚠️ **reviewer 提問**：
  1. 「效能差距 100 倍」的數字來源？哪種 CPU、哪種陣列大小、是否暖機？內部分享可以不嚴謹，但至少標示是 ballpark。
  2. Numba、Cython、`@np.vectorize` 的角色應在這頁一併討論——`np.vectorize` 是 syntactic sugar，不是真正向量化，這是高頻誤解。

---

## A6 — NumPy 在 ML/DL 的實際角色

- 🎯 **宏觀**：實用頁，串起 pandas/NumPy/PyTorch 的資料流，方向對。
- 🔬 **細部**：
  - `torch.from_numpy` zero-copy 成立的前提：dtype 相容、CPU tensor、記憶體連續。轉到 GPU 時會 copy。這是現場 debug 高頻點。
  - scikit-learn 從 1.2 起部分 API 接受 pandas DataFrame 並保留欄名（`set_output(transform='pandas')`），這段沒提。
- ⚠️ **reviewer 提問**：
  1. `df.values` 與 `df.to_numpy()` 的差別？（答：`.values` 對 ExtensionArray 行為不一致，官方建議用 `.to_numpy()`。）
  2. 在 Arrow backend 的 DataFrame 上呼叫 `.to_numpy()` 會發生什麼（可能觸發 copy + dtype downgrade）？這與 B6 直接相關。

---

## A7 — 里程碑：NumPy 2.0

- 🎯 **宏觀**：版本意識很好。但把 NumPy 2.0 當獨立投影片，份量稍重，可以併到 A6 尾或作為 bridge 頁。
- 🔬 **細部**：
  - NumPy 2.0 的實際 breaking changes 還包括：（1）`np.ptp`、`np.round` 等 API 行為修正；（2）預設 integer 在 Windows 從 int32 → int64（終於跟 Linux 一致）；（3）`np.in1d` → `np.isin`。
  - StringDType 的效能提升不只是「快」，而是**記憶體模型變了**——variable-length string 用 Arrow 式儲存而非 object dtype。這點值得多講一句。
- ⚠️ **reviewer 提問**：
  1. NumPy 2.0 的 ABI break 對下游（SciPy、scikit-learn、PyTorch）的相容性影響？目前生態狀態如何？
  2. 是否要提 Array API standard（https://data-apis.org/array-api/）？這是 NumPy / PyTorch / JAX / CuPy 的共同介面標準，學生日後會撞到。

---

## B1 — DataFrame：分析世界的工作台

- 🎯 **宏觀**：「帶標籤的矩陣」這個定義精準，保留。但「每欄獨立 dtype」的實作背景（BlockManager vs ArrayManager vs Arrow）值得一句背景交代。
- 🔬 **細部**：
  - pandas 內部在 2.0 之前預設使用 BlockManager——把相同 dtype 的欄位合併成一個 2D block。這個設計導致 `df['new_col'] = ...` 常常觸發 block consolidation，是效能熱點。2.0 的 CoW + Arrow backend 繞過了這個問題。
  - Index 的角色：不只是「身份證」，它是 pandas 的 join key、alignment key。`s1 + s2` 會自動按 index 對齊，這是 pandas 與 NumPy 最大的語意差異，值得獨立講。
- ⚠️ **reviewer 提問**：
  1. MultiIndex 是否在本模組範圍內？目前完全沒提，但實務上 `groupby(['a','b'])` 的結果就是 MultiIndex。
  2. `df.columns` 本身也是 Index 物件，這個「Index 不只是列索引」的觀念要不要建立？

---

## B2 — 讀進來、看一眼、查型別

- 🎯 **宏觀**：五步驟偵察流程是良好的肌肉記憶，沒問題。
- 🔬 **細部**：
  - `df.info(memory_usage='deep')` 才會給真正的 object dtype 記憶體用量，預設的 memory_usage 對 object 欄位是低估的。
  - 型別推斷陷阱漏掉一個致命的：`pd.read_csv` 對 ID 欄（如 `'007'`）會推成 int 而去掉前導零。需要用 `dtype={'id': str}` 強制。
- ⚠️ **reviewer 提問**：
  1. 為何不推薦 `dtype_backend='pyarrow'` 作為 2026 年的預設？目前講 Arrow backend 放在 B6，但 B2 的讀檔第一步就可以啟用，時序不對。
  2. `pd.read_csv` 的 `parse_dates`、`na_values`、`thousands` 三個參數是處理「NT$1,200」「2023-01-15」的正解，文件在 B2 只講「陷阱」沒講「解法」。

---

## B3 — 篩選、排序、聚合、轉換

- 🎯 **宏觀**：標題說四件事，但主張句「掌握四個操作就能解決 80%」過於樂觀。實際上 merge/join、pivot/melt 才是高頻痛點。
- 🔬 **細部**：
  - Boolean indexing + 鏈式賦值的陷阱（B6 才提）在這一頁就會踩到：`df[df['age']>30]['salary'] = 0` 是典型錯誤，應在 B3 就預告、B6 解釋。
  - `df.query('age > 30 and city == "Taipei"')` 的語法學生容易搞混（query 裡是 `and`、外面是 `&`），可放「常見坑」欄位。
  - Method chaining 提了但沒示範 `.pipe()` — 這是傳遞自定義函式的慣用法。
- ⚠️ **reviewer 提問**：
  1. `.loc[]` vs `.iloc[]` vs 直接 `[]` 的三層語意差異，現場一定會被問。
  2. `.assign()` 方法鏈 vs `df['x'] = ...` 賦值的差別？前者是 functional、後者是 mutating，與 CoW 哲學一致。

---

## B4 — groupby 不是語法，是業務切片的思維工具

- 🎯 **宏觀**：split-apply-combine 是 Wickham 2011 年的經典論文（R 的 plyr 套件），值得一句 credit。
- 🔬 **細部**：
  - `transform` vs `agg` vs `apply` 的三者差異：
    - `agg`：每組 → 一個值（降維）
    - `transform`：每組 → 同長度結果（保持形狀）
    - `apply`：最通用，但最慢、回傳形狀不保證
  - `groupby(sort=False)` 可以省下一次排序成本，大資料時是顯著效能優化。
  - `observed=True`（對 Categorical groupby）避免產生所有 cross product，pandas 2.2 起預設會改，要提版本意識。
- ⚠️ **reviewer 提問**：
  1. groupby 的結果 index 問題（為何要 `.reset_index()`）與 as_index 參數沒有深入講。
  2. 與 SQL 的等價對照沒做——`SELECT dept, AVG(salary) FROM emp GROUP BY dept` ↔ `df.groupby('dept')['salary'].mean()`，這個橋樑對 BI 背景學生是金鑰。
  3. window function（`rolling`、`expanding`、`groupby().rolling()`）是 groupby 的進階，是否本模組範圍？

---

## B5 — 缺失值與離群值

- 🎯 **宏觀**：四種缺失值處理策略清晰，方向正確。但缺失機制的理論基礎（MCAR / MAR / MNAR）一字沒提，對統計背景的學生是缺口。
- 🔬 **細部**：
  - MCAR（完全隨機缺失）、MAR（隨機但可由其他欄位預測）、MNAR（缺失本身帶資訊）是統計學處理缺失值的分類，決定了可用的填補策略。四種處理策略應該對應這三種機制。
  - IQR 1.5 倍是 Tukey 經驗法則，不是理論最優。Z-score > 3 預設資料常態分布——若資料是長尾（如收入），這兩個方法都會誤殺。建議補 MAD（Median Absolute Deviation）或 Isolation Forest。
  - `pd.NA` 與 `np.nan` 的差異、傳播語意（`pd.NA | True` vs `np.nan | True`）沒提。Arrow backend 下會頻繁遇到 `pd.NA`。
- ⚠️ **reviewer 提問**：
  1. 缺失值填補會影響下游模型的變異數估計，這個統計學後果要不要講？
  2. `scikit-learn` 的 `SimpleImputer`、`IterativeImputer` 是 pandas 之外的替代方案，為何不提？

---

## B6 — pandas 2.0：Arrow backend、Copy-on-Write

- 🎯 **宏觀**：這頁是整個 Part B 的精華，但目前只是「介紹」等級，沒有 CoW 的觸發規則說明，學生遇到實際情境還是會踩坑。
- 🔬 **細部**：
  - CoW 的核心規則：**所有 DataFrame 操作回傳的物件在寫入時會 copy，讀取共享底層 array**。這意味著：
    - `df2 = df.loc[...]`；`df2.iloc[0, 0] = 5` 不會影響 df（正確語意）
    - `df[df['a']>0]['b'] = 5` 仍然無效，但不再是未定義行為，而是明確的「對中間物件寫入，丟棄」
  - Arrow backend 的代價：某些 API 尚未完全支援（如 `.values` 行為、`applymap`），遷移時要測試。
  - SettingWithCopyWarning 的根因就是 BlockManager + view/copy 語意不明——CoW 消滅了這個警告的必要。但 pandas 2.x 下某些操作仍會觸發，因為 CoW 還不是預設（需要 `pd.options.mode.copy_on_write = True`，預計 3.0 預設）。
- ⚠️ **reviewer 提問**：
  1. `pd.options.mode.copy_on_write = True` 在 2.x 是可選的，3.0 預設開啟。這個時序講清楚了嗎？
  2. Arrow backend 對 `object` dtype 的影響——字串會自動轉成 `string[pyarrow]`，效能與記憶體都大幅改善，但某些正則 API 可能退化。需要實測。
  3. CoW 對「修改 df 本身」的程式碼是否破壞性？答：不是，`df['a'] = ...` 仍然 in-place 修改 df。CoW 只影響**衍生物件**的語意。這是常見誤解。

---

## B7 — 工具規模感：pandas / Polars / DuckDB / Spark

- 🎯 **宏觀**：工具地圖做得好，但 2026 年的事實需要更新——Polars 已經不只是「比 pandas 快」，而是有獨立的 API 哲學（expression-based、lazy frame）。
- 🔬 **細部**：
  - Polars 與 pandas 的差別不只在效能：
    - 沒有 index
    - expression API（`pl.col('a').mean()`）取代 method call
    - 原生 lazy evaluation（`lf.collect()`）
    - 查詢最佳化器（predicate pushdown、projection pushdown）
  - DuckDB 的殺手鐧：可以直接 `SELECT * FROM 'file.parquet'`，不用 ingest。Zero-ETL 場景的最佳工具。
  - Modin、Dask 兩個「盡量兼容 pandas API」的替代品沒提。Modin 特別值得一句——幾乎 drop-in。
  - 選擇框架的「資料大小」門檻過時，現代筆電 64GB RAM 是常態，pandas 實務上可處理到 10–20GB。
- ⚠️ **reviewer 提問**：
  1. 為何只推 Polars/DuckDB，不提 Modin/Dask？選擇準則是什麼？
  2. 與 SQL 的等價性是這頁漏掉的主線——pandas/Polars/DuckDB 之間的共通語意是關聯代數（relational algebra），用這個視角講能讓學生看透三個工具的一致性。
  3. 「pandas 是預設選擇」在 2026 年仍然成立嗎？Polars 在新專案的採用率？

---

## 練習 A — NumPy 數值計算

- 🎯 **宏觀**：任務設計合理，但少了「broadcasting 的錯誤情境」的 negative test。
- ⚠️ **reviewer 提問**：
  1. 標準化用 `axis=0` 為何是對的？如果用 `axis=1` 會發生什麼（每個樣本被標準化，變成 per-sample normalization，完全不同的語意）？這個對比應該納入驗收。
  2. `X.T @ X` 的 shape 是 `(4, 4)`，但文件沒明確要求學生回答「為何不是 `(5, 5)`」。這是 shape-of-product 的核心檢驗。

---

## 練習 B — pandas 資料操作

- 🎯 **宏觀**：涵蓋篩選、groupby、分箱三大核心，範圍得當。
- ⚠️ **reviewer 提問**：
  1. `pd.cut` 與 `np.select` 的選擇依據是什麼？`pd.cut` 回傳 Categorical（有序），`np.select` 回傳 object/numeric，下游行為差很多。
  2. 是否要求學生用 method chaining 寫一次，對照賦值式寫一次？這是風格訓練的好機會。

---

## 練習 C — Mini EDA 工作坊

- 🎯 **宏觀**：設計細膩，從偵察到清理到答題，是 M3 最有價值的練習。
- ⚠️ **reviewer 提問**：
  1. `performance_score == 99` 的「錯誤碼填入」是真實世界的經典（SPSS、SAS 時代的遺產），是否要講這個歷史背景？
  2. 「年資從 hire_date 算到 2026 年」要注意 datetime 的 timezone 問題——`pd.Timestamp('2026-04-14')` vs `pd.Timestamp.now(tz='Asia/Taipei')` 會有微妙差異。
  3. 清理後要不要用 `df.to_parquet()` 存檔？這是 2026 年的實務標準，比 CSV 強太多（型別保留、壓縮）。

---

## 里程碑卡 A / B

- 🎯 **宏觀**：敘事強，適合作為記憶錨點。
- ⚠️ **reviewer 提問**：
  1. NumPy 2.0 卡片沒提 ABI break 對整個科學計算生態的遷移成本，這是故事的另一半。
  2. pandas 2.0 卡片稱 CoW 是「修正設計錯誤」語氣偏重，社群中仍有人認為原設計是 trade-off 而非錯誤。措辭可斟酌。

---

## 整體架構級 reviewer 提問（跨投影片）

1. **view / copy / stride 三件套**從未作為獨立主題出現，是 NumPy 側最大的知識空白。建議在 A2 或 A3 加一個子頁專門講。
2. **SQL 等價性**貫穿 pandas 所有操作（filter=WHERE、groupby=GROUP BY、merge=JOIN、pivot=CASE WHEN），但文件完全沒建立這個橋樑。對 BI/資料庫背景的學生，這是最高 ROI 的類比。
3. **Polars/DuckDB 的 API 哲學**與 pandas 有實質差異（expression、lazy、無 index），只在 B7 提一筆太輕。如果要建立「工具規模感」，應該做一張對照表。
4. **SettingWithCopyWarning** 在 B3 就會撞到、B6 才解釋，中間 20 分鐘學生會在現場炸鍋。建議在 B3 預告、B5 demo、B6 總結。
5. **效能實測**一個都沒有。對「向量化快 100 倍」、「Arrow backend 減 30–50% 記憶體」這類宣告，內部技術會議應附 benchmark 腳本（即使是 ballpark）。
6. **記憶體佈局視覺化**（row-major / column-major / BlockManager / Arrow columnar）是整個模組最需要但最缺的圖。04 文件會補。
