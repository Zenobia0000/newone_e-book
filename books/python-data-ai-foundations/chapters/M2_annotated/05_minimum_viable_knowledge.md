# 05 — M2 Minimum Viable Knowledge（速學卡）

> **文件定位**：M2 的最小可用知識集。13 張速學卡，涵蓋「上線一個 AI 專案前必須會的 OOP」。
> **對象**：時間有限的工程師、review 前要快速補課的同事、需要為新進 junior 做 onboarding 的 team lead。
> **立場**：不求全，只求「少了這張就會在生產環境出事」。
> **使用方式**：每張卡 2 分鐘讀完，全部 13 張 30 分鐘內掃完。讀完後能答出每張卡底部的「自我檢測」，就算通過 M2 核心。

---

## 卡 01 — class vs object

**一句話**：class 是模板，object 是模板的實例；修改一個 instance 的 attribute 不會影響其他 instance。

**最小範例**：
```python
class Dataset:
    def __init__(self, path): self.path = path

a = Dataset("a.csv")
b = Dataset("b.csv")
a.path = "X"
print(b.path)   # "b.csv" — 不受 a 影響
```

**踩坑**：class attribute 若是 mutable（list/dict），**會被所有 instance 共享**。寫 `self.x = []` 在 `__init__` 裡，不要寫在 class body。

**自我檢測**：能用一句話說清楚 `type(Dataset)` 與 `type(a)` 的差別。（答：前者是 `type`，後者是 `Dataset`。）

---

## 卡 02 — `__init__`、`self`、attribute、method

**一句話**：`__init__` 是初始化（不是建構子），`self` 是物件對自己的稱呼，attribute 存狀態，method 存行為。

**最小範例**：
```python
class Counter:
    def __init__(self, start=0):
        self.n = start            # instance attribute

    def inc(self):                # method
        self.n += 1
        return self
```

**踩坑**：忘記寫 `self` 是 top 1 新手錯誤。method 的第一個參數永遠是 `self`（慣例名稱，理論上可換）。

**自我檢測**：`Counter().inc().inc().n` 會輸出什麼？（答：2，因為 `inc` 回傳 `self`，支援鏈式呼叫。）

---

## 卡 03 — `@property` 與 getter/setter

**一句話**：`@property` 讓 method 看起來像 attribute，外部用 `obj.x` 存取，內部可以執行驗證或 lazy 計算。

**最小範例**：
```python
class Dataset:
    def __init__(self): self._data = None
    @property
    def data(self):
        if self._data is None: raise RuntimeError("not loaded")
        return self._data
    @data.setter
    def data(self, value):
        if not hasattr(value, "shape"): raise TypeError
        self._data = value
```

**踩坑**：把所有 attribute 都包 `@property` 是過度工程；只有需要「驗證／惰性／變換」時才包。

**自我檢測**：什麼時候該用 `@property` 而不是直接暴露 attribute？（答：存取需要驗證、需要 lazy、或未來可能換實作時。）

---

## 卡 04 — Encapsulation 的 `_` 與 `__`

**一句話**：`_x` 是慣例（「請不要碰」）、`__x` 是 name mangling（真的會改名成 `_ClassName__x`，用於避免子類別衝突），不是隱私機制。

**最小範例**：
```python
class A:
    def __init__(self):
        self._internal = 1       # 慣例：外部不應直接碰
        self.__mangled = 2       # 被改名成 _A__mangled

a = A()
print(a._internal)               # 可以存取，但不該
print(a._A__mangled)             # 要用改名後的才能存取
```

**踩坑**：`__` 的目的常被誤解為「隱私」。它的真正目的是避免子類別覆寫。實務用 `_` 就夠。

**自我檢測**：子類別 `B(A)` 要覆寫 `__mangled` 會發生什麼？（答：`B.__mangled` 會變成 `_B__mangled`，和父類別的 `_A__mangled` 不衝突——這正是 name mangling 的用途。）

---

## 卡 05 — Inheritance + `super()` + `__mro__`

