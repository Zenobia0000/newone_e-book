# M7 On-Page Annotation（逐節批註）

> **文件定位**：這份文件是對 `M7_ML_DL_BigData前導與學習路徑.md` 原稿的「逐知識點」逐段批註。面向內部技術 reviewer（資深架構師、DS Lead、DE Lead、ML Platform Lead）。每段採三層標記：
>
> - 🎯 **宏觀**：這一段在「24 小時課程收束 + 分流」這個 narrative 裡的功能性定位。
> - 🔬 **細部**：技術細節的正確性、模糊點、容易被學員或講師誤讀的地方。
> - ⚠️ **reviewer 補齊**：原稿沒講清楚、但第一線工程師一進業界就會踩到的內容。以批判補齊為主，不是在客氣。
>
> **語氣**：內部 review。直說問題、直接補齊。繁體中文，台灣業界用語（DE、DS、pipeline、叢集、流量、部署）。
> **日期**：2026-04-14（今日）。以 2026 年的技術現況評估原稿（2023–2025 期間寫成）。

---

## 批註 §1 模組定位（第 10–30 行）

🎯 **宏觀**
這一段是整門 24 小時課程的「收束句」。原稿講三件事：(1) 你已站在哪裡 (2) 前方有什麼 (3) 你要自己選路。這個結構沒問題，但定位語氣偏「溫柔」——在技術討論會的語境下我會把它改為「分流宣言」：前六個模組是中立底盤，M7 是第一次要求學員做「方向承諾」的節點。

🔬 **細部**
- 「資料分析底盤」這個詞 OK，但「底盤」在中文技術語境下有時會被誤讀為「框架」。建議在 S01 明確定義：底盤 = 三樣東西（資料結構語彙、統計直覺、系統底層常識），不是工具集合。
- 「三小時結構」表裡 Part A 60 分鐘只涵蓋到 scikit-learn 建模工作流，對第一次接觸 ML 的學員偏緊。S03–S06 至少要 75 分鐘才不會變成跑投影片。

⚠️ **reviewer 補齊**
原稿完全沒提「data leakage」這個概念，但 train/test split 一旦講錯，學員整個職涯都會被汙染。Part A 必須硬塞一個 5 分鐘的 leakage 示例（例如：在 split 前就做 `StandardScaler.fit` 全量資料 → 測試集效能被高估）。後面 S05 我會再補一次。

---

## 批註 §2 S02「ML 不是魔法，是函數逼近」

🎯 **宏觀**
這張投影片的 job-to-be-done 是「拆除神秘化」。敘事正確。放在 Part A 第二張是對的。

🔬 **細部**
- 「ML 在找一個函數 f，使得 f(input) 盡可能接近 output」——這個定義精準，但**只涵蓋監督式學習**。原稿在 S03 才點出「監督式」的範圍，順序上有一個兩分鐘的認知空窗。建議 S02 結尾補一句「今天談的是監督式這一支，非監督與強化學習先擱著」。
- 「線性迴歸、決策樹、神經網路本質上都在做同一件事」——這句話策略上有用（降低學員焦慮），但技術上不完全精準：決策樹不是在最佳化一個可微分函數，它是貪婪切割特徵空間。講師可以講得粗略，但投影片文字最好改成「都是在 fit 一個從 X 到 y 的映射」，避免日後學員讀 XGBoost 論文時困惑。

⚠️ **reviewer 補齊**
**scikit-learn Estimator API 一致性哲學**——這一點原稿只在 S04 用一句話帶過（`.fit()` / `.predict()` / `.score()`），太薄。這個 API 設計是 scikit-learn 能成為業界標準的**最大原因**，值得 S04 多花 3 分鐘：

- `BaseEstimator` + `TransformerMixin` + `ClassifierMixin` 的 Mixin 組合設計
- `fit` 改變狀態、`transform`/`predict` 不改變狀態的純函數哲學
- 所有超參數都透過 `__init__` 傳入、能用 `get_params` / `set_params` 取出，這是 `GridSearchCV` 能通用的前提
- 這個一致性讓 pipeline 可以組合（後面 Route B 的 Pipeline / ColumnTransformer 就是靠這個活下來）

不講這一層，學員只會把 scikit-learn 當「API 很像」的巧合，不會知道那是**設計哲學**。

