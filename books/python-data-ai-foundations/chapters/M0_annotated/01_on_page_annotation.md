# M0 On-Page 技術註記 — 逐知識點 Review

> **本文件定位**：這是一份內部技術 review 文件，不是給學生看的教材。
> **讀者**：課程 co-author、資深工程師、TA、技術審稿人。
> **使用情境**：出書前的技術辯論會、模組定稿前的 red team 會議、助教訓練前的技術對齊。
> **語氣**：直接、批判，挑錯比給讚多。凡是讀過 production ML pipeline 的人看到這份文件，應該能立刻找到可以辯論的點。

---

## 0. 模組頂層聲明的 Review

### 知識點 0.1：「這不是一堂 Python 語法課」

**🎯 宏觀定位**
這句話是整門 24 小時課程的「北極星 statement」，決定了 M0–M20 的敘事基調：Python 是載體，系統思維才是產品。如果這句話沒有立住，後面所有「雙軌設計」「AI 解剖圖」都會被學員當成賣弄術語。

**🔬 細部強化**
- 「語法只是通行證」這個比喻在工程上是危險的半真半假。語法不熟的工程師在 debug `pandas` chained indexing、`async/await` 傳染性、`__slots__` 行為時會吃大虧。對學員要明講：**不是不重要，是不在這門課教**。
- 「把資料變成決策、把模型變成產品、把想法變成系統」三句話在排版上是金句，但在教學上是三個完全不同的職能（Data Analyst / ML Engineer / Software Architect）。別讓學員誤以為 24 小時能同時覆蓋這三個角色。

**⚠️ 技術討論 reviewer 提問**
1. 「Python 思維」到底是什麼？能否給出一個可證偽的操作定義？（否則就是話術）
2. 如果學員只剩 2 小時，這句話會不會讓他們跳過 M1–M3 直接衝 PyTorch？那樣反而害了他們。
3. 是否該加一句反向校正：「但你仍然需要認真學會 list comprehension、generator、context manager，這門課假設你會在自修時補足」？

---

### 知識點 0.2：引言 "Data is the raw material; Python is the operating language."

**🎯 宏觀定位**
這是全課程的 tagline，會重複出現在 S01、S09、講義封面。功能類似 BCG 的 governing thought。

**🔬 細部強化**
- 「Operating language」這個詞組在英文語感上更接近 "the language you operate in"（你工作時使用的語言），而非 operating system 的 operating。容易讓學員誤解為「Python 是作業系統」。S02 裡又真的用了「AI 產業的作業系統」這個隱喻，兩個隱喻打架。**建議統一**：要嘛全部用「產業作業系統」(industry OS)，要嘛全部用「操作語言」(operating language)，不要混用。
- Raw material / operating language 的對偶，在中文語境下「原料 / 操作語言」並不對仗，翻譯上可考慮「資料是素材，Python 是你手上的工具機」。

**⚠️ 技術討論 reviewer 提問**
1. 對 2026 年的現實，SQL 其實才是資料真正的 operating language。這句話對資料工程師是否站得住腳？
2. 如果把 Python 換成 TypeScript / Rust / Julia，這句話是否依然成立？可證偽性有多強？

---

## 1. S01：你為什麼在這裡

### 知識點 1.1：「只會 Python 和 懂 Python 生態系 + 能交付 AI 產品的薪資差距 3-5 倍」

**🎯 宏觀定位**
S01 唯一的量化主張，用來給學員動機錨點。如果數字被挑戰，S01 的說服力會崩盤。

**🔬 細部強化**
- 「3-5 倍」這個數字**沒有引用來源**，跟 S02 的調查資料引用格式不一致。內部 review 的第一要求：**補上來源**（Levels.fyi、LinkedIn Talent Insights、104 資料科學職缺調查其中之一）。
- 台灣市場實際觀察：初階 Python 工程師 vs. 資深 ML Engineer 的薪資差距落在 2–3 倍較為常見，3–5 倍是 Sr. ML Engineer vs. Junior 的區間。這個陳述在台灣市場要小心，容易被學員事後查證打臉。
- 「交付 AI 產品」的定義不清。端到端的 LLM 應用？還是 classical ML on tabular data？薪資區間差很大。

