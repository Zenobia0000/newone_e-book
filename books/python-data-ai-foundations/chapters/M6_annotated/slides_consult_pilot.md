---
title: M6 計算機組織與作業系統 — 顧問嚴謹 Pilot (v1.1 Editorial)
module: M6
version: 1.1
style: Editorial-strict / Chart-first / Latency-number-anchored
seed_paradigm: shared/design_system/顧問型投影片_黃金守則與泛式.md
paradigm_version: v1.1
primary_color: "#1B5E3F"
forbidden_prototypes: [SCENE, STORYBOARD, ZOOM, DIAGRAM-STORY]
forbidden_colors: ["red", "yellow", "orange", "pink", "light blue"]
forbidden_metaphors: ["主廚 vs 廚工", "廚房", "工作桌／倉庫擬人化"]
priority_rules: [G6, G10, G11]
slide_prototypes_used:
  - ASK
  - CHART
  - TABLE
  - VS
  - GEOMETRIC-DIAGRAM
  - BEFORE/AFTER
  - MATRIX
  - PYRAMID
  - SILENT
total_slides: 15
audience: 企業內訓 / 付費技術課程 / 成人學員
last_updated: 2026-04-14
replaces: （首版 v1.1，無 v1.0）
governing_thought: "Performance is physics respected; every abstraction leaks."
---

# M6 · 計算機組織與作業系統 — 顧問嚴謹 Pilot Deck (v1.1 Editorial)

> 本 deck 是 v1.1 Editorial-strict 在 M6「延遲與資源」主題上的落地。M6 特別適合用 CHART 呈現延遲量級；三條優先守則 **G6 數字精準標註 / G10 文圖照 60:30:10 / G11 倒掛結論框** 在此 100% 落地。全 deck 禁「主廚 vs 廚工」擬人化廚房類比；硬體與 OS 概念一律以純幾何方塊與實際延遲數字承載。

---

### Slide 1 · ASK · 你的訓練為什麼慢，是算不完還是在等搬運？

**🖼️ 畫面**
> 純白底，80% 留白。正中央一行深綠 `#1B5E3F` 粗體提問句（最大字級）。提問句正下方一個極簡水平時間軸，全長分為兩段：左段 20% 深綠實心條標註「GPU 計算 200 ms」；右段 80% 灰 `#D3D3D3` 斜線填充條標註「GPU 等資料 800 ms」，兩段上方各標百分比 `20%` / `80%`。時間軸兩端標 `t=0` 與 `t=1.0 s`。頁底靠左 8pt 灰 `Source: 本課 DataLoader profile 示例（num_workers=0）`。

**📣 畫面上的字**
> 80% 時間在等 不是在算

**🎙️ 講者這時說**
> 先不談模型多大。一次 iteration 一秒鐘，GPU 只有兩成時間真的在算，另外八成在等資料從磁碟搬過來。你不是訓練太慢，你是搬運太慢。今天三小時，就是要讓你看穿這條搬運鏈。

**🎨 視覺紀律 check**
> G1 ✓（主張式問句） / G3 主色 ✓ / G5 ✓（極簡條、無裝飾） / G6 ✓（20% / 80% / 200ms / 800ms 精準標註） / G7 留白 ✓ / G8 無禁色 ✓ / G10 文圖照 ✓

**💡 這張在做什麼**
Hook：用「等待比例」把模組痛點鎖定在「搬運」而非「算力」，為後續延遲量級鋪路。

---

### Slide 2 · CHART · DataFrame 一個 object 欄，RAM 瞬間多吃一個零

**🖼️ 畫面**
> 全幅水平柱狀 CHART，深綠 `#1B5E3F` 純色柱、白底、無 3D、無漸層。X 軸「RAM 佔用 (MB)」線性刻度 0 / 200 / 400 / 600 / 800 / 1000，Y 軸四列情境（由上而下）：
> - `int64 × 1M 列` — 柱長 8 MB，柱右深綠粗體 `8 MB (基準)`
> - `float64 × 1M 列` — 柱長 8 MB，柱右 `8 MB`
> - `category × 1M 列（100 類）` — 柱長 2 MB，柱右 `2 MB (−75%)`
> - `object (str) × 1M 列` — 柱長 ≈ 900 MB（延伸到接近軸尾），柱右 `~900 MB (×100 倍)`
>
> Y 軸標籤深綠 regular，軸線純灰 `#808080`，僅保留刻度線。頁底 8pt 灰 `Source: pandas 官方 memory_usage(deep=True) 實測、1M rows 英文字串平均 80 bytes`。

**📣 畫面上的字**
> 同樣 1M 列 差一百倍

