# Ch10 — 建模調參、評估與 ML 治理｜考試分析與模擬題

> 對應評鑑範圍：中級 L233 + L234
> 科目：科目3 機器學習技術與應用
> 考試時間：90 分鐘 / 50 題 / Python 程式題約 25%

---

## 一、評鑑範圍對照表

| 評鑑代碼 | 評鑑項目 | 考試重點 | 預估題數 | 本章對應 |
|----------|---------|---------|---------|---------|
| L233-1 | 數據準備特徵工程 | 標準化/正規化、One-Hot、特徵選擇 | 3-4 題 | S4-S8 |
| L233-2 | 模型選擇架構設計 | 標註品質、訓練前配置 | 1-2 題 | S6 |
| L233-3 | 模型訓練評估驗證 | Accuracy/Precision/Recall/F1/AUC/Loss Curve | 5-6 題 | S9-S13 |
| L233-4 | 模型調整優化 | Learning rate/Batch size/Regularization/Early Stopping/重抽樣 | 4-5 題 | S14-S17 |
| L234-1 | 數據隱私安全合規 | GDPR 被遺忘權 | 2-3 題 | S18 |
| L234-2 | 演算法偏見公平性 | 偏誤來源、公平性指標 | 2-3 題 | S19 |

**合計預估**：~17-23 題（佔科目3的 34-46%）

---

## 二、考題類型分析

### 類型 A：概念辨識與判斷（~30%）
- 標準化 vs 正規化辨識
- 特徵工程步驟分類
- Loss Function 選擇
- GDPR 要求辨識

### 類型 B：指標計算與應用（~25%）
- Accuracy 計算（混淆矩陣）
- Precision/Recall/F1 計算
- R² 解讀
- 指標場景選用

### 類型 C：診斷與調參（~20%）
- Loss Curve 診斷（overfitting/underfitting）
- 調參方向判斷
- Class imbalance 處理策略

### 類型 D：Python 程式題（~25%）
- sklearn 程式碼排序
- 程式碼讀懂與判斷
- API 參數意義

---

## 三、樣題考點對應

| 樣題編號 | 考點 | 評鑑代碼 | 類型 | 難度 |
|---------|------|---------|------|------|
| Q3 | Overfitting 辨識 | L233-3 | A | 易 |
| Q5 | 標註品質 | L233-2 | A | 易 |
| Q9 | 標準化(Z-score)公式 | L233-1 | A | 中 |
| Q10 | Accuracy 計算 | L233-3 | B | 中 |
| Q11 | Loss Function 選擇 | L233-3 | A | 中 |
| Q12 | GDPR 被遺忘權 | L234-1 | A | 易 |
| Q13 | 資料重抽樣 | L233-4 | C | 中 |
| Q15 | sklearn 程式排序 | L233-4 | D | 中 |

---

## 四、模擬試題（10 題）

### 模擬題 1（類型 A — 標準化 vs 正規化）

下列關於資料前處理方法的描述，何者正確？

(A) 標準化（Standardization）使用 Min-Max 公式將資料壓縮到 [0, 1] 區間
(B) 正規化（Normalization）使用 Z-score 公式使資料均值為 0、標準差為 1
(C) 標準化（Z-score）適用於對距離敏感的演算法如 SVM 和 KNN
(D) 正規化（Min-Max）不受離群值（outlier）影響

**答案：(C)**

**詳解**：標準化（Z-score）公式為 z = (x - mean) / std，使資料均值為 0、標準差為 1，適用於 SVM、KNN 等對距離敏感的演算法。(A)(B) 把標準化和正規化的公式反了——Z-score 是標準化、Min-Max 是正規化。(D) Min-Max 正規化會受 outlier 嚴重影響，因為 min 和 max 容易被極端值拉偏。

---

### 模擬題 2（類型 B — Accuracy 計算）

一個二元分類模型的混淆矩陣如下：

|  | 預測正 | 預測負 |
|--|--------|--------|
| 實際正 | 40 | 10 |
| 實際負 | 20 | 930 |

請問此模型的 Accuracy、Precision、Recall 各為多少？

(A) Accuracy=97%, Precision=80%, Recall=67%
(B) Accuracy=97%, Precision=67%, Recall=80%
(C) Accuracy=93%, Precision=67%, Recall=80%
(D) Accuracy=93%, Precision=80%, Recall=67%

**答案：(B)**

**詳解**：
- Accuracy = (TP + TN) / 全部 = (40 + 930) / (40 + 10 + 20 + 930) = 970 / 1000 = 97%
- Precision = TP / (TP + FP) = 40 / (40 + 20) = 40/60 = 66.7% ≈ 67%
- Recall = TP / (TP + FN) = 40 / (40 + 10) = 40/50 = 80%

注意：此模型 Accuracy 高達 97%，但 Precision 只有 67%（預測為正的有 1/3 是錯的）。在 imbalanced data 場景下 Accuracy 可能不是最佳指標。

