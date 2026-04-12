# M3 進階 Python 工程

## 系統設計與架構思維：從軟體工程到 AI 時代的架構師之路

**模組編號：** M3 / 8  
**主線：** A — 工程基礎線  
**時數：** 3 小時  
**前置模組：** M1（軟體工程第一原理）、M2（OOP 與程式結構）

---

## 一、模組定位

M3 是工程基礎線的轉折點。

M1 讓你理解「軟體是什麼」；M2 讓你理解「程式如何被組織成系統」；M3 要回答一個更實際的問題：**一個真正的 Python 工程師，在寫完功能邏輯之後，還需要做哪些事？**

答案是：環境管理、例外處理、檔案 I/O、並行設計、測試，以及用型別注解把工程契約寫清楚。

這些能力不是裝飾。它們決定了你的程式碼是「只能在你電腦上跑的腳本」，還是「能被別人維護、在生產環境穩定運行的系統」。

從 Course 1 的進階 Python 模組延伸而來，M3 在三個維度上更深：
- **並行**：從「知道有這回事」到「理解 GIL 機制、能選對工具、看懂 Python 3.13 的方向」
- **測試**：Course 1 沒有觸及，M3 正式引入 TDD 觀念與 pytest 實踐
- **型別注解**：從語法糖升格為工程契約，理解為什麼靜態分析比 runtime 檢查更有價值

**模組金句：**
> "Your script runs. Your code works. Your system is reliable. These are three very different things."

---

## 二、學習目標

完成本模組後，學員能夠：

| # | 目標 | 層次 |
|---|------|------|
| 1 | 解釋 Python 的 import 機制與 `sys.path` 搜尋順序 | 理解 |
| 2 | 設計合理的 package 結構，正確使用 `__init__.py` 與相對 import | 應用 |
| 3 | 使用 `venv` + `pip` + `pyproject.toml` 建立可重現的開發環境 | 應用 |
| 4 | 設計完整的例外處理層次，區分 `logging` 與 `print` 的適用場景 | 分析 |
| 5 | 用 `pathlib` 安全操作檔案路徑，處理 JSON / CSV 的讀寫與編碼問題 | 應用 |
| 6 | 根據任務特性（I/O 密集 vs CPU 密集）選擇 threading / multiprocessing / asyncio | 分析 |
| 7 | 解釋 GIL 的本質與影響，說明 Python 3.13 free-threading 的意義 | 理解 |
| 8 | 用 pytest 撰寫單元測試，理解 TDD 的核心循環 | 應用 |
| 9 | 用型別注解表達函數契約，整合 mypy 進行靜態分析 | 應用 |

---

## 三、概念檢查清單

學員在進入本模組前應確認已掌握：
- [ ] Python 函數定義、`*args`、`**kwargs`
- [ ] class 定義與繼承（M2 範疇）
- [ ] list comprehension、generator expression
- [ ] `with` 語句（context manager 基礎使用）
- [ ] 知道 `os.path` 的存在（不需要熟練）

本模組結束後應能回答：
- [ ] 為什麼 `import` 有時候找不到模組？`sys.path` 裡有什麼？
- [ ] 「在我電腦可以跑」的根本原因是什麼？怎麼修？
- [ ] `except Exception` 和 `except BaseException` 有什麼差？
- [ ] 為什麼 Python 的 threading 對 CPU 密集任務沒用？
- [ ] 什麼是 GIL？它保護的是什麼？
- [ ] 測試要測「行為」還是「實作」？為什麼？

---

## 四、投影片大綱（12 張核心 + 補充）

| 張次 | 標題 | 所屬 Block | 類型 |
|------|------|-----------|------|
| S1 | 模組定位：腳本到系統的最後一哩路 | 導入 | 定位 |
| S2 | Import 機制：Python 怎麼找到你要的東西 | Block 1 | 機制圖 |
| S3 | Package 結構：從檔案到可重用工程單元 | Block 1 | 架構圖 |
| S4 | 環境隔離：「在我電腦可以跑」的解法 | Block 2 | 問題/解法 |
| S5 | 現代依賴管理：從 requirements.txt 到 pyproject.toml | Block 2 | 演化圖 |
| S6 | 例外處理：防禦性設計不是「多包幾層 try」 | Block 3 | 設計圖 |
| S7 | Logging vs Print：工程師的觀測工具 | Block 3 | 對比表 |
| S8 | 檔案 I/O：pathlib + 編碼 + buffer 的完整圖像 | Block 4 | 流程圖 |
| S9 | 並行三選一：GIL 決定你的選項 | Block 5 | 決策樹 |
| S10 | GIL 深潛：它保護什麼、犧牲什麼 | Block 5 | 機制圖 |
| S11 | 測試：測試的是行為，不是實作 | Block 6 | TDD 循環 |
| S12 | 型別注解：讓機器讀懂你的工程意圖 | Block 7 | 契約圖 |

---

## 五、各 Block 詳細內容

---

### Block 1：模組化設計（30 分鐘）

