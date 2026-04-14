# M3 速學卡：Minimum Viable Knowledge

> **文件定位**：濃縮 M3 NumPy 與 pandas 為 14 張速學卡，作為工程師考前抱佛腳、面試前 30 分鐘回顧、或跨團隊快速對齊的最小知識集。每張卡正面是觸發問題（prompt），反面是核心答案（answer），附「延伸挖深」指向本 annotated 資料夾的其他文件。
> **使用方式**：可列印成雙面卡片，或匯入 Anki。語氣為內部 review，技術詞保留英文。
> **完成標準**：14 張全部能在 60 秒內口述重點。

---

## 速學卡 01 — ndarray vs list

**Prompt**：為什麼 ML 用 ndarray 不用 Python list？

**Answer**：
- `list` 是異質容器，每元素是獨立 PyObject，記憶體散落、帶型別標記與 refcount。
- `ndarray` 是同質連續陣列，只存純值，帶 `dtype` + `shape` + `strides`。
- 結果：記憶體省 8 倍、SIMD 可用、cache 命中高、可批次運算。
- 同質性不是限制，是**讓計算能發生**的前提。

**延伸**：02_three_lens_analysis § 1.1、04_layout_visual_spec IG-01

---

## 速學卡 02 — shape / axis / dtype 三劍客

**Prompt**：看到 `ValueError: shape mismatch`，第一步做什麼？

**Answer**：
- 印出兩邊的 `.shape` 與 `.dtype`。
- shape 從**右往左對齊**，找第一個不相容維度。
- axis 記憶法：**「reduce 類」axis 是壓掉的那一維**（sum、mean）；**「沿著類」axis 是走的方向**（cumsum、concat）。
- dtype 陷阱：`int + NaN` 會自動升到 `float64`（除非用 Arrow nullable int）。

**延伸**：01_on_page_annotation § A3

---

## 速學卡 03 — Broadcasting 四步驟

**Prompt**：`(3, 1, 5) + (4, 5)` 能不能相加？結果 shape？

**Answer**：
1. 右對齊、較短側補 1 → `(3, 1, 5)` vs `(1, 4, 5)`
2. 每維檢查：相等或其中之一為 1 → 相容
3. stride 0 偽裝（零記憶體），廣播成 `(3, 4, 5)`
4. 逐元素運算

**答案**：合法，結果 `(3, 4, 5)`。

**延伸**：04_layout_visual_spec IG-02、02 § 1.3

---

## 速學卡 04 — 向量化為什麼快

**Prompt**：NumPy 向量化比 Python for 迴圈快 100 倍，物理原因？

**Answer**：三層堆疊：
1. **SIMD**：AVX2 一指令處理 8 個 float32。
2. **Cache line**：連續記憶體一次搬 64 byte。
3. **BLAS**：矩陣運算委託給 OpenBLAS/MKL（50 年工程積累）。

for 迴圈三層都放棄：每元素解引用 + 物件協議 + cache miss。

**延伸**：03_bcg_narrative Page 5、02 § 1.1–1.2

---

## 速學卡 05 — View vs Copy

**Prompt**：`arr[::2]`、`arr.T`、`arr.reshape(...)`、`arr[mask]` 哪些是 view？

**Answer**：
- **View（共享記憶體）**：basic slicing（`arr[::2]`）、`arr.T`、`reshape`（若 contiguous）、`ravel()`
- **Copy（新配記憶體）**：fancy indexing（`arr[[0,2,4]]`）、boolean indexing（`arr[mask]`）、`flatten()`、`astype`
- **測試**：`np.shares_memory(a, b)`
- **為何重要**：對 view 賦值會改到原陣列；對 copy 賦值不會。

**延伸**：01 § A2、04 § 5.6

---

## 速學卡 06 — DataFrame 的 Index 是什麼

**Prompt**：`s1 + s2` 在 pandas 和 NumPy 結果為何不同？

**Answer**：
- NumPy 按**位置**對齊。
- pandas 按 **index 標籤**對齊；不在兩邊交集的標籤，結果填 NaN。
- Index 是資料的**身份**，不是位置。
- `df.columns` 本身也是 Index 物件。
- MultiIndex = 複合主鍵。

**延伸**：02 § 1.4、03 Page 8

---

## 速學卡 07 — 初次偵察五步驟

**Prompt**：拿到一份新的 CSV，前五行程式碼寫什麼？

**Answer**：
```python
df.head()                       # 看樣貌
df.info(memory_usage='deep')    # 欄名 + dtype + 非空數 + 記憶體
df.describe(include='all')      # 數值與類別摘要
df.shape                        # 尺寸
df.dtypes                       # 型別驗證
```
- `.info()` 是最重要的——一眼看完知道缺失與型別問題。
- 加 `memory_usage='deep'` 才有準確的 object dtype 記憶體。

**延伸**：01 § B2

---

## 速學卡 08 — Boolean Indexing 語法陷阱

**Prompt**：多條件篩選為何不能用 `and`？

**Answer**：
```python
# ❌ 錯誤
df[df['age'] > 30 and df['city'] == 'Taipei']

# ✓ 正確
df[(df['age'] > 30) & (df['city'] == 'Taipei')]
```
- Python 的 `and`/`or` 不支援 Series 逐元素運算。
- 必用 `&`、`|`、`~`，且每個條件**必須用括號包住**（運算優先順序）。
- `df.query('age > 30 and city == "Taipei"')` 裡面可以用 `and`（query 內是 Python 表達式解析器）。

**延伸**：01 § B3

---

## 速學卡 09 — groupby 的 split-apply-combine

**Prompt**：「各部門按城市分組的平均薪資」怎麼寫？`agg` vs `transform` 差在哪？

