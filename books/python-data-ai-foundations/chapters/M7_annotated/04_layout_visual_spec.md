# M7 Layout & Visual Spec（版面與視覺規格）

> **文件定位**：這份文件是 M7 投影片 / 講義 / 書籍版型的視覺規格書。面向設計師、排版工程師、講義製作團隊。規範 grid、字體、色票、資訊圖規格、圖表 mermaid 原始碼。
>
> **使用方式**：依此檔案可直接在 Figma / Keynote / Reveal.js / LaTeX Beamer / Quarto 等工具建立一致的版型。色票以 hex 表示，字體以開源可商用字型為主。
>
> **語氣**：內部 review。規格文件，不解釋設計哲學，直接給尺寸。
> **日期**：2026-04-14。

---

## 1. Grid 系統

### 1.1 投影片（16:9, 1920×1080）

- Base grid：**12 columns × 6 rows**
- Gutter：24 px
- Margin：64 px（左右）/ 48 px（上下）
- Safe area：1792 × 984 px

```
│ 64 │   12 cols × 128 px 寬 + 24 px gutter    │ 64 │
```

**layout preset（五種）**
| preset | 用途 | 內容區 |
|---|---|---|
| L1 cover | 封面/分節頁 | title 居中、副標下置 |
| L2 quote | 金句頁 | 單欄居中、字 96pt |
| L3 content-1col | 單欄內文 | 12 cols 全寬、Action title + 3 bullets + takeaway |
| L4 content-2col | 雙欄（文+圖） | 5 cols 文 / 7 cols 圖 |
| L5 full-viz | 全幅資訊圖 | 12 cols × 5 rows、底部 1 row 放 caption |

### 1.2 講義/書籍內頁（A4, 210×297 mm）

- Base grid：**8 columns × 12 rows**
- Gutter：4 mm
- Margin：20 mm（內外）/ 24 mm（上下）
- Footer reserved：10 mm（頁碼 + 章節）

---

## 2. 字體

### 2.1 字型家族

| 用途 | 字型 | 授權 |
|---|---|---|
| 中文內文 | Noto Sans TC / 思源黑體 | OFL |
| 中文強調 | Noto Serif TC / 思源宋體 | OFL |
| 英文內文 | Inter | OFL |
| 英文 code | JetBrains Mono | OFL |
| 數學公式 | STIX Two Math | OFL |

**不使用** Microsoft YaHei、PingFang（授權風險）。

### 2.2 字級階層（投影片）

| tier | size | line-height | 用途 |
|---|---|---|---|
| T1 display | 96 pt | 1.1 | 金句頁 |
| T2 title | 56 pt | 1.2 | 分節頁標題 |
| T3 action title | 36 pt | 1.3 | 每頁 action title |
| T4 body | 24 pt | 1.5 | bullet 內文 |
| T5 caption | 18 pt | 1.4 | 圖表 caption / takeaway |
| T6 footnote | 14 pt | 1.4 | 頁碼 / attribution |

### 2.3 字級階層（講義）

| tier | size | line-height |
|---|---|---|
| H1 | 24 pt | 1.3 |
| H2 | 18 pt | 1.3 |
| H3 | 14 pt | 1.3 |
| body | 11 pt | 1.6 |
| caption | 9 pt | 1.4 |
| code | 10 pt | 1.5 |

---

## 3. 色票

### 3.1 主色系統（Foundation Neutral + 三支柱強調色）

```
Foundation（中性底色）
─────────────────────
ink        #0F172A   主要文字
graphite   #334155   次要文字
slate      #64748B   caption / 輔助
mist       #E2E8F0   分隔線
paper      #F8FAFC   背景
white      #FFFFFF   畫布

Pillar accents（三支柱強調色）
──────────────────────────
pillar-ml      #2563EB   (Pillar 1 — ML / 函數逼近)     深藍
pillar-dl      #9333EA   (Pillar 2 — DL / 可微分程式)    紫
pillar-scale   #059669   (Pillar 3 — Data Scale)        深綠

Semantic（語意色）
─────────────────
success    #16A34A
warning    #F59E0B
danger     #DC2626
info       #0EA5E9
```

