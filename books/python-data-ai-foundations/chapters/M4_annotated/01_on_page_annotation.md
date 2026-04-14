# 01 逐頁註解（On-Page Annotation）— M4 EDA、視覺化與統計直覺

> **文件定位**：內部技術 reviewer 對課程逐張投影片的批註稿。針對每個知識點標注三層視角：🎯 **宏觀**（它在整個資料科學 BoK 裡的位置）、🔬 **細部**（講師要說清楚但最容易含糊的技術細節）、⚠️ **reviewer 批註**（現有教材沒講、但業界真的會踩雷的坑）。閱讀對象：授課講師、課程審稿人、資深 mentor。
> **語氣**：內部 review，直話直說，不客套。
> **來源**：`M4_EDA視覺化與統計直覺.md`

---

## Slide 1：圖表不是裝飾，是思考的外掛

### 🎯 宏觀定位
這張是整個 M4 的哲學基調，呼應 Tukey 1977 所確立的 EDA 典範：分析的第一階段是 **hypothesis generation**（假設生成），不是 hypothesis testing（假設驗證）。投影片把圖表重新定位成「認知工具」而非「溝通產物」，這是對的，但現場講解常常滑掉這個關鍵區分。

### 🔬 細部技術點
- **Anscombe's Quartet（1973）**：四組 (x, y) 的均值、變異數、相關係數、迴歸線斜率都一樣，但畫出來一組是線性、一組是曲線、一組有單一離群點、一組是垂直堆疊 + 一個拉動點。講師要真的把四張散佈圖同時貼出來，不能只用嘴巴講。
- **Datasaurus Dozen（Matejka & Fitzmaurice, 2017）**：Anscombe 的進化版，13 組資料集統計量小數點後兩位都一樣，其中一張是恐龍形狀。這是 2020 年後的教材標配，現在還只提 Anscombe 稍嫌過時。
- **EDA 圖 vs 報告圖**：這兩者的設計準則完全不同。EDA 圖要快、要多、要醜沒關係；報告圖要一張頂十張、要能離開作者獨立存活。

### ⚠️ Reviewer 批註
- 現行講稿只寫「Anscombe」一句話就帶過，**強烈建議把 Datasaurus 補進視覺建議區**，學員看到恐龍圖印象深度差一個數量級。
- 「圖表的目的是問問題，不是給答案」這句很漂亮，但跟 Slide 5 的「觀察 → 洞察 → 建議」其實有張力——EDA 階段是問問題，報告階段是給答案。**建議在這裡明講這是 EDA 圖，避免學員困惑**。
- 缺一個反例：「為什麼 Excel 預設 3D pie chart 是視覺化災難」——講這個會讓學員有痛點連結。

---

## Slide 2：四種圖表任務類型

### 🎯 宏觀定位
這個四分類（分佈 / 比較 / 關聯 / 時序）本質上是 Cleveland & McGill (1984) 「圖形感知任務階層」的業界簡化版。學術上還有「組成（composition）」、「空間（spatial）」等類別，對入門夠用但要知道是刻意簡化。

### 🔬 細部技術點
- **為何箱形圖（boxplot）比長條圖（bar chart）誠實**：bar chart 只畫均值（或總和），把整個分佈壓縮成一個數字；boxplot 至少揭露中位數、IQR、whisker、離群點五個資訊。一句話：**bar chart 是撒謊的均值，boxplot 是誠實的分佈**。Weissgerber et al. (2015) 的 "Beyond Bar and Line Graphs" 是必讀。
- **Matplotlib vs Seaborn vs Plotly**：
  - *Matplotlib*：低階 API，可控性最高，畫 publication-ready figure 的底盤。缺點：預設樣式醜、API 囉嗦。
  - *Seaborn*：建構在 matplotlib 之上，統計圖（violin、pairplot、regplot）幾乎一行搞定，預設美學好。適合 EDA 主力。
  - *Plotly*：互動式，hover / zoom / 下拉篩選，適合 dashboard 或要給業務方自己探索。缺點：離線部署稍重，PDF 輸出需要額外設定。
- **Pie chart 的禁用場景**：超過 3 個類別就幾乎不該用，因為人眼對角度的判讀精度遠低於長度。

### ⚠️ Reviewer 批註
- 講稿把三個套件的「選擇時機」帶過太快。**建議補一張決策樹**：要不要互動 → 要不要出 publication → 是不是統計圖 → 三套件選一個。
- 四分類缺「組成圖」（stacked bar、treemap、sankey），雖然入門可忽略，但學員碰到「市佔率變化」這類題目會卡住。至少要在講師備註提一句。

