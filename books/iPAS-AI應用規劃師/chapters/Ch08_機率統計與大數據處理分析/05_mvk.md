# Ch08 · Minimum Viable Knowledge（MVK）— 考前速查卡

> 若只記得 15 件事，這就是 Ch08 的精華。
> 評鑑範圍：中級 L221 + L222 + L223 + L224（科目2）
> 含公式速查 + Python 程式碼模式

---

## 公式速查卡（考前 10 分鐘必看）

### Z-score

```
Z = (X - mu) / sigma
```

- **意義**：距離平均值幾個標準差。
- **異常值判定**：|Z| > 3 通常視為異常。
- **68-95-99.7 法則**：1sigma 內 68%，2sigma 內 95%，3sigma 內 99.7%。

### IQR 異常值法則

```
IQR = Q3 - Q1
下界 = Q1 - 1.5 * IQR
上界 = Q3 + 1.5 * IQR
```

- **超出上下界 = 異常值**。
- **千萬記得乘 1.5**。

### ROC / AUC

```
TPR (Recall) = TP / (TP + FN)
FPR          = FP / (FP + TN)
AUC          = ROC 曲線下面積
```

- AUC = 0.5 → 隨機猜（沒用）。
- AUC = 1.0 → 完美分類。
- AUC > 0.8 → 通常算不錯。

### PCA

```
累積 explained variance ratio >= 85%（或 95%）→ 停止
```

- PCA 是無監督降維，不用標籤。
- 使用前必須先標準化（StandardScaler）。

### 差分隱私

```
epsilon 小 → 噪音大 → 隱私保護強 → 可用性低
epsilon 大 → 噪音小 → 隱私保護弱 → 可用性高
```

- **記法**：epsilon 和隱私成反比。

---

## 描述統計三維度

| 維度 | 指標 | 考試重點 |
|---|---|---|
| **集中趨勢** | Mean / Median / Mode | 右偏：Mean > Median > Mode |
| **離散程度** | Range / IQR / Var / SD | IQR 對異常值穩健，SD 受極端值影響 |
| **分佈型態** | Skewness / Kurtosis | 偏態=0 對稱，正偏尾巴在右 |

**考試口訣**：右偏（正偏）= 尾巴在右 = Mean 被拉高 → Mean > Median > Mode。

---

## 假設檢定決策樹

```
你要比較什麼？
├── 兩組「平均值」→ t 檢定
│   ├── 獨立兩組 → 獨立樣本 t
│   └── 同一組前後 → 配對樣本 t
├── 三組以上「平均值」→ F 檢定（ANOVA）
└── 類別變數「頻次/關聯」→ 卡方檢定
    ├── 一個變數 vs 期望 → 適合度
    └── 兩個變數是否獨立 → 獨立性
```

**口訣**：兩組 t、三組 F、類別卡方。

**p-value 解讀**：p < 0.05 → 拒絕 H0 → 差異顯著。但 p < 0.05 不等於「效果很大」。

---

## 機率分佈三模型

| 分佈 | 適用場景 | 參數 | 記憶關鍵字 |
|---|---|---|---|
| **常態分佈** | 連續且對稱：身高/成績/測量誤差 | mu, sigma | 鐘形曲線 |
| **二項分佈** | n 次獨立試驗的成功次數 | n, p | 成功/失敗 + 固定次數 |
| **Poisson 分佈** | 單位時間/空間的事件計數 | lambda | 計數 + 固定時間/空間 |

---

## PCA 主成分分析

- **原理**：找資料變異最大的方向投影，壓縮維度。
- **步驟**：標準化 → 協方差矩陣 → 特徵值分解 → 選前 k 個。
- **關鍵指標**：`explained_variance_ratio_`（每個主成分解釋的比例）。
- **決策規則**：累積 >= 85% 就夠。
- **考試重點**：PCA 是無監督的（不用標籤）。使用前必須標準化。

---

## ROC 曲線與 AUC

| 指標 | 意義 |
|---|---|
| ROC 曲線 | 不同 threshold 下 (FPR, TPR) 的軌跡 |
| AUC = 0.5 | 等同隨機猜（對角線），模型無效 |
| AUC = 0.8 | 不錯的分類器 |
| AUC = 1.0 | 完美分類器（曲線經過左上角） |

**優勢**：AUC 對類別不平衡不敏感（比 accuracy 更可靠）。