### 3.2 路線色（Route A–E）

與三支柱獨立、用於職涯地圖：

```
Route A 統計      #0EA5E9   天青（推論）
Route B ML        #2563EB   寶藍（與 Pillar-ML 同色系，深一階）
Route C DL        #9333EA   紫（與 Pillar-DL 同）
Route D DE        #059669   深綠（與 Pillar-Scale 同）
Route E LLM       #EA580C   橘（跨支柱標記色）
```

### 3.3 對比度檢驗

所有正文色對背景色需 ≥ WCAG AA（4.5:1）。投影片大字可放寬到 AA-Large（3:1）。code block 底色使用 `#F1F5F9` + `ink` 文字（對比 10.3:1）。

---

## 4. 資訊圖規格（5 張核心視覺）

### 4.1 資訊圖 #1 — 五條路線 Roadmap

**用途**：S11 / BCG 頁 13–14。
**尺寸**：full-viz（12 cols × 5 rows）。
**布局**：左側「畢業點」圓盤（240 px 直徑）、右側輻射出五條路線，每條路線是一條時間軸（0–30 天、30–90 天、90 天+ 三個里程碑節點）。
**配色**：五條路線各用其 Route 色、畢業點用 `ink`、時間軸用 `graphite`。
**節點 icon**：30 天 = 實心圓、90 天 = 雙圈、90+ = 三角（代表開放方向）。
**caption**：底部一行「同一個底盤，五條真實職涯。」T5 caption 大小。

### 4.2 資訊圖 #2 — scikit-learn Pipeline 結構

**用途**：S04 / S05 / 講義附錄。
**尺寸**：content-2col 的圖區（7 cols × 4 rows）。
**布局**：水平流程圖，從左到右：
```
[raw df] → [ColumnTransformer] → [Estimator (.fit/.predict)] → [eval]
```
**細節**：
- ColumnTransformer 內分上下兩格：numeric（StandardScaler）/ categorical（OneHotEncoder）
- Estimator 下方標示 `.fit` / `.predict` / `.score` / `.get_params` 四個方法
- 箭頭上方寫 dtype（DataFrame → ndarray → ndarray → float）
**配色**：`pillar-ml` 主色、處理節點用 `mist` 底 + `ink` 字。

### 4.3 資訊圖 #3 — PyTorch 訓練迴圈

**用途**：S07 / S08 / Route C 參考。
**尺寸**：content-2col 的圖區。
**布局**：垂直循環箭頭圖，六個節點：
```
forward → loss → zero_grad → backward → step → log
  ↑                                              │
  └──────────────────────────────────────────────┘
```
**細節**：
- 每個節點標示一行 PyTorch 代碼
- 在 `backward` 右側掛一個「autograd tape」圖示（虛線框住 forward → loss）
- 在 `step` 下方標 `optimizer.zero_grad()` 的位置含義
**配色**：`pillar-dl` 主色、tape 框用虛線 `slate`。

### 4.4 資訊圖 #4 — PySpark 執行計畫 DAG

**用途**：S10 / Route D 參考。
**尺寸**：full-viz。
**布局**：Catalyst 分三層展示：
```
邏輯計畫（LogicalPlan）→ 優化後邏輯計畫 → 物理計畫（PhysicalPlan）
                                             │
                                             ▼
                                    stage 1 ──shuffle── stage 2
                                       │                   │
                                  narrow op            narrow op
```
**細節**：
- stage 邊界用紅色虛線 + 「shuffle boundary」標示
- 每個 stage 內畫 3–5 個 task（小方塊）
- 底部放一個 mini code snippet 展示 `df.explain(mode="formatted")` 的前 5 行輸出
**配色**：`pillar-scale` 主色、shuffle 邊界 `danger` 色。

