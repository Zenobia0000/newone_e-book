# F3 — OOP 核心觀念與實例化｜講師講稿

> **課程時長**：1.5 小時（講授 60 min + 課堂練習 20 min + QA 10 min）
> **前置知識**：F2 Python 核心與資料結構（函式、list / dict、變數作用域）
> **後續銜接**：F4（封裝 / 繼承 / 魔術方法）、F5（DataCleaner 整合實戰）

---

## 1. 本節目標 (Learning Objectives)

完成本節後，學員應能：

1. 解釋資料工程採用 OOP 的三大效益（可重用 / 可測試 / 可組合），並辨識「何時不該用 class」。
2. 分辨 Class 與 Object（Instance）的差異，寫出第一個 `class`，使用 `__init__` 與 `self` 正確保存狀態。
3. 說出實例化 `pipe = DataPipeline("ETL")` 背後的三步驟：建空物件 → 呼叫 `__init__` → 綁名字。
4. 區分 Class Attribute 與 Instance Attribute，避開「可變預設值共享」這個 Python OOP 最常見 bug。
5. 設計最小的 `DataPipeline` 雛形（狀態 + 行為 + `return self`），為 F4 / F5 的 method chaining 鋪路。

---

## 2. 時間切分表

```
00:00-00:10  動機：ASK → VS → MATRIX → SILENT（為什麼要用 OOP）
00:10-00:25  概念：Class vs Object（S5）+ 最小類別（S6）
00:25-00:40  機制：實例化三步驟（S7）+ __init__/self 解剖（S8）+ self 三問 CP（S9）
00:40-00:55  狀態隔離：兩實例獨立驗證（S10）+ P3 陷阱（S11）+ 紅綠燈表（S12）
00:55-01:05  中段驗收 + P4 陷阱 + 反例「何時不該用」（S13-S15）
01:05-01:15  實戰雛形（S16）+ 課堂練習（S17，5 分鐘）
01:15-01:30  收束 + 銜接 F4 / F5（S18-S21）+ QA
```

---

## 3. 關鍵教學點 (Key Teaching Points)

1. **OOP 不是炫技，是管理狀態**：學員最容易誤解 OOP 是「程式碼好看」。要在 S2 的 VS 頁強調——兩邊都 100 行，差的不是行數，是「狀態住哪裡」。狀態在 global namespace → 改一處、擔心三處；狀態在 `self.xxx` → 實例化 N 次 = 獨立 N 條管線。

2. **實例化三步驟要背熟**：S7 的 EXAMPLE-I/O 三欄是本節骨架。`pipe = DataPipeline("ETL")` 背後 Python 做了：① 建一顆空 instance、② 呼叫 `DataPipeline.__init__(self=obj, name="ETL")`、③ 把 obj 綁到名字 `pipe`。這三步背熟，任何 class 都一樣流程，學生以後看陌生 class 不會怕。

3. **Class Attribute 的可變陷阱是 Python OOP 最常見 bug**：S11 要停下來現場 demo 一次。`class Bad: items = []` 看起來像每個實例獨立，實際上所有 instance 共享同一個 list——`a.items.append('x')` 會污染 `b.items`。鐵律：**list / dict / set 一律放 `__init__`，類別頂端只留不可變常數**。這條紀律不建立，F4 / F5 debug 會無止境。

4. **self 不是關鍵字，是慣例名**：S8 / S9 要說清楚——`self` 是 Python 把實例自動塞進方法的「第一個參數」，叫什麼名字理論上自由（PEP 8 規定叫 `self`）。學生真正的誤解是「省略 self 會不會自動加？」答案是不會，會直接 `TypeError`。S14 的 PITFALL 演示這個錯誤訊息。

5. **不是所有腳本都該 OOP（反例）**：S15 是本節平衡點。一次性腳本、純函式轉換、單一資料結構——用 function / dataclass / NamedTuple 更輕量。判斷準則：**有沒有跨方法共享的狀態 + 重複套用的需求？兩個都有再用 class**。這條是防止學生上完 F3 就把所有 function 改寫成 class 的解藥。

6. **`return self` 是本節留給 F5 的伏筆**：S16 的 `add_step` 加一行 `return self`，為 F5 的 `cleaner.read().clean().export()` 鋪路。學生當下不需要理解 method chaining，但看到 S20 銜接頁時會恍然大悟——今日的一行伏筆，就是明日的實戰骨架。

