# M5 最小可行知識卡（Minimum Viable Knowledge）

> **文件定位：** 本文件為 M5 的「速學卡片」——面向「會議前 30 分鐘快速回顧」、「新同事第一天 onboarding」、「半年後忘了再翻一遍」三個使用場景。每張卡片一個知識點，正面一句錨句、背面一個「為什麼」+「怎麼做」+「反模式」三格。共 13 張。內部 review 語氣、繁體中文台灣用語。
>
> **使用方式：** 可列印成實體閃卡、也可直接掃 markdown 快速讀。每張讀完應該能在 2 分鐘內對同事口頭複述。

---

## 卡 01｜腳本 vs 系統

**正面：**
> 「能跑一次」和「能活下去」是兩種不同的東西。

**背面：**
- **為什麼：** 腳本依賴個人環境的隱性設定；系統把所有依賴顯性化，才能跨人、跨機器、跨時間復現。
- **怎麼做：** 檢查三件事——有沒有模組結構、有沒有 venv + requirements、有沒有 try/except + logging。
- **反模式：** 「我電腦上可以跑」——這句話在團隊裡是警訊，不是辯解。

---

## 卡 02｜module vs package

**正面：**
> 一個 `.py` 檔是 module；一個有 `__init__.py` 的資料夾是 package。

**背面：**
- **為什麼：** module 管理功能邊界，package 管理命名空間結構。PyTorch、pandas 本身都是 package。
- **怎麼做：** 大於 200 行的腳本就該開始拆；每個 module 負責單一責任（清理／特徵／視覺化）。
- **反模式：** 把所有函式塞在同一個 `.py` 裡、或把類別和資料全部塞進 `__init__.py`（拖慢 import）。

---

## 卡 03｜`__init__.py` 三種用途

**正面：**
> 空檔案／re-export／初始化——選一種、或混用。

**背面：**
- **為什麼：** 它決定 `import mypkg` 時使用者看到什麼介面。
- **怎麼做：**
  ```python
  # re-export（最常見）
  from .clean import normalize, drop_nulls
  from .features import compute_ratio
  __all__ = ["normalize", "drop_nulls", "compute_ratio"]
  ```
- **反模式：** 在 `__init__.py` 做昂貴的初始化（讀大檔、連資料庫），讓 `import` 變慢。

---

## 卡 04｜venv 生命週期四步

**正面：**
> Create → Activate → Install → Freeze。

**背面：**
- **為什麼：** 一個專案一個環境，避免全域污染與版本衝突。
- **怎麼做：**
  ```bash
  python -m venv .venv
  source .venv/bin/activate     # Windows: .venv\Scripts\activate
  pip install pandas matplotlib
  pip freeze > requirements.txt
  ```
- **反模式：** 直接用系統 Python 裝套件、`.venv` 沒放 `.gitignore`、在全域環境跑專案。

---

## 卡 05｜venv vs conda vs poetry vs uv

**正面：**
> 工具四選一——看場景、看團隊、看時代。

**背面：**
- **為什麼：** 四者解決不同層次的問題，沒有絕對最佳解。
- **怎麼做：**
  | 情境 | 首選 |
  |---|---|
  | 學習、簡單專案 | `venv` |
  | AI/CUDA 環境 | `conda`/`mamba` |
  | 要發布套件 | `poetry` |
  | 現代新專案、CI 加速 | `uv` |
- **反模式：** 同一專案混用兩套（venv + conda 同時）。

---

## 卡 06｜requirements.txt vs pyproject.toml vs lockfile

**正面：**
> 快照 vs 宣告 vs 鎖定——三種檔案三種角色。

**背面：**
- **為什麼：** `requirements.txt` 是當下安裝結果的快照；`pyproject.toml` 宣告抽象相依（`pandas>=2,<3`）；lockfile（`uv.lock`、`poetry.lock`）把宣告 solve 成具體版本。
- **怎麼做：** 應用部署可只有 `requirements.txt`；套件發布必有 `pyproject.toml`；要 reproducible 建置加 lockfile。
- **反模式：** 以為 `pip freeze` 輸出的 `requirements.txt` 等於 lockfile——它不處理平台差異與解析一致性。

---

## 卡 07｜try/except/else/finally 四區塊

**正面：**
> try 放危險、except 處理、else 成功才跑、finally 必跑。

**背面：**
- **為什麼：** 四個區塊各管一種狀態，語意清楚。
- **怎麼做：**
  ```python
  try:
      data = load(path)          # 危險動作
  except FileNotFoundError:
      logger.error("missing: %s", path)
      data = {}
  else:
      logger.info("loaded %d rows", len(data))  # 成功才執行
  finally:
      cleanup()                  # 無論如何都跑
  ```
