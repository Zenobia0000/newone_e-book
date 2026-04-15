# F4 — 封裝、繼承與魔術方法｜Slides Design

> 20 張內容投影片（封面 + 20 + 版權）｜教學型七原型為主
> 對齊 `01_outline.md` 的 4 個 Learning Objectives × 5 個 Common Pitfalls
> 配色：主色 `#1B5E3F` + 錯誤紅 `#C62828`（僅 PITFALL 頁）+ 成功綠 `#2E7D32`

---

## F4-S1 · ASK — code review 退件第一名

- 🖼️ 畫面：白底 / 大字痛點問句 / 右下資料卡（#1 退件原因）
- 📣 畫面上的字：
  - 「為什麼資深工程師的 class，很少直接 `obj.field =` 改值？」
  - 卡片：code review 常見退件 · #1 · 直接改內部欄位
- 🎙️ 講者這時說：「先把這個問題放著。你如果去看過任何一個成熟團隊的 Python code review，『直接改別人 class 的內部欄位』是第一名被打回的原因。今天這節課就是在回答——他們擋的到底是什麼。」

---

## F4-S2 · SILENT — 立論一句

- 🖼️ 畫面：全綠底、白色 HERO 大字置中
- 📣 畫面上的字：「類別要守門，不是把變數塞在一起。」
- 🎙️ 講者這時說：「一句話立論。class 不是『幫你把相關變數放在一起』的容器——那樣 dict 或 dataclass 就夠了。class 存在的意義是『守門』：誰能讀、誰能改、改的時候要滿足什麼條件。」

---

## F4-S3 · CONCEPT-CARD — 封裝三道門（使用時機）

- 🖼️ 畫面：2×2 matrix，四格各一門
- 📣 畫面上的字：
  - `x`：時機——穩定、無驗證需求
  - `_x`：時機——內部用，不強制（linter 警告）
  - `__x`：時機——避免子類意外覆蓋
  - `@property`：時機——需要驗證／計算／未來換實作
- 🎙️ 講者這時說：「這頁你只要記一件事——**三道門，各有使用時機**。不是『底線越多越安全』。需要驗證就 `@property`；只是想提醒『這是內部用』就 `_x`；只有在你怕子類命名衝突時才用 `__x`。」

---

## F4-S4 · EXAMPLE-I/O — `_x` / `__x` 實測

- 🖼️ 畫面：左側 code panel（`Account` 類）+ 右側 4 條要點
- 📣 畫面上的字：
  - `a._hint` 拿得到；`a.__secret` 報錯；`a._Account__secret` 又拿到了
  - 四個 bullet：`_x` 是約定 / `__x` 被改名 / 本意是避免覆蓋 / 不是加密
- 🎙️ 講者這時說：「實測。單底線 Python 根本不阻止你存取——只是 linter 會警告。雙底線看起來神秘，其實只是 Python 偷偷把它改名叫 `_Account__secret`。你知道新名字，照樣拿得到。所以記住：`__x` 是**提示**，不是**鎖**。」

---

## F4-S5 · EXAMPLE-I/O — `@property` 真實用途

- 🖼️ 畫面：左側 code panel（`Temperature` 類，celsius setter + fahrenheit 唯讀）+ 右側 4 條要點
- 📣 畫面上的字：
  - `t.celsius = 25` 看起來是欄位，其實會跑驗證
  - `t.fahrenheit` 看起來是欄位，其實是計算
  - 未來換實作 → 呼叫端零改動
- 🎙️ 講者這時說：「看這個溫度類。`t.celsius = 25` 在呼叫端看起來就是賦值——但裡面會檢查絕對零度。`t.fahrenheit` 看起來也是欄位，其實每次都現算。**對外是欄位介面、對內是方法**——這就是 `@property` 的殺手應用：未來你想改內部實作，呼叫端一行都不用動。」

---

## F4-S6 · PITFALL (P1) — `__x` 不是加密