**⚠️ 技術討論 reviewer 提問**
1. 若學員上完 24 小時，能不能真的進入「3-5 倍」那個群體？答案是否定的。這是否在設立不切實際的期望？
2. 能否改成「薪資分布的右尾」而不是具體倍數？避免被打臉又保留動機。

---

### 知識點 1.2：「24 小時後，你應該能獨立完成一個完整的資料分析管線，並對 ML 模型部署流程有全景理解」

**🎯 宏觀定位**
這是課程的 capability promise，是驗收 M0–M20 成功與否的合約條款。

**🔬 細部強化**
- 「完整的資料分析管線」= ingestion → cleaning → EDA → modeling → evaluation → reporting。24 小時平均下來，每階段 4 小時，扣掉講授時間剩 2 小時動手。這在工程實務上是**非常緊**的，真要做到，pipeline 必須是 toy dataset（<100MB，無 schema drift）。**教材中需誠實標註這個假設**。
- 「全景理解」是弱承諾，容易變成免責聲明。建議用「能畫出 deployment diagram 並解釋每一層的角色」這種可驗證的輸出取代。

**⚠️ 技術討論 reviewer 提問**
1. 如果一個學員只能做出 toy pipeline，他算不算達到了這個學習目標？驗收標準要明文化。
2. 「ML 模型部署」的全景是否包含 monitoring / drift detection / A/B test？若不包含，這個「全景」是殘缺的全景。

---

## 2. S02：2026 年的 Python 數據報告

### 知識點 2.1：JetBrains/PSF、Stack Overflow、Anaconda 三份報告的引用

**🎯 宏觀定位**
S02 是全模組**唯一**用外部數據背書的投影片，是 M0 「可信度」的承重牆。引用品質決定整門課是「有據可查」還是「講師憑感覺」。

**🔬 細部強化**
- 三份報告都是**自我選樣（self-selected）調查**，樣本並非隨機抽樣。三份都有 open-source 社群過度代表、企業閉源環境低度代表的偏誤。教材中需補一句 methodology caveat，否則就是在教學生「不要質疑引用」。
- 「年增率不減」這類模糊敘述容易被挑戰。應給出具體的年份-百分比對照。
- Stack Overflow Survey 2025 在本文件寫作時（2026-04）應已發布完整結果。需確認引用的是 final report 還是 preliminary。

**⚠️ 技術討論 reviewer 提問**
1. JetBrains 的調查樣本嚴重偏向 JetBrains IDE 使用者，這對 Python vs. 其他語言的比較有沒有系統性偏誤？
2. 三份報告的抽樣方法是否一致？能不能直接加總或比較？（答案：不能）

---

### 知識點 2.2：「Python 已進入基礎設施鎖定階段」

**🎯 宏觀定位**
這是 S02 的**關鍵洞察句**，從「流行」升級到「鎖定」是一個重要的理論判斷。

**🔬 細部強化**
- 「基礎設施鎖定」(infrastructure lock-in) 是個強命題，類比於 COBOL / Java 在金融業的鎖定。這個類比是否過度？Python 生態其實有 Rust-accelerated 子生態（Polars、Ruff、uv、Pydantic v2）正在部分取代 Python 原生實作，鎖定的邊界其實在移動。
- 真正鎖定的不是「Python 語言」，而是「Python 的 C-extension ABI + NumPy array protocol + Jupyter protocol」。這幾個介面才是真正的護城河。教學時應該把這個細節點出來。

**⚠️ 技術討論 reviewer 提問**
1. 如果 Mojo / Julia 出現一個完美 NumPy-compatible 後端，鎖定會不會在 5 年內瓦解？
2. 「鎖定」用在學員面前是否會引發反向焦慮（「我被鎖定，不能選其他語言」）？

---

### 知識點 2.3：PEP 703 / No-GIL 里程碑框

**🎯 宏觀定位**
這是給程度較高學員的 Easter egg，暗示 Python 正在解決歷史性技術債。

**🔬 細部強化**
- PEP 703 在 3.13 是 **experimental opt-in**，不是預設開啟。學員若沒讀原文，容易誤以為「2024 年後 Python 沒有 GIL 了」。教材用「正式進入標準庫」這個措辭有誤導風險，正確說法是「以 free-threaded build 的形式提供」。
- No-GIL 對資料科學的實際影響其實很小，因為 NumPy/pandas 的熱路徑早已透過 C extension 釋放 GIL。真正受益的是純 Python CPU-bound code，這在資料科學中不是主流。**這個里程碑對 M0 的學員其實沒那麼重要，放在里程碑框可能 over-emphasize**。

