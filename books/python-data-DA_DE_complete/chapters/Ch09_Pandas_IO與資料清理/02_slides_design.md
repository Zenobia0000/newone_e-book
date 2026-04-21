---
session: S2
title: Pandas I/O 與資料清理
total_content_slides: 23
style: 教學型 · Editorial-strict
primary: "#1B5E3F" · pitfall: "#C62828" · confirm: "#2E7D32"
---

# S2 · Pandas I/O 與資料清理 — 設計稿

> 三格結構：🖼️ 畫面 / 📣 畫面上的字 / 🎙️ 講者這時說
> 對齊 teacher_notes §1 Learning Objectives、§3 Key Teaching Points、§4 Common Pitfalls、§5 Discussion Prompts

---

## S1 · SILENT · Motivation

- 🖼️ 全深綠背景，中央白色 hero statement。
- 📣 「資料科學家 80% 時間在清資料。\n這一節，把 SOP 刻進肌肉。」
- 🎙️ 這句不是唬人——是 Kaggle 調查的真實比例。多數人把 Pandas 當 API 字典背，我們今天反過來：先建立『拿到新檔案』的 SOP，API 只是肌肉後面的關節。

## S2 · ASK · Hook（對應 Learning Objective 2）

- 🖼️ 白底，大問句置中；右下 data card「Kaggle 2024 · 80%」。
- 📣 「拿到一份新 CSV，你的第一個指令是什麼？」
- 🎙️ 如果你第一時間想到 `df = pd.read_csv(...)` 就打完收工，那你的後面 80% 時間會在補救這一行的副作用。好的 DE/DA 會先問五件事：shape、head、info、describe、isna。今天這張投影片的答案，會在 S5 揭曉。

## S3 · CONCEPT MATRIX 2×3 · DataFrame/Series/Index 三件套（LO 1）

- 🖼️ 2×3 matrix：Series / DataFrame / Index；對齊 / 不可變 / set-reset_index。
- 📣 標題「DataFrame / Series / Index：Pandas 的三件套心智模型」。
- 🎙️ 把這三個記清楚，後面 merge、groupby 都是它的變奏。Index 是關鍵——它不是欄位、不是 row number，是對齊的根據。Excel 沒這個概念，所以從 Excel 轉來的同學最容易卡在這裡。

## S4 · CONCEPT CODE · Index 對齊示範（LO 1）

- 🖼️ 左 code panel：兩個 Series 相加，依 Index 對齊產生 NaN；右 bullet 說明。
- 📣 「Index 不是欄位——它是對齊與合併的根據。」
- 🎙️ 看 s1+s2——位置完全對不上，但 pandas 靠 Index 名字對齊。這就是 merge 底層。理解這張圖，Pandas 你已經懂 50%。

## S5 · CONCEPT CODE · 建立 + 五件事 SOP（LO 2 · Key Teaching Point 1）

- 🖼️ 整頁 code panel：三條建立路徑 + `shape/head/info/describe/isna().sum()`。
- 📣 「建立 DataFrame 的三條路 + 看資料的五件事」。
- 🎙️ 這五行是 senior 和 junior 的差別。拿到新檔一律先跑，別急著 query。info() 會告訴你哪欄是 object（通常就是髒源頭），isna().sum() 告訴你缺值分佈——這兩個是 debug 第一站。

## S6 · MECHANISM FLOW · read_csv 四個關鍵參數（LO 2）

- 🖼️ 四節點 flow_chain：encoding → sep → dtype → parse_dates。
- 📣 標題「read_csv 一行背後的四個關鍵參數」。
- 🎙️ 大家都會 `pd.read_csv('a.csv')`，但真實檔案常常不是 UTF-8、不是逗號、不是文字日期。這四個參數決定你後面要不要重來。

## S7 · CONCEPT CODE · 四參數實戰（LO 2）

- 🖼️ 整頁 code panel：encoding='utf-8-sig'、sep='\t'、dtype={...}、parse_dates=[...]。
- 📣 「encoding / sep / dtype / parse_dates：讓讀檔一次對」。
- 🎙️ encoding 中文檔常用 utf-8-sig 或 big5；dtype 一開始就釘住，後面不用再 astype；parse_dates 讓日期一開始就是 datetime64 而不是字串。