**一句話**：用 `super()` 呼叫父類別方法，別硬寫父類別名；`Class.__mro__` 告訴你方法解析的順序。

**最小範例**：
```python
class A:
    def hello(self): return "A"
class B(A):
    def hello(self): return super().hello() + "B"

print(B().hello())          # "AB"
print(B.__mro__)            # (B, A, object)
```

**踩坑**：多重繼承要看 MRO；寫 `A.hello(self)` 而不是 `super().hello()` 會在 diamond inheritance 出事。

**自我檢測**：單繼承下，為何還是建議用 `super()`？（答：日後若加入第二個父類別或 mixin，不需改既有程式。）

---

## 卡 06 — 組合優於繼承（Composition over Inheritance）

**一句話**：`has-a` 用組合（把別的 object 當 attribute 存），`is-a` 用繼承；不確定時用組合，因為耦合最低。

**最小範例**：
```python
class ChatAgent:
    def __init__(self, store, llm):
        self._store = store        # composition
        self._llm = llm
    def ask(self, q):
        ctx = self._store.search(q)
        return self._llm.complete(f"{ctx}\n{q}")
```

**踩坑**：繼承第三方函式庫的 class 是 anti-pattern；用 wrapper（composition）包起來。

**自我檢測**：`ChatAgent(store, llm)` 要換 vector DB，需要改什麼？（答：呼叫端改傳的 `store` 即可，`ChatAgent` 本身不動。）

---

## 卡 07 — Duck Typing 與 `typing.Protocol`

**一句話**：Python 不靠 inheritance 表達抽象，靠「有沒有對的 method」。`Protocol` 是 Python 3.8+ 的型別化 duck typing。

**最小範例**：
```python
from typing import Protocol

class Loadable(Protocol):
    def load(self) -> None: ...

class CSVLoader:                 # 不繼承任何東西
    def load(self) -> None: ...

def run(x: Loadable) -> None:
    x.load()                     # 只要有 load 就過

run(CSVLoader())                 # 通過，mypy 也承認
```

**踩坑**：不要寫 `class CSVLoader(BaseLoader)` 除非你真的需要共用實作；只需要「有 load」就用 `Protocol`。

**自我檢測**：scikit-learn 的 Pipeline 怎麼決定你寫的 class 能不能進？（答：看有沒有 `fit` 和 `transform` 方法，不看 inheritance。）

---

## 卡 08 — `@dataclass`（2026 年預設）

**一句話**：寫「裝資料的 class」第一選擇是 `@dataclass`，免寫 `__init__` / `__repr__` / `__eq__`。

**最小範例**：
```python
from dataclasses import dataclass, field

@dataclass
class TrainingConfig:
    lr: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)
```

**踩坑**：mutable default（`tags: list = []`）是 Python 最經典陷阱；必用 `field(default_factory=list)`。

**自我檢測**：何時選 `pydantic` 而不選 `dataclass`？（答：需要從外部資料（API、JSON、LLM 輸出）做型別驗證時。）

---

## 卡 09 — `__repr__` 與 `__eq__`

**一句話**：`__repr__` 永遠要寫（debug 必需），`__eq__` 要寫就同時寫 `__hash__`。

**最小範例**：
```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __repr__(self): return f"Point({self.x}, {self.y})"
    def __eq__(self, other): return (self.x, self.y) == (other.x, other.y)
    def __hash__(self): return hash((self.x, self.y))
```

**踩坑**：只寫 `__eq__` 不寫 `__hash__`，object 會變 unhashable（不能放 `set` / `dict` key）。`@dataclass(frozen=True)` 自動處理。

**自我檢測**：`is` 和 `==` 差在哪？（答：`is` 比 identity（記憶體位址），`==` 比 `__eq__` 定義的值。）

---

## 卡 10 — Module / Package / `__init__.py`

**一句話**：一個 `.py` 是 module、含 `__init__.py` 的資料夾是 package、`__init__.py` 做 re-export 不放重邏輯。

