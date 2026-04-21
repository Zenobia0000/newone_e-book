# Ch02 — 機器學習：表格世界的主戰場｜Slides Design

> 22 張內容投影片（封面 + 22 + 版權）｜教學型七原型為主
> 對齊 `01_outline.md` 的 6 個 Learning Objectives x 5 個 Common Pitfalls
> 配色：主色 `#1565C0` + 錯誤紅 `#C62828`（僅 PITFALL 頁）+ 成功綠 `#2E7D32`
> 受眾：有基礎 Python / 統計能力的學員，類比走「考試 / 射擊 / 工具箱」路線

---

## S1 · MOTIVATION — 企業 80% 的 AI 專案是表格 + 傳統 ML

- 🖼️ 畫面：白底 / 大字痛點句 / 右側資料卡「Kaggle 2023：tree-based model 稱霸 tabular」
- 📣 畫面上的字：
  - 標題：「你以為 AI 就是 ChatGPT？企業內部 80% 的 AI 專案，是一張 Excel 表加一棵決策樹。」
  - 卡片：tabular 場景 · tree-based model · 低成本高解釋性
- 🎙️ 講者這時說：「我知道你可能是被 ChatGPT 吸引來學 AI 的，但真相是——你進公司後接到的前十個 AI 任務，八個是表格資料。客戶流失預測、銷售額預估、風險評分——全部是行跟列。今天這一章教你怎麼用最少的模型，解最多的商業問題。」

---

## S2 · ASK — 同一份資料為什麼有人 0.95 有人 0.55

- 🖼️ 畫面：白底中央問句 + 資料卡
- 📣 畫面上的字：「同一份客戶資料——為什麼有人做出 AUC 0.95、有人 0.55？」 · 卡片：差距不在模型複雜度，在有沒有犯 leakage
- 🎙️ 講者這時說：「線索：那個 0.95 的人其實犯了 leakage，上線後掉到 0.55。而那個做出 0.72 的人反而是對的。今天你會學到怎麼分辨真分數和假分數。」

---

## S3 · SILENT — 立論

- 🖼️ 畫面：全藍底 / 白色 HERO 大字
- 📣 畫面上的字：「先做 baseline，再談複雜模型。／先檢查 leakage，再看分數。／先做 error analysis，再調參。」
- 🎙️ 講者這時說：「這三句話是本章的核心信仰。如果你今天只能記住三句話，就是這三句。順序比模型重要。」

---

## S4 · CONCEPT-CARD — Supervised vs Unsupervised

- 🖼️ 畫面：左右對比 vs_two_col
- 📣 畫面上的字：
  - 左：Supervised — 有標準答案 · 你給電腦考古題 + 答案，讓它學規律 · 預測/分類
  - 右：Unsupervised — 沒有答案 · 你給電腦一堆資料，讓它自己找結構 · 分群/降維/異常偵測
  - 底部：判斷法 → 你的資料有沒有 label？有就是 supervised
- 🎙️ 講者這時說：「最簡單的判斷法：你手上有沒有答案？有標準答案的就是 supervised——你在教電腦；沒有答案的就是 unsupervised——你在讓電腦自己探索。企業場景大部分是 supervised，因為你通常知道你要預測什麼。」

---

## S5 · CONCEPT-CARD — Regression vs Classification + Feature vs Label

- 🖼️ 畫面：上方左右對比 + 下方定義框
- 📣 畫面上的字：
  - 左：Regression — Label 是連續數字 · 預測房價、銷售額、溫度
  - 右：Classification — Label 是類別 · 預測是否流失、垃圾郵件、風險等級
  - 下方：Feature = 你的線索（輸入欄位）· Label = 你要猜的答案（目標欄位）
- 🎙️ 講者這時說：「Label 是數字就是 regression，Label 是類別就是 classification。Feature 就是你手上所有的線索。記住：你的任務定義決定了你該用什麼模型，不是反過來。」

---

## S6 · PRACTICE-PROMPT — 五個商業問題快速分類

- 🖼️ 畫面：白底五題列表 + 底部答案行
- 📣 畫面上的字：
  - Q1 客戶分群（unsupervised · clustering）
  - Q2 房價預測（supervised · regression）
  - Q3 垃圾郵件偵測（supervised · classification）
  - Q4 信用卡異常偵測（unsupervised 或 supervised，看有無 label）
  - Q5 下個月銷售額預估（supervised · regression）
