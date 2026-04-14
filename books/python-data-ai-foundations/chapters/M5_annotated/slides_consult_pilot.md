---
title: M5 進階 Python — 從腳本到可維護系統 · 顧問嚴謹 Pilot (v1.1 Editorial)
module: M5
version: 1.1
style: Editorial-strict / Structure-led / Zero-illustration
seed_paradigm: shared/design_system/顧問型投影片_黃金守則與泛式.md
paradigm_version: v1.1
primary_color: "#1B5E3F"
accent_discipline: 主色深綠 #1B5E3F + 炭灰 #333333 + 淺灰 #D3D3D3 + 白；禁紅黃橙粉淺藍
forbidden_prototypes: [SCENE, STORYBOARD, ZOOM, DIAGRAM-STORY]
forbidden_colors: ["red", "yellow", "orange", "pink", "light blue"]
priority_rules: [G4, G3, G7]
slide_prototypes_used:
  - GEOMETRIC-DIAGRAM
  - ASK
  - TABLE
  - SILENT
  - BEFORE/AFTER
  - MATRIX
  - CHART
total_slides: 15
audience: 企業內訓 / 付費技術課程 / 成人學員（非兒童繪本受眾）
target_time_minutes: 25
last_updated: 2026-04-14
replaces: 無（M5 首版顧問嚴謹 pilot）
governing_thought: "能跑的 Python，和能活下去的 Python，是兩回事。"
note: >
  M5 本模組以 G4 MECE 為首要守則：工具比較（venv / conda / poetry / uv）、
  依賴聲明（requirements.txt / pyproject.toml / lockfile）、三種並行機制
  （asyncio / threading / multiprocessing）皆以互斥窮盡的 TABLE / MATRIX
  呈現。全 deck 主色深綠單色紀律（G3），三張 SILENT 呼吸頁（G7）分散於
  第 5 / 10 / 15 張，形成節奏停頓。類比（例：腳本 = 筆記、系統 = 廠房）
  一律留在講者口白，畫面只呈現資料、結構、表格與純文字框。
---

# M5 · 進階 Python — 從腳本到可維護系統（Consult Pilot v1.1 Editorial-strict）

> 腳本和系統之間有一條分界線：腳本跑一次就算完成，系統要能被重現、被協作、被接手。
> M5 的五個 Block 不是五個獨立技巧，是讓一個 Python 專案活下去的最低基礎設施。

---

### Slide 1 · GEOMETRIC-DIAGRAM · 腳本能跑一次，系統要跑一千次——中間隔著五道基礎設施

**🖼️ 畫面**
> 畫面分左右兩塊，中央一條純灰 #D3D3D3 垂直細分隔線。
> 左塊標題「腳本 Script」14pt 炭灰：一個 320×200 單一方塊，深綠 #1B5E3F 細邊（1pt），內含十幾條交錯灰線（#D3D3D3，1pt）代表函式互相呼叫、路徑寫死、print 散落；方塊下方小字「單檔 / 硬編碼路徑 / print 除錯 / 全域環境」。
> 右塊標題「系統 System」14pt 炭灰：五個等寬深綠 #1B5E3F 實心方塊縱向堆疊，上方小標籤依序「① 模組化」「② 環境」「③ 例外 / 日誌」「④ I/O」「⑤ 並行」；五個方塊左側一條深綠細軸線串起（1.5pt）。
> 左右兩塊之間畫一條深綠實心箭頭由左指向右，箭頭下方 12pt 炭灰註記「跨越這條線 = 從『會寫 Python』到『能做 Python 工程』」。
> 整頁上下留白 18%，純幾何，無光影、無人物、無物件類比。
> 右下 8pt 灰 `Source: M5 module thesis`。

**📣 畫面上的字**
> 標題如上。
> 左塊小字：「單檔 / 硬編碼路徑 / print 除錯 / 全域環境」
> 右塊五層標籤：「① 模組化 / ② 環境 / ③ 例外 / 日誌 / ④ I/O / ⑤ 並行」
> 箭頭註記：「跨越這條線 = 從『會寫 Python』到『能做 Python 工程』」

**🎙️ 講者這時說**
> 「各位寫的腳本很多都能跑。問題是能不能跑第二次、第一百次、在別人電腦、三個月後的你自己手上，還能跑。這五層基礎設施，不是進階技巧，是專業門檻。」

