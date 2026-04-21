# Ch09 — 機器學習演算法與深度學習｜Slides Design

> 22 張內容投影片（封面 + 22 + 版權）｜考試導向七原型為主
> 對齊 `01_outline.md` 的 6 個 Learning Objectives x 5 個 Common Pitfalls
> 配色：主色 `#0D1B2A` + 強調 `#00D4AA` + 警告橘 `#FF6B35`
> 受眾：iPAS 中級科目3 考生，類比走「工具箱 / 地圖 / 選型」路線

---

## S1 · MOTIVATION — 科目3 演算法題佔比最高

- 畫面：白底 / 大字痛點句 / 右側資料卡「歷屆分析：演算法+架構辨識佔~50%」
- 畫面上的字：
  - 標題：「科目3 有一半的題目跟演算法有關——但它不考你推導公式，考的是你知不知道什麼場景該用什麼工具。」
  - 卡片：L231 數學基礎 + L232 演算法與深度學習 · ~50 題中約 25 題
- 講者這時說：「很多人看到『機器學習演算法』就開始背公式。先停下來。我們分析了歷屆考題和樣題，科目3 考的不是推導，是判斷力。它會給你一個場景問你該用什麼演算法，給你一個架構名字問你它的特色。今天教你怎麼用最少的記憶量，覆蓋最多的考點。」

---

## S2 · ASK — 10 種演算法怎麼選

- 畫面：白底中央問句 + 演算法名字散落
- 畫面上的字：「Linear Regression / Logistic Regression / Decision Tree / Random Forest / SVM / KNN / K-means / DBSCAN / PCA / CNN / RNN / Transformer... 這麼多，考試到底考什麼？」
- 講者這時說：「看到這一堆名字頭就暈了對吧？好消息是考試不會要你全部精通。它考的是三件事：第一，每個演算法的一句話定位。第二，什麼場景該用什麼。第三，深度學習架構的設計哲學。今天我們就按這三條線走。」

---

## S3 · SILENT — 立論

- 畫面：全深藍底 / 白色 HERO 大字
- 畫面上的字：「演算法不用全背，但必須知道每個的定位。／考試考的是選型判斷力，不是公式記憶力。」
- 講者這時說：「這句話記住。你不需要能推導 SVM 的對偶問題，但你必須知道 SVM 什麼時候比 Random Forest 好。你不需要畫出 ResNet 的完整架構，但你必須知道 ResNet 解決了什麼問題。」

---

## S4 · CONCEPT-CARD — ML 演算法全景地圖

- 畫面：樹狀圖/心智圖（真圖佔位）
- 畫面上的字：
  - 監督式學習
    - 迴歸：Linear Regression
    - 分類：Logistic Regression / Decision Tree / Random Forest / SVM / KNN
  - 非監督式學習
    - 分群：K-means / DBSCAN
    - 降維：PCA
  - 深度學習：CNN / RNN / Transformer
- 講者這時說：「這張地圖是今天的導航。所有演算法就分成這幾個區塊。先記住大分類，後面我們一個一個填細節。考試的時候，你拿到一個場景，第一步就是在這張地圖上定位：它是監督還是非監督？迴歸還是分類？然後再從那個區塊裡挑。」

---

## S5 · CONCEPT-CARD — Linear Regression + R²

- 畫面：左邊散點+迴歸線 / 右邊 R² 公式與解讀
- 畫面上的字：
  - Linear Regression：假設 y = wx + b 的線性關係
  - R²（判定係數）= 1 - (SS_res / SS_tot)
  - R² = 1 → 完美預測 · R² = 0 → 跟猜平均值一樣 · R² < 0 → 比猜平均值還爛
  - 考點：R² 代表模型解釋了多少百分比的變異
- 講者這時說：「Linear Regression 是最簡單的監督式演算法，假設輸入和輸出之間是線性關係。R² 是它的成績單——告訴你模型解釋了多少百分比的資料變異。樣題 Q4 直接考 R² 的解讀，你只要記住：R² 越接近 1 越好，等於 0 代表你的模型跟直接猜平均值一樣沒用。」

---