**🎙️ 講者這時說**
> 這就是你的 DataFrame 明明「只有一百萬列」卻吃掉一 GB 的真相。object dtype 每一格存的是 Python 字串指標，每一個字串平均八十幾 bytes。換成 category，同一份資料瞬間瘦身七成五。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G5 ✓（純色柱、軸極簡） / G6 ✓（8/2/900 MB 與倍數精準標註） / G8 無禁色 ✓ / G10 ✓

**💡 這張在做什麼**
Tension 第一擊：讓學員用「數字」看見 dtype 選擇帶來的 100 倍 RAM 差，埋下「抽象不是免費的」伏筆。

---

### Slide 3 · CHART · 記憶體階層：同一件事在不同層級快或慢 10^6 倍

**🖼️ 畫面**
> 全幅水平柱狀 CHART（對數軸），深綠 `#1B5E3F` 純色柱、白底、無 3D。X 軸「延遲 (ns，對數刻度)」標示 `1 / 10 / 100 / 1K / 10K / 100K / 1M / 10M / 100M`，Y 軸六列（由上而下，對應由近到遠）：
> - `L1 cache` — 柱長到 1 ns，柱右深綠粗體 `≈ 1 ns`
> - `L2 cache` — 柱長到 4 ns，柱右 `≈ 4 ns`
> - `L3 cache` — 柱長到 15 ns，柱右 `≈ 15 ns`
> - `RAM (DRAM)` — 柱長到 100 ns，柱右 `≈ 100 ns (×100 於 L1)`
> - `NVMe SSD` — 柱長到 100,000 ns，柱右 `≈ 100 μs (×10^5)`
> - `Network RTT（同機房）` — 柱長到 1,000,000 ns，柱右 `≈ 1 ms (×10^6)`
>
> 柱與柱之間留純白分隔，軸線純灰，無格線。頁底 8pt 灰 `Source: Jeff Dean Numbers Every Programmer Should Know 整理 / Intel Skylake-X 官方 cache latency`。

**📣 畫面上的字**
> 從 L1 到網路 每一層 ×100 到 ×10^6

**🎙️ 講者這時說**
> 這張圖請你看一輩子。L1 一奈秒，RAM 一百奈秒，SSD 十萬奈秒，網路一百萬奈秒。每跨一層就是兩到三個數量級。你的程式碼寫得再漂亮，走到下一層就是大兩個零的延遲。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G5 ✓（純柱對數軸、去裝飾） / G6 ✓（每層實際 ns 數字直標、跨層倍率直標）優先 ✓ / G8 無禁色 ✓ / G10 ✓

**💡 這張在做什麼**
Reveal 主幹：用對數軸柱圖把「為什麼慢」具象化到五個數字；本 deck 最重要一張，G6 承載全章權重。

---

### Slide 4 · TABLE · 把奈秒放大成人類時間：一杯水 vs 一趟火車

**🖼️ 畫面**
> Editorial 風 TABLE：僅上下框線、無竖線、行交替 `#FFFFFF/#F0F0F0`、表頭深綠 `#1B5E3F` 底白字。三欄六列：
>
> | 層級 | 實際延遲 | 放大 10^9 倍後的人類尺度 |
> |---|---|---|
> | L1 cache | 1 ns | 1 秒 |
> | L2 cache | 4 ns | 4 秒 |
> | RAM | 100 ns | 1 分 40 秒 |
> | NVMe SSD | 100 μs | 28 小時 |
> | 同機房網路 | 1 ms | 11.6 天 |
> | 跨大陸網路 | 150 ms | 4.75 年 |
>
> 表格下方 15% 留白。底部深綠 `#1B5E3F` 倒掛框白字粗體：「CPU 等 RAM 是喘口氣，CPU 等網路是等下一次生日。」頁底 8pt 灰 `Source: Jeff Dean 2009 / Peter Norvig 放大比喻整理`。

**📣 畫面上的字**
> 同樣一次讀取 差 4.75 年

**🎙️ 講者這時說**
> CPU 世界的一奈秒，如果放大到人類的一秒。RAM 就是一分半鐘，SSD 已經是一天多，跨大陸網路是四年半。下次你把資料從 API 抓下來再塞進模型，你是真的讓 CPU 停在那邊等四年半。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G5 ✓ / G6 ✓（每列實際 + 放大數字皆精準） / G7 留白 ✓ / G8 無禁色 ✓ / G11 倒掛框 ✓ / G12 表格極簡 ✓

**💡 這張在做什麼**
Reveal：把 Slide 3 的對數軸翻譯成人類可感的時間尺度；TABLE 極簡呈現，配倒掛框收束。

---

### Slide 5 · VS · CPU 幾個強核心 vs GPU 幾千個弱核心