#### 核心概念

Python 的模組系統是其可擴展性的基石。理解它，你才能組織大型專案；不理解它，你會花大量時間在 `ImportError` 上。

**Import 機制的執行順序：**

```
import foo
  │
  ├─ 1. sys.modules 快取查詢（已匯入則直接返回）
  │
  ├─ 2. sys.path 搜尋順序：
  │      ① 當前腳本所在目錄（或空字串 = CWD）
  │      ② PYTHONPATH 環境變數指定的目錄
  │      ③ 標準函式庫目錄
  │      ④ site-packages（第三方套件）
  │
  ├─ 3. 找到後：編譯為 bytecode（.pyc），載入記憶體
  │
  └─ 4. 執行模組頂層代碼，繫結名稱到 sys.modules
```

**為什麼 `import` 有時候找不到你的模組：** 你的 `.py` 不在 `sys.path` 的任何一個目錄裡。常見誤解是「只要在同一個資料夾就能 import」——這在腳本執行時成立，在 pytest / IDE 執行時不一定成立。

#### Package 結構設計

一個符合工程標準的 Python package：

```
my_project/
├── pyproject.toml          # 專案元數據與依賴（現代方式）
├── README.md
├── src/
│   └── my_package/
│       ├── __init__.py     # 定義 public API
│       ├── core.py         # 核心邏輯
│       ├── utils.py        # 工具函數
│       └── models/
│           ├── __init__.py
│           └── user.py
└── tests/
    ├── __init__.py
    ├── test_core.py
    └── test_utils.py
```

**`__init__.py` 的三個角色：**

```python
# 角色 1：標記這個目錄是 package（空檔案即可）

# 角色 2：定義 public API，控制 from package import * 的行為
__all__ = ["UserModel", "process_data"]

# 角色 3：集中轉發，讓使用者不需要知道內部結構
from .models.user import UserModel
from .core import process_data
```

**相對 import vs 絕對 import：**

```python
# 絕對 import（推薦：明確、不受 CWD 影響）
from my_package.models.user import UserModel
from my_package.utils import validate

# 相對 import（適用於 package 內部引用）
from .models.user import UserModel  # 同層
from ..utils import validate        # 上一層
```

相對 import 的限制：只能在 package 內使用，不能在頂層腳本（`__main__`）使用。

---

### Block 2：環境管理（25 分鐘）

#### 問題根源：「Works on My Machine」

這不是個笑話，是工程中最常見的失敗模式。根本原因：

```
開發者 A 的電腦              CI / 生產環境
─────────────              ──────────────
Python 3.11.2              Python 3.10.4
pandas 2.1.0               pandas 1.5.3
numpy 1.26.0（pandas 依賴） numpy 1.23.5
requests 2.31.0            requests 2.28.0
```

依賴版本不同 → 行為不同 → bug 只在某些環境出現。

#### 解法一：虛擬環境（venv）

```bash
# 建立虛擬環境
python -m venv .venv

# 啟動（macOS/Linux）
source .venv/bin/activate

# 啟動（Windows PowerShell）
.\.venv\Scripts\Activate.ps1

# 確認使用的是虛擬環境的 Python
which python  # 應該指向 .venv/bin/python

# 安裝依賴
pip install pandas numpy requests

# 離開虛擬環境
deactivate
```

**原理：** `venv` 建立一個隔離的 Python 環境，有自己的 `site-packages`。啟動後，`python` 和 `pip` 都指向虛擬環境內的版本，不影響系統 Python。

#### 解法二：精確記錄依賴

```bash
# 舊方式：記錄當前環境所有套件（有缺點：把間接依賴也都記錄了）
pip freeze > requirements.txt

# 安裝
pip install -r requirements.txt
```

`requirements.txt` 的問題：無法區分「我真正需要的」和「被間接安裝的」。`requests` 依賴 `urllib3`，但 `urllib3` 不應該出現在你的直接依賴清單裡。

#### 解法三：現代依賴管理 — pyproject.toml

```toml
# pyproject.toml（PEP 517/518/621 標準）
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "pandas>=2.0,<3.0",    # 直接依賴，版本範圍
    "numpy>=1.24",
    "requests>=2.28",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "mypy>=1.0",
    "black>=23.0",
]
```

**依賴衝突的診斷：**

```bash
# 查看依賴樹（需要 pipdeptree）
pip install pipdeptree
pipdeptree

# 常見衝突訊號
# ERROR: pip's dependency resolver does not currently take into account
# all the packages that are installed.

# 解決策略：
# 1. 升級到能同時滿足所有依賴的版本
# 2. 用 pip install --upgrade 逐步更新
# 3. 換用 poetry 或 uv（能正確解析依賴圖）
```

**現代替代工具一覽：**

| 工具 | 特點 | 適用場景 |
|------|------|---------|
| `pip` + `venv` | 標準，無額外安裝 | 學習與簡單專案 |
| `poetry` | 完整依賴解析，lock file | 正式專案 |
| `uv` | Rust 實作，極速，2024 新興主流 | 追求速度的現代專案 |
| `conda` | 包含非 Python 依賴（如 CUDA） | 資料科學 / ML |

