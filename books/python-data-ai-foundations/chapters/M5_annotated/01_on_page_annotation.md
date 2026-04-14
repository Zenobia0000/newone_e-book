# M5 逐頁批註：進階 Python — 從腳本到系統的工程門檻

> **文件定位：** 本文件以「內部 reviewer」語氣，對 M5 每張投影片與每個知識點進行逐頁標註。每個知識點採三層鏡頭：🎯 宏觀（這在工程全景中的位置）／🔬 細部（實作上容易踩的坑）／⚠️ Reviewer 批判（原稿漏掉、需補齊的觀點）。目標是讓講師在上台前知道每個頁面的深度上限與風險，也讓讀者能在原文之上再獲得一層「為什麼這樣教／哪裡教得不夠」的判斷力。
>
> **適用對象：** M5 主講講師、助教、內部技審。繁體中文、台灣用語。

---

## 導論｜腳本與系統的分界線（Slide 1）

### 知識點 1.1：腳本 vs 系統的本質差別

- 🎯 **宏觀：** 這張頁面是整個 M5 的錨點，學生日後回想 M5 只會記得「腳本 vs 系統」這組對照。它對應軟體工程成熟度曲線上「個人生產力 → 團隊可維護」的那一階躍遷。
- 🔬 **細部：** 腳本的隱性依賴不只是套件版本，還包含：作業系統語系（cp950/UTF-8）、檔案系統大小寫敏感度、環境變數（`PYTHONPATH`、`LANG`）、當下工作目錄（`cwd`）。這些都不會寫在程式碼裡，但會決定能不能跑。
- ⚠️ **Reviewer：** 原稿只用「可重現」一詞帶過，太輕。建議講師在台上多補一句：「可重現是一個光譜，不是二元值——從『我明天還能跑』到『十年後任何人在任何硬體都能跑』，中間有很多級。M5 只帶你走到第一級。」這樣學生不會誤以為學完 M5 就等於 reproducible research。

### 知識點 1.2：M5 五個 Block 的組合論

- 🎯 **宏觀：** 五個 Block 並非平行並列，而是有依賴順序：模組化是前提，其餘四者都建構在「程式已經有邊界」之上。reviewer 建議在開場圖上直接用箭頭畫出依賴，不要用平行條列。
- 🔬 **細部：** 「並行前導」和其他四者層級不同——前四者是 day 1 就該有的工程衛生，並行是遇到效能瓶頸才需要的工具。混在同一張圖會誤導學生以為它和環境管理一樣是必備項。
- ⚠️ **Reviewer：** 原稿寫「最低基礎設施」五件套，但真正的最低其實是三件：模組化、環境、例外。I/O 視專案而定，並行更是選修。建議講師在講的時候分層說明，避免學生焦慮地認為沒有並行就不專業。

---

## Block 1｜模組化（Slide 2–3）

### 知識點 2.1：`import` 機制與 `sys.path`

- 🎯 **宏觀：** `import` 是 Python 命名空間的主要機制，理解它才能理解後續所有套件管理、可編輯安裝（`pip install -e .`）、namespace package（PEP 420）。
- 🔬 **細部：** `sys.path` 的實際組成順序：`''`（或腳本所在目錄）→ `PYTHONPATH` 環境變數 → site-packages → 使用者 site-packages。Jupyter 的 `sys.path` 行為和命令列執行 `python file.py` 不同，這是 notebook 改 package 時最大的踩雷點。
- ⚠️ **Reviewer：** 原稿沒提 `from module import *` 受 `__all__` 控制、也沒提 circular import 的問題。circular import 是學生拆模組後一定會遇到的第一個陷阱，建議 Slide 2 講解要點至少補一行：「如果 A import B、B 又 import A，會出現 ImportError，這通常代表你的模組邊界切錯了。」

### 知識點 2.2：`__init__.py` 與 package 邊界

