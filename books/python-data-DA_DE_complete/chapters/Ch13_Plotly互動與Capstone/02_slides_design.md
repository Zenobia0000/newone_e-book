# S6 · 02_slides_design.md

> 24 張內容投影片設計規格（🖼️ 視覺 / 📣 一句話 / 🎙️ 講者腳本）

---

## S01 · SILENT · 起

- 🖼️ 深綠滿版，白字 hero：「12 小時的終點，不是『你會用 Plotly』。是你能獨立把一份髒 CSV 變成老闆願意轉寄的 dashboard。」
- 📣 收斂章開場定錨。
- 🎙️ 今天是最後一章，語法只佔三成，產品思維佔七成。

## S02 · ASK · 起

- 🖼️ 大哉問 + 右下資料卡：stat「80%」caption「老闆轉寄的是 HTML，不是 notebook」。
- 📣 從使用者視角問：你會交一個 .py 還是一份 dashboard.html？
- 🎙️ DA 的終端使用者是非技術主管，他不跑 Python，他點連結。

## S03 · MATRIX 2x2 · 靜態 vs 互動

- 🖼️ 四格：展示媒介 / hover 能力 / 檔案大小 / 場景。
- 📣 靜態與互動不是誰取代誰，是場景選擇。
- 🎙️ 投影片用 .png；但 email 轉寄、內網公告要 .html。

## S04 · VS · .png vs .html

- 🖼️ 兩欄對比：matplotlib.savefig vs plotly.write_html。
- 📣 互動圖的本質是「帶 JS 的單一 HTML」。
- 🎙️ write_html 輸出可直接寄，對方不需裝 Python。

## S05 · MATRIX 2x2 · express vs graph_objects

- 🖼️ 四格：高階一行 / 底層客製 / subplot 支援 / 學習曲線。
- 📣 px 畫圖，go 組圖，兩者分工。
- 🎙️ make_subplots 一定要搭 go，這是本章最常問的問題。

## S06 · CODE · px.line + px.bar

- 🖼️ 左側 code panel，右側 4 個重點 bullet。code 展示時序營收 + 類別銷售。
- 📣 時間選 line，類別選 bar。
- 🎙️ 強調 labels 參數讓圖「自己會說中文」。

## S07 · CODE · px.scatter + px.box

- 🖼️ code panel：scatter 加 trendline="ols"；box 加 color 分群。
- 📣 關聯用 scatter + 趨勢線；分布看分群差異用 box。
- 🎙️ hover_data 只挑 2~3 欄最有商業意義的。

## S08 · CODE · px.histogram + px.pie

- 🖼️ code panel：hist bins 與 pie 的 hole 參數（donut）。
- 📣 次數看 hist，占比看 pie（但超過 5 類就別用 pie）。
- 🎙️ pie 的 type 是 domain，埋下 S10 的伏筆。

## S09 · SILENT · 承

- 🖼️ 深綠滿版：「一行畫一張，是 Plotly Express 的承諾。複雜的組裝，才是 make_subplots 的舞台。」
- 🎙️ 過渡到 Part B 整合段。

## S10 · PITFALL · 踩雷一 · domain vs xy

- 🖼️ 用 vs_two_col：左「錯誤寫法 specs=[[{}, {}]]」→ 報錯訊息；右「正確 specs=[[{'type':'xy'}, {'type':'domain'}]]」。
- 📣 pie/sunburst 是 domain 型，specs 必須標註。
- 🎙️ 這是本章最常出錯的點，背起來。

## S11 · CODE · make_subplots 2x2

