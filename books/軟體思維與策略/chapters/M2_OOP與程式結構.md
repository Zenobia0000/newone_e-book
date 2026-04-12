# M2：OOP 與程式結構

## 系統設計與架構思維 — Course 2，Module 2

**時數：** 3 小時  
**主線：** 工程基礎線（A）  
**前置模組：** M1 軟體工程第一原理  
**後續模組：** M3 進階 Python 工程

---

> "OOP is not academic gymnastics — it's how systems survive."

---

## 一、模組定位

Course 1 介紹過 class 和 object 的基本語法。你知道怎麼定義一個 class、加 `__init__`、呼叫方法。

這個模組不從那裡出發。

**這個模組的問題是：** 你已經會寫 class 了，但你寫出來的 class 能不能活過六個月？能不能被不認識你的人維護？能不能在需求改變時只動一個地方？

從「語法正確」到「設計正確」，中間有一整個體系叫做物件導向設計原則。這個模組把它講清楚。

### M2 在課程架構中的位置

```
M1 軟體工程第一原理
  ↓ 理解程式本質
M2 OOP 與程式結構      ← 你在這裡
  ↓ 把程式組織成可維護系統
M3 進階 Python 工程
  ↓ 工具鏈與工程實踐
M4-M5 計組與 OS
  ↓ 底層執行環境
M6-M8 系統設計與架構
```

M1 讓你理解程式是什麼。M2 讓你知道如何組織程式。沒有 M2 的基礎，M6 的系統設計就只是在空中畫圈。

---

## 二、學習目標（7 項）

完成本模組後，你能夠：

1. **區分「語法層」與「設計層」的 OOP**：知道 class/object 是機制，封裝/繼承/組合是選擇，SOLID 是原則——三個層次不同，混淆是設計災難的根源。

2. **用封裝思維設計介面**：理解什麼是「公開契約」與「私有實作」，能判斷一個 method 或 attribute 應該暴露還是隱藏。

3. **在繼承和組合之間做出有根據的選擇**：能說明「is-a」vs「has-a」，知道過深的繼承樹會帶來什麼風險，以及什麼場景應該優先選組合。

4. **解釋 SOLID 五大原則並識別違反它們的程式碼**：不是背定義，而是看到真實程式碼能說出「這裡違反了 OCP，因為...」。

5. **辨識三個核心設計模式的意圖**：Strategy、Observer、Factory——不求記住實作細節，但要知道各自解決什麼問題，在 AI 應用程式中在哪裡出現。

6. **理解程式組織的層次**：notebook → script → module → package → service，每個層次的邊界在哪裡，什麼時候應該往上一層走。

7. **閱讀真實函式庫的 API 設計**：看 scikit-learn、pandas、LangChain 的 class 結構，能說出設計者在做什麼決策，為什麼這樣設計。

---

## 三、核心概念清單

### 3.1 OOP 機制層
- `class` 定義：藍圖 vs 實例
- `__init__`：物件初始化
- `self`：實例綁定
- instance attribute vs class attribute
- instance method vs class method vs static method
- `__repr__` / `__str__`：物件的自我描述

### 3.2 OOP 設計層
- **封裝（Encapsulation）**：公開介面 vs 私有實作；`_` 和 `__` 的語義
- **繼承（Inheritance）**：is-a 關係；`super()`；方法覆寫（override）；MRO
- **多型（Polymorphism）**：同一介面，不同行為；duck typing in Python
- **組合（Composition）**：has-a 關係；delegation pattern
- **抽象（Abstraction）**：`abc.ABC`；`@abstractmethod`

### 3.3 SOLID 原則
- **S**：Single Responsibility Principle（單一職責）
- **O**：Open/Closed Principle（開放/封閉）
- **L**：Liskov Substitution Principle（里氏替換）
- **I**：Interface Segregation Principle（介面隔離）
- **D**：Dependency Inversion Principle（依賴反轉）

### 3.4 設計模式預覽
- **Strategy Pattern**：把演算法封裝成可替換的物件
- **Observer Pattern**：事件通知機制，解耦發布者與訂閱者
- **Factory Pattern**：把物件建立邏輯集中管理

### 3.5 程式組織層次
- Notebook：探索與實驗
- Script：單次執行任務
- Module：可重用的程式單元（`.py` 檔）
- Package：模組集合（`__init__.py` + 目錄結構）
- Service：對外提供介面的獨立部署單元

### 3.6 AI 應用中的 OOP
- `Dataset`：資料抽象
- `ModelTrainer`：訓練流程封裝
- `FeaturePipeline`：特徵工程管線
- `ChatAgent`：對話狀態與工具管理
- `VectorStoreClient`：向量資料庫介面

---

## 四、投影片大綱

