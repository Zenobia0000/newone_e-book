# M2：OOP 與程式抽象 — 從腳本到可維護系統

> **課程定位**：第 2 模組，共 24 小時課程中的第 4–6 小時
> **前置模組**：M1 Python 語言基礎與資料型別
> **後接模組**：M3 NumPy 數值計算基礎
> **建議學習時數**：3 小時（含 2 次工作坊練習）

---

## 模組定位說明

學生完成 M1 後，手上有了 for loop、function、list/dict 這些工具，可以寫出可以跑的腳本。但腳本不等於系統。當資料管線變複雜、API wrapper 需要維護狀態、模型訓練需要重複使用邏輯、Chatbot 需要記憶對話歷史，線性腳本就會垮掉。

這個模組的存在理由只有一個：**讓學生理解「把資料和行為綁在一起」是什麼意思，以及為什麼這樣組織程式碼，系統才能活得久。**

本模組不教設計模式，不談 SOLID 原則，只教生產環境真正用到的最小 OOP 核心：class、object、attribute、method、encapsulation、inheritance vs composition，以及程式碼如何從一個 .py 檔長成一個 package。

---

## 模組學習目標

完成本模組後，學生能夠：

1. 說清楚 class 與 object 的關係，不再把兩者混淆
2. 寫出具有 `__init__`、instance method、property 的 class
3. 解釋 encapsulation 的用途，並用 `_` 前綴慣例保護內部狀態
4. 判斷一個問題應該用 inheritance 還是 composition 解決
5. 把一個超過 100 行的腳本拆成 module，再組成 package
6. 閱讀 scikit-learn、pandas、LangChain 等函式庫的 class API，理解其設計意圖

---

## 關鍵概念清單

| 概念 | 一句話定義 | AI 應用對應 |
|------|-----------|-------------|
| `class` | 把資料（狀態）與行為（函數）打包成一個模板 | `ModelTrainer`、`FeaturePipeline` |
| `object` | class 的具體實例，佔用記憶體、有自己的狀態 | 每個 `trainer = ModelTrainer(...)` 都是獨立個體 |
| `attribute` | object 的狀態，用 `self.x` 存取 | `self.model_path`、`self.history` |
| `method` | object 的行為，是屬於這個 class 的函數 | `trainer.fit()`、`pipeline.transform()` |
| `encapsulation` | 把內部狀態藏起來，外部只能透過公開介面操作 | 保護 `_weights` 不被外部直接改壞 |
| `inheritance` | 子類別繼承父類別的介面與實作 | `BaseLoader -> CSVLoader` |
| `composition` | 把其他物件當作 attribute 嵌入，組合行為 | `ChatAgent` 內嵌 `VectorStoreClient` |
| `module` | 一個 `.py` 檔就是一個 module | `from dataset import Dataset` |
| `package` | 含有 `__init__.py` 的資料夾，是 module 的集合 | `from myproject.data import Dataset` |

---

## 投影片大綱（12 張）

| # | 標題 | 核心訊息 | 預計時長 |
|---|------|---------|---------|
| 1 | 腳本為什麼會垮掉 | 線性腳本的上限在哪裡 | 10 min |
| 2 | 從函數到物件：一個比喻 | class 是資料的合約，不是技術炫技 | 10 min |
| 3 | class 的最小可用語法 | `__init__`、`self`、attribute、method | 15 min |
| 4 | object 是什麼：記憶體與狀態 | 每個 instance 有自己的狀態 | 10 min |
| 5 | Encapsulation：邊界與信任 | `_` 慣例與保護內部狀態 | 10 min |
| 6 | 工作坊 1：Dataset 類別 | 動手寫第一個有意義的 class | 25 min |
| 7 | Inheritance vs Composition | 繼承不是唯一的重用方式 | 15 min |
| 8 | 腳本的進化路徑 | notebook -> script -> module -> package -> service | 10 min |
| 9 | Module 與 Package 實作 | `import` 機制、`__init__.py`、相對匯入 | 15 min |
| 10 | AI 工程中的 OOP 全景 | 真實專案裡這些 class 長什麼樣 | 15 min |
| 11 | 工作坊 2：拆解腳本成 Package | 把 200 行腳本重組成三個 module | 30 min |
| 12 | 模組總結與銜接 | 這些技能在 M3 之後如何被用到 | 5 min |

---

## 投影片詳細內容

---

### Slide 1 — 腳本為什麼會垮掉