**⚠️ 技術討論 reviewer 提問**
1. No-GIL 對 pandas 2.x 的 performance 有沒有可量測的影響？若沒有，為什麼要在 M0 講？
2. 是否會讓學員誤以為 `threading` 從此可以取代 `multiprocessing`？

---

## 3. S03：生態系地圖

### 知識點 3.1：四層架構（互動環境 / 資料操作 / 模型 / 分散式與部署）

**🎯 宏觀定位**
這是 M0 唯一的**結構性心智模型**（structural mental model），決定學員未來學任何新工具時往哪個抽屜塞。

**🔬 細部強化**
- 這個四層分法是**教學性**分法，不是工程現實。在真實架構中，「互動環境」是 IDE 議題而非執行議題，它跟其他三層不在同一個軸上。一個更準確的分層是：**執行環境層（runtime）／資料介面層（array/frame）／演算法層（modeling）／服務層（serving/orchestration）**。
- Jupyter 放在「互動環境層」容易讓學員以為 Jupyter 是「給初學者的 IDE」，而忽略它作為 **executable document** 的本質（這也是為什麼 Netflix、Airbnb 的資料團隊把 Jupyter 當 production artifact）。
- Polars 標為「下一代高效能替代」這個 framing 有爭議。Polars 的 API 並不是 pandas 的替代品，它是不同的 DataFrame 哲學（lazy、Arrow-native、函數式）。「替代」暗示 drop-in replacement，但實際上是 paradigm shift。

**⚠️ 技術討論 reviewer 提問**
1. 為什麼把 MLflow 放「分散式/部署層」而不是和 sklearn 同層？MLflow 是 meta-tool，橫跨模型層和部署層。
2. Hugging Face Transformers 放在「模型層」與 PyTorch/TensorFlow 並列是否誤導？Transformers 依賴 PyTorch，不是同級工具。
3. 缺失的重要工具：DuckDB、Ray、Dask、Ruff、uv、LangChain、Pydantic。是刻意省略還是遺漏？刻意省略的話，選擇標準是什麼？

---

### 知識點 3.2：工具關係箭頭（NumPy → pandas → sklearn，NumPy → PyTorch，pandas → PySpark）

**🎯 宏觀定位**
這是學員建立「依賴直覺」的第一張圖，決定他們對 Python 科學計算棧的心智拓樸。

**🔬 細部強化**
- 「NumPy → PyTorch」這個箭頭有誤。PyTorch 的 tensor 是獨立實作，不依賴 NumPy。有的是**協議相容**（`__array__`、`from_numpy`、`numpy()`），不是依賴關係。教學上應該畫「NumPy ↔ PyTorch（介面相容）」而不是單向箭頭。
- 「pandas → PySpark」也不精確。PySpark 有自己的 DataFrame（Spark DataFrame），與 pandas DataFrame 是完全不同的物件。真正的橋樑是 pandas API on Spark (koalas 後繼)，但那是一個**可選介面**。
- 遺漏：NumPy → scikit-learn 是**強依賴**，應該加粗。

**⚠️ 技術討論 reviewer 提問**
1. 「依賴箭頭」和「資料流箭頭」被混在同一張圖，這在教學上是否會造成長期誤解？
2. 是否應該把 Apache Arrow 畫成一個橫跨所有工具的底層基礎？那才是真正的基建。

---

## 4. S04：里程碑版本

### 知識點 4.1：pandas 2.0 / Copy-on-Write / Arrow 後端

**🎯 宏觀定位**
這是 S04 中**唯一會影響學員寫 code 正確性**的里程碑，其他三個比較是背景知識。

**🔬 細部強化**
- Copy-on-Write (CoW) 在 pandas 2.x 是 opt-in（`pd.options.mode.copy_on_write = True`），2.2 變成 future warning，3.0 才會是預設。2026-04 的時點，需要明確告訴學員：**你現在寫的 code 會在 pandas 3.0 發布時有行為變更**。這是 M0 裡對工程實踐最重要的一句話，但投影片只是一筆帶過。
- Arrow 後端 (`dtype_backend="pyarrow"`) 也是 opt-in，不是預設。措辭「底層切換至 Apache Arrow」是錯的，正確是「**新增** Arrow-backed dtype 選項」。
- 「很多舊教程的程式碼在 2.0 下有 FutureWarning」— 舉例應該具體：`df['col'][row] = value`（chained assignment）、`inplace=True` 的各種用法、`SettingWithCopyWarning` 的新語意。

