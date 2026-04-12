# M0：開場 — Python 與 AI 系統全景

> **課程定位**：24 小時「Python 資料分析 + AI 工程基礎」第 0 模組
> **時長**：2 小時（含工作坊 30 分鐘）
> **先修需求**：無，但建議已安裝 Python 3.11+

---

## 模組定位聲明

這不是一堂 Python 語法課。

這是你進入 AI 世界的第一道門。語法只是通行證，真正重要的是：你能不能用 Python 思維把資料變成決策、把模型變成產品、把想法變成系統。

**本模組的任務**：建立全局視野，讓你在學完第一行 `import pandas as pd` 之前，就知道自己在哪裡、要去哪裡、為什麼要去那裡。

> "Data is the raw material; Python is the operating language."

> "AI product = data + code + runtime + infra"

---

## 模組學習目標

完成本模組後，學員能夠：

1. 說明 Python 在 2026 年資料科學與 AI 工程領域的主導地位及其原因
2. 繪製 Python 生態系核心工具地圖（從 Jupyter 到 PyTorch 到 Spark）
3. 識別課程雙軌設計（資料 + AI 能力線 vs. 軟體 + 系統線）並知道自己目前在哪個位置
4. 說出課程 24 小時的主要里程碑與內容脈絡
5. 建立「工具是手段，問題求解才是目的」的學習心態

---

## 投影片大綱總覽

| # | 投影片標題 | 核心訊息 | 預估時間 |
|---|------------|----------|----------|
| S01 | 你為什麼在這裡 | 重新定義這門課的性質 | 8 min |
| S02 | 2026 年的 Python 數據報告 | 用調查數據說話，建立信心 | 12 min |
| S03 | 生態系地圖：從 Jupyter 到 Spark | 讓工具有位置感，不再茫然 | 15 min |
| S04 | 里程碑版本：這幾年發生了什麼 | 技術演進的歷史感 | 10 min |
| S05 | AI 產品的解剖圖 | 看清全局：data + code + runtime + infra | 12 min |
| S06 | 課程雙軌設計 | 知道自己在哪條線、去哪裡 | 12 min |
| S07 | 24 小時路線圖 | 建立課程整體預期 | 10 min |
| S08 | 學習方法論 | 主動學習 vs. 被動聽課 | 8 min |
| S09 | 你的票，通向未來 | 收尾的情感錨點 | 3 min |

---

## 詳細投影片規格

---

### S01：你為什麼在這裡

**核心訊息**：這不是語法課，是進入 AI 世界的入場券。

**講師要點**：
- 開門見山：「如果你只是要學 Python 語法，YouTube 10 小時教學已經夠了。你來這裡是因為你想做更大的事。」
- 點出 2026 年的現實：工作市場中「只會 Python」和「懂 Python 生態系 + 能交付 AI 產品」的薪資差距已達 3-5 倍
- 定義課程的性質：這是一門「從資料素養到 ML/DL/BigData 邊界」的旅程，Python 是語言，但目的地是系統思維
- 明確學員終點：24 小時後，你應該能獨立完成一個完整的資料分析管線，並對 ML 模型部署流程有全景理解
- 設立心理契約：「這堂課不會讓你成為專家，但會讓你知道專家在解決什麼問題」

**視覺建議**：
- 全螢幕黑底白字的開場引言：「Data is the raw material; Python is the operating language.」
- 緊接一張對比圖：左側「語法學習者」（停在 for loop 層），右側「AI 工程師」（站在系統架構層），用高度差視覺化技能天花板

**轉場**：「先告訴我為什麼值得花 24 小時在這裡 — 來看數據怎麼說。」

---

### S02：2026 年的 Python 數據報告

**核心訊息**：Python 的主導地位有數據支撐，不是信仰。

