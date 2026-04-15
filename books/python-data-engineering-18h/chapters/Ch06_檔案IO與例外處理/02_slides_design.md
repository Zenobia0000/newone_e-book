# Ch06 · 02_slides_design — SOP §4.2

- 章節：檔案 I/O 與例外處理（M3 · 1.5 hr · 17 張內容）
- Governing thought：資料能進、錯誤能擋、大檔吃得下 —— 這是數據工程的第一道門。
- 配色：黑 + 灰 + 深綠（#1B5E3F）
- 每張格式：🖼️（視覺規格）/ 📣（文字骨架）/ 🎙️（口頭引導）

---

## S1 · SILENT — 開場第一口氣
- 🖼️ 深綠滿版，白字 hero，中央水平細線。
- 📣 「資料能進、錯誤能擋 ——\n這是數據工程的第一道門。」
- 🎙️ 從今天起進入 M3 數據工程核心。Ch07 NumPy、Ch08 Pandas 之前，先學會「資料怎麼進來、錯誤怎麼擋住」。運算很美，I/O 很髒，但 I/O 沒搞好，下面全崩。

## S2 · ASK — Socratic 開場
- 🖼️ 白底，大哉問 + 右下 data card。
- 📣 Q：「為什麼生產環境 80% 的 bug，不是邏輯錯，是檔案長得跟你想的不一樣？」
  Data card：label「Airbnb Data Platform 2022 post-mortem」· stat「82%」· caption「資料管線故障源自『格式 / 缺值 / 編碼』，非計算邏輯錯誤」
- 🎙️ 你想的是「金額欄是數字」，現場給你的是 `'1,234'` 帶逗號的字串。你想的是檔案存在，使用者昨天把它搬走了。I/O 與例外處理，就是給這些「長得不一樣」的現實留一道門。

## S3 · MATRIX 2×3 — pathlib vs os.path 對照
- 🖼️ 2×3 方陣，左欄 os.path 寫法、右欄 pathlib 寫法。
- 📣 標題「pathlib 取代 os.path：跨平台六組對照」
  cells（row-major）：
  - `os.path.join('data', 'a.csv')` — 字串拼接、跨平台要自己管分隔符
  - `Path('data') / 'a.csv'`（highlight）— 運算子重載，/ 會自動用 OS 分隔符
  - `os.path.exists(p)` + `os.listdir(d)` — 兩個函式、回傳字串
  - `p.exists()`、`d.iterdir()`、`d.glob('*.csv')`（highlight）— 方法鏈、回傳 Path 物件
  - `os.path.splitext(p)[1]` / `os.stat(p).st_size` — 元組索引、老派
  - `p.suffix`、`p.stat().st_size`、`p.stem`（highlight）— 屬性化、可讀
- 🎙️ Python 3.4 之後的世界：不要再寫 `os.path.join` 了。`pathlib` 把路徑當物件看，而不是當字串拼。

## S4 · CODE — pathlib 實戰
- 🖼️ 滿版 code panel，label「遍歷資料夾 · 讀取內容 · 取元資訊」
- 📣 code：
  ```python
  from pathlib import Path

  data_dir = Path('data')
  for csv in data_dir.glob('*.csv'):
      print(csv.name, csv.stat().st_size)

  # 讀小檔整顆進來
  text = (data_dir / 'config.json').read_text(encoding='utf-8')

  # 確認路徑與建資料夾
  out = Path('output') / '2026' / 'report.csv'
  out.parent.mkdir(parents=True, exist_ok=True)
  ```
  bullets：
  - `glob('*.csv')` 內建 pattern，不用 fnmatch
  - `read_text / write_text` 小檔一行搞定
  - `mkdir(parents=True, exist_ok=True)` 是建資料夾鐵三角
  - 回傳物件可繼續鏈接操作
- 🎙️ 三個最常用 pattern：遍歷、讀入、建目錄。這三樣佔你 90% 的 I/O。

## S5 · CODE — CSV 讀寫
- 🖼️ 滿版 code panel，label「csv.DictReader / DictWriter — 欄位有名有姓」
- 📣 code：
  ```python
  import csv
  from pathlib import Path

  # 讀：每列是 dict，欄位有名字
  with open('orders.csv', encoding='utf-8', newline='') as f:
      reader = csv.DictReader(f)
      for row in reader:
          print(row['order_id'], row['amount'])

  # 寫：先給 header，再一列列寫
  rows = [{'id': 1, 'name': '王小明'}, {'id': 2, 'name': '陳小華'}]
  with open('out.csv', 'w', encoding='utf-8', newline='') as f:
      w = csv.DictWriter(f, fieldnames=['id', 'name'])
      w.writeheader()
      w.writerows(rows)
  ```
  bullets：
  - `newline=''` 必加，否則 Windows 多出空行
  - `DictReader` > `reader`：欄位名不會錯位
  - 中文必設 `encoding='utf-8'`
  - Ch08 Pandas 會包掉，但底層就是這個
