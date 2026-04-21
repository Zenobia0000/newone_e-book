# F5 · 02_slides_design.md

> 22 張內容投影片設計規格（🖼️ 視覺 / 📣 一句話 / 🎙️ 講者腳本）
> 對應 `slides_build/slides/f5_deck.py` · archetype mix：SILENT 3 / ASK 1 / VS 1 / MATRIX 2 / CONCEPT 1 / CODE 9 / MECHANISM-FLOW 1 / PITFALL 2 / PRACTICE 1 / TABLE 1

---

## F01 · SILENT · 起

- 🖼️ 深綠滿版，白字 hero：「6 小時基礎的終點，不是『你會 OOP』。是你能把 F1-F4 + Pandas 組成一條會跑的管線。」
- 📣 開場立論。
- 🎙️ 今天不教新語法，教你把之前 4 章的零件組起來。

## F02 · ASK · 起

- 🖼️ 大哉問 + 右下資料卡 `3×`：寫成 class 的程式 6 個月後還能用的機率。
- 📣 零散 function vs 鏈式類別，你選哪個？
- 🎙️ DA/DE 現場不是缺會寫 function 的人，是缺會組裝的人。

## F03 · VS · 零散 vs 類別

- 🖼️ 兩欄對比：左「df = load(); df = validate(df); df = clean(df)」；右「cleaner = DataCleaner(path).validate().clean().apply()」。
- 📣 差距不在能不能跑，在 6 個月後能不能改。
- 🎙️ 用共享狀態、錯誤邊界、呼叫語意三個維度對比。

## F04 · MATRIX 2x2 · 狀態 vs 動作

- 🖼️ 四格：狀態（self.path/df）/ 動作（method）/ 鏈式（return self）/ 例外（raise）。
- 📣 先分清誰該存、誰該做、誰該回、誰該爆。
- 🎙️ 這是整章骨架，搞清楚這 4 格，6 個 method 只是把它寫出來。

## F05 · CONCEPT-CARD · 6 個方法簽名

- 🖼️ 全寬 code panel 展示 DataCleaner 六個 method 簽名 + 4 bullet。
- 📣 先寫介面、再寫實作。
- 🎙️ 型別提示（`-> "DataCleaner"`）是鏈式呼叫的前置條件，IDE 才會提示下一步能接什麼。

## F06 · CODE · DataValidationError

- 🖼️ code panel：自訂 Exception class + raise 範例 + except 範例。
- 📣 繼承 Exception，帶 column/reason 兩欄。
- 🎙️ 一個就夠 —— 別學業界流行定義 10 種 Exception，使用者會不知道該 catch 哪個。

## F07 · MECHANISM-FLOW · 六段管線

- 🖼️ flow_chain 六節點：__init__ → validate → clean → apply → eda → export，每節點標 caption。
- 📣 六段成鏈，每段對應你學過的某一章。
- 🎙️ 這張是整章地圖，後面 6 張 CODE 一一展開。

## F08 · CODE · EXAMPLE I/O

- 🖼️ code panel 上半「raw.csv 髒資料四列」，下半「預期輸出 clean.csv + eda.png」。
- 📣 先看輸入/輸出，再看程式碼。
- 🎙️ 強調三種髒資料典型：缺值、異常值、型別錯；輸出要有 _transformed 欄（可追溯）。

## F09 · CODE · __init__

- 🖼️ code panel：pathlib + 讀檔 + fail fast。
- 📣 錯就現在炸，不要讓錯誤延後。
- 🎙️ 標題 label 補「呼應 F3」—— 這是 F3 `__init__` 的實戰版。

## F10 · CODE · validate

- 🖼️ code panel：empty 檢查 + revenue 負值檢查 + raise DataValidationError + return self。
- 📣 業務規則寫成 if。
- 🎙️ 強調「return self 少了就不能鏈式」，現場可以故意漏寫看 traceback。

## F11 · CODE · clean_missing_values