**🎨 視覺紀律 check**
> G1 ✓（完整主張句標題） / G3 主色 #1B5E3F 單色 ✓ / G4 五層 MECE ✓ / G5 純幾何無裝飾 ✓ / G7 上下 18% 留白 ✓ / G8 無禁色 ✓ / 原型 GEOMETRIC-DIAGRAM 非退役 ✓

**💡 敘事弧角色**
> Hook

---

### Slide 2 · ASK · 同一份程式、同一份資料，跑出不同結果——誰的錯？

**🖼️ 畫面**
> 純白底，70% 留白。
> 畫面上方 1/3 處一句深綠 #1B5E3F 28pt 粗體提問句置中。
> 提問句下方 80px 留白，畫面中下方一條極簡對比列，由三個等寬小卡並列（每卡占畫面寬 22%，卡間距 24px，純白底 + 深綠 1pt 細邊）：
>   卡 1 標籤 12pt 炭灰「你的電腦」：深綠 36pt 粗體「pandas 2.2」 / 12pt 灰「Python 3.11」
>   卡 2 標籤「同事電腦」：深綠 36pt 粗體「pandas 1.5」 / 12pt 灰「Python 3.9」
>   卡 3 標籤「CI Server」：深綠 36pt 粗體「pandas 2.0」 / 12pt 灰「Python 3.10」
> 三卡下方一行 12pt 炭灰：「同程式 · 同資料 · 三種結果」
> 右下 8pt 灰 `Source: 2024 pandas release notes — breaking changes`。
> 無人物、無裝飾、無情境插畫。

**📣 畫面上的字**
> 標題：「同一份程式、同一份資料，跑出不同結果——誰的錯？」
> 三卡內容、底部註記如上。

**🎙️ 講者這時說**
> 「答案是：誰都沒錯，是環境沒被聲明。可重現性（reproducibility）不是玄學，是工程衛生。這張問題請各位帶進下一頁。」

**🎨 視覺紀律 check**
> G1 ✓（Socratic 完整問句） / G3 主色 ✓ / G5 無裝飾 ✓ / G7 70% 留白 ✓ / G8 無禁色 ✓ / 原型 ASK 非退役 ✓

**💡 敘事弧角色**
> Tension

---

### Slide 3 · GEOMETRIC-DIAGRAM · 一個套件的「版本」，背後是一棵相依 DAG

**🖼️ 畫面**
> 純幾何有向無環圖（DAG），純方塊 + 深綠直角折線箭頭（1pt），無曲線、無光影、無人物。
> 頂端一個深綠 #1B5E3F 實底白字方塊：`your_project`。
> 第 2 層由頂點分出兩條箭頭向下指向兩個白底深綠邊方塊：`pandas==2.2` · `scikit-learn==1.4`。
> 第 3 層：
>   - `pandas==2.2` 再向下分出三條箭頭：`numpy>=1.26` · `python-dateutil>=2.8` · `pytz>=2023`
>   - `scikit-learn==1.4` 向下分出三條箭頭：`numpy>=1.19` · `scipy>=1.6` · `joblib>=1.2`
> 第 4 層：`numpy>=1.26` 與 `numpy>=1.19` 兩箭頭匯合進入同一個方塊 `numpy` — 此處以深綠粗邊（2pt）強調該方塊，並於右側 12pt 炭灰註「共用相依 → 必須同時滿足兩個版本約束」。
> 最底部 15% 留白。
> 右下 8pt 灰 `Source: PyPI dependency graph, 2024 snapshot`。

**📣 畫面上的字**
> 標題、DAG 各節點名、共用相依註記如上。

**🎙️ 講者這時說**
> 「你裝的不是一個套件，是一棵樹。而且這棵樹的葉子會互相打架——numpy 同時被兩個父節點拉向不同版本，這就是依賴衝突的本質。看到這張圖，你就知道為什麼需要 lockfile。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 層級 MECE ✓ / G5 純幾何 ✓ / G7 底部留白 15% ✓ / G8 無禁色 ✓ / 原型 GEOMETRIC-DIAGRAM 非退役（與 Slide 1 間隔 1 張，不連續） ✓

**💡 敘事弧角色**
> Tension

---

### Slide 4 · TABLE · venv / conda / poetry / uv 四方對比；2026 預設建議是 uv