## S6 · CONCEPT-CARD — Logistic Regression + Decision Tree + Random Forest

- 畫面：三欄比較表
- 畫面上的字：
  - Logistic Regression：Sigmoid 函數輸出 0-1 機率 · 線性決策邊界 · 適合特徵跟結果近似線性的場景
  - Decision Tree：用規則做 if-else 分裂 · 高解釋性 · 容易 overfit
  - Random Forest：多棵 Decision Tree 投票 · Bagging 降低 variance · 穩定的 baseline 首選
  - 選型口訣：資料量小/要解釋 → LR；需要規則可視化 → DT；要穩定 → RF
- 講者這時說：「這三個是分類問題的常客。Logistic Regression 雖然名字有 Regression，但它是分類演算法——用 Sigmoid 函數把線性結果壓縮到 0-1 之間。Decision Tree 的優點是你可以把它畫出來給老闆看，缺點是很容易 overfit。Random Forest 就是用很多棵 Tree 投票，犧牲一點解釋性換來穩定性。」

---

## S7 · CONCEPT-CARD — SVM 與 KNN

- 畫面：左邊 SVM 最大間隔示意 / 右邊 KNN 鄰居投票示意（真圖佔位）
- 畫面上的字：
  - SVM：找最大間隔的超平面 · kernel trick 可處理非線性 · 高維資料有效 · 大資料量慢
  - KNN：用最近 K 個鄰居投票 · 不需要訓練（懶學習）· 預測慢 · 維度詛咒嚴重
  - 考試重點：SVM 的 kernel trick / KNN 的 K 值影響 / 兩者對特徵縮放敏感
- 講者這時說：「SVM 和 KNN 是兩種完全不同的思路。SVM 找一條邊界，讓兩邊的資料離邊界越遠越好——這叫最大間隔。如果資料不是線性可分的，就用 kernel trick 把資料映射到高維空間。KNN 更簡單：你要分類一個新點，就看離它最近的 K 個鄰居，多數決。注意兩者都對特徵縮放敏感，考試會考。」

---

## S8 · CHECKPOINT — 演算法選型快問快答

- 畫面：白底五題 + 答案摺疊
- 畫面上的字：
  - Q1：電商客戶分群 → K-means 或 DBSCAN（非監督）
  - Q2：房價預測 → Linear Regression（監督-迴歸）
  - Q3：垃圾郵件分類 → Logistic Regression 或 Random Forest（監督-分類）
  - Q4：人臉辨識 → CNN（深度學習-影像）
  - Q5：工廠設備異常偵測，沒有標註 → DBSCAN 或 Isolation Forest（非監督）
- 講者這時說：「30 秒自己做。關鍵是第一步先判斷監督還是非監督——有沒有 label。第二步判斷任務類型——迴歸還是分類。第三步才挑具體演算法。Q5 特別注意：沒有標註所以不能用監督式。」

---

## S9 · CONCEPT-CARD — K-means vs DBSCAN

- 畫面：左右對比 + 群集形狀示意圖（真圖佔位）
- 畫面上的字：
  - K-means：需預先指定 K · 假設球狀群集 · 對 outlier 敏感 · 計算快
  - DBSCAN：不需指定 K · 能找任意形狀群集 · 自動標記噪音點 · 需設定 eps 和 min_samples
  - 選型判斷：知道群數 + 球狀 → K-means；不知道群數 + 形狀不規則 → DBSCAN
- 講者這時說：「這兩個的區分是高頻考點。K-means 的致命假設是球狀群集——如果你的資料是月牙形或環形，K-means 就會切錯。DBSCAN 靠密度找群集，什麼形狀都能處理，而且能自動把離群點標記為噪音。代價是你要調 eps（鄰域半徑）和 min_samples。」

---

## S10 · CONCEPT-CARD — PCA 降維

- 畫面：PCA 投影示意 + 累積變異解釋圖（真圖佔位）
- 畫面上的字：
  - PCA 原理：找到資料變異量最大的方向（第一主成分），然後找正交的第二大方向...
  - 保留 95% 累積變異通常就夠
  - 考試必記：PCA 是線性降維 · 需要先標準化 · 主成分彼此正交 · 不適合非線性結構
  - 用途：特徵太多時降維 / 資料視覺化（降到 2D/3D）
