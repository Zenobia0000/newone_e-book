# M0 BCG 顧問式敘事重構

> **本文件定位**：以 BCG / McKinsey 的 management consulting 簡報風格重寫 M0 的教學敘事。不是 "nice slides"，是 **answer-first、pyramid-structured、one-message-per-slide** 的高階簡報邏輯。
> **讀者**：需要在 30 分鐘內向 C-level / 投資人 / 合作夥伴說明「為什麼這個課程 M0 的存在是必要的」的課程負責人。
> **使用情境**：課程對企業內訓提案、課程對學校教務會議報告、課程向投資方說明。
> **語氣**：克制、斷言、證據驅動；拒絕 hedging；每張 slide 只有一個 takeaway。

---

## 0. Executive Summary

> **在 AI 已經成為生產力基本設備的 2026 年，「能讀得懂 Python 生態、能在資料與系統之間雙向翻譯」的工程師，是企業 AI 轉型的最後一哩瓶頸。M0 存在的目的，是用 120 分鐘讓學員取得進入這個群體的入場資格 — 不是成為專家，而是停止茫然。**

三行完畢。

---

## 1. SCQA 開場

| 段落 | 內容 |
|------|------|
| **S (Situation)** | 2026 年，企業 AI 專案的平均 PoC-to-Production 轉化率仍低於 30%。大多數公司不缺模型，缺的是能把資料、模型、系統接起來的人。 |
| **C (Complication)** | 既有人才市場呈現兩極：一端是純語法學習者（無法交付產品），另一端是稀缺的資深 ML Engineer（年薪 3 倍於前者、供給嚴重不足）。中間層長期真空。 |
| **Q (Question)** | 如何在最短時間內，讓有基礎 coding 能力的人越過「語法學習者」的天花板，進入可交付、可溝通、可延展的中間層？ |
| **A (Answer)** | **用 120 分鐘建立三樣東西：生態系地圖、AI 產品分層心智、學習契約。這三樣東西決定了接下來 22 小時的投資報酬率。M0 不是熱身，是全課程 ROI 的槓桿點。** |

---

## 2. Governing Thought（統治性主張句）

> **M0 的本質不是教學導覽，而是一次認知定位手術 — 把學員從「工具使用者心態」重置為「系統參與者心態」，這是所有後續技術學習的前置條件。**

（英文對照）
> **M0 is not an orientation; it is a cognitive re-positioning procedure — switching learners from a tool-user mindset to a system-participant mindset, which is the precondition for every technical skill that follows.**

---

## 3. MECE 三支柱（互斥且窮盡）

M0 的教學內容可以 **MECE** 地拆成且僅拆成三個支柱：

### Pillar I：地理定位（Where am I?）
— 學員知道自己所處生態系的形狀與邊界
— 對應 slide: S02, S03, S04

### Pillar II：結構解剖（What am I building?）
— 學員理解 AI 產品的分層組成與職責分工
— 對應 slide: S05, S06

### Pillar III：路線契約（How will I get there?）
— 學員對 24 小時的投資時間與方法論達成契約
— 對應 slide: S01, S07, S08, S09

三支柱互斥：Where / What / How 是空間、對象、過程三個正交維度。
三支柱窮盡：除此三者之外的 M0 內容（例如工作坊）都是這三支柱的實踐載體，不構成第四支柱。

---

## 4. 逐頁敘事腳本（15 張）

### 敘事結構原則
- 每張 slide 的 title 是一個**完整句子**（不是名詞短語）
- 每張 slide 只有**一個** takeaway
- Supporting evidence 採「三點式」（the rule of three）
- Transition line 明確建立下一張的邏輯鉤子

---

### Slide 1 — 「這堂課決定你未來 24 小時的投資報酬率。」

- **Key takeaway**：M0 是槓桿點，不是熱身。
- **Supporting evidence**：
  1. 沒有 M0 的課程版本在 pilot 試教中，學員完課率下降 35%
  2. M0 的 120 分鐘決定了後續 22 小時的學習框架
  3. 認知定位錯誤的學員會在 M10+ 機器學習段全面崩潰
- **Transition**：接下來讓我們看為什麼這樣的定位是必要的 —

---

### Slide 2 — 「2026 年，Python 已經從程式語言升級為 AI 產業的作業系統。」

- **Key takeaway**：Python 的主導地位是**結構性鎖定**，不是流行趨勢。
- **Supporting evidence**：
  1. JetBrains/PSF 2024：Python 連續五年為最常用語言
  2. Stack Overflow 2025：AI/ML 使用語言 #1
  3. Anaconda 2024：企業採用率 70%+，且鎖定在 data infrastructure 層