**核心訊息**：線性腳本解決小問題，但一旦邏輯複雜化，它沒有任何機制阻止你把一切寫成一堆全域變數和相互依賴的函數。

**講師說明要點**：

- 展示一個 150 行的資料分析腳本：全域變數 `df`、`model`、`results` 混在一起，沒有任何隔離
- 問學生：如果你的同事要在這個腳本上加一個功能，他要怎麼知道哪些變數是安全的？
- 點出「可以跑」和「可以維護」是兩件事，面試可能考前者，工作只看後者
- 說明生產環境三個痛點：(1) 邏輯分散、(2) 狀態難追蹤、(3) 測試幾乎不可能
- 預告：OOP 不是讓程式更聰明，而是讓程式更可預測

**視覺建議**：左欄放 150 行腳本截圖（模糊化），右欄放三個紅色警示框標示問題區域。底部一行大字：「可以跑 ≠ 可以維護」。

**轉場**：「要解決這個問題，我們需要一種新的思維方式——把資料和操作它的函數，放在同一個地方。」

---

### Slide 2 — 從函數到物件：一個比喻

**核心訊息**：class 是一份合約，它說清楚這個東西有什麼資料、能做什麼事。

**講師說明要點**：

- 用「一個資料集」做比喻：資料集有路徑、有欄位、有筆數；資料集能被載入、能被清理、能被切割
- 提問：如果你用函數做，你要傳多少參數進去？每次都要記住 `df`、`file_path`、`schema` 是怎麼來的
- 用 class 的話，這些全都住在物件裡面，函數不需要從外部拿這些東西，因為它自己就有
- 強調：class 不是 Java 那種刻板印象。Python 的 class 很輕，你不需要為每個小東西都寫 class
- 黃金標準：當一組資料和一組函數總是一起出現，就是該包成 class 的訊號

**視覺建議**：兩欄對比。左欄：五個散落的函數和三個全域變數，用箭頭畫出混亂的依賴關係。右欄：一個方框代表 `Dataset` class，內部清楚標示 attributes 和 methods。

**轉場**：「概念講完了，直接看語法。Python 的 class 比你想的還要直白。」

---

### Slide 3 — Class 的最小可用語法

**核心訊息**：`__init__` 是物件出生的地方，`self` 是物件對自己的稱呼，其他的都是附加的。

**講師說明要點**：

- 現場 live code 一個最小的 `Dataset` class，只有 `__init__` 和一個 `load` method
- 解釋 `__init__` 不是建構子，是初始化方法，物件已經建好了，`__init__` 只是設定初始狀態
- 解釋 `self`：每個 method 的第一個參數都是 `self`，代表「這個物件自己」，不是魔法，是慣例
- 說明 attribute 的兩種存活區域：instance attribute（每個物件各自擁有）vs class attribute（所有物件共享）
- 展示用 `dir()` 和 `__dict__` 觀察一個物件的內容

```python
class Dataset:
    # class attribute: 所有 Dataset 共享
    supported_formats = ["csv", "parquet", "json"]

    def __init__(self, file_path: str):
        # instance attributes: 每個 Dataset 獨立擁有
        self.file_path = file_path
        self._data = None        # 用 _ 表示內部狀態
        self.is_loaded = False

    def load(self):
        import pandas as pd
        self._data = pd.read_csv(self.file_path)
        self.is_loaded = True
        return self

    def shape(self):
        if not self.is_loaded:
            raise RuntimeError("Dataset not loaded. Call load() first.")
        return self._data.shape
```

**視覺建議**：程式碼高亮，用顏色分別標示：`__init__`（藍色）、`self`（橘色）、instance attribute（綠色）、class attribute（紫色）。旁邊加三個小標籤解釋每個顏色的含義。

**轉場**：「你已經知道怎麼寫 class 了。但 class 和 object 是不同的東西，我們來看看物件是什麼。」

---

### Slide 4 — Object 是什麼：記憶體與狀態

**核心訊息**：每個 object 是 class 的一個獨立複製，有自己的記憶體空間和自己的狀態，彼此不干擾。

**講師說明要點**：

- 用 `id()` 展示兩個 `Dataset` instance 的記憶體位址不同
- 展示修改一個 instance 的 attribute，另一個不受影響
- 解釋這和函數的差別：函數沒有「記憶」，每次呼叫都是重新開始；object 有狀態，它記得之前發生了什麼
- 用 Chatbot 的例子說明狀態的重要性：對話歷史必須住在某個地方，放全域變數很脆弱，放在 `ChatAgent` 物件的 `self.history` 裡才合理
- 簡單提示 `__repr__` 讓 object 的印出結果更可讀