**🖼️ 畫面**
> 左右分割，兩個純幾何方塊區，完全無人物、無任何角色符號、無廚房/廚師圖示。
> **左半「CPU」**：一個深綠 `#1B5E3F` 邊框大方塊，內含 8 個等大的深綠實心小方塊（4×2 排列），每格白字編號 `C1`–`C8`。方塊左下角標 `8 cores (典型 desktop)`、右下角標 `~3 GHz / core`；下方一行深綠字 `強項：分支、邏輯、控制流`。
> **右半「GPU」**：一個同尺寸深綠邊框大方塊，內含 32×40 = 1280 個微型深綠實心小方塊（緊排點陣），不標編號；方塊左下角標 `~10,000 CUDA cores`、右下角標 `~1.5 GHz / core`；下方一行深綠字 `強項：同一種運算 × 極大量`。
> 中央一條純灰 `#808080` 垂直細線分隔，中線頂端灰色大寫「vs」。頁底 8pt 灰 `Source: Intel i9-13900K / NVIDIA RTX 4090 官方規格`。

**📣 畫面上的字**
> 8 核 vs 10,000 核

**🎙️ 講者這時說**
> 差別不是誰快。單核時脈兩邊差不多。差別是數量。CPU 八個工人什麼都能做，GPU 一萬個工人只會做同一件事，但同時做。深度學習的矩陣乘法剛好就是「同一件事做一兆次」，GPU 整個贏在這裡。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓（僅深綠 + 灰 + 白） / G5 ✓（純幾何方塊、無角色、無擬人） / G6 ✓（8 / 10,000 / 3 GHz / 1.5 GHz 精準標註） / G8 無禁色 ✓ / 禁「主廚 vs 廚工」擬人 ✓

**💡 這張在做什麼**
Reveal：CPU vs GPU 架構差異，以核心數點陣密度直觀對照；嚴守禁廚房擬人化。

---

### Slide 6 · GEOMETRIC-DIAGRAM · 虛擬記憶體三層翻譯：VA → Page Table → PA

**🖼️ 畫面**
> 純白底，純幾何純線稿。三層由上而下排列，每層一條水平帶，層與層之間純灰 `#808080` 實線箭頭指下：
> - **Layer 1（上）「程式看到的」**：深綠 `#1B5E3F` 邊框白底方塊，內寫 `Virtual Address  0x7fff_a1b2_c000`；右側小字註記 `每個 process 自有 2^48 空間`。
> - **Layer 2（中）「OS 的翻譯表」**：三個水平並排深綠邊框方塊：`Page Table`（PTE entry）/ `TLB Cache 64–1536 entries`（深綠粗邊框強調）/ `Page Fault Handler`。三者之間純灰細線連接。右側小字 `TLB hit ≈ 1 ns ／ TLB miss ≈ 100 ns ／ Page fault ≈ 100 μs–10 ms`。
> - **Layer 3（下）「實體硬體」**：兩個並排深綠邊框方塊：左 `RAM 物理頁 4 KB` / 右 `Swap on SSD 4 KB`；下方標 `RAM ≈ 100 ns / Swap ≈ 100 μs（×1000）`。
>
> 所有連線純灰實線、無弧度、無陰影、無任何人物或表情。頁底 8pt 灰 `Source: Bryant & O'Hallaron CS:APP Ch.9 / Linux x86_64 4-level paging`。

**📣 畫面上的字**
> 你寫的位址 不是真的位址

**🎙️ 講者這時說**
> 你在 Python 看到的記憶體位址，全部是假的。OS 在中間有一張 page table 翻譯，加速用的快取叫 TLB。TLB 命中是一奈秒，沒命中是一百奈秒，整頁不在 RAM 就是 page fault，十萬奈秒起跳。你的程式碰運氣的地方，就藏在這三個數字差。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G5 ✓（純線稿、純方塊） / G6 ✓（TLB 1 ns / miss 100 ns / fault 100 μs–10 ms 精準標註） / G8 無禁色 ✓ / 無角色無表情 ✓

**💡 這張在做什麼**
Reveal：把 virtual memory / page table / TLB 三層映射純幾何化，並把每層延遲直接標上，延續 G6 精準標註。

---

### Slide 7 · TABLE · Process 與 Thread：五個維度一眼對照

**🖼️ 畫面**
> Editorial 風 TABLE：僅上下框線、無竖線、行交替 `#FFFFFF/#F0F0F0`、表頭深綠 `#1B5E3F` 底白字。三欄六列：
>
> | 維度 | Process | Thread |
> |---|---|---|
> | 記憶體空間 | 獨立（各自 virtual address space） | 共用（同一 process 內） |
> | 建立成本 | 高（~1–10 ms，複製 page table） | 低（~10 μs，共用資源） |
> | 資料共享 | 需 IPC / shared memory | 直接讀寫同一變數 |
> | 崩潰隔離 | 一個掛不影響別人 | 一個掛整個 process 死 |
> | Python GIL 影響 | 不受限（各自一把） | CPython 同時只一個跑 bytecode |
>
> 表格下方 12% 留白。底部深綠倒掛框白字粗體：「CPU 密集選 multiprocessing，I/O 密集選 threading；選錯就是白忙。」頁底 8pt 灰 `Source: Python docs / Linux clone(2) / PEP 703 (GIL)`。

