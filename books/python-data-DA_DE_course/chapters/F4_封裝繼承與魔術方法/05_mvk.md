# F4 · MVK 速學卡（Minimum Viable Knowledge）

> 離開本節後，你的肌肉記憶裡必須長出這四個反射。
> 對應 01_outline.md 的 4 個 Learning Objectives。

---

## ① 封裝三道門，各有使用時機（對應 LO1）

```python
class Temperature:
    def __init__(self, c):
        self._celsius = c      # 弱封裝：提示內部用

    @property
    def celsius(self):         # 需要驗證 / 計算 / 換實作
        return self._celsius

    @celsius.setter
    def celsius(self, v):
        if v < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = v
```

**時機對照表**：

| 手法 | 什麼時候用 |
|------|-----------|
| `x` | 穩定、無驗證需求、對外合約的一部分 |
| `_x` | 內部用、不強制，linter / IDE 會提示 |
| `__x` | 只為避免子類命名衝突，**不是加密** |
| `@property` | 需要驗證 / 計算 / 未來可能換實作 |

**關鍵真相**：`obj._ClassName__x` 照樣拿得到 `__x` 的值。敏感資料該 hash、加密、不存。

---

## ② 單一繼承 + `super` + override（對應 LO2）

```python
class DataReader:
    def __init__(self, encoding="utf-8"):
        self.encoding = encoding
        self.rows_read = 0

    def read(self, path):
        raise NotImplementedError


class CSVReader(DataReader):
    def __init__(self, encoding="utf-8", sep=","):
        super().__init__(encoding)   # 先做父親那份
        self.sep = sep

    def read(self, path):            # override
        df = pd.read_csv(path, sep=self.sep, encoding=self.encoding)
        self.rows_read = len(df)
        return df
```

**三條鐵律**：

1. 子類 `__init__` 第一行永遠 `super().__init__(...)`。
2. override 方法同名、可延伸簽章，子類可直接用父類屬性。
3. **先問 IS-A 還是 HAS-A**：能用組合（`self.items = []`）就別用繼承（`class MyList(list)` 是反模式）。

---

## ③ 魔術方法四件套（對應 LO3）

```python
class Order:
    def __init__(self, id_, amount):
        self.id, self.amount = id_, amount

    def __repr__(self):            # 給開發者：理想可反貼重跑
        return f"Order(id_={self.id!r}, amount={self.amount!r})"

    def __str__(self):             # 給使用者：好看為主
        return f"訂單 #{self.id}：NT$ {self.amount:,}"


class DataPipeline:
    def __init__(self):
        self._steps = []

    def __len__(self):             # 有『數量感』就實作
        return len(self._steps)

    def __iter__(self):            # 能『逐一處理』就實作
        return iter(self._steps)
```

**選擇邏輯**：

| 方法 | 何時實作 |
|------|---------|
| `__str__` | 物件會被 print / log |
| `__repr__` | **任何類別都該寫**（debug 地基） |
| `__len__` | 物件裡有『幾個』概念 |
| `__iter__` | 物件能被 for 逐一處理 |

**一句話**：只寫一個的話，寫 `__repr__`——因為 `print` 沒 `__str__` 會退用 `__repr__`。

---

## ④ Method Chaining：`return self`（對應 LO4）

```python
class DataCleaner:
    def __init__(self, df):
        self.df = df

    def drop_na(self):
        self.df = self.df.dropna()
        return self                # ← 一定要

    def normalize(self, cols):
        z = (self.df[cols] - self.df[cols].mean()) / self.df[cols].std()
        self.df[cols] = z
        return self

    def export(self, path):
        self.df.to_csv(path, index=False)
        return self


(DataCleaner(df)
 .drop_na()
 .normalize(["price"])
 .export("out.csv"))
```

**為什麼重要**：程式結構 = 資料流結構。讀起來像一句話：「拿資料 → 去空值 → 標準化 price → 匯出」。這是 F5 `DataCleaner` 的骨架。

**地雷**：鏈上任何一個方法漏 `return self` → 下一環拿到 `None` → `AttributeError: 'NoneType' object has no attribute ...`。錯誤訊息很誤導，要往**上一個方法**找。

---

## 五個必踩地雷（考前必背）

| # | 地雷 | 錯 | 對 |
|---|------|----|----|
| P1 | 把 `__x` 當加密 | `self.__password = pw` | 走 hash / 加密 / 不存 |
| P2 | 漏呼 `super().__init__()` | 子類只設自己的 | 第一行 `super().__init__(...)` |
| P3 | 繼承解決組合問題 | `class OrderList(list):` | `self.items = []` 組合 |
| P4 | 只寫 `__str__` 不寫 `__repr__` | REPL 看到 `<obj at 0x..>` | 兩個都寫，至少先寫 repr |
| P5 | Chaining 忘 `return self` | 下一環 NoneType | 每個方法最後 `return self` |

---

## 下一節銜接（F5 OOP + Pandas 整合實戰）

> `DataCleaner` = 封裝（`_df` / `@property`）+ 繼承（`BaseCleaner` → `PriceCleaner`）
> + 魔術方法（`__len__` / `__iter__` / `__repr__`）+ Chaining（`return self`）
>
> **今天的每個零件，明天都會在 `DataCleaner` 裡再出現一次。**
