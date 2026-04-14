# M1 Minimum Viable Knowledge — MVK 速學卡

> **本文件定位：** M1 的核心知識濃縮為 15 張速學卡，每張含「一句話定義 + 最小可操作範例 + 常見誤解 + 跨模組連結」，可直接印成索引卡或做成 Anki deck。
> **讀者：** 已上過 M1 需複習的學員、帶新人的資深工程師、要快速了解 M1 範圍的 reviewer。
> **使用情境：** 課後 48 小時記憶鞏固期的快速複習；課程認證的 checkpoint；面試 Python 資料分析職位的自我檢核。

---

## 卡片使用說明

每張卡片五欄位：
1. **概念**：名詞 / 技能名
2. **一句話定義**：資深工程師怎麼向同事解釋
3. **最小可操作範例**：3-5 行可跑的程式
4. **常見誤解**：新人最容易踩的坑
5. **跨模組連結**：這個概念在 M2-M7 怎麼延伸

---

## 卡 01 — 結構化資料的五元素

**一句話定義：** 一份表格資料由 row（觀測）/ column（變數）/ schema（欄名+型態）/ type（欄的資料類型）/ key（唯一識別欄）五個元素完整描述。

**最小範例：**
```python
import pandas as pd
df = pd.read_csv("sales.csv")
df.shape       # (rows, cols)
df.dtypes      # 每欄型態
df.columns     # 欄名
df.head(3)     # 前三筆
```

**常見誤解：** 以為「看到表格長什麼樣」就懂資料。真正要問的是 schema 與 key 是什麼。沒有 key 就無法 join。

**跨模組連結：** M3 pandas `merge` 靠 key；M7 特徵工程靠 schema；M4 視覺化前要先確認 type。

---

## 卡 02 — 資料污染的四種面孔

**一句話定義：** 髒資料 = 缺失（missing）+ 重複（duplicate）+ 離群（outlier）+ 型態錯誤（type error），四者各有檢測與處理哲學。

**最小範例：**
```python
df.isna().sum()            # 缺失
df.duplicated().sum()      # 重複
df["amount"].describe()    # 看 min/max 找離群
df.dtypes                  # 看型態是否符合期待
```

**常見誤解：**
- `NaN` ≠ `None` ≠ `""` ≠ `0`，四者語義不同。
- 離群值不一定是錯誤，可能是真實的頂級客戶。
- 型態錯誤最危險：`"10" + "2" == "102"` 會默默跑過。

**跨模組連結：** M3 的 `pd.to_numeric(errors="coerce")`、M4 的箱型圖找離群、M7 的異常偵測模型。

---

## 卡 03 — Excel 思維 vs Python 思維

**一句話定義：** Excel 是手動操作，每次分析從零開始；Python 是腳本化流程，同樣輸入永遠得到同樣輸出。

**最小範例：**
```python
# Python 思維：每一步都是可讀的決策
df = pd.read_csv("sales.csv")
df = df.dropna(subset=["amount"])
df["amount"] = df["amount"].astype(float)
df.to_csv("sales_clean.csv", index=False)
```

**常見誤解：** 以為「Python 比 Excel 厲害」是速度問題。其實是**可重現性（reproducibility）**的問題。Excel 沒有錯，只是不留痕跡。

**跨模組連結：** M5 的 logging / 錯誤處理；M7 的 MLOps reproducibility；公司 CI/CD。

---

## 卡 04 — Jupyter Notebook 四合一

**一句話定義：** Notebook 把 markdown 說明、Python 程式、數值輸出、圖表整合在一個 `.ipynb` 檔，讓分析過程可讀、可重現、可分享。

**最小範例：**
```python
# Markdown cell：寫下「為什麼做這步」
# Code cell：
import pandas as pd
df = pd.read_csv("sales.csv")
df["amount"].hist()   # 直接在 cell 下方顯示圖
```

**常見誤解：**
- 以為 cell 由上到下跑——**錯，執行順序看 `In[]` 編號**，可能亂跳。
- 以為 kernel 重開還會在——**錯，restart 後所有變數消失**。
- **交付前一定要 `Restart & Run All`**，否則會有 hidden state bug。