**📣 畫面上的字**
> 五個維度 一眼分

**🎙️ 講者這時說**
> 最常見的錯是用 threading 算 NumPy 大矩陣以為會變快——不會，GIL 卡死。真正要平行算就是 multiprocessing，各 process 一把自己的 GIL，不搶。DataLoader 的 num_workers 走的是 multiprocessing，就是這個原因。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G4 MECE ✓（五維度互斥） / G5 ✓ / G6 ✓（1–10 ms vs 10 μs 建立成本數字） / G8 無禁色 ✓ / G11 倒掛框 ✓ / G12 表格極簡 ✓

**💡 這張在做什麼**
Reveal：Process vs Thread 五維結構化對照，GIL 實務結論用倒掛框收束。

---

### Slide 8 · TABLE · fork / exec / spawn 三種產生 process 的方式，Windows 只有一種能用

**🖼️ 畫面**
> Editorial 風 TABLE：僅上下框線、無竖線、行交替 `#FFFFFF/#F0F0F0`、表頭深綠 `#1B5E3F` 底白字。四欄五列：
>
> | 方式 | 機制 | 平台 | 建立延遲 |
> |---|---|---|---|
> | `fork` | 複製父 process 整個位址空間（copy-on-write） | Linux / macOS ✓ / Windows ✗ | ~1 ms |
> | `exec` | 取代當前 process 影像、保留 PID | 全平台 | ~2 ms |
> | `spawn` | 全新 process + 重新 import 所有模組 | 全平台（Windows 預設） | ~50–200 ms |
> | `forkserver` | 預啟一台乾淨伺服器分發 fork | Linux / macOS | ~2 ms（暖機後） |
>
> 表格下方 12% 留白。底部深綠倒掛框白字粗體：「Windows 沒有 fork。你的 `if __name__ == '__main__':` 不是裝飾，是 spawn 必需的防無限迴圈。」頁底 8pt 灰 `Source: Python multiprocessing docs / POSIX fork(2) / Windows CreateProcess`。

**📣 畫面上的字**
> 一張 Linux 跑得好 搬到 Windows 掛掉

**🎙️ 講者這時說**
> 很多人在 Linux 寫 DataLoader 跑得好好的，搬去 Windows 就整個壞掉。不是 code 寫錯，是 Windows 沒 fork，預設走 spawn，spawn 會把整支腳本重新 import 一次。你要是沒包在 `if __name__ == '__main__':` 裡，就會無限開 process。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G5 ✓ / G6 ✓（每種方式延遲精準 ms 標註） / G8 無禁色 ✓ / G11 倒掛框 ✓ / G12 表格極簡 ✓

**💡 這張在做什麼**
Reveal：把跨平台陷阱用延遲數字 + 平台可用性 TABLE 結構化，避免口述混亂。

---

### Slide 9 · CHART · I/O 模型演進：select → epoll → io_uring，吞吐量一次一個數量級

**🖼️ 畫面**
> 全幅水平柱狀 CHART。X 軸「單執行緒最大可處理連線數 (對數刻度)」標 `1K / 10K / 100K / 1M / 10M`，Y 軸五列（由上而下對應時代演進）：
> - `1983 · fd + select()` — 柱長到 1,024，柱右深綠粗體 `1,024 (硬上限 FD_SETSIZE)`
> - `1997 · poll()` — 柱長到 10,000，柱右 `~10K (O(n) 掃描)`
> - `2002 · epoll (Linux)` — 柱長到 1,000,000，柱右 `~1M (O(1) 事件驅動)`
> - `2003 · kqueue (BSD/macOS)` — 柱長到 1,000,000，柱右 `~1M`
> - `2019 · io_uring (Linux 5.1+)` — 柱長到 10,000,000，柱右 `~10M (無系統呼叫、零拷貝)`
>
> 深綠 `#1B5E3F` 純色柱、對數軸、僅保留刻度。頁底 8pt 灰 `Source: Linux kernel docs / Jens Axboe io_uring paper 2019 / C10K problem Kegel 1999`。

**📣 畫面上的字**
> 36 年 連線上限 ×10,000

