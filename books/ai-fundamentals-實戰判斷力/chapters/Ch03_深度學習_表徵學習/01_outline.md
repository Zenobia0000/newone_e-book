# Ch03 — 深度學習：從人工特徵到表徵學習｜講師講稿

> **課程時長**：2 小時（講授 75 min + 課堂練習 30 min + QA 15 min）
> **前置章節**：Ch02 機器學習——表格世界的主戰場

---

## 1. 本節目標 (Learning Objectives)

完成本節後，學員應能：

1. 用一句話解釋 tensor 是什麼，並說出 shape / dtype / device 的意義。
2. 畫出訓練循環五步（data → forward → loss → backward → update）並說明每一步做什麼。
3. 用直覺解釋 gradient、backpropagation、autograd 各自的角色。
4. 區分 batch / epoch / learning rate 對訓練的影響，並能讀懂 loss curve。
5. 說明 representation learning 的意義，以及 CNN / RNN / Transformer 各自解決什麼類型的問題。
6. 解釋 embedding 為什麼重要，以及它在現代 AI pipeline 中的角色。

---

## 2. 時間切分表

```
00:00-00:08  開場暖身：Ch02 回顧（ML 的特徵工程到底多累）＋ 為什麼需要 DL
00:08-00:20  核心觀念 1/4：tensor 直覺 + shape/dtype/device
00:20-00:40  核心觀念 2/4：訓練循環五步 + model/loss/optimizer 三件套
00:40-00:55  核心觀念 3/4：gradient / backprop / autograd 直覺 + batch/epoch/lr
00:55-01:10  核心觀念 4/4：representation learning + CNN/RNN/Transformer 選型 + embedding
01:10-01:15  實務 Case：三組 loss curve 判讀
01:15-01:30  實務 Case：三個業務情境架構選型
01:30-01:45  課堂練習（15 min）：loss curve 診斷 + 架構選型
01:45-02:00  QA + 下節預告（Ch04 生成式 AI 系統工程）
```

---

## 3. 關鍵教學點 (Key Teaching Points)

1. **從 ML 的痛點切入**：Ch02 學了特徵工程，學員應該體會到「手工設計特徵很累且有天花板」。用 ImageNet 2012 的數據（手工 73% → AlexNet 85%）讓學員感受到 DL 的突破不是數學更難，而是讓模型自己學特徵。

2. **訓練循環是一切的骨架**：不要讓學員被 CNN/RNN/Transformer 的名詞淹沒。先把 data → forward → loss → backward → update 這五步跑通，讓他們知道「不管什麼架構，訓練循環都是同一套」。PyTorch 官方就把 workflow 定義為 data → model → optimize → save。

3. **梯度的直覺比公式重要**：gradient 想成「方向盤」——告訴你參數該往哪邊修、修多少。backprop 就是沿著計算圖反向把方向盤傳回去。autograd 是 PyTorch 幫你自動算的引擎。不用背 chain rule 的數學，但要知道這三個角色的分工。

4. **loss curve 是你的儀表板**：學會讀 loss curve 比學會調參數更重要。train_loss 降 + val_loss 降 = 正常收斂；train_loss 降 + val_loss 升 = overfitting；兩個都不動 = underfitting 或 lr 太小。這是判斷「問題出在哪」的第一張牌。

5. **三大架構不是互相取代**：CNN 解空間結構（圖片、醫療影像）、RNN 解序列依賴（時間序列、語音）、Transformer 解長距離關聯（語言、多模態）。強調「選架構 = 看你的資料結構」，不是追潮流。

6. **embedding 是現代 AI 的通用語言**：從 one-hot（稀疏、無語意）到 embedding（密集、有語意距離），這是搜尋、推薦、RAG 能 work 的基礎。在 Ch04 生成式 AI 中會大量用到。

---

## 4. 學員常犯錯誤 (Common Pitfalls)

- **把 DL 當成選架構名詞套上去**：看到影像就喊 CNN、看到文字就喊 Transformer，但忽略 data pipeline 品質、標註一致性、訓練超參數設定。架構只是骨架，資料和訓練設定才是肉。
- **loss 下降就以為模型在學**：只看 train_loss 不看 val_loss，結果 overfitting 了還在加 epoch。務必在 loss curve demo 時讓學員看到 train/val 分叉的經典圖。
- **learning rate 沒調好就怪模型**：lr 太大 loss 爆炸震盪，lr 太小 loss 平坦不動。建議先用 lr=1e-3 當起點，再根據 loss curve 微調。
- **以為 CNN/RNN/Transformer 是進化關係**：Transformer 不是「比 CNN 好」，是解決不同問題。很多產線上的影像模型仍然用 CNN，因為夠快夠好。

---

## 5. 提問設計 (Discussion Prompts)

1. 如果你要做一個醫療影像分類系統，你會選 CNN 還是 Transformer？為什麼？有什麼 trade-off？
2. 你在訓練一個模型，train_loss 持續下降但 val_loss 在第 10 個 epoch 開始上升。你會怎麼做？你會調整哪些旋鈕？
3. embedding 讓「國王 - 男人 + 女人 = 皇后」成為可能。這代表 embedding 捕捉到了什麼？它在搜尋引擎或推薦系統中能怎麼用？

---

## 6. 延伸資源 (Further Reading)

- PyTorch 官方 Tutorial：Learn the Basics — Tensors / Build Model / Autograd / Optimization（pytorch.org/tutorials）
- 3Blue1Brown《But what is a neural network?》系列影片（YouTube，視覺化 gradient 與 backprop 極佳）
- Google ML Crash Course (2025)：Training Neural Nets 章節

---

## 7. 常見 Q&A

**Q1：一定要學數學才能懂深度學習嗎？**
A：不用先背數學。你需要的是「直覺」：gradient 是方向盤、loss 是評分表、backprop 是把評分回傳給每個參數。能讀懂 loss curve、能判斷 overfitting，比手推 chain rule 重要 100 倍。

**Q2：CNN 不是被 Transformer 淘汰了嗎？**
A：沒有。Transformer 在 NLP 領域碾壓了 RNN，在 Vision 領域（ViT）也有進展，但 CNN 在邊緣裝置、即時影像、醫療影像等場景仍然大量使用——因為它更輕、推論更快。選架構看場景，不是看潮流。

**Q3：什麼時候應該用 DL 而不是 ML？**
A：當你的資料是非結構化的（圖片、文字、語音、影片），或者手工特徵已經到天花板時，DL 是更好的選擇。但如果你的資料是結構化表格、樣本量不大、需要可解釋性，ML（Ch02 的 tree-based models）往往更實用。

**Q4：embedding 跟 feature engineering 有什麼關係？**
A：embedding 本質上就是「自動化的特徵工程」。傳統 ML 你手動設計特徵；DL 用 embedding 層讓模型自己學出最適合下游任務的特徵表示。這也是為什麼 Ch03 的副標題是「表徵學習」。