**⚠️ 技術討論 reviewer 提問**
1. 如果 M0 不講 CoW 的實際語意差異，M4–M6 的 pandas 實作課程會不會踩雷？
2. 是否應該在 M0 就要求學員設定 `pd.options.mode.copy_on_write = True`，讓他們直接寫面向未來的 code？

---

### 知識點 4.2：PyTorch 2.0 / torch.compile() 「效能提升 30–200%」

**🎯 宏觀定位**
引用 PyTorch 官方行銷數據，用於說明 DL 框架的世代跳躍。

**🔬 細部強化**
- 「30–200%」是 PyTorch 官方 blog 在 TorchBench 上量測的**平均值區間**，不是普遍經驗。實務上，對小模型、CPU 推論、dynamic shape 的 case，`torch.compile()` 反而可能變慢或報錯。
- 「不需要改動模型程式碼」是半真半假。真實狀況：需要確保模型沒有 graph break，這常常需要 rewrite forward pass。對 M0 學員來說，這個細節不重要，但講師要知道自己在簡化。

**⚠️ 技術討論 reviewer 提問**
1. 2024 年以後，torch.compile 的普及率實際如何？Hugging Face 的 model cards 有多少預設開啟？
2. 是否該提 `torch.export` / ExecuTorch，作為部署導向的下一個里程碑？

---

## 5. S05：AI 產品的解剖圖

### 知識點 5.1：核心公式 `AI product = data + code + runtime + infra`

**🎯 宏觀定位**
這是 M0 **最容易被記住**的口訣，會在全書反覆引用。

**🔬 細部強化**
- 四項加法隱含**可加性**（additivity），但實際上這四項有強烈的耦合關係。例如：runtime 的選擇（CPU / GPU / TPU）會反向影響 code（你能不能用 bfloat16、要不要寫 CUDA kernel）。教學上用加法式呈現簡單，但要在講稿中點出「這是分解，不是構成，真實產品是四者的 joint optimization」。
- **嚴重缺項**：`evaluation`、`monitoring`、`data contract`、`model governance`。對 2026 年的 MLOps 來說，evaluation pipeline 和 monitoring 是第五、第六根柱子。公式若不更新，學員會建立 2020 年的心智模型。
- 建議修正版：`AI product = data + code + runtime + infra + evaluation + governance`，或至少補一句「此為最小化公式，真實產品還需 evaluation 與 governance」。

**⚠️ 技術討論 reviewer 提問**
1. 這個公式和 Google 的 "ML Test Score" 或 MLOps Maturity Model 是否一致？若不一致，為什麼選擇這個簡化版？
2. 在 LLM 時代，prompt / context / retrieval 放在哪一格？Data？Code？還是需要新增一格？

---

### 知識點 5.2：「80% 時間花在 Data 和 Code 層」

**🎯 宏觀定位**
給學員合理的時間分配預期，避免被 runtime / infra 的複雜度嚇退。

**🔬 細部強化**
- 這個「80%」源自 2017–2019 年的 Data Scientist 職能研究（Anaconda / Kaggle surveys），2026 年已經過時。隨著 feature store、MLOps 平台、AutoML 成熟，data prep 的時間佔比在下降，evaluation + governance 的時間在上升。教材應該 update 到 2024 年後的數據（或承認自己在引用舊資料）。
- 「若不理解 Runtime 和 Infra，做出來的東西無法進入生產環境」這個斷言是對的，但跟「80% 時間花在 Data 和 Code」形成張力 — 既然 80% 在 Data/Code，那花 20% 時間就能理解 Runtime/Infra？這是矛盾訊息。

**⚠️ 技術討論 reviewer 提問**
1. 這個 80% 的引用來源？若是 Kaggle 2017 survey，是否應該明講「這個數字正在變化」？
2. Data Engineer / ML Engineer / MLOps Engineer 是三個不同職能，這個 80% 對哪個角色成立？

---

## 6. S06：課程雙軌設計

### 知識點 6.1：軌道一（資料 + AI）與 軌道二（軟體 + 系統）

