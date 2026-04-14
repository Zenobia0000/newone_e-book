---
title: 投影片生成 SOP — Agent 工作流與模組資料夾規範
version: 1.0
last_updated: 2026-04-14
scope: books/python-data-ai-foundations 所有模組（M0–M7 demo，未來擴展至 M8–M20）
related:
  - ./顧問型投影片_黃金守則與泛式.md  # §1–§10 設計紀律
  - ../../books/python-data-ai-foundations/slides_build/  # 實作端
governing_thought: "人類規劃骨架（thesis + 敘事弧），系統填內容（layout + render）。每一層交付物都有明確 schema，讓 agent 接力不漂移。"
---

# 投影片生成 SOP — Agent 工作流

## § 0. 為什麼需要這份 SOP

既有痛點：
1. **LLM 只會生成內容，不會控制座標系統**——產出看似完整，但 Source 跑位、badge 漂移、annotation 對不準 bar
2. **不同 agent 接力時缺乏契約**——每個 agent 的輸入/輸出沒有 schema，後一棒要重新理解前一棒的意圖
3. **真實圖片（案例截圖、實地照片）無法自動取得**——AI 沒有 headless browser、沒有版權判斷能力、看不到客戶的真實資料
4. **人類介入點散落**——什麼時候該人審、什麼時候可以放手跑，沒有明確的閘門

本 SOP 解決上述四點，把流程切成 **7 個階段 × 5 種 agent 角色 × 10 份契約化文件**。

---

## § 1. 設計原則（MECE）

| 原則 | 含義 | 反例 |
|------|------|------|
| **分離關注點** | 內容（thesis）≠ 結構（layout）≠ 視覺（render）三者解耦 | 一個 agent 同時做三件事，改內容時順手改版型 |
| **契約化交付** | 每個 artefact 有 schema，後棒 agent 只認 schema 不認前棒 | 「你看前面 markdown 自己體會」 |
| **人類在骨架，系統在填充** | 人類寫 skeleton（thesis + 敘事弧 + 資料鉤點），agent 產全稿 | 人類逐字寫 15 張 slide 內容 |
| **絕對定位優先於流式排版** | 重要元素用 constraint 寫死（align / anchor / offset），不交給 LLM 臨場發揮 | 用 flow layout 讓 LLM 「自己排版」 |
| **圖片先框位、後填圖** | AI 無法自動取真實圖片，pipeline 先產佔位框 + 規格註記，人類最後貼圖 | 讓 AI 生成 stock photo 充數 |

---

## § 2. 角色與職責

### 2.1 人類（2 個觸點）

| 觸點 | 工作 | 預期耗時 |
|------|------|---------|
| **H-1 · 模組企劃** | 寫 `00_skeleton.yaml`：governing_thought、15–17 張 slide 各自的 thesis + prototype + 數據鉤點 | 60–90 分鐘/模組 |
| **H-2 · 真圖審核** | 依 `04_image_placeholders.yaml` 清單補真實圖片；審 Agent-QA 報告決定是否重跑 | 30–60 分鐘/模組 |

**人類不做**：寫全稿、排版、調色、畫圖表、寫版權條款。

### 2.2 Agents（5 種）

| Agent | 輸入 | 輸出 | 核心能力 |
|-------|------|------|---------|
| **A · Content** | `00_skeleton.yaml` + `01_outline.md` | `02_slides_design.md`、`05_mvk.md` | 主張句展開、口白生成、誤解欄位 |
| **B · Layout** | `02_slides_design.md` + 視覺語法合約 | `03_layout_spec.json` | 絕對定位、constraint 解析、anchor 綁定 |
| **C · Scout** | `02_slides_design.md` | `04_image_placeholders.yaml` | 識別需要真圖的 slide，產規格清單 |
| **D · Builder** | `03_layout_spec.json` + 已填圖之佔位資產 | `output/*.pptx` + `07_build_manifest.json` | 呼叫 `primitives.py` / `charts.py` 生成 .pptx |
| **E · QA** | `output/*.pptx` + 驗收規則（Layer C + §10.6） | `08_qa_report.md` | 14 條驗收自動掃描、截圖 sampling、回饋 |

