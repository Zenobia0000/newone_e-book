# M5 BCG 敘事版簡報腳本：Reproducibility is the minimum viable professionalism.

> **文件定位：** 本文件以 BCG（顧問公司）簡報敘事風格重寫 M5 的核心訊息，面向「技術討論會議」場景——與會者不只是學生，還有技術主管、跨部門 stakeholder。風格特徵：governing thought 鎖 3 秒、MECE 拆三支柱、每張投影片一個 punchline、金句頁壓節奏、Closing ask 明確要行動。
>
> **篇幅：** 12–18 頁投影片腳本。每頁含版面位置、主標、副標、內容要點、講者口白建議。
>
> **使用場景：** 公司內部技術討論會、新人 onboarding 高階說明、跨部門對齊 Python 工程標準。內部 review 語氣。

---

## Governing Thought（封面前一頁必讀）

> **Reproducibility is the minimum viable professionalism.**
>
> 「可重現」是專業的最低門檻。做不到這件事，你寫的程式只是個人愛好，不是工程資產。

**副支點（MECE 三支柱）：**
1. **環境（Environment）：** 程式必須能在別人的機器上以可預期方式跑起來。
2. **錯誤處理（Error Handling）：** 程式必須能在意外發生時說清楚發生了什麼。
3. **並行前導（Concurrency Foundations）：** 程式必須知道自己的效能瓶頸在哪裡，才能合理擴張。

三者互斥且窮盡覆蓋「一個 Python 專案從個人腳本邁向團隊資產」的最小必要工程。

---

## Slide 1｜封面

**版面：** 全黑背景、白色大字置中、右下角小 Logo。
**主標：**
> **From Script to System**
> 讓你的 Python 專案活下去

**副標：**
> M5 — 進階 Python 工程門檻
> 3 小時 × 3 支柱 × 1 個專業起點

**口白：**
「今天 3 小時，我們要完成一件事——把各位手上的 Python 從『能跑』推到『能活下去』。」

---

## Slide 2｜Governing Thought

**版面：** 大字金句頁，中央一句話，無其他元素。

**主標：**
> **Reproducibility is the minimum viable professionalism.**

**副標：**
> 可重現，是專業的最低門檻。

**口白：**
「這句話今天會出現五次——開場、每個 Block 結尾一次、最後收尾一次。每次出現的意義都不同。這是我們今天的錨。」

---

## Slide 3｜問題陳述

**版面：** 左右分屏。左側「Script」、右側「System」。

**主標：**
> 你的程式只有兩種狀態：能跑一次，或能活下去。

**左側（Script）：**
- 200 行寫在一個檔案
- 路徑寫死、環境寫死
- print 滿天飛
- 「我電腦上可以」

**右側（System）：**
- 模組化結構、package 骨架
- venv + requirements/pyproject
- try/except + logging
- 「任何人、任何時候、任何機器都能跑」

**口白：**
「左邊的叫腳本，右邊的叫系統。兩者之間的距離，就是今天要走完的距離。這不是選修——左邊那位工程師三年後不會成長，因為他寫的每一行都無法累積。」

---

## Slide 4｜三支柱總覽（MECE）

**版面：** 三等分直欄，三個 icon 並列。

**主標：**
> 三支柱：環境、錯誤處理、並行前導

| 支柱 | 解決的問題 | 工具關鍵字 |
|---|---|---|
| **環境（Environment）** | 別人的機器跑不起來 | venv / pip / pyproject |
| **錯誤處理（Error Handling）** | 出錯時不知道發生了什麼 | try/except / raise from / logging |
| **並行前導（Concurrency）** | 該快的地方不快、不該快的地方亂並行 | process / thread / asyncio / GIL |

**口白：**
「這三件事彼此獨立（互斥），加起來完整覆蓋『Python 專案的工程基礎』（窮盡）。我們一個一個來。」

---

## Slide 5｜支柱一｜環境：問題根源

**版面：** 中央一張示意圖——兩台電腦中間一條「相依 DAG 差異」的裂縫。

**主標：**
> 「我電腦上可以跑」——這句話的成本是什麼？