**🎯 宏觀定位**
這是課程的**結構設計聲明**，直接決定 M1–M20 的順序、權重、工作坊設計。

**🔬 細部強化**
- 「雙軌」是一個**教學敘事**，不是工程現實。真實的工程師在每個任務中這兩軌是交織的（寫一個 pandas pipeline 同時涉及資料操作 + 模組化 + 測試 + 環境管理）。用「軌道」這個比喻，學員容易誤以為這是兩條平行課、可以只學一邊。應該強調「雙軌=DNA 雙螺旋」而非「雙軌=兩條鐵路」。
- 軌道二的清單缺失重要項目：**日誌（logging）、錯誤處理哲學、concurrency 基礎、I/O 模式（同步 vs. 非同步）**。這些是「能寫 code」到「能交付產品」的真實差距，比 Linting 重要得多。
- 「Jupyter 與 Git 的衝突問題」被點名是好事，但解法只有兩派（nbstripout vs. jupytext），教材需要表態選哪個。

**⚠️ 技術討論 reviewer 提問**
1. 為什麼 SQL 不在任一軌道？2026 年的資料工作者不會 SQL 是重大缺陷。
2. 「整合工作坊」的比例是 30%，具體是每個模組都有 30%，還是某幾個模組 100%？排程需要明確。

---

### 知識點 6.2：「軌道二常被忽略，但它是從能寫程式碼到能交付產品的關鍵差距」

**🎯 宏觀定位**
這句是軌道二的**存在辯護**，回應「學資料科學為什麼要學 Git 和 Docker」的質疑。

**🔬 細部強化**
- 這個論點成立，但**只有一半正確**。另一半：軌道二的很多技能（CI、Docker、基礎部署）在公司裡本來就有 DevOps / Platform team 負責，資料科學家學過就好，不需要精通。教材若把軌道二吹得太重要，會讓學員誤以為自己要同時做兩份工。
- 更準確的敘述：「軌道二的目的不是讓你成為 DevOps，而是讓你能**跟 DevOps 對話**，以及在沒有 DevOps 的小團隊獨立出貨。」

**⚠️ 技術討論 reviewer 提問**
1. 軌道二的驗收標準是什麼？學員能不能寫 Dockerfile 就算通過？還是要能 debug container networking？
2. 若學員在大公司（有 DevOps 團隊），軌道二的 ROI 是否應重新評估？

---

## 7. S07：24 小時路線圖

### 知識點 7.1：模組時數分配（M0:2 / M1-3:6 / M4-6:6 / M7-9:4 / M10-14:4 / M15-17:2 / M18-20:0）

**🎯 宏觀定位**
這是整個課程的**時間預算**，一旦公布就是契約。

**🔬 細部強化**
- M10–M14 **五個模組 4 小時**意味著平均每個模組 48 分鐘。這對「sklearn 工作流 + 監督學習 + 模型評估 + Pipeline」來說**極度緊縮**。光是「模型評估」一題（confusion matrix、ROC-AUC、cross-validation、train-test leakage）認真講就要 1 小時。這個排程在技術上不可行，除非每個模組退化成「10 分鐘介紹 + 自修指引」。
- M18–M20 標註「0 小時，概念模組」是誠實的，但名為「模組」卻沒時數會讓學員混淆。建議改名「補充閱讀」或「延伸地圖」。
- M15–M17 深度學習 2 小時只能做到「讓學員知道 tensor 是什麼」，這個期望管理在 S07 的敘述中不夠清楚。

**⚠️ 技術討論 reviewer 提問**
1. 時數分配的依據是什麼？是從教學目標反推，還是湊 24 小時的總量？
2. 若 M10–M14 真的只能 4 小時，是否應該砍到 M10–M12 三個模組就好，避免假裝涵蓋？

---

## 8. S08：學習方法論

### 知識點 8.1：「主動學習者留存率高 6 倍」

**🎯 宏觀定位**
這是 S08 的**量化 hook**，用來說服學員動手做。

**🔬 細部強化**
- 「6 倍」對應的是 NTL Institute 的 **Learning Pyramid**（學習金字塔），該模型在教育學術界被反覆批評為**無實證基礎**（原始數據無法溯源）。引用它會讓有教育背景的讀者質疑整個課程的科學性。
- 更安全的引用：Freeman et al. (2014) PNAS 的 meta-analysis（active learning in STEM），顯示 active learning 將 failure rate 從 34% 降到 22%。這是有 peer-reviewed 背書的。**強烈建議替換**。

