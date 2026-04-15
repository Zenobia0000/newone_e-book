# Ch02 · MVK 速學卡（Minimum Viable Knowledge）

> 下課前一頁要帶走的 5 件事。每項一句話定義 + 一個判準。

---

### 1. 容器選用 30 秒決策

**定義：** 選 List / Dict / Tuple / Set 的四題判準——要順序？要唯一？要查找？要不變？
**判準：** 寫下任一容器前，心裡默問這四題；若答不出為什麼選 List，多半該改 Set 或 Dict。

---

### 2. 變數 = 便利貼（name → object → value）

**定義：** Python 的 `a = b` 不是複製值，是把 a 這張便利貼貼到 b 指向的同一個 object。
**判準：** 看到 `a = b` 後 `b` 被修改、`a` 跟著變——這是正常的，不是 bug。

---

### 3. 可變 vs 不可變 與 hashable

**定義：** 不可變 = hashable = 能當 dict/set 的 key；可變（list/dict/set）不能當 key。
**判準：** 寫 `d[some_list] = ...` 會爆 TypeError；要當 key 請改 tuple 或 frozenset。

---

### 4. 淺拷貝 vs 深拷貝

**定義：** `list.copy()` / `copy.copy()` 只複製外殼，內層仍共用；`copy.deepcopy()` 連骨頭一起複製。
**判準：** 只要結構有「list of list」「dict of list」「物件含 mutable 成員」——一律 `deepcopy` 保命。

---

### 5. Generator = 記住現場的函式

**定義：** 用 `yield` 的函式呼叫時不執行，每次 `next()` 才算到下一個 yield 點，且局部變數被凍住；記憶體只裝當前一幀。
**判準：** 處理檔案 / 串流 / 管線資料，預設寫 `yield`；要一次全載入用 list comprehension，否則一律用 generator expression `()`。

---

## 一句話收束

> 會選容器，代表你能寫對；會用 generator，代表你能寫大。
