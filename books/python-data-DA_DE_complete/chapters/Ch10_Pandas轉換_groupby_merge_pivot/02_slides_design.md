# S3 — Pandas 轉換：groupby / merge / pivot｜投影片設計稿

> **時長**：2 hr（講授 70 min + 練習 40 min + QA 10 min）
> **張數**：22 張內容 + 封面 + 版權頁
> **設計軌道**：教學型（7 原型：MOTIVATION / CONCEPT-CARD / MECHANISM-FLOW / EXAMPLE-IO / PITFALL / PRACTICE-PROMPT / CHECKPOINT）
> **主色**：`#1B5E3F`；PITFALL 紅 `#C62828`；OK 綠 `#2E7D32`

符號說明：
- 🖼️ 投影片視覺
- 📣 講師一句話 takeaway
- 🎙️ 講師口白腳本

---

## S1 · MOTIVATION（SILENT）
🖼️ 深綠底，hero 三句：「groupby 是思考模型，merge 是通行證，pivot 是視角。」
📣 這一節用三個動詞把你帶離「單表查詢」。
🎙️ 「S2 你學會了讀和清，但真實世界資料不會只有一張表、也不會只問一個維度。S3 的三把刀一次講完——groupby 是你的思考模型、merge 是多表通行證、pivot 是把結果換個視角。」

## S2 · MOTIVATION（ASK + 數據卡）
🖼️ 大問句：「同一題三種寫法，背後運算一樣嗎？」數據卡 stat=3 刀。
📣 三種寫法互通，選哪個是品味問題。
🎙️ 「等一下看到同一題會有三種解法。你要問自己：它們的結果一樣嗎？選誰比較好？這會決定你寫的程式碼別人讀不讀得懂。」

## S3 · CONCEPT-CARD（條件篩選補強）
🖼️ 全頁 code panel：between / isin / 布林括號 / query 四段。
📣 篩選先寫乾淨，後面 groupby、merge 才不會打結。
🎙️ 「between 省掉兩個比較、isin 是多個 == 的簡寫、多條件一定要括號——這三招把你 80% 的篩選需求吃掉。」

## S4 · PITFALL（& 優先級陷阱）
🖼️ 紅／綠兩欄 VS：無括號 TypeError vs 有括號正確。
📣 `&` 優先級高於 `>`，少一個括號就炸。
🎙️ 「這是 Pandas 新手第一大坑。記住：`&` 是位元運算、優先級比比較運算高，所以每個比較一定要括起來。不想括就用 query。」

## S5 · MECHANISM-FLOW（Split-Apply-Combine）
🖼️ 左半：Split-Apply-Combine 示意圖（orders 依 region 切 3 組 → 各算 sum → 合併）；右半 code panel。
📣 背概念，不背 API；所有 groupby 題都是這三步。
🎙️ 「這是 1956 年提出的概念，到今天還是 Pandas / SQL / dplyr 的心臟。卡住的時候問自己：我在 split 什麼？apply 什麼？combine 出來是什麼形狀？」

## S6 · CONCEPT-CARD（groupby Level 1）
🖼️ 全頁 code panel：單欄單函式、多鍵、Top N、reset_index 四段。
📣 Level 1 就能吃掉 80% 日常報表。
🎙️ 「先求熟練這一層。`groupby → 選欄 → 聚合` 三步寫出來，再加個 sort_values + head 就是 Top N。」

## S7 · CONCEPT-CARD（groupby Level 2）
🖼️ Code panel：單欄多函式、字典版多欄多函式、lambda。
📣 `.agg([...])` 是 Level 2，一次算多個統計。
🎙️ 「Level 2 讓你一次算 count、sum、mean。但你會看到結果欄名是 tuple，下游很難接——這就是 Level 3 要解決的。」

## S8 · CONCEPT-CARD（groupby Level 3 具名聚合）
🖼️ Code panel：`agg(total=('amount','sum'), ...)` + 對比 Level 2。
📣 具名聚合 = 推薦寫法，結果欄名乾淨、下游最好接。
🎙️ 「以後寫報表都用這個格式：`new_col=(source_col, func)`。結果是平面 DataFrame、欄名自己取，後續 merge 和畫圖直接用，不用再 reset_index 修欄名。」

## S9 · PITFALL（忘 reset_index）
🖼️ VS 兩欄：左邊 KeyError，右邊加 reset_index 或 as_index=False。
📣 groupby 完要 merge / 畫圖，一律 reset_index()。
🎙️ 「MultiIndex 是隱形坑——你以為 region 是欄，其實它在 Index 裡。規則很簡單：要 merge、畫圖、匯出 CSV，先 reset_index。」

## S10 · EXAMPLE-IO（SQL 對照表）
🖼️ 編輯型表格：SQL 子句 / Pandas 對應 / 範例 / 備註 六列。
📣 熟 SQL 就能把 Pandas 當 SQL 寫。
🎙️ 「唯一不一樣的是 HAVING——Pandas 沒有，你得先 agg 再 query 篩結果。其他一對一。」

