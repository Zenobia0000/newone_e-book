# Ch08 講師講稿 — 機率統計與大數據處理分析

> 節次時長：150 分鐘（講授 100 + 演練計算 35 + 總結回顧 15）
> Governing thought：「統計和大數據不是兩件事——考試考的是你能否用統計語言解讀大數據結果。」
> 評鑑範圍：中級 L221 + L222 + L223 + L224（科目2 全覆蓋）
> 特別注意：本章約 25% 為 Python 程式題

---

## 1. 本節目標（對齊評鑑範圍）

1. **LO1**：用描述統計三維度正確摘要資料集（L221）。
2. **LO2**：辨識常見機率分佈模型（常態/二項/Poisson），依場景選擇（L221）。
3. **LO3**：依研究設計選擇假設檢定方法（t/F/卡方），正確解讀 p-value（L221）。
4. **LO4**：執行 Z-score 計算與 IQR 異常值偵測（L221 + L223）。
5. **LO5**：解釋 PCA 降維原理，讀懂 explained variance（L223）。
6. **LO6**：解讀 ROC 曲線與 AUC（L223）。
7. **LO7**：說明串流處理技術與批次處理的差異（L222）。
8. **LO8**：解釋差分隱私原理與 epsilon 參數意義（L224）。
9. **LO9**：讀懂 Python 程式碼片段並預測輸出（科目2 程式題）。

## 2. 時間切分表（100 + 35 + 15）

| 時間 | 區段 | 內容 | 對應評鑑 |
|---|---|---|---|
| 0~5 | 講授 | 開場：科目2 考試結構 + 本章四大範圍 | — |
| 5~20 | 講授 | Part A：描述統計三維度（集中趨勢/離散/分佈） | L221 |
| 20~30 | 講授 | Z-score 計算 + 標準常態分佈（Q10 考點） | L221+L223 |
| 30~40 | 講授 | IQR 異常值偵測（Q7 考點） | L223 |
| 40~50 | 講授 | 機率分佈三模型（常態/二項/Poisson） | L221 |
| 50~65 | 講授 | Part B：假設檢定——t/F/卡方選擇決策樹（Q1 考點） | L221 |
| 65~75 | 講授 | Part C：PCA 降維原理 + explained variance（Q9 考點） | L223 |
| 75~85 | 講授 | ROC 曲線 + AUC 解讀（Q2 考點） | L223 |
| 85~90 | 講授 | K-means vs DBSCAN 聚類比較 | L223 |
| 90~95 | 講授 | Part D：串流處理 vs 批次處理（Q12 考點） | L222 |
| 95~100 | 講授 | 差分隱私 + epsilon 參數（Q8 考點） | L224 |
| 100~115 | 演練 | Python 程式題實戰（CIFAR-10 + Z-score + PCA + ROC） | L223+L224 |
| 115~135 | 演練 | 計算題三連發：Z-score + IQR + PCA 手算 | L221+L223 |
| 135~150 | 總結 | 公式速查回顧 + 考試策略 + Ch09 預告 | — |

## 3. 關鍵教學點

### Part A：敘述性統計與機率分佈（L221）

#### 描述統計三維度

- **集中趨勢**：均值（Mean）、中位數（Median）、眾數（Mode）。
  - 均值受極端值影響 → 偏態分佈看中位數更可靠。
  - 考試要點：右偏分佈 Mean > Median > Mode。

- **離散程度**：範圍（Range）、四分位距（IQR）、變異數（Variance）、標準差（SD）。
  - IQR = Q3 - Q1，對異常值穩健。
  - 變異數 = 離差平方和的平均，標準差 = 變異數的平方根。

- **分佈型態**：偏態（Skewness）、峰態（Kurtosis）。
  - 正偏（右偏）：尾巴在右邊，均值 > 中位數。
  - 負偏（左偏）：尾巴在左邊，均值 < 中位數。
  - 常態分佈：偏態=0、峰態=3（超額峰態=0）。

#### Z-score（Q10 考點）

- **公式**：Z = (X - mu) / sigma
- **意義**：距離平均值幾個標準差。Z=2 表示高於平均 2 個標準差。
- **應用**：標準化（讓不同量綱的特徵可比較）、異常值偵測（|Z|>3 為異常）。
- **標準常態分佈**：68-95-99.7 法則（1sigma/2sigma/3sigma 涵蓋比例）。

#### IQR 異常值偵測（Q7 考點）

- **計算步驟**：
  1. 排序資料，找 Q1（25%）和 Q3（75%）。
  2. IQR = Q3 - Q1。
  3. 下界 = Q1 - 1.5 * IQR。
  4. 上界 = Q3 + 1.5 * IQR。
  5. 超出上下界的即為異常值。