- 🎙️ 講者這時說：「三十秒，自己判斷這五個。注意第四題——異常偵測可以是 supervised 也可以是 unsupervised，取決於你有沒有標過哪些是異常。這就是為什麼『有沒有 label』是第一個要問的問題。」

---

## S7 · CONCEPT-CARD — Train / Validation / Test Split

- 🖼️ 畫面：橫向三段 bar + 考試類比圖（真圖佔位）
- 📣 畫面上的字：
  - Train（60-70%）= 課本 · 模型從這裡學
  - Validation（15-20%）= 模擬考 · 用來調參、選模型，可以考很多次
  - Test（15-20%）= 正式考 · 最後只能用一次，用來報告最終成績
  - 時間序列提醒：不能 random split，要用 time-based split
- 🎙️ 講者這時說：「為什麼要切三份？因為你需要一份完全沒被碰過的資料來評估真實表現。如果你拿 test set 調參，就像期中考用考古題——你以為自己考 95 分，正式考發現只有 60。Validation 可以反覆用，Test 只用一次。」

---

## S8 · CHECKPOINT — 哪些做法在偷看考卷

- 🖼️ 畫面：白底三題 + 合法/非法標記
- 📣 畫面上的字：
  - 情境 A：用 test set 調 learning_rate → 非法（偷看正式考）
  - 情境 B：用 validation set 選 RandomForest vs XGBoost → 合法（模擬考選讀書法）
  - 情境 C：用 train+val 重新訓練，最後在 test 評估一次 → 合法（考前總複習 + 正式考一次）
- 🎙️ 講者這時說：「核心原則就一條：test set 只能碰一次，而且只用來報告最終數字，不能回頭改任何東西。碰第二次就不是 test set 了，它變成了第二個 validation set。」

---

## S9 · CONCEPT-CARD — Overfitting vs Underfitting 圖解

- 🖼️ 畫面：三張曲線並排（真圖佔位）
- 📣 畫面上的字：
  - 左：Underfitting — 直線穿過彎曲資料 · train 差 val 也差 · 模型太簡單
  - 中：Just Right — 平滑曲線貼合趨勢 · train 好 val 也好
  - 右：Overfitting — 鋸齒亂飛穿過每個點 · train 完美 val 爆炸 · 模型背答案
- 🎙️ 講者這時說：「這三張圖要記一輩子。左邊是學渣——課本都讀不好；右邊是背答案的學生——考古題滿分但新題全錯。中間才是真正理解的人。你的目標永遠是中間。」

---

## S10 · PITFALL (P1) — 跳過 baseline 直上複雜模型

- 🖼️ 畫面：左紅錯 / 右綠對 / 底部 why 綠條
- 📣 畫面上的字：
  - 錯：一開始就調 XGBoost 500 棵樹 + GridSearch 三天 · 結果比 LogReg 好 0.3%
  - 對：DummyClassifier → LogisticRegression → RandomForest → 才考慮 boosting
  - Why：沒有 baseline 的分數沒有意義；0.85 到底是好還是爛？跟 random guess 比呢？
- 🎙️ 講者這時說：「我見過太多人第一行就 import xgboost。你連 baseline 都沒跑，怎麼知道 0.85 是好是壞？也許 DummyClassifier 全猜多數類就有 0.83。那你花三天只贏了 0.02，這不叫 AI，這叫浪費生命。」

---

## S11 · CONCEPT-CARD — Bias-Variance Tradeoff

- 🖼️ 畫面：四象限靶心射擊圖（真圖佔位）
- 📣 畫面上的字：
  - 左上：High Bias, Low Variance — 每次都瞄偏但很集中（underfitting）
  - 右上：Low Bias, High Variance — 中心對但太散（overfitting）
  - 左下：High Bias, High Variance — 又偏又散（最慘）
  - 右下：Low Bias, Low Variance — 集中又準（目標）
  - 底部：模型複雜度升高 → bias 下降 + variance 上升 → 找到 sweet spot
- 🎙️ 講者這時說：「這張靶心圖比任何數學公式都直覺。Bias 就是瞄不準——你的模型系統性地偏離正確答案。Variance 就是太敏感——每次換一批資料結果就大變。好模型是在中間取平衡，不是把複雜度開到最大。」

---

## S12 · CHECKPOINT — 看 Learning Curve 判斷 Over/Under

- 🖼️ 畫面：兩張 learning curve + 診斷選項
- 📣 畫面上的字：
  - 圖 A：train loss 極低 + val loss 很高 → Overfitting · 解法：regularization / 更多資料 / 簡化模型
  - 圖 B：train loss 和 val loss 都很高 → Underfitting · 解法：增加模型複雜度 / 加特徵 / 減少 regularization
