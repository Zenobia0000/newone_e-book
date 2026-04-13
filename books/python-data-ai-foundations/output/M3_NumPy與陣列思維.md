# Module 3：NumPy 與陣列思維 — 從數值計算到機器學習的底層語言

**所屬課程：** Python 數據分析與 AI 工程基礎  
**模組編號：** M3  
**時長：** 3 小時  
**難度：** 中階入門  
**前置模組：** M2 Python 分析基礎  
**後續模組：** M4 pandas 與資料清理

---

## 一、模組定位

這個模組是你從「寫 Python」到「做資料運算」的第一道門。

M2 之前，你處理的是字串、串列、字典——通用的資料容器。  
M3 之後，你操作的是陣列——為科學計算而生的數值引擎。

NumPy 不只是「讓計算快一點」的工具。它是機器學習框架的共通語言：PyTorch、TensorFlow、scikit-learn 底層全部以多維陣列為核心資料結構。你現在學的 `shape`、`axis`、`broadcasting`，正是日後看懂任何 ML 程式碼的鑰匙。

這個模組教你三件事：

1. **陣列思維**：理解為何 AI/ML 用陣列而非串列，以及兩者的根本差異
2. **核心操作**：shape 操控、broadcasting、向量化、線性代數基礎
3. **實戰工具**：亂數生成、統計計算、切片模式、在 ML 工作流中的定位

---

## 二、學習目標

完成本模組後，學生能夠：

1. 說明 ndarray 與 Python list 的根本差異，解釋為何 ML 框架選擇陣列作為基本資料結構
2. 正確使用 `shape`、`axis`、`dtype` 描述與操作一個 NumPy 陣列
3. 理解 broadcasting 規則，寫出不含 for 迴圈的向量化運算
4. 使用 `reshape`、`transpose`、切片等操作靈活改變陣列的視角與形狀
5. 使用 NumPy 完成基本矩陣操作（乘法、轉置、逆矩陣）與統計摘要
6. 使用 NumPy 亂數工具建立模擬資料，支援資料科學實驗
7. 識別可以向量化的程式碼模式，並完成重寫
8. 說明 NumPy 在 ML 工作流中的定位，以及 NumPy 2.0 的重要改動

---

## 三、關鍵概念清單

學完本模組應能用自己的話解釋以下所有詞彙：

- [ ] ndarray vs Python list（記憶體結構的根本差異）
- [ ] shape 與 reshape（尺寸描述與重塑）
- [ ] axis（操作方向：行軸 vs 列軸）
- [ ] dtype（數值精度與記憶體的關係）
- [ ] broadcasting（不需要迴圈的條件與規則）
- [ ] vectorized operation（向量化操作，與 for 迴圈的語義差異）
- [ ] np.random（亂數生成與種子固定）
- [ ] 切片模式（基本切片、布林切片、花式索引）
- [ ] 矩陣乘法 `@` 與 `np.dot()`
- [ ] np.linalg（線性代數基本工具）
- [ ] 統計函式（mean、std、var、median、percentile）
- [ ] 特徵矩陣 X 與標籤向量 y 的慣例形狀
- [ ] NumPy 2.0 的重大 API 改動

---

## 四、投影片大綱（11 張）

| 編號 | 標題 | 核心主張 |
|------|------|----------|
| S1 | 你以為在學工具，其實在學模型的底層語言 | NumPy 不是可選的，它是 ML 框架的地基 |
| S2 | ndarray：為科學計算設計的資料結構 | list 是通用容器，ndarray 是計算引擎 |
| S3 | shape / axis / dtype：三個你必須看懂的概念 | 不理解這三個，就看不懂任何模型的 shape mismatch |
| S4 | reshape 與切片：改變陣列的視角 | 資料本身沒有動，只是你換了看它的方式 |
| S5 | Broadcasting：讓資料自己跑起來 | 理解規則就能消滅 90% 的迴圈操作 |
| S6 | 向量化思維：不是快，是對的 | for 迴圈是思維問題，不只是效能問題 |
| S7 | 亂數生成：資料科學的實驗工具 | 可重現的亂數是科學實驗的基礎 |
| S8 | 統計計算：從陣列到摘要指標 | NumPy 的統計函式是資料分析的第一層 |
| S9 | 基礎線性代數：矩陣乘法與逆矩陣 | ML 的核心計算是矩陣乘法，不是數字加減 |
| S10 | NumPy 在 ML/DL 的實際角色 | 從特徵矩陣到模型權重，NumPy 是共通語言 |
| S11 | 里程碑：NumPy 2.0 — 2006 年以來第一個 major release | 工具也有版本意識，演進不停歇 |