```python
# 兩個獨立的 Dataset 物件，各自有自己的狀態
ds1 = Dataset("train.csv")
ds2 = Dataset("test.csv")

ds1.load()

print(ds1.is_loaded)  # True
print(ds2.is_loaded)  # False — 彼此完全獨立
print(id(ds1) == id(ds2))  # False — 不同的記憶體位址
```

**視覺建議**：記憶體示意圖，兩個方框代表 `ds1` 和 `ds2`，各自內部顯示自己的 attribute 值，用虛線框框住 `Dataset` class 模板放在上方，兩個箭頭從模板指向各自的 instance。

**轉場**：「現在你知道狀態住在哪裡了。下一步是學會保護它——因為不是所有外部程式碼都應該直接碰你的內部狀態。」

---

### Slide 5 — Encapsulation：邊界與信任

**核心訊息**：Encapsulation 不是把東西藏起來，而是畫清楚邊界：什麼是公開介面，什麼是實作細節。

**講師說明要點**：

- 解釋 Python 用 `_` 前綴表示「內部使用，外部不要直接碰」，這是慣例不是強制
- 解釋 `__` 前綴（name mangling）：真正的阻擋機制，但實務上很少用，`_` 就夠了
- 用 `@property` 展示如何讓外部用 attribute 語法，但背後執行驗證邏輯
- 核心論點：如果你讓外部直接改 `self._data`，你就失去了控制。日後改內部實作，所有外部程式碼都可能崩
- AI 應用舉例：`ModelTrainer._weights` 不應該被外部直接覆寫，應該只能透過 `trainer.load_weights(path)` 來更新

```python
class Dataset:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._data = None        # 外部不應直接存取

    @property
    def data(self):
        """公開介面：只允許讀取，不允許外部直接賦值"""
        if self._data is None:
            raise RuntimeError("Dataset not loaded yet.")
        return self._data

    @property
    def num_rows(self):
        return len(self._data) if self._data is not None else 0
```

**視覺建議**：一個方框代表 class，中間畫一條虛線分成兩層：上層標「Public Interface」（綠色）列出公開 methods 和 properties；下層標「Internal State」（紅色）列出 `_` 前綴的 attributes。外部程式碼只能碰上層。

**轉場**：「理論說夠了。現在你們自己動手，寫一個 Dataset class，我們看看它在真實情境下能做什麼。」

---

### Slide 6 — 工作坊 1：Dataset 類別（25 分鐘）

**核心訊息**：把一個資料載入的線性腳本，重構成一個有邊界的 `Dataset` class。

**練習規格**：

學生從以下線性腳本開始：

```python
# 起始腳本：線性版本
import pandas as pd

file_path = "titanic.csv"
df = pd.read_csv(file_path)
df = df.dropna(subset=["Age", "Fare"])
df["FareLog"] = df["Fare"].apply(lambda x: x ** 0.5)
num_rows = len(df)
columns = list(df.columns)

print(f"Loaded {num_rows} rows with columns: {columns}")
```

**任務要求（三個關卡）**：

**關卡 1（10 分鐘）**：寫一個 `Dataset` class，包含：
- `__init__(self, file_path: str)`
- `load(self)` — 讀取 CSV
- `clean(self, required_cols: list)` — 移除含有 NaN 的列
- `num_rows` property — 回傳目前列數

**關卡 2（8 分鐘）**：加入 `add_feature(self, col_name: str, transform_fn)` method，讓特徵工程可以被鏈式呼叫（回傳 `self`）。

**關卡 3（7 分鐘）**：寫一個 `__repr__` 讓 `print(ds)` 輸出有意義的資訊，並用 `_` 保護 `_data` attribute。

**講師觀察重點**：學生是否混淆了 `self.data` 和 `data`、是否正確用 `return self` 實現鏈式呼叫、是否清楚 `@property` 的用途。

**視覺建議**：投影片分三格，每格顯示一個關卡的說明和預期輸出，底部放計時器圖示。

**轉場**：「你已經寫過 class 了。現在來看一個常被誤解的主題：inheritance。很多人以為繼承是 OOP 的核心，其實不然。」

---

### Slide 7 — Inheritance vs Composition

**核心訊息**：繼承表達「是一種（is-a）」關係，組合表達「有一個（has-a）」關係。大部分 AI 工程問題，composition 比 inheritance 好用。

**講師說明要點**：