**跨模組連結：** M4 的 EDA notebook、M7 的模型訓練 notebook；生產環境要改寫為 `.py`。

---

## 卡 05 — Python 的六個基礎型態與容器

**一句話定義：** 資料分析常用 6 個：`int / float / str`（純量）+ `list / dict / tuple`（容器），加上 `set` 做去重共 7 個。

**最小範例：**
```python
n = 42                       # int
pi = 3.14                    # float
name = "Alice"               # str
scores = [95, 87, 72]        # list - 有序可變
record = {"name": "Alice",   # dict - 映射
          "score": 95}
shape = (1000, 5)            # tuple - 不可變 record
unique = set([1, 1, 2, 3])   # set - {1,2,3}
```

**常見誤解：**
- list 和 tuple 差別**不只**可不可變；tuple 代表 fixed-arity record，list 代表 variable-length array。
- dict key 必須 hashable（immutable），所以不能用 list 當 key。
- Python 3.7+ 的 dict 保證 insertion order，但不要濫用這特性。

**跨模組連結：** M3 pandas `Series = list + index`、`DataFrame = dict of Series`；M5 的 `collections.OrderedDict / defaultdict / Counter`。

---

## 卡 06 — 可變（mutable）vs 不可變（immutable）

**一句話定義：** immutable 物件內容不能改（`int / str / tuple`），mutable 物件可被 in-place 修改（`list / dict / set`）；可變性屬於物件、不屬於變數。

**最小範例：**
```python
a = [1, 2]; b = a; b.append(3)
print(a)  # [1,2,3] — a 和 b 指向同一個 list

x = "hi"; y = x; y = y + "!"
print(x)  # "hi" — str 不可變，y 指向新物件
```

**常見誤解：**
- 函式預設參數陷阱：`def f(x=[]):` 的 list 在每次呼叫**共享同一個物件**。
- dict key 必須 immutable，因為 hash 在物件生命期內必須穩定。
- Jupyter cell 之間共享 mutable 物件，容易互相污染。

**跨模組連結：** M2 OOP 的 `__eq__ / __hash__` 設計；M5 functional programming；平行化（不變性 = 無競爭）。

---

## 卡 07 — 變數即名字綁定（name binding）

**一句話定義：** Python 沒有「值型別」，所有變數都是名字綁到 heap 上 `PyObject` 的指標；`a = b` 是讓兩個名字指向同一個物件。

**最小範例：**
```python
a = [1, 2, 3]
b = a           # 共享同一 list
c = a.copy()    # 真正複製

import copy
d = copy.deepcopy(a)  # 巢狀結構也複製
```

**常見誤解：**
- 以為 `b = a` 是複製。錯，是共享引用。
- 函式傳參是「pass by object reference」，不是 pass by value / reference。
- `del x` 只刪名字，物件靠 refcount + GC 回收。

**跨模組連結：** M2 class 實例共享；M5 closure 與 LEGB；M6 記憶體管理。

---

## 卡 08 — 分支與迴圈：if / for / comprehension

**一句話定義：** 資料處理的三種基本控制流：`if` 做條件判斷、`for` 做逐元素處理、comprehension 是 for + 條件的一行簡寫。

**最小範例：**
```python
# if
label = "high" if amount > 1000 else "low"

# for + enumerate + zip
for i, (col, dtype) in enumerate(zip(df.columns, df.dtypes)):
    print(i, col, dtype)

# list comprehension
cleaned = [s.strip().lower() for s in names if s]

# generator expression（不爆記憶體）
total = sum(x*x for x in big_iter)
```

**常見誤解：**
- 以為 comprehension 永遠比 for 好——巢狀超過兩層反而難讀。
- 大資料用 for 迴圈慢得離譜，應改 pandas 向量化。
- `.apply()` **不是真的向量化**，底層還是 Python loop。

**跨模組連結：** M3 pandas 向量化；M5 `itertools / functools`；M7 批次訓練的 batch iteration。

---

## 卡 09 — 函式三要素：input → logic → output

**一句話定義：** 好函式 = 單一職責 + 輸入明確（type hint）+ 回傳明確（不要默默吃錯誤）+ 無副作用（pure function）。