---

## 批註 §3 S03「監督式學習的一張圖」+ train/test split

🎯 **宏觀**
這張是 Part A 的骨架。S03 + S05 兩張一起承擔了「建模工作流的正確心智模型」這個任務。

🔬 **細部**
- 「訓練集通常佔 70–80%」——這個比例在 2026 年的實務上已經偏保守。現代工作流比較常見的是 `train:val:test = 60:20:20` 或 `train:val:test = 70:15:15`。原稿**完全沒有提到 validation set**，這是大問題。

⚠️ **reviewer 補齊**

**(a) 三分割：train / validation / test**
原稿把世界壓縮成兩分割，這在教學上會直接種下後面的錯誤習慣。正解：

- **train**：餵模型、更新參數
- **validation / dev**：調超參數、選模型、做 early stopping
- **test**：**只能動一次**，是對外報數字的真實性檢驗

學員日後一旦用 test set 挑模型，整個評估就廢了。這點 S05 的「診斷 / 迭代」如果用 test set 做，就是在教壞學生。

**(b) data leakage**
原稿完全沒點名這個詞。必須補：

- **預處理 leakage**：`StandardScaler.fit(全資料)` 再 split → 測試集統計資訊滲透進訓練
- **時間 leakage**：用未來資訊預測過去（時序資料必須用 `TimeSeriesSplit`，不能隨機 split）
- **target leakage**：特徵裡包含了目標的代理變數（例如預測流失時把「已退費金額」放進 X）
- **group leakage**：同一客戶的多筆記錄被拆到 train / test（必須用 `GroupKFold`）

Leakage 是新人第一年最常踩的坑，教材不講等於失職。

**(c) cross-validation 種類**
原稿 Route B 只提「k-fold / stratified / time-series split」三種，但 Part A 主體完全沒介紹 CV，只有在延伸挑戰裡出現 `cross_val_score`。應該在 S05 正式介紹：

| CV 類型 | 適用情境 |
|---|---|
| `KFold` | 一般獨立同分布資料 |
| `StratifiedKFold` | 分類、類別不平衡 |
| `GroupKFold` | 同群樣本不能跨 fold（病人、客戶、session） |
| `TimeSeriesSplit` | 時序，train 永遠在 test 之前 |
| `RepeatedKFold` | 資料少、要降低單次 split 的隨機性 |
| `LeaveOneOut` | 資料極少（< 50 筆） |

這張表應該進講義，不是附錄。

---

## 批註 §4 S04「scikit-learn 標準入口」

🎯 **宏觀**
定位清楚、里程碑抓對（1.0 / 2021）。

🔬 **細部**
- 2026 年的當下 scikit-learn 已經到 1.5+。原稿停留在 1.0 的敘事是 OK 的（里程碑意義），但講師應該補充「現在版本是 1.5，已支援 Array API（可以跑在 CuPy / PyTorch tensor 上）」——這會連到 Route C/D 的伏筆。
- 「邊界清楚是優點，不是缺陷」——這句話保留，很重要。但要補一句：「scikit-learn 不做 GPU 訓練，不做序列建模，不做分散式」——講清楚才不會有人問「那我怎麼用 sklearn 訓 Transformer」。

⚠️ **reviewer 補齊**
見批註 §2 ⚠️ 補齊的 Estimator API 哲學段落。

另外補：
- **Pipeline / ColumnTransformer** 在 S04 或 S05 必須出現一次，哪怕只是 30 秒。否則學員會在 Route B 才第一次接觸 Pipeline，屆時已是第二層認知負擔。
- **scikit-learn 不處理「時間」**：所有 fold 都是隨機的，時序資料必須明確手動切。這點要在 Route A / B 都再強調一次。

---

## 批註 §5 S05「建模工作流」

🎯 **宏觀**
用循環圖表示工作流是對的。但原稿的四節點（分割 → 訓練 → 評估 → 診斷）**把特徵工程藏在「訓練」前面的一句話裡**，這是比例失衡。真實工作流裡特徵工程佔掉 60–70% 工時。

