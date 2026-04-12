# M5：進階 Python — 從分析腳本到可維護專案

**模組定位：** 第五幕開場，系統底層線核心模組  
**時數：** 3 小時  
**前置模組：** M1（Python 基礎）、M2（OOP）、M3（NumPy/pandas）、M4（EDA）  
**後接模組：** M6（計算機組織與作業系統）

---

## 一、模組定位與核心主張

M4 結束後，學生已能寫出「可以跑起來的分析腳本」。但腳本和系統之間有一條分界線：

> **腳本：** 你自己看得懂，跑一次就算完成。  
> **系統：** 別人能跑、未來你自己也能接手、不同環境都能重現結果。

M5 就是在幫學生跨越這條分界線。五個主題環環相扣，組成「讓 Python 專案活下去」的最低基礎設施：

- **模組化**讓程式有骨架
- **環境管理**讓程式能在其他人電腦上跑
- **例外處理**讓程式遇到錯誤不直接死掉
- **檔案 I/O**讓程式能讀寫真實世界的資料
- **並行前導**讓學生聽到 `async def`、`num_workers=4` 不再一頭霧水

這五個能力，是從「會寫 Python」升級到「能做 Python 工程」的必要橋樑。

---

## 二、學習目標

完成本模組後，學生能夠：

| # | 目標 | 對應主題 |
|---|------|----------|
| 1 | 把分析程式拆分成多個模組並組織成 package | Block 1 模組化 |
| 2 | 建立 virtual environment、管理相依套件、輸出 requirements | Block 2 環境管理 |
| 3 | 用 try/except 包住危險操作，用 logging 取代 print 除錯 | Block 3 例外處理 |
| 4 | 用 pathlib 讀寫文字檔、JSON、CSV，理解 buffer 概念 | Block 4 檔案 I/O |
| 5 | 能說清楚 process/thread 的差別、I/O bound vs CPU bound 的差別 | Block 5 並行前導 |
| 6 | 看到 `DataLoader(num_workers=4)`、`async def` 時知道在解決什麼問題 | Block 5 並行前導 |

---

## 三、投影片大綱

| # | 投影片標題 | 對應 Block | 核心訊息 |
|---|-----------|-----------|---------|
| 1 | M5 開場：腳本與系統的分界線 | 導論 | 你的程式「能跑」和「能活下去」是兩件事 |
| 2 | Block 1：import 機制與模組化思維 | Block 1 | import 不是語法糖，是程式組織的骨架 |
| 3 | Block 1：package 結構與 `__init__.py` | Block 1 | folder + `__init__.py` = package，這是 Python 組織大型專案的方式 |
| 4 | Block 2：「同一份程式在別人電腦跑不起來」— 環境問題根源 | Block 2 | 套件版本差異是工程現實，不是你的錯 |
| 5 | Block 2：venv 建立與 pip 生命週期 | Block 2 | 一個專案一個環境，這是行業標準做法 |
| 6 | Block 3：例外處理 — 程式的防彈衣 | Block 3 | 生產環境的程式不能崩潰，要能說清楚為什麼出錯 |
| 7 | Block 3：logging vs print — 工程師的除錯觀 | Block 3 | print 是草稿，logging 是工程工具 |
| 8 | Block 4：pathlib 與檔案 I/O | Block 4 | 路徑不是字串，是物件；I/O 不是讀寫，是流 |
| 9 | Block 4：JSON 與 CSV — 資料交換的兩種語言 | Block 4 | 結構化資料有型態，序列化是有代價的 |
| 10 | Block 5：並行前導 — process、thread、async 三條線 | Block 5 | 三種並行機制解決三種不同問題，不能混用 |
| 11 | Block 5：I/O bound vs CPU bound — 選錯工具比不並行更慢 | Block 5 | 模型訓練和網頁爬取是兩種不同的瓶頸 |
| 12 | M5 總結：Python 工程底盤地圖 | 總結 | 五個 Block 組合成「能活下去的 Python 專案」 |

---

## 四、投影片詳細說明

---

### Slide 1：M5 開場 — 腳本與系統的分界線

**核心訊息：** 「能跑一次」和「能在任何地方、任何時候、被任何人跑起來」是兩件完全不同的事。