**最小範例：**
```python
def clean_amount(raw: str) -> float | None:
    """Convert '$1,200.50' to 1200.50; return None on failure."""
    try:
        return float(raw.replace("$", "").replace(",", ""))
    except ValueError:
        return None   # 明確失敗，不要默默回 0.0

assert clean_amount("$1,200") == 1200.0
assert clean_amount("bad") is None
```

**常見誤解：**
- 失敗時回傳 0.0 會污染下游統計，**請回傳 None / NaN**。
- type hint 不會在 runtime 檢查，要配 mypy / pydantic。
- 預設參數若是 mutable（`def f(x=[]):`）會共享，請用 `None` 當 sentinel。

**跨模組連結：** M2 class method；M5 decorator / higher-order function；M7 pipeline step 封裝。

---

## 卡 10 — f-string 與格式化

**一句話定義：** Python 3.6+ 的 f-string 是字串格式化首選：`f"{var}"` 內嵌表達式、`f"{x:.2f}"` 控制格式。

**最小範例：**
```python
name, score = "Alice", 95.5
print(f"{name}: {score:.1f}")              # Alice: 95.5
print(f"{score:>10.2f}")                   # 右對齊 10 欄、2 位小數
print(f"{1234567:,}")                      # 1,234,567（千分位）
print(f"{0.85:.1%}")                       # 85.0%

# logging 例外：用 %s 占位，不用 f-string
logger.info("processed %s rows", n)
```

**常見誤解：**
- 還在用 `"%s" % x` 或 `"{}".format(x)`——舊寫法，新程式請用 f-string。
- logging 用 f-string 會**提早求值**，影響效能與 sanitization，這裡例外用 `%s`。

**跨模組連結：** M3 的 `df.to_string()` / display 格式；M5 的 logging / repr；M7 的模型輸出報告。

---

## 卡 11 — type hint 的實務價值

**一句話定義：** type hint（`x: int`、`-> float`）是**寫給人與工具看的文件**，不是 runtime 檢查；價值在 IDE 補全、mypy 靜態檢查、Pydantic/FastAPI 生態。

**最小範例：**
```python
from typing import Optional

def summarize(values: list[float], top_n: int = 10) -> dict[str, float]:
    return {
        "min": min(values),
        "max": max(values),
        "mean": sum(values) / len(values),
    }

# 進階
def lookup(key: str) -> Optional[dict]:
    return cache.get(key)
```

**常見誤解：**
- 以為寫了 hint，傳錯型別會自動報錯——錯，**Python runtime 不檢查**。
- 以為 hint 拖慢效能——幾乎無影響。
- 以為是裝飾不寫也沒差——**團隊協作、重構、AI IDE 全部倚賴它**。

**跨模組連結：** M2 dataclass / Pydantic；M5 mypy / Protocol；M7 FastAPI 的 request/response schema。

---

## 卡 12 — import 與套件生態

**一句話定義：** `import` 把別人寫好的能力引入命名空間；Python 的戰力不是語言，是 `pandas / numpy / sklearn / pytorch` 這條生態鏈。

**最小範例：**
```python
import math                    # 標準庫
import numpy as np             # 約定短別名
import pandas as pd
from datetime import datetime  # 只取需要的
from pathlib import Path

# 絕對不要：
# from pandas import *   # 命名空間污染
```

**常見誤解：**
- 以為 `pip` 和 `conda` 能混用——會導致相依衝突，**選一邊用到底**。
- 以為 `import *` 方便——破壞可讀性，團隊會罵人。
- 以為套件版本不重要——`numpy 1.x vs 2.x` 會炸掉整個 pipeline，**請用 `requirements.txt` 或 `uv.lock` 鎖版本**。

**跨模組連結：** M3 pandas / numpy；M4 matplotlib / seaborn；M5 虛擬環境與 `pyproject.toml`；M7 `scikit-learn / pytorch`。

---

## 卡 13 — 可重現性（Reproducibility）

**一句話定義：** 同輸入 + 同程式 + 同環境 + 同執行順序 → 同輸出；四個「同」缺一不可。