---

### Block 3：例外處理（25 分鐘）

#### 例外的本質：控制流，不是錯誤訊息

Python 例外不只是顯示錯誤，它是一種控制流機制。理解這點，你才能設計合理的錯誤處理策略，而不是到處塞 `try/except` 假裝問題不存在。

**完整語法結構：**

```python
try:
    result = risky_operation()
except ValueError as e:
    # 處理特定例外：知道原因，能恢復
    logger.warning(f"Invalid value: {e}")
    result = default_value
except (IOError, OSError) as e:
    # 同時捕捉多種例外
    logger.error(f"I/O error: {e}")
    raise  # 重新拋出：我處理不了，向上傳遞
except Exception as e:
    # 兜底捕捉：要記錄，不要吞掉
    logger.exception(f"Unexpected error: {e}")  # 會記錄完整 traceback
    raise RuntimeError("Operation failed") from e  # 包裝成更有語意的例外
else:
    # 只在 try 沒有發生例外時執行
    # 適合放「成功後的後續邏輯」，語義比在 try 末尾寫更清晰
    logger.info(f"Success: {result}")
finally:
    # 無論如何都執行：釋放資源
    cleanup()
```

**例外繼承階層（Python 標準）：**

```
BaseException
├── SystemExit              ← sys.exit() 觸發，不應被 except Exception 捕捉
├── KeyboardInterrupt       ← Ctrl+C，不應被 except Exception 捕捉
├── GeneratorExit           ← generator 關閉
└── Exception               ← 你應該處理的例外基類
    ├── ValueError          ← 值的類型正確但值不合法
    ├── TypeError           ← 類型錯誤
    ├── KeyError            ← dict 的 key 不存在
    ├── IndexError          ← list 的 index 超界
    ├── AttributeError      ← 屬性不存在
    ├── FileNotFoundError   ← 繼承自 OSError
    ├── RuntimeError        ← 通用執行期錯誤
    └── StopIteration       ← 迭代器耗盡
```

**關鍵：永遠不要用 `except Exception` 吞掉例外而不記錄。** 沉默的失敗比崩潰更難除錯。

#### 自訂例外：定義你的業務邊界

```python
# 自訂例外的正確做法
class AppError(Exception):
    """應用層基礎例外，所有業務例外繼承此類"""
    pass

class ValidationError(AppError):
    """資料驗證失敗"""
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        super().__init__(f"Validation failed on '{field}': {message}")

class NotFoundError(AppError):
    """資源不存在"""
    def __init__(self, resource_type: str, identifier: str):
        super().__init__(f"{resource_type} '{identifier}' not found")

# 使用方式
def get_user(user_id: str) -> dict:
    if not user_id:
        raise ValidationError("user_id", "cannot be empty")
    user = db.find(user_id)
    if user is None:
        raise NotFoundError("User", user_id)
    return user
```

自訂例外的好處：呼叫端可以精確捕捉業務層的錯誤，而不需要用字串比對 `except Exception as e: if "not found" in str(e)` 這種脆弱的寫法。

#### Logging vs Print

```python
import logging

# 設定 logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()  # 同時輸出到 console
    ]
)

logger = logging.getLogger(__name__)  # 用模組名稱作為 logger 名稱

# 五個層級，從低到高
logger.debug("Variable value: %s", variable)    # 除錯細節
logger.info("Processing started for user %s", user_id)  # 一般資訊
logger.warning("Retry attempt %d/3", attempt)   # 警告但不影響執行
logger.error("Failed to connect: %s", error)    # 錯誤，影響功能
logger.critical("Database is down")             # 嚴重，系統無法運作
```

| 維度 | `print` | `logging` |
|------|---------|-----------|
| 用途 | 開發期快速檢查 | 生產環境觀測 |
| 層級 | 無 | DEBUG / INFO / WARNING / ERROR / CRITICAL |
| 輸出目標 | stdout | 可設定：console / file / 網路 / 多個同時 |
| 格式 | 手動 | 可設定時間戳、模組名、行號 |
| 效能 | 直接 IO | 可設定為非同步、批次寫入 |
| 關閉 | 要一一刪除 | 調整 `level` 即可過濾 |

**鐵律：生產環境的 code 裡不應該有 `print`。**

---

### Block 4：檔案 I/O（20 分鐘）

#### pathlib：現代 Python 的路徑處理標準

```python
from pathlib import Path

# 不要再用 os.path 了
# 舊方式：
import os
config_path = os.path.join(os.path.dirname(__file__), "config", "settings.json")

# 新方式：
config_path = Path(__file__).parent / "config" / "settings.json"
```

**pathlib 常用操作：**

