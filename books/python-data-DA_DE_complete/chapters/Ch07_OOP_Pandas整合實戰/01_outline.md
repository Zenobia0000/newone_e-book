# F5 — OOP × Pandas 整合實戰｜講師講稿

> **課程時長**：1.5 小時（講授 55 min + 課堂練習 25 min + 能力盤點與下一步 10 min）
> **章節定位**：F1-F5 基礎段收斂章。不學新語法，把 F1-F4 + Pandas 組成可重用的 `DataCleaner`。

---

## 1. 本節目標 (Learning Objectives)

完成本節後，學員應能：

1. 從零設計一個資料管線類別，分辨「狀態（attribute）」與「動作（method）」的職責邊界。
2. 用 Method Chaining（`return self`）寫出可讀性高的資料處理工作流。
3. 用自訂 Exception（`DataValidationError`）把錯誤攔在邊界，讓上游能精準 catch。
4. 把 F2 的 Lambda / F3 的 `__init__` / F4 的繼承 + Pandas 的 `apply`、`dropna`、`fillna` 整合成 `DataCleaner`。
5. 盤點 F1-F5 + S1-S6 共 11 段能力地圖，知道接下來該深挖哪個方向。

---

## 2. 時間切分表

```
00:00-00:05  開場：F5 不是新語法，是收斂章（SILENT + ASK）
00:05-00:15  對照：零散 function 版 vs 類別管線版（VS + MATRIX）
00:15-00:25  設計：6 個方法簽名 + 自訂 Exception（CONCEPT + CODE）
00:25-00:35  總覽：六段管線 flow + 範例 I/O（MECHANISM-FLOW + CODE）
00:35-01:00  實作 Walkthrough：__init__ / validate / clean / apply / eda / export 六段 CODE
01:00-01:10  踩雷：P1-P5 全部走過一遍（兩張 PITFALL）
01:10-01:25  課堂練習：把 DataCleaner 改造成自己的領域（PRACTICE）
01:25-01:30  能力盤點 + 下一步五條路（MATRIX + TABLE + 結業 SILENT）
```

---

## 3. 關鍵教學點 (Key Teaching Points)

1. **收斂章的立論**：這 90 分鐘不教新語法，而是把 F1（系統）、F2（Lambda/Comprehension）、F3（`__init__`）、F4（繼承/封裝）+ Pandas 基礎組成一個「可被你未來工作重用」的 `DataCleaner`。開場一定要強調——這才是學完基礎該長出來的產物。
2. **狀態 vs 動作 2x2 是整章骨架**：學員最常見的誤區是把 `DataFrame` 當參數在 function 之間傳，而不是存成 `self.df`。第 4 張 MATRIX 要讓學員分清：`self.path` / `self.df` 是狀態；`validate` / `clean` / `apply` 是動作。這個框架想清楚了，後面的 6 個 method 簽名只是把它寫出來。
3. **`return self` 是鏈式的唯一靈魂**：每個改動 `self.df` 的 method，結尾都必須 `return self`，否則第二層 chain 就是 `None`。現場可以故意漏寫一次，讓學員看到 `AttributeError: 'NoneType' object has no attribute ...`，這個 traceback 印象最深。
4. **自訂 Exception 是工程紀律，不是炫技**：`raise Exception('revenue 負值')` 能跑，但上游要 catch 只能用 `except Exception`，連同其他毫無關聯的錯都會一起接進來。自訂 `DataValidationError(column, reason)` 讓錯誤帶上「欄位」與「原因」兩個欄位——上游 `except DataValidationError as e: log.warning(e.column, e.reason)` 才叫工程。
5. **`__init__` 裡就要 fail fast**：檔案不存在、欄位缺失，在 `__init__` 就 raise。很多學員會把驗證延後到 `validate` method，結果 `DataCleaner(path)` 就爆但訊息不明。`__init__` 負責「物件能不能活下來」，不能活就當場炸。
6. **apply_custom_transform 是 F2 Lambda 的實戰場**：學 F2 時 Lambda 看起來像玩具；在這裡 `df['col'].apply(func)` 把 `func` 當參數注入——這就是策略模式（Strategy Pattern），也是 F2 Lambda 存在的真正理由。
7. **能力盤點 + 下一步五條路線**：結尾的 F1-F5 + S1-S6 盤點不是裝飾，而是幫學員建立「我已經有什麼、接下來缺什麼」的自我認知。五條路線（SQL / sklearn / Polars+DuckDB / Airflow / 雲端）各有進入場景，強調「挑一條走 3 個月，比五條都碰過更值錢」。

