# Ch04 — 生成式 AI 系統工程｜Slides Design

> 24 張內容投影片（封面 + 24 + 版權）｜教學型七原型為主
> 對齊 `01_outline.md` 的 7 個 Learning Objectives x 5 個 Common Pitfalls
> 配色：主色 `#1565C0` + 錯誤紅 `#C62828`（僅 PITFALL 頁）+ 成功綠 `#2E7D32`
> 2 張銜接導引：S23 收束 + S24 → Ch05

---

## S1 . ASK — 你上次被 AI 幻覺騙到是什麼時候？

- 🖼️ 畫面：全白底 / 大字痛點問句 / 右下一張資料卡（數據）
- 📣 畫面上的字：
  - 標題：「你上次被 ChatGPT 的回答騙到，是什麼時候？」
  - 資料卡：`GenAI 幻覺率 . 3-15% . 依任務與模型而異（Stanford HAI 2024）`
- 🎙️ 講者這時說：「在開始之前先想一件事——你上次把 ChatGPT 的回答直接拿來用，結果發現是錯的，那是什麼時候？GenAI 的風險不是不會回答，是太會回答——它的回答有自信、有結構、有引用，但事實可能完全錯誤。這就是為什麼我們今天不只學怎麼用 GenAI，而是學怎麼把它變成一個可靠的系統。」

---

## S2 . VS — 聊天工具 vs 系統元件

- 🖼️ 畫面：雙欄對照 / 左標題「聊天工具」右標題「系統元件」/ 中央 delta「工程化程度」/ 底部 summary
- 📣 畫面上的字：
  - 左：打開 ChatGPT 問問題 / 人工看回答判斷品質 / 無法追蹤版本 / 無法規模化 / 結果因 prompt 而異
  - 右：LLM 嵌入應用後端 / 自動化 eval 量測品質 / retrieval + generation 分層 / API 呼叫可監控 / 結果可重現可量化
  - Summary：「把 LLM 當聊天機器人是入門，把它嵌進系統才是工程。」
- 🎙️ 講者這時說：「左邊是大部分人現在的用法——打開 ChatGPT、問個問題、人眼看回答。右邊是 GenAI 真正上線的樣子——LLM 是系統裡的一個元件，前面有 retrieval，後面有 eval，每一段都可以獨立測試、獨立最佳化。今天要從左邊走到右邊。」

---

## S3 . SILENT — 立論

- 🖼️ 畫面：全藍底 (`#1565C0`) / 白色 HERO 大字置中
- 📣 畫面上的字：「GenAI 已經從模型知識變成系統工程——token / RAG / tools / agents / evals 是新的必修。」
- 🎙️ 講者這時說：「這節課若只能記一句話，就是這句。兩年前學 GenAI 是學模型原理——Transformer、attention、scaling law。現在學 GenAI 是學系統工程——怎麼算 token、怎麼做 retrieval、怎麼設計 tool schema、怎麼跑 eval、怎麼控制成本。你不需要會訓練 GPT-4，但你需要會把它嵌進一個可靠的系統。」

---

## S4 . CONCEPT-CARD — Token / Context Window / Parameters

- 🖼️ 畫面：左欄三層金字塔圖 + 右欄中文 token 計算實例（pending real image）
- 📣 畫面上的字：
  - 標題：「Token 是計費單位也是思考單位」
  - 金字塔底層：Parameters（70B / 405B）— 模型學過多少知識
  - 金字塔中層：Context Window（128K / 200K tokens）— 一次能看多少
  - 金字塔頂層：Token（1 中文字 ≈ 1.5-2 tokens）— 最小處理單位
  - 右欄：「你好嗎」→ BPE 分詞 → 4 tokens → 成本計算
- 🎙️ 講者這時說：「從底層往上看。Parameters 是模型訓練時學到的知識量——70B 還是 405B，決定它的能力上限。Context window 是一次對話能塞進去的 token 總量，input + output 合計。Token 是最小的計費和處理單位——注意，不是字也不是詞，是 BPE 分詞後的片段。中文因為不在主要訓練語料中，一個字通常會被切成 1.5 到 2 個 token，比英文貴。」

---

## S5 . EXAMPLE-I/O — Token 計算實戰

- 🖼️ 畫面：三欄橫排（輸入 → 過程 → 產出）+ 下方成本表
- 📣 畫面上的字：
  - ①輸入：一份 10 頁中文報告（約 5000 字）
  - ②過程：5000 字 x 1.8 tokens/字 ≈ 9000 input tokens + 預估 1000 output tokens = 10000 tokens
  - ③產出：GPT-4o: ~$0.05 / Claude Sonnet: ~$0.04 / 開源 Llama 3: 自架成本另計
  - Bottom：「Token 計算是成本控制的第一步——不會算 token 就不會控預算。」
