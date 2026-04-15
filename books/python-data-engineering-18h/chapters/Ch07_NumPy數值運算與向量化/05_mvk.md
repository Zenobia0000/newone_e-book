# Ch07 · Minimum Viable Knowledge

**章節**：NumPy 數值運算與向量化（M3 · 2.0 hr）
**Governing thought**：NumPy 不是讓你算快一點，而是讓你用 shape × broadcasting 的語言描述計算問題。

---

## 四件必帶走的柱子

### 1. ndarray 三件套
- `shape`：每個維度的長度（tuple）
- `dtype`：所有元素的統一型別（`float64` / `int32` / ...）
- `ndim`：維度數（= `len(shape)`）
- **底層**：連續記憶體 + 單一型別 → 可上 SIMD、可進 CPU cache（呼應 Ch1）

### 2. 索引三招
| 招式 | 語法 | 回傳 |
|------|------|------|
| 切片 | `arr[1:3, ::2]` | **view**（共享記憶體） |
| 布林索引 | `arr[arr > 0]` | copy，一維攤平 |
| Fancy Indexing | `arr[[0, 2, 5]]` | copy |
- **view 陷阱**：改 view 就改到原 array；真要獨立資料用 `.copy()`。

### 3. Broadcasting 三步規則
1. 從**右**往左對齊維度
2. **缺少**的維度補 1
3. 大小為 **1** 的維度可沿該軸拉伸配對
- 不符合 → `ValueError: operands could not be broadcast together`
- 實務：`(X - X.mean(axis=0)) / X.std(axis=0)` 一行做 z-score

### 4. axis 心智模型
- `axis=0` → 沿「列」方向聚合 → 結果是「每欄一個值」
- `axis=1` → 沿「欄」方向聚合 → 結果是「每列一個值」
- 記法：**axis=k 就是把第 k 維摺掉**

---

## 向量化效能為什麼快

1. **底層 C 實作**：無 Python 直譯開銷（呼應 Ch1 編譯 vs 直譯）
2. **SIMD 指令**：CPU 一次處理 4/8 筆資料
3. **無 Python 物件包裝**：每個數字不是 `PyObject`
4. 實測差距：1e8 筆加總，list vs `np.sum` 約 **50–100×**

---

## 學生離開教室時應能

1. 看到 ndarray 能用 `shape` / `dtype` / `ndim` 描述它
2. 寫出多維切片、布林索引、Fancy Indexing 並說明 view vs copy
3. 說明 broadcasting 三步規則並寫出無 for 的運算
4. 判斷 `axis=0` / `axis=1` 對 shape 的影響
5. 用一句話解釋「為什麼 NumPy 快 50 倍以上」

## 本章刻意不教

- `np.einsum`（需要另起一章）
- `stride_tricks` / `as_strided`（危險）
- Structured array（`dtype` 複合欄位）— 交給 Ch08 Pandas
- Masked array / `np.ma`
- 線性代數 `np.linalg`（AI 章節再碰）

## 銜接
- **Ch08 Pandas**：`DataFrame` / `Series` 的 `.values` 就是 ndarray，所有本章技能直接複用
- **Ch09 Matplotlib**：`plt.plot` 吃的就是 ndarray
