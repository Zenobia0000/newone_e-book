# Ch06 — AI 技術應用：NLP、CV、多模態｜講師講稿

> **課程時長**：2 小時（講授 75 min + 考題演練 30 min + 總結回顧 15 min）
> **受眾定位**：iPAS 中級科目一考生，需掌握四大技術領域的選型判斷
> **前置知識**：Ch03 ML 概念與鑑別式/生成式 AI
> **後續銜接**：Ch07 AI 導入規劃與系統部署
> **評鑑範圍**：中級 L211（NLP技術 / CV技術 / 生成式AI技術 / 多模態AI）

---

## 1. 本節目標 (Learning Objectives)

完成本節後，學員應能：

1. 掌握 NLP 核心技術鏈（Tokenization → 表示法 → 下游任務），能在考題中正確配對技術與場景。
2. 區分 CV 四大任務的輸入輸出格式，不再搞混語義分割和實例分割。
3. 理解 Transformer 的 Self-Attention 機制，知道它為何能跨 NLP/CV/多模態通用。
4. 比較模型壓縮三劍客（蒸餾/剪枝/量化），能判斷哪種壓縮適合哪種場景。
5. 辨識多模態融合三策略，能解釋早期融合與晚期融合的差異。
6. 了解 AutoML 的基本概念與考試出題趨勢。

---

## 2. 時間切分表

```
00:00-00:05  開場：四大技術領域地圖 + AI vs Rule-based 判斷基準
00:05-00:20  Part A：NLP（Tokenization → Word2Vec/TF-IDF → 情緒分析/NER）
00:20-00:25  Part A 踩雷：Word2Vec vs TF-IDF 混淆陷阱
00:25-00:40  Part B：CV 四大任務 + CNN → ViT 演進
00:40-00:45  Part B 踩雷：語義分割 vs 實例分割
00:45-00:55  Part C：Transformer 核心機制 + 模型壓縮三劍客
00:55-01:10  Part D：多模態融合三策略 + 醫療應用案例
01:10-01:15  四大領域總覽 + AutoML 趨勢
01:15-01:25  考題演練 Round 1：NLP 技術辨識（5 題）
01:25-01:35  考題演練 Round 2：CV + 模型壓縮（5 題）
01:35-01:45  考題演練 Round 3：多模態 + Transformer（5 題）
01:45-02:00  錯題檢討 + 四大領域速查卡 + Ch07 預告
```

---

## 3. 關鍵教學點 (Key Teaching Points)

### Part A：NLP 技術

1. **NLP 不是直接「讀文字」**：流程是原始文字 → 前處理 → Tokenization → 向量化 → 下游任務。模型處理的是數字（向量），不是文字。

2. **Word2Vec vs TF-IDF 核心差異**：Word2Vec 是稠密向量，捕捉語義相似度（king-queen 類比）。TF-IDF 是稀疏權重，衡量詞的重要程度。兩者解決不同問題。考題記住「稠密/語義/king-queen」三個關鍵字。

3. **Tokenization 三級別**：字元級（小詞彙量、長序列）、詞級（直覺但 OOV 問題）、子詞級 BPE（GPT/BERT 用的折衷方案）。

### Part B：CV 技術

4. **CV 四大任務的判斷標準**：分類=整張圖一個標籤、偵測=Bounding Box+類別、語義分割=像素級但不分個體、實例分割=像素級且分個體。關鍵在「有沒有 bounding box」和「分不分個體」。

5. **ViT 是跨領域的橋樑**：把圖像切成 patch 當 token，用 Transformer 處理。證明 Transformer 不只能做 NLP，也是多模態的基礎。

### Part C：生成式 AI 技術

6. **Transformer 是現代 AI 的共同基礎**：GPT/BERT/ViT/CLIP 都建立在 Transformer 上。Self-Attention 讓每個 token 看所有其他 token。理解它就理解了一半的現代 AI。

7. **模型壓縮三劍客要能區分**：蒸餾=大模型教小模型、剪枝=移除不重要的連接、量化=降低數值精度（FP32→INT8）。記法：蒸餾「教」、剪枝「砍」、量化「降」。

### Part D：多模態 AI

8. **融合三策略的記憶法**：早期融合=特徵層合併（交互充分但計算大）、晚期融合=決策層合併（模組化但錯過低層交互）、注意力融合=Cross-Attention（兼顧兩者）。

---

## 4. 學員常犯錯誤 (Common Pitfalls)

- **Word2Vec 和 TF-IDF 搞混**：Word2Vec 是向量（語義），TF-IDF 是權重（重要度）。
- **語義分割和實例分割搞混**：語義不分個體（所有貓同色），實例分個體（每隻貓不同色）。
- **以為 Transformer 只做 NLP**：ViT、CLIP、多模態都用 Transformer。
- **量化和剪枝搞反**：量化是降數值精度（FP32→INT8），剪枝是移除連接。
- **早期融合和晚期融合選反**：早期 = 特徵層（early in pipeline），晚期 = 決策層（late in pipeline）。
- **物件偵測和實例分割混淆**：偵測輸出 bounding box，分割輸出像素級遮罩。

---

## 5. 提問設計 (Discussion Prompts)

1. 給你一段商品評論，你會用 Word2Vec 還是 TF-IDF 來找出關鍵詞？為什麼？（預期答：TF-IDF，因為它衡量的是詞的重要程度。）

2. 自動駕駛需要知道「前面有三輛車各在哪裡」，該用 CV 四大任務中的哪一個？（預期答：物件偵測或實例分割。需要定位+分個體。）

3. 為什麼 Transformer 能同時用在文字、圖像、多模態？核心機制是什麼？（預期答：Self-Attention 不限定輸入型態，只要能轉成 token 序列就能處理。）

---

## 6. 延伸資源 (Further Reading)

- 《Attention Is All You Need》原始論文（Transformer 奠基之作）
- Stanford CS231n（CV 課程，免費線上）
- Jay Alammar 的 The Illustrated Transformer（視覺化解說）
- iPAS 中級考試範圍公告與歷屆考題
- Hugging Face 官方文件（Tokenization / Model Compression 章節）

---

## 7. 常見 Q&A

**Q1：NLP 的技術細節會考到什麼程度？**
A：考的是技術配對（什麼技術做什麼任務），不考實作細節。例如「情緒分析屬於 NLP 的哪個下游任務」。

**Q2：CNN 的架構差異要背嗎？**
A：記住每個架構的「一句話設計哲學」就夠：VGG=簡單堆疊、Inception=加寬不加深、ResNet=殘差連接。不需要記層數。

**Q3：AutoML 會怎麼考？**
A：以定義題為主——「AutoML 的目的是什麼」「AutoML 能自動化哪些步驟」。不會考 AutoML 的技術細節。
