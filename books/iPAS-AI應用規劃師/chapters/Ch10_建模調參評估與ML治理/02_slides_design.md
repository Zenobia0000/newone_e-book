# Ch10 — 建模調參、評估與 ML 治理｜Slides Design

> 22 張內容投影片（封面 + 22 + 版權）｜考試導向七原型為主
> 對齊 `01_outline.md` 的 6 個 Learning Objectives x 5 個 Common Pitfalls
> 配色：主色 `#0D1B2A` + 強調 `#00D4AA` + 警告橘 `#FF6B35`
> 受眾：iPAS 中級科目3 考生，類比走「儀表板 / 品管 / 合規」路線

---

## S1 · MOTIVATION — 模型做出來只是開始

- 畫面：白底 / 大字痛點句 / 右側資料卡「歷屆分析：調參+評估+治理佔~40-50%」
- 畫面上的字：
  - 標題：「科目3 的另一半考題不是考演算法，而是考你會不會調參、會不會評估、懂不懂治理。」
  - 卡片：L233 建模調參評估 + L234 隱私與偏見 · 約 20-25 題
- 講者這時說：「上一章教你選刀，這一章教你磨刀和用刀。很多考生把所有時間花在背演算法，結果特徵工程、評估指標、GDPR 的題目全丟分。這些題目不難，但你必須知道它們會考。」

---

## S2 · ASK — Accuracy 95% 真的可以上線嗎

- 畫面：白底中央問句 + 三個子問題
- 畫面上的字：「你的模型 Accuracy 95%——真的可以上線嗎？」
  - 如果資料 95% 是同一類？→ 可能全猜多數類
  - 如果 GDPR 不合規？→ 法律風險
  - 如果模型對特定族群有偏見？→ 倫理風險
- 講者這時說：「Accuracy 95% 聽起來很棒，但這三個問題任何一個沒過關，模型就不能上線。今天我們從特徵工程開始，一路走到評估指標、調參策略，最後講 GDPR 和演算法偏見。每一站都有考題。」

---

## S3 · SILENT — 立論

- 畫面：全深藍底 / 白色 HERO 大字
- 畫面上的字：「模型做出來只是開始。／調好、評好、管好才是考試重點。」
- 講者這時說：「這句話是本章的核心。Ch09 教你建模，Ch10 教你讓模型真正能用。考試考的不是你會不會 import sklearn，是你知不知道什麼時候該用什麼指標、什麼參數該怎麼調、什麼時候模型不能上線。」

---

## S4 · CONCEPT-CARD — 特徵工程三步驟

- 畫面：三欄流程 + 範例
- 畫面上的字：
  - 特徵轉換（Feature Transformation）：把原始資料變成模型能吃的格式
    - One-Hot Encoding（類別 → 0/1 向量）
    - 標準化/正規化（數值縮放）
    - Log 轉換（處理偏態分佈）
  - 特徵萃取（Feature Extraction）：從現有特徵創造新特徵
    - 多項式特徵、交互特徵
    - TF-IDF（文字 → 數值）
    - PCA（降維也是一種萃取）
  - 特徵選擇（Feature Selection）：挑有用的、丟沒用的
    - 相關係數篩選
    - Feature Importance
    - L1 Regularization（自動選擇）
- 講者這時說：「特徵工程是建模前最重要的工序。垃圾進垃圾出——再好的演算法也救不了爛特徵。三個步驟記住：轉換是格式化、萃取是創造新特徵、選擇是去蕪存菁。考試會考你分辨哪個操作屬於哪個步驟。」

---

## S5 · CONCEPT-CARD — 標準化(Z-score) vs 正規化(Min-Max)

- 畫面：左右對比 + 公式 + 適用場景
- 畫面上的字：
  - 左：標準化 Standardization（Z-score）
    - 公式：z = (x - mean) / std
    - 結果：均值 0、標準差 1
    - 適用：SVM、KNN、神經網路（對距離/梯度敏感的演算法）
    - 不受 outlier 影響太大
  - 右：正規化 Normalization（Min-Max）
    - 公式：x' = (x - min) / (max - min)
    - 結果：壓縮到 [0, 1]
    - 適用：需要固定範圍的場景（影像像素、Neural Network 輸入）
    - 對 outlier 敏感
  - 底部口訣：Z 標 M 正（Z-score = 標準化、Min-Max = 正規化）