---

## 五、逐張投影片詳述

---

### S1 — 你以為在學工具，其實在學模型的底層語言

**核心主張：** 所有 ML/DL 框架的核心計算都建立在多維陣列操作上，NumPy 是理解這一切的最短路徑。

**講師講解要點：**

- 打開任何 PyTorch 或 TensorFlow 的教學，第一步幾乎都是 `import numpy as np`。為什麼？因為 tensor 的概念與操作幾乎直接繼承自 NumPy。
- 線性迴歸的預測公式 `y = Xw + b`，X 是特徵矩陣、w 是權重向量。沒有矩陣概念，你就只能背公式，無法理解為什麼這樣計算。
- NumPy 不是「讓你算快一點」的工具，而是讓你用正確的語言描述計算問題的工具。快只是副作用。
- 2024 年的 AI 工程師每天用的概念：batch size、feature dimension、embedding dimension，全部是 ndarray 的 shape 概念。
- 學 NumPy 的終點不是 NumPy，而是讓 PyTorch、JAX、TensorFlow 都變得可讀。

**視覺建議：** 一張橫向對照表，左邊是數學符號（向量、矩陣、張量），右邊是對應的 NumPy 程式碼。中間畫箭頭，標示「你已經懂概念，只差語法」。底部附一行：「這堂課學完，你看得懂 ML 框架的原始碼」。

**轉場：** 「但 Python 不是本來就有 list 嗎？為什麼需要 ndarray？下一張說清楚。」

---

### S2 — ndarray：為科學計算設計的資料結構

**核心主張：** list 是通用容器，可以放任何東西；ndarray 是同質性的數值陣列，這個限制帶來根本性的效能與語義優勢。

**講師講解要點：**

- Python list 可以放 `[1, "hello", None, [2, 3]]`，這種彈性在記憶體上付出代價：每個元素是一個獨立的 Python 物件，有額外的類型標記、引用計數、記憶體位址。
- ndarray 只放一種型別（例如 float64），所有元素緊密排列在連續記憶體空間中，CPU 的快取命中率大幅提升。
- 效能差距在小資料看不出來，但在 100 萬筆資料時，list 的迭代可能慢 50-100 倍。
- `np.array([1,2,3])` vs `[1,2,3]`：外表相似，底層天壤之別。前者是 C 語言陣列包了一層 Python 介面，後者是 Python 物件指標的集合。
- 關鍵：ndarray 讓你把一個「對整個陣列的操作」送進去，而不是對每個元素分別操作。這就是向量化的基礎。

**常見建立方式一覽：**

```python
import numpy as np

# 從 list 建立
a = np.array([1, 2, 3, 4, 5])

# 建立特定形狀的陣列
zeros = np.zeros((3, 4))        # 全零矩陣
ones = np.ones((2, 3))          # 全一矩陣
eye = np.eye(4)                 # 單位矩陣
arange = np.arange(0, 10, 2)    # 類似 range，回傳 ndarray
linspace = np.linspace(0, 1, 5) # 等間距 5 個點
```

**視覺建議：** 記憶體示意圖。左邊畫 Python list：一排格子，每格指向分散的物件（含型別標記、值、引用計數）。右邊畫 ndarray：一排緊密排列的數值格子，直接是值，沒有額外開銷。底部加一行：「同樣 100 萬個 float，ndarray 用的記憶體約是 list 的 1/8」。

**轉場：** 「有了 ndarray，接下來最重要的三個概念：shape、axis、dtype。理解這三個，你就能看懂任何框架的錯誤訊息。」

---

### S3 — shape / axis / dtype：三個你必須看懂的概念

**核心主張：** shape 描述尺寸、axis 描述操作方向、dtype 描述元素型別。這三個概念是所有後續操作的語言基礎。

**講師講解要點：**

- **shape**：`arr.shape` 回傳一個 tuple，例如 `(100, 28, 28)` 表示 100 張 28×28 的灰階影像。shape 不只是「大小」，它是資料的意義標記。在 ML 裡，`(batch_size, features)` 是你最常看到的 2D shape。
- **axis**：`np.sum(arr, axis=0)` 是沿著第 0 軸加總，對矩陣來說就是對每一列加總得到一行向量。`axis=1` 則是對每一行加總。關鍵記憶法：axis 是你要「壓縮掉」的那個維度。
- **dtype**：`float64` 精度高但佔記憶體，`float32` 是深度學習的標準選擇（GPU 的原生精度），`int8` 用於模型量化。型別不只影響記憶體，也影響計算精度。

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)   # (2, 3) — 2 列 3 欄
print(arr.dtype)   # int64（預設）
print(arr.ndim)    # 2 — 二維陣列

