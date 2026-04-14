# M5 三鏡分析：First Principles／Fundamentals／BoK

> **文件定位：** 本文以三種思考鏡頭重新切 M5——先用第一性原理拆到不能再拆的物理／數學根源，再用「業界 fundamentals」盤點一份進階 Python 工程師必備 checklist，最後用 BoK（Body of Knowledge，這裡以 SWEBOK v3 為主）對齊國際知識體系。末段給「合流建議」——三個鏡頭的交集怎麼落到 M5 的上課節奏。
>
> **適用對象：** 課程設計審稿、技術主管、希望理解「為什麼這樣排課」的學員。內部 review 語氣。

---

## 鏡頭一｜First Principles（第一性原理）

把 M5 五個 Block 剝到不能再剝，剩下的是三條物理／數學層級的原理。

### 原理 1：環境隔離 = 依賴圖的可重現建置

**第一性陳述：**
> 一個軟體系統是一張有向無環圖（DAG），節點是套件版本，邊是相依宣告。要讓系統 A 在機器 M1 與 M2 上行為一致，兩台機器必須解析出**同一張圖**（同一組節點、同一組邊）。

**推論：**
- 全域 Python 環境等於「所有專案共用一張全局圖」——當兩個專案對同一節點版本要求不同，圖就無解。venv 的本質是「為每個專案建立獨立的圖空間」。
- `requirements.txt` 是一張圖的快照；`pyproject.toml` 是圖的抽象宣告（只有上下界）；lockfile（`uv.lock`、`poetry.lock`）是把抽象宣告「solve」成具體快照的結果。
- Docker 往上一層：連 Python 直譯器本身、OS 函式庫都納入 DAG。

**為什麼 M5 選 venv + requirements.txt：** 這是能展示完整「宣告 → 解析 → 快照」三步驟的**最小可演示模型**。poetry/uv 把三步驟包成黑盒，學生看不到機制。

### 原理 2：例外 = 非線性控制流的結構化命名

**第一性陳述：**
> 函式只有兩種結束方式——正常回傳與非正常中止。非正常中止需要一種機制把「中止原因」和「中止點」同時傳遞給呼叫方。例外就是這個機制的結構化、可命名版本。

**推論：**
- stack trace 是呼叫鏈的**線性化記錄**，是例外機制對「中止點」的實作。
- 例外類型繼承樹是對「中止原因」的分類系統——學生該記的不是類型列表，而是「我的中止原因屬於哪一類、呼叫方會怎麼分類處理」。
- `raise ... from ...` 是把「因果鏈」加進中止原因的描述——低層錯誤不直接暴露給最上層，而是被高層錯誤包裹、但保留根因。這是 API 設計的核心工具。

**為什麼 logging 在這一章：** logging 是「當非正常中止發生時，事後還能重建現場」的機制。例外處理和 logging 是一組互補工具——前者決定程式怎麼繼續，後者決定未來的人怎麼理解。

### 原理 3：並行收益上限 = Amdahl's Law

**第一性陳述：**
> 一個程式有可並行部分 p 和不可並行部分 (1−p)。用 n 個執行單位同時跑，總加速比 S(n) = 1 / ((1−p) + p/n)。當 n → ∞，S 的上限是 1/(1−p)。

**推論：**
- 若程式 90% 可並行（p=0.9），無論開幾核，加速上限是 10 倍。
- 選錯並行模型會讓 p 變小（例如把 I/O bound 用 multiprocessing 去打，process 啟動成本吃掉可並行部分）。
- GIL 的影響：Python thread 對於 CPU bound 任務，p 事實上近似於 0（因為 bytecode 互斥），無論多少 thread 都不會變快。
- PEP 703 free-threaded 要改變的就是這個 p——讓 Python thread 在 CPU bound 任務上也有非零 p。

**為什麼 I/O bound vs CPU bound 是核心區分：** 這決定了 p 的組成。I/O 操作會 release GIL → p 對 thread 有效；CPU 操作被 GIL 鎖住 → p 對 thread 為零，必須走 process 才能恢復。

---

## 鏡頭二｜Fundamentals（進階 Python 必備 checklist）

以「剛接手一個 Python 專案、需要判斷它健康嗎、能不能擴張」的 reviewer 視角，列出**進階 Python 工程師每一項都該會的 fundamentals**。這張 checklist 同時是 M5 驗收標準。

### 模組與封裝

- [ ] 能說清楚 module 與 package 差別，知道 `__init__.py` 三種用途（標記／re-export／初始化）
- [ ] 能使用相對 import（`from .module import func`）並理解其限制（只能在 package 內）
- [ ] 知道 circular import 是 smell，能判斷該切開還是延遲 import
- [ ] 理解 `__all__` 對 `from X import *` 的控制
- [ ] 知道 namespace package（PEP 420）存在，能判斷自己是否在用

