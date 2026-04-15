# F1 · MVK 速學卡（Minimum Viable Knowledge）

> 離開本節後，你的肌肉記憶裡必須長出這三個反射 + 六個 LO 的心智模型。
> 對應 01_outline.md 的 6 個 Learning Objectives。
> 本章的核心判斷：**寫得快的程式是懂硬體的人寫的，不是語法炫的人寫的。**

---

## ① 廚房三角色（對應 LO1）

| 電腦零件 | 廚房角色 | 一句話 |
|---------|---------|--------|
| CPU | 廚師 | 真正做事的人；核越多=廚師越多 |
| RAM | 工作檯 | 料要放檯面才能切；檯面大小決定一次做多少 |
| Storage | 倉庫 | 容量大但遠；廚師看不到，要叫人搬 |

**一句口訣**：料不搬到工作檯，廚師碰不到 → 這就是「讀檔」在做的事。

---

## ② RAM 估算公式（對應 LO2）

```
一個 float64 = 8 Bytes    ← 唯一要背的數字

1 億筆 float64        ≈ 800 MB
1000 萬列 × 50 欄 × 8B ≈ 4 GB
float64 → float32      省 50% RAM
```

**你的筆電安全上限**：
```
安全額度 = RAM × 0.3          （OS + Chrome + Pandas 膨脹預留）
安全筆數 = 安全額度 ÷ (欄數 × 8B)

例：16GB RAM × 50 欄 → 約 1200 萬列
```

超過這個就要上 **S2 chunksize + dtype downcast**。

---

## ③ I/O 100× 定律（對應 LO3）

| 動作 | 時間量級 | 類比 |
|------|---------|------|
| CPU 加一次 | ~1 ns | 廚師切一刀 1 秒 |
| RAM 存取 | ~100 ns | 從檯面拿料 1.5 分鐘 |
| SSD 讀一次 | ~0.1 ms | 倉庫叫貨 5 分鐘 |
| HDD 讀一次 | ~10 ms | 倉庫叫貨 8 小時 |
| 網路一趟 | ~100 ms | 倉庫叫貨 3 天 |

**關鍵反射**：你的 Pandas 卡住，90% 在等讀檔，不是在等計算。
→ 銜接 S1 向量化（把計算也交給 C 層）／ S2 少讀一次就少一次。

---

## ④ OS 三大職責（對應 LO4）

```
記憶體管理  →  決定誰吃多少 RAM / Swap / 誰被 kill (OOM)
檔案系統    →  路徑、權限、I/O  （Windows \ vs Linux /）
行程排程    →  Process / Thread / GIL 怎麼分工
```

**口訣**：Python 是租客，OS 是管委會。你什麼都要透過 OS 要。

---

## ⑤ I/O Bound vs CPU Bound（對應 LO5）

```python
# I/O Bound：CPU 閒著在等
# 爬蟲、讀大檔、API 呼叫
→ async / threading

# CPU Bound：CPU 100%、風扇狂轉
# 矩陣運算、特徵工程、ML 訓練
→ 向量化（S1）/ multiprocessing
```

**判斷法**：打開工作管理員看 CPU 飆滿還是網路/硬碟燈閃。

---

## ⑥ 路徑反射（對應 LO6）

```python
# ✗ 永遠不要這樣
path = 'data\\2024\\sales.csv'   # Linux 爆炸

# ✓ 從今天開始這樣
from pathlib import Path
path = Path('data') / '2024' / 'sales.csv'
```

**理由**：DA/DE 工作幾乎都在 Linux 雲端跑；第一次部署就會被反斜線咬。

---

## 五個必踩地雷（考前必背）

| # | 地雷 | 錯 | 對 |
|---|------|----|----|
| P1 | 整檔 read_csv 大 CSV | `pd.read_csv('5gb.csv')` | `chunksize=100_000` + dtype |
| P2 | 硬拼路徑字串 | `'data\\x.csv'` | `Path('data')/'x.csv'` |
| P3 | I/O 任務開 multiprocessing | `Pool(8).map(fetch)` | `asyncio.gather` |
| P4 | 以為 RAM 沒滿就安全 | 忽略 Swap | 看 memory usage 別只看 free |
| P5 | 以為 Python 語言爛 | 直接放棄 | 運算交給 C 層（S1 向量化） |

---

## 三件帶走的事（全課核心）

1. **RAM 是工作檯** → 檔案大小 ≤ RAM × 0.3，超過就要分批
   ↳ 銜接 **S2 chunksize** / **S4 大資料 EDA**

2. **I/O 很慢**（比計算慢 100×） → 能少讀一次就少讀
   ↳ 銜接 **S1 向量化** / **S2 read_csv 技巧**

3. **路徑用 `/`** → `pathlib.Path` 而非字串
   ↳ 銜接 **S2 pathlib 起手式**

---

## 下一節銜接（F2 Python 核心與資料結構深化）

> RAM 省一半的秘訣，不在換硬體——在你選哪個資料結構。
> list vs tuple vs dict vs generator 的記憶體差距可以到 **幾十倍**。
> 同樣處理一百萬筆資料：
> - `list` 一次吃滿 RAM
> - `generator` 一次只吃一筆
>
> **今天的 RAM 直覺，是明天選對資料結構的地基。**