```python
p = Path("/data/project/output/results.csv")

# 路徑組件
p.name        # "results.csv"
p.stem        # "results"
p.suffix      # ".csv"
p.parent      # Path("/data/project/output")
p.parts       # ('/', 'data', 'project', 'output', 'results.csv')

# 路徑操作
p.exists()                    # bool
p.is_file() / p.is_dir()      # bool
p.mkdir(parents=True, exist_ok=True)  # 遞迴建立目錄

# 搜尋
list(p.parent.glob("*.csv"))            # 當前目錄
list(p.parent.rglob("*.json"))          # 遞迴搜尋

# 讀寫
text = p.read_text(encoding="utf-8")
p.write_text("content", encoding="utf-8")
```

#### JSON 與 CSV 處理

```python
import json
from pathlib import Path
import csv

# JSON 讀寫
def load_config(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save_result(data: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        # ensure_ascii=False：保留中文等非 ASCII 字元
        # indent=2：人類可讀的格式

# CSV 讀寫（row-by-row，適合大檔案）
def process_csv(input_path: Path, output_path: Path) -> None:
    with (
        open(input_path, encoding="utf-8", newline="") as infile,
        open(output_path, "w", encoding="utf-8", newline="") as outfile
    ):
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            # 逐行處理，不需要把整個檔案載入記憶體
            writer.writerow(transform(row))
```

#### Buffer 概念：為什麼要用 `with`

```
應用程式
   │  write("hello")
   ▼
 Buffer（記憶體緩衝區）─── flush() ──► 作業系統 ──► 磁碟
```

`write()` 不會直接寫到磁碟，而是寫到 buffer。`flush()` 才真正觸發 IO。`with open(...) as f` 在離開 `with` 區塊時會自動呼叫 `f.close()`，而 `close()` 會觸發 `flush()`。

**不用 `with` 的風險：** 程式崩潰時 buffer 裡的資料還沒寫到磁碟，就永遠丟失了。

#### 編碼問題

```python
# 編碼錯誤的常見症狀
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa4 in position 0

# 原因：檔案是 Big5（台灣繁體中文常見）或 GBK（簡體中文常見）編碼
# 用 utf-8 解讀 → 找不到對應字元

# 解法一：明確指定編碼
with open(path, encoding="big5") as f:  # 或 "gbk", "cp950"
    content = f.read()

# 解法二：偵測編碼（需要 chardet 套件）
import chardet
raw = path.read_bytes()
detected = chardet.detect(raw)
encoding = detected["encoding"]  # e.g., "UTF-8", "Big5"
content = raw.decode(encoding)

# 黃金法則：你的程式碼永遠用 UTF-8 輸出
```

---

### Block 5：並行深潛（35 分鐘）

#### 問題場景：為什麼你的程式這麼慢？

```python
import time
import requests

urls = ["https://api.example.com/data/" + str(i) for i in range(100)]

# 版本一：序列執行
start = time.time()
results = []
for url in urls:
    response = requests.get(url)  # 等待網路 → 等待 → 等待...
    results.append(response.json())
print(f"Sequential: {time.time() - start:.1f}s")  # ~50 秒

# 問題：每次 requests.get() 都在等待網路 IO
# CPU 99% 的時間都在空等，啥都沒做
```

這就是「I/O 密集型任務」的特徵：CPU 大量閒置，瓶頸在等待外部資源。

#### 三種並行工具的本質差異

```
threading（執行緒）
─────────────────
同一個 process 內的多個執行緒
共享記憶體空間
有 GIL（Global Interpreter Lock）
適合：I/O 密集型（網路請求、檔案讀寫）

multiprocessing（多程序）
────────────────────────
多個獨立的 process
各自有獨立的記憶體空間
沒有 GIL 的限制
適合：CPU 密集型（資料處理、數值計算）
代價：process 啟動成本高，資料傳遞需要序列化

asyncio（非同步 IO）
───────────────────
單執行緒，事件驅動
透過協程（coroutine）交出 CPU 控制權
適合：大量 I/O 密集型任務（尤其是網路）
特點：協作式多工，不是搶佔式
```

#### 實際 Benchmark

```python
import time
import threading
import multiprocessing
import asyncio
import concurrent.futures

# 任務 A：I/O 密集（模擬網路請求）
def io_task(n: int) -> float:
    time.sleep(0.1)  # 模擬 100ms 網路延遲
    return n * 2

# 任務 B：CPU 密集（計算 Fibonacci）
def cpu_task(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

N = 50  # 任務數量

# --- I/O 密集型比較 ---
# 序列
start = time.time()
[io_task(i) for i in range(N)]
print(f"Sequential:          {time.time()-start:.2f}s")  # ~5.0s

# threading
start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    list(executor.map(io_task, range(N)))
print(f"ThreadPoolExecutor:  {time.time()-start:.2f}s")  # ~0.6s

# asyncio
async def async_io_task(n: int) -> float:
    await asyncio.sleep(0.1)
    return n * 2

start = time.time()
asyncio.run(asyncio.gather(*[async_io_task(i) for i in range(N)]))
print(f"asyncio:             {time.time()-start:.2f}s")  # ~0.1s

# --- CPU 密集型比較 ---
FIBO_N = 50_000  # 計算量夠大

# threading（因為 GIL，幾乎沒有加速）
start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    list(executor.map(lambda _: cpu_task(FIBO_N), range(8)))
print(f"Threading (CPU):     {time.time()-start:.2f}s")  # ~2.0s（沒加速）

# multiprocessing（真正並行）
start = time.time()
with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    list(executor.map(lambda _: cpu_task(FIBO_N), range(8)))
print(f"Multiprocessing:     {time.time()-start:.2f}s")  # ~0.6s（加速）
```

