# M0 三視角分析 — First Principles / Fundamentals / Body of Knowledge

> **本文件定位**：用三個互補但不重疊的學術視角重新解構 M0，檢驗這個模組在「知識論 / 教學論 / 工程學科地位」三個維度上是否立得住。
> **讀者**：課程設計者、教學主管、外部學術審稿人。
> **使用情境**：課程大綱送外審前的自我檢查；回應「為什麼是這些內容而不是那些」的質疑。
> **語氣**：學術嚴謹但保留工程實作立場；每個判斷可反駁。

---

## Lens 1：First Principles — 把 M0 拆到不可再分的本質命題

### 1.1 方法論說明

First Principles thinking 要求我們把 M0 的每個主張，往下推到**物理定律 / 資訊理論 / 經濟學邏輯**這三層之一，直到無法再分解。

### 1.2 M0 的核心主張拆解

#### 命題 A：「為什麼要學 Python？」

往下推：
- **A1（表層）**：因為產業都在用。 → 這是從眾論證，非本質。
- **A2（中層）**：因為 Python 是「膠水語言」，能黏合高效能組件。 → 為什麼需要膠水？繼續推。
- **A3（深層）**：因為 **人類認知頻寬 vs. 機器計算頻寬** 存在 6 個數量級的差距（人腦語言處理 ~10 bit/s，GPU ~10^13 FLOPS），需要一種「人可讀、機可呼叫」的中介層。Python 的語法近自然語言、runtime 可呼叫 C/CUDA，正好填補這個落差。
- **A4（根本）**：**資訊理論角度**：Python 是一個「高熵輸入、低熵輸出」的翻譯器 — 工程師用語意模糊的自然語言式 code 表達意圖，由 interpreter + libraries 壓縮為確定性機器指令。這個中介層的存在是**必要的**（根本命題），「是不是 Python」是**偶然的**（歷史路徑依賴）。

**結論**：M0 應該教的**不是「Python 為何主導」**，而是**「為什麼需要這一層翻譯器，以及 Python 恰好佔據了這個位置」**。這樣學員理解了即使 Python 被取代，「翻譯器」這個結構不會消失。

---

#### 命題 B：「為什麼 AI 產品需要 data + code + runtime + infra 四層？」

往下推：
- **B1**：這是工程分工。 → 還不是本質。
- **B2**：因為 **狀態 (data)**、**邏輯 (code)**、**執行 (runtime)**、**容器 (infra)** 是任何計算系統的四個正交維度。這可以追溯到 **Von Neumann 架構**（資料與指令分離）+ **作業系統抽象**（process vs. kernel vs. hardware）。
- **B3**：往更本質推，這四層對應四種**不同的變動頻率**：
  - Data：每秒 ~ 每小時變動
  - Code：每天 ~ 每週變動
  - Runtime：每月 ~ 每季變動
  - Infra：每季 ~ 每年變動
  分層的**本質原因**是**變動頻率差異**需要不同的變更管理機制（不同的版本控制、測試、部署節奏）。這是 Parnas 1972 "On the Criteria To Be Used in Decomposing Systems into Modules" 的 **information hiding** 原則在 ML 上的延伸。

**結論**：M0 的公式應該補充註記：「分層不是設計偏好，是變動頻率的函數。」這讓學員理解為什麼 ML 系統和傳統軟體的架構原則是一致的。

---

#### 命題 C：「為什麼 2026 年是學 Python 的時點？」

往下推：
- **C1**：因為 AI 熱潮。 → 流行論證，非本質。
- **C2**：因為工具鏈成熟（pandas 2、NumPy 2、PyTorch 2）。 → 為什麼現在成熟？
- **C3**：**經濟學角度 — 生態系飛輪效應**：Python 在 2010 年代吃下 NumPy / Jupyter 後，形成正回饋循環（使用者多 → 函式庫多 → 使用者更多）。2024 年左右達到 **Metcalfe 飽和點**（用戶數邊際效益遞減），剩餘的成長空間是「深化」而非「擴張」。
- **C4**：**資本論角度** — Python 的主導地位是 open source 資本（社群勞動時間）的累積，這種資本的複利效應在第 20+ 年進入收割期。2026 年剛好是收割期的高峰。

**結論**：「2026 年」的特殊性不是 hype driven，而是**社群資本複利 + 工具鏈世代更新 + 企業 IT 債務清償**的三重重合。這個論述比「AI 很熱」更站得住。

---

#### 命題 D：「為什麼雙軌設計？」

