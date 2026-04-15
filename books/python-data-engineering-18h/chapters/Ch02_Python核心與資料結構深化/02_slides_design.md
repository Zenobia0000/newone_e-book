# Ch02 · Python 核心快速複習與資料結構深化 — 投影片設計稿

**模組：** M1 系統前導與 Python 機制
**時數：** 1.5 小時（90 分鐘）
**投影片張數：** 17 張內容 + 封面 + 版權頁 = 19 張
**governing thought：** 學員已會語法，真正要的是兩件事——30 秒選對容器、能用 generator 處理比 RAM 大的資料。

---

## S1 · SILENT — 開場金句

- 🖼️ 畫面：深綠全幅底，中央白字一句英雄敘述，底下一道短白線作為斷句。
- 📣 畫面上的字：
  - 「10GB 檔案不會讓你的 RAM 爆炸——」
  - 「只要你選對迭代方式。」
- 🎙️ 講者這時說：今天這 90 分鐘不教你語法，你們都會。我只教你兩件事——第一件，30 秒內選對容器；第二件，用 generator 處理比記憶體還大的資料。這兩件做對了，你寫的 Python 才能從「能跑」變成「能上線」。

---

## S2 · ASK — 把張力打開

- 🖼️ 畫面：白底、上三分之一一個蘇格拉底式問句（深綠粗體 30pt），右下一張小資料卡（深綠細框）對比數字。
- 📣 畫面上的字：
  - 問句：「你要一次讀完 10GB log 找出所有 ERROR 行，需要多少 RAM？」
  - 資料卡：label「Naive vs Generator」 / stat「~200×」 / caption「naive readlines() 吃 10GB+；generator 逐行 < 50MB」
- 🎙️ 講者這時說：這題是面試常問，更是你每天會遇到。如果你答「10GB」，你就會在生產機上被 kill。正確答案是「不到 50MB」——差了 200 倍。這 200 倍來自今天下半場的主角：generator。

---

## S3 · MATRIX 2×3 — 型別系統快速校準

- 🖼️ 畫面：六格矩陣，左三格為「純值」（int/float/str/bool+None），右三格為「容器」（list/tuple/dict/set），右下格反白實綠做金句收束。
- 📣 畫面上的字：
  - 標題：「Python 六種內建型別：純值負責表達，容器負責組織」
  - 六格：數字型 int/float｜文字 str｜布林與空值 bool/None｜序列 list/tuple｜鍵值 dict｜集合 set
  - 反白格：「純值 = 一個事實；容器 = 一群事實的結構。」
- 🎙️ 講者這時說：先把地圖畫清楚。左邊這三格是「一個值就是一個值」，右邊這三格是「一群值要怎麼組織」。這堂課只深化右邊——因為資料工程 99% 的時間在處理一群值。

---

## S4 · FLOW — name → object → value 三層模型

- 🖼️ 畫面：三節點單向鏈，節點 1「name（便利貼）」→ 節點 2「object（記憶體物件）」→ 節點 3「value（實際資料）」；第二節點 highlight 反白，下方一條金句帶。
- 📣 畫面上的字：
  - 標題：「變數不是盒子，是便利貼——Python 的三層心智模型」
  - 三節點：name = 便利貼｜object = 被貼的東西｜value = 東西裡的內容
  - 底部金句：「a = b 不是複製，是貼第二張便利貼到同一個東西上。」
- 🎙️ 講者這時說：這張看似簡單，卻是所有踩坑的根。Python 裡的 `a = b` 不是把 b 的值複製給 a，是把「a」這張便利貼貼到 b 指向的同一個 object 上。理解這點，S7、S8 的所有地雷都會自動失效。

---

## S5 · TABLE — 四容器選用對照表

- 🖼️ 畫面：四欄表（容器｜何時用｜關鍵操作｜時間複雜度），深綠表頭白字，交替行灰底，五列（List/Tuple/Dict/Set + 底部一行金句）。
- 📣 畫面上的字：
  - 標題：「四種容器，四個不同任務——選錯會付兩種代價：效能與正確性」
  - List：順序、可變、可重複｜append/index｜O(1) append, O(n) search
  - Tuple：固定欄位、不可變｜解構、可當 key｜同 List，但不可變
  - Dict：key-value 查找｜get / items｜O(1) 平均
  - Set：去重、集合運算｜add / & \| -｜O(1) 平均
  - 底部金句：「要順序選 List；要唯一選 Set；要查找選 Dict；要保證不被改選 Tuple。」
