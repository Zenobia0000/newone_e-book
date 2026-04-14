# M1 on-page 技術註記 — 逐知識點 review

> **本文件定位：** 公司內部技術 review 的 on-page 批註版，針對 M1 講義逐張投影片、逐程式片段做資深工程師視角的技術質疑與補強。
> **讀者：** 資料 / 平台 / 後端工程師、具 Python 實務經驗的 reviewer、課程共同備課者。
> **使用情境：** 備課前的同儕審查、試講後的技術檢討、針對初學者教材做「技術正確性 / 誤導風險 / 補充深度」三軸檢核。

---

## 註記圖例

- 🎯 **宏觀定位**：這個知識點在整份課綱的位置與戰略意圖
- 🔬 **細部強化**：原講義未覆蓋、但資深 Python 工程師一定會補的細節
- ⚠️ **reviewer 提問**：技術 review 會議上，我會當場丟出的批判性問題

---

## S01 — 你以為的資料分析 vs. 實際在做什麼

🎯 **宏觀定位**
這是全模組的 framing slide，目的不是教技術，是要把學員從「Excel 使用者」心態切換到「資料工程思維」。講義把「60-80% 時間花在清理」這個業界共識講出來，策略上正確，但沒引用來源（CrowdFlower 2016 / Anaconda State of Data Science 都可引）。

🔬 **細部強化**
- 「清理 / 探索 / 推論」三步驟講法偏 Tukey EDA 傳統，現代應補上 **「蒐集（acquisition）」與「部署（deployment）」**，尤其是要通往 M7 ML 路徑時，資料蒐集的 pipeline 才是真實工作的起點。
- 「推論不必然是統計推論」這句話好，但容易被誤解成「不用懂統計」。應清楚切開 inferential statistics 與 business inference 兩個詞。

⚠️ **reviewer 提問**
1. 「60-80%」這個數字要不要標 source？課堂上被學員追問會很尷尬。
2. S01 的循環箭頭圖，會不會誤導學員以為「探索完就推論」是線性？實務上探索會回頭修改清理規則，視覺建議要補雙向箭頭。
3. 為什麼 framing 完全不提 data contract / schema registry？若目標觀眾有後端工程師，這個 framing 會顯得太學術。

---

## S02 — 結構化資料的五個元素

🎯 **宏觀定位**
用「列 / 欄 / 綱要 / 型態 / 鍵」五元素當作整個資料分析 vocabulary 的地基。這五個詞在 M3（pandas）、M4（EDA）、M7（特徵工程）都會重複出現，是教材的中繼變數。

🔬 **細部強化**
- **列 / 欄的順序其實有意識形態**：tidy data（Hadley Wickham, JSS 2014）規定「每一列一個觀測、每一欄一個變數」，講義隱含 tidy data 但沒點名。這是之後 pandas `melt` / `pivot` 的理論基礎，建議點到。
- **鍵（key）** 只講「唯一識別」不夠。要補 **primary key / foreign key / surrogate key / composite key** 四種，否則 M3 做 `merge` 時會一臉茫然。
- **型態**：講義只列 int/float/str/bool/date，漏掉 **categorical**（pandas 的 `category` dtype）與 **nullable integer**（`Int64` 大寫 I），這兩個在 pandas 1.0+ 後是實務必備。

⚠️ **reviewer 提問**
1. 為什麼沒有半結構化（JSON、nested）與非結構化（文本、影像）在此對照？初學者以為世界只有表格，進 M7 做 NLP 會斷層。
2. `df.shape` 回傳 tuple 這個細節被放到 S07 才講，但 S02 就用了 shape，順序是否調整？
3. schema 的定義是「欄名 + 型態」，但實務上 schema 還包含 nullable、default、constraint、unit。是否至少在 footnote 提一下？

---

## S03 — 什麼叫做「乾淨的資料」

🎯 **宏觀定位**
教材的 data quality 入口。四類污染（缺失 / 重複 / 離群 / 型態）是分類框架，不是完整清單。