**要點：**
- 程式的依賴是一張 DAG：套件、版本、間接相依。
- 兩台機器解析出不同的 DAG，就是 `ImportError` / `AttributeError` 的真正來源。
- 全域環境 = 全局 DAG，專案變多必衝突。

**口白：**
「依賴衝突不是你的錯、不是同事的錯，是全域環境這個結構性問題。不隔離，衝突只是時間問題。」

---

## Slide 6｜支柱一｜環境：解法工具箱

**版面：** 四欄並列，底部一條時間軸從左（學習）到右（產線）。

**主標：**
> venv / conda / poetry / uv — 選工具，不是選宗教

| 工具 | 一句話定位 |
|---|---|
| `venv` | 標準函式庫內建，學習起點 |
| `conda` | 跨語言、含 CUDA，AI 環境常用 |
| `poetry` | 有 lockfile、發布友善 |
| `uv` | Rust 寫的新一代快工具，現代首選 |

**要點：**
- 今天先學 `venv`——最小可演示模型，理解它，其他都看得懂。
- 重點不是記工具，是記三件事：**宣告相依、解析相依、鎖定相依**。

**口白：**
「工具會換，核心不變——宣告、解析、鎖定。這三件事只要你能在腦裡畫出來，你用什麼工具都會。」

---

## Slide 7｜金句頁（一）

**版面：** 全白背景、黑色大字置中。

**主標：**
> **「環境不是程式的背景，它就是程式的一部分。」**

**口白：**
「這句話請記住。你寫的程式不只是那些 `.py` 檔——你裝的套件版本、你用的 Python build，和程式碼一樣決定執行結果。」

---

## Slide 8｜支柱二｜錯誤處理：視角轉換

**版面：** 上下二區。上「錯誤 = 意外」（紅叉），下「錯誤 = 非線性控制流」（藍勾）。

**主標：**
> 錯誤不是意外，是函式的第二種正常結束方式。

**要點：**
- 函式只有兩種結束：正常 return、引發例外。兩者都是合法、都是設計的一部分。
- `try/except` 的目的不是「讓程式不出錯」，是「讓程式出錯時能說清楚」。
- 過度 catch（`except Exception: pass`）= 靜默失敗 = 最貴的 bug。

**口白：**
「覺得 try/except 是防禦性程式碼的人，思維層級還停在『意外』。真正的工程師視角：錯誤是一種控制流，設計它、命名它、傳遞它。」

---

## Slide 9｜支柱二｜錯誤處理：例外鏈與 logging

**版面：** 左側一個例外鏈圖（低層錯誤被高層包裹），右側一個 logging 分層圖（Logger → Handler → Formatter）。

**主標：**
> `raise ... from ...` + `logging` = 錯誤的可追溯性

**要點：**
- **例外鏈：** `raise HigherError("context") from low_error`——保留根因、表達上下文、不洩露底層。
- **logging 三層：** Logger 決定誰在記、Handler 決定記到哪、Formatter 決定記成什麼樣。library code 只建 logger，不設 handler。
- print 是草稿紙，logging 是工程日誌。

**口白：**
「線上服務出問題，三個月後的你只剩 log 可以靠。今天寫 print 的每一行，三個月後都是你的自作自受。」

---

## Slide 10｜金句頁（二）

**版面：** 全黑背景、白色大字置中。

**主標：**
> **「Silent failure is the most expensive kind of failure.」**
> **靜默失敗是最貴的失敗。**

**口白：**
「`except: pass` 寫起來最快，debug 起來最慢。後者的成本比前者高 100 倍，還不算名譽成本。」

---

## Slide 11｜支柱三｜並行前導：瓶頸決定工具

**版面：** 決策樹，根節點「你的瓶頸在哪？」，兩分支「I/O bound」「CPU bound」，各自再延伸到工具。

**主標：**
> 選錯並行工具，比不並行更慢。

**要點：**
- **I/O bound**（等網路、等硬碟、等資料庫）→ `asyncio` 或 `threading`
- **CPU bound**（算矩陣、算特徵、算影像）→ `multiprocessing` 或 NumPy/PyTorch 的底層並行
- GIL 真相：CPython 同一時刻只有一個 thread 能跑 Python bytecode。I/O 會 release GIL，所以 thread 對 I/O 有效；CPU 任務被鎖住，必須走 process。

