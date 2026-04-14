# 01 — M2 On-Page 註記（Reviewer Notes）

> **文件定位**：M2「OOP 與程式抽象」逐頁技術審閱註記。
> **對象**：內部技術架構 review 會議參與者、M2 教材維護者。
> **立場**：把自己當成嚴格的 reviewer，不是學生。每個知識點都要能被挑戰、補強、或退回。
> **符號**：🎯 宏觀（策略與定位）／🔬 細部（技術與實作）／⚠️ Reviewer 提問（必須被回答的疑點）。
> **使用方式**：對照 `M2_OOP與程式抽象.md` 逐節閱讀。紅字是我認為現行教材缺漏、誤導、或需要補齊的地方。

---

## 模組定位說明（原文行 10-18）

🎯 **宏觀**：定位清楚，「把資料和行為綁在一起」這句話抓對了抽象的核心。不講 SOLID、不講 Design Patterns，這是正確的取捨——24 小時課程沒本錢教那些。

🔬 **細部**：原文用「線性腳本會垮掉」當入口，這在教學上有效，但 reviewer 要小心一件事：**學生很容易把「用 class 包起來」誤認為「就是 OOP」**。包起來只是語法，OOP 的核心是把「變動的資料」和「共用的行為」分離。

⚠️ **Reviewer 提問**：
- 為何完全不碰 SOLID？至少 SRP（單一職責）與 DIP（依賴反轉）在後面講 composition 時會被隱性用到，不明講會讓學生知其然不知其所以然。建議在 Slide 7 加一句「這就是依賴反轉的雛形」。
- 「讓系統活得久」這句話是對的，但缺乏量化：什麼叫久？建議補一句：「當你的程式碼被第二個人讀、或六個月後的你自己讀時，還能被理解與修改。」

---

## 模組學習目標（原文行 20-30）

🎯 **宏觀**：六個目標都可驗證，這點做得好（大多數課程大綱的目標是不可驗證的形容詞）。

⚠️ **Reviewer 提問**：
- 目標 4「判斷 inheritance 還是 composition」太難，24 小時課程學生做不到「判斷」，只做得到「在這個場景選 composition」。建議弱化為：「在資料管線與 agent 場景預設用 composition，並能說出一個理由。」
- 缺少一個關鍵目標：**能讀 traceback 定位到 class/module**。這個在 debug 真實 package 時天天用。

---

## 關鍵概念清單（原文行 33-46）

🎯 **宏觀**：九個概念收斂得乾淨。

🔬 **細部 — 必須補齊的概念**：

| 缺漏概念 | 為何非補不可 |
|---|---|
| **class vs type** | Python 的 `class` 建立出的就是 `type` 的實例（`type(Dataset) is type` 為 True）。不講這個，學生永遠搞不清楚 metaclass、`isinstance` vs `type()` 的差別。 |
| **identity / equality** | `is` vs `==` 是 OOP 第一天就會踩的坑。object 有三個屬性：identity、type、value，教材只提了 value（state）。 |
| **`__mro__` / Method Resolution Order** | 講 inheritance 不講 MRO 是知識漏洞。即使不講多重繼承，也要知道 `Child.mro()` 的存在，否則 debug `super()` 時會卡住。 |
| **duck typing 與 `typing.Protocol`** | 這是 Python 做抽象的真正方式。scikit-learn 的 `fit/transform` 就是 structural typing，不是 inheritance。教 class contract 卻不提 Protocol 是錯的。 |
| **`dataclass` / `attrs` / `pydantic`** | 教材完全沒提 `@dataclass`。2026 年寫 Python class 不用 dataclass 幾乎是錯誤示範。三者取捨：`dataclass`（標準庫、零相依、最輕）vs `attrs`（功能多但要外部套件）vs `pydantic`（有驗證、AI/LLM 場景預設，但有效能開銷）。 |
| **namespace package（PEP 420）** | 只提有 `__init__.py` 的 package，沒提 namespace package。雖然實務上少用，但 reviewer 來看會指出這是錯誤陳述。 |