**講師講解要點：**
- 打開一個典型的初學者分析腳本：200 行、全部寫在一個 `.py` 或 Notebook，沒有函式分組、路徑寫死在程式裡、用 `print` 除錯、沒有套件版本記錄。問學生：這份程式六個月後還能跑嗎？
- 「腳本」的本質：一次性、個人化、對環境有隱性依賴。「系統」的本質：可重現、可協作、對環境有顯性宣告。
- M5 的五個主題不是獨立的技巧清單，而是讓程式「活下去」的最低基礎設施：骨架（模組化）、隔離（環境）、防護（例外）、輸入輸出（I/O）、效能預備（並行）。
- 強調：這五個主題是 Python 官方文件中正式列為語言核心的部分，不是進階選修，而是專業門檻。

**視覺建議：** 左右對比圖。左欄「腳本的樣子」：一個 Notebook 截圖，print 滿天飛、路徑寫死、沒有結構。右欄「系統的樣子」：一個清晰的資料夾結構樹，含 `src/`、`tests/`、`requirements.txt`、`pyproject.toml`。

**過渡語：** 「我們從最基本的問題開始：一個程式如果有很多功能，你怎麼組織它？」

---

### Slide 2：Block 1 — import 機制與模組化思維

**核心訊息：** `import` 不只是引用別人的程式碼，它是你組織自己程式碼的主要機制。

**講師講解要點：**
- 從學生已知的 `import pandas as pd` 出發：這行程式在做什麼？Python 怎麼找到 `pandas`？搜尋路徑（`sys.path`）是什麼概念。
- 模組（module）= 一個 `.py` 檔。任何 `.py` 檔都可以被 `import`。這代表你自己寫的分析函式，也可以被組織成模組被其他程式引用。
- 三種 import 型態的語意差別：`import module`（保留命名空間）、`from module import func`（直接引入名稱，小心命名衝突）、`from module import *`（幾乎不應該用，原因是命名污染）。
- 為什麼模組化重要：當分析腳本成長到 500 行，你需要把「資料清理邏輯」、「特徵工程邏輯」、「視覺化邏輯」分開，這樣才能獨立測試、獨立修改、獨立重用。
- 連結 M2 OOP：class 管理「物件的狀態」，module 管理「功能的邊界」，兩者是不同層次的組織工具。

**視覺建議：** 動畫步驟圖，顯示 Python 執行 `import` 時的搜尋順序：1. 內建模組 → 2. 當前目錄 → 3. `sys.path` 中的其他路徑。搭配一個簡單的程式碼示例，對比沒有模組化和有模組化的同一功能。

**過渡語：** 「一個模組是一個 .py 檔，那如果我有很多模組，我要怎麼組織它們？這就是 package 的用途。」

---

### Slide 3：Block 1 — package 結構與 `__init__.py`

**核心訊息：** 一個資料夾 + 一個 `__init__.py` = 一個 package。這是 Python 組織大型專案的標準方式。

**講師講解要點：**
- Package 的本質：一個包含 `__init__.py` 的資料夾，讓 Python 認識它是可以被 `import` 的命名空間。`__init__.py` 可以是空檔案，也可以控制「對外暴露哪些東西」。
- 展示一個典型的資料分析專案結構：
  ```
  my_project/
  ├── src/
  │   └── analysis/
  │       ├── __init__.py
  │       ├── clean.py        # 資料清理函式
  │       ├── features.py     # 特徵工程函式
  │       └── visualize.py    # 視覺化函式
  ├── notebooks/
  │   └── explore.ipynb
  ├── data/
  └── requirements.txt
  ```
- `__init__.py` 的三個常見用法：空檔案（只標記 package）、re-export（讓使用者可以從 package 直接引入，不需知道內部結構）、初始化邏輯（設定 logging、版本號）。
- 相對 import 的概念：在 package 內部模組間互相引用時用 `from . import` 或 `from .clean import normalize`，不要硬寫絕對路徑。
- 連結 AI 工程現實：PyTorch、scikit-learn、pandas 本身都是 package，它們的 `__init__.py` 控制了你用 `import torch` 時能拿到什麼。

**視覺建議：** 資料夾樹狀圖搭配箭頭，顯示 `__init__.py` 如何決定對外介面。左側是內部結構（複雜），右側是使用者看到的（簡潔）。