🔬 **細部**
- 「訓練集表現好但測試集差 = 過擬合」——對，但要補反面：「訓練集和測試集表現都差 = 欠擬合或資料/特徵有問題」。只講一半會讓學員以為「差距小 = 沒問題」，但其實可能是「兩邊都爛」。
- 「評估結果告訴你去哪裡」這句話很棒，建議保留。但下方三分支「過擬合 / 欠擬合 / 資料問題」要各給一個 concrete 動作：
  - 過擬合 → regularization、減模型容量、增資料、early stopping
  - 欠擬合 → 增模型容量、加特徵、換模型
  - 資料問題 → 重新檢查 label、檢查 leakage、畫 learning curve

⚠️ **reviewer 補齊**
**learning curve**：這是診斷「到底該補資料還是補模型」的標準工具，原稿沒提。畫 `learning_curve` 看訓練/驗證分數隨資料量的變化，形狀告訴你該走哪一步。這個工具一張圖就能讓學員一輩子受用。

---

## 批註 §6 S06「動手做：scikit-learn 實作」

🎯 **宏觀**
放在 Part A 最後做收束，OK。

🔬 **細部**
- 程式碼骨架把 `StandardScaler` 放在第四部完整練習區、S06 的骨架裡**沒有 scaler**——這是錯誤示範，邏輯迴歸對特徵尺度敏感，會直接誤導學員。必須補。
- 原稿骨架直接 `train_test_split(X, y)`，沒有 `stratify=y`、沒有 `random_state`。前者在分類不平衡時會炸，後者沒寫就不可重現——這兩個參數在教學程式碼裡**一定要寫滿**。

⚠️ **reviewer 補齊**
- 測試集 score 和 classification_report 的 precision / recall / f1 應該在 S06 當場解讀。不解讀就只是跑程式，不是教 ML。
- `confusion_matrix` 比單一 score 資訊密度高，強烈建議畫出來。

---

## 批註 §7 S07「為什麼 DL 順理成章」+ tensor vs ndarray

🎯 **宏觀**
「把新知識掛到舊知識上」——這張投影片的策略正確。

🔬 **細部**
- 「NumPy array → tensor」這個類比**方向對、細節錯**。tensor 不是 ndarray 的擴充，它多了三個 ndarray 沒有的東西：

  1. **device**：可以 `.to("cuda")`，ndarray 只能在 CPU
  2. **autograd / requires_grad**：可以追蹤計算圖並回傳梯度
  3. **dtype 政策**：DL 預設 float32（甚至 bfloat16），NumPy 預設 float64——學員遇到 `RuntimeError: expected scalar type Float but found Double` 就是這個坑

  教學上可以用「ndarray 的超集」這個比喻，但要明講三個差異點。

⚠️ **reviewer 補齊**

**(a) PyTorch autograd tape 的心智模型**
原稿只說「`.grad` → autograd」，沒解釋 tape。補：

- PyTorch 的 autograd 是**動態的**（define-by-run）：每次 forward 都重新建一條 tape
- tape 記錄每個 operation 的反向函數（`grad_fn`），`.backward()` 從 loss 沿 tape 反走
- `with torch.no_grad()` / `.detach()` 是最常用的 tape 控制工具，推論時必用
- leaf tensor（`requires_grad=True` 的那批）才會收到 `.grad`

這段 3 分鐘可以讓學員一輩子不會搞錯為什麼 inference 時 memory 爆掉。

**(b) eager vs graph (torch.compile)**
見批註 §8。

---

## 批註 §8 S08「PyTorch 2.0：從寫模型到效能工程」

🎯 **宏觀**
標題抓得對——「從寫模型到效能工程」是 PyTorch 在 2023–2026 這條曲線上的本質轉折。這張投影片的 narrative 可以支撐 Route C 的整個「效能工程」層次。

🔬 **細部**
- 原稿提「30–200% 加速」——這個數字要加 disclaimer：加速倍率**高度依賴模型結構與 batch size**，純 Transformer backbone 加速明顯，有大量 Python 控制流的模型加速有限（甚至 compile 失敗退回 eager）。
- `torch.compile()` 在 2026 年實務上不是「免費加速」——編譯開銷、recompile cost、dynamic shape 不穩定都是真實痛點。教材要誠實。

⚠️ **reviewer 補齊**