- 🎯 **宏觀：** `__init__.py` 同時承擔「標記」、「re-export」、「初始化」三種責任，這是 Python 大型專案 API 設計的關鍵。PyTorch、pandas 的頂層 import 體驗都是由它決定。
- 🔬 **細部：** Python 3.3+ 引入 namespace package（PEP 420），沒有 `__init__.py` 也能當 package，但行為差異很細微（無 `__file__`、無初始化）。教學階段建議一律要求有 `__init__.py`，避免學生遇到 editable install 時混亂。
- ⚠️ **Reviewer：** 原稿沒提 `__init__.py` 裡寫太多初始化邏輯會拖慢 import 時間——這在大型 AI 專案（像 transformers）是真實痛點。建議加一句「`__init__.py` 越輕越好，能 lazy import 就 lazy」。

---

## Block 2｜環境管理（Slide 4–5）

### 知識點 3.1：環境隔離為什麼必要

- 🎯 **宏觀：** 這是學生從「自己跑」邁向「別人也能跑」的第一道門檻，對應 SWEBOK Software Configuration Management 的「可重現建置」要求。
- 🔬 **細部：** Python 套件衝突有三層：Python 版本（3.9 vs 3.12）、套件大版本（pandas 1.x vs 2.x）、套件間接相依（A 要 numpy<2，B 要 numpy>=2）。venv 只解決第二、三層，解不了第一層——那需要 pyenv、conda、或 Docker。
- ⚠️ **Reviewer：** 原稿完全沒談 **venv vs conda vs poetry vs uv** 的差異，這是目前 Python 生態最常被問的問題，學生回公司看到前輩用不同工具會困惑。**必須補齊這張比較表**（見下）。

#### Reviewer 必補｜環境工具四方比較

| 工具 | 定位 | 優勢 | 限制 | 建議使用時機 |
|------|------|------|------|--------------|
| `venv` | 標準函式庫內建的虛擬環境 | 零依賴、官方保證、跨平台 | 不管理 Python 版本本身、不做 lockfile | 學習階段、簡單專案 |
| `conda` / `mamba` | 跨語言套件管理（含非 Python 二進位） | 能裝 CUDA、R、C 函式庫、管理 Python 版本 | 速度較慢、生態與 PyPI 不完全相容 | 資料科學／AI 環境（需 CUDA、MKL）|
| `poetry` | PEP 517/518 相容的現代依賴管理 | 有 lockfile、發布流程完整 | 學習曲線稍陡、與 pip 行為偶有差異 | 套件作者、需要 lockfile 的應用 |
| `uv` | Rust 寫的新一代快速工具（取代 pip/pip-tools/venv） | 極快、單一工具涵蓋建環境+安裝+lock | 2024 才穩定、部分企業尚未採用 | 新專案、CI 加速、現代開發流程 |

> **Reviewer 建議台詞：** 「venv 是考駕照的手排車，conda 是露營車，poetry 是可以申報的正式發票，uv 是特斯拉。我們在 M5 先學手排，因為手排學會了其他都看得懂。」

### 知識點 3.2：`requirements.txt` vs `pyproject.toml`

- 🎯 **宏觀：** 這是 Python 打包歷史演進的縮影——從 `setup.py`（可執行、危險）到 `setup.cfg`（宣告式但分散）到 `pyproject.toml`（PEP 518/621 統一入口）。
- 🔬 **細部：** `requirements.txt` 是「已安裝套件的快照」，適合應用部署；`pyproject.toml` 是「專案的身分證與依賴宣告」，適合套件發布。兩者不是替代關係，在大型專案常並存：`pyproject.toml` 宣告抽象依賴（`pandas>=2,<3`），`requirements.txt` 或 `uv.lock`／`poetry.lock` 鎖定具體版本。
- ⚠️ **Reviewer：** 原稿 Slide 5 只用「現代替代方案」一筆帶過，太輕。建議加一張對照表直接點明：`requirements.txt` = 快照、`pyproject.toml` = 宣告、`*.lock` = 鎖定。學生回職場看到三種檔案並存不會迷路。

---

## Block 3｜例外處理（Slide 6–7）

### 知識點 4.1：例外繼承樹與例外鏈

