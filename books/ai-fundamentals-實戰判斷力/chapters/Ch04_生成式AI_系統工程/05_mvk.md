# Ch04 . MVK 速學卡（Minimum Viable Knowledge）

> 離開本節後，你的肌肉記憶裡必須長出這五個反射。
> 對應 01_outline.md 的 7 個 Learning Objectives。

---

## ① Token / Context 計算（對應 LO1）

```
中文 1 字 ≈ 1.5-2 tokens（BPE 分詞，比英文貴）
英文 1 word ≈ 1-1.3 tokens

範例：一份 10 頁中文報告 ≈ 5000 字 ≈ 9000 tokens
     + 預估 output 1000 tokens = 總計 10,000 tokens
     GPT-4o 成本 ≈ $0.05 / Claude Sonnet ≈ $0.04

Context Window = input tokens + output tokens（合計上限）
Parameters = 模型學過的知識量（70B / 405B）
```

**一句口訣**：Token 是最小計費單位，Context Window 是一次能塞多少，Parameters 是模型能力上限。

---

## ② RAG 三步驟（對應 LO4 + LO5）

```
Step 1  Retrieve   從 vector DB 撈 top-k 相關段落
        ↓          失敗模式：embedding 不適合、chunk size 不對、metadata filtering 沒做好
Step 2  Augment    把段落塞進 prompt 的 context 區域
        ↓          失敗模式：context 太長超出 window、不相關段落稀釋重點
Step 3  Generate   LLM 基於 context 生成回答
                   失敗模式：LLM 忽略 context 自行發揮（幻覺）、引用錯誤段落
```

**一句口訣**：撈段落 → 塞 context → 讓 LLM 照著答。Debug RAG 先定位問題在哪一層。

**Anthropic 建議**：retrieval pipeline 和 end-to-end performance 要**分開評估**。

---

## ③ Agent Loop（對應 LO6）

```
          ┌─────────────────────────┐
          │                         │
          ▼                         │
    ┌──────────┐   ┌──────────┐   ┌──────────┐
    │ Observe  │──▶│  Think   │──▶│   Act    │
    │ 看到什麼？│   │ 該做什麼？│   │ 執行什麼？│
    └──────────┘   └──────────┘   └────┬─────┘
                                       │
                                       ▼
                                 任務完成？
                                 Yes → 回傳使用者
                                 No  → 回到 Observe
```

**Tool Use vs Agent 的區分**：

| 維度 | Tool Use / Function Calling | Agent |
|------|---------------------------|-------|
| 步數 | 單次呼叫 | 多步迴圈 |
| 規劃 | 不需要 | 需要（拆解任務） |
| 狀態 | 無狀態 | 維持狀態（記憶體） |
| 複雜度 | 低 | 高（每步都是失敗點） |

**判斷準則**：任務能一步完成 → tool use；需要多步 + 動態決策 → agent。先把單 agent 做穩，不要跳 multi-agent。

---

## ④ Eval Checklist（對應 LO7）

```
✅ Gold Set         準備有標準答案的測試集（50-100 起步）
✅ 指標定義         accuracy / faithfulness / relevance / latency / cost
✅ 分層評估         retrieval 品質 vs end-to-end 品質分開量
✅ 自動化           每次改 prompt / 換模型都重跑 eval
✅ Edge Case        多語言 / 長文 / 模糊問題 / 對抗性 input
✅ 持續監控         上線後持續跑 eval，不是部署完就結束
```

**鐵律**：不要 vibe-based evaluation。「感覺不錯」不是 eval，「task success rate 87%，比上版提升 3%」才是 eval。

---

## ⑤ GenAI 系統架構圖（對應全章）

```
User Query
    │
    ▼
┌─────────────┐     ┌──────────────┐
│ Embedding   │────▶│  Vector DB   │
│ Model       │     │  (top-k)     │
└─────────────┘     └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   Context    │◀── System Prompt
                    │  Assembly    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │     LLM      │──── Tool Call? ──▶ External Tool
                    └──────┬───────┘                        │
                           │◀───────────────────────────────┘
                           ▼
                    ┌──────────────┐
                    │    Post-     │
                    │  processing  │
                    └──────┬───────┘
                           │
                    ┌──────┴───────┐
                    ▼              ▼
              ┌──────────┐  ┌──────────┐
              │   Eval   │  │ Logging  │
              └──────────┘  └──────────┘
```

**每個節點都是可以獨立測試、獨立最佳化的元件。**

---

## 決策矩陣速查（考前必背）

| 策略 | 何時用 | 何時不用 |
|------|--------|---------|
| Prompt Only | 知識不常更新、風險低、不需外部文件 | 知識常更新、需要引用來源 |
| RAG | 知識常更新、需要內部文件、需要引用來源 | 不需要外部知識、模型自身知識就夠 |
| Fine-tune | 需改變回答風格/格式、有高品質小資料集 | 知識常更新（fine-tune 後無法即時更新） |
| Agent | 需要多步任務、呼叫工具、動態決策 | 單步就能完成、不需要工具 |

**順序**：先試 Prompt Only → 不夠加 RAG → 還不夠考慮 Fine-tune 或 Agent。不要跳級。

---

## 五個必踩地雷（考前必背）

| # | 地雷 | 症狀 | 解藥 |
|---|------|------|------|
| P1 | Prompt 萬能論 | 知識過時、幻覺、無法引用來源 | 加 RAG |
| P2 | RAG 萬靈丹 | Retrieval 不準，LLM 再強也救不回 | 分層 eval，先修 retrieval |
| P3 | 過早 multi-agent | 失敗模式指數成長、latency 爆炸 | 先用單 agent + 多 tools |
| P4 | Vibe-based eval | 上線後 edge case 翻車 | Gold set + 指標 + 自動化 |
| P5 | 忽略成本/延遲 | 月費 $15K、P95 latency 8 秒 | 從第一天就做成本監控 |

---

## 下一章銜接（Ch05 評估與治理 — 可上線系統）

> Ch05 在 Ch04 的系統工程觀點上加三層：
> - **評估框架**：從 eval checklist 延伸到完整的評估方法論（offline eval / online eval / A/B test）
> - **治理策略**：從 guardrails 延伸到組織層級的 AI 治理（policy / audit / compliance）
> - **上線準備**：從 demo 到 production 的 checklist（monitoring / alerting / rollback / SLA）
>
> **今天的系統架構圖是地基**；沒有地基，Ch05 的評估與治理沒處量、沒處管。
