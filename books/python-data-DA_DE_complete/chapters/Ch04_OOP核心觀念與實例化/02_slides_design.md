# F3 — OOP 核心觀念與實例化｜Slides Design

> 21 張內容投影片（封面 + 21 + 版權）｜教學型七原型為主
> 對齊 `01_outline.md` 的 5 個 Learning Objectives × 5 個 Common Pitfalls
> 配色：主色 `#1B5E3F` + 錯誤紅 `#C62828`（僅 PITFALL 頁）+ 成功綠 `#2E7D32`
> 2 張銜接導引：S18 → F4、S20 → F5

---

## S1 · ASK — 複製貼上第四次

- 🖼️ 畫面：全白底 / 大字痛點問句 / 右下一張資料卡（61%）
- 📣 畫面上的字：
  - 標題：「為什麼同一段清洗邏輯，你已經複製貼上第四次？」
  - 資料卡：`資料工程師日常 · 61% · 每週維護 ≥ 3 條結構相似的管線`
- 🎙️ 講者這時說：「今天開始之前先問：你手邊多少支 Python 腳本，長得八成像？讀檔、清欄名、補遺失值、匯出——這套流程你每週做幾次？複製貼上不是你懶，是沒有把狀態封裝起來的代價。這節課要把『重複貼』換成『重複實例化』。」

---

## S2 · VS — 腳本式 vs 類別式

- 🖼️ 畫面：雙欄對照 / 左標題「腳本式」右標題「類別式」/ 中央 delta「狀態\n的歸屬」/ 底部 summary
- 📣 畫面上的字：
  - 左：5 個散落的函式 / 10 個全域變數 / 狀態在 global namespace / 改一處擔心三處 / 單元測試難寫
  - 右：1 個 DataPipeline 類別 / 狀態收進 self.xxx / 行為封裝成方法 / 實例化 N 次 = 管線複製 N 條 / 測試 < 10 行
  - Summary：「兩邊都 100 行，但維護成本差 10 倍——因為狀態的可見性不同。」
- 🎙️ 講者這時說：「注意看中間那塊『狀態的歸屬』。腳本式把 10 個變數攤在全域，改一個要擔心另外三個；類別式把狀態收進 `self.xxx`，一個實例就是一條完整、獨立的管線。差的不是行數，是**誰擁有狀態**。」

---

## S3 · MATRIX 1×3 — 三大效益

- 🖼️ 畫面：三欄矩陣 / 左欄 highlight 主打「可重用」
- 📣 畫面上的字：
  - 可重用：清洗邏輯寫一次 / 套到 N 個資料集 / 實例化 = 複製管線
  - 可測試：小單元獨立驗證 / pipe.add_step() 可 mock / 單元測試 < 10 行
  - 可組合：管線各步驟可替換 / 換資料源不改邏輯 / F5 method chaining 基礎
- 🎙️ 講者這時說：「三大效益背後都指向一個詞——**降耦**。耦合度越低，你改一個地方其他地方越不會爆。OOP 不是為了『面向對象』這個詞好聽，是為了降耦。」

---

## S4 · SILENT — 立論

- 🖼️ 畫面：全綠底 / 白色 HERO 大字置中
- 📣 畫面上的字：「腳本解決問題，類別解決規模。」
- 🎙️ 講者這時說：「這節課若只能記一句話，就是這句。腳本寫得快、好懂、一次性——它解決**問題**。類別慢一點、要設計、可以複製——它解決**規模**。你今天要不要用 class，就看你的問題有沒有規模這個維度。」

---

## S5 · CONCEPT-CARD — Class vs Object

- 🖼️ 畫面：左欄文字（類比 + 術語對照）+ 右欄圖（class 定義 vs 三個 instance 實體方塊）
- 📣 畫面上的字：
  - 標題：「Class 是建築藍圖，Object 是蓋出來的房子」
  - 左欄：一份 class → N 個 instance / Class 是定義模板 / Object 是執行期的實體 / 術語對照表
  - 右欄：class 原始碼 + 三個記憶體方塊示意圖（pending real image）