## S8 · PITFALL · 讀 CSV 不指定 encoding（Common Pitfall #6）

- 🖼️ draw_vs_two_col：左標「❌ 常見寫法」紅框，右標「✅ 推薦寫法」綠框。
- 📣 左：`pd.read_csv('orders.csv')` ← 中文變亂碼；右：`pd.read_csv('orders.csv', encoding='utf-8-sig')`。
- 🎙️ Windows 匯出的 CSV 常帶 BOM，utf-8-sig 才正確。遇到 big5，乖乖改 big5。別在下游用 replace 補救——源頭解決。

## S9 · CONCEPT MATRIX · loc vs iloc 四把鑰匙（LO 3 · Key Teaching Point 3）

- 🖼️ 2×2 matrix：loc 標籤 / iloc 位置 / 布林遮罩 / query。
- 📣 標題「loc vs iloc：標籤 vs 位置，bug 排行第一名」。
- 🎙️ 兩個設計就是故意——pandas 要同時服務『我知道列標籤』和『我知道列位置』兩種人。set_index 後 df.loc[0] 和 df.iloc[0] 完全不同列，這就是坑。

## S10 · CONCEPT CODE · loc/iloc 切片差異（LO 3）

- 🖼️ 上下雙 code_panel：上 iloc 包前不包後、下 loc 包前包後。
- 📣 「同樣的 0:3，loc 包後、iloc 不包後」。
- 🎙️ 這不是 bug 是設計——iloc 遵循 Python list 慣例，loc 遵循 SQL BETWEEN。混用就是災難。業務邏輯 90% 用 loc。

## S11 · PITFALL · 布林條件要用 loc（Common Pitfall #3）

- 🖼️ draw_vs_two_col。
- 📣 左：`df.iloc[df['age']>18]` ← IndexError；右：`df.loc[df['age']>18]` ✓。
- 🎙️ iloc 只接整數位置，布林 Series 會 raise。寫錯時別硬改，退回去想：我用的是條件還是位置？

## S12 · MECHANISM FLOW · 清理四大手法（LO 4）

- 🖼️ 四節點 flow_chain：欄名標準化 → 型別轉換 → 缺值處理 → 重複移除。
- 📣 標題「清理四大手法：順序不要亂」。
- 🎙️ 順序重要——先正名欄（不然後面所有 key 都對不上）、再定型別（不然 NaN 會從型別不對來）、再補缺值（看分佈再決定策略）、最後去重（去重要以正名 + 型別後的欄位為準）。

## S13 · CONCEPT CODE · 欄名標準化（Key Teaching Point 4）

- 🖼️ code_panel：`df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')`。
- 📣 「欄名標準化：三行下去，未來不會再崩潰」。
- 🎙️ 這是『免費』的投資——成本三行，收益是你之後寫的每一行 query。Customer ID 和 customer_id 在後面 merge 會爆，在這裡先擋掉。

## S14 · CONCEPT CODE · 型別轉換 + errors='coerce'（Key Teaching Point 2）

- 🖼️ code_panel：`pd.to_datetime(..., errors='coerce')`、`pd.to_numeric(..., errors='coerce')`、金額字串先 str.replace('$','').str.replace(',','')。
- 📣 「型別轉換的救命符：errors='coerce'」。
- 🎙️ coerce 會把不合法值轉成 NaT/NaN 而不是 raise——這是處理髒資料的救命符。但副作用是『失敗悄悄發生』，做完一定要回頭看 isna().sum()。

## S15 · CONCEPT CODE · 缺值處理三策略（Key Teaching Point 5）

- 🖼️ 三欄 draw_three_blocks_flow：訂單日期缺失→丟、金額缺失→中位數、類別缺失→'Unknown'。
- 📣 標題「缺值處理沒有標準答案——依欄位意義決定」。
- 🎙️ 時序分析缺日期就廢了，直接 dropna subset；金額補中位數比平均穩；類別補 'Unknown' 保留『缺本身』這個訊號。不要無腦 dropna 或 fillna(0)。

