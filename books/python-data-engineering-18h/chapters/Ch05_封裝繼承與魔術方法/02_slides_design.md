# Ch05 · 02_slides_design — SOP §4.2

- 章節：封裝、繼承與魔術方法（M2 · 1.5 hr · 18 張內容）
- Governing thought：類別不是把變數塞在一起，而是用封裝守門、繼承分工、魔術方法讓它像 Python 內建型別一樣自然。
- 配色：黑 + 灰 + 深綠（#1B5E3F）
- 每張格式：🖼️（視覺規格）/ 📣（文字骨架）/ 🎙️（口頭引導）

---

## S1 · SILENT — 封面後第一口氣
- 🖼️ 深綠滿版，白字 hero。
- 📣 「類別要守門，\n不是把變數塞在一起。」
- 🎙️ Ch04 我們學會定義類別，今天要讓它變「可靠」。Ch05 不是把類別寫得更長，是把它寫得更不容易壞。

## S2 · ASK — Socratic 開場
- 🖼️ 白底，大哉問 + 右下 data card。
- 📣 Q：「為什麼資深工程師的 class 很少直接 obj.field = 改值？」
  Data card：label「大型專案 code review 慣例」· stat「92%」· caption「『直接改內部欄位』是第一名被退回原因」
- 🎙️ 不是不能改，是改了沒人知道誰改的、什麼時候改的。封裝是「給未來的自己留線索」。

## S3 · MATRIX 2×3 — 封裝三道門全景
- 🖼️ 2×3 方陣，左欄三種寫法、右欄三個語意。
- 📣 標題「封裝的三道門：從禮貌提醒到改名防呆」
  cells：
  - `x`（public，highlight）— 任何人都能讀寫，約定：外部介面
  - `_x`（弱封裝）— 單底線禮貌提醒，Python 不阻止你
  - `__x`（強封裝）— 雙底線 name mangling，實際改名為 `_Class__x`
  - `@property`（計算屬性，highlight）— 對外是欄位，對內是方法
  - `@x.setter`（可控寫入）— getter 成對出現，用來驗證值
  - `Python 沒有 private`（真相）— 一切靠慣例 + 工具，不是語法
- 🎙️ 三道門的差別不是「誰更安全」，是「你想給使用者看多少」。

## S4 · CODE — `_x` 與 `__x` 實測
- 🖼️ 滿版 code panel，標題 label「單底線 vs 雙底線 — name mangling 現場」
- 📣 code：
  ```
  class Account:
      def __init__(self, balance):
          self._hint     = balance   # 禮貌提醒
          self.__secret  = balance   # 真的改名

  a = Account(100)
  a._hint         # OK，Python 不阻止
  a.__secret      # AttributeError
  a._Account__secret  # 仍可拿到，只是改名了
  ```
  bullets：
  - `_x` 只是約定，linter 會警告
  - `__x` 被改寫成 `_ClassName__x`
  - 本意是「避免子類別意外覆蓋」，不是加密
- 🎙️ 雙底線不是保險箱，是把鑰匙藏在有名字的抽屜裡。

## S5 · CODE — @property 的真實用途
- 🖼️ 滿版 code panel，單一範例。
- 📣 code：溫度類 Celsius → Fahrenheit
  ```
  class Temperature:
      def __init__(self, c):
          self._celsius = c

      @property
      def celsius(self):
          return self._celsius

      @celsius.setter
      def celsius(self, value):
          if value < -273.15:
              raise ValueError("below absolute zero")
          self._celsius = value

      @property
      def fahrenheit(self):
          return self._celsius * 9 / 5 + 32
  ```
  bullets：
  - 對外：`t.celsius = 25`、`t.fahrenheit`
  - 對內：可驗證、可計算、可換實作
  - 寫法像欄位，實際是方法 — 這是關鍵
- 🎙️ 重點不是用了 decorator，是：未來能換實作而不動呼叫端。