---

## Slide 3：什麼是好的資料問題？

### 🎯 宏觀定位
這張其實是在教 **問題建構**（problem framing），這是 ASA Data Science BoK 第一大領域 "Data Acumen" 的核心。內容方向正確，但深度可以再推一層——好問題不只是「可觀察、可比較、可驗證」，還要有 **決策連結**（actionability）。

### 🔬 細部技術點
- 三要素可以對應到科學方法：**可觀察 = 操作型定義**、**可比較 = 對照組**、**可驗證 = 可證偽性**（Popper）。
- 「問題從業務痛點來」這個講法沒錯，但實務上還有另外兩個來源：**異常警示**（monitoring alert）與 **目標對齊**（OKR / KPI gap）。這三種來源對應不同的 EDA 策略。

### ⚠️ Reviewer 批註
- 建議補一個 **「壞問題 → 好問題」重寫練習**，讓學員自己改寫，而不只是看對比表。
- 「可驗證」這個詞有歧義——是指「資料能回答」還是「實驗能驗證」？**建議拆成 answerable（資料可答）與 actionable（答案可用）兩個維度**。

---

## Slide 4：EDA 標準路徑

### 🎯 宏觀定位
「看全貌 → 抓異常 → 找關係 → 形成假設」這個四步法是 Tukey EDA + Wickham's `dplyr` 工作流的折衷版。結構清楚，但 **缺了「看資料品質」這個在業界佔 EDA 七成時間的步驟**。

### 🔬 細部技術點
- **看全貌**：`df.info()`, `df.describe()`, `df.isna().sum()` 只是起步。更深的是：dtype 是否合理（日期被存成 object？類別被存成 int？）、index 是否唯一、類別欄位的 cardinality（unique count）分佈。
- **抓異常**：要區分三種異常 —— **資料品質異常**（負數的年齡）、**統計離群**（超過 Q3+1.5×IQR）、**業務意義異常**（VIP 客戶的極端行為）。現行講稿把這三者混為一談。
- **找關係**：相關係數（Pearson）只抓線性，Spearman 抓單調，互信息（mutual information）抓任意關係。入門至少要提 Pearson 的局限。
- **形成假設**：假設要滿足 SMART-H 原則（Specific, Measurable, Achievable, Relevant, Time-bound, + Hypothesizable 可檢定）。

### ⚠️ Reviewer 批註
- **強烈建議把四步擴為「七步法」**：0. 資料品質審視 → 1. 看全貌 → 2. 單變量分析 → 3. 雙變量分析 → 4. 多變量分析 → 5. 抓異常 → 6. 形成假設。現有四步把單/雙/多變量塞進「看全貌 + 找關係」太粗糙。
- 迭代箭頭畫得好，但要強調 **「回頭的觸發條件」**——什麼時候該回頭？（發現新欄位相依、發現資料品質問題、發現假設不成立）。

---

## Slide 5：如何用一頁圖表講業務故事

### 🎯 宏觀定位
這張從 EDA 橋接到溝通，引入 McKinsey 的 SCR（Situation-Complication-Resolution）思維在顧問界的本地化版本「觀察 → 洞察 → 建議」。方向對，但要避免讓學員以為這是唯一結構。

### 🔬 細部技術點
- **標題句（takeaway title）**：這是整頁紙最重要的一行，不是「銷售分析」而是「新客三日留存崩跌 40%，主因為 Onboarding Step 3 的跳出率」。一句話包含 What + So What。
- **圖表說謊術警示**：
  - **Truncated Y-axis**（截斷縱軸）：把 Y 軸從 70% 起跳而不是 0%，會讓 2% 的差異看起來像天差地別。業務簡報常見操弄手法。
  - **Dual Y-axis**（雙縱軸）：兩條線看起來相關，其實是刻意縮放出來的。Matplotlib 的 `twinx()` 會害死新人。
  - **Cherry-picked time range**：只取對自己論點有利的時間窗。

### ⚠️ Reviewer 批註
- **這張一定要加「圖表說謊術」的反面教材**，否則學員會被教成善於操弄視覺的人，而不是誠實的分析師。至少 truncated axis 與 dual axis 兩個一定要講。
- 「建議（Recommendation）」要區分 **觀察層建議**（再多收一份資料）vs **決策層建議**（下架某個 SKU）。學員最常給的是前者，以為自己給了後者。

---

## Slide 6：【練習 A】三段洞察簡報

### 🎯 宏觀定位
實作練習設計合理，但評估標準只有三條、沒有 rubric 分級，實際批改時評審間一致性會很差。