**(a) eager vs graph 的二元光譜**
| 模式 | 代表 | 優點 | 痛點 |
|---|---|---|---|
| eager | PyTorch 1.x 預設 | debug 直觀、Python print 可用 | 不能融合 kernel、overhead 高 |
| graph | TensorFlow 1.x、TorchScript | 可做 graph 優化、可導出部署 | 難 debug、Python 控制流受限 |
| trace + compile | `torch.compile()`、JAX `jit` | 兩邊兼顧 | recompile cost、dynamic shape 限制 |

PyTorch 2.0 的創新是在 eager 使用介面下偷偷做 graph 優化（TorchDynamo 抓 Python bytecode、AOTAutograd 算反向、Inductor 產生 GPU kernel）。

**(b) CUDA stream 與非同步執行**
原稿完全沒提，但凡講 GPU 效能這是繞不開的：

- GPU kernel launch 是**非同步**的，`tensor.to("cuda")` 之後立刻 print 到的 tensor 可能還沒真的跑完
- `torch.cuda.synchronize()` 是量測執行時間的必要操作，不 sync 測到的都是「我把任務丟給 GPU 的時間」
- 多 stream 可以讓資料傳輸與計算重疊（常在 DataLoader + 訓練迴圈裡隱含發生）
- `pin_memory=True` + `non_blocking=True` 是這套流程能跑快的兩個關鍵旋鈕

這一段 Part B 至少要 5 分鐘，否則 Route C 學員下一步學混合精度、分散式訓練會完全接不上。

**(c) DataLoader 多進程**
原稿沒提。但 DataLoader 的 `num_workers > 0` 是新人第二年才搞懂的陷阱：

- `num_workers=N` 時 PyTorch 會 fork N 個子進程做資料載入
- 子進程之間不共享記憶體，每個都會複製一份 dataset object（注意 memory footprint）
- `persistent_workers=True` 避免每個 epoch 重建 worker
- Windows 上必須把訓練腳本包進 `if __name__ == "__main__":`，否則 fork 炸鍋
- 如果 dataset 裡有 CUDA tensor、lambda、未 pickle-able 的物件，`num_workers > 0` 會直接爆

這段 3 分鐘，M6 講過 process / IPC 的知識剛好接上。

---

## 批註 §9 S09「當 pandas 不夠用時」

🎯 **宏觀**
這張投影片把 tool choice 從「品味」升級為「工程判斷」，這個立場正確。

🔬 **細部**
- 「100MB 用 pandas、10GB 用 Polars/DuckDB、100GB+ 用 PySpark」——這是 2024 年的標準說法，2026 年的當下我會微調：
  - Polars + Arrow backend 讓上限推到 50–100GB（單機 128GB RAM 機器上可行）
  - DuckDB 純 analytical query 在 200GB+ 仍可跑（out-of-core 讀 Parquet）
  - PySpark 的門檻往上抬到 500GB+ 或「資料本來就在 Lakehouse」這個情境
- 「lazy evaluation」在這張只提到 Polars/DuckDB，但 Spark 也是 lazy，術語放在 S10 才講，順序有點散。建議 S09 就定義 lazy 這個詞。

⚠️ **reviewer 補齊**

**(a) pandas 2.0+ Arrow backend 的真相**
- `pd.options.mode.dtype_backend = "pyarrow"` 或建立時 `dtype_backend="pyarrow"` 可以換成 Arrow-backed 的 dtype
- 好處：字串 4–10x 快、memory 少一半、`NaT`/`NA` 語意一致
- 但不是所有 API 都支援，遇到不支援會 fallback 到 NumPy backend——這是隱藏的 footgun

**(b) Polars 的 lazy vs eager API**
- `pl.DataFrame` 是 eager、`pl.LazyFrame` 是 lazy
- `scan_csv` / `scan_parquet` 回傳 LazyFrame，`.collect()` 才真的跑
- Lazy API 才能觸發 Polars 的 query optimizer（predicate pushdown、projection pushdown、common subplan elimination）
- 從 pandas 遷移時不改寫成 lazy 會錯過 80% 的效能

**(c) DuckDB 的定位**
- DuckDB 不是「Polars 的競品」，而是「SQLite for analytics」
- 最大殺招：直接對 Parquet / CSV / pandas / Polars DataFrame 跑 SQL，零 ETL
- 現在 Python 資料工作流裡常見的三明治：`pandas → duckdb.sql(...) → polars`