🔬 **細部強化**
- **缺失值**：`NaN`、`None`、`pd.NA`、`np.nan` 四者語義不同。`NaN` 是 IEEE 754 float 的特殊值，不等於自己（`np.nan == np.nan` 回 False），這個坑會在 boolean indexing 出事。講義應提一句。
- **重複值**：邏輯重複（「台灣積體電路」vs「TSMC」vs「台積電」）屬於 **entity resolution** 問題，是 record linkage / fuzzy matching 子領域，一句話帶過即可，但要讓學員知道這有專門研究。
- **離群值**：講義的判斷很成熟（「不一定是錯誤」），但缺 **檢測方法**（IQR rule、z-score、Isolation Forest 預告），哪怕只列名詞也好。
- **型態錯誤**：「默默產生錯誤結果」是狠話，要給具體例子。例如 `"10" + "2" == "102"`（字串串接）vs `10 + 2 == 12`，這個反直覺 bug 教材沒點破。

⚠️ **reviewer 提問**
1. 四類污染 MECE 嗎？**編碼錯誤（encoding，Big5 vs UTF-8）、時區錯誤、單位錯誤（USD vs TWD）** 都不在這四類，是否要補第五、第六類？
2. 「清理的目的是讓分析可信」的可信如何度量？要不要引入 data quality dimensions（completeness / accuracy / consistency / timeliness / validity / uniqueness，DAMA-DMBOK 六維）？

---

## S04 — Excel 思維 vs. Python 思維

🎯 **宏觀定位**
戰略級 framing，目的是把 Excel 背景的學員引導到 reproducibility / version control 的價值觀。

🔬 **細部強化**
- 「可重現性」應該分三層講：**re-runnable**（同環境能重跑）、**reproducible**（同資料同程式同結果）、**replicable**（他人能驗證）。這是 ACM / NAS 的標準定義。
- 漏了 Excel 的合法領地：**快速原型、給非技術人員看、單次性探索**。講義口吻偏貶抑 Excel，在有 PM / 業務旁聽時會政治不正確。建議加一句「Excel 是 UI，Python 是 pipeline，兩者並非互斥」。
- 可以順手預告 **Power Query / dbt / Airflow** 的位置，讓學員有 ecosystem 感。

⚠️ **reviewer 提問**
1. 「下次只要換一行檔名」這個 pitch 實際上低估了路徑管理、環境差異、相依套件版本等問題，是否會給學員錯覺 Python 真的這麼簡單？
2. Reproducibility 不只靠腳本，還靠環境鎖定（`requirements.txt` / `poetry.lock` / Docker）。這段要不要在 S10 的 import 預告？

---

## S05 — 為什麼 Jupyter Notebook 成為標準

🎯 **宏觀定位**
工具選擇的 rationale。用 literate programming（Knuth 1984）的哲學來正當化 Notebook。

🔬 **細部強化**
- **Notebook 的黑暗面講義完全沒提**，但資深工程師都知道：
  - **Hidden state / out-of-order execution**：cell 執行順序可亂跳，`[1], [5], [2], [3]` 的 `In[]` 編號會害人。Joel Grus 有名的 "I don't like notebooks" JupyterCon 2018 talk 必看。
  - **版本控制不友善**：`.ipynb` 是 JSON，diff 難讀，需要 `nbdime` 或 `jupytext`。
  - **變數污染 / 記憶體洩漏**：大 DataFrame 留在 kernel memory，重啟才乾淨。
  - **Notebook != production**：生產環境該用 `.py`，Notebook 是 EDA 工具。講義 S05 最後有帶到但太輕描淡寫。
- 四合一裡漏了 **互動式 widget（ipywidgets）** 與 **rich display（`IPython.display`）**，這兩個是 Notebook 之於 IDE 的真正優勢。