- 🎙️ 講者這時說：「動手算一次就記住了。一份 10 頁報告約 5000 中文字，乘以 1.8 大概 9000 tokens。加上你要求模型回答的 output tokens，總共約 1 萬 tokens。用 GPT-4o 大約 5 分美金，用 Sonnet 大約 4 分。聽起來便宜？但如果一天跑 1 萬次，月費就是 1.5 萬美金。這就是為什麼 token 計算是系統工程的基本功。」

---

## S6 . CONCEPT-CARD — Self-Attention 的直覺

- 🖼️ 畫面：左欄文字說明 + 右欄 attention heatmap 示意圖（pending real image）
- 📣 畫面上的字：
  - 標題：「每個 token 回頭看所有人，計算『跟我有多相關？』」
  - 左欄：句子「他昨天買的那本書今天到了」→ 「書」回頭看「他」「買」「昨天」→ 權重最高的是「他」和「買」
  - 右欄：attention heatmap 示意（pending real image）
  - Bottom：「這就是 Transformer 能抓長距離語意關聯的核心機制。」
- 🎙️ 講者這時說：「Self-attention 用一句話講就是：每個 token 回頭看所有其他 token，問一個問題——『你跟我有多相關？』然後把相關的資訊加權混進自己的表徵。看這個例子：『他昨天買的那本書今天到了』。當模型處理『書』這個 token 時，它會回頭看整個句子，發現『他』和『買』跟自己最相關——所以它知道這本書是『他買的』，即使隔了好幾個字。RNN 做不到這個，因為它只能一步一步往前看。這就是 Transformer 的核心優勢。」

---

## S7 . CODE — Prompt Engineering 的角色與限制

- 🖼️ 畫面：上方 code panel（prompt 範例）+ 下方三欄「能做 / 不能做 / 解法」
- 📣 畫面上的字：
  - 標題：「好的 prompt = 清楚的指令 + 範例 + 格式約束」
  - Code 範例：
    ```
    system: 你是一位台灣金融法規專家。
    user:   請根據以下條文回答問題，若條文未涵蓋請回答「資訊不足」。
            條文：{context}
            問題：{question}
            請用繁體中文、條列式回答。
    ```
  - 能做：角色設定 / 格式約束 / few-shot 範例 / chain-of-thought
  - 不能做：知識更新（training cutoff）/ 事實查核（無外部來源）/ 大量文件（超出 context window）
  - 解法：RAG / tool use / agent
- 🎙️ 講者這時說：「看這個 prompt 範例——角色設定、指令、格式約束都有了，很完整。但注意三件它做不到的事：第一，模型的知識有 cutoff，今天的新法規它不知道；第二，它沒有外部來源可以查核事實；第三，如果你的條文有 500 頁，塞不進 context window。這三個限制正好是 RAG 的入場理由——接下來我們先學 RAG 的基礎設施：embeddings。」

---

## S8 . CONCEPT-CARD — Embeddings：把文字變成向量

- 🖼️ 畫面：左欄文字 + 右欄 2D 向量空間示意圖（pending real image）
- 📣 畫面上的字：
  - 標題：「語意相近的文字，在向量空間中距離也近」
  - 左欄：「國王」embed → [0.2, 0.8, ...] / 「女王」embed → [0.3, 0.7, ...] / 「蘋果」embed → [0.9, 0.1, ...]
  - 右欄：2D 投影圖——國王/女王 靠在一起，蘋果在遠方（pending real image）
  - Bottom：「Embedding 把語意變成數學——這是 RAG 能找到相關文件的基礎。」
- 🎙️ 講者這時說：「Embedding 做的事就是把一段文字壓成一組數字向量——通常 384 到 1536 維。關鍵在於：語意相近的文字，壓出來的向量也會相近。『國王』和『女王』的向量距離很近，但『國王』和『蘋果』的距離就很遠。這不是人工設計的規則，是 embedding model 從大量文本中學到的語意結構。接下來的 semantic search 就是利用這個特性。」

---

## S9 . CONCEPT-CARD — Semantic Search