---

## 批註 §10 S10「PySpark：分散式橋樑」+ lazy / DAG / shuffle

🎯 **宏觀**
收尾 Part B 放 PySpark 是對的。但原稿沒講到「為什麼分散式需要不同的心智模型」，只講了「API 很像 pandas」——這是在教學員寫錯 Spark 的最短路徑。

🔬 **細部**
- 原稿說 Catalyst「一次性規劃最有效率的執行計畫」，這句話沒錯但太浪漫。實務上 Catalyst 會出錯、會選到糟糕的 join strategy、UDF 會直接關掉優化——這些都要講。
- 「你用 Python 寫，Spark 把工作分派到整個叢集」——這句話把 PySpark 當成透明層，實務上完全不是。Python UDF 有 serialization overhead（pickle + arrow batch），Spark SQL + `pyspark.sql.functions` 才是真正 native。Python lambda 跑在 driver 還是 executor，學員必須分得清。

⚠️ **reviewer 補齊**

**(a) PySpark 的 lazy evaluation 與 DAG**
- 所有 transformation（`select`, `filter`, `groupBy`）是 lazy，不會觸發計算
- 只有 action（`count`, `collect`, `show`, `write`）才觸發 job
- 一個 action → 一個 job → 多個 stage → 多個 task
- stage 邊界由 shuffle 決定（narrow dependency 在一個 stage 內，wide dependency 切 stage）
- `df.explain(mode="formatted")` 是學員第一個要學會的 debug 工具

**(b) shuffle 成本**
Spark 效能的頭號敵人就是 shuffle。必須講：

- shuffle = 資料跨 executor 重新分派（`groupBy`、`join`、`orderBy`、`repartition` 都會觸發）
- shuffle 寫磁碟、讀磁碟、過網路，cost 是 narrow transformation 的 100–1000 倍
- `broadcast join`（小表）可以完全避免 shuffle——這是第一個效能旋鈕
- `repartition(n)` vs `coalesce(n)`：前者會 shuffle、後者不會（但只能減 partition）
- skew（資料分布不均）會讓一個 task 跑超久——2024 年後 AQE（Adaptive Query Execution）預設開啟有改善，但不是萬靈丹

**(c) PySpark vs Pandas on Spark (舊 Koalas)**
- `pyspark.pandas` API 存在，但不建議新專案直接採用
- 教學路徑：先學 Spark DataFrame API（`select`, `withColumn`, `groupBy.agg`）再碰 pandas API——反過來會養出錯誤直覺

---

## 批註 §11 S11「五條職涯路線」+ Route E 的 LLM/RAG/agent 落地陷阱

🎯 **宏觀**
五條路線切得很準。Route E 的存在本身就是這份教材在 2026 年仍站得住的理由（2023 年的教材常常沒這條）。但 Route E 的技術堆疊**在內部 review 的標準下還是偏薄**。

🔬 **細部**
- Route A–D 的堆疊都是「技術能力 × 層次遞進」，結構清楚。
- Route E 的堆疊停留在「工具層」（向量 DB、RAG、LLM API），缺少「系統層」——沒有講到 context window 管理、token budget、latency budget、cost control 這些真正卡生產的東西。

⚠️ **reviewer 補齊**

**Route E 必須補的落地陷阱：**

1. **RAG 的第一個殺手是 retrieval 品質，不是 LLM**
   - chunking 策略（fixed / semantic / hierarchical）直接決定上限
   - embedding 模型選擇（多語言、domain-specific）的影響 > prompt 工程
   - hybrid search（BM25 + vector）幾乎永遠比純 vector 好
   - reranking（cross-encoder）是把 recall 轉成 precision 的關鍵一步

2. **Agent 的真實失效模式**
   - tool call 錯參數（schema 不符）
   - 無窮迴圈（agent 一直 call 同個 tool）
   - context window 爆掉（工具回傳太長）
   - 非確定性造成 eval 很難做

3. **evaluation 是 Route E 最難的部分**
   - 沒有 accuracy 這種單一指標
   - 人工評估貴、LLM-as-a-judge 有偏差
   - 實務常用：RAGAS、Phoenix、Langfuse 的 trace-based eval
   - golden set 維護是 MLOps 級別的工作