**結論表格：**

| 任務類型 | threading | multiprocessing | asyncio |
|---------|-----------|-----------------|---------|
| I/O 密集（網路、磁碟）| 好 | 可以但殺雞用牛刀 | 最佳 |
| CPU 密集（計算、處理）| 幾乎無用（GIL） | 最佳 | 無效 |
| 混合型 | 視比例 | 視比例 | 視比例 |
| 記憶體用量 | 低 | 高（多份資料） | 最低 |
| 程式碼複雜度 | 中 | 中 | 高（需要 async/await） |

#### GIL 深潛：它到底是什麼？

**GIL（Global Interpreter Lock）的定義：** CPython（Python 的標準實作）中，一個互斥鎖（mutex），確保同一時刻只有一個執行緒在執行 Python bytecode。

**為什麼存在？** CPython 的記憶體管理使用「引用計數（reference counting）」——每個物件記錄有多少變數指向它，計數為 0 時自動釋放記憶體。引用計數是 non-atomic 操作，多執行緒同時修改同一個計數會產生 race condition，導致 double-free（同一塊記憶體被釋放兩次，造成崩潰）。GIL 是最簡單的解法：加一把大鎖，任何時候只讓一個執行緒跑。

```
時間軸：
Thread 1: ─── Python bytecode ─── GIL released ─── waiting ───
Thread 2: ─── waiting ────────── GIL acquired ─── Python bytecode ──
Thread 3: ─── waiting ────────────────────── waiting ───────────────

※ 真正並行的只有一個執行緒在執行 Python bytecode
※ I/O 操作（網路、磁碟）會釋放 GIL，這就是為什麼 threading 對 I/O 有用
```

**為什麼這是個大問題？** 2006 年以後，多核 CPU 已經普及。Java、Go、Rust 都能真正利用多核進行 CPU 並行計算。Python 因為 GIL，在 CPU 密集型任務上，多執行緒等於沒有加速。

**緩解方案（現在）：**
- CPU 密集 → 用 `multiprocessing`（繞過 GIL，每個 process 有自己的 GIL）
- 科學計算 → 用 NumPy / pandas（底層是 C，在 C 層釋放 GIL，實現真正並行）
- 高效能需求 → 考慮 PyPy（不同的 Python 實作，GIL 行為不同）

#### Python 3.13 + PEP 703：Free-Threading 方向

PEP 703（"Making the Global Interpreter Lock Optional"）在 Python 3.13 實驗性實作。這是 Python 社群討論了近 20 年的里程碑。

```
Python 3.13 之後：
─────────────────
實驗性 free-threading build（--disable-gil）
可以真正利用多核 CPU 執行 Python 程式碼
代價：需要所有 C 擴充套件重新認證為 thread-safe

Python 3.14+：
─────────────
GIL 逐步成為可選項
生態系套件逐步適配

實際影響（現階段）：
─────────────────
大多數開發者目前不需要使用 free-threading build
GIL 對 I/O 密集型應用影響很小（asyncio 已經夠用）
關注它的理由：未來 3-5 年，Python 的多核 CPU 利用率會大幅改善
```

**對你現在的工程決策的意義：** 不要因為 PEP 703 而現在就改寫你的 threading 程式碼。但要知道：Python 的並行限制不是永久的，方向已定。

---

### Block 6：測試基礎（25 分鐘）

#### 為什麼測試不是「寫完才補的文件」

測試是工程保證，不是形式主義。沒有測試的程式碼，每次修改都是在黑暗中摸索。有了測試：
- 重構時知道有沒有破壞東西
- 新成員能理解「這個函數應該做什麼」
- Bug 修好後能防止同樣的 bug 再次出現

**什麼是值得測試的行為：**

```python
# 不好的測試：測試實作細節
def test_internal_counter():
    obj = MyProcessor()
    obj.process(data)
    assert obj._internal_counter == 3  # 為什麼要管內部狀態？

# 好的測試：測試可觀察的行為
def test_process_returns_correct_result():
    processor = MyProcessor()
    result = processor.process([1, 2, 3])
    assert result == [2, 4, 6]

def test_process_raises_on_empty_input():
    processor = MyProcessor()
    with pytest.raises(ValueError, match="Input cannot be empty"):
        processor.process([])
```

#### pytest 基礎

