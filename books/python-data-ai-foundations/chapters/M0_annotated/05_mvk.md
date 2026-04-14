# M0 MVK 速學卡 — Minimum Viable Knowledge Flashcards

> **本文件定位**：30 分鐘 onboarding speed-run 材料。用於新進工程師、跨部門協作者、或課前 prerequisite check。
> **讀者**：任何需要在最短時間內掌握 M0 骨幹概念的人。
> **使用情境**：新人第一週、跨 team PM 快速入門、資深工程師備課前的自我校準。
> **語氣**：速度優先，一張卡一個概念，誤解與連結必寫清楚。
> **姊妹檔**：[`02_slides_design.md`](./02_slides_design.md) — 25 分鐘 Editorial-strict 顧問型投影片 15 張，正式授課用。本 MVK 為其課後/課前自學配套，卡片對應 slide 編號見該 deck 結尾「課後延伸資源」區塊。

---

## 使用說明

- **卡片結構**：每張卡含 5 個欄位 — 概念 / 一句話定義 / 最小可操作範例 / 常見誤解 / 與其他模組連結
- **建議速度**：每張 2 分鐘（含自測），全部 13 張約 26 分鐘
- **自測方法**：蓋住「一句話定義」，看「概念」能否說出定義 → 再看「最小可操作範例」能否解釋做什麼

---

## Card 01 — Python 作為「操作語言」

| 欄位 | 內容 |
|------|------|
| **概念** | Python-as-Operating-Language |
| **一句話定義** | Python 是工程師用來「指揮」高效能底層（C/C++/CUDA/Rust）的中介層，它本身不是高效能，但是生態系的 orchestration layer。 |
| **最小可操作範例** | `import numpy as np; a = np.array([1,2,3]); a * 2` — 你寫了 Python，但乘法是在 C 層執行。 |
| **常見誤解** | ❌「Python 慢所以要換 Rust」— 錯。Python 慢的是 interpreter，熱路徑幾乎都在 C 層；真正的議題是「如何讓熱路徑正確地卸載到底層」。 |
| **連結** | → M1（Python 核心）、M3（NumPy）、M7（PyTorch / DL 前導） |

---

## Card 02 — 生態系四層結構

| 欄位 | 內容 |
|------|------|
| **概念** | Four-Layer Ecosystem Topology |
| **一句話定義** | Python 資料/AI 生態可分為四層：互動環境層、資料操作層、模型層、部署層；任何新工具都能被歸位到這四層之一。 |
| **最小可操作範例** | Jupyter（L1）寫 `import pandas`（L2）做 feature engineering，送入 `sklearn`（L3），部署用 `FastAPI + Docker`（L4）。 |
| **常見誤解** | ❌「Hugging Face Transformers 和 PyTorch 同層」— 錯。Transformers 依賴 PyTorch，是 L3 內的高階封裝層。 |
| **連結** | → M0 S03、M3（pandas）、M7（sklearn / ML 路徑） |

---

## Card 03 — AI 產品四項構成公式

| 欄位 | 內容 |
|------|------|
| **概念** | `AI product = data + code + runtime + infra` |
| **一句話定義** | 任何 AI 產品都由「資料狀態 + 邏輯程式 + 執行環境 + 基礎設施」四個正交維度構成，各層有不同變動頻率與負責工具。 |
| **最小可操作範例** | 一個 Netflix 推薦：data=user logs、code=recommender model、runtime=TorchServe、infra=AWS k8s。 |
| **常見誤解** | ❌「這個公式是完整的」— 不完整。缺 evaluation 與 governance 兩項，在 2026 年的 MLOps context 下需補充。 |
| **連結** | → M0 S05、M5（進階 Python）+ M7（ML 路徑）、未來延伸：ML monitoring / drift detection |

---

## Card 04 — pandas 2.0 Copy-on-Write 分水嶺

| 欄位 | 內容 |
|------|------|
| **概念** | pandas 2.x CoW / Arrow backend |
| **一句話定義** | pandas 2.0（2023）新增 Copy-on-Write 語意（opt-in，3.0 將預設）與 Arrow dtype 後端（opt-in），舊 code 的 chained assignment 行為會變更。 |
| **最小可操作範例** | `pd.options.mode.copy_on_write = True; df['col'][0] = 1` — 在 CoW 模式下**不會**修改原 df。 |
| **常見誤解** | ❌「pandas 2.0 預設用 Arrow」— 錯。Arrow 是 opt-in dtype，預設仍是 NumPy-backed。需顯式指定 `dtype_backend="pyarrow"`。 |
| **連結** | → M4–M6 資料操作（要在一開始就開 CoW）、讀 pandas whatsnew v2.x |

---

## Card 05 — 版本敏感度（Version Sensitivity）