## S6 · VS-CODE — 直接存取 vs @property
- 🖼️ 上下兩 code panel（BEFORE / AFTER 結構）。
- 📣
  - BEFORE（label_dark=False，label「BEFORE：公開欄位 — 改動要改全世界」）
    ```
    class Order:
        def __init__(self, price):
            self.price = price    # 直接公開

    o = Order(100)
    o.price = -50   # 合理嗎？沒人擋
    ```
    bullets：
    - 外部四處在寫 `o.price = ...`
    - 要加驗證就要回頭改每一處
  - AFTER（label_dark=True，label「AFTER：@property — 介面不動，內部隨便換」）
    ```
    class Order:
        def __init__(self, price):
            self.price = price    # 觸發 setter

        @property
        def price(self): return self._price

        @price.setter
        def price(self, v):
            if v < 0: raise ValueError
            self._price = v
    ```
    bullets：
    - 外部程式碼「完全不用改」
    - 驗證、log、cache 都能偷偷加
    - 這就是 Open/Closed 原則的 Python 版
- 🎙️ 一條分界線：公開欄位是合約，@property 是服務台。服務台可以換內部流程，櫃台接待不變。

## S7 · ASK — 繼承的觸發場景
- 🖼️ 白底大問，右下 data card。
- 📣 Q：「如果要支援 CSV / JSON / Parquet 三種來源，\n你要寫三個獨立類別，還是一個家族？」
  Data card：label「重複邏輯的比例」· stat「70%」· caption「讀檔 → 檢查 → 回傳 DataFrame\n70% 步驟相同」
- 🎙️ 繼承不是為了看起來很 OO，是為了：相同邏輯寫一次、不同邏輯各自覆寫。

## S8 · IMAGE + CODE — 繼承樹 + 家族範例
- 🖼️ 左：image placeholder（DataReader 繼承樹），右：code panel。
- 📣 左側 slot「DataReader 繼承樹圖」，placeholder_id `Ch05_S08_inheritance_tree`
  右側 code：
  ```
  class DataReader:
      def read(self, path): raise NotImplementedError

  class CSVReader(DataReader):
      def read(self, path):
          return pd.read_csv(path)

  class JSONReader(DataReader):
      def read(self, path):
          return pd.read_json(path)
  ```
  bullets：
  - 基類定介面（合約）
  - 子類負責實作
  - 共用邏輯（log / 檢查）寫在基類
- 🎙️ 樹的根是「共同點」，樹的葉是「差異點」。對的繼承，差異最小化。

## S9 · CODE — super() 與 override
- 🖼️ 滿版 code panel。
- 📣 code：
  ```
  class DataReader:
      def __init__(self, encoding="utf-8"):
          self.encoding = encoding
          self.rows_read = 0

      def read(self, path):
          raise NotImplementedError

  class CSVReader(DataReader):
      def __init__(self, encoding="utf-8", sep=","):
          super().__init__(encoding)   # 呼叫父類別建構
          self.sep = sep

      def read(self, path):            # 覆寫
          df = pd.read_csv(path, sep=self.sep, encoding=self.encoding)
          self.rows_read = len(df)
          return df
  ```
  bullets：
  - `super().__init__()` 必做，否則父類別屬性沒設
  - override = 同名重寫，簽章可延伸
  - 子類別可用 `self.encoding` 讀父類屬性
- 🎙️ 看到 super() 就想「先做父親那份」。漏掉它，bug 通常兩個月後才爆。

## S10 · TABLE — 本課程的邊界
- 🖼️ Editorial table，四欄：主題 / 是什麼 / 為何進階 / 何時學
- 📣
  | 主題 | 是什麼 | 為何本章不教 | 何時學 |
  | 多重繼承 | class C(A, B) | 容易形成菱形歧義、工業級代碼很少用 | 用到時再查 MRO |
  | MRO（C3 線性化） | Python 決定呼叫順序的演算法 | 單一繼承用不到 | debug 多重繼承時 |
  | 抽象基類 ABC | abc.ABCMeta / @abstractmethod | 強制介面，但 duck typing 通常夠 | 寫框架才需要 |
  | Mixin | 只給方法、不繼承狀態 | 是多重繼承的節制用法 | Ch10 進階版可接觸 |
