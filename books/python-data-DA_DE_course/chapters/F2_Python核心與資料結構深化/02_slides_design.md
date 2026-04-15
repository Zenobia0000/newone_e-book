# F2 — Python 核心與資料結構深化｜Slides Design

> 21 張內容投影片（封面 + 21 + 版權）｜教學型七原型 + 銜接導引 3 張
> 對齊 `01_outline.md` 的 5 個 Learning Objectives × 5 個 Common Pitfalls
> 配色：主色 `#1B5E3F` + 警示紅 `#C62828`（僅 PITFALL 頁）+ 成功綠 `#2E7D32`
> 受眾：只有 Python 基礎的非理工背景學員——禁用 CS 術語，大量生活類比

---

## S1 · MOTIVATION — Pandas 踩的坑，根在 Python 基礎

- 🖼️ 畫面：白底 / 中央大字痛點句 / 右下 60% 數據卡
- 📣 畫面上的字：
  - 「你在 Pandas 裡踩過的那些『改了 A 結果 B 也變』『一個警告看不懂』，根源其實不在 Pandas——在 Python 基礎。」
  - 數據卡：**60%** / Pandas 初學者的錯誤，回溯到容器選錯 / 複製不對 / 迭代用錯
- 🎙️ 講者這時說：「今天不是基礎複習，是要解決你未來學 Pandas 會踩的 60% 坑。先打地基。」

---

## S2 · ASK — 10GB log 怎麼讀？

- 🖼️ 畫面：白底 / 大字問句 / 右下 200× 數據卡
- 📣 畫面上的字：
  - 「要在 10GB 的 log 檔裡挑出所有 ERROR 行，你會怎麼寫？整個檔案讀進來還是怎樣？」
  - 卡片：**~200×** / 全部讀進來 → 電腦直接卡死；逐頁翻 → 只用 < 50 MB
- 🎙️ 講者這時說：「這是一個真實場景：10GB 的 log。不會寫的人開下去電腦就躺了。會寫的人 3 行解決。差在思維，不在程式。」

---

## S3 · SILENT — 一句話立論

- 🖼️ 畫面：全綠底 / 白色 HERO 大字
- 📣 畫面上的字：「今天只教兩件事：會選容器 → 能寫對；會用 generator → 能寫大。」
- 🎙️ 講者這時說：「我只教兩件事。其它你已經會了，或是網路上查就有。這兩件是 Pandas 前不補、永遠會卡的。」

---

## S4 · CONCEPT-CARD — 四容器生活類比

- 🖼️ 畫面：2×2 matrix / 每格用生活場景 + 圖示短語
- 📣 畫面上的字：
  - List = 聯絡人清單（有順序、可重複）
  - Tuple = 身分證欄位（固定、不可變）
  - Dict = 字典查字（用關鍵字翻答案）
  - Set = 收藏夾 / 去重袋（自動去重）
- 🎙️ 講者這時說：「不背定義，背場景。List 是『排隊的』、Dict 是『查字典』、Set 是『去重袋』、Tuple 是『鎖死的欄位』。記這四個畫面就夠。」

---

## S5 · MECHANISM-FLOW — 30 秒決策樹

- 🖼️ 畫面：2×2 matrix 四題串成流程 / 最後一格 highlight
- 📣 畫面上的字：
  - Q1 要順序＋重複 → List（營業額紀錄）
  - Q2 只在乎有沒有 → Set（去重客戶編號）
  - Q3 用關鍵字查答案 → Dict（員工編號 → 姓名）
  - Q4 欄位鎖死 / 要當 key → Tuple（縣市郵遞區號）
- 🎙️ 講者這時說：「照順序問這四個，選到就停。實務上 80% 是 List，15% 是 Dict——別每次都糾結。」

---

## S6 · EXAMPLE-I/O — 四容器操作對照表

- 🖼️ 畫面：editorial 表格 4 欄 × 4 列 / 下方一句 take-away
- 📣 畫面上的字：
  - 欄：容器 / 生活場景 / 關鍵操作 / 查一筆資料的速度
  - 最關鍵一列：List = 翻整本；Dict / Set = 直接翻到索引
  - 下方：「10 萬筆時，List 要翻幾秒、Set 幾乎 0 秒」
- 🎙️ 講者這時說：「資料量小時你感覺不到差別。10 萬筆以上差距會跳出來。這就是為什麼『查有沒有』一律 Set。」

---

## S7 · EXAMPLE-I/O — 商業場景（銜接 S2 DataFrame）

