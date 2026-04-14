# M7 BCG-Style Narrative（BCG 敘事腳本）

> **文件定位**：把 M7 的 3 小時教材壓縮為一份 BCG-style 顧問簡報腳本。Governing Thought 一句收束、MECE 三支柱切分、12–18 頁的 pyramid、明確的 closing ask。
>
> **用途**：(1) 對外（企業內訓提案、給 CTO / VP Eng 的 30 分鐘簡報）；(2) 對內（講師用這份骨架反推投影片、對齊敘事節奏）。
>
> **風格守則**：每頁一個 message、每頁有 action title、每頁有 takeaway 一句。金句頁單獨成頁、留白多、字少。
>
> **語氣**：內部 review。顧問式、直接、非學術。
> **日期**：2026-04-14。

---

## Governing Thought（核心主張）

> **Choose your path before you choose your framework.**
>
> 在 scikit-learn、PyTorch、PySpark、LangChain 之前，你要先選一條路；否則你學的是工具、不是職涯。

**中文副標**
> 「框架在五年內會換，方向在五年內不會換。先決定你要解什麼問題，再決定你要用什麼工具。」

這句話是整場簡報的錨點。開場第一頁放、金句頁重複、結尾 closing ask 再指一次。

---

## MECE 三支柱

把「資料 / AI 能力」的技術光譜用三根互斥、窮盡的柱子切開：

```
┌───────────────────────────────────────────────────────────┐
│                Governing Thought                          │
│        Choose your path before you choose your framework  │
└───────────────────────────────────────────────────────────┘
        │                    │                    │
 ┌──────▼──────┐      ┌──────▼──────┐      ┌──────▼──────┐
 │  Pillar 1   │      │  Pillar 2   │      │  Pillar 3   │
 │     ML      │      │     DL      │      │ Data Scale  │
 │ 函數逼近     │      │ 可微分程式   │      │ 分散式計算   │
 └──────┬──────┘      └──────┬──────┘      └──────┬──────┘
        │                    │                    │
   scikit-learn         PyTorch 2.x         Arrow / Polars
   Route A / B          Route C             DuckDB / PySpark
                                            Route D
                        ─────────────────────
                         跨支柱：LLM / Agent
                             Route E
```

**MECE 檢驗**
- 互斥性：三支柱切在**問題型態**而非工具（ML = 結構化 + 函數擬合、DL = 表示學習、Data Scale = 計算分散）
- 窮盡性：任何一個 AI/資料任務都能落在某一支柱或跨支柱的交集（Route E 正是 DL × Scale 的交集）

---

## 12–18 頁腳本

每頁格式：**action title（句子，不是標題）｜ supporting points（3 點）｜ takeaway（一句）**。

### 頁 1｜Governing Thought

**Action title**：在選框架之前，先選路

**Supporting**
- 框架 3 年就換一代（PyTorch 0.x → 1.x → 2.x、Spark 2 → 3、LangChain 0 → 1）
- 方向 10 年不變（統計推論、預測建模、表示學習、資料管線、AI 應用）
- 學員卡關的八成原因：學了工具、沒選方向

**Takeaway**：Choose your path before you choose your framework.

---

### 頁 2｜走了多遠（Where you stand）

**Action title**：你已經用 21 小時搭好一座底盤

**Supporting**
- Python + 資料結構 + NumPy + pandas + 統計 + OOP + OS = 一個可以生成生產級工作流的最小集合
- 這組能力是五條路線的**共同前置**，不是任一條的專屬
- 底盤搭完才看得見路，顛倒過來學工具等於盲人摸象

**Takeaway**：你現在站的地方，就是五條路的分岔口。

---

### 頁 3｜三支柱 MECE 總覽

**Action title**：AI/資料的技術光譜有三根柱子，彼此互斥且窮盡

**Supporting**
- Pillar 1 ML：從資料找函數（結構化、可解釋）
- Pillar 2 DL：用可微分的程式組函數（非結構化、表示學習）
- Pillar 3 Data Scale：資料分散 + 計算分散（大規模工程）

**Takeaway**：選路線之前先認柱子，柱子決定你讀哪類論文、用哪類工具、面試哪類職位。

---

### 頁 4｜Pillar 1 — ML 是函數逼近

**Action title**：ML 不是魔法，是在 $\mathcal{H}$ 裡找一個 $\hat f$ 接近 $f^*$

**Supporting**
- 輸入 X、輸出 y、假設空間 $\mathcal{H}$、損失 $L$、優化器——五個成分就能描述整個監督式學習
- scikit-learn 的 `.fit` / `.predict` / `.score` 是這五個成分的**工程化**介面
- 工作流是迴圈：split → train → evaluate → diagnose → iterate

