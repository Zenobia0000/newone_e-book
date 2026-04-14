# M7 Three-Lens Analysis（三透鏡分析）

> **文件定位**：這份文件用三個透鏡重新審視 M7 模組——(1) First Principles（從物理/數學/資訊理論的本質重寫一次）、(2) Fundamentals（三領域入門 checklist）、(3) BoK（對齊 ACM Data Science BoK 與 MLOps BoK）。最後收束為「合流建議」：把 ML / DL / Big Data 的教學順序用 BoK 重新校準。
>
> **面向 reviewer**：資深架構師、教學設計負責人、課綱委員會。
> **語氣**：內部 review。不解釋常識，直接對位。
> **日期**：2026-04-14。

---

## 透鏡一：First Principles

把 M7 涵蓋的三個領域——ML、DL、Big Data——還原成各自最少的本質陳述。教材如果不能在這三句話上站穩，後面的技術堆疊就是積木堆在沙上。

### 1.1 ML = 從資料學到函數近似

**一句話定義**
給定分布未知的 $(X, y) \sim \mathcal{D}$，從假設空間 $\mathcal{H}$ 裡找到一個函數 $\hat f \in \mathcal{H}$，使得期望風險 $\mathbb{E}_{(X,y) \sim \mathcal{D}}[L(\hat f(X), y)]$ 最小。

**本質拆解**
| 成分 | 物件 | 工程意義 |
|---|---|---|
| 資料分布 $\mathcal{D}$ | 未知 | 只能用樣本逼近；泛化能力的根 |
| 假設空間 $\mathcal{H}$ | 模型族 | 線性模型、樹、神經網路都是不同的 $\mathcal{H}$ |
| 損失 $L$ | 優化目標 | MSE / cross-entropy 是我們對「好」的操作定義 |
| 期望風險 → 經驗風險 | 無限 → 有限 | train/val/test 切割就是在管理這個差 |
| 優化器 | 學習算法 | GD / Adam / LBFGS 都是在走 $\mathcal{H}$ 的參數空間 |

**教材對應**
- S02「函數逼近」：正確對上這個本質
- S03「監督式一張圖」：是在教 empirical risk 的資料管理
- S05「工作流」：是在教泛化誤差的診斷循環
- **未出現但應該出現**：bias-variance tradeoff、generalization bound 的直覺（不需要數學，但心智模型必要）

**First Principle 判準**
> 如果學員不能回答「為什麼 test set 表現比 train set 差是正常的」，就代表 ML 的第一性原理沒建立起來。

---

### 1.2 DL = 可微分程式（Differentiable Programming）

**一句話定義**
把模型寫成一個**由可微分運算子組成的計算圖** $f_\theta(x)$，用反向傳播算梯度 $\nabla_\theta L$，用梯度下降更新參數 $\theta \leftarrow \theta - \eta \nabla_\theta L$。

**本質拆解**
DL 相對於傳統 ML 的三個本質差異：
1. **參數化是多層函數組合**：$f_\theta = f_L \circ f_{L-1} \circ \dots \circ f_1$，每層都是可微分的
2. **特徵是學出來的，不是設計的**：representation learning 取代 feature engineering
3. **優化在高維非凸空間**：不保證收斂到全局最小，但實務上夠用（loss landscape 有大量平坦低點）

**為什麼「可微分程式」這個框架比「神經網路」更精準**
- JAX / PyTorch 的設計哲學就是「任何可微分的東西都能 train」
- 物理模擬、可微渲染、可微邏輯推理都是這個框架的延伸
- `torch.compile()` 的存在說明這個框架已經把 DL 推向「一門新的程式語言」，不只是「一種模型」

**教材對應**
- S07「DL 順理成章」：正確地把 DL 建在 NumPy tensor 的底座上
- S08「PyTorch 2.0」：正確地把 DL 拉到「效能工程 / 程式語言」的層次
- **未出現但應該出現**：自動微分（forward vs reverse mode）的直覺、計算圖（static vs dynamic）的分野、device / dtype / autograd tape 作為 tensor 的「三個附加屬性」

**First Principle 判準**
> 如果學員只能寫 `model.fit()`，不能解釋 `loss.backward()` 在做什麼，代表 DL 的第一性原理沒建立。