**🖼️ 畫面**
> 一張 Editorial 風 TABLE：僅上下框線（1.5pt 深綠 #1B5E3F），無竖線，行交替 `#FFFFFF / #F0F0F0`，表頭深綠實底白字 14pt。
> 五欄五列（含表頭）：
>
> | 工具 | 定位 | 速度 | 依賴解析 | 2026 適用情境 |
> |---|---|---|---|---|
> | `venv` + `pip` | 標準庫 / 最低門檻 | 中 | 無 lockfile | 簡單腳本 / 教學入門 |
> | `conda` | 環境 + 非 Python 套件 | 慢 | 有 solver | 科學計算 / C/CUDA 相依 |
> | `poetry` | 專案管理 + lockfile | 中 | `poetry.lock` | 純 Python 套件開發 |
> | `uv` | Rust 實作 / 全功能 | **10–100× 快** | `uv.lock` | **2026 預設建議** |
>
> 表格下方 18% 垂直留白。
> 底部置中一條深綠 #1B5E3F 倒掛框（占畫面寬 62%）白字 14pt 粗體一句：
>   「選一個，就全 deck 不動——工具輪替的成本比想像高。」
> 右下 8pt 灰 `Source: Astral uv 0.5 benchmarks / Python Packaging Authority, 2025`。
> 第 4 列（uv）以深綠粗體字強調，表示建議預設。

**📣 畫面上的字**
> 標題、表頭、四列、倒掛框主張句如上。

**🎙️ 講者這時說**
> 「四個工具互斥且窮盡主流選項。venv 是底線，conda 在 GPU/科學棧仍有位置，poetry 是前一代標準，uv 是 2026 的新預設——同樣一個 solve + install，uv 比 pip 快兩個數量級。但請記住：選工具的成本比用工具高，全公司一條線最重要。」

**🎨 視覺紀律 check**
> G1 ✓（完整主張句含建議） / G3 主色 ✓ / G4 四工具 MECE 互斥窮盡 ✓ / G5 表格極簡 ✓ / G8 無禁色 ✓ / G11 倒掛框 ✓ / G12 表格極簡（無竖線 / 行交替） ✓ / 原型 TABLE 非退役 ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 5 · SILENT · 可重現，不是美德，是協作的最低義務

**🖼️ 畫面**
> 整頁深綠 #1B5E3F 實底。
> 畫面中央偏上一行白字 28pt 粗體，為主標。
> 主標下方 80px 留白，一行白字 14pt 輕量：「— 若同事拿到你的程式跑不出來，錯的是你沒聲明，不是他沒本事」。
> 畫面右下 8pt 灰白 `Source: M5 module thesis — Block 2`。
> 其餘 100% 留白。無任何圖形、無引號符號、無裝飾。

**📣 畫面上的字**
> 「可重現，不是美德，是協作的最低義務。」
> 副句如上。

**🎙️ 講者這時說**
> 「停三秒。這一句請你抄到筆記上。協作的起點，不是你寫得多漂亮，是別人能不能跑起來。下半場開始。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 深綠底白字 ✓ / G5 無圖表 ✓ / G7 深色全底即留白（呼吸頁） ✓ / G8 無禁色 ✓ / 原型 SILENT 非退役 ✓

**💡 敘事弧角色**
> Breather（G7 呼吸頁第 1/3）

---

### Slide 6 · BEFORE/AFTER · `raise ... from ...`：例外鏈保留第一現場，不讓根因消失

**🖼️ 畫面**
> 上下兩個程式碼截圖區塊（PHOTO 作為代碼截圖子類；非場景），寬度各占畫面 78% 置中，區塊間距 32px。
>
> 上方標籤「BEFORE（吞掉原始例外）」炭灰 14pt，程式碼區塊白底深綠細邊（1pt）、等寬字型 13pt：
> ```python
> def load_config(path):
>     try:
>         return json.loads(path.read_text())
>     except Exception:
>         raise ConfigError("無法載入設定")  # 原始例外被吞掉
> ```
> 右側標註 14pt 深綠粗體「stack trace 斷鏈」。
>
> 下方標籤「AFTER（`raise ... from e` 保留鏈結）」深綠 14pt 粗體，程式碼區塊：
> ```python
> def load_config(path):
>     try:
>         return json.loads(path.read_text())
>     except (OSError, json.JSONDecodeError) as e:
>         raise ConfigError(f"無法載入設定：{path}") from e
> ```
> 右側標註 14pt 深綠粗體「根因可追 · 第一現場保留」。
>
> 兩區塊之間一條深綠 2pt 向下箭頭，箭頭右側 12pt 炭灰小字「`from e` 把原始例外接在 `__cause__`，traceback 會印出兩段」。
> 右下 8pt 灰 `Source: PEP 3134 — Exception Chaining`。
> 不畫任何圖示、不加陰影。