| # | 投影片標題 | 類型 | 預估時間 |
|---|-----------|------|---------|
| 01 | OOP 是什麼：語法、機制、原則三個層次 | 概念定位 | 8 分鐘 |
| 02 | Class 解剖：從藍圖到實例 | 核心概念 | 12 分鐘 |
| 03 | 封裝：公開契約與私有實作 | 核心概念 | 15 分鐘 |
| 04 | 繼承 vs 組合：最重要的設計選擇 | 核心概念 | 15 分鐘 |
| 05 | 多型與抽象：讓系統可替換 | 核心概念 | 12 分鐘 |
| 06 | SOLID 原則：設計的五條鐵律 | 設計原則 | 20 分鐘 |
| 07 | 設計模式預覽：Strategy、Observer、Factory | 模式預覽 | 18 分鐘 |
| 08 | 程式組織的進化：notebook → service | 架構視角 | 12 分鐘 |
| 09 | AI 應用中的 OOP：五個核心 class | 應用連結 | 15 分鐘 |
| 10 | 閱讀真實 API：scikit-learn / pandas / LangChain | 實戰閱讀 | 15 分鐘 |
| 11 | Workshop 1：重構一個違反 SOLID 的程式 | 動手練習 | 25 分鐘 |
| 12 | Workshop 2：設計一個 AI Pipeline 的 class 結構 | 動手練習 | 25 分鐘 |
| 13 | 模組總結：OOP 是系統生存的機制 | 收尾 | 8 分鐘 |

**合計：** 約 180 分鐘（3 小時）

---

## 五、投影片詳細規格

---

### Slide 01｜OOP 是什麼：語法、機制、原則三個層次

**核心訊息**

「class 是語法，封裝是設計決策，SOLID 是原則體系——大多數 OOP 教學只教第一層，這門課教三層。」

**談話要點**

1. Course 1 已經教過 class 語法。今天不複習語法，而是往上升兩層。
2. 很多工程師「會用 class」但「不懂設計 class」。差別在哪裡？看看六個月後的 codebase 就知道了。
3. 語法層：`class`、`__init__`、`self`——這些是 Python 提供的工具。
4. 設計層：封裝、繼承、組合、多型——這些是你的選擇，選錯了很痛。
5. 原則層：SOLID——這些是前人在痛過之後總結出來的規則，讓你避免重蹈覆轍。

**視覺建議**

三層金字塔圖：底層「語法（Syntax）」→ 中層「設計（Design）」→ 頂層「原則（Principles）」。每層旁邊列出代表元素。金字塔右側標注：「大多數人停在第一層。」

**轉場**

「我們先從最基礎的機制開始，確認你對 class 的理解是精確的，不只是『能跑就好』。」

---

### Slide 02｜Class 解剖：從藍圖到實例

**核心訊息**

「Class 是藍圖，object 是蓋出來的房子。搞清楚誰的東西是誰的，是後面所有設計的基礎。」

**談話要點**

1. Class 在 Python 中是一個物件（everything is an object），但它的職責是「定義結構」，不是「儲存資料」。
2. Instance attribute（`self.x`）屬於每個 object，class attribute（`cls.x`）屬於 class 本身——混淆這兩者是初學者最常見的 bug 來源。
3. `__init__` 不是建構子（constructor），它是初始化方法（initializer）。真正的建構子是 `__new__`，但大多數時候你不需要碰它。
4. `__repr__` 是給開發者看的，`__str__` 是給使用者看的。永遠都要實作 `__repr__`。
5. 看程式碼前先問：這個 class 的責任是什麼？它知道什麼？它能做什麼？它不知道什麼？

**視覺建議**

左側：一段清楚的 Python class 定義（`ModelTrainer`），標注每個部分的名稱和作用。右側：兩個 instance，顯示 instance attribute 各自獨立，class attribute 共享。

```python
class ModelTrainer:
    default_epochs = 10  # class attribute: 所有 instance 共享

    def __init__(self, model, lr: float = 0.001):
        self.model = model          # instance attribute: 每個 instance 獨立
        self.lr = lr
        self.history = []           # instance attribute: 每個 instance 獨立

    def train(self, dataset):
        # 訓練邏輯
        ...

    def __repr__(self):
        return f"ModelTrainer(lr={self.lr})"
```

**轉場**

「現在你對 class 的基本結構有精確的理解了。下一步是最關鍵的設計概念——封裝。」

---

### Slide 03｜封裝：公開契約與私有實作

**核心訊息**

「封裝不是把東西藏起來，而是定義介面與實作的邊界。邊界清楚，系統才能獨立演化。」

**談話要點**

1. 封裝的本質：分離「你需要知道的」和「你不需要知道的」。公開 API 是契約；私有實作是細節。
2. Python 的慣例：`_` 前綴表示「內部使用，不保證穩定」；`__` 前綴觸發 name mangling，更強的隱藏。沒有前綴 = 公開 API。
3. 使用者應該只依賴公開 API。如果你在用別人 class 的 `_method`，你在打破契約，未來版本可能直接消失。
4. 好的封裝讓你可以安全地重構內部實作，不影響任何使用者。這就是「可演化性」的來源。
5. 反例：一個 `DataProcessor` class 把所有東西都放成 public，使用者直接操作內部 list，之後你想改資料結構——改不了，因為所有人都依賴了你的內部細節。

**視覺建議**