- **反模式：** `except Exception: pass`（靜默失敗）、裸 `except:`（連 Ctrl+C 都攔）。

---

## 卡 08｜例外鏈 `raise ... from ...`

**正面：**
> 低層錯誤被高層包住，但根因保留。

**背面：**
- **為什麼：** API 不該洩露底層實作，但除錯需要根因。例外鏈兩全其美。
- **怎麼做：**
  ```python
  try:
      parse(raw)
  except ValueError as e:
      raise DataValidationError("invalid row") from e  # 保留根因
  ```
  要隱藏可用 `from None`。
- **反模式：** 直接 `raise RuntimeError(...)` 把底層錯誤訊息丟掉，debug 時少一個線索。

---

## 卡 09｜logging 五層級 + 三架構

**正面：**
> DEBUG/INFO/WARNING/ERROR/CRITICAL；Logger → Handler → Formatter。

**背面：**
- **為什麼：** 五層級讓你能分級過濾；三架構讓你能同一訊息同時輸出到 stderr、檔案、email。
- **怎麼做：**
  ```python
  import logging
  logger = logging.getLogger(__name__)     # library code 只取 logger
  logger.info("loaded %d rows", n)
  # 應用入口才設定 handler / formatter / level
  ```
- **反模式：** library code 呼叫 `logging.basicConfig`（會覆蓋使用者設定）；用 `print` 除錯生產程式。

---

## 卡 10｜pathlib + 永遠指定 encoding

**正面：**
> `Path("data") / "raw" / "a.csv"`；`read_text(encoding="utf-8")`。

**背面：**
- **為什麼：** 字串路徑跨平台易錯；Python 3 text mode 預設 encoding 因 OS 而異（Windows 常踩 cp950 地雷）。
- **怎麼做：**
  ```python
  from pathlib import Path
  p = Path(__file__).parent / "data" / "input.csv"
  text = p.read_text(encoding="utf-8")
  ```
- **反模式：** `"data/" + filename`；`open(path)` 不指定 encoding。

---

## 卡 11｜context manager（`with`）

**正面：**
> 進入時取資源、離開時釋放——不論有無例外。

**背面：**
- **為什麼：** `with` 背後的 `__enter__` / `__exit__` 協定保證資源清理，比手動 `try/finally` 乾淨。
- **怎麼做：**
  ```python
  with open(path, encoding="utf-8") as f:
      data = f.read()
  # 離開 with 自動 flush + close
  ```
  自製：`@contextlib.contextmanager` 裝飾器 + `yield`。
- **反模式：** 手動 `f = open(...); f.close()`（例外發生時檔案沒關）。

---

## 卡 12｜process / thread / coroutine 三選一

**正面：**
> 瓶頸決定工具，不是反過來。

**背面：**
- **為什麼：** 啟動成本、記憶體隔離、GIL 影響都不同，選錯直接白做。
- **怎麼做：**
  | 任務類型 | 工具 |
  |---|---|
  | CPU bound（純 Python 運算） | `multiprocessing` |
  | CPU bound（能向量化） | NumPy / PyTorch（底層並行）|
  | I/O bound（blocking lib） | `threading` |
  | I/O bound（高併發、可 async） | `asyncio` |
- **反模式：** 用 `threading` 處理純 Python CPU 運算（被 GIL 擋住、毫無收益）。

---

## 卡 13｜GIL + PEP 703 未來訊號

**正面：**
> CPython 當下有 GIL；Python 3.13 起 free-threaded 實驗中。

**背面：**
- **為什麼：** GIL 讓 CPython 實作簡單，但限制 thread 的 CPU 並行。PEP 703 方向是可選擇性地關掉 GIL。
- **怎麼做：** 現在寫 Python 繼續照「I/O→thread、CPU→process」寫；持續關注 `python3.13t`、主要套件（NumPy、PyTorch）的支援進度。
- **反模式：** 以為 GIL 是 Python 語言規格（它是 CPython 實作）；以為 free-threaded 會馬上全面可用（套件適配要 1–3 年）。

---

## 附錄｜使用建議

- **onboarding 情境：** 新人 day 1 給卡 01–04、09、10、11；day 7 再給其他。
- **會議前回顧：** 只看「正面」一句話，能在 3 分鐘內刷完全部 13 張。
- **半年後複習：** 只讀「反模式」——你犯過的錯會自己浮出來。
- **Reviewer 備註：** 這 13 張卡刻意不包含測試、type hint、CI/CD——那些不在 M5 範圍。若學生問「這樣就夠嗎」，回答：「不夠，但這是『能活下去』的最小必要集合。其他東西站在這之上。」