**最小範例**：
```text
ml_project/
├── __init__.py     # from .data import Dataset
├── data/
│   ├── __init__.py
│   └── dataset.py
```

```python
# ml_project/data/__init__.py
from .dataset import Dataset      # 讓外部可以 from ml_project.data import Dataset
```

**踩坑**：在 `__init__.py` 放重邏輯會讓 `import package` 超慢且容易 circular import。

**自我檢測**：為何 `__init__.py` 該盡量輕？（答：它在 `import package` 時就執行，重的副作用會拖慢整個程式啟動。）

---

## 卡 11 — 絕對匯入 vs 相對匯入

**一句話**：package 內用相對匯入（`from .sibling import X`），外部呼叫用絕對匯入（`from myproject.data import Dataset`）。

**最小範例**：
```python
# ml_project/features/pipeline.py
from ..data.dataset import Dataset    # 相對，兩層上
from ml_project.models.trainer import ModelTrainer  # 絕對
```

**踩坑**：script 直接跑含相對匯入的檔會爆（`ImportError: attempted relative import with no known parent package`）；要用 `python -m ml_project.features.pipeline`。

**自我檢測**：`python foo.py` 和 `python -m foo` 差在哪？（答：後者把 `foo` 當 module 執行，`__package__` 有值，相對匯入才 work。）

---

## 卡 12 — AI Chatbot 為何非 OOP 不可

**一句話**：對話歷史、tool call 中間態、session 隔離，三者都是長生命週期的狀態；函數無法承載。

**最小範例**：
```python
class ChatAgent:
    def __init__(self, llm):
        self._llm = llm
        self._history: list[dict] = []
    def ask(self, q: str) -> str:
        self._history.append({"role": "user", "content": q})
        ans = self._llm.complete(self._history)
        self._history.append({"role": "assistant", "content": ans})
        return ans
```

**踩坑**：把 `history` 放全域變數，多用戶場景會互相污染。每個 session 一個 `ChatAgent()`，天然隔離。

**自我檢測**：為何 agent 要寫成 class 而不是 function？（答：需要跨呼叫保存狀態、需要 session 隔離、需要序列化與復原。）

---

## 卡 13 — 重構檢核：何時該包成 class

**一句話**：當一組資料與一組操作它的函數「總是一起出現」或「需要跨呼叫記住狀態」，就該包成 class。

**判準（三取一即可）**：
1. 有 3 個以上函數接同一組參數。
2. 需要在呼叫之間保留中間狀態。
3. 需要多個實例獨立並存（multi-session、multi-model A/B test）。

**反向判準（不該包）**：
- 純資料不帶行為 → 用 `@dataclass` 或 `dict`。
- 無狀態純函數 → 放 `utils.py` 就好。
- 只會有一個實例且沒狀態 → 直接寫 function 或 module。

**自我檢測**：把 `def load_and_clean(path, drop_cols, fill_strategy)` 改寫成 class 合理嗎？（答：看情況——若之後要儲存 `df` 狀態、要支援 `add_feature` / `split`，就合理；若只是單次載入清理，function 就夠。）

---

## 總表：13 張卡覆蓋 vs SWEBOK/Fundamentals

| 卡號 | 對應 OOP 支柱 | SWEBOK 對齊 |
|---|---|---|
| 01–02 | Object 本質 | Design Concepts: Abstraction |
| 03–04 | Encapsulation | Design Concepts: Information Hiding |
| 05–06 | Inheritance + Composition | Design Strategies: OOD |
| 07 | Polymorphism (structural) | Design Strategies: OOD |
| 08–09 | Python 慣例 | Language-specific idioms |
| 10–11 | Modularity | Design Concepts: Modularity |
| 12 | AI 應用整合 | Architectural Application |
| 13 | 重構決策 | Design Concepts: Coupling & Cohesion |

**通過門檻**：13 張自我檢測能答出 ≥ 11 張，視為 M2 核心知識到位，可以開始 M3（NumPy）。