**口白：**
「Amdahl's law 告訴我們，並行有收益上限。選錯模型，上限直接歸零——錢花了、複雜度上來了，一毛錢速度都沒多。」

---

## Slide 12｜支柱三｜並行前導：未來訊號

**版面：** 一條時間軸，左 Python 3.12，中 3.13 free-threaded experimental，右 3.14/3.15 可能穩定。

**主標：**
> GIL 不是永恆真相——PEP 703 free-threaded Python 正在改寫規則。

**要點：**
- Python 3.13 已有 free-threaded experimental build（`python3.13t`）。
- C extension 需要明確標記支援，AI 生態（PyTorch、NumPy）正在適配，預估 1–3 年逐步完成。
- 學生現在學的 GIL，是「當前的真相」，未來會變成「某些版本的真相」。

**口白：**
「並行是 Python 十年內變化最大的地方。今天打的直覺是 2024 的直覺，但你該對未來有心理準備——GIL 不會永遠在那裡。」

---

## Slide 13｜金句頁（三）

**版面：** 全白背景、黑色大字置中。

**主標：**
> **「Your bottleneck decides your tool. Not the other way around.」**
> **你的瓶頸決定你的工具，不是反過來。**

**口白：**
「不要因為 asyncio 聽起來很潮就到處用、不要因為 multiprocessing 看起來很威就到處開。先量，再選，再寫。」

---

## Slide 14｜三支柱合流圖

**版面：** 中央一個「可維護的 Python 專案」方塊，三條線向外連到三支柱；三支柱下方各標註對應工具關鍵字。

**主標：**
> 三支柱支撐同一個目標：專案活下去。

**要點：**
- 環境 → 讓專案能在不同地方復現
- 錯誤處理 → 讓專案遇到意外不崩潰、崩潰了能診斷
- 並行前導 → 讓專案遇到效能瓶頸時有工具可用

**口白：**
「三支柱不是三個獨立技能，是三種角度看同一個目標——可重現、可診斷、可擴張。缺一個，專案就少一條腿。」

---

## Slide 15｜Closing Ask（行動）

**版面：** 白底、左側條列三個 ask、右側一個「下週 check-in」日期。

**主標：**
> 離開會議前，請各位承諾三件事。

**Ask 列表：**
1. **Ask 1（本週內）：** 把手上最常跑的那支分析腳本，建一個 `.venv`，輸出 `requirements.txt`，加進 git。
2. **Ask 2（本月內）：** 把專案裡所有 `print` 改成 `logging.getLogger(__name__)`；把所有 I/O 操作包上 try/except。
3. **Ask 3（本季內）：** 量一次自己最慢的那段程式——它是 I/O bound 還是 CPU bound？記錄結論，下次 review 帶來。

**口白：**
「知識不變成動作，就不會變成資產。這三個 ask 是我們共同的契約——下週的 check-in 我會問。」

---

## Slide 16｜收尾

**版面：** 回到 Governing Thought 金句頁，第二次出現。

**主標：**
> **Reproducibility is the minimum viable professionalism.**

**副標：**
> 今天結束後，「我電腦上可以」這句話不該再從你口中說出。

**口白：**
「我們從這句話開始，也從這句話結束。『我電腦上可以』——從今天起，這句話在我們團隊是警訊，不是辯解。謝謝各位。」

---

## 附錄｜講者備忘

- **節奏控制：** 16 頁投影片、3 小時課。平均每頁 11 分鐘——金句頁只停 30 秒，解釋頁要 15–20 分鐘。
- **互動點：** Slide 3（問「你的程式屬左還屬右？」）、Slide 11（實際讓學生舉手自評瓶頸）、Slide 15（要求學生當場填 ask 承諾）。
- **Reviewer 提醒：** 技術討論會場景下，與會者會有主管，不要過度技術細節——BCG 敘事的重點是**讓非技術人也能跟上 governing thought**，把 try/except 的語法細節留給練習時間。
- **退路：** 如時間壓縮，優先砍 Slide 12（PEP 703 前瞻）和 Slide 13（第三張金句頁），不要砍 Slide 7/10/16（錨句反覆）。
