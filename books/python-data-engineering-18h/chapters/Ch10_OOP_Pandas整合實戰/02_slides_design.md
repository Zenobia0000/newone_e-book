# Ch10 · 02_slides_design — SOP §4.2

- 章節：OOP × Pandas 整合實戰（M4 · 1.5 hr · 17 張內容 · 最終收斂章）
- Governing thought：不是再學一個新 API，是把前九章每一項能力擰成一條可執行、可擴充、可交付的資料管線。
- 配色：黑 + 灰 + 深綠（#1B5E3F）
- 每張格式：🖼️（視覺規格）/ 📣（文字骨架）/ 🎙️（口頭引導）

---

## S1 · SILENT — 開場第一口氣
- 🖼️ 深綠滿版，白字 hero。
- 📣 「這一章不教新語法。\n這一章把你學過的九章，組成一台車。」
- 🎙️ 前面九章像是拆了車所有零件給你看，這一章我們把它組裝起來，讓它跑起來。

## S2 · ASK — 腳本型 vs 管線型
- 🖼️ 白底，大哉問 + 右下 data card。
- 📣 Q：「如果今天就被要求交出一個『可以跑』的資料管線，你會從 import pandas 開始，還是從 class 開始？」
  Data card：label「2025 業界 Code Review 觀察」· stat「2 種」· caption「『腳本型』30 行搞定，『管線型』可重用可擴充 — 新人與資深的分水嶺就這一題」
- 🎙️ 這不是對錯題 — 30 行腳本不需要 class，300 行沒有 class 你會崩潰。今天我們學的是判斷的時機。

## S3 · MATRIX 2×2 — 狀態 vs 動作
- 🖼️ 2×2 方陣。
- 📣 標題「狀態 vs 動作：DataCleaner 的職責拆分」
  cells：
  - 狀態（Instance Attribute，highlight）— `self.path`、`self.df`：整個物件生命週期裡都在的東西
  - 動作（Method，highlight）— `validate / clean / apply / eda / export`：做完就回傳 self
  - 可鏈式（return self）— 鏈式方法全回傳 self，最後一呼必執行
  - 應 raise（DataValidationError）— 錯資料不吞、不 print，走例外語意
- 🎙️ OOP 第一個問題永遠不是「要繼承誰」，是「這個物件有什麼狀態、會做什麼動作」。

## S4 · IMAGE + CODE — DataCleaner 介面草圖
- 🖼️ 左：DataCleaner 類別結構圖 placeholder；右：介面 code。
- 📣 code：
  ```
  class DataCleaner:
      def __init__(self, data_path: str): ...
      def validate(self) -> 'DataCleaner': ...
      def clean_missing_values(self, strategy: str = 'drop') -> 'DataCleaner': ...
      def apply_custom_transform(self, column: str, func) -> 'DataCleaner': ...
      def generate_eda_report(self, out_path: str) -> 'DataCleaner': ...
      def export_data(self, out_path: str) -> 'DataCleaner': ...
  ```
  bullets：每個方法的回傳型別都是 'DataCleaner'、看型別就知道能接、命名用動詞而非名詞、型別註解是未來你自己的文件。
- 🎙️ 這張草圖寫完其實類別就寫完一半了 — 寫 code 之前先寫介面，是資深工程師的肌肉記憶。

## S5 · CODE — 自訂 Exception（呼應 Ch6）
- 🖼️ 滿版 code panel。
- 📣 code：`DataValidationError(Exception)`，存 `column` + `reason` 兩個屬性，`__init__` 呼叫 super。
  bullets：不要 raise Exception 的泛型、不要 print 再 return、Exception 帶結構化資料、try/except 上游能精準攔截。
- 🎙️ Ch6 教你「錯就 raise」，這裡是它的成年禮 — 一個專案一定要有一套自訂例外。

## S6 · SILENT — 介面優先
- 🖼️ 深綠滿版。
- 📣 「好介面的特徵：\n看名字就知道能做什麼、看型別就知道能怎麼串。」
- 🎙️ 介面寫對了，裡面的實作怎麼重構都不會害到使用者。

## S7 · CODE — __init__（呼應 Ch4 + Ch6）
- 🖼️ 滿版 code panel。
- 📣 code：用 `Path` 檢查檔案存在、不存在 raise `FileNotFoundError`、讀 CSV 後 `print(shape)`。
  bullets：fail fast 原則、pathlib 取代 os.path、`self.df` = 狀態、建構子就讀檔、除非非常必要才懶載入。
- 🎙️ 這四行是 OOP 的精神縮影 — 物件一誕生，狀態就得是正確的。

## S8 · CODE — validate（呼應 Ch6）
- 🖼️ 滿版 code panel。
- 📣 code：檢查 `df.empty` → raise；檢查 `revenue < 0` → raise；最後 `return self`。
  bullets：驗證是一個動作、不是副作用；raise 帶欄名 + 理由；return self 開啟鏈式；這就是 Ch6 自訂 Exception 的真實場景。
- 🎙️ validate 是一條紅線 — 過了就能繼續、沒過就炸給上游。絕對不能偷偷改資料。

## S9 · CODE — clean_missing_values（呼應 Ch8）
- 🖼️ 滿版 code panel。
- 📣 code：`strategy='drop'` → dropna；`strategy='mean'` → fillna(mean)；其他策略容易擴充；return self。
  bullets：策略以字串參數化而非 if 樹層疊、mean 只對數值欄、Ch8 的四種策略都可以擴進來、呼叫方一句話切換行為。
- 🎙️ 策略模式的 poor man's version — 用字串派發通常夠用，真的複雜了再考慮 Strategy Pattern。

