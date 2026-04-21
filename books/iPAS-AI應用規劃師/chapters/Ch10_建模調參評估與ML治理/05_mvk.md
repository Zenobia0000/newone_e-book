# Ch10 · MVK 考前速查卡（Minimum Viable Knowledge）

> 離開本節後，你的記憶裡必須長出「評估指標公式 + 標準化/正規化口訣 + Loss Curve 診斷 + GDPR 知識點」。
> 對應 01_outline.md 的 6 個 Learning Objectives。
> 本章的核心判斷：**模型做出來只是開始，調好、評好、管好才是考試重點。**

---

## 1 特徵工程三步驟速查（對應 LO1）

| 步驟 | 英文 | 做什麼 | 常見方法 |
|------|------|--------|---------|
| 轉換 | Feature Transformation | 把原始資料格式化 | One-Hot Encoding / 標準化 / 正規化 / Log 轉換 |
| 萃取 | Feature Extraction | 從現有特徵創造新特徵 | 多項式特徵 / TF-IDF / PCA / 交互特徵 |
| 選擇 | Feature Selection | 挑有用的、丟沒用的 | 相關係數篩選 / Feature Importance / L1 Regularization |

**一句口訣**：轉換格式化、萃取造新的、選擇去蕪存菁。

---

## 2 標準化 vs 正規化速查（對應 LO1）

| 項目 | 標準化 Standardization | 正規化 Normalization |
|------|----------------------|---------------------|
| 別名 | Z-score | Min-Max Scaling |
| 公式 | z = (x - mean) / std | x' = (x - min) / (max - min) |
| 結果 | 均值 0、標準差 1 | 壓縮到 [0, 1] |
| 適用 | SVM / KNN / 神經網路 | 需要固定範圍的場景 |
| 對 outlier | 較不敏感 | 敏感（min/max 被拉偏） |

**必記口訣**：**Z 標 M 正**（Z-score = 標準化、Min-Max = 正規化）

**考試陷阱**：中文翻譯混亂，不同教科書可能反著定義。記公式最保險。

---

## 3 評估指標公式速查（對應 LO2）

### 混淆矩陣

```
               預測正(P)   預測負(N)
實際正(P)        TP          FN
實際負(N)        FP          TN

T/F = 模型判斷對/錯
P/N = 模型的預測結果（正/負）
```

### 分類指標

| 指標 | 公式 | 白話 | 什麼時候用 |
|------|------|------|-----------|
| Accuracy | (TP+TN) / All | 整體正確率 | Balanced data |
| Precision | TP / (TP+FP) | 預測正裡面對了幾個 | 誤報嚴重時（垃圾郵件） |
| Recall | TP / (TP+FN) | 真正是正的抓到幾個 | 漏掉嚴重時（癌症篩檢） |
| F1 Score | 2PR / (P+R) | P 和 R 的調和平均 | 兩者都重要時 |
| AUC-ROC | ROC 曲線下面積 | 不受閾值影響的整體表現 | 比較不同模型 |
| AUC-PR | PR 曲線下面積 | 極度不平衡時比 AUC-ROC 好 | Imbalanced data |

### 迴歸指標

