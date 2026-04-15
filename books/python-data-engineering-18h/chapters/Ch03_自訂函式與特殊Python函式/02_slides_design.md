# Ch03 自訂函式與特殊 Python 函式 — Slides Design

> Governing thought：Lambda / map / filter / Comprehension 不是炫技糖衣，是為 Pandas `apply` 鋪跑道。
> 20 張內容 + 封面 + 版權頁。配色：黑 + 灰 + 深綠 (#1B5E3F)。

---

## S1 · SILENT · 開場主張

- 🖼️ 畫面：全頁深綠底，白色 hero 字置中。
- 📣 畫面上的字：「會宣告，就少寫 80% 迴圈。」
- 🎙️ 講者這時說：「這章最重要的一句話先給你。你後面會看到很多糖衣語法，但核心只有一件事——從『一步一步告訴電腦怎麼做』，換成『一句話講清楚我要什麼』。」

## S2 · ASK · 痛點勾引

- 🖼️ 畫面：白底，上方巨大問句；右下 data card（73% / 89%）。
- 📣 畫面上的字：「為什麼資深資料工程師讀到 `for` 迴圈就皺眉？」／data card：「Pandas 使用者 73% 日常用 apply(lambda)；Comprehension 使用率 89%」。
- 🎙️ 講者這時說：「不是 for 不好，是多數時候有更貼近需求的寫法。這章三件武器——Lambda、map/filter、Comprehension——都是給你讀得像英文的宣告式 Python。」

## S3 · MATRIX 2×3 · 函式參數五種

- 🖼️ 畫面：2×3 綠框矩陣；左上 highlight。
- 📣 畫面上的字：標題「函式參數五種分工，位置由嚴到鬆」；六格：
  1. 位置參數 `def f(x, y)`（highlight）
  2. 關鍵字參數 `f(x=1)`
  3. 預設參數 `def f(x=10)`
  4. `*args` 收散彈
  5. `**kwargs` 收規則
  6. `/` `*` 分隔（進階）
- 🎙️ 講者這時說：「由嚴到鬆五種。最前面是位置、最後面是 kwargs。寫 API 時你會想把最重要的放前面當位置參數，把可選的當 kwargs。」

## S4 · CODE · `*args` / `**kwargs` 實戰

- 🖼️ 畫面：單一 code panel，左碼右 bullets。
- 📣 畫面上的字：標題「*args 收散彈，**kwargs 收規則」；code：
  ```
  def validate(row, *required_fields, **rules):
      for f in required_fields:
          if f not in row: return False
      for k, rule in rules.items():
          if not rule(row.get(k)): return False
      return True

  validate(row, "id", "email",
           age=lambda x: 0 < x < 120,
           email=lambda s: "@" in s)
  ```
  bullets：「*args → tuple；**kwargs → dict」「規則用 lambda 注入」「日後 DataCleaner 的核心型式」。
- 🎙️ 講者這時說：「這就是 Ch10 DataCleaner 的雛形。不同資料集、不同規則，我不用每次改函式簽章，規則從 kwargs 進來就好。」

## S5 · VS-CODE · 可變預設值陷阱

- 🖼️ 畫面：上 BEFORE code panel（淺灰 label）、下 AFTER code panel（深綠 label）。
- 📣 畫面上的字：標題「可變預設值：Python 最常被當面試考的陷阱」
  - BEFORE：`def add(item, bag=[]): bag.append(item); return bag` bullets：「第一次呼叫 bag=[1]」「第二次呼叫 bag=[1,2]」「預設值在『定義時』建立一次，終身共用」。
  - AFTER：`def add(item, bag=None): bag = bag or []; ...` bullets：「None 是不可變哨兵」「每次呼叫都重建」「PEP 8 / Ruff B006 會直接告警」。
- 🎙️ 講者這時說：「這個雷幾乎所有人踩過。記住：預設值是在 def 那一刻就算好存在函式物件上，不是每次呼叫重建。可變物件當預設值 = 全域狀態藏在簽章裡。」

## S6 · CODE · LEGB 作用域（需真圖）

- 🖼️ 畫面：左側 image placeholder（LEGB 四層同心圓示意）；右側 code panel。
- 📣 畫面上的字：標題「LEGB：由內往外找一個名字」
  - code：
    ```
    x = "Global"
    def outer():
        x = "Enclosing"
        def inner():
            x = "Local"
            print(x)      # Local
        inner()
        print(x)          # Enclosing
    outer()
    print(x)              # Global
    ```
  - 左圖佔位：四層由內到外 Local → Enclosing → Global → Built-in。
- 🎙️ 講者這時說：「Python 找變數的規矩就四層，由內往外。90% 的 NameError / UnboundLocalError 都是沒搞清楚自己在哪一層。」

## S7 · TABLE · global / nonlocal 的真正代價

- 🖼️ 畫面：editorial table，四欄。
- 📣 畫面上的字：標題「能不用就不用：global / nonlocal 的真正問題不是語法」
  - 欄位：關鍵字 / 作用 / 合理場景 / 為什麼少用
  - 列：
    - `global x` / 從函式內改全域名字 / module-level flag、logging 設定 / 呼叫端無法預測結果，測試難 mock
    - `nonlocal x` / 改外層函式的名字 / Closure 累加器 / 只有在寫 decorator / closure 才該出現
    - （避免）/ —— / 大多用回傳值即可 / 回傳值 > 共用狀態
- 🎙️ 講者這時說：「看到 global 就該問一句：真的沒辦法用回傳值嗎？99% 時候有。Pandas 的 pipeline 寫多了你就懂：共享狀態會讓 pipeline 不可重跑。」

## S8 · ASK · Lambda 存在的理由

- 🖼️ 畫面：ASK 版型，白底綠字問句；右下 data card。
- 📣 畫面上的字：「如果 Lambda 只能寫一行，它能解決什麼樣的問題？」／ card「Lambda 設計意圖：當函式 / 臨時 / 即用即丟 / 一行以內」stat「< 1 行」。
- 🎙️ 講者這時說：「答案是：把小邏輯塞進別人要吃 function 參數的地方。sorted(key=)、map()、filter()、pandas apply()——它們要一個 callable，你給個即用即丟的 lambda 剛剛好。」

## S9 · CODE · def vs lambda 邊界

- 🖼️ 畫面：上下兩個 code panel，左碼右 bullets。
- 📣 畫面上的字：標題「def 與 lambda 的邊界：一行是線，過線就 def」
  - LAMBDA OK：`square = lambda x: x**2` bullets：「單一 expression」「即用即丟」「傳給 HOF 當 callback」。
  - 過線該 def：
    ```
    # BAD: lambda row: row['p']*0.9 if row['p']>100 else row['p']
    def discount(row):
        if row["p"] > 100:
            return row["p"] * 0.9
        return row["p"]
    ```
    bullets：「可讀性 > 一行主義」「有分支 / 例外 / 多行 → def」「def 才能加 docstring、單元測試」。
- 🎙️ 講者這時說：「Lambda 沒有名字、沒有 docstring、沒有註解空間。超過一行邏輯就去 def，這不是品味問題，是維護成本問題。」

## S10 · CODE · map / filter / sorted(key=)

- 🖼️ 畫面：單一 code panel。
- 📣 畫面上的字：標題「三件套：告訴 Python『做什麼』，不寫『怎麼做』」
  - code：
    ```
    prices = [120, 80, 200, 50]

    # map：全部套函式
    discounted = list(map(lambda x: x*0.9, prices))

    # filter：保留符合條件
    bigs = list(filter(lambda x: x > 100, prices))

    # sorted(key=)：自訂排序鍵
    users = [{"age":30}, {"age":22}, {"age":45}]
    by_age = sorted(users, key=lambda u: u["age"])
    ```
  - bullets：「map/filter 回傳 iterator，要 list() 才物化」「sorted 是穩定排序」「這三招是 Pandas apply / sort_values 的祖先」。
- 🎙️ 講者這時說：「把這三個寫進肌肉記憶。Ch08 你會發現 `df.sort_values(key=...)` / `df['col'].apply(...)` 就是同樣的概念搬到表格上。」

## S11 · VS · map+filter 與 List Comprehension

- 🖼️ 畫面：VS 雙欄，中間 VS 徽章。
- 📣 畫面上的字：標題「兩種寫法，一個是 Python 偏愛的母語」
  - 左欄 map+filter：「list(map(lambda x: x*0.9, filter(lambda x: x>100, prices)))」/「要 list() 物化」/「巢狀 lambda 難讀」/「函數式語言的遺產」。
  - 右欄 List Comp：「[x*0.9 for x in prices if x > 100]」/「讀起來就是需求本身」/「CPython 內部優化更快」/「Pythonic 首選」。
  - delta：「可讀性\n單向勝」
  - summary：「寫得出 map+filter 代表你懂原理；寫 Comprehension 代表你在 code review 會過。」
- 🎙️ 講者這時說：「原理都是一樣的，但 Guido van Rossum 自己公開說過：Comprehension 就是 Python 想讓你寫的版本。map/filter 能不用就不用。」

## S12 · CODE · List Comprehension 三段式

- 🖼️ 畫面：單一 code panel。
- 📣 畫面上的字：標題「List Comprehension 三格：輸出 / 來源 / 條件」
  - code：
    ```
    # 三格骨架
    # [  expr    for  x  in  iterable   if  cond  ]
    #    ↑輸出        ↑來源              ↑可選條件

    squares       = [x**2 for x in range(10)]
    big_squares   = [x**2 for x in range(10) if x > 5]
    cleaned_names = [n.strip().lower()
                     for n in raw_names
                     if n and n.strip()]
    ```
  - bullets：「輸出可以是任何 expression」「條件可連鎖：if a if b」「換行排版：expr / for / if 一格一行」。
- 🎙️ 講者這時說：「讀 Comprehension 從中間讀：先看 for，再看右邊 if 篩過沒有，最後看最左邊輸出什麼。三秒內要能講完一行 comprehension 在做什麼。」

## S13 · CODE · Dict / Set Comprehension

- 🖼️ 畫面：單一 code panel。
- 📣 畫面上的字：標題「同骨架，換外框：{} 就換容器」
  - code：
    ```
    # Dict Comprehension
    name_age = {u["name"]: u["age"] for u in users}
    inverse  = {v: k for k, v in name_age.items()}

    # Set Comprehension（自動去重）
    domains = {email.split("@")[1] for email in emails}

    # Generator Expression（不物化）
    total = sum(x**2 for x in range(10**7))
    ```
  - bullets：「{} + key: value → dict」「{} 只有 value → set」「() → generator，見 S17」「四兄弟同根同源」。
- 🎙️ 講者這時說：「看到括號就能判斷結果型態：方括號是 list，大括號配冒號是 dict，大括號沒冒號是 set，圓括號是 generator。」

## S14 · CODE · 巢狀 Comprehension 的界線

- 🖼️ 畫面：上下兩個 code panel。
- 📣 畫面上的字：標題「兩層可讀，三層就拆」
  - OK（兩層扁平化）：
    ```
    matrix = [[1,2,3], [4,5,6]]
    flat = [x for row in matrix for x in row]
    ```
    bullets：「讀順序：由左而右對應 for 的由外而內」「兩層且無 if 仍可讀」。
  - NOT OK（三層 + 條件）：
    ```
    # 不要這樣
    result = [f(x, y, z)
              for x in xs for y in ys for z in zs
              if x>0 if y<z if g(x,y)]
    ```
    bullets：「三層 + 多條件 → 拆回 for」「for 迴圈可加 log、可 debug」「可讀性 > 炫技」。
- 🎙️ 講者這時說：「單行主義不是信仰。寫給人看的優先於寫給 interpreter 看的，這是 PEP 20 的話。」

## S15 · MATRIX 2×2 · 選型四象限

- 🖼️ 畫面：2×2 矩陣。
- 📣 畫面上的字：標題「四種寫法的選型：資料量 × 可讀性需求」
  - 左上（小量 × 簡單）：「List Comprehension」highlight／「90% 日常場景首選／簡潔、快、Pythonic」
  - 右上（大量 × 簡單）：「Generator Expression」／「資料過大 / 一次讀不進記憶體／用 () 省 memory」
  - 左下（小量 × 複雜邏輯）：「def + 普通 for」／「邏輯複雜要 log、要例外處理／可讀優先」
  - 右下（大量 × 複雜邏輯）：「def + yield + pipeline」／「串流處理／Ch06 例外 + Ch10 整合」
- 🎙️ 講者這時說：「先問兩件事：資料量會不會爆 memory？邏輯能不能一行講完？答案組合就告訴你該用哪種寫法。」

## S16 · TABLE · 時間複雜度直覺

- 🖼️ 畫面：editorial table 四欄。
- 📣 畫面上的字：標題「時間複雜度直覺：線性是命，巢狀是罪」
  - 欄：寫法 / 複雜度 / 相對速度 / 何時該警覺
  - 列：
    - `for x in xs:` 單層 / O(N) / 基準 1× / 100 萬以下都沒事
    - `[f(x) for x in xs]` Comprehension / O(N) / ~0.7× / CPython 內部優化，一般更快
    - `for x in xs: for y in ys:` 巢狀 / O(N×M) / N×M × / 兩邊都是千級就小心
    - `x in some_list` 成員查找 / O(N) 每次 / 慢 / 改用 set 變 O(1)
    - early `break` / O(k)，k ≤ N / 視情況 / 找到就停比全掃快
- 🎙️ 講者這時說：「你不用背 Big-O，只要有三個直覺：單層 OK、巢狀看乘積、查找要用 set 或 dict。」

## S17 · VS-CODE · List vs Generator

- 🖼️ 畫面：上下兩個 code panel，右下 data badge。
- 📣 畫面上的字：標題「差一個括號，記憶體差 1000 倍」
  - LIST：
    ```
    sq = [x**2 for x in range(10_000_000)]
    sum(sq)   # ~350 MB 常駐
    ```
    bullets：「立刻物化全部」「可多次迭代」「佔約 350 MB」。
  - GENERATOR：
    ```
    sq = (x**2 for x in range(10_000_000))
    sum(sq)   # ~128 B 整段流
    ```
    bullets：「懶求值，yield one by one」「只能迭代一次」「常駐僅 ~128 B」「Pandas chunked read 就是這個概念」。
- 🎙️ 講者這時說：「只要你發現 list 只會『跑一遍然後丟』，就換成 generator。記憶體差 N 倍，你在做大資料時會回來謝我。」

## S18 · PHOTO-CODE · 預告 Pandas apply（需真圖）

- 🖼️ 畫面：左半 image placeholder（Pandas apply 官方文件截圖）；右半 code panel。
- 📣 畫面上的字：標題「Lambda 的真實棲地：Pandas apply（Ch08 主場）」
  - 左圖佔位：pandas DataFrame.apply 官方文件首屏。
  - code：
    ```
    # Ch03 學的 map
    list(map(lambda x: x*0.9, prices))

    # Ch08 你會天天寫
    df["price"] = df["price"].apply(lambda x: x*0.9)
    df["tier"]  = df["amount"].apply(
        lambda x: "high" if x > 1000 else "low"
    )
    ```
  - bullets：「apply = 把 lambda 套到每一列」「概念與 map 完全一致」「Ch03 練好的 lambda 功力直接可用」。
- 🎙️ 講者這時說：「這張是給你一個預告：Ch03 不是教完就丟。你現在學的每一招，Ch08 都會再以 Pandas 版本出現一次。重複是刻意的，這叫螺旋上升。」

## S19 · PYRAMID · 收束

- 🖼️ 畫面：thesis_hierarchy 兩層堆疊。
- 📣 畫面上的字：標題「Ch03 收束：參數四件 + Lambda 三件套 + Comprehension 三格」
  - 上層「Python 特殊機制三件套」：
    - 「Lambda：即用即丟，一行為限」
    - 「map / filter / sorted(key=)：聲明式處理 iterable」
    - 「Comprehension：[expr for x in iter if cond]」
  - 下層「設計紀律」：
    - 「可變預設值 → None + 首行初始化」
    - 「global / nonlocal 能不用就不用」
    - 「巢狀 Comprehension 超過兩層就拆回 for」
  - thesis：「Ch04 起進入 OOP：把這些函式技巧升級為『物件方法』，為 Ch10 DataCleaner 奠基。」
- 🎙️ 講者這時說：「這一章教完，Python 語法正式結束。接下來要把這些函式裝進類別裡，變成一個可重用的資料清理管線。」

## S20 · SILENT · 收尾主張

- 🖼️ 畫面：全頁深綠底，白色 hero 字。
- 📣 畫面上的字：「好程式不是寫得多，是說得準。」
- 🎙️ 講者這時說：「記住今天這句話。你之後寫 Pandas、寫 scikit-learn Pipeline，都會用到這個心法。」
