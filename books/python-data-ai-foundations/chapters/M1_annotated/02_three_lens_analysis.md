# M1 三視角分析 — First Principles / Fundamentals / Body of Knowledge

> **本文件定位：** 用三種不同知識論角度交叉檢視 M1「Python 基礎與資料思維」的內容完整度與理論基座。
> **讀者：** 課程設計者、技術 lead、對課程深度有高標要求的 reviewer。
> **使用情境：** 判斷教材是否「只教會了用法，沒教會原理」；判斷它與工業界知識體系（SWEBOK、DS-BoK）的對齊度；決定補強方向。

---

## Lens 1：First Principles — 不可再分的根本命題

從物理學式的第一性原理拆解 Python 與資料思維，找到「不能再問為什麼」的底層事實。

### 命題 1：Python 是 CPython 的語法糖皮層

- 使用者寫的 `.py` / `.ipynb` 只是表層文字。**真正在跑的是 CPython 把 source code 編譯成 bytecode，再由 eval loop（`ceval.c`）逐條 dispatch 執行**。
- 可用 `dis.dis(func)` 看任何函式的 bytecode。這一步讓「Python 慢」這件事有物理解釋：每條 bytecode 都要過 PyObject 的型別 dispatch。
- 推論：NumPy / pandas 的「向量化」本質是把 Python eval loop 外移到 C loop，這是 M3 效能論述的地基，M1 就該先埋伏。

### 命題 2：所有 Python 值都是 heap 上的 `PyObject*`

- Python 沒有「值型別」。`a = 1` 不是把 1 放進 a，是 a 這個 **名字（name）** 綁到 heap 上那個 `PyObject` 的指標。
- 所有變數皆指標，這解釋了：
  - 為什麼 `a = [1,2]; b = a; b.append(3)` 之後 `a == [1,2,3]`（a 和 b 綁同一個物件）。
  - 為什麼 `id(x) == id(y)` 可能 True（small int cache、string interning）也可能 False。
  - 為什麼函式參數是「pass by object reference」，既不是 pass by value 也不是 pass by reference。
- **name binding 不可再分**：Python 中「變數」這個詞應改稱「名字綁定」。`del x` 只刪名字不刪物件，物件靠 refcount + GC 回收。

### 命題 3：可變性（mutability）是物件的內稟屬性，不是變數的屬性

- `x = 1; x = 2`：看起來 x 變了，實際是 x 這個名字從綁 `1` 改綁 `2`，`1` 和 `2` 兩個物件都沒變（int 是 immutable）。
- `lst = [1]; lst.append(2)`：lst 這個名字沒變，是它指的 list 物件被 in-place 修改（list 是 mutable）。
- 所有「函式預設參數陷阱 / Jupyter 跨 cell 共享狀態 / dict 不能用 list 當 key」的現象，根源都是這條命題。
- **immutable = hashable 的必要條件**：因為 hash 在物件生命期內不能變。

### 命題 4：名字解析遵守 LEGB

- Local → Enclosing → Global → Built-in。這條規則說明為什麼 `def f(): print(df)` 在 Jupyter 能「魔法地」抓到上一個 cell 定義的 `df`。
- 這是 closure / 裝飾器 / 全域污染的統一解釋。

### 命題 5：資料是映射（mapping），不是表格

- 「表格」是展示層的 metaphor。底層每份結構化資料都是一組 **(key → value) 映射**：
  - 一列 = 一個 record = dict from column name to cell value
  - 一個 DataFrame = dict from column name to Series（欄式儲存）
  - pandas 是 **column-oriented**（所以 `df["col"]` 比 `df.iloc[row]` 便宜）
- 推論：tidy data 只是把「每一行是一個觀測、每一欄是一個變數」這條規範套到這個映射上。理解「資料 = 映射」就能跳脫 Excel 矩形格的思維，通往 JSON / document / graph。

### 命題 6：乾淨資料 = 滿足 schema 契約的資料

- 一份資料的 cleanness 不是絕對的，是 **相對於宣告的 schema / 業務契約**。沒有 schema 就沒有 clean 可言。
- 缺失 / 重複 / 離群 / 型態 錯誤四大污染，本質上都是 **「實際資料與 schema 契約不符」** 的四種面向。
- 這命題支撐整個 data contract / data quality 文獻。

### 命題 7：可重現性 = (同輸入 ⊕ 同程式 ⊕ 同環境) → 同輸出

- 三個「同」缺一不可。Excel 缺「同程式」（操作無紀錄），Python 裸跑缺「同環境」（套件版本漂移）。
- Notebook 還缺一個：**「同執行順序」**。hidden state 破壞此命題。
- `Restart & Run All` 是把執行順序規範化的唯一辦法。

---

## Lens 2：Fundamentals — Python 速學 checklist