## S10 · CODE — apply_custom_transform（呼應 Ch3 + Ch8）
- 🖼️ 滿版 code panel。
- 📣 code：檢查欄位存在 → raise `DataValidationError`；新增 `{column}_transformed` 欄位；`self.df[column].apply(func)`；return self。
  bullets：func 是 first-class citizen（Ch3）、lambda 在這裡找到主場（Ch8）、新增欄而非覆寫（可追溯）、失敗用自訂 Exception 而不是 KeyError。
- 🎙️ Ch3 教 lambda、Ch8 教 apply，這裡它們終於同台 — 你設計的類別，讓使用者傳任意函式就能擴充。

## S11 · IMAGE + CODE — generate_eda_report（呼應 Ch9）
- 🖼️ 左：Method Chaining 視覺化 placeholder；右：EDA code。
- 📣 code：`select_dtypes('number')` → `plt.subplots(2,2)` → 每欄 hist → `tight_layout` → `savefig` → `plt.close`；return self。
  bullets：把 Matplotlib 包進類別、關圖是禮貌（防記憶體洩漏）、Ch9 探索性視覺化的 4-subplot 骨架、回傳 self 讓下游繼續串。
- 🎙️ Ch9 畫圖時我們是手動敲、手動存；這裡它變成管線的一環，呼叫方一行就拿到報表。

## S12 · CODE — export_data + 完整鏈（呼應 Ch5）
- 🖼️ 滿版 code panel。
- 📣 code：
  ```
  (DataCleaner('raw.csv')
      .validate()
      .clean_missing_values(strategy='mean')
      .apply_custom_transform('revenue', lambda x: x*1.05)
      .generate_eda_report('report.png')
      .export_data('clean.csv'))
  ```
  bullets：括號包起來、一個動作一行、每行一看就知道在做什麼、Ch5 魔術方法 + return self 的實踐、比流程圖還清楚的文件。
- 🎙️ 看這段 code 你應該懂為什麼 Ch5 花時間講 return self — 這就是回報你的時刻。

## S13 · TABLE — 可改進方向
- 🖼️ Editorial table，3 欄。
- 📣 標題「可改進方向：logging / from_config / 單元測試（作業指引）」
  header：改進方向 / 為什麼 / 下一步 API
  rows：
  - 加入 logging / print 不能關、logging 有等級 / `import logging` + `logger = logging.getLogger(__name__)`
  - 從 config 載入 / 參數寫死就不可重用 / `@classmethod from_config(cls, path)`
  - 單元測試 / return self 很好測 / `pytest` + `tmp_path` fixture
  - 切出 Strategy Pattern / 策略太多時 if 會爆 / `CleanStrategy` 抽象類別
- 🎙️ 這張表就是期末作業的改進清單 — 做兩個以上交出來，你的 GitHub 就有一個亮點。

## S14 · PYRAMID — 18 小時能力盤點
- 🖼️ 五層 pyramid（由下而上）。
- 📣 標題「18 小時能力盤點」
  blocks：
  - 五層（底→頂）：
    - 系統直覺（OS/RAM/I/O） — Ch1
    - Python 進階（Generator/Lambda/Comprehension/自訂函式） — Ch2–Ch3
    - OOP（類別、繼承、魔術方法、Method Chaining） — Ch4–Ch5
    - 資料工程（I/O、Exception、NumPy、Pandas） — Ch6–Ch8
    - 視覺化與整合（Matplotlib、OOP×Pandas） — Ch9–Ch10
  - thesis：「底層越穩、上層越能長；今天你能寫 DataCleaner，是因為前四層都穩了。」
- 🎙️ 這五層不是平行的，是堆疊的 — 少一層，上面就不穩。這是為什麼我們花時間在 Ch1 講 OS 與 I/O。

## S15 · IMAGE + TABLE — 五條學習路徑
- 🖼️ 上：五條學習路徑生態圖 placeholder；下：對應 editorial table。
- 📣 table：
  header：方向 / 推薦起點 / 一句話
  rows：
  - 資料庫整合 / SQL × Python（SQLAlchemy） / 把 CSV 換成資料庫
  - 機器學習 / scikit-learn 入門 / 把清洗好的資料餵給模型
  - 大規模資料 / Polars、DuckDB / 當 Pandas 變慢時的下一站
  - 自動化排程 / Airflow / Prefect / n8n / 讓你的管線每天自動跑
  - 雲端部署 / AWS S3+Lambda、GCP BigQuery / 把腳本搬上雲
- 🎙️ 這五條路線不是選擇題，是地圖 — 看你下一份工作的需求排優先序。

## S16 · VS-LIST — Linus 三句忠告
- 🖼️ 兩欄：左為「常見迷思」、右為「Linus 式紀律」。
- 📣 標題「Linus 三句結業忠告：給三個月後的自己」
  左欄（常見迷思）：
  - 「跑得起來就好」
  - 「先寫再說、能 work 就優化」
  - 「什麼都 OOP 最優雅」
  右欄（Linus 式紀律）：
  - 跑得起來不算數，能讓三個月後的自己看懂才算數
  - 最強的優化是「不要做」—— 在向量化之前，先想能不能跳過這步
  - OOP 不是萬靈丹，30 行的腳本不需要類別
  summary：寫 code 是寫給未來的自己 — 好品味先於聰明。
- 🎙️ 這三句貼在你之後每個專案的 README 都合適 — 實用主義不是口號。

## S17 · SILENT — 結業
- 🖼️ 深綠滿版，白字 hero。
- 📣 「18 小時結束了。\n從現在起，程式碼是寫給三個月後的自己看的。」
- 🎙️ 謝謝你陪到最後 — 下一站見。