每個 agent 是**無狀態**的：只看輸入契約、不看前棒的推理過程。

---

## § 3. 每模組資料夾標準檔案清單

**完整版 manifest（目標態）** — M2 起採用此結構：

```
chapters/M{N}_annotated/
├── 00_skeleton.yaml            ← H-1 人類寫（骨架）
├── 01_outline.md               ← H-1 人類寫（選填：模組說明 / 特殊要求）
├── 02_slides_design.md         ← Agent-A 產（可讀全稿，審閱用）
├── 03_layout_spec.json         ← Agent-B 產（constraint layout DSL）
├── 04_image_placeholders.yaml  ← Agent-C 產（需要真圖的清單）
├── 05_mvk.md                   ← Agent-A 產（MVK 速學卡）
├── 06_review_prose.md          ← Agent-A 產（敘事弧說明 / governing thought 展開；可選）
├── 07_build_manifest.json      ← Agent-D 產（中間品：primitive call graph）
├── 08_qa_report.md             ← Agent-E 產（驗收結果 + 失敗項）
├── 09_change_log.md            ← Agent 所有動作的 audit trail（append-only）
└── assets/                     ← H-2 人類放真實圖片（依 04 清單補）
    ├── s14_pandas_groupby.png
    ├── s14_sklearn_pipeline.png
    └── s14_pytorch_module.png
```

**最小可行版（M0–M7 現階段）**：每個模組維護 `00_skeleton.yaml` / `02_slides_design.md` / `04_image_placeholders.yaml` / `05_mvk.md` 四份核心檔案。`03_layout_spec.json` / `07_build_manifest.json` 暫由 `slides_build/slides/m{N}_deck.py` 代替（人類直接用 Python 寫 layout）。待 Agent-B 原型完成後可退役 `m{N}_deck.py`。

---

## § 4. 各文件的契約（schema）

### 4.1 `00_skeleton.yaml` — 人類唯一必填

```yaml
module: M0
title: "開場：Python 與 AI 系統全景"
governing_thought: "開場不是介紹課程，是讓學員在 25 分鐘內看見自己要去哪裡。"
target_time_minutes: 25
audience: "企業內訓 / 付費技術課程 / 成人學員"
style: Editorial-strict
primary_color: "#1B5E3F"

narrative_arc:
  hook: [1, 2]       # slide indices
  tension: [3, 6, 13]
  reveal: [4, 5, 7, 8]
  ground: [9, 10, 11, 12]
  feel: [14, 15]

slides:
  - index: 1
    prototype: SILENT
    thesis: "Data is the raw material; Python is the operating language."
    data_hook: null       # 這張不需要資料
    needs_real_image: false

  - index: 2
    prototype: ASK
    thesis: "2026 年，你為什麼要把 24 小時押在 Python 上？"
    data_hook: "Stack Overflow Survey 2025 — Python 於 AI/ML 使用率 #1（連續兩年）"
    needs_real_image: false

  - index: 3
    prototype: CHART
    thesis: "Python 於 AI / DS / DE 的使用率已從熱潮進入基礎設施鎖定"
    data_hook: |
      三線折線圖 2019-2025：
        AI/ML: 41→78 (+37pp)
        Data Science: 52→75
        Data Engineering: 28→63
      2023 年分水嶺（pandas 2.0 / PyTorch 2.0）
    sources:
      - "JetBrains/PSF Developer Ecosystem 2024"
      - "Stack Overflow 2025"
    needs_real_image: false

  # ... 其餘 12 張

  - index: 14
    prototype: PHOTO
    thesis: "本課程的真實棲地：你終將打開這三份官方文件"
    data_hook: |
      三聯拼貼：
        pandas: DataFrame.groupby 官方文件
        sklearn: Pipeline 官方文件
        PyTorch: torch.nn.Module 官方文件
    needs_real_image: true
    image_specs:
      - slot: left
        description: "pandas.pydata.org/docs/reference/groupby 頁面截圖（含 URL 列）"
        url_hint: "https://pandas.pydata.org/docs/reference/groupby.html"
        size_px: [410, 560]
      - slot: center
        description: "scikit-learn.org Pipeline class 文件"
        url_hint: "https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html"
        size_px: [410, 560]
      - slot: right
        description: "PyTorch torch.nn.Module 文件"
        url_hint: "https://pytorch.org/docs/stable/generated/torch.nn.Module.html"
        size_px: [410, 560]
```