往下推：
- **D1**：因為資料能力和軟體能力是不同技能。 → 為什麼不同？
- **D2**：**認知科學角度** — 兩軌對應不同的認知模式：
  - 軌道一（資料 + AI）偏 **歸納思維**（從數據找模式）
  - 軌道二（軟體 + 系統）偏 **演繹思維**（從規則推行為）
- **D3**：**不可交換性** — 歸納技能不會自動產生演繹技能，反之亦然。這是教育學的 **transfer of learning** 問題（Barnett & Ceci, 2002）— 遠距離知識遷移是困難的，必須明確設計雙軌訓練。

**結論**：雙軌不是方便的教學分類，是**認知模式分離**的必然結果。M0 可以補充這個底層邏輯，讓學員不把雙軌當成 marketing。

---

### 1.3 自下而上重建的 M0

若以 First Principles 重建 M0，順序應該是：

1. **公設**：人機頻寬落差需要翻譯器（Python 的存在理由）
2. **公設**：計算系統有四個變動頻率層（data/code/runtime/infra 的分層理由）
3. **公設**：歸納與演繹是兩種不可互轉的認知模式（雙軌的理由）
4. **推論 1**：Python 在 2026 年佔據翻譯器生態位（生態系地圖）
5. **推論 2**：AI 產品的四層結構是公設 2 的特例（解剖圖）
6. **推論 3**：課程的 24 小時需要在雙軌上配比時間（路線圖）
7. **方法論**：主動學習是歸納 + 演繹雙管齊下的唯一實踐途徑（學習方法論）

**優點**：每一層都可反駁、可驗證。
**代價**：太硬核，不適合作為學員直接看到的敘事，但應該作為講師備課的內部邏輯骨架。

---

## Lens 2：Fundamentals — Minimum Viable Knowledge Checklist

### 2.1 方法論說明

Fundamentals 視角追求「如果只能保留 20% 的內容，要保留哪 20% 才能支撐 80% 的後續學習」。以下是 M0 的 MVK checklist，格式為可操作的 yes/no 驗收條件。

### 2.2 M0 Fundamentals 必修清單

#### ✅ Knowledge Checklist（共 12 條）

- [ ] **F1. Python 版本意識**：能正確回答「你本機的 Python 是哪個版本、從哪裡來、在哪裡」三個問題。驗收：`python --version && which python && python -c "import sys; print(sys.executable)"` 能正確解讀輸出。
- [ ] **F2. 虛擬環境基礎**：能建立、啟用、停用 venv（或 uv venv）。驗收：能在兩個 project 間切換不同 Python 環境而不汙染全域。
- [ ] **F3. 套件安裝的三種來源**：知道 pip / conda / uv 的差別與何時使用何者。驗收：能說明「pip install 的 package 從哪裡下載」（PyPI）。
- [ ] **F4. Jupyter 的本質**：知道 Jupyter = Kernel + Notebook document，而非「給初學者的 IDE」。驗收：能解釋 kernel restart 為何會清掉變數。
- [ ] **F5. 生態系四層結構**：能在白紙上畫出「互動層 / 資料層 / 模型層 / 部署層」並各舉一個工具。驗收：看到新工具（例如 Polars、Ray）能判斷屬於哪一層。
- [ ] **F6. NumPy 在棧中的地位**：知道 pandas、sklearn、PyTorch 都依賴或相容於 NumPy array protocol。驗收：能解釋為什麼換掉 NumPy 等於換掉整個棧。
- [ ] **F7. AI 產品四層公式**：能默寫 `data + code + runtime + infra`，並各舉一個代表工具。驗收：給一個新工具（例如 MLflow），能說明它橫跨哪幾層。
- [ ] **F8. 工程師 80/20 時間分配直覺**：知道 data prep 是大宗，但 runtime/infra 不理解就無法出貨。驗收：能在一個假設 ML 專案中說明每階段的大致時數。
- [ ] **F9. 雙軌意識**：能區分一個技能屬於「資料 + AI」還是「軟體 + 系統」軌道。驗收：給定 10 個技能名詞（pandas groupby、docker build、git rebase、cross-validation ...），能正確分類。
- [ ] **F10. Pipeline 心智模型**：知道「資料分析管線」是 ingestion → cleaning → EDA → modeling → evaluation → reporting 的線性 + 迴圈混合。驗收：能畫出簡化版 DAG。
- [ ] **F11. 搜尋策略與工具**：知道官方文檔、Stack Overflow、AI 各自的定位與限制。驗收：遇到 pandas FutureWarning，能說出「先去 pandas whatsnew 頁查」。
- [ ] **F12. 版本敏感度**：知道 pandas 2.x / NumPy 2.x / PyTorch 2.x 是 breaking change 的邊界。驗收：看到 2018 年的教程 code 能辨識「這段可能在 2.0 下會 warning」。