**過渡語：** 「現在程式有骨架了。但如果你把這個專案傳給同學，他能跑起來嗎？這就是環境管理要解決的問題。」

---

### Slide 4：Block 2 — 「同一份程式在別人電腦跑不起來」的根源

**核心訊息：** 不是你的程式有問題，是環境不一致。套件版本差異是工程現實，不是意外。

**講師講解要點：**
- 從一個學生一定遇過的場景出發：程式在自己電腦能跑，傳給同學後第一行就報錯 `ImportError` 或 `AttributeError`，因為對方的 pandas 版本不同。
- 根本原因：Python 套件安裝在「全域環境」時，所有專案共用同一份套件。當 A 專案需要 pandas 1.5、B 專案需要 pandas 2.0，它們不能共存——除非隔離。
- 版本衝突的三個來源：直接相依（你裝了 X）、間接相依（X 裝了 Y）、系統 Python 污染（用系統 Python 裝套件影響全域）。
- 為什麼 Python 官方把 virtual environment 列為正式語言主題（`venv` 模組在標準函式庫）：因為這不是技巧，是工程衛生。
- 拉高視角：這個問題在 Docker / Container 技術出現後有了另一層解法，但 venv 仍是本機開發的標準第一步。

**視覺建議：** 示意圖：兩台電腦（你的 / 同學的），同一份程式碼，但套件版本格子不同，導致執行結果有差異。強調「環境」和「程式碼」是分開的兩個維度。

**過渡語：** 「知道了問題根源，解法很清楚：每個專案配一個隔離的環境。這就是 venv 的用途。」

---

### Slide 5：Block 2 — venv 建立與 pip 生命週期

**核心訊息：** 一個專案，一個 venv。建立、啟動、安裝、凍結——四個動作就是完整的環境管理生命週期。

**講師講解要點：**
- 完整的四步驟示範（邊講邊在 terminal 操作）：
  1. `python -m venv .venv`：在專案目錄建立隔離環境
  2. `source .venv/bin/activate`（macOS/Linux）/ `.venv\Scripts\activate`（Windows）：啟動環境，此後所有 pip 操作都在這個環境內
  3. `pip install pandas numpy`：安裝套件到隔離環境
  4. `pip freeze > requirements.txt`：把當前環境的精確版本輸出成清單
- `requirements.txt` 的用途：別人拿到你的專案後執行 `pip install -r requirements.txt`，就能還原一模一樣的環境。這是協作的基礎。
- 現代替代方案提示（不深入，只種概念）：`pyproject.toml` + `pip install -e .` 是更現代的做法，被 pip、poetry、uv 等工具採用。PEP 517/518/621 規範了這個方向。學生日後看到 pyproject.toml 時不會陌生。
- `.venv` 加入 `.gitignore`：環境本身不應該被 git 追蹤，要追蹤的是 `requirements.txt` 或 `pyproject.toml`。
- 實用提示：現代 IDE（VS Code、PyCharm）能自動偵測 `.venv` 並切換 interpreter，不需要手動 activate。

**視覺建議：** 圓圈生命週期圖：Create → Activate → Install → Freeze → Share。每個步驟配上對應指令。加一個小提示框：「.venv 放 .gitignore，requirements.txt 放 git」。

**過渡語：** 「環境隔離好了，程式可以跑了。但跑起來之後，如果資料有問題、網路斷掉、檔案不存在——程式怎麼辦？」

---

### Slide 6：Block 3 — 例外處理 — 程式的防彈衣

**核心訊息：** 程式在真實世界一定會遇到意外。try/except 不是讓程式不出錯，而是讓程式出錯時能說清楚發生了什麼。

**講師講解要點：**
- 從 stack trace 開始：展示一個典型的 Python 錯誤訊息，教學生從下往上讀：最後一行是錯誤類型和訊息，往上追是呼叫鏈。stack trace 是最重要的除錯工具，但初學者常常看到就關掉。
- Python 的例外繼承樹簡介：`BaseException` → `Exception` → 常見子類別（`FileNotFoundError`、`ValueError`、`TypeError`、`KeyError`、`IndexError`）。理解繼承關係，才知道 `except Exception` 會抓到什麼、不會抓到什麼。
- try/except/else/finally 四個區塊的語意：
  - `try`：放可能出錯的程式碼
  - `except`：出錯時怎麼處理（可以針對不同例外類型分別處理）
  - `else`：只有沒出錯時才執行
  - `finally`：無論如何都執行（用來釋放資源）
