# M0：開場 — 為什麼是 Python，為什麼是現在

> **課程定位**：24 小時「Python 資料分析與 AI 入門」第 0 模組
> **時長**：3 小時（含工作坊 60 分鐘）
> **先修需求**：無，但建議已安裝 Python 3.11+

---

## 模組定位聲明

這不是一堂 Python 語法課。

這是你進入資料世界的第一道門。語法只是通行證，真正重要的是：你能不能用 Python 思維把資料變成洞察、把數字變成決策、把問題變成可執行的分析。

**本模組的任務**：建立全局視野，讓你在學完第一行 `import pandas as pd` 之前，就知道自己在哪裡、要去哪裡、為什麼要去那裡。

> "Data is the raw material; Python is the operating language."

> "Good analysis = clean data + right tools + clear questions"

---

## 模組學習目標

完成本模組後，學員能夠：

1. 說明 Python 在 2026 年資料科學與 AI 應用領域的主導地位及其背後原因
2. 繪製 Python 資料分析生態系核心工具地圖（從 Jupyter 到 scikit-learn）
3. 說出課程 8 個模組的主要里程碑與內容脈絡
4. 完成本機開發環境建置，並在 Jupyter 中執行第一個資料探索練習
5. 建立「工具是手段，問題求解才是目的」的學習心態

---

## 投影片大綱總覽

| # | 投影片標題 | 核心訊息 | 預估時間 |
|---|------------|----------|----------|
| S01 | 你為什麼在這裡 | 重新定義這門課的性質 | 10 min |
| S02 | 2026 年的 Python 數據報告 | 用調查數據說話，建立信心 | 15 min |
| S03 | 生態系地圖：從 Jupyter 到 scikit-learn | 讓工具有位置感，不再茫然 | 20 min |
| S04 | 里程碑版本：這幾年發生了什麼 | 技術演進的歷史感 | 15 min |
| S05 | AI 產品的解剖圖 | 看清全局：data + code + insights + action | 15 min |
| S06 | 課程 8 模組路線圖 | 知道自己在哪條路上、去哪裡 | 15 min |
| S07 | 學習方法論 | 主動學習 vs. 被動聽課 | 10 min |
| S08 | 你的票，通向未來 | 收尾的情感錨點 | 5 min |
| W01–W04 | 工作坊：環境建置 + 生態系初探 | 動手做，讓知識落地 | 60 min |

**總計：約 3 小時**

---

## 詳細投影片規格

---

### S01：你為什麼在這裡

**核心訊息**：這不是語法課，是進入資料與 AI 世界的入場券。

**講師要點**：
- 開門見山：「如果你只是要學 Python 語法，YouTube 10 小時教學已經夠了。你來這裡是因為你想做更大的事。」
- 點出 2026 年的現實：工作市場中「只會 Python」和「懂 Python 生態系 + 能交付資料分析成果」的價值差距已非常顯著
- 定義課程的性質：這是一門「從資料素養到機器學習入門邊界」的旅程，Python 是語言，目的地是資料驅動的思維與行動能力
- 明確學員終點：24 小時後，你應該能獨立完成一個完整的資料分析流程，並對機器學習的應用場景有全景理解
- 設立心理契約：「這堂課不會讓你成為專家，但會讓你知道專家在解決什麼問題，以及如何繼續往下走」
- 課程定位說明：本課程專注於資料分析與 AI 入門（單一主線）。若你之後想深入軟體工程與系統設計，可接續「系統設計與架構思維」課程

**視覺建議**：
- 全螢幕黑底白字的開場引言：「Data is the raw material; Python is the operating language.」
- 緊接一張對比圖：左側「只學語法的學習者」（停在 for loop 層），右側「資料分析從業者」（能從數據中提取洞察並交付成果），用高度差視覺化技能天花板

**轉場**：「先告訴我為什麼值得花 24 小時在這裡 — 來看數據怎麼說。」

---

### S01-B：分析成熟度階梯 — 你現在在哪裡，課程帶你到哪裡

**核心訊息**：資料分析不是只有一種，Gartner 分析成熟度模型把它分成四層。這門課帶你從第一層走到第三層的門口。