**📣 畫面上的字**
> 標題、Before/After 標籤、右側標註、箭頭註記如上。

**🎙️ 講者這時說**
> 「很多人把例外當地雷——炸了就換一顆更溫和的扔出去。真正的工程做法是把第一現場保存下來。`raise ... from e` 這一個字，決定了半年後凌晨三點你能不能抓到 bug。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G5 代碼純文本無裝飾 ✓ / G7 上下等高 ✓ / G8 無禁色 ✓ / 原型 BEFORE/AFTER 非退役 ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 7 · TABLE · 依賴聲明三層級：requirements.txt / pyproject.toml / lockfile 各管什麼

**🖼️ 畫面**
> 一張 Editorial 風 TABLE：僅上下框線（1.5pt 深綠），無竖線，行交替 `#FFFFFF / #F0F0F0`，表頭深綠實底白字 14pt。
> 四欄四列（含表頭）：
>
> | 檔案 | 管什麼 | 不管什麼 | 進 git？ |
> |---|---|---|---|
> | `requirements.txt` | 頂層套件清單（常含版本區間） | 相依樹完整解析 / 傳遞性鎖定 | ✓ |
> | `pyproject.toml` | 專案 metadata + 套件宣告 + build 設定 | 精確版本鎖定（是宣告，不是鎖） | ✓ |
> | `*.lock`（`uv.lock` / `poetry.lock`） | 全樹每個套件的精確版本與 hash | 人類手寫（由 solver 產出） | ✓（關鍵！） |
>
> 表格下方 15% 垂直留白。
> 底部深綠 #1B5E3F 倒掛框白字 14pt 粗體（寬占畫面 70%）：
>   「宣告（pyproject）≠ 鎖定（lockfile）。兩者都進 git，缺一不可重現。」
> 右下 8pt 灰 `Source: PEP 517 / 518 / 621 / Python Packaging Guide, 2025`。

**📣 畫面上的字**
> 標題、表頭、三列、倒掛框如上。

**🎙️ 講者這時說**
> 「這三個檔案 90% 的團隊會搞混。requirements.txt 是清單，pyproject.toml 是宣告，lockfile 才是真正能重現的那份契約。尤其 lockfile 一定要進 git——這是很多團隊掉過的坑。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 三層級 MECE（宣告 / 清單 / 鎖定互斥） ✓ / G5 純色 ✓ / G8 無禁色 ✓ / G11 倒掛框 ✓ / G12 表格極簡 ✓ / 原型 TABLE 非退役（與 Slide 4 間隔 2 張，不連續） ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 8 · GEOMETRIC-DIAGRAM · logging 三層架構：Logger → Handler → Formatter，各司其職

**🖼️ 畫面**
> 純幾何三層堆疊結構圖，從左至右水平流動，純深綠 #1B5E3F 方塊 + 深綠箭頭（1.5pt），無人物、無光影、無圖示。
>
> 第 1 層（左）：三個縱向堆疊的白底深綠邊方塊（1pt，圓角 4px）標題上方 12pt 炭灰「Logger（入口 · 命名空間）」：
>   · `logging.getLogger("app")`
>   · `logging.getLogger("app.loader")`
>   · `logging.getLogger("app.model")`
>
> 三個 Logger 以深綠箭頭向右匯入第 2 層。
>
> 第 2 層（中）：兩個縱向堆疊方塊，上方標籤「Handler（輸出目的地）」：
>   · `StreamHandler → stderr`
>   · `RotatingFileHandler → app.log`
>
> 兩個 Handler 以深綠箭頭向右進入第 3 層。
>
> 第 3 層（右）：一個方塊，上方標籤「Formatter（訊息外觀）」：
>   · `"%(asctime)s %(levelname)s %(name)s: %(message)s"`
>
> 三層下方一條 12pt 炭灰橫向註記：「Logger 決定『誰說』· Handler 決定『送到哪』· Formatter 決定『長什麼樣』——三者 MECE」
> 頂部留白 12%、底部留白 18%。
> 右下 8pt 灰 `Source: Python logging HOWTO, cpython 3.13 docs`。

