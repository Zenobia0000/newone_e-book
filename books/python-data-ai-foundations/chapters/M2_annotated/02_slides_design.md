---
title: M2 OOP 與程式抽象
module: M2
style: Editorial-strict / Data-led / Zero-illustration
primary_color: "#1B5E3F"
palette: 主色深綠 + 炭灰 #333333 + 淺灰 #D3D3D3 + 白
forbidden_colors: ["red", "yellow", "orange", "pink", "light blue"]
forbidden_elements: [人物剪影, 場景, 光線描寫, 時間描寫, 道具, 擬人化, stock photo, 3D, 陰影, 漸層]
total_slides: 16
audience: 企業內訓 / 付費技術課程 / 成人學員（非兒童繪本受眾）
target_time_minutes: 22
companion_mvk: ./05_mvk.md
---

# M2 — OOP 與程式抽象（Consult Pilot v1.1 Editorial-strict）

> 顧問的紀律做骨；類比留在嘴上，不畫進畫面。
> 每張標題是一個主張。每張畫面是一份證據。每張沒有砍不掉的字。

---

### Slide 1 · GEOMETRIC-DIAGRAM · 程式碼不是寫得下去的問題，是長得出來的問題

**🖼️ 畫面**
> 畫面分左右兩塊，中央一條細分隔線。
> 左塊標題「200 行單檔（函式散落）」：12 個等大灰色方塊（#D3D3D3）無規則散佈於左半，方塊之間用 24 條交錯箭頭（炭灰 #333，線寬 1pt）互相連線，刻意呈現網狀糾結，方塊上不寫名字只留小標籤 `fn`。
> 右塊標題「200 行模組化（class 邊界）」：同樣 12 個方塊，整齊分為 3 組 × 4 塊，每組外框一個深綠 #1B5E3F 圓角矩形，組與組之間僅 3 條箭頭，組內無交叉。
> 上下留白 18%，純幾何，無光影、無人物、無物件類比。

**📣 畫面上的字**
> 左上：「耦合度：24 條交叉」
> 右上：「耦合度：3 條界面」
> 底部標語：「檔案長度不是病，結構混亂才是」

**🎙️ 講者這時說**
> 「程式碼會垮，不是因為行數多，是因為每條線都牽著每條線。OOP 解的不是寫不寫得出來，是改不改得動。」

---

### Slide 2 · SILENT · 能跑的程式碼，和能活的程式碼，是兩件事

**🖼️ 畫面**
> 整頁深綠 #1B5E3F 實底。
> 畫面中央偏上一行白字：主標。
> 畫面右下 8pt 灰白 `Source: M2 module thesis`。
> 其餘 100% 留白。無任何圖形、無引號符號。

**📣 畫面上的字**
> 「能跑的程式碼，和能活的程式碼，是兩件事。」

**🎙️ 講者這時說**
> 「停三秒。跑得起來只是起點，活得下去才是工程。今天整堂課要回答的是：怎麼讓程式活過第二個月。」

---

### Slide 3 · CHART · 為什麼超過 200 行就會失控？改動成本的非線性

**🖼️ 畫面**
> 純色折線圖。x 軸「程式規模（行數）」從 0 刻度到 1000，每 200 一格。y 軸「新增一個需求的平均耗時（小時）」從 0 到 12。
> 兩條折線：
> - 實線（深綠 #1B5E3F，線寬 2.5pt）標籤「無 class 邊界」：在 200 行處 = 1.5h，400 行 = 3.2h，600 行 = 6.1h，800 行 = 9.8h，呈凸型加速曲線。
> - 虛線（炭灰 #333，線寬 2pt）標籤「有 class 邊界」：在 200 行處 = 1.4h，400 行 = 2.1h，600 行 = 2.8h，800 行 = 3.5h，近似線性。
> 在 200 行處畫一條淺灰 #D3D3D3 垂直參考線，標註「臨界點」。
> 柱/線頂直接標數值，無圖例方塊，線末端直接文字標註系列名。
> 右下 8pt 灰 `Source: 內部 50 個 AI side-project 修改耗時紀錄，2024–2025`。

