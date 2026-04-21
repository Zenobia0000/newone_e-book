# Ch02 — 機器學習：表格世界的主戰場｜講師講稿

> **課程時長**：2 小時（講授 80 min + 課堂練習 25 min + QA 15 min）
> **受眾定位**：有基礎 Python / 統計能力的學員，目標是在企業 tabular 場景選對模型、避免常見地雷
> **前置知識**：Ch01 統計作為 AI 的底盤
> **後續銜接**：Ch03 深度學習、Ch05 評估與治理

---

## 1. 本節目標 (Learning Objectives)

完成本節後，學員應能：

1. 區分 supervised / unsupervised，並判斷手上的商業問題該走哪一邊。
2. 區分 regression / classification，正確定義 feature 與 label。
3. 說明 train / validation / test 三份切法的目的，避免用錯 split。
4. 用圖解直覺辨認 overfitting / underfitting，連結到 bias-variance tradeoff，並理解 regularization 的作用。
5. 列出 data leakage 三大紅旗，能在建模前主動檢查。
6. 說明為何 tree-based model 是表格資料 baseline 首選，以及 pipeline + preprocessing 一致性的必要。

---

## 2. 時間切分表

```
00:00-00:08  開場暖身：企業 80% AI 專案是表格 + 傳統 ML（S1-S3）
00:08-00:20  Supervised vs Unsupervised + Regression vs Classification（S4-S6）
00:20-00:35  Train/Val/Test Split + Checkpoint（S7-S8）
00:35-00:55  Overfitting/Underfitting + Bias-Variance + Regularization（S9-S13）
00:55-01:10  Data Leakage 三大紅旗 + Class Imbalance 陷阱（S14-S16）
01:10-01:25  Tree-Based Model 為何稱霸 + Pipeline 一致性（S17-S18）
01:25-01:40  綜合場景判斷 Checkpoint（S19）
01:40-01:55  SWOT 收束 + 三原則 Pyramid（S20-S21）
01:55-02:00  銜接 Ch03 + QA（S22）
```

---

## 3. 關鍵教學點 (Key Teaching Points)

1. **Baseline 是信仰**：整章最重要的訊息是「先做 baseline」。要讓學員離開教室時帶著一個反射：拿到任何建模任務，第一件事不是挑模型，而是跑一個 DummyClassifier 或簡單 LogisticRegression 建立底線。沒有 baseline 的分數就是沒有意義的數字。

2. **Leakage 比模型選擇重要 10 倍**：學員最常犯的致命錯誤不是選錯模型，而是 leakage。要反覆用案例強化：AUC 0.99 幾乎都是 leakage，不是你模型厲害。三大紅旗要讓學員背到能夢中念出來。

3. **考試類比貫穿全章**：train = 課本、validation = 模擬考、test = 正式考。這個類比要用在 split、overfitting、leakage 三個地方，讓非技術背景學員秒懂。「用 test set 調參 = 考古題直接當期中考」這句話要重複至少兩次。

4. **Bias-Variance 用靶心射擊圖**：不要用數學公式推導。四象限靶心圖一看就懂：集中但偏（high bias low variance）、散但中心對（low bias high variance）。這張圖比任何數學推導都有效。

5. **Tree-based model 是表格世界的瑞士刀**：不需要講 tree 的數學，只要讓學員知道三件事：(a) 不需要特徵縮放、(b) 自動抓非線性、(c) Kaggle tabular 場景幾乎都是 tree 贏。然後銜接到 pipeline 確保 preprocessing 不 leak。

6. **每個 pitfall 要配真實案例**：P2 leakage 用流失預測把「取消日期」當特徵的案例；P4 imbalance 用詐騙偵測 99.5% accuracy 的案例。真實案例比定義有效 10 倍。

---

## 4. 學員常犯錯誤 (Common Pitfalls)

- **跳過 baseline 直上複雜模型**：花三天調 XGBoost 結果跟 LogisticRegression 差不到 1%。→ 先跑 DummyClassifier → LogReg → 再考慮 ensemble。
- **Data leakage 不自知**：驗證分數好到不真實卻沒起疑。→ 建模前檢查每個特徵的「時間合法性」和「因果方向」。
- **不切 validation set**：直接用 test set 調參，等於考古題當期中考。→ train/val/test 嚴格三分。
- **Imbalanced data 用 accuracy**：99% accuracy 其實全猜多數類。→ 看 precision/recall/F1/AUC-PR。
- **Preprocessing 在 split 前 fit**：`scaler.fit_transform(X_all)` 再 split → 測試集資訊已洩漏。→ 用 Pipeline 包起來，fit 只碰 train。

---

## 5. 提問設計 (Discussion Prompts)

1. 你是電商數據分析師，老闆要你預測「哪些客戶下個月會流失」。這是 supervised 還是 unsupervised？regression 還是 classification？你的 baseline 是什麼？
2. 你建了一個模型 AUC 0.98，老闆很開心。你第一個反應應該是什麼？（預期答：先懷疑 leakage，不是慶祝）
3. 信用卡盜刷偵測：10 萬筆只有 200 筆盜刷。你用 accuracy 評估得到 99.8%——這個數字代表什麼？（預期答：什麼都不代表，可能全猜「不是盜刷」就能達到）

---

## 6. 延伸資源 (Further Reading)

- Google ML Crash Course（免費）：涵蓋 linear regression/classification/generalization/datasets，是本章最對齊的參考
- scikit-learn 官方 User Guide：Pipeline 和 cross_val_score 的正確用法
- Kaggle「Tabular Playground Series」：練習 tree-based model 的好場地
- 論文參考：「Do We Need Deep Learning for Tabular Data?」— tree-based model 在 tabular 場景的系統性比較

---

## 7. 常見 Q&A

**Q1：所以深度學習在表格資料完全沒用嗎？**
A：不是完全沒用，但 ROI 通常不划算。研究顯示 tree-based model 在大多數 tabular 場景跟 DL 打平甚至更好，而且訓練快 10-100 倍、解釋性高。除非你有特殊理由（例如跟其他模態融合），否則先用 tree。

**Q2：Baseline 要做到什麼程度才算夠？**
A：至少兩層。第一層 DummyClassifier（隨機猜或全猜多數類），這是「不用任何模型」的底線。第二層簡單線性模型（LogReg 或 LinearRegression），這是「最簡單的模型」的底線。之後的每一個模型都要能明確打贏第二層才值得用。

**Q3：怎麼知道我有沒有 leakage？**
A：三個信號。(1) 分數好到不像真的（AUC > 0.95 就要懷疑）。(2) 某個特徵的 feature importance 異常高。(3) 上線後效果斷崖式下跌。建模前的習慣是：每一個特徵都問自己「在預測時間點，這個資訊真的已經知道了嗎？」

**Q4：Class imbalance 該怎麼處理？**
A：先換指標（precision/recall/F1/AUC-PR），這是第一步也是最重要的一步。然後可以考慮：(a) 調整決策閾值、(b) class_weight='balanced'、(c) SMOTE 等 oversampling（但要在 cross-validation 的 fold 內做，不能在外面做）。