**📣 畫面上的字**
> 標題、三層標籤、各節點名稱、下方 MECE 註記如上。

**🎙️ 講者這時說**
> 「logging 被多數人當成『加時間戳的 print』用，其實它是三層架構。Logger 是入口，Handler 決定送到哪（終端機、檔案、Sentry），Formatter 決定長什麼樣。這三層是互斥的職責，改一層不會污染另一層——這就是為什麼它能在真實系統裡活下去，而 print 不行。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 三層 MECE 職責分離 ✓ / G5 純幾何 ✓ / G7 頂底留白 30%（合計） ✓ / G8 無禁色 ✓ / 無人物無光影 ✓ / 原型 GEOMETRIC-DIAGRAM 非退役（與 Slide 3 間隔 4 張） ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 9 · BEFORE/AFTER · `with` context manager：不是糖，是資源釋放的契約

**🖼️ 畫面**
> 上下兩個程式碼截圖區塊，寬度各占畫面 78% 置中，區塊間距 32px。
>
> 上方標籤「BEFORE（手動 close · 遇例外就洩漏）」炭灰 14pt，程式碼白底深綠 1pt 細邊、等寬字 13pt：
> ```python
> f = open("data.csv", "r", encoding="utf-8")
> data = process(f.read())   # 若此行拋例外
> f.close()                  # 就永遠不會被呼叫 → 檔案握柄洩漏
> ```
> 右側 14pt 深綠粗體「例外路徑 = 資源洩漏」。
>
> 下方標籤「AFTER（`with` 保證無論成功失敗都釋放）」深綠 14pt 粗體，程式碼：
> ```python
> with open("data.csv", "r", encoding="utf-8") as f:
>     data = process(f.read())
> # 離開 with 區塊，__exit__ 自動關閉，例外發生亦然
> ```
> 右側 14pt 深綠粗體「契約等價於 try/finally」。
>
> 兩區塊之間深綠 2pt 向下箭頭，箭頭右側 12pt 炭灰小字「`with` = `__enter__` / `__exit__` 雙方法契約；自寫 class 可 `@contextmanager` 裝飾」。
> 右下 8pt 灰 `Source: PEP 343 — The "with" Statement`。

**📣 畫面上的字**
> 標題、Before/After 標籤、右側標註、箭頭註記如上。

**🎙️ 講者這時說**
> 「`with` 不是讓你少打兩行字的語法糖，是一份資源釋放契約。例外發生時，手寫 close 會被跳過，`with` 不會。檔案、資料庫連線、鎖、GPU 記憶體——凡是需要釋放的，全部該進 with。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G5 代碼純文本 ✓ / G7 上下區塊等高 ✓ / G8 無禁色 ✓ / 原型 BEFORE/AFTER 非退役（與 Slide 6 間隔 2 張） ✓

**💡 敘事弧角色**
> Ground

---

### Slide 10 · SILENT · 會寫程式的多，會釋放資源的少

**🖼️ 畫面**
> 整頁深綠 #1B5E3F 實底。
> 畫面中央偏上一行白字 28pt 粗體，為主標。
> 主標下方 64px 留白，一行白字 14pt 輕量：「— 例外處理、logging、with、lockfile，都是『釋放』的不同形式」。
> 畫面右下 8pt 灰白 `Source: M5 module thesis — Block 3 & 4`。
> 其餘 100% 留白。無任何圖形、無引號符號。

**📣 畫面上的字**
> 「會寫程式的多，會釋放資源的少。」
> 副句如上。

**🎙️ 講者這時說**
> 「停三秒。整個 M5 到目前為止，其實在講同一件事——如何優雅地釋放。例外、資源、鎖、版本，全是同個主題。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 深綠底白字 ✓ / G5 無圖表 ✓ / G7 深色全底即留白（呼吸頁） ✓ / G8 無禁色 ✓ / 原型 SILENT 非退役（與 Slide 5 間隔 4 張） ✓

**💡 敘事弧角色**
> Breather（G7 呼吸頁第 2/3）