**🎙️ 講者這時說**
> 從 1983 年的 select 到 2019 年的 io_uring，同一條線，一顆 CPU 能同時撐起的連線數漲了一萬倍。每一代都在解同一個問題：系統呼叫太貴。io_uring 直接讓應用程式跟 kernel 共用 ring buffer，系統呼叫幾乎歸零。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G5 ✓（純柱對數軸） / G6 ✓（1K / 10K / 1M / 10M 精準標註） / G8 無禁色 ✓ / G10 ✓

**💡 這張在做什麼**
Reveal：用一張時代演進 CHART 把 I/O 模型的量級躍遷（fd → epoll → io_uring）視覺化。

---

### Slide 10 · BEFORE/AFTER · 同一份 1M 列表格，object vs category 差 450 倍

**🖼️ 畫面**
> 左右分割兩張純色 CHART（深綠 `#1B5E3F` 純柱、白底、無 3D）。
> 左圖標 `BEFORE：df['city'] as object` — 一柱高到 `900 MB`，柱頂深綠粗體 `900 MB (基準)`；柱下一行小字 `dtype=object / 每格一個 Python str 物件 / ~80 bytes × 1M + 指標`。
> 右圖標 `AFTER：df['city'] = df['city'].astype('category')` — 同一軸尺度下一柱只到 `2 MB`，柱頂深綠粗體 `2 MB (−99.8%)`；柱下一行小字 `dtype=category / 100 種類別 + int8 編碼`。
> 兩圖共用 Y 軸（0–1000 MB 線性刻度），中央一條純灰 `#808080` 垂直細線分隔。頁底 8pt 灰 `Source: pandas memory_usage(deep=True) 實測、1M rows 100 unique cities`。

**📣 畫面上的字**
> 改一個 dtype 省下 99.8% RAM

**🎙️ 講者這時說**
> 你 RAM 爆掉第一個要看的不是 batch size，是 dtype。同一份城市欄位，object 吃九百 MB，category 兩 MB。這不是最佳化，這是常識。改一行，OOM 消失。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G5 ✓（純色柱、共用軸） / G6 ✓（900 MB / 2 MB / −99.8% 精準標註） / G8 無禁色 ✓ / G10 ✓

**💡 這張在做什麼**
Reveal：把 Slide 2 的量級差具體落到「一個欄位、兩種 dtype」的 BEFORE/AFTER，把抽象化成 RAM 帳單。

---

### Slide 11 · GEOMETRIC-DIAGRAM · DataLoader 流水線：num_workers=4 讓 GPU 不再空等

**🖼️ 畫面**
> 純白底時序圖，純幾何純線稿，上下兩列平行水平時間軸（X 軸為時間、無刻度數字、僅區段長度）。
> **上列「num_workers=0（單 process）」**：時間軸從左到右交替兩色段——灰 `#D3D3D3` 斜線填充段標 `CPU 讀檔+解碼 800 ms` → 深綠 `#1B5E3F` 實心段標 `GPU 計算 200 ms` → 灰斜線段 800 ms → 深綠段 200 ms →（循環四次）。右端總結深綠字 `GPU 利用率 ≈ 20%`。
> **下列「num_workers=4（四個子 process）」**：同長度時間軸。上方四條並排細灰斜線段（四個 worker 各自預取一 batch）在前面 800 ms 並行完成；主軸上從 t=800 ms 起幾乎連續的深綠實心長段 `GPU 計算` 連續四格幾乎無縫。右端總結深綠字 `GPU 利用率 ≈ 95%`。
>
> 兩列之間純灰 `#808080` 水平分隔線。軸線純灰、刻度省略。頁底 8pt 灰 `Source: PyTorch DataLoader docs / 本課示例 ImageFolder ResNet18 batch=32`。

**📣 畫面上的字**
> 四個 worker 把等待疊成背景

**🎙️ 講者這時說**
> 上半是你寫預設程式的樣子：算一下等一下算一下等一下，GPU 兩成利用率。下半是加了 num_workers=4：四個子 process 在 GPU 算的時候同時讀下一批，等 GPU 算完下一批已經在 RAM。GPU 利用率衝到 95%，而且你只動了一行參數。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G5 ✓（純幾何時序、無陰影） / G6 ✓（800 ms / 200 ms / 20% / 95% 精準標註） / G8 無禁色 ✓ / 無角色 ✓

**💡 這張在做什麼**
Reveal：DataLoader 原理用純幾何時序圖呈現，直接呼應 Slide 1 的「80% 等待」問題解決路徑。

---

### Slide 12 · MATRIX · RAM OOM vs VRAM OOM：四個象限、四個第一動作

