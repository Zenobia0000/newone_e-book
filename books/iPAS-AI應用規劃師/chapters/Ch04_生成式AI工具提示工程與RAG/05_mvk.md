# Ch04 · 考前速查卡（Minimum Viable Knowledge）

> 考前 30 分鐘翻這張卡，把關鍵判斷刻進短期記憶。
> 對應評鑑範圍：L121 No Code/Low Code 概念 + L122 GenAI 應用領域與工具
> 核心判斷：**工具會用不難，難的是知道什麼時候用、怎麼用對——這正是考試在考的。**

---

## ① No Code vs Low Code（對應 LO1）— 必背對比表

| | No Code | Low Code |
|--|---------|----------|
| 程式碼 | 完全零程式碼 | 少量程式碼 |
| 開發方式 | 拖拉視覺化介面 | 視覺化為主 + 程式碼擴充 |
| 目標用戶 | 非技術人員（業務/行銷/管理者）| 有基礎技術者（公民開發者）|
| 客製化 | 低 | 中 |
| 複雜度上限 | 低 | 中高 |
| 代表平台 | Bubble / Airtable / Zapier | Power Platform / OutSystems / Mendix |

**優勢（共同）**：開發快、成本低、迭代快
**限制（共同）**：平台綁定（vendor lock-in）、效能受限

**一句口訣**：No Code 零程式碼給非技術人員，Low Code 少量程式碼給有底子的人。

---

## ② GenAI 工具四象限地圖（對應 LO2）

```
        文字                     圖片
  ┌─────────────────┬─────────────────┐
  │  ChatGPT        │  Midjourney     │
  │  Gemini         │  DALL-E         │
  │  Claude         │  Stable Diffusion│
  │  （通用對話/寫作）│  （設計/創意）    │
  ├─────────────────┼─────────────────┤
  │  GitHub Copilot │  Copilot Studio │
  │  Cursor         │  Power Automate │
  │  VS Code Copilot│  M365 Copilot   │
  │  （程式碼補全）   │  （流程自動化）   │
  └─────────────────┴─────────────────┘
        程式                     流程
```

**場景決定象限，象限決定工具。**

---

## ③ Copilot 家族辨別（高頻考點）

| 名稱 | 定位 | 用途 | 目標用戶 |
|------|------|------|---------|
| GitHub Copilot | IDE 外掛 | 程式碼自動補全/生成 | 開發者 |
| VS Code Copilot | GitHub Copilot 在 VS Code 的實現 | 同上 | 同上 |
| Copilot Studio | Low Code 平台 | 聊天機器人/工作流程 | 業務/IT |
| Microsoft 365 Copilot | Office 助手 | Word/Excel/PPT 中的 AI | 所有員工 |

**必記**：Copilot Studio 不是寫程式工具！是做流程自動化和聊天機器人的。

---

## ④ ChatGPT vs OpenAI API

| | ChatGPT | OpenAI API |
|--|---------|-----------|
| 定位 | 產品 | 程式介面 |
| 用戶 | 終端用戶 | 開發者 |
| 使用方式 | 網頁/App 直接對話 | 程式碼呼叫 |
| 客製化 | 有限（Custom GPT） | 完全控制（system prompt/參數）|
| 嵌入產品 | 不行 | 可以 |

**口訣**：ChatGPT 是成品直接用，API 是積木拿來蓋。

---

## ⑤ 提示工程速查（對應 LO3）

### RTFC 四要素

| 要素 | 說明 | 範例片段 |
|------|------|---------|
| R = Role 角色 | 設定 AI 的角色/專業 | 「你是一位資深行銷專家」|
| T = Task 任務 | 明確說明要做什麼 | 「請撰寫一篇 500 字的產品介紹」|
| F = Format 格式 | 指定輸出格式 | 「使用條列式重點」|
| C = Constraint 限制 | 設定邊界條件 | 「避免使用專業術語」|

**好提示 = 有 RTFC 結構。壞提示 = 含糊沒結構。**

### 三種提示技巧

| 技巧 | 特徵 | 適用場景 | 辨認方式 |
|------|------|---------|---------|
| Zero-shot | 不給範例直接問 | 簡單明確的任務 | 沒有範例 |
| Few-shot | 給 2-3 個範例 | 需要特定格式/風格 | 有「範例：...」|
| Chain-of-Thought | 要求一步步推理 | 推理/計算/邏輯 | 有「一步步」「讓我們想想」|

---

## ⑥ RAG 速查（對應 LO4）

### RAG 是什麼

- **全名**：Retrieval-Augmented Generation（檢索增強生成）
- **不是模型**，是一種架構模式/方法
- **解決的問題**：LLM 知識過時 + 幻覺（亂編）

### RAG 三步驟

```
Step 1: Retrieve 檢索
  用戶提問 → 從知識庫搜尋相關段落

Step 2: Augment 增強
  問題 + 檢索到的文件 = 增強提示

Step 3: Generate 生成
  增強提示 → LLM → 有依據的回答
```

### RAG vs 微調

| | RAG | 微調 Fine-tuning |
|--|-----|------------------|
| 是否改模型 | 不改 | 改權重 |
| 知識來源 | 外部知識庫 | 訓練資料 |
| 知識更新 | 更新知識庫即可 | 需重新訓練 |
| 成本 | 低 | 高（需 GPU + 資料）|
| 適合場景 | 知識會變動 | 行為要改變 |
| 類比 | 帶小抄考試 | 讀完整本書再考 |

**判斷口訣**：知識更新 → RAG。行為改變 → 微調。

---

## ⑦ GenAI 三大風險（必考）

| 風險 | 說明 | 應對 |
|------|------|------|
| 幻覺 Hallucination | AI 自信地生成錯誤資訊 | 人工審核 + RAG 提供依據 |
| 偏見 Bias | 訓練資料的偏差反映在輸出 | 多元資料 + 輸出檢測 |
| 隱私 Privacy | 機密資料輸入公開 AI 服務 | 企業版/私有部署 + 政策管控 |

**必記**：GenAI 是輔助工具，不能完全取代人工。最後一關永遠是人工審核。

---

## ⑧ 三層工具選擇法（考場武器）

```
Step 1：任務類型是什麼？
         ├── 文字生成 → ChatGPT / Gemini
         ├── 圖片生成 → Midjourney / DALL-E
         ├── 程式輔助 → GitHub Copilot / Cursor
         └── 流程自動化 → Copilot Studio

Step 2：用戶技術能力如何？
         ├── 非技術人員 → No Code
         ├── 有基礎技術 → Low Code
         └── 開發者 → Pro Code (API / SDK)

Step 3：知識需求是什麼？
         ├── 通用知識就夠 → 直接用 LLM
         ├── 需要特定/即時知識 → RAG
         └── 需要改變 AI 行為 → 微調
```

---

## 五個必踩地雷（考前必背）

| # | 地雷 | 錯 | 對 |
|---|------|----|----|
| P1 | No Code = Low Code | 兩者是同一種東西 | No Code 零程式碼，Low Code 少量程式碼 |
| P2 | 提示越長越好 | 字多就是好提示 | 有 RTFC 結構才是好提示 |
| P3 | RAG 是模型 | RAG 是一種新的語言模型 | RAG 是架構模式，結合檢索+生成 |
| P4 | Copilot 都一樣 | Copilot Studio = 寫程式 | GitHub Copilot 寫程式，Copilot Studio 做流程 |
| P5 | GenAI 取代人工 | GenAI 可以不需要人工審核 | GenAI 有幻覺，必須人工把關 |