- 🖼️ 畫面：流程圖（query → embed → 比對 → top-k 結果）
- 📣 畫面上的字：
  - 標題：「不比對關鍵字，比對語意向量」
  - 流程：User query「退貨流程是什麼？」→ embed → 跟知識庫所有段落的向量比距離 → 回傳最相近的 top-5 段落
  - 對比：Keyword search「退貨」只找有這兩字的文件 / Semantic search 也能找到「商品歸還」「退款申請」等語意相關段落
  - Bottom：「Semantic search 是 RAG 的 retrieval 層——找得準，後面才有好 context。」
- 🎙️ 講者這時說：「傳統 keyword search 靠的是字面匹配——你搜『退貨』，只會找到含有『退貨』兩字的文件。Semantic search 靠的是語意匹配——你搜『退貨』，它也會找到『商品歸還流程』『退款申請步驟』這些字面不同但語意相關的段落。這就是為什麼 RAG 比傳統搜尋強——它理解意思，不只比對字串。」

---

## S10 . MATRIX 1x3 — RAG 三步驟

- 🖼️ 畫面：三欄矩陣 / 每欄標示步驟名 + 做什麼 + 失敗模式
- 📣 畫面上的字：
  - Retrieve：從 vector DB 撈 top-k 相關段落 / 失敗：embedding 不適合、chunk size 太大或太小、metadata filtering 沒做好
  - Augment：把段落塞進 prompt 的 context 區域 / 失敗：context 太長超出 window、段落順序影響 attention、不相關段落稀釋重點
  - Generate：LLM 基於 context 生成回答 / 失敗：LLM 忽略 context 自行發揮（幻覺）、回答格式不符要求、引用錯誤段落
- 🎙️ 講者這時說：「RAG 三步——Retrieve、Augment、Generate——像呼吸一樣要記住。每一步都有自己的失敗模式，這很重要。很多人說『我的 RAG 不準』，但不準到底是哪一步不準？是 retrieval 撈錯段落？是 context 太長 LLM 沒注意到？還是 LLM 看到正確 context 卻自己亂講？Debug RAG 的第一步是定位問題在哪一層。」

---

## S11 . CONCEPT-CARD — RAG 端到端架構圖

- 🖼️ 畫面：完整 RAG pipeline 橫向架構圖（pending real image）
- 📣 畫面上的字：
  - 標題：「從使用者問題到可靠回答的完整管線」
  - 架構：User query → Embedding → Vector DB query → Top-k retrieval → Context assembly → System prompt + User prompt + Context → LLM → Response → Post-processing → Eval → Logging
  - 標註：每個節點標示可能的失敗點（紅色小旗）
  - Bottom：「每一段都是可以獨立測試、獨立最佳化的元件。」
- 🎙️ 講者這時說：「這張圖是本節的核心——請拍下來。從左到右：使用者問問題 → 問題被 embed 成向量 → 去 vector DB 找最相關的段落 → 段落加上 system prompt 組成完整 context → 丟給 LLM 生成回答 → 回答經過 post-processing（格式化、過濾）→ eval 量測品質 → logging 記錄每次呼叫。每個紅色小旗都是可能出錯的地方。這就是為什麼說 GenAI 是系統工程——不是一個模型，是一條管線。」

---

## S12 . CHECKPOINT — 前半段驗收

- 🖼️ 畫面：三欄 Matrix / 每欄一題
- 📣 畫面上的字：
  - Q1：一段 3000 字的中文，大約幾個 tokens？成本怎麼估？
  - Q2：RAG 的三步驟是什麼？每步的失敗模式各一個？
  - Q3：Prompt engineering 做不到的三件事是什麼？解法是什麼？
- 🎙️ 講者這時說：「停下來——不看投影片回答這三題。第一題考 token 計算，第二題考 RAG 三步驟和失敗模式，第三題考 prompt 的限制。答得出來的往下走；答不出來翻回 S4-S10。前半段的基礎不穩，後半段的 agent 和 eval 會很痛苦。」

---

## S13 . CONCEPT-CARD — Tool Use / Function Calling

- 🖼️ 畫面：左欄概念說明 + 右欄 JSON schema 範例
- 📣 畫面上的字：
  - 標題：「讓 LLM 不只回答文字，還能觸發動作」
  - 左欄：LLM 看到使用者問題 → 判斷需要呼叫工具 → 產生 function name + arguments JSON → 系統執行工具 → 結果餵回 LLM → LLM 組成自然語言回答
  - 右欄 Code：
    ```json
    {
      "name": "query_order",
      "parameters": {
        "order_id": "A12345",
        "fields": ["status", "delivery_date"]
      }
    }
    ```
  - Bottom：「Function calling = LLM 決定呼叫什麼工具 + 產生參數；系統負責執行。」
