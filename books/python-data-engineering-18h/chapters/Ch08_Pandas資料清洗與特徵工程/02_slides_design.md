# Ch08 · 02_slides_design — SOP §4.2

- 章節：Pandas 資料清洗與特徵工程（M3 · 3.5 hr · 23 張內容 · 本課程最長章）
- Governing thought：Pandas 不是 API 字典，是資料工程師的工作台 — 讀→看→篩→清→轉→聚→併。
- 配色：黑 + 灰 + 深綠（#1B5E3F）
- 每張格式：🖼️（視覺規格）/ 📣（文字骨架）/ 🎙️（口頭引導）

---

## S1 · SILENT — 開場第一口氣
- 🖼️ 深綠滿版，白字 hero。
- 📣 「Pandas 不是 API 字典，\n是資料工程師的工作台。」
- 🎙️ 上一章 NumPy 是引擎，今天的 Pandas 是駕駛艙。我們不背 API，我們建立流水線。

## S2 · ASK — 為什麼大家還是邊查邊寫
- 🖼️ 白底，大哉問 + 右下 data card。
- 📣 Q：「如果 80% 的工作時間花在清洗，為什麼大家還是邊查文件邊寫？」
  Data card：label「Kaggle 2024 State of ML & DS Survey」· stat「80%」· caption「受訪資料工作者選 pandas 作為日常工具，且坦承『大多 API 用過就忘』」
- 🎙️ 因為大家把 pandas 當字典查，沒當作工作流學。今天我們把流程內化，API 就會自然落位。

## S3 · MATRIX 2×3 — Series / DataFrame / Index 三角
- 🖼️ 2×3 方陣，左欄三個型別、右欄三個原則。
- 📣 標題「Series / DataFrame / Index 三角關係」
  cells：
  - `Series`（一維帶索引，highlight）— NumPy 陣列 + Index 標籤
  - `DataFrame`（二維表）— 多個 Series 共用同一 Index
  - `Index`（標籤）— 不是欄位、不是 row number，是「資料的名字」
  - 對齊（alignment，highlight）— 兩個 Series 相加自動依 Index 對齊
  - 不可變（immutable）— Index 一旦建立不能 in-place 改值
  - `reset_index` / `set_index` — 在 Index 與欄位之間切換的兩個門
- 🎙️ 學 pandas 的第一個分水嶺，就是把 Index 當「資料的名字」而不是「欄位」。

## S4 · CODE — 三種建立方式 + 6 個觀察方法
- 🖼️ 滿版 code panel + 右側 bullets。
- 📣 code 上半：from dict / from list of dicts / from CSV；下半：head/tail/info/describe/dtypes/shape。
  bullets：每拿到新資料先跑這 6 個方法、`info` 看型別與缺失、`describe` 看分佈、`dtypes` 是 debug 第一站。
- 🎙️ 不要急著篩選，先「看」清楚 — 工程師的職業病是直接寫 query，職業修為是先 `info()`。

## S5 · IMAGE + CODE — Index 對齊
- 🖼️ 左：Index 對齊示意圖 placeholder（兩個 Series 不同 Index 相加，缺位 NaN）；右：對應 code。
- 📣 code：兩個 Series（A、B、C）+（B、C、D）相加 → 結果 A、D 為 NaN。
  bullets：對齊是 pandas 的隱藏外掛、不對齊就 NaN、Excel 沒這功能、合併操作底層原理。
- 🎙️ 這張圖看懂了，你就懂為什麼 pandas 比 Excel 強 — 它幫你對齊「名字」，不是對齊「位置」。

## S6 · MATRIX 2×2 — 四把鑰匙
- 🖼️ 2×2 方陣。
- 📣 標題「取資料的四把鑰匙：loc / iloc / 布林 / query」
  cells：
  - `df.loc[label]`（標籤索引，highlight）— 用 Index 名字取
  - `df.iloc[pos]`（位置索引）— 用整數位置取
  - `df[df.col > x]`（布林遮罩，highlight）— 條件式篩選
  - `df.query("col > x")` — 字串條件，可讀性高、可參數化
- 🎙️ 四把鑰匙各有主場，沒有最強只有最對 — 用標籤就 loc、用位置就 iloc、邏輯複雜就 query。

## S7 · VS-CODE — loc vs iloc
- 🖼️ 上下兩個 code panel：BEFORE = iloc 易混、AFTER = loc 清晰。
- 📣 上 panel：iloc 切片 `df.iloc[0:3, 0:2]`（包前不包後）；下 panel：loc 切片 `df.loc['A':'C', 'name':'age']`（包前包後）。
  bullets：iloc 像 Python list、loc 像 SQL；混用是 bug 第一名。
- 🎙️ 一個包後一個不包後 — 這是無數 bug 的原點，務必背下。

## S8 · CODE — query 與 Copy-on-Write
- 🖼️ 滿版 code panel。
- 📣 code：多條件用 `&` `|` 加括號 → 改用 `query("age > 30 and city == 'Taipei'")`；最後示範 `df.loc[df.age>30, 'tag'] = 'senior'` 與 SettingWithCopyWarning。
  bullets：query 可讀性提升、字串可參數化、pandas 2.x 預設 Copy-on-Write、鏈式賦值即將被棄用。