### 4.5 資訊圖 #5 — 職涯地圖 2×2 Matrix

**用途**：BCG 頁 13 補充 / S11 延伸。
**尺寸**：content-1col 置中（8 cols × 4 rows）。
**兩軸**：
- X：資料型態（結構化 ← → 非結構化）
- Y：工作角色（建模/分析 ← → 系統/工程）

```
                   系統 / 工程
                        │
           Route D     │    Route E
        (結構化+工程)   │  (非結構化+工程)
                        │
  結構化 ────────────────┼──────────────── 非結構化
                        │
           Route A/B    │    Route C
         (結構化+建模)   │  (非結構化+建模)
                        │
                   建模 / 分析
```

**細節**：Route E 跨在右上象限但延伸箭頭指向其他象限（代表 LLMOps 在合流）。
**配色**：四象限用極淡色底（`paper` + 10% Route 色）、Route 名稱用該 Route 色、箭頭用 `graphite`。

---

## 5. Mermaid 片段

以下 5+ 個 mermaid diagram 可直接貼進講義/書籍渲染。繁體中文標籤，使用 `graph` / `flowchart` / `sequenceDiagram` 等。

### 5.1 Mermaid #1 — 三支柱 MECE（BCG 頁 3）

```mermaid
flowchart TB
  GT["<b>Governing Thought</b><br/>Choose your path<br/>before you choose your framework"]:::governing
  ML["Pillar 1<br/><b>ML</b><br/>函數逼近"]:::ml
  DL["Pillar 2<br/><b>DL</b><br/>可微分程式"]:::dl
  DS["Pillar 3<br/><b>Data Scale</b><br/>資料分散 + 計算分散"]:::scale
  GT --> ML
  GT --> DL
  GT --> DS
  ML --> RA["Route A 統計"]:::routeA
  ML --> RB["Route B ML 工程"]:::routeB
  DL --> RC["Route C 深度學習"]:::routeC
  DS --> RD["Route D 資料工程"]:::routeD
  DL -.-> RE["Route E LLM 應用"]:::routeE
  DS -.-> RE

  classDef governing fill:#0F172A,color:#fff,stroke:#0F172A
  classDef ml fill:#2563EB,color:#fff,stroke:#1D4ED8
  classDef dl fill:#9333EA,color:#fff,stroke:#7E22CE
  classDef scale fill:#059669,color:#fff,stroke:#047857
  classDef routeA fill:#E0F2FE,color:#0F172A,stroke:#0EA5E9
  classDef routeB fill:#DBEAFE,color:#0F172A,stroke:#2563EB
  classDef routeC fill:#F3E8FF,color:#0F172A,stroke:#9333EA
  classDef routeD fill:#D1FAE5,color:#0F172A,stroke:#059669
  classDef routeE fill:#FFEDD5,color:#0F172A,stroke:#EA580C
```

### 5.2 Mermaid #2 — scikit-learn 建模工作流（S05）

```mermaid
flowchart LR
  A["原始 DataFrame"]:::data --> B["train_test_split<br/>(含 stratify + random_state)"]:::split
  B --> C["訓練集 X_train, y_train"]:::train
  B --> D["驗證集 X_val, y_val"]:::val
  B --> E["測試集 X_test, y_test<br/>⚠️ 只動一次"]:::test
  C --> F["Pipeline<br/>前處理 + 模型"]:::model
  F --> G[".fit()"]:::op
  G --> H["在 val 上評估"]:::eval
  H -->|不滿意| I["診斷 + 迭代<br/>過擬合/欠擬合/資料問題"]:::diag
  I --> F
  H -->|鎖定模型| J["在 test 上做最終報告"]:::final

  classDef data fill:#F8FAFC,stroke:#64748B
  classDef split fill:#DBEAFE,stroke:#2563EB
  classDef train fill:#E0F2FE,stroke:#0EA5E9
  classDef val fill:#FEF3C7,stroke:#F59E0B
  classDef test fill:#FEE2E2,stroke:#DC2626
  classDef model fill:#DBEAFE,stroke:#2563EB
  classDef op fill:#fff,stroke:#2563EB
  classDef eval fill:#D1FAE5,stroke:#059669
  classDef diag fill:#FEF3C7,stroke:#F59E0B
  classDef final fill:#DCFCE7,stroke:#16A34A
```

