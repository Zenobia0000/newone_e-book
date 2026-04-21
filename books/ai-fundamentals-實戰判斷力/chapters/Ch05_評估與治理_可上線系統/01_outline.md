# Ch05 講師講稿 — 評估與治理：可上線系統

> 節次時長：120 分鐘（講授 80 + 討論演練 30 + 總結回顧 10）
> Governing thought：「AI 系統不是能跑就好，而是能不能被信任。」

---

## 1. 本節目標

1. 區分 offline/online × human/auto 四象限評估，知道何時用哪一種。
2. 學會建立結構化測試集並做版控（dataset versioning），不靠感覺驗收。
3. 能用 failure taxonomy 五類（資料錯、retrieval 錯、推理錯、工具錯、格式錯）快速定位根因。
4. 掌握上線前 checklist：safety policy、rollback / fallback、observability。
5. 辨識治理最小集：hallucination、privacy / data leakage、copyright、prompt injection。
6. 設計 KPI 組合與小規模試點流程，完成「從 demo 到上線」的最後一哩路。

## 2. 時間切分表（80 + 30 + 10）

| 時間 | 區段 | 內容 |
|---|---|---|
| 0~5 | 講授 | 開場定錨：為什麼 AI 專案最大風險不在技術，在信任 |
| 5~15 | 講授 | Part A：Eval 四象限（offline/online × human/auto） |
| 15~25 | 講授 | 結構化測試集 vs vibe-based eval；dataset versioning |
| 25~40 | 講授 | Part B：Failure taxonomy 五類 + 對應修正手段 |
| 40~50 | 講授 | Observability 三支柱：trace / logs / metrics |
| 50~65 | 講授 | Part C：上線流程（shadow → canary → GA → rollback） |
| 65~80 | 講授 | Part D：治理最小集（hallucination / privacy / copyright / prompt injection） |
| 80~95 | 演練 | 學員分組：為指定情境撰寫上線 checklist + KPI 組合 |
| 95~110 | 討論 | 各組報告 + 講師補充 evaluation blind spots 與 human-in-the-loop |
| 110~120 | 總結 | Ch00-Ch05 六章回顧 + 下一步行動建議 |

## 3. 關鍵教學點

### Part A：Eval 四象限

- **Offline + Auto**：跑測試集、比對預期輸出（如 exact match、BLEU、ROUGE）。最便宜、最快、但覆蓋面最窄。
- **Offline + Human**：人工標註評分（如 Likert scale）。品質高但昂貴且慢。
- **Online + Auto**：上線後用 metrics 自動監控（成功率、延遲、token 成本）。
- **Online + Human**：收集使用者回饋（thumbs up/down、CSAT 問卷）。最真實但有延遲。
- **核心訊息**：四種不是選一種，而是組合使用。OpenAI evals 的原則——「早做、常做、針對任務做」。

### Part B：Failure Taxonomy

- **資料錯**：輸入資料品質差、格式異常、缺值。→ 修正：資料清洗 + 輸入驗證。
- **Retrieval 錯**：RAG 取回不相關或過時文件。→ 修正：chunk 策略 + embedding 品質 + reranker。
- **推理錯**：模型邏輯推導失誤、hallucination。→ 修正：prompt 改寫 + few-shot + chain-of-thought。
- **工具錯**：function calling 呼叫錯誤工具或傳錯參數。→ 修正：tool schema 約束 + 輸出驗證。
- **格式錯**：回覆格式不符預期（JSON 壞掉、多餘文字）。→ 修正：structured output + 後處理 parser。
- **教學要點**：出錯時先分類再修，不要一股腦改 prompt。

### Part C：上線流程與退路

- **Shadow mode**：新系統與舊系統並行，新系統的結果不給使用者看，只用來比對。
- **Canary release**：先給 5-10% 使用者試跑，監控指標穩定再放量。
- **GA（General Availability）**：全量上線。
- **Rollback**：版本回退到上一版（緊急時用）。
- **Fallback**：AI 無法處理時自動降級（如轉人工、給預設回覆）。
- **關鍵區別**：rollback 是「退回上一版」，fallback 是「走備用路徑」。兩者都要在上線前設計好。