⚠️ **reviewer 提問**
1. 為什麼不提 **Google Colab / VS Code Notebook / Databricks / Deepnote**？環境選擇會大幅影響學員體驗。
2. Notebook 的 reproducibility 實際上比 `.py` 差（因為 hidden state），這跟 S04 的「Python 可重現」論述是否矛盾？要不要在此承認？
3. `Restart & Run All` 這個習慣要不要在此就強調？學員不做 restart run all，交作業會遇到「我電腦上會跑啊」的經典鬼故事。

---

## S06 — 工作坊 A：用 Notebook 說一個資料故事

🎯 **宏觀定位**
行為養成 workshop，目的不是技術，是「邊寫 code 邊寫 markdown」的職業習慣。

🔬 **細部強化**
- `pd.read_csv("sales_sample.csv")` 的相對路徑在不同學員環境會炸。應明確指示 `Path(__file__).parent / "sales_sample.csv"` 或 Colab 的 mount 流程，並處理 encoding、sep、header 三個常見參數。
- `df.head()` 是 DataFrame 的 repr，只有在 Jupyter 才會 HTML 渲染。若學員複製到 `.py` 執行，會看不到好看的表格。這是 Notebook 專屬行為，值得解釋。
- `groupby("category")["amount"].sum()` 在金額欄是字串時會炸（CSV 的 amount 若含 `$`）。Workshop A 的資料需要事先保證是乾淨的數值，否則 Step 2 會卡住。

⚠️ **reviewer 提問**
1. Step 3 的「結論寫 2-3 句」如何評分？講師注意事項 3 說要主動引導，但缺乏 rubric。
2. 有沒有準備「故意髒一點」的 CSV，讓學員真實踩坑？還是走完全順風的 happy path？順風太多會讓工作坊失真。

---

## S07 — Python 型態與容器

🎯 **宏觀定位**
Python 最小可用詞彙表。有意識地避開 `set` / `frozenset` / `bytes` / `bytearray` / `range` / `complex`，只留六個。教學取捨 OK，但要在講師腳本裡承認「這不是完整 Python，是分析子集」。

🔬 **細部強化**
- **可變 vs 不可變（mutable vs immutable）這條主軸講義完全沒拉出來**，是最大缺口。必須補：
  - immutable：`int`, `float`, `str`, `tuple`, `frozenset`, `bytes`
  - mutable：`list`, `dict`, `set`, `bytearray`
  - 為什麼重要：**dict key 必須 hashable / 函式預設參數陷阱（`def f(x=[]):`）/ Jupyter 跨 cell 共享 mutable 物件的坑**。
- **list vs tuple 的真正差別**不只是「可不可改」：
  - tuple 作為 **struct 語義**（fixed-arity、異質）；list 作為 **array 語義**（variable-length、同質）。
  - tuple 可當 dict key / set element，list 不行。
  - tuple unpacking（`a, b = point`）在函式多值回傳無所不在。
- **str 是 unicode，bytes 才是位元組**。Python 3 把這兩個分開，CSV 讀取的 encoding 錯誤根源就在這。值得一頁補充。
- **f-string vs `.format()` vs `%`**：教材全用 f-string（好），但應說明 f-string 是 3.6+、在 logging 應用 `logger.info("msg %s", x)` 而非 `f"msg {x}"`（避免提早求值與 sanitization 問題）。
- **type hint**：S09 的 `def clean_amount(raw: str) -> float:` 第一次出現 type hint 卻沒解釋。實務價值：IDE 自動補全、mypy 靜態檢查、Pydantic / FastAPI 生態入場券。至少開一格講「為什麼要寫 hint」。
- **Python 3 整數除法**：`7 / 2 == 3.5`，`7 // 2 == 3`。講義有提 `/` 回傳 float，但沒對照 `//`（floor division）。同場加映 `divmod`。
- **浮點精度**：講義有提 `0.1 + 0.2`，但沒給出 IEEE 754 的根本原因（二進位無法精確表示 0.1），也沒提替代方案 `decimal.Decimal` / `fractions.Fraction`。金融例子請用 `Decimal`，別用 float。

