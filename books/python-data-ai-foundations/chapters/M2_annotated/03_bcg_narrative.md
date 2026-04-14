# 03 — M2 BCG 式敘事腳本

> **文件定位**：把 M2 的技術內容重新包裝成 BCG / McKinsey 顧問式的 executive 敘事，用於內部技術討論會的 pitch 或向非技術 stakeholder（PM、產品、學程主管）報告。
> **對象**：需要把 OOP 課程價值向上管理、向橫向部門說明的同事。
> **立場**：技術內容不稀釋，但表達改成 top-down、一頁一論點、由結論倒推支撐。
> **使用方式**：依序走完 Executive Summary → SCQA → Governing Thought → MECE 三支柱 → 12–18 頁腳本 → 金句頁 → Closing Ask。

---

## Executive Summary（一頁，30 秒能講完）

**What**：M2 教 OOP 與程式抽象，是 24 小時課程的第 4–6 小時、3 小時教學。

**Why Now**：學生 M1 學完語法後，會卡在「腳本能跑但無法維護」的天花板。AI 工程的真實工作 90% 在這個天花板以上，包括 chatbot 狀態管理、資料管線、模型版本控制。

**How**：用 6 張核心投影片（概念）+ 4 張實作投影片（程式碼）+ 2 場工作坊，帶學生從「寫 class」到「拆 package」。

**So What**：完成 M2 的學生能讀懂 scikit-learn / pandas / LangChain 的 class API，能寫出一個真實 AI 專案的 package 結構。沒完成 M2，後續 M3–M12 的每一個模組都會被拖慢。

**Ask**：請 reviewer 同意 P0 修訂案（補 `@dataclass` / Protocol / polymorphism / object 三要素）。

---

## SCQA 敘事結構

**Situation（共識的現況）**
- 公司內部 AI 工程師招募中，新進 junior 90% 卡在「會寫 notebook、不會寫 package」。
- 市面 Python 課程教 OOP，但多數停留在 Java 風格的教法，與 Python 2026 的慣例脫節。

**Complication（矛盾／缺口）**
- 傳統 OOP 教學 → 教 class 和 inheritance → 學生進職場 → 面對的是 dataclass、Protocol、composition、async agent → 學了的用不上，該用的沒學到。
- 24 小時課程預算有限，不能無限加內容。

**Question（真正要問的問題）**
- 如何在 3 小時內，讓學生從 notebook 思維升級到 package 思維，且內容與 2026 的 Python 生態對齊？

**Answer（我們的回答）**
- M2 用「資料+行為綁在一起」這個單一主題貫穿，以 chatbot / dataset / pipeline 三個 AI 場景為載體，讓學生 3 小時內建立可遷移的抽象思維。

---

## Governing Thought（統御思想）

> **"Abstraction is how engineering scales beyond the individual mind."**
> **抽象，是工程能超越個人腦容量的唯一手段。**

這句話是整個 M2 的北極星。所有支線論點最終必須回到這句話。

**為何這句話站得住**：
- 人類工作記憶 7±2 chunk，這是生物學上限。
- 任何有價值的系統複雜度遠超過這個上限。
- 唯一的技術手段：**打包、隱藏、重用**——這就是 OOP 的三件事。
- 不是「因為 OOP 好所以要學」，是「因為人腦有上限所以必須抽象，而 OOP 是當代 Python 的抽象語法」。

---

## MECE 三支柱

整個 M2 的內容 **互斥且窮盡** 地分為三個支柱：

```
                  抽象如何讓工程超越個人腦容量
                              │
      ┌───────────────────────┼───────────────────────┐
      │                       │                       │
   【封裝】                【繼承+組合】              【模組化】
  Encapsulation       Inheritance+Composition        Modularity
      │                       │                       │
  控制可見性             控制重用關係             控制程式碼物理邊界
      │                       │                       │
  降低介面熵             降低變更擴散             降低跨檔耦合
      │                       │                       │
  Slide 3-5              Slide 7                 Slide 8-9
```

**為何是這三支柱（MECE 驗證）**：
- 互斥：封裝控制「邊界」，繼承+組合控制「關係」，模組化控制「物理組織」，三者不重疊。
- 窮盡：OOP 的所有技術內容都落在這三個之一，沒有第四類。

**反方可能提問**：polymorphism 放哪裡？
**回答**：polymorphism 是「繼承+組合」的**結果**，不是獨立支柱。在本敘事中歸入第二支柱。

---

## 12–18 頁腳本（建議 15 頁）

> 每頁一個論點，由上而下推。粗體是頁標題，下方是講稿要點與轉場。

---

### P1 — 封面：Abstraction is how engineering scales beyond the individual mind

- 單句 governing thought 佔 80% 版面。
- 下方一行：M2 of 12｜Hour 4–6 of 24｜OOP & Abstraction。

### P2 — 現況：我們的 junior 在哪裡卡住？

- 一張圖：招募 funnel，「能寫 notebook」→ 90% → 「能寫 package」→ 30%。
- 金句：**可以跑 ≠ 可以維護。**

### P3 — 矛盾：傳統 OOP 教學與 2026 Python 脫節