- **考試陷阱**：忘記乘 1.5 是最常見的計算錯誤。

#### 機率分佈三模型

| 分佈 | 適用場景 | 參數 | 形狀 |
|---|---|---|---|
| 常態分佈 | 連續資料、中央極限定理 | mu, sigma | 鐘形對稱 |
| 二項分佈 | n 次獨立伯努利試驗的成功次數 | n, p | 離散、可偏 |
| Poisson 分佈 | 單位時間/空間內事件發生次數 | lambda | 離散、右偏 |

### Part B：假設檢定（L221）

#### 檢定方法選擇決策樹（Q1 考點）

```
你要比較什麼？
├── 兩組「平均值」差異 → t 檢定
│   ├── 獨立兩組 → 獨立樣本 t 檢定
│   └── 同一組前後 → 配對樣本 t 檢定
├── 三組以上「平均值」差異 → F 檢定（ANOVA）
└── 類別變數之間的「關聯性/頻次分佈」→ 卡方檢定
    ├── 適合度檢定：觀察頻次 vs 期望頻次
    └── 獨立性檢定：兩個類別變數是否獨立
```

- **考試記憶口訣**：兩組均值 t，三組均值 F，類別頻次 chi-square。
- **p-value 解讀**：p < alpha（通常 0.05）→ 拒絕 H0 → 差異顯著。
- **考試陷阱**：p < 0.05 不等於「效果很大」——還要看效果量（effect size）。

### Part C：大數據分析方法（L223）

#### PCA 主成分分析（Q9 考點）

- **原理**：找到資料變異最大的方向，將高維資料投影到低維空間。
- **步驟**：標準化 → 計算協方差矩陣 → 特徵值分解 → 選前 k 個主成分。
- **關鍵指標**：explained variance ratio——每個主成分解釋了多少比例的總變異。
- **決策規則**：累積 explained variance > 85%（或 95%）即可停止。
- **考試要點**：PCA 是「無監督」的降維方法，不使用標籤資訊。

#### ROC 曲線與 AUC（Q2 考點）

- **ROC 曲線**：X 軸 = FPR（False Positive Rate），Y 軸 = TPR（True Positive Rate / Recall）。
- **AUC（Area Under Curve）**：ROC 曲線下方面積。
  - AUC = 1.0：完美分類器。
  - AUC = 0.5：隨機猜測（對角線）。
  - AUC < 0.5：比隨機猜還差（模型可能標籤反了）。
- **考試要點**：AUC 對類別不平衡不敏感（相對於 accuracy），所以常用於不平衡資料集。

#### K-means vs DBSCAN

| | K-means | DBSCAN |
|---|---|---|
| 需要預設群數 | 是（k） | 否 |
| 群形狀 | 球型/凸形 | 任意形狀 |
| 對異常值 | 敏感 | 穩健（標記為噪聲） |
| 參數 | k | eps, min_samples |

#### 數據可視化原則

- 連續 vs 連續 → 散佈圖（scatter plot）。
- 類別 vs 連續 → 箱型圖（box plot）/ 長條圖。
- 類別分佈 → 直方圖（histogram）/ 圓餅圖。
- 時間序列 → 折線圖（line chart）。
- 原則：先問「你要回答什麼問題」，再選圖表類型。

### Part D：數據處理技術與隱私保護（L222 + L224）

#### 串流處理 vs 批次處理（Q12 考點）

| | 批次處理 | 串流處理 |
|---|---|---|
| 資料特性 | 靜態、完整資料集 | 動態、持續流入 |
| 延遲 | 高（分鐘~小時） | 低（毫秒~秒） |
| 工具 | Hadoop MapReduce, Spark Batch | Spark Streaming, Kafka Streams, Flink |
| 適用場景 | 日報表、歷史分析 | 即時推薦、詐騙偵測、IoT 監控 |

#### 差分隱私（Q8 考點）

- **核心概念**：在查詢結果中加入隨機噪音，讓攻擊者無法判斷某個人是否在資料集中。
- **epsilon (epsilon)**：隱私預算參數。
  - epsilon 越小 → 噪音越大 → 隱私保護越強 → 但資料可用性越低。
  - epsilon 越大 → 噪音越小 → 隱私保護越弱 → 但資料可用性越高。
- **考試記法**：epsilon 小 = 隱私大（反比關係）。

### Part E：Python 程式題（科目2 ~25%）

#### 考試常見程式碼模式

