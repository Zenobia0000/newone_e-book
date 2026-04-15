# Chapter 3：自訂函式與特殊 Python 函式

**模組：** M1 系統前導與 Python 機制  
**時數：** 2.0 小時  
**前置知識：** Ch2 容器與 Iterator  
**後續銜接：** Ch8（Pandas `apply(lambda ...)`）、Ch10（整合實戰）

---

## 一、章節定位

本章教 Python 最具表達力的「**特殊機制三件套**」：Lambda、map/filter、Comprehension。這些不是炫技語法，而是日後 Pandas 欄位轉換、特徵工程的必備武器。

---

## 二、學習目標

完成本章後，學生能夠：

1. 正確使用位置參數、關鍵字參數、`*args`、`**kwargs`
2. 解釋變數作用域（LEGB 規則）
3. 將 3 行 for 迴圈改寫為 1 行 List Comprehension
4. 使用 Lambda 搭配 `map()` / `filter()` / `sorted(key=...)` 處理資料
5. 估算 Comprehension 的時間複雜度

---

## 三、章節結構

### 3-1. 自訂函式進階（40 分鐘）
- 函式定義回顧：`def`、return 多值、type hints
- 參數種類：
  - 位置參數（positional）
  - 關鍵字參數（keyword）
  - 預設參數（與可變預設值的陷阱：`def f(x=[]):` 的雷）
  - `*args`：收集多餘位置參數
  - `**kwargs`：收集多餘關鍵字參數
- **作用域 LEGB**：Local → Enclosing → Global → Built-in
- `global` 與 `nonlocal` 何時需要（提示：盡量不要用）
- **實戰範例**：寫一個資料驗證函式，用 `**kwargs` 接受任意欄位規則

### 3-2. Lambda 與函數式三件套（40 分鐘）
- Lambda 的本質：「沒有名字的小函式」
- 何時用 Lambda、何時還是該 `def`（超過一行邏輯就該 def）
- `map(func, iterable)`：對每個元素套用函式
- `filter(func, iterable)`：保留符合條件的元素
- `sorted(iterable, key=lambda x: ...)`：自訂排序鍵
- **常見搭配**：
  ```python
  prices = [120, 80, 200, 50]
  # 取出超過 100 的，打 9 折
  result = list(map(lambda x: x*0.9, filter(lambda x: x > 100, prices)))
  ```
- **預告 Ch8**：`df['price'].apply(lambda x: x*0.9)` 就是同樣的概念

### 3-3. Comprehension 與時間複雜度（40 分鐘）
- **List Comprehension**：`[expr for x in iterable if cond]`
- **Dict Comprehension**：`{k: v for ... }`
- **Set Comprehension**：`{x for ... }`
- **巢狀 Comprehension**：何時可讀、何時該回去用 for
- **時間複雜度直覺**：
  - List Comprehension 與 for 迴圈同為 O(N)，但 Comprehension 在 CPython 內部優化更快
  - 巢狀 = O(N×M)
- **可讀性原則**：超過兩層巢狀就拆回 for
- **與 Generator Expression 的差異**（呼應 Ch2）：括號形式 `()` 不會立即生成全部結果

---

## 四、課後練習

1. **改寫題**：把以下 5 行 for 迴圈改寫成一行 Comprehension
2. **應用題**：給一份 `users = [{'name':..., 'age':...}, ...]`，用 `sorted` + lambda 按年齡排序
3. **效能題**：產生 1000 萬個平方數，比較 `[x**2 for x in range(N)]` 與 `(x**2 for x in range(N))` 的記憶體使用

---

## 五、銜接下一章

至此 Python 語法部分結束。Ch4 進入 OOP —— 把這些「函式技巧」升級為「物件方法」，為日後設計可重用的資料管線（Ch10 DataCleaner）奠基。