**人類只需要填這份 YAML**。其他所有檔案都由 agent 產。

### 4.2 `02_slides_design.md` — Agent-A 輸出

每張 slide 含三個必要段落 `🖼️ 畫面`、`📣 畫面上的字`、`🎙️ 講者這時說`，以及 v1.2 建議加入的 `👁️ 視線路徑`、`📊 三層分層`、`🎯 視覺錨點`（見黃金守則 §10.4）。

### 4.3 `03_layout_spec.json` — Agent-B 輸出（Layout DSL 核心）

這是解決 "LLM 不會控制座標" 痛點的關鍵文件。單一 slide 範例：

```json
{
  "slide": 3,
  "canvas": {"w": 13.333, "h": 7.5, "unit": "inch"},
  "background": {"color": "#FFFFFF"},
  "elements": [
    {
      "id": "title",
      "type": "title",
      "text": "Python 於 AI / DS / DE 的使用率已從熱潮進入基礎設施鎖定",
      "constraint": {"x": 0.6, "y": 0.4, "w": 12.1, "h": 0.7},
      "style": {"color": "#1B5E3F", "font_size_pt": 20, "bold": true},
      "z_index": 10
    },
    {
      "id": "chart",
      "type": "chart_png",
      "generator": "line_chart_s3",
      "generator_args": {},
      "constraint": {"x": 0.8, "y": 1.2, "w": 11.7},
      "z_index": 20
    },
    {
      "id": "callout_arrow",
      "type": "callout_arrow",
      "constraint": {
        "from": {"anchor": "chart", "x_pct": 0.82, "y_pct": 0.22},
        "to": {"anchor": "chart", "x_pct": 0.90, "y_pct": 0.18}
      },
      "note": "已跨越 75% 基礎設施門檻",
      "z_index": 50
    },
    {
      "id": "source",
      "type": "source",
      "text": "JetBrains/PSF Developer Ecosystem 2024 · Stack Overflow 2025",
      "constraint": {"align": "bottom-right", "margin": {"x": 0.6, "y": 0.7}},
      "z_index": 5
    },
    {
      "id": "footer_logo",
      "type": "logo",
      "constraint": {"align": "bottom-right", "margin": {"x": 0.35, "y": 0.2}, "w": 0.55, "h": 0.55},
      "z_index": 100
    },
    {
      "id": "footer_copyright",
      "type": "footer_text",
      "text_template": "© 2026 桑尼資料科學 · {module} · {n}/{total}",
      "constraint": {"align": "bottom-left", "margin": {"x": 0.6, "y": 0.35}},
      "z_index": 100
    }
  ]
}
```

**Constraint 支援的三種定位**：
1. **絕對座標**：`{x, y, w, h}` — 數值 inches
2. **對齊約束**：`{align: bottom-right, margin: {x, y}}` — 讀者預期位置
3. **錨定約束**：`{anchor: <id>, x_pct, y_pct}` 或 `{anchor: <id>, edge: top, offset_y}` — 綁定到其他元素