兩欄對比：左側「不好的封裝」（所有屬性都是 public，使用者亂碰內部狀態）vs 右側「好的封裝」（只暴露必要的 method，內部實作自由變化）。中間畫一條邊界線，標注「Public API = 契約」。

```python
# 不好的封裝：暴露內部細節
class FeaturePipeline:
    def __init__(self):
        self.steps = []          # 使用者可以直接操作 steps
        self.fitted = False      # 使用者可以手動改 fitted 狀態

# 好的封裝：透過方法控制狀態
class FeaturePipeline:
    def __init__(self):
        self._steps = []         # 私有：使用者不直接碰
        self._fitted = False

    def add_step(self, transformer):
        if self._fitted:
            raise RuntimeError("Pipeline already fitted; cannot add steps.")
        self._steps.append(transformer)

    def fit(self, X):
        for step in self._steps:
            step.fit(X)
        self._fitted = True
```

**轉場**

「封裝管理的是單一 class 內部的邊界。現在我們來看 class 之間的關係——繼承和組合。」

---

### Slide 04｜繼承 vs 組合：最重要的設計選擇

**核心訊息**

「繼承建立 is-a 關係；組合建立 has-a 關係。優先選組合，除非你真的在建模 is-a 關係。」

**談話要點**

1. 繼承的力量：共享行為、建立型別層次、讓多型成為可能。繼承適合真正的「is-a」關係。`Dog` is a `Animal`，沒問題。
2. 繼承的危險：繼承是強耦合。子類別依賴父類別的所有細節。父類別一改，子類別可能全壞。繼承層次超過兩層，就要開始緊張了。
3. 組合的邏輯：「這個 class 需要某種能力」→ 把那個能力封裝成獨立物件，用 has-a 關係引入，而不是繼承進來。
4. 實際判斷標準：問「能不能用一句話說清楚 is-a 關係，而且未來不會變？」如果不能，用組合。`ModelTrainer` is a `Logger`？不對。`ModelTrainer` has a `Logger`？對。
5. Go 語言沒有繼承，只有組合——這不是缺陷，這是刻意的設計選擇。它讓工程師不得不把設計想清楚。

**視覺建議**

左側繼承圖：一個過度設計的動物繼承樹（四層），標注「每一層都是一個依賴風險」。右側組合圖：`ModelTrainer` 持有 `Logger`、`Optimizer`、`EarlyStopper` 的 UML 組合關係，標注「各自獨立，可替換」。

```python
# 繼承：is-a 關係明確時使用
class BaseTrainer:
    def train(self, dataset): raise NotImplementedError

class SupervisedTrainer(BaseTrainer):
    def train(self, dataset):
        # 監督學習訓練邏輯
        ...

# 組合：has-a 關係，優先選擇
class ModelTrainer:
    def __init__(self, model, optimizer, logger):
        self.model = model
        self.optimizer = optimizer    # has-a Optimizer
        self.logger = logger          # has-a Logger

    def train(self, dataset):
        self.logger.info("Training started")
        self.optimizer.step(self.model, dataset)
```

**轉場**

「了解繼承和組合後，我們來看讓繼承和組合真正發揮力量的機制——多型與抽象。」

---

### Slide 05｜多型與抽象：讓系統可替換

**核心訊息**

「多型讓你的程式碼對介面編程，而不是對實作編程。這是系統可替換、可擴展的根本機制。」

**談話要點**

1. 多型的本質：「同一個呼叫，不同的行為」。你的程式碼呼叫 `trainer.train(data)`，不需要知道 `trainer` 是 `SGDTrainer` 還是 `AdamTrainer`，只要它有 `train` 方法。
2. Python 的 duck typing：Python 不強制要求型別宣告，只要物件有對應的方法就能被呼叫。「如果它走路像鴨子、叫聲像鴨子，它就是鴨子。」
3. 抽象基礎類別（ABC）的作用：當你想明確宣告「任何實作了這個介面的 class 必須實作這些方法」時，用 `abc.ABC` 和 `@abstractmethod`。這是讓合約變成強制檢查。
4. 真實場景：scikit-learn 所有 estimator 都實作 `fit()` / `predict()` / `transform()`，你可以把任何 estimator 傳進 `Pipeline`，因為它們有共同的抽象介面。這就是多型在真實系統中的力量。
5. 替換是架構的核心能力。能替換意味著能測試（換掉真實資料庫用假的）、能演化（換掉舊演算法用新的）、能配置（用設定檔決定用哪個實作）。

**視覺建議**

一個「插座」比喻圖：一個統一的插座介面（`BaseEmbedder`），可以插入不同的實作（`OpenAIEmbedder`、`CohereEmbedder`、`LocalEmbedder`）。呼叫端只看到插座，不知道插的是什麼。

```python
from abc import ABC, abstractmethod

class BaseEmbedder(ABC):
    @abstractmethod
    def embed(self, texts: list[str]) -> list[list[float]]:
        """將文字轉換為向量"""
        ...

class OpenAIEmbedder(BaseEmbedder):
    def embed(self, texts):
        # 呼叫 OpenAI API
        ...

class LocalEmbedder(BaseEmbedder):
    def embed(self, texts):
        # 用本地模型推論
        ...

# 呼叫端對介面編程，不對實作編程
def build_index(embedder: BaseEmbedder, documents: list[str]):
    vectors = embedder.embed(documents)
    # 建立索引...
```

