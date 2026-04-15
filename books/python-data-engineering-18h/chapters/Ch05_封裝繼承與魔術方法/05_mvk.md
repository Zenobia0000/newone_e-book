# Ch05 · Minimum Viable Knowledge

**章節**：封裝、繼承與魔術方法（M2 · 1.5 hr）
**Governing thought**：類別要守門，不是把變數塞在一起。

---

## 三根必帶走的柱子

### 1. 封裝 — 誰能改、怎麼改
- `x`（公開）／`_x`（禮貌提醒）／`__x`（name mangling，改名為 `_Class__x`）
- `@property` 是對外介面與內部實作的解耦器
- **Python 沒有 private**，一切靠慣例 + linter

### 2. 繼承 — 共用向上、差異向下
- `class Child(Parent):` + `super().__init__(...)`
- 覆寫（override）：同名方法，子類重新定義
- **本章只教單一繼承**；多重繼承 / MRO / ABC 留給進階
- 實務鐵則：**能用組合（HAS-A）不用繼承（IS-A）**

### 3. 魔術方法 — 讓類別說 Python 的母語
| 方法 | 誰會呼叫 | 口訣 |
|------|---------|------|
| `__str__` | `print(obj)` | 給人看 |
| `__repr__` | REPL / `repr()` | 給開發者看，最好能反貼重跑 |
| `__len__` | `len(obj)` | 有「數量感」才實作 |
| `__iter__` | `for x in obj` | 有「逐一處理」才實作 |

---

## Method Chaining（Ch10 鋪路）
- 每個方法 `return self`，就能寫出：
  ```python
  cleaner.read('data.csv').drop_na().normalize().export('out.csv')
  ```
- 結構 = 資料流 → 可讀性自然高

---

## 學生離開教室時應能

1. 看到 `_x` / `__x` 能說出「差別是 name mangling、不是 private」
2. 寫出帶 `@property` 與 `@setter` 的類別並解釋為何使用
3. 寫出單一繼承 + `super().__init__()` + override 的三層骨架
4. 為自訂類別實作 `__str__` / `__repr__` / `__len__` / `__iter__` 的判斷與範例
5. 設計一個支援 chaining 的類別（所有方法 `return self`）

## 本章刻意不教（Linus 原則：解決實際問題）

- 多重繼承 / 菱形繼承 / MRO（C3 linearization）
- `abc` 模組與 `@abstractmethod`
- `__new__` / metaclass
- `__slots__` 記憶體優化

## 銜接
- **Ch06**：I/O 與例外處理 — 會用本章的繼承寫自訂 `Exception`
- **Ch10**：DataCleaner 實戰 — 三根柱子（封裝 + 繼承 + chaining）合體
