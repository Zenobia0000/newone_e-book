# M6 逐頁標注：On-Page Annotation

> **定位：** 本文件是 M6（計算機組織與作業系統）原始投影片的「逐頁批注層」，供內部 reviewer 逐頁檢核。每頁附三道鏡頭：🎯 宏觀定位、🔬 細部補齊、⚠️ Reviewer 批判。目標是把 AI 工程師真正會踩到的底層直覺補足，而不只是教科書式覆蓋。
>
> **讀者：** 授課講師、技術 reviewer、後續改版負責人。
> **語氣：** 內部 review，直接指出原稿不足，補上工程師 napkin math。
> **日期基準：** 2026-04-14。

---

## P1 | 開場：你遇過這些卡關嗎？

**🎯 宏觀**：用三個真實錯誤（CUDA OOM / MemoryError / Permission Denied）建立「症狀 → 系統根因」的敘事錨點。整章的骨幹。

**🔬 細部**：三個錯誤其實對應 OS 三大次系統——VRAM（裝置記憶體管理）、虛擬記憶體（page allocator 失敗）、VFS/權限（DAC 檢查失敗）。這個對應原稿沒明說，reviewer 應在講師備忘裡補一行「三錯誤 = 三子系統」。

**⚠️ Reviewer**：
- 缺「我也遇過但不是這三個」的逃生口，建議加第四類：`Broken pipe` / `Too many open files`（file descriptor 耗盡），這在資料管線與 `DataLoader(num_workers=32)` 特別常見。
- 錯誤訊息要標示 Python/CUDA/Linux 三個來源層，避免學生以為全都是 Python 的鍋。

---

## P2 | 一段訓練背後的硬體旅程

**🎯 宏觀**：建立 disk → RAM → CPU ↔ GPU → output 的貫穿圖，作為後面所有概念的掛點。

**🔬 細部（原稿缺口補齊）**：
- **馮紐曼 vs 哈佛架構**：原稿沒提，但這是理解「為什麼 cache 存在」的根。馮紐曼（指令與資料共用記憶體與匯流排）→ von Neumann bottleneck → 現代 CPU 用 split L1（L1i / L1d，哈佛風格）來緩解。GPU SM 內部也是分離指令快取。
- **PCIe 是瓶頸層級**：CPU RAM → GPU VRAM 走 PCIe 4.0 x16（~32 GB/s）或 5.0 x16（~64 GB/s），相較 HBM3（~3 TB/s）差兩個數量級。原稿只畫箭頭，沒標頻寬數字。

**⚠️ Reviewer**：流程圖需加一層「指令路徑」與「資料路徑」分色，否則學生容易誤以為「Python 指令也要搬到 GPU」。

---

## P3 | CPU — 指令執行者

**🎯 宏觀**：CPU 是通用邏輯引擎，核心數少但單核能力強。

**🔬 細部（原稿缺口）**：
- **Pipeline**：現代 CPU 是深度管線化（Intel Golden Cove ~20 stages），fetch → decode → rename → issue → execute → retire。分支預測失敗代價 = flush pipeline = 15–20 cycles。
- **Superscalar + OoO**：單核每 cycle 可發射 4–8 μops，亂序執行。學生誤以為「單核一次做一件事」，實際上單核同時有上百個 in-flight 指令。
- **SIMD**：AVX2（256-bit）可一次處理 8 個 float32；AVX-512 可一次 16 個。NumPy 的速度優勢一半來自 SIMD，一半來自 cache locality。
- **Cache hierarchy**（整章最關鍵但原稿僅用「cache (ns)」一語帶過）：

| 層級 | 容量 | 延遲 | 量級記憶法 |
|------|------|------|-----------|
| L1 | 32–64 KB / core | ~1 ns（4 cycles） | 一個心跳的百萬分之一 |
| L2 | 256 KB–1 MB / core | ~3–10 ns | |
| L3 | 8–64 MB / socket | ~10–30 ns | |
| RAM (DDR5) | 16–512 GB | ~80–100 ns | L1 的 100 倍 |
| NVMe SSD | TB 級 | ~10–100 μs | RAM 的 100–1000 倍 |
| HDD | TB 級 | ~5–10 ms | SSD 的 100 倍 |
| Network (same DC) | — | ~0.5 ms | |
| Network (cross region) | — | ~100 ms | |

**⚠️ Reviewer**：原稿「核心數 4–128」低估了伺服器端（AMD EPYC 9754 有 128 實體核、Intel Xeon Max 56 核 + HBM）。建議改為「桌機 4–24，伺服器 32–256」。SIMD 與 pipeline 這兩個觀念如果不補，後面講「為什麼 NumPy 比 list 快」就沒有力道。

---

## P4 | RAM — 工作桌，不是倉庫