- 🎯 **宏觀：** 例外是 Python 的「非線性控制流」，它和 `return` 一樣是函式的正常結束方式之一，不是異常現象。理解這點才能設計出好的 API。
- 🔬 **細部：** `BaseException` 下面是 `Exception`、`KeyboardInterrupt`、`SystemExit`、`GeneratorExit`。只 `except Exception` 不會攔到 Ctrl+C（這是好事）；寫 `except:` 裸 except 會攔到 Ctrl+C（這是壞事）。
- ⚠️ **Reviewer：** 原稿**完全沒提例外鏈（`raise ... from ...`）**，這是 Python 3 例外處理最重要的演進之一。必補：

#### Reviewer 必補｜例外鏈三種寫法

```python
# 1. 隱式鏈：except 中又拋，自動帶 __context__
try:
    risky()
except ValueError:
    raise RuntimeError("higher-level failure")

# 2. 顯式鏈（建議）：明確標示因果
try:
    risky()
except ValueError as e:
    raise RuntimeError("higher-level failure") from e

# 3. 切斷鏈：用 from None 隱藏低層細節（對外 API 用）
try:
    risky()
except ValueError:
    raise RuntimeError("higher-level failure") from None
```

> **Reviewer 建議：** Slide 6 至少要加一個「raise from」的示意，否則學生寫出的 library 永遠是黑盒子——外面只看到 `RuntimeError`，看不到根因的 `ValueError`。

### 知識點 4.2：logging 的 handler / formatter / logger 三層架構

- 🎯 **宏觀：** logging 不是單一物件，是一套層級式系統：`Logger` 決定「誰在記」、`Handler` 決定「記到哪」、`Formatter` 決定「記成什麼樣」、`Filter` 決定「要不要記」。這個設計呼應 Unix 的「關注點分離」哲學。
- 🔬 **細部：** `logging.basicConfig()` 只會在 root logger 尚未設定 handler 時生效；重複呼叫第二次什麼都不會做。這是初學者最常踩的坑——改了 format 結果沒變，以為 logging 壞了，其實是 basicConfig 早被呼叫過了。
- ⚠️ **Reviewer：** 原稿**只介紹了 Logger 和五層級，沒介紹 Handler / Formatter 的層級關係**。建議 Slide 7 補一張層級圖（見 `04_layout_visual_spec.md`）：Logger（樹狀，按 `__name__` 自動繼承）→ Handler（可多個：StreamHandler、FileHandler、RotatingFileHandler）→ Formatter（每個 Handler 一個）。這樣學生看到生產環境的 `logging.yaml`／`dictConfig` 才不會懵。

### 知識點 4.3：logger 的樹狀繼承與 propagate

- 🎯 **宏觀：** `logging.getLogger("a.b.c")` 會自動繼承 `a.b` 的設定，這是 logger 樹的核心機制。library 作者應該只建立 logger、不設定 handler，把 handler 配置權留給應用作者——這是 Python logging 的慣例。
- 🔬 **細部：** `propagate = False` 可以切斷向上傳播，常用於避免訊息重複輸出。但切斷後就要自己配 handler，否則什麼都看不到。
- ⚠️ **Reviewer：** 原稿沒提這個，但這是助教批改學生作業時最常見的 bug：學生在一個模組裡 `logging.basicConfig`、又在另一個模組裡 `logging.basicConfig`，結果輸出重複或消失。建議至少在講師備忘中提醒。

---

## Block 4｜檔案 I/O（Slide 8–9）

### 知識點 5.1：pathlib 與 context manager

- 🎯 **宏觀：** `pathlib` 是 Python 面向物件化的一個縮影，和 `open()` 配合 `with` 的 context manager 一樣，都在推動「資源管理的自動化」。
- 🔬 **細部：** `pathlib.Path` 不做 I/O 直到你呼叫 `.read_text()` 或 `.open()`。這代表建立 Path 物件很便宜，可以大量傳遞。另外 `Path.resolve()` 會解析符號連結，`Path.absolute()` 不會——兩者經常被混用。
- ⚠️ **Reviewer：** 原稿沒詳細解釋 **context manager 的 `__enter__` / `__exit__` 協定**，這是 Python 相當重要的協定（和 iterator、async context manager 並列）。建議補：