- 🖼️ 畫面：VS 兩欄，左紅「以為 `__x` 是 private」右綠「敏感資料該 hash」，下方一句 why
- 📣 畫面上的字：
  - 左：`self.__password = pw` → `u._User__password` 照樣拿到 `"s3cret"`
  - 右：`hashlib.sha256(pw).hexdigest()` + `verify()` 方法
  - why：`__x` 的目的是避免子類命名衝突，不是安全機制
- 🎙️ 講者這時說：「這是每年都會有人踩的坑。學員把密碼丟進 `__password`，覺得『外人拿不到就是安全』。錯。外人只要多打幾個字就繞過了。**敏感資料不是靠語法保護的**——要 hash、加密，或者根本不存在記憶體裡。」

---

## F4-S7 · ASK — 三種讀檔器要寫三次嗎？

- 🖼️ 畫面：白底大字問句 + 右下資料卡（70% 重複）
- 📣 畫面上的字：
  - 「要支援 CSV / JSON / Parquet 三種來源，你要寫三個獨立類別，還是一個家族？」
  - 卡片：重複邏輯比例 · 70% · 讀檔 → 檢查 → 回 DataFrame
- 🎙️ 講者這時說：「課堂實測：讓 10 位學員各寫三個 Reader，70% 的步驟完全一樣——開檔、檢查編碼、回傳 DataFrame、記錄列數。重複三次的代價，就是改一次要改三個地方。繼承就是解這個。」

---

## F4-S8 · CONCEPT-CARD — DataReader 家族

- 🖼️ 畫面：左側繼承樹圖（真圖佔位 F4_S08_inheritance_tree）+ 右側 code panel
- 📣 畫面上的字：
  - 樹：DataReader → CSVReader / JSONReader / ParquetReader（每支註 override read）
  - code：基類拋 `NotImplementedError`，子類覆寫 `read`
  - bullets：基類定介面、子類實作差異、共用邏輯寫一次
- 🎙️ 講者這時說：「這就是繼承的正確用法——**共同點上移、差異點下放**。基類負責合約（這家族一定有 `read` 方法）；子類負責差異（CSV 怎麼讀、JSON 怎麼讀）。下週要加 Excel？只要寫一個新子類，舊的完全不動。」

---

## F4-S9 · EXAMPLE-I/O — super + override

- 🖼️ 畫面：全寬 code panel（`DataReader` + `CSVReader` 完整骨架）+ 右側 bullets
- 📣 畫面上的字：
  - `super().__init__(encoding)` 父類先設好 → `self.sep = sep` 子類加自己的
  - `read()` override：sep + encoding 都用得到
  - bullets：super 必做 / override 可延伸簽章 / 漏 super → 兩個月才爆
- 🎙️ 講者這時說：「子類 `__init__` 的第一件事永遠是 `super().__init__()`——先把父親那份做完，再做自己的。`read` 方法是 override：同名、重寫，但可以接更多參數。子類裡 `self.encoding` 直接可以用，因為父類已經設好了。」

---

## F4-S10 · PITFALL (P2) — 漏呼 super().__init__()

- 🖼️ 畫面：VS 兩欄，左紅「漏呼 super」右綠「先 super 再設自己的」
- 📣 畫面上的字：
  - 左：`CSVReader()` → `r.read("a.csv")` → `AttributeError: no attribute 'encoding'`
  - 右：`super().__init__(encoding)` 後，`r.encoding` 有值
  - why：漏呼 = 父類屬性全沒初始化，錯誤延後兩個月才爆
- 🎙️ 講者這時說：「這個坑比 P1 更陰險。你漏呼 super，測試時如果剛好沒走到父類屬性，單元測試全綠。兩個月後生產環境某條冷路徑用到了 `self.encoding`——AttributeError。所以：**子類 `__init__` 第一行永遠是 super**。」

---

## F4-S11 · CONCEPT-CARD — IS-A vs HAS-A

- 🖼️ 畫面：2×2 matrix（IS-A ✓ / HAS-A 繼承 ✗ / 組合 ✓ / 本章不教）
- 📣 畫面上的字：
  - IS-A ✓：CSVReader is a DataReader
  - HAS-A 繼承 ✗：OrderList(list) 別這樣
  - 組合 ✓：Cleaner has a Logger
  - 本章不教：多重繼承 / MRO / ABC