```python
# tests/test_calculator.py
import pytest
from my_package.calculator import Calculator, DivisionByZeroError

class TestCalculator:
    def setup_method(self):
        """每個測試方法執行前都會呼叫"""
        self.calc = Calculator()

    def test_add_two_positive_numbers(self):
        assert self.calc.add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert self.calc.add(-1, -2) == -3

    def test_divide_raises_on_zero(self):
        with pytest.raises(DivisionByZeroError):
            self.calc.divide(10, 0)

    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),
        (9, 3, 3),
        (-6, 2, -3),
        (0, 5, 0),
    ])
    def test_divide_parametrized(self, a, b, expected):
        assert self.calc.divide(a, b) == expected

    def test_result_is_float(self):
        result = self.calc.divide(7, 2)
        assert isinstance(result, float)
        assert result == pytest.approx(3.5)
```

```bash
# 執行測試
pytest tests/                     # 執行所有測試
pytest tests/test_calculator.py   # 執行特定檔案
pytest -v                         # 詳細輸出
pytest -k "divide"                # 只執行名稱含 "divide" 的測試
pytest --tb=short                 # 短格式的錯誤追蹤
pytest --cov=my_package           # 測試覆蓋率（需要 pytest-cov）
```

#### TDD（測試驅動開發）的核心循環

```
Red → Green → Refactor
────────────────────────

1. Red：先寫測試（測試應該失敗，因為功能還沒實作）
   └─ 這一步強迫你先想清楚「這個函數應該做什麼」

2. Green：用最簡單的方式讓測試通過
   └─ 不要過度設計，先讓它跑

3. Refactor：在測試保護下重構，改善代碼品質
   └─ 測試通過就是你的安全網

重複以上循環
```

**TDD 的實際效益不是「程式碼有測試」，而是：**
- 設計驅動：先想介面（function signature），再想實作
- 快速回饋：每幾分鐘就知道有沒有破壞東西
- 文件效果：測試就是最好的使用範例

#### 測試類型簡介

| 類型 | 測試對象 | 速度 | 隔離度 |
|------|---------|------|-------|
| 單元測試（Unit Test）| 單一函數 / class | 最快 | 最高 |
| 整合測試（Integration Test）| 多個模組協作 | 中 | 中 |
| 端對端測試（E2E Test）| 完整使用者流程 | 慢 | 最低 |

**原則：** 測試金字塔——大量單元測試，少量整合測試，極少量 E2E 測試。不要反過來。

---

### Block 7：型別注解作為工程契約（20 分鐘）

#### 從語法糖到工程工具

Python 的型別注解（Type Hints，PEP 484+）在語言層面只是「元數據」——Python 執行期不做型別檢查。但配合靜態分析工具（mypy / pyright），它變成了：

1. **機器可讀的文件**：不需要看 docstring，IDE 直接告訴你這個函數接受什麼、回傳什麼
2. **早期錯誤偵測**：型別錯誤在執行前就被發現
3. **重構安全網**：改了某個函數的 signature，mypy 立刻告訴你哪些呼叫點需要更新

#### 基礎語法

```python
from typing import Optional, Union, Any
from collections.abc import Sequence, Callable, Generator
from pathlib import Path

# 基本型別注解
def greet(name: str) -> str:
    return f"Hello, {name}"

# Optional：可能是 None
def find_user(user_id: int) -> Optional[dict]:
    # 等同於 Union[dict, None]
    return db.get(user_id)  # 可能找不到，回傳 None

# Union：接受多種型別（Python 3.10+ 可用 str | int）
def process(value: str | int | float) -> str:
    return str(value)

# Sequence：泛型容器
def calculate_mean(numbers: Sequence[float]) -> float:
    return sum(numbers) / len(numbers)

# Callable：函數作為參數
def apply_transform(
    data: list[int],
    transform: Callable[[int], int]
) -> list[int]:
    return [transform(x) for x in data]

# 複雜回傳型別
def load_config(path: Path) -> dict[str, Any]:
    ...

# Generator
def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

#### TypedDict 與 dataclass：讓結構清晰

```python
from typing import TypedDict
from dataclasses import dataclass, field

# TypedDict：當你必須用 dict 時
class UserConfig(TypedDict):
    name: str
    email: str
    age: int
    is_admin: bool

def create_user(config: UserConfig) -> None:
    # IDE 會知道 config["name"] 是 str
    # 型別錯誤在寫代碼時就被標記出來
    ...

# dataclass：更好的選擇，有方法、有預設值、可以繼承
@dataclass
class ProcessingConfig:
    input_path: Path
    output_path: Path
    batch_size: int = 100
    max_retries: int = 3
    tags: list[str] = field(default_factory=list)

    def validate(self) -> None:
        if not self.input_path.exists():
            raise ValidationError("input_path", "path does not exist")
        if self.batch_size <= 0:
            raise ValidationError("batch_size", "must be positive")
```

#### mypy：讓靜態分析變成流程的一部分

```bash
# 安裝
pip install mypy

# 執行
mypy src/my_package/