## S16 · PITFALL · inplace / append / dropna 地雷（Pitfall #4,#5 + LO 4）

- 🖼️ draw_vs_two_col：左三條紅字錯用、右三條綠字改寫。
- 📣 左：`df.drop(..., inplace=True)` / `df.append(...)` / `df.dropna()`；右：賦值寫法 / `pd.concat([...])` / `df.dropna(subset=['date'])`。
- 🎙️ inplace 在新版已不建議、append 已 deprecated、dropna 無 subset 會砍到不想砍的。三個都是 review 會被打槍的經典錯。

## S17 · MECHANISM FLOW · orders_raw → orders_clean 七步（LO 5）

- 🖼️ 七節點 flow_chain：讀檔 → 看五件事 → 欄名 → 型別 → 缺值 → 去重 → 輸出。
- 📣 標題「orders_raw → orders_clean：七步微型 ETL」。
- 🎙️ 我們現在把前面所有觀念串成一條線——這就是 Notebook 裡 Case 走的路徑。你只要記得這七步的順序，未來任何髒檔都不會慌。

## S18 · EXAMPLE CODE · 七步一次跑完（LO 5）

- 🖼️ 整頁 code_panel：完整 clean_orders() 雛形，20 行內完成七步。
- 📣 「七步流水線一次跑完」。
- 🎙️ 逐行唸一遍——這就是課堂 Notebook 的 Case。每一行對應上一張流程圖的一個節點。等一下練習會請你把這段封裝成 clean_orders(path) 函式。

## S19 · EXAMPLE TABLE · 清理前 vs 清理後（LO 5）

- 🖼️ draw_editorial_table：欄（指標 / raw / clean / 變化）；列（列數、dtypes 正確率、日期欄 NaN、金額欄 NaN、重複列）。
- 📣 標題「清理前 vs 清理後：用數字驗證我們做了什麼」。
- 🎙️ 清理完務必出這張驗證表——不是憑感覺說『我清好了』，是用數字證明。這也是 code review 時最快讓別人信任你工作的方式。

## S20 · PITFALL · 六個常犯錯誤綜合（Common Pitfalls §4 全部）

- 🖼️ draw_editorial_table：欄（錯誤 / 為什麼錯 / 正確寫法）六列。
- 📣 標題「六個常犯錯誤一次看清」。
- 🎙️ 這六個是我看過最多次的坑：to_datetime 沒 coerce、$1,355 直接 astype、布林用 iloc、inplace 濫用、append 還在用、CSV 沒 encoding。印下來貼在螢幕邊。

## S21 · PRACTICE ASK · 練習題 + 三個 Discussion Prompts（LO 5 · §5）

- 🖼️ draw_ask_page；data_card 顯示「40 min · 兩題 + 三討論」。
- 📣 大問句「把剛剛 18 行封裝成 clean_orders(path) ——並回答三個討論題」。
- 🎙️ 練習題一：🟡 跑通 Notebook 的七步 Case。練習題二：🔴 封裝成函式、加 type hints、加 docstring。同時請討論：(1) 100 萬筆三種缺值策略怎麼選？(2) 為什麼 loc/iloc 要兩個？(3) 清完覆蓋還是另存？

## S22 · CHECKPOINT · MVK 回顧（全部 LO 對齊）

- 🖼️ draw_thesis_hierarchy 兩欄：左「概念 MVK」、右「動作 MVK」；底部 inverted thesis。
- 📣 左：五件事 SOP / loc vs iloc / errors='coerce' / 四大手法順序。右：read_csv 四參數 / 欄名三行式 / to_datetime(coerce) / dropna(subset=)。
- 🎙️ 這張是你帶回家的筆記——記住這八項，90% 的清理場景都有手感了。

## S23 · SILENT · 下節預告

- 🖼️ 全深綠，中央白字。
- 📣 「下節 S3：把乾淨資料變成洞察——groupby / merge / pivot」。
- 🎙️ S2 把資料洗乾淨，S3 開始創造價值。下次見。