⚠️ **reviewer 提問**
1. 為什麼沒有 `set`？`set` 在去重（`set(values)`）與成員檢查（`x in s` 是 O(1)）非常實用，工作坊 B 根本會用到。
2. dict 的 **insertion order 保證（Python 3.7+）** 要不要提？這是影響後續 pandas `.to_dict()` 行為的關鍵。
3. list 的 `.append()` 是 O(1) amortized，`.insert(0, x)` 是 O(n)，`deque` 才是兩端 O(1)。資料分析常見 anti-pattern 是 `list.insert(0, x)` 累積，要不要打預防針？
4. `tuple` 範例用 `df.shape` 很好，但不該只講 shape，應順便講 `(lo, hi, avg) = get_stats(...)` 這種 **packing / unpacking** 的主要使用場景（S09 其實有用，但 S07 沒打預告）。

---

## S08 — 條件與迴圈

🎯 **宏觀定位**
資料篩選的語法基本功。策略上用 `if / for / comprehension` 三件組，點到 pandas 向量化收尾，合理。

🔬 **細部強化**
- **list comprehension 的性能與可讀性邊界**：
  - 性能：`[x*2 for x in lst]` 比等價 `for` loop 快約 30%（少一次 `.append` 方法查找），但跟 `map` / NumPy 向量化比還差一個數量級。
  - 可讀性：單層加單條件 OK，**巢狀 comprehension 超過兩層就該改寫**，否則同事要罵人。
- **generator expression**：`sum(x*x for x in range(n))` 懶惰求值，大資料不爆記憶體。講義一個字都沒提。至少要讓學員看過一次 `(...)` 版本。
- **`enumerate` / `zip`** 是 `for` 的孿生兄弟，沒有它們的 for 迴圈是殘缺的：
  ```python
  for i, row in enumerate(df.itertuples()): ...
  for col, dtype in zip(df.columns, df.dtypes): ...
  ```
- **`for` 迴圈 vs pandas 向量化**：講義說「大部分情況用 `.apply()` 或向量化操作取代」。這句話危險：
  - `.apply()` **不是真的向量化**，它底層還是 Python loop，只是 API 漂亮。真正向量化是 `df["a"] + df["b"]` 這種 NumPy ufunc。
  - 正確排序：**NumPy ufunc > pandas built-in > `.apply()` > Python for loop > `df.iterrows()`（反模式）**。
- **if 表達式（三元）**：`"high" if x > 1000 else "low"`，在 list comprehension 裡是標配，講義沒介紹。
- **walrus operator（`:=`，3.8+）**：在 while 讀檔、filter comprehension 會用到，可選講。

⚠️ **reviewer 提問**
1. `label_order` 函式的 elif 邏輯在 amount 為負數時回傳 `"low_value"`，但負金額通常是退款，是資料污染。這個 edge case 要不要在課堂上故意問出來，訓練學員的 defensive programming 意識？
2. 「資料量大改用 pandas」的切換點在哪？幾萬列？幾百萬列？給學員一個直覺數字。
3. `cleaned = [name.strip().lower() for name in names]` 若 `names` 裡有 `None`，會 AttributeError。要不要示範 `if name is not None` 的防呆？

---

## S09 — 函式：把重複工作變成可呼叫的流程

🎯 **宏觀定位**
從 scripting 邁向 structured programming 的關鍵點。M2 OOP 的前置。

🔬 **細部強化**
- **函式的「純度」（purity）** 必須講：**沒有副作用、同樣輸入永遠同樣輸出**。講義有講「不依賴外部狀態」，但沒給 pure function 這個詞。這個詞是 M5 functional programming、測試、平行化的地基。
- **`clean_amount` 用 `except ValueError` 默默回傳 0.0 是 anti-pattern**：在資料分析情境會造成靜默資料污染，0.0 被當成真實金額混入統計。改良：
  - 回傳 `None` 或 `np.nan`，讓下游清楚這是失敗。
  - 或拋出自訂 exception 由上層決策。
  - 或用 `logging.warning` 留痕跡。
  - **絕對不要用 `except Exception:` 吞掉所有錯誤**（太寬），也絕對不該默默回傳「看起來合理」的數字。