4. **成本與延遲**
   - token 計算要到「per-request p99 cost」這個粒度
   - streaming 是 UX 的必要條件，但複雜化 trace/log
   - caching（prompt cache、embedding cache、retrieval cache）三層都要想

Route E 的堆疊建議補一層「生產工程」：observability、eval harness、cost/latency budget、prompt 版本控管。

---

## 批註 §12 五條路線的交集與分歧點（原稿缺的 meta 層）

🎯 **宏觀**
原稿把五條路線並列呈現，但**沒有畫出路線之間的共享底座與分岔點**。這在一張職涯地圖上是最值錢的 meta 資訊。我在這裡補上 reviewer 視角的分析。

🔬 **細部：共享底座**

所有五條路線的共同前置底盤（這是 M1–M7 搭完的內容）：

| 共享能力 | 覆蓋路線 |
|---|---|
| pandas + SQL | A / B / D / E |
| 統計直覺（抽樣、顯著、分布） | A / B / C / E-eval |
| Python OOP + 模組化 | B / C / D / E |
| 系統底層（process / memory / GPU） | C / D |
| 向量/矩陣直覺 | B / C / E-embedding |

**所以：M1–M6 的底盤不是「都要學」的湊合，而是五條路線的實際交集。**

🔬 **細部：兩兩分歧點**

| 路線對 | 第一個分岔決策 |
|---|---|
| A vs B | 「要推論 / 解釋」vs「要預測 / 部署」 |
| B vs C | 「結構化資料 + 可解釋」vs「非結構化資料 + 表示學習」 |
| B vs D | 「模型品質」vs「資料可靠性」 |
| C vs E | 「訓練模型」vs「使用模型」——2026 年最關鍵的分岔 |
| D vs E | 「資料管線」vs「AI 管線」——其實殊途同歸，MLOps / LLMOps 正在合流 |

⚠️ **reviewer 補齊**

**2026 年的實際觀察：**

- Route D 與 Route E 的合流：「LLMOps」在企業裡常常掛在 Data Platform 底下，不是單獨部門
- Route B 的相對萎縮：傳統 ML 工程師的職缺在「有 LLM 可以解」的場景被擠壓，但「結構化資料 + 可解釋性 + 低延遲」的場景仍然是 ML 工程師的護城河
- Route C 的兩極化：研究型 DL（頂尖模型訓練）職缺極少且集中在頭部公司；應用型 DL（微調、蒸餾、部署）的機會反而變多
- Route A 的回歸：2025 年後「LLM 實驗 A/B test」的需求讓 Route A 能力被 LLM 工程師倒抽需求，會統計的人溢價明顯

**建議教材給學員的真實話：**
> 「五條路線沒有一條是死路，但有一條可能比其他條都更窄——純訓練大模型。除非你進頭部實驗室，否則比較務實的組合是 B+E 或 D+E。」

---

## 批註 §13 原稿缺的「整體評估」與 reviewer 總評

**原稿強項**（保留）
1. 「函數逼近」框架：把 ML 神秘化拆除得乾淨
2. 「工具是規模問題不是品味問題」：S09 這個立場非常強
3. 雙主線回顧：最後一節把 M1–M7 的 narrative 收得漂亮
4. 五條路線選擇的「問題類型」判斷法：比列技術堆疊高明

**原稿弱項**（必補）
1. train / val / test 三分割、data leakage、CV 種類——**必須補**
2. scikit-learn Estimator API 哲學——太輕
3. tensor 與 ndarray 的三個差異（device / grad / dtype）——不補會種下一輩子的 bug
4. autograd tape 的心智模型——沒有這個，`torch.no_grad()` 永遠是 magic
5. CUDA stream / DataLoader worker——GPU 效能兩個關鍵旋鈕
6. PySpark 的 shuffle / DAG / lazy——教 PySpark 不教這三個等於沒教
7. Route E 的生產工程層——eval、cost、latency、observability
8. 五條路線的交集矩陣——meta 視角缺席

**總評**
原稿在**敘事品質**上是四顆星（滿分五），在**技術完整性**上是三顆星。這份文件的目的就是把後者補到四顆星半。上課時這些補齊不必全講，但講義和 reference material 一定要放齊——不然學員進業界第一年踩的坑，九成都來自這份教材沒講的東西。

— end of annotation —