- 🎙️ Copy-on-Write 是 pandas 2.x 最大改動 — 它讓「改一份不影響另一份」成為預設行為。

## S9 · ASK — 缺失值的真相
- 🖼️ 白底 + data card。
- 📣 Q：「缺失值出現了 — 你第一個想到 dropna() 還是先問為什麼缺？」
  Data card：label「真實專案缺失值來源拆解」· stat「3 種」· caption「『沒填』、『編碼問題』、『計算產生』— 處理策略截然不同」
- 🎙️ dropna 是無腦解，但無腦解通常會丟掉訊號。先問為什麼缺。

## S10 · IMAGE + CODE — 缺失值決策樹
- 🖼️ 左：缺失值決策樹 placeholder；右：對應 code。
- 📣 code：`df.isna().sum()` 偵測 → 三種來源分流 → 對應 API。
  bullets：先偵測再處理、編碼問題用 `na_values=['-', 'N/A']` 在讀檔時擋下、計算產生通常該保留。
- 🎙️ 決策樹照著走，至少不會在 review 時被問「你為什麼這樣補？」。

## S11 · TABLE — 缺失值四種策略
- 🖼️ Editorial table，4 欄。
- 📣 標題「缺失值四種策略：何時 drop / fillna / ffill / interpolate」
  header：策略 / API / 何時用 / 風險
  rows：
  - 整列刪除 / `dropna()` / 缺失少且資料量充足 / 可能丟掉「缺本身就是訊號」
  - 整欄刪除 / `dropna(axis=1, thresh=...)` / 整欄高比例缺失 / 損失維度
  - 填補定值 / `fillna(0/mean/median/mode)` / 缺失有合理替代值 / 改變分佈
  - 向前 / 內插 / `ffill / bfill / interpolate()` / 時間序列 / 假設「鄰近=相似」
- 🎙️ 四種策略，沒有預設答案 — 看資料、看下游、看 stakeholder。

## S12 · SILENT — Lambda 找到主場
- 🖼️ 深綠滿版。
- 📣 「Ch3 學過的 lambda，\n今天在 Pandas 找到主場。」
- 🎙️ Ch3 教 lambda 時你可能覺得「這跟一般 def 差不多」— 今天 apply + lambda 是 pandas 最常見的搭配，你會明白為什麼要學它。

## S13 · CODE — apply 三層級
- 🖼️ 滿版 code panel。
- 📣 code：
  - `Series.apply(func)` — 對每個元素
  - `DataFrame.apply(func, axis=0)` — 對每欄
  - `DataFrame.apply(func, axis=1)` — 對每列
  - `Series.map(dict)` — 字典映射（取代 deprecated 的 applymap）
  bullets：lambda 一行解、複雜邏輯抽 def、axis=0 是 column-wise（預設）、axis=1 才是 row-wise。
- 🎙️ axis 是 pandas 學員最常搞錯的 — 預設 0 是「沿列前進」也就是「對每欄做」，這個方向感要建立起來。

## S14 · VS-CODE — apply vs 向量化
- 🖼️ 上下兩個 code panel + 中間延遲標註（用 bullets 強調）。
- 📣 上 panel BEFORE：`df['tax'] = df['price'].apply(lambda x: x * 1.05)`（10 秒）
  下 panel AFTER：`df['tax'] = df['price'] * 1.05`（0.05 秒，200×）
  bullets：能向量化就不要 apply、apply 是 fallback 不是 first choice、Ch7 NumPy 的向量化哲學在這裡發揮、一行差別效能差兩個量級。
- 🎙️ apply 是退路，不是首選。先問「能不能用算術 / 比較 / Series 方法直接做？」做不到才 apply。

## S15 · CODE — 特徵工程實戰
- 🖼️ 滿版 code panel。
- 📣 code：
  - 日期拆解：`df['year'] = df['date'].dt.year` / `dt.month` / `dt.dayofweek`
  - 分組標記：`df['grade'] = df['score'].apply(lambda x: 'A' if x>=90 else 'B' if x>=60 else 'C')`
  - 字串清洗：`df['name'] = df['name'].str.strip().str.lower()`
  bullets：`.dt` / `.str` 是兩個高頻 accessor、能用 accessor 就不要 apply、特徵工程的本質是「把隱藏訊號顯現出來」。
- 🎙️ 90% 的特徵工程是這三招的排列組合 — 拆時間、分組、清字串。

## S16 · IMAGE + CODE — Split-Apply-Combine
- 🖼️ 左：Split-Apply-Combine 流程圖 placeholder；右：對應 code。
- 📣 code：`df.groupby('city')['revenue'].mean()` — 一句話完成三步驟。
  bullets：split = 切組、apply = 對每組做運算、combine = 合併回結果、心智模型清晰後語法只是裝飾。
- 🎙️ 1956 年 Wilkinson 提的概念，今天還是 pandas 的核心。背概念，不背 API。