---

### 模擬題 3（類型 B — 指標選用）

以下四個場景，各應優先關注哪個評估指標？

| 場景 | 最優先指標 |
|------|-----------|
| I. 癌症篩檢 | (?) |
| II. 垃圾郵件過濾 | (?) |
| III. 房價預測 | (?) |
| IV. 信用卡詐騙偵測（0.1% 正樣本） | (?) |

(A) I-Recall, II-Precision, III-R², IV-AUC-PR
(B) I-Precision, II-Recall, III-Accuracy, IV-F1
(C) I-Recall, II-Precision, III-Accuracy, IV-Accuracy
(D) I-F1, II-F1, III-F1, IV-F1

**答案：(A)**

**詳解**：I. 癌症篩檢不能漏診（False Negative 代價極高）→ 高 Recall。II. 垃圾郵件不能誤殺正常信（False Positive 代價高）→ 高 Precision。III. 房價是迴歸任務 → R²（不是分類指標）。IV. 詐騙偵測正樣本極少 → AUC-PR 比 AUC-ROC 更適合極度不平衡的資料。(B) I 和 II 反了。(C) III 用 Accuracy 不適合迴歸、IV 用 Accuracy 在 0.1% 正樣本下毫無意義。(D) F1 不適合迴歸任務。

---

### 模擬題 4（類型 C — Loss Curve 診斷）

觀察一個深度學習模型的 Loss Curve：訓練 loss 持續下降至接近 0，但驗證 loss 在第 20 個 epoch 後開始上升。下列處理方式何者最不適合？

(A) 在第 20 個 epoch 附近設定 Early Stopping
(B) 增加 Dropout 比率
(C) 增加更多的隱藏層和神經元
(D) 增加訓練資料量

**答案：(C)**

**詳解**：這是典型的 Overfitting——訓練 loss 極低但驗證 loss 上升代表模型在背答案。(A) Early Stopping 在最佳點停止，直接有效。(B) Dropout 是 regularization，降低模型複雜度，適合。(D) 更多資料增加泛化能力，適合。(C) 增加層數和神經元讓模型更複雜，反而加劇 overfitting。

---

### 模擬題 5（類型 C — Class Imbalance）

處理 Class Imbalance 問題時，下列做法何者有 data leakage 的風險？

(A) 在 train/test split 之後，對 train set 做 SMOTE oversampling
(B) 在 train/test split 之前，對整個 dataset 做 SMOTE oversampling
(C) 在訓練時設定 class_weight='balanced'
(D) 調整分類閾值從 0.5 改為 0.3

**答案：(B)**

**詳解**：SMOTE 在 split 前對整個 dataset 做，合成的樣本是基於少數類的鄰居插值生成的。如果先 SMOTE 再 split，合成樣本和原始樣本可能分別落入 train 和 test set，導致 test set 包含了從 train 資料衍生出的合成樣本——這就是 data leakage。(A) 在 split 後只對 train set 做 SMOTE 是正確做法。(C)(D) 是模型層面的調整，不涉及資料洩漏。

---

### 模擬題 6（類型 A — Loss Function）

下列關於損失函數（Loss Function）的描述，何者正確？

(A) 迴歸任務通常使用 Cross-Entropy Loss
(B) 二元分類任務通常使用 MSE（Mean Squared Error）
(C) Cross-Entropy Loss 衡量預測機率分佈與實際標籤之間的差距
(D) Loss Function 的值越大代表模型表現越好

**答案：(C)**

**詳解**：Cross-Entropy Loss 衡量的是模型預測的機率分佈與真實標籤之間的差距——預測越接近真實標籤，loss 越低。(A) 迴歸用 MSE 不是 Cross-Entropy。(B) 二元分類用 Binary Cross-Entropy 不是 MSE。(D) Loss 越低越好，不是越大。

---

### 模擬題 7（類型 A — GDPR）

根據歐盟 GDPR 的「被遺忘權」（Right to Erasure），當用戶要求刪除其個人資料時，對已訓練好的機器學習模型可能產生什麼影響？

(A) 無需任何處理，因為模型參數中不包含原始資料
(B) 只需要刪除資料庫中的原始記錄即可
(C) 可能需要重新訓練模型，因為模型可能從該用戶資料中學到了模式
(D) 只需要在模型推論時排除該用戶即可

**答案：(C)**

**詳解**：雖然模型參數不直接儲存原始資料，但模型是從訓練資料（包含該用戶資料）中學習的，模型的參數已經受到該資料的影響。嚴格遵守被遺忘權，可能需要移除該用戶的訓練資料後重新訓練模型。(A) 模型參數確實受訓練資料影響。(B) 光刪資料庫不夠，模型本身也受影響。(D) 排除推論不等於刪除資料的影響。這就是為什麼 data lineage（資料血統追蹤）在 ML 系統中很重要。

---

### 模擬題 8（類型 D — Python 程式題）

