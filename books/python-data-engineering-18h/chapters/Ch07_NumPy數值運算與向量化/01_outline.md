# Chapter 7：NumPy 數值運算與向量化

**模組：** M3 數據工程核心  
**時數：** 2.0 小時  
**前置知識：** Ch1（CPU/RAM）、Ch3（Lambda）  
**後續銜接：** Ch8（Pandas 底層即 NumPy）、Ch9（Matplotlib 吃 ndarray）

---

## 一、章節定位

NumPy 不是「讓你算快一點」的工具，而是「讓你用正確的語言描述計算問題」。本章重點是建立**向量化思維**，讓學員從「我寫個 for 迴圈」直接跳到「shape × broadcasting」的心智模型。

---

## 二、學習目標

完成本章後，學生能夠：

1. 建立 ndarray，並用 `shape`、`dtype`、`ndim` 描述它
2. 用切片、布林索引、Fancy Indexing 取出子陣列
3. 解釋 broadcasting 規則，寫出無 for 迴圈的運算
4. 估算 NumPy 與純 Python 的效能差距，並說明原因

---

## 三、章節結構

### 7-1. ndarray：科學計算的基本資料結構（30 分鐘）
- 為何 list 不夠用：型別混雜、無向量化、記憶體散落
- ndarray 的三大屬性：
  - `shape`：每個維度的長度
  - `dtype`：所有元素的統一型別（int32, float64, ...）
  - `ndim`：維度數
- 建立方式：`np.array`、`np.zeros`、`np.ones`、`np.arange`、`np.linspace`
- **記憶體配置**：ndarray 是連續記憶體區塊（呼應 Ch1 RAM 與 CPU cache）

### 7-2. 索引與切片（30 分鐘）
- 一維切片：跟 list 一樣
- 多維切片：`arr[行, 列]`、`arr[:, 0]`、`arr[1:3, ::2]`
- **布林索引**：`arr[arr > 0]` 過濾元素
- **Fancy Indexing**：`arr[[0, 2, 5]]` 用整數陣列當索引
- **常見陷阱**：切片是 view（共享記憶體），Fancy Indexing 是 copy

### 7-3. Broadcasting：讓資料自己跑起來（35 分鐘）
- 兩個 array 維度不同也能運算的規則：
  1. 從右往左對齊維度
  2. 缺少的維度補 1
  3. 大小為 1 的維度可被「拉伸」配對
- 經典範例：
  ```python
  prices = np.array([100, 200, 300])      # shape (3,)
  discount = np.array([[0.9], [0.8]])      # shape (2,1)
  result = prices * discount               # shape (2,3)
  ```
- 何時 broadcasting 不適用（dimension mismatch）
- **資料工程實例**：對整個 DataFrame 的數值欄做 z-score 標準化

### 7-4. 向量化運算與效能對比（25 分鐘）
- 為何向量化比 for 迴圈快 10–100 倍：
  - **底層 C 實作**（呼應 Ch1 編譯 vs 直譯）
  - **SIMD 指令**：CPU 一次處理多筆資料
  - **無 Python 物件包裝開銷**
- **Demo**：1 億個元素加總，list comprehension vs `np.sum`
- 內建統計函式：`mean`、`std`、`min`、`max`、`argmax`、`percentile`
- `axis` 參數的意義：沿哪個方向聚合
  - `axis=0`：沿列方向（每欄聚合）
  - `axis=1`：沿欄方向（每列聚合）

---

## 四、課後練習

1. **基礎題**：建立 5×5 的隨機矩陣，取出對角線、最大值座標、每列平均
2. **Broadcasting 題**：給 100 名學生 × 5 科成績的矩陣，用 broadcasting 算出每人相對於該科平均的差值
3. **效能題**：對 1000 萬筆資料分別用 for、Comprehension、NumPy 計算平方加總，比較執行時間

---

## 五、銜接下一章

NumPy 處理數值矩陣，但真實業務資料是「帶欄位名稱、混型別、有缺失」的表格。Ch8 進入 Pandas —— 它的底層就是 NumPy，但加上了業務友善的介面。