---

### 1.3 大數據 = 資料分散 + 計算分散

**一句話定義**
當資料量或計算量超出單機能力，用**分片（partition）+ 協調（coordination）+ 容錯（fault tolerance）** 三個機制，在多台機器上完成原本單機的工作。

**本質拆解**
| 維度 | 單機 | 分散式 |
|---|---|---|
| 資料 | 全部在 RAM / 本地磁碟 | 分片到多節點（HDFS / S3 / GCS） |
| 計算 | 一個進程的多 thread | 多節點多進程（executor） |
| 協調 | OS scheduler | cluster manager（YARN / K8s / Mesos） |
| 失敗 | 進程 crash = 工作失敗 | 某節點 crash = 重新排程那塊 task |
| 延遲 | ns–μs | ms–s（網路 + 序列化主導） |

**為什麼這是**真正**的分野，不是「pandas 大一點」**
- 單機的前提是**資料可以全放進 RAM**，算法可以假設隨機存取是 O(1)
- 分散式的前提是**資料必須分片**，算法必須在「local compute + network shuffle」這個 primitive 上重寫
- 所有「GroupBy / Join / Sort」在分散式下都是 shuffle-heavy 操作，cost model 完全不同

**教材對應**
- S09「pandas 邊界」：正確地把尺寸當作工程判斷依據
- S10「PySpark 橋樑」：正確地把 lazy + 分散式當作兩個獨立維度
- **未出現但應該出現**：CAP / PACELC 的極簡直覺（不必深講，但要知道「分散式一定要取捨」）、shuffle 作為 cost 主導項、storage-compute 分離（Lakehouse 架構）

**First Principle 判準**
> 如果學員不能解釋「為什麼同一個 groupBy 在 pandas 幾秒、在 Spark 幾分鐘」，代表大數據的第一性原理沒建立。

---

## 透鏡二：Fundamentals（三領域入門 checklist）

這是一份內部 review 會用來檢查「學員走完 M7 後算不算入門」的清單。不是進階，只是**能不能合格地說自己入門了**。

### 2.1 ML 入門 checklist（Route A/B 前置）

- [ ] 能用自己的話定義 feature / target / train / val / test
- [ ] 能解釋「為什麼 test set 只能動一次」
- [ ] 知道 data leakage 的三種形式並能各舉一例
- [ ] 會用 `train_test_split` 並正確使用 `stratify` 與 `random_state`
- [ ] 會至少三種 CV（KFold / StratifiedKFold / TimeSeriesSplit）及其適用情境
- [ ] 能在 `classification_report` 看出 precision / recall / f1 的差異含義
- [ ] 會畫 confusion matrix 並能解讀 false positive / false negative 的業務意義
- [ ] 理解 bias-variance tradeoff（不必懂公式，要有直覺）
- [ ] 會用 `Pipeline` + `ColumnTransformer` 把前處理與模型組起來
- [ ] 能解釋 overfitting / underfitting 在 learning curve 上的形狀
- [ ] 知道至少一個 tree-based 模型（RandomForest / XGBoost）與線性模型的選擇情境

### 2.2 DL 入門 checklist（Route C 前置）

- [ ] 能解釋 tensor 相對 ndarray 多了哪三件事（device / grad / dtype）
- [ ] 會建立 `requires_grad=True` 的 tensor，知道什麼是 leaf tensor
- [ ] 能描述 forward / backward 兩階段各自在做什麼
- [ ] 理解 `loss.backward()` 只填 `.grad`，不更新參數；`optimizer.step()` 才更新
- [ ] 會用 `optimizer.zero_grad()` 並能解釋為什麼要清零
- [ ] 能寫出最小訓練迴圈的六行（forward / loss / zero_grad / backward / step / log）
- [ ] 知道 `torch.no_grad()` 和 `.eval()` 的差異與各自用途
- [ ] 會把 tensor 和 model 搬到 GPU，且理解 `.to(device)` 不是 in-place
- [ ] 理解 DataLoader 的 `num_workers` / `pin_memory` / `shuffle` 三個參數各自做什麼
- [ ] 會用 TensorBoard 或 wandb 追蹤 training loss
- [ ] 知道 `torch.compile()` 的基本使用與適用邊界