- 🎙️ 講者這時說：「Function calling 的關鍵：LLM 不執行工具，它只決定要呼叫什麼、參數是什麼。實際執行是你的系統做的。這很重要——LLM 負責理解和決策，系統負責執行和安全控制。你可以在執行層加上權限檢查、rate limiting、audit logging，LLM 管不到也不該管。」

---

## S14 . CONCEPT-CARD — Agent：規劃、調用工具、維持狀態

- 🖼️ 畫面：左欄定義 + 右欄 Agent Loop 圖：Observe → Think → Act → Observe（pending real image）
- 📣 畫面上的字：
  - 標題：「Agent = LLM + 規劃能力 + 工具箱 + 記憶體」
  - 左欄：
    - Tool use：單次呼叫，一問一答
    - Agent：多步迴圈，能拆解任務、每步決定下一步
    - OpenAI 定義：agent 能規劃、調用工具、維持狀態完成多步任務
  - 右欄：Observe（接收使用者指令或工具回傳）→ Think（分析現狀、規劃下一步）→ Act（呼叫工具或回答使用者）→ 回到 Observe（pending real image）
  - Bottom：「Agent 不只回答，還能做事——但每多一步就多一個失敗點。」
- 🎙️ 講者這時說：「Tool use 是單次呼叫——使用者問問題，LLM 呼叫一個工具，回傳結果，結束。Agent 是多步迴圈——使用者說『幫我查上季營收並畫成圖表』，agent 要拆成至少兩步：先呼叫資料庫查營收，再呼叫繪圖工具畫圖。每一步都是一次 Observe-Think-Act。這個迴圈是 agent 的核心架構——也是複雜度的來源。」

---

## S15 . PITFALL (P3) — 不要一開始就 multi-agent

- 🖼️ 畫面：VS 左紅「✗」右綠「✓」+ 下方 primary 色 why 條
- 📣 畫面上的字：
  - 左（✗）：一開始就設計 3 個 agent（搜尋 agent / 分析 agent / 報告 agent）→ 互相呼叫 → 每個 agent 各自的 prompt / tool / eval → 失敗模式指數成長
  - 右（✓）：先用 1 個 agent + 3 個 tools 跑通端到端 → eval 穩定後再考慮拆分 → 每次只拆一個步驟出去
  - Why：「Multi-agent 不是更好的 agent——是更多的失敗點。先穩再拆。」
- 🎙️ 講者這時說：「我知道 demo 裡多個 agent 協作看起來很酷，但現實是：每多一個 agent 你就多一組 prompt 要維護、多一組 tool schema 要設計、多一組 eval 要跑、多一個 latency 來源、多一個成本項目。先用單 agent 把流程跑通、eval 穩定、使用者滿意，再考慮拆分。這跟 Ch02 的原則一樣——先把 baseline 做好再上複雜模型。」

---

## S16 . EXAMPLE-I/O — Agent Loop 實例

- 🖼️ 畫面：縱向流程圖（4 步驟）+ 右側每步標注 LLM 的思考
- 📣 畫面上的字：
  - 標題：「從使用者問題到完成任務的完整流程」
  - Step 1 Observe：使用者輸入「幫我查上季營收並畫成長趨勢圖」
  - Step 2 Think：LLM 分析 → 需要兩步：(1) 查資料庫取營收數據 (2) 用數據畫圖 → 先做第一步
  - Step 3 Act：呼叫 `query_revenue(quarter="2025Q4")` → 取得 JSON 數據
  - Step 4 Observe：收到數據 → Think：數據已取得，進行畫圖 → Act：呼叫 `plot_chart(data=..., type="line")` → 回傳圖表給使用者
  - Bottom：「兩步迴圈、兩次工具呼叫、一次完成——但每一步都可能出錯。」
- 🎙️ 講者這時說：「走一遍完整的 agent loop。使用者說『查營收畫圖』——agent 先拆解成兩步，不是隨便拆的，是 LLM 判斷的。第一步呼叫資料庫 tool，拿到數據。第二步用數據呼叫繪圖 tool。注意每一步之間 agent 都會 observe 上一步的結果，re-think 下一步該做什麼。如果第一步查詢失敗呢？好的 agent 會嘗試修正 query 或告訴使用者為什麼失敗——不是無限重試。」

---

## S17 . CONCEPT-CARD — Evals：結構化測試，不要靠感覺