**轉場**

「以上五個機制是 OOP 的工具箱。現在我們進入最重要的問題：你怎麼知道自己用對了？答案是 SOLID 原則。」

---

### Slide 06｜SOLID 原則：設計的五條鐵律

**核心訊息**

「SOLID 是前人在真實系統中反覆摔跤之後總結出來的。每一條都對應一種真實的痛。」

**談話要點（每一條原則）**

**S — Single Responsibility Principle（SRP）**

- 一個 class 只做一件事，只有一個改變的理由。
- 違反時的症狀：class 名稱包含 `And`（`UserAuthAndEmailSender`），或者 class 超過 200 行，或者改一個功能導致不相關的測試壞掉。
- 修復方法：找出這個 class 被改動的不同原因，每個原因拆成一個 class。

**O — Open/Closed Principle（OCP）**

- 對擴展開放，對修改封閉。新增功能不應該修改現有程式碼，而是加新的程式碼。
- 達成方式：用抽象介面 + 多型。新增行為 = 加一個實作新介面的 class，不改原有程式碼。
- 違反時的症狀：每次新增一個功能，你都在改一個 `if-elif` 鏈。

**L — Liskov Substitution Principle（LSP）**

- 子類別必須可以完全替換父類別，且不改變程式的正確性。
- 通俗說法：如果你把父類別換成子類別，程式應該表現一樣好，不應該出現 `isinstance` 才能判斷的特殊行為。
- 著名反例：`Rectangle` → `Square` 繼承（正方形繼承長方形）看起來合理，但改變 width 的同時也改變 height，破壞了 `Rectangle` 的語義。

**I — Interface Segregation Principle（ISP）**

- 不要強迫使用者依賴他們不需要的介面。大而全的介面比小而精的介面更糟糕。
- 實務：如果你的抽象基礎類別有 10 個 abstractmethod，但大多數實作只用到 3 個，該介面太胖了，應該拆分。

**D — Dependency Inversion Principle（DIP）**

- 高層模組不應該依賴低層模組，兩者都應該依賴抽象。
- 具體說：你的 `ReportGenerator` 不應該直接 `import PDFWriter`，應該依賴 `BaseWriter` 介面。這樣你可以在不改 `ReportGenerator` 的情況下，換成 `HTMLWriter` 或 `ExcelWriter`。
- 這是依賴注入（Dependency Injection）的理論基礎。

**視覺建議**

五行表格，每行一個原則：縮寫 + 原則名 + 一句話定義 + 違反時的症狀（用紅色標注）。表格下方一句話：「違反 SOLID 不會讓程式崩潰，但會讓每次改動都越來越痛。」

**轉場**

「SOLID 告訴你設計的原則。設計模式告訴你已經被驗證的解法。我們來看三個最重要的模式。」

---

### Slide 07｜設計模式預覽：Strategy、Observer、Factory

**核心訊息**

「設計模式是反覆出現的設計問題的命名解法。學模式不是學語法，是學如何思考設計問題。」

**談話要點**

**Strategy Pattern（策略模式）**

- 問題：你有一個演算法，但演算法的核心步驟需要可替換（不同的排序策略、不同的評分函數、不同的訓練演算法）。
- 解法：把演算法封裝成一個物件，讓呼叫端注入（inject）它想要的策略。
- AI 場景：`EmbeddingStrategy`（可以是 OpenAI 或本地模型）、`SamplingStrategy`（可以是 greedy 或 beam search）。
- 和 OCP 的關係：Strategy 模式是 OCP 最常見的實作方式。

```python
class RetrievalStrategy(ABC):
    @abstractmethod
    def retrieve(self, query: str, k: int) -> list[str]: ...

class DenseRetrieval(RetrievalStrategy):
    def retrieve(self, query, k):
        # 向量相似度搜尋
        ...

class SparseRetrieval(RetrievalStrategy):
    def retrieve(self, query, k):
        # BM25 關鍵字搜尋
        ...

class RAGPipeline:
    def __init__(self, retrieval: RetrievalStrategy):
        self.retrieval = retrieval  # 注入策略

    def answer(self, question: str) -> str:
        context = self.retrieval.retrieve(question, k=5)
        # 生成回答...
```

**Observer Pattern（觀察者模式）**

- 問題：當某件事發生時，你需要通知多個不同的物件，但不想讓事件來源直接依賴通知目標。
- 解法：事件來源（Subject）維護一個觀察者清單，當狀態改變時通知所有觀察者。
- AI 場景：訓練迴圈（Subject）在每個 epoch 結束時通知各種回調（Callback）：`LossLogger`、`ModelCheckpointer`、`EarlyStopper`。
- 這就是 Keras `callbacks` 的設計原理。