**講師要點**：
- JetBrains/PSF 2024 Python Developer Survey：Python 連續多年為最常用語言，資料科學、ML/AI 使用率穩定在前三名，年增率不減
- Stack Overflow Developer Survey 2025：Python 在「最受歡迎語言」與「AI/ML 最常使用語言」雙榜並列第一
- Anaconda State of Data Science 2024：企業採用 Python 作為首要資料平台的比率達 70%+，Jupyter Notebook 仍是最普遍的交互式工作環境
- 一個關鍵洞察：Python 的增長已超越「學習熱潮」，進入「基礎設施鎖定」階段 — 大型企業的 ML pipeline 幾乎全部基於 Python 生態
- 對學員的意義：你選擇的不只是一個流行語言，你選擇的是當前 AI 產業的「作業系統」

**視覺建議**：
- 三份報告的 logo 並排，搭配各自最關鍵的一個數字（如 48% 用 Python 做 ML、#1 最受歡迎等）
- 折線圖：2019–2025 Python 在 Stack Overflow 調查中的語言排名趨勢
- 標註框：「里程碑：Python 3.13 + PEP 703 (No-GIL) — 2024 年正式進入標準庫」

**里程碑插入點**：
- 引用 JetBrains/PSF Python Developer Survey 2024（[jetbrains.com/lp/devecosystem-2024/python](https://www.jetbrains.com/lp/devecosystem-2024/python)）
- 引用 Stack Overflow Developer Survey 2025
- 引用 Anaconda State of Data Science Report 2024

**轉場**：「數字說服了你。現在讓我們看清楚這個生態系長什麼樣子。」

---

### S03：生態系地圖：從 Jupyter 到 Spark

**核心訊息**：工具不是孤島，每個工具都有它的位置和職責。

**講師要點**：
- 介紹分層生態系架構，分為四層：互動環境層、資料操作層、模型層、分散式/部署層
- 互動環境層：Jupyter Notebook / JupyterLab / VS Code — 你思考和實驗的地方
- 資料操作層：NumPy（數值核心）、pandas（表格資料）、Polars（下一代高效能替代）、Matplotlib / Seaborn / Plotly（視覺化）
- 模型層：scikit-learn（傳統 ML）、PyTorch / TensorFlow（深度學習）、Hugging Face Transformers（LLM 應用）
- 分散式/部署層：Apache Spark / PySpark（大資料）、MLflow（實驗追蹤）、FastAPI（模型服務）、Docker（容器化）
- 強調：這張地圖就是本課程的「目錄」，每個工具在後續模組都會出現

**視覺建議**：
- 核心視覺：一張分層架構圖，用顏色區分四層，每層列出 2-4 個工具名稱加圖標
- 特別標記：哪些工具本課程會深入教、哪些只做概念介紹（用實心/空心圓區分）
- 工具關係箭頭：NumPy → pandas → sklearn，NumPy → PyTorch，pandas → PySpark

**轉場**：「這些工具不是憑空冒出來的。讓我們看它們這幾年發生了什麼巨變。」

---

### S04：里程碑版本：這幾年發生了什麼

**核心訊息**：Python 生態正在劇烈演進，你學的是 2025 年的版本，不是 2018 年的。

**講師要點**：
- **pandas 2.0（2023 年）**：底層切換至 Apache Arrow 記憶體格式，Copy-on-Write 語意改變，效能大幅提升 — 很多舊教程的程式碼在 2.0 下有 `FutureWarning`，要注意
- **NumPy 2.0（2024 年）**：第一個重大版本，API 清理，dtype 行為更一致，部分舊程式碼需要修改
- **PyTorch 2.0（2023 年）**：引入 `torch.compile()`，模型訓練速度提升 30–200%，不需要改動模型程式碼
- **Python 3.12/3.13 + PEP 703（2024 年）**：實驗性 Free-threaded（No-GIL）模式，正式開始解鎖 CPU 多核並行；3.13 正式版含 JIT 編譯器實驗旗標
- 對學員的意義：「你不是在學一個靜態工具，你在追一個快速行進的生態。學會怎麼看 changelog 比背 API 更重要。」

**視覺建議**：
- 時間軸（2022–2026），標記各大版本釋出日期
- 每個里程碑用一行黃底文字框強調最重要的一個變化
- 最後加一個「預告框」：Python 3.14 / pandas 3.0 預計方向

**里程碑插入點**：
- pandas 2.0 Migration Guide（[pandas.pydata.org/docs/whatsnew/v2.0.0.html](https://pandas.pydata.org/docs/whatsnew/v2.0.0.html)）
- NumPy 2.0 Release Notes
- PyTorch 2.0 Blog（[pytorch.org/blog/pytorch-2.0-release](https://pytorch.org/blog/pytorch-2.0-release/)）
- PEP 703 — Making the Global Interpreter Lock Optional

**轉場**：「知道工具在哪裡、發展到哪裡。現在問最核心的問題：AI 產品到底是什麼做的？」

---

### S05：AI 產品的解剖圖

**核心訊息**：一個 AI 產品背後有四個層次，Python 是貫穿全局的語言。

**講師要點**：
- 提出核心公式：**AI product = data + code + runtime + infra**
- **Data 層**：原始資料的收集、清洗、轉換、儲存 — 這是 pandas / SQL / Spark 的舞台
- **Code 層**：特徵工程、模型訓練、評估、預測邏輯 — 這是 sklearn / PyTorch / Hugging Face 的舞台
- **Runtime 層**：模型服務化、API 端點、推理優化 — FastAPI、ONNX、TorchServe
- **Infra 層**：容器化、雲端部署、監控、版本管理 — Docker、MLflow、云平台
- 重要洞察：大多數「AI 工程師」80% 的時間花在 Data 和 Code 層，但若不理解 Runtime 和 Infra，做出來的東西無法進入生產環境
- 對學員的意義：本課程覆蓋 Data + Code 層的核心，並提供 Runtime + Infra 的概念地圖

**視覺建議**：
- 四層堆疊架構圖，每層標注代表工具和技能
- 用顏色梯度（深藍到淺藍）表示「基礎設施到應用層」的抽象程度
- 在圖旁加一個「本課程覆蓋範圍」的括號標記

**轉場**：「你現在知道地圖了。讓我解釋這門課怎麼帶你走過這張地圖。」

---

### S06：課程雙軌設計

**核心訊息**：課程有兩條平行的能力線，你需要同時進步。

**講師要點**：
- **軌道一：資料 + AI 能力線**
  - 資料素養（數據類型、統計思維、視覺化判讀）
  - 資料操作（pandas、NumPy、資料清洗管線）
  - 機器學習（監督學習、評估、特徵工程）
  - 深度學習入門（PyTorch 基礎、神經網路直覺）
  - 大資料預覽（PySpark 概念、分散式計算思維）
- **軌道二：軟體 + 系統線**
  - Python 工程實踐（型別標注、模組化、測試）
  - 版本管理（Git 工作流、Jupyter 與 Git 的衝突問題）
  - 環境管理（venv / conda / uv，可重現性）
  - 程式碼品質（Linting、格式化、CI 概念）
  - 基礎部署（FastAPI 包裝模型、Docker 概念）
- 兩軌的交點是每個模組的「整合工作坊」，學員在真實資料集上同時練習兩軌技能
- 強調：軌道二常被忽略，但它是從「能寫程式碼」到「能交付產品」的關鍵差距

**視覺建議**：
- 雙軌鐵路圖，兩條軌道平行延伸，中間有「整合工作坊」的枕木連接點
- 每條軌道列出主要站點（4-5 個），用圓圈標記
- 軌道末端匯合成一個終點站：「可交付的 AI 工程基礎」

**轉場**：「兩條軌道，24 小時，讓我告訴你每一段的里程。」

---

### S07：24 小時路線圖

**核心訊息**：你知道自己要去哪裡，每一步都有意義。

**講師要點**：
- **M0（2h）**：開場與全景（本模組）
- **M1–M3（6h）**：Python 核心 + 工程基礎（語法精要、型別、函數式思維、環境與工具）
- **M4–M6（6h）**：資料操作核心（NumPy 矩陣操作、pandas 資料管線、資料清洗實戰）
- **M7–M9（4h）**：探索性資料分析（EDA 方法論、視覺化、統計直覺）
- **M10–M14（4h）**：機器學習基礎（sklearn 工作流、監督學習、模型評估、Pipeline）
- **M15–M17（2h）**：深度學習入門預覽（PyTorch 張量、自動微分直覺、簡單 MLP）
- **M18–M20（0h，概念模組）**：大資料 + 工程化預覽（PySpark 思維、MLflow 實驗追蹤、FastAPI 部署）
- 強調：前半段（M0–M9）是「地基」，沒有地基就沒有後半段的 ML/DL 穩定性
- 對學員的期望管理：「24 小時讓你有能力獨立學習，而不是讓你成為專家」

**視覺建議**：
- 橫向時間軸，標記各模組群的小時數
- 用顏色區分：基礎期（綠）、進階期（藍）、預覽期（紫）
- 在 M6 和 M14 標記「能力里程碑」檢查點

**轉場**：「路線圖清楚了。最後，我要談談怎麼學，才能真的學到。」

---

### S08：學習方法論

**核心訊息**：主動學習者比被動聽課者的留存率高 6 倍。

**講師要點**：
- **費曼技巧應用**：每個模組結束後，用自己的話解釋一個概念給假想的同事聽
- **最小可行程式（MVP Code）原則**：先讓程式能跑，再讓它跑得好，再讓它跑得快 — 這個順序不能倒
- **錯誤是資料，不是失敗**：debug 的過程就是學習的過程，保留你的錯誤紀錄
- **工作坊 > 練習題**：每個模組的整合工作坊比例 > 30%，不要跳過
- **搜尋策略**：遇到問題先看官方文檔，再看 Stack Overflow，最後才問 AI — 這個順序建立真正的理解
- 一個具體建議：建立一個 `learning_notes/` 目錄，每個模組存一個 `.ipynb` 記錄你的問題和發現

**視覺建議**：
- 「主動 vs. 被動學習」對比圖，右側列出本課程採用的主動學習手段
- 學習效率金字塔（Learning Pyramid），標記各種學習方式的知識留存率

**轉場**：「方法論在手，最後一張投影片 — 也是最重要的一張。」

---

### S09：你的票，通向未來

**核心訊息**：你不是在學一個工具，你在取得一張進入 AI 世界的門票。

**講師要點**：
- 回到開場引言：「Data is the raw material; Python is the operating language.」
- 點題：2026 年，能夠用 Python 操作資料、構建模型、交付系統的人，擁有在 AI 時代參與重要工作的資格
- 這不是誇大其詞 — 這是當前就業市場和產品開發現實的直接反映
- 課程承諾：24 小時之後，你將擁有獨立探索這個生態的能力地基，以及知道在哪裡繼續深挖的地圖
- 結語留一個問題給學員思考：「你想用 Python 解決的第一個真實問題是什麼？」

**視覺建議**：
- 全螢幕極簡設計：深色背景，中央一行大字「你不是在學工具，你在取得通往未來的入場券。」
- 底部小字：課程 GitHub repo 連結 + 社群討論頻道

---

## 工作坊 / 練習段落

**時長**：30 分鐘

**工作坊標題**：環境建置 + 生態系初探

### 練習一：建立你的學習環境（10 分鐘）

**目標**：確保所有學員的開發環境統一可用

```bash
# 步驟一：確認 Python 版本
python --version  # 應為 3.11 或更高

# 步驟二：建立課程虛擬環境
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# 或 .venv\Scripts\activate  # Windows

# 步驟三：安裝課程核心套件
pip install jupyter pandas numpy matplotlib scikit-learn

# 步驟四：確認安裝成功
python -c "import pandas as pd; print(f'pandas {pd.__version__}')"
python -c "import numpy as np; print(f'numpy {np.__version__}')"
```

**驗收標準**：能成功印出 pandas 和 numpy 版本號

---

### 練習二：你的第一個生態系地圖（15 分鐘）

**目標**：用程式碼驗證你理解工具的位置

在 Jupyter Notebook 中建立一個新的 notebook，命名為 `M0_ecosystem_map.ipynb`。

**任務**：
1. Import 以下套件並印出版本：`pandas`、`numpy`、`matplotlib`、`sklearn`
2. 用 `print()` 輸出一段文字，描述這四個套件分別在「生態系地圖」的哪一層（照你自己的理解）
3. 建立一個 Python `dict`，key 是工具名稱，value 是「用一句話說明這個工具做什麼」

```python
# 範例結構（不要複製，用你自己的話）
ecosystem = {
    "numpy": "...",
    "pandas": "...",
    "matplotlib": "...",
    "sklearn": "...",
}

for tool, description in ecosystem.items():
    print(f"{tool:15s}: {description}")
```

**討論問題**：你現在最不確定的工具是哪一個？為什麼？

---

### 練習三：反思紀錄（5 分鐘）

在 notebook 最後一個 cell，寫下：
1. 你來這門課最想解決的一個真實問題（一句話）
2. 你對哪個模組最期待？
3. 你最擔心的學習障礙是什麼？

這是你的學習契約，24 小時後我們會回頭看它。

---

## 里程碑 / 引用插入點

以下資源應在對應投影片中引用，確保技術陳述有據可查：

| 資源 | 對應投影片 | 引用重點 |
|------|------------|----------|
| JetBrains/PSF Python Developer Survey 2024 | S02 | Python 使用率、ML/AI 場景佔比 |
| Stack Overflow Developer Survey 2025 | S02 | 最受歡迎語言排名、AI 工具使用統計 |
| Anaconda State of Data Science Report 2024 | S02 | 企業 Python 採用率、Jupyter 使用率 |
| pandas 2.0 What's New | S04 | Copy-on-Write、Arrow 後端 |
| NumPy 2.0 Release Notes | S04 | API 清理、dtype 行為變更 |
| PyTorch 2.0 Blog Post | S04 | `torch.compile()` 效能提升數據 |
| PEP 703 — Making GIL Optional | S04 | Free-threaded Python 的意義 |
| Python 3.13 Release Notes | S04 | JIT 實驗旗標、PEP 703 實驗性支援 |

---

## 講師備注

### 常見學員問題預備

**Q：我需要先學 R 還是 Python？**
A：2026 年的資料科學職缺，80% 以上要求 Python。R 在學術統計領域仍有地位，但如果你的目標是 AI 工程或資料科學職位，Python 優先沒有疑問。

**Q：Python 這麼慢，為什麼不用 Rust 或 Go？**
A：Python 本身慢，但 NumPy、pandas、PyTorch 的核心都是 C/C++/CUDA 寫的。你用 Python 呼叫它們，速度不輸原生語言。Python 是「膠水語言」，黏合高效能元件。

**Q：我沒有數學背景，能學 ML 嗎？**
A：本課程 M0–M9 完全不需要線性代數或微積分。M10+ 的機器學習部分會用直覺先建立理解，數學推導是可選深入路徑。

### 時間控制提示

- S01–S02 最容易超時，學員有很多問題。預留 5 分鐘 buffer。
- S05（AI 產品解剖圖）是全場情緒最高點，不要急著跳過討論。
- 工作坊環境建置常遇到 Windows 路徑問題，建議助教提前準備 troubleshooting checklist。

---

## 模組總結

本模組完成了三件事：

1. **建立視野**：你知道 Python 在 AI 世界的地位不是偶然，有數據支撐
2. **建立地圖**：你知道生態系的工具分層和它們的職責
3. **建立期望**：你知道這 24 小時要帶你去哪裡、用什麼方法帶你去

下一模組（M1）從 Python 核心語言特性開始 — 不是「從頭教語法」，而是「從工程角度重新審視你已知的 Python」。

---

*本模組屬於「Python 資料分析 + AI 工程基礎」課程體系。*
*課程版本：v1.0 | 最後更新：2025 年*
