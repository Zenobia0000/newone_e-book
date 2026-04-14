# M6 BCG 敘事腳本：Performance Is Physics Respected

> **定位：** 本文件是 M6 模組的「高階敘事版」，以 BCG / McKinsey 式 pyramid principle 撰寫。用於技術主管、產品經理、跨部門技術討論會的 15 分鐘簡報版本。Governing Thought 先行，MECE 三支柱支撐，每頁一個 so-what。
>
> **對象：** 工程主管、資料科學團隊 lead、跨部門技術討論會參與者。
> **時長：** 15 分鐘報讀 + 15 分鐘討論。
> **頁數：** 14 頁主線 + 金句頁。
> **語氣：** 顧問式，結論前置，每頁 so-what 明確。

---

## Governing Thought（總論金句）

> **"Performance is not magic; it is physics respected."**

**Supporting**：
- AI 系統的效能與穩定性，由三個物理約束決定——運算速度、記憶體階層、I/O 與排程。
- 這三者都不是「工程選擇」，是光速、能量、通訊成本強加的結構。
- 工程師的工作不是繞過物理，是**在物理限制內做最佳取捨**。

**So-what for the business**：
- 投入 GPU 不等於訓練會變快——瓶頸常在資料管線（I/O bound），單純加 GPU 是錢燒掉。
- OOM 不是偶發 bug，是容量規劃問題，有結構化解法。
- 跨環境重現性不是運維問題，是系統邊界設計問題。

---

## MECE 三支柱

```
                   Performance Is Physics Respected
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
    運算 (Compute)      記憶體 (Memory)       I/O 與排程 (I/O & Scheduling)
    ───────────          ──────────             ───────────────
    CPU / GPU           階層與容量              檔案系統與排程
    異構架構             OOM 結構                Process / Thread
    SIMD / SIMT        VRAM vs RAM             DataLoader
    能量取捨            TLB / Page              容器化
```

這三支柱彼此正交（MECE），合起來窮盡 AI 系統效能的所有物理決定因素。

---

## 腳本（14 頁主線）

### 頁 1 — Title / Hook

**標題**：M6: Performance Is Physics Respected — 為什麼 AI 系統的機械室值得你打開

**Hook（30 秒）**：
> 過去一季我們的團隊遇到三類卡關：訓練跑不快、記憶體爆掉、在我機器上沒問題。這三類問題看似無關，其實是同一件事——我們的程式碰到了物理邊界，但我們還在用抽象語言解釋它。今天 15 分鐘，我想把這個邊界畫清楚。

**So-what**：這不是一場「底層技術分享」，是一次**成本結構復盤**。

---

### 頁 2 — Executive Summary（結論先行）

三個 bullet，全章壓縮：

1. **效能瓶頸 80% 在資料搬運，不在運算**。GPU 利用率低於 70% 的團隊，問題幾乎都在 disk → RAM → VRAM 這條鏈。
2. **OOM 是可預測的容量問題**，不是 bug。RAM OOM 與 VRAM OOM 有不同戰場，診斷路徑固定。
3. **跨環境失敗有四根因**（OS / 權限 / 套件 / 環境變數），Docker 是工業解。不是 nice-to-have，是部署前提。

**So-what**：接下來三支柱展開。

---

### 頁 3 — 支柱 1 標題頁 | Compute

**標題**：運算 — 通用引擎 vs 平行引擎

**核心訊息**：CPU 與 GPU 不是替代關係，是分工關係。深度學習愛 GPU，不是因為 GPU 神奇，是因為深度學習的計算結構（大量同質矩陣運算）剛好命中 GPU 的物理設計。

**一張圖**：CPU（少量強核 + 大 cache + 複雜控制）vs GPU（萬級 lane + SIMT + HBM）。

**So-what**：買 GPU 之前先問「我的瓶頸是 compute 還是 I/O」，roofline 圖說了算。

---

### 頁 4 — Compute 的物理根源

**核心訊息**：三個量級差決定了 CPU 與 GPU 的分工：

| 維度 | CPU (桌機級) | GPU (A100) |
|------|-------------|-----------|
| 核心數 | ~16 | 6,912 CUDA + 432 Tensor Core |
| 單核頻率 | ~4 GHz | ~1.4 GHz |
| 記憶體頻寬 | ~50 GB/s (DDR5) | ~2,000 GB/s (HBM2e) |
| 分支友善度 | 極高 | 極低（warp 發散） |
| 適用 | if/else、小批次、系統任務 | 矩陣乘加、大批次、同質運算 |

