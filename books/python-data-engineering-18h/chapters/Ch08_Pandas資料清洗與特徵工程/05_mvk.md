# Ch08 · Minimum Viable Knowledge

**章節**：Pandas 資料清洗與特徵工程（M3 · 3.5 hr · 本課程最長章）
**Governing thought**：Pandas 不是 API 字典，是資料工程師的工作台 — 讀→看→篩→清→轉→聚→併。

---

## 七步流水線（背下這個就贏一半）

| 步驟 | 動詞 | 主要 API |
|------|------|---------|
| 1 | 讀 | `read_csv` / `read_parquet` / `read_json` |
| 2 | 看 | `head` / `tail` / `info` / `describe` / `dtypes` / `shape` |
| 3 | 篩 | `loc` / `iloc` / 布林遮罩 / `query` |
| 4 | 清 | `dropna` / `fillna` / `ffill` / `interpolate` |
| 5 | 轉 | `apply(lambda)` / `.dt` / `.str` / `map` |
| 6 | 聚 | `groupby` + `agg` / `transform` / `pivot_table` |
| 7 | 併 | `concat` / `merge` / `join` |

---

## 三角心智模型

- **Series** = 帶 Index 的 1D 陣列（NumPy + Index）
- **DataFrame** = 多個 Series 共用同一 Index
- **Index** = 資料的「名字」，不是欄位、不是 row number
- **對齊（alignment）** = pandas 的隱藏外掛：兩個 Series 相加自動依 Index 對齊，缺位 NaN

---

## 篩選：四把鑰匙

| 鑰匙 | 適用 |
|------|------|
| `df.loc[label]` | 用標籤（Index / 欄名） |
| `df.iloc[pos]` | 用整數位置（Pythonic, 包前不包後） |
| `df[df.col > x]` | 布林遮罩，最 Pythonic |
| `df.query("col > x and city=='Taipei'")` | 字串條件，可讀性高 |

⚠ **loc 是包前包後、iloc 是包前不包後** — bug 第一名。
⚠ **pandas 2.x 預設 Copy-on-Write**，鏈式賦值即將被棄用。

---

## 缺失值：四種策略

| 策略 | API | 何時 |
|------|-----|------|
| 整列刪除 | `dropna()` | 缺失少、資料充足 |
| 整欄刪除 | `dropna(axis=1, thresh=...)` | 整欄高比例缺失 |
| 填補定值 | `fillna(0/mean/median/mode)` | 缺失有合理替代 |
| 向前/內插 | `ffill / bfill / interpolate()` | 時間序列 |

⚠ **dropna 不是預設答案** — 先問為什麼缺。

---

## apply + lambda（呼應 Ch3）

- `Series.apply(func)` — 每元素
- `DataFrame.apply(func, axis=0)` — 每欄（預設）
- `DataFrame.apply(func, axis=1)` — 每列
- `Series.map(dict_or_func)` — 字典映射
- ⚠ **能向量化就不要 apply**（`df.col * 1.05` 比 `apply(lambda x: x*1.05)` 快 100×–200×）
- 高頻 accessor：`.dt`（時間）、`.str`（字串）

---

## groupby：Split-Apply-Combine

```python
df.groupby('city')['revenue'].sum()
df.groupby(['city','product']).agg({'revenue':'sum','qty':'mean'})
df['city_avg'] = df.groupby('city')['revenue'].transform('mean')  # 保 shape
df.pivot_table(index='city', columns='month', values='revenue', aggfunc='sum')
```

- `agg` 縮減 / `transform` 保 shape / `pivot_table` wide-format

---

## 合併：concat / merge / join

- `concat`：堆疊（axis=0 加列、axis=1 加欄）
- `merge`：依鍵合併（how = inner/left/right/outer）
- `join`：簡化版 merge，預設用 Index
- ⚠ 合併後必跑 `len()` 比對；用 `indicator=True` debug

---

## 時間序列三件套

```python
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df['2024-01']                # partial string indexing
df.resample('D').sum()       # groupby 的時間版
df['ma7'] = df['rev'].rolling(7).mean()
```

---

## 學生離開教室時應能

1. 解釋 Series / DataFrame / Index 三角關係，並能畫出對齊範例
2. 用 `loc` / `iloc` / `query` 精確取資料，並能說出 loc 與 iloc 的差別
3. 偵測缺失值並依「為什麼缺」選對處理策略
4. 用 `apply(lambda)` + `.dt` / `.str` 衍生 5 個以上特徵欄位
5. 用 `groupby` + `agg` / `transform` / `pivot_table` 完成業務切片
6. 用 `merge` 完成兩表合併並能解釋四種 `how` 的差別
7. 用 `to_datetime` + `resample` + `rolling` 處理時間序列基本聚合

## 本章刻意不深教（留給後續或進階）

- MultiIndex 進階操作
- pandas 內部 BlockManager
- 與 PyArrow / Dask 的整合
- pandas-stubs 型別檢查

## 銜接

- **Ch09 Matplotlib**：本章產出的 DataFrame 直接吃進視覺化
- **Ch10 OOP × Pandas 整合**：把這 7 步流水線封裝成 `DataCleaner` 類別（Ch05 的繼承 + chaining 派上用場）
