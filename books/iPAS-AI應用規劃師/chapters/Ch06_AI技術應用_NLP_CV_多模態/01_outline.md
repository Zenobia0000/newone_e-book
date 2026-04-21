# Ch06 講師講稿 — AI技術應用：NLP、CV、多模態

> 節次時長：120 分鐘（講授 75 + 考題演練 30 + 總結回顧 15）
> Governing thought：「中級科目一的核心：你能否在 NLP、CV、GenAI、多模態之間選對技術。」
> 考試對應：中級 L211（NLP技術 / CV技術 / 生成式AI技術 / 多模態AI）

---

## 1. 本節目標

1. 掌握 NLP 核心技術鏈（Tokenization → 表示法 → 下游任務），能在考題中正確配對技術與場景。
2. 區分 CV 四大任務的輸入輸出格式，不再搞混語義分割和實例分割。
3. 理解 Transformer 的 Self-Attention 機制，知道它為何能跨 NLP/CV/多模態通用。
4. 比較模型壓縮三劍客（蒸餾/剪枝/量化），能判斷哪種壓縮適合哪種場景。
5. 辨識多模態融合三策略，能解釋早期融合與晚期融合的差異。
6. 了解 AutoML 的基本概念與考試出題趨勢。

## 2. 考試對應表（含歷屆/模擬考題映射）

| 考試能力指標 | 本章對應段落 | 歷屆相關考題 |
|---|---|---|
| NLP 技術 | Part A（S03-S07） | Q2（Tokenization）、Q10（Word2Vec） |
| CV 技術 | Part B（S08-S11） | Q7（CV技術配對） |
| 生成式AI技術 | Part C（S12-S13） | Q1（AI vs Rule-based）、Q8（模型壓縮） |
| 多模態AI | Part D（S14-S16） | Q11（Early Fusion）、Q12（Transformer多模態醫療） |
| 業界趨勢 | 穿插各 Part | AutoML 概念題 |

## 3. 時間切分表（75 + 30 + 15）

| 時間 | 區段 | 內容 |
|---|---|---|
| 0~5 | 講授 | 開場：四大技術領域地圖 + AI vs Rule-based 判斷基準 |
| 5~20 | 講授 | Part A：NLP（Tokenization → Word2Vec/TF-IDF → 情緒分析/NER） |
| 20~25 | 講授 | Part A 踩雷：Word2Vec vs TF-IDF 混淆陷阱 |
| 25~40 | 講授 | Part B：CV 四大任務 + CNN → ViT 演進 |
| 40~45 | 講授 | Part B 踩雷：語義分割 vs 實例分割 |
| 45~55 | 講授 | Part C：Transformer 核心機制 + 模型壓縮三劍客 |
| 55~70 | 講授 | Part D：多模態融合三策略 + 醫療應用案例 |
| 70~75 | 講授 | 四大領域總覽 + AutoML 趨勢 |
| 75~85 | 演練 | 考題演練 Round 1：NLP 技術辨識（5 題） |
| 85~95 | 演練 | 考題演練 Round 2：CV + 模型壓縮（5 題） |
| 95~105 | 演練 | 考題演練 Round 3：多模態 + Transformer（5 題） |
| 105~120 | 總結 | 錯題檢討 + 四大領域速查卡 + Ch07 預告 |

## 4. 關鍵教學點

### Part A：NLP 技術

#### A-1 NLP Pipeline
- **全流程**：原始文字 → 前處理（清洗/正規化）→ Tokenization → 向量化/表示法 → 下游任務。
- **教學要點**：讓學員理解 NLP 不是直接「讀文字」，而是先把文字轉成數字（向量），再讓模型處理。

#### A-2 Tokenization
- **字元級（Character）**：每個字一個 token。詞彙量小，但序列長。
- **詞級（Word）**：每個詞一個 token。直覺但 OOV（未登錄詞）問題嚴重。
- **子詞級（Subword / BPE）**：折衷方案，GPT/BERT 都用。平衡詞彙量與 OOV。
- **考試重點**：Q2 考 Tokenization 的定義與作用，要知道「把文字切成模型能處理的最小單位」。

#### A-3 Word2Vec vs TF-IDF
- **Word2Vec**：稠密向量（dense vector），捕捉語義相似度。king - man + woman ≈ queen。
- **TF-IDF**：稀疏權重（sparse），衡量詞在文件中的重要程度。TF（詞頻）x IDF（逆文件頻率）。
- **核心差異**：Word2Vec 懂語義，TF-IDF 懂重要性。兩者解決不同問題。
- **考試重點**：Q10 考 Word2Vec 的特性，要記住「稠密/語義/king-queen 類比」三個關鍵字。

#### A-4 下游任務
- **情緒分析（Sentiment Analysis）**：判斷文本正面/負面/中性。應用：社群監控、客戶回饋。
- **命名實體辨識（NER）**：從文本中抽取人名/地名/組織名等實體。應用：資訊萃取、知識圖譜。
- **文本分類**：將文本歸入預定義類別。應用：客服工單分類、新聞分類。
- **文本摘要**：將長文縮短保留重點。應用：新聞摘要、會議紀錄。

### Part B：CV 技術