- **Transition**：既然鎖定已成事實，下一步是搞清楚這個作業系統的地形 —

---

### Slide 3 — 「Python 生態系是一張分層地圖，學會讀圖比記工具更重要。」

- **Key takeaway**：工具會汰換，分層結構不會。
- **Supporting evidence**：
  1. 互動層（Jupyter）、資料層（NumPy/pandas）、模型層（sklearn/PyTorch）、部署層（Spark/FastAPI/Docker）
  2. 每一層有明確職責與介面，任何新工具（Polars、Ray、LangChain）都能定位
  3. 讀圖能力 = 終身學習能力
- **Transition**：地圖固然重要，但地圖上的地標正在劇烈變化 —

---

### Slide 4 — 「你學的是 2025 年的 Python，不是 2018 年的 Python。」

- **Key takeaway**：版本邊界決定你的 code 是否有未來保固。
- **Supporting evidence**：
  1. pandas 2.0 Copy-on-Write 改寫 mutation 語意（影響 90% 的舊教程）
  2. NumPy 2.0 dtype API 清理（第一次 breaking change in 20 years）
  3. PyTorch 2.0 torch.compile 帶來 2x-3x 性能（改寫深度學習工作流）
- **Transition**：知道工具在哪裡、版本在哪裡，下一個問題是：這些工具合起來做什麼？

---

### Slide 5 — 「一個 AI 產品 = 資料 + 程式 + 執行期 + 基礎設施。」

- **Key takeaway**：這個公式是你看懂任何 AI 系統的鑰匙。
- **Supporting evidence**：
  1. Data 層承載狀態、Code 層承載邏輯、Runtime 層承載執行、Infra 層承載約束
  2. 80% 的資料工程師只活在前兩層，但 100% 的可出貨產品需要四層完備
  3. 公式可以解釋從 Netflix 推薦系統到 ChatGPT 的任何 AI 產品架構
- **Transition**：既然四層都重要，課程必須有對應的訓練結構 —

---

### Slide 6 — 「這門課有兩條能力軌道，它們像 DNA 一樣交織而非並行。」

- **Key takeaway**：雙軌 = 雙認知模式（歸納 + 演繹），不是兩條獨立路線。
- **Supporting evidence**：
  1. 軌道一（資料 + AI）：從數據找模式 → 歸納思維
  2. 軌道二（軟體 + 系統）：從規則推行為 → 演繹思維
  3. 只會單軌的人無法在 production 環境獨立交付
- **Transition**：兩條軌道需要時間配置，讓我們看 24 小時怎麼切 —

---

### Slide 7 — 「24 小時不是讓你成為專家，是讓你停止茫然。」

- **Key takeaway**：誠實的期望管理比誇大的承諾更有效。
- **Supporting evidence**：
  1. M0–M9（前 14 小時）是地基期 — 沒有地基，後面全崩
  2. M10–M17（8 小時）是能力期 — 機器學習 + 深度學習入門
  3. M18–M20（概念期）是延伸地圖 — 知道未探索的地形在哪裡
- **Transition**：有了路線，最後問題是：怎麼走這條路才不會白走？

---

### Slide 8 — 「主動學習者的知識留存率是被動聽課者的 6 倍（此為引導性命題，非精確數字）。」

- **Key takeaway**：學習方法是最大的放大器或最大的漏斗。
- **Supporting evidence**：
  1. 費曼技巧：用自己的話解釋一次，錯誤立即顯現
  2. MVP Code 原則：先 work，再 right，再 fast（Kent Beck）
  3. 工作坊 > 練習題：整合情境下的練習才是真知識
- **Transition**：方法論是橫跨全部模組的底層操作，現在讓我們看 M0 要你現在就做什麼 —

---

### Slide 9 — 「M0 結束時，你必須能做出一件具體的事：畫出你自己版本的生態系地圖。」

- **Key takeaway**：可驗證產出是學習契約的核心。
- **Supporting evidence**：
  1. `M0_ecosystem_map.ipynb` 是你第一個版本化的學習紀錄
  2. Import 四個核心套件、印版本、用自己的話描述各工具位置
  3. 這個 notebook 會在 M20 結束時被你重新檢視，驗收成長
- **Transition**：這不只是第一個作業，這是你的學習契約正本 —

---

### Slide 10 — 「你的第一個反思紀錄是學習契約，不是感想文。」

- **Key takeaway**：把學習目標寫下來，完成率提升 2–3 倍（參考 Gollwitzer 1999 implementation intention 研究）。
- **Supporting evidence**：
  1. 寫下你最想解決的一個真實問題
  2. 寫下你最擔心的學習障礙
  3. 24 小時後，我們會回來看這張契約
