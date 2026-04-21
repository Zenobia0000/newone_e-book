# Ch09 · MVK 考前速查卡（Minimum Viable Knowledge）

> 離開本節後，你的記憶裡必須長出「演算法選型地圖 + 深度學習架構辨識 + 激活函數三條規則」。
> 對應 01_outline.md 的 6 個 Learning Objectives。
> 本章的核心判斷：**演算法不用全背，但必須知道每個的定位——考試考的是選型判斷力。**

---

## 1 ML 演算法選型速查表（對應 LO1）

### 監督式學習 — 迴歸

| 演算法 | 一句話定位 | 適用場景 | 不適用場景 |
|-------|-----------|---------|-----------|
| Linear Regression | 假設線性關係，最簡單的迴歸 | 特徵與目標近似線性 | 非線性關係、高維特徵 |

### 監督式學習 — 分類

| 演算法 | 一句話定位 | 適用場景 | 不適用場景 |
|-------|-----------|---------|-----------|
| Logistic Regression | Sigmoid 輸出機率，線性決策邊界 | 二元分類、需要機率輸出、可解釋 | 非線性邊界 |
| Decision Tree | 規則分裂 if-else，高解釋性 | 需要可視化規則、小資料 | 容易 overfit |
| Random Forest | 多棵樹投票（Bagging），穩定 | 通用 baseline、中大型資料 | 需要極高解釋性 |
| SVM | 最大間隔超平面，kernel trick | 高維資料、中小型資料 | 大資料量（慢）|
| KNN | 最近 K 鄰居投票，懶學習 | 小資料、簡單場景 | 高維（維度詛咒）、大資料（預測慢）|

### 非監督式學習

| 演算法 | 一句話定位 | 適用場景 | 不適用場景 |
|-------|-----------|---------|-----------|
| K-means | 指定 K 個群心，迭代更新 | 球狀群集、已知群數 | 不規則形狀、有噪音 |
| DBSCAN | 密度分群，自動排除噪音 | 任意形狀群集、不知群數 | 密度差異大的群集 |
| PCA | 線性降維，保留最大變異 | 特徵太多、資料視覺化 | 非線性結構 |

**選型口訣**：
1. 有沒有 label → 監督 / 非監督
2. label 是數字還是類別 → 迴歸 / 分類
3. 資料特性（維度/量級/形狀）→ 具體演算法

---

## 2 R² 判定係數速查（對應 LO1）

```
R² = 1 - (SS_res / SS_tot)

SS_res = Σ(y_actual - y_predicted)²   # 殘差平方和
SS_tot = Σ(y_actual - y_mean)²        # 總變異平方和

R² = 1.0  → 完美預測（幾乎不可能，懷疑 leakage）
R² = 0.85 → 模型解釋了 85% 的變異（不是 85% 準確率！）
R² = 0.0  → 跟猜平均值一樣爛
R² < 0    → 比猜平均值還爛
```

**考試陷阱**：R² 不等於準確率（accuracy），它是迴歸指標不是分類指標。

---

## 3 深度學習架構速查（對應 LO3）

### CNN 經典架構三兄弟

| 架構 | 核心設計 | 一句話口訣 | 解決的問題 |
|------|---------|-----------|-----------|
| VGG | 3x3 小卷積核簡單堆疊 | 加深 | 證明深度有效 |
| Inception | 同層多尺度卷積並行(1x1/3x3/5x5) | 加寬不加深 | 多尺度特徵擷取 |
| ResNet | 殘差連接(skip connection) | 跳接 | 梯度消失 → 可訓練 100+ 層 |

### 其他架構

| 架構 | 任務 | 核心特色 |
|------|------|---------|
| R-CNN | 物件偵測（框+分類） | Region Proposal + CNN |
| RNN/LSTM | 序列資料（文字/時間序列） | 循環結構；LSTM 用 gate 解決梯度消失 |
| Transformer | NLP + CV 主流 | Self-Attention 可平行處理，取代 RNN |

**架構口訣**：「VGG 深、Inception 寬、ResNet 跳、R-CNN 框、RNN 序、Transformer 注意力」

---

## 4 激活函數速查（對應 LO4）

| 函數 | 公式 | 輸出範圍 | 使用位置 | 特點 |
|------|------|---------|---------|------|
| ReLU | max(0, x) | [0, +inf) | 隱藏層首選 | 計算快、緩解梯度消失、但有 Dead ReLU |
| Sigmoid | 1/(1+e^-x) | (0, 1) | 二元分類輸出層 | 輸出機率、梯度消失嚴重 |
| Softmax | e^xi / Σe^xj | (0, 1) 加總=1 | 多元分類輸出層 | 各類機率加總為 1 |
| Tanh | (e^x-e^-x)/(e^x+e^-x) | (-1, 1) | 偶爾用於隱藏層 | 中心化版 Sigmoid |

**三條必記規則**：
1. 隱藏層 → ReLU（不用想）
2. 二元分類輸出 → Sigmoid
3. 多元分類輸出 → Softmax