**🎯 宏觀**：RAM 是工作空間，速度與容量的折衷，OOM 發生在這一層。

**🔬 細部（原稿缺口）**：
- **DataFrame 爆記憶體的物理原因**：pandas `object` dtype 每個 cell 是 Python 物件指標（8 bytes）+ 物件 header（~56 bytes for str）+ 實際資料，一個看似 1 GB 的 CSV 讀進來可能膨脹到 5–10 GB。這是 AI 工程師最常踩的坑，原稿僅說「100 萬 × 100 欄 = 800 MB」只涵蓋 numeric dtype 的理想情境。
- **複製成本**：`df2 = df.copy()` 是 O(n) 複製；`df[df.a > 0]` 視條件可能是 view 也可能是 copy（SettingWithCopyWarning 的根源）。pandas 2.x 的 Copy-on-Write 改變了這個行為，建議在講師備忘加一行。
- **虛擬記憶體**：學生會問「我有 32 GB RAM，為什麼載到 24 GB 就 OOM？」答案：OS 為其他 process、page cache、kernel 保留空間；Linux 的 overcommit + OOM killer 可能在到達物理上限前就砍掉你的 process。
- **Page 大小**：標準 4 KB，Transparent HugePages 2 MB。大 tensor 分配若走 huge page TLB 命中率大幅提升。

**⚠️ Reviewer**：「速度層級 CPU cache (ns) >> RAM (ns-μs)」這句有誤，RAM 延遲是 **ns 級（~80–100 ns）不是 μs**。必須修正，否則後面所有量級推論都會歪。

---

## P5 | GPU — 為什麼深度學習愛它？

**🎯 宏觀**：SIMT（Single Instruction Multiple Threads）架構，為 dense linear algebra 設計。

**🔬 細部（原稿缺口）**：
- **SM / Warp 概念**：NVIDIA GPU 由數十個 SM（Streaming Multiprocessor）組成，每個 SM 以 warp（32 threads）為最小排程單元，一個 warp 內 32 threads 同時執行同一條指令（lockstep）。分支發散（warp divergence）會讓一半 threads 空轉——原稿完全沒提，但這是「為什麼 if/else 在 GPU 很貴」的根因。
- **CUDA memory hierarchy**（必補）：

| 層級 | 範圍 | 延遲（cycles） | 容量 |
|------|------|---------------|------|
| Register | per thread | 1 | ~256 / thread |
| Shared memory / L1 | per SM | ~20–30 | 100–228 KB |
| L2 | per GPU | ~200 | 40–60 MB |
| HBM (VRAM) | per GPU | ~400–800 | 24–80 GB |
| PCIe to host | — | ~數 μs | — |

- **Tensor Core**：Ampere/Hopper 的矩陣乘加專用單元，FP16/BF16/FP8 吞吐是一般 CUDA core 的 8–16 倍。PyTorch 的 `autocast` 自動走 Tensor Core。
- **VRAM vs RAM 物理分離**：透過 PCIe 連接，`.to('cuda')` 是真實的 DMA 複製。NVLink（H100 900 GB/s）在伺服器 GPU 間才有。

**⚠️ Reviewer**：原稿「幾千個弱核心」這個比喻在 SIMT 語境下其實不精確——GPU 的「核」不是獨立核，是 warp lane。建議改成「幾萬條 lane，以 32 lane 為一組 lockstep」。

---

## P6 | 資料移動成本 — DataLoader

**🎯 宏觀**：I/O bound vs compute bound 的教學點，DataLoader 就是在解 I/O bound。

**🔬 細部（原稿缺口）**：
- **DataLoader 為何能加速（物理解釋）**：
  1. `num_workers=N` 建立 N 個子 process（fork + CoW），每個 process 有自己的 Python 直譯器繞過 GIL。
  2. 子 process 並行走 syscall `read()` / `pread()`，讓 kernel page cache 預熱、讓 NVMe queue depth 拉滿（NVMe 最佳 QD ~ 32–128）。
  3. 主 process 透過 shared memory（`/dev/shm`，tmpfs）或 queue 收回資料，避免 pickle 序列化成本（`persistent_workers=True` 可以避免 worker 重啟）。
  4. `pin_memory=True` 讓 tensor 配置在 page-locked memory，GPU 可以直接 DMA 而不需 CPU 中介的 bounce buffer → 傳輸速度 2–3 倍。
  5. `non_blocking=True` 搭配 pinned memory 讓 `.to('cuda')` 非同步，CPU 可以繼續排下一個 batch。
- **roofline 模型**：compute / bandwidth 的比值（arithmetic intensity）決定了你是 memory bound 還是 compute bound。小 batch + 大模型常是 compute bound，大 batch + 小模型常是 memory bound。原稿講 batch size 取捨但沒給出模型。