---

### Slide 11 · MATRIX · 三種並行機制：啟動成本 × 適用瓶頸，不能混用

**🖼️ 畫面**
> 經典 2×2 MATRIX（擴充標示三個定位點）。
> 水平軸「啟動成本」（左低右高），垂直軸「適用瓶頸類型」（下 I/O-bound、上 CPU-bound）。
> 軸線純灰 #808080 1pt，軸標深綠 14pt。
> 三個深綠 #1B5E3F 實心圓點（直徑 56px）標註於下列座標，圓點旁 14pt 深綠粗體名稱、12pt 炭灰一行特徵：
>
> - **左下（啟動成本低 · I/O-bound）**：`asyncio`
>   特徵：「單 thread / 協作式 / `await` 顯式讓出 / 適合大量 HTTP / DB I/O」
>
> - **左中偏上（啟動成本中 · I/O-bound 為主）**：`threading`
>   特徵：「共享記憶體 / 受 GIL 限制 / 適合 blocking I/O / 啟動快於 process」
>
> - **右上（啟動成本高 · CPU-bound）**：`multiprocessing`
>   特徵：「獨立 process / 繞過 GIL / 真並行 / 啟動慢 / 資料要序列化」
>
> 四個象限底色皆白底，無任何彩色填充。
> 矩陣右下方一行 12pt 炭灰：「三機制 MECE —— 選錯工具不是沒效果，是更慢」
> 右下 8pt 灰 `Source: Python 3.13 concurrency docs / David Beazley 2021 talk`。
> 禁繪人物、動物、平行宇宙插畫。

**📣 畫面上的字**
> 標題、兩軸標籤、三個定位點名與特徵、底部註記如上。

**🎙️ 講者這時說**
> 「這是今天最重要的一張。asyncio、threading、multiprocessing 解的是三個不同的問題——請把它們釘在這個矩陣的三個位置上。混用的代價不是沒加速，是比單執行緒還慢。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 三機制 MECE ✓ / G5 純色無裝飾 ✓ / G7 矩陣四角留白 ✓ / G8 無禁色 ✓ / 原型 MATRIX 非退役 ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 12 · CHART · GIL 真相：純 Python CPU 任務，thread 加再多 CPU 利用率都卡在 1 核

**🖼️ 畫面**
> 全幅一張純色 CHART（折線圖）。白底，無 3D、無漸層、無陰影。
> X 軸「Thread 數量」線性刻度 1 · 2 · 4 · 8 · 16，軸線純灰 1pt、僅保留刻度。
> Y 軸「CPU 利用率（%，8 核機器上限 800%）」線性刻度 0 · 100 · 200 · 400 · 600 · 800。
>
> 兩條折線：
> - 實線（深綠 #1B5E3F，線寬 2.5pt）標籤「純 Python CPU 任務（受 GIL）」：依序 `98%` / `102%` / `104%` / `101%` / `99%` — 近乎水平卡在 100% 附近。線末端直接標註系列名。
> - 虛線（炭灰 #333，線寬 2pt）標籤「I/O bound 任務（釋放 GIL）」：依序 `95%` / `180%` / `340%` / `610%` / `720%` — 近線性爬升至接近 8 核上限。線末端直接標註系列名。
>
> 各節點柱/線頂直接以深綠粗體標註數值。
> 無圖例方塊；標籤直接貼線尾。
> 橫跨 100% 處一條淺灰 #D3D3D3 虛線參考線，右端小字「單核上限」。
> 右下 8pt 灰 `Source: 內部基準測試 — 8 核 M2 Pro / Python 3.12 / cpython-GIL`。

**📣 畫面上的字**
> 標題、兩條線尾標籤、「單核上限」參考線、節點數值如上。

**🎙️ 講者這時說**
> 「這張圖一次講完 GIL。深綠線是純 Python 計算——加到 16 個 thread，CPU 利用率依然卡在 100%，也就是 1 個核。虛線是 I/O 任務，因為 I/O 會釋放 GIL，thread 真的能重疊。GIL 不是 bug，是 CPython 的記憶體管理設計，但它劃清了 threading 在 Python 能走到哪。」