**Answer**：
```python
df.groupby(['department', 'city'])['salary'].mean()
```
- **Split**：按 key 分組
- **Apply**：套函式
- **Combine**：結果合回

**agg vs transform**：
- `agg`：每組 → 一個值（**降維**），結果 index 為 group key
- `transform`：每組 → 同長度結果（**保持形狀**），結果 index 與原 df 對齊
- `apply`：最通用、最慢，回傳形狀不保證

**延伸**：01 § B4、04 IG-04

---

## 速學卡 10 — 缺失值的四種處理策略

**Prompt**：`last_review_date` 有 15% 缺失，怎麼處理？

**Answer**：四象限決策：

| 策略 | 何時用 | API |
|------|--------|-----|
| 刪除 | 缺失比例極低且隨機（MCAR） | `dropna()` |
| 填固定值 | 「無值=零/未知」有業務語意 | `fillna(0)`, `fillna('Unknown')` |
| 統計填補 | 數值型、分布接近常態 | `fillna(df.mean())` |
| 模型填補 | 缺失比例高且欄位重要 | `sklearn.IterativeImputer` |

先分辨 MCAR / MAR / MNAR 機制，再選策略。`pd.NA` 與 `np.nan` 在 Arrow backend 下行為不同。

**延伸**：01 § B5

---

## 速學卡 11 — Copy-on-Write 核心規則

**Prompt**：pandas 2.0 的 CoW 改變了什麼？

**Answer**：
- **規則**：所有衍生 DataFrame 共享底層 array（讀共享），寫入時 clone（寫克隆）。
- **影響的程式碼**：對 slice / filter 回傳物件的寫入，不再改到原 df（消除未定義行為）。
- **不影響**：直接對 df 的賦值（`df['a'] = ...`）仍是 in-place。
- **啟用**：`pd.options.mode.copy_on_write = True`（2.x 可選，3.0 預設）。
- **SettingWithCopyWarning** 的根因就是 BlockManager view/copy 歧義，CoW 消滅此歧義。

**延伸**：01 § B6、02 § 1.5、04 § 5.5

---

## 速學卡 12 — Arrow Backend 何時啟用

**Prompt**：`dtype_backend='pyarrow'` 為什麼值得切換？

**Answer**：
- 記憶體：典型資料集省 **30–50%**
- 字串：從 object dtype 升級為 `string[pyarrow]`，ops 快數倍
- Nullable：原生支援 `int64[pyarrow]` + `pd.NA`，不必用 float 裝 NaN
- I/O：與 Parquet、Polars、DuckDB 零拷貝互操作

**啟用**：
```python
df = pd.read_csv('file.csv', dtype_backend='pyarrow')
```

**代價**：少數 legacy API 在 Arrow backend 下行為略有差異，遷移要測試。

**延伸**：01 § B6、03 Page 10

---

## 速學卡 13 — 工具規模感

**Prompt**：什麼時候該離開 pandas？

**Answer**：經驗法則：
- **< 1 GB**：pandas（生態成熟，預設選擇）
- **1–100 GB 單機**：
  - 偏好 DataFrame API → **Polars**（Rust、expression、lazy）
  - 偏好 SQL → **DuckDB**（embedded、zero-ETL、Parquet 原生）
- **> 100 GB 或需分散式** → **Spark**（集群、TB+）

Polars 不只是「更快的 pandas」——expression API、lazy frame、無 index、query optimizer 是哲學差異。DuckDB 是 SQL 哲學的本地化。

**延伸**：01 § B7、03 Page 11、04 IG-05、04 § 5.7

---

## 速學卡 14 — SQL ↔ pandas ↔ Polars 等價性

**Prompt**：你會寫 `SELECT region, SUM(revenue) FROM orders WHERE revenue > 1000 GROUP BY region ORDER BY SUM(revenue) DESC`，怎麼翻成 pandas？

**Answer**：

```python
# pandas
(df[df['revenue'] > 1000]
   .groupby('region', as_index=False)
   .agg(total=('revenue', 'sum'))
   .sort_values('total', ascending=False))

# Polars（等價語意）
(df.lazy()
   .filter(pl.col('revenue') > 1000)
   .group_by('region')
   .agg(pl.col('revenue').sum().alias('total'))
   .sort('total', descending=True)
   .collect())
```

**對照表**：
| SQL | pandas | Polars |
|-----|--------|--------|
| WHERE | `df[cond]` / `.query()` | `.filter()` |
| GROUP BY | `.groupby()` | `.group_by()` |
| SELECT agg | `.agg()` | `.agg(pl.col(..).sum())` |
| ORDER BY | `.sort_values()` | `.sort()` |
| JOIN | `.merge()` | `.join()` |

三套工具共享關聯代數語意。會一套就能遷移。

**延伸**：02 § 3.1、03 Page 6 & 11

---

## 附：快速自測

若能在 60 秒內答完每題，視為掌握。

- [ ] 01 ndarray vs list 三個差異
- [ ] 02 shape / axis / dtype 各自角色
- [ ] 03 Broadcasting 四步驟
- [ ] 04 向量化快的三層原因
- [ ] 05 哪些操作回傳 view 哪些 copy
- [ ] 06 pandas 的 `+` 為何跟 NumPy 不同
- [ ] 07 初次偵察五個函式
- [ ] 08 多條件篩選的語法陷阱
- [ ] 09 agg 與 transform 差別
- [ ] 10 缺失值四種處理策略
- [ ] 11 CoW 的核心規則
- [ ] 12 切 Arrow backend 的理由
- [ ] 13 pandas / Polars / DuckDB / Spark 選擇準則
- [ ] 14 SQL ↔ pandas ↔ Polars 任意操作互譯

通過 12/14 以上視為可上線。低於 10 建議回到 01_on_page_annotation.md 重看對應段落。
