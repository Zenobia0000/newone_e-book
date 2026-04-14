# M1 BCG 顧問式簡報敘事 — Python 基礎與資料思維

> **本文件定位：** 以 BCG / McKinsey 頂級顧問的敘事規範，重構 M1 課程成為高階決策者可一頁秒懂的簡報。
> **讀者：** 事業部主管、技術決策者、訓練發展主管、課程採購 sponsor。
> **使用情境：** 向非技術的 sponsor 推銷「為什麼公司要讓員工上這門 3 小時的 Python 基礎課」；也是講師在試講現場用來快速對齊高階主管期待的腳本。

---

## Executive Summary（一頁結論）

> **若我們希望組織具備資料驅動決策能力，第一步不是買 BI 工具，而是讓關鍵人員具備「把分析流程寫成可重現腳本」的基本能力。M1 用 3 小時建立兩個底盤——資料思維與 Python 表達力——並讓學員帶著三個可重用函式離開教室。投資報酬不在於「會寫 Python」，而在於「每一次資料分析不再是一次性的手工勞動」。**

**三個量化錨點：**

- 資料分析師工作時間的 **60-80% 花在資料清理**。教會清理，就釋放半個 FTE。
- Excel 驅動的分析無法版本控制，**重做同一份月報平均要 2-4 小時**；Python 腳本化後 **< 5 分鐘**。
- M1 交付的不是語法，是 **可轉譯到任何程式語言的資料思維 mental model**，折舊慢、遷移性高。

---

## SCQA 結構

### S — Situation（現狀）

公司同仁處理資料的主力工具仍是 Excel。月報、KPI 拆解、客戶分群，靠手動滑鼠操作完成。一份分析報告平均 80% 時間花在資料整理，但這些整理動作沒有任何一筆被記錄下來。

### C — Complication（衝突）

- **重做成本高**：同樣邏輯下週換一批資料又要重來一次。
- **不可審計**：主管無法驗證 analyst 到底做了哪幾步清理。
- **人員流動即知識蒸發**：操作習慣鎖在個人的 Excel 技巧裡。
- **資料規模逼近 Excel 上限**：百萬列、多表關聯、半結構化 JSON，Excel 撐不住。

### Q — Question（問題）

**我們要花多少時間、給員工什麼最小工具組，才能讓「下次分析」變成「改一個檔名就好」？**

### A — Answer（主張）

**3 小時的 M1 模組**，由兩個支柱構成：

1. **資料思維底盤**（看得懂結構、識別污染、理解工具差異）
2. **Python 基本表達力**（型態、容器、流程、函式、套件）

完成後學員將以 Jupyter Notebook 為工作介面，產出可重用的三個分析函式。投資報酬在第二次重複分析時即回本。

---

## Governing Thought（總綱金句）

> **Syntax is the interface; semantics is the contract; reproducibility is the asset.**
>
> 語法是介面，語義是契約，可重現性才是資產。Python 的價值不在寫得快，在寫一次、跑一輩子。

---

## Pyramid Principle — MECE 三支柱

### 支柱 1：語法（Syntax）——用最小詞彙表達資料

- 六個型態與容器：`int / float / str / list / dict / tuple`
- 三種流程：`if / for / comprehension`
- 一個抽象單位：`function`

### 支柱 2：資料結構（Data Structures）——把世界看成列與欄

- 結構化資料的五元素：列、欄、綱要、型態、鍵
- 污染的四種形式：缺失、重複、離群、型態錯誤
- 乾淨 = 符合 schema 契約

### 支柱 3：工作流（Workflow）——把分析變成資產

- Excel 思維 vs Python 思維：手動 vs 可重現
- Jupyter Notebook：文字 + 程式 + 結果 + 圖表四合一
- 函式化：把一次性操作變成可呼叫流程
- 生態系：import 打開的 pandas / numpy / matplotlib 大門

> **三支柱的 MECE 切割邏輯：** 語法回答「怎麼表達」；資料結構回答「要表達什麼」；工作流回答「表達完之後怎麼保存和重用」。三者無重疊，合起來就是「用 Python 做資料分析」的完整定義。

---

## 逐頁敘事腳本（14 頁）

### P01 — 封面

**標題：** Python 基礎與資料思維——讓每一次分析都不再是一次性勞動
**副標：** M1 | 3 小時 | Python & Data AI Foundations
**視覺：** 左側大字「Excel → Python」箭頭；右側三個支柱圖示

### P02 — Executive Summary

**一頁五 bullet：** 重述最上方 Executive Summary 的三個錨點 + 三支柱 + 一句 governing thought。

### P03 — SCQA 展開

**版面：** 2x2 matrix，左上 S、右上 C、左下 Q、右下 A。每格 2 行字。
**敘事重點：** 停在 Q 那格 3 秒，給聽眾咀嚼時間。

### P04 — 我們要解決的真實問題（反駁「資料分析 = 畫圖表」）

**金句頁：** 「資料分析師 80% 的時間花在你看不到的地方。」
**視覺：** 冰山圖。水面上是「圖表、dashboard」（20%），水面下是「清理、探索、推論」（80%）。

### P05 — 結構化資料的五元素