**Takeaway**：會 ML = 會管理 train/val/test + 會解讀評估指標 + 會診斷 bias/variance。

---

### 頁 5｜Pillar 1 — 建模工作流的生死線

**Action title**：切好 train / val / test 決定你這輩子寫的 ML 是否可信

**Supporting**
- 三分割、不是兩分割：val 調參、test 只動一次
- 四種 leakage（預處理 / 時間 / target / group）每一個都會讓你 demo 漂亮、上線崩盤
- CV 五種：KFold、Stratified、Group、TimeSeries、Repeated——選錯等於沒切

**Takeaway**：leakage 是 ML 工程師一輩子的敵人，入門第一天就要認識它。

---

### 頁 6｜Pillar 2 — DL 是可微分程式

**Action title**：把模型寫成計算圖，讓梯度自己走回來

**Supporting**
- tensor = ndarray + device + grad + dtype 政策
- autograd tape 自動記錄每個 op 的反向函數，`loss.backward()` 沿 tape 填梯度
- 訓練迴圈永恆六行：forward / loss / zero_grad / backward / step / log

**Takeaway**：DL 不是新數學，是新的程式寫法。

---

### 頁 7｜Pillar 2 — PyTorch 2 的轉折

**Action title**：DL 的下一步是效能工程，不是新模型

**Supporting**
- `torch.compile()` 把 eager 的開發體驗 + graph 的執行效能合併（TorchDynamo + Inductor）
- 效能旋鈕三件套：混合精度（bf16/fp16）、`pin_memory`/`non_blocking`、DataLoader `num_workers`
- CUDA stream 非同步執行——不 `synchronize` 量到的時間都是假的

**Takeaway**：寫得出模型是入場券，跑得快跑得穩才是真本事。

---

### 頁 8｜金句頁（full-bleed quote slide）

> **"You're not picking a library.
> You're picking a problem shape."**
>
> —— 選 scikit-learn vs PyTorch vs PySpark，本質上是在選你要解的問題長什麼樣。

（整頁留白，只有這兩行 + 底部小字 attribution）

---

### 頁 9｜Pillar 3 — 當 pandas 不夠用時

**Action title**：工具選擇不是品味，是尺寸

**Supporting**
- < 1 GB：pandas（Arrow backend 更快）
- 1–100 GB 單機：Polars（lazy）/ DuckDB（SQL on file）
- 100 GB+ 或 Lakehouse：PySpark

**Takeaway**：沒有最好的工具，只有對應規模的工具。

---

### 頁 10｜Pillar 3 — PySpark 的心智模型

**Action title**：lazy + DAG + shuffle 是大數據三件事

**Supporting**
- transformation 是 lazy、action 才觸發 job
- stage 邊界由 shuffle 決定；shuffle 比 narrow op 貴 100–1000 倍
- `broadcast join`、AQE、`explain(formatted)` 是入門三把鑰匙

**Takeaway**：會 Spark ≠ 會寫 `df.groupBy`，會 Spark = 會讀 `explain` 並能算 shuffle cost。

---

### 頁 11｜跨支柱 — LLM / RAG / Agent 的落地現實

**Action title**：LLM 的難處在於 retrieval、eval、cost，不在 prompt

**Supporting**
- RAG 的上限由 retrieval 品質決定（chunking、hybrid search、reranking）
- Agent 的失效模式是結構化的：schema 錯、無窮迴圈、context 爆、eval 難做
- 生產工程四件套：prompt 版控、trace observability、cost/latency budget、guardrails

**Takeaway**：Route E 不是「寫 prompt」的職位，是「經營 AI 系統」的職位。

---

### 頁 12｜金句頁（full-bleed quote slide）

> **"先會寫，再會組；
> 先懂資料，再懂系統；
> 先搭底盤，再碰 AI。"**

（整頁只有三行中文、極大字、大量留白）

---

### 頁 13｜五條路線總覽

**Action title**：同一個底盤，五條真實職涯

| 路線 | 核心問題 | 核心工具 |
|---|---|---|
| A 統計 | 這現象真實還是噪聲？ | scipy / statsmodels / SQL |
| B ML 工程 | 怎麼把預測系統穩定上線？ | sklearn / XGBoost / MLflow |
| C 深度學習 | 怎麼讓模型自己學表示？ | PyTorch / CUDA / Triton |
| D 資料工程 | 資料怎麼可靠流動？ | Spark / dbt / Airflow |
| E AI 應用 | 怎麼讓 LLM 解真問題？ | LangChain / 向量 DB / eval |