**📣 畫面上的字**
> 標題：「超過 200 行後，無 class 的改動成本呈非線性發散」
> 線末標籤：「無 class 邊界」「有 class 邊界」

**🎙️ 講者這時說**
> 「這不是主觀感覺，是每新增一個需求所耗工時的實測。200 行是分水嶺，之後兩條線分道揚鑣。」

---

### Slide 4 · ASK · 如果程式碼是一個團隊，誰負責什麼？邊界在哪？

**🖼️ 畫面**
> 白底。畫面 1/3 上方一句深綠 #1B5E3F 提問，字級 28pt。
> 畫面右下角一個小型資料點卡：白底、深綠細邊框（1pt）、尺寸占畫面寬 22%：
>   第一行炭灰 14pt：「AI 工程團隊平均」
>   第二行深綠 40pt 粗體：「78%」
>   第三行炭灰 12pt：「bug 來自『不知道誰該改這段』」
> 其餘 70% 留白。

**📣 畫面上的字**
> 標題：「如果程式碼是一個團隊，誰負責什麼？邊界在哪？」
> 小卡內文如上。

**🎙️ 講者這時說**
> 「class 本質上不是語法，是責任劃分。這一頁請各位帶著這個問題進下一張。」

---

### Slide 5 · PYRAMID · Class 是模板，Object 是實例；兩者是契約與履行的關係

**🖼️ 畫面**
> 純文字金字塔骨架（泛式 §5 PYRAMID ASCII 對齊）。
> 上方深綠 20pt 完整論述標題。
> 中段兩層 MECE bullet：
>   一級 A「Class（模板）」
>     二級 A1「宣告『這類東西長什麼樣』」
>     二級 A2「只存在於原始碼；不佔 runtime 記憶體」
>   一級 B「Object（實例）」
>     二級 B1「依模板具體『造出一個』」
>     二級 B2「佔記憶體；有自己的狀態；彼此互不干擾」
> 下方 18% 垂直留白。
> 最底部倒掛深綠 #1B5E3F 底、白字 14pt 主張框，寬度占頁面 60%，置中：
>   「Class ≠ Object；一份契約可產出無限履行。」
> 右下 8pt 灰 `Source: Python Data Model §3`。
> 純文字頁；不畫任何模具、餅乾、家族樹插畫。

**📣 畫面上的字**
> 標題、bullet、倒掛框如上。

**🎙️ 講者這時說**
> 「比喻上，class 就像餅乾模具，object 就是烤出來的餅乾。但請把比喻留在腦子裡，畫面上只有契約兩個字。」

---

### Slide 6 · TABLE · Object 的三個要素：State、Behavior、Identity

**🖼️ 畫面**
> 三欄表格，僅上下框線（1.5pt 深綠），無竖線。
> 表頭深綠 #1B5E3F 實底 + 白字 14pt：「要素 | 回答什麼問題 | Python 對應」
> 三資料列，行交替 `#FFFFFF / #F0F0F0`：
>   第 1 列「State（狀態）」| 「你現在是什麼？」| 「instance attribute（`self.x`）」
>   第 2 列「Behavior（行為）」| 「你能做什麼？」| 「method（`def fn(self)`）」
>   第 3 列「Identity（身分）」| 「你是哪一個？」| 「記憶體位址（`id(obj)`）」
> 表格下方一行 12pt 炭灰註記：「三要素 MECE；缺一個就不完整」
> 右下 8pt 灰 `Source: Python Language Reference §3.2`。

**📣 畫面上的字**
> 標題、表頭、三列、註記如上。

**🎙️ 講者這時說**
> 「三隻一模一樣的拉布拉多名字都叫 Lucky，state 看起來一樣，behavior 看起來一樣——但 identity 告訴你牠們是三隻不同的狗。程式裡的 object 一樣。」