- 講者這時說：「樣題 Q9 直接考標準化。最大的陷阱是中文翻譯——不同教科書的定義可能相反。考試用的定義是：Z-score 是標準化、Min-Max 是正規化。記口訣『Z 標 M 正』就不會搞混。」

---

## S6 · CONCEPT-CARD — 標註品質與訓練前配置

- 畫面：標註品質影響流程圖
- 畫面上的字：
  - 標註品質 = 模型天花板
  - 垃圾標註 → 垃圾模型（Garbage In, Garbage Out）
  - 考點一：標註者間信度（Inter-Annotator Agreement）→ Cohen's Kappa
  - 考點二：標註不一致 → 模型學到噪音
  - 訓練前配置：Loss Function 選擇 / 優化器選擇 / 學習率設定
  - 樣題 Q5：標註品質對模型的影響
- 講者這時說：「樣題 Q5 考標註品質。記住一個概念：模型的天花板不是演算法決定的，是標註品質決定的。如果你的訓練資料標註不一致——同一張圖有人標貓有人標狗——模型學到的就是噪音。標註品質的評估用 Cohen's Kappa 或 inter-annotator agreement。」

---

## S7 · PITFALL — 標準化和正規化搞混

- 畫面：左紅錯 / 右綠對 / 底部口訣
- 畫面上的字：
  - 錯：把 Min-Max 叫做標準化 · 把 Z-score 叫做正規化
  - 對：Z-score = 標準化（Standardization）· Min-Max = 正規化（Normalization）
  - Why：中文翻譯混亂，不同教科書定義不同，但 iPAS 考試用的是上述定義
  - 口訣：Z 標 M 正 · 記公式更保險
- 講者這時說：「這是送分也是送命的考點。翻譯混亂到我都見過教科書把兩個反著寫的。解決方案：不要記中文名稱，記公式。Z-score 公式 (x-mean)/std 看到 mean 和 std 就知道是標準化。Min-Max 公式 (x-min)/(max-min) 看到 min 和 max 就知道是正規化。」

---

## S8 · CHECKPOINT — 特徵工程分類

- 畫面：白底分類題
- 畫面上的字：
  - 以下操作屬於轉換、萃取、還是選擇？
  - One-Hot Encoding → 轉換（格式化類別特徵）
  - TF-IDF → 萃取（從文字創造數值特徵）
  - PCA 降維 → 萃取（從多個特徵萃取主成分）
  - 相關係數篩選 → 選擇（根據相關性挑特徵）
  - 多項式特徵 → 萃取（x → x, x², x³ 等）
  - L1 Regularization → 選擇（自動將不重要特徵權重歸零）
- 講者這時說：「快速確認。關鍵區分：轉換是『格式化現有特徵』，萃取是『創造新特徵』，選擇是『挑選/刪除特徵』。PCA 有點特殊——它既是降維也是萃取，因為主成分是新的特徵組合。」

---

## S9 · CONCEPT-CARD — 分類評估指標全家福

- 畫面：混淆矩陣 + 四大指標公式（真圖佔位）
- 畫面上的字：
  - 混淆矩陣（Confusion Matrix）：
    ```
                   預測正  預測負
    實際正          TP      FN
    實際負          FP      TN
    ```
  - Accuracy = (TP + TN) / (TP + TN + FP + FN) → 整體正確率
  - Precision = TP / (TP + FP) → 預測為正的有多少是對的
  - Recall = TP / (TP + FN) → 真正為正的你抓到多少
  - F1 = 2 × (Precision × Recall) / (Precision + Recall) → 調和平均
- 講者這時說：「混淆矩陣是一切指標的起點。TP FP FN TN 四個格子，所有指標都從這裡算出來。Precision 回答的是『你說是正的裡面有幾個真的是正的』，Recall 回答的是『真的是正的裡面你抓到幾個』。F1 是兩者的平衡——當你不確定該看哪個的時候就看 F1。」

---

## S10 · CONCEPT-CARD — AUC-ROC 與 R²