**好處**：
- Source 一定在右下（不會漂）
- Logo 一定在右下（不會蓋住 Source，用 z_index 分層）
- Callout arrow 一定指到 chart 的 82%/22% 位置（資料變動也不跑）
- Layout engine 在 render 前解析所有 constraint，沒解出來的直接 fail fast

### 4.4 `04_image_placeholders.yaml` — Agent-C 輸出（也可手動維護）

```yaml
module: M0
generated_at: 2026-04-14T14:32:00
status_summary:
  total: 3
  pending: 3
  resolved: 0

placeholders:
  - id: M0_S14_left
    slide: 14
    slot_name: "pandas 官方文件截圖"
    bounding_box:
      x: 0.6
      y: 1.5
      w: 4.0
      h: 4.2
    description: "pandas.pydata.org/docs/reference/groupby 首屏截圖（瀏覽器含 URL 列，1024×1400 裁切為 4:5.6）"
    source_url: "https://pandas.pydata.org/docs/reference/groupby.html"
    recommended_size_px: [1200, 1680]
    depth_tag: "使用層"
    status: pending           # pending | resolved | skipped
    asset_path: null          # 人類補上後填 "assets/s14_pandas.png"
    author_notes: null

  - id: M0_S14_center
    slide: 14
    slot_name: "scikit-learn Pipeline 文件"
    bounding_box: {x: 4.85, y: 1.5, w: 4.0, h: 4.2}
    description: "scikit-learn Pipeline class 文件首屏，顯示類別簽章"
    source_url: "https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html"
    status: pending
    asset_path: null

  - id: M0_S14_right
    slide: 14
    slot_name: "PyTorch nn.Module 文件"
    bounding_box: {x: 9.1, y: 1.5, w: 4.0, h: 4.2}
    description: "PyTorch torch.nn.Module 文件首屏"
    source_url: "https://pytorch.org/docs/stable/generated/torch.nn.Module.html"
    status: pending
    asset_path: null
```

**協定**：
- `status: pending` → Builder 渲染為佔位框（白底深綠邊 + 灰字說明 + URL + TODO 標記）
- `status: resolved` + `asset_path` → Builder 讀圖片、縮放填入 bbox
- `status: skipped` → Builder 渲染為永久佔位（上線前必須決斷）

### 4.5 `08_qa_report.md` — Agent-E 輸出

```markdown
# M0 QA Report — 2026-04-14 14:35

## Layer C 七條（§5.Layer C）
| # | 條款 | 結果 |
|---|------|------|
| 1 | 標題完整論述 | ✓ 15/15 |
| 2 | 顏色 ≤ 黑+灰+1 accent | ✓ |
| ...

## §10.6 v1.2 四條新增
| # | 條款 | 結果 |
|---|------|------|
| C-A | 單一錨點 | ⚠ S7 PYRAMID 有兩個並列焦點（見附圖）
| C-B | 三層完整性 | ✓ 所有資料型 slide 皆有 Data/Insight/Guidance
| C-C | 合約一致性 | ✓
| C-D | 三秒測試 | ⚠ S9 TABLE 縮成 300px 後難辨主張

## 截圖抽樣
- S7.png  — 單一錨點問題
- S9.png  — 三秒測試問題

## 建議修改
1. S7：把 Infra 層改白底深綠邊以降權，保留 Data 層作為單一錨點
2. S9：副標字級 14pt → 16pt，砍最後一列

## 圖片佔位符狀態
- 3 個 pending（S14 三聯）

本報告由 Agent-E 產出；人類決定是否要求重跑。
```

---

## § 5. 流水線七階段

