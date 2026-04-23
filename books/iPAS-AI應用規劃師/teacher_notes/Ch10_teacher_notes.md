# Ch10 — 建模調參、評估與 ML 治理｜講師講稿

> **課程時長**：2 小時（講授 80 min + 練習 25 min + QA 15 min）
> **受眾定位**：iPAS 中級科目3 考生，需掌握特徵工程、評估指標、調參策略及 ML 治理
> **前置知識**：Ch09 機器學習演算法與深度學習
> **後續銜接**：全課程最終章，銜接總複習
> **評鑑範圍**：中級 L233（數據準備特徵工程/模型選擇架構設計/模型訓練評估驗證/模型調整優化）+ L234（數據隱私安全合規/演算法偏見公平性）

---

## 1. 本節目標 (Learning Objectives)

完成本節後，學員應能：

1. 執行特徵工程三步驟（轉換/萃取/選擇），區分標準化（Z-score）與正規化（Min-Max）的適用場景。
2. 正確選用評估指標（Accuracy/Precision/Recall/F1/AUC/R²），避免在 imbalanced data 上誤用 Accuracy。
3. 說明 Loss Function 的角色與常見類型（MSE/Cross-Entropy），從 Loss Curve 診斷訓練狀態。
4. 運用調參策略（learning rate/batch size/regularization/Early Stopping）提升模型效能。
5. 處理 class imbalance：資料重抽樣（oversampling/undersampling/SMOTE）與指標調整。
6. 說明 GDPR 被遺忘權的要求，識別演算法偏誤並理解公平性調整策略。

---

## 2. 時間切分表

```
00:00-00:08  開場：模型做出來只是開始 + 立論
00:08-00:25  特徵工程三步驟 + 標準化 vs 正規化 + 標註品質
00:25-00:35  特徵工程 Checkpoint
00:35-00:55  評估指標全家福 + AUC/R² + Imbalance 陷阱
00:55-01:10  Loss Function + 調參策略 + Loss Curve 診斷
01:10-01:25  Class Imbalance 處理 + GDPR + 演算法偏誤
01:25-01:40  sklearn 程式排序題模擬
01:40-01:55  收束金字塔 + 課程總結
01:55-02:00  QA
```

---

## 3. 關鍵教學點 (Key Teaching Points)

1. **標準化 vs 正規化是送分題也是送命題**：中文翻譯混亂是最大陷阱。必須同時給中英文對照：標準化 = Standardization = Z-score（均值0標準差1）；正規化 = Normalization = Min-Max（壓到0-1）。口訣「Z 標 M 正」要讓學員背到反射。

2. **評估指標的選擇比分數本身重要**：Accuracy 在 balanced data 上好用，但在 imbalanced data 上是謊言。醫療場景要高 Recall（不能漏診）、垃圾郵件要高 Precision（不能誤殺正常信）。教學時用場景倒推指標。

3. **Loss Curve 是最被低估的診斷工具**：train loss 低但 val loss 高 = overfitting → 加 regularization。train/val loss 都高 = underfitting → 加模型複雜度或特徵。一張圖就能告訴你該做什麼。

4. **SMOTE 必須在 split 之後做**：在整個 dataset 上做 SMOTE 再 split，合成樣本同時出現在 train 和 test 中——這是 data leakage。正確做法是 split 後只在 train set 上做。

5. **GDPR 和偏見不能跳過**：科目3 不只考技術。樣題直接考 GDPR 被遺忘權。L234 評鑑範圍明確包含數據隱私和演算法偏見。至少花 15 分鐘講。

6. **sklearn 程式排序題是固定考型**：學員只要記住標準流程（import → split → model → fit → predict → evaluate），就能穩拿這類題目。

---

## 4. 學員常犯錯誤 (Common Pitfalls)

- **Imbalanced data 用 Accuracy**：99% accuracy 可能是全猜多數類。→ 看 Precision/Recall/F1/AUC-PR。
- **標準化和正規化搞混**：Z-score = 標準化（均值0標準差1）、Min-Max = 正規化（壓到0-1）。口訣「Z 標 M 正」。
- **不看 Loss Curve**：直接調參等於盲人調琴。→ 先畫 train/val loss curve 再決定調什麼。
- **SMOTE 在 split 前做**：合成樣本洩漏到 test set = data leakage。→ 只在 train set 內做。
- **忽略 GDPR 和偏見題**：以為科目3 純技術。→ L234 明確在評鑑範圍內。

---

## 5. 提問設計 (Discussion Prompts)

1. 你的醫療 AI 系統要偵測癌症，你會優先追求高 Precision 還是高 Recall？為什麼？（預期答：Recall，不能漏診。）

2. 你的訓練資料中 95% 是正常交易、5% 是詐騙。模型 Accuracy 96%——你該開心嗎？（預期答：不該，可能全猜正常就有 95%。）

3. 你的模型 train loss 很低但 val loss 很高。你該增加模型複雜度還是加 regularization？（預期答：加 regularization，這是 overfitting。）

4. 一個歐洲用戶要求你刪除他在系統中的所有個人資料。根據 GDPR，你必須怎麼做？對已訓練好的模型有什麼影響？（預期答：刪除資料 + 可能需要重新訓練模型。）

---

## 6. 延伸資源 (Further Reading)

- scikit-learn 官方文件：Preprocessing / Model Evaluation / Pipeline
- Google ML Crash Course：Classification 章節（Precision/Recall/ROC 的互動教學）
- iPAS 中級科目3 學習指引：L233/L234 章節
- EU GDPR 官方網站：被遺忘權（Right to Erasure）條文

---

## 7. 常見 Q&A

**Q1：標準化和正規化到底哪個是哪個？**
A：記口訣「Z 標 M 正」。Z-score（(x-mean)/std）是標準化（Standardization），結果均值0標準差1。Min-Max（(x-min)/(max-min)）是正規化（Normalization），結果壓縮到0-1。

**Q2：什麼時候用 Precision、什麼時候用 Recall？**
A：問自己「漏掉比較嚴重，還是誤報比較嚴重？」漏掉嚴重（癌症/安全監控）→高 Recall。誤報嚴重（垃圾郵件/推薦系統）→高 Precision。兩者都重要→看 F1。不確定→看 AUC。

**Q3：GDPR 被遺忘權對 ML 有什麼具體影響？**
A：用戶要求刪除資料時，不只要刪資料庫記錄，還要考慮模型是否需要重新訓練（因為模型可能「記住」了該用戶的資料模式）。

**Q4：SMOTE 跟普通 oversampling 有什麼差別？**
A：普通 oversampling 只是複製少數類樣本（完全重複）。SMOTE 在少數類樣本之間「插值」合成新樣本——找到最近鄰，在兩者之間生成新樣本。合成樣本更多樣化，但仍然要在 train set 內做。