- 🖼️ code panel：strategy 參數（drop / mean）+ raise ValueError。
- 📣 策略化，不要寫死。
- 🎙️ 這是策略模式（Strategy Pattern），但不用講這個名詞，講「把選擇權留給呼叫者」即可。

## F12 · CODE · apply_custom_transform

- 🖼️ code panel：欄位檢查 + df[col].apply(func) + 新增 _transformed 欄 + lambda 使用範例。
- 📣 F2 Lambda 的實戰場。
- 🎙️ func 當參數注入 —— 這就是「把行為傳給物件」，F2 Lambda 不再是玩具。

## F13 · CODE · generate_eda_report

- 🖼️ code panel：select_dtypes + plt.subplots(2,2) + 自動 hist + plt.close + savefig。
- 📣 EDA 不是手畫，是一個 method。
- 🎙️ plt.close 很重要，批次跑 100 個檔不會 OOM。

## F14 · CODE · export_data + 完整鏈式

- 🖼️ code panel：export_data 的 3 行實作 + 完整 5 行鏈式呼叫。
- 📣 這就是 6 小時基礎換來的產物。
- 🎙️ 把鏈式讀出來像英文：「驗證 → 清洗 → 變換 → 報表 → 匯出」。

## F15 · PITFALL · P1/P2/P4

- 🖼️ vs_two_col：業餘寫法 4 條 vs 資深紀律 4 條。
- 📣 return self / fail fast / 別過度設計。
- 🎙️ 這三條是基礎段的工程紀律門檻。

## F16 · PITFALL · P3/P5

- 🖼️ vs_two_col：Exception 濫用 + 只會抄範本 vs 一個 Exception 就夠 + 範本要改造。
- 📣 粗分類 Exception；範本當框架，不當標準答案。
- 🎙️ P5 是隱藏殺手：學員會「看起來會」但換資料集就卡，下一張練習就是在逼他們跨過這門檻。

## F17 · PRACTICE-PROMPT · 改造三任務

- 🖼️ 1x3 matrix：加 method / 加驗證 / 加 EDA 圖，下方倒數條。
- 📣 改得動才算會。
- 🎙️ 5 分鐘計時，要求學員當場改一條 validate 規則出來。

## F18 · SILENT · 段落收束

- 🖼️ 深綠滿版：「能改別人的範本，才算真的會 OOP。能把自己的資料套進去，才算真的過關。」
- 📣 會用到會改，才是真的過關。
- 🎙️ 從「會用」過渡到「會改」的門檻宣言。

## F19 · MATRIX · F1-F5 + S1-S6 能力盤點

- 🖼️ 2x3 matrix 六格：F1 系統 / F2 資料結構 / F3-F4 OOP（highlight）/ F5 整合（highlight）/ S1-S4 資料處理 / S5-S6 視覺化。
- 📣 11 段地基，少一段上面就不穩。
- 🎙️ 你今天能寫 DataCleaner，是因為前 4 章都穩了。

## F20 · TABLE · 下一站五條路

- 🖼️ editorial_table：方向 / 推薦起點 / 什麼時候該選它。SQL / sklearn / Polars+DuckDB / Airflow / Cloud。
- 📣 挑一條走 3 個月。
- 🎙️ 別五條都開坑；3 個月後你會是那個主題的可靠同事。

## F21 · CODE · 結業三句忠告

- 🖼️ code panel（用註解形式寫三條紀律）：跑起來不算 / 最強優化是不做 / OOP 不是萬靈丹。
- 📣 Linus 實用主義版。
- 🎙️ 這三條內化了，下一份工作直接用。

## F22 · SILENT · 結業

- 🖼️ 深綠滿版：「6 小時基礎段到此收束。你今天寫出的 DataCleaner，就是 F1-F5 的結業證書。下一站 —— 選一條路，3 個月後見。」
- 📣 結業不是終點，是實戰段的起跑線。
- 🎙️ 鞠躬。這是 F1-F5 基礎段的完結，也是銜接 S1-S6 實戰段的交棒點。