### 環境與依賴

- [ ] 能以 `venv` 建環境、`pip freeze` 輸出快照、`pip install -r` 還原
- [ ] 能讀懂 `pyproject.toml` 的 `[project]`、`[build-system]` 段落
- [ ] 理解 `requirements.txt`、`pyproject.toml`、lockfile 三者定位差異
- [ ] 能在 `venv` / `conda` / `poetry` / `uv` 四者中選擇合適工具並解釋理由
- [ ] 知道 `pip install -e .`（editable install）用途與 `src/` layout 的搭配

### 例外與日誌

- [ ] 能正確使用 `try/except/else/finally` 四個區塊
- [ ] 會用 `raise ... from ...` 建立例外鏈
- [ ] 能自定義例外類別並設計繼承關係
- [ ] 不使用 `except:` 或 `except Exception: pass`（除非有極特殊理由且有註解）
- [ ] 以 `logging.getLogger(__name__)` 取得 logger，不在 library code 做 `basicConfig`
- [ ] 能設定 Handler + Formatter，並理解 logger 的樹狀繼承與 `propagate`
- [ ] 知道 `logging.exception()`、`exc_info=True` 的用途

### 檔案 I/O

- [ ] 使用 `pathlib.Path` 取代字串路徑
- [ ] 永遠指定 `encoding="utf-8"`
- [ ] 使用 `with` 管理檔案、鎖、連線等資源
- [ ] 能自己實作 context manager（`__enter__` / `__exit__` 或 `@contextmanager`）
- [ ] 區分 text mode 與 binary mode，知道何時不能用 text mode
- [ ] 處理大檔案時用 iteration 而非 `.read()`
- [ ] 理解 buffer 概念，知道 `flush()` 的時機

### 並行（前導）

- [ ] 能判斷任務屬 I/O bound 或 CPU bound
- [ ] 能在 asyncio／threading／multiprocessing 三者中選擇並說明理由
- [ ] 理解 GIL 的存在、影響與例外情況（I/O 與 C extension）
- [ ] 知道 `concurrent.futures` 的 `ThreadPoolExecutor` / `ProcessPoolExecutor`
- [ ] 對 PEP 703 / free-threaded Python 有基本認識（知道有這件事、方向是什麼）

### 工程素養（隱性但必要）

- [ ] 知道 `.gitignore` 該放什麼、不該放什麼
- [ ] 能寫 docstring 並理解 `help()` / IDE 自動提示從何而來
- [ ] 會用 `python -m` 執行模組（為何它和直接執行不同）
- [ ] 理解 `if __name__ == "__main__":` 的用途

> **Reviewer 備註：** 以上約 35 項。助教批作業時可以轉成 rubric，逐項打勾。若 checklist 通過率低於 70%，代表學生還在「能跑 Python」階段，尚未邁入「能做 Python 工程」。

---

## 鏡頭三｜BoK 對齊（SWEBOK v3／v4）

SWEBOK（Software Engineering Body of Knowledge）是 IEEE Computer Society 維護的國際軟體工程知識體系。M5 的五個 Block 主要對齊其中兩個 Knowledge Area（KA）。

### 對齊 KA 1：Software Construction

SWEBOK 的 Software Construction 章節涵蓋「編寫可被他人理解、修改、測試的程式碼」所需的核心活動。M5 對應段落：

| SWEBOK Construction 主題 | M5 對應 Block | 覆蓋程度 |
|---|---|---|
| Construction Fundamentals: Anticipation of Change | Block 1（模組化邊界） | 部分 |
| Managing Construction: API Design & Reuse | Block 1（`__init__.py` 作為對外 API） | 部分 |
| Coding: Error Handling & Defensive Programming | Block 3（try/except + logging） | 良好 |
| Coding: Construction Standards（程式碼風格與慣例） | 隱性帶過，未專章 | 缺口 |
| Construction Testing | 未涵蓋（預留） | 缺口 |
| Integration | Block 1（package 整合）、Block 2（環境整合） | 部分 |

**Reviewer 觀察：**
- **缺口 1（測試）：** M5 完全沒碰單元測試、pytest、mock。這是 SWEBOK Construction 中佔比不小的主題。建議在 M5 末尾加一個「預告」投影片：「測試在 M5 缺席，不代表不重要——它的戰場在下一門軟體工程課／實作專題。」
- **缺口 2（coding standards）：** 沒提 PEP 8、type hint、`black`/`ruff`/`mypy`。至少應在 Block 1 補一句：「程式碼風格有統一工具，自己寫時先用 `ruff` + `black`，不用自己記。」

