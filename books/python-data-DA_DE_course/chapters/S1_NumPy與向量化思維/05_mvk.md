# S1 · MVK 速學卡（Minimum Viable Knowledge）

> 離開本節後，你的肌肉記憶裡必須長出這五個反射。
> 對應 01_outline.md 的 5 個 Learning Objectives。

---

## ① ndarray 的三張身分證（對應 LO1）

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape   # (2, 3)  ← 形狀
a.dtype   # int64   ← 型別（同質！）
a.ndim    # 2       ← 維度
```

**心智模型**：ndarray ＝ 一塊連續記憶體 + 一層 view（眼鏡）。reshape 只換眼鏡，資料零搬動。

---

## ② 三種索引，三種語意（對應 LO2）

```python
a[1:3]          # 基本切片：view、零複製、修改會回傳
a[a > 0]        # 布林遮罩：用 & | ~ 不是 and/or，每塊括號都要 ()
a[[0, 2, 5]]    # fancy indexing：copy，任意挑元素
```

**一句口訣**：切片是借鏡、遮罩像 WHERE、fancy 是點名。

---

## ③ 向量化的真義（對應 LO3）

```python
# ✗ 慢：運算在 Python 層
total = 0
for x in data:
    total += x * 2

# ✓ 快 50-80×：運算送進 C 層
total = (data * 2).sum()
```

**關鍵**：向量化 ≠ 加 np.；是讓整塊運算「一次離開 Python」。for 裡面呼叫 np.sum 仍然慢。

---

## ④ Broadcasting 兩條規則（對應 LO4）

1. **從右對齊**每個維度
2. 該維度**相等或其中一個是 1** → 可擴展；否則 `ValueError`

```python
# (3,1) + (1,4) → (3,4)
# (3,)  + (3,1) → (3,3) ← 注意！跟 (3,)+(3,) 結果完全不同
```

**debug 第一步**：`print(a.shape, b.shape)`。

---

## ⑤ 商業一行解（對應 LO5）

```python
(price * stock).sum()      # 總庫存價值（SUMPRODUCT）
(stock < 10).sum()         # 低庫存商品數（COUNT-IF）
price[stock < 10].mean()   # 低庫存品均價（條件式均值）
```

**招式名**：布林遮罩 + sum ＝ count-if；逐元素乘 + sum ＝ sumproduct。

---

## 五個必踩地雷（考前必背）

| # | 地雷 | 錯 | 對 |
|---|------|----|----|
| P1 | for-loop 處理數字 | `for x in data: total += x*2` | `(data*2).sum()` |
| P2 | `and` / `or` | `a[a>0 and a<10]` | `a[(a>0) & (a<10)]` |
| P3 | 切片以為是 copy | `b = a[:3]; b[0]=9` 會改到 a | `b = a[:3].copy()` |
| P4 | shape 搞錯 | `(3,) + (3,1) → (3,3)` 意外！ | 先 `print(shape)` |
| P5 | `==` 比浮點 | `0.1+0.2 == 0.3 → False` | `np.isclose(...)` |

---

## 下一節銜接（S2 Pandas I/O）

> DataFrame 是「加了欄名的 ndarray」——shape/dtype 直覺完全沿用；
> `df[df['price'] > 100]` 的本質就是布林遮罩；
> groupby / merge 底層都是 shape 運算。
>
> **今天的 shape 直覺，是明天 Pandas 的地基。**