- 🖼️ 畫面：左欄 VS（vibe vs structured）+ 右欄 eval checklist
- 📣 畫面上的字：
  - 標題：「Eval 不是跑幾個 prompt 看看回答好不好」
  - 左欄 VS：
    - Vibe-based：跑 5 個 prompt、人看回答、「感覺不錯」→ 上線
    - Structured：50+ gold set、定義指標、自動化比對、持續跑
  - 右欄 Eval Checklist：
    - ✅ 準備 gold set（有標準答案的測試集）
    - ✅ 定義指標（accuracy / faithfulness / relevance / latency）
    - ✅ 分層評估：retrieval 品質 vs end-to-end 品質分開量
    - ✅ 自動化：每次改 prompt / 換模型都重跑
    - ✅ 覆蓋 edge case + 對抗性 input
- 🎙️ 講者這時說：「Anthropic 的 RAG guide 有一個重要建議：retrieval pipeline 和 end-to-end performance 要分開評估。為什麼？因為你的 retrieval 可能很準但 LLM 亂用 context，或者 retrieval 不準但 LLM 剛好靠自己的知識答對了。分開測才知道問題在哪。這就是結構化 eval 的力量——不是『感覺不錯』，是『哪一層不夠好、差多少、怎麼改』。」

---

## S18 . CHECKPOINT — 後半段驗收

- 🖼️ 畫面：三欄 Matrix / 每欄一題
- 📣 畫面上的字：
  - Q1：Tool use 和 Agent 的核心差異是什麼？
  - Q2：為什麼不建議一開始就用 multi-agent？
  - Q3：Eval checklist 至少要包含哪三項？
- 🎙️ 講者這時說：「再停一次。Q1：tool use 是單次呼叫，agent 是多步迴圈——這個差別決定架構複雜度。Q2：multi-agent 是更多的失敗點，不是更好的 agent。Q3：gold set、指標定義、分層評估。三題都答得出來，你已經有了 GenAI 系統工程的基本功。」

---

## S19 . PITFALL (P4/P5) — Vibe-based Eval 與成本失控

- 🖼️ 畫面：雙列 PITFALL / 上列 P4 + 下列 P5 / 紅色底
- 📣 畫面上的字：
  - P4（上）：「只看 demo 回答不做 eval」→ 上線一個月 task success rate 從 85% 掉到 60% → edge case / 對抗性 input / 多語言 input 全部翻車
  - P5（下）：「開發時不算成本不量 latency」→ 上線後每次呼叫 $0.10 / P95 latency 8 秒 / 月費 $15,000 / 使用者等不及就關掉
  - Bottom：「成本和延遲是系統工程的一部分，不是上線後才最佳化的。」
- 🎙️ 講者這時說：「兩個致命陷阱放在一起講。P4：你在 demo 裡跑了 10 個漂亮的問題，回答都很好，你覺得可以上線了。一個月後客服告訴你：客戶用台語問問題、用簡體字問問題、故意繞 prompt 問問題，全部答錯。Demo 不是 eval。P5：你開發時用 GPT-4、不做 caching、每次都塞滿 context window。上線後帳單 1.5 萬美金，老闆問你能不能用便宜一點的模型——你發現沒做過 eval，不知道換模型品質會掉多少。這兩個陷阱的解藥一樣：從第一天就做 eval + 成本監控。」

---

## S20 . TABLE — GenAI 系統決策矩陣

- 🖼️ 畫面：四列四欄表格 + 底部決策準則
- 📣 畫面上的字：
  - 標題：「何時用什麼策略？」

  | 策略 | 適用場景 | 成本 | 風險 |
  |------|---------|------|------|
  | Prompt Only | 知識不常更新、不需外部文件、風險低 | 最低 | 幻覺、知識過時 |
  | RAG | 知識常更新、需要內部文件、需要引用來源 | 中（vector DB + embedding） | Retrieval 不準、context 稀釋 |
  | Fine-tune | 需改變回答風格/格式、高品質小資料集 | 高（訓練 + hosting） | 過擬合、維護成本 |
  | Agent | 需要多步任務、呼叫外部工具、動態決策 | 最高（多次 LLM 呼叫） | 失敗模式多、latency 高 |

  - Bottom：「從上往下走——先試 prompt only，不夠再加 RAG，還不夠再考慮 fine-tune 或 agent。」
- 🎙️ 講者這時說：「這張表是決策的地圖。從最簡單的開始：prompt only 成本最低、風險最低，能解決就不要往下走。知識常更新或需要內部文件？加 RAG。需要改變模型行為？fine-tune。需要多步任務和工具？agent。每往下走一層，成本和複雜度都在增加。記住這個順序——不要跳級。」