- **預設參數陷阱**：`def f(x=[]):` 的 list 預設會在函式間共享（因為 list 是 mutable，default 只在 def 時 evaluate 一次）。這是 Python 最經典面試題之一，教材不提等於埋雷。
  ```python
  def bad(x=[]): x.append(1); return x
  bad(); bad()  # [1, 1]，不是 [1]
  ```
- **args / kwargs**：資料分析寫 utility 時 `def plot(df, **kwargs):` 轉傳到 matplotlib 很常見。可略提。
- **type hint（接上 S07）**：`def clean_amount(raw: str) -> float:` 寫了但沒解釋 hint 是文件 + 工具輔助、**不是 runtime enforcement**（除非用 Pydantic / dataclass）。學員常誤以為寫了 hint 型別就會檢查。
- **docstring 規範**：範例用自由格式，實務上團隊應用 Google style / NumPy style / Sphinx reST 三擇一。無所謂哪個，要一致。
- **回傳多值**：講義用 tuple，現代 Python 更推 `typing.NamedTuple` 或 `dataclass`，當欄位 3 個以上可讀性大勝。可預告 M2。

⚠️ **reviewer 提問**
1. `clean_amount` 回傳 0.0 的設計在工作坊 B 會被照搬。我們要不要在 S09 先修正這個 anti-pattern？
2. 「一個函式只做一件事」（SRP）這個原則跟講義的 `describe_dataset` 函式（做了 4 件事：shape、dtypes、na、head）自相矛盾。要不要重寫 workshop B 的範例？
3. 函式的 scope / closure / LEGB rule 完全沒提。當學員在 Notebook 的 cell 1 定義 `df`，cell 5 的函式內直接用 `df`（閉包捕獲全域變數），這是隱形 bug 源頭。

---

## S10 — import 與套件

🎯 **宏觀定位**
Python ecosystem 的入口 framing。策略上正確——強調「語言 + 生態」才是 Python 的價值。

🔬 **細部強化**
- **三種 import 寫法**講了，漏了兩種危險寫法：
  - `from module import *`：**幾乎不該用**，會污染命名空間、讓 reader 不知道名字從哪來。
  - 條件 / 延遲 import：`if TYPE_CHECKING:`、函式內 import，在循環相依與啟動時間最佳化時會用。
- **絕對 import vs 相對 import**（`from .utils import x`）：在 package 開發重要，單檔 Notebook 不會遇到，點到即可。
- **套件安裝不該混用 `pip` 和 `conda`**，會產生破碎的相依圖。講義說「簡單帶過」，但這是最常見教學現場災難，應至少一行明確建議：初學者全走 `conda` 或全走 `pip + venv`。
- **`sys.path` / `PYTHONPATH` / import resolution 機制** 對初學者太深，略過合理，但講師應知道學員在 Notebook `ModuleNotFoundError` 九成是 kernel 選錯 Python。
- 套件地圖的圓心輻射圖裡，**應加一層「標準庫」**（`datetime / collections / itertools / pathlib / functools / dataclasses`），讓學員知道很多能力內建、不必 pip。

⚠️ **reviewer 提問**
1. 要不要現場示範一個 `pip install` 失敗（權限、網路、版本衝突）？學員遇到第一次失敗會崩潰。
2. `pyproject.toml` / `uv` / `poetry` 這些現代工具要不要在此略提，還是留給 M5？
3. ecosystem 圖放了 `docker sdk`，放在「系統與工程」層，但 docker 是容器不是 Python 套件，位置容易誤導。

---

## S11 — 工作坊 B：把手動分析步驟變成小函式

🎯 **宏觀定位**
把 S09 的函式化抽象落地到真實資料情境。