- 🎙️ 講者這時說：「這是唯一一次用生活類比——藍圖 vs 房子。一份藍圖蓋出三棟房子，結構一樣、門牌地址各自獨立。回到程式：一份 class 可以實例化成三個 instance，方法與屬性名由 class 決定，但每個 instance 的屬性**值**各自獨立。接下來我們都用 Class / Instance / Attribute / Method 這幾個詞，不再講房子。」

---

## S6 · CODE — 最小類別

- 🖼️ 畫面：全寬 code panel + 右側 5 個 bullet 標註
- 📣 畫面上的字：
  - 標題：「最小類別：三個關鍵字 + 兩個方法，比 5 個散落函式好用」
  - Code：class DataPipeline + `__init__(self, name)` + `self.name` / `self.steps = []` + `add_step`
  - Bullets：class 宣告類別 / `__init__` 初始化鉤子 / self 當前實例參照 / add_step 行為 / pipe 是 instance
- 🎙️ 講者這時說：「這就是你今天要帶走的最小骨架。七行程式 + 三個實例化操作。注意兩件事：`self.steps = []` 放在 `__init__` 裡——這決定了實例能不能獨立，等下 S11 會示範為什麼。另外 `self.name` 前綴一定要寫，漏了就是 P2 陷阱。」

---

## S7 · EXAMPLE-I/O — 實例化三步驟

- 🖼️ 畫面：三欄橫排（輸入 → 過程 → 產出）+ 下方 bottom_note
- 📣 畫面上的字：
  - ①輸入：`pipe = DataPipeline("ETL_v1")` / 使用者只寫一行 / 看起來像呼叫函式
  - ②過程：建立空 instance obj / 呼叫 `__init__(self=obj, ...)` / 執行 `self.name = ...`
  - ③產出：obj 綁到 pipe / `pipe.name == 'ETL_v1'` / `pipe.steps == []`
  - Bottom：「三步背熟 → 任何 class 的實例化都一樣流程；不是黑魔法，是固定劇本。」
- 🎙️ 講者這時說：「背熟這三步，以後看任何陌生的 class 你都不會怕。Python 做的事永遠是：建空殼 → 把空殼塞進第一個參數跑 `__init__` → 把殼綁到等號左邊的名字。一致、可預測、無魔法。」

---

## S8 · CODE — `__init__` / self 解剖

- 🖼️ 畫面：全寬 code panel + 右側 4 個 bullet
- 📣 畫面上的字：
  - 標題：「__init__ 是初始化鉤子，self 是當前實例參照——都是慣例，不是關鍵字」
  - Code：正版 `__init__(self, name)` + 反例 `__init__(me, x)` + 方法呼叫翻譯 `pipe.add_step("x")` → `DataPipeline.add_step(pipe, "x")`
  - Bullets：`__init__` 不是建構子是初始化鉤子 / self 由 Python 自動傳入 / self 是 PEP 8 慣例 / 省略 self → TypeError
- 🎙️ 講者這時說：「注意我強調『不是關鍵字』——`__init__` 和 `self` 都只是慣例。理論上改成 `me` 可以跑，但 linter、IDE、你的同事都預期看到 `self`。守慣例，不要標新立異。重點在底下那段翻譯：`pipe.add_step("x")` 其實是 `DataPipeline.add_step(pipe, "x")`——實例被自動塞進第一個參數。理解這條，self 的存在就不神秘了。」

---

## S9 · CHECKPOINT — self 三問

- 🖼️ 畫面：三欄 Matrix / 左欄 highlight
- 📣 畫面上的字：
  - Q1：誰傳進來？ — Python 自動把當前實例塞進第一個參數
  - Q2：指到哪？ — 指到那一顆 instance，`self.name = ...` 就是寫入這顆物件
  - Q3：不寫會怎樣？ — TypeError，或被誤判為 classmethod