| 欄位 | 內容 |
|------|------|
| **概念** | Ecosystem Version Drift Awareness |
| **一句話定義** | Python 資料生態的主要套件（pandas、NumPy、PyTorch）在 2023–2024 皆經歷 2.0 breaking change，2018 年的教程 code 在 2026 年運行常產生 warning 或錯誤。 |
| **最小可操作範例** | 執行 `import warnings; warnings.simplefilter("error", FutureWarning)` 可讓舊 code 直接報錯而非隱藏。 |
| **常見誤解** | ❌「pip install 最新就好」— 錯。最新版可能和 tutorial 不一致，需要 pinned versions + lock file。 |
| **連結** | → M3（環境管理）、M2（工程實踐）、讀套件的 whatsnew / changelog |

---

## Card 06 — 虛擬環境（venv / uv）

| 欄位 | 內容 |
|------|------|
| **概念** | Virtual Environment Isolation |
| **一句話定義** | 虛擬環境是 Python 依賴的「沙盒」，避免不同專案的套件版本衝突；2026 年標準工具從 `python -m venv` 正在轉向 `uv venv`（Rust 寫的 10-100x 快速版）。 |
| **最小可操作範例** | `uv venv .venv && source .venv/bin/activate && uv pip install pandas` |
| **常見誤解** | ❌「conda 跟 venv 可以混用」— 不建議。兩者各自有對 Python runtime 的假設，混用會出現難 debug 的路徑衝突。 |
| **連結** | → M3 環境管理、軌道二工程實踐、依賴 lock file 概念 |

---

## Card 07 — Jupyter 的本質

| 欄位 | 內容 |
|------|------|
| **概念** | Jupyter = Kernel + Document |
| **一句話定義** | Jupyter 是「可執行文件」（executable document），由 kernel（執行引擎）+ notebook（JSON 文件格式）組成，不是一個「給新手的 IDE」。 |
| **最小可操作範例** | 在 Jupyter 中 `import sys; sys.executable` — 輸出的是 kernel 對應的 Python，不一定是 shell 的 `which python`。 |
| **常見誤解** | ❌「重啟 kernel 只是清 output」— 錯。Kernel restart 會清掉所有記憶體中的變數；以 cell 執行順序依賴變數會失效。 |
| **連結** | → M0 workshop、M4 pandas 探索、軌道二 Git 與 notebook 衝突問題 |

---

## Card 08 — NumPy array protocol（為何 NumPy 不可替代）

| 欄位 | 內容 |
|------|------|
| **概念** | NumPy Array Protocol |
| **一句話定義** | NumPy 定義了 `__array__`、buffer protocol、dtype 系統，成為 pandas、sklearn、PyTorch、JAX 等上層工具的**事實通訊介面**，這使 NumPy 成為生態底層。 |
| **最小可操作範例** | `torch.from_numpy(np.array([1,2,3]))` — NumPy array 可零拷貝轉 PyTorch tensor，反之亦然。 |
| **常見誤解** | ❌「Polars 可以完全取代 NumPy」— 錯。Polars 目標是取代 pandas，但底層 array protocol 層的取代者不是 Polars，是 Apache Arrow。 |
| **連結** | → M3 NumPy、M7 PyTorch、了解 Arrow 作為下一代底層 |

---

## Card 09 — 雙軌能力線（Dual-Track Skill Model）

| 欄位 | 內容 |
|------|------|
| **概念** | Dual-Track Competency（資料+AI / 軟體+系統） |
| **一句話定義** | 成為 AI 工程師需要兩種不可互轉的能力：軌道一（歸納思維 — 從數據找模式）與軌道二（演繹思維 — 從規則寫系統），兩者交織產生「可交付產品」的能力。 |
| **最小可操作範例** | 一個技能清單自測：給 10 個技能（groupby、docker、cross-validation、git rebase...），分類到兩軌。 |
| **常見誤解** | ❌「資料科學家可以不學軌道二」— 在現代 team 可以，但成為 senior 或小團隊獨立出貨者必須兩軌。 |
| **連結** | → M0 S06、軌道二在 M2、M5 有主要著墨，M7 收束到路徑 |

---

## Card 10 — 時間分配直覺（80/20 注意事項）

| 欄位 | 內容 |
|------|------|
| **概念** | Data Prep 佔比的世代變化 |
| **一句話定義** | 2017–2019 調查顯示 data prep 佔 data scientist 80% 時間，但 2024+ 隨 feature store / MLOps 平台成熟，此比例下降到 50–60%，evaluation 與 governance 時間上升。 |
| **最小可操作範例** | 在一個假設 ML 專案估時：data=50%、modeling=20%、evaluation=15%、ops=15%（比舊 80/20 更真實）。 |
| **常見誤解** | ❌「80% 是恆定數字」— 錯，這是時代依賴的，且依職能（DE / DS / MLE）分布不同。 |
| **連結** | → M0 S05、M7 MLOps 與路徑討論、職涯規劃 |

---

## Card 11 — 學習方法論 MVP Code 原則

| 欄位 | 內容 |
|------|------|
| **概念** | Kent Beck 的 "Make it work, make it right, make it fast" |
| **一句話定義** | 開發順序永遠是：先讓程式能跑（work）→ 再讓它正確（right）→ 最後才優化速度（fast）；這個順序不可倒置。 |
| **最小可操作範例** | 實作 pandas pipeline：先 hardcode 完成功能 → 加入 edge case 處理 → 最後考慮 vectorization / Polars 替換。 |
| **常見誤解** | ❌「ML 的正確 = 高 accuracy」— 錯。ML 的「right」包含無 data leakage、正確的 train/test 切分、metric 選擇適當，不只是分數高。 |
| **連結** | → M4 EDA、M7 ML 前導、整個課程的工作坊哲學 |

