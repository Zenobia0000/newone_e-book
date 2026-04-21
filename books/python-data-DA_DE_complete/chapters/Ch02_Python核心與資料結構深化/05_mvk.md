# F2 · MVK 速學卡（Minimum Viable Knowledge）

> 離開本節後，你的肌肉記憶裡必須長出這五個反射。
> 對應 01_outline.md 的 5 個 Learning Objectives。
> 受眾：只有 Python 基礎的非理工背景學員。

---

## ① 四容器，四個生活場景（對應 LO1）

```python
# List = 聯絡人清單（有順序、可重複）
sales = [1200, 980, 1500]            # 每天營業額

# Dict = 字典查字（用關鍵字查答案）
emp = {'E1024': '王小明', 'E1025': '林小華'}
emp['E1024']                          # '王小明' — 直接翻到

# Set = 去重袋（自動去重 / 判斷有沒有）
customers = set(['A1', 'A2', 'A1'])   # {'A1', 'A2'}
'A1' in customers                     # True — 幾乎 0 秒

# Tuple = 身分證欄位（鎖死、能當 key）
loc = ('台北', '大安', '106')
```

**一句口訣**：要順序 → List / 要查找 → Dict / 要去重 → Set / 要鎖死 → Tuple。

---

## ② 便利貼心智模型（對應 LO2）

```python
a = [1, 2, 3]
b = a                    # b 不是影印，是再貼一張便利貼到同一個 list
b.append(99)
print(a)                 # [1, 2, 3, 99] ← a 也變了！

# 要真的複製：
import copy
c = copy.copy(a)         # 淺：扁平用這個
d = copy.deepcopy(a)     # 深：巢狀保命用這個
```

**心智模型**：變數不是盒子，是便利貼。`b = a` 是貼第二張便利貼，不是影印。

**Pandas 銜接**：這就是 `SettingWithCopyWarning` 的根源——系統在問你：「你改的是本尊還是分身？」

---

## ③ 可變 vs 不可變 × 能否當 key（對應 LO2）

| 類型 | 會變嗎？ | 能當 dict key 嗎？ |
|------|---------|-------------------|
| int / str / tuple | 不會變 | ✅ 可以 |
| list / dict / set | 會變 | ❌ 不行（`TypeError`） |

**為什麼**：會變的東西 Python 記不住它的「指紋」，所以不能拿來當關鍵字。

---

## ④ for 其實是『要下一個』（對應 LO3）

```python
# 你寫的
for x in [1, 2, 3]:
    print(x)

# Python 幫你做的（生活版）
# for 問容器：還有嗎？→ 容器答：有，這是 1 → for 印 1
# for 問容器：還有嗎？→ 容器答：有，這是 2 → for 印 2
# for 問容器：還有嗎？→ 容器答：沒了（停止迭代）→ for 自動結束
```

**關鍵**：你不用寫 while 與計數器，Python 的 for 已經幫你處理「問到底就停」。

---

## ⑤ Generator = 逐頁翻書（對應 LO4 + LO5）

```python
# 10GB log 挑 ERROR 行 —— 三行解決
def read_errors(path):
    with open(path) as f:
        for line in f:                      # 檔案天生就能『一頁一頁』
            if 'ERROR' in line:
                yield line.rstrip()         # 翻到一頁就給出去

for err in read_errors('/var/log/app.log'): # RAM < 50 MB
    send_to_alert(err)
```

**心智模型**：`yield` = 本集結尾；下次呼叫 `next()` 從暫停點接著演。整本書 10GB，RAM 只裝當下一頁。

**Pandas 銜接**：
```python
# 下週 S2 你會這樣寫
for chunk in pd.read_csv('5GB.csv', chunksize=100_000):
    ...  # chunksize 回傳的就是 generator，跟 yield 同一套引擎
```

---

## 五個必踩地雷（考前必背）

| # | 地雷 | 錯 | 對 |
|---|------|----|----|
| P1 | `[[]] * 3` 以為建三個 | `a = [[]] * 3; a[0].append(1)` → 全中 | `[[] for _ in range(3)]` |
| P2 | `b = a` 以為複製 | 改 b 會動到 a | `b = a.copy()` 或 `deepcopy` |
| P3 | 淺拷貝踩巢狀 | `.copy()` 後改內層，原本也中 | 巢狀用 `copy.deepcopy` |
| P4 | list 當 dict key | `d[[1,2]] = ...` → TypeError | 改用 tuple `d[(1,2)] = ...` |
| P5 | generator 跑兩次 | 第二次 `list(g)` → `[]` | 重建 generator 或先 list() |

---

## 下一節銜接

### → F3 OOP
今天的「變數是便利貼、object 在記憶體裡」就是 OOP 的 `self` 心智基礎——self 就是指向 instance 的那張便利貼。

### → S1 NumPy
NumPy 的 ndarray 是「一塊連續記憶體 + 一層眼鏡」——跟今天「變數 → object」的便利貼模型同源。view vs copy 的坑也完全對應。

### → S2 Pandas
- 一個 dict = DataFrame 的一列（row）；一串 dict = DataFrame 本身。
- `pd.read_csv(chunksize=...)` 回傳的是 generator——今天的 yield 就是它的引擎。
- `SettingWithCopyWarning` 的根源就是今天 S11 的淺深拷貝。

**一句話**：F2 不是基礎複習，是 S1/S2 能不能學得動的門票。