**⚠️ 技術討論 reviewer 提問**
1. 學習金字塔的引用是否要撤回？撤回會不會削弱 S08 的說服力？
2. 「費曼技巧」在 ML/DL 這種高度數學化的領域是否有效？費曼自己教物理時也承認不是所有主題都能「用簡單語言解釋」。

---

### 知識點 8.2：「先讓程式能跑，再讓它跑得好，再讓它跑得快」

**🎯 宏觀定位**
這是軌道二的**工程哲學原則**，出自 Kent Beck 的 "Make it work, make it right, make it fast"。

**🔬 細部強化**
- 引用時應該**給出原始出處**（Kent Beck / XP movement），否則變成講師原創口號，失去 credibility。
- 「跑得好」在原版是 "make it right"（正確性），翻成「跑得好」有歧義（好 = 優雅？正確？易讀？）。建議改為「**先讓它能跑，再讓它正確，再讓它快**」。
- 在 ML context 下這個順序要小心。ML code 的「正確」包含資料正確性（沒有 train-test leakage、沒有 target leakage），這比傳統軟體的「正確」更微妙。若只強調 make it work，學員容易交出一個 accuracy 99%（因為 leakage）的「可跑」pipeline。

**⚠️ 技術討論 reviewer 提問**
1. 在 ML 專案中，「正確」的驗收標準跟傳統軟體有何不同？
2. 是否應在 M10+ 的 ML 模組中重新引用這句話，並加上 ML 專屬的詮釋？

---

### 知識點 8.3：「搜尋策略：官方文檔 → Stack Overflow → AI」

**🎯 宏觀定位**
這是 S08 最有實操價值的**工作流建議**，直接影響學員 debug 效率。

**🔬 細部強化**
- 2026 年的現實：**這個順序已經顛倒**。多數工程師遇到問題會先問 AI（Claude / ChatGPT / Cursor），AI 解不了才查 Stack Overflow 或官方文檔。堅持舊順序是教條，不符合當前工作流。
- 但是，AI 答案有**幻覺風險**，特別是 pandas/PyTorch 這種 API 快速演進的庫。正確的順序不是「哪個先用」，而是「哪個**作為真相來源**」：AI 可以用來生成假設，但驗證必須回到官方文檔。
- 建議改為：「**用 AI 加速探索，用官方文檔驗證真相，用 Stack Overflow 看他人踩過的坑**。」這才是 2026 年的實際工作流。

**⚠️ 技術討論 reviewer 提問**
1. 這個傳統順序是否源自前 AI 時代的直覺？在 2026 年還能成立嗎？
2. 是否應該教學員「如何識別 AI 幻覺」（例如檢查 API 是否真的存在），這比順序更重要。

---

## 9. 工作坊段落 Review

### 知識點 9.1：`pip install jupyter pandas numpy matplotlib scikit-learn`

**🎯 宏觀定位**
這是學員寫的**第一行 production 相關的指令**，會建立他們的環境管理習慣。

**🔬 細部強化**
- 2026 年還在教 `pip install` 裸裝是**嚴重過時**。當前最佳實踐：**uv**（Astral 出品，10–100x faster than pip，2024 起成為新標準）。教材應該教 `uv pip install` 或至少提 `uv` 作為 recommended path。
- `python -m venv .venv` 也已不是最佳選擇。`uv venv` 比 `python -m venv` 快一個量級，且行為更一致。
- 不指定版本的 `pip install` 在 24 小時後會因 pandas / numpy 小版本不同導致學員間行為不一致。應該給出 `requirements.txt` 或 `pyproject.toml` with pinned versions。

**⚠️ 技術討論 reviewer 提問**
1. 為什麼不教 uv？是刻意保守還是遺漏？若是保守，本課程的「2026 版」定位就站不住。
2. 工作坊是否該在 M0 就建立 lock file 的概念？還是留給軌道二後面處理？

---

### 知識點 9.2：`python --version  # 應為 3.11 或更高`

**🎯 宏觀定位**
環境 baseline 聲明。