### 5.3 Mermaid #3 — PyTorch 訓練迴圈 + autograd tape（S07/S08）

```mermaid
flowchart TB
  subgraph tape["autograd tape (動態計算圖)"]
    F1["x"] --> F2["linear1"]
    F2 --> F3["relu"]
    F3 --> F4["linear2"]
    F4 --> F5["loss"]
  end
  F5 --> B1["loss.backward()<br/>沿 tape 反向填 .grad"]:::backward
  B1 --> S1["optimizer.step()<br/>參數更新"]:::step
  S1 --> Z1["optimizer.zero_grad()<br/>清空 .grad 給下一批"]:::zero
  Z1 --> F1
  S1 --> L1["log: loss / metric"]:::log

  classDef backward fill:#F3E8FF,stroke:#9333EA
  classDef step fill:#DBEAFE,stroke:#2563EB
  classDef zero fill:#E2E8F0,stroke:#64748B
  classDef log fill:#D1FAE5,stroke:#059669
```

### 5.4 Mermaid #4 — PySpark 執行模型：lazy → action → DAG（S10）

```mermaid
flowchart LR
  T1["df.filter(...)"]:::lazy --> T2["df.select(...)"]:::lazy
  T2 --> T3["df.groupBy(...).agg(...)"]:::lazy
  T3 --> T4["df.join(other, ...)"]:::lazy
  T4 --> A1["df.show() / .write()<br/><b>action 觸發 job</b>"]:::action
  A1 --> C1["Catalyst 優化器"]:::catalyst
  C1 --> P1["Physical Plan"]:::plan
  P1 --> ST1["Stage 1<br/>narrow ops"]:::stage
  ST1 -->|shuffle| ST2["Stage 2<br/>reduce/join"]:::stage
  ST2 --> OUT["結果"]:::out

  classDef lazy fill:#F8FAFC,stroke:#64748B,stroke-dasharray:5 5
  classDef action fill:#FEE2E2,stroke:#DC2626
  classDef catalyst fill:#D1FAE5,stroke:#059669
  classDef plan fill:#DCFCE7,stroke:#16A34A
  classDef stage fill:#DBEAFE,stroke:#2563EB
  classDef out fill:#fff,stroke:#0F172A
```

### 5.5 Mermaid #5 — 五條路線職涯地圖（S11 / BCG 頁 13）

```mermaid
flowchart TB
  HUB(("🎓<br/>M1–M7<br/>畢業底盤")):::hub
  HUB --> A["Route A<br/>統計分析<br/>A/B test · 推論 · BI"]:::rA
  HUB --> B["Route B<br/>ML 工程<br/>sklearn · XGBoost · MLflow"]:::rB
  HUB --> C["Route C<br/>深度學習<br/>PyTorch · CUDA · Transformer"]:::rC
  HUB --> D["Route D<br/>資料工程<br/>Spark · Airflow · Lakehouse"]:::rD
  HUB --> E["Route E<br/>LLM 應用<br/>RAG · Agent · Eval"]:::rE

  A -.合流.-> B
  B -.合流.-> D
  C -.合流.-> E
  D -.合流.-> E

  classDef hub fill:#0F172A,color:#fff,stroke:#0F172A,stroke-width:3px
  classDef rA fill:#E0F2FE,color:#0F172A,stroke:#0EA5E9,stroke-width:2px
  classDef rB fill:#DBEAFE,color:#0F172A,stroke:#2563EB,stroke-width:2px
  classDef rC fill:#F3E8FF,color:#0F172A,stroke:#9333EA,stroke-width:2px
  classDef rD fill:#D1FAE5,color:#0F172A,stroke:#059669,stroke-width:2px
  classDef rE fill:#FFEDD5,color:#0F172A,stroke:#EA580C,stroke-width:2px
```