資深工程師教新人時的最小可操作清單。不是完整 Python，是「能開始做資料分析」的 80/20。

### A. 容器四寶（不是六寶）


| 容器      | 序列性       | 可變  | 用途           | 底層                         |
| ------- | --------- | --- | ------------ | -------------------------- |
| `list`  | 有序        | 是   | 變長同質序列       | 動態陣列                       |
| `tuple` | 有序        | 否   | 定長異質 record  | 不可變陣列                      |
| `dict`  | 插入序（3.7+） | 是   | key→value 映射 | open-addressing hash table |
| `set`   | 無序        | 是   | 去重、O(1) 成員檢查 | hash table                 |


記憶口訣：**「序列用 list、記錄用 tuple、映射用 dict、去重用 set」**。M1 講義漏 set，checklist 要補。

### B. 流程四式（不是三式）

1. **分支**：`if / elif / else`；三元 `a if cond else b`
2. **迭代**：`for x in iterable`；配 `enumerate` / `zip`
3. **推導**：list / dict / set / generator comprehension
4. **例外**：`try / except / else / finally` ← **M1 沒教但資料清理必用**

### C. 函式設計五條軍規

1. **單一職責**：一個函式做一件事，名字就是這件事。
2. **輸入明確**：用 type hint，避免 `**kwargs` 黑箱。
3. **純度優先**：能不碰全域就不碰；能回傳就不 print。
4. **錯誤外顯**：失敗時 raise 或回傳 `None` / `NaN`，不要默默回 0。
5. **文件同步**：docstring 說「為什麼」，type hint 說「是什麼」，程式碼說「怎麼做」。

### D. Notebook 工作流三守則

1. **一個 cell 一件事**：想像每個 cell 是一個段落。
2. **Markdown 不可省**：每個程式 cell 之前，用 markdown 寫一句「為什麼要做這步」。
3. **交付前 Restart & Run All**：若 restart 後跑不過，這份 notebook 不能交付。

### E. import 三種寫法時機


| 寫法                    | 何時用                                     |
| --------------------- | --------------------------------------- |
| `import foo`          | 命名空間要清楚，或名字會衝突                          |
| `import foo as f`     | 套件約定有短名（`pd`, `np`, `plt`, `sns`, `tf`） |
| `from foo import bar` | 只要一兩個名字、且不會混淆                           |
| `from foo import *`   | **永不**（除了在 REPL 一次性探索）                  |


### F. 資料表達力五題自我檢測

1. 給你一份 CSV，你能五行內印出 shape / dtypes / 缺失值比例嗎？
2. 你能分辨 `NaN` 與 `None` 與空字串嗎？
3. 給一個 list of dict，你能用 comprehension 篩出 `amount > 1000` 的記錄嗎？
4. 你能寫一個函式，輸入 `"$1,200.50"`，輸出 `1200.50`，失敗時回傳 `None`（不是 0）嗎？
5. 你的 notebook 能 `Restart & Run All` 一次跑過嗎？

---

## Lens 3：Body of Knowledge — 與 SWEBOK / DS-BoK 對齊

從工業標準知識體系看 M1 的覆蓋率。

### 3.1 SWEBOK v3 — Knowledge Area: Software Construction

SWEBOK（IEEE Computer Society）v3 第 3 章 Software Construction 下有 **Fundamentals of Construction**，其中與 M1 對應的條目：


| SWEBOK 條目                     | M1 覆蓋         | 差距                              |
| ----------------------------- | ------------- | ------------------------------- |
| Minimizing Complexity         | 部分（函式化）       | 沒談 cyclomatic complexity / 巢狀深度 |
| Anticipating Change           | 無             | M1 沒談到「為未來改變留空間」                |
| Constructing for Verification | 無             | **完全沒教 assert / test**          |
| Standards in Construction     | 部分（PEP 8 提一句） | 沒講 type hint / docstring 規範     |
| Coding                        | 有             | 基本覆蓋                            |
| Construction Testing          | 無             | 缺 unit test 入門                  |
| Reuse                         | 有（函式、import）  | 基本覆蓋                            |


**評估**：M1 落在 SWEBOK 的 Coding + Reuse 兩格，**Construction for Verification / Testing 完全缺席**。補救建議：S09 或 S11 加 30 秒 assert 範例；S12 明確承認「測試留給 M5」。

### 3.2 SWEBOK — Programming Fundamentals（Computing Foundations 章）


| 條目                                 | M1 覆蓋                               |
| ---------------------------------- | ----------------------------------- |
| Problem Solving Techniques         | 隱含於 workshop A / B                  |
| Abstraction                        | 有（函式）                               |
| Programming Fundamentals           | 有（型態、容器、流程）                         |
| Data Structure and Representation  | **部分**，list/dict/tuple 有講，但沒談複雜度、底層 |
| Algorithms and Complexity          | **無**                               |
| Basic Concepts of a System         | 無（合理，M6 才談）                         |
| Computer Organization              | 無（M6）                               |
| Parallel and Distributed Computing | 無（M7）                               |


