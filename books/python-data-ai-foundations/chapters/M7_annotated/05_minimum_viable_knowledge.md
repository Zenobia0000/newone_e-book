# M7 Minimum Viable Knowledge（速學卡）

> **文件定位**：M7 模組的「最小可行知識」速學卡。面向時間有限、但要能在內部技術討論會上不露怯的工程師（例如從後端 / 前端 / infra 轉入資料/AI 相關會議的同仁）。每張卡一個知識點、一面 Q 一面 A、3 分鐘內可讀完。
>
> **使用方式**：(1) 會議前翻一次；(2) 教材回顧；(3) 新人上任第一週的 onboarding handout。
>
> **語氣**：內部 review、直接、去廢話。繁體中文、台灣業界用語。
> **日期**：2026-04-14。

---

## 速學卡 #01 — ML 一句話定義

**Q**：機器學習到底在做什麼？

**A**
ML = 從一堆 $(X, y)$ 樣本裡找一個函數 $\hat f$，讓 $\hat f(X) \approx y$，而且對沒看過的資料也要接近。
- **訓練**：從資料更新模型參數
- **泛化**：對新資料也要準
- **損失**：衡量「接近」的量尺
- **不是魔法**：只是在函數空間裡做最佳化

**一句金句**：Pattern in → function out → prediction on unseen data.

---

## 速學卡 #02 — train / val / test 三分割

**Q**：為什麼不能只切 train / test 兩份？

**A**
因為你**需要一個可以反覆用來調模型的資料**——那就是 val（驗證集）。
- **train**：給模型學、更新參數
- **val**：調超參數、選模型、early stopping
- **test**：**一輩子只動一次**，是對外報數字的真實檢驗

常見比例：60/20/20 或 70/15/15。用 test 調模型 = 考試前偷看答案，整個評估作廢。

**旗語**：看到「用 test set 選模型」直接打叉。

---

## 速學卡 #03 — Data Leakage 四種形式

**Q**：哪些操作會讓模型看起來很好、上線崩盤？

**A**
1. **預處理 leakage**：`StandardScaler.fit(全資料)` 再切 → 測試集統計滲透
2. **時間 leakage**：時序資料用隨機 split，未來資料被用來預測過去
3. **target leakage**：X 裡有目標的代理變數（預測流失時放「退費金額」）
4. **group leakage**：同一客戶多筆記錄被拆進 train/test，用 `GroupKFold` 解

**心法**：每做一次特徵工程，問自己——「這個特徵在預測時點真的拿得到嗎？」

---

## 速學卡 #04 — scikit-learn Estimator API 哲學

**Q**：為什麼所有 sklearn 模型用法都長得很像？

**A**
不是巧合，是**設計哲學**。所有 estimator 遵守：
- `__init__`：收所有超參數、**不碰資料**
- `.fit(X, y)`：學、改變自身狀態
- `.predict(X)` / `.transform(X)`：用、不改狀態
- `get_params` / `set_params`：讓 GridSearchCV 能通用
- 靠 `BaseEstimator` + 各種 `Mixin` 組合

**結果**：Pipeline、ColumnTransformer、GridSearchCV 之所以能無縫串接，都是因為這個契約。學一個 = 會一百個。

---

## 速學卡 #05 — Cross-Validation 五種常見切法

**Q**：CV 有幾種？什麼時候用哪種？

**A**

| 切法 | 用在哪 |
|---|---|
| `KFold` | 一般獨立同分布 |
| `StratifiedKFold` | 分類、類別不平衡 |
| `GroupKFold` | 同群樣本不能跨 fold（病人/客戶/session） |
| `TimeSeriesSplit` | 時序，train 永遠在 test 之前 |
| `RepeatedKFold` | 資料少、降單次 split 隨機性 |

**口訣**：「時間時序、分類 stratify、同群 group、小資料 repeat」。

---

## 速學卡 #06 — tensor vs ndarray 的三個差別

**Q**：PyTorch tensor 跟 NumPy ndarray 差在哪？

**A**
tensor = ndarray + **三件事**：
1. **device**：可以 `.to("cuda")` / `.to("mps")`
2. **autograd**：`requires_grad=True` 可追蹤計算圖反傳梯度
3. **dtype 政策**：DL 預設 `float32`（甚至 `bfloat16`），NumPy 預設 `float64`

看到 `RuntimeError: expected scalar type Float but found Double`——就是 dtype 不合，強制 `.float()` 或在資料端轉 `astype(np.float32)`。

---

## 速學卡 #07 — PyTorch 訓練迴圈六行

**Q**：最小可行訓練迴圈長什麼樣？

**A**

```python
for x, y in dataloader:
    pred = model(x)                # 1. forward
    loss = loss_fn(pred, y)        # 2. loss
    optimizer.zero_grad()          # 3. 清上一步的 .grad
    loss.backward()                # 4. autograd 沿 tape 填 .grad
    optimizer.step()               # 5. 用 .grad 更新參數
    logger.log(loss.item())        # 6. 記錄
```

**記憶要點**：
- `zero_grad` 忘了 → 梯度累積、訓練爆炸
- `backward` 不更新參數、`step` 才更新
- `loss.item()` 取 Python float，避免保留 tape

---

## 速學卡 #08 — torch.compile 是什麼

**Q**：PyTorch 2.x 最大的新東西是什麼？

**A**
`torch.compile(model)` 一行，把 eager 模型用 graph 編譯加速：
- 背後：TorchDynamo（抓 Python bytecode）+ AOTAutograd（算反向圖）+ Inductor（產 GPU kernel）
- 典型加速：Transformer backbone 30–200%，但有 recompile cost 和 dynamic shape 限制
- **不是免費加速**：有控制流的模型可能 fallback 或編譯失敗