### 5.6 Mermaid #6（bonus）— 路線分岔決策樹（BCG 頁 14）

```mermaid
flowchart TB
  Q1{"你最感興趣的<br/>問題類型？"}:::q
  Q1 -->|為什麼是這樣？| A["Route A 統計"]:::rA
  Q1 -->|能不能預測更準？| Q2{"資料型態？"}:::q
  Q1 -->|資料/系統如何運作？| Q3{"資料 or AI 系統？"}:::q
  Q2 -->|結構化| B["Route B ML 工程"]:::rB
  Q2 -->|非結構化| C["Route C 深度學習"]:::rC
  Q3 -->|資料管線| D["Route D 資料工程"]:::rD
  Q3 -->|AI 管線| E["Route E LLM 應用"]:::rE

  classDef q fill:#F8FAFC,stroke:#0F172A,stroke-width:2px
  classDef rA fill:#E0F2FE,stroke:#0EA5E9
  classDef rB fill:#DBEAFE,stroke:#2563EB
  classDef rC fill:#F3E8FF,stroke:#9333EA
  classDef rD fill:#D1FAE5,stroke:#059669
  classDef rE fill:#FFEDD5,stroke:#EA580C
```

### 5.7 Mermaid #7（bonus）— tensor vs ndarray 的三個差異

```mermaid
flowchart LR
  ND["NumPy ndarray"]:::nd --> DIFF1["+ device<br/>（CPU / CUDA / MPS）"]:::diff
  ND --> DIFF2["+ requires_grad<br/>（autograd 追蹤）"]:::diff
  ND --> DIFF3["+ dtype 政策<br/>（fp32/bf16 預設）"]:::diff
  DIFF1 --> T["PyTorch tensor"]:::t
  DIFF2 --> T
  DIFF3 --> T

  classDef nd fill:#E0F2FE,stroke:#0EA5E9
  classDef diff fill:#FEF3C7,stroke:#F59E0B
  classDef t fill:#F3E8FF,stroke:#9333EA,stroke-width:2px
```

---

## 6. 圖示與 icon 規格

- 線寬一致：1.5 px（細）/ 2.5 px（粗強調）
- 圓角半徑：4 px（小方塊）/ 12 px（大卡片）
- 陰影：`0 2px 8px rgba(15, 23, 42, 0.08)`（輕微浮起）
- icon set：Lucide Icons（MIT，線性風格、與 Inter 字型搭配和諧）

---

## 7. 程式碼區塊樣式

```
背景：#F1F5F9
文字：#0F172A
行高：1.5
font：JetBrains Mono 10pt (講義) / 20pt (投影片)
highlight line：背景 #FEF3C7
error line：背景 #FEE2E2 + 左側紅色 2px 標記條
```

**語言標記**：code block 右上角小標籤（10pt、slate 色）顯示 `python` / `bash` / `sql`。

---

## 8. 版型一致性檢查表（ship 前必跑）

- [ ] 所有投影片都有 action title（非名詞性標題）
- [ ] 所有內容頁都有 takeaway 一行
- [ ] 三支柱的配色在整份教材中保持一致（ML 藍 / DL 紫 / Scale 綠）
- [ ] Route 色與 Pillar 色可清楚區分
- [ ] 所有 mermaid diagram 在最終渲染環境下可正確顯示繁中
- [ ] 金句頁至少 5 張，且均為 full-bleed
- [ ] 所有圖表 caption 使用 T5 字級
- [ ] 所有 code block 有語言標籤
- [ ] 封面 + 分節頁共 4 張（開場 + Part A/B/C）

— end of layout & visual spec —
