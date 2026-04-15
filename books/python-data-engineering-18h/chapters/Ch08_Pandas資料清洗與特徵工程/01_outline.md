# Chapter 8：Pandas 資料清洗與特徵工程

**模組：** M3 數據工程核心  
**時數：** 3.5 小時（本課程最長章節）  
**前置知識：** Ch3 Lambda、Ch6 I/O、Ch7 NumPy  
**後續銜接：** Ch9（視覺化吃 DataFrame）、Ch10（DataCleaner 整合）

---

## 一、章節定位

本章是整門課的**核心工作台**。學員結業後 80% 的時間會在 Pandas 上度過。本章的取捨原則：
- **教實戰流程**（讀→看→篩→清→轉→聚→併），不是 API 字典
- **與 Ch3 Lambda 合流**：所有 `apply` 都會用到
- **為 Ch10 鋪路**：所有操作將被封裝進 `DataCleaner` 類別

---

## 二、學習目標

完成本章後，學生能夠：

1. 解釋 Series / DataFrame / Index 的關係
2. 用 `loc` / `iloc` / `query` 精確取資料
3. 偵測並處理缺失值，選對策略（drop / fillna / interpolate）
4. 用 `apply(lambda)` 進行欄位轉換與特徵工程
5. 使用 `groupby` + `agg` 完成業務切片
6. 用 `merge` / `join` / `concat` 合併多張表
7. 處理時間序列：`to_datetime`、`resample`

---

## 三、章節結構

### 8-1. Series / DataFrame / Index 三角關係（30 分鐘）
- Series：帶索引的一維陣列（底層 NumPy + Index）
- DataFrame：多個 Series 共用 Index
- **索引哲學**：Index 不是欄位，是「資料的標籤」
- 建立方式：from dict / from list of dicts / from CSV
- 看資料：`head`、`tail`、`info`、`describe`、`dtypes`、`shape`
- **教學原則**：每個新資料集都先跑這 6 個方法

### 8-2. 篩選與索引：loc / iloc / query（40 分鐘）
- `df['col']` vs `df[['col1', 'col2']]`：Series vs DataFrame
- **`loc`**：用標籤（label-based）
- **`iloc`**：用位置（integer-based）
- **布林篩選**：`df[df['age'] > 30]`
- **多條件**：`df[(df['age'] > 30) & (df['city'] == 'Taipei')]`
- **`query`**：可讀性更高的篩選 `df.query('age > 30 and city == "Taipei"')`
- **Copy-on-Write 與鏈式賦值警告**（Pandas 2.0+）

### 8-3. 缺失值處理（40 分鐘）
- **偵測**：`isna`、`notna`、`isnull`
- **三種來源**：
  1. 真的缺資料（沒填寫）
  2. 編碼問題（"-" 或 "N/A" 沒被識別）
  3. 計算產生（除以 0、時間平移）
- **四種策略**：
  | 策略 | API | 何時用 |
  |------|-----|--------|
  | 整列刪除 | `dropna()` | 缺失少、資料充足 |
  | 整欄刪除 | `dropna(axis=1)` | 整欄高比例缺失 |
  | 填補定值 | `fillna(0 / mean / median / mode)` | 缺失有合理替代 |
  | 向前/向後補 | `ffill / bfill` | 時間序列 |
- **異常值處理**：用 IQR 或標準差判定，搭配布林索引

### 8-4. apply + lambda：欄位轉換與特徵工程（45 分鐘）
- 三個層級：
  - `Series.apply(func)`：對每個元素
  - `DataFrame.apply(func, axis=0/1)`：對每欄/每列
  - `DataFrame.applymap(func)`：對每個元素（已 deprecated，改用 `df.map`）
- **與 Ch3 Lambda 合流**：
  ```python
  df['price_with_tax'] = df['price'].apply(lambda x: x * 1.05)
  df['name_clean'] = df['name'].apply(lambda s: s.strip().lower())
  df['category'] = df['score'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 60 else 'C')
  ```
- **效能注意**：能用向量化運算就不要用 apply（`df['x'] * 1.05` 比 `apply(lambda x: x*1.05)` 快很多）
- **特徵工程實例**：日期欄位拆出年/月/週幾、文字欄位長度、類別欄 one-hot

### 8-5. groupby 與聚合（35 分鐘）
- **Split-Apply-Combine 心智模型**
- 基本用法：
  ```python
  df.groupby('city')['revenue'].sum()
  df.groupby(['city', 'product']).agg({'revenue': 'sum', 'qty': 'mean'})
  ```
- 自訂聚合：`agg(lambda g: ...)`
- `transform` vs `agg`：保持原 shape vs 聚合縮減
- `pivot_table`：交叉表速成

### 8-6. 合併操作：merge / join / concat（25 分鐘）
- **`concat`**：沿軸堆疊（縱向加列、橫向加欄）
- **`merge`**：依鍵值合併（類似 SQL join）
  - `how='inner' / 'left' / 'right' / 'outer'`
  - `on='key'` 或 `left_on / right_on`
- **常見陷阱**：合併後出現 `_x`、`_y` 重複欄

### 8-7. 時間序列基礎（25 分鐘）
- `pd.to_datetime`：字串轉時間
- DatetimeIndex 的優勢：可以 `df['2024-01']` 直接切片
- `resample('D' / 'W' / 'M')`：時間重採樣（呼應 groupby）
- `rolling(window=7).mean()`：移動平均

---

## 四、課後練習

1. **清洗題**：給一份混亂的銷售 CSV（缺失、字串日期、混型別），完成標準化
2. **特徵題**：對使用者資料表，用 `apply + lambda` 衍生 5 個新欄位（年齡分組、活躍度標記等）
3. **聚合題**：用 `groupby` + `pivot_table` 做出「各城市各月份營收交叉表」
4. **整合題**：合併三張表（users / orders / products），輸出每位使用者的消費總額排名

---

## 五、銜接下一章

資料已清洗、聚合，但表格不會說話。Ch9 進入 Matplotlib，把這些 DataFrame 變成可呈報的圖表。