# axis 示範
print(arr.sum(axis=0))  # [5, 7, 9]  — 沿列方向壓縮
print(arr.sum(axis=1))  # [6, 15]    — 沿欄方向壓縮

# 型別轉換
arr_f32 = arr.astype(np.float32)
```

**視覺建議：** 三個並排的方塊示意圖。第一個：一個 3D 立方體，標示三個軸的方向。第二個：一個 2D 矩陣，展示 `sum(axis=0)` 與 `sum(axis=1)` 的結果方向。第三個：dtype 精度對照表（float64 / float32 / int32 / int8 + 記憶體占用 + 使用場景）。

**轉場：** 「理解 shape 之後，我們看如何重塑陣列的形狀，以及如何精確地取出你要的部分。」

---

### S4 — reshape 與切片：改變陣列的視角

**核心主張：** reshape 讓你改變陣列的維度結構而不移動資料；切片讓你精確地取出子集。這兩個操作在 ML 資料預處理中每天都在用。

**講師講解要點：**

- **reshape**：`arr.reshape(3, 4)` 把陣列重塑為 3 列 4 欄，但資料本身沒有複製，只是換了一個「看的方式」（view）。`-1` 是魔法數字：`arr.reshape(-1, 1)` 表示「欄數為 1，列數自動計算」，在 scikit-learn 餵資料時非常常用。
- **flatten 與 ravel**：`arr.flatten()` 壓平成一維，會複製資料；`arr.ravel()` 也壓平但盡量回傳 view（不複製）。
- **基本切片**：與 Python list 相同語法，但支援多維。`arr[0, :]` 取第 0 列所有欄；`arr[:, 2]` 取所有列的第 2 欄；`arr[1:3, 0:2]` 取子矩陣。
- **布林切片**：`arr[arr > 3]` 回傳所有大於 3 的元素（攤平為一維）；`arr[mask]` 支援任意布林陣列。這是資料篩選的核心操作。
- **花式索引（Fancy Indexing）**：`arr[[0, 2, 4]]` 取第 0、2、4 列，回傳的是複製（不是 view）。

```python
arr = np.arange(12)

# reshape
matrix = arr.reshape(3, 4)
col_vector = arr.reshape(-1, 1)  # shape: (12, 1)

# 切片
print(matrix[0, :])      # 第 0 列
print(matrix[:, -1])     # 最後一欄
print(matrix[0:2, 1:3])  # 左上 2×2 子矩陣

# 布林切片
mask = matrix > 6
print(matrix[mask])      # [7, 8, 9, 10, 11]

# 轉置
print(matrix.T.shape)    # (4, 3)
```

**視覺建議：** 一個 4×4 的矩陣示意圖，用不同顏色區塊標示不同切片模式的結果（第 0 列、第 2 欄、左上子矩陣、對角線）。旁邊附對應的程式碼。底部加一行：「切片回傳的是 view，修改它會影響原始陣列——這是常見的 bug 來源」。

**轉場：** 「理解切片之後，來看 NumPy 最神奇的能力：broadcasting。它讓不同形狀的陣列可以直接運算，不需要迴圈。」

---

### S5 — Broadcasting：讓資料自己跑起來

**核心主張：** Broadcasting 是 NumPy 的核心魔法，允許不同 shape 的陣列在特定規則下進行操作，消滅大量重複的迴圈程式碼。

**講師講解要點：**

- 最簡單的案例：`arr + 5`，一個陣列加一個純量。你沒有寫迴圈，NumPy 自動把 5「廣播」到每個元素。這是 broadcasting 的最基本形式。
- 更複雜的案例：一個 `(3, 4)` 的矩陣加一個 `(1, 4)` 的向量，向量會沿著第 0 軸廣播，等效於把向量複製三份再相加。但 NumPy 實際上不複製記憶體，只是在計算時虛擬地廣播。
- **Broadcasting 規則（從右往左對齊）**：
  1. 如果兩個維度相同，可以直接操作
  2. 如果一個維度是 1，可以廣播
  3. 如果兩個維度不同且都不是 1，報錯
- 實際應用：特徵標準化。一行搞定，不需要任何迴圈：

```python
X = np.random.randn(100, 5)  # 100 個樣本、5 個特徵