### 2.3 Big Data 入門 checklist（Route D 前置）

- [ ] 能用規模（MB / GB / TB）選出合適的工具
- [ ] 會寫 SQL（SELECT / JOIN / GROUP BY / WINDOW）
- [ ] 理解 lazy vs eager 的差異並能舉 Polars / Spark 的例子
- [ ] 會讀 Spark 的 `explain()` 執行計畫（至少能辨識 Exchange / BroadcastHashJoin）
- [ ] 知道 shuffle 是什麼、為什麼貴、哪些操作會觸發
- [ ] 會用 `broadcast` 做小表 join 避免 shuffle
- [ ] 能解釋 narrow 與 wide transformation 的差別
- [ ] 理解 Parquet 相對 CSV 的三個優勢（column、壓縮、schema）
- [ ] 會用 DuckDB 直接對 Parquet/CSV 跑 SQL
- [ ] 知道 `repartition` vs `coalesce` 的差別
- [ ] 對 storage-compute 分離的 Lakehouse 架構有基本概念

### 2.4 跨領域共同 checklist（所有 Route 都要）

- [ ] Python 型別、collections、itertools 流利
- [ ] 會寫 context manager、decorator、generator
- [ ] 會 `venv` / `uv` / `poetry` 管理環境
- [ ] 會用 `logging` 而不是 `print`
- [ ] 會寫可被 pytest 測的純函數
- [ ] 讀得懂 traceback、會用 `pdb` / `breakpoint()`
- [ ] 會 git（commit / branch / rebase / PR review）

---

## 透鏡三：BoK（Body of Knowledge）對齊

把 M7 的內容對位到兩份業界標準：**ACM Data Science BoK**（2021 版，ACM Task Force on Data Science）與**MLOps BoK**（合併 Google MLOps Level 0–2、LF AI & Data 的 MLOps SIG、以及 EuroSys / MLSys 的 reference architecture）。

### 3.1 對齊 ACM Data Science Body of Knowledge

ACM DS BoK 把資料科學分為 11 個 Knowledge Area（KA）。M7 的覆蓋如下：

| ACM KA | M7 覆蓋度 | 對位節 | 缺口 |
|---|---|---|---|
| KA1 Analysis and Presentation | ✅ 涵蓋 | S05/S06 評估與解讀 | 無 |
| KA2 Artificial Intelligence | 🟡 部分 | S07/S08 DL 前導、S11 Route E | 無符號推理、planning |
| KA3 Big Data Systems | ✅ 涵蓋 | S09/S10 | 缺 streaming、CDC |
| KA4 Computing and Computer Fundamentals | ✅ 由 M6 涵蓋 | M6 CO/OS | 本模組不需重覆 |
| KA5 Data Acquisition, Management, and Governance | 🟡 部分 | S09 工具選型 | 缺 governance、lineage、quality |
| KA6 Data Mining | ✅ 涵蓋 | S02–S06 scikit-learn | 缺 association rule、clustering |
| KA7 Data Privacy, Security, Integrity, and Analysis for Security | ❌ 未涵蓋 | — | 整塊缺 |
| KA8 Machine Learning | ✅ 涵蓋 | S02–S08 | 缺非監督、強化學習 |
| KA9 Professionalism | 🟡 部分 | S11 職涯路線 | 缺 ethics、responsible AI |
| KA10 Programming, Data Structures, and Algorithms | ✅ 由 M1–M5 涵蓋 | M1–M5 | 本模組不需重覆 |
| KA11 Software Development and Engineering | ✅ 部分 | 本模組引用 M2 | 缺 testing、CI/CD |

**BoK 對齊結論**
- M7 在 KA2 / KA3 / KA6 / KA8 的覆蓋是合格的「前導」等級
- KA5（data governance）、KA7（security）、KA9（ethics / responsible AI）是明顯缺口——但這三塊不是 3 小時能塞的，建議作為「Route 的共同延伸讀物」
- **本模組定位應該明確承認：它是 KA1 / KA2 / KA6 / KA8 的 onboarding，不是 coverage**

### 3.2 對齊 MLOps Body of Knowledge

MLOps BoK（合併版本）通常分為 9 層：