- 🎙️ Pandas 很香，但你偶爾會遇到「pandas 讀不進來」的髒檔。那時你回來這張 slide，用純 Python 逐列清。

## S6 · CODE — JSON 讀寫（中文陷阱）
- 🖼️ 滿版 code panel，label「json.load / json.dump — ensure_ascii 的那個坑」
- 📣 code：
  ```python
  import json
  from pathlib import Path

  # 讀
  with open('config.json', encoding='utf-8') as f:
      cfg = json.load(f)           # dict / list

  # 寫：中文要看得見，ensure_ascii=False
  data = {'city': '台北', 'count': 1203}

  json.dumps(data)
  # '{"city": "\\u53f0\\u5317", "count": 1203}'   # 😡 預設跳脫

  json.dumps(data, ensure_ascii=False, indent=2)
  # '{\n  "city": "台北",\n  "count": 1203\n}'    # ✅
  ```
  bullets：
  - `ensure_ascii=False` 幾乎永遠要加
  - `indent=2` 給人看；機器傳輸時省略
  - `json.load(f)` vs `json.loads(s)` 差一個 s
  - JSON 沒有 `date` 型別，日期要自己轉字串
- 🎙️ 第一次寫完 JSON 開啟是一堆 `\u53f0\u5317`，不是你壞、是 default 壞。記住這行：`ensure_ascii=False`。

## S7 · VS-CODE — with 之必要
- 🖼️ 上下兩個 code panel，上 BEFORE（淺灰 label）、下 AFTER（深綠 label）。
- 📣 標題「沒 with vs 有 with：context manager 是 I/O 的止血閥」
  BEFORE code：
  ```python
  f = open('data.csv', encoding='utf-8')
  rows = f.readlines()
  process(rows)            # 如果這裡炸了…
  f.close()                # 這行永遠不會跑
  ```
  bullets：
  - 例外會跳過 close，檔案 handle 洩漏
  - 累積到 ulimit 上限就真的卡死
  - 程式當機後 OS 才幫你收

  AFTER code：
  ```python
  with open('data.csv', encoding='utf-8') as f:
      rows = f.readlines()
      process(rows)        # 這裡炸也沒關係
  # 離開 with 區塊自動 f.close()，不論成功失敗
  ```
  bullets：
  - `__enter__` / `__exit__` 魔術方法保證收尾
  - 等價於隱式 try / finally
  - DB 連線、檔案、lock 全靠它
  - 是 Python「不寫 try 也安全」的主力
- 🎙️ 你還記得 Ch5 的 dunder 嗎？`with` 就在呼叫 `__enter__` / `__exit__`。不寫它，你每一支 script 都在漏資源。

## S8 · IMAGE + CODE — 四段骨架
- 🖼️ 左：try-except-else-finally 流程圖 placeholder（深綠節點 + except 實心）
  右：code panel「完整四段骨架」
- 📣 標題「try / except / else / finally：四段骨架各司其職」
  code：
  ```python
  try:
      data = load('orders.csv')        # 可能炸
  except FileNotFoundError as e:
      logger.warning(f'檔案不存在：{e}')
      data = []
  except ValueError as e:
      logger.error(f'格式錯：{e}')
      raise                            # 重新拋出
  else:
      logger.info(f'成功讀入 {len(data)} 列')   # try 沒炸才跑
  finally:
      close_db()                       # 不論成功失敗都跑
  ```
  bullets：
  - try：把「會炸的那一行」包起來，不要包太廣
  - except：依型別分流，可多個
  - else：try 沒炸才執行 — 區分「讀檔」與「用資料」
  - finally：釋放資源的最後機會
- 🎙️ else 很多人不用，其實它才是高手技。把「讀檔」放 try、「用資料」放 else，錯誤才不會被 except 意外吃掉。

## S9 · MATRIX 2×2 — 四種最常見例外
- 🖼️ 2×2 方陣，每格一種例外型別。
- 📣 標題「四種最常見的例外：90% 資料管線的錯都在這四格」
  cells：
  - `FileNotFoundError`（highlight）— 檔案被搬走 / 使用者打錯路徑\n觸發：`open('not_there.csv')`
  - `KeyError` — dict / JSON 欄位不存在\n觸發：`row['unknown_column']`
  - `ValueError`（highlight）— 型別對、值不合法\n觸發：`int('abc')`、`float('N/A')`
  - `TypeError` — 型別根本錯\n觸發：`'3' + 5`、`len(None)`