**Takeaway**：選的不是「學什麼」，是「為什麼學」。

---

### 頁 14｜路線的分歧決策樹（Closing Ask 的核心視覺）

**Action title**：用三個問題、兩分鐘，選出你的下一步

```
            你對哪種問題最感到好奇？
                     │
     ┌───────────────┼────────────────┐
     │               │                │
   推論          預測/建模           系統/管線
     │               │                │
     ▼               ▼                ▼
 Route A         非結構化？         資料 or AI？
                    │                  │
              ┌─────┴─────┐      ┌─────┴─────┐
              是         否      資料       AI
              ▼          ▼       ▼          ▼
          Route C   Route B   Route D    Route E
```

**Takeaway**：不是終身承諾，是 30 天承諾——選一條，走 30 天，再回來評估。

---

### 頁 15｜每條路線的 30 天啟動包

**Action title**：30 天內做一件能放進 portfolio 的事

| 路線 | 30 天 milestone |
|---|---|
| A | 一個 A/B test 的完整報告（含 power analysis） |
| B | 一個端到端 sklearn pipeline + MLflow tracking |
| C | 一個 PyTorch 微調專案（HuggingFace 模型 + 自訂資料） |
| D | 一個 Airflow + Spark 的每日 ETL + 資料品質檢查 |
| E | 一個 RAG + eval harness + cost dashboard 的 demo |

**Takeaway**：「做出來」比「學會了」值錢一個數量級。

---

### 頁 16｜金句頁（full-bleed quote slide）

> **"You didn't learn a tool.
> You built a foundation."**
>
> 工具會換，底盤不換。

---

### 頁 17｜Closing Ask

**Action title**：離開這間教室前，做一件事

**三個請求**（對學員）
1. **選一條路線**——在課後 7 天內決定（不是一輩子，是 30 天）
2. **找一個真問題**——不是 kaggle、是你遇到的
3. **走到第一次碰壁**——碰壁的點就是你的下一個學習目標

**一個請求**（對組織贊助方）
> 把這門課的 checklist（見 M7_annotated/02 透鏡二）當成團隊能力地圖，在 3 / 6 / 12 個月各評一次，建立持續的 upskilling loop。

---

### 頁 18｜回到 Governing Thought

**Action title**：回到起點那句話

> **Choose your path before you choose your framework.**

你在這 3 小時學的不是 scikit-learn、不是 PyTorch、不是 PySpark——你學的是**辨認自己站在哪根柱子前面**。

**Takeaway**：底盤已搭好，路已畫好，下一步你決定。

---

## 金句頁索引（full-bleed quote slides）

| 頁次 | 金句 |
|---|---|
| 頁 1 | Choose your path before you choose your framework. |
| 頁 8 | You're not picking a library. You're picking a problem shape. |
| 頁 12 | 先會寫，再會組；先懂資料，再懂系統；先搭底盤，再碰 AI。 |
| 頁 16 | You didn't learn a tool. You built a foundation. |
| 頁 18 | (回到頁 1) Choose your path before you choose your framework. |

金句頁的設計原則：**整頁一句、字夠大、夠安靜**。聽眾記不住投影片，但記得住金句頁。這五張就是本簡報的「記憶鉤」。

---

## Pyramid 結構檢驗

```
                    Choose your path before
                    you choose your framework
                           (Governing)
                    ┌──────────┼──────────┐
                    │          │          │
                   ML         DL       Data Scale
                (Pillar 1)(Pillar 2) (Pillar 3)
                    │          │          │
              ┌─────┼─────┐   │      ┌───┼───┐
             工作流 leakage CV  PyT2  pandas Spark
                    │     │        邊界  lazy
                    ▼     ▼         ▼     ▼
                  頁4–5 頁6–7      頁9  頁10
                                  (跨柱: 頁11 LLM)
                                       ▼
                                 五條路線 頁13–15
                                       ▼
                                 Closing 頁17
```

**MECE 最終檢驗**
- 三支柱互斥：以「問題型態」切，不重疊
- 三支柱窮盡：任何 AI/資料問題可歸屬一柱或交集
- 路線與柱子的對位：A 在 Pillar 1；B 在 Pillar 1；C 在 Pillar 2；D 在 Pillar 3；E 在 Pillar 2 × Pillar 3 的交集

這是 BCG-style 簡報要的東西：**一個 Governing Thought、一個 MECE 結構、一組金句、一個清楚的 ask**。講者照這份腳本走，45 分鐘一次、不看稿也能講。

— end of BCG narrative —
