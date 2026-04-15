# F1 — 計算機概論與 OS 角色｜講師講稿

> **課程時長**：1.5 小時（講授 60 min + 課堂練習 20 min + QA 10 min）
> **受眾定位**：僅有 Python 基礎的非理工資訊背景學生（商管、人文、行銷、行政、設計、醫護轉職或自學）
> **前置知識**：無
> **後續銜接**：F2 Python 資料結構、S1 向量化、S2 Pandas I/O

---

## 1. 本節目標 (Learning Objectives)

完成本節後，學員應能：

1. 用「廚房三角色」類比（廚師 / 工作檯 / 倉庫）說出 CPU / RAM / Storage 的分工。
2. 用 Bit/Byte 估算「1 億筆 float64」的記憶體佔用（≈ 800 MB），並算出自己筆電的安全 CSV 上限。
3. 解釋為何「讀一個檔」比「算 10 億次加法」慢——建立 I/O 100× 瓶頸的直覺。
4. 說明 OS 三大職責（記憶體 / 檔案 / 行程）以及 Python 如何透過 OS 代理才能碰到硬體。
5. 區分 I/O Bound 與 CPU Bound 任務，判斷該用 async/threading、向量化或 multiprocessing。
6. 用 `pathlib.Path` 取代反斜線字串，避免 Windows → Linux 跨平台部署 bug。

---

## 2. 時間切分表

```
00:00-00:05  開場暖身：Excel 開 5 萬筆訂單卡 3 分鐘的共鳴故事
00:05-00:15  廚房三角色類比（F4）+ read_csv 七步旅程（F5）+ 角色連連看（F6）
00:15-00:25  Bit/Byte 量級感（F7）+ RAM 能裝多少筆 CHECKPOINT（F8）
00:25-00:40  RAM vs Storage 1000× 差距（F9）+ OOM 陷阱（F10）+ I/O 為何慢（F11）
00:40-00:55  OS 三大職責（F12）+ 路徑跨平台陷阱（F13）
00:55-01:10  估算你自己的筆電上限（F14）+ I/O vs CPU Bound（F15）+ 三任務判斷（F16）
01:10-01:20  multiprocessing 用錯地方陷阱（F17）+ 三核心回顧（F18）
01:20-01:30  三件帶走（F19）+ 全景 pyramid（F20）+ 銜接 F2（F21）+ QA
```

---

## 3. 關鍵教學點 (Key Teaching Points)

1. **廚房類比是整章的地基**：非理工學員最容易卡在「CPU / RAM / Storage 到底差在哪」。一開始就把三角色講死，後面每次出現 OOM、I/O、Swap 都回去指那張廚房圖。「料不搬到工作檯，廚師碰不到」這句話要重複 3 次以上。
2. **I/O 100× 慢的直覺必須建立**：學員常以為 Python 慢是「Python 語言爛」，這是錯的認知。真正原因有兩個：(a) I/O 慢、(b) 運算沒交給 C 層。第一點在本章建立（F11），第二點留給 S1 向量化。這兩件事加起來解釋 90% 的「Pandas 為什麼卡」。
3. **OOM 不是語法錯，是硬體抗議**：要讓學員認得出 `MemoryError` 的長相，並且理解「為什麼系統會在沒爆訊息前先卡死 10 分鐘」—— 那是 Swap 在做拿硬碟假裝 RAM 的垂死掙扎。這個畫面描述比任何定義都有效。
4. **pathlib 要現場寫一次**：口頭講「用 pathlib」學員回家還是會 `'data\\x.csv'`。請打開終端機現場 demo `Path('data') / '2024' / 'x.csv'` 並印出結果給他們看，再刻意在 Linux 機器上跑一次字串版讓它爆 `FileNotFoundError`。
5. **I/O vs CPU Bound 的判斷法要簡單到不會忘**：就是「打開工作管理員看 CPU 還是網路飆」。不要講 GIL、不要講 context switch。這些是 F2/F3 以後的事。這一章只要學員會選對武器即可。
6. **每個 PITFALL 都要配一條銜接箭頭**：F10 → S2 chunksize、F11 → S1 向量化、F13 → S2 pathlib。讓學員帶著「我現在看不懂沒關係，某月某日會回來用到」的預期往前走，降低認知焦慮。

---

## 4. 學員常犯錯誤 (Common Pitfalls)

- **一口氣 `pd.read_csv()` 讀 5GB**：記憶體爆炸或系統凍結。→ 對應 S2 `chunksize` + `dtype` 下修。
- **`'data\\2024\\x.csv'` 硬拼路徑**：Windows 能跑、雲端 Linux `FileNotFoundError`。→ 改用 `pathlib.Path`。
- **爬蟲 / API 呼叫開 multiprocessing**：CPU 本來就閒，開再多行程也是一起等網路。→ 改用 `asyncio` 或 `threading`。
- **以為 RAM 沒滿就安全**：忽略 Swap 被觸發時，系統會卡到學員以為電腦當機而硬關機。
- **以為「Python 慢 = Python 語言爛」**：其實是運算留在 Python 直譯器層。這個誤解會在 S1 用向量化打破，但要先在本章埋伏筆。

---

## 5. 提問設計 (Discussion Prompts)

1. 如果你現在手上有一個 20GB 的交易紀錄 CSV，你只有 8GB RAM 的筆電——你有幾種方法讓這份資料還是能被分析？（預期答：chunksize、dtype 下修、欄選擇、上雲、改用 DuckDB / Polars）
2. 為什麼你家的檔案總管可以「秒開」一個 5GB 的影片檔，但 Pandas 讀 5GB 的 CSV 會卡死？（預期答：影片是串流播放只讀局部；Pandas 預設要把整份塞 RAM 才能做欄運算）
3. 同樣是「讓程式跑更快」，為什麼爬蟲要開 threading、機器學習訓練要開 multiprocessing？（預期答：前者 I/O Bound 需要並行「等」；後者 CPU Bound 需要並行「算」）

---

## 6. 延伸資源 (Further Reading)

- Jake VanderPlas《Python Data Science Handbook》第 1-2 章的「為什麼 NumPy 快」討論（線上免費版）
- Real Python - 「pathlib 官方 tutorial」與「async IO 入門」兩篇
- 建議學員安裝 `psutil` 套件，一行 `psutil.virtual_memory()` 就能看見自己電腦的 RAM 現況

---

## 7. 常見 Q&A

**Q1：我完全不是資工背景，這些對我以後有用嗎？**
A：有用到讓你省下每月幾小時的 Excel 凍結時間。本章三件事（RAM 工作檯 / I/O 慢 / 路徑用 /）在你之後寫的每一行 Pandas 都會出現。

**Q2：那我是不是要背 CPU 指令集、暫存器這些？**
A：不用。這是底層工程師的事。你只要記住廚房三角色 + 三個反射即可，這堂課的目標是讓你「看得懂瓶頸在哪」，不是「手寫一顆 CPU」。

**Q3：Mac / Windows / Linux 哪個最適合做資料分析？**
A：開發用什麼都可以，但**部署幾乎 100% 在 Linux**。所以第一天就養成「路徑用 pathlib、不要依賴 Windows 特性」的習慣，未來上雲零痛苦。