- 講者這時說：「PCA 的直覺：你有 100 個特徵但很多是冗餘的。PCA 找出最重要的幾個方向，把 100 維壓到例如 10 維，同時保留 95% 的資訊。考試重點：PCA 是線性降維——如果資料結構是非線性的，PCA 效果不好。另外 PCA 前一定要做標準化，因為它對量綱敏感。」

---

## S11 · PITFALL — MapReduce 不是 ML 但會考

- 畫面：左紅錯 / 右綠對 / 底部流程圖
- 畫面上的字：
  - 錯：跳過 MapReduce 覺得不是 ML 範圍 · 結果樣題 Q1 直接考
  - 對：理解 Map（拆解+處理）→ Shuffle（分組）→ Reduce（合併結果）的流程
  - 範例：計算全校平均分 → Map：每班算總分和人數 → Reduce：合併所有班的總分除以總人數
  - Why：MapReduce 屬於 L231「演算法效率與可擴展性」範疇
- 講者這時說：「很多考生看到 MapReduce 就跳過，覺得這不是 ML。但它屬於 L231 的評鑑範圍，而且樣題 Q1 就考了。MapReduce 的邏輯很簡單：Map 把大問題拆成小問題各自處理，Reduce 把小結果合併成最終結果。用一個簡單例子記住就好：計算全校平均分——Map 讓每個班算自己的總分和人數，Reduce 把所有班的結果加起來除以總人數。」

---

## S12 · CHECKPOINT — 演算法特性配對

- 畫面：左欄特性 / 右欄演算法 / 配對連線
- 畫面上的字：
  - 「不需指定群數」→ DBSCAN
  - 「需要 kernel trick 處理非線性」→ SVM
  - 「輸出 0-1 之間的機率值」→ Logistic Regression
  - 「對特徵縮放不敏感」→ Decision Tree / Random Forest
  - 「線性降維、需要標準化」→ PCA
  - 「懶學習、不建模型」→ KNN
- 講者這時說：「配對題是考試高頻題型。這六個配對你要能秒答。重點是 tree-based 的演算法不需要特徵縮放——因為它是用規則分裂，不看距離。SVM 和 KNN 都對縮放敏感——因為它們看距離。」

---

## S13 · CONCEPT-CARD — CNN 經典架構：VGG / Inception / ResNet

- 畫面：三欄架構比較 + 核心差異（真圖佔位）
- 畫面上的字：
  - VGG：3x3 小卷積核 · 簡單堆疊加深 · 16/19 層 · 概念直覺但參數多
  - Inception (GoogLeNet)：同一層用 1x1、3x3、5x5 卷積核並行 → 加寬不加深 · 多尺度特徵擷取
  - ResNet：殘差連接（skip connection）→ 解決深層網路梯度消失 · 可以訓練 100+ 層
  - 考試口訣：VGG 加深 / Inception 加寬 / ResNet 跳接
- 講者這時說：「樣題 Q2 直接考 Inception 的設計哲學。答案是『加寬不加深』——Inception 在同一層放了不同大小的卷積核並行處理，而不是像 VGG 一樣一直往深處堆。ResNet 的突破是殘差連接——讓資訊可以跳過幾層直接傳遞，解決了深層網路訓練困難的問題。這三個的一句話定位背下來就好。」

---

## S14 · CONCEPT-CARD — R-CNN / RNN / Transformer

- 畫面：三欄 + 任務對應
- 畫面上的字：
  - R-CNN 系列：影像物件偵測 · Region Proposal + CNN 分類 · 進化：R-CNN → Fast R-CNN → Faster R-CNN
  - RNN / LSTM：序列資料處理（文字/時間序列）· RNN 有梯度消失問題 → LSTM 用 gate 機制解決
  - Transformer：Self-Attention 機制 · 可平行處理（比 RNN 快）· 已成為 NLP + CV 的主流架構
  - 任務配對：影像分類 → CNN / 物件偵測 → R-CNN / 序列 → RNN|Transformer / NLP → Transformer