- 🎙️ 背起來。這四個是你下一年每天都會遇到的老朋友。指定型別去 except，不要用 bare except 一網打盡。

## S10 · VS-CODE — 反模式
- 🖼️ 上下 code panel。
- 📣 標題「`except Exception: pass` 是反模式：吞錯等於放火」
  BEFORE code：
  ```python
  try:
      data = pd.read_csv(path)
      result = heavy_process(data)
      save_to_db(result)
  except Exception:
      pass              # 什麼都不做，假裝沒事
  ```
  bullets：
  - 連 KeyboardInterrupt 都可能被吞
  - bug 三週後才爆、沒人找得到
  - log 一行都沒留下來
  - 面試會被退件的寫法

  AFTER code：
  ```python
  try:
      data = pd.read_csv(path)
  except FileNotFoundError:
      logger.warning(f'跳過不存在檔案：{path}')
      return None
  except pd.errors.ParserError as e:
      logger.error(f'CSV 格式錯：{path} — {e}')
      raise
  ```
  bullets：
  - 只 catch 你預期會發生的錯
  - 其他錯讓它炸，讓 stack trace 幫你找 bug
  - 每個 except 都要有 log 或 raise
  - 「吞錯」是團隊信用的頭號殺手
- 🎙️ Bare except 不是容錯、是把火吞進肚子。真正的容錯是：我知道這裡可能炸、我知道怎麼處理、我留下證據。

## S11 · CODE — 自訂 Exception（呼應 Ch5）
- 🖼️ 滿版 code panel，label「繼承 Ch5 的 class — 自訂 Exception」
- 📣 code：
  ```python
  class DataValidationError(Exception):
      """資料驗證失敗的語意錯誤"""
      def __init__(self, column: str, reason: str):
          self.column = column
          self.reason = reason
          super().__init__(f'[{column}] {reason}')

  class NegativeAgeError(DataValidationError):
      def __init__(self, value):
          super().__init__('age', f'age 不可為負，收到 {value}')

  # 使用
  if df['age'].min() < 0:
      raise NegativeAgeError(df['age'].min())

  # 上層接
  try:
      validate(df)
  except DataValidationError as e:
      logger.error(f'欄位 {e.column} 驗證失敗：{e.reason}')
  ```
  bullets：
  - Exception 就是普通 class，沿用 Ch5 繼承語法
  - 自訂型別讓 except 可精準分流
  - 多攜帶欄位（column / reason）給 log 抓
  - 子類化再細分：`NegativeAgeError(DataValidationError)`
- 🎙️ Ch5 的繼承今天就派上用場。自訂 Exception 的重點不是炫技，是讓你的管線能用型別分流、讓 log 有結構。

## S12 · CODE — exception chaining
- 🖼️ 滿版 code panel，label「raise ... from e — 保留兇手指紋」
- 📣 code：
  ```python
  class PipelineError(Exception):
      pass

  def load_orders(path):
      try:
          return pd.read_csv(path)
      except FileNotFoundError as e:
          raise PipelineError(f'orders 管線無法啟動：{path}') from e
          #                                                   ^^^^^^
          # 保留原始 traceback；拿掉 from e 就是「重新包裝但藏線索」

  # 錯誤訊息長這樣：
  #   FileNotFoundError: [Errno 2] ... 'orders.csv'
  #   The above exception was the direct cause of the following exception:
  #   PipelineError: orders 管線無法啟動：orders.csv
  ```
  bullets：
  - `raise X from e` → 上下文 traceback 都保留
  - `raise X from None` → 刻意隱藏（少用）
  - 什麼都不寫 → 預設 implicit chain
  - debug 時兩層線索都看得到
- 🎙️ 把底層 error 重新包成業務語意 error 是正確的；但別把原始 traceback 砍掉 — 那是幫未來的自己留證據。

## S13 · ASK — 大檔問題
- 🖼️ 白底大哉問 + data card。
- 📣 Q：「50GB 的 CSV，你 16GB 的 RAM —— 怎麼讀進來？」
  Data card：label「Ch1 OOM 回顧」· stat「3×」· caption「RAM 只夠檔案大小 1/3，直接 `pd.read_csv` 必 OOM」
- 🎙️ Ch1 我們講過 OS 與 RAM 的關係，今天真的遇到了。答案不是買大記憶體，是「分段吃」。