| 指標 | 公式 | 白話 |
|------|------|------|
| MSE | Σ(y-y')²/n | 平均平方誤差（對大誤差敏感） |
| MAE | Σ\|y-y'\|/n | 平均絕對誤差（對大誤差較不敏感） |
| R² | 1 - (SS_res/SS_tot) | 模型解釋了多少比例的變異 |

### 指標選用心法

```
漏掉嚴重 → Recall（癌症篩檢、安全監控）
誤報嚴重 → Precision（垃圾郵件、推薦系統）
兩者平衡 → F1
不確定   → AUC
迴歸任務 → R² 或 MSE（不是 Accuracy！）
極度不平衡 → AUC-PR > AUC-ROC > Accuracy
```

---

## 4 Accuracy 手算模板（考試必用）

```
範例：
         預測正  預測負
實際正     40     10     ← 實際正 50 人
實際負     20    930     ← 實際負 950 人
         ↑60    ↑940     全部 1000 人

Accuracy  = (40+930)/1000 = 97.0%
Precision = 40/(40+20) = 40/60 = 66.7%
Recall    = 40/(40+10) = 40/50 = 80.0%
F1        = 2 × 0.667 × 0.800 / (0.667+0.800) = 72.7%

注意：Accuracy 97% 看起來很高，但 Precision 只有 67%
→ 預測為正的裡面有 1/3 是錯的
```

---

## 5 Loss Function 速查（對應 LO3）

| 任務類型 | Loss Function | 公式簡記 |
|---------|--------------|---------|
| 迴歸 | MSE (Mean Squared Error) | Σ(y-y')²/n |
| 迴歸 | MAE (Mean Absolute Error) | Σ\|y-y'\|/n |
| 二元分類 | Binary Cross-Entropy | -[y·log(p) + (1-y)·log(1-p)] |
| 多元分類 | Categorical Cross-Entropy | -Σ y_i · log(p_i) |

**口訣**：迴歸用 MSE/MAE、分類用 Cross-Entropy。

---

## 6 Loss Curve 診斷速查（對應 LO3）

```
模式 A：正常收斂
  train loss ↓  val loss ↓  兩線接近
  → 繼續訓練或微調

模式 B：Overfitting
  train loss ↓↓  val loss 先↓後↑
  → Early Stopping / Dropout / Regularization / 加資料

模式 C：Underfitting
  train loss 高  val loss 高  下降慢
  → 增加模型複雜度 / 加特徵 / 減 regularization

關鍵：val loss 才是真實成績，train loss 是自我感覺良好
```

---

## 7 調參策略速查（對應 LO4）

| 參數 | 太大的效果 | 太小的效果 | 常見起手值 |
|------|-----------|-----------|-----------|
| Learning Rate | 震盪不收斂 | 收斂太慢 | 0.001(Adam) / 0.01(SGD) |
| Batch Size | 穩定但泛化差 | 噪音大但泛化好 | 32 / 64 / 128 |
| L2 Regularization | Underfitting | Overfitting | 0.001 ~ 0.01 |
| Dropout Rate | Underfitting | Overfitting | 0.2 ~ 0.5 |

**Early Stopping**：監控 val loss → 連續 N 個 epoch 沒改善就停 → 最簡單有效的防 overfitting

---

## 8 Class Imbalance 處理速查（對應 LO5）

| 策略 | 做什麼 | 優點 | 缺點 |
|------|--------|------|------|
| Random Oversampling | 複製少數類樣本 | 簡單、不丟資料 | 容易 overfit |
| SMOTE | 在少數類鄰居間插值合成新樣本 | 更多樣化 | 仍可能 overfit |
| Random Undersampling | 隨機移除多數類樣本 | 快速 | 丟失資訊 |
| class_weight='balanced' | 調整 loss 中各類的權重 | 最簡單、不改資料 | 不一定夠 |
| 調整閾值 | 從 0.5 改成更低的值 | 不改模型 | 需要找最佳閾值 |

**致命規則**：SMOTE / Oversampling / Undersampling 只能在 **train set 內做**！
Split 前做 = Data Leakage。

---

## 9 GDPR 被遺忘權速查（對應 LO6）

```
GDPR = General Data Protection Regulation（歐盟資料保護法規）

被遺忘權（Right to Erasure）：
  - 用戶有權要求刪除其個人資料
  - 組織必須在合理時間內完成
  - 包含：資料庫記錄 + 備份 + 衍生資料

對 ML 的影響：
  - 模型可能需要重新訓練（移除該用戶訓練資料後）
  - 需要 data lineage（追蹤哪些資料訓練了哪個模型）
  - 需要 model versioning（記錄每個模型版本用了什麼資料）

考試重點：
  - 知道被遺忘權是什麼
  - 知道對已訓練模型的影響
  - 知道 data lineage 的必要性
```

---

## 10 演算法偏誤速查（對應 LO6）

```
偏誤三大來源：
  1. 訓練資料偏差 → 某族群樣本不足
  2. 特徵選擇偏差 → 用了敏感特徵（性別/種族）
  3. 標籤偏差 → 歷史決策本身有偏見

公平性指標（知道名字就好）：
  - Demographic Parity：各族群的正面預測比例相同
  - Equalized Odds：各族群的 TPR 和 FPR 相同
  - Predictive Parity：各族群的 Precision 相同

調整策略：
  - 預處理：重新平衡訓練資料
  - 處理中：移除/遮蔽敏感特徵
  - 後處理：針對不同族群校正閾值
```

---

## 11 sklearn API 速查（Python 程式題用）

```python
# 完整建模流程（程式排序題模板）
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Step 1: 切資料
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Step 2: 前處理（fit_transform 只用在 train，transform 用在 test）
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit + transform
X_test_scaled = scaler.transform(X_test)         # 只 transform！

# Step 3: 建模 + 訓練
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train_scaled, y_train)

# Step 4: 預測 + 評估
y_pred = model.predict(X_test_scaled)
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 關鍵 API
scaler.fit_transform(X_train)   # 學習參數 + 轉換（只用在 train）
scaler.transform(X_test)        # 套用已學的參數（用在 test）
model.fit(X, y)                 # 訓練
model.predict(X)                # 預測
model.score(X, y)               # 評估（accuracy for classification, R² for regression）

# 常見 metrics
from sklearn.metrics import (
    accuracy_score,              # 準確率
    precision_score,             # 精確率
    recall_score,                # 召回率
    f1_score,                    # F1
    roc_auc_score,               # AUC
    confusion_matrix,            # 混淆矩陣
    classification_report,       # 完整報告
    mean_squared_error,          # MSE
    r2_score                     # R²
)
```

**程式排序必記順序**：import → split → preprocess → model → fit → predict → evaluate

**致命細節**：`fit_transform` 只用在 train set，test set 只用 `transform`。

---

## 考前 30 分鐘最後掃描清單

- [ ] 混淆矩陣 TP/FP/FN/TN 的位置記得嗎？
- [ ] Accuracy/Precision/Recall/F1 四個公式能秒寫嗎？
- [ ] 指標選用心法：漏掉→Recall / 誤報→Precision / 迴歸→R²
- [ ] 標準化 vs 正規化口訣：Z 標 M 正
- [ ] Loss Curve 三模式能診斷嗎？（正常/Overfitting/Underfitting）
- [ ] Loss Function 配對：迴歸→MSE / 分類→Cross-Entropy
- [ ] 調參四大參數的影響方向知道嗎？
- [ ] SMOTE 在 split 後才做（不能在 split 前）
- [ ] GDPR 被遺忘權 + 對 ML 模型的影響
- [ ] 演算法偏誤三大來源能列出來嗎？
- [ ] sklearn 流程：import → split → preprocess → model → fit → predict → evaluate
- [ ] fit_transform 只用 train、transform 用 test