### 2.3 MVK 優先級矩陣

| 項目 | 認知類型 | 教學時間 | 後續模組依賴度 |
|------|----------|----------|----------------|
| F1–F3 | 程序性知識 | 15 min | 全部模組 |
| F4 | 概念性知識 | 5 min | M1–M9 |
| F5–F7 | 結構性知識 | 25 min | 全部模組 |
| F8–F9 | 情境性知識 | 15 min | M18–M20 |
| F10 | 程序性知識 | 15 min | M4–M14 |
| F11–F12 | 元認知 | 10 min | 全部模組 |

**總時間**：85 分鐘。這與 M0 預計 90 分鐘（120 - 30 workshop）吻合。

### 2.4 可砍除的「Nice-to-have」

以下內容可在 M0 砍除而不影響後續學習：

- PEP 703 No-GIL 細節（放到 M18+ 的進階補充）
- Stack Overflow Developer Survey 2025 數字（講 JetBrains 一份就夠）
- PyTorch 2.0 torch.compile 30-200% 數字（放到 M15+ 深度學習）
- Polars 作為 pandas 替代的敘述（放到 M6 資料清洗）
- 費曼技巧的具體操作（學習方法論可精簡為一句 principle）

**砍除後節省**：約 20 分鐘，可用於加強 F1–F3 環境實作，這對學員長期 ROI 更高。

---

## Lens 3：Body of Knowledge — SWEBOK / SEBoK / DS-BoK 對齊

### 3.1 方法論說明

以下把 M0 的知識點對齊到三個既有學科體系：

- **SWEBOK v4** (IEEE Software Engineering Body of Knowledge, 2024)
- **SEBoK v2.8** (Systems Engineering Body of Knowledge, 2023)
- **EDISON Data Science Framework** (DS-BoK, 2017，目前事實標準)

### 3.2 對齊表

#### 3.2.1 SWEBOK 對齊

| M0 知識點 | SWEBOK Knowledge Area | 涵蓋深度 |
|-----------|----------------------|----------|
| S03 生態系地圖 | KA: Software Construction → Construction Languages | 🟢 涵蓋（概念層） |
| S04 版本里程碑 | KA: Software Configuration Management → Release Management | 🟡 淺層（僅提版本號，未提語意化版本） |
| S06 軌道二工程實踐 | KA: Software Engineering Process, Tools, Quality | 🟡 淺層（僅點名，未深入） |
| S05 AI 產品四層 | KA: Software Architecture → Architectural Structures | 🟢 涵蓋（映射到分層架構） |
| 工作坊 venv + pip | KA: Software Engineering Tools → Environment Management | 🟢 涵蓋 |

**SWEBOK 未涵蓋的缺口**：
- KA: Software Requirements（課程對「需求工程」完全未提）
- KA: Software Testing（軌道二提 Linting 但未提 unit testing for ML）
- KA: Software Maintenance（沒有討論 model / code 維護策略）
- KA: Software Engineering Economics（薪資敘述屬此，但未系統化）

#### 3.2.2 SEBoK 對齊

| M0 知識點 | SEBoK Part / Knowledge Area | 涵蓋深度 |
|-----------|----------------------------|----------|
| S05 AI 產品解剖圖 | Part 3: Systems Engineering → System Lifecycle Processes | 🟡 淺層（僅分層，未討論 lifecycle） |
| S06 雙軌設計 | Part 6: Related Disciplines → Software/Systems Engineering Interface | 🟢 涵蓋（雙軌本質上是此交界） |
| S07 24 小時路線圖 | Part 4: Applications → Product Systems Engineering | ❌ 未對齊 |

**SEBoK 未涵蓋的重大缺口**：
- Emergence（系統湧現屬性，ML 系統最關鍵的特徵）完全未討論
- Stakeholder Needs & Requirements — M0 完全缺失「誰是這個 AI 產品的使用者」這個系統工程核心問題
- System Assurance（可信賴 AI、safety engineering）未提

#### 3.2.3 EDISON Data Science Framework (DS-BoK) 對齊