1. **NumPy 陣列操作**：shape / reshape / axis 參數。
2. **Pandas 資料處理**：read_csv / describe / groupby / fillna。
3. **sklearn 建模**：train_test_split / fit / predict / score。
4. **matplotlib 視覺化**：plot / scatter / hist / xlabel / ylabel / title。
5. **CIFAR-10 題型**：載入資料 → 查看 shape → 正規化 → 建模（Q15 考點）。

#### 常見陷阱
- **shape 混淆**：CIFAR-10 影像是 (32, 32, 3)，不是 (3, 32, 32)。
- **axis 方向**：axis=0 是沿列（向下），axis=1 是沿行（向右）。
- **dtype 問題**：影像像素值需要 /255.0 轉成 float，否則標準化會出錯。
- **train_test_split**：random_state 參數確保可重現，test_size 預設 0.25。

## 4. 演練設計（35 min）

### 演練 A：Python 程式題實戰（15 min）

> 給定以下 Python 程式碼，預測輸出結果：

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 模擬資料
np.random.seed(42)
X = np.random.randn(100, 5)
X[:, 0] = X[:, 0] * 10  # 第一個特徵變異很大

# 標準化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

print(X_pca.shape)
print(np.round(pca.explained_variance_ratio_, 2))
print(np.round(sum(pca.explained_variance_ratio_), 2))
```

> 問題：(1) X_pca 的 shape 是什麼？(2) 前三個主成分的 explained variance 加總大約多少？(3) 如果要保留 85% 的變異量，至少需要幾個主成分？

### 演練 B：手算計算題（20 min）

> **題 1（Z-score）**：某班成績平均 72 分，標準差 8 分。小明考 88 分，他的 Z-score 是多少？代表什麼意義？

> **題 2（IQR）**：一組資料的 Q1=20, Q3=40。計算 IQR 及異常值上下界。資料值 65 是否為異常值？

> **題 3（檢定選擇）**：研究者想知道三個不同教學法的考試成績是否有顯著差異，應選用什麼檢定方法？寫出 H0 和 H1。

## 5. 考試常見陷阱

1. **Z-score 計算**：題目可能不直接給 mu 和 sigma，而是給原始資料要你先算出來。
2. **IQR 乘數**：忘記 1.5 會導致異常值範圍太窄或太寬。常見選項會故意放 IQR 不乘 1.5 的答案。
3. **檢定方法選錯**：兩組配對 vs 兩組獨立的 t 檢定不同——配對是「同一組人前後比較」。
4. **PCA 結果解讀**：explained_variance_ratio_ 是「比例」不是「數值」，加總最大=1.0。
5. **ROC 曲線方向**：FPR 在 X 軸、TPR 在 Y 軸——不要畫反。AUC=0.5 不是「還行」，是「沒用」。
6. **Python shape**：(100, 32, 32, 3) 意思是 100 張 32x32 的 RGB 影像，不要把 100 當作高度。

## 6. 提問設計

1. 「Z-score = -2.5 代表什麼？這個資料點正常嗎？」
2. 「你有三組使用者的停留時間資料，想知道三組有沒有差異，用什麼檢定？為什麼不用 t 檢定做三次？」
3. 「PCA 降到 2 維時 explained variance = 60%，你會怎麼決定要不要繼續降維？」

## 7. 延伸資源

- iPAS 中級科目2 學習指引：L221-L224 章節。
- scipy.stats 文件（假設檢定函式：ttest_ind, f_oneway, chi2_contingency）。
- sklearn.decomposition.PCA 文件。
- sklearn.metrics.roc_curve / roc_auc_score 文件。
- 差分隱私入門：「The Algorithmic Foundations of Differential Privacy」（Dwork & Roth）。

## 8. 常見 Q&A

- **Q：考試的計算題需要用計算機嗎？**
  A：iPAS 中級考試通常不允許使用計算機，但計算題的數字會設計成可以心算或簡單手算。重點是方法和公式，不是複雜計算。
- **Q：Python 程式題需要會寫程式嗎？**
  A：不需要從零寫程式。考試是給你程式碼片段，問你「輸出是什麼」或「哪一行有錯」或「該填什麼」。重點是讀懂 code，不是寫 code。
- **Q：差分隱私的 epsilon 常考什麼？**
  A：最常考 epsilon 大小與隱私強度的「反比關係」——epsilon 小=隱私保護強、噪音大、可用性低。

## 9. 收斂金句

「統計給你判斷工具，大數據給你分析場景，Python 給你實作能力——科目2 考的是三者的交叉。記住：Z-score 問標準差、IQR 問四分位、檢定問比什麼、PCA 問解釋量、ROC 問 AUC——五個問題框架能解大部分考題。」