- 講者這時說：「R-CNN 是用在物件偵測——不只要分類圖片裡有什麼，還要框出在哪裡。RNN 是處理序列資料的，但它有梯度消失問題——長序列記不住前面的資訊，所以有了 LSTM 用 gate 機制來選擇性記憶。Transformer 用 attention 機制取代了 RNN 的循環結構，可以平行處理所以速度快很多。現在 GPT、BERT 都是 Transformer 架構。」

---

## S15 · CONCEPT-CARD — 激活函數四大天王

- 畫面：四格函數圖形 + 使用場景（真圖佔位）
- 畫面上的字：
  - ReLU：f(x) = max(0, x) · 隱藏層首選 · 計算快 · 解決梯度消失 · 缺點：Dead ReLU
  - Sigmoid：f(x) = 1/(1+e^-x) · 輸出 0-1 · 二元分類輸出層 · 缺點：梯度消失
  - Softmax：輸出多個機率加總為 1 · 多元分類輸出層
  - Tanh：f(x) = (e^x - e^-x)/(e^x + e^-x) · 輸出 -1 到 1 · 中心化版 Sigmoid
  - 考試必記：隱藏層 → ReLU / 二分類輸出 → Sigmoid / 多分類輸出 → Softmax
- 講者這時說：「樣題 Q6 考 Sigmoid 和 Softmax 的使用場景。規則很簡單：二元分類最後一層用 Sigmoid，因為它輸出一個 0-1 的機率。多元分類最後一層用 Softmax，因為它輸出每個類別的機率，加總等於 1。隱藏層統一用 ReLU——因為計算快、不容易梯度消失。這三條規則就夠了。」

---

## S16 · CHECKPOINT — 深度學習架構與激活函數配對

- 畫面：白底問答
- 畫面上的字：
  - Q1：CNN 影像分類（10 類）最後一層用什麼激活函數？→ Softmax
  - Q2：二元情感分析（正面/負面）最後一層用什麼？→ Sigmoid
  - Q3：為什麼隱藏層不用 Sigmoid？→ 梯度消失問題，深層網路訓練困難
  - Q4：哪個 CNN 架構的核心設計是「加寬不加深」？→ Inception
  - Q5：Transformer 為什麼能取代 RNN？→ Self-Attention 可平行處理，不需循環
- 講者這時說：「五題快速確認。Q3 特別重要——Sigmoid 在深層網路的隱藏層會讓梯度越乘越小，到最後前面幾層幾乎學不到東西，這就是梯度消失。ReLU 的好處是正數部分梯度恆為 1，不會衰減。」

---

## S17 · CONCEPT-CARD — 前向傳播：矩陣乘法

- 畫面：矩陣運算圖 + 手算範例
- 畫面上的字：
  - 前向傳播：Z = X · W + b → A = activation(Z)
  - 維度規則：(batch, input) × (input, output) = (batch, output)
  - 手算範例：
    ```
    X = [[1, 2, 3]]       # (1, 3)
    W = [[0.1],           # (3, 1)
         [0.2],
         [0.3]]
    b = [0.1]
    Z = 1×0.1 + 2×0.2 + 3×0.3 + 0.1 = 1.5
    A = ReLU(1.5) = 1.5
    ```
  - 考點：維度對齊 + 加偏差 + 過激活函數
- 講者這時說：「樣題 Q8 就是這種題型。前向傳播的流程就三步：輸入乘以權重、加上偏差、通過激活函數。矩陣乘法的關鍵是維度要對齊——前一層的輸出維度必須等於後一層的輸入維度。考試會給你小矩陣讓你算，用這個模板走一遍就行。」

---

## S18 · CONCEPT-CARD — 優化器：SGD / Adam / Adagrad