- 常見錯誤示範：過度使用 `except Exception: pass`（靜默吞掉所有錯誤，程式看起來正常但其實什麼都沒做）、或只寫 `except:` 連 `KeyboardInterrupt` 都抓進去。
- 自定義例外：繼承 `Exception` 建立語意清晰的錯誤類型，讓呼叫者能精確處理。這在 AI pipeline 中很常見（例如 `DataValidationError`、`ModelLoadError`）。

**視覺建議：** 一個 try/except/else/finally 的流程圖，搭配每個區塊的觸發條件。加上一個「常見反模式」對比框：`except: pass` 為什麼是壞習慣。

**過渡語：** 「知道怎麼接住錯誤之後，下一個問題是：程式出錯了，你怎麼知道？怎麼記錄下來讓未來的自己能診斷？」

---

### Slide 7：Block 3 — logging vs print — 工程師的除錯觀

**核心訊息：** `print` 是草稿紙，`logging` 是工程日誌。從腳本升級到系統，就從這個替換開始。

**講師講解要點：**
- 為什麼 print 不夠：print 輸出沒有時間戳、沒有嚴重程度標記、無法控制要不要顯示、無法導向到檔案、在 library code 裡會污染使用者的輸出。
- `logging` 模組的五個層級及其語意：`DEBUG`（開發時的詳細資訊）、`INFO`（正常流程記錄）、`WARNING`（出現了不預期但不致命的情況）、`ERROR`（某個操作失敗）、`CRITICAL`（程式無法繼續）。
- 基本設定示範：`logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')`。說明 format 字串的各個欄位。
- 在 AI/資料工程場景的重要性：資料 pipeline 執行時間可能很長（幾小時），你不可能一直盯著螢幕。logging 讓你事後能知道每個步驟是什麼時候完成、在哪個步驟出了什麼問題。
- logger 的命名慣例：使用 `logging.getLogger(__name__)` 讓 log 訊息帶有模組名稱，方便在大型專案中追蹤問題來源。

**視覺建議：** 左右對比：同一個資料讀取函式，左側用 print 除錯，右側用 logging。右側版本的輸出多了時間戳、層級、模組名，可以清楚知道什麼時候、哪個地方、發生什麼事。

**過渡語：** 「程式有骨架、有環境保護、有錯誤防護了。接下來要解決最基本的問題：程式怎麼跟外部世界交換資料？」

---

### Slide 8：Block 4 — pathlib 與檔案 I/O

**核心訊息：** 路徑不是字串，是物件。`pathlib` 讓跨平台路徑操作變成物件導向的事。

**講師講解要點：**
- 從痛點出發：字串路徑的問題——Windows 用反斜線、Linux/Mac 用正斜線，用字串拼接路徑（`"data/" + filename`）很容易出錯，也沒有自動補全。
- `pathlib.Path` 的核心操作：
  - `Path("data") / "raw" / "input.csv"`：用 `/` 運算子拼接路徑（跨平台自動處理分隔符）
  - `path.exists()`、`path.is_file()`、`path.is_dir()`：檢查路徑狀態
  - `path.stem`、`path.suffix`、`path.parent`：解析路徑各部分
  - `path.glob("*.csv")`：找出目錄下所有 CSV 檔案
  - `Path(__file__).parent`：取得當前腳本所在目錄（讓相對路徑不依賴執行位置）
- 文字檔讀寫：用 `path.read_text(encoding="utf-8")` 和 `path.write_text()`，或用 `open(path)` context manager。強調一定要指定 encoding，避免 Windows 的 cp950 vs UTF-8 問題。
- buffer 概念的直覺建立：檔案 I/O 不是直接讀寫硬碟，中間有 buffer（緩衝區）。`with open(...) as f` 結束時會 flush buffer 並關閉檔案。這是為什麼要用 context manager 而非手動 `f.close()`。

**視覺建議：** 路徑物件的解剖圖，把 `Path("/home/user/data/raw/input.csv")` 拆解成 `parent`、`stem`、`suffix` 等各部分。搭配一個 context manager 流程示意。