- 🎙️ 講者這時說：這張要背。面試會問、code review 會戳。選錯容器的代價是：O(n²) 的迴圈你以為是 O(n)，或者你以為的「只讀」被別人改掉。

---

## S6 · MATRIX 2×2 — 可變/不可變 × 能否當 key

- 🖼️ 畫面：2×2 矩陣，橫軸「可變 / 不可變」、縱軸「能當 key / 不能當 key」；右上象限（不可變 × 能當 key）highlight 反白。
- 📣 畫面上的字：
  - 標題：「hashable = 不可變 = 能當 dict/set 的 key」
  - 左上：可變但想當 key？不行｜list, dict, set
  - 右上（highlight）：不可變且能當 key｜int, str, tuple, frozenset
  - 左下：可變且不當 key｜list, dict, set
  - 右下：不可變但你不需要｜int, str（只是當值）
  - 下方軸說明：「橫軸：可變性　·　縱軸：能否作 dict/set 的 key」
- 🎙️ 講者這時說：為什麼 list 不能當 dict key？因為 list 的內容會改，一旦改了，hash 就變了，dict 就找不到它。而 tuple 不會變，hash 永遠一致，所以可以。這是 Python 的第一性設計。

---

## S7 · CODE — `[[]] * 3` 踩坑示範

- 🖼️ 畫面：左側 code panel 深綠標籤「陷阱示範」＋灰底程式碼，右側 bullet note 列出「為什麼」。
- 📣 畫面上的字：
  - 標題：「`[[]] * 3` 不是建三個 list——是一個 list 被指向三次」
  - 程式碼：
    ```python
    a = [[]] * 3
    a[0].append(1)
    print(a)   # [[1], [1], [1]]  ← 全中
    ```
  - 右側 bullets：
    - `*` 是複製「參照」，不是複製 object
    - 三格便利貼貼在同一個 list 上
    - 正解：`[[] for _ in range(3)]`
    - 延伸：numpy zeros / pandas copy 都有類似陷阱
- 🎙️ 講者這時說：這段程式我每一屆都要示範一次，因為它會在最不該出錯的時候出錯——通常是凌晨三點生產事故。記住：要建 n 個獨立 list，用 list comprehension，不要用 `*`。

---

## S8 · VS — 淺拷貝 vs 深拷貝

- 🖼️ 畫面：雙欄 VS 對比，中央 VS 標、下方 delta pill「只差一層」；左欄「淺拷貝」、右欄「深拷貝」。
- 📣 畫面上的字：
  - 標題：「淺拷貝複製外殼，深拷貝連骨頭一起——巢狀結構只有後者安全」
  - 左欄「淺拷貝（shallow）」：
    - `list.copy()` / `copy.copy(x)` / `list(x)` / `x[:]`
    - 外層是新的，內層還是同一個
    - 巢狀 list 改內層會污染原本
    - 適用：扁平結構
  - 右欄「深拷貝（deep）」：
    - `copy.deepcopy(x)`
    - 遞迴複製到葉子節點
    - 改任何一層都不影響原本
    - 適用：巢狀 / 有 mutable 成員的物件
  - Delta badge：「只差一層」
  - 底部金句：「扁平用淺、巢狀用深；不確定時，先 deepcopy 保命。」
- 🎙️ 講者這時說：九成的 pandas/numpy bug 都是淺拷貝沒拷深造成的。有效的心法：看到「為什麼我改 b，a 也變了」，第一反應就是拷貝問題。

---

## S9 · MATRIX 2×2 — 30 秒容器決策樹