# 設定（mypy.ini 或 pyproject.toml）
[mypy]
python_version = 3.11
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True  # 要求所有函數都要有型別注解
```

```python
# mypy 能抓到的錯誤範例
def add(a: int, b: int) -> int:
    return a + b

result = add("hello", "world")
# mypy error: Argument 1 to "add" has incompatible type "str"; expected "int"

user = find_user(123)
print(user["name"])  # user 可能是 None！
# mypy error: Item "None" of "Optional[dict]" has no attribute "__getitem__"

# 正確處理：
user = find_user(123)
if user is not None:
    print(user["name"])  # mypy 現在知道 user 一定是 dict
```

**型別注解的工程哲學：** 型別注解不是給執行期看的，是給「未來的你」和「你的同事」看的。它把你對資料的假設（"這個參數應該是個非空的字串列表"）從腦子裡、docstring 裡，移到機器可以驗證的地方。這是一種契約，而不是裝飾。

---

## 六、練習題

### 練習一：從腳本到工程模組（90 分鐘）

**情境：** 你有一段爬取天氣資料的腳本（提供），它能跑，但不是一個工程專案：沒有模組結構、沒有環境管理、沒有錯誤處理、沒有型別注解、也沒有測試。

**任務：**

**Part A — 環境建立（15 分鐘）**
1. 建立 `venv` 虛擬環境
2. 建立 `pyproject.toml`，聲明依賴（`requests>=2.28`, `pytest>=7.0`）
3. 安裝依賴，確認環境可重現

**Part B — 模組化重構（30 分鐘）**
把以下腳本重構成 package 結構：

```
weather_fetcher/
├── pyproject.toml
├── src/
│   └── weather_fetcher/
│       ├── __init__.py       # 公開 fetch_weather, WeatherData
│       ├── fetcher.py        # 負責 HTTP 請求
│       ├── parser.py         # 負責解析回應
│       └── models.py         # WeatherData dataclass
└── tests/
    ├── test_parser.py
    └── test_fetcher.py
```

要求：
- `__init__.py` 要清楚定義 public API
- 使用相對 import 在 package 內部引用

**Part C — 錯誤處理 + Logging（20 分鐘）**
1. 定義 `WeatherFetcherError`, `NetworkError`, `ParseError` 自訂例外
2. 在 `fetcher.py` 中用 `logging` 取代所有 `print`
3. 確保所有可能失敗的操作都有適當的 try/except

**Part D — 型別注解（15 分鐘）**
1. 為所有函數加上完整的型別注解
2. 安裝並執行 `mypy`，確保零型別錯誤

**Part E — 測試（10 分鐘）**
1. 為 `parser.py` 的解析邏輯撰寫至少 3 個測試
2. 覆蓋：正常案例、邊界案例（空資料）、錯誤案例（格式錯誤）

**驗收標準：**
- `pytest` 全部通過
- `mypy` 零錯誤
- 任何同學從 git clone 你的 repo 後，只需要 `python -m venv .venv && pip install -e .` 就能跑起來

---

### 練習二：並行效能診斷（30 分鐘）

**情境：** 你的資料處理管線有三個步驟，需要找出瓶頸並選擇正確的並行策略。

**Part A — 效能量測（10 分鐘）**

```python
import time
import random

# 三種不同特性的任務
def download_task(url_id: int) -> str:
    """模擬網路下載：大量 I/O 等待"""
    time.sleep(random.uniform(0.05, 0.15))
    return f"data_{url_id}"

def transform_task(data: str) -> str:
    """模擬 CPU 密集計算：數值處理"""
    result = 0
    for i in range(100_000):
        result += i * len(data)
    return str(result)

def write_task(data: str, file_id: int) -> None:
    """模擬磁碟寫入：I/O 等待"""
    time.sleep(0.02)
```

對每種任務分別測試：序列、threading、multiprocessing 的執行時間（每種任務各 20 個）。

**Part B — 結果分析（10 分鐘）**
填寫下表，並解釋觀察到的結果：

| 任務類型 | 序列 | threading | multiprocessing |
|---------|------|-----------|-----------------|
| download_task | ? | ? | ? |
| transform_task | ? | ? | ? |
| write_task | ? | ? | ? |

**Part C — Pipeline 設計（10 分鐘）**
設計一個完整的 pipeline，對每個步驟選擇最適合的並行策略：

```python
def pipeline(item_ids: list[int]) -> None:
    # Step 1: download_task — 用什麼並行？
    # Step 2: transform_task — 用什麼並行？
    # Step 3: write_task — 用什麼並行？
    pass