**過渡語：** 「純文字檔解決了，但資料分析最常遇到的是結構化資料：JSON 和 CSV。這兩種格式各有特性。」

---

### Slide 9：Block 4 — JSON 與 CSV — 資料交換的兩種語言

**核心訊息：** JSON 保留型態，適合巢狀結構；CSV 是純表格，快速但型態需要另外處理。序列化是有代價的。

**講師講解要點：**
- JSON 的使用場景：API 回應、設定檔、模型 metadata、結果輸出。`json.dumps()` 把 Python 物件序列化成字串、`json.loads()` 反序列化。`json.dump()`/`json.load()` 直接讀寫檔案。重要：JSON 不支援 Python 的所有型態（`datetime`、`numpy.int64`、自定義 class 需要自己處理序列化）。
- CSV 的使用場景：表格資料交換、pandas 讀入前的原始資料。`csv.reader` / `csv.DictReader` 的區別。強調為什麼在資料分析實務中，CSV 讀寫通常直接用 `pandas.read_csv()` 而非標準函式庫的 `csv` 模組。
- 序列化代價的直覺：資料在記憶體中是 Python 物件（有型態、有方法）；序列化成 JSON/CSV 後是「文字」（型態資訊部分丟失）；反序列化時需要重新建立型態。這就是為什麼 pandas 讀 CSV 時需要手動指定 `dtype`。
- 連結 AI 工程：模型訓練後的 metrics、超參數配置、資料集 metadata，都常以 JSON 格式儲存。能正確讀寫 JSON 是 AI pipeline 的基礎技能。

**視覺建議：** Python dict → JSON 字串 → 回到 Python dict 的雙向箭頭圖，標記序列化/反序列化步驟，並標注型態在過程中的變化（例如 `numpy.int64` → JSON 無法直接處理 → 需要轉換）。

**過渡語：** 「I/O 解決了。最後一個主題，是讓很多初學者困惑的：Python 怎麼同時做多件事？」

---

### Slide 10：Block 5 — 並行前導 — process、thread、async 三條線

**核心訊息：** Python 有三種「同時做多件事」的機制，解決三種不同的問題。選錯工具不是沒效果，是更慢。

**講師講解要點：**
- 先建立直覺：什麼叫「同時做多件事」？真正的同時（多核心 CPU 並行執行）vs. 感覺上的同時（等待 I/O 時切換去做別的事）。這兩個是根本不同的情況。
- 三條線的定位：
  - `multiprocessing`：多個獨立 process，真正利用多核心，適合 CPU bound 任務（數值計算、影像處理）。每個 process 有自己的記憶體空間，啟動成本高。
  - `threading`：多個 thread 共享同一個 process 的記憶體，但受 GIL（Global Interpreter Lock）限制，Python thread 不能真正並行執行 Python 程式碼（但可以並行等待 I/O）。
  - `asyncio`：單 thread 的協作式排程，靠 `await` 主動讓出控制權。適合大量 I/O 操作（HTTP 請求、資料庫查詢）但每個操作本身不耗 CPU 的場景。
- GIL 的直覺解釋（不深入）：Python 有一把全域鎖，同一時間只有一個 thread 能執行 Python bytecode。這是為了保護 reference counting 的記憶體管理。thread 並行執行 I/O 沒問題（I/O 操作釋放 GIL），但並行執行 CPU 密集運算會被 GIL 限制。
- Python 3.13 + PEP 703 的方向提示：free-threaded Python（無 GIL 模式）已在 3.13 進入實驗性支援。這代表 Python 的 threading 在未來可能真正實現 CPU 並行。這是 Python 歷史上的重要里程碑。

**視覺建議：** 三欄對比表：`multiprocessing` / `threading` / `asyncio`，每欄標注：適合什麼場景、記憶體隔離程度、受 GIL 影響與否、啟動成本。搭配一個簡單的「平行宇宙」示意圖：process 是完全獨立的宇宙，thread 是同一個宇宙的不同時間軸，asyncio 是同一個宇宙的事件排班。

**過渡語：** 「知道三條線各是什麼，下一步是知道什麼時候用哪條線。這取決於你的瓶頸在哪裡。」

---

### Slide 11：Block 5 — I/O bound vs CPU bound — 選對工具才有意義