- 🎙️ 講者這時說：「以後每次訓練完模型，第一件事畫 learning curve。兩條線的間距就是 variance，兩條線的高度就是 bias。一看就知道該加複雜度還是加 regularization。」

---

## S13 · CONCEPT-CARD — Regularization：給模型加手銬

- 🖼️ 畫面：三欄比較 L1 / L2 / Early Stopping
- 📣 畫面上的字：
  - L1 (Lasso)：把不重要的特徵權重砍到 0 → 自動特徵選擇
  - L2 (Ridge)：把所有權重都縮小但不砍到 0 → 整體變保守
  - Early Stopping：訓練到 val loss 開始上升就停 → 不讓模型背太多答案
  - Tree 版本：max_depth / min_samples_leaf / n_estimators
- 🎙️ 講者這時說：「模型太自由就會背答案，regularization 就是限制它的自由度。L1 像是直接砍掉不需要的工具，L2 像是把每個工具的力道都調小。兩種各有用途，但共同目標一樣——不讓模型太自信。」

---

## S14 · PITFALL (P2) — Data Leakage

- 🖼️ 畫面：左紅錯 / 右綠對 / why 綠條 / 底部三大紅旗預告
- 📣 畫面上的字：
  - 錯：AUC 0.99 → 報告給老闆 → 上線後 AUC 0.55
  - 對：AUC 0.99 → 先懷疑 leakage → 檢查特徵 → 移除問題特徵 → AUC 0.72（真實實力）
  - Why：你的模型不是很強，是在偷看答案
- 🎙️ 講者這時說：「我給你一個反射：AUC 超過 0.95 的時候，你的第一個反應不應該是開心，應該是懷疑。真實商業場景很少有乾淨到讓你做到 0.95 的。如果分數好到不像真的，它通常就不是真的。」

---

## S15 · CONCEPT-CARD — Data Leakage 三大紅旗

- 🖼️ 畫面：三格紅旗 flag card，每格一個紅旗
- 📣 畫面上的字：
  - 紅旗一：特徵是 label 的「結果」而非「原因」 · 例：流失預測用「取消訂閱日期」當特徵
  - 紅旗二：特徵包含「預測時間點之後」的資訊 · 例：用下個月的交易次數預測這個月會不會流失
  - 紅旗三：Preprocessing 在 split 前 fit 了整個 dataset · 例：`scaler.fit_transform(X_all)` 再 split
- 🎙️ 講者這時說：「三大紅旗，背下來。每次建模前把特徵表拿出來，一個一個問：這個特徵在預測的那個時間點，真的已經知道了嗎？因果方向對嗎？有沒有偷用到未來的資訊？這三個問題能救你整個專案。」

---

## S16 · PITFALL (P4) — Class Imbalance 陷阱

- 🖼️ 畫面：左紅錯 / 右綠對 / why 綠條
- 📣 畫面上的字：
  - 錯：詐騙偵測 accuracy 99.5% → 報告「模型很準」 · 真相：模型全猜「不是詐騙」
  - 對：看 precision / recall / F1 / AUC-PR · 搭配 class_weight='balanced' 或調閾值
  - Why：當正樣本只佔 0.2%，全猜負樣本 accuracy 就是 99.8%——accuracy 在這裡是謊言
- 🎙️ 講者這時說：「這是第二個致命陷阱。你回去跟老闆說『模型 99.5% 準確度』，老闆很開心。結果上線一個月抓到 0 個詐騙。為什麼？因為你的模型學到的策略就是『全部說不是詐騙』——在 imbalanced data 上 accuracy 是最大的謊言。」

---

## S17 · CONCEPT-CARD — Tree-Based Model 為何稱霸表格資料

- 🖼️ 畫面：左欄四大優勢 + 右欄 Random Forest vs Gradient Boosting 比較
- 📣 畫面上的字：
  - 優勢一：不用特徵縮放（StandardScaler 省了）
  - 優勢二：自動處理非線性交互作用
  - 優勢三：可解釋性高（feature importance 一看就懂）
  - 優勢四：抗 outlier
  - Random Forest：穩定、不太 overfit、適合 baseline
  - Gradient Boosting (XGB/LGBM/CatBoost)：更準但需要調參、容易 overfit