**講師要點**：
- **Gartner 分析成熟度四階梯**：
  - **Level 1 描述性分析（Descriptive）**：「發生了什麼？」— 報表、dashboard、KPI 彙總。大部分 Excel 工作停在這裡。
  - **Level 2 診斷性分析（Diagnostic）**：「為什麼發生？」— EDA、下鑽分析、根因探索。本課程 M5/M6 的核心。
  - **Level 3 預測性分析（Predictive）**：「會發生什麼？」— 統計建模、機器學習。本課程 M7 的前導。
  - **Level 4 規範性分析（Prescriptive）**：「該怎麼做？」— 最佳化、決策引擎。屬於進階課程。
- **Excel vs Python 效能對比**（讓學生直觀感受差距）：
  - 100 萬筆資料篩選：Excel 3-5 分鐘 / Python pandas 約 3 秒
  - 10 張交叉分析表：Excel 手動操作 30 分鐘 / Python groupby + pivot 10 行程式碼
  - 重複執行同一份分析：Excel 每次重做 / Python 一行指令重跑整個流程
- **課程目標定位**：本課程的 M1-M4 建立 Level 1 能力，M5-M6 建立 Level 2 能力，M7 讓你站在 Level 3 的入口看到全貌
- 關鍵訊息：大部分企業的資料團隊仍卡在 Level 1-2，能做到 Level 2 並看懂 Level 3 已經非常有價值

**視覺建議**：
- 左側：四階梯圖，從下到上標示 Descriptive -> Diagnostic -> Predictive -> Prescriptive，旁邊標注對應的核心問題
- 右側：Excel vs Python 的三組效能對比數字，用色塊對比

**轉場**：「知道目標在哪裡了，來看 Python 在這個世界的地位。」

---

### S02：2026 年的 Python 數據報告

**核心訊息**：Python 的主導地位有數據支撐，不是信仰。

**講師要點**：
- JetBrains/PSF 2024 Python Developer Survey：Python 連續多年為最常用語言，資料科學、ML/AI 使用率穩定在前三名，年增率不減
- Stack Overflow Developer Survey 2025：Python 在「最受歡迎語言」與「AI/ML 最常使用語言」雙榜並列第一
- Anaconda State of Data Science 2024：企業採用 Python 作為首要資料平台的比率達 70%+，Jupyter Notebook 仍是最普遍的交互式工作環境
- 一個關鍵洞察：Python 的增長已超越「學習熱潮」，進入「基礎設施鎖定」階段 — 大型企業的 ML pipeline 幾乎全部基於 Python 生態
- 對學員的意義：你選擇的不只是一個流行語言，你選擇的是當前 AI 產業的「作業語言」

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

### S03：生態系地圖：從 Jupyter 到 scikit-learn

**核心訊息**：工具不是孤島，每個工具都有它的位置和職責。這門課帶你走過核心的每一層。

**講師要點**：
- 介紹分層生態系架構，分為四層：互動環境層、資料操作層、分析與視覺化層、模型層
- **互動環境層**：Jupyter Notebook / JupyterLab / VS Code — 你思考和實驗的地方；這也是職場資料科學家最常用的工作介面
- **資料操作層**：NumPy（數值核心，所有矩陣運算的基礎）、pandas（表格資料操作的業界標準）
- **分析與視覺化層**：Matplotlib（底層繪圖引擎）、Seaborn（統計圖表的高階介面）、Plotly（互動式圖表）
- **模型層**：scikit-learn（傳統 ML 的完整工具箱）、Hugging Face（LLM 應用的入口）、PyTorch 概念預覽
- 延伸生態說明：Polars（下一代高效能 DataFrame）、Apache Spark / PySpark（大資料處理）屬於進階路徑
- 強調：這張地圖就是本課程的「目錄」，M1 到 M7 的每個模組都對應地圖上的一個區域

**視覺建議**：
- 核心視覺：一張分層架構圖，用顏色區分四層，每層列出 2-4 個工具名稱加圖標
- 特別標記：哪些工具本課程會深入教（實心圓）、哪些只做概念介紹（空心圓）
- 工具關係箭頭：NumPy → pandas → sklearn，NumPy → Matplotlib → Seaborn
- 在圖旁加一個標記：「本課程覆蓋範圍」括號，讓學員清楚知道邊界