**核心訊息：** 瓶頸在等待（I/O bound）還是在計算（CPU bound），決定你該用哪個並行工具。

**講師講解要點：**
- I/O bound 的特徵：程式大部分時間在等——等網路回應、等硬碟讀寫、等資料庫查詢。CPU 使用率低，但時鐘時間長。解法：`threading` 或 `asyncio`，讓等待時間重疊。
- CPU bound 的特徵：程式大部分時間在算——矩陣乘法、影像轉換、特徵工程。CPU 使用率高，無論怎麼等都不會變快，要真正並行才有意義。解法：`multiprocessing`，或直接用 NumPy/PyTorch（它們底層已經並行）。
- 具體場景對應（讓學生能直接對號入座）：
  - 網頁爬蟲 / API 呼叫 → I/O bound → asyncio 或 threading
  - 讀寫大量本地檔案 → I/O bound → threading 或 asyncio
  - 資料預處理（純 Python 迴圈）→ CPU bound → multiprocessing 或改用 NumPy
  - 模型訓練（PyTorch）→ CPU/GPU bound → 不是靠 Python 並行，而是靠 PyTorch 內部的 CUDA 和 C++ 並行
  - DataLoader 資料讀取 → I/O bound → `num_workers=4` 使用 multiprocessing 在訓練時預先讀取資料
- 種下種子：`DataLoader(dataset, num_workers=4)` 這行程式，`num_workers` 決定了開幾個獨立 process 來預先讀取資料，讓 GPU 訓練時不用等資料。理解了 process vs thread vs I/O bound vs CPU bound，這行程式就不是黑盒子了。
- `async def` 在哪裡會出現：現代 web framework（FastAPI）、LLM API 呼叫、async 資料庫 client。學生未來碰到 `await openai.chat.completions.create(...)` 時，知道這是在做什麼。

**視覺建議：** 決策樹圖：「你的瓶頸是什麼？」→ 「等待（I/O）」→ asyncio/threading；「計算（CPU）」→ multiprocessing/NumPy/PyTorch。加上真實程式碼片段：`DataLoader(num_workers=4)` 和 `async def fetch_data()` 各自的使用場景說明。

**過渡語：** 「五個 Block 都覆蓋了。讓我們回頭看整張地圖，確認每個部分的定位。」

---

### Slide 12：M5 總結 — Python 工程底盤地圖

**核心訊息：** 五個 Block 不是獨立的技術清單，而是讓一個 Python 專案「能活下去」的完整基礎設施。

**講師講解要點：**
- 總結五個 Block 的系統關係：模組化讓程式有骨架 → 環境管理讓骨架能在不同地方復現 → 例外處理讓骨架遇到問題不崩潰 → I/O 讓骨架能跟外部世界溝通 → 並行前導讓骨架能應對效能需求。
- 強調 M5 的定位：這不是「進階 Python 技巧」，而是「從學習者到工程師」的分界線。所有軟體工程的核心問題（可維護、可重現、可協作、可擴展），都在這五個面向有對應的工具。
- 連結到後續模組：M6 會深入 CPU/GPU/記憶體/process 的系統底層，讓 M5 的「並行前導」有更紮實的硬體直覺支撐。M7 的 ML pipeline 和 DataLoader 都會直接用到 M5 的知識。
- 給學生的行動清單：
  - 把現有的分析腳本，試著拆成至少兩個模組
  - 建立一個 venv，輸出 requirements.txt
  - 把最可能出錯的 I/O 操作包上 try/except + logging
- 引子：「下一個模組，我們打開 Python 程式背後的機械室——CPU 怎麼執行你的程式、記憶體怎麼管理你的 DataFrame、GPU 怎麼加速你的模型。」

**視覺建議：** 一張整合圖：中心是「可維護的 Python 專案」，五條線分別延伸到五個 Block，每條線旁標注核心工具名稱（import/package、venv/pip、try/except/logging、pathlib/json/csv、multiprocessing/threading/asyncio）。

---

## 五、工作坊練習

---

### 練習一：拆分分析腳本並建立專案結構

**目標：** 把一個「全部寫在一起」的分析腳本，拆分成有組織的 package 結構，並建立隔離的 virtual environment。

**預估時間：** 35 分鐘