---

## S21 . CONCEPT-CARD — Guardrails / Safety

- 🖼️ 畫面：四層防護架構圖（input → processing → output → monitoring）
- 📣 畫面上的字：
  - 標題：「防護不是可選項——四大風險 x 四層防線」
  - 四大風險：幻覺（答錯）/ Prompt Injection（被操控）/ 越權操作（做錯）/ PII 洩漏（漏錯）
  - 四層防線：
    - Input Layer：input validation + injection detection + rate limiting
    - Processing Layer：context grounding + tool permission control
    - Output Layer：output filtering + citation verification + format check
    - Monitoring Layer：anomaly detection + audit logging + cost alerting
  - Bottom：「每一層可以獨立調整鬆緊度——guardrails 是風險管理，不是什麼都不准做。」
- 🎙️ 講者這時說：「四大風險記一句口訣：答錯、被操控、做錯、漏錯。幻覺是答錯——模型自信地回答了錯誤資訊。Prompt injection 是被操控——有人用惡意 prompt 讓模型做不該做的事。越權操作是做錯——agent 有工具權限但執行了不該執行的動作。PII 洩漏是漏錯——模型在回答中洩漏了個人資料。四層防線對應四個位置：進來之前擋、處理時控制、出去之前過濾、全程監控。」

---

## S22 . PRACTICE-PROMPT — 核心練習

- 🖼️ 畫面：題目描述 + 交付物清單 + 時間限制
- 📣 畫面上的字：
  - 標題：「10 分鐘設計：客服 FAQ 系統」
  - 場景：「你的公司有 500 頁內部規章，客服每天被問 200 次相關問題。老闆要你用 GenAI 做一個自動回答系統。」
  - 交付物：
    - ✅ 選擇策略：Prompt Only / RAG / Fine-tune / Agent？為什麼？
    - ✅ 畫出系統架構（至少包含 retrieval → LLM → response 三個節點）
    - ✅ 列出 3 個 eval 指標
    - ✅ 列出 2 個最大風險 + 對應的 guardrail
  - 時間：10 分鐘獨立思考 + 5 分鐘小組討論
- 🎙️ 講者這時說：「現在是動手時間。這個場景很常見——500 頁文件、200 次日常問答。你要做四件事：選策略、畫架構、定 eval、想風險。10 分鐘後我們小組討論。提示：不要把它想得太複雜，從今天學的決策矩陣開始——先問自己三個問題：知識會更新嗎？需要內部文件嗎？是回答還是執行任務？」

---

## S23 . PYRAMID — GenAI 系統工程五層金字塔

- 🖼️ 畫面：五層金字塔 + 右側每層關鍵詞
- 📣 畫面上的字：
  - 標題：「先穩底層再疊上層」
  - 第 1 層（底）：Token / Context / Parameters — 計算基礎
  - 第 2 層：Embeddings / Semantic Search — 語意基礎
  - 第 3 層：RAG / Prompt Engineering — 知識增強
  - 第 4 層：Tool Use / Agent — 任務執行
  - 第 5 層（頂）：Evals / Guardrails / Cost — 可靠性
  - Bottom：「Ch04 從底層到頂層走了一遍——Ch05 聚焦頂層：評估與治理。」
- 🎙️ 講者這時說：「收束。今天走了五層：從 token 計算開始，到 embedding 語意基礎，到 RAG 知識增強，到 tool use / agent 任務執行，最後到 eval 和 guardrails。這個順序不是隨便排的——底層不穩，上層蓋不住。不會算 token 就不會控成本；embedding 不準 retrieval 就爛；retrieval 爛了 RAG 就沒用；agent 沒有 eval 就是定時炸彈。先穩底層，再疊上層。」

---

## S24 . SILENT — 銜接 Ch05

- 🖼️ 畫面：全藍底 / 白色文字置中
- 📣 畫面上的字：「會蓋系統還不夠，下一步是學會量測它、治理它、讓它可上線。」
- 🎙️ 講者這時說：「今天你學會了 GenAI 系統工程的全貌——從 token 到 agent 到 eval。但會蓋不等於能上線。下一章 Ch05 我們聚焦在：怎麼評估一個 AI 系統夠不夠好？怎麼治理它讓它持續可靠？怎麼從 demo 走到 production？今天的系統工程觀點是地基，Ch05 的評估與治理是讓它真正可上線的最後一哩路。」