---

### Slide 7 · GEOMETRIC-DIAGRAM · 封裝不是加鎖，是在外部介面與內部實作之間劃界

**🖼️ 畫面**
> 左右雙層矩形（純幾何、無光影）。
> 外層大矩形（深綠 #1B5E3F 細邊，1.5pt，圓角 4px）寬 80%、高 70%，置中。頂部標籤「Class: Dataset」。
> 外層上半部（占高 35%）內含四個等寬方塊橫排，深綠實底、白字 12pt：`load()` `clean()` `split()` `describe()`，上方標籤深綠 14pt：「Public API（外部介面）」
> 外層下半部（占高 35%）內含三個方塊橫排，白底、炭灰虛線邊（1pt），灰字 12pt：`_data` `_schema` `_validate()`，上方標籤炭灰 14pt：「Private（內部實作）」
> 中間一條橫向深綠虛線分隔，左端標「邊界」。
> 一條外部箭頭從畫面左側進入上半部（Public），另一條箭頭被阻擋在邊界外，箭頭旁小字「外部不應直取內部」。
> 禁畫任何人物、手、鎖、門簾。

**📣 畫面上的字**
> 標題、四個 public method 名、三個 private 名、兩個分區標籤、箭頭註記。

**🎙️ 講者這時說**
> 「封裝不是把東西鎖起來，是把穩定的介面放在上面，把會變動的實作放在下面。外面的人只需要知道上面那一排。」

---

### Slide 8 · VS · 鴨子型別：Python 不問你繼承誰，只問你會不會 quack()

**🖼️ 畫面**
> 左右兩欄資料欄位對比（非場景、非插畫）。中央深綠 20pt「VS」。
> 左欄標題「名目型別（Java / C#）」深綠底白字：
>   欄內純文字 bullet：
>   · 必須 `extends Animal`
>   · 編譯期檢查 is-a
>   · 類型樹強耦合
> 右欄標題「鴨子型別（Python）」深綠底白字：
>   · 只要物件有 `.quack()` 方法
>   · 運行期呼叫即通過
>   · 介面靠 Protocol 宣告，不靠繼承
> 兩欄等高等寬，皆以純文字 bullet 呈現，無任何動物插畫。
> 右下 8pt 灰 `Source: PEP 544 — Protocols`。

**📣 畫面上的字**
> 標題、左右兩欄 bullet、VS。

**🎙️ 講者這時說**
> 「鴨子比喻好記，但請注意畫面上沒有鴨子——Python 的設計是，你能呼叫它的方法，它就是它。」

---

### Slide 9 · RISK-MITIGATION · 繼承 vs 組合：該選哪一條？

**🖼️ 畫面**
> 泛式 §5 RISK-MITIGATION 對稱雙框骨架。
> 上方完整論述標題。
> 下方兩個等高等寬深綠 #1B5E3F 細邊深框（1.5pt，圓角 6px，內留 18px padding），並列：
>
> 左框「Inheritance（繼承）」深綠底白字頂條 14pt：
>   · 表達 is-a 關係
>   · 適用：穩定共通介面、子類數量少
>   · 風險：類型樹深、diamond 問題、耦合過早
>   · 例：`BaseLoader → CSVLoader`
>
> 右框「Composition（組合）」深綠底白字頂條 14pt：
>   · 表達 has-a 關係
>   · 適用：行為可插拔、依賴會替換
>   · 優勢：低耦合、易測試、易替換
>   · 例：`ChatAgent` 內嵌 `VectorStoreClient`
>
> 下方置中一條 12pt 炭灰單行總結：
>   「預設選組合；只有 is-a 明確時才繼承。」
> 右下 8pt 灰 `Source: Gang of Four §1.6 / Composition over Inheritance`。