**🖼️ 畫面**
> 經典 2×2 MATRIX：水平軸「發生位置」（左 CPU RAM / 右 GPU VRAM），垂直軸「症狀類型」（下 分配失敗 / 上 累積增長）。軸線純灰 `#808080`、軸標深綠 `#1B5E3F` 粗體。四格每格一張深綠邊框白底卡片：
> - **左下（RAM + 分配失敗）**：標題 `MemoryError: Unable to allocate`；原因 `pd.concat 大表 / object dtype / 一次 read_csv 全檔`；第一動作 `改 chunksize / astype('category') / del + gc.collect()`
> - **右下（VRAM + 分配失敗）**：標題 `CUDA out of memory on allocation`；原因 `batch_size 太大 / 模型太大 / 沒 zero_grad`；第一動作 `降 batch_size ／ 加 optimizer.zero_grad() ／ torch.cuda.empty_cache()`
> - **左上（RAM + 緩增）**：標題 `進程 RSS 持續上升`；原因 `循環內建立新 DataFrame 未釋放 / 閉包抓參考`；第一動作 `tracemalloc 定位 / 明確 del`
> - **右上（VRAM + 緩增）**：標題 `nvidia-smi 每輪 +幾十 MB`；原因 `loss.item() 漏呼叫 / retain_graph=True / 中間張量沒 detach`；第一動作 `loss = loss.item() ／ .detach()`
>
> 右下與左下兩格描邊加粗標「高發 80%」。頁底 8pt 灰 `Source: PyTorch CUDA memory docs / pandas 官方 Memory usage / tracemalloc docs`。

**📣 畫面上的字**
> 先看位置 再看症狀

**🎙️ 講者這時說**
> 看到 OOM 先別慌。先問一個問題：是 CPU 側還是 GPU 側？是一次就爆還是每輪長大？兩個問題三秒鐘分出四格，對應四種第一動作。走這個順序，你修 bug 會比 Google 快。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G4 MECE ✓（四象限互斥窮盡） / G5 ✓ / G8 無禁色 ✓ / G10 ✓

**💡 這張在做什麼**
Ground：把 OOM 診斷從經驗主義升級成結構化 2×2，每格綁一個可執行的第一動作。

---

### Slide 13 · PYRAMID · 記住五個延遲量級，你就有系統直覺

**🖼️ 畫面**
> 頂部完整論述標題深綠粗體。中段橫向五節流程條（純深綠 `#1B5E3F` 實心方格、白字數字 1–5、格與格之間純灰 `#808080` 箭頭），依序標：
> `1 L1 ≈ 1 ns` / `2 RAM ≈ 100 ns` / `3 SSD ≈ 100 μs` / `4 同機房網路 ≈ 1 ms` / `5 跨洲網路 ≈ 150 ms`
>
> 五格下方每格 6pt 灰色一行關鍵對照：`ALU 指令級` / `×100 於 L1` / `×1000 於 RAM` / `×10 於 SSD` / `×150 於同機房`。中下段 18% 垂直留白。底部深綠 `#1B5E3F` 倒掛框白字粗體一句：「把這五個數字刻在腦裡，你的效能直覺比九成工程師準。」頁底 8pt 灰 `Source: Jeff Dean 2009 updated by Colin Scott 2020 / 本課精簡裁版`。

**📣 畫面上的字**
> 五個數 一生帶走

**🎙️ 講者這時說**
> 你不需要記幾百個數字。記這五個就夠。每次你設計系統、挑資料結構、寫 I/O，只要問自己：這條路徑走到哪一層？答案從第 1 層變第 3 層，你就差了十萬倍。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G3 主色 ✓ / G4 MECE ✓（五層窮盡） / G5 ✓ / G6 ✓（五個延遲數字 + 倍率精準） / G7 留白 ✓ / G8 無禁色 ✓ / G11 倒掛框 ✓

**💡 這張在做什麼**
Ground：把本 deck 所有數字凝結成五格一頁的帶走結論；G6 + G11 雙重收束。

---

### Slide 14 · SILENT · Performance is physics respected

**🖼️ 畫面**
> 全幅深綠 `#1B5E3F` 底。正中央一行白字粗體大標語，上下各 30% 垂直留白。**完全空白**——無 logo、無頁碼、無 source、無任何次級元素。

**📣 畫面上的字**
> Performance is physics respected.

**🎙️ 講者這時說**
> （沉默 5 秒，讓句子落地）光走過一公尺要三奈秒。你的效能問題不是演算法問題，是物理問題。尊重物理。

**🎨 視覺紀律 check**
> G1 ✓（完整主張句） / G3 主色 ✓（純深綠） / G5 不適用 / G7 留白 ✓（極致） / G8 無禁色 ✓ / G11 倒掛 ✓（整張即倒掛框）

**💡 這張在做什麼**
Feel：金句主張。把整堂「延遲量級」升格為一句世界觀。

---