- 🖼️ 畫面：code panel 三段商業範例 + 右側 bullets（銜接點）
- 📣 畫面上的字：
  - ① 訂單去重 → `set(orders)`
  - ② 員工對照 → `emp['E1024']`
  - ③ 一列資料 = 一個 dict；一串 dict = DataFrame 前身
  - bullet：**下週 S2：`pd.DataFrame(rows)` 直接變表**
- 🎙️ 講者這時說：「這張是今天最重要的銜接。記住：一個 dict = 資料表的一列。你今天手上這個 list-of-dict，下週就是 DataFrame。」

---

## S8 · CONCEPT-CARD — 便利貼心智模型

- 🖼️ 畫面：flow_chain 三節點 / 下方 inverted thesis box
- 📣 畫面上的字：
  - name（便利貼）→ 指向 → object（真正的東西）
  - thesis：「`b = a` 不是影印一份，是再貼一張便利貼到同一個東西上」
- 🎙️ 講者這時說：「變數不是盒子——是便利貼。這個畫面今天帶走就夠了。下一頁的坑全都從這裡來。」

---

## S9 · CONCEPT-CARD — 可變 × 當 key 的 2×2

- 🖼️ 畫面：2×2 matrix / 右上 highlight
- 📣 畫面上的字：
  - 會變（list/dict/set）→ 不能當 key
  - 不會變（數字/字串/tuple）→ 能當 key
  - 下方注記：「Python 記不住一個會變的東西的『指紋』」
- 🎙️ 講者這時說：「為什麼 tuple 能當 key、list 不行？因為 tuple 鎖死了，Python 記得住。list 一直在變，Python 記不住。」

---

## S10 · PITFALL — `[[]] * 3` 是貼三張便利貼

- 🖼️ 畫面：code panel + 右側 bullets
- 📣 畫面上的字：
  - `a = [[]] * 3; a[0].append(1)` → `[[1],[1],[1]]`（嚇到）
  - 正解：`[[] for _ in range(3)]`
- 🎙️ 講者這時說：「這題我看過 10 年——每一屆都有人踩。記口訣：要 n 個獨立的，用 comprehension 逐一生。」

---

## S11 · PITFALL — 淺深拷貝（銜接 Pandas）

- 🖼️ 畫面：VS 兩欄 / 下方 summary + delta badge「只差一層」
- 📣 畫面上的字：
  - 左：淺 = 只複製外殼（`list.copy()`、`x[:]`）
  - 右：深 = 連裡面一起（`copy.deepcopy`）
  - summary：「這就是你未來看到 Pandas `SettingWithCopyWarning` 的根源——系統在提醒你：你改的到底是本尊還是分身？」
- 🎙️ 講者這時說：「這張是銜接點——學 Pandas 會看到 `SettingWithCopyWarning` 的人就是吃這個虧。今天懂了，未來不會卡。」

---

## S12 · CONCEPT-CARD — for 是在『要下一個』

- 🖼️ 畫面：flow_chain 四節點對話式 / 下方 inverted thesis box
- 📣 畫面上的字：
  - for 問：還有嗎？→ 容器答：有 → for 處理 → 容器答：沒了（停止）
  - thesis：「你不用寫 while 跟計數器——Python 的 for 已經幫你問到底、接收到『沒了』就自動停」
- 🎙️ 講者這時說：「不要背 `__iter__` / `__next__`。記住 for 在『要下一個』就夠——這個直覺下一頁 yield 會用到。」

---

## S13 · MECHANISM-FLOW — yield = 連續劇

- 🖼️ 畫面：code panel 連續劇比喻 + 右側 bullets
- 📣 畫面上的字：
  - `yield 1` = 本集結束、`yield 2` = 下集開播
  - bullet：「呼叫 g = counter() 不會播——只是訂閱」「每次 yield 凍住『場景 + 進度』」
- 🎙️ 講者這時說：「yield 不是 return。return 是一去不回、yield 是本週結尾、下週接著演。記住這個畫面。」

---

## S14 · EXAMPLE-I/O — [ ] vs ( )

- 🖼️ 畫面：VS 兩欄 / delta badge「~200× RAM」
- 📣 畫面上的字：
  - 左：`[x*2 for x in range(10**8)]` → 3.2 GB（電腦哀號）
  - 右：`(x*2 for x in range(10**8))` → 200 bytes
  - summary：「括號不同、命運不同」
- 🎙️ 講者這時說：「一個括號之差，記憶體差兩個數量級。這不是修飾——是『能不能跑』的差別。」

---

