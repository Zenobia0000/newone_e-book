# Ch04 — 生成式 AI 工具、提示工程與 RAG｜講師講稿

> **課程時長**：2 小時（講授 75 min + 模擬考練習 30 min + QA 15 min）
> **受眾定位**：iPAS 初級考生，需掌握 No Code/Low Code、GenAI 工具生態、提示工程與 RAG
> **前置知識**：Ch03 ML 概念與鑑別式/生成式 AI
> **後續銜接**：Ch05 生成式 AI 導入評估與風險管理

---

## 1. 評鑑範圍對照

| 評鑑代碼 | 評鑑名稱 | 本章涵蓋主題 | 預估考題比重 |
|----------|---------|-------------|-------------|
| L121 | No Code/Low Code 概念 | No Code/Low Code 定義、差異、優劣、典型平台、適用場景 | 初級科目二 ~10-15% |
| L122 | GenAI 應用領域與工具 | 主流 GenAI 工具定位、提示工程框架與技巧、RAG 原理、AI 工具整合 | 初級科目二 ~20-25% |

**合計佔比**：初級科目二約 30-40%，是科目二的最大考區。

---

## 2. 目標 (Learning Objectives)

完成本節後，學員應能：

1. 說明 No Code 與 Low Code 的定義、差異、優勢與限制，能判斷場景適合哪種方式。
2. 辨識主流 GenAI 工具的定位與適用場景。
3. 說明提示工程的核心框架與設計原則，能判斷好壞提示。
4. 解釋 RAG 的原理、流程與價值，知道為什麼需要 RAG。
5. 說明 AI 工具整合的概念與常見模式。
6. 面對考題能快速判斷 No Code vs Low Code、提示工程好壞、RAG vs 微調的選型。

---

## 3. 時間切分表

```
00:00-00:08  開場暖身：GenAI 工具考試佔比 + 核心問題引入（S1-S3）
00:08-00:20  No Code / Low Code 概念與差異（S4-S6）
00:20-00:40  GenAI 工具全景：ChatGPT/API/Copilot 系列/Midjourney/Gemini（S7-S12）
00:40-00:58  提示工程：框架/技巧/判斷好壞（S13-S16）
00:58-01:15  RAG 原理 + RAG vs 微調選型（S17-S19）
01:15-01:25  AI 工具整合 + 三層判斷法收束（S20-S21）
01:25-01:30  銜接 Ch05（S22）
01:30-02:00  模擬題演練 + QA
```

---

## 4. 教學重點 (Key Teaching Points)

1. **No Code vs Low Code 是必考送分題**：只要記住一個差異——No Code 完全不寫程式，Low Code 需要少量程式。考題會用各種方式包裝這個差異，但核心就是這一點。再加上各自的優勢和限制就夠了。

2. **GenAI 工具要建地圖不要背清單**：工具太多背不完。用四象限分類（文字/圖片/程式/流程）建立心智地圖，考題給你場景時直接定位到象限，再選工具。

3. **Copilot 家族容易搞混**：VS Code Copilot / GitHub Copilot / Copilot Studio / Microsoft 365 Copilot——名字都有 Copilot 但定位完全不同。GitHub Copilot 是寫程式的，Copilot Studio 是做流程自動化的，Microsoft 365 Copilot 是辦公軟體助手。這是高頻考點。

4. **提示工程用 RTFC 框架教**：Role-Task-Format-Constraint 四要素。不用背複雜的提示工程方法論，記住這四個就能判斷提示好壞。考題會給你兩段提示問哪個比較好——有 RTFC 結構的就是好提示。

5. **RAG 用類比教**：RAG = 帶小抄考試（知識庫是小抄，LLM 是考生）。微調 = 讀完整本書再考（改變了考生的知識）。這個類比可以快速判斷場景該用 RAG 還是微調。

6. **GenAI 工具的限制是隱藏考點**：考題不只考你知不知道工具，還考你知不知道限制——幻覺、知識截止、偏見、隱私風險。每個工具教完都要提一句限制。

---

## 5. 考題陷阱 (Exam Traps)

- **No Code = Low Code 混淆**：「No Code 平台也需要撰寫少量程式碼」→ 錯，那是 Low Code。
- **Copilot Studio = 寫程式**：「Copilot Studio 是用來輔助寫程式碼的工具」→ 錯，是 Low Code 流程自動化平台。
- **提示越長越好**：「提示工程的核心原則是提供越詳細越長的提示」→ 錯，核心是結構化，不是字數。
- **RAG 是一種模型**：「RAG 是一種新型的語言模型」→ 錯，是一種架構模式/方法。
- **GenAI 可以完全取代人工**：「使用 GenAI 工具可以完全不需要人工審核」→ 錯，GenAI 有幻覺風險，需要人類把關。
- **API vs 產品混淆**：「ChatGPT 和 OpenAI API 是同一個東西」→ 錯，ChatGPT 是產品，API 是程式介面。

---

## 6. 提問設計 (Discussion Prompts)

1. 你是一位完全沒有程式能力的行銷經理，想做一個客戶問卷收集工具。你該用 No Code、Low Code、還是找工程師？為什麼？
2. 公司想建一個「能回答公司內部規章制度」的 AI 助手。你會建議用通用 ChatGPT、RAG、還是微調？為什麼？
3. 同事說「我用 ChatGPT 寫程式比用 GitHub Copilot 方便」——你覺得什麼情況他說得對，什麼情況說得不對？

---

## 7. 延伸資源 (Further Reading)

- iPAS 官方學習指引：初級科目二 L121/L122 對應章節
- OpenAI 官方 Prompt Engineering Guide
- LangChain RAG Tutorial（RAG 實作概念理解）
- Microsoft Copilot Studio 官方文件（了解定位差異）

---

## 8. 常見 Q&A

**Q1：提示工程的 Zero-shot/Few-shot/CoT 考試會考嗎？**
A：會。通常考定義辨認——給你一段提示問你用了什麼技巧。Zero-shot 不給範例直接問，Few-shot 給幾個範例，CoT 要求一步步推理。

**Q2：RAG 的技術細節會考嗎？比如 embedding、向量資料庫？**
A：初級不考技術細節。考的是 RAG 解決什麼問題（知識過時/幻覺）、基本流程（檢索→增強→生成）、跟微調的差異。中級才可能涉及 embedding 和向量搜尋。

**Q3：GenAI 工具更新很快，考試會考最新的工具嗎？**
A：考試考的是概念和判斷力，不是特定版本。理解工具的「類型」和「定位」比記住特定功能重要。ChatGPT-4 還是 4o 不重要，重要的是你知道它是通用文字生成 LLM。

**Q4：No Code/Low Code 的具體平台名稱要背嗎？**
A：建議記 2-3 個代表性的。No Code：Bubble、Airtable。Low Code：Power Platform、OutSystems。不需要背所有平台，但要能舉例。