- 🖼️ 畫面：2×2 矩陣當決策圖，四個問題做選答；右下格 highlight 作為主建議。
- 📣 畫面上的字：
  - 標題：「30 秒容器選用決策：照順序問這四個問題」
  - 四格：
    - 左上：需要順序且允許重複？→ **List**
    - 右上：需要唯一性、要做集合運算？→ **Set**
    - 左下：要用 key 快速查找？→ **Dict**
    - 右下（highlight）：要保證欄位不會被改、能作 key？→ **Tuple**
  - 底部：「實務：80% List、15% Dict、4% Set、1% Tuple（配合 namedtuple / @dataclass(frozen)）」
- 🎙️ 講者這時說：寫程式前先花 10 秒問這四題，你的資料結構就會乾淨七成。Code review 我最常問的就是：「這裡為什麼不用 Set？」八成時候答不出來的人，該用 Set。

---

## S10 · ASK — 打開 Iterator 主題

- 🖼️ 畫面：白底 ASK，中央問句深綠粗體；右下資料卡顯示「for 只是一層糖」。
- 📣 畫面上的字：
  - 問句：「`for line in file:` 這一行，Python 底下到底發生了什麼？」
  - 資料卡：label「for 的真實身份」 / stat「糖」 / caption「for 是一層語法糖，底下是 iter() + next() + StopIteration 的契約」
- 🎙️ 講者這時說：從這裡開始，我們從「型別」走到「行為」。for 迴圈看起來很簡單，但它不是「從頭跑到尾」，而是「每次跟 iterator 要下一個」——這個差異就是 generator 能處理大檔的原因。

---

## S11 · FLOW — Iterator 協議

- 🖼️ 畫面：四節點單向鏈「Iterable → iter() → Iterator → next() → value / StopIteration」；最後節點 highlight；下方反白金句帶。
- 📣 畫面上的字：
  - 標題：「Iterator 協議只有兩個方法——這是 Python 迴圈的契約」
  - 節點：
    - Iterable｜caption: 有 `__iter__`
    - iter(x)｜caption: 呼叫 `__iter__`
    - Iterator｜caption: 有 `__next__`
    - next(it)｜caption: 取下一個 / 擲 StopIteration（highlight）
  - 底部金句：「for 迴圈 = 不斷呼叫 `next()`，直到收到 `StopIteration`。」
- 🎙️ 講者這時說：兩個魔術方法、一個例外——整個 Python 的迭代世界就建在這三樣東西上。list、dict、file、甚至 requests 的串流，都是這個協議的實作。

---

## S12 · CODE — yield 的暫停/續行

- 🖼️ 畫面：左 code panel 標籤「yield 示範」，右 bullet note 對照 yield 與 return。
- 📣 畫面上的字：
  - 標題：「yield 不是 return——它讓函式暫停、記住現場、下次從這裡繼續」
  - 程式碼：
    ```python
    def counter():
        print("start")
        yield 1     # ← 暫停在這裡
        print("resume")
        yield 2
        print("end")

    g = counter()           # 此時什麼都沒印
    next(g)  # start → 1
    next(g)  # resume → 2
    next(g)  # end → StopIteration
    ```
  - 右側 bullets：
    - `return` 一去不回；`yield` 可反覆回來
    - 函式成為 generator，呼叫時不執行，next() 時才執行
    - 每次 yield 把「局部變數 + 指令位置」凍住
    - 記憶體只裝「當下那一幀」
- 🎙️ 講者這時說：把函式想成一部連續劇，`return` 是最後一集、`yield` 是每週的結尾——下週從同一場景接著演。記住現場的能力，就是 generator 省記憶體的祕訣。

---

## S13 · VS — List Comp vs Generator Expression

- 🖼️ 畫面：雙欄 VS，左「List Comprehension」、右「Generator Expression」（右欄 delta badge「200× 記憶體差」）。
- 📣 畫面上的字：
  - 標題：「括號不同、命運不同：List 立刻算完全部，Generator 要一個算一個」
  - 左欄「List Comprehension `[]`」：
    - `[x*2 for x in range(10**8)]`
    - 一次算 1 億個，全存 RAM
    - 記憶體：~3.2 GB
    - 適用：小資料、要多次重讀
  - 右欄「Generator Expression `()`」：
    - `(x*2 for x in range(10**8))`
    - 只算當下一個
    - 記憶體：~200 bytes
    - 適用：大資料、只讀一遍
  - Delta badge：「200× 記憶體差」
  - 底部金句：「要存結果用 `[]`；要串管線用 `()`。」