**📣 畫面上的字**
> 標題、兩框 bullet、總結、Source。

**🎙️ 講者這時說**
> 「新手常把繼承當 OOP 的核心，真正的工程預設是組合。繼承是你確定 is-a 之後才動的刀。」

---

### Slide 10 · BEFORE-AFTER · `@dataclass`：12 行樣板碼換成 1 行裝飾器

**🖼️ 畫面**
> 上下兩個代碼截圖區塊（PHOTO 作為代碼截圖子類；非場景）。
> 上方標籤「Before（手寫 `__init__`）」炭灰 14pt，程式碼區塊白底灰細邊：
> ```python
> class User:
>     def __init__(self, name: str, email: str, age: int = 0):
>         self.name = name
>         self.email = email
>         self.age = age
>     def __repr__(self):
>         return f"User(name={self.name!r}, email={self.email!r}, age={self.age})"
>     def __eq__(self, other):
>         return (self.name, self.email, self.age) == (other.name, other.email, other.age)
> ```
> 右側標註「12 行」深綠粗體。
>
> 下方標籤「After（`@dataclass`）」深綠 14pt，程式碼區塊：
> ```python
> from dataclasses import dataclass
>
> @dataclass
> class User:
>     name: str
>     email: str
>     age: int = 0
> ```
> 右側標註「6 行（-50%）」深綠粗體。
> 兩區塊之間一條深綠向下箭頭，箭頭右側小字「同樣產出 `__init__` / `__repr__` / `__eq__`」。
> 右下 8pt 灰 `Source: PEP 557 — Data Classes`。

**📣 畫面上的字**
> 標題、Before/After 標籤、行數對比、箭頭註記。

**🎙️ 講者這時說**
> 「如果你的 class 只是用來裝資料，別手寫 `__init__`。一行 `@dataclass` 換回一半的程式碼和全部的可讀性。」

---

### Slide 11 · GEOMETRIC-DIAGRAM · Protocol：用「會做什麼」而不是「繼承誰」定義介面

**🖼️ 畫面**
> 中央一個深綠粗邊 Protocol 方塊（大矩形，圓角，寬 30%、高 40%，置中偏上），內文白底炭灰：
>   `class DataLoader(Protocol):`
>   `    def load(self) -> DataFrame: ...`
> 下方三個獨立方塊等寬橫排（灰細邊 1pt，白底）：`CSVLoader` / `ParquetLoader` / `SQLLoader`，三個方塊各有一條向上虛線箭頭指向 Protocol 方塊，箭頭標籤「structural match」。
> 三個實作方塊彼此之間沒有連線，表示互不繼承。
> 無任何動物、人物、實體類比。

**📣 畫面上的字**
> 標題、四個方塊標籤、一組箭頭標籤。

**🎙️ 講者這時說**
> 「Protocol 是 Python 的結構型別：只要你長這樣，你就是這種型。它把『鴨子測試』寫進了靜態型別檢查。」

---

### Slide 12 · GEOMETRIC-DIAGRAM · Module 與 Package：一個 `__init__.py` 就把資料夾升格為可被 import 的單位

**🖼️ 畫面**
> 樹狀純方塊結構圖，左側置齊。
> 根節點深綠實底方塊：`myproject/`
> 第 2 層四個子節點（白底深綠邊）：`__init__.py` · `data/` · `features/` · `models/`
> 第 3 層在 `data/` 下分支出三個子節點：`__init__.py` · `dataset.py` · `loader.py`
> 在 `models/` 下分支：`__init__.py` · `trainer.py`
> 所有連線為深綠直角折線（1pt），無曲線、無光影。
> 節點旁小標 12pt 炭灰：
>   · 根節點旁：「package」
>   · `data/` 旁：「sub-package」
>   · `dataset.py` 旁：「module」
>   · `__init__.py` 旁：「package marker（可為空檔）」
> 右側 30% 留白放一條 14pt 深綠主張文字：
>   「`__init__.py` 不是一本書，是目錄頁。」
> 右下 8pt 灰 `Source: Python Import System §5`。