- 🎙️ 講者這時說：「停下來——不看投影片，用自己的話答這三題。誰？哪？不寫怎樣？答得出來再往下；答不出來翻回 S8。self 三問背熟，OOP 一半的焦慮就沒了。」

---

## S10 · CODE — 兩實例獨立驗證

- 🖼️ 畫面：左圖（記憶體示意，pending real image）+ 右 code panel
- 📣 畫面上的字：
  - 標題：「兩個實例各自的 steps，互不污染——記憶體才是真相」
  - 左：p1 / p2 兩方塊各自指向獨立 steps list
  - 右 Code：`p1 = DataPipeline("ETL_A")` / `p2 = DataPipeline("ETL_B")` / 各自 add_step / `p1.steps is p2.steps → False`
  - Bullets：每次 `__init__` 都建新 list / 不同記憶體 / 實例獨立的根基
- 🎙️ 講者這時說：「`is` 不是 `==`——`is` 問的是『兩個名字是不是指到同一顆物件』。這裡 False 證明 p1 和 p2 的 steps 是兩塊獨立的記憶體。這就是『實例獨立』四個字的真正意思。接下來 S11 要看的是，**為什麼**每次 `__init__` 都要重建這顆 list。」

---

## S11 · PITFALL (P3) — 可變 Class Attribute

- 🖼️ 畫面：VS 左紅「✗」右綠「✓」+ 下方 primary 色 why 條
- 📣 畫面上的字：
  - 左錯：`class Bad: items = []`（類別頂端）→ `a.items.append('x')` → `b.items == ['x']` 被污染
  - 右對：`class Good: def __init__(self): self.items = []`（每實例獨立）
  - Why：「類別頂端只在 class 定義時執行一次；`__init__` 每次實例化都重建 → list/dict/set 必須放 `__init__`」
- 🎙️ 講者這時說：「這是 Python OOP **最常見**的 bug——連 5 年經驗的工程師都會踩。記住這條鐵律：**list / dict / set 一律放 `__init__`，類別頂端只留不可變常數**。為什麼？因為類別頂端的 `[]` 只被創造一次，所有實例共享那顆 list；`__init__` 每次都重跑，才會每實例一顆新 list。這條不建立，F5 的 DataCleaner 你一定會爆。」

---

## S12 · TABLE — Class Attribute 紅綠燈

- 🖼️ 畫面：全寬 editorial table / 6 列 / 4 欄
- 📣 畫面上的字：
  - 標題：「Class Attribute 的紅綠燈：只給不可變物件用」
  - OK 列：常數 `PI=3.14159` / 預設字串 `DEFAULT_ENCODING="utf-8"` / 版本號 `VERSION="1.0"`
  - 禁列：list `items=[]` / dict `cache={}` / set `seen=set()`
- 🎙️ 講者這時說：「這張表拍照存起來——決定 class attribute 能不能用，就看它是不是不可變 (immutable)。int / float / str / tuple 可以；list / dict / set 永遠是 bug。Ruff 有條規則 RUF012 會自動檢查，建議把它加進 CI。」

---

## S13 · CHECKPOINT — 中段驗收

- 🖼️ 畫面：三欄 Matrix / 左欄 highlight
- 📣 畫面上的字：
  - Q1 · 可變放哪？：`self.cache = {}` 放 `__init__` 還是類別頂端？
  - Q2 · 共享會怎樣？：`class Bad: items=[]` 兩實例 append 後 shape 長怎樣？
  - Q3 · 哪些可以放頂端？：`VERSION='1.0'` / `PI=3.14` / `DEFAULT_CONF={}`，三選二，哪個不行？
- 🎙️ 講者這時說：「30 秒口頭答——答得出來我們就往下走 P4 陷阱；答不出來先回 S10-S12 翻一遍。不要急著看下一頁，這三題是進入 F4 前的最後閘門。」

---

## S14 · PITFALL (P4) — 省略 self