**🔬 細部強化**
- 2026-04 的時點，Python 3.13 已正式發布（2024-10），3.14 進入 beta。要求 3.11+ 是合理的（3.11 加入了明顯的效能提升和 better error messages），但若課程要用 free-threaded 功能（S02 提到），就需要 3.13t build。
- 沒說明如何在多版本 Python 環境下切換（pyenv / uv python install）。Windows 用戶和 macOS Homebrew 用戶的 Python 來源差異很大，這在助教 troubleshooting 時是大坑。

**⚠️ 技術討論 reviewer 提問**
1. 是否應該鎖定單一版本（例如 3.12.x）而非「3.11+」？鎖定的好處是 reproducibility，壞處是把用 3.13 的學員排除。
2. Windows Store 版 Python vs. python.org 版 vs. Anaconda 版，在本課程的假設是哪一個？

---

## 10. 講師備注 Review

### 知識點 10.1：「Python 本身慢，但 NumPy/pandas/PyTorch 的核心是 C/C++/CUDA」

**🎯 宏觀定位**
回應「為什麼不用 Rust/Go」的 FAQ，是工程直覺題。

**🔬 細部強化**
- 這個答案**正確但不完整**。補充：
  1. Python 慢的是 **interpreter overhead**，對於 IO-bound 任務（多數 data pipeline）其實無關緊要。
  2. 「膠水語言」這個詞源自 1990 年代的 Python 社群論述，學員可能沒聽過，需要解釋。
  3. 2024 年後的變化：Rust 正在**吃掉 Python 生態**的底層（Polars、Ruff、uv、Pydantic v2 core、tokenizers）。所以真正的答案不是「Python vs. Rust」，而是「Python 作為 orchestration layer + Rust/C++ 作為 compute layer」的混合。

**⚠️ 技術討論 reviewer 提問**
1. 若學員再追問「那我要不要學 Rust？」，講師的標準答案是什麼？
2. 「膠水語言」這個詞是否應該更新為 "orchestration language" 或 "control plane language"？

---

## 11. 模組總結的 Review

### 知識點 11.1：「建立視野 / 建立地圖 / 建立期望」三件事

**🎯 宏觀定位**
M0 的 deliverable 自我聲明。

**🔬 細部強化**
- 三件事都是「心態類」deliverable，沒有任何**可驗證**的知識點產出。對比其他課程模組（M1 結束時學員能寫 type hints），M0 的 deliverable 偏軟。
- 工作坊已經提供了可驗證的產出（`M0_ecosystem_map.ipynb`），但沒被列在「模組總結」裡。應該把工作坊產出列為第四件事：「**建立第一個版本化的學習紀錄**」。

**⚠️ 技術討論 reviewer 提問**
1. 若學員完成 M0 但沒做工作坊，他算通過 M0 嗎？通過與否的定義需要寫死。
2. 「建立期望」會不會和其他模組的「建立期望」重複？每個模組的 kickoff 都在做類似的事，M0 和 M1 的邊界在哪裡？

---

## 12. 整體 Review 總結：10 個結構性問題

這份 M0 寫得好的地方是**敘事節奏**和**視覺設計意圖**，寫得弱的地方是**技術精確性**和**時效性**。以下 10 個問題是內部 review 前必須決議的：

1. **引用不一致**：S01 的「3-5 倍薪資差距」無來源，但 S02 有三份報告引用。標準要統一。
2. **口號衝突**：「operating language」和「產業作業系統」兩個隱喻打架。
3. **過時工具鏈**：教 `pip + venv` 而不教 `uv` 在 2026 年是倒退。
4. **CoW 誤導**：pandas 2.0 的 Copy-on-Write 是 opt-in，教材講得像預設。
5. **80% 數字過時**：data prep 佔 80% 的說法是 2017-2019 年的數據。
6. **公式缺項**：`data + code + runtime + infra` 缺 evaluation 和 governance。
7. **學習金字塔引用問題**：「6 倍留存率」基於無實證的理論，應撤換。
8. **搜尋策略倒置**：2026 年的工作流是 AI 先、文檔驗證，不是文檔先。
9. **時數分配不可行**：M10-M14 四小時覆蓋 sklearn 全工作流太緊。
10. **雙軌比喻陷阱**：應強調雙螺旋交織，而非平行鐵路。

**Recommendation**：在定稿前至少解決 1、3、4、6、7 五項，其他可作為 v1.1 修訂。

---

*— End of M0 On-Page Annotation —*