⚠️ **Reviewer 提問**：
- `method` 定義為「屬於這個 class 的函數」——不夠精確。method 是 **descriptor**，`instance.method` 會走 `__get__` 綁定。這對 M2 太深，但請至少不要說「method 就是函數」，要說「method 是綁定到物件的函數」。

---

## Slide 1 — 腳本為什麼會垮掉（原文行 72-86）

🎯 **宏觀**：入口正確。痛點（邏輯分散、狀態難追蹤、測試不可能）三點到位。

⚠️ **Reviewer 提問**：
- 「可以跑 ≠ 可以維護」這句是本 slide 的 money line，但視覺上放底部太小。建議放大到佔視覺 40%。
- 少了一個關鍵痛點：**合作成本**。生產環境真正的崩潰點是「兩個人同時改這個腳本」，不是單人維護。

---

## Slide 2 — 從函數到物件（原文行 90-104）

🎯 **宏觀**：「黃金標準：當一組資料和一組函數總是一起出現，就是該包成 class 的訊號」——這句講得準，是本 slide 的 governing thought。

⚠️ **Reviewer 提問**：
- 「class 是一份合約」這個隱喻好，但下一句又退回到「有什麼資料、能做什麼事」，弱化了合約的力道。合約的重點是**對外承諾**，不是**內部組成**。建議改：「class 是一份對外承諾：給定這些輸入，你會得到這些行為與狀態變化。」
- **反向提醒必須加**：「不是所有東西都該寫成 class」。純 function + dataclass 常常更好。這個警告不加，學生會 class 病發作（everything is a hammer）。

---

## Slide 3 — Class 最小可用語法（原文行 108-145）

🔬 **細部**：
- `__init__` 不是建構子這段講對了，建構子是 `__new__`。但 reviewer 要問：你講了 `__init__` 不是建構子，卻不講 `__new__` 存在，學生會更混亂。要嘛兩個都不提（統一叫「初始化」），要嘛一句話帶過 `__new__`。
- 範例程式缺 `@dataclass` 版本對照。2026 年的範例只有這種手寫 `__init__` 版本是時代錯置。

⚠️ **Reviewer 提問**：
- `self` 的解釋「不是魔法，是慣例」——精確，加分。但要補：`self` 只是第一個參數的慣例名稱，理論上可以叫 `this`、`me`，Python 不在乎。這個補充能破除神秘感。
- `class attribute` vs `instance attribute` 的陷阱沒講：當 class attribute 是 mutable（例如 `supported_formats = []`）時，所有 instance 會共享同一個 list，這是 Python 新手 top 3 的地雷。**必須加一個警告框**。

---

## Slide 4 — Object 是什麼（原文行 149-175）

🎯 **宏觀**：用 chatbot 對話歷史當例子，精準。AI 聊天機器人的狀態管理確實是本模組最說服人的 use case。

🔬 **細部 — 為何 chatbot 非 OOP 不可**：
1. **Session 隔離**：每個使用者一個 `ChatAgent` instance，`self.history` 天然隔離，不需要手動傳 session_id。
2. **狀態的生命週期**：history 要在整個 conversation 存活，function scope 無法承載。
3. **可序列化**：OOP 讓 `agent.to_dict()` / `ChatAgent.from_dict(d)` 成為自然介面，支援暫存/復原。
4. **中介狀態**：LLM agent 常有 `_pending_tool_calls`、`_reasoning_trace`，這些都是典型的內部狀態。

⚠️ **Reviewer 提問**：
- `id()` 示範記憶體位址——在 CPython 成立，在 PyPy / Jython 不保證。要加一句「在 CPython 實作下」。Reviewer 不加這句會被打槍。
- 完全沒提 `__eq__` / `__hash__`。講 identity 不講 equality 是殘缺的。建議 Slide 4 加一段：「identity（`is`）比的是位址；equality（`==`）比的是你在 `__eq__` 定義的內容。」