- 🎙️ Linus 原則：解決實際問題，不是炫技。本章守住單一繼承，已經能覆蓋資料工程 90% 需求。

## S11 · MATRIX 2×2 — 繼承 vs 組合
- 🖼️ 2×2 方陣，兩軸：「行為 vs 資料」×「IS-A vs HAS-A」
- 📣 標題「繼承是 IS-A，組合是 HAS-A — 先問關係，再選工具」
  cells：
  - 繼承 · IS-A（highlight）— CSVReader is a DataReader ✓
  - 繼承 · HAS-A ✗ — Order 不 is a List，即使它「裝了」items
  - 組合 · HAS-A（highlight）— Cleaner has a Logger ✓
  - 組合 · 靠注入 — 傳進去就能換，比繼承靈活
- 🎙️ 實務鐵則：能用組合不用繼承。這會在 Ch10 DataCleaner 再被驗證一次。

## S12 · MATRIX 2×2 — 魔術方法四件套
- 🖼️ 2×2 方陣。
- 📣 標題「魔術方法：Python 幫你自動呼叫的那些 dunder」
  cells：
  - `__str__`（highlight）— `print(obj)` / `str(obj)` 時呼叫 · 給人看
  - `__repr__` — REPL 顯示 / `repr(obj)` · 給開發者看，最好可重建
  - `__len__`（highlight）— `len(obj)` · 長度有意義才實作
  - `__iter__` — `for x in obj` · 讓物件可被迭代
- 🎙️ 四件套不是裝飾品，是「讓你的類別說 Python 的母語」。

## S13 · CODE — __str__ vs __repr__
- 🖼️ 滿版 code panel。
- 📣 code：
  ```
  class Order:
      def __init__(self, id_, amount):
          self.id, self.amount = id_, amount

      def __repr__(self):
          return f"Order(id_={self.id!r}, amount={self.amount!r})"

      def __str__(self):
          return f"訂單 #{self.id}：NT$ {self.amount:,}"

  o = Order("A01", 12800)
  print(o)        # 訂單 #A01：NT$ 12,800
  repr(o)         # "Order(id_='A01', amount=12800)"
  ```
  bullets：
  - `__str__` 給終端使用者 / log
  - `__repr__` 給開發者 debug — 能反向重建最好
  - 沒定義 `__str__` 時，`print` 會退而求其次用 `__repr__`
- 🎙️ 口訣：repr 要能貼回 Python 重跑，str 要讓人看得懂。

## S14 · CODE — __len__ 與 __iter__
- 🖼️ 滿版 code panel。
- 📣 code：
  ```
  class DataPipeline:
      def __init__(self):
          self._steps = []

      def add(self, step):
          self._steps.append(step)
          return self               # 預告 Method Chaining

      def __len__(self):
          return len(self._steps)

      def __iter__(self):
          return iter(self._steps)

  pipe = DataPipeline()
  pipe.add(clean).add(normalize).add(export)
  len(pipe)        # 3
  for s in pipe: ...  # 自動逐步跑
  ```
  bullets：
  - 有「數量感」才實作 `__len__`
  - 有「逐一處理」才實作 `__iter__`
  - 兩者通常成對 — 集合類概念的必備配件
- 🎙️ 這張已經鋪兩張後路：Ch10 DataCleaner 的 chaining，和馬上要講的魔術方法 debug。