- 畫面：左邊 ROC 曲線 / 右邊 R² 示意（真圖佔位）
- 畫面上的字：
  - AUC-ROC：
    - ROC 曲線：X 軸 FPR（False Positive Rate）、Y 軸 TPR（True Positive Rate/Recall）
    - AUC = 曲線下面積 · 0.5 = 隨機猜 · 1.0 = 完美
    - 優點：不受閾值影響、適合比較不同模型
  - R²（判定係數）：
    - 迴歸專用指標（不是分類！）
    - R² = 1 - (SS_res/SS_tot)
    - 代表模型解釋了多少百分比的變異
  - 考試提醒：分類用 AUC/F1，迴歸用 R²/MSE，不要混用
- 講者這時說：「AUC 的好處是不受分類閾值影響——你不需要先決定 threshold 是 0.5 還是 0.3，它評估的是模型在所有可能閾值下的整體表現。R² 是迴歸指標，跟分類完全無關。考試會考你什麼場景用什麼指標，記住這個大原則就不會選錯。」

---

## S11 · PITFALL — Imbalanced Data 上用 Accuracy

- 畫面：左紅錯 / 右綠對 / 數字範例
- 畫面上的字：
  - 場景：詐騙偵測，10,000 筆資料中只有 20 筆詐騙（0.2%）
  - 錯：模型全猜「不是詐騙」→ Accuracy = 9980/10000 = 99.8% → 報告「模型很準」
  - 對：Precision = 0/0 = undefined · Recall = 0/20 = 0% → 一筆詐騙都沒抓到
  - 解法：看 Precision/Recall/F1/AUC-PR，不要只看 Accuracy
  - 樣題 Q10：Accuracy 計算——但更重要的是知道什麼時候 Accuracy 沒意義
- 講者這時說：「這個考點會從不同角度反覆出現。樣題 Q10 考 Accuracy 的計算，但真正的考點是：你算出來之後，要知道這個數字在 imbalanced data 上可能毫無意義。99.8% accuracy 聽起來很好——但如果你一筆詐騙都沒抓到，這個模型就是廢物。」

---

## S12 · CHECKPOINT — 指標選用判斷

- 畫面：白底三場景 + 指標選擇
- 畫面上的字：
  - 場景 A：癌症篩檢——不能漏診比誤診重要
    → 高 Recall 優先（寧可多檢查也不能放過）
  - 場景 B：垃圾郵件過濾——不能把正常信當垃圾
    → 高 Precision 優先（寧可漏一些垃圾也不能誤殺）
  - 場景 C：信用評分——整體表現 + 不受閾值影響
    → AUC 或 F1
  - 場景 D：房價預測——迴歸任務
    → R² 或 MSE（不是 Accuracy！）
- 講者這時說：「指標選擇的心法就一句話：『漏掉嚴重還是誤報嚴重？』漏掉嚴重追 Recall，誤報嚴重追 Precision。兩者都重要看 F1。迴歸任務完全不看 Accuracy——那是分類指標。這個判斷邏輯考試至少出兩題。」

---

## S13 · CONCEPT-CARD — Loss Function 與 Loss Curve