**情境設定：**
學生拿到一份 150 行的資料分析腳本（助教提供，或使用 M3/M4 練習成果），裡面包含：資料讀取、資料清理、特徵計算、視覺化輸出，全部混在一起。

**步驟：**

1. **（5 分鐘）分析現有程式碼的功能邊界**
   - 在腳本上標記：哪幾行是讀取？哪幾行是清理？哪幾行是計算？哪幾行是輸出？
   - 識別哪些函式/邏輯可以被「重用」，哪些是一次性的流程。

2. **（10 分鐘）建立 package 結構**
   - 建立以下目錄結構：
     ```
     my_analysis/
     ├── src/
     │   └── pipeline/
     │       ├── __init__.py
     │       ├── load.py
     │       ├── clean.py
     │       └── visualize.py
     ├── notebooks/
     │   └── analysis.ipynb
     ├── data/
     └── requirements.txt
     ```
   - 把腳本中的函式分別移到對應模組。

3. **（10 分鐘）建立 virtual environment 並安裝套件**
   - `python -m venv .venv`
   - 啟動 venv
   - `pip install pandas matplotlib jupyter`
   - `pip freeze > requirements.txt`
   - 把 `.venv` 加入 `.gitignore`

4. **（10 分鐘）在 Notebook 中驗證**
   - 在 `notebooks/analysis.ipynb` 中，用 `from pipeline.load import read_data` 等方式引入函式
   - 確認邏輯能完整跑通

**驗收標準：**
- [ ] 至少三個模組，每個模組有明確的單一職責
- [ ] `__init__.py` 存在於 package 目錄
- [ ] `requirements.txt` 存在且包含正確版本
- [ ] `.gitignore` 包含 `.venv`
- [ ] Notebook 能正確 import 並執行

**常見卡關點：**
- import 找不到模組：檢查是否在正確的目錄執行、是否有 `__init__.py`
- Notebook 的 sys.path 不包含 `src/`：需要在 Notebook 開頭加 `sys.path.insert(0, "../src")`

---

### 練習二：錯誤處理、logging 與 JSON I/O

**目標：** 為一個資料讀取與處理流程加入完整的錯誤處理、logging 和 JSON 格式的結果輸出。

**預估時間：** 30 分鐘

**情境設定：**
學生拿到一個「樂觀版」的資料處理函式——假設所有事都會正常發生，沒有任何錯誤處理。任務是把它改造成「悲觀版」——預期所有可能出錯的地方，並用 logging 記錄執行過程。

**起始程式碼（助教提供）：**
```python
import pandas as pd
import json
from pathlib import Path

def process_sales_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df['total'] = df['quantity'] * df['price']
    summary = {
        'total_sales': float(df['total'].sum()),
        'avg_order': float(df['total'].mean()),
        'num_orders': len(df)
    }
    with open(output_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print("Done!")
```

**步驟：**

1. **（5 分鐘）識別所有可能的失敗點**
   - 檔案不存在
   - CSV 欄位名稱不對（`quantity`、`price` 不存在）
   - 欄位中有非數值資料導致計算失敗
   - 輸出路徑的目錄不存在

2. **（15 分鐘）加入 try/except 和 logging**
   - 在函式頂部設定 logger：`logger = logging.getLogger(__name__)`
   - 把每個失敗點包上對應的 except（`FileNotFoundError`、`KeyError`、`ValueError`）
   - 用 `logger.info()` 記錄正常流程（「開始讀取 X」、「處理完成，共 N 筆」）
   - 用 `logger.error()` 記錄例外情況，包含有意義的錯誤訊息

3. **（10 分鐘）驗證與測試**
   - 用不存在的路徑呼叫函式，確認 logging 輸出正確的 ERROR 訊息而非 crash
   - 用欄位名稱錯誤的 CSV 呼叫，確認能捕捉 `KeyError` 並輸出有意義的訊息
   - 用正確的輸入呼叫，確認 JSON 輸出格式正確，logging 顯示 INFO 訊息

**驗收標準：**
- [ ] 三種以上的例外情況各自有對應的 except 處理
- [ ] 使用 `logging` 模組，不再用 `print`
- [ ] logger 使用 `__name__` 命名
- [ ] 輸出的 JSON 可以用 `json.load()` 重新讀入並驗證型態正確
- [ ] 錯誤發生時程式能繼續執行（或優雅地結束），而非直接 crash