**🎨 視覺紀律 check**
> G1 ✓（完整主張含結果） / G3 主色 ✓（純深綠 + 灰） / G5 ✓（純色折線、無漸層、軸極簡） / G6 ✓（節點精準標註） / G8 無禁色 ✓ / 原型 CHART 非退役 ✓

**💡 敘事弧角色**
> Reveal

---

### Slide 13 · TABLE · PEP 703 時間軸：free-threaded Python 從實驗到預設的路線

**🖼️ 畫面**
> 一張 Editorial 時間軸 TABLE（橫向以年份欄對齊）：僅上下框線（1.5pt 深綠），無竖線，行交替 `#FFFFFF / #F0F0F0`，表頭深綠實底白字 14pt。
> 四欄六列（含表頭）：
>
> | 年份 | 版本 | 狀態 | 對工程實務意義 |
> |---|---|---|---|
> | 2023 | PEP 703 提案通過 | 方向確認 | 社群確認朝「可選移除 GIL」路線走 |
> | 2024 | Python 3.13 | **實驗性**（`--disable-gil` 建置旗標） | 生產禁用；NumPy / pandas thread-safe 驗證中 |
> | 2025 | Python 3.14 | 第二階段穩定化 | 主流套件開始出 free-threaded wheels |
> | 2026（今年） | Python 3.14 + 生態 | **有限生產試點** | 新專案可在隔離服務評估；主訓練管線仍建議 GIL 版 |
> | 2027–2028（預估） | Python 3.15+ | 可能進入預設 | threading 有機會真正取代部分 multiprocessing 場景 |
>
> 表格下方 12% 留白。
> 底部置中 12pt 炭灰單行：「此表反映 2026-04 時點社群進度，版本與時程以 PEP 703 最新狀態為準。」
> 右下 8pt 灰 `Source: PEP 703 / python.org status tracker, 2026-04`。

**📣 畫面上的字**
> 標題、表頭、五列、底部註記如上。

**🎙️ 講者這時說**
> 「2026 的現在，free-threaded Python 還是實驗性，別在生產跑。但方向非常明確——三到四年內，threading 在 Python 的定位會被重寫。你今天學的 MECE 定位，在那之前不會變。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G5 純色 ✓ / G8 無禁色 ✓ / G12 表格極簡 ✓ / 原型 TABLE 非退役（與 Slide 7 間隔 5 張） ✓

**💡 敘事弧角色**
> Ground

---

### Slide 14 · GEOMETRIC-DIAGRAM · I/O-bound 或 CPU-bound？一條決策樹定錨

**🖼️ 畫面**
> 純幾何決策樹，純方塊 + 深綠直角折線箭頭（1pt），無曲線、無光影、無角色、無表情。
>
> 頂端深綠 #1B5E3F 實底白字菱形方塊（決策節點）：
>   「瓶頸在等待 · 還是在計算？」
>
> 向下分兩支：
>
> - **左支「等待（I/O-bound）」**：一個中繼灰字標籤 12pt，再分兩支：
>   - 深綠細邊方塊「大量小 I/O（HTTP / DB）」 → 深綠實底白字方塊「→ `asyncio`」
>   - 深綠細邊方塊「blocking I/O（檔案、舊 client）」 → 深綠實底白字方塊「→ `threading`」
>
> - **右支「計算（CPU-bound）」**：一個中繼灰字標籤，再分兩支：
>   - 深綠細邊方塊「純 Python 迴圈計算」 → 深綠實底白字方塊「→ `multiprocessing`」
>   - 深綠細邊方塊「數值運算 / 張量」 → 深綠實底白字方塊「→ NumPy / PyTorch（底層已並行）」
>
> 樹底部一行 12pt 炭灰橫向註記（占寬 80%）：「兩條路 × 兩個葉 = 四個工具；四者 MECE，不含模糊地帶」
> 左下另標一個深綠粗邊 callout 方塊（寬 30%，置於最底部左側）：
>   「AI 工程實例：`DataLoader(num_workers=4)` = 左支 I/O-bound × `multiprocessing`（資料讀取是 I/O，但 cpython 為了繞開 GIL 用 process 代替 thread）」
> 右下 8pt 灰 `Source: M5 Block 5 + PyTorch DataLoader 文件`。

**📣 畫面上的字**
> 標題、頂端決策節點、四個葉節點工具、底部註記、左下 callout 如上。