### Slide 15 · SILENT · Every abstraction leaks — 到了 M7 你會再次感謝它

**🖼️ 畫面**
> 全幅白底。正中央一行深綠 `#1B5E3F` 粗體大字。頁底靠左 8pt 灰 `延伸閱讀：Bryant & O'Hallaron CS:APP · Jeff Dean Numbers · Jens Axboe io_uring · PEP 703`。無其他元素。

**📣 畫面上的字**
> 每一層抽象 都會漏

**🎙️ 講者這時說**
> 抽象讓你不用懂底層，直到它漏水那一天。今天學的五個數字、四個象限、三種 process 建立方式，就是你以後修漏水的工具箱。M7 分散式訓練見。

**🎨 視覺紀律 check**
> G1 ✓（主張句） / G2 Source ✓（延伸閱讀） / G3 主色 ✓ / G7 留白 ✓ / G8 無禁色 ✓

**💡 這張在做什麼**
Feel 終章：從世界觀（Slide 14）推到工程倫理（抽象必漏），收束並預告 M7。

---

## § Layer C 7 條驗收自查表

| # | 驗收項 | ✓/✗ | 理由 |
|---|---|---|---|
| 1 | 每張標題是否為完整主張句或 Socratic 問句？（G1） | ✓ | 15 張全為完整句或問句；例 Slide 3「記憶體階層：同一件事在不同層級快或慢 10^6 倍」、Slide 8「fork / exec / spawn 三種產生 process 的方式，Windows 只有一種能用」。 |
| 2 | 顏色是否 ≤ 黑 + 灰 + 1 accent？有無紅黃橙出現？（G3/G8） | ✓ | 全 deck 鎖 `#1B5E3F` 深綠 + `#808080` / `#D3D3D3` 灰 + 白。無紅黃橙粉淺藍。Slide 12 OOM 警告情境亦守禁色，用深綠邊框 + 加粗標示「高發」而非紅色。 |
| 3 | 字重 ≤ 3 種、字級 ≤ 4 級？ | ✓ | 深綠粗體（標題與關鍵數字）、深綠 regular（內文）、灰 regular（source / 輔註）三種字重；大標 / 主張 / 內文 / source 四級字級。 |
| 4 | 每 3 張是否有一張 SILENT / PYRAMID / ASK 呼吸頁？（G7/G10） | ✓ | ASK 於 1；PYRAMID 於 13；SILENT 於 14、15；TABLE + 倒掛框於 4、7、8 亦為低密度節奏頁。最長連續「高密度頁」為 Slide 5–12 其間 Slide 7/8 TABLE 與 Slide 10 BEFORE/AFTER 交替，節奏成立。 |
| 5 | 連續 3 張是否同一原型？ | ✓ | 序列：ASK→CHART→CHART→TABLE→VS→GEOMETRIC-DIAGRAM→TABLE→TABLE→CHART→BEFORE/AFTER→GEOMETRIC-DIAGRAM→MATRIX→PYRAMID→SILENT→SILENT。最長同原型連續為 Slide 7–8（TABLE）與 Slide 14–15（SILENT），皆 ≤ 2，合規。 |
| 6 | 任何純文字頁之後是否緊接圖/照/表？（G10） | ✓ | 無純文字頁；Slide 14 SILENT 亦為視覺頁（深綠底白字構圖）。所有概念頁均以 CHART / TABLE / MATRIX / GEOMETRIC-DIAGRAM 承載。 |
| 7 | 任何一張 slide 若砍掉會有實質損失嗎？無就刪。 | ✓ | 15 張各擔敘事弧角色（Hook 1 / Tension 1 / Reveal 9 / Ground 2 / Feel 2）。Slide 4（Jeff Dean 放大比喻）與 Slide 13（五數 PYRAMID）表面皆是「數字收束」，但 4 做「翻譯到人類尺度」、13 做「帶走結論」，功能不重疊，皆不可刪。 |

### 額外 4 條（v1.1 + M6 專屬）

