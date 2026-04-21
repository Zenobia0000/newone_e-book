# Ch02 · MVK 速學卡（Minimum Viable Knowledge）

> 離開本節後，你的肌肉記憶裡必須長出這四個反射 + 六個 LO 的心智模型。
> 對應 01_outline.md 的 6 個 Learning Objectives。
> 本章的核心判斷：**先做 baseline，再談複雜模型——表格資料場景，傳統 ML 常常就是最佳解。**

---

## ① Supervised vs Unsupervised 選型（對應 LO1, LO2）

| 問題 | 判斷 | 典型任務 |
|------|------|---------|
| 你有 label 嗎？ | 有 → Supervised | 預測/分類 |
| 你沒有 label？ | 無 → Unsupervised | 分群/降維/異常偵測 |

**Supervised 再問一層**：

| Label 類型 | 任務類型 | 範例 |
|-----------|---------|------|
| 連續數字 | Regression | 房價、銷售額、溫度 |
| 類別 | Classification | 流失/不流失、垃圾/正常、風險等級 |

**核心術語**：
- **Feature** = 你手上的線索（輸入欄位）
- **Label** = 你要猜的答案（目標欄位）

**一句口訣**：有沒有答案決定 supervised/unsupervised；答案是數字還是類別決定 regression/classification。

---

## ② Bias-Variance Tradeoff（對應 LO4）

```
Bias 高  = 瞄不準（模型太簡單 → underfitting）
Variance 高 = 太敏感（模型太複雜 → overfitting）

           Underfitting          Overfitting
Train 表現    差                    完美
Val 表現      差                    爛
診斷         兩條線都高             兩條線間距大
處理         加複雜度/加特徵        regularization/更多資料/簡化
```

**Regularization 三劍客**：

| 方法 | 作用 | 適用場景 |
|------|------|---------|
| L1 (Lasso) | 不重要的特徵砍到 0 | 想自動做特徵選擇 |
| L2 (Ridge) | 所有權重都縮小 | 想整體變保守 |
| Early Stopping | val loss 上升就停 | tree/neural network |

**Tree 的 regularization**：`max_depth` / `min_samples_leaf` / `n_estimators`

**靶心記憶法**：
- 集中但偏 = high bias, low variance → 加複雜度
- 散但中心對 = low bias, high variance → 加 regularization
- 目標 = 集中又準 = low bias, low variance

---

## ③ ML Pipeline Checklist（對應 LO3, LO6）

```
Step 1：定義問題
  → supervised / unsupervised？
  → regression / classification？
  → 評估指標是什麼？（不是 accuracy！看場景選）

Step 2：切資料
  → train (60-70%) / validation (15-20%) / test (15-20%)
  → 時間序列 → time-based split，不能 random shuffle
  → test set 只碰一次

Step 3：建 baseline
  → DummyClassifier / DummyRegressor（底線中的底線）
  → LogisticRegression / LinearRegression（最簡單的模型）
  → 後面的模型要明確打贏 baseline 才值得用

Step 4：Preprocessing 放進 Pipeline
  → Pipeline([('scaler', StandardScaler()), ('model', LogReg())])
  → fit 只碰 train，transform 自動帶到 val/test
  → 黃金守則：所有 preprocessing 都在 Pipeline 內

Step 5：迭代
  → RandomForest（穩定 baseline）→ GradientBoosting（拼精度）
  → 用 validation set 調參、選模型
  → 最後在 test set 報告一次最終數字

Step 6：Error Analysis
  → 看 confusion matrix：錯在哪一類？
  → 看 feature importance：哪些特徵在出力？有沒有異常高的？
  → 看 residual plot（regression）：有沒有系統性偏差？
```

**考試類比**：
- Train = 課本（學習用）
- Validation = 模擬考（可以考很多次，用來調整讀書方法）
- Test = 正式考（只考一次，報告最終成績）

---

## ④ Data Leakage 紅旗（對應 LO5）

### 三大紅旗

| # | 紅旗 | 案例 | 怎麼查 |
|---|------|------|--------|
| 1 | 特徵是 label 的「結果」而非「原因」 | 流失預測用「取消訂閱日期」當特徵 | 問：因果方向對嗎？ |
| 2 | 特徵包含「預測時間點之後」的資訊 | 用下個月交易次數預測本月流失 | 問：這個資訊在預測時真的已知嗎？ |
| 3 | Preprocessing 在 split 前 fit 整個 dataset | `scaler.fit_transform(X_all)` 再 split | 問：有沒有在 Pipeline 外面做 fit？ |

### Leakage 警鈴

- AUC > 0.95 → 先懷疑，不是慶祝
- 某特徵 feature importance 異常高 → 檢查因果方向
- 上線後效果斷崖式下跌 → 回去查 leakage

**反射**：每一個特徵都問自己——「在預測時間點，這個資訊真的已經知道了嗎？」

---

## 五個必踩地雷（考前必背）

| # | 地雷 | 錯 | 對 |
|---|------|----|----|
| P1 | 跳過 baseline | 一開始就上 XGBoost | DummyClassifier → LogReg → 再考慮 |
| P2 | Data leakage | 用結果當特徵、未來資訊混入 | 每個特徵檢查因果 + 時間合法性 |
| P3 | 不切 validation | 用 test set 調參 | train/val/test 嚴格三分 |
| P4 | Imbalanced 用 accuracy | 99% accuracy 全猜多數類 | precision/recall/F1/AUC-PR |
| P5 | Preprocessing 外 fit | `fit_transform(X_all)` 再 split | Pipeline 內 fit 只碰 train |

---

## 實戰三原則（全課核心）

1. **先做 baseline，再談複雜模型** → 沒有底線的分數沒有意義
   ↳ DummyClassifier → LogReg → RandomForest → Boosting

2. **先檢查 leakage，再看分數** → 分數是假的比分數低更可怕
   ↳ 三大紅旗 + 每個特徵問因果 + 時間合法性

3. **先做 error analysis，再調參** → 不要盲目 GridSearch
   ↳ confusion matrix + feature importance + residual plot

---

## Tree-Based Model 速記（對應 LO6）

| 特性 | Random Forest | Gradient Boosting (XGB/LGBM) |
|------|--------------|------------------------------|
| 穩定性 | 高（bagging 降 variance） | 中（容易 overfit） |
| 精度天花板 | 中 | 高 |
| 調參難度 | 低 | 中高 |
| 定位 | 穩定 baseline | 拼精度武器 |

**共同優勢**：不用特徵縮放 / 自動抓非線性 / 抗 outlier / 可解釋

---

## 下一節銜接（Ch03 深度學習：表徵學習）

> 表格資料場景，ML 常常就是最佳解。
> 但當你面對的是圖片、文字、語音——行跟列裝不下這些資料。
> 你需要一套能「自動學特徵」的模型架構。
>
> **今天的 ML 判斷力，是明天選擇「要不要上 DL」的地基。**