- 左右對比表：傳統教法 vs Python 2026 慣例。
- 結論：不是 OOP 沒用，是**教的 OOP 用不上**。

### P4 — 問題：3 小時內能把 junior 從 notebook 思維升到 package 思維嗎？

- 限制：3 小時、2 場工作坊、24 小時課程的一部分。
- 目標：學生能獨立拆解 200 行腳本成 package，能讀 scikit-learn class 文件。

### P5 — 答案：Governing Thought 與三支柱（MECE）

- 重申 governing thought。
- 三支柱圖（封裝／繼承+組合／模組化）。
- 每支柱一句話：各自控制什麼。

### P6 — 支柱一：封裝（Encapsulation）

- 定義：把 state 與 behavior 綁在一起，控制對外可見性。
- 資訊理論洞察：**介面越小，系統越可替換。**
- 範例：`Dataset._data` 不對外。
- AI 場景：`ChatAgent` 的 `_history` 必須藏起來，否則多用戶場景崩潰。

### P7 — 支柱一示範：從函數散落到 class 凝聚

- 左：5 個散落函數 + 3 個全域變數。
- 右：一個 `Dataset` class，同樣功能，介面縮小到 4 個 public method。
- 金句：**把 20 個參數縮成 1 個 object，是 OOP 的第一個勝利。**

### P8 — 支柱二：繼承 + 組合（Inheritance + Composition）

- 定義：繼承管 is-a，組合管 has-a。
- 資訊理論洞察：**繼承是最高耦合，組合是最低耦合。**
- 預設立場：**2026 年 Python，預設用 composition。**
- Python 的真實做法：用 `typing.Protocol` 表達抽象，不靠 `class X(BaseX)`。

### P9 — 支柱二示範：ChatAgent 的 composition 設計

- `ChatAgent` 內嵌 `VectorStoreClient`、`LLMClient`、`ConversationMemory`。
- 任何一個元件換掉（Pinecone → Chroma、OpenAI → Claude），`ChatAgent` 不動。
- 金句：**能替換的系統才是活的系統。**

### P10 — 支柱三：模組化（Modularity）

- 定義：把相關的 class 放進 module，相關的 module 放進 package。
- 判準：**高內聚、低耦合**（cohesion & coupling，SWEBOK 明列指標）。
- Python 特定：`__init__.py` 做 re-export，不放重邏輯。

### P11 — 支柱三示範：腳本的進化路徑

- 橫軸：Notebook → Script → Module → Package → Library → Service。
- 每一步解決前一步的新痛點。
- 金句：**你不是在寫程式，你是在讓程式能被別人用。**

### P12 — 三支柱合流：一個 AI 專案的樣貌

- 系統圖：`Dataset → FeaturePipeline → ModelTrainer → ChatAgent(VectorStoreClient)`。
- 標示每一段展現了哪一個支柱。
- 金句：**scikit-learn 的介面穩定 20 年，內部重寫無數次，這就是抽象的勝利。**

### P13 — 工作坊設計：把論點變成肌肉記憶

- 工作坊 1（25 min）：寫一個 `Dataset` class，覆蓋支柱一。
- 工作坊 2（30 min）：拆解 200 行腳本成 package，覆蓋支柱二與三。
- 驗收：重構前後執行 `train.py`，metrics 完全一致。

### P14 — 金句頁（獨立一頁，留白 70%）

> **"A class is a contract. A package is a promise."**
>
> **class 是合約，package 是承諾。**
>
> 合約規範單一物件的行為，承諾跨檔案的穩定邊界。

### P15 — Closing Ask（行動呼籲）

- **決策請求**：通過 P0 修訂案（補 `@dataclass` / Protocol / polymorphism / object 三要素）。
- **資源請求**：15 分鐘額外內容從 Slide 1/8/工作坊 1 壓縮而來，**不增加總時長**。
- **時程**：下個 cohort 開課前（4 週內）完成修訂 + 同儕 review。
- **風險**：不改，本模組內容落後生態 5–8 年，3 年內會失去可信度。
- **最後一問**：**我們要教 2020 年的 Python，還是 2026 年的 Python？**

---

## 金句頁清單（可抽離到簡報或社群）

1. **Abstraction is how engineering scales beyond the individual mind.**
2. **可以跑 ≠ 可以維護。**
3. **把 20 個參數縮成 1 個 object，是 OOP 的第一個勝利。**
4. **能替換的系統才是活的系統。**
5. **你不是在寫程式，你是在讓程式能被別人用。**
6. **A class is a contract. A package is a promise.**
7. **介面越小，系統越可替換。**
8. **繼承是最高耦合，組合是最低耦合。預設用組合。**

---

## Closing Ask（給 reviewer 的明確勾選項）

- [ ] 同意 governing thought：「Abstraction is how engineering scales beyond the individual mind.」
- [ ] 同意 MECE 三支柱（封裝 / 繼承+組合 / 模組化）
- [ ] 同意 P0 修訂案進下個 cohort
- [ ] 指派 P1 修訂的負責人與 deadline
- [ ] 核准工作坊 1/2 的驗收腳本撰寫預算（約 4 人時）

**若以上全部 checked**，M2 可以在 4 週內完成修訂並上線。
