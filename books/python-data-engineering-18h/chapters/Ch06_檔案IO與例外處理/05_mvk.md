# Ch06 · Minimum Viable Knowledge

**章節**：檔案 I/O 與例外處理（M3 數據工程核心 · 1.5 hr）
**Governing thought**：資料能進、錯誤能擋、大檔吃得下 —— 這是數據工程的第一道門。

---

## 三層必帶走的骨架

### 1. I/O — 資料進得來
- **`pathlib`** 取代 `os.path`：`Path('data') / 'file.csv'` 跨平台、可鏈接、物件化
- **`with open(...) as f:`** 是鐵律 — context manager 自動關檔、釋放 lock
- **CSV**：`csv.DictReader` 讓每列成為 dict（欄位有名有姓，勝過 index）
- **JSON**：`json.dump(..., ensure_ascii=False, indent=2)` 中文才不會變 `\uXXXX`

### 2. 例外 — 錯誤擋得住
- **四段完整骨架**：
  ```python
  try:        # 可能炸的那一段
      ...
  except SpecificError as e:
      ...     # 預期的錯，好好處理
  else:
      ...     # try 完全沒炸才執行
  finally:
      ...     # 成功失敗都要執行（關資源）
  ```
- **四種最常見**：`FileNotFoundError` / `KeyError` / `ValueError` / `TypeError`
- **反模式**：`except Exception: pass` — 把火吞進肚子裡，bug 三週後才爆
- **自訂 Exception**：`class DataValidationError(Exception):` 繼承 Ch5 學的類別語法
- **鏈接 traceback**：`raise CleanedError(...) from e` 保留兇手指紋

### 3. 大檔 — 吃得下
- **Pandas chunking**：`for chunk in pd.read_csv(path, chunksize=100_000):`
- **純 Python 逐行**：`for line in f:` — 檔案物件天生是 generator（呼應 Ch2）
- **chunk 大小**：通常 10 萬 ~ 100 萬筆，太小 I/O 頻繁、太大又 OOM

---

## 學生離開教室時應能

1. 用 `pathlib` 遍歷資料夾下所有 CSV 並列出檔名與大小
2. 寫出 `try / except / else / finally` 四段完整結構並解釋每段用途
3. 區分 `FileNotFoundError` / `KeyError` / `ValueError` / `TypeError` 的適用場景
4. 設計一個自訂 Exception 並用 `raise ... from e` 保留原始 traceback
5. 用 `pd.read_csv(chunksize=)` 處理大於 RAM 的 CSV 並說明 chunk 大小取捨

---

## 本章刻意不教（Linus 原則：解決實際問題）

- **Dask / Polars streaming** — 下一階段課程的範圍
- **`asyncio` / `aiofiles`** — 此課程 I/O 瓶頸不是 CPU 併發
- **二進位檔 / `struct` / `pickle`** — 資料工程現場不常用
- **`contextlib` 自製 context manager** — Ch10 會自然碰到時再教

---

## 銜接

- **呼應 Ch1**：OS 檔案系統、RAM vs Disk、OOM 的場景這章真的會撞到
- **呼應 Ch2**：檔案逐行讀就是 generator
- **呼應 Ch5**：自訂 Exception 用繼承語法
- **銜接 Ch07**：NumPy 的 `np.loadtxt` / `np.load` 會再碰 I/O
- **銜接 Ch08**：Pandas 的 `read_csv` / `read_json` 是本章的高階封裝
- **銜接 Ch10**：管線裡的錯誤處理、log、retry，都從這章的骨架長出去