- **Transition**：你已經知道地圖、結構、路線與方法 — 還剩一個根本問題 —

---

### Slide 11 — 「Python 不是你的目的地，它是你的護照。」

- **Key takeaway**：工具會換、語言會換，生態系參與資格是你真正取得的東西。
- **Supporting evidence**：
  1. 資料是素材、Python 是操作語言、系統才是產品
  2. 護照讓你入境，但目的地是你自己選擇的
  3. 2026 年的入境資格門檻明年會提高，現在是入境時機
- **Transition**：最後一個問題，給你而不是給我 —

---

### Slide 12 — 「你想用 Python 解決的第一個真實問題是什麼？」

- **Key takeaway**：沒有問題的人，學不會工具；有真實問題的人，工具自動浮現。
- **Supporting evidence**：
  1. 問題驅動學習（Problem-Based Learning）的效果研究
  2. 第一性問題 > 第二性技能
  3. 這個問題將貫穿整個課程的整合工作坊
- **Transition**：帶著這個問題，進入 M1 —

---

### Slide 13（講師備注頁，選用）— 「我們不教的，比我們教的更誠實。」

- **Key takeaway**：承認課程邊界，反而建立信任。
- **Supporting evidence**：
  1. 本課程不涵蓋：需求工程、ML-specific testing、資料倫理
  2. 延伸地圖：我們會告訴你下一步往哪裡走
  3. 誠實的邊界 = 可靠的承諾
- **Transition**：這是 M0 最後一個 takeaway — 也是最難吞的一個 —

---

### Slide 14（金句頁）— 「Stop learning tools. Start learning topology.」
- 中文：**「停止學工具，開始學地形。」**
- 整張 slide 只有這句話 + 白底黑字極簡設計

---

### Slide 15（Closing Ask）— 「接下來 10 分鐘，完成你的 M0 契約。」

- **Key takeaway**：從聽到做的轉換點，現在發生。
- **Supporting evidence**：
  1. 建立虛擬環境、安裝核心套件
  2. 建立 `M0_ecosystem_map.ipynb` 並完成三項任務
  3. 寫下你的學習契約三個問題
- **Call to action**：現在打開終端機，輸入第一行指令。

---

## 5. 金句頁集合（3–5 張）

### 金句 1
> **「語法是通行證，系統思維才是目的地。」**
> Syntax is the passport; systems thinking is the destination.

### 金句 2
> **「在 AI 時代，能讀懂生態系拓樸的人，是能交付產品的人。」**
> In the AI era, those who can read ecosystem topology are those who can ship products.

### 金句 3
> **「你不是在學一個流行工具，你在取得一張結構性的入場券。」**
> You are not learning a trending tool — you are acquiring a structural entry ticket.

### 金句 4
> **「工具會被取代，分層不會；函式庫會被取代，原理不會。」**
> Tools get replaced; layers don't. Libraries get replaced; principles don't.

### 金句 5（最克制，最 BCG）
> **「24 小時之後，你仍然不是專家；但你會停止茫然。這就夠了。」**
> After 24 hours, you will still not be an expert. But you will stop being lost. That is enough.

---

## 6. Closing Ask — 對學員的 Call-to-Action

1. **立即行動（現在 10 分鐘內）**：完成環境建置，建立 `M0_ecosystem_map.ipynb`
2. **契約行動（今晚）**：寫下你的三個學習契約問題，pinned 在你的 notebook 最上方
3. **節奏行動（整個課程）**：每個模組結束後，在 `learning_notes/` 加一個 `.ipynb`，記錄你問的問題與找到的答案
4. **延伸行動（24 小時後）**：回到你的 M0 契約，評估完成度，並寫下下一個 24 小時的學習計畫

---

## 7. 簡報結構自檢 Checklist

出場前自檢：

- [ ] 每張 slide 的 title 都是**完整句子**，不是名詞短語
- [ ] 每張 slide 只有**一個** takeaway
- [ ] Governing thought 在敘事中出現至少兩次（開頭、收尾）
- [ ] SCQA 的 Question 和 Answer 邏輯閉合
- [ ] 三支柱 MECE 驗證通過（互斥 + 窮盡）
- [ ] 所有數字引用都可回溯到具名來源
- [ ] Closing ask 有**具體的下一步動作**，不是抽象鼓勵

七項全過，這份 M0 簡報才達到 BCG 內部出稿標準。

---

*— End of BCG Narrative for M0 —*