**延伸討論（5 分鐘）**：
- 請學員思考：在你目前的工作或生活中，哪種資料最常出現？表格？圖片？文字？
- 對應到生態系地圖，讓學員開始建立個人的工具優先序

**轉場**：「這些工具不是憑空冒出來的。讓我們看它們這幾年發生了什麼巨變。」

---

### S04：里程碑版本：這幾年發生了什麼

**核心訊息**：Python 生態正在劇烈演進，你學的是 2025 年的版本，不是 2018 年的。

**講師要點**：
- **pandas 2.0（2023 年）**：底層切換至 Apache Arrow 記憶體格式，Copy-on-Write 語意改變，效能大幅提升 — 很多舊教程的程式碼在 2.0 下有 `FutureWarning`，要注意
- **NumPy 2.0（2024 年）**：第一個重大版本，API 清理，dtype 行為更一致，部分舊程式碼需要修改
- **scikit-learn 1.4–1.5（2023–2024 年）**：Pipeline 介面改進、更好的 metadata routing、新增多個轉換器，讓 ML 工作流更簡潔
- **Python 3.12/3.13 + PEP 703（2024 年）**：實驗性 Free-threaded（No-GIL）模式，3.13 正式版含 JIT 編譯器實驗旗標
- **Jupyter / JupyterLab 4.x（2023–2024 年）**：效能大幅改善、更好的 real-time 協作、extension 生態更穩定
- 對學員的意義：「你不是在學一個靜態工具，你在追一個快速行進的生態。學會怎麼看 changelog 比背 API 更重要。」

**視覺建議**：
- 時間軸（2022–2026），標記各大版本釋出日期
- 每個里程碑用一行黃底文字框強調最重要的一個變化
- 最後加一個「預告框」：pandas 3.0 / NumPy 2.1+ / scikit-learn 2.0 預計方向