#### B-1 CV 四大任務
- **圖像分類（Classification）**：整張圖一個標籤。輸出：類別。例：這是一隻貓。
- **物件偵測（Object Detection）**：找出圖中物件的位置和類別。輸出：Bounding Box + 類別。例：這裡有一隻貓、那裡有一隻狗。
- **語義分割（Semantic Segmentation）**：每個像素標類別，但同類不分個體。例：所有「貓」像素標同色。
- **實例分割（Instance Segmentation）**：每個像素標類別且分個體。例：貓 A 藍色、貓 B 紅色。
- **考試重點**：Q7 考 CV 技術配對，關鍵在「有沒有 bounding box」和「分不分個體」。

#### B-2 技術演進
- **CNN（LeNet → AlexNet → VGG）**：卷積提取局部特徵，層越深特徵越抽象。
- **ResNet**：殘差連接解決深層網路梯度消失問題。
- **ViT（Vision Transformer）**：把圖像切成 patch 當 token，用 Transformer 處理。證明 Transformer 不只能做 NLP。
- **教學要點**：ViT 是跨領域的橋樑，連接 NLP 和 CV，也是多模態的基礎。

### Part C：生成式 AI 技術

#### C-1 Transformer 核心
- **Self-Attention**：每個 token 看所有其他 token，計算注意力權重，決定「該關注哪裡」。
- **位置編碼（Positional Encoding）**：因為 Attention 本身不管順序，需要額外加入位置資訊。
- **為何重要**：Transformer 是 GPT/BERT/ViT/CLIP 的共同基礎，理解它就理解了一半的現代 AI。
- **考試重點**：Q12 考 Transformer 在多模態的應用，要知道它的跨模態通用性。

#### C-2 模型壓縮三劍客
- **知識蒸餾（Distillation）**：大模型（teacher）教小模型（student）。保留能力，縮小體積。
- **剪枝（Pruning）**：移除不重要的神經元或連接。結構化剪枝 vs 非結構化剪枝。
- **量化（Quantization）**：降低數值精度（FP32 → FP16 → INT8 → INT4）。速度快但可能掉精度。
- **考試重點**：Q8 考模型壓縮，要能區分三者的原理和取捨。量化是「降精度」，剪枝是「砍連接」，蒸餾是「教小模型」。

### Part D：多模態 AI

#### D-1 融合三策略
- **早期融合（Early Fusion）**：在特徵層就合併不同模態的資料。優點：模態間交互充分。缺點：維度高、計算量大。
- **晚期融合（Late Fusion）**：各模態獨立處理，在決策層合併結果。優點：模組化、各模態可獨立優化。缺點：錯過低層交互。
- **注意力機制融合（Attention-based Fusion）**：用 Cross-Attention 讓不同模態互相「看」對方。兼顧交互深度與模組彈性。
- **考試重點**：Q11 考 Early Fusion 的定義，要記住「特徵層合併」vs「決策層合併」。

#### D-2 多模態醫療應用
- **場景**：結合醫學影像（X光/MRI）+ 電子病歷（文字）+ 基因數據（序列）→ 輔助診斷。
- **技術選擇**：影像用 CNN/ViT，文字用 BERT，融合用 Cross-Attention。
- **考試重點**：Q12 考 Transformer 在多模態醫療的應用，是綜合題型。

### 補充：AutoML
- **概念**：自動化機器學習——自動做特徵工程、模型選擇、超參數調優。
- **代表工具**：Google AutoML、Auto-sklearn、H2O AutoML。
- **考試出題方向**：定義題為主，不會深入技術細節。

## 5. 學員常犯錯誤（考試易錯點）

1. **Word2Vec 和 TF-IDF 搞混**：Word2Vec 是向量（語義），TF-IDF 是權重（重要度）。
2. **語義分割和實例分割搞混**：語義不分個體（所有貓同色），實例分個體（每隻貓不同色）。
3. **以為 Transformer 只做 NLP**：ViT、CLIP、多模態都用 Transformer。
4. **量化和剪枝搞反**：量化是降數值精度（FP32→INT8），剪枝是移除連接。
5. **早期融合和晚期融合選反**：早期 = 特徵層（early in pipeline），晚期 = 決策層（late in pipeline）。
6. **物件偵測和實例分割混淆**：偵測輸出 bounding box，分割輸出像素級遮罩。

## 6. 提問設計

1. 「給你一段商品評論，你會用 Word2Vec 還是 TF-IDF 來找出關鍵詞？為什麼？」
2. 「自動駕駛需要知道『前面有三輛車各在哪裡』，該用 CV 四大任務中的哪一個？」
3. 「為什麼 Transformer 能同時用在文字、圖像、多模態？核心機制是什麼？」

## 7. 延伸資源

- 《Attention Is All You Need》原始論文（Transformer 奠基之作）。
- Stanford CS231n（CV 課程，免費線上）。
- Jay Alammar 的 The Illustrated Transformer（視覺化解說，搜尋即得）。
- iPAS 中級考試範圍公告與歷屆考題。
- Hugging Face 官方文件（Tokenization / Model Compression 章節）。

## 8. 收斂金句

「技術不是越新越好，是選對的那一個。NLP、CV、GenAI、多模態——考試考的不是你背了多少名詞，是你能不能在情境中選出最適合的技術。」