- 解釋 inheritance 的語法與用途：當你有一個基本行為，要被多個子類別共用時，繼承才有意義
- 以 `BaseDataLoader -> CSVLoader, JSONLoader, ParquetLoader` 為例，說明 inheritance 的合理使用場景
- 說明 composition 的概念：把其他物件當作 attribute 嵌入，不是「我是」，而是「我有」
- 以 `ChatAgent` 為例：它「有」一個 `VectorStoreClient`，不是「是」一個 `VectorStoreClient`
- 核心判斷準則：如果你改了父類別，所有子類別都會受影響，這是 inheritance 的代價。如果你想避開這個代價，就用 composition

```python
# Inheritance: CSVLoader 是 BaseLoader 的一種
class BaseLoader:
    def validate(self) -> bool:
        raise NotImplementedError

class CSVLoader(BaseLoader):
    def __init__(self, path: str):
        self.path = path

    def validate(self) -> bool:
        return self.path.endswith(".csv")


# Composition: ChatAgent 有一個 VectorStoreClient
class ChatAgent:
    def __init__(self, store_client: VectorStoreClient):
        self._store = store_client    # composition
        self._history = []

    def ask(self, question: str) -> str:
        context = self._store.search(question)
        # ... 生成回答
```

**視覺建議**：左欄用樹狀圖表示 inheritance 關係（`BaseLoader` 在上，三個子類別在下）；右欄用方框嵌套圖表示 composition（`ChatAgent` 方框內有 `VectorStoreClient` 和 `history` 方框）。兩欄下方各一行判斷準則。

**轉場**：「好，我們知道怎麼寫 class 了。但現實中，程式碼不會全部住在一個檔案裡。來看看程式碼是怎麼長大的。」

---

### Slide 8 — 腳本的進化路徑

**核心訊息**：從 notebook 到 service，每一步都是為了解決前一步帶來的新問題，不是為了炫技。

**講師說明要點**：

- **Notebook**：最快驗證想法，但無法被其他程式 import，無法測試，無法版本控制
- **Script**：把 notebook 的核心邏輯整理成 `.py`，可以被執行，但仍然是線性的
- **Module**：把 script 拆成多個 `.py` 檔，每個負責一個職責，可以被 import
- **Package**：把相關的 module 放進資料夾加上 `__init__.py`，可以被外部專案使用
- **Service**：加上 API 介面（FastAPI/Flask），讓其他系統可以呼叫你的邏輯
- 說明大部分 AI 工程師的工作，就是把 Jupyter Notebook 裡的原型，變成 Package 甚至 Service 等級的產品

**視覺建議**：一條水平的進化路線，五個階段各有一個圖示（筆記本、腳本圖示、多個 .py 圖示、資料夾圖示、伺服器圖示），每個階段下方標注它解決了什麼問題、帶來了什麼新需求。

**轉場**：「知道了路線，來看 Module 和 Package 實際怎麼做。這涉及到 Python 的 import 機制。」

---

### Slide 9 — Module 與 Package 實作

**核心訊息**：`import` 不是魔法，Python 有清楚的搜尋路徑，`__init__.py` 讓一個資料夾變成可被 import 的 package。

**講師說明要點**：

- 展示一個 package 的最小結構：

```
myproject/
├── __init__.py          # 讓 myproject 成為 package
├── data/
│   ├── __init__.py
│   ├── dataset.py       # Dataset class 住在這裡
│   └── loader.py        # CSVLoader, JSONLoader 住在這裡
├── features/
│   ├── __init__.py
│   └── pipeline.py      # FeaturePipeline class
└── models/
    ├── __init__.py
    └── trainer.py       # ModelTrainer class
```

- 說明 Python 的 import 搜尋順序：sys.modules 快取 → 內建模組 → sys.path 中的路徑
- 展示三種 import 寫法：`import myproject.data.dataset`、`from myproject.data import Dataset`、相對匯入 `from .loader import CSVLoader`
- 解釋 `__init__.py` 的角色：可以空的，也可以在裡面重新 export 讓外部 import 路徑更乾淨
- 強調：不要在 `__init__.py` 放重邏輯，它只做 re-export

**視覺建議**：左欄是檔案樹結構，右欄是對應的 import 語句，用顏色連線顯示哪個 import 對應哪個檔案。底部一張 Python import 搜尋路徑的流程圖。

**轉場**：「這個結構在 AI 工程裡幾乎處處出現。我們來看看真實的 AI 應用是怎麼用 OOP 組織起來的。」

---

### Slide 10 — AI 工程中的 OOP 全景

