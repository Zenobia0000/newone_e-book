# S4 · 時間序列與 EDA 實戰 — Slides Design

> 23 張內容 + 封面 + 版權頁，對應 01_outline.md 的 §1 LO / §4 Pitfalls / §5 Prompts。四拍節奏：概念→例子→問題→小結。

---

## S1 · SILENT — 開場金句
- 🖼️ 深綠滿版、白字 hero
- 📣 「數字不會說話，時間軸和 EDA 會。」
- 🎙️ 這堂課要把「時間」與「EDA」從散裝概念，變成能產報表的工作流。

## S2 · MOTIVATION — 老闆四問
- 🖼️ 左痛點故事 + 右四問卡
- 📣 「上週 vs 上月差多少？哪天賣最好？哪款在衰？下個月預估？」
- 🎙️ 每一個老闆會問的問題都帶著時間維度。不會時間，就永遠只能回「讓我查一下」。

## S3 · ASK — 入門提問
- 🖼️ 白底大字疑問
- 📣 「你拿到訂單 CSV 的第一件事是什麼？」
- 🎙️ 90% 的人會 `head()`，但正確答案是 `parse_dates` + `sort_index`。

## S4 · CONCEPT-CARD — 學習目標
- 🖼️ 左字右示意（四卡：.dt / resample / rolling / corr）
- 📣 「本節結束後你能：寫出月度經營報表」
- 🎙️ 五個可測量動詞，對應 LO1–LO5。

## S5 · CONCEPT-CARD — datetime64 與 .dt
- 🖼️ 左定義右示意（Timestamp 物件的結構圖）
- 📣 「datetime64[ns] 是 pandas 的時間原語；.dt 把它當成結構化欄位」
- 🎙️ 跟 Excel 的 `YEAR()` 公式類比，但不同的是：一行 code 一次拆四欄。

## S6 · MECHANISM-FLOW — 讀時序資料的 4 步驟
- 🖼️ 四方塊水平流：read_csv(parse_dates) → to_datetime → set_index → sort_index
- 📣 「忘一步，下游全錯」
- 🎙️ 這四步是「時序版 hello world」，每次拿到帶時間的 CSV 都要走一次。

## S7 · EXAMPLE-I/O — .dt 四連拆
- 🖼️ 單欄 code panel
- 📣 Input: 訂單日期欄 → Output: year / month / day / weekday 四欄
- 🎙️ Excel 要四個公式 + 下拉；pandas 一次四行，向量化秒殺。

## S8 · CONCEPT-CARD — resample = 時間版 groupby
- 🖼️ 左定義 + 右示意（每日 → 每月 bucket）
- 📣 「resample 只認 DatetimeIndex；否則 TypeError」
- 🎙️ 與 groupby 的關係像「專門處理時間鍵的特化 API」。

## S9 · MECHANISM-FLOW — D / W / ME 三種粒度
- 🖼️ 三方塊 + 每塊下日期範例
- 📣 「D=每日、W=每週、ME=每月末」
- 🎙️ 2.2+ 後 `'M'` 被 deprecation，改用 `'ME'`；等下 Pitfall 頁會秀警告。

## S10 · EXAMPLE-I/O — resample 月營收
- 🖼️ code panel：三行 resample
- 📣 Input: 日訂單 → Process: `.resample('ME')['amount'].sum()` → Output: 月序 Series
- 🎙️ 報表型需求就靠這一句話。

## S11 · PITFALL — 沒 sort_index 的慘案
- 🖼️ 左紅框錯誤、右綠框正確
- 📣 「resample 不會噴錯，只會默默給你錯數字」
- 🎙️ 紅色專用：錯誤版 vs 正確版並陳。真實專案因此 review 被打回最常見。

## S12 · CONCEPT-CARD — rolling
- 🖼️ 左定義右示意（sliding window 圖）
- 📣 「rolling(window) = 移動視窗；N 筆平均壓雜訊」
- 🎙️ 類比股票 MA5/MA20，但不同的是：rolling 輸出是 Series，可直接當新欄位。

## S13 · CHART — window 大小 vs 平滑度
- 🖼️ 三層圖表示意：原始 / rolling(7) / rolling(30)
- 📣 「window 小保留雜訊、window 大看趨勢」
- 🎙️ 前 N-1 列是 NaN 是常問點，這頁先鋪梗，下一頁範例揭示。

## S14 · EXAMPLE-I/O — rolling(7).mean()
- 🖼️ code panel + 折線示意
- 📣 「一句話把鋸齒日線變趨勢線」
- 🎙️ 對比 window=3 和 7；畫圖前 `.dropna()`，或加 `min_periods=1`（但要提醒失真）。

## S15 · CONCEPT-CARD — EDA 三板斧
- 🖼️ 2×2 matrix：describe / value_counts / corr / （+ 空白留第四位給下一節）
- 📣 「三行拆解任何新資料」
- 🎙️ 拿到資料先跑這三件套，還沒動手清洗前先「認識它」。

## S16 · EXAMPLE-I/O — 三板斧一次跑
- 🖼️ code panel 三行 + 輸出摘要
- 📣 Input: orders.csv → Output: 一句話結論（星期幾最旺、品類相關性）
- 🎙️ 相關係數解讀口訣：>0.7 強 / 0.3–0.7 中 / <0.3 弱，一定要說結論不能只丟數字。

## S17 · PITFALL — corr 解讀陷阱
- 🖼️ 左紅：只丟 0.65 / 右綠：0.65 + 口語化結論
- 📣 「corr 0.65 不是答案，『客單與品項數中度正相關』才是」
- 🎙️ 類別欄要 `crosstab`/`chi2`；這是進階課題，這裡先點到。

## S18 · PITFALL — 'M' vs 'ME' 及四個常見錯
- 🖼️ 2×2 matrix：四個錯誤 / 改法並陳
- 📣 「deprecation 警告要當回事」
- 🎙️ 逐條 mapping §4 五大陷阱。

## S19 · EXAMPLE-I/O — 月度經營報表 walkthrough
- 🖼️ 完整 code panel（輸入 orders → resample+pct_change → 六欄輸出）
- 📣 「這就是你交付給 S5 的 monthly_revenue.csv」
- 🎙️ 第一個月成長率 NaN 是 expected（沒有前一月）；要不要補 0 看下游用途。

## S20 · PRACTICE-PROMPT — 三題分層練習（10 分鐘）
- 🖼️ 三卡：送分 / 核心 / 挑戰
- 📣 「送分：算每月營收 / 核心：加上 7 日 rolling / 挑戰：月度報表 + 週一平均」
- 🎙️ 預期時間：3 / 5 / 10 分鐘；挑戰題直接對應 §5-Q1。

## S21 · CHECKPOINT — 選用決策
- 🖼️ 題目卡 + 四選項
- 📣 「下列哪個要 resample？哪個要 groupby？哪個要 rolling？」
- 🎙️ 答案留到口頭揭示；重點是訓練「看到問題能分類」。

## S22 · PYRAMID — 收束三層
- 🖼️ 三層金字塔：時間軸 → EDA 直覺 → 報表產出
- 📣 「What：四工具 / Why：商業問題都有時間 / Next：S5 畫給老闆看」
- 🎙️ T12 三件套：What / Why / Next。

## S23 · SILENT — 下一節預告
- 🖼️ 深綠滿版白字 hero
- 📣 「S5 預告：數字不會說話，圖會。」
- 🎙️ 銜接視覺化章節。