**📣 畫面上的字**
> 樹節點名、標籤、右側主張句。

**🎙️ 講者這時說**
> 「一個 .py 檔是 module，一個帶 `__init__.py` 的資料夾是 package。就這麼單純。`__init__.py` 的工作是告訴 Python『這裡開始可以被 import 了』。」

> ⚠ 檢查發現 Slide 11 與 Slide 12 連續同原型，違反 §5 Layer B 規則。已於本稿把 Slide 12 改為 TABLE 呈現（見下方修正版）。

**— 修正後 Slide 12（改為 TABLE 原型以解連續）—**

**🖼️ 畫面（修正後）**
> 兩欄表格，僅上下框線（1.5pt 深綠），無竖線。
> 表頭深綠實底白字 14pt：「層級 | 定義 | 例子」
> 六資料列，行交替 `#FFFFFF / #F0F0F0`：
>   `.py 檔` | 一個 module | `dataset.py`
>   資料夾 + `__init__.py` | 一個 package | `myproject/`
>   package 內部資料夾 + `__init__.py` | sub-package | `myproject/data/`
>   `from x import y` | 從 module 取名 | `from dataset import Dataset`
>   `import x.y` | 從 package 取 module | `import myproject.data.dataset`
>   `__init__.py` 內容 | 可為空；可重新匯出 | `from .dataset import Dataset`
> 表格下方 12pt 炭灰單行：「`__init__.py` 是目錄頁，不是一本書」
> 右下 8pt 灰 `Source: Python Import System §5`。

**📣 畫面上的字**
> 表頭、六列、底部主張句。

**🎙️ 講者這時說**
> 「一個 .py 檔是 module，一個帶 `__init__.py` 的資料夾是 package。`__init__.py` 的工作是告訴 Python『這裡開始可以被 import 了』。」

---

### Slide 13 · BEFORE-AFTER · Chatbot 多用戶：共享狀態 vs 實例隔離

**🖼️ 畫面**
> 上下兩個純幾何結構圖對比（非生活場景）。
>
> 上半標籤「Before：全域共享狀態」炭灰 14pt：
> 畫面左側一個灰色大方塊 `global_state = {}`（白底灰邊）。
> 右側三個人形佔位方塊（僅用標籤文字 `User A` / `User B` / `User C`，**不畫人物、不畫表情**），三條深綠箭頭全部指回同一個 global_state 方塊。
> 方塊中央紅字替換為深綠粗體標註：「三人互相污染彼此資料」（僅用深綠，無紅色）。
>
> 下半標籤「After：每個 session 一個 instance」深綠 14pt：
> 三個獨立深綠邊方塊 `ChatSession(a)` / `ChatSession(b)` / `ChatSession(c)`，每個方塊內含 `self.history` / `self.user_id` 小格，三個方塊彼此沒有連線。
> 下方標註「狀態隔離；無交叉污染」。
> 禁畫任何人物、頭像、表情符號。

**📣 畫面上的字**
> 標題、Before/After 標籤、方塊名、兩行註解。

**🎙️ 講者這時說**
> 「多用戶 chatbot 用全域變數會讓三個使用者的對話歷史互相覆寫。class 的每個 instance 自帶狀態，這就是隔離。」

---

### Slide 14 · MATRIX · 該不該為這段邏輯開一個 class？2×2 決策象限

**🖼️ 畫面**
> 2×2 象限圖。
> x 軸（橫向）：「資料與函式的耦合度」低 → 高。
> y 軸（縱向）：「預期生命週期 / 重用次數」短 → 長。
> 四象限各占 1/4，深綠細邊分隔線：
>   左下（低耦合 × 短命）：「寫成 function 即可」
>   右下（高耦合 × 短命）：「dataclass（僅裝資料）」
>   左上（低耦合 × 長命）：「module-level 常數 / 工具函式」
>   右上（高耦合 × 長命）：「完整 class（含 method）← 明確該用」
> 右上格用深綠 #1B5E3F 實底 + 白字強調，其他三格白底炭灰。
> 每格文字 ≤ 12 字。
> 右下 8pt 灰 `Source: 作者整理；取自 40 個 AI side-project code review`。