### Part D：治理最小集

- **Hallucination / Confabulation**：模型編造不存在的事實。防線：grounding（RAG）、citation、confidence threshold。
- **Privacy / Data Leakage**：使用者個資外洩、訓練資料被反推。防線：PII 遮蔽、存取控制、logging 脫敏。
- **Copyright / IP**：生成內容侵犯智財權。防線：來源標註、使用條款、人工審查高風險輸出。
- **Prompt Injection**：使用者透過惡意輸入操控系統行為。防線：input sanitization、system prompt 隔離、output filtering。
- **參考框架**：NIST AI 600-1 GenAI Profile — 把可信度考量放進 AI 設計、開發、使用與評估。

## 4. 演練設計（30 min）

### 情境題

> 你的公司要上線一個「內部知識庫 QA Bot」，用 RAG 架構，回答員工關於 HR 政策的問題。請為這個系統設計：
> 1. Eval 策略（從四象限各選至少一種方法）
> 2. 上線前 checklist（至少 8 項）
> 3. KPI 組合（至少 5 個指標 + 各自的警戒線）
> 4. 出錯時的 fallback 方案

### 分組方式

- 3-4 人一組，15 分鐘討論 + 撰寫，10 分鐘報告，5 分鐘講師補充。
- 講師補充重點：evaluation blind spots（測試集沒覆蓋的邊界條件）、human-in-the-loop（何時該把決策權交回人類）。

## 5. 學員常犯錯誤

1. **只做 offline eval 就上線**：測試集表現好不代表實際使用者場景都覆蓋，一定要有 online eval 持續監控。
2. **測試集太小或不做版控**：10 題測完就上線，三個月後改了 prompt 回不去原來的 baseline。
3. **出錯只說「AI 不準」**：不分類就沒有改善方向，用 failure taxonomy 五分法是最小可行分類。
4. **沒有 rollback / fallback**：出事只能全線停機，對業務衝擊巨大。
5. **忽略 prompt injection**：上線第一天就被使用者套出 system prompt，信任崩塌。
6. **Logging 沒做脫敏**：把使用者對話完整存進 log，違反隱私法規。

## 6. 提問設計

1. 「你的 AI 系統上線第一天就回答錯誤，老闆問你『怎麼回事』，你會怎麼回答？用 failure taxonomy 的語言。」
2. 「如果測試集有 100 題全部通過，你敢上線嗎？還缺什麼？」
3. 「Rollback 和 fallback 差在哪？各給一個實際場景。」

## 7. 延伸資源

- NIST AI 600-1 GenAI Profile（搜尋 "NIST AI 600-1"）。
- OpenAI Evals Guide（搜尋 "OpenAI evals guide"）。
- Anthropic 的 RAG 與 Prompt Engineering 最佳實踐。
- 《Building LLM Apps》（Chip Huyen）中的 eval 與 monitoring 章節。

## 8. 常見 Q&A

- **Q：小公司沒有專門的 AI 治理團隊，怎麼辦？**
  A：治理不一定需要獨立團隊。最小做法：一份 checklist + 一個負責人 + 定期 review。NIST AI 600-1 可以當 checklist 的起點。
- **Q：Eval 要做到多少題才夠？**
  A：沒有絕對數字，但原則是：覆蓋主要使用場景 + 已知邊界條件 + 歷史出錯案例。50-200 題是常見的起步範圍，重點是持續增補。
- **Q：Hallucination 能完全消除嗎？**
  A：目前技術無法 100% 消除。策略是降低頻率（grounding、RAG）+ 偵測（citation check、confidence score）+ 人工兜底（human-in-the-loop）。
- **Q：Prompt injection 有銀彈嗎？**
  A：沒有銀彈。多層防禦：input sanitization、system/user prompt 隔離、output filtering、權限最小化。持續更新攻防知識。

## 9. 收斂金句

「AI 專案的終點不是 demo day，而是上線第 30 天還穩定可用。能跑是工程師的事，能被信任是整個組織的事。六章課程走完，你已經有了從問題定義到可上線系統的完整判斷框架——下一步，選一個真實場景，跑一輪。」
