# 02 — M2 三透鏡分析（First Principles / Fundamentals / BoK）

> **文件定位**：用三個獨立透鏡重新解構 M2，驗證教材的論述基礎是否牢靠。
> **對象**：內部架構師、課程總監、跨模組教材協調人。
> **立場**：不把教材視為既定，而是重新推導。若第一性原理推不出教材裡的某個結論，該結論就是弱的。
> **使用方式**：三個透鏡獨立讀完後，看「合流建議」落回 M2 的修訂 action。

---

## Lens 1 — First Principles（第一性原理）

### 1.1 抽象的本質

**問題**：為何需要抽象？

**推導**：
- 人類工作記憶（Miller 1956）上限約 7±2 個 chunk。
- 一個中等複雜度系統的元素數遠超過 7。
- 唯一的工程對策：**把多個元素打包成一個 chunk**，讓高層思考時只操作少數符號。
- 打包的關鍵條件：**打包後的對外介面，資訊量要遠小於內部資訊量**。

**推論**：抽象 = 把「相同行為」分離出「變動資料」，讓呼叫者只看到行為，不看到資料。

這直接對應 M2 Slide 2 的「class 是合約」，但 M2 的說法偏弱。正確版本是：

> **抽象的本質是資訊不對稱的人工建構。你刻意讓外部看不到內部，才換來可組合性。**

### 1.2 Object = state + behavior + identity

Alan Kay 1966（Smalltalk 原始設計）：object 的三要素。

| 要素 | 意義 | Python 實作 |
|---|---|---|
| state | 當下的資料 | `self.__dict__` |
| behavior | 對 state 的操作 | methods（bound functions） |
| identity | 獨立存在性 | `id(obj)` / `is` 比較 |

M2 Slide 4 只談了 state，identity 一筆帶過，behavior 與 state 的耦合講了但沒給名字。三要素少一個，就不是完整的 object 概念。

**推論**：M2 必須明講三要素，這是 object 不可分割的最小單位。

### 1.3 資訊隱藏的資訊理論基礎

**問題**：為何 encapsulation 有效？

**資訊理論角度**：
- 系統耦合度 ∝ 模組間可交換資訊的位元數（mutual information）。
- 降耦合 = 限制 interface 的資訊頻寬。
- encapsulation 就是**強制把 interface 的位元數壓縮到最小必要集**。

**實務推論**：
- public interface 越小，模組越可替換。
- 若某個 class 的 public method 超過 10 個，大概率設計有問題（職責過廣）。
- 這是為何 scikit-learn 所有 estimator 只有 `fit` / `predict` / `transform` 三個核心 method——它在刻意壓縮介面熵。

M2 Slide 5 講「邊界與信任」，方向對，但沒給出「介面越小越好」這個可量化準則。

### 1.4 為何「組合優於繼承」是第一性原理的直接推論

- 繼承 = 子類別和父類別共享**完整內部狀態 + 完整行為**。
- 資訊頻寬：極高（所有 protected member 都是介面的一部分）。
- 組合 = 持有者只透過被持有者的 public interface 互動。
- 資訊頻寬：等於 public interface 的位元數。

**結論**：繼承是最高頻寬的耦合，組合是最低頻寬。從資訊理論角度，**composition 永遠是耦合下界更低的選擇**。繼承只有在需要 Liskov 替換（LSP）時才划算。

M2 Slide 7 的立場正確，但論證薄。建議改用此推導補強。

---

## Lens 2 — Fundamentals（學科基本功）

### 2.1 OOP 四大支柱

| 支柱 | 定義 | Python 實作關鍵 | M2 覆蓋度 |
|---|---|---|---|
| **Encapsulation** | 把 state 與 behavior 綁在一起，並控制對外可見性 | `_` / `__` 慣例、`@property` | ✅ Slide 5 |
| **Abstraction** | 用介面掩蓋實作 | `abc.ABC`、`typing.Protocol`、duck typing | ⚠️ 只講 class，沒講 Protocol |
| **Inheritance** | 從既有 class 建立特化 class | `class Child(Parent):`、`super()`、`__mro__` | ⚠️ Slide 7 提及但無 MRO |
| **Polymorphism** | 同一介面呼叫不同實作 | duck typing、`__magic__` methods、`singledispatch` | ❌ 幾乎沒提 |

**缺口**：M2 對 abstraction 的處理過度等同於 class，對 polymorphism 幾乎不提。但真實 AI 工程的 polymorphism 到處都是（`len(df)` 對 DataFrame/list/dict 都成立）。

### 2.2 Python-Specific 慣例 Checklist

下列每一項，M2 教材都應該在某張投影片覆蓋：