以下程式碼計算了哪個評估指標？

```python
from sklearn.metrics import confusion_matrix
import numpy as np

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()
result = tp / (tp + fn)
print(f"Result: {result:.2f}")
```

(A) Accuracy
(B) Precision
(C) Recall
(D) F1 Score

**答案：(C)**

**詳解**：`tp / (tp + fn)` 就是 Recall（召回率）的公式。Recall = TP / (TP + FN)，代表真正為正的樣本中模型抓到了多少。(A) Accuracy = (TP+TN)/(TP+TN+FP+FN)。(B) Precision = TP/(TP+FP)。(D) F1 = 2×Precision×Recall/(Precision+Recall)。

---

### 模擬題 9（類型 A — 演算法偏誤）

一家銀行使用歷史貸款審核資料訓練了一個 AI 模型來自動審核貸款申請。發現模型對某些族群的拒絕率明顯高於其他族群。這種偏誤最可能的來源是什麼？

(A) 模型的 learning rate 設定過大
(B) 模型使用了太多隱藏層
(C) 訓練資料中歷史人為決策本身就存在偏見
(D) 模型的 batch size 設定過小

**答案：(C)**

**詳解**：這是典型的「標籤偏差」——歷史的人為審核決策本身就可能對某些族群有偏見（例如過去對某些群體核貸率較低），模型從這些有偏見的歷史決策中學習，就會複製甚至放大這些偏見。(A)(B)(D) 是模型架構和超參數的問題，與族群偏見無直接關係。

---

### 模擬題 10（類型 D — sklearn 程式排序）

以下 Python 程式碼片段被打亂了順序。請選出正確的執行順序：

```
(1) scaler = StandardScaler()
(2) from sklearn.preprocessing import StandardScaler
(3) X_test_scaled = scaler.transform(X_test)
(4) X_train_scaled = scaler.fit_transform(X_train)
(5) from sklearn.model_selection import train_test_split
(6) X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

(A) 2 → 5 → 6 → 1 → 4 → 3
(B) 5 → 2 → 6 → 1 → 3 → 4
(C) 2 → 5 → 1 → 6 → 4 → 3
(D) 5 → 2 → 1 → 6 → 3 → 4

**答案：(A)**

**詳解**：正確流程：
1. import 所有需要的模組（2, 5 順序可互換）
2. 切分資料（6）
3. 建立 scaler（1）
4. 對 train set 做 fit_transform（4）——fit 學習 mean/std，transform 套用
5. 對 test set 只做 transform（3）——用 train 的 mean/std，不重新 fit

注意 (4) 用 `fit_transform` 而 (3) 只用 `transform`——這是為了避免 data leakage。如果 test set 也做 fit_transform，就用了 test set 自己的 mean/std，等於洩漏了測試集資訊。

---

## 五、備考策略

### 優先級排序

1. **最高優先（必拿分）**：Accuracy/Precision/Recall/F1 公式與計算、指標選用判斷、標準化 vs 正規化 → 幾乎每次都考
2. **高優先**：Loss Curve 診斷、Class Imbalance 處理、GDPR 被遺忘權
3. **中優先**：特徵工程三步驟分類、調參策略（learning rate/batch size）、演算法偏誤
4. **持續練習**：sklearn 程式碼排序和閱讀 → 記住標準流程即可

### 記憶技巧

- **標準化 vs 正規化**：口訣「Z 標 M 正」（Z-score = 標準化、Min-Max = 正規化）
- **指標選用**：「漏掉嚴重追 Recall、誤報嚴重追 Precision、兩者平衡看 F1、迴歸看 R²」
- **混淆矩陣**：TP/FP/FN/TN 的位置記法——T/F 判斷對錯、P/N 是模型的預測
- **Loss Curve 三模式**：正常收斂（兩線接近）/ Overfitting（train 低 val 高）/ Underfitting（兩線都高）
- **sklearn 流程**：import → split → preprocess → model → fit → predict → evaluate
- **SMOTE 注意**：split 後才做、只做 train set

### Accuracy 計算速查

```
混淆矩陣：
           預測正(P)  預測負(N)
實際正(P)    TP         FN
實際負(N)    FP         TN

Accuracy  = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)     ← 預測正裡面有幾個是對的
Recall    = TP / (TP + FN)     ← 真正是正的裡面抓到幾個
F1        = 2 × P × R / (P + R)
FPR       = FP / (FP + TN)    ← ROC 曲線的 X 軸
TPR       = Recall             ← ROC 曲線的 Y 軸
```

### 時間分配建議（90 分鐘 50 題）

- 本章範圍約 17-23 題，平均每題 1.5 分鐘
- 先做概念辨識題（標準化/正規化、GDPR）→ 最快最穩
- 計算題用公式模板（混淆矩陣 → 代數字）
- Loss Curve 題先判斷 overfitting 還是 underfitting → 再選處理方式
- Python 題看 import 和 fit/transform 的順序
