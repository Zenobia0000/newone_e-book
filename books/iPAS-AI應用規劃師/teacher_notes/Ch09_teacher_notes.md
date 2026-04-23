# Ch09 — 機器學習演算法與深度學習｜講師講稿

> **課程時長**：2 小時（講授 80 min + 練習 25 min + QA 15 min）
> **受眾定位**：iPAS 中級科目3 考生，需掌握 ML 演算法選型邏輯與深度學習架構辨識
> **前置知識**：Ch08 機率統計與大數據處理分析
> **後續銜接**：Ch10 建模調參評估與 ML 治理
> **評鑑範圍**：中級 L231（機率統計ML基礎/線性代數ML基礎/數值優化）+ L232（ML原理與技術/常見ML演算法/深度學習原理與框架）

---

## 1. 本節目標 (Learning Objectives)

完成本節後，學員應能：

1. 區分常見 ML 演算法的適用場景，做出正確選型判斷（Linear/Logistic Regression, Decision Tree, Random Forest, SVM, KNN, K-means, DBSCAN）。
2. 說明 PCA 降維原理與變異解釋，判斷何時該用降維。
3. 描述 CNN 經典架構（Inception/ResNet/VGG/R-CNN）的核心差異與設計哲學。
4. 辨識激活函數特性與適用位置（ReLU/Sigmoid/Softmax/Tanh）。
5. 理解前向傳播的矩陣運算流程，能手算簡單範例。
6. 比較常見優化器（SGD/Adam/Adagrad）的特點與適用情境。

---

## 2. 時間切分表

```
00:00-00:08  開場：科目3 演算法題佔比分析 + 立論
00:08-00:25  ML 演算法全景地圖 + 迴歸/分類家族
00:25-00:35  演算法選型 Checkpoint + 非監督式
00:35-00:50  PCA 降維 + MapReduce + 配對練習
00:50-01:10  深度學習架構：CNN/RNN/Transformer + 激活函數
01:10-01:25  前向傳播矩陣運算 + 優化器比較
01:25-01:40  Python 程式題模擬 + Overfitting 跨章考點
01:40-01:55  收束金字塔 + 銜接 Ch10
01:55-02:00  QA
```

---

## 3. 關鍵教學點 (Key Teaching Points)

1. **選型判斷力是核心**：考試不會要你推導 SVM 的數學，但會給你一個場景問該用什麼演算法。每個演算法記住「一句話定位」和「適用/不適用場景」。

2. **演算法地圖先建骨架**：第一張概念圖把所有演算法分成「監督式-迴歸/分類」和「非監督式-分群/降維」兩大類。有了骨架，後面填細節才不會混亂。

3. **CNN 架構考設計哲學不考結構細節**：VGG=「簡單堆疊」、Inception=「加寬不加深」、ResNet=「殘差連接」。樣題直接考 Inception 的設計特色，不考 Inception 有幾層。

4. **激活函數考場景配對**：隱藏層用 ReLU、二元分類輸出用 Sigmoid、多元分類輸出用 Softmax。這三條規則能解大部分考題。

5. **矩陣乘法前向傳播要能手算**：樣題直接給矩陣要你算。用 2x3 × 3x2 的小例子走一遍，確認維度對齊規則 (m,n)×(n,p)=(m,p)。

6. **Python 程式題佔 25%**：重點是 sklearn API 呼叫流程：`model.fit(X_train, y_train)` → `model.predict(X_test)`。不考語法細節，考的是能不能讀懂程式碼在做什麼。

---

## 4. 學員常犯錯誤 (Common Pitfalls)

- **背公式不背定位**：能寫出 SVM 目標函數但不知道什麼時候該用 SVM。→ 每個演算法記住「一句話定位 + 適用場景 + 不適用場景」。
- **Sigmoid vs Softmax 混用**：二元分類輸出層用 Sigmoid（0-1 機率），多元分類用 Softmax（各類機率加總為 1）。
- **以為 Inception 是加深**：Inception 核心創新是同一層用不同大小卷積核並行（加寬），不是像 VGG 堆更多層（加深）。
- **忽略 MapReduce**：看起來不像 ML 但屬於 L231 評鑑範圍，歷屆樣題有考。
- **K-means 和 DBSCAN 搞混**：K-means 要預先指定 K、假設球狀群集；DBSCAN 不用指定 K、能找任意形狀、自動排除噪音。
- **Adagrad 和 Adam 搞混**：Adagrad 自適應但學習率會一直衰減趨近零；Adam 結合動量+自適應，是最常用的預設優化器。

---

## 5. 提問設計 (Discussion Prompts)

1. 你有一份電商客戶資料，想做客戶分群。你會選 K-means 還是 DBSCAN？如果群集形狀不規則呢？（預期答：規則形狀用 K-means，不規則用 DBSCAN。）

2. 一個 CNN 影像分類模型，最後一層應該用什麼激活函數？如果是 10 類分類呢？二元分類呢？（預期答：10 類用 Softmax，二元用 Sigmoid。）

3. 給你一個 2x3 的輸入矩陣和一個 3x1 的權重矩陣，請算出前向傳播的結果。（→ 現場手算練習）

4. MapReduce 的 Map 階段和 Reduce 階段各做什麼事？用「計算全班平均分」來舉例。（→ Map=每人算自己的分數和、Reduce=匯總全班。）

---

## 6. 延伸資源 (Further Reading)

- scikit-learn 演算法選擇流程圖（官方文件）：最經典的演算法選型參考
- 3Blue1Brown 的神經網路影片系列：前向傳播和反向傳播的直覺化解釋
- iPAS 中級科目3 學習指引：L231/L232 章節
- CS231n Convolutional Neural Networks for Visual Recognition：CNN 架構標準教材

---

## 7. 常見 Q&A

**Q1：演算法這麼多，考試真的不考公式嗎？**
A：幾乎不考。考的是「給你一個場景，你選哪個演算法、為什麼」以及「給你一個演算法名字，你知不知道它的特性」。唯一需要「算」的是簡單矩陣乘法和 R² 的解讀。

**Q2：深度學習的題目會很難嗎？**
A：不會考你實作 ResNet，但會考「Inception 的設計哲學」「RNN 適合什麼任務」「Transformer 為什麼能取代 RNN」。記住每個架構的一句話定位就夠。

**Q3：Python 程式題要準備到什麼程度？**
A：能讀懂 sklearn 基本流程：`import` → `model = Algorithm()` → `model.fit()` → `model.predict()` / `model.score()`。不需要寫完整程式，但要能判斷程式碼在做什麼。

**Q4：Adagrad 和 Adam 怎麼區分？**
A：Adagrad 根據歷史梯度自動調整學習率，但會一直衰減趨近零。Adam 結合動量+自適應學習率，是目前最常用的預設優化器。考試記住：Adagrad=「自適應但會衰減」，Adam=「最常用的預設選擇」。
