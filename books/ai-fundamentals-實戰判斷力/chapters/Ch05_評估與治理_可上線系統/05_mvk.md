# Ch05 · Minimum Viable Knowledge（MVK）

> 若只記得 10 件事，這就是 Ch05 的精華。

---

## Eval 四象限（offline/online x human/auto）

| | Human | Automatic |
|---|---|---|
| **Offline** | 人工標註評分（Likert scale、A/B 盲測）。品質高但貴且慢。 | 測試集自動跑（exact match、BLEU、ROUGE、LLM-as-judge）。最便宜最快，覆蓋面窄。 |
| **Online** | 使用者回饋（thumbs up/down、CSAT 問卷）。最真實但有延遲。 | Metrics 自動監控（成功率、延遲、token 成本、異常偵測）。即時但看不到品質細節。 |

**原則**：四種不是選一種，是組合使用。早做、常做、針對任務做（OpenAI evals）。

---

## Failure Taxonomy 五類

| 錯誤類型 | 典型症狀 | 修正手段 |
|---|---|---|
| **資料錯** | 輸入格式異常、缺值、過時資料 | 資料清洗 + 輸入驗證 + schema check |
| **Retrieval 錯** | RAG 取回不相關或過時文件 | chunk 策略優化 + embedding 品質 + reranker |
| **推理錯** | 模型邏輯推導失誤、hallucination | prompt 改寫 + few-shot + chain-of-thought |
| **工具錯** | function calling 呼叫錯誤工具或傳錯參數 | tool schema 約束 + 輸出驗證 + retry |
| **格式錯** | 回覆格式不符預期（JSON 壞掉、多餘文字） | structured output + 後處理 parser |

**記憶口訣**：資料 → 取回 → 推理 → 工具 → 格式，從輸入到輸出逐層排查。

---

## 上線前 Checklist（10 項）

- [ ] 1. 結構化測試集建立且通過率達標（≥ 90%）
- [ ] 2. Failure taxonomy 已分類，已知問題已修正
- [ ] 3. Observability 已接入（trace + logs + metrics）
- [ ] 4. Rollback 腳本已測試，可在 5 分鐘內退回上一版
- [ ] 5. Fallback 路徑已驗證（AI 掛了使用者不會卡死）
- [ ] 6. Safety policy 已定義（什麼能回答、什麼不能回答）
- [ ] 7. PII 脫敏已實作（logging 不存完整個資）
- [ ] 8. Prompt injection 防禦已測試（至少跑過 10 種攻擊模式）
- [ ] 9. Logging 符合法規（GDPR / 個資法相關要求）
- [ ] 10. KPI 警戒線已設定，超標自動告警

---

## 治理最小集（四道關卡）

### 1. Hallucination / Confabulation
- **風險**：模型編造不存在的事實，使用者信以為真。
- **防線**：Grounding（RAG + citation）、confidence threshold、human-in-the-loop 審核高風險輸出。

### 2. Privacy / Data Leakage
- **風險**：使用者個資外洩、訓練資料被反推。
- **防線**：PII 遮蔽（NER + regex）、存取控制、logging 脫敏、資料保留政策。

### 3. Copyright / IP
- **風險**：生成內容侵犯智財權。
- **防線**：來源標註、使用條款明確、人工審查高風險輸出、避免 verbatim 複製。

### 4. Prompt Injection
- **風險**：使用者透過惡意輸入操控系統行為、洩漏 system prompt。
- **防線**：Input sanitization、system/user prompt 隔離、output filtering、權限最小化。

---

## KPI 組合（五個必追指標）

| KPI | 定義 | 警戒線範例 |
|---|---|---|
| 成功率 | 回答正確且完整的比例 | > 90% |
| P95 延遲 | 95% 請求的回應時間 | < 3 秒 |
| 單次成本 | 每次請求的 token + API 費用 | < $0.05 |
| 使用者滿意度（CSAT） | thumbs up 比例或 1-5 分評分 | > 4.0 / 5.0 |
| 風險事件率 | hallucination / 違規回答的比例 | < 0.1% |

---

## 上線部署四階段

1. **Shadow**：新系統與舊系統並行，新系統結果不給使用者看，只用來比對差異。
2. **Canary**：先給 5-10% 使用者試跑，監控指標穩定再放量。
3. **GA（General Availability）**：全量上線，持續監控。
4. **Rollback**：指標異常時版本回退到上一版（5 分鐘內完成）。

**Rollback vs Fallback**：Rollback 是退回上一版（版本維度），Fallback 是走備用路徑（功能維度，如轉人工）。兩者都要在上線前設計好。

---

## 課程總結：Ch00-Ch05 六章能力堆疊

| 層級 | 章節 | 核心能力 |
|---|---|---|
| 1. 全局判斷 | Ch00 | AI 四大流派邊界 + 專案生命週期 |
| 2. 統計底盤 | Ch01 | 假設檢定、A/B test、因果 vs 相關 |
| 3. ML 主戰場 | Ch02 | 表格資料、feature engineering、tree-based |
| 4. DL 表徵學習 | Ch03 | Tensor、CNN/RNN/Transformer 問題分工 |
| 5. GenAI 系統 | Ch04 | Prompt / RAG / Tools / Agents / Evals |
| 6. 評估與治理 | Ch05 | Eval 四象限 + Failure taxonomy + 上線 checklist |

**底層越穩，上層越能長。六章走完，你有了從問題定義到可上線系統的完整判斷框架。**

---

## 結語金句

> 「AI 專案的終點不是 demo day，而是上線第 30 天還穩定可用。AI 系統不是能跑就好，而是能不能被信任。」