### 3.3 Data Science Body of Knowledge (EDISON DS-BoK) — Data Wrangling

EDISON Data Science Framework（EU, 2017）把 Data Science 知識體系分九區，M1 高度對應 **DSDM（Data Science Engineering）** 下的 Data Wrangling / Data Munging 子領域：


| DS-BoK Data Wrangling 條目                            | M1 覆蓋                             |
| --------------------------------------------------- | --------------------------------- |
| Data Acquisition                                    | 無（只假設 CSV 已存在）                    |
| Data Parsing（含 encoding / format）                   | **部分**，只提 CSV，沒談 encoding         |
| Data Cleaning（missing / duplicate / outlier / type） | **有**（S03 四類污染）                   |
| Data Transformation（normalize / encode / aggregate） | 無（M3 / M4）                        |
| Data Validation（schema / constraint / contract）     | **部分**，schema 提了但沒教驗證             |
| Data Profiling（descriptive stats）                   | 部分（workshop B 的 describe_dataset） |
| Data Integration（merge / join / resolve）            | 無（M3）                             |
| Provenance / Lineage                                | 無                                 |
| Reproducibility                                     | **有**（S04 Excel vs Python）        |


**評估**：M1 在 DS-BoK 拿到 **Data Cleaning + Reproducibility 兩格滿分，Profiling 半格，其餘 Acquisition / Validation / Integration 都是零或預告**。對 3 小時的入門模組來說合理，但 **Data Validation（schema check）是一個低成本高回報的補強點**，加一張投影片示範 `assert df.dtypes["amount"] == "float64"` 就有感。

### 3.4 ACM CS2023 Curriculum — Foundations of Programming Languages

ACM CS2023（最新版）強調 **「type system」與「semantic model」** 比語法更基礎。M1 的落差：

- Python 是 **dynamic, strongly typed**，但教材一次都沒用這個詞。學員會以為 Python「沒有型態」。
- **duck typing** 的概念在 workshop B 的 `describe_dataset(df)` 已在用（不檢查 df 是不是 DataFrame，只要它有 `.shape` / `.dtypes` 就跑），但沒點名。

補救建議：S07 一句話帶過「Python 是動態強型別，型別屬於物件不屬於變數」，就能對齊 ACM 標準。

---

## 三視角合流建議

### 合流觀察


| 視角                   | 看到的事實                                                | 對 M1 的評語                                                          |
| -------------------- | ---------------------------------------------------- | ----------------------------------------------------------------- |
| First Principles     | Python = CPython + PyObject + name binding；資料 = 契約映射 | **缺**：可變性主軸、name binding 心智模型、schema 契約語言                         |
| Fundamentals         | 容器四寶、流程四式、函式五軍規、Notebook 三守則                         | **缺**：`set`、try/except、assert、Restart & Run All 明確訓練              |
| BoK（SWEBOK + DS-BoK） | Coding / Reuse / Cleaning / Reproducibility 覆蓋       | **缺**：testing、validation、parsing（encoding）、algorithmic complexity |


### 三條補強軸（優先序）

**第一優先（低成本高回報，建議併入 M1）：**

1. **S07 加「可變 vs 不可變」總表一張**（First Principles 合 Fundamentals）
2. **S09 加 type hint 專屬說明 30 秒**（Fundamentals 合 BoK 的 standards）
3. **Workshop B 加一行 `assert`**（BoK 的 verification 合 Fundamentals 軍規 4）
4. **明確把 `set` 加入容器清單**（Fundamentals 的容器四寶合 BoK 的 data structures）

**第二優先（中成本，可考慮擴充到 3.5 小時）：**
5. **S05 誠實加一頁 Notebook 黑暗面**（First Principles 的命題 7）
6. **S08 補 try/except 與 generator 各一張**（Fundamentals 的流程四式）
7. **Workshop B 的 `clean_amount` 改用 `pd.to_numeric(errors="coerce")`，並示範錯誤外顯**（軍規 4）

**第三優先（留待 M5 / 外讀）：**
8. 複雜度（時間 / 空間）、bytecode、GC、GIL、套件管理、測試框架、schema validation 工具（pandera / great_expectations）。

### 一句總評

> **M1 在 Fundamentals 上 80 分、在 Body of Knowledge 上 60 分、在 First Principles 上 40 分。** 補強方向不是加廣度（更多語法），而是把「可變性 / 型別 / 契約 / 可重現性」四條第一性主軸明確抽出來，讓每個 Fundamentals 條目都能掛上一條 First Principles 的錨點。