### ⚠️ Reviewer 批註
- **色盲友善配色**應該是練習要求之一。全球約 8% 男性、0.5% 女性有色覺異常，紅綠對比是最危險的搭配。硬性要求用 **ColorBrewer** 或 **Okabe-Ito palette**，講師直接發一張色票貼在牆上。
- 建議加一條「資料倫理」檢查：不要用 `mean()` 對高偏態欄位（如購買金額）做聚合；不要用 pie chart；Y 軸不得截斷除非明確標示。
- 5000 筆 × 30 分鐘：學員做 EDA + 三張圖 + 三段文字，時間其實偏緊。**建議提供一個 starter notebook** 把 `df.info()` 那一步跑好，學員直接從抓異常開始。

---

## Slide 7：為什麼分析需要統計？

### 🎯 宏觀定位
這張是 Part B 的 anchor。切入點「描述 vs 判斷」很好，但 **error bar 用在比例指標（轉換率）其實有坑**——那是 binomial CI，不是常態 CI。

### 🔬 細部技術點
- 轉換率的信賴區間要用 **Wilson score interval** 或 **Clopper-Pearson**，不能直接套常態公式（normal approximation 在 p 接近 0 或 1 時會崩）。
- 「95% 信賴水準下無法排除隨機誤差」這句話是標準話術，但嚴格說應該是「我們不能拒絕 H0」，不等於「沒有差異」。**Absence of evidence ≠ evidence of absence**。

### ⚠️ Reviewer 批註
- 講師話術要精準：不要說「p=0.08 所以沒差異」，要說「p=0.08，在 α=0.05 下我們無法拒絕 H0」。這個語言潔癖是統計素養的分水嶺。

---

## Slide 8：母體、樣本、均值、變異數

### 🎯 宏觀定位
基礎概念，沒什麼可挑剔。但 **變異數 vs 標準差** 的使用時機講稿沒提，學員常搞不清為何有兩個指標。

### 🔬 細部技術點
- **變異數單位是平方**（元²、公分²），所以實務解讀都用 **標準差**（單位與原資料一致）。變異數的價值在數學運算（可加性）。
- **樣本變異數的分母是 n-1 而不是 n**（Bessel's correction），這是無偏估計。Pandas 的 `.var()` 預設 `ddof=1`，NumPy 的 `np.var()` 預設 `ddof=0`——這個**陷阱一定要講**，否則學員兩邊數字對不起來會瘋掉。

### ⚠️ Reviewer 批註
- 「平均薪資陷阱」的反例很好，但可以再加 **中位數 vs 均值 vs 幾何平均** 的使用時機對照表。
- 母體 / 樣本的記號（μ vs x̄、σ² vs s²）要在這張明確打出來，後面 slide 會反覆用到。

---

## Slide 9：分佈與抽樣直覺

### 🎯 宏觀定位
引入 **中央極限定理（CLT）** 是對的，但講稿的表述容易誤導。

### 🔬 細部技術點
- **CLT 的正確陳述**：樣本均值的抽樣分佈，在 n 夠大時趨近常態，**不論母體分佈為何**（只要有限變異數）。
- **CLT 的誤用**：
  1. 誤以為「資料越多，資料本身會變常態」——錯。資料分佈不會變，變的是**樣本均值的分佈**。
  2. 誤以為 n=30 就一定夠——錯。高偏態資料（收入、等待時間）可能需要 n > 200。
  3. 把 CLT 套在中位數、最大值上——錯。CLT 只適用於和/均值這類線性統計量。
- **長尾分佈（Pareto、log-normal）** 對 CLT 收斂速度很慢，而且變異數可能不存在（如 Cauchy 分佈），CLT 根本不適用。

### ⚠️ Reviewer 批註
- **CLT 這一頁是統計誤解最大宗之一，必須單獨處理**。建議把 Slide 9 切成 9a（分佈直覺）與 9b（CLT 正解與誤用）。
- 示範「從右偏母體反覆抽樣 → 樣本均值分佈變常態」的動畫或 matplotlib 動態，效果遠勝靜態圖。

---

## Slide 10：假設檢定在做什麼？

### 🎯 宏觀定位
法庭類比很經典，Ronald Fisher 本人就是這麼教的。但 **p-value 的定義在講稿裡仍有微妙錯誤**。