**為什麼隱藏層不用 Sigmoid？** → 梯度消失：Sigmoid 的梯度最大只有 0.25，多層連乘後趨近於 0。

---

## 5 前向傳播計算模板（對應 LO5）

```
前向傳播公式：
  Z = X · W + b       # 線性變換
  A = activation(Z)    # 非線性激活

維度規則：
  X: (batch_size, input_dim)
  W: (input_dim, output_dim)
  b: (output_dim,)
  Z: (batch_size, output_dim)
  A: (batch_size, output_dim)

手算範例：
  X = [2, 3]                    # (1, 2)
  W = [[0.5, -0.1],             # (2, 2)
       [0.3,  0.2]]
  b = [0.1, -0.2]

  Z[0] = 2×0.5 + 3×0.3 + 0.1 = 2.0
  Z[1] = 2×(-0.1) + 3×0.2 + (-0.2) = 0.2

  ReLU(2.0) = 2.0
  ReLU(0.2) = 0.2

  輸出 = [2.0, 0.2]
```

**考試口訣**：乘、加、激活。先看維度對不對齊。

---

## 6 優化器速查（對應 LO6）

| 優化器 | 學習率 | 核心特色 | 致命缺點 |
|-------|--------|---------|---------|
| SGD | 固定（手動設） | 最基本、概念直覺 | 容易卡 local minimum、需手動調 lr |
| Adagrad | 自適應（自動調） | 稀疏特徵友善 | 學習率持續衰減 → 後期停止學習 |
| Adam | 自適應 + 動量 | 收斂快、最常用預設 | 某些場景泛化不如 SGD+momentum |

**優化器口訣**：「SGD 手動、Adagrad 衰減、Adam 萬用」

---

## 7 K-means vs DBSCAN 速查（考試高頻對比）

| 比較項目 | K-means | DBSCAN |
|---------|---------|--------|
| 需要指定群數？ | 要（K） | 不要 |
| 群集形狀假設 | 球狀 | 任意形狀 |
| 對 outlier | 敏感（強制歸群） | 自動標記為噪音 |
| 需要的參數 | K | eps（鄰域半徑）, min_samples |
| 計算速度 | 快（O(n)） | 中（O(n log n)） |

---

## 8 sklearn API 速查（Python 程式題用）

```python
# 通用流程（所有演算法都一樣）
from sklearn.xxx import AlgorithmName

model = AlgorithmName(hyperparameters)
model.fit(X_train, y_train)          # 監督式
# model.fit(X)                       # 非監督式
y_pred = model.predict(X_test)
score = model.score(X_test, y_test)  # 監督式

# 常見 import
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score

# K-means 特殊用法
labels = model.fit_predict(X)        # fit + predict 一步完成
centroids = model.cluster_centers_   # 群心座標

# PCA 特殊用法
pca = PCA(n_components=0.95)         # 保留 95% 累積變異
X_reduced = pca.fit_transform(X_scaled)
pca.explained_variance_ratio_        # 各主成分解釋變異比例
```

---

## 9 MapReduce 速查（別漏了這個考點）

```
MapReduce 三步驟：
  1. Map：拆解大任務 → 每個節點各自處理自己的資料子集
  2. Shuffle：按 key 分組 → 相同 key 的結果送到同一個節點
  3. Reduce：合併結果 → 每個 key 的結果彙總成最終答案

範例：計算全校每科平均分
  Map：每班計算 {科目: (總分, 人數)}
  Shuffle：同科目的結果送到同一個 Reduce 節點
  Reduce：Σ總分 / Σ人數 = 平均分

考試重點：Map 和 Reduce 各做什麼、為什麼能分散式處理
```

---

## 10 Overfitting 速查（跨 Ch09 + Ch10 考點）

```
辨識：
  訓練集分數高 + 測試集分數低 = Overfitting
  兩者都低 = Underfitting

處理 Overfitting 五招：
  1. 增加訓練資料
  2. Regularization（L1 / L2）
  3. Dropout（深度學習專用）
  4. Early Stopping
  5. 簡化模型（減少層數/特徵）

處理 Underfitting 三招：
  1. 增加模型複雜度
  2. 增加特徵
  3. 減少 regularization
```

---

## 考前 30 分鐘最後掃描清單

- [ ] 演算法全景地圖畫得出來嗎？（監督/非監督 × 迴歸/分類/分群/降維）
- [ ] 每個演算法的一句話定位記得嗎？
- [ ] CNN 三架構口訣：VGG 深、Inception 寬、ResNet 跳
- [ ] 激活函數三規則：隱藏層 ReLU / 二分類 Sigmoid / 多分類 Softmax
- [ ] R² 的正確解讀（不是準確率！）
- [ ] 前向傳播計算：乘、加、激活
- [ ] 優化器：SGD 手動、Adagrad 衰減、Adam 萬用
- [ ] K-means vs DBSCAN 五個比較項
- [ ] sklearn API 流程：import → model → fit → predict → score
- [ ] MapReduce：Map 拆、Shuffle 分、Reduce 合