- 🖼️ 完整 code：subplot_titles + specs + add_trace(go.Bar(...)，注意不要直接 add px.Figure。
- 📣 組裝順序：建骨架 → add_trace → update_layout。
- 🎙️ 強調 row/col 參數，不寫會全部疊在 (1,1)。

## S12 · PITFALL · 踩雷二 · px 不是 trace

- 🖼️ vs_two_col：左「錯：fig.add_trace(px.bar(...))」；右「對：fig.add_trace(go.Bar(...)) 或 fig.add_trace(px.bar(...).data[0])」。
- 📣 px 回傳 Figure；要的是它裡面的 trace。
- 🎙️ 教學生用 .data[0] 這招救場。

## S13 · MECHANISM-FLOW · Capstone 五站

- 🖼️ flow_chain 五節點：read → clean → merge+agg → subplots → write_html。每站 caption 標關鍵 API。
- 📣 這條管線是 S1-S6 十二小時能力的總和。
- 🎙️ 強調不要 import 舊 notebook，從頭寫才學得會。

## S14 · CODE · load_and_clean_orders

- 🖼️ code panel：pd.read_csv + to_datetime(errors='coerce') + dropna + astype。
- 📣 coerce 是本函式的靈魂。
- 🎙️ 髒日期遇到直接噴錯是新手之痛，coerce 讓它變 NaT 再處理。

## S15 · CODE · merge + KPIs

- 🖼️ code panel：merge orders × products → groupby 月 → agg revenue/qty。
- 📣 S3 的 groupby + merge 在這裡回報。
- 🎙️ KPI 要落到一個乾淨的 monthly_df，接下來畫圖用它。

## S16 · CODE · 4 張子圖組裝

- 🖼️ code：subplot_titles=["月營收","品類","散點","占比"]，specs 含一格 domain。
- 📣 2x2 是業界儀表板的預設版型。
- 🎙️ 把 S14+S15 的 df 灌進去，四張同時活起來。

## S17 · CODE · write_html

- 🖼️ code：fig.update_layout(height, title) → fig.write_html(Path(out).absolute())。
- 📣 一行交付。
- 🎙️ 絕對路徑 + include_plotlyjs='cdn' 可以讓檔案縮小到 50KB。

## S18 · PITFALL · 踩雷三 · 路徑 + hover 爆版

- 🖼️ vs_two_col：左「相對路徑打不開 / hover_data 塞 10 欄變資訊牆」；右「絕對路徑 + hover_data 只留 2-3 欄商業語意」。
- 📣 便利性的設計才是專業。
- 🎙️ 給主管看的圖，hover 一格要能自己說話。

## S19 · TABLE · Grading Rubric

- 🖼️ editorial_table：技術完成度 40% / 洞察品質 30% / 視覺呈現 20% / 口語表達 10%。
- 📣 分數拆解就是交付優先序。
- 🎙️ 學生最常拿 B 是因為沒有具體數字結論。

## S20 · PRACTICE-PROMPT · 三問

- 🖼️ draw_ask_page 變形：列出 3 個必答問題，下方 30 秒倒數視覺。
- 📣 發現 → 下一步 → 應用場景。
- 🎙️ 這套 30 秒模板未來 standup 也會用。

## S21 · VS · 迷思 vs 紀律

- 🖼️ 左「跑得起來就好 / 圖越多越好 / hover 越詳細越好」；右「能寄出去給主管才算成品 / 4 張足以講完故事 / hover 只留商業關鍵」。
- 🎙️ DA 交付紀律 = 為收件者設計。

## S22 · PYRAMID · S1-S6 能力盤點

- 🖼️ matrix 2x3 模擬六層：S1 NumPy / S2 Pandas IO / S3 Transform / S4 時序EDA / S5 視覺化 / S6 Plotly+整合。
- 📣 少一層，上面就不穩。
- 🎙️ 你今天能寫 dashboard，是因為前五週都穩了。

## S23 · TABLE · 下一站五條路線

- 🖼️ editorial_table：方向 / 推薦起點 / 一句話。Streamlit / Dash / SQL / Cloud / ML。
- 🎙️ 挑一條走 3 個月，你就超過 80% 的同業。

## S24 · SILENT · 結業

- 🖼️ 深綠滿版：「把髒 CSV 變成老闆願意轉寄的 dashboard —— 這才是 DA 的商業價值。12 小時結束了，從今天起，寫給非技術主管看。」
- 🎙️ 鞠躬。