**So-what**：
- 前處理 pipeline 常被誤放到 GPU，反而慢（分支密集 + 小批次）。
- 模型推論若 batch size = 1，GPU 高達 80% 的 lane 在空轉。考慮 CPU 推論或 batching。

---

### 頁 5 — 支柱 2 標題頁 | Memory

**標題**：記憶體階層 — 光速強加的金字塔

**核心訊息**：記憶體不是一種東西，是一個階層。每層延遲差 10–100 倍，這是光速決定的，不是工程選擇。

**一張圖**（記憶體階層金字塔）：

```
        Register (1 cycle)            ← CPU 內部
        L1 Cache (1 ns)
       L2 Cache (4 ns)
      L3 Cache (30 ns)
     RAM (100 ns)                    ← 主機板
    NVMe SSD (10-100 μs)             ← 外接裝置
   HDD (5-10 ms)
  Network (0.5-150 ms)               ← 跨機器/跨區
```

**So-what**：寫程式時你看到的是「記憶體」三個字，實際跨越 8 個數量級。一次誤用（例如 random access 一個不在 cache 的大陣列）可能讓效能降 100 倍。

---

### 頁 6 — Memory 的工程後果

**核心訊息**：階層決定了三類 AI 工程最常踩的坑：

1. **DataFrame 物理膨脹**：pandas `object` dtype 讓 1 GB CSV 膨脹 5–10 倍進 RAM。根因：每 cell 是 Python 物件指標 + header + 資料。
2. **VRAM 碎片化**：PyTorch caching allocator 不會把已分配 block 還回給 driver，長時間訓練 VRAM 使用率虛高。
3. **TLB miss**：大 tensor 隨機索引會繞過 TLB，每次存取多 100 ns。Hugepage 可解。

**So-what**：OOM 不是等它發生才處理。**容量規劃應在 architect 階段完成**：估算 model + activation + gradient + optimizer state 四項記憶體（典型 1:1:1:2 比例）。

---

### 頁 7 — 支柱 3 標題頁 | I/O & Scheduling

**標題**：I/O 與排程 — 讓硬體忙起來的 OS 工作

**核心訊息**：硬體是被動的。讓 GPU 跑滿 95% 利用率、讓磁碟跑滿頻寬，是 OS 排程 + 程式設計的責任。

**一張圖**：訓練時序圖，`num_workers=0` vs `num_workers=8` 的 GPU 空窗差異。

**So-what**：GPU 利用率低 = 錢在燒。H100 每小時 $6，70% 利用率等於每小時丟 $1.8。一年 8760 小時 = $15,768 白燒。

---

### 頁 8 — I/O 的三個槓桿

**核心訊息**：三個參數可以把 GPU 利用率從 40% 拉到 90%：

| 槓桿 | 機制 | 效益 |
|------|------|------|
| `num_workers=N` | 多 process fork，繞過 GIL，並行 read syscall | 2–8× throughput |
| `pin_memory=True` | tensor 配置在 page-locked RAM，DMA 直通 | 2–3× transfer speed |
| `non_blocking=True` | 非同步 host→device 傳輸，重疊 compute 與 transfer | 1.5–2× overall |

**So-what**：三個 bool/int 參數，綜合可換 3–5 倍訓練速度。應成為 training checklist 第一行。

---

### 頁 9 — Scheduling 的 Python 陷阱

**核心訊息**：Python GIL 讓 threading 在 CPU 密集任務上無效。這不是 bug，是工程取捨。

**一張圖**：threading（一把 GIL 鎖住多 thread）vs multiprocessing（N 個 process 各有 GIL，真正並行）。

**決策樹**：
- CPU 密集（NumPy 計算、純 Python loop） → `multiprocessing` 或 C 擴充
- I/O 密集（網路、檔案） → `asyncio` 或 `threading` 皆可
- 混合 → `ProcessPoolExecutor` for compute + `asyncio` for I/O

**So-what**：選錯並行模型，投入再多 CPU 都沒用。先分類任務，再選工具。

---

### 頁 10 — 跨支柱整合：一次訓練的物理旅程

**核心訊息**：把三支柱串起來看一次 PyTorch 訓練步驟，每個物理動作對應一個支柱：

| 步驟 | 物理動作 | 支柱 |
|------|---------|------|
| 讀取 batch | NVMe 4KB random read, DMA to RAM | I/O |
| 前處理 | CPU SIMD 解碼 JPEG | Compute |
| `.to('cuda')` | PCIe DMA RAM → VRAM | Memory + I/O |
| Forward | GPU Tensor Core 矩陣乘 | Compute |
| Backward | autograd 反向圖執行 | Compute + Memory |
| Optimizer step | VRAM 內讀取權重 + 梯度 | Memory |

