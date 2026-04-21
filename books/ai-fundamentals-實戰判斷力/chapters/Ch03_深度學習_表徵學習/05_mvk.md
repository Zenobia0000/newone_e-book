# Ch03 · MVK 速學卡（Minimum Viable Knowledge）

> 離開本節後，你的肌肉記憶裡必須長出這四個反射。
> 對應 01_outline.md 的 6 個 Learning Objectives。

---

## ① tensor 直覺（對應 LO1）

```python
import torch
t = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
t.shape    # torch.Size([2, 2])  ← 形狀
t.dtype    # torch.float32       ← 精度
t.device   # device(type='cpu')  ← 跑在哪裡
```

**心智模型**：tensor = 有形狀的數字容器。跟 NumPy ndarray 幾乎一樣，但多了 autograd（自動記錄運算、自動算梯度）。

**常見 shape 直覺**：
- `(3, 224, 224)` = 一張彩色圖片（3 通道 x 224 x 224 像素）
- `(32, 3, 224, 224)` = 一個 batch 32 張彩色圖片
- `(16, 128)` = 一個 batch 16 筆資料，每筆 128 維特徵

---

## ② 訓練循環五步（對應 LO2 + LO3）

```
Data Loader  →  Forward  →  Loss  →  Backward  →  Update
 (切batch)    (model(x))  (算誤差)  (算梯度)    (改參數)
     ↑                                              |
     └──────────────── 重複到收斂 ──────────────────┘
```

**PyTorch 對應程式碼**（不用背，但要能讀懂）：

```python
for epoch in range(num_epochs):          # 整個資料集看幾遍
    for X, y in dataloader:              # 每次一個 batch
        pred = model(X)                  # Forward
        loss = loss_fn(pred, y)          # Loss
        loss.backward()                  # Backward（autograd 算梯度）
        optimizer.step()                 # Update（根據梯度改參數）
        optimizer.zero_grad()            # 清掉梯度，準備下一輪
```

**三個角色分工**：
- **gradient**（方向盤）：告訴你每個參數該往哪邊修、修多大
- **backpropagation**（chain rule）：從 loss 一路回推到每個參數的梯度
- **autograd**（自動引擎）：PyTorch 幫你自動完成上面兩件事

---

## ③ CNN / RNN / Transformer 選型（對應 LO5）

| 架構 | 擅長問題 | 資料結構 | 典型場景 |
|------|---------|---------|---------|
| CNN | 空間結構 | 圖片、影像 | 醫療影像、衛星圖、物件偵測 |
| RNN | 序列依賴 | 時間序列、短文本 | 感測器、股價（短序列） |
| Transformer | 長距離關聯 | 語言、多模態 | 翻譯、聊天、搜尋、RAG |

**一句口訣**：CNN 看局部、RNN 看順序、Transformer 看全局。選架構 = 看資料結構，不是追潮流。

**representation learning 的核心**：DL 不用人先把特徵寫死，讓多層網路自己從原始資料學出越來越抽象的表徵。這才是深度學習最核心的價值。

---

## ④ loss curve 判讀（對應 LO4）

| 現象 | 診斷 | 行動 |
|------|------|------|
| train 降 + val 降 | 正常收斂 | 繼續訓練或 early stop |
| train 降 + val 升 | Overfitting | early stop / 加 data / regularization |
| 兩條都平 | Underfitting 或 lr 太小 | 加大模型 / 調高 lr |
| train 劇烈震盪 | lr 太大 | 降低 lr |

**三個旋鈕**：
- `batch_size`：一次看多少筆（起手 32 或 64）
- `epoch`：看幾遍（看 loss curve 決定何時停）
- `learning_rate`：每步修多大（起手 1e-3）

**判斷流程**：看到問題先問三件事 → 是資料問題（標註品質差）？模型問題（太小或太大）？還是訓練設定問題（lr / batch / epoch）？

---

## ⑤ embedding 為什麼重要（對應 LO6）

```
one-hot:    [0, 0, 0, 1, 0, ..., 0]   → 10000 維、稀疏、沒有語意距離
embedding:  [0.23, -0.45, 0.78, ...]   → 128 維、密集、有語意距離
```

**關鍵差異**：
- one-hot 裡 cat 和 dog 的距離 = cat 和 pizza 的距離（都一樣遠）
- embedding 裡 cat 和 dog 靠近、cat 和 pizza 遠離（有語意）

**為什麼重要**：embedding 讓離散的東西（文字 / 商品 / 用戶）變成可以算距離的向量。這是搜尋引擎、推薦系統、RAG 能 work 的基石。Ch04 的生成式 AI 大量依賴 embedding。

---

## 四個必踩地雷（考前必背）

| # | 地雷 | 錯誤直覺 | 正確判斷 |
|---|------|---------|---------|
| P1 | 只看架構名詞 | 「用 Transformer 因為最新」 | 先看資料品質、再選架構、再調訓練 |
| P2 | 只看 train_loss | 「loss 0.01 超棒！」 | 同時看 val_loss，差距比絕對值重要 |
| P3 | lr 沒調好 | 「模型不行換一個」 | 先用 1e-3，看 loss curve 再調 |
| P4 | 架構進化論 | 「Transformer 取代了 CNN」 | CNN/RNN/Transformer 各有擅場 |

---

## 下一章銜接（Ch04 生成式 AI）

> Transformer 產出的 embedding 是生成式 AI 的燃料——
> prompt engineering 靠 token embedding 理解意圖；
> RAG 靠 embedding 搜尋找到相關知識；
> tool use 和 agent 靠模型的表徵理解來決定行動。
>
> **今天的訓練機制直覺，是明天理解生成式 AI 系統的地基。**