## S15 · EXAMPLE-I/O — 10GB log 三行

- 🖼️ 畫面：code panel 三行解法 + bullets
- 📣 畫面上的字：
  - `def read_errors(path): with open(..) as f: for line in f: if 'ERROR' in line: yield line.rstrip()`
  - bullet：「檔案本身就是『一頁一頁』」「10GB 流過，RAM < 50 MB」
- 🎙️ 講者這時說：「回到一開始的題目——三行。這三行背下來，你職場的第一個 data engineering 任務就解得掉。」

---

## S16 · EXAMPLE-I/O — 銜接 S2 chunksize

- 🖼️ 畫面：code panel Pandas 範例 + 右側 bullets（銜接點高亮）
- 📣 畫面上的字：
  - `pd.read_csv('orders_5GB.csv', chunksize=100_000)` → 回傳 generator
  - `for chunk in chunks:` 處理一塊、丟掉一塊
  - bullet：「Pandas chunksize = 今天教的 yield」「今天你懂 yield = 下週你懂 chunksize」
- 🎙️ 講者這時說：「這張就是 F2 → S2 的護照。下週你會看到 chunksize——到時候你會回想起這張。」

---

## S17 · PITFALL — generator 只能翻一次

- 🖼️ 畫面：code panel + 右側 bullets
- 📣 畫面上的字：
  - `sum(g)` → 20 ✅、`list(g)` → []（空！）
  - 救法 A：重建；救法 B：先 list() 存下來
- 🎙️ 講者這時說：「Generator 像書——翻完就到最後一頁。想多次用？要嘛重建、要嘛存成 list。」

---

## S18 · PRACTICE-PROMPT — 3 分鐘練習

- 🖼️ 畫面：1×3 matrix 三題 / 下方答案提示
- 📣 畫面上的字：
  - ① 訂單去重（用 set）
  - ② ID 對照（用 dict）
  - ③ 逐行讀檔（用 yield）
  - 答案：`set(orders)` / `dict(zip(...))['E1']` / S15 三行
- 🎙️ 講者這時說：「3 分鐘——跟隔壁對答案。這三題答得出來，今天就值回票價。」

---

## S19 · CHECKPOINT — 三題快問

- 🖼️ 畫面：1×3 matrix / 下方答案
- 📣 畫面上的字：
  - Q1 10 萬筆 ID 查『有沒有下過單』→ 選誰？
  - Q2 `a.copy()` 後改內層 → a 變什麼？
  - Q3 `list(g)` 跑兩次 → 兩次印什麼？
- 🎙️ 講者這時說：「不看投影片、口頭答。三題答得出來就繼續；卡住就翻 S6 / S11 / S17。」

---

## S20 · PYRAMID — 三層 take-away

- 🖼️ 畫面：pyramid_stack 四層 + 底部 inverted thesis box
- 📣 畫面上的字：
  - 頂：思維 — 寫大（generator 逐頁翻）
  - 第二：心智 — 寫對（便利貼、可變性）
  - 第三：工具 — 選容器（List/Dict/Set/Tuple）
  - 底：地基 — Python 基礎
  - thesis：「這三層會了，下週 S1/S2 你會發現它們就長在這塊地基上」
- 🎙️ 講者這時說：「最後收束——從地基往上：Python 基礎 → 選容器 → 懂可變 → 用 generator。三層都踏穩，Pandas 就順。」

---

## S21 · SILENT — 收束 + 銜接下一節

- 🖼️ 畫面：全綠底 / 白色 HERO 大字
- 📣 畫面上的字：「會選容器 → 能寫對；會用 generator → 能寫大。下一站：S2 Pandas —— DataFrame 就是一排 dict + chunksize。」
- 🎙️ 講者這時說：「下課前記住這句話。下週 S2 見——你會發現 Pandas 就是今天這兩招長大的樣子。」

---

**節奏檢查**：
- 動機（S1-2）→ 立論（S3）→ 容器（S4-7）→ 可變（S8-11）→ 迭代（S12-17）→ 練習（S18）→ 驗收（S19）→ 收束（S20-21）
- 5 個 PITFALL 頁（S10 P1 / S11 P3 / S17 P5）+ 隱含（S8 P2 / S9 P4）全數對應 outline §4
- 1 個 CHECKPOINT（S19）+ 1 個 PRACTICE（S18）+ 1 個 PYRAMID（S20）
- **3 張銜接導引**：S7（dict → DataFrame）/ S11（copy → SettingWithCopyWarning）/ S16（yield → chunksize）