```
H-1 ──▶ 00_skeleton.yaml
         │
         ▼
       Agent-A (Content)
         │ ▶ 02_slides_design.md
         │ ▶ 05_mvk.md
         │
         ▼
       Agent-B (Layout)  + 視覺語法合約 §10.2
         │ ▶ 03_layout_spec.json
         │
         ▼
       Agent-C (Scout)
         │ ▶ 04_image_placeholders.yaml (status=pending)
         │
         ▼
       Agent-D (Builder)  ◀── slides_build/primitives.py / charts.py
         │ ▶ output/M{N}_*.pptx (v1 — 帶佔位框)
         │ ▶ 07_build_manifest.json
         │
         ▼
       Agent-E (QA)
         │ ▶ 08_qa_report.md
         │
         ▼
       H-2 決策分歧：
         ├─ (a) QA 通過且無 pending 圖 → v1 = final，寄出
         ├─ (b) QA 有 warning → 人類修 skeleton → 回 Agent-A
         └─ (c) pending 圖需補 → 人類放 assets/*.png、改 04_image_placeholders status=resolved → Agent-D 重跑（輕量 rebuild，不重跑 Agent-A/B）
```

### 5.1 失敗恢復矩陣

| 症狀 | 可能原因 | 哪一棒重跑 |
|------|---------|-----------|
| Source 跑位 | layout_spec 的 align 欄位沒寫對 | 只重 Agent-D |
| 主張句模糊 | skeleton thesis 寫得不夠狠 | 人類改 skeleton → Agent-A 全跑 |
| 缺 Guidance 層 | Agent-A 漏寫 `📊 三層分層` | 只重 Agent-A |
| 圖表標籤重疊 | chart generator 參數錯 | 改 charts.py 對應函式，只重 Agent-D |
| pending 圖未補 | 人類未提供 asset | H-2 介入 |

---

## § 6. Layout DSL 詳細規格（`03_layout_spec.json` 完整 schema）

### 6.1 元素型別 `type`

| type | 用途 | 必要欄位 |
|------|------|---------|
| `title` | 主張句 | text, constraint |
| `subtitle` | 副標 | text, constraint |
| `paragraph` | 一般文字段 | text, constraint, style |
| `rect` | 背景色塊 / 分組框 | constraint, style |
| `chart_png` | matplotlib 產的 PNG | generator, generator_args, constraint |
| `image` | 真實圖片（從 asset_path 讀） | asset_path, constraint |
| `placeholder` | 圖片佔位框（未 resolved） | placeholder_id, constraint |
| `arrow` / `callout_arrow` | 箭頭 | constraint(from, to), note |
| `dividing_rule` | 分水嶺虛線 | constraint, label, kind |
| `delta_badge` | 變化徽章 | value, constraint, inverted |
| `emphasis_pill` | 強調膠囊 | text, constraint |
| `highlight_ring` | 圈選框 | constraint |
| `source` | 資料來源 | text, constraint(align) |
| `logo` | Logo | constraint(align), asset=theme.LOGO_PATH |
| `footer_text` | 頁碼版權 | text_template, constraint |
| `matrix` | 格狀 | rows, cols, cells, constraint |
| `table` | 極簡表 | header, rows, col_widths, constraint |
| `pyramid` | 堆疊 | layers, cross_cuts, constraint |
| `flow_chain` | 單向流 | nodes, branch, constraint |
| `dual_track` | 雙軌 | track_a, track_b, bridges, constraint |
| `risk_mitigation` | 對稱雙框 | risks, mitigations, summary, constraint |
| `vs_two_col` | 對比 | left_title, right_title, delta, constraint |

### 6.2 Constraint 解析順序

Builder 收到 layout_spec 後執行拓撲排序：

1. 先解 `{x, y, w, h}` 絕對座標元素（記入座標表）
2. 再解 `{align: ...}` 對齊元素（依 canvas 邊緣）
3. 最後解 `{anchor: <id>, ...}` 錨定元素（需前兩輪已算完被錨定的元素）

**Cycle detection**：若 A 錨定 B、B 錨定 A → fail fast，回報 agent 修。

### 6.3 z_index 階層慣例