# 每個特徵（欄）減去均值、除以標準差
X_mean = X.mean(axis=0)   # shape: (5,)
X_std = X.std(axis=0)     # shape: (5,)
X_normalized = (X - X_mean) / X_std  # broadcasting 自動對齊
# X shape (100,5), X_mean shape (5,) → broadcasting 沿 axis=0 廣播
```

- 注意事項：broadcasting 的錯誤訊息是 `operands could not be broadcast together with shapes (3,4) (4,)`，看到這個，先從右到左對齊兩個 shape，找出不相容的維度。

**視覺建議：** 動態圖示（靜態版）：左邊一個 `(3, 4)` 的藍色矩陣，右邊一個 `(1, 4)` 的橙色向量，用虛線箭頭表示橙色向量「複製」三份覆蓋到藍色矩陣上，最後變成一個綠色的 `(3, 4)` 結果矩陣。底部加一個 broadcasting 規則的簡表（合法 vs 非法的 shape 組合各三例）。

**轉場：** 「Broadcasting 讓你不用寫迴圈，但為什麼不用迴圈這件事如此重要？下一張說向量化思維。」

---

### S6 — 向量化思維：不是快，是對的

**核心主張：** 用 for 迴圈處理陣列操作不只是效能問題，而是用了錯誤的抽象層次描述問題。向量化是讓程式碼的語義與數學意圖對齊。

**講師講解要點：**

- 以計算兩個向量的點積為例，展示三個版本：Python for 迴圈版、NumPy 向量化版、`np.dot()` 版。效能差距可達 100 倍，但更重要的是：哪一個最清楚說明「這是點積運算」？

```python
a = np.array([1.0, 2.0, 3.0, 4.0])
b = np.array([5.0, 6.0, 7.0, 8.0])

# 方式一：for 迴圈（語義不清、效能差）
result = 0
for i in range(len(a)):
    result += a[i] * b[i]

# 方式二：向量化（清晰、快速）
result = np.sum(a * b)

# 方式三：語義最清晰
result = np.dot(a, b)
```

- 向量化迫使你用「整個陣列」來思考，而不是「每個元素」。這和 ML 框架的思維一致：你不操作單一樣本，你操作一個 batch。
- 常見的向量化替換模式：
  - `np.where()` 替換條件迴圈（類似三元運算子，但作用在整個陣列）
  - `np.cumsum()` 替換累加迴圈
  - `np.maximum(0, arr)` 實作 ReLU，不需要任何 if
- 識別「可以向量化」的信號：如果你的 for 迴圈在遍歷 ndarray 的每個元素做相同操作，幾乎都可以向量化。
- 反例：遞歸依賴（後一個值依賴前一個值的計算結果）無法向量化。不要盲目去除所有迴圈。

**視覺建議：** 左右對比程式碼塊。左邊：8 行的 for 迴圈版。右邊：1 行的 `np.dot(a, b)`。底部加時間比較條形圖（100 萬維向量）：for 迴圈約 2500ms vs NumPy 約 5ms。右邊下方標注：「更短、更清晰、更接近數學原意」。

**轉場：** 「向量化思維建立之後，我們來看一個實際工作中天天用到的工具：亂數生成。」

---

### S7 — 亂數生成：資料科學的實驗工具

**核心主張：** 可重現的亂數是科學實驗的基礎。NumPy 的亂數工具讓你能建立模擬資料、初始化模型、驗證演算法。

**講師講解要點：**

- 亂數在資料科學中的使用場景：建立測試資料集、模擬實驗、初始化神經網路權重、交叉驗證的資料分割、Bootstrap 抽樣。
- **固定種子（seed）**：可重現性是科學實驗的基本要求。`np.random.seed(42)` 固定全域種子，但更推薦使用現代的 Generator API：

```python
# 現代推薦寫法（NumPy 1.17+）
rng = np.random.default_rng(seed=42)

# 常用分布
normal = rng.normal(loc=0, scale=1, size=(100, 5))    # 常態分布
uniform = rng.uniform(low=0, high=1, size=(100,))      # 均勻分布
integers = rng.integers(low=0, high=10, size=(50,))    # 整數

# 舊版語法（仍常見於教學中）
np.random.seed(42)
X = np.random.randn(100, 5)    # 標準常態
y = np.random.randint(0, 2, 100)  # 二元標籤