```python
class TrainingSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def _notify(self, event: dict):
        for obs in self._observers:
            obs.update(event)

    def train_epoch(self, epoch, loss):
        # 訓練一個 epoch...
        self._notify({"epoch": epoch, "loss": loss})

class LossLogger:
    def update(self, event):
        print(f"Epoch {event['epoch']}: loss={event['loss']:.4f}")

class EarlyStopper:
    def __init__(self, patience=5):
        self.patience = patience
        self._no_improve = 0

    def update(self, event):
        # 判斷是否應該停止訓練
        ...
```

**Factory Pattern（工廠模式）**

- 問題：你需要建立物件，但物件的型別要在執行時根據設定決定，而且不想讓呼叫端知道建立細節。
- 解法：把物件建立邏輯集中在一個工廠函數或工廠 class 中。
- AI 場景：根據設定檔決定用哪個 LLM 提供者（`create_llm("openai")` 或 `create_llm("anthropic")`）。

```python
def create_llm(provider: str, **kwargs):
    """工廠函數：根據 provider 名稱建立對應的 LLM 實例"""
    providers = {
        "openai": OpenAIClient,
        "anthropic": AnthropicClient,
        "local": LocalLLMClient,
    }
    if provider not in providers:
        raise ValueError(f"Unknown provider: {provider}")
    return providers[provider](**kwargs)

# 使用端不需要知道各 class 的建立細節
llm = create_llm("openai", model="gpt-4o", temperature=0.7)
```

**轉場**

「三個模式都見識過了。現在換個視角：當你的程式越來越大，class 本身已經不夠用，你需要更大的組織單位——module 和 package。」

---

### Slide 08｜程式組織的進化：notebook → service

**核心訊息**

「每一層組織方式都有它的適用場景。問題不是哪個更好，而是你的程式在哪個成長階段。」

**談話要點**

1. **Notebook（探索）**：快速實驗、資料探索、一次性分析。狀態散落在各個 cell，難以重現，不適合協作和維護。適合：研究、EDA、概念驗證（PoC）。
2. **Script（任務）**：單一 `.py` 檔，有 `if __name__ == "__main__"`，可以重複執行。適合：資料處理管線、排程任務、一次性轉換。
3. **Module（重用）**：有清楚職責的 `.py` 檔，設計成被 `import` 使用，不設計成直接執行。函數和 class 集中在這裡。適合：工具函數庫、共用邏輯。
4. **Package（系統）**：多個 module 組成的目錄，有 `__init__.py`，有清楚的對外 API。適合：可重用的函式庫、中型專案的內部組件。
5. **Service（部署）**：對外暴露介面（HTTP API、gRPC、message queue）的獨立部署單元。其他系統透過網路呼叫，不透過 `import`。適合：需要獨立擴展、獨立部署的功能模組。

移動到下一層的信號：
- Notebook → Script：「我需要重複執行這個分析」
- Script → Module：「我在多個 script 裡複製貼上同一段程式碼」
- Module → Package：「我有超過 3 個 module，需要組織和統一的對外介面」
- Package → Service：「這個功能需要獨立擴展，或者被不同語言的系統呼叫」

**視覺建議**

一條水平時間軸，從左到右標注五個階段，每個階段底下列出「適用場景」和「移動到下一層的觸發條件」。時間軸上方畫出每個階段的典型檔案結構。

**轉場**

「理論說夠了。讓我們看 OOP 在 AI 應用中是怎麼實際應用的——從真實的設計案例出發。」

---

### Slide 09｜AI 應用中的 OOP：五個核心 class

**核心訊息**

「AI 應用的複雜性，最終都落實到幾個核心物件的設計上。把這些物件設計好，整個系統就穩了。」

**談話要點**

**1. Dataset**

- 職責：資料的來源、格式化、切割、批次化。
- 關鍵設計決策：`__len__` 和 `__getitem__` 讓它和 PyTorch `DataLoader` 整合；`split()` 回傳的是另一個 `Dataset`，不是 raw data。
- 封裝重點：資料讀取的實作（從 CSV？從 HDF5？從 S3？）應該是私有的，對外只暴露統一的資料訪問介面。

**2. ModelTrainer**

- 職責：管理訓練迴圈，不負責模型架構（SRP）。
- 組合關係：has-a `Optimizer`、has-a `LossFunction`、has-a `Logger`、has-a `Callbacks`。
- 關鍵設計決策：`fit(dataset)` 是公開 API；每個 epoch 的細節是私有的。

**3. FeaturePipeline**

- 職責：特徵工程步驟的有序執行。
- 關鍵設計決策：`Pipeline` 本身是一個 transformer（fit/transform），每個 step 也是 transformer——遞迴組合。這是 scikit-learn `Pipeline` 的設計精髓。
- Strategy 模式應用：每個 step 可以替換，整個 pipeline 不需要改。

**4. ChatAgent**

- 職責：管理對話狀態（history）、工具調用（tools）、與 LLM 的交互。
- 關鍵設計決策：`history` 是私有的，外部只能透過 `chat()` 方法與 agent 交互，不能直接操作歷史記錄。
- Observer 模式應用：工具調用的結果作為事件通知 agent。

