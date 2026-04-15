# Chapter 6：檔案 I/O 與例外處理

**模組：** M3 數據工程核心  
**時數：** 1.5 小時  
**前置知識：** Ch5 OOP（自訂 Exception 用得到）  
**後續銜接：** Ch7（NumPy 讀檔）、Ch8（Pandas 讀檔）、Ch10（管線錯誤處理）

---

## 一、章節定位

進入數據工程的第一道門：**資料從哪裡進、錯誤怎麼處理**。本章呼應 Ch1 的 OS 檔案系統與 RAM 概念，並用 Ch5 的 OOP 自訂 Exception。

---

## 二、學習目標

完成本章後，學生能夠：

1. 用 `pathlib` 跨平台處理檔案路徑
2. 讀寫 CSV / JSON（純 Python 與 Pandas 兩種途徑）
3. 用 `with` context manager 安全管理檔案開關
4. 寫出明確的 `try / except / finally / else` 結構
5. 設計自訂 Exception 類別並正確 raise
6. 用 chunking 處理大於 RAM 的檔案

---

## 三、章節結構

### 6-1. 路徑與 I/O 基礎（25 分鐘）
- **`pathlib` 取代 `os.path`**：
  ```python
  from pathlib import Path
  data_dir = Path('data')
  for csv in data_dir.glob('*.csv'):
      print(csv.name, csv.stat().st_size)
  ```
- **跨平台路徑**（呼應 Ch1 OS）：為何 `'data/file.csv'` 比 `'data\\file.csv'` 安全
- **with statement** 與 context manager：自動關閉檔案、釋放資源
- 純 Python 讀寫 CSV（`csv.reader` / `csv.DictReader`）
- 讀寫 JSON（`json.load` / `json.dump`，注意 `ensure_ascii=False`）

### 6-2. 例外處理：try / except / finally / else（35 分鐘）
- 為什麼需要例外處理：資料工程現場 80% 的問題不是邏輯錯，是「資料長得跟你想的不一樣」
- 完整結構：
  ```python
  try:
      result = risky_op()
  except SpecificError as e:
      handle(e)
  except (ErrorA, ErrorB):
      ...
  else:
      # try 沒出錯才執行
      use(result)
  finally:
      # 不論成功失敗都執行
      cleanup()
  ```
- **常見錯誤類別**：`FileNotFoundError`、`KeyError`、`ValueError`、`TypeError`
- **反模式**：`except:` 或 `except Exception:` 吞掉所有錯誤
- **自訂 Exception**（呼應 Ch5）：
  ```python
  class DataValidationError(Exception):
      def __init__(self, column, reason):
          self.column = column
          self.reason = reason
          super().__init__(f"Column {column}: {reason}")
  
  if df['age'].min() < 0:
      raise DataValidationError('age', 'negative value detected')
  ```

### 6-3. 大檔處理：Chunking（30 分鐘）
- **呼應 Ch1 OOM**：當 CSV 大小 > RAM，怎麼辦
- Pandas chunking：
  ```python
  for chunk in pd.read_csv('huge.csv', chunksize=100_000):
      process(chunk)
  ```
- 純 Python 逐行讀（呼應 Ch2 Generator）
- **思考**：為何 chunk 大小通常設 10 萬 ~ 100 萬筆
- **本課程不教**：Dask、Polars streaming（屬下一階段課程）

---

## 四、課後練習

1. **基礎題**：寫一段程式，讀取資料夾下所有 CSV，列出每個檔案的列數
2. **例外題**：給定一個會隨機出錯的函式，用 `try-except-else-finally` 完整處理
3. **挑戰題**：寫一個 `SafeReader` 類別，繼承自定義 Exception，能在讀檔時記錄錯誤檔案到 log

---

## 五、銜接下一章

資料能進、錯誤能擋，下一步是「**運算它**」。Ch7 進入 NumPy，學會用向量化思維處理數值資料。
