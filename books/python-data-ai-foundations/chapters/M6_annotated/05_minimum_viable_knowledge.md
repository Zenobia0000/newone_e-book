# M6 最小可行知識：Minimum Viable Knowledge（MVK）速學卡

> **定位：** 本文件是 M6 的「考前一晚 30 分鐘讀完就不慌」版本，提供 12 張速學卡 + 延遲數字快查表。每卡一面 Q / 一面 A 形式，可直接印成實體卡片或塞進 Anki。對象：新進 AI 工程師、跨組快速 onboarding、M7 前的 spaced repetition。內部 review 語氣。

---

## 使用方法

1. 先看 **延遲數字快查表**，能背出 5 個量級就及格。
2. 再翻 **12 張速學卡**，Q 面自問，A 面驗證。
3. 不會的標記起來，一週後重做（spaced repetition）。
4. 若 10 張以上能當場答出，M6 算是內化了，可以進 M7。

---

## 延遲數字快查表（必背）

### CPU / Memory 側

| 操作 | 延遲 | 記憶法 |
|------|-----:|--------|
| L1 cache | **1 ns** | baseline（一個脈搏） |
| L2 cache | 4 ns | 4× |
| L3 cache | 30 ns | 30× |
| Main memory (DDR5) | **100 ns** | 100× |
| Mutex lock/unlock | 17 ns | 比 RAM 快 |
| Branch mispredict | 3 ns | |
| Syscall | ~100 ns | 和 RAM 同級 |
| Function call | ~1 ns | 不計成本 |

### I/O 側

| 操作 | 延遲 | 記憶法 |
|------|-----:|--------|
| NVMe SSD random 4K read | **10 μs** | 10⁴× vs L1 |
| NVMe SSD sequential 1MB | 50 μs | |
| HDD seek | 5 ms | 已少用 |
| Send 1 KB over 10 Gbps | 1 μs | |
| Same-DC round trip | **500 μs** | 5×10⁵× |
| Cross-region RTT | **150 ms** | 光速限制 |

### GPU / PCIe

| 操作 | 數字 |
|------|-----:|
| GPU register | 1 cycle |
| GPU shared memory | ~30 cycles |
| GPU L2 | ~200 cycles |
| HBM VRAM | ~500 cycles / 2 TB/s |
| PCIe 4.0 x16 | ~32 GB/s |
| NVLink 4 | 900 GB/s |
| Warp size | **32 threads** |

### 並行成本

| 操作 | 成本 |
|------|-----:|
| Thread context switch | 0.5–2 μs |
| Process context switch | 1–10 μs |
| fork (1 GB process, CoW) | ~1 ms 建立 |
| TLB miss → page walk | ~100 cycles |
| Major page fault (swap) | ms 級 |

---

## 速學卡 × 12

---

### 卡 01 | 為什麼 L1 存取比 RAM 快 100 倍？

**A：光速物理。** L1 cache 緊貼 CPU core（距離 mm 級），RAM 在主機板另一側（距離 cm 級）。即使頻寬無限，單次 round trip 仍受光速限制。記憶體階層不是工程選擇，是物理強加的結構。

**一句話**：延遲由**距離**決定，不是由頻寬決定。

---

### 卡 02 | 為什麼 GPU 適合深度學習？

**A：三件事的交集**：

1. **SIMT 架構** — 一條指令同時驅動 32 thread（warp），適合「相同運算重複上百萬次」
2. **HBM 頻寬** — ~2 TB/s，是 DDR5 的 40 倍，餵得飽大量平行 ALU
3. **Tensor Core** — 專用矩陣乘加單元，FP16 吞吐是一般 CUDA core 的 8–16 倍

**一句話**：深度學習的計算結構（大量同質矩陣運算）剛好命中 GPU 的物理設計。

---

### 卡 03 | CPU RAM 與 GPU VRAM 是同一塊記憶體嗎？

**A：不是。** 物理上分離，透過 PCIe 連接。

- `.to('cuda')` 是真實的 DMA 複製，不是「指向」
- `MemoryError` = CPU RAM 滿；`CUDA out of memory` = GPU VRAM 滿
- 診斷工具也不同：`htop` vs `nvidia-smi`

---

### 卡 04 | Python GIL 是什麼，為什麼存在？

**A**：Global Interpreter Lock。CPython 在任何時刻只允許**一個** thread 執行 Python bytecode。