# 從現有資料中抽樣
arr = np.arange(100)
sample = rng.choice(arr, size=10, replace=False)  # 不重複抽樣
shuffled = rng.permutation(arr)  # 隨機排列
```

- `np.random.randn` vs `np.random.rand`：前者是標準常態分布（均值 0，標準差 1），後者是 [0,1) 的均勻分布。混用是初學者的常見錯誤。
- 工程意義：在機器學習實驗中，固定 seed 讓結果可重現，報告結果時應說明使用的 seed 值。

**視覺建議：** 兩個並排的直方圖示意：左邊是常態分布 `randn`，右邊是均勻分布 `rand`，各自標示均值與範圍。底部附一個 seed 固定的示意圖：「相同的 seed → 相同的序列 → 結果可重現」。

**轉場：** 「有了資料之後，接下來是從陣列中提取統計摘要。」

---

### S8 — 統計計算：從陣列到摘要指標

**核心主張：** NumPy 內建完整的統計函式，是資料分析的第一層工具。理解 axis 參數讓你能沿任意維度計算統計量。

**講師講解要點：**

- NumPy 的統計函式幾乎都支援 `axis` 參數，讓你能對矩陣的行或列分別計算：

```python
data = np.array([
    [85, 92, 78, 90],   # 學生 A 的四科成績
    [70, 88, 95, 72],   # 學生 B
    [93, 79, 85, 88],   # 學生 C
])

# 基本統計量
print(data.mean())          # 整體平均：83.75
print(data.mean(axis=1))    # 每位學生的平均：[86.25, 81.25, 86.25]
print(data.mean(axis=0))    # 每科的平均：[82.67, 86.33, 86.0, 83.33]

print(data.std(axis=1))     # 每位學生的標準差
print(data.max(axis=0))     # 每科最高分
print(data.min(axis=1))     # 每位學生最低分

# 百分位數
print(np.percentile(data, 75))        # 全體第 75 百分位
print(np.percentile(data, [25, 50, 75]))  # 四分位數

# 排序與排名
print(np.sort(data, axis=1))           # 每位學生成績由低到高排序
print(np.argsort(data, axis=1))        # 排序的索引（可用於找出最低分的科目）

# 累積計算
print(np.cumsum(np.array([1, 2, 3, 4])))  # [1, 3, 6, 10]
```

- `np.percentile` 是分析資料分布的重要工具，也是後續離群值檢測（IQR 方法）的基礎。
- `np.argsort` 回傳排序後的索引，常用於找出「第幾個特徵最大」。

**視覺建議：** 一個 3×4 的成績矩陣示意圖，用不同顏色箭頭標示 `axis=0`（垂直壓縮，得到 4 個科目均值）和 `axis=1`（水平壓縮，得到 3 個學生均值）的方向。旁邊附對應的數字結果。

**轉場：** 「統計計算之後，我們看 ML 最核心的數學操作：矩陣乘法。」

---

### S9 — 基礎線性代數：矩陣乘法與逆矩陣

**核心主張：** 機器學習的核心計算是矩陣乘法，不是數字加減。`@` 運算符和 `np.linalg` 是這一層的工具。

**講師講解要點：**

- **矩陣乘法**：ML 中每一層神經網路的前向傳播就是 `output = W @ input + b`，W 是權重矩陣、`@` 是矩陣乘法。

```python
# 矩陣乘法的三種寫法（結果相同）
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C1 = A @ B              # 推薦寫法（Python 3.5+）
C2 = np.dot(A, B)       # 傳統寫法
C3 = np.matmul(A, B)    # 等同於 @

print(C1)
# [[19 22]
#  [43 50]]

# shape 規則：(m, k) @ (k, n) → (m, n)
# A.shape = (2,2), B.shape = (2,2) → C.shape = (2,2)
```

- **轉置**：`A.T` 或 `A.transpose()`。在線性迴歸的正規方程 `w = (X^T X)^{-1} X^T y` 中，轉置是關鍵步驟。
- **常用 linalg 工具**：

```python
# 行列式
det = np.linalg.det(A)

# 逆矩陣（僅方陣且可逆時有效）
A_inv = np.linalg.inv(A)
print(A @ A_inv)  # 接近單位矩陣（因浮點精度不完全等於）

# 特徵值與特徵向量（PCA 的基礎）
eigenvalues, eigenvectors = np.linalg.eig(A)