- 畫面：Loss Function 對照表 + Loss Curve 三種模式（真圖佔位）
- 畫面上的字：
  - Loss Function = 模型成績單的反面（越低越好）
  - 迴歸：MSE（Mean Squared Error）= Σ(y-y')²/n · MAE = Σ|y-y'|/n
  - 分類：Cross-Entropy = -Σ[y·log(p) + (1-y)·log(1-p)]
  - Loss Curve 三種模式：
    - A 正常收斂：train/val 都下降且接近
    - B Overfitting：train 持續下降但 val 先降後升
    - C Underfitting：train/val 都很高且下降慢
  - 樣題 Q11：Loss Function 的選擇
- 講者這時說：「Loss Function 就是模型的導航儀——它告訴模型往哪個方向調整。分類用 Cross-Entropy、迴歸用 MSE，這是標準配置。更重要的是 Loss Curve：畫出 train loss 和 val loss 的走勢，一眼就能判斷模型狀態。train 很低 val 很高 = overfitting，兩個都很高 = underfitting。」

---

## S14 · CONCEPT-CARD — 調參策略

- 畫面：四大參數 + 影響方向表
- 畫面上的字：
  - Learning Rate：
    - 太大 → 震盪不收斂 · 太小 → 收斂太慢
    - 常見起手：0.001（Adam）或 0.01（SGD）
  - Batch Size：
    - 大 → 訓練穩定但泛化可能差 · 小 → 噪音大但泛化可能好
    - 常見：32, 64, 128, 256
  - Regularization（L1/L2/Dropout）：
    - 加強 → 降低 overfitting 但可能 underfitting
    - Dropout rate 常見 0.2-0.5
  - Early Stopping：
    - 監控 val loss → 連續 N 個 epoch 沒改善就停
    - 最簡單有效的防 overfitting 手段
- 講者這時說：「調參不是亂試。每個參數都有明確的影響方向。Learning rate 影響收斂速度，batch size 影響泛化能力，regularization 影響模型複雜度。Early Stopping 是最偷懶但最有效的方法——不需要你手動調任何東西，它自動在最好的時候停下來。」

---

## S15 · PITFALL — 不看 Loss Curve 就調參

- 畫面：左紅錯 / 右綠對
- 畫面上的字：
  - 錯：不畫 Loss Curve 直接跑 GridSearch → 三小時後得到一組參數但不知道為什麼好
  - 對：先畫 Loss Curve → 判斷是 overfitting 還是 underfitting → 針對性調參
  - 如果 overfitting → 加 regularization / dropout / early stopping / 更多資料
  - 如果 underfitting → 增加模型複雜度 / 減少 regularization / 加特徵
  - Why：盲目調參 = 盲人調琴，效率極低
- 講者這時說：「很多人拿到模型就開始跑 GridSearch，三小時後得到一組『最佳參數』但不知道為什麼。更聰明的做法是先畫一張 Loss Curve——如果是 overfitting，你需要的是 regularization 不是更多 epochs；如果是 underfitting，你需要的是更複雜的模型不是更小的 learning rate。先診斷再治療。」

---

## S16 · CHECKPOINT — Loss Curve 診斷練習

- 畫面：三張 Loss Curve + 診斷選項
- 畫面上的字：
  - 圖 A：train loss 和 val loss 都穩定下降，最終接近
    → 正常收斂 · 可以繼續訓練或微調
  - 圖 B：train loss 持續下降，val loss 先降後升
    → Overfitting · 解法：Early Stopping / Dropout / Regularization / 更多資料
  - 圖 C：train loss 和 val loss 都很高，下降很慢
    → Underfitting · 解法：增加模型複雜度 / 加特徵 / 減少 regularization
- 講者這時說：「三張圖三種狀態。重點是圖 B——那個 val loss 開始上升的轉折點就是 Early Stopping 應該停的地方。很多人看到 train loss 還在降就繼續訓練，結果模型越來越 overfit。Val loss 才是你的真實成績，train loss 是自我感覺良好。」

---

## S17 · CONCEPT-CARD — 處理 Class Imbalance

- 畫面：三種策略 + 注意事項
- 畫面上的字：
  - 策略一：Oversampling（增加少數類）
    - 簡單複製（random oversampling）
    - SMOTE（合成新樣本：在少數類鄰居之間插值）
  - 策略二：Undersampling（減少多數類）
    - Random undersampling（簡單移除）
    - 缺點：可能丟失重要資訊
  - 策略三：演算法層面
    - class_weight='balanced'（調整損失函數權重）
    - 調整分類閾值
  - 致命注意事項：重抽樣只能在 train set 內做！在 split 前做 = data leakage
  - 樣題 Q13：資料重抽樣策略
- 講者這時說：「樣題 Q13 考重抽樣。三種策略各有優缺點——oversampling 不丟資料但可能 overfit、undersampling 快但丟資料、class_weight 最簡單但不一定夠。但最重要的注意事項是：SMOTE 或任何重抽樣必須在 train/test split 之後、只在 train set 上做。如果在 split 前做，合成的樣本可能同時出現在 train 和 test 中，這就是 leakage。」

---

## S18 · CONCEPT-CARD — GDPR 被遺忘權

- 畫面：GDPR 要點 + 對 ML 的影響
- 畫面上的字：
  - GDPR（General Data Protection Regulation）：歐盟資料保護法規
  - 被遺忘權（Right to Erasure / Right to be Forgotten）：
    - 用戶有權要求刪除其個人資料
    - 組織必須在合理時間內完成刪除
    - 包含資料庫記錄 + 備份 + 衍生資料
  - 對 ML 的影響：
    - 模型可能需要重新訓練（移除該用戶的訓練資料後）
    - 需要建立資料血統追蹤（data lineage）
    - 需要記錄哪些資料用於訓練哪個模型
  - 樣題 Q12：GDPR 被遺忘權的具體要求
- 講者這時說：「樣題 Q12 直接考 GDPR。被遺忘權的意思是：如果一個歐洲用戶說『刪掉我的資料』，你不只要刪資料庫的記錄，還要思考——你的模型是用他的資料訓練的，模型裡面可能『記住』了他的模式。嚴格來說你可能需要重新訓練模型。這就是為什麼 data lineage 很重要——你要知道哪些資料訓練了哪個模型。」

---

## S19 · CONCEPT-CARD — 演算法偏誤與公平性

- 畫面：偏誤來源 + 公平性指標
- 畫面上的字：
  - 偏誤三大來源：
    - 訓練資料偏差（某族群樣本不足 → 模型對該族群表現差）
    - 特徵選擇偏差（用性別/種族等敏感特徵 → 直接歧視）
    - 標籤偏差（歷史決策本身就有偏見 → 模型學會偏見）
  - 公平性指標（考試知道名字就好）：
    - Demographic Parity：各族群的正面預測比例相同
    - Equalized Odds：各族群的 TPR 和 FPR 相同
    - Predictive Parity：各族群的 Precision 相同
  - 調整策略：移除敏感特徵 / 重新平衡訓練資料 / 後處理校正閾值
- 講者這時說：「演算法偏見不是模型故意歧視——是它從有偏見的資料中學到了偏見。經典案例：用歷史招聘資料訓練的 AI，因為過去男性被錄取的比例較高，就學會了對女性評分較低。考試考的是：偏誤從哪裡來、怎麼偵測、怎麼調整。公平性指標知道名字和基本概念就好，不需要計算。」

---

## S20 · PRACTICE-PROMPT — sklearn 程式排序題

- 畫面：白底打亂程式碼 + 正確順序
- 畫面上的字：
  ```
  打亂順序的程式碼：
  (A) model.fit(X_train, y_train)
  (B) from sklearn.ensemble import RandomForestClassifier
  (C) print(classification_report(y_test, y_pred))
  (D) X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
  (E) model = RandomForestClassifier(n_estimators=100)
  (F) y_pred = model.predict(X_test)
  (G) from sklearn.model_selection import train_test_split
  (H) from sklearn.metrics import classification_report

  正確順序：B → G → H → D → E → A → F → C
  流程：import → 切資料 → 建模 → 訓練 → 預測 → 評估
  ```
  - 樣題 Q15：sklearn 程式排序題
- 講者這時說：「樣題 Q15 就是這種題型。不需要你會寫程式，只要你知道 sklearn 的標準流程：先 import、再切資料、建模型、訓練、預測、最後評估。這個順序是固定的——import 永遠在最前面、evaluate 永遠在最後面、fit 一定在 predict 前面。記住這個順序就能穩拿分。」

---

## S21 · PYRAMID — 建模三層功夫

- 畫面：pyramid_stack 三層
- 畫面上的字：
  - 頂層：治理到位（合規+公平——GDPR/偏見/可解釋性）
  - 中層：評估指標選對（不要用錯指標騙自己——Precision/Recall/F1/AUC）
  - 底層：特徵工程做好（垃圾進垃圾出——轉換/萃取/選擇）
  - 底部：底層不穩，上面全白做
- 講者這時說：「從下往上。特徵工程是地基——資料不好模型再強也沒用。評估指標是品管——用錯指標你以為模型很好其實很爛。治理是最後一關——技術上完美但法律上違規或倫理上有偏見，一樣不能上線。三層功夫缺一不可。」

---

## S22 · MOTIVATION — 課程總結

- 畫面：10 章全景回顧 + 考試加油
- 畫面上的字：
  - 「從 Ch01 AI 概念到 Ch10 ML 治理——你已經完成 iPAS 中級科目3 的完整備考。」
  - 10 章路線圖縮略版
  - 考試不只考技術，更考判斷力
  - 「演算法不用全背，但必須知道每個的定位。模型做出來只是開始，調好評好管好才是重點。」
- 講者這時說：「恭喜你走完了整個課程。回顧一下我們走過的路：Ch01-05 打底，Ch06-07 中級必考，Ch08 統計基礎，Ch09 演算法選型，Ch10 建模到治理。科目3 的考試範圍到此全部覆蓋。記住兩句話帶進考場：演算法考的是選型不是推導、指標要會選不只會算。祝你考試順利，我們考場見。」