**⚠️ Reviewer**：`num_workers=4` 的「4」在 Linux 是 `fork`，在 Windows 是 `spawn`（重新啟動 Python 直譯器 + 重 import），這跨平台差異會在練習 A 踩雷，建議在 P6 腳註加一行警告。

---

## P7 | 練習 A — 資料搬運標注

**🎯 宏觀**：把流程內化到程式碼對應。

**🔬 細部**：原稿參考答案第 (2) 行「建立 4 個子 process」在 Windows spawn 模式下其實要到 `for images, labels in loader:` 才真正建立。第 (5) 行 `images.to('cuda')` 若未加 `non_blocking=True`，會是 blocking transfer，GPU 必須等待。

**⚠️ Reviewer**：
- 練習沒涵蓋 `pin_memory` 與 `non_blocking`，是原稿在 P6 提了但練習沒考，建議加第 (10) 行改寫題讓學生補回這兩個參數。
- 「inode 被讀取」這個用詞對 Windows（NTFS MFT）學生不公平，建議改「目錄索引被讀取」較中性。

---

## P8 | 從硬體到作業系統

**🎯 宏觀**：Red Hat 的三大 OS 功能（排程 / 記憶體 / 檔案系統）是接下來的章節骨架。

**🔬 細部**：漏掉第四支柱——**I/O 與網路子系統**（VFS、block layer、epoll、io_uring）。AI 工程師在資料管線、分散式訓練、線上推論都會碰到，不該省。

**⚠️ Reviewer**：建議改為四支柱（加 I/O），或至少在 P11 File System 頁補回 epoll / io_uring 的概念卡。

---

## P9 | Process vs Thread

**🎯 宏觀**：隔離 vs 共享的本質對比，GIL 是 Python 特殊限制。

**🔬 細部（原稿缺口）**：
- **Context switch 成本**：process 切換 ~1–10 μs（刷 TLB、換 page table root）；thread 切換 ~0.5–2 μs（同 address space，不刷 TLB）。核心上下文切換涉及 register file save/restore + cache pollution。
- **fork vs exec**：`fork()` 複製整個 process（CoW 讓複製延遲到寫入時才發生）；`exec()` 用新程式替換當前 process image。Python `multiprocessing` 在 Linux 預設 `fork`（快，但共用 CUDA context 會出問題，所以 PyTorch 建議 `spawn`）；macOS 3.8+ 預設 `spawn`。
- **GIL 的本質**：每 ~5 ms（Python 3.2+ 用 `sys.setswitchinterval`）釋放一次，I/O bound thread 可自動釋放 GIL（`time.sleep`、`socket.recv`、NumPy C 擴充），所以 I/O 多執行緒仍有用。**原稿沒講 I/O bound 例外**，會讓學生以為 threading 全無用。
- **PEP 703 free-threaded CPython**：3.13 實驗性支援，2026 年值得在備忘提一句（「GIL 不是永恆的」）。

**⚠️ Reviewer**：建議加一張 context switch 成本量級表，和 cache hierarchy 表並列放在備忘的 napkin math 附錄。

---

## P10 | 記憶體管理 — OOM

**🎯 宏觀**：兩戰場（RAM / VRAM），不同診斷路徑。

**🔬 細部（原稿缺口）**：
- **虛擬記憶體 / page table / TLB**：每個 process 看到的是 virtual address，MMU 用 page table（x86-64 四級 / 五級）翻譯成 physical address。TLB cache 這個翻譯（~64–1024 entries），TLB miss 要走 page walk（數十到數百 cycles）。大 DataFrame 連續走訪會命中 TLB，隨機索引會 TLB miss。
- **Page fault**：分 minor（page 在 RAM 但尚未映射）、major（page 在 swap / 檔案需讀回）。Major page fault 可到 ms 級，是「突然很慢」的常見根因。
- **OOM killer**：Linux 在記憶體耗盡時會挑 `oom_score` 高的 process 砍掉，你看到的不是 `MemoryError` 而是 process 被 `SIGKILL` 直接消失。`dmesg | grep -i oom` 可以找到日誌。
- **VRAM 碎片化**：PyTorch 有自己的 caching allocator，`torch.cuda.empty_cache()` 只釋放未使用的 block，不會釋放已分配給 tensor 的。`PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` 可緩解碎片。

**⚠️ Reviewer**：原稿的診斷工具清單缺 `/proc/meminfo`、`free -h`、`torch.cuda.memory_summary()`，都該補。

---

## P11 | File System — 路徑不只是字串

**🎯 宏觀**：路徑是 OS 提供的命名抽象，不是字串。