# 解線性方程組 Ax = b
b = np.array([1, 2])
x = np.linalg.solve(A, b)

# 範數（向量長度）
v = np.array([3.0, 4.0])
print(np.linalg.norm(v))  # 5.0
```

- 對初學者最重要的是理解矩陣乘法的 shape 規則：`(m, k) @ (k, n) → (m, n)`。中間維度必須相同，這是 shape mismatch 最常見的來源。

**視覺建議：** 一張矩陣乘法的 shape 示意圖：兩個矩陣並排，標示 m、k、k、n 的對應關係，箭頭指向輸出矩陣的 shape (m, n)。旁邊附一個「常見 shape mismatch 錯誤」的解讀示範。

**轉場：** 「所有這些操作在 ML 工作流裡是如何串起來的？」

---

### S10 — NumPy 在 ML/DL 的實際角色

**核心主張：** NumPy 是 ML 工作流的共通貨幣，從特徵矩陣到模型權重，都以陣列形式流通。

**講師講解要點：**

- 一個典型的 ML 流程：載入資料 → 預處理 → 建立特徵矩陣 X（shape: `(n_samples, n_features)`）→ 建立標籤向量 y（shape: `(n_samples,)`）→ 送入模型訓練。X 和 y 幾乎永遠是 NumPy ndarray 或與其相容的格式。
- scikit-learn 的所有估計器（Estimator）都接受 NumPy 陣列作為輸入。`clf.fit(X, y)` 中的 X 就是一個 `(n_samples, n_features)` 的 ndarray。
- PyTorch 的 tensor 可以直接從 NumPy 陣列轉換：`torch.from_numpy(arr)`，且在 CPU 上共享記憶體（zero-copy）。PyTorch 的設計刻意與 NumPy 保持介面一致性。
- 深度學習的核心是矩陣乘法：每一層的前向傳播就是 `output = activation(W @ input + b)`。
- 工程意義：學會 NumPy 之後，你看 ML 框架的原始碼不再是天書。`(batch_size, seq_len, hidden_dim)` 這種三維 tensor 的 shape，就是 ndarray 概念的直接延伸。

**視覺建議：** 一張 ML 工作流管道圖，從「原始資料（CSV）」出發，標示每個節點的資料形態與工具：pandas DataFrame → NumPy ndarray（X, y）→ scikit-learn / PyTorch → model output。每個轉換箭頭上標示對應的程式碼（`.to_numpy()`、`torch.from_numpy()` 等）。

**轉場：** 「在進入練習之前，我們先看一個工具演進的里程碑。」

---

### S11 — 里程碑：NumPy 2.0 — 2006 年以來第一個 major release

**核心主張：** NumPy 2.0（2024 年發布）是 18 年來第一個 major version 升級，代表科學計算 Python 生態在成熟後仍保持演進的能力。

**講師講解要點：**

- NumPy 1.0 於 2006 年發布。此後 18 年都以 1.x 的形式發展，每個版本都保持嚴格的向後相容性。2024 年的 2.0 是一個明確信號：生態願意接受破壞性變更來提升品質。
- NumPy 2.0 的三個重要改動：
  1. 清理了大量已棄用的 API，移除長達 10 年的「deprecated 但沒刪」函式
  2. 提升 Python 類型標註的覆蓋率，讓 IDE 靜態分析更準確
  3. 字串類型的大幅改進，加入 `StringDType`，讓字串陣列效能大幅提升
- **對學習者的實際意義**：如果你搜尋到的教學使用了 `np.bool`、`np.int`、`np.float` 等裸型別名稱，那是 NumPy 1.x 的語法。在 2.0 中這些已被移除，應改用 Python 原生型別 `bool`、`int`、`float` 或 NumPy 特定型別如 `np.float64`。

| NumPy 1.x 舊語法 | NumPy 2.0 正確語法 |
|-----------------|-------------------|
| `np.bool` | `bool` 或 `np.bool_` |
| `np.int` | `int` 或 `np.int_` |
| `np.float` | `float` 或 `np.float64` |
| `np.complex` | `complex` 或 `np.complex128` |

- 工具有版本意識是工程師的基本素養。不要只學「如何用」，也要有能力識別「這是哪個版本的用法」。

**視覺建議：** 一條時間軸，從 2006 年的 NumPy 1.0 到 2024 年的 NumPy 2.0，中間標示幾個重要的 1.x 里程碑。右側用醒目框格標示 2.0 的三個主要改動。底部加上上方的 API 變更對照表。

---

## 六、練習設計

---

### 練習 1：ndarray 基礎操作與切片（S2-S4 結束後，25 分鐘）

**情境說明：**  
你正在準備一組學生成績資料，用於後續的機器學習實驗。需要完成一系列陣列操作，熟悉 NumPy 的基本工具。

**任務清單：**

1. 建立一個 shape 為 `(6, 5)` 的成績矩陣，使用 `np.random.default_rng(42).integers(60, 100, size=(6, 5))`，代表 6 名學生的 5 科成績
2. 查看陣列的 `shape`、`dtype`、`ndim`，並轉換型別為 `float32`
3. 取出第 0 名學生的所有成績（第 0 列）、所有學生的第 2 科成績（第 2 欄）
4. 取出前 3 名學生的後 3 科成績（子矩陣切片）
5. 找出所有低於 70 分的成績（布林切片），並統計有幾筆
6. 將低於 70 分的成績替換為 70（使用布林索引賦值）
7. 計算每位學生的總分與平均分（使用 `axis=1`），找出總分最高的學生（使用 `np.argmax`）
8. 用 `reshape` 將整個成績矩陣重塑為 `(1, 30)` 的一維格式，再重塑回 `(6, 5)`

**延伸思考：**  
`arr[mask] = 70` 這個操作修改了原始陣列。如果你想保留原始資料同時得到修改後的版本，應該怎麼做？（提示：`arr.copy()`）

**驗收標準：**
- 每個操作都能正確印出預期的 shape 與數值
- 能解釋 axis=0 vs axis=1 的方向差異
- reshape 操作前後元素總數一致（6×5 = 30）

---

### 練習 2：向量化與 Broadcasting（S5-S6 結束後，25 分鐘）

**情境說明：**  
你是一個機器學習工程師，需要從頭建立一個玩具版本的特徵矩陣，並用向量化操作完成所有預處理，不使用任何 for 迴圈。

**任務清單：**

1. 建立 shape 為 `(8, 4)` 的隨機浮點矩陣 X（使用 `np.random.default_rng(0).normal(size=(8,4))`），代表 8 個樣本、4 個特徵
2. 計算每個特徵（每欄）的均值與標準差，確認 shape 為 `(4,)`
3. 對 X 進行特徵標準化：`(X - X.mean(axis=0)) / X.std(axis=0)`，用向量化一行完成，不使用任何迴圈
4. 確認標準化後每欄的均值接近 0、標準差接近 1（使用 `np.allclose`）
5. 使用 `np.where(X_normalized > 0, X_normalized, 0)` 實作 ReLU 激活函式（負值歸零）
6. 計算 `X_normalized.T @ X_normalized`，說明結果的 shape 與這個計算在統計上的意義（共變異矩陣）
7. 用 `np.linalg.norm(X_normalized, axis=1)` 計算每個樣本的 L2 範數（歐氏長度）
8. **Broadcasting 練習**：建立一個 `(4,)` 的偏移向量 `bias = np.array([1.0, -1.0, 0.5, -0.5])`，將每個樣本加上這個偏移（不使用迴圈，驗證 shape 廣播正確）

**延伸思考：**  
特徵標準化在機器學習裡為什麼重要？當兩個特徵的數值範圍差距很大（例如年齡 20-60 vs 薪資 30000-100000），不標準化會對梯度下降產生什麼影響？

**驗收標準：**
- 整個練習沒有使用任何 for 迴圈
- 能正確解釋每個操作的 shape 變化
- `np.allclose` 驗證標準化結果通過

---

### 練習 3：統計計算與矩陣操作綜合實戰（S7-S9 結束後，35 分鐘）

**情境說明：**  
你需要模擬一份線性迴歸的資料集，並用 NumPy 的矩陣操作手動實作線性迴歸的正規方程（Normal Equation）求解，驗證結果。

**任務清單：**

**Part A：亂數資料生成與統計摘要**

1. 固定種子 `rng = np.random.default_rng(seed=2024)`
2. 生成 50 個樣本的特徵矩陣：`X_raw = rng.normal(loc=[5, 10, 3], scale=[2, 5, 1], size=(50, 3))`（3 個特徵，各有不同的均值與標準差）
3. 計算每個特徵的均值、標準差、最小值、最大值、第 25/50/75 百分位數，整理成一份摘要表（可以用 print 輸出）
4. 標準化 `X_raw` 為 `X`（每欄減均值除標準差）
5. 確認標準化後的均值接近 0、標準差接近 1

**Part B：手動線性迴歸**

6. 生成真實權重 `w_true = np.array([2.0, -1.5, 3.0])`，偏差 `b_true = 5.0`
7. 生成標籤：`y = X @ w_true + b_true + rng.normal(0, 0.5, size=(50,))`（加入少量噪聲）
8. 在 X 的左側加入全 1 欄位（偏差項）：`X_with_bias = np.hstack([np.ones((50,1)), X])`，確認 shape 為 `(50, 4)`
9. 用正規方程求解：`w_hat = np.linalg.inv(X_with_bias.T @ X_with_bias) @ X_with_bias.T @ y`
10. 印出估計的 `w_hat`，對比真實的 `[b_true, *w_true]`，說明為什麼估計值與真實值接近但不完全相同

**驗收標準：**
- 能正確生成具有指定分布的資料
- `np.hstack` 拼接後的 shape 正確
- 正規方程的計算不報錯，估計值合理（與真實值誤差在 0.3 以內）
- 能解釋噪聲的存在為何導致估計值不完全等於真實值

---

## 七、模組里程碑卡

---

```
里程碑 — NumPy 2.0（2024 年 6 月）