- 🎙️ 講者這時說：這是全場最容易省錢的單一改動：把外層的 `[` 改成 `(`。同樣的 CPU、同樣的語義，記憶體省兩個數量級。

---

## S14 · IMAGE 真圖 — Generator 記憶體運作示意

- 🖼️ 畫面：橫幅寬框圖片佔位，下方一句 thesis 金句。示意圖左 10GB 硬碟檔案 → 中 yield「一次一行，僅一行在 RAM」→ 右 for 迴圈消費者；中間點出 generator 的「暫停指標」。
- 📣 畫面上的字：
  - 標題：「Generator 只在 RAM 中留一格——真正的資料還在硬碟上」
  - 圖片佔位：`[ 待補真圖 · Generator 記憶體運作示意 ]`（描述如上）
  - 下方 thesis：「你處理的不是資料本身，是『下一筆資料怎麼來』的指令。」
- 🎙️ 講者這時說：這張圖是你以後所有大檔處理的心智模型。硬碟是倉庫，generator 是輸送帶——你只看得到送過來的那一箱，後面還有多少，generator 記得、你不用。

---

## S15 · CODE — 實戰：10GB log 讀 ERROR 行

- 🖼️ 畫面：整頁 code panel（佔版面較大），右側 bullet note 列三個重點。
- 📣 畫面上的字：
  - 標題：「10GB log 讀 ERROR 行——三行 generator 解決」
  - 程式碼：
    ```python
    def read_errors(path):
        with open(path, encoding="utf-8") as f:
            for line in f:           # file object 本身就是 iterator
                if "ERROR" in line:
                    yield line.rstrip()

    # 使用端：完全不 care 檔案多大
    for err in read_errors("/var/log/app.log"):
        send_to_alert(err)
    ```
  - 右側 bullets：
    - `open()` 回傳 file 是天生 iterator，for line in f 是 O(1) 記憶體
    - yield 讓呼叫端也是「要一個給一個」
    - 組合起來：10 GB 流過，RAM 佔用 < 50 MB
    - 要過濾 / 轉換 / 去重，全都可以串下一個 generator
- 🎙️ 講者這時說：這 5 行就是本堂課的高潮。理解它之後，你再也不會寫 `f.readlines()` 這種會在生產炸 OOM 的程式碼。

---

## S16 · MATRIX 2×3 — 三個常用 Generator 模式

- 🖼️ 畫面：2×3 矩陣，上排三個模式、下排三個對應的一句總結；右下格 highlight 作為收束金句。
- 📣 畫面上的字：
  - 標題：「三個你會反覆使用的 generator 模式——吃下 80% 大檔情境」
  - 上排三格（模式）：
    - 「① 逐行讀」｜sub：`for line in open(path): yield line`
    - 「② 分塊讀」｜sub：`while chunk := f.read(1<<20): yield chunk`
    - 「③ 管線串接」｜sub：`map → filter → transform` 串成一條 iterator chain
  - 下排三格（用途 + 最後格 highlight 金句）：
    - 文字 log / JSONL｜sub：「逐行流處理」
    - 二進位檔 / 大 CSV｜sub：「固定記憶體窗口」
    - ETL / 資料清洗（highlight）：「惰性運算，耗時只在真正消費時發生」
- 🎙️ 講者這時說：這三個模式認得，你做的 ETL 就不會卡在 I/O。到 Ch6 我們會看到 pandas 的 `read_csv(chunksize=...)` 就是模式 ② 的包裝；Ch7 的 numpy 串接是模式 ③ 的變形。

---

## S17 · SILENT — 收束金句

- 🖼️ 畫面：深綠全幅，中央白字雙行金句，底下一道短白線。
- 📣 畫面上的字：
  - 「會選容器，代表你能寫對；」
  - 「會用 generator，代表你能寫大。」
- 🎙️ 講者這時說：這 90 分鐘的收束就一句：把對的資料結構放在對的位置，把對的迭代方式放在對的資料量——這兩件事決定你的程式是「玩具」還是「上線系統」。下一章（Ch3）我們會把這兩件事，用 lambda / map / comprehension 包成可以一行寫完的武器。