- 🎙️ 講者這時說：「在表格資料場景，tree-based model 就是瑞士刀。你不需要標準化、不需要手動做交互特徵、不太怕 outlier。Random Forest 是你的穩定 baseline，Gradient Boosting 是你要拼精度時的武器。Kaggle tabular 競賽的 top 解法，九成以上是這兩類。」

---

## S18 · CONCEPT-CARD — Pipeline + Preprocessing 一致性

- 🖼️ 畫面：流程圖 flow_chain + 程式碼片段
- 📣 畫面上的字：
  - 問題：scaler.fit_transform 在 split 前做 → 測試集資訊洩漏
  - 解法：`Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression())])`
  - Pipeline 的 fit 只碰 train · transform 自動帶到 val/test
  - 黃金守則：所有 preprocessing 都放進 Pipeline，不要在外面做
- 🎙️ 講者這時說：「最後一個關鍵觀念。你可能覺得 StandardScaler 在 split 前做比較方便——但這就是 leakage。因為 scaler 看到了測試集的 mean 和 std。解法很簡單：用 sklearn 的 Pipeline 把 preprocessing 和 model 包在一起。Pipeline 會自動確保 fit 只碰 train，transform 自動帶到 val/test。一行程式消滅一整類 leakage。」

---

## S19 · CHECKPOINT — 綜合場景判斷

- 🖼️ 畫面：白底場景描述 + 四個子問題
- 📣 畫面上的字：
  - 場景：信用卡盜刷偵測 · 10 萬筆資料只有 200 筆盜刷
  - Q1：supervised 還是 unsupervised？（supervised，有 label）
  - Q2：regression 還是 classification？（classification，二元）
  - Q3：你的 baseline 是什麼？（DummyClassifier 全猜不是盜刷 → accuracy 99.8%）
  - Q4：該用什麼指標？（precision / recall / F1 / AUC-PR，不是 accuracy）
  - Q5：要檢查什麼 leakage？（交易後才知道的欄位有沒有混入特徵）
- 🎙️ 講者這時說：「五分鐘，小組討論。這個場景把今天學的所有東西串在一起。注意：你的 DummyClassifier baseline accuracy 是 99.8%——這就是為什麼 accuracy 在這裡沒有意義。你真正要看的是 recall：200 筆盜刷你抓到幾筆。」

---

## S20 · CONCEPT-CARD — SWOT 收束

- 🖼️ 畫面：四格 SWOT 矩陣
- 📣 畫面上的字：
  - S（優勢）：低成本、高解釋性、快速迭代
  - W（劣勢）：對非結構化資料（圖片/文字/語音）較弱
  - O（機會）：企業大量 tabular 場景可直接落地、ROI 高
  - T（威脅）：資料 drift 效果容易掉、需要持續監控
- 🎙️ 講者這時說：「這張 SWOT 是你跟老闆報告時的框架。ML 在表格場景的優勢是成本低、解釋性高、能快速證明價值。但弱點也很明確——碰到圖片、文字、語音就力不從心，這是下一章深度學習的事。最大的威脅是 data drift：你的模型今天很準，三個月後資料分布變了就不準了，所以需要持續監控。」

---

## S21 · PYRAMID — ML 實戰三原則

- 🖼️ 畫面：pyramid_stack 三層
- 📣 畫面上的字：
  - 頂層：先做 error analysis，再調參
  - 中層：先檢查 leakage，再看分數
  - 底層：先做 baseline，再談複雜模型
  - 底部：順序比模型重要
- 🎙️ 講者這時說：「這個金字塔從下往上看。最底下是 baseline——沒有底線的分數沒有意義。中間是 leakage——分數是假的比分數低更可怕。最上面是 error analysis——不要盲目調參，先看你的模型錯在哪裡、錯的是哪一類、為什麼錯。這三個順序比你選什麼模型重要一百倍。」

---

## S22 · MOTIVATION — 銜接 Ch03 深度學習

- 🖼️ 畫面：問句 + 下一章資料卡
- 📣 畫面上的字：「表格資料場景，ML 常常就是最佳解——但當你的資料是圖片、文字、語音時，你需要另一套武器。」 · 卡片：Ch03 · 深度學習：表徵學習
- 🎙️ 講者這時說：「今天你學到了表格世界的武器庫——baseline、tree-based model、pipeline。但企業不是只有表格。當你面對的是一萬張產品圖片、十萬篇客服對話、一千小時的語音紀錄，今天的 tree model 就不夠用了。下一章我們進入深度學習——不是因為它比較潮，而是因為它能處理今天處理不了的資料類型。我們下次見。」