「NumPy 1.0 發布於 2006 年。
 此後整整 18 年，它以 1.x 的形式陪伴了整個機器學習崛起的時代。
 2024 年的 2.0 是第一個打破向後相容承諾的版本。
 科學計算社群願意為了更乾淨的 API 和更好的語意，承擔遷移成本。
 這本身就是一種成熟。」

關鍵數字：
- 18 年：1.0 到 2.0 的間隔
- 移除了 100+ 個已棄用 API
- StringDType 效能提升高達數倍
- 型別標註覆蓋率大幅提升

對你的意義：
搜尋到的舊教學可能用 np.bool / np.int / np.float
這些在 NumPy 2.0 已移除
認識工具的版本，和認識工具本身一樣重要
```

---

## 八、本模組結語

NumPy 不是 Python 資料分析的「前菜」，它是整個 AI/ML 生態的基礎語言。

你現在理解的每一個概念——shape、broadcasting、向量化——在你日後閱讀 PyTorch 原始碼、調試 scikit-learn 模型、理解 batch normalization 的實作時，都會再次出現。

下一個模組 M4 pandas 與資料清理，建立在 NumPy 的基礎上，把結構化表格資料（有欄名、有型別、有索引）帶入你的工具箱。

---

## 參考文獻與引用來源

### NumPy 官方資源
1. **NumPy 2.0.0 Release Notes (June 16, 2024)** — 自 2006 年 NumPy 1.0 以來首個 major release，經 11 個月開發、212 位貢獻者、1,078 個 PR。約 100 個主命名空間成員被棄用、移除或搬遷。[numpy.org/doc/stable/release/2.0.0-notes.html](https://numpy.org/doc/stable/release/2.0.0-notes.html)
2. **NumPy 2.0 Migration Guide** — 詳細的 API 變更對照表與自動遷移工具（Ruff 規則 NPY201）。[numpy.org/devdocs/numpy_2_0_migration_guide.html](https://numpy.org/devdocs/numpy_2_0_migration_guide.html)
3. **NumPy Official Documentation** — ndarray、broadcasting、dtype 完整說明。[numpy.org/doc/stable](https://numpy.org/doc/stable/)

### 效能數據說明
4. **ndarray vs list 效能差距** — 本課程引用的「50-100 倍速度差距」與「1/8 記憶體佔用」為教學用估算值，基於連續記憶體佈局（cache locality）與固定 dtype 帶來的優勢。精確數值依操作類型、資料規模與硬體而異。可用 `%timeit` 與 `sys.getsizeof()` 自行驗證。
5. **向量化 vs for 迴圈** — NumPy 向量化操作透過底層 C 實作與 SIMD 指令集加速，避免 Python 直譯器的逐元素開銷。效能差距在大陣列（> 10,000 元素）時最為顯著。

### 延伸閱讀
6. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media. — Chapter 2: Introduction to NumPy. 免費線上版：[jakevdp.github.io/PythonDataScienceHandbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
7. Harris, C.R. et al. (2020). "Array programming with NumPy." *Nature*, 585, 357-362. — NumPy 的學術論文，發表於 Nature。[doi.org/10.1038/s41586-020-2649-2](https://doi.org/10.1038/s41586-020-2649-2)