**So-what**：任一環節慢，整鏈就慢。Profiler（PyTorch Profiler / Nsight）告訴你卡在哪一環。

---

### 頁 11 — 金句頁（中段能量點）

> **"Every abstraction leaks; know the layer below yours."**
>
> —— Joel Spolsky, Law of Leaky Abstractions

全頁大字排版，深藍灰背景。底下一行小字：

> 抽象不是用來讓你不懂底層，是用來讓你在需要時**能下潛**。

**So-what**：AI 工程師的護城河，是在抽象層工作、在物理層思考的能力。

---

### 頁 12 — 跨環境的困境：重現性

**核心訊息**：「在我機器上沒問題」的四根因（OS / 權限 / 套件 / 環境變數）本質是**環境邊界未被定義**。

**一張圖**：Docker 把 OS 層 + 套件層 + 環境變數層全部打包進 image，邊界明確。

**商業意涵**：
- 沒 Docker → 每次部署靠人工校對 = 高 MTTR + 低敢動性
- 有 Docker → image 即契約 = 快速 rollback + 可重複訓練

**So-what**：Docker 不是技術選擇，是**部署契約**。沒有契約，協作不可 scale。

---

### 頁 13 — 團隊能力地圖

**核心訊息**：M6 的概念，對應三類團隊角色的最低能力線：

| 角色 | 必會 | 建議會 |
|------|------|-------|
| Data Scientist | OOM 診斷、DataLoader 三參數、`pathlib` | Roofline、Profiler |
| ML Engineer | 上欄全部 + Docker + `multiprocessing` | TLB / page、CUDA memory hierarchy |
| ML Platform | 上欄全部 + cgroups / namespaces + io_uring | Kernel tuning、NCCL |

**So-what**：新人入職 60 天內應能達到角色對應的「必會」欄。招聘與 onboarding 教材可以直接對齊。

---

### 頁 14 — Closing / The Ask

**標題**：從能跑到能上線 — 我們下一步請這樣做

**三個具體 ask**：

1. **訓練腳本 PR checklist 新增三行**：是否設定 `num_workers`、`pin_memory`、`torch.cuda.memory_summary()` 監控。
2. **新進工程師入職 30 天內過一遍 M6 napkin math checklist**（10–15 題，見配套文件 05）。
3. **團隊本季指標新增 GPU 利用率目標 ≥ 80%**。利用率低於 50% 的 job 須提出 profiling 報告。

**Closing 金句**（回扣 Governing Thought）：
> Performance is not magic; it is physics respected.
> 我們不對抗物理——我們對齊它，然後讓業務跑贏。

---

## 金句頁總表（給設計師）

| 位置 | 金句 | 配色 |
|------|------|------|
| 扉頁 | "Performance is not magic; it is physics respected." | 深藍灰底 + 金色字 |
| 中段 P11 | "Every abstraction leaks; know the layer below yours." | 深藍灰底 + 白字 |
| 結尾 | "We don't fight physics — we align with it." | 漸層背景 + 大字 |

---

## Closing Ask 詳版（給主管層）

給技術 VP / 工程總監可帶走的三份 artifact：

1. **《M6 napkin math 速查卡》**（配套文件 05）— 發放到團隊 wiki，onboarding 必讀。
2. **訓練 job profiling SOP** — 基於 PyTorch Profiler，產出 GPU 利用率、I/O 時間比、VRAM peak 三指標。
3. **容器化部署契約範本** — Dockerfile + `requirements.lock` + `.env.example` 三件組，成為所有 ML 專案 baseline。

---

## 備援 Q&A 卡（預期 pushback）

**Q1：資料科學家不用懂到這麼底層吧？**
A：不用精通實作，但要會**讀**。讀懂 `nvidia-smi`、讀懂 Profiler 輸出、讀懂 OOM 訊息——這是效率與成本的直接差異。

**Q2：這些是不是 DevOps 的工作？**
A：容器化是 DevOps，但**知道 batch size 與 VRAM 的關係**是 DS/ML 自己的工作。界線要清楚。

**Q3：Docker 學習成本高？**
A：團隊只需要 3 個動作：`docker build`、`docker run --gpus all`、`docker push`。其他交給 template。

**Q4：GPU 利用率 80% 目標太激進？**
A：業界大廠（Meta、OpenAI 公開數據）訓練作業通常 >85%。80% 是保守線。未達線先看 I/O，不是先加硬體。

---

_配套文件：`01_on_page_annotation.md`、`02_three_lens_analysis.md`、`04_layout_visual_spec.md`、`05_minimum_viable_knowledge.md`。_