**核心訊息**：你在 AI 工程裡遇到的每個重要工具——scikit-learn、pandas、LangChain、Hugging Face——背後都是精心設計的 class 系統。

**講師說明要點**：

- 展示五個 AI 工程常見 class，說明它們的 attribute 和 method 設計意圖：

| Class 名稱 | 核心 Attributes | 核心 Methods | 設計原因 |
|-----------|----------------|--------------|---------|
| `Dataset` | `file_path`, `_data`, `schema` | `load()`, `clean()`, `split()` | 把資料生命週期封裝在一起 |
| `FeaturePipeline` | `steps`, `fitted` | `fit()`, `transform()`, `fit_transform()` | 讓特徵工程可以被重複使用和版本控制 |
| `ModelTrainer` | `model`, `config`, `history` | `train()`, `evaluate()`, `save()` | 把訓練流程和超參數綁在一起 |
| `ChatAgent` | `_history`, `_store`, `model_name` | `ask()`, `clear_history()`, `get_context()` | 維護對話狀態，不靠全域變數 |
| `VectorStoreClient` | `index`, `embedding_fn`, `top_k` | `add()`, `search()`, `delete()` | 把向量資料庫操作抽象成乾淨介面 |

- 用 scikit-learn 的 `fit/transform` 介面說明：這是一個 class contract，所有 transformer 都遵守相同介面，所以可以被放進 `Pipeline`
- 強調：學 OOP 不是為了考試，是因為你未來要用的工具都是用 OOP 寫的

**視覺建議**：一張系統架構圖，顯示這五個 class 在一個 AI 專案裡的關係：`Dataset` 餵給 `FeaturePipeline`，`FeaturePipeline` 輸出給 `ModelTrainer`，`ModelTrainer` 訓練的模型被 `ChatAgent` 使用，`ChatAgent` 內嵌 `VectorStoreClient`。

**轉場**：「現在輪到你們動手，把一個混亂的腳本變成一個有組織的 package。」

---

### Slide 11 — 工作坊 2：拆解腳本成 Package（30 分鐘）

**核心訊息**：重構不是重寫，是在不改變外部行為的前提下，改善內部組織。

**練習規格**：

學生收到一個 200 行的訓練腳本 `train.py`，包含資料載入、特徵工程、模型訓練、評估四個邏輯區塊，全部混在一起，用全域變數傳遞狀態。

**任務目標**：把這個腳本重組成以下 package 結構：

```
ml_project/
├── __init__.py
├── data/
│   ├── __init__.py
│   └── dataset.py      # Dataset class
├── features/
│   ├── __init__.py
│   └── pipeline.py     # FeaturePipeline class
└── models/
    ├── __init__.py
    └── trainer.py      # ModelTrainer class
```

**任務步驟（分三階段，各 10 分鐘）**：

**階段 1（10 分鐘）**：識別並提取 `Dataset` class
- 找出所有和資料載入/清理相關的程式碼
- 把它們包進 `Dataset` class，確認 `_data` 被保護
- 測試：`from ml_project.data import Dataset` 能正確執行

**階段 2（10 分鐘）**：提取 `FeaturePipeline` class
- 找出特徵工程相關程式碼
- 實作 `fit()` 和 `transform()` 兩個 method
- 測試：pipeline 能接受 Dataset 的輸出

**階段 3（10 分鐘）**：提取 `ModelTrainer` class 並整合
- 把訓練和評估邏輯包進 `ModelTrainer`
- 確認 `trainer.train(pipeline.transform(dataset.load()))` 這條呼叫鏈能執行
- 確認重構後的行為和原始腳本一致（輸出數字相同）

**講師觀察重點**：學生是否能識別邊界、是否用 composition 而非全域變數傳遞資料、`__init__.py` 是否被正確設定。

**視覺建議**：兩欄對比，左欄是混亂的 200 行腳本（縮略版），右欄是整理後的 package 結構圖，用顏色標示哪些程式碼去了哪個 module。

**轉場**：「你們剛剛做的事，就是 AI 工程師每天在做的事：把原型變成系統。」

---

### Slide 12 — 模組總結與銜接

**核心訊息**：OOP 讓你從「能跑的程式」升級到「能維護的系統」。這個模組的技能，在接下來的每一個模組都會用到。

**講師說明要點**：