- 🎙️ 講者這時說：「關鍵一題——**IS-A 還是 HAS-A**。CSVReader 『是一個』DataReader，這是 IS-A，繼承合理。但 `Order` 不是 `List`——它『裝了』幾個商品而已，這是 HAS-A，該用組合（`self.items = []`）。記住鐵則：**能用組合不用繼承**。」

---

## F4-S12 · CONCEPT-CARD — 魔術方法四件套

- 🖼️ 畫面：2×2 matrix，四個 dunder 各一格
- 📣 畫面上的字：
  - `__str__`：print / str → 給人看
  - `__repr__`：REPL / repr → 給開發者看，最好能反貼重跑
  - `__len__`：len() → 有數量感才實作
  - `__iter__`：for-in → 讓物件可迭代
- 🎙️ 講者這時說：「魔術方法是什麼？名字前後有雙底線的方法——Python 會在特定時機幫你自動呼叫。你寫 `print(obj)`，Python 自動跑 `obj.__str__()`；你寫 `len(obj)`，Python 自動跑 `obj.__len__()`。這四個最常用，學會你的類就像 Python 內建型別一樣自然。」

---

## F4-S13 · EXAMPLE-I/O — `__str__` vs `__repr__`

- 🖼️ 畫面：全寬 code panel（Order 類同時定義 str / repr）+ 右側 bullets
- 📣 畫面上的字：
  - `print(o)` → 訂單 #A01：NT$ 12,800
  - `repr(o)` → `Order(id_='A01', amount=12800)`
  - bullets：str 給使用者 / repr 給 debug / repr 理想可反貼 / 沒 str 會退而求其次用 repr
- 🎙️ 講者這時說：「兩個都要寫。`__str__` 給終端使用者看——訂單編號、金額、單位都好看；`__repr__` 給開發者 debug——理想狀態是你把 REPL 的輸出複製貼回去，能重建一個一樣的物件。**沒寫 `__repr__` 的後果**：print 一個 list of Order 會看到七個 `<Order at 0x7f...>`。」

---

## F4-S14 · EXAMPLE-I/O — `__len__` / `__iter__`

- 🖼️ 畫面：全寬 code panel（`DataPipeline` 類）+ 右側 bullets
- 📣 畫面上的字：
  - `pipe.add(clean).add(normalize).add(export)` → chaining 預告
  - `len(pipe)` → 3；`for s in pipe: ...` → 自動逐步
  - bullets：有數量感→__len__ / 有逐一處理→__iter__ / 通常成對
- 🎙️ 講者這時說：「`DataPipeline` 裡裝了幾個步驟——這叫『數量感』，該實作 `__len__`；可以逐一跑每個步驟——這叫『逐一處理』，該實作 `__iter__`。這兩個通常成對出現：是集合概念的必備配件。順便注意 `add` 最後那行 `return self`——下一頁的伏筆。」

---

## F4-S15 · CONCEPT-CARD — Method Chaining

- 🖼️ 畫面：左側流程圖（真圖佔位 F4_S15_chaining_flow：read→drop_na→normalize→export）+ 右側 code panel
- 📣 畫面上的字：
  - 四節點水平排列，每節點標 `return self`
  - code：`DataCleaner` 每個方法最後都 `return self`
  - 呼叫端 `(DataCleaner(df).drop_na().normalize(["price"]).export("out.csv"))`
  - bullets：每個方法 return self / 像句子 / 程式結構 = 資料流結構 / F5 骨架
- 🎙️ 講者這時說：「看右下那段呼叫端——`DataCleaner(df).drop_na().normalize(["price"]).export("out.csv")`。這**讀起來像一句話**：拿資料 → 去空值 → 標準化 price → 匯出。為什麼能這樣寫？因為每個方法最後都 `return self`，讓你可以繼續點下一個。這個模式就是 F5 `DataCleaner` 的骨架——今天埋下來。」

---

## F4-S16 · PITFALL (P5) — Chaining 忘記 `return self`