```
100 — 右下 Logo、左下 Footer（永遠在最上面，不被蓋）
 50 — Guidance 層（箭頭、badge、圈選）
 30 — Insight 層（數字標註、delta）
 20 — Data 層（主要內容：chart、table、matrix）
 10 — 標題、副標
  5 — Source 標註
  0 — 背景色塊
```

---

## § 7. 圖片佔位符協定（本次實作重點）

### 7.1 視覺規格

佔位框一律使用以下規格（統一外觀，辨識度高）：

- 外框：深綠 `#1B5E3F` 2pt 實線
- 底色：`#F7F7F7` 淺灰底（與純白頁面區隔，暗示「這是預留區」）
- 中央文字：「[ 待補真圖：{slot_name} ]」，字級 12pt，灰色 `#808080` 斜體
- 下方副行：URL hint（10pt 灰，可選）
- 右下角角標：紅字「TODO」8pt（刻意破色，讓作者一眼看到；印刷前務必全部解決）

### 7.2 Builder 行為

```python
# 偽代碼
for ph in layout_spec["elements"]:
    if ph["type"] == "placeholder":
        entry = image_placeholders[ph["placeholder_id"]]
        if entry["status"] == "resolved":
            draw_image(slide, entry["asset_path"], ph["constraint"])
        else:
            draw_image_placeholder(
                slide, **ph["constraint"],
                description=entry["description"],
                url_hint=entry["source_url"],
            )
            # 同時把 placeholder id 記入 build_manifest 供 QA 追蹤
```

### 7.3 人類工作流

1. 看 `04_image_placeholders.yaml`，找 `status: pending` 的條目
2. 依 `description` + `source_url` + `recommended_size_px` 取得圖片
3. 存到 `assets/` 資料夾，檔名對應 id（如 `s14_pandas.png`）
4. 改 YAML：`status: resolved`、`asset_path: assets/s14_pandas.png`
5. Agent-D 重跑，真圖取代佔位框

### 7.4 版權標示要求

若使用他人截圖或素材：
- 該 slide 的 Source 行必須註明來源
- 若為官方文件 / 政府公開資料，註「Source: {網站}, {日期}」即可
- 若為受版權保護之商業素材，需取得授權；無授權時改用 `status: skipped` + 替代設計

---

## § 8. 跨模組擴展（M0 → M7 → M8+）

### 8.1 當前階段（M0 / M1 demo）

- 人類直接在 `slides/m{N}_deck.py` 用 Python 呼叫 primitives 寫 layout
- 相當於「人類兼 Agent-A + Agent-B + Agent-C + Agent-D」
- 但已經有 Agent-E 的驗收雛型（Layer C + §10.6 人工對照）

### 8.2 過渡階段（M2 / M3 / M4）

- 手工抽出 `00_skeleton.yaml`（把 m{N}_deck.py 裡的 thesis / data 上抽）
- 實驗 Agent-B：寫一個小工具 `extract_layout.py` 從 m{N}_deck.py 讀出 layout_spec.json（反向工程）
- 建立 `04_image_placeholders.yaml` 慣例

### 8.3 目標階段（M5 起）

- 人類只寫 `00_skeleton.yaml` + `01_outline.md`
- Agent-A / B / C / D / E 接力自動化
- `m{N}_deck.py` 不再手寫，由 Builder 從 layout_spec.json generate
- 每次人類改 skeleton → pipeline 全跑 → QA report → 迭代

### 8.4 成熟階段（M8+）

- `00_skeleton.yaml` 進一步簡化到「15 行 × 3 欄」（thesis / prototype / data_hook）
- 加入 `generation_config.yaml` 控制風格變體（Editorial 嚴謹 / Editorial 輕量 / 學員互動版）
- 單一命令 `sbuild M5 --full` 執行整個 pipeline

---

## § 9. 執行命令（CLI 擬定）