---

## 4. 學員常犯錯誤 (Common Pitfalls)

- **P1 · 過度設計**：為 30 行一次性腳本硬套 class，`__init__` 只存一個 `self.path`，之後所有方法都是 static-like——這是噪音，function 就夠了。
- **P2 · 忘記 `self.` 前綴**：`def __init__(self, name): name = name` 這行不會報錯，但 `self.name` 從未被賦值，之後 `pipe.name` 會 `AttributeError`。
- **P3 · 可變物件放類別頂端**：`class Bad: items = []` 會讓所有實例共享同一 list。**這是本節最關鍵的 bug**，實戰中一旦踩到，往往查半天才找到。
- **P4 · 省略 self 或亂改名**：`def __init__(name)` → 實例化時 `TypeError: __init__() takes 1 positional argument but 2 were given`。把 `self` 改成 `me` / `this` 雖然能跑，但違反 PEP 8，同事看了會翻白眼。
- **P5 · 方法不回傳 self**：`add_step` 忘記 `return self` → F5 無法 `.read().clean().export()` 串接，學生會抱怨「為什麼我的 chaining 爆炸」。

---

## 5. 提問設計 (Discussion Prompts)

1. 你拿到三家客戶的銷售資料，欄位名略有不同。用 function 寫（三個函式各自處理一家）還是 class 寫（實例化三次、傳不同 config）？各自的維護成本在哪？
2. `class Config: default = {}` 這個寫法為什麼會在多實例場景下踩雷？改成什麼版本才對？
3. 你看過的 Python 函式庫中（pandas / requests / scikit-learn），哪些設計讓你覺得 OOP 真的幫了忙？它們解決的「狀態」是什麼？

---

## 6. 延伸資源 (Further Reading)

- Python 官方 Tutorial §9 Classes（最精華的入門，官方寫得比大部分書好）。
- Python Data Model §3.3.1 Basic customization（`__init__` / `__new__` 的精確語意）。
- PEP 8 §Function and method arguments（為什麼 `self` 是慣例）。
- Martin Fowler, *Refactoring* §Encapsulate Record（何時該把散裝函式收進類別）。
- Ruff rule RUF012（靜態檢查 class attribute 是否誤用可變預設值）。

---

## 7. 常見 Q&A

**Q1：OOP 會不會讓簡單的事變複雜？**
A：會，如果你用在錯的場景。判斷準則就一條：**有沒有跨方法共享的狀態 + 重複套用的需求**？兩個都沒有就寫 function。F3 的核心不是「把所有東西改成 class」，是「知道什麼時候該用」。

**Q2：`__init__` 和其他語言的 constructor 有什麼不同？**
A：嚴格來說 `__init__` 不是 constructor，是 **initializer**（初始化鉤子）。真正建立物件的是 `__new__`（你現在不需要碰）。`__init__` 被呼叫時，物件已經存在，它只負責填屬性。這個區分在 F4 講 `@classmethod` / `@staticmethod` 時會再提。

**Q3：dataclass 和 class 差在哪？什麼時候用哪個？**
A：`@dataclass` 是 Python 3.7+ 的語法糖，自動產生 `__init__` / `__repr__` / `__eq__`。適合**純資料容器**（幾個欄位、少量行為）。本節講一般 class 是為了讓你理解底層；實戰若只是裝資料，`@dataclass` 更清爽。F4 會補充。

**Q4：為什麼 class 頂端的 `items = []` 會被所有實例共享？**
A：因為類別頂端的程式碼只在 class 定義時執行**一次**，那個 `[]` 從此就是固定那一顆 list 物件。所有實例透過 `self.items` 查找時，會沿著 attribute lookup 規則找到這同一顆。`__init__` 每次實例化都會執行，所以 `self.items = []` 才能每實例獨立。這條規則若沒記住，F5 的 DataCleaner 一定會踩雷。

**Q5：`self` 可以改成別的名字嗎？**
A：技術上可以（Python 沒檢查），但 PEP 8 明文規定用 `self`，所有 linter / IDE / 讀你 code 的人都預期是 `self`。改成 `me` / `this` 只會讓同事懷疑你不是 Python 背景出身。守慣例，不要標新立異。