#### Reviewer 必補｜context manager 協定

```python
class ManagedResource:
    def __enter__(self):
        # 取得資源（開檔、鎖、連線）
        return self                 # with ... as X 中的 X

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 無論有無例外都執行
        # 回傳 True 代表吞掉例外；回傳 False/None 讓例外繼續傳播
        return False
```

> **Reviewer 建議：** 講師應該點出 `with open(...)` 背後就是這個協定，學生自己也可以寫，例如管理資料庫連線、臨時目錄、計時器。連結到 `contextlib.contextmanager` 裝飾器是更優雅的替代寫法。

### 知識點 5.2：text vs binary、buffered vs unbuffered

- 🎯 **宏觀：** I/O 在 Python 中分三層：raw（`io.RawIOBase`，無 buffer）、buffered（`io.BufferedIOBase`，有 buffer）、text（`io.TextIOBase`，有 buffer + 編碼解碼）。`open()` 預設給你 text mode + buffered。
- 🔬 **細部：** text mode (`"r"`) vs binary mode (`"rb"`) 的差異：text mode 會做編碼轉換（bytes ↔ str）與行尾正規化（`\r\n` → `\n`）；binary mode 不做。處理 PDF、圖片、protobuf 一定要用 binary，否則會被改壞。
- ⚠️ **Reviewer：** 原稿 Slide 8 只用一句話帶過 buffer，**沒區分 text/binary、沒解釋 buffered/unbuffered**。這在真實工程很重要：寫 log 時若 buffered 沒 flush，程式 crash 後 log 就遺失。必補：

| 模式 | 開啟旗標 | 資料型態 | 編碼 | 預設 buffer |
|------|----------|----------|------|-------------|
| Text | `"r"`/`"w"` | `str` | 有（必須給 `encoding=`）| line-buffered（tty）／block（file） |
| Binary | `"rb"`/`"wb"` | `bytes` | 無 | block-buffered |
| Unbuffered binary | `"rb"` + `buffering=0` | `bytes` | 無 | 無（每呼叫即 syscall） |

> **Reviewer 建議：** 至少提一次「Python 3 text mode 預設 encoding 在 Windows 是 locale（cp950），在 Linux/macOS 是 UTF-8。這個不一致性會讓你的程式跨平台壞掉。永遠明確指定 `encoding="utf-8"`。」

### 知識點 5.3：generator vs iterator（原稿未提，Reviewer 認為該加）

- 🎯 **宏觀：** iterator 是 Python 的迭代協定（`__iter__` + `__next__`），generator 是用 `yield` 寫的 iterator 的糖衣語法。這在處理大檔案 I/O 時是核心工具——一次一行讀，不把整份載入記憶體。
- 🔬 **細部：** `for line in open("big.csv"):` 其實就是一個 generator-like 的迭代，不會把整個檔案載入。`pandas.read_csv(..., chunksize=10000)` 回傳的也是 iterator，讓你能處理比記憶體大的資料。
- ⚠️ **Reviewer：** 原稿 I/O 章節**完全沒連結到 generator/iterator**，但這其實是大檔案 I/O 的核心技巧。建議 Slide 8 末尾或 Slide 9 補一個小節：「處理大檔案時，不要 `read()`，用 iteration。」

---

## Block 5｜並行前導（Slide 10–11）

### 知識點 6.1：三種並行機制的本質差別

- 🎯 **宏觀：** process / thread / coroutine 對應三個不同的「單位」：作業系統調度單位（process）、作業系統內的輕量執行緒（thread）、應用層的協作任務（coroutine）。這條層級從 M6 的 OS 概念會進一步展開。
- 🔬 **細部：** 啟動成本（process > thread > coroutine，差三個數量級）、記憶體隔離（process 完全隔離、thread 共享、coroutine 共享）、上下文切換成本（process 最貴、thread 中等、coroutine 最便宜）。
- ⚠️ **Reviewer：** 原稿的三欄對比**沒談啟動成本與 context switch 成本**，這是選工具時真正的權衡。建議補數字級直覺：process 啟動 ~10ms、thread 啟動 ~10μs、coroutine 建立 <1μs。

