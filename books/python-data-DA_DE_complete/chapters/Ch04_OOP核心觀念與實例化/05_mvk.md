# F3 · MVK 速學卡（Minimum Viable Knowledge）

> 離開本節後，你的肌肉記憶裡必須長出這五個反射。
> 對應 01_outline.md 的 5 個 Learning Objectives。

---

## ① 最小 class 骨架（對應 LO2）

```python
class DataPipeline:
    def __init__(self, name):
        self.name = name        # instance attribute
        self.steps = []         # 可變物件放 __init__！

    def add_step(self, step):
        self.steps.append(step)
        return self             # 留給 F5 chaining 的伏筆

pipe = DataPipeline("ETL_v1")
pipe.add_step("read_csv")
```

**記三個關鍵字**：`class` / `__init__` / `self`。三個都不是魔法，是可以背下來的固定劇本。

---

## ② 實例化三步驟（對應 LO3）

```python
pipe = DataPipeline("ETL_v1")
# 背後 Python 做的事：
# ① 建立空 instance obj
# ② 呼叫 DataPipeline.__init__(self=obj, name="ETL_v1")
# ③ 把 obj 綁到名字 pipe
```

**一句口訣**：建空殼 → 跑 `__init__` → 綁名字。任何 class 都一樣。

---

## ③ self 三問（對應 LO3）

| 問題 | 答案 |
|------|------|
| 誰傳進來？ | Python 把當前 instance 自動塞進第一個參數 |
| 指到哪？ | 指到那一顆 instance；`self.x = ...` 是寫入這顆物件 |
| 不寫會怎樣？ | `TypeError: ... takes 1 positional argument but 2 were given` |

**慣例提醒**：`self` 不是關鍵字，是 PEP 8 慣例。別改成 `me` / `this`。

---

## ④ Class Attribute 紅綠燈（對應 LO4）

```python
class Bad:
    items = []              # ✗ 所有實例共享同一 list！

class Good:
    VERSION = "1.0"         # ✓ 不可變常數 OK
    def __init__(self):
        self.items = []     # ✓ 每實例獨立
```

**鐵律**：
- 類別頂端只放**不可變**（int / float / str / tuple）→ 常數、版本號、預設字串
- 可變容器（list / dict / set）**一律**放 `__init__`

這是 Python OOP 最常見的 bug，Ruff 規則 `RUF012` 會檢查。

---

## ⑤ 何時該用 / 不該用 OOP（對應 LO1 + LO5）

| 情境 | 選擇 |
|------|------|
| 跨方法共享狀態 + 重複套用 | ✓ class |
| 一次性腳本 | ✗ function |
| 純函式轉換 (input → output) | ✗ function |
| 單一資料結構 + 少量欄位 | ✗ dataclass / NamedTuple |
| 需要 method chaining | ✓ class + `return self` |

**判斷準則**：兩個條件（跨方法共享狀態 + 重複套用需求）都有 → 用 class；只有一個 → function 即可。

---

## 五個必踩地雷（考前必背）

| # | 地雷 | 錯 | 對 |
|---|------|----|----|
| P1 | 過度設計 | 30 行一次性腳本硬包 class | function 即可 |
| P2 | 忘記 `self.` 前綴 | `def __init__(self, x): x = x` | `self.x = x` |
| P3 | 可變物件放類別頂端 | `class Bad: items = []` | 放 `__init__`：`self.items = []` |
| P4 | 省略 self 或亂改名 | `def __init__(name):` → TypeError | `def __init__(self, name):` |
| P5 | 方法不回傳 self | `def add_step(self, x): self.steps.append(x)` | 加 `return self` |

---

## 下一章銜接（F4 封裝 / 繼承 / 魔術方法）

> F4 在 F3 的 class 骨架上加三層：
> - **封裝**：`@property` 把內部細節藏起來，對外只露 getter
> - **繼承**：`class SalesPipeline(DataPipeline)` 直接沿用功能、只寫差異
> - **魔術方法**：`__repr__` / `__eq__` / `__len__` 讓你的類別支援 `print()` / `==` / `len()`
>
> **今天的 `self.xxx` 是地基**；沒有地基，F4 的裝修都沒處貼。

## 再下一章（F5 OOP + Pandas 實戰）

> 今天的 `DataPipeline` 雛形，在 F5 會長大成：
>
> ```python
> cleaner = DataCleaner("sales.csv")
> (cleaner.read()
>         .drop_duplicates()
>         .fill_missing("price", 0)
>         .clean_column_names()
>         .export("clean.parquet"))
> ```
>
> **今日的 `return self` 一行，就是明日 chaining 的骨架。**
