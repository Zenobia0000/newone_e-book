# F2 — Python 核心與資料結構深化｜講師講稿

> **課程時長**：90 分鐘（講授 55 min + 課堂練習 25 min + QA 10 min）
> **對應 Notebook**：`F2_Python核心/F2_containers_and_generators.ipynb`
> **受眾**：只有 Python 基礎的非理工背景學員（商管/人文/行銷/行政/設計/醫護）
> **銜接**：F1 (OS/計概) ← F2 → F3 (OOP) / S1 (NumPy) / S2 (Pandas I/O)

---

## 1. 本節目標 (Learning Objectives)

完成本節後，學員應能：

1. 在 30 秒內用生活化類比判斷該用 List / Dict / Tuple / Set 中的哪一個。
2. 解釋「變數是便利貼」的心智模型，並避開淺/深拷貝在巢狀結構上的坑。
3. 用自己的話說明 for 迴圈在做什麼：不斷跟容器要下一個，直到它說「沒了」。
4. 用 yield 寫一個「逐頁翻書」的 generator，處理大於記憶體的資料。
5. 指認 `pd.read_csv(chunksize=...)` 背後的引擎就是今天教的 yield。

---

## 2. 時間切分表

```
00:00-00:05  開場：Pandas 60% 的坑根源在 Python 基礎（S1-3）
00:05-00:25  核心 1/3：四容器生活類比 + 決策樹 + 商業場景（S4-7）
00:25-00:45  核心 2/3：便利貼心智模型 + 可變性 + 兩個經典坑（S8-11）
00:45-01:05  核心 3/3：Iterator/Generator + 10GB log + chunksize 銜接（S12-16）
01:05-01:15  最後一坑 + 練習（S17-18）
01:15-01:25  Checkpoint 快問 + Pyramid 收束（S19-20）
01:25-01:30  收束 + QA（S21）
```

---

## 3. 關鍵教學點 (Key Teaching Points)

1. **受眾不是 CS 背景——術語要換成生活話**：把 hash table 說成「字典查字」、把 iterator 說成「跟容器要下一個」、把 generator 說成「逐頁翻書」、把變數說成「便利貼」。學員聽得懂，才會願意聽下去。
2. **容器選用是商業決策題，不是語法題**：S5 的決策樹四個問題，用「營業額紀錄 / 客戶編號去重 / 員工 ID 查名 / 郵遞區號鎖死」這種場景，而不是用抽象例子。
3. **淺深拷貝直接連結 Pandas 的 `SettingWithCopyWarning`**：學員之後用 Pandas 看到這個警告一定會想起 F2。別跳過這個連結。
4. **Generator 要講「逐頁翻書」而非「惰性求值」**：前者人人聽得懂、後者只有學過 FP 的懂。畫面上配 S15 的 10GB log 範例 + S16 的 chunksize 對照，讓他們看到同一套心智模型跨章節復用。
5. **三張銜接導引張數充足**：S7（dict → DataFrame row）、S11（copy → SettingWithCopyWarning）、S16（yield → chunksize）。這三張決定他們下週學 Pandas 時會不會卡住。

---

## 4. 學員常犯錯誤 (Common Pitfalls)

- **P1 `[[]] * 3`**：以為建了三個獨立 list，實際是一個 list 被貼了三張便利貼。改用 `[[] for _ in range(3)]`。
- **P2 `b = a` 當成複製**：這只是再貼一張便利貼到同一個東西上，改 b 會動到 a。
- **P3 淺拷貝踩巢狀**：`list.copy()` 只複製外殼，內層仍共用——巢狀資料必用 `copy.deepcopy()`。
- **P4 用 list 當 dict key**：會直接報 `TypeError: unhashable type: 'list'`——因為會變的東西 Python 記不住它的指紋。
- **P5 generator 重複迭代**：第二次 `list(g)` 會是空的，因為已經翻到書的最後一頁了。

---

## 5. 提問設計 (Discussion Prompts)

1. 你現在手上有 10 萬筆訂單編號要檢查「某 ID 有沒有下過單」，用 List 跟用 Set 差多少？為什麼？
2. 為什麼 Python 規定「會變的東西不能當 dict 的 key」？若允許會發生什麼？
3. 如果要處理一個 20GB 的 CSV，你會全部讀進來還是分塊？分塊的話，這跟今天教的 yield 有什麼關係？

---

## 6. 延伸資源 (Further Reading)

- Python 官方 tutorial §5.1「More on Lists」與 §9.9「Iterators」。
- Luciano Ramalho《Fluent Python》第 3 章 Dict/Set、第 17 章 Generators（進階學員推薦）。
- Pandas 官方文件 `read_csv(chunksize=...)` 的範例——驗證今天的 yield 在實務裡的樣子。

---

## 7. 常見 Q&A

**Q1：list 跟 tuple 看起來很像，為什麼要分兩個？**
A：list 是讓你「之後還要加東西、改東西」用的；tuple 是寫好就鎖死、保證不被改。固定欄位（如 (縣, 市, 郵遞區號)）用 tuple 比較安全，還能當 dict 的 key。

**Q2：什麼時候該 deepcopy，什麼時候不用？**
A：扁平（例如 `[1, 2, 3]`）用 `.copy()` 就夠；巢狀（例如 `[[1,2],[3,4]]` 或 dict 裡面還有 list）就要 `copy.deepcopy`。不確定時先 deepcopy 保命，效能之後再優化。

**Q3：generator 跟 list 到底差在哪？我什麼時候該用哪個？**
A：資料量小、需要多次讀、要用 `[i]` 取 → 用 list。資料量大、只需讀一遍、記憶體緊 → 用 generator。下週你會看到 `pd.read_csv(chunksize=...)` 正是為了讀大檔而設計的 generator。
