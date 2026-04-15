# Ch01 · MVK 速學卡（Minimum Viable Knowledge）

> 離開教室前，你要能用一分鐘回答以下五題。答不出來，整章重看。

---

## 1. 為什麼 NumPy 比純 Python 快？

**一句話：** Python 是黏合語言——上層語法是 Python、下層運算是 C。NumPy 把熱點從 Python 解譯器搬到 C/Fortran 的 BLAS，所以同樣一個 `sum()`，快 10–100 倍。

**關鍵字：** 直譯 vs 編譯、C 後端、向量化

---

## 2. 1 億筆 float64 資料要多少 RAM？

**一句話：** 列數 × 欄數 × 每格 Bytes。1e8 × 1 × 8 B = 8e8 B ≈ **800 MB**；20 欄就 16 GB——這個量級感決定你該用 pandas、chunk、Polars 還是 Parquet。

**關鍵字：** Bit / Byte、float64 = 8 B、OOM 預估

---

## 3. 馮紐曼架構的三區分工？

**一句話：** **CPU 運算 · Memory 暫存 · I/O 進出**。1945 年定型，80 年不變。後續所有效能議題都落在這三個區的其中一個：向量化在 CPU、OOM 在 Memory、async 在 I/O。

**關鍵字：** CPU / RAM / I/O、儲存金字塔（Register → Cache → RAM → SSD → HDD，差 10^7 倍）

---

## 4. OS 的三大職責？

**一句話：** **記憶體管理（OOM / Swap）· 檔案系統（路徑 / 權限）· 行程排程（Process / Thread / GIL）**。Python 不能直接摸硬體，每一次 `open()` 都是向 OS 發出的一張 System Call 申請單。

**關鍵字：** System Call、pathlib（跨平台路徑）、GIL（CPU-bound 要 multiprocess）

---

## 5. I/O Bound vs CPU Bound 怎麼分？

**一句話：** 瓶頸在**等**（網路 / 硬碟）= I/O Bound → 用 async / threading；瓶頸在**算**（矩陣 / 特徵工程）= CPU Bound → 用 multiprocessing / 向量化 / GPU。診斷錯了，開 100 條 thread 也跑不快。

**關鍵字：** GIL、async、multiprocessing、向量化

---

## 本章一句話總結

> **你寫的每一行 Python，都是向 OS 借硬體的一張申請單。**
> 看懂這張申請單的傳遞路徑（Python → Bytecode → OS → Hardware → RAM → CPU），後面六章的效能問題，都只是在這條路徑上標註堵點。