**🎙️ 講者這時說**
> 「這是你帶走的那張卡。第一步永遠先分等 vs 算，再分子類。`DataLoader(num_workers=4)` 這行程式，九成工程師背出來但講不清楚——答案就在左下這個小框裡。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 主色 ✓ / G4 兩層 MECE（等 / 算 → 四個葉） ✓ / G5 純幾何 ✓ / G7 底部 callout 外留白 ✓ / G8 無禁色 ✓ / 無人物無光影 ✓ / 原型 GEOMETRIC-DIAGRAM 非退役（與 Slide 8 間隔 5 張） ✓

**💡 敘事弧角色**
> Ground

---

### Slide 15 · SILENT · 工程不是寫得下去，是改得動、跑得再一次、交得出手

**🖼️ 畫面**
> 整頁深綠 #1B5E3F 實底。
> 畫面中央一行白字 30pt 粗體主標，橫跨畫面寬 80%，左右各 10% 邊距。
> 主標下方 80px 留白，一行白字 14pt 輕量：「模組化 · 環境 · 例外 / 日誌 · I/O · 並行 —— 五個 Block，一句結論」。
> 畫面右下 8pt 灰白 `Source: M5 Summary`。
> 其餘 100% 留白。無任何圖形、無引號符號、無裝飾。

**📣 畫面上的字**
> 「工程不是寫得下去，是改得動、跑得再一次、交得出手。」
> 副句如上。

**🎙️ 講者這時說**
> 「M5 結束。下一個模組，我們打開這些抽象概念背後的機械室——CPU 怎麼跑你的程式，記憶體怎麼管你的 DataFrame，process 在作業系統裡長什麼樣。謝謝各位。」

**🎨 視覺紀律 check**
> G1 ✓ / G3 深綠底白字 ✓ / G5 無圖表 ✓ / G7 深色全底即留白（呼吸頁收束） ✓ / G8 無禁色 ✓ / 原型 SILENT 非退役（與 Slide 10 間隔 4 張） ✓

**💡 敘事弧角色**
> Breather / Close（G7 呼吸頁第 3/3）

---

## Deck-level 驗收（Layer C 七條檢查）

1. **完整主張句標題**（G1）：15 張皆為主張句或 Socratic 問句，無名詞片語。✓
2. **顏色紀律**（G3 / G8）：全 deck 僅深綠 `#1B5E3F` + 炭灰 `#333333` + 淺灰 `#D3D3D3` + 白；無紅黃橙粉淺藍。✓
3. **字重 / 字級**：14pt 炭灰 body、20–30pt 深綠標、36–40pt 強調數值、12pt 灰 source；字重 ≤ 3 種、字級 ≤ 4 級。✓
4. **呼吸頁節奏**（G7）：SILENT 分配於 Slide 5 / 10 / 15（3 張 / 4 張 / 5 張間隔），近似每 3–5 張一張。✓
5. **連續原型檢查**：
    - S1 GEO → S2 ASK → S3 GEO（隔 1 張，不連續）
    - S4 TABLE → S5 SILENT → S6 BEFORE/AFTER → S7 TABLE（隔 2 張）
    - S8 GEO → S9 BEFORE/AFTER（不同）
    - S10 SILENT → S11 MATRIX → S12 CHART → S13 TABLE → S14 GEO → S15 SILENT（無連續）
    ✓ 無連續兩張同原型。
6. **純文字頁後緊接圖/表**（G10）：S5 SILENT → S6 BEFORE/AFTER（代碼圖）；S10 SILENT → S11 MATRIX；S15 SILENT 為收束頁。✓
7. **Delete Check**：每張都回應一個 Block 的不可替代主張（可重現性 / 依賴 DAG / 工具選擇 / 例外鏈 / 依賴層級 / logging 架構 / with 契約 / 並行矩陣 / GIL 真相 / PEP 703 / 決策樹），無可刪。✓

**優先三守則落地總結**：
- **G4 MECE**：工具四方（S4）、依賴三層（S7）、logging 三層（S8）、並行三機制（S11）、決策樹兩層（S14）—— 五張以 MECE 為骨。
- **G3 單色紀律**：全 deck 鎖 `#1B5E3F`，無輔色干擾。
- **G7 留白即訊息**：三張 SILENT（S5 / S10 / S15）+ ASK 頁（S2）70% 留白 + 所有 GEO 頁 18% 上下留白。
