# Ch04 · MVK 速學卡（Minimum Viable Knowledge）

> 15 分鐘讀完 = Ch04 1.5 小時精華。進 Ch05 前的最低門檻。

---

## 一、核心主張（一句話）

**腳本解決問題，類別解決規模。** OOP 的價值不在語法，在把散落的狀態收進一個可重用、可測試、可組合的殼。

---

## 二、四個關鍵詞（硬記）

| 關鍵詞 | 比喻 | Python 裡長什麼樣 |
|--------|------|--------------------|
| Class | 建築藍圖 | `class DataPipeline:` |
| Object（Instance） | 蓋出來的房子 | `pipe = DataPipeline("ETL")` |
| `__init__` | 誕生禮 | 實例化時自動呼叫一次 |
| `self` | 身分證 | 指向當前物件，慣例名不是關鍵字 |

---

## 三、最小可用類別（背下來）

```python
class DataPipeline:
    def __init__(self, name):
        self.name = name
        self.steps = []           # 可變屬性放 __init__！

    def add_step(self, step):
        self.steps.append(step)
        return self               # Ch05 method chaining 伏筆

pipe = DataPipeline("ETL_v1")
pipe.add_step("read_csv")
```

---

## 四、Class Attribute vs Instance Attribute（最常考陷阱）

```python
# BAD — 所有實例共用同一個 list
class Bad:
    data = []

a, b = Bad(), Bad()
a.data.append(1)
b.data           # [1]  ← 被污染！

# GOOD — 每個實例獨立
class Good:
    def __init__(self):
        self.data = []
```

**鐵律**：可變物件（list / dict / set）**絕不**放類別頂端，一律放 `__init__`。

---

## 五、何時該用 Class Attribute

| 用途 | 範例 | 備註 |
|------|------|------|
| 常數 | `PI = 3.14159` | 不可變 |
| 預設設定 | `DEFAULT_ENCODING = "utf-8"` | 字串 OK |
| 計數器（配 classmethod） | `_count = 0` | 立刻升級為 classmethod |
| （禁） | `items = []` / `cache = {}` | 永遠是 bug |

---

## 六、self 三問（閉卷檢測）

1. **誰傳進來？** —— Python 自動把當前物件塞進第一個參數。
2. **指到哪？** —— 指到那一顆 instance，讀寫 `self.xxx` 就是讀寫它。
3. **不寫會怎樣？** —— 會 `TypeError: missing 1 required positional argument`；或變成類別層方法（未進階前別用）。

---

## 七、Ch04 紀律四條

1. 可變屬性（`list` / `dict` / `set`）一律放 `__init__`
2. `self` 不省略，不要用花俏名字（`me` / `this`）
3. 先想「狀態是什麼」再想「方法有什麼」
4. 單檔 50 行以下的腳本**不要**開類別——是增加複雜度

---

## 八、Ch04 → Ch05 → Ch10 銜接

```
Ch04 · 藍圖 + 誕生禮 + 身分證
   ↓ 加封裝、繼承、魔術方法
Ch05 · DataPipeline 變 BaseCleaner(ABC)
   ↓ 加 method chaining + pandas 整合
Ch10 · DataCleaner().read().clean().export()
```

本章是整個 M2 模組的地基。**地基不穩，上面再漂亮都會塌。**

---

## 九、自我檢核題（閉卷）

1. `class Foo: items = []` 為什麼危險？怎麼修？
2. `__init__` 與一般方法的差別是什麼？
3. `pipe = DataPipeline("X")` 這一行 Python 做了哪幾件事？
4. `self` 能不能改成叫 `me`？應該不應該？
5. 什麼情境下**不**該把腳本升級成類別？

> 答對 4 題以上 = 可進 Ch05。答錯 ≥ 2 題：回看 S7 / S10 / S12。