**一句話**：開發體驗像 eager、執行效能像 graph。

---

## 速學卡 #09 — GPU 效能三個關鍵旋鈕

**Q**：PyTorch 在 GPU 上跑慢，先看哪三個旋鈕？

**A**
1. **混合精度**：`torch.autocast(device_type="cuda", dtype=torch.bfloat16)` + `GradScaler`（fp16 時）
2. **DataLoader**：`num_workers > 0`、`pin_memory=True`、`persistent_workers=True`
3. **非同步傳輸**：`tensor.to(device, non_blocking=True)`

量時間要 `torch.cuda.synchronize()`，不 sync 量到的都是假的（kernel 非同步）。

---

## 速學卡 #10 — pandas 的邊界

**Q**：pandas 幾 GB 就該換工具？

**A**
粗略：DataFrame 吃記憶體 30–50% 就該警覺。
- **< 1 GB**：pandas（2.0+ 啟 Arrow backend 更快）
- **1–100 GB（單機）**：Polars（lazy）或 DuckDB（SQL on Parquet）
- **100 GB+ 或 Lakehouse**：PySpark

**心法**：工具選擇不是品味，是**尺寸**。

---

## 速學卡 #11 — PySpark lazy + DAG + shuffle

**Q**：學 PySpark 第一件事要懂什麼？

**A**
三件事：
1. **lazy**：transformation（`filter` / `select` / `groupBy`）不跑，action（`show` / `write` / `count`）才跑
2. **DAG**：Catalyst 把你的指令組成執行計畫，用 `df.explain(mode="formatted")` 讀
3. **shuffle**：跨 executor 重新分派資料，比 narrow op 貴 100–1000 倍；`groupBy` / `join` / `orderBy` 都會觸發

**第一個優化**：小表用 `broadcast(df_small)` 做 broadcast join，避免 shuffle。

---

## 速學卡 #12 — overfitting / underfitting 診斷

**Q**：看到 train / test score 差距怎麼解讀？

**A**

| train | test | 狀態 | 下一步 |
|---|---|---|---|
| 高 | 高 | 健康 | 部署 / 繼續迭代 |
| 高 | 低 | overfit | regularization、減容量、加資料、early stopping |
| 低 | 低 | underfit | 加容量、換模型、補特徵 |
| 低 | 高 | 罕見 | 通常是 test 太小或 leakage 反向，查資料 |

**延伸工具**：learning curve（看訓練/驗證分數 vs 資料量）判斷該補資料還補模型。

---

## 速學卡 #13 — RAG 的真實痛點

**Q**：RAG 做不好，先檢查哪裡？

**A**
**不是 LLM，是 retrieval。** 按優先序檢查：
1. **chunking**：固定長度往往太蠢，試 semantic / hierarchical
2. **embedding 模型**：多語言場景用多語言模型，domain 特殊就 fine-tune
3. **hybrid search**：BM25（關鍵字）+ vector（語意）幾乎永遠贏純 vector
4. **reranking**：cross-encoder 重排前 K 個結果，recall → precision 的關鍵一步
5. **prompt**：做完上面 4 步再調 prompt

**經驗法則**：RAG 八成的效能問題是 retrieval，LLM 只是放大器。

---

## 速學卡 #14 — 五條路線的一句話選擇

**Q**：我該選哪條路？

**A**
用「你最常問什麼問題」對照：

| 你最常問 | 路線 |
|---|---|
| 為什麼結果是這樣？這個差異有意義嗎？ | Route A 統計 |
| 能不能預測更準？能不能部署上線？ | Route B ML 工程 |
| 機器怎麼看懂圖 / 語言？ | Route C 深度學習 |
| 資料怎麼可靠地從 A 流到 B？ | Route D 資料工程 |
| 怎麼讓 AI 幫我完成任務？ | Route E LLM 應用 |

**不是終身承諾，是 30 天承諾**——選一條、走 30 天、做出一個能放 portfolio 的 artifact、再回來評估。

---

## 速學卡 #15 — 最終心法

**Q**：走完 M7 要帶走哪一句話？

**A**

> **先會寫，再會組；
> 先懂資料，再懂系統；
> 先搭底盤，再碰 AI。**

工具會換（scikit-learn → 什麼都可能）、框架會改版（PyTorch 2 → n）、API 會汰換（OpenAI 的 schema 半年一變）。
但資料思維、系統直覺、程式設計能力**不會換**——你在 24 小時學的就是那個不換的部分。

> **You didn't learn a tool. You built a foundation.**

---

## 速學卡索引（快速查找）

| # | 主題 | Pillar / Route |
|---|---|---|
| 01 | ML 一句話定義 | Pillar 1 |
| 02 | train/val/test 三分割 | Pillar 1 |
| 03 | Data Leakage 四形式 | Pillar 1 |
| 04 | sklearn Estimator API | Pillar 1 / Route B |
| 05 | CV 五種切法 | Pillar 1 / Route B |
| 06 | tensor vs ndarray | Pillar 2 |
| 07 | PyTorch 訓練迴圈六行 | Pillar 2 / Route C |
| 08 | torch.compile | Pillar 2 / Route C |
| 09 | GPU 效能三旋鈕 | Pillar 2 / Route C |
| 10 | pandas 邊界 | Pillar 3 |
| 11 | PySpark lazy/DAG/shuffle | Pillar 3 / Route D |
| 12 | overfit/underfit 診斷 | Pillar 1 |
| 13 | RAG 痛點 | Route E |
| 14 | 五條路線選擇 | 全 |
| 15 | 最終心法 | 全 |

— end of minimum viable knowledge —