| MLOps 層 | M7 覆蓋 | 說明 |
|---|---|---|
| 1. Data ingestion & versioning | ❌ | 原稿只提資料讀取，沒提 DVC / LakeFS / Delta |
| 2. Feature store | ❌ | 完全沒提 |
| 3. Model training & experiment tracking | 🟡 | 有訓練迴圈，沒提 MLflow / W&B |
| 4. Model registry | ❌ | 沒提 |
| 5. Model serving | ❌ | Route B 有一句 FastAPI |
| 6. Monitoring (data drift, model drift) | ❌ | 沒提 |
| 7. CI/CD for ML | ❌ | 沒提 |
| 8. Infrastructure (K8s, GPU scheduling) | 🟡 | M6 有 process / GPU，沒拉到 K8s |
| 9. Governance / compliance | ❌ | 沒提 |

**BoK 對齊結論**
- 這不是批評。M7 是 3 小時的前導，MLOps 是另一整個 track
- **必須在教材顯著位置聲明**：「本模組教的是 model development 的入門，MLOps 是 Route B / D 的主線」
- S11 Route B 的堆疊應該把 MLflow / model registry 至少**提到**（不需要教）

### 3.3 額外對齊：LLMOps（2025 起成形中）

LLMOps 目前還沒有 ACM 等級的 BoK，但業界已經形成 de facto 的九層結構：

| LLMOps 層 | M7 Route E 覆蓋 |
|---|---|
| 1. Prompt management / versioning | 🟡 原稿 prompt 工程 |
| 2. Retrieval（embedding、向量 DB、hybrid search） | 🟡 原稿 embedding + 向量 DB |
| 3. RAG orchestration | ✅ 原稿 RAG |
| 4. Agent orchestration（tools、planning） | 🟡 原稿 agent |
| 5. Evaluation（offline + online） | ❌ 原稿只提「評估指標」一句 |
| 6. Observability / tracing | ❌ |
| 7. Cost / latency optimization | ❌ |
| 8. Safety / guardrails | ❌ |
| 9. Fine-tuning / distillation | ❌ |

**結論**：Route E 的堆疊只覆蓋前四層，這是 2026 年的教材**必須補強**的部分（見 01_on_page_annotation §11 的補齊建議）。

---

## 合流建議（Synthesis）

把三個透鏡的觀察收束為三條 actionable 建議：

### 建議一：用「三條第一性原理」開場 Part B

現在 Part B 是從「DL 順理成章」切入，偏技術銜接。建議在 S07 前插入一張 meta slide：

> **三個領域、三句話：**
> - ML 是從資料找函數（$\hat f \approx f^*$）
> - DL 是用可微分的程式組函數（$f_\theta = f_L \circ \dots \circ f_1$）
> - 大數據是把函數拆到多台機器上算（partition + coordination）

這張 slide 讓學員在進入技術細節前，有三個「錨點」可以掛接後面所有內容。走完 Part B/C 回到這張 slide，收束效果會非常好。

### 建議二：用 BoK 對齊表作為教材的「誠實地圖」

在講義附錄放 3.1 / 3.2 / 3.3 三張對齊表，明確告訴學員：
- 我們教了哪些、沒教哪些
- 沒教的部分在哪個 Route 會延伸
- 完整 BoK 的 reference 怎麼找

這件事做了，教材的**可信度**會上一個層次——學員會知道這不是一門「什麼都教」的假課，而是一門「知道自己邊界的」真課。

### 建議三：五條路線的 Fundamentals checklist 當成畢業憑證

把透鏡二的四張 checklist 直接做成「畢業認證表」，學員可以自評打勾。**這比任何證書都實用**——因為它是業界第一年會被主管拿來比對的能力地圖。

建議在課程結束後一個月、三個月、六個月各寄一次提醒，讓學員自評進度。這會是這門課的長期 retention 機制。

---

**總結**
三個透鏡指向同一個診斷：**M7 的 narrative 強、first principles 對、但 BoK 覆蓋率需要誠實聲明**。只要做到第三點（誠實地圖），這份教材在內部 review 上就能從「好的入門課」升級為「具備 BoK 自覺的入門課」——後者在 enterprise training 的市場上有數量級差異的說服力。

— end of three-lens analysis —