**里程碑插入點**：
- pandas 2.0 Migration Guide（[pandas.pydata.org/docs/whatsnew/v2.0.0.html](https://pandas.pydata.org/docs/whatsnew/v2.0.0.html)）
- NumPy 2.0 Release Notes
- scikit-learn 1.4 What's New（[scikit-learn.org/stable/whats_new/v1.4.html](https://scikit-learn.org/stable/whats_new/v1.4.html)）
- PEP 703 — Making the Global Interpreter Lock Optional

**轉場**：「知道工具在哪裡、發展到哪裡。現在問最核心的問題：資料分析與 AI 應用的全景是什麼？」

---

### S05：AI 產品的解剖圖

**核心訊息**：從資料到洞察再到行動，Python 是貫穿全局的語言。初學者先紮穩前兩層。

**講師要點**：
- 提出核心公式：**資料 → 清洗 → 分析 → 視覺化 → 模型 → 洞察 → 行動**
- **資料收集與清洗層**：原始資料的讀取、清洗、轉換 — pandas / NumPy 的主場
- **分析與視覺化層**：探索性分析（EDA）、統計摘要、圖表輸出 — Matplotlib / Seaborn / Plotly
- **建模與預測層**：特徵工程、模型訓練、評估、解釋 — scikit-learn 的核心場景
- **部署與應用層**：模型服務化、API 端點、自動化報告 — FastAPI、Streamlit、MLflow（進階路徑）
- 重要洞察：大多數資料分析工作 80% 的時間花在前兩層（資料清洗與 EDA），這也是本課程的核心覆蓋範圍
- 對學員的意義：本課程從 M1 到 M7 系統地帶你通過這條路，終點是具備獨立完成端到端分析的能力
- 課程邊界說明：部署與大型系統工程屬於「系統設計與架構思維」課程的範疇

**視覺建議**：
- 線性流程圖（左到右）：資料 → 清洗 → 分析 → 視覺化 → 建模 → 洞察 → 行動
- 每個節點下標注代表工具
- 用括號標記「本課程覆蓋範圍：清洗 → 建模」，其餘部分用淡色表示

**轉場**：「你現在知道地圖了。讓我告訴你這 8 個模組如何帶你走過這張地圖。」

---

### S06：課程 8 模組路線圖

**核心訊息**：每個模組都有明確的任務，你知道每一步要去哪裡。

**講師要點**：

- **M0（3h）：開場 — 為什麼是 Python，為什麼是現在**
  - 建立全局視野，完成環境建置，建立學習心態
- **M1（3h）：資料思維與 Notebook 工作流**
  - 學會用 Jupyter 思考、資料類型與問題框架、第一次 EDA 體驗
- **M2（3h）：Python 基礎 — 資料分析必用語法**
  - 精要語法（不是全部）：list / dict / 函數 / 條件 / 迴圈，以「資料操作」為導向
- **M3（3h）：NumPy — 數值計算的核心**
  - 陣列操作、廣播規則、向量化計算思維，為 pandas 和 ML 打基礎
- **M4（3h）：pandas — 表格資料的瑞士刀**
  - DataFrame 操作、資料清洗、groupby、merge，核心使用模式
- **M5（3h）：資料視覺化 — 讓數字說話**
  - Matplotlib 基礎 + Seaborn 統計圖表 + 好圖的設計原則
- **M6（3h）：統計思維與探索性分析**
  - 描述統計、分佈直覺、相關性、假設驗證的資料導向方法
- **M7（3h）：機器學習前導 — scikit-learn 入門**
  - ML 工作流（train/test split → 訓練 → 評估）、常見監督學習算法直覺、Pipeline 概念

**課程設計說明**：
- 這是一條單一主線，專注於「資料分析 → AI 入門」
- 每個模組 3 小時，總計 24 小時
- 想深入軟體工程、系統架構的學員，可接續「系統設計與架構思維」課程

**視覺建議**：
- 橫向時間軸，8 個模組等距排列，每格標注模組名稱與時長
- 用顏色區分三階段：基礎期 M0–M2（綠）、核心工具期 M3–M5（藍）、分析與建模期 M6–M7（紫）
- 在 M2 和 M5 標記「能力里程碑」檢查點，說明達到後能做到什麼

**轉場**：「路線圖清楚了。最後，我要談談怎麼學，才能真的學到。」

---

### S07：學習方法論

**核心訊息**：主動學習者比被動聽課者的知識留存率高 6 倍。

**講師要點**：
- **費曼技巧應用**：每個模組結束後，用自己的話解釋一個概念給假想的同事聽。如果解釋不清楚，就是還沒真正學會
- **最小可行程式（MVP Code）原則**：先讓程式能跑，再讓它跑得好，再讓它跑得快 — 這個順序不能倒
- **錯誤是資料，不是失敗**：debug 的過程就是學習的過程，保留你的錯誤紀錄
- **工作坊 > 練習題**：每個模組的動手時間佔比超過 30%，不要跳過
- **搜尋策略**：遇到問題先看官方文檔，再看 Stack Overflow，最後才問 AI — 這個順序建立真正的理解，而不只是得到答案
- **建立學習日誌**：建立一個 `learning_notes/` 目錄，每個模組存一個 `.ipynb` 記錄你的問題和發現。24 小時後，這個目錄本身就是你能力成長的證明

**視覺建議**：
- 「主動 vs. 被動學習」對比圖，右側列出本課程採用的主動學習手段（工作坊、反思紀錄、問題解決）
- 學習效率金字塔（Learning Pyramid），標記各種學習方式的知識留存率
- 搜尋策略流程圖：官方文檔 → Stack Overflow → AI 助手，每個節點說明適合什麼情況使用

**轉場**：「方法論在手，最後一張投影片 — 也是最重要的一張。」

---

### S08：你的票，通向未來

**核心訊息**：你不是在學一個工具，你在取得一張進入資料與 AI 世界的門票。

**講師要點**：
- 回到開場引言：「Data is the raw material; Python is the operating language.」
- 點題：2026 年，能夠用 Python 操作資料、探索規律、建立模型的人，擁有在資料驅動的職場中創造真實價值的能力
- 這不是誇大其詞 — 這是當前就業市場和產品開發現實的直接反映
- 課程承諾：24 小時之後，你將擁有獨立完成端到端資料分析的能力地基，以及知道在哪裡繼續深挖的地圖
- 對想走得更深的學員：「資料分析是你的起點，不是終點。系統設計、工程化部署、架構思維是下一條路，我們也有對應的課程。」
- 結語留一個問題給學員思考：「你想用 Python 解決的第一個真實資料問題是什麼？」

**視覺建議**：
- 全螢幕極簡設計：深色背景，中央一行大字「你不是在學工具，你在取得通往未來的入場券。」
- 底部小字：課程 GitHub repo 連結 + 社群討論頻道 + M1 預習資源

---

## 工作坊 / 練習段落

**時長**：60 分鐘

**工作坊標題**：環境建置 + 生態系初探 + 個人學習契約

---

### W01：建立你的學習環境（15 分鐘）

**目標**：確保所有學員的開發環境統一可用，消除後續模組的環境障礙

```bash
# 步驟一：確認 Python 版本
python --version  # 應為 3.11 或更高

# 步驟二：建立課程虛擬環境
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# 或 .venv\Scripts\activate  # Windows

# 步驟三：安裝課程核心套件
pip install jupyter pandas numpy matplotlib seaborn scikit-learn plotly

# 步驟四：確認安裝成功
python -c "import pandas as pd; print(f'pandas {pd.__version__}')"
python -c "import numpy as np; print(f'numpy {np.__version__}')"
python -c "import sklearn; print(f'scikit-learn {sklearn.__version__}')"

# 步驟五：啟動 Jupyter
jupyter lab
```

**驗收標準**：能成功印出三個套件版本號，JupyterLab 在瀏覽器中正常開啟

**常見問題處理**：
- Windows 路徑問題：建議使用 WSL2 或 Anaconda Prompt
- pip 版本過舊：`python -m pip install --upgrade pip`
- Port 已佔用：`jupyter lab --port 8889`

---

### W02：生態系地圖的第一次探索（20 分鐘）

**目標**：用程式碼驗證你理解工具的位置，建立對生態系的第一手感受

在 JupyterLab 中建立一個新 notebook，命名為 `M0_ecosystem_map.ipynb`。

**任務一：匯入並確認版本（5 分鐘）**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

print("=== 你的課程環境 ===")
print(f"pandas     : {pd.__version__}")
print(f"numpy      : {np.__version__}")
print(f"matplotlib : {plt.matplotlib.__version__}")
print(f"seaborn    : {sns.__version__}")
print(f"scikit-learn: {sklearn.__version__}")
```

**任務二：生態系定位練習（10 分鐘）**

建立一個 Python `dict`，key 是工具名稱，value 是「用一句話說明這個工具做什麼、在哪一層」。
**不要複製範例，用你自己的理解寫。**

```python
# 用你自己的話填寫，這是理解測試，不是填空題
ecosystem = {
    "numpy": "...",       # 數值計算層
    "pandas": "...",      # 資料操作層
    "matplotlib": "...",  # 視覺化層
    "seaborn": "...",     # 視覺化層
    "scikit-learn": "...",# 模型層
}

print("=== 我眼中的生態系地圖 ===")
for tool, description in ecosystem.items():
    print(f"{tool:15s}: {description}")
```

**任務三：第一張真實圖表（5 分鐘）**

用幾行程式碼畫出你的第一張圖，感受「資料 → 視覺」的過程：

```python
import numpy as np
import matplotlib.pyplot as plt

# 模擬一組成績資料
np.random.seed(42)
scores = np.random.normal(loc=72, scale=15, size=100)

plt.figure(figsize=(8, 4))
plt.hist(scores, bins=20, color='steelblue', edgecolor='white', alpha=0.8)
plt.axvline(scores.mean(), color='red', linestyle='--', label=f'平均：{scores.mean():.1f}')
plt.title('班級成績分佈')
plt.xlabel('分數')
plt.ylabel('人數')
plt.legend()
plt.tight_layout()
plt.show()

print(f"最高分：{scores.max():.1f}")
print(f"最低分：{scores.min():.1f}")
print(f"標準差：{scores.std():.1f}")
```

**討論問題（全班）**：
- 你在圖表中觀察到了什麼？這個分佈「正常」嗎？
- 如果你是老師，你會根據這張圖做什麼決定？

---

### W03：你的第一次資料探索（15 分鐘）

**目標**：用真實資料集體驗完整的「讀取 → 觀察 → 提問」流程

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 使用 seaborn 內建的 tips 資料集（餐廳小費資料）
tips = sns.load_dataset("tips")

# 第一步：認識資料
print("=== 資料基本資訊 ===")
print(f"資料筆數：{len(tips)}")
print(f"欄位清單：{list(tips.columns)}")
print()
print(tips.head())
print()
print(tips.describe())
```

**引導提問（讓學員先思考，再執行）**：

1. 「你認為小費金額和帳單總額之間有關係嗎？」
   ```python
   # 畫出散點圖，自己判斷
   plt.figure(figsize=(7, 5))
   sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", alpha=0.7)
   plt.title("帳單金額 vs. 小費金額")
   plt.show()
   ```

2. 「午餐和晚餐的小費習慣有差異嗎？」
   ```python
   # 用 boxplot 比較分佈
   plt.figure(figsize=(6, 4))
   sns.boxplot(data=tips, x="time", y="tip", palette="pastel")
   plt.title("午餐 vs. 晚餐的小費分佈")
   plt.show()
   ```

**反思問題**：你從這兩張圖中發現了什麼？你還想再問資料哪些問題？

---

### W04：學習契約 — 你的起點紀錄（10 分鐘）

**目標**：把這一刻的狀態記錄下來。24 小時後，這份記錄會讓你看見自己走了多遠。

在 `M0_ecosystem_map.ipynb` 的最後幾個 cell 中，寫下：

```python
# === 我的學習契約 ===

learning_contract = {
    "today_date": "2026-xx-xx",  # 填入今天日期
    
    "real_problem": """
    # 填入你想用 Python 解決的第一個真實問題（一句話描述）
    # 例如：分析公司每月業績數據，找出哪個產品線成長最快
    """,
    
    "most_anticipated_module": """
    # 你最期待哪個模組？為什麼？
    """,
    
    "biggest_learning_concern": """
    # 你最擔心的學習障礙是什麼？
    """,
    
    "current_python_level": """
    # 誠實評估：1-5 分，你的 Python 目前在哪個程度？
    # 1 = 完全沒碰過  2 = 看過但沒寫過  3 = 寫過簡單腳本
    # 4 = 能獨立完成任務  5 = 有生產環境經驗
    """,
}

print("=== 學習契約已記錄 ===")
for key, value in learning_contract.items():
    print(f"\n[{key}]")
    print(value.strip())
```

**重要**：儲存這個 notebook。在 M7 的最後一個工作坊，我們會回來看這份契約，對照 24 小時前後的自己。

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
| scikit-learn 1.4 What's New | S04 | Pipeline 改進、metadata routing |
| JupyterLab 4.x Release Notes | S04 | 效能改善、協作功能 |
| PEP 703 — Making GIL Optional | S04 | Free-threaded Python 的意義 |
| Python 3.13 Release Notes | S04 | JIT 實驗旗標、PEP 703 實驗性支援 |

---

## 講師備注

### 常見學員問題預備

**Q：我需要先學 R 還是 Python？**
A：2026 年的資料科學職缺，80% 以上要求 Python。R 在學術統計領域仍有地位，但如果你的目標是資料分析職位或 AI 相關工作，Python 優先沒有疑問。

**Q：Python 這麼慢，為什麼不用 Rust 或 Go？**
A：Python 本身慢，但 NumPy、pandas、PyTorch 的核心都是 C/C++/CUDA 寫的。你用 Python 呼叫它們，速度不輸原生語言。Python 是「膠水語言」，黏合高效能元件。

**Q：我沒有數學背景，能學 ML 嗎？**
A：本課程 M0–M6 完全不需要線性代數或微積分。M7 的機器學習入門部分會用直覺先建立理解，數學推導是可選深入路徑，不是必要條件。

**Q：這門課學完之後，下一步是什麼？**
A：有兩條路。一是繼續深化資料科學（統計學習、深度學習、大資料工程），二是轉向軟體工程與系統設計（我們的「系統設計與架構思維」課程）。這門課的終點是資料與 AI 入門，但它是一個清晰的起點。

### 時間控制提示

- S01–S02 最容易超時，學員有很多問題。預留 5 分鐘 buffer。
- S03（生態系地圖）建議做延伸討論，讓學員說出自己的工具認知，這有助於後續模組的情境連結。
- S05（AI 產品解剖圖）是全場情緒最高點，不要急著跳過討論。
- W01（環境建置）常遇到 Windows 路徑問題，建議助教提前準備 troubleshooting checklist。
- W03（tips 資料探索）是本工作坊最有互動潛力的段落，可以根據時間彈性延伸討論。

---

## 參考文獻與引用來源

### 產業調查與報告
1. **JetBrains/PSF Python Developers Survey 2024** — Python 使用場景、社群規模與技術趨勢的年度調查。[lp.jetbrains.com/python-developers-survey-2024](https://lp.jetbrains.com/python-developers-survey-2024/)
2. **Stack Overflow Developer Survey 2025** — 全球最大開發者調查，涵蓋語言流行度、AI 工具採用率。[survey.stackoverflow.co/2025](https://survey.stackoverflow.co/2025/)
3. **Anaconda State of Data Science Report 2024** — 企業 AI 採用率、資料工作者工具偏好與挑戰。[anaconda.com/resources/report/state-of-data-science-report-2024](https://www.anaconda.com/resources/report/state-of-data-science-report-2024)

### 分析框架
4. **Gartner Analytic Ascendancy Model** — 分析成熟度四階梯（描述性 / 診斷性 / 預測性 / 規範性）。Gartner, Inc. 原始框架，廣泛引用於企業數據策略文獻。參見 [digital.ai/catalyst-blog/gartners-analytics-maturity-model](https://digital.ai/catalyst-blog/it-decision-making-through-the-lens-of-gartners-analytics-maturity-model/)

### 效能對比數據
5. **Excel vs Python 效能對比** — 本課程引用的「100 萬筆資料篩選：Excel 3-5 分鐘 vs pandas 約 3 秒」為教學用估算值，基於典型桌機環境（16GB RAM, SSD）的實測經驗。精確數值依硬體與資料結構而異。

### 工具版本里程碑
6. **pandas 2.0 Release Notes (April 2023)** — Arrow backend、Copy-on-Write 語意。[pandas.pydata.org/docs/whatsnew/v2.0.0.html](https://pandas.pydata.org/docs/whatsnew/v2.0.0.html)
7. **NumPy 2.0 Release Notes (June 2024)** — 自 2006 年 NumPy 1.0 以來首個 major release，約 100 個已棄用 API 被移除。[numpy.org/doc/stable/release/2.0.0-notes.html](https://numpy.org/doc/stable/release/2.0.0-notes.html)
8. **scikit-learn 1.0 Release (September 2021)** — 始於 2007 年 Google Summer of Code，1.0 標誌 API 穩定化里程碑。[scikit-learn.org/stable/whats_new/v1.0.html](https://scikit-learn.org/stable/whats_new/v1.0.html)
9. **PyTorch 2.0 Release (March 2023)** — `torch.compile()` 在 A100 GPU 上平均加速 43%。[pytorch.org/get-started/pytorch-2-x](https://pytorch.org/get-started/pytorch-2-x/)
10. **Python 3.13 What's New (October 2024)** — 實驗性 free-threaded 模式（PEP 703）。[docs.python.org/3/whatsnew/3.13.html](https://docs.python.org/3/whatsnew/3.13.html)

### 工作坊節奏建議

| 工作坊段落 | 建議時長 | 節奏提示 |
|-----------|---------|---------|
| W01 環境建置 | 15 min | 以助教協助為主，講師巡場 |
| W02 生態系探索 | 20 min | 任務一、二獨立完成；任務三可帶著做 |
| W03 資料探索 | 15 min | 先讓學員自行觀察，再引導討論 |
| W04 學習契約 | 10 min | 靜默寫作，不討論，個人儀式感 |

---

## 模組總結

本模組完成了四件事：

1. **建立視野**：你知道 Python 在資料與 AI 世界的地位不是偶然，有數據支撐
2. **建立地圖**：你知道生態系的工具分層和它們的職責，以及這門課覆蓋哪些範圍
3. **建立環境**：你的開發環境已就緒，第一個 notebook 已經能跑起來
4. **建立期望**：你知道這 24 小時要帶你去哪裡、用什麼方法帶你去，以及之後的路在哪裡

下一模組（**M1：資料思維與 Notebook 工作流**）從「如何用資料回答問題」開始 — 不是「從頭教語法」，而是「建立用資料思考的習慣，並學會把 Jupyter 當成你的思考介面」。

---

*本模組屬於「Python 資料分析與 AI 入門」課程體系。*
*課程版本：v2.0 | 最後更新：2026 年*