## S11 · CHECKPOINT（三種寫法）
🖼️ ASK 頁 + 數據卡 stat=3。
📣 能寫三種 = 真理解；只會一種 = 還在背 API。
🎙️ 「暫停兩分鐘，用 groupby().sum()、.agg()、pivot_table() 三種寫出『各 region 總營收』。結果應該一樣——為什麼？」

## S12 · CONCEPT-CARD（merge 基礎）
🖼️ Code panel：on / how / len 驗證 / indicator 四段。
📣 on + how 吃掉 90% merge 情境；merge 完一定比 len。
🎙️ 「記住兩件事：90% 實務用 `how='left'`、merge 完立刻 `assert len(merged) == len(orders)`。這兩個習慣讓你閃過 80% merge bug。」

## S13 · MECHANISM-FLOW（四種 how Venn 圖）
🖼️ 左：四聯 Venn 圖；右：2×2 矩陣卡片（inner / left / right / outer）。
📣 left 打 90%，outer 搭 indicator 當 debug 工具。
🎙️ 「這張 Venn 圖是面試常考——inner 取交集但會默默丟資料；left 從主表角度補資訊；outer 主要拿來 debug，加 indicator=True 看每筆來自哪邊。」

## S14 · CONCEPT-CARD（left_on / right_on / suffixes）
🖼️ Code panel：欄名不一致 + 同名非鍵欄 + rename 三段。
📣 `_x / _y` 是 pandas 在喊救命——自己指定 suffixes 或先 rename。
🎙️ 「看到 `_x / _y` 就代表你沒指定 suffixes。給它取個有意義的名字——`_order / _prod` 比 `_x / _y` 有用 10 倍。」

## S15 · PITFALL（筆數暴增）
🖼️ 紅／綠 VS：沒驗 key 炸 150 萬筆 vs 三行護身符。
📣 S3 第一名 bug；三行護身符背下來。
🎙️ 「orders 100 萬、customers 1 萬，merge 完變 150 萬——代表 customers 的 key 重複。記住三行：duplicated 驗前、validate='m:1' 驗中、len 驗後。」

## S16 · CONCEPT-CARD（三表鏈式 merge）
🖼️ Code panel：orders × customers × products 鏈式 merge + 驗收。
📣 從主表出發、每一步都 assert。
🎙️ 「鏈式 merge 看起來優雅，但每一步都可能爆。練習：打開 notebook、照這段跑一遍，故意把 customers 弄出重複 key，看 validate 怎麼救你。」

## S17 · CONCEPT-CARD + IMAGE（pivot_table）
🖼️ 左：long→wide pivot 結構示意；右：code panel（四件套 + 多 aggfunc）。
📣 想「行=A 列=B 值=m」就用 pivot_table。
🎙️ 「Excel 用戶會覺得親切——這就是樞紐分析。四件套 index / columns / values / aggfunc 一個都不能省，下一頁就是沒省的下場。」

## S18 · PITFALL（aggfunc 預設 mean）
🖼️ VS 兩欄：省略 aggfunc 算平均 vs 明確寫 sum。
📣 pivot_table 預設是 mean，不是 sum。
🎙️ 「這是我看過最常見的報表 bug——寫『總營收』但跑出來是平均。Pandas 的 pivot_table 和 Excel 樞紐不一樣，預設 mean 不是 sum。」

## S19 · EXAMPLE-IO（電商三問）
🖼️ 三欄 flow：Q1 各地區營收 / Q2 地區 Top3 / Q3 VIP 佔比。
📣 三題都走 Split-Apply-Combine；這就是 S3 的組合拳。
🎙️ 「三個真實商業問題、三段短程式。Q1 單層 groupby、Q2 兩層 groupby+nlargest、Q3 query 篩 VIP 再 sum。這堂課目標就是讓你看到任何商業問題都能拆成這種組合。」

## S20 · CONCEPT-CARD（groupby vs pivot_table）
🖼️ VS 兩欄 + delta badge「shape」。
📣 給人看 → pivot_table；接程式 → groupby。
🎙️ 「兩者本質一樣、都是 Split-Apply-Combine。差別只在結果形狀——wide 給人看、long 給程式吃。選錯會讓下游多寫一堆 reshape。」

## S21 · PRACTICE-PROMPT（SILENT）
🖼️ 深綠底 SILENT：🟡 品類營收 Top N + 🔴 RFM 粗估挑戰題。
📣 動手前先問：split 什麼？apply 什麼？
🎙️ 「接下來 40 分鐘動手。🟡 是基本款，🔴 給想挑戰的——RFM 只需要 groupby + agg，你已經有所有工具了。卡住先回去看 S5 的三步驟。」

## S22 · CHECKPOINT（收束）
🖼️ thesis_hierarchy：三把刀 / 四條紀律 + 銜接 S4 thesis。
📣 三把刀背下來 + 四條紀律抄到 checklist。
🎙️ 「今天結束前，把這兩段存成你的個人 checklist。S4 我們把這些結果畫出來、做時間序列 EDA——groupby / merge / pivot 的產物會一路用到 capstone。」