---

## Slide 5 — Encapsulation（原文行 179-211）

🎯 **宏觀**：「邊界與信任」這個框架對了。Encapsulation 的本質不是隱藏，是**降低耦合面**。

🔬 **細部**：
- `__` name mangling 提到「實務上很少用」——同意，但要說清楚它**不是為了隱私**，是為了避免子類別意外覆蓋父類別屬性。這個誤解非常普遍。
- `@property` 範例好，但缺 setter 範例。`@data.setter` 才完整展示「公開介面、內部驗證」這個概念。

⚠️ **Reviewer 提問**：
- 資訊隱藏的理論基礎沒講：Parnas 1972「On the Criteria To Be Used in Decomposing Systems into Modules」。這是 SWEBOK 明列的 Design Principle。24 小時課不必引用，但講師心裡要有。

---

## Slide 6 — 工作坊 1（原文行 215-253）

🎯 **宏觀**：三關卡切分合理，25 分鐘合理。

⚠️ **Reviewer 提問**：
- 關卡 2 要求 fluent interface（`return self`）——這是個有爭議的 pattern。pandas 走 fluent，scikit-learn 不走（`fit` 回傳 `self` 但使用者不常鏈）。建議補一句：「鏈式呼叫方便但會讓 debug 變難，慎用。」
- 缺驗收腳本。工作坊應該附一個 `test_workshop1.py` 讓學生能 `pytest` 自驗，而不是靠講師觀察。

---

## Slide 7 — Inheritance vs Composition（原文行 257-296）

🎯 **宏觀**：選了正確立場（預設 composition），這是 2026 年業界共識。Gamma et al. 1994「Favor composition over inheritance」三十年後依然成立。

🔬 **細部 — 必須補齊**：

1. **duck typing & `Protocol`**：CSVLoader 繼承 BaseLoader 在 Python 不是必要的。只要 `validate()` 存在，duck typing 就成立。用 `Protocol` 表達更乾淨：

```python
from typing import Protocol

class Loader(Protocol):
    def validate(self) -> bool: ...

class CSVLoader:  # 不繼承任何東西
    def validate(self) -> bool: ...
```

這才是 Python 慣用做法。範例中用 `class CSVLoader(BaseLoader)` 是 Java-ism，教材裡沒澄清會誤導。

2. **`__mro__`**：至少一張圖展示 `CSVLoader.__mro__` 是 `[CSVLoader, BaseLoader, object]`。

3. **abstract base class**：如果真要用繼承，應該用 `abc.ABC` + `@abstractmethod`，而不是 `raise NotImplementedError`。後者是 1998 的寫法。

⚠️ **Reviewer 提問**：
- 「改父類別子類別會受影響」這個論點太淡化，應該強化：**繼承是最強耦合**（同步變更的強制性），composition 是最弱耦合。這是為什麼預設 composition。

---

## Slide 8 — 腳本進化路徑（原文行 300-315）

🎯 **宏觀**：五階段梯度合理。

⚠️ **Reviewer 提問**：
- Notebook → Service 這條路隱含單向演化假設，但實務上 Notebook 在探索、Service 在部署，**兩者會長期共存**。建議補：「這不是一條單向路，是一個光譜，專案不同位置用不同階段。」
- 缺「Library」這個節點：你的 package 可能是 internal library（pip install），不一定要變 service。

---

## Slide 9 — Module 與 Package（原文行 319-348）

🔬 **細部 — `__init__.py` 的歷史包袱必須講**：