## S15 · VS-CODE — 加上魔術方法前後
- 🖼️ 上下兩 code panel。
- 📣
  - BEFORE（label「BEFORE：print 出來是一串記憶體位址」）
    ```
    pipe = DataPipeline()
    print(pipe)
    # <__main__.DataPipeline object at 0x7f8e1c2a4d90>
    ```
    bullets：
    - debug 看不懂在看什麼
    - code review 要多寫 print 拆解
  - AFTER（label「AFTER：print 直接講人話」）
    ```
    def __str__(self):
        return f"DataPipeline({len(self)} 步)：{' → '.join(s.__name__ for s in self._steps)}"

    print(pipe)
    # DataPipeline(3 步)：clean → normalize → export
    ```
    bullets：
    - log 自帶語意，不用再拆
    - 錯誤訊息變自我說明
    - 每多寫 5 分鐘，省未來 50 次 debug
- 🎙️ 不是為了好看，是為了 3 個月後的自己還看得懂。

## S16 · IMAGE + CODE — Method Chaining 流程圖
- 🖼️ 左：image placeholder（chaining flow），右：code panel。
- 📣 左側 slot「Method Chaining 流程圖」，placeholder_id `Ch05_S16_chaining_flow`
  右側 code：
  ```
  class DataCleaner:
      def __init__(self, df):
          self.df = df

      def drop_na(self):
          self.df = self.df.dropna()
          return self

      def normalize(self, cols):
          self.df[cols] = (self.df[cols] - self.df[cols].mean()) / self.df[cols].std()
          return self

      def export(self, path):
          self.df.to_csv(path, index=False)
          return self

  (DataCleaner(df)
      .drop_na()
      .normalize(["price"])
      .export("out.csv"))
  ```
  bullets：
  - 每個方法 `return self`
  - 讀起來像句子：資料 → 去空 → 標準化 → 匯出
  - 這就是 Ch10 DataCleaner 的骨架
- 🎙️ 為什麼這種寫法流行？因為資料處理天生就是一條流水線。用 chaining 寫，程式結構 = 資料流結構。

## S17 · CODE — 封裝 + 繼承 + Chaining 合體雛形
- 🖼️ 滿版 code panel。
- 📣 label「Ch05 合體預告 — 三根柱子一起出場」
  ```
  class BaseCleaner:
      def __init__(self, df):
          self._df = df              # 封裝：底線提示不要外部改

      @property
      def shape(self):               # property：暴露計算屬性
          return self._df.shape

      def __len__(self):             # 魔術方法：len() 回傳列數
          return len(self._df)

      def drop_na(self):
          self._df = self._df.dropna()
          return self                # Chaining

  class PriceCleaner(BaseCleaner):   # 繼承 + override
      def drop_na(self):
          super().drop_na()
          self._df = self._df[self._df["price"] > 0]
          return self
  ```
  bullets：
  - 封裝：`_df` 禮貌提醒 + `@property` 暴露形狀
  - 繼承：`PriceCleaner` 擴充基類
  - 魔術方法：`len(cleaner)` 直接可用
  - Chaining：每個動作 return self
- 🎙️ 這就是 Ch10 DataCleaner 的前身。你離做出「自己的 pandas pipeline」只差 5 章。

## S18 · PYRAMID — Ch05 收束
- 🖼️ draw_thesis_hierarchy 雙欄。
- 📣 標題「Ch05 收束：守門 + 分工 + 自然 = 可長可久的類別」
  block 1「三根柱子」：
  - 封裝：`_x` / `__x` / `@property` — 誰能改、怎麼改
  - 繼承：super + override — 共用邏輯上移、差異下放
  - 魔術方法：`__str__` / `__repr__` / `__len__` / `__iter__` — 與 Python 內建整合
  block 2「設計紀律」：
  - 能用組合不用繼承
  - 單一繼承已夠，多重繼承是最後手段
  - 方法鏈要一路 return self，才不破壞
  thesis：「Ch06 進入 M3 數據工程：I/O 與例外 — 並會用本章的繼承寫自己的 Exception。」