**5. VectorStoreClient**

- 職責：抽象向量資料庫的介面。
- 關鍵設計決策：對外暴露 `upsert()` / `query()` / `delete()`，隱藏底層是 Pinecone、Weaviate 還是 pgvector 的細節。
- DIP 應用：上層邏輯依賴 `BaseVectorStore` 介面，不依賴具體實作。

**視覺建議**

五個 class 的 UML 關係圖，標出它們之間的組合和依賴關係。例如 `ChatAgent` has-a `VectorStoreClient`（用於 RAG）、has-a `ModelTrainer`（如果 agent 會 fine-tune）。

**轉場**

「這些設計不是我發明的——它們來自真實的函式庫。讓我們去讀那些程式碼，理解設計者在想什麼。」

---

### Slide 10｜閱讀真實 API：scikit-learn / pandas / LangChain

**核心訊息**

「讀真實函式庫的 API，不是為了學用法，而是為了理解設計者做了什麼決定，以及為什麼這樣決定。」

**談話要點**

**scikit-learn 的統一 Estimator 介面**

- 所有 estimator 都有 `fit(X, y)` 和 `predict(X)`（或 `transform(X)`）。
- 這是 LSP 的完美體現：你可以把任何 estimator 傳進 `cross_val_score`，因為它們都符合同一個協議。
- `Pipeline` 把多個 transformer 鏈接起來，用組合而非繼承——每個 step 是 has-a 關係。
- `clone()` 函數的存在說明了什麼：estimator 需要是無狀態的藍圖（fit 前）和有狀態的模型（fit 後）的結合。

**pandas 的方法鏈設計**

- `DataFrame` 的 `filter()` / `assign()` / `groupby()` 都回傳新的 `DataFrame`，讓你可以鏈式調用。
- 這是不可變性（immutability）的設計哲學：每次操作建立新物件，不修改原物件。
- 代價是記憶體；收益是可預測性和可組合性。這是明確的取捨。

**LangChain 的 Runnable 協議**

- LangChain v0.1+ 的核心設計：所有元件（LLM、prompt、chain、retriever）都實作 `invoke()` / `stream()` / `batch()`。
- 這讓 `|` 運算子（LCEL）成為可能：`prompt | llm | parser` 把三個元件組成一個管線。
- 這是 Strategy + Composite 模式的組合：元件可替換（Strategy），管線可巢狀（Composite）。

**視覺建議**

三個並排的程式碼框，每個展示一個函式庫的典型使用模式，下方標注「哪個 OOP 原則在這裡體現」。

**轉場**

「夠了——理論和範例都夠了。現在是你動手的時候。」

---

### Slide 11｜Workshop 1：重構一個違反 SOLID 的程式

**類型：** 動手練習  
**時間：** 25 分鐘（10 分鐘閱讀 + 10 分鐘重構 + 5 分鐘討論）

**情境設定**

你接手了一個同事寫的 `DataAnalyzer` class。它能跑，但是一個設計災難。你的任務是重構它，讓它符合 SOLID 原則。

**給學員的起始程式碼**

```python
# 有問題的設計：請找出至少 3 個 SOLID 違反
import csv
import json
import smtplib
from email.message import EmailMessage

class DataAnalyzer:
    def __init__(self, filepath: str, output_format: str = "csv"):
        self.filepath = filepath
        self.output_format = output_format
        self.data = []
        self.results = {}

    def load_data(self):
        """載入資料——只支援 CSV"""
        with open(self.filepath) as f:
            reader = csv.DictReader(f)
            self.data = list(reader)

    def analyze(self, analysis_type: str):
        """根據 analysis_type 做不同的分析"""
        if analysis_type == "count":
            self.results["count"] = len(self.data)
        elif analysis_type == "mean":
            values = [float(row["value"]) for row in self.data]
            self.results["mean"] = sum(values) / len(values)
        elif analysis_type == "max":
            values = [float(row["value"]) for row in self.data]
            self.results["max"] = max(values)
        # 每次新增分析類型都要修改這個方法

    def save_results(self):
        """儲存結果——根據 output_format 決定格式"""
        if self.output_format == "csv":
            with open("results.csv", "w") as f:
                writer = csv.DictWriter(f, fieldnames=self.results.keys())
                writer.writeheader()
                writer.writerow(self.results)
        elif self.output_format == "json":
            with open("results.json", "w") as f:
                json.dump(self.results, f)

    def send_email(self, recipient: str):
        """發送結果到指定信箱"""
        msg = EmailMessage()
        msg["Subject"] = "Analysis Results"
        msg["To"] = recipient
        msg.set_content(str(self.results))
        with smtplib.SMTP("localhost") as s:
            s.send_message(msg)
```

**引導問題**

1. 這個 class 有幾個改變的理由？（提示：SRP）
2. 如果你想新增 `median` 分析，你需要改哪裡？（提示：OCP）
3. 如果你想支援從資料庫載入資料，你需要改哪裡？（提示：DIP）

**重構方向提示**