- 🖼️ 畫面：VS 左紅右綠 + why 條
- 📣 畫面上的字：
  - 左錯：`def __init__(name)` → `TypeError: __init__() takes 1 positional argument but 2 were given`
  - 右對：`def __init__(self, name): self.name = name`
  - Why：「Python 呼叫方法時會自動把實例塞進第一個參數；沒 self 接 → 參數數量對不上 → TypeError」
- 🎙️ 講者這時說：「錯誤訊息『takes 1 but 2 were given』是經典——你寫 `Pipeline('ETL')` 只傳一個參數，為什麼說 2 個？因為 Python 把實例自己也算進去。看到這個錯誤訊息，直接檢查 `def __init__(...)` 第一個參數有沒有寫 `self`。」

---

## S15 · CONCEPT-CARD — 何時「不」該用 OOP

- 🖼️ 畫面：雙欄 / 左紅標✗「不該用」右綠標✓「該用」/ 底部 primary 色判斷準則
- 📣 畫面上的字：
  - 左不該用：① 一次性腳本 ② 純函式式轉換 ③ 單一資料結構 + 少量操作（dataclass / NamedTuple 更輕量）
  - 右該用：① 狀態跨方法共享 ② 同一組邏輯套到多個資料集 ③ 需要 method chaining / 可替換步驟
  - 底：「判斷準則：有沒有『跨方法共享的狀態』＋『重複套用的需求』？兩個都有 → 用 class；只有一個 → function 即可。」
- 🎙️ 講者這時說：「這頁是本節的平衡點——避免你上完 F3 就把所有 function 改成 class。反例：一次性匯出當月報表的 50 行腳本，寫 class 是噪音。正例：三家客戶格式略不同，要套同一套清洗邏輯，這才值得 OOP。判斷準則就一條，兩個都符合再動手。」

---

## S16 · CODE — DataPipeline 完整雛形

- 🖼️ 畫面：全寬 code panel + 5 個 bullet
- 📣 畫面上的字：
  - 標題：「DataPipeline 雛形：F3 的終點，F5 的起點」
  - Code：完整 class + `__init__` + `add_step(self, step): self.steps.append(step); return self` + `run(self, data)`
  - 使用：`pipe.add_step(str.strip).add_step(str.lower)` / `pipe.run("  HELLO ")` → `'hello'`
  - Bullets：狀態 name/steps / 行為 add_step/run / `return self` → chaining / F4 加繼承+魔術方法 / F5 擴成 DataCleaner
- 🎙️ 講者這時說：「注意 `add_step` 最後一行 `return self`——現在你可能覺得多此一舉，但這是留給 F5 的伏筆。一旦 `return self`，你就能 `pipe.add_step(...).add_step(...)` 串起來，這就是 pandas / scikit-learn 的 chaining 風格。S20 會把這條伏筆接起來。」

---

## S17 · PRACTICE-PROMPT — Student 類別

- 🖼️ 畫面：白底 / 標題 + 難度標籤 + 任務敘述 + 底部 emphasis pill
- 📣 畫面上的字：
  - 難度：🟡 核心題 · 容易 · 鞏固 LO3 / LO4 / LO5
  - 情境：三家客戶銷售資料格式略不同 → 用 function 還是 class？各自成本？
  - 任務：寫 Student 類別 — 屬性 name / scores (放哪裡？) / 方法 add_score / average
  - 驗收：兩個 Student，互不污染
  - 思考題：改成「三家客戶平均客單價」，這類別改幾行就能重用？
  - Pill：「Think · Pair · Share — 5 分鐘後對答案」
- 🎙️ 講者這時說：「五分鐘——現在打開 Notebook。兩個重點：`scores` 放哪裡（`__init__` 還是類別頂端），這題是檢驗你有沒有記住 P3 陷阱。第二個思考題才是精華——同一個類別怎麼從『學生成績』改幾行就變『客戶客單價』？這就是**可重用**三個字的真正意義。」

---

## S18 · SILENT — 銜接 F4 預告