### 對齊 KA 2：Software Configuration Management（SCM）

SWEBOK SCM 章節涵蓋「管理變更、追蹤版本、確保建置可重現」。M5 對應：

| SWEBOK SCM 主題 | M5 對應 Block | 覆蓋程度 |
|---|---|---|
| Configuration Identification（誰是 artifact、版本怎麼標） | Block 2（`requirements.txt`、pyproject） | 部分 |
| Configuration Control（變更如何控管） | 未涵蓋（假設有 git） | 缺口 |
| Configuration Status Accounting | 未涵蓋 | 缺口 |
| Configuration Auditing | 未涵蓋 | 缺口 |
| Release Management & Delivery | 未涵蓋 | 缺口（預留給日後） |
| Build Engineering（含可重現建置） | Block 2 核心 | 良好 |
| Environment Management | Block 2 核心 | 良好 |

**Reviewer 觀察：**
- M5 對 SCM 的覆蓋集中在「build & environment」兩個子題，這是合理的——其他 SCM 主題（release、auditing）超出 3 小時能涵蓋的範圍。
- 建議在 Slide 4 或 Slide 12 明確說一句「這屬於軟體組態管理的入門」，讓學生知道自己在學的知識在業界知識體系中的位置。

### 次要對齊：Software Design（部分）

- Block 1 的模組化與 package 邊界，也對應 SWEBOK Software Design 的「Modularity」與「Cohesion & Coupling」。建議講師在 Slide 2 口頭連結到「高內聚、低耦合」這組經典術語，讓學生未來看到這些詞不陌生。

---

## 合流建議（Synthesis）

三個鏡頭在 M5 的教學節奏上，應該如何合流？以下是我的 reviewer 建議。

### 合流點 1：開場定位（Slide 1）

- **First Principles 鏡頭：** 強調「可重現」是物理層面的圖解析問題，不是口號。
- **Fundamentals 鏡頭：** 把 checklist 的前五項當「學完 M5 後你能答出什麼」的宣告。
- **BoK 鏡頭：** 一句話告訴學生「這對應國際標準裡的 Construction + SCM」。
- **合流台詞（建議）：** 「你今天學的五件事，不是老師挑的，是國際標準裡『把程式碼變成工程』最小必要集合。我們用第一性原理搞清楚為什麼，用 checklist 確認你會了，最後對齊業界標準，讓你知道自己站在哪。」

### 合流點 2：環境管理（Slide 4–5）

- **First Principles 鏡頭主導：** 先講「依賴是 DAG」這張圖，再推出工具是在解什麼問題。
- **Fundamentals 鏡頭收束：** checklist 點名 venv/conda/poetry/uv 四者定位。
- **BoK 鏡頭作為權威背書：** 「這屬於 SCM 的 build engineering，IEEE 有章節專門討論。」
- **風險：** 若時間不夠，`01_on_page_annotation.md` 裡的四方比較表要壓縮成一張圖、口頭帶過，不要強講。

### 合流點 3：並行前導（Slide 10–11）

- **First Principles 鏡頭主導：** Amdahl's law 是這一段的物理天花板。
- **Fundamentals 鏡頭收束：** checklist 要求學生能判斷 I/O vs CPU、能選對工具。
- **BoK 鏡頭：** SWEBOK Construction 有專節討論「concurrency primitives」，可以點名一句就好。
- **風險：** 避免把 GIL、PEP 703、free-threaded 講太深——這屬於 M6（系統底層）與 M7（ML 效能）的地盤，M5 只種直覺。

### 合流點 4：收尾（Slide 12）

把三個鏡頭各用一句話收束：

1. **First Principles：** 「今天學的三件事在物理上都只是圖解析、控制流、Amdahl's law 的應用。原理看得深，記不住也能推出來。」
2. **Fundamentals：** 「回去把 checklist 打勾——能打七成就算跨過門檻。」
3. **BoK：** 「你站在 SWEBOK 的 Construction 與 SCM 兩座山的山腳。M6 接著爬系統底層那一座。」

---

## Reviewer 結語

- 三個鏡頭的設計哲學，其實是 M5 的**元教學方法**：同一件事，從「為什麼」（First Principles）、「怎麼做」（Fundamentals）、「社群怎麼看」（BoK）三個角度重複撞擊，讓知識點不只是背下來，而是被三次獨立的理由支撐。
- 實務上 3 小時課不可能三鏡頭平均分配。建議：第一鏡頭（First Principles）口頭帶過、點睛用；第二鏡頭（Fundamentals）是主戰場，練習與作業就是 checklist；第三鏡頭（BoK）放在講師備忘、投影片頁尾小字，學生有興趣自己深挖。
