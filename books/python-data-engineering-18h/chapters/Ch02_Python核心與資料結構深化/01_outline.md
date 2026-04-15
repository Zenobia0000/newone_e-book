# Chapter 2：Python 核心快速複習與資料結構深化

**模組：** M1 系統前導與 Python 機制  
**時數：** 1.5 小時  
**前置知識：** 變數、條件、迴圈、函式  
**後續銜接：** Ch3（特殊函式）、Ch6（大檔分塊讀取）

---

## 一、章節定位

學員已具備基本語法，本章不重複教學，而是：
1. 用 30 分鐘**校準**所有人到同一基準
2. 用 60 分鐘**深化**容器選用直覺與 Iterator/Generator —— 後者是大檔處理的關鍵

---

## 二、學習目標

完成本章後，學生能夠：

1. 在 30 秒內判斷該用 List / Dict / Tuple / Set 中的哪一個
2. 解釋可變 vs 不可變的差異，避開淺/深拷貝陷阱
3. 用 Generator 處理「大於記憶體」的資料流
4. 解釋 `yield` 與 `return` 的差別

---

## 三、章節結構

### 2-1. 語法快速校準（30 分鐘）
- 型別系統：int / float / str / bool / None
- 控制流：if-elif-else、for / while、break / continue
- 函式定義：`def`、return、預設參數
- import 機制與標準函式庫一覽
- **快速練習**：用一個迷你題目（讀數字 → 篩選 → 加總）確認所有人在線

### 2-2. 容器深化：選用直覺（30 分鐘）
| 容器 | 何時用 | 關鍵操作 | 時間複雜度 |
|------|--------|---------|-----------|
| List | 順序資料、可重複 | append、index | O(1) append, O(n) search |
| Tuple | 不可變、固定欄位 | 解構 | 同 list 但不可變 |
| Dict | key-value 查找 | get、items | O(1) 平均查找 |
| Set | 去重、集合運算 | add、union、& \| - | O(1) 平均查找 |

- 可變 vs 不可變：哪些可作為 Dict key
- **淺拷貝 vs 深拷貝**：`list1 = list2` 與 `copy.deepcopy` 的踩坑示範
- **真實情境**：為何巢狀 list 用 `.copy()` 還是會出問題

### 2-3. Iterator 與 Generator（30 分鐘）
- Iterator 協議：`__iter__` 與 `__next__`
- Generator 函式：`yield` 的暫停 / 續行語意
- Generator Expression：`(x*2 for x in range(10))` vs List Comprehension
- **實戰範例**：
  ```python
  # 不會 OOM 的大檔處理
  def read_large_file(path):
      with open(path) as f:
          for line in f:
              yield line.strip()
  ```
- **呼應 Ch1**：為何這種寫法不會載入整個檔案到 RAM

---

## 四、課後練習

1. **觀念題**：為何 `dict` 的 key 不能用 list？
2. **除錯題**：給定一段使用 `[[]] * 3` 的程式，解釋為何修改一個元素會影響全部
3. **實作題**：寫一個 generator，逐行讀取 1GB 的 log 檔，並只回傳含 "ERROR" 的行

---

## 五、銜接下一章

學會了「資料如何儲存與迭代」，Ch3 將學習「如何用簡潔語法操作這些資料」—— Lambda、map/filter、Comprehension，為 Ch8 的 Pandas `apply` 預作準備。