### 🔬 細部技術點
- **p-value 精確定義**：假設 H0 為真，觀察到**當前或更極端**統計量的機率。講稿寫「這麼大（或更大）差異的機率」方向對，但 reviewer 要確認講師現場口頭別滑成「H0 為真的機率」——這是經典誤解（那是貝氏後驗，不是 p-value）。
- **p-value 的五大誤用**（ASA 2016 Statement on p-values）：
  1. p-value 不是 H0 為真的機率
  2. p < 0.05 不代表結果重要
  3. p > 0.05 不代表沒有效應
  4. 科學結論不該只靠 p-value
  5. p-value 不代表 effect size
- **Effect size**：Cohen's d、相對風險、提升率。**統計顯著 + effect size 才是完整判斷**。

### ⚠️ Reviewer 批註
- **強烈建議加一張「統計顯著 vs 實務顯著」的 2×2 矩陣**：
  - 統計顯著 + 實務顯著 → 上線
  - 統計顯著 + 實務不顯著 → 別做（這是大樣本陷阱）
  - 統計不顯著 + 實務看起來顯著 → 加樣本或承認不確定
  - 都不顯著 → 放棄
- 建議引用 ASA 2016 聲明，提升課程的專業感。

---

## Slide 11：A/B Test 的統計本質

### 🎯 宏觀定位
內容基本完整，涵蓋了隨機化、sample size、power、統計 vs 業務顯著。**但漏掉了 A/B Test 業界最大兩個坑：peeking 與 multiple testing**。

### 🔬 細部技術點
- **Peeking problem**：每天偷看結果，看到 p<0.05 就停止實驗——這會把 false positive rate 從 5% 推高到 30% 以上。解法：pre-registration of sample size，或用 sequential testing（如 mSPRT、always-valid inference）。
- **Multiple testing**：同時測 10 個指標，至少有一個 p<0.05 的機率是 1-0.95^10 ≈ 40%。解法：Bonferroni、BH-FDR。
- **SRM（Sample Ratio Mismatch）**：分組比例應該是 50/50，如果實際是 49/51 且 p < 0.001，代表分流機制壞了，結果全部作廢。Kohavi 書裡強調這是 **launch 前必檢**。

### ⚠️ Reviewer 批註
- 至少把 peeking 和 SRM **口頭提一次**，否則學員到公司會立刻踩。
- 「統計顯著 vs 業務顯著」講稿已經帶到，但還可以提 **minimum detectable effect (MDE)** 這個術語——在實驗設計前就決定「我在乎多大的差異」，反推 sample size。

---

## Slide 12：【練習 B】業務問題翻譯機

### 🎯 宏觀定位
練習設計優秀，三題覆蓋了 A/B、雙樣本 t、時序比較三種情境。**但標準答案沒公開，批改會有分歧**。

### ⚠️ Reviewer 批註
- 第 2 題「週末 vs 平日訂單金額」：訂單金額通常是 **右偏 + 可能包含零**，雙樣本 t 檢定的常態假設不成立。應該引導學員考慮 **Mann-Whitney U** 或 **bootstrap**。現行教材沒提 t-test 的前提檢查，會教出一批「不管分佈就套 t-test」的分析師。
- 第 3 題「三個月留存」：留存是 survival analysis 的範疇，用信賴區間粗略比較 OK，但要提一句這在嚴謹情況下應該用 Kaplan-Meier。
- 建議加第 4 題挑戰題：「為什麼我們的推薦系統點擊率下降了？」——這是 **無法用 A/B Test 回答的問題**（沒有對照組，只有觀察資料），需要引入 causal inference 的提示，讓強的學員有東西挑戰。

---

## 全章統整 Reviewer 結論

**優點**：
1. 哲學層清晰——圖表是思考工具、統計是判斷工具，這兩句 anchor 做得好。
2. Part A / Part B 的對稱結構（各 6 張 slide）讓學員容易記憶。
3. 練習設計真實、有業務連結，不是玩具資料集。

**必修補丁（上課前務必補）**：
1. Slide 1 補 Datasaurus Dozen。
2. Slide 2 補三套件決策樹 + bar vs boxplot 誠實度對比。
3. Slide 4 四步擴為七步（補資料品質、拆單/雙/多變量）。
4. Slide 5 補圖表說謊術（truncated axis、dual axis、cherry pick）。
5. Slide 9 CLT 誤用的三個常見坑。
6. Slide 10 加 2×2 統計 vs 實務顯著矩陣，引用 ASA 2016 聲明。
7. Slide 11 至少口頭提 peeking 與 SRM。
8. 全章硬性要求色盲友善配色（Okabe-Ito / ColorBrewer）。

**選修強化**：
- Bayesian 視角的極簡介紹（至少讓學員知道 p-value 不是唯一世界觀）。
- causal inference 的 teaser（Slide 12 挑戰題）。