**🔬 細部（原稿缺口）**：
- **File descriptor**：`open()` 回傳的整數是 process 的 fd table 索引，指向 kernel 的 open file table，再指向 inode。Python `f.close()` 未呼叫會導致 fd 洩漏，ulimit 預設 1024，AI 資料管線爬大量小檔容易耗盡。`Too many open files` 的根因。
- **epoll / io_uring**：
  - `select`（O(n)）→ `poll` → `epoll`（O(1)，Linux 2.6）：監聽大量 fd 事件的機制，asyncio、aiohttp、Kafka client 全靠它。
  - `io_uring`（Linux 5.1+）：ring buffer 式非同步 I/O，syscall amortized 成本極低，對資料集 scan 場景有量級提升。2026 年的資料工程新寵。
- **VFS 抽象層**：ext4 / XFS / tmpfs / NFS / FUSE / s3fs 統一透過 VFS，所以 `/mnt/s3/...` 的路徑看起來和本地一樣，但每次 read 其實是 HTTP 請求——這是「為什麼資料在 S3 上訓練慢」的根因。
- **權限**：rwx 只是 DAC；還有 ACL（`getfacl`）、SELinux / AppArmor（MAC），在企業伺服器會遇到「rwx 看起來對但還是 Permission denied」。

**⚠️ Reviewer**：`pathlib.Path` 很好但原稿沒提 `os.PathLike` 協議與 `pathlib` 在 Windows 路徑長度限制（260 字元，非 long path 模式）。部署到 Windows CI 容易踩。

---

## P12 | 環境差異

**🎯 宏觀**：跨環境重現性，Docker 是工業標準答案。

**🔬 細部（原稿缺口）**：
- **Container 本質**：不是虛擬機，是 Linux namespaces（pid / net / mount / uts / ipc / user）+ cgroups（CPU / memory / I/O 配額）+ union filesystem（overlayfs）。這個底層知識幫助學生理解「為什麼 Docker 比 VM 輕」。
- **CUDA 相容性矩陣**：host driver 版本 ≥ container CUDA runtime，否則 `nvidia-container-toolkit` 會失敗。建議在備忘加「查詢 `nvidia-smi` 最上面那行」的 SOP。
- **環境變數 `LD_LIBRARY_PATH`**：常見陷阱，conda 與系統 CUDA 衝突。

**⚠️ Reviewer**：「Windows 沒有 fork()」是對的，但應補一句「Windows 10+ 的 WSL2 其實是 Linux kernel，所以在 WSL 下 fork 正常」。很多學員在 WSL，搞錯會迷惑。

---

## P13 | 練習 B — 診斷 OOM

**🎯 宏觀**：症狀 → 原因 → 解法的逆推練習。

**🔬 細部**：參考答案正確但不完整。梯度累積的物理機制應明說：`.backward()` 會把梯度 **加** 到 `param.grad` 上（不是覆蓋），所以不清零會疊加。這個 API 設計是 for gradient accumulation，不是 bug。

**⚠️ Reviewer**：
- 應加第四問：「如果降了 batch size 還是 OOM？」引導到 mixed precision、gradient checkpointing、activation offload。
- `CUDA out of memory` 訊息通常帶「Reserved 而未分配」數字，應教學生讀這個數字判斷碎片化。

---

## P14 | 模組總結

**🎯 宏觀**：六問串全章，回扣金句。

**🔬 細部**：第 4 問「為什麼 NumPy 比 list 快」回答只有 cache，漏了 SIMD 與避開 Python 物件開銷（每個 int 物件 28 bytes vs int64 8 bytes）。三因素都該提。

**⚠️ Reviewer**：金句 "Systems turn local scripts into scalable applications." 很好，但 M6 的真正 takeaway 更接近「Performance is physics」。建議在結尾加第二金句："Every abstraction leaks; know the layer below yours." 以呼應 Joel Spolsky 的 Law of Leaky Abstractions，點醒 AI 工程師不是不碰底層，而是要有能力下潛。

---

## 全章補齊清單（給下一版改稿人）

必補：
1. Cache hierarchy 延遲量級表（放 P3 或附錄）
2. 虛擬記憶體 / page table / TLB（P10）
3. GPU SM / warp / CUDA memory hierarchy（P5）
4. fork vs exec vs spawn 三者差異（P9）
5. File descriptor 與 epoll / io_uring（P11）
6. DataFrame object dtype 膨脹機制（P4 或 P10）
7. RAM 延遲單位修正（P4，ns 非 μs）

建議補：
8. Roofline 模型一張圖（P6）
9. PyTorch caching allocator 行為（P10）
10. Container namespaces + cgroups（P12）

---

_本文件結束。配套文件：`02_three_lens_analysis.md`、`03_bcg_narrative.md`、`04_layout_visual_spec.md`、`05_minimum_viable_knowledge.md`。_