| M0 知識點 | DS-BoK Group | 涵蓋深度 |
|-----------|--------------|----------|
| S03 生態系地圖 | DSENG (Data Science Engineering) | 🟢 涵蓋 |
| S05 AI 產品四層 | DSDA (Data Analytics) + DSENG | 🟢 涵蓋 |
| S06 軌道一（資料+AI） | DSDM (Data Management) + DSDA | 🟡 淺層 |
| S02 調查報告 | DSPM (Data Science Professional Practice) | 🟢 涵蓋（背景知識） |
| 工作坊 | DSDA + DSENG | 🟢 涵蓋 |

**DS-BoK 未涵蓋的缺口**：
- **DSDK (Data Science Domain Knowledge)** — 完全未提「領域知識是資料科學的一半」
- **DSRMP (Research Methods and Project Management)** — 未提科學方法、假設檢定哲學
- **DSBA (Business Analytics)** — 未連結到商業決策情境，「數據變決策」停留在口號
- 資料倫理、隱私、偏見這些 DS-BoK 的必修項目，在 M0 完全空白

### 3.3 三個 BoK 合計的重大空白

將三個 BoK 交叉比對，M0 在以下**跨體系的重要條目**完全缺席：

1. **需求工程 / 利害關係人分析**（SWEBOK + SEBoK）
2. **測試工程（包含 ML-specific testing）**（SWEBOK）
3. **系統湧現與可信賴性**（SEBoK）
4. **領域知識整合**（DS-BoK）
5. **研究方法與假設檢定**（DS-BoK）
6. **資料倫理與治理**（DS-BoK）

這 6 項對一門「AI 工程基礎」課程而言是嚴重缺口。建議在 M0 至少用一張投影片承認這些領域的存在（而非佯裝不存在）。

---

## 三視角合流建議：教師如何交替佈課

### Teaching Choreography（佈課編排）

#### 開場（S01）— 用 Fundamentals Lens
直接告訴學員「這 90 分鐘要你帶走 12 個 checklist」，降低焦慮，給出明確驗收。

#### 敘事段（S02-S07）— 主用 First Principles Lens
每介紹一個新概念（生態系、公式、雙軌），往下推一層「為什麼」。不要停在「產業都這樣」。First Principles 讓學員獲得**可遷移的推理能力**。

#### 方法論段（S08）— 用 Body of Knowledge Lens
承認 M0 的邊界，告訴學員「我們沒教的東西在哪裡」（需求工程、倫理、測試）。這反而建立學員的元認知地圖，讓他們知道 24 小時之外還有多少領地。

#### 工作坊（30 min）— 三視角交織
- **Fundamentals**：完成 F1–F3 的 checklist 驗收
- **First Principles**：討論題「為什麼需要虛擬環境」推到依賴隔離的本質
- **BoK**：在反思紀錄中填入「我最想補的 BoK 空白領域」

#### 收尾（S09）— 回到 First Principles
金句「你不是在學工具，你在取得入場券」 → 本質是「你在學的是翻譯器 + 分層系統 + 雙認知模式」三個不會過時的原理。工具會變，原理不會。

### 三視角的檢查問題（每次備課用）

1. **First Principles 檢查**：我這張投影片的主張，能不能推到物理 / 資訊理論 / 經濟學三層之一？若不能，是話術。
2. **Fundamentals 檢查**：這張投影片對應哪一條 F1–F12？若對應不到，是 nice-to-have，考慮刪除。
3. **BoK 檢查**：這張投影片涵蓋了 SWEBOK/SEBoK/DS-BoK 哪個 KA？是否誠實標註了「未涵蓋」的邊界？

三個檢查都通過，這張投影片才算**結構合格**。

---

## 結論：M0 的三視角健康度體檢

| 視角 | 健康度 | 主要問題 |
|------|--------|----------|
| First Principles | 🟡 中 | 敘事停在「產業觀察」層，未下推到資訊理論/經濟學 |
| Fundamentals | 🟢 良好 | 12 條 MVK 與 90 分鐘時間吻合，可操作性強 |
| Body of Knowledge | 🔴 待改善 | 6 個重要 BoK 條目完全未提，邊界未誠實標註 |

**整體診斷**：M0 作為一個 **宏觀敘事** 模組合格，作為一個 **學科定位** 模組不合格。建議在 S09 之前插入一張「本課程的邊界」投影片，明文承認未涵蓋的 BoK 領域，並指出延伸閱讀路徑。

---

*— End of Three Lens Analysis —*