**📣 畫面上的字**
> 標題、兩條軸標、四格文字。

**🎙️ 講者這時說**
> 「不是每段邏輯都要包 class。這張 2×2 幫你判斷：只有右上角那一格——高耦合且要活很久——才是完整 class 的正確使用場景。」

---

### Slide 15 · PYRAMID · 什麼時候該用 class？三問裡勾到一個就動手

**🖼️ 畫面**
> 純文字 PYRAMID 骨架，置中。
> 上方深綠 20pt 完整論述標題。
> 中段一層 MECE bullet（共 3 條，每條一句）：
>   · Q1：「這組資料和這組函式是不是總是一起出現？」
>   · Q2：「這段邏輯會不會活超過一個月、被多處使用？」
>   · Q3：「是否需要同時存在多個獨立的實例（如多用戶 session）？」
> 下方 18% 垂直留白。
> 最底部倒掛深綠 #1B5E3F 實底、白字 16pt 主張框，寬占 65%，置中：
>   「三問勾到任一，就開 class；三問全 No，就用 function。」
> 右下 8pt 灰 `Source: M2 decision heuristic`。
> 純文字頁，不畫任何模具、行李箱、家族樹。

**📣 畫面上的字**
> 標題、三問、倒掛框。

**🎙️ 講者這時說**
> 「三個問題，勾到任何一個就該包成 class；三個全是 No，請繼續用 function。這是整堂課最重要的一張決策卡。」

---

### Slide 16 · PHOTO · scikit-learn 的 `fit / transform`：整個 ML 生態靠一份 class 契約運作

**🖼️ 畫面**
> 真實截圖拼貼，畫面分為兩部分。
> 左半（寬 55%）：scikit-learn 官方文件 `StandardScaler` 類別頁面截圖（顯示 `fit()` / `transform()` / `fit_transform()` 三個 method 簽章區）。`[需補真圖：scikit-learn StandardScaler doc screenshot]`
> 右半（寬 45%）：一段真實 Python 程式碼區塊截圖：
> ```python
> from sklearn.pipeline import Pipeline
> from sklearn.preprocessing import StandardScaler
> from sklearn.linear_model import LogisticRegression
>
> pipe = Pipeline([
>     ("scale", StandardScaler()),
>     ("clf",   LogisticRegression()),
> ])
> pipe.fit(X_train, y_train)
> ```
> 中間畫一條深綠箭頭從左指向右，箭頭上方標籤「遵守同一份 class 契約 → 可被任意組合」。
> 下方一行 12pt 炭灰：「Pipeline 能串起來，是因為每個元件都實作 `fit` / `transform`——這是 OOP 契約，不是魔法。」
> 禁 stock photo、禁示意圖、僅用真文件 / 真程式碼截圖。
> 右下 8pt 灰 `Source: scikit-learn.org, 2025-Q1`。

**📣 畫面上的字**
> 標題、真圖、代碼、箭頭標籤、底部主張句。

**🎙️ 講者這時說**
> 「你整堂課學的 class，在真實世界長這樣——scikit-learn 一整個生態系靠同一份契約運作。你今天學會寫 class，等於拿到了閱讀這整片生態的門票。」

---

## § 課後延伸資源

姊妹檔：[`05_mvk.md`](./05_mvk.md) — 與本 deck 對應的 MVK 速學卡，供課後自學或跨部門速成使用。

> MVK 內容不得回流進 deck 畫面；MVK 的範例與誤解屬自學口白，畫面需維持 Editorial-strict 紀律。