**進階挑戰（選做）：**
- 加入輸出目錄不存在時自動建立的邏輯（`output_path.parent.mkdir(parents=True, exist_ok=True)`）
- 建立自定義例外 `DataValidationError`，在欄位缺失時拋出

---

## 六、關鍵概念清單

學生完成本模組後，應能用自己的話解釋以下概念：

**Block 1 模組化：**
- [ ] module 和 package 的差別是什麼
- [ ] `__init__.py` 的用途是什麼
- [ ] 為什麼要用相對 import 在 package 內部互相引用
- [ ] `sys.path` 是什麼，影響哪些行為

**Block 2 環境管理：**
- [ ] 為什麼同一份程式在不同電腦可能跑不起來
- [ ] virtual environment 解決了什麼問題
- [ ] `requirements.txt` 和 `pyproject.toml` 各是什麼
- [ ] 哪些檔案要放進 git，哪些不要

**Block 3 例外處理：**
- [ ] stack trace 怎麼讀（從哪裡開始看）
- [ ] try/except/else/finally 各個區塊的觸發時機
- [ ] 為什麼 `except: pass` 是壞習慣
- [ ] logging 五個層級的語意差別

**Block 4 檔案 I/O：**
- [ ] `pathlib.Path` 相比字串路徑的優勢
- [ ] context manager（`with open(...) as f`）在做什麼
- [ ] JSON 序列化的型態限制
- [ ] buffer 的直覺概念

**Block 5 並行前導：**
- [ ] process 和 thread 的根本差別
- [ ] I/O bound 和 CPU bound 分別是什麼意思
- [ ] GIL 的直覺解釋（不需要細節）
- [ ] `DataLoader(num_workers=4)` 用的是哪種並行、解決什麼問題
- [ ] `async def` / `await` 的使用場景

---

## 七、與 AI 工程的連結

M5 的五個 Block 不只是「好的工程實踐」，它們直接對應到 AI 工程中的真實問題：

| M5 主題 | AI 工程對應場景 |
|---------|---------------|
| 模組化與 package | ML pipeline 的 feature engineering、preprocessing、evaluation 各模組獨立開發與測試 |
| 環境管理 | 訓練環境與推論環境的套件版本隔離；Docker image 的依賴管理基礎 |
| 例外處理 | 資料 pipeline 中的格式錯誤、API 呼叫超時、模型推論失敗的優雅降級 |
| 檔案 I/O + JSON | 模型 checkpoint 的 metadata 儲存；訓練結果的 metrics 輸出；設定檔讀取 |
| 並行 — I/O bound | `DataLoader(num_workers=4)` 資料預取；async LLM API 呼叫；爬蟲資料收集 |
| 並行 — CPU bound | PyTorch 內部的 C++ 並行；`torch.compile` 的計算圖優化；multiprocessing 資料預處理 |

**一個完整的 AI pipeline 實際上長這樣：**

```
資料收集（async I/O）
  → 資料清理（純 Python，可能需要 multiprocessing）
  → 特徵工程（NumPy，底層已並行）
  → 模型訓練（PyTorch + DataLoader num_workers + GPU）
  → 結果輸出（JSON 序列化 + pathlib 路徑管理）
  → 部署服務（FastAPI async def + logging）
```

M5 的每個 Block 都在這條鏈上有一個位置。這不是抽象的「軟體工程原則」，而是真實 AI 工程師每天面對的工具組合。

---

**Python 3.13 + PEP 703 里程碑備註（講師補充說明用）：**

Python 3.13 將 free-threaded 模式（無 GIL）作為實驗性選項引入，對應 PEP 703。這代表在未來，Python 的 threading 可能真正實現 CPU 並行，而不再受 GIL 限制。這是 Python 自 1.5 版引入 GIL 以來最重要的架構變化。目前（2026）仍是實驗性階段，主要套件（NumPy、pandas）的 thread-safe 驗證仍在進行中，不建議在生產環境使用。但這個方向說明了 Python 正在認真解決 CPU 並行的問題，學生看到「Python 不支援真正的多線程」這類說法時，需要加上「在 GIL 存在的前提下」這個但書。

---

*M5 — 進階 Python | 3 小時 | 24 小時 Python 數據分析與 AI 工程基礎課程*