1. **為何需要 `__init__.py`**：Python 2 時代，`__init__.py` 是 package 的唯一標記。
2. **PEP 420 namespace package（Python 3.3+）**：沒有 `__init__.py` 的資料夾也可以是 package（namespace package），但有限制（不能有 `__init__` 初始化、跨路徑合併）。
3. **實務建議**：明確的 package 一定要 `__init__.py`，哪怕是空的。這讓 tooling（mypy、pytest、IDE）行為可預測。
4. **`__init__.py` 不該放重邏輯**——教材有提到，但沒解釋原因：因為它會在 `import package` 時就執行，放重邏輯會讓 import 時間爆炸，且造成 circular import。

⚠️ **Reviewer 提問**：
- import 搜尋順序教材寫「sys.modules → 內建 → sys.path」——順序對，但少了 **meta path finders / path hooks**（`sys.meta_path`）。這對 24 小時課太深，但講師應該知道。
- 絕對匯入 vs 相對匯入教材輕描淡寫。建議補 rule of thumb：「package 內部用相對匯入（`from .loader`），外部呼叫用絕對匯入。」

---

## Slide 10 — AI 工程 OOP 全景（原文行 353-373）

🎯 **宏觀**：五個 class 挑得好，完整覆蓋 AI pipeline。

⚠️ **Reviewer 提問**：
- scikit-learn 的 `fit/transform` 是 **structural typing / duck typing**，不是 class contract（Pipeline 不檢查 inheritance，只檢查有沒有 method）。教材用「class contract」一詞會誤導，建議換成「介面契約（interface protocol）」。
- `ChatAgent` 的範例缺 `async` 版本。2026 年實務上 LLM agent 幾乎都是 async（`async def ask`）。這對 M2 可能太早，但建議 Slide 12 銜接裡預告。

---

## Slide 11 — 工作坊 2（原文行 378-423）

🎯 **宏觀**：30 分鐘拆解 200 行腳本成 package，節奏緊但可完成。

⚠️ **Reviewer 提問**：
- 缺「如何驗證重構成功」的標準。建議要求：重構前後執行 `train.py`，最終 metrics 完全一致（bit-for-bit 相同）。這是業界 refactoring 的黃金標準（Fowler）。
- `__init__.py` 在這個工作坊該放什麼沒明說。建議統一答案：每個子 package 的 `__init__.py` 做 re-export（`from .dataset import Dataset`），讓外部 `from ml_project.data import Dataset` 能 work。

---

## Slide 12 — 總結（原文行 427-448）

🎯 **宏觀**：銜接 M3/M4/M7 做得好，給學生一個 why now 的理由。

⚠️ **Reviewer 提問**：
- 自我檢測清單六點都可驗證，但缺一項：「我能畫出這個 package 的依賴圖（哪個 module import 哪個）」。能不能畫出依賴圖，是判斷學生真的懂 package 還是只會照抄結構的試金石。

---

## 跨頁結構性批判（Reviewer 收尾）

1. **完全沒教 `@dataclass`**：這是最大漏洞。2026 年寫 Python value object 的第一選擇就是 dataclass。M2 不教 dataclass，學生進職場第一天就會被同事改 code。
2. **Protocol / duck typing 缺席**：這是 Python 做抽象的靈魂，現行教材仍停留在 Java 風格的 inheritance 思維。
3. **`__mro__` / `super()` 沒提**：只要教 inheritance，就必須教 MRO，不然 debug 時卡死。
4. **缺 testing mindset**：OOP 的最大價值之一是可測試性，但整個 M2 完全沒提 pytest 或 mock。至少 Slide 5 或 11 應該示範「因為有 encapsulation，所以我能 mock `_store`」。
5. **`__init__.py` 歷史沒講**：會被資深 reviewer 指出是知識空洞。

**修訂優先序建議**：
- P0（必改）：補 `@dataclass`、補 duck typing/Protocol、補 mutable class attribute 警告。
- P1（該改）：補 `__mro__` 一張圖、`__init__.py` 歷史一段、ABC 正確寫法。
- P2（加分）：補 async chatbot 預告、補 namespace package 註腳、補 identity vs equality。