---

## K-means vs DBSCAN

| | K-means | DBSCAN |
|---|---|---|
| 預設群數 | 需要（k） | 不需要 |
| 群形狀 | 球型/凸形 | 任意形狀 |
| 異常值處理 | 敏感（被拉偏） | 穩健（標記為噪聲） |
| 參數 | k（群數） | eps（鄰域半徑）, min_samples |

**考試判斷**：看到月牙形/環形/不規則分佈 → DBSCAN。看到球型分佈 → K-means。

---

## 串流 vs 批次處理

| | 批次 | 串流 |
|---|---|---|
| 關鍵字 | 排程、日報表、完整資料集 | 即時、低延遲、持續流入 |
| 延遲 | 分鐘~小時 | 毫秒~秒 |
| 工具 | Hadoop MapReduce, Spark Batch | Kafka, Spark Streaming, Flink |
| 場景 | 歷史分析、月報 | 即時推薦、詐騙偵測、IoT |

---

## 差分隱私

- **核心**：查詢結果加隨機噪音，讓攻擊者無法判斷某人是否在資料集中。
- **epsilon**：隱私預算。epsilon 越小 → 噪音越大 → 隱私越強 → 可用性越低。
- **不是加密**：差分隱私是加噪音，不是加密資料。

---

## 數據可視化速查

| 資料類型 | 推薦圖表 |
|---|---|
| 連續 vs 連續 | 散佈圖（scatter） |
| 類別 vs 連續 | 箱型圖（box）/ 長條圖（bar） |
| 頻率分佈 | 直方圖（histogram） |
| 時間序列 | 折線圖（line） |
| 類別占比 | 圓餅圖（pie）/ 堆疊長條 |

---

## Python 程式題速查

### 常見 API 模式

```python
# Z-score
z = (x - np.mean(x)) / np.std(x)          # 母體 std
z = (x - np.mean(x)) / np.std(x, ddof=1)  # 樣本 std

# IQR
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

# PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)
# X_pca.shape = (n_samples, 3)
# pca.explained_variance_ratio_ = 每個 PC 的比例

# ROC / AUC
from sklearn.metrics import roc_curve, roc_auc_score
fpr, tpr, thresholds = roc_curve(y_true, y_score)
auc = roc_auc_score(y_true, y_score)

# CIFAR-10
from tensorflow.keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
# x_train.shape = (50000, 32, 32, 3)
x_train = x_train.astype('float32') / 255.0  # 正規化到 [0,1]
```

### Python 四大陷阱

| 陷阱 | 說明 | 正確做法 |
|---|---|---|
| **shape** | (50000,32,32,3) 第一個是樣本數不是維度 | 先 print shape 確認 |
| **axis** | axis=0 沿列（向下），axis=1 沿行（向右） | 0=跨樣本，1=跨特徵 |
| **dtype** | 整數/255=0，要除 255.0 | astype('float32') 再除 |
| **np.std** | 預設母體 std（除 N），ddof=1 才是樣本 std | 看清題目要求 |

---

## 易混淆概念速查

| 概念 A | 概念 B | 一句話區分 |
|---|---|---|
| Z-score 標準化 | Min-Max 正規化 | Z-score 用 mu/sigma → 均值 0 標準差 1；Min-Max → [0,1] |
| 母體 std（/N） | 樣本 std（/N-1） | np.std 預設母體，加 ddof=1 才是樣本 |
| t 檢定 | F 檢定 | t 比兩組，F 比三組以上 |
| 卡方適合度 | 卡方獨立性 | 適合度：一個變數 vs 期望。獨立性：兩個變數是否獨立 |
| 正偏（右偏） | 負偏（左偏） | 右偏：尾巴在右、Mean > Median。左偏反之 |
| 批次處理 | 串流處理 | 批次=排程+完整，串流=即時+持續 |
| PCA | t-SNE | PCA 線性降維（可逆），t-SNE 非線性（不可逆、只做可視化） |
| 差分隱私 | 加密 | 差分隱私=加噪音，加密=密碼學轉換 |

---

## 收斂金句

> 「Z-score 問標準差、IQR 問四分位、檢定問比什麼、PCA 問解釋量、ROC 問 AUC——五個問題框架能解大部分科目2 考題。統計給你判斷工具，大數據給你分析場景，Python 給你實作能力。」