---

## 4. 學員常犯錯誤 (Common Pitfalls)

- **P1 · method 忘記 `return self`**：chain 到第二層變 `None`，`AttributeError`。每個改動 `self.df` 的 method 都要 return self，即使是 `export_data` 這種「尾端」method 也要（為了一致性）。
- **P2 · `__init__` 不做驗證**：錯誤延後到 `clean_missing_values` 才爆，訊息指向下游、debug 往上追很痛。`__init__` 就該 fail fast。
- **P3 · `raise Exception('xxx')` 充當自訂錯誤**：上游無法精準 catch，語意全靠字串解析。正確是定義一個 `DataValidationError(Exception)`，帶 column/reason 欄位。
- **P4 · 30 行腳本硬包成 class**：一次性分析、notebook 內的 EDA，不需要 class。`class` 是為了「會被呼叫第二次以上」才包。Linus 的實用主義：先有重用需求，再做抽象。
- **P5 · 只學會範本、不會改造**：會背 DataCleaner 但換一份資料集（例如 HR 履歷、IoT 感測器）就完全卡住。課堂練習刻意要求學員加 method / 加規則 / 加 EDA 圖，就是在逼他們跨過這個門檻。

---

## 5. 提問設計 (Discussion Prompts)

1. 如果今天 `DataCleaner` 要處理「HR 員工資料」而不是「銷售資料」，`validate` 方法要改哪幾行？哪些規則會從 `revenue < 0` 變成什麼？
2. 為什麼 `apply_custom_transform` 要把 `func` 當參數傳進來，而不是把 10 種常見變換都寫成 method？（提示：開放封閉原則 / Strategy Pattern）
3. 什麼情況下你會選擇「不要包成 class」？舉一個你工作上的實例。

---

## 6. 延伸資源 (Further Reading)

- Wes McKinney《Python for Data Analysis》第 5、7 章（Pandas 資料清洗與 apply 模式）。
- Python Docs §Built-in Exceptions、§Defining Clean-up Actions（自訂 Exception 與 try/except 設計）。
- Martin Fowler "Fluent Interface"（Method Chaining 的經典論述）。
- pandas 官方 §DataFrame.pipe（進階版 Method Chaining，之後可以自學）。

---

## 7. 常見 Q&A

**Q1：那什麼時候該用 `df.pipe(func)` 而不是 Method Chaining？**
A：當你的轉換邏輯是「可重用的純函式」（跨多個 DataFrame 都用得到），用 `pipe`；如果是「特定管線的一步」，包在 class method 裡 + return self 更自然。pipe 是進階版，這章先掌握基本的。

**Q2：為什麼 `generate_eda_report` 的 `import matplotlib` 寫在 method 內？正式專案會這樣嗎？**
A：不會。正式專案 import 放檔案頂端。這章把 import 放 method 內是為了示範「這個 method 才用到 matplotlib，其他 method 不需要」的依賴邊界；實務上若類別會用到 matplotlib，import 就放頂端，不要繞。

**Q3：自訂 Exception 還要不要繼承 `ValueError` 而不是 `Exception`？**
A：看語意。`DataValidationError` 本質是「值不符合業務規則」，繼承 `ValueError` 也合理；但繼承 `Exception` 比較保險，上游如果 `except ValueError` 會連你的錯也吞掉。這章示範繼承 `Exception` 是為了讓「自訂錯誤」與「通用錯誤」的邊界更清楚。

**Q4：我下一步到底該學 SQL 還是 scikit-learn？**
A：看工作性質。要接資料庫、要跟後端溝通 → SQL。要做預測、要往 ML 走 → sklearn。不要五條都碰；挑一條走 3 個月。
