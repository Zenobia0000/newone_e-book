# F4 — 封裝、繼承與魔術方法｜講師講稿

> **課程時長**：1.5 小時（講授 60 min + 課堂練習 25 min + QA 5 min）
> **對應 Notebook**：`M2_OOP/F4_encapsulation_inheritance_magic.ipynb`
> **前置**：F3 OOP 核心（class / `__init__` / self / method）
> **後續**：F5 OOP + Pandas 整合實戰（DataCleaner）

---

## 1. 本節目標 (Learning Objectives)

完成本節後，學員應能：

1. 區分 `x` / `_x` / `__x` / `@property` 四種封裝手法的**使用時機**（不是只記語法），並解釋 Python「沒有 private」的真相。
2. 寫出單一繼承，正確呼叫 `super().__init__()`、覆寫父類別方法，並能解釋子類建構時的執行順序。
3. 為自訂類別實作 `__str__` / `__repr__` / `__len__` / `__iter__` 四件套，讓物件能被 Python 內建 API（`print`、`len`、`for`）自然使用。
4. 設計支援 Method Chaining 的類別（每個方法 `return self`），為 F5 `DataCleaner` 奠定骨架。

---

## 2. 時間切分表

```
00:00-00:05  開場 ASK：為什麼資深工程師的 class 很少直接改欄位
00:05-00:25  封裝三道門 × @property × __x 不是加密（Pitfall P1）
00:25-00:50  繼承 × super × override × 漏 super 的 Pitfall P2 × IS-A vs HAS-A
00:50-01:10  魔術方法四件套（__str__ / __repr__ / __len__ / __iter__）
01:10-01:25  Method Chaining × 忘 return self 的 Pitfall P5 × 四柱合體
01:25-01:30  銜接 F5 + Checkpoint 五題 + 收束
```

---

## 3. 關鍵教學點 (Key Teaching Points)

1. **封裝不是語法題，是時機題**：學員最常問「那我到底該用底線還是 property？」。答案是：需要驗證／計算／未來換實作用 `@property`；只是提示內部用就 `_x`；避免子類命名衝突才用 `__x`。反覆強調「三道門各有使用時機」，不要當成加密層級。
2. **`__x` 不是加密**：務必現場 demo `a._Class__x` 拿得到值。這是 P1 最常見誤用——把密碼丟進 `__password` 就以為安全。安全資料要 hash / 加密 / 外存。
3. **`super().__init__()` 必做，錯誤延後兩個月才爆**：這是 P2 最陰險的地方。父類屬性沒設，測試時沒用到那屬性就不會報；等到 production 某條路徑用到才 AttributeError。示範時要把 traceback 秀出來。
4. **IS-A vs HAS-A**：`Order` 不是 `List`，哪怕它「裝了」items。學員常寫 `class OrderList(list):`——這是 P3。教學重點：**先問關係**，再選繼承或組合。本課程不教多重繼承 / MRO / ABC，單一繼承已夠 90% 場景。
5. **`__str__` vs `__repr__`**：`__str__` 給人看、`__repr__` 給開發者看。只寫 `__str__` 在 REPL 會看到 `<Order object at 0x...>`（P4）。記住原則：`repr` 理想上能反貼回 Python 重跑。
6. **Method Chaining 的 `return self` 是 F5 地基**：每個方法 `return self`，鏈中一環漏寫就 `AttributeError: NoneType...`（P5）。這個模式是 F5 `DataCleaner` 的核心，本節埋下伏筆。

---

## 4. 學員常犯錯誤 (Common Pitfalls)

- **P1 · 把 `__x` 當加密**：`self.__password = pw` 然後以為外人拿不到。`obj._Class__password` 照樣拿得到。
- **P2 · 子類 `__init__` 漏呼 `super().__init__()`**：父類屬性沒設，兩個月後才爆出 AttributeError。
- **P3 · 用繼承解決組合問題**：`class OrderList(list):` 這種反模式，該用 `self.items = []` 組合。
- **P4 · 只寫 `__str__` 不寫 `__repr__`**：在 REPL / log / debug 看到 `<object at 0x...>`，看不到內容。
- **P5 · Chaining 方法漏 `return self`**：鏈中任何一環回 `None`，下一步就 `AttributeError: 'NoneType' object has no attribute ...`。

---

## 5. 提問設計 (Discussion Prompts)

1. 你寫的 class 裡，有哪些屬性你「完全不希望」使用者直接改？換成 `@property` 之後，呼叫端需要改嗎？
2. 如果下週要支援第四種資料來源（例如 Excel），你的 `DataReader` 家族要改哪裡？哪裡不用改？
3. `Order` 類需不需要 `__len__`？你會讓 `len(order)` 回傳什麼——商品種類數、總數量、還是金額？為什麼？
4. 如果 `DataCleaner` 的某個方法執行失敗，要 `return self` 讓鏈繼續，還是 `raise` 中斷？這兩種設計各有什麼代價？

---

## 6. 延伸資源 (Further Reading)

- Python 官方文件：Data Model §3.3 Special method names（`__str__` / `__repr__` / `__len__` / `__iter__` 完整列表）。
- PEP 8 §Naming Conventions（`_x` / `__x` 的官方慣例說明）。
- Fluent Python, Luciano Ramalho — Ch1 "The Python Data Model"、Ch11 "A Pythonic Object"。
- Martin Fowler 的 "Method Chaining" 與 "Fluent Interface" 短文。

---

## 7. 常見 Q&A

**Q1：Python 為什麼沒有 `private` 關鍵字？這樣不是很不安全嗎？**
A：Python 的設計哲學是「我們都是成年人」（consenting adults）。封裝是慣例，不是強制。好處是反射、debug、測試、mock 都方便；代價是靠團隊紀律。真正的安全（密碼、金鑰）要走 hash / 加密 / 權限系統，不該靠語法。

**Q2：什麼時候該用繼承、什麼時候該用組合？**
A：一句話——**IS-A 用繼承，HAS-A 用組合**。`CSVReader` *is a* `DataReader` → 繼承合理；`Cleaner` *has a* `Logger` → 組合。口訣：「能用組合不用繼承」。繼承耦合強、組合耦合弱，之後換實作成本差很多。

**Q3：`__repr__` 和 `__str__` 如果只實作一個，該選哪個？**
A：選 `__repr__`。因為 `print(obj)` 如果沒有 `__str__` 會退而求其次用 `__repr__`；反過來不會。所以 `__repr__` 是「底線」，`__str__` 是「錦上添花」。

**Q4：Method Chaining 是不是就等於 Pandas 的鏈式寫法？**
A：原理一樣——每個方法回傳物件本身（或新物件），就能接下一個。差別在 Pandas 回傳**新** DataFrame（immutable 風格），我們的 `DataCleaner` 回傳 `self`（mutable 風格）。兩種都有人用，F5 會用 `return self` 的版本以求簡單。

**Q5：本章為什麼不教多重繼承和 ABC？**
A：實務上資料工程 90% 用單一繼承就夠。多重繼承會牽扯 MRO（Method Resolution Order），教了反而增加混淆點。ABC（抽象基類）在本課程後期若真需要會補；目前用 `raise NotImplementedError` 就夠表達「這個方法必須被子類實作」。