### 知識點 6.2：asyncio vs threading vs multiprocessing 的決策樹

- 🎯 **宏觀：** 這三者不是「哪個比較好」，而是「用在哪個場景」。Amdahl's law（後面 `02_three_lens_analysis.md` 會展開）告訴我們並行化收益有上限，選錯模型直接上限歸零。
- 🔬 **細部：** 一個進階但實用的區分：「I/O bound 且連線數多」→ asyncio（可以開幾萬 coroutine）；「I/O bound 但用 blocking library」→ threading（改 async 改不動）；「CPU bound」→ multiprocessing 或 C/Rust 擴充。
- ⚠️ **Reviewer：** 原稿雖然區分了 I/O vs CPU bound，但**沒提到「legacy blocking library」這個 threading 仍然必要的現實理由**。pandas、requests、很多資料庫 driver 都是 blocking 的，asyncio 不能直接用，要包 `run_in_executor` 或改用 async 版 library。

### 知識點 6.3：GIL 的真相

- 🎯 **宏觀：** GIL 是 CPython 實作細節，不是 Python 語言規格的一部分（這點講師要講清楚）。其他實作（Jython、IronPython）沒有 GIL；PyPy 也在走自己的路。
- 🔬 **細部：** GIL 存在的原因：保護 reference counting 不需要每個物件都上鎖。代價：多 thread 不能同時執行 Python bytecode。但 I/O 系統呼叫、NumPy 的 C 擴充、很多底層操作都會主動釋放 GIL，所以 thread 對 I/O bound 依然有用。
- ⚠️ **Reviewer：** 原稿的 GIL 解釋「為了保護 reference counting」是對的，但**沒提 GIL 每 5ms（Python 3.2+，原本 100 bytecode）會 release 一次給其他 thread**，這個細節能解釋很多「為什麼我的 thread 看起來有動但還是很慢」的疑問。

### 知識點 6.4：PEP 703 / free-threaded Python 路線影響

- 🎯 **宏觀：** PEP 703 是 Python 歷史上最大的語言實作變革之一，3.13 已進入 experimental、3.14/3.15 會逐步推進。對 AI 工程生態影響巨大——PyTorch、NumPy 都在適配。
- 🔬 **細部：** free-threaded build（`python3.13t`）和預設 build 不同。C extension 要明確宣告支援（`Py_mod_gil = Py_MOD_GIL_NOT_USED`），否則會自動 fallback 到 GIL。第三方套件適配可能要 1–3 年。
- ⚠️ **Reviewer：** 原稿只提了「進入實驗性支援」，**沒講「這代表學生目前學的 threading + GIL 直覺未來會部分失效」**。建議在 Slide 10 結尾加一句：「這頁現在教的 GIL，是 Python 3.13 之前的真相；未來的真相會是『某些版本有 GIL、某些沒有』，你需要問你的 Python build 用哪種。」

---

## 總結與共通批註

### Reviewer 全篇觀察

1. **原稿最大優點：** 「腳本 vs 系統」錨點抓得很好，五個 Block 的組合邏輯清楚。
2. **原稿最大缺口：** 工具生態的「現代替代方案」只點到為止——venv/conda/poetry/uv、requirements.txt/pyproject.toml、logging 分層、例外鏈、buffered I/O、generator。這些是真實工程會踩的東西，M5 應該至少「種下名字」。
3. **深度分級建議：** 本章很容易講成「炫技大雜燴」。建議講師採三層深度：**必教**（原稿已有）、**點名**（提到名字讓學生日後不陌生，如 poetry、uv、PEP 703）、**助教補充**（細節寫在講義附錄，如 context manager 協定、例外鏈）。三層分清楚，3 小時才夠用。
4. **對齊後續模組：** 並行前導的深度應該刻意留白給 M6，M5 只負責「種直覺」。若在 M5 把 GIL、process table、context switch 講透，M6 會無戲可唱。