- 🖼️ 畫面：全綠底 / 白色 HERO 大字 + 底部白色細字列出 F4 三個主題
- 📣 畫面上的字：
  - 主句：「懂了藍圖，下一步是學會美化它。」
  - 底部：「F4 · 封裝 (property) ｜ 繼承 (is-a 關係) ｜ 魔術方法 (`__repr__` / `__eq__` / `__len__`)」
- 🎙️ 講者這時說：「你今天會的是『定義一個類別』。F4 要教的是『擴充與美化這個類別』——封裝把內部細節藏起來、繼承讓 SalesPipeline 直接拿 DataPipeline 的功能、魔術方法讓你的類別能被 `print()` / `==` / `len()` 這些 Python 原生語法使用。下節見。」

---

## S19 · PYRAMID — 收束

- 🖼️ 畫面：PYRAMID 兩層 blocks + 底部 inverted thesis box
- 📣 畫面上的字：
  - 上層「四個關鍵詞」：Class / Object (Instance) / `__init__` / self 各一行定義
  - 下層「三章銜接線」：F3 class+__init__+self (今日) → F4 封裝/繼承/魔術方法 → F5 DataCleaner().read().clean().export()
  - Thesis：「先搞懂狀態住哪，才配談設計——F4 延伸封裝、繼承與魔術方法；F5 擴成實戰 DataCleaner。」
- 🎙️ 講者這時說：「收束。四個關鍵詞拍照存起來：class 是定義模板、instance 是執行期實體、`__init__` 是初始化鉤子、self 是當前實例參照。三章銜接線提醒你——F3 / F4 / F5 是一條接力，今天的地基決定後面能蓋多高。」

---

## S20 · CONCEPT-CARD — 銜接 F5 DataCleaner

- 🖼️ 畫面：雙欄左右對照 / 左標 primary 色「F3 雛形」右標綠色「F5 實戰」/ 底部 primary 色 takeaway
- 📣 畫面上的字：
  - 左 F3：DataPipeline 最小骨架（`__init__` / `add_step` / `run`）
  - 右 F5：`cleaner = DataCleaner("sales.csv")` → `.read().drop_duplicates().fill_missing(...).export(...)` + 註解「今日的 `return self` 就是明天的 chaining」
  - 底：「沒有 F3 的三個關鍵詞，F5 的 method chaining 都只是抄語法；會了 F3，F5 只是把規模做大。」
- 🎙️ 講者這時說：「這頁把今天和兩週後接起來——左邊是你今天會的雛形，右邊是 F5 你要寫出來的實戰。差別看起來很大，但骨架一樣：`self.xxx` 存狀態、方法改狀態、`return self` 串起來。今天的一行伏筆，就是那時的實戰骨架。」

---

## S21 · SILENT — 過渡

- 🖼️ 畫面：全綠底 / 白色 HERO 大字
- 📣 畫面上的字：「先搞懂狀態住哪，才配談設計。」
- 🎙️ 講者這時說：「最後一句——先搞懂狀態住哪，才配談設計。今天你把 class / `__init__` / self 這條鏈接起來，F4 / F5 就只是往上疊東西。下課十分鐘。」

---

**節奏檢查**：
- 動機（S1-4） → 概念（S5-6） → 機制（S7-8） → 檢核（S9） → 狀態隔離（S10-12） → 檢核（S13） → 陷阱（S14） → 反例（S15） → 實戰（S16） → 練習（S17） → 銜接 F4（S18） → 收束（S19） → 銜接 F5（S20） → 過渡（S21）
- 2 個 PITFALL 頁（S11 P3 / S14 P4）對應 teacher_notes §4 最關鍵的兩個 bug
- 2 個 CHECKPOINT（S9 / S13）落在 9/13 位置，符合 T10「每 5 張插一次」
- 2 個銜接導引（S18 → F4、S20 → F5）落在實戰後，符合教學型守則「銜接明確指向下章」
- 字級：所有 body ≥ 14pt（FONT_CAPTION 以上）