- [ ] **everything is an object**：function、module、class 本身都是 object。
- [ ] **class 本身是 type 的 instance**（`type(Dataset) is type`）。
- [ ] **name mangling (`__`)**：不是隱私機制，是避免子類別衝突。
- [ ] **`__slots__`**：限制 attributes、節省記憶體，AI 高頻 object 必備。
- [ ] **`@dataclass`**：2026 年寫資料 class 的預設。
- [ ] **`typing.Protocol`**：structural typing，Python 抽象的當代最佳實踐。
- [ ] **`@classmethod` / `@staticmethod`**：factory pattern 的 Python 慣用寫法。
- [ ] **`__repr__` 永遠要寫**，`__str__` 選擇性。
- [ ] **`__eq__` 寫了就要寫 `__hash__`**（或設 `__hash__ = None`）。
- [ ] **不要繼承 `object`**（Python 3 隱式繼承，明寫是 Python 2 殘留）。
- [ ] **MRO / `super()`**：多重繼承必備，單繼承也建議用 `super()` 不用硬寫父類別名。
- [ ] **`__init_subclass__` / descriptor**：進階但存在，點到為止即可。

**M2 目前覆蓋度**：13 項中只覆蓋 3 項（`_`、`__init__`、`@property`）。這個缺口是 reviewer 級別的。

### 2.3 dataclass vs attrs vs pydantic 取捨

這是 2026 年 Python class 設計的真實決策點：

| 維度 | `@dataclass` | `attrs` | `pydantic` |
|---|---|---|---|
| 標準庫 | ✅ | ❌ | ❌ |
| 樣板碼 | 低 | 最低 | 中（定義 schema） |
| 型別驗證 | 不驗證 | 可選 | 預設驗證 |
| 效能 | 最快 | 快 | 有驗證開銷 |
| AI/LLM 場景適用 | 內部資料 | 進階配置 | **API 邊界、tool calling schema** |
| 序列化 | 要手動 | 要 `asdict` | 內建 `model_dump_json` |

**M2 應教 `@dataclass`**，`attrs` / `pydantic` 在 AI 應用連結裡點名即可（pydantic 在 LangChain / OpenAI function calling 是事實標準）。

### 2.4 組合優於繼承的操作準則

1. **預設用組合**。
2. 只有當「子類別是父類別的一種」且「子類別完全可以替換父類別」（LSP 成立）時，才用繼承。
3. 不要繼承超過 2 層。
4. 不要繼承你不擁有的 class（第三方函式庫）——用 wrapper（composition）包起來。

### 2.5 Duck Typing 與 Protocol

```python
# 傳統 OOP（Java 風）：靠 inheritance
class CSVLoader(BaseLoader): ...

# Python 慣用 1：duck typing（無型別標註）
def run(loader):
    loader.load()  # 只要有 load 就行

# Python 慣用 2：Protocol（structural typing + 型別檢查）
from typing import Protocol
class Loadable(Protocol):
    def load(self) -> None: ...

def run(loader: Loadable) -> None:
    loader.load()
```

Protocol 是 Python 3.8+ 的正解，它保留 duck typing 的彈性，又得到 mypy / IDE 的型別檢查。M2 教 `BaseLoader` 而不教 Protocol，是落後於 2020 年後的社群共識。

### 2.6 Module vs Package vs Namespace Package

| 類型 | 定義 | 標記 |
|---|---|---|
| Module | 單一 `.py` 檔，或 built-in C extension | `.py` 存在 |
| Regular Package | 含 `__init__.py` 的資料夾 | `__init__.py` 存在 |
| Namespace Package (PEP 420) | 不含 `__init__.py` 的資料夾，可跨多個路徑合併 | 無 `__init__.py`，且該目錄在 `sys.path` 相關路徑下 |

**`__init__.py` 的歷史**：
- Python 2：package 的唯一標記。
- Python 3.3（PEP 420，2012）：引入 namespace package，`__init__.py` 變成 optional。
- 實務：99% 情況仍該寫 `__init__.py`，tooling 相容性最好。
- 反模式：在 `__init__.py` 放重邏輯、大量 `import *`、或 side effect——會讓 `import` 慢且難 debug。

### 2.7 AI 聊天機器人為何必須 OOP

從第一性原理推：

1. **每個 session 是一個獨立的狀態容器**——這就是 object 的定義。
2. **狀態跨時間存在**（對話歷史、tool call 中間態、memory）——function scope 無法承載。
3. **狀態要可序列化/復原**——OOP 天然支援 `to_dict` / `from_dict`。
4. **多個 agent 實例並存**（multi-agent 系統、A/B test）——object 的 identity 天然支援。
5. **行為多態**（同一個 `ask(question)` 介面，背後可能是 GPT-4、Claude、Gemini）——polymorphism 天然支援。