**為什麼存在**：CPython 的 reference counting 需要原子操作，GIL 是最簡單的正確性保證。細粒度鎖會讓同步成本吃掉 multithreading 的收益。

**後果**：
- CPU 密集任務用 `threading` **不會變快** → 用 `multiprocessing`
- I/O bound 仍有用（`socket.recv` 等會釋放 GIL）
- NumPy / PyTorch 的 C 擴充會主動釋放 GIL，所以它們的計算不受 GIL 限制

**一句話**：GIL 不是 bug，是 CPython 的工程取捨；PEP 703（3.13）開始實驗性移除。

---

### 卡 05 | Process 與 Thread 差在哪？

| 維度 | Process | Thread |
|------|---------|--------|
| 記憶體空間 | 獨立 | 共用 |
| 建立成本 | ~1 ms（fork CoW） | ~10 μs |
| Context switch | ~1–10 μs（刷 TLB） | ~0.5–2 μs |
| 通訊 | pipe / queue / shm | 共享記憶體（直接） |
| 崩潰影響 | 隔離 | 整個 process 崩 |

**一句話**：Process 是**隔離**單位，Thread 是**共享**單位。

---

### 卡 06 | OOM 發生時實際上在哪一層？

**兩戰場**：

**RAM OOM**：
- Linux overcommit allocator 耗盡可用 page
- 輕則 `MemoryError` 拋出，重則 OOM killer 直接 `SIGKILL`
- 症狀：process 突然消失，`dmesg | grep -i oom` 可見日誌

**VRAM OOM**：
- PyTorch caching allocator 無法再分配 block
- 訊息：`RuntimeError: CUDA out of memory. Tried to allocate X GiB`
- 通常可恢復（不會殺 process）

**解法路徑不同**：RAM 用 chunking、釋放引用；VRAM 用降 batch、AMP、gradient checkpointing、`optimizer.zero_grad()`。

---

### 卡 07 | DataLoader 的三個魔法參數

| 參數 | 作用 | 物理解釋 |
|------|------|---------|
| `num_workers=N` | N 個子 process 並行讀檔 | 繞過 GIL，拉滿 NVMe queue depth |
| `pin_memory=True` | tensor 放 page-locked RAM | DMA 直通，省掉 bounce buffer，傳輸 2–3× |
| `non_blocking=True` | 非同步 `.to('cuda')` | CPU 與 GPU overlap，再疊 1.5–2× |

**三者合起來**：綜合 3–5 倍訓練加速。應進入 training SOP。

**警告**：Windows 下 `num_workers > 0` 用 `spawn`（重 import），頂端程式碼不能放 side effect。

---

### 卡 08 | 為什麼 DataFrame 容易爆記憶體？

**A：pandas 的 object dtype**。每個 cell 是：

```
Python object pointer (8 B) + object header (~56 B) + actual data
```

一個看似 1 GB 的 CSV（若大量字串欄）讀進來**可膨脹 5–10 倍**到 RAM。

**解法**：
- 字串欄轉 `category`（重複值少時大幅節省）
- 數字欄強制 `int32` / `float32` 而非預設 `int64` / `float64`
- 用 `chunksize` 分批讀，或改用 polars / pyarrow（Arrow columnar 格式）

**一句話**：pandas 記憶體不是你看到的 CSV 大小，是 CSV 大小 × 物件膨脹係數。

---

### 卡 09 | 虛擬記憶體、Page Table、TLB

**虛擬記憶體**：每個 process 看到自己的 0 ~ 2⁴⁸ 位址空間（x86-64），由 MMU 翻譯為物理位址。

**Page Table**：4 級（x86-64）樹狀結構，儲存 virtual → physical 對應。Page 大小 4 KB（標準）或 2 MB（hugepage）。

**TLB**：Page Table 的 cache，64–1024 entries。
- TLB hit：1 ns
- TLB miss：走 page walk，~100 cycles

**工程後果**：
- 大 tensor 連續存取 → TLB 友善
- 大 tensor 隨機索引 → TLB miss 密集，可能慢 10 倍
- Hugepage（2 MB）可減少 TLB pressure

---

### 卡 10 | File Descriptor 與 `Too many open files`

**fd 是什麼**：`open()` 回傳的整數，是 process 的 fd table 索引 → kernel open file table → inode。

**常見坑**：
- Python `open()` 忘了 `close()`（用 `with` 解決）
- `DataLoader(num_workers=32)` × 每 worker 開幾十檔 → 破 ulimit 1024
- socket 洩漏、requests session 沒關