- 畫面：三欄比較表
- 畫面上的字：
  - SGD（隨機梯度下降）：基本款 · 學習率固定 · 容易卡在 local minimum · 需要手動調 lr
  - Adagrad：自動調整學習率 · 稀疏特徵友善 · 但學習率會持續衰減 → 後期幾乎停止學習
  - Adam：結合 Momentum + 自適應學習率 · 收斂快 · 最常用的預設選擇
  - 考試口訣：SGD 手動調 / Adagrad 會衰減 / Adam 最常用
  - 樣題 Q14 考點：Adagrad 的自適應學習率特性
- 講者這時說：「樣題 Q14 考的是 Adagrad。它的特色是會根據過去的梯度自動調整每個參數的學習率——更新多的參數學習率會變小，更新少的參數學習率相對大。問題是學習率只會越來越小，最後會衰減到幾乎不更新。Adam 解決了這個問題，結合了動量和自適應學習率，是目前最常用的優化器。考試只要記住各自的一句話特色。」

---

## S19 · PRACTICE-PROMPT — Python 程式題模擬

- 畫面：白底程式碼 + 選項
- 畫面上的字：
  ```python
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import accuracy_score

  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42)
  model = RandomForestClassifier(n_estimators=100)
  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  print(accuracy_score(y_test, y_pred))
  ```
  - Q1：這段程式碼使用什麼演算法？→ Random Forest
  - Q2：`test_size=0.2` 代表什麼？→ 20% 的資料作為測試集
  - Q3：`n_estimators=100` 代表什麼？→ 使用 100 棵決策樹
  - Q4：如果改成迴歸任務，import 要改成什麼？→ RandomForestRegressor
- 講者這時說：「科目3 約 25% 是 Python 程式題。不要怕——它不考你寫程式，考的是你能不能讀懂。這段程式碼的流程就是：切資料 → 建模 → 訓練 → 預測 → 評估。把這個 pattern 記住，換成什麼演算法都是同一個流程。」

---

## S20 · CONCEPT-CARD — Overfitting 辨識與處理（跨章考點）

- 畫面：診斷表 + 處理方法
- 畫面上的字：
  - 辨識：訓練集表現好 + 測試集表現差 = Overfitting
  - 處理方法：
    - 更多訓練資料
    - Regularization（L1/L2/Dropout）
    - Early Stopping
    - 簡化模型（減少層數/減少特徵）
    - Cross-Validation
  - 樣題 Q3：直接考 Overfitting 的定義與辨識
  - 注意：此考點同時出現在 Ch09 和 Ch10
- 講者這時說：「Overfitting 是跨章考點——Ch09 和 Ch10 都會考到。樣題 Q3 直接考。辨識方法就一句話：訓練集分數很高但測試集分數很低。處理方法背這五個就夠了。特別注意 Dropout 是深度學習特有的 regularization——隨機關閉一部分神經元，強迫網路不要依賴任何單一路徑。」

---

## S21 · PYRAMID — 演算法選型三層思維

- 畫面：pyramid_stack 三層
- 畫面上的字：
  - 頂層：效能需求決定調參方向（速度/精度/可解釋性）
  - 中層：資料特性決定具體演算法（維度/量級/分布形狀）
  - 底層：問題類型決定演算法大類（監督/非監督 × 迴歸/分類/分群）
  - 底部：從下往上選，不要反過來
- 講者這時說：「選演算法的思路從下往上走。最底層：先問這是什麼類型的問題——有沒有 label、要預測什麼。中間層：看你的資料長什麼樣——多少維度、多大量級、群集是什麼形狀。最頂層：看效能需求——要速度快還是精度高、需不需要可解釋。不要反過來——不要先決定要用某個演算法再去套問題。」

---

## S22 · MOTIVATION — 銜接 Ch10

- 畫面：問句 + 下一章資料卡
- 畫面上的字：「模型做出來只是開始——調好、評好、管好才是考試重點。」 · 卡片：Ch10 · 建模調參評估與 ML 治理 · L233+L234
- 講者這時說：「今天你建好了演算法的工具箱——知道什麼場景用什麼工具。但選對工具只是第一步。下一章 Ch10 教你怎麼調參讓模型更好、怎麼用正確的指標評估、怎麼處理 GDPR 和演算法偏見。如果說 Ch09 教你選刀，Ch10 教你磨刀和用刀。我們下次見。」