這五點同時成立，就是 OOP 的完美 use case。換成 function + 全域字典會每一條都痛。

---

## Lens 3 — BoK（Body of Knowledge）對齊

### 3.1 SWEBOK v3 / v4 Software Design 章節對齊

| SWEBOK 章節 | M2 是否覆蓋 | 評估 |
|---|---|---|
| Design Concepts: Abstraction | 部分 | 只講 procedural abstraction，缺 data abstraction 與 control abstraction |
| Design Concepts: Information Hiding | 部分 | Slide 5 對到，但沒引用 Parnas 1972 的理論基礎 |
| Design Concepts: Coupling & Cohesion | 未覆蓋 | 必須補，這是 modular design 的核心測量指標 |
| Design Concepts: Modularity | 部分 | Slide 8-9 有提到，但沒給出「高內聚低耦合」的判準 |
| Design Strategies: Object-Oriented Design | 主體覆蓋 | 四大支柱缺一（polymorphism） |
| Design Patterns | 刻意不教 | 取捨合理，24 小時課不該教 |
| Architectural Styles | 未覆蓋 | M2 範圍外，M8 再處理 |

**對齊缺口**：coupling / cohesion 應該在 Slide 7 或 Slide 11 引入。這兩個詞不教，學生評估自己 package 結構好壞時沒有標準。

### 3.2 SEBoK (Systems Engineering BoK) 對齊

| SEBoK 概念 | M2 對應 |
|---|---|
| System boundary | Slide 5 的「邊界與信任」對應 |
| Interface definition | Slide 7 的 class contract 對應 |
| Modular decomposition | Slide 8-11 的 module/package 拆解對應 |
| System of Systems | M2 範圍外 |

SEBoK 強調 **interface is the system**。介面定義好了，系統就完成了大半。M2 應該在 Slide 10（AI OOP 全景）強化這點：scikit-learn 的 `fit/transform` 介面穩定二十年，內部實作換了無數次——這才是抽象的勝利。

### 3.3 ACM Computing Classification / IEEE 相關標準

- IEEE 1016 Software Design Descriptions：M2 的 package 結構圖可視為 design viewpoint 的教學版。
- ISO/IEC/IEEE 42010 Architecture Description：M2 的「class 作為 design element」對應 architectural element 概念。

這兩個標準不必在課堂引用，但教材撰寫者應知道自己在教的是什麼層級。

---

## 合流建議（三透鏡匯流到 M2 修訂行動）

從三個透鏡獨立看，M2 共同指向同一組修訂優先序：

### P0（非改不可，影響知識正確性）

1. **補 `@dataclass`**（Fundamentals + 時代共識）。插入點：Slide 3 補一個對照版本。
2. **補 `typing.Protocol` / duck typing**（First Principles 的抽象本質 + Fundamentals 的 polymorphism）。插入點：Slide 7。
3. **補 polymorphism 作為第四支柱**（Fundamentals + BoK 對齊 SWEBOK）。插入點：Slide 10 明講 `fit/transform` 是 polymorphism。
4. **補 object 三要素（state/behavior/identity）**（First Principles 完整性）。插入點：Slide 4 標題改為「Object = state + behavior + identity」。

### P1（該改，影響 reviewer 可信度）

5. **補 coupling / cohesion 作為判準**（BoK 對齊 SWEBOK）。插入點：Slide 7 與 Slide 11。
6. **補 `__mro__` 一張圖**（Fundamentals 的 inheritance 完整性）。插入點：Slide 7。
7. **補 `__init__.py` 歷史與 namespace package**（Fundamentals 的 module 完整性）。插入點：Slide 9。
8. **補資訊隱藏的資訊理論定位**（First Principles 理論基礎）。插入點：Slide 5 一句話註腳。

### P2（加分，提升內容深度）

9. **補 dataclass / attrs / pydantic 三者取捨**。插入點：AI 應用連結章節。
10. **補 chatbot 非 OOP 不可的五個理由**。插入點：Slide 4 或 AI 應用連結。
11. **補 async agent 預告**。插入點：Slide 12 銜接段。

### 教學負荷評估

- P0 四項預估增加 15 分鐘教學時間 → 壓縮 Slide 1（腳本痛點）5 分鐘 + Slide 8（進化路徑）5 分鐘 + 工作坊 1 縮 5 分鐘即可吸收。
- P1 三項以「加註腳 / 補一張圖」形式插入，不佔主線時間。
- P2 三項進閱讀材料，不進投影片。

**最終立場**：M2 框架正確，方向正確，但在 2026 年的 Python 生態裡，內容細節已經落後約 5–8 年。P0 不修，這個模組撐不過三年；P0 修了，架構依然站得住。