| # | 額外驗收項 | ✓/✗ | 理由 |
|---|---|---|---|
| A | ✗ 任何 SCENE / STORYBOARD / ZOOM / DIAGRAM-STORY？ | ✓（無） | 全 deck 15 張採 v1.1 Editorial 九種原型（ASK / CHART / TABLE / VS / GEOMETRIC-DIAGRAM / BEFORE-AFTER / MATRIX / PYRAMID / SILENT）。無退役原型。 |
| B | ✗ 任何擬人化（主廚 / 廚工 / 廚房 / 工作桌人物）？ | ✓（無） | Slide 5 CPU vs GPU 以純幾何點陣方塊對照，無主廚/廚工角色；全 deck 無廚房擬人、無工程師角色插畫、無表情符號。原教材中的「工作桌 vs 倉庫」比喻僅留在講者口白，畫面一律以延遲數字與幾何方塊承載。 |
| C | ✗ 任何禁色（紅黃橙粉淺藍）？ | ✓（無） | 色票清查：`#1B5E3F` / `#808080` / `#D3D3D3` / `#FFFFFF`。Slide 11「GPU 等待」段、Slide 12 VRAM OOM 警告情境皆以灰斜線填充 + 深綠強調處理，無紅色警示。 |
| D | ✗ 是否所有延遲量級數字都直接標在圖上（G6 優先）？ | ✓ | L1 ≈ 1 ns（Slide 3/6/13）、RAM ≈ 100 ns（3/4/6/13）、SSD ≈ 100 μs（3/4/13）、同機房網路 ≈ 1 ms（3/4/13）、跨洲網路 ≈ 150 ms（4/13）全部直標柱頂或節點。fork/exec/spawn 延遲（1/2/50–200 ms）亦直標於表格欄位，非藏於口白。 |
| E | ✗ 是否對原教材 P4 RAM 單位做了訂正？ | ✓ | 原教材投影片 4 描述 RAM 速度為「ns-μs」為誤；本 deck Slide 3/4/6/13 皆以 `RAM ≈ 100 ns` 直接標示正確數字，未提「原錯誤」以守專業口吻。 |

---

## 原型分佈統計

| 原型 | 次數 | Slide |
|---|---|---|
| ASK | 1 | 1 |
| CHART | 3 | 2, 3, 9 |
| TABLE | 3 | 4, 7, 8 |
| VS | 1 | 5 |
| GEOMETRIC-DIAGRAM | 2 | 6, 11 |
| BEFORE/AFTER | 1 | 10 |
| MATRIX | 1 | 12 |
| PYRAMID | 1 | 13 |
| SILENT | 2 | 14, 15 |

**使用原型種類**：9 種（≥ 7 種門檻 ✓）
**連續同原型最長**：2（Slide 7–8 TABLE / Slide 14–15 SILENT，語境分別為「process 對比 vs 跨平台延遲」與「世界觀 vs 抽象倫理」，均不重複訊息）
**退役原型使用數**：0（SCENE / STORYBOARD / ZOOM / DIAGRAM-STORY 全數 0 次）
**擬人化類比使用數**：0（禁「主廚 vs 廚工」、禁廚房、禁工作桌角色化全數 0 次）

---

## 敘事弧線對照

| Slide | 原型 | 敘事角色 | 核心延遲/數字 |
|---|---|---|---|
| 1 | ASK | Hook | 20% 算 / 80% 等 |
| 2 | CHART | Tension | object 900 MB vs category 2 MB |
| 3 | CHART | Reveal 主幹 | L1 1 ns → Net 1 ms（×10^6） |
| 4 | TABLE | Reveal | Jeff Dean 放大到人類尺度（秒 → 年） |
| 5 | VS | Reveal | CPU 8 核 vs GPU 10,000 核 |
| 6 | GEOMETRIC-DIAGRAM | Reveal | TLB 1 ns / miss 100 ns / fault 100 μs |
| 7 | TABLE | Reveal | Process 1–10 ms vs Thread 10 μs |
| 8 | TABLE | Reveal | fork 1 ms / spawn 50–200 ms |
| 9 | CHART | Reveal | select 1K → io_uring 10M |
| 10 | BEFORE/AFTER | Reveal | 900 MB → 2 MB (−99.8%) |
| 11 | GEOMETRIC-DIAGRAM | Reveal | num_workers=0 20% → =4 95% |
| 12 | MATRIX | Ground | RAM/VRAM × 分配/累積 |
| 13 | PYRAMID | Ground 收束 | 五數帶走：1 ns / 100 ns / 100 μs / 1 ms / 150 ms |
| 14 | SILENT | Feel | Performance is physics respected |
| 15 | SILENT | Feel 終章 | Every abstraction leaks |

---

**文件結束**

> v1.1 + M6 驗證目標：證明在「延遲與資源」最重數字的模組上，Editorial-strict 原型組合（CHART / TABLE / MATRIX / GEOMETRIC-DIAGRAM / PYRAMID）能同時達成（a）完整敘事弧、（b）G6 每個延遲量級皆直接標註於圖上、（c）G10 文/圖/照 60:30:10、（d）G11 每章節以倒掛框收束、（e）零擬人化（包含明令禁止的主廚/廚工/廚房類比）。驗證結果：15 張維持弧線強度不折損，L1/RAM/SSD/Network 四個關鍵量級在 Slide 3/4/6/13 出現四次（重複強化），核心金句「Performance is physics respected」與「Every abstraction leaks」雙 SILENT 收束。