## S17 · CODE — groupby + agg 完整用法
- 🖼️ 滿版 code panel。
- 📣 code：
  - 單欄單聚合：`df.groupby('city')['revenue'].sum()`
  - 多鍵分組：`df.groupby(['city', 'product']).sum()`
  - 多欄不同聚合：`df.groupby('city').agg({'revenue': 'sum', 'qty': 'mean'})`
  - 自訂：`df.groupby('city').agg(lambda g: g.max() - g.min())`
  bullets：`agg` 是進階入口、字典指定欄位 → 函式、lambda 接受整個 group。
- 🎙️ 字典版的 agg 是業務報表最常見寫法，務必熟。

## S18 · CODE — transform vs agg + pivot_table
- 🖼️ 滿版 code panel + bullets。
- 📣 code：
  - `agg`：縮減 — 每組變一個值
  - `transform`：保持原 shape — 每列補上組內統計
  - 應用：`df['city_avg'] = df.groupby('city')['revenue'].transform('mean')` → 每筆訂單都帶上城市平均
  - `pivot_table(index='city', columns='month', values='revenue', aggfunc='sum')` — 交叉表速成
  bullets：transform 用於「需要 group 統計但要保留原行」、pivot_table 是 groupby 的 wide-format 版、Excel 樞紐分析的 pandas 版。
- 🎙️ transform 是初學者最常忽略的方法，但業務上「給每筆訂單標上城市平均」這需求每天都遇到。

## S19 · MATRIX 2×2 — 三種合併
- 🖼️ 2×2 方陣（其中一格放總結）。
- 📣 標題「concat / merge / join：三種合併、各自場景」
  cells：
  - `concat`（堆疊，highlight）— 沿軸接起來，不依賴鍵；axis=0 加列、axis=1 加欄
  - `merge`（鍵值合併，highlight）— 類似 SQL JOIN；指定 `on` 或 `left_on/right_on`
  - `join`（簡化版 merge）— 預設用 Index 合併，常用於兩個 DataFrame 都已 set_index
  - 常見陷阱 — 合併後出現 `_x` `_y`：用 `suffixes=('_left','_right')` 或先 rename
- 🎙️ 工業上 90% 場景用 merge，concat 是 ETL 拼批次資料、join 是 Index 已對齊時的捷徑。

## S20 · IMAGE + CODE — merge 四種 how
- 🖼️ 左：四種 how Venn 圖 placeholder；右：對應 code。
- 📣 code：四個 merge 範例 inner / left / right / outer。
  bullets：inner 是預設 — 取交集、left 保留左表全部、outer 全保留 — 缺的 NaN、indicator=True 加 `_merge` 欄位除錯神器。
- 🎙️ 第一個合併寫完一定要 `len()` 比對前後 — 多了 = 有重複鍵、少了 = 該 left 沒 left。

## S21 · CODE — to_datetime + DatetimeIndex
- 🖼️ 滿版 code panel。
- 📣 code：
  - `df['date'] = pd.to_datetime(df['date'])` — 字串轉時間
  - `df.set_index('date', inplace=True)` — 設成 Index
  - 切片：`df['2024-01']` / `df['2024-01':'2024-03']` / `df.loc['2024-Q1']`
  bullets：時間 Index 解鎖 partial string indexing、`format=` 加速大檔轉換、`.dt` accessor 拆出年月日。
- 🎙️ 字串轉時間這一步常被跳過，結果整個分析卡死。先轉時間，再做事。

## S22 · CODE — resample + rolling
- 🖼️ 滿版 code panel。
- 📣 code：
  - `df.resample('D').sum()` — 日聚合
  - `df.resample('W').mean()` / `'M'` / `'Q'`
  - `df['ma7'] = df['revenue'].rolling(window=7).mean()` — 7 日移動平均
  bullets：resample 是 groupby 的時間版、rolling 是窗口統計、兩者組合就是時間序列分析的基本盤。
- 🎙️ resample 一句話完成「每日營收 → 每週營收」這種繁瑣聚合。它是 groupby 的時間特化版。

## S23 · PYRAMID — 收束
- 🖼️ 兩欄階層 + 底部 thesis。
- 📣 標題「Ch08 收束：七步流水線 — 讀→看→篩→清→轉→聚→併」
  block 1：七步流水線
  - 讀（read_csv/parquet）→ 看（info/describe/dtypes）
  - 篩（loc/iloc/query）→ 清（dropna/fillna/interpolate）
  - 轉（apply/lambda/dt/str）→ 聚（groupby/agg/transform/pivot_table）
  - 併（concat/merge/join）
  block 2：今天該帶走的紀律
  - Index 是名字、不是欄位
  - 能向量化就別 apply
  - dropna 不是預設答案
  - 合併後用 `len()` 比對
  thesis：「Ch09 我們進入視覺化 — 把這條流水線的產物畫出來給人看。」
- 🎙️ 七步流水線記下來，你的 pandas 程式碼就會自然有結構。下一章把成果視覺化。