---

## Card 12 — 搜尋策略（2026 版）

| 欄位 | 內容 |
|------|------|
| **概念** | 2026 Debugging Search Workflow |
| **一句話定義** | 用 AI 加速探索假設 → 用官方文檔驗證真相 → 用 Stack Overflow 看他人踩過的坑；順序不是「哪個先用」，是「哪個作為 truth source」。 |
| **最小可操作範例** | pandas `FutureWarning` → 先問 AI「這是什麼警告」→ 到 `pandas.pydata.org/docs/whatsnew` 驗證 → 搜 SO 看 migration 模式。 |
| **常見誤解** | ❌「AI 答案可以直接 copy」— 錯，AI 對 pandas/PyTorch 快速演進的 API 有幻覺風險，必須回官方文檔驗證。 |
| **連結** | → M0 S08、整個課程的 debug 訓練、元認知能力 |

---

## Card 13 — 學習契約（Learning Contract）

| 欄位 | 內容 |
|------|------|
| **概念** | Implementation Intention for Learning |
| **一句話定義** | 在學習啟動時明確寫下「想解決的真實問題 + 學習障礙 + 期待模組」，可將完成率提升 2–3 倍（Gollwitzer 1999 研究）。 |
| **最小可操作範例** | 在 `M0_ecosystem_map.ipynb` 最後 cell 寫三題答案，pinned 在 notebook 頂部，M7 結束時回顧。 |
| **常見誤解** | ❌「這是感想文，可有可無」— 錯。這是可驗證的學習目標設定機制，有教育心理學實證支撐。 |
| **連結** | → M0 workshop 練習三、M7 課程總結、每個模組的 reflection 段 |

---

## Speed-Run 自測表（26 分鐘）

| # | 卡片 | 自測問題 | 時間 |
|---|------|----------|------|
| 1 | Python-as-OL | 為什麼 Python 慢但還是主導 AI？ | 2 min |
| 2 | 四層生態 | 畫出四層並各舉一工具 | 2 min |
| 3 | 產品四項 | 背出 `data+code+runtime+infra` 並解釋缺了什麼 | 2 min |
| 4 | pandas 2.0 | 什麼是 CoW？是預設嗎？ | 2 min |
| 5 | 版本敏感度 | pandas / NumPy / PyTorch 的 2.0 分別何時？ | 2 min |
| 6 | venv | uv 和 venv 的關係？ | 2 min |
| 7 | Jupyter 本質 | Kernel restart 會發生什麼？ | 2 min |
| 8 | NumPy 協議 | 為什麼 NumPy 不可替代？ | 2 min |
| 9 | 雙軌 | 分類 5 個技能到兩軌 | 2 min |
| 10 | 80/20 | 這個比例的時代變化？ | 2 min |
| 11 | MVP Code | 三步驟順序？ML 的「right」是什麼？ | 2 min |
| 12 | 搜尋策略 | AI / 官方文檔 / SO 各自的角色？ | 2 min |
| 13 | 學習契約 | 寫下你自己的三題答案 | 2 min |

**通過標準**：13 張卡片在 30 分鐘內全部自測通過，誤解欄位不超過 2 個錯誤。達標者可直接進入 M1，未達標者建議回看 M0 對應 slide。

---

## 附錄 A：與後續模組的 dependency map

| MVK 卡片 | 強依賴模組 | 弱依賴模組 |
|----------|-----------|-----------|
| C01 Python-as-OL | M1 | M7 |
| C02 四層生態 | 全課程 | — |
| C03 AI 四項 | M5 + M7 | M3 |
| C04 pandas 2.0 | M3 | M7（pipeline 選型） |
| C05 版本敏感度 | M5 | 全課程 |
| C06 venv/uv | M5 | 全課程 |
| C07 Jupyter | M0 workshop | M3, M4 |
| C08 NumPy 協議 | M3 | M7 |
| C09 雙軌 | — | 整個課程結構 |
| C10 80/20 | M7 | 職涯決策 |
| C11 MVP Code | M4, M7 | 全課程 |
| C12 搜尋策略 | 全課程 | 元認知 |
| C13 學習契約 | M0 workshop | M7 |

---

## 附錄 B：單一 slide 速查表（若只有 5 分鐘）

如果你**只有 5 分鐘**，只需記住這三件事：

1. **Python 是 orchestration layer，不是 compute layer** — 所以不要用 Python 的效能挑戰它。
2. **AI 產品 = data + code + runtime + infra** — 缺任何一層都無法出貨。
3. **2023–2024 是 pandas/NumPy/PyTorch 的 2.0 分水嶺** — 你看到的舊 code 多數已過時。

這三點 = M0 的壓縮包。

---

*— End of MVK Flashcards —*