```bash
# 目前可用（demo 階段）
python -m slides_build.build --module M0
python -m slides_build.build --demo         # M0 + M1

# 未來（完整 pipeline）
sbuild skeleton M3                          # 從 template 建 00_skeleton.yaml
sbuild gen M3 --stage content               # 只跑 Agent-A
sbuild gen M3 --stage layout                # 只跑 Agent-B
sbuild gen M3 --stage scout                 # 只跑 Agent-C，產圖片清單
sbuild gen M3 --full                        # A + B + C + D + E 全跑
sbuild rebuild M3                           # 只跑 D（圖補完後的重 render）
sbuild qa M3                                # 只跑 E
sbuild status M3                            # 看 pending 的圖片 / warning 清單
```

---

## § 10. 驗收閘門（誰確認才算過）

| 閘門 | 誰把關 | 通過標準 |
|------|-------|---------|
| G-A · skeleton 合格 | H-1 自檢 | 15–17 張 slide、thesis 全為完整句、敘事弧 5 段皆有對應 slide |
| G-B · 設計稿合格 | Agent-E 自動 | Layer C 七條全 ✓，§10.6 四條全 ✓ |
| G-C · 圖片全解 | Agent-C + H-2 | `04_image_placeholders.yaml` 無 pending（全 resolved 或 skipped） |
| G-D · 建置成功 | Agent-D 自動 | .pptx 能打開、總頁數正確（封面 + N + 版權）、無渲染錯誤 |
| G-E · 三秒測試 | H-2 人工 | 縮圖抽 5 張，3 秒內能說主張 |
| G-F · 版權檢查 | H-2 人工 | 所有外部素材都有 Source；版權條款頁完整 |

**六道閘門全過才能標記 module 為 `status: released`**。

---

## § 11. 本 SOP 的自我維護

- 每次新增 primitive（如未來的 `draw_z_curve`）必須同步更新 §6.1 type 表
- 每次新黃金守則（G14、G15...）必須同步更新 Agent-E 的驗收清單
- 視覺語法合約（§10.2）凍結後 3 個月內不改；若必須改，同步 PR 上所有 `03_layout_spec.json`

---

## 附錄 A：現狀 vs 目標態對照（Gap Analysis）

| 能力 | 現狀（M0/M1 demo） | 目標態（M5+） |
|------|-----------------|--------------|
| 內容生成 | 人類 + Claude 協作直接寫 markdown | Agent-A 自動展開 |
| 版面定義 | Python 硬編碼 (m0_deck.py) | layout_spec.json DSL |
| 座標控制 | Inches() 手動設定 | constraint solver |
| 圖片處理 | S14 一個 hardcoded triptych | 通用 placeholder + resolved 雙態 |
| QA | 人眼看 PDF | Agent-E 自動 + 截圖抽樣 |
| 擴展新模組 | 複製 m0_deck.py 改 | 改 skeleton.yaml 重跑 pipeline |
| 時間成本 | 手動 ~4 小時/模組 | 自動 ~10 分鐘/模組（不含真圖補件） |

---

## 附錄 B：短期 Action Items（本次 PR 落地）

1. ✅ 新增 `draw_image_placeholder` primitive（支援通用佔位，非僅 S14 三聯）
2. ✅ M0 / M1 產出時同步寫 `output/_image_placeholders.yaml`（audit 用）
3. 📋 寫 `chapters/M0_annotated/00_skeleton.yaml` 範例（示範人類輸入）
4. 📋 寫 `chapters/M0_annotated/04_image_placeholders.yaml` 範例
5. 🔜 M2 起改用 00_skeleton.yaml 為起點（過渡階段）
6. 🔜 未來：`slides_build/layout_engine/` 模組（讀 layout_spec.json → 呼叫 primitives）

圖標：✅ 本 SOP 落地時同步完成  ·  📋 範例文件，複製即可擴展  ·  🔜 下一階段工作

---

**文件結束**

> 本 SOP 若能讓下一位接手的人（或 agent）在讀完後 30 分鐘內產出一個新模組的 `.pptx`，並通過 Agent-E 的全部驗收，就算成功。