```

實作並驗證：你的 pipeline 比全序列快多少？

**討論問題：** 如果 `transform_task` 改成用 NumPy 做向量計算，threading 的結果會不會不同？為什麼？

---

## 七、講師筆記

### 時間分配建議（3 小時）

| 段落 | 時間 | 備註 |
|------|------|------|
| 開場定位（S1）| 5 分鐘 | 強調「腳本和系統的差距」 |
| Block 1 Import + Package（S2-S3）| 30 分鐘 | 現場 Demo：故意製造 ImportError，再修復 |
| Block 2 環境管理（S4-S5）| 25 分鐘 | 現場 Demo：建立 venv，比較 freeze 和 pyproject.toml |
| Block 3 例外處理 + Logging（S6-S7）| 25 分鐘 | 強調「沉默的失敗比崩潰更難除錯」 |
| Block 4 File I/O（S8）| 20 分鐘 | 現場製造 UnicodeDecodeError，再修復 |
| 中間休息 | 10 分鐘 | |
| Block 5 並行（S9-S10）| 35 分鐘 | 現場執行 benchmark，讓學員看數字 |
| Block 6 測試（S11）| 25 分鐘 | 現場示範 TDD 循環，從 failing test 到 passing |
| Block 7 型別注解（S12）| 20 分鐘 | 現場示範 mypy 抓到的錯誤 |
| 練習說明 + Q&A | 5 分鐘 | |
| **合計** | **180 分鐘** | |

### 常見誤解與糾正點

**誤解 1：「exception 就是用 try/except 包起來」**
糾正：exception 是控制流機制。問題不是「要不要包」，而是「在哪一層處理、怎麼處理」。底層函數拋例外，上層函數決定怎麼恢復或向上傳遞。永遠不要「捕捉例外只為了讓程式不崩潰」而不記錄也不恢復。

**誤解 2：「用 threading 就能加速所有程式」**
糾正：GIL 讓 Python threading 對 CPU 密集型任務幾乎無效。現場 benchmark 是最有說服力的工具。讓學員自己跑，看數字。

**誤解 3：「型別注解讓 Python 變成靜態語言」**
糾正：型別注解只是元數據，Python 執行期照樣不做型別檢查。它的價值在靜態分析工具（mypy）和 IDE 的自動補全。你加了型別注解，呼叫時傳錯型別，Python 照樣跑，只有 mypy 會報錯。

**誤解 4：「測試要在功能完成後才寫」**
糾正：這是最常見的借口，結果就是「永遠沒時間寫測試」。TDD 不是完美主義，是一種讓設計更清晰的工作流。哪怕只是「先想好函數的 signature 和邊界條件」，再開始寫實作，品質就會不同。

### 課堂互動建議

**Block 5（並行）可以做個「猜數字」環節：**
在跑 benchmark 之前，讓學員先猜：「threading 版本比序列快多少？」、「multiprocessing 版本比 threading 快多少？」大多數人在看到 CPU 密集型任務 threading 幾乎沒有加速時，都會感到驚訝。這個驚訝就是學習的起點。

**Block 6（測試）可以做「壞掉的程式碼」示範：**
展示一個沒有測試的函數，然後「重構」它（故意引入一個 bug），問學員：「你怎麼知道我沒有改壞？」答案是：你不知道。然後展示有測試的版本，重構後馬上執行，測試立刻抓到 bug。

### 與後續模組的連接

- **M4（計算機組織）**：Block 5 的 GIL 和 multiprocessing，在 M4 會從 CPU / process / thread 的硬體視角重新解釋。M3 是工程面，M4 是底層面。
- **M5（作業系統）**：venv 的隔離概念、process 之間的資料傳遞，都會在 M5 的「process / thread / 記憶體管理」章節獲得更深的解釋。
- **M8（整合）**：testing、logging、型別注解這些工程習慣，在 M8 的「從程式到生產系統」案例研究中會被整體呈現。

### 延伸資源

- CPython 原始碼中的 GIL：`Modules/ceval.c`（真正想理解底層的學員可以看）
- PEP 703 原文：[https://peps.python.org/pep-0703/](https://peps.python.org/pep-0703/)
- pytest 官方文件：[https://docs.pytest.org/](https://docs.pytest.org/)
- mypy 官方文件：[https://mypy.readthedocs.io/](https://mypy.readthedocs.io/)
- "Hypermodern Python" 系列文章（Claudio Jolowicz）：現代 Python 工程的最佳實踐參考

---

## 八、模組總結

M3 的核心訊息可以用三層來記：

**第一層（工具層）：** 你現在有一套工具——venv 管環境、pathlib 管路徑、logging 管觀測、pytest 管品質保證、mypy 管契約。這些工具各司其職。

**第二層（原則層）：** 背後有三條原則——
1. 可重現性（Reproducibility）：你的程式必須能在別人的機器上以相同的行為執行
2. 可觀測性（Observability）：系統出問題時，你要能知道哪裡出問題、為什麼
3. 可驗證性（Verifiability）：你的修改必須能被驗證是否破壞了現有行為

**第三層（工程師視角）：** 這些能力合起來，讓你從「會寫 Python 的人」變成「能交付可維護系統的工程師」。程式能跑是起點，不是終點。

下一站，M4（計算機組織）：你寫的這些 Python 程式，在 CPU 和記憶體層面究竟發生了什麼？

---

*M3 完 — 工程基礎線繼續進行*
