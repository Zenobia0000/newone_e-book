# Ch03 · MVK 速學卡（Minimum Viable Knowledge）

> 一頁看完就能上戰場：20 分鐘讀完 = Ch03 2 小時精華。

---

## 一、核心主張（一句話）

**會宣告，就少寫 80% 迴圈。** Lambda / map / filter / Comprehension 的共同精神是「告訴 Python 要什麼，不寫怎麼做」。

---

## 二、必記五組肌肉記憶

### 1. 函式參數五種分工（由嚴到鬆）

```python
def f(pos, kw=10, *args, **kwargs):
    ...
# pos   : 位置參數，必填
# kw=10 : 預設參數
# *args : 收剩下的位置參數，進來是 tuple
# **kwargs: 收剩下的關鍵字參數，進來是 dict
```

### 2. 可變預設值陷阱（PEP 8 / Ruff B006）

```python
# BAD — bag 在第一次 def 時建立，之後共用
def add(x, bag=[]): bag.append(x); return bag

# GOOD — None 哨兵 + 首行初始化
def add(x, bag=None):
    bag = bag if bag is not None else []
    bag.append(x); return bag
```

### 3. LEGB 作用域（查名字順序）

**Local → Enclosing → Global → Built-in**。由內往外找，找不到 NameError。`global` / `nonlocal` 能不用就不用。

### 4. Lambda 三件套

```python
list(map(lambda x: x*0.9, prices))         # map：套函式
list(filter(lambda x: x > 100, prices))    # filter：篩選
sorted(users, key=lambda u: u["age"])      # sorted(key=)：自訂排序
```

**邊界規則**：超過一行邏輯 → 改 `def`。

### 5. Comprehension 四兄弟（同骨架，換外框）

```python
[x**2 for x in xs if x > 0]                # list
{x**2 for x in xs}                         # set（自動去重）
{u["id"]: u["name"] for u in users}        # dict
(x**2 for x in xs)                         # generator（懶求值）
```

**三格骨架**：`[  輸出  for  來源  if  條件  ]`，讀時從 `for` 開始讀。

---

## 三、時間複雜度三直覺

| 寫法 | 複雜度 | 警戒線 |
|------|--------|--------|
| 單層 for / Comprehension | O(N) | 百萬級都 OK |
| 巢狀 | O(N×M) | 兩邊千級就小心 |
| `x in list` | O(N) 每次 | 改 set → O(1) |

---

## 四、生死判斷 · List vs Generator

| 場景 | 用 `[]` | 用 `()` |
|------|---------|---------|
| 跑一遍就丟 | ✗ | **✓** |
| 要索引、要跑多次 | **✓** | ✗ |
| 資料量 > 記憶體 | ✗ | **✓（必用）** |

1000 萬平方數：list ≈ 350 MB，generator ≈ 128 B。**差 N 倍不是誇飾。**

---

## 五、Ch03 → Ch08 銜接梗

```python
# Ch03 你學的
list(map(lambda x: x*0.9, prices))

# Ch08 你天天寫
df["price"] = df["price"].apply(lambda x: x*0.9)
```

**同一個概念搬到表格上。** Ch03 練好 lambda，Ch08 省一半時間。

---

## 六、紀律三條（code review 會被釘的地方）

1. 預設參數絕不給可變物件（`[]` / `{}` / `set()`）→ 用 `None` + 首行初始化。
2. Lambda 超過一行 → 改 `def`，才能寫 docstring、加測試。
3. 巢狀 Comprehension 超過兩層 → 拆回 `for`，可讀性優先。

---

## 七、自我檢核題（閉卷）

1. `def f(x, y=[]):` 為什麼有雷？怎麼修？
2. 把 `list(map(lambda x: x*2, filter(lambda x: x>0, xs)))` 改寫成 Comprehension。
3. `users = [{'age':30}, {'age':22}]`，按年齡排序怎麼寫？
4. 1000 萬個平方數只要求和一次，用 `[]` 還是 `()`？為什麼？
5. `{x for x in xs}` 是 list、set 還是 dict？怎麼判斷？

> 全答對 = 可進 Ch04。答錯 2 題以上，回去重看 S5 / S11 / S12 / S17。