**最小範例：**
```python
# 1. 固定隨機種子
import numpy as np
np.random.seed(42)

# 2. 鎖定套件版本
# requirements.txt:
#   pandas==2.2.0
#   numpy==1.26.4

# 3. Notebook 交付前：Kernel → Restart & Run All

# 4. Git 追蹤 .ipynb 與資料 schema
```

**常見誤解：**
- 以為 Notebook 天然可重現——錯，**hidden state 是最大破壞者**。
- 以為鎖套件版本是潔癖——等你的 pipeline 在新同事電腦炸掉就懂。
- 以為「結果差不多」就 OK——金融、醫療領域「差不多」等於法遵風險。

**跨模組連結：** M5 venv / Docker；M6 作業系統環境；M7 MLOps 的 model versioning / DVC。

---

## 卡 14 — 錯誤處理：try / except 的正確姿勢

**一句話定義：** `try/except` 用來處理**預期的失敗**（IO 錯、parse 錯），不是用來吞掉所有錯誤；抓越窄越好，絕不 `except Exception: pass`。

**最小範例：**
```python
# 好的：明確捕捉特定錯誤、明確行為
try:
    df = pd.read_csv(path)
except FileNotFoundError:
    logger.error("File not found: %s", path)
    raise     # 重新 raise，不要吞
except pd.errors.ParserError as e:
    logger.warning("Parse error: %s", e)
    df = pd.DataFrame()

# 壞的 anti-pattern：
try:
    do_something()
except:              # 裸 except 會抓到 KeyboardInterrupt
    pass             # 靜默吞錯，永遠別這樣
```

**常見誤解：**
- 以為 try/except 越大越安全——錯，**越寬越危險**，會把 bug 藏起來。
- 以為 except 裡能 `print` 就好——請用 `logging`。
- 以為要自己寫 exception class 很麻煩——繼承 `Exception` 三行就好，**domain error 請命名**。

**跨模組連結：** M5 logging 深度；M7 pipeline 的 retry / dead letter queue。

---

## 卡 15 — Workshop 心法：從手動到函式化

**一句話定義：** 把一段分析流程函式化的三步驟：（1）找出重複的動作，（2）抽出輸入和輸出，（3）給它一個名字。

**最小範例：**
```python
# 手動（每次都重寫）
print(df.shape); print(df.dtypes); print(df.isna().sum())

# 函式化（寫一次，跑一輩子）
def describe_dataset(df: pd.DataFrame) -> None:
    print(f"Shape: {df.shape}")
    print(df.dtypes)
    print(df.isna().sum())

# 甚至更好：拆成單一職責
def describe_shape(df): ...
def describe_types(df): ...
def describe_missing(df): ...

# 加一行 assert 當最小單元測試
assert describe_dataset.__doc__  # 至少有 docstring
```

**常見誤解：**
- 以為「一個函式做很多事」是好函式——**錯**，單一職責才是好函式。
- 以為寫函式浪費時間——第二次呼叫時就回本。
- 以為函式化 = 封裝——**下一步才是 class（M2）**，它處理的是 state + behavior 的綁定。

**跨模組連結：** M2 class；M5 decorator 組合；M7 pipeline step 抽象。

---

## 附錄：M1 → M7 能力漸進表

| 能力 | M1 | M2 | M3 | M4 | M5 | M6 | M7 |
|---|---|---|---|---|---|---|---|
| 表達資料 | 六型態 + 容器 | class 封裝 | DataFrame | 圖表 | — | — | tensor |
| 處理資料 | for / comprehension | method | 向量化 | groupby / pivot | async / parallel | — | batch |
| 組織程式 | 函式 | class / 繼承 | module | — | package / decorator | — | pipeline |
| 可重現性 | Notebook + 腳本 | — | — | — | venv / log / test | OS / container | MLOps |
| 錯誤處理 | try/except 入門 | exception 階層 | coerce | — | 深度 logging | — | model failure |

---

## 如何使用這組速學卡

1. **課後 48 小時**：15 張每天看 5 張，做「常見誤解」自我檢測。
2. **每週複習**：抽 3 張測試最小範例能否背出。
3. **上工應用**：遇到實務問題時，回查「跨模組連結」找下一步學習方向。
4. **面試準備**：把 15 張的「一句話定義」練到能用 30 秒對同事解釋。