**診斷**：
```bash
ulimit -n               # 查上限
ls /proc/<pid>/fd | wc -l   # 查當前用量
```

**解法**：`ulimit -n 65536`；或用 `with` / context manager 嚴格管理生命週期。

---

### 卡 11 | epoll / io_uring 為什麼重要？

**背景**：監聽大量 fd 事件（socket、檔案）時，`select`（O(n)）→ `poll` → `epoll`（O(1), Linux 2.6）是核心演進路線。

**epoll**：asyncio、aiohttp、Kafka client、nginx 全靠它。高併發網路服務的基石。

**io_uring**（Linux 5.1+，2019）：ring buffer 式非同步 I/O，syscall 成本 amortized 極低，對資料集 scan、日誌寫入、DB 引擎有量級提升。2026 年新寵，ScyllaDB、PostgreSQL 17+ 都整合了。

**一句話**：你不一定直接寫 epoll，但你用的每個現代框架都靠它。

---

### 卡 12 | Docker 為什麼能解決「在我機器上沒問題」？

**A：它不是虛擬機，是 Linux namespace + cgroups + overlayfs 的組合**。

- **Namespace**（隔離）：pid / net / mount / uts / ipc / user 六種
- **cgroups**（配額）：CPU / memory / I/O / network 限制
- **Overlayfs**（分層）：image 是唯讀層 + 可寫層，build 增量快取

**打包了什麼**：
1. OS userspace（glibc 版本）
2. Python 與套件版本（`requirements.lock`）
3. 環境變數（`ENV`）
4. 檔案系統佈局（`COPY`）
5. 啟動指令（`CMD`）

**沒打包什麼**：
- Kernel（共用 host）→ 所以 Linux image 不能跑在純 Windows（需 WSL2 / Hyper-V）
- GPU driver（需 `nvidia-container-toolkit` + host driver ≥ container CUDA runtime）

**一句話**：Docker 是**部署契約**，不是 nice-to-have。

---

## 自測題（不給答案，想清楚再翻卡）

1. 你訓練 GPU 利用率只有 40%，前三個要檢查的地方？
2. `MemoryError` 與 `CUDA out of memory` 你會用哪個工具診斷各自？
3. `num_workers=8` 在 Windows 與 Linux 的差異是什麼？
4. 為什麼 `del df` 後記憶體沒立刻釋放？
5. NVMe 隨機 4K 讀取要幾微秒？比 L1 cache 慢幾倍？
6. Process 與 Thread 的 context switch 成本差幾倍，為什麼？
7. TLB miss 發生在什麼情況下？對大 DataFrame 有什麼影響？
8. 為什麼 pandas object dtype 是 OOM 高發區？
9. `pin_memory=True` 的物理機制是什麼？
10. Docker 與 VM 的核心差別？什麼是 namespace？

參考答案都在上面 12 張卡內。

---

## 通過標準（給主管核對）

- [ ] 能背出延遲表中至少 8 個量級（1 ns / 100 ns / 10 μs / 500 μs / 5 ms / 150 ms …）
- [ ] 能在白板畫出記憶體階層金字塔（7 層）
- [ ] 能解釋 GIL 的存在原因與 I/O bound 的例外
- [ ] 能從錯誤訊息（`CUDA OOM` / `MemoryError` / `Too many open files` / `Permission denied`）反推系統層根因
- [ ] 能讀懂 `nvidia-smi` 輸出（VRAM 使用、GPU 利用率、process 列表）
- [ ] 能說出 DataLoader 三參數的物理機制
- [ ] 能解釋 Docker 為什麼比 VM 輕

**達標 ≥ 6/7 = M6 內化完成，可進 M7。**

---

## 下一步

- **深化**：讀 Kleppmann《Designing Data-Intensive Applications》Ch.1–3。
- **實作**：用 PyTorch Profiler 剖析一個你手上的訓練 job，定位瓶頸在 compute / memory / I/O 哪一軸。
- **語言擴充**：Rust 或 C++ 寫一次 memory-mapped file 讀取，體會 OS 介面。
- **系統觀察**：在 Linux 用 `perf`、`strace`、`bpftrace` 觀察一個 process 的 syscall 與 cache miss 分佈。

---

_配套文件：`01_on_page_annotation.md`、`02_three_lens_analysis.md`、`03_bcg_narrative.md`、`04_layout_visual_spec.md`。_