🔬 **細部強化**
- `describe_dataset` 違反 SRP（見 S09 提問）。實務上更好的寫法：
  ```python
  def describe_shape(df): ...
  def describe_types(df): ...
  def describe_missing(df): ...
  def describe_dataset(df):
      describe_shape(df); describe_types(df); describe_missing(df)
  ```
  這才是真正「函式化思維」示範。
- `clean_amount_column` 的 `.apply(lambda x: float(x) if x.replace(".", "").isdigit() else None)`：
  - `"1.5.5".replace(".", "").isdigit()` 回 True 但 `float("1.5.5")` 炸。邏輯有漏洞。
  - 更穩健：用 `try/except` 包 `float()`，而非 pre-check。
  - 更 Pythonic：用 `pd.to_numeric(series, errors="coerce")`，一行搞定，直接回傳 `NaN` 於失敗項。**這才是 pandas way**。
- `category_summary` 函式設計不錯，但回傳 `Series` 而非 `DataFrame`，下游若想 join 會需要 `.reset_index()`。可在 docstring 標注回傳型別。
- **缺少測試 / 驗證**：資深工程師寫函式第一步是 `assert` 或 `pytest`，這個工作坊完全沒 test。至少可以加一行：
  ```python
  assert clean_amount_column(pd.Series(["$1,200"])).iloc[0] == 1200.0
  ```

⚠️ **reviewer 提問**
1. 工作坊 B 用了 pandas `.str` / `.apply()` / `groupby`，但 M3 還沒教 pandas。這個順序是否該反過來？
2. 講師注意事項 5 說「可以簡化版本用純 Python for 迴圈」，那為什麼預設版本要用 pandas？取捨不一致。
3. 三個函式寫完之後，學員有沒有看到「這三個函式可以組成 pipeline」的 insight？要不要加第四步把它們串起來？

---

## S12 — 模組總結

🎯 **宏觀定位**
收束 + 製造好奇心通往 M2。

🔬 **細部強化**
- 「還不能做的事」列表漏了一項很重要的：**錯誤處理與日誌**。學員現在寫的函式全是 happy path，真實資料會炸，這是 M5 的入口。
- 「函式 -> class」的類比稍嫌簡化，M2 若處理得不好，學員會以為 class 就是「把一堆函式裝在一起」（其實 class 是 state + behavior 的綁定，重點是 state）。此處先不點破沒關係，但講師要有意識。

⚠️ **reviewer 提問**
1. 模組總結沒有回看「學習目標」的 checkbox 打勾動作，學員難自評。是否加一頁 self-assessment？
2. S12 的時間只有 4 分鐘，但包含回顧 + 預告 + 鼓勵三件事，實務上會超時。要不要砍鼓勵語、留給講師自由發揮？

---

## 跨投影片系統性問題（meta-review）

1. **可變性（mutability）主軸沒拉出來**：M1 的 list / dict / tuple / 函式預設參數 / Notebook 跨 cell 狀態，背後都是同一個議題。教材把它們拆成獨立知識點，學員建立不起 mental model。建議在 S07 加一頁「可變 vs 不可變」總表。
2. **type hint 出現但未教授**：S09 的範例用了 `: str` 和 `-> float`，但沒有一張投影片專門講 hint。初學者會困惑。
3. **Notebook 的黑暗面缺席**：S05 過度 pro-Notebook，S06/S11 工作坊沒訓練 `Restart & Run All` 習慣。這在業界交接時是常見痛點。
4. **錯誤處理（try/except）只在 S09 的 `clean_amount` 隱形出現**，沒有專門教學。資料清理的核心就是錯誤處理，這個缺口會延伸到 M3。
5. **pandas 的提前使用**：S06 / S11 已經大量使用 pandas（`pd.read_csv / groupby / .str / .apply`），但 pandas 在 M3 才教。學員被迫照抄，失去理解。建議 M1 的工作坊全用純 Python（list / dict），pandas 留給 M3。
6. **測試文化完全缺席**：連一行 `assert` 都沒出現。資料工程的可重現性 + 可測試性是雙胞胎，建議 S09 或 S11 加 30 秒「寫函式就順手寫一個 assert」的示範。