- 快速回顧六個核心概念：class、object、attribute、method、encapsulation、module/package
- 說明 M3（NumPy）和 M4（pandas）的 API 都是 class-based，有了今天的基礎才能讀懂文件
- 提示 M7（scikit-learn）的 `Pipeline`、`Estimator`、`Transformer` 全部都是 class contract，是 OOP 概念的直接應用
- 預告最終專案的架構會用到今天練習的 package 結構
- 給出自我檢測問題：「我能不看提示，從頭寫出一個有意義的 class 嗎？」

**學習確認清單**：

- [ ] 我能解釋 class 和 object 的差別
- [ ] 我能寫出帶有 `__init__`、method、`@property` 的 class
- [ ] 我知道為什麼要用 `_` 保護內部狀態
- [ ] 我能判斷什麼時候用 inheritance，什麼時候用 composition
- [ ] 我能把一個腳本拆成 module，並組成 package
- [ ] 我能讀懂 scikit-learn / pandas 的 class API 文件

**視覺建議**：一頁乾淨的總結，左欄是概念清單（帶勾選框），右欄是「下一步」的 M3 預告，包含 NumPy array 的 class 關係示意圖。

---

## AI 應用連結深探

### 為什麼 AI 工程師必須懂 OOP

AI 工程和傳統資料分析最大的差別，在於系統規模和複雜度。一個 Jupyter Notebook 可以做探索性分析，但以下這些場景，沒有 OOP 是做不到的：

**1. 資料管線（Data Pipeline）**
```python
# 沒有 OOP：很難重複使用，很難測試
def load_and_clean(path, drop_cols, fill_strategy):
    df = pd.read_csv(path)
    df = df.drop(columns=drop_cols)
    # ... 20 行清理邏輯
    return df

# 有 OOP：可以被組合、被繼承、被測試
class DataPipeline:
    def __init__(self, steps: list):
        self.steps = steps

    def run(self, data):
        for step in self.steps:
            data = step.transform(data)
        return data
```

**2. 模型版本管理**
`ModelTrainer` class 可以把模型路徑、超參數、訓練歷史全部綁在一起，讓你的實驗結果可以被追蹤和比較。

**3. Chatbot 狀態管理**
對話歷史必須有一個「家」。`ChatAgent` class 讓每個對話 session 都有自己獨立的狀態，不會互相干擾。這在多用戶場景下至關重要。

**4. 向量資料庫封裝**
`VectorStoreClient` 把底層 API 呼叫封裝起來，讓上層的 `ChatAgent` 不需要知道用的是 Pinecone 還是 Chroma。這是 encapsulation 的直接應用。

### 真實函式庫的 OOP 設計

| 函式庫 | 核心 Class | OOP 概念的應用 |
|--------|-----------|--------------|
| scikit-learn | `BaseEstimator`, `TransformerMixin` | inheritance + class contract（fit/transform 介面） |
| pandas | `DataFrame`, `Series` | encapsulation（內部是 NumPy array，外部不需知道）|
| LangChain | `BaseChain`, `BaseTool`, `BaseMemory` | inheritance + composition（Chain 組合多個 Tool） |
| PyTorch | `nn.Module` | inheritance（所有模型繼承 `nn.Module`，必須實作 `forward()`） |
| Hugging Face | `PreTrainedModel`, `Tokenizer` | encapsulation（複雜的模型架構被包進乾淨介面）|

---

## 課前準備與課後延伸

### 課前建議（M1 完成後）

- 閱讀 Python 官方文件：[Classes](https://docs.python.org/3/tutorial/classes.html)（約 15 分鐘）
- 觀察一個你用過的函式庫（如 pandas），用 `dir()` 看看一個 `DataFrame` 物件有哪些 attribute 和 method

### 課後延伸練習

1. 把你之前寫過的任何一個超過 80 行的腳本，嘗試識別出 2 個可以包成 class 的概念
2. 閱讀 scikit-learn 的 `Pipeline` 文件，理解它為什麼要求所有 step 都要有 `fit` 和 `transform` 方法
3. 寫一個 `ChatHistory` class，能夠儲存對話歷史、計算總 token 數、輸出最近 N 輪對話

### 參考資源

- Python 官方文件：[9. Classes](https://docs.python.org/3/tutorial/classes.html)
- Python 官方文件：[6. Modules](https://docs.python.org/3/tutorial/modules.html)
- Real Python：[Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- scikit-learn 文件：[Developing scikit-learn estimators](https://scikit-learn.org/stable/developers/develop.html)（理解 class contract 的最佳範例）

---

*本模組為 24 小時 Python 數據分析與 AI 工程基礎課程的第 2 模組，對應課程總計畫第 4–6 小時。*