**視覺：** 一張標記過的訂單表格，五色箭頭分別標出列、欄、schema、type、key。
**敘事：** 「看懂這五個元素是所有分析的起點，看不懂就算會寫程式也做不對。」

### P06 — 污染的四種面孔

**視覺：** 四格矩陣，每格一種污染類型（缺失 / 重複 / 離群 / 型態）配對應的資料截圖。
**敘事：** 「清理不是追求好看，是追求可信。四種污染，四種處理哲學。」

### P07 — Excel 思維 vs Python 思維（決策轉折頁）

**視覺：** 左右對照時間軸。左側 Excel 流程 6 步（每步都是人工操作），右側 Python 流程 3 步（`clean.py → analyze.py → report`）。
**敘事重點：** 「不是 Excel 不好，是 Excel 的操作不會留下腳印。」

### P08 — 為什麼 Jupyter Notebook 是共通語言

**視覺：** 真實 Notebook 截圖，標記四個 cell 類型（markdown / code / numeric output / chart）。
**金句：** 「一個好的 Notebook 是一篇可執行的論文，不是一堆跑過的 cell。」

### P09 — Python 的最小詞彙表（支柱 1）

**視覺：** 三欄表。型態名 / 資料世界的例子 / Python 寫法。
**敘事：** 「我們不教完整 Python，只教分析會用到的子集。」

### P10 — 資料篩選的三種句型（支柱 1 延伸）

**視覺：** 左右程式碼對比。左 for loop，右 list comprehension，中間箭頭寫 "equivalent, more Pythonic"。

### P11 — 函式：把一次性動作變成資產（轉折頁）

**金句：** 「寫一次，跑一輩子。」
**視覺：** 函式三要素圖（input → logic → output），下方一行：「函式名稱 = 這個流程的名字。」

### P12 — import：Python 的生態槓桿

**視覺：** 圓心輻射圖。中心 Python 核心 → 第一圈分析（pandas/numpy）→ 第二圈 ML/DL → 第三圈系統/工程。
**敘事：** 「Python 的強大 = 語言 + 生態。語法是起點，生態才是終局。」

### P13 — Workshop：從手動到函式化（示範 ROI）

**視覺：** 前後對比。左：學員在 Excel 做的 5 個手動步驟（截圖）；右：學員在 Notebook 定義的 3 個函式（程式）。
**敘事：** 「下週換一批資料，左邊要重做 2 小時，右邊改一行檔名 5 分鐘跑完。」

### P14 — 通往 M2 與可見的 ROI

**視覺：** 課程地圖。M0 / M1 打勾（綠），M2 高亮（橘色邊框），M3-M7 淡灰。M1→M2 箭頭上寫「函式 → class，表達 → 結構」。
**Closing ask：** 「若您同意『重做成本』是組織的隱性稅，M1 就是第一筆退稅。接著的 M2 會把退稅規模再放大一倍。」

---

## 金句頁（Money Slides）

以下 4 張建議做成單行大字 + 視覺極簡，貼在 deck 的策略位置：

### 金句 1（開場後 3 分鐘）

> **「Syntax is the interface; semantics is the contract.」**
> 語法是介面，語義是契約。

### 金句 2（講到 Excel vs Python 時）

> **「Excel 讓你做一次；Python 讓你做一輩子。」**
> 也可以寫成：**「Clicks don't compound; code does.」**

### 金句 3（講到 Notebook 時）

> **「A good notebook is not a record of what you ran—it's a document of what you thought.」**
> 好的 Notebook 記錄的不是你跑了什麼，而是你怎麼想。

### 金句 4（講到函式時）

> **「Write once, run forever. Name it, and it becomes a process.」**
> 寫一次、跑一輩子。給它一個名字，它就成為一個流程。

### 金句 5（Closing 前）

> **「Reproducibility is not a virtue. It is an asset.」**
> 可重現性不是美德，是資產。

---

## Closing Ask（決策頁）

**我們向 sponsor 請求三件事：**

1. **時間預算：3 小時。** 不是 3 天、不是 3 週。M1 的 ROI 曲線在第二次重複分析時就會翻正。
2. **硬體預算：零。** 學員只需自備筆電，Anaconda 免費。雲端版（Colab）連安裝都省。
3. **組織承諾：Notebook 進 Git。** 訓練後的 `.ipynb` 要求學員放進公司的 repo，被 code review。**沒有這一步，訓練失效率 > 50%。**

> **若能同意第 3 項，M1 就從訓練課程升級為組織能力資產的轉換器。**

---

## 顧問式小技巧（給講師的敘事心法）

1. **Pyramid top-down**：每一頁先給結論、再給理由。不要說「我們先看資料，然後發現...」，要說「結論是 X，理由有三：A / B / C」。
2. **Rule of Three**：每張 slide 最多三個要點。M1 的三支柱、三個核心動作、三種 import 寫法，都遵守這條。
3. **Signposting**：講到支柱 2 前，先說「剛才講完語法，現在進支柱 2：資料結構」。高階主管離開注意力 30 秒後還能跟得上。
4. **Concrete before abstract**：先給一個訂單表格，再講 schema 抽象定義。不要反過來。
5. **Numbers over adjectives**：不要說「很慢」，要說「2-4 小時」。不要說「很多時間」，要說「80%」。
6. **One slide one message**：若一頁要講兩件事，切成兩頁。