- 🖼️ 畫面：VS 兩欄，左紅「忘寫 return self」右綠「每一個都 return self」
- 📣 畫面上的字：
  - 左：`drop_na()` 沒 return → `.normalize(...)` 炸 AttributeError（NoneType）
  - 右：每個方法 `return self`
  - why：Python 函式沒 return 就回 None；鏈上任一環回 None，下一步就 AttributeError
- 🎙️ 講者這時說：「這是 F5 會反覆提醒的坑。你的 `drop_na` 邏輯完全對、結果也對——但忘了 `return self`。鏈的下一環拿到 `None`，然後 `None.normalize(...)` 炸。錯誤訊息還很誤導：『NoneType has no attribute normalize』——你以為 normalize 有 bug，其實問題在上一個方法。記住：**鏈上每個方法都要 return self**。」

---

## F4-S17 · EXAMPLE-I/O — 四柱合體

- 🖼️ 畫面：全寬 code panel（`BaseCleaner` + `PriceCleaner`）+ 右側 5 條 bullets 標出四柱
- 📣 畫面上的字：
  - `_df` → 封裝、`@property shape` → property、`__len__` → 魔術方法
  - `drop_na` return self → chaining
  - `PriceCleaner(BaseCleaner)` 覆寫 `drop_na`，super + 擴充條件
  - bullets：封裝 / 繼承 / 魔術方法 / Chaining / F5 起跑線
- 🎙️ 講者這時說：「四柱合體預告。`BaseCleaner` 裡——`_df` 是封裝、`@property shape` 是封裝的進階版、`__len__` 是魔術方法、`drop_na` 最後 `return self` 是 chaining。`PriceCleaner` 繼承基類、覆寫 `drop_na`、先 `super()` 再加自己的條件。一個類別把今天四件事全部用上了。」

---

## F4-S18 · BRIDGE — 銜接 F5

- 🖼️ 畫面：水平 flow chain 四節點（封裝 / 繼承 / 魔術方法 / Chaining）+ 下方 2 行總結
- 📣 畫面上的字：
  - 四節點各一句描述
  - 「F5 會把這四柱接成一條完整清理管線——今天你手上的每個零件，明天都會再裝回去一次。」
- 🎙️ 講者這時說：「下節 F5，我們要做一個真正能跑的 `DataCleaner`——讀 CSV、檢查空值、處理異常、標準化欄位、匯出。今天教的這四件事**不是四個獨立知識點**，是一條管線上的四個零件。你如果現在覺得 `return self` 沒什麼用——下節課你會看到它撐起整個 API。」

---

## F4-S19 · CHECKPOINT — 五題快問（90 秒）

- 🖼️ 畫面：標題 + 五題條列，字級較大
- 📣 畫面上的字：
  - Q1 `__x` 真的私有嗎？
  - Q2 漏呼 `super().__init__()` 會怎樣？
  - Q3 只寫 `__str__`，REPL 打物件名看到什麼？
  - Q4 Chaining 忘 `return self`，下一次呼叫拿到什麼？
  - Q5 「訂單裝了三個商品」——繼承還是組合？
- 🎙️ 講者這時說：「不看講義，90 秒。五題對應今天五個核心坑——封裝的真相、super 的必要、repr 的存在感、return self 的後果、繼承 vs 組合的分界。答不出來的題就是待會下課要再翻一次 outline 的地方。」

---

## F4-S20 · PYRAMID — 收束

- 🖼️ 畫面：pyramid 兩層（三根柱子 + 設計紀律）+ 下方 thesis 銜接句
- 📣 畫面上的字：
  - 三根柱子：封裝 / 繼承 / 魔術方法
  - 設計紀律：組合優先 / 單一繼承已夠 / 一路 return self
  - thesis：F5 進入 OOP + Pandas 整合實戰 —— 用本章四柱打造 DataCleaner
- 🎙️ 講者這時說：「收束——三根柱子加三條設計紀律。柱子是工具：封裝、繼承、魔術方法。紀律是取捨：能組合就別繼承、能單繼承就別多重、鏈上一路 `return self` 不破。下節 F5 把這些接起來做 `DataCleaner`。今天到這裡。」