- 把 `load_data`、`analyze`、`save_results`、`send_email` 分別拆入有單一職責的 class
- 用抽象介面讓 `analyze` 和 `save_results` 可以擴展，而不是修改
- `DataAnalyzer` 本身只負責協調，不負責任何具體操作

**預期重構後的結構**

```
DataLoader（抽象）→ CSVLoader / DBLoader / APILoader
AnalysisStrategy（抽象）→ CountAnalysis / MeanAnalysis / MaxAnalysis
ResultWriter（抽象）→ CSVWriter / JSONWriter
Notifier（抽象）→ EmailNotifier / SlackNotifier
DataAnalyzer（協調者）→ 注入以上四個介面
```

---

### Slide 12｜Workshop 2：設計一個 AI Pipeline 的 class 結構

**類型：** 動手練習  
**時間：** 25 分鐘（10 分鐘設計 + 10 分鐘實作核心 class + 5 分鐘討論）

**情境設定**

你要為一個 RAG（Retrieval-Augmented Generation）系統設計 class 結構。需求如下：

- 支援多種文件格式輸入（PDF、DOCX、TXT）
- 文件需要被切割（chunking）後嵌入成向量
- 向量儲存在向量資料庫中（可以是不同的提供者）
- 查詢時先檢索相關文件，再用 LLM 生成回答
- 需要能夠記錄每次查詢的延遲和 token 使用量

**任務**

1. 識別系統中的核心物件（至少 5 個 class）
2. 畫出 class 之間的關係（繼承？組合？依賴？）
3. 用 Python 實作核心抽象介面（至少 3 個 ABC）
4. 說明你在哪裡應用了哪個 SOLID 原則

**引導框架**

```
輸入層：DocumentLoader（抽象）
處理層：TextChunker、EmbeddingModel（抽象）
儲存層：VectorStore（抽象）
查詢層：Retriever（抽象）
生成層：LLMClient（抽象）
協調層：RAGPipeline
監控層：MetricsCollector
```

**評估標準**

- 每個 class 只有一個職責（SRP）
- 新增一個 `DocumentLoader` 實作不需要修改 `RAGPipeline`（OCP + DIP）
- 抽象介面足夠小，不強迫實作不需要的方法（ISP）
- 有示範如何通過建構子注入依賴（DI）

**延伸挑戰（如果完成得快）**

在 `RAGPipeline.query()` 中加入 Observer 模式：讓 `MetricsCollector` 和 `QueryLogger` 都能接收查詢完成事件，而 `RAGPipeline` 不需要知道有哪些觀察者。

---

### Slide 13｜模組總結：OOP 是系統生存的機制

**核心訊息**

「你學到的不只是 class 怎麼寫，而是程式如何被組織成能活過時間考驗的系統。」

**談話要點**

1. 回顧今天走過的路：從精確理解 class 機制，到封裝/繼承/組合的設計選擇，到 SOLID 原則，到設計模式，到程式組織層次，到 AI 應用落地，到閱讀真實 API。這是一個完整的認知升級路徑。
2. OOP 的核心價值不是「整潔」，而是「可演化」。你不知道六個月後的需求是什麼，但你可以用 OOP 設計讓改動的代價更小。
3. 最常犯的錯誤：把「會寫 class」等於「懂 OOP」。真正的測試是：你的 class 在需求改變時有多容易改？
4. 下一步：M3 會把今天學到的設計原則落實到更完整的工程實踐中——型別系統、測試、環境管理、logging。設計正確只是第一步，工程化才能讓設計存活。
5. 一個真正的工程師看到「可以用 class 但不需要 class」的情況，會選擇不用。最好的 OOP 是恰到好處的 OOP，而不是為了用而用。

**視覺建議**

一頁整潔的知識地圖，把今天所有概念按照「機制」→「設計選擇」→「原則」→「模式」→「組織層次」的層次排列。每個節點用 2-3 個關鍵字標注。最底部一行大字：

> "OOP is not academic gymnastics — it's how systems survive."

**轉場**

「帶著今天建立的設計思維，我們在 M3 裡把它轉化成具體的工程實踐。」

---

## 六、Workshop 練習詳細規格

### Workshop 1：SOLID 重構練習

| 項目 | 內容 |
|------|------|
| 目標 | 識別並修復真實程式碼中的 SOLID 違反 |
| 前置知識 | Slide 01-06 |
| 時間 | 25 分鐘 |
| 分組 | 建議 2 人一組 |
| 交付物 | 重構後的 class 結構（可以只寫 class 骨架，不需要完整實作） |
| 成功標準 | 能說出至少 3 個 SOLID 違反，並說明重構後如何修復 |

**評分維度**

1. 識別正確性（3 分）：找到的問題是真的問題，不是假問題。
2. 重構合理性（3 分）：重構後的設計確實解決了問題，沒有過度設計。
3. 原則對應（2 分）：能說明每個重構決定對應哪個 SOLID 原則。
4. 簡潔性（2 分）：沒有為了用 OOP 而用 OOP，該簡單的地方保持簡單。

**常見錯誤警示**