## S14 · IMAGE + CODE — Chunking
- 🖼️ 左：Chunking 記憶體示意圖 placeholder（大檔 vs RAM + sliding window）
  右：code panel「Pandas chunking 實戰」
- 📣 標題「Chunking：把大檔切成 RAM 吃得下的小口」
  code：
  ```python
  import pandas as pd

  total_rows = 0
  total_amount = 0

  for chunk in pd.read_csv('huge_orders.csv',
                            chunksize=100_000,
                            dtype={'amount': 'float32'}):
      chunk = chunk[chunk['status'] == 'paid']
      total_rows += len(chunk)
      total_amount += chunk['amount'].sum()
      # chunk 出了這個區塊就被 GC，RAM 不爆

  print(f'{total_rows:,} 列 / ${total_amount:,.0f}')
  ```
  bullets：
  - `chunksize=100_000` 是 DataFrame iterator
  - 每輪只載 10 萬列，RAM 平穩
  - 常見範圍 10 萬 ~ 100 萬列
  - 做 sum/count 可累加；做 sort 就不行
- 🎙️ Chunking 不是魔法，是 streaming 思維：一次只看一段、處理完就丟。做統計好用，做全域排序不行。

## S15 · CODE — 純 Python 逐行讀
- 🖼️ 滿版 code panel，label「檔案物件天生是 generator（呼應 Ch2）」
- 📣 code：
  ```python
  # 純 Python 逐行 — 適用任何 text 檔、不限 CSV
  total = 0
  with open('huge.log', encoding='utf-8') as f:
      for line in f:                    # 這就是 generator
          if 'ERROR' in line:
              total += 1
  print(total)

  # 對比：錯誤寫法
  with open('huge.log') as f:
      lines = f.readlines()             # 一次載全部 → RAM 爆
      for line in lines: ...

  # 進階：寫成自己的 generator（呼應 Ch2）
  def tail_errors(path):
      with open(path, encoding='utf-8') as f:
          for line in f:
              if 'ERROR' in line:
                  yield line.strip()
  ```
  bullets：
  - `for line in f:` 是懶載入，一行一行讀
  - `readlines()` 是眼殘寫法，RAM 必爆
  - 自製 generator → 可 chain、可 filter、可複用
  - 這就是 Ch2 generator 的生產場景
- 🎙️ 檔案物件本身就是 iterator。你不用做任何事、不用 import 任何東西，`for line in f` 就是 streaming。

## S16 · TABLE — 本章邊界
- 🖼️ 四欄表格：主題 / 是什麼 / 為何本章不教 / 何時學。
- 📣 標題「本章邊界：Linus 原則 — 解決真問題，不炫技」
  rows：
  - Dask / 工業級 parallel DataFrame / 本課程情境 chunking 已夠、學習成本高 / 真的需要跨機器計算時
  - Polars streaming / Rust 寫的高效替代品 / API 與 Pandas 不同、造成學習分岔 / Ch08 後想進階時
  - `asyncio` / `aiofiles` / 非同步 I/O / 資料工程瓶頸多在 CPU、非 I/O 併發 / 寫 web backend 時
  - `pickle` / `struct` / 二進位序列化 / 資料工程現場 95% 用 CSV/JSON/Parquet / 寫框架 / 通訊協定時
  - `contextlib` 自製 with / 自己做 context manager / Ch10 管線會自然碰到 / Ch10 之後
- 🎙️ 三小時學不完所有 I/O；我們學的是「80% 的場景直接可用」。剩下 20% 遇到了再查，基本功夠強就好。

## S17 · PYRAMID — 收束
- 🖼️ thesis_hierarchy 兩區塊（blocks）+ 底部 thesis line。
- 📣 標題「Ch06 收束：進得來 + 擋得住 + 吃得下 = 可上線的 I/O 層」
  block 1「三層骨架」：
  - 進得來：pathlib + with + csv/json 讀寫
  - 擋得住：try/except/else/finally + 自訂 Exception + raise from
  - 吃得下：pd.read_csv chunksize + 檔案 generator 逐行
  block 2「心法」：
  - 只 catch 你預期的錯，其他讓它炸
  - 自訂 Exception 讓 log 有結構（Ch5 繼承再次派上用場）
  - Streaming > batch：能 chunk 就 chunk
  thesis line：「Ch07 進入 NumPy — 資料進得來、擋得住、吃得下之後，我們開始把它算快。」
- 🎙️ 這章的每一樣都不是知識點，是「每個上線的管線都要有的生產工具」。沒有這三層，你下面的 Pandas、NumPy 再強都救不了。