- 為了分責任而製造過多的小 class，每個 class 只有一個方法
- 抽象介面定義得太細，導致每個 class 都要實作一堆用不到的方法（違反 ISP）
- 把依賴注入理解成「把所有東西都傳進建構子」

---

### Workshop 2：AI Pipeline 設計練習

| 項目 | 內容 |
|------|------|
| 目標 | 從需求出發，設計一個真實 AI 系統的 class 結構 |
| 前置知識 | Slide 01-10 |
| 時間 | 25 分鐘 |
| 分組 | 建議 2-3 人一組 |
| 交付物 | class 關係圖 + 核心 ABC 的 Python 程式碼 |
| 成功標準 | 設計能清楚說明可替換性和擴展性 |

**引導問題序列**

1. 哪些東西會變？（不同的文件格式、不同的 embedding 模型、不同的向量資料庫）
2. 哪些東西不會變？（先檢索後生成的流程、輸入是文字輸出是文字）
3. 誰協調誰？哪個 class 是「知道整個流程」的那個？
4. 如果六個月後要從 OpenAI embeddings 換成自訂模型，需要改幾個 class？
5. 如果要加上快取層，它插在哪裡？需要改現有 class 嗎？

---

## 七、講師備注

### 節奏控制

本模組資訊密度高，容易超時。關鍵控制點：

- Slide 06（SOLID）是最容易拖長的。每條原則不超過 4 分鐘，概念 + 一個例子 + 一個症狀就足夠。深度留給 Workshop。
- Slide 07（設計模式）的三個模式只做「意圖介紹」，不做完整的 Gang of Four 格式講解。學員在 Workshop 2 會自然應用它們。
- Workshop 是模組的核心，不能壓縮。如果前面 slides 超時，壓縮 Slide 10 的 LangChain 部分。

### 和 Course 1 的連接

開場時可以說：「Course 1 你學了 class 的語法。今天我們問的問題不是『class 怎麼寫』，而是『class 該怎麼設計』。這是一個完全不同的問題。」

如果班上有學員沒修過 Course 1，Slide 02 要多留一點時間確認基礎概念沒有問題。

### 常見學員困惑

**「SOLID 感覺很抽象，我什麼時候才會自然地用到它？」**

答：SOLID 原則在你設計 class 的當下可能感覺是約束，但在你六個月後回來改自己的程式碼時，你會開始感謝它。在 Workshop 1 裡，你已經在改「沒有遵循 SOLID 的程式碼」了——痛感就是答案。

**「繼承和組合到底什麼時候選哪個？」**

答：預設選組合。只有當你能清楚說出「X is-a Y，而且這個 is-a 關係在未來不會改變」時，才選繼承。在 Python 的 AI 應用中，超過 80% 的情況應該選組合。

**「設計模式是不是必須學？」**

答：不需要把 23 個 GoF 模式全部背下來。今天講的三個（Strategy、Observer、Factory）涵蓋了 AI 應用中 90% 的設計模式使用場景。其他模式在你遇到具體問題時再學。

### 延伸閱讀推薦

- Robert C. Martin, *Clean Code*（第 8-10 章關於 class 設計）
- Eric Evans, *Domain-Driven Design*（關於如何識別真實世界的物件）
- scikit-learn 原始碼的 `base.py`（最好的 Python OOP 教材之一）
- LangChain LCEL 文件（現代 Python OOP 的實際應用）

### 評估問題（用於課後自我檢測）

1. 說出一個你現有程式碼中違反 SRP 的例子，並描述如何重構它。
2. 為什麼說「優先選組合而非繼承」？舉一個組合比繼承更合適的場景。
3. 用一句話說明 DIP 和 Strategy Pattern 的關係。
4. 你正在設計一個可以替換 LLM 提供者的系統。你會定義什麼抽象介面？它需要哪些 abstract method？
5. 一個 `DataPipeline` class 有 500 行，包含資料讀取、清洗、特徵工程、儲存四個部分。違反了哪條 SOLID 原則？如何拆分？

---

## 八、與其他模組的連接

### 往前連接（來自 M1）

M1 建立了「程式是什麼」的第一原理視角：程式是對計算的描述，資料和行為是其核心構成要素。M2 把這個視角往上一層：class 是封裝資料（attribute）和行為（method）的機制。物件就是「有行為的資料」。

### 往後連接（通往 M3）

M3 的進階 Python 工程建立在今天設計好的 class 基礎上：

- 型別提示（type hints）讓抽象介面變成靜態可驗證的契約
- 例外處理（exception handling）讓 class 在失敗時行為可預測
- 測試（testing）讓「可替換性」從設計原則變成可驗證的事實
- logging 讓 Observer Pattern 有了工程層面的實作

### 往後連接（通往 M6-M7）

M6 的系統設計和 M7 的架構模式，是今天學到的概念在更大尺度上的延伸：

- 微服務是把 Package 層次的職責分離推到網路邊界
- API 設計是封裝原則在服務層面的體現
- 事件驅動架構是 Observer 模式在分散式系統中的實現
- 依賴注入容器（DI container）是 DIP 在框架層次的系統化實作

---

*M2 完*
