# F5 · Minimum Viable Knowledge（MVK）

> 若只記得 10 件事，這就是 F5（也是整個 6 小時基礎段的收斂版）。
> 對應 01_outline.md 的 5 個 Learning Objectives。

---

## ① 類別設計 2x2：狀態 vs 動作（對應 LO1）

| 維度 | 歸屬 | 寫法 |
|---|---|---|
| 狀態 | Instance Attribute | `self.path` / `self.df` |
| 動作 | Method | `validate` / `clean` / `apply` / `export` |
| 鏈式 | `return self` | 每個改 `self.df` 的 method 結尾 |
| 例外 | 自訂 Exception | `raise DataValidationError(col, reason)` |

**一句口訣**：狀態存起來、動作做事情、鏈式回自己、例外帶語意。

---

## ② 六個方法簽名（必背）

```python
class DataCleaner:
    def __init__(self, data_path: str): ...
    def validate(self) -> "DataCleaner": ...
    def clean_missing_values(self, strategy: str = "drop") -> "DataCleaner": ...
    def apply_custom_transform(self, column: str, func) -> "DataCleaner": ...
    def generate_eda_report(self, out_path: str) -> "DataCleaner": ...
    def export_data(self, out_path: str) -> "DataCleaner": ...
```

**一進（init）、五動（其他）、全部 return self**。

---

## ③ 自訂 Exception（對應 LO3）

```python
class DataValidationError(Exception):
    def __init__(self, column: str, reason: str):
        self.column = column
        self.reason = reason
        super().__init__(f"[{column}] {reason}")

# 使用
raise DataValidationError("revenue", "出現負值")

# 上游精準 catch
try:
    cleaner.validate()
except DataValidationError as e:
    log.warning(f"{e.column}: {e.reason}")
```

**一個就夠，別定義 5 種**；column/reason 兩個欄位帶語意。

---

## ④ 六段管線完整鏈式（對應 LO2 + LO4）

```python
(DataCleaner("raw.csv")
    .validate()
    .clean_missing_values(strategy="mean")
    .apply_custom_transform("revenue", lambda x: x * 1.05)
    .generate_eda_report("report.png")
    .export_data("clean.csv"))
```

**讀起來像英文**：驗證 → 清洗 → 變換 → 報表 → 匯出。

---

## ⑤ 五大踩雷速查

| ID | 踩雷 | 修正 |
|---|---|---|
| P1 | method 忘記 `return self` | 每個改 self.df 的 method 結尾都加 |
| P2 | `__init__` 不驗證 | 檔案不存在就 `raise FileNotFoundError` |
| P3 | `raise Exception('xxx')` | 自訂 `DataValidationError(col, reason)` |
| P4 | 30 行腳本硬包 class | 用兩次以上才包，否則保持腳本 |
| P5 | 只會抄範本、不會改 | 課堂練習逼自己加 1 method / 1 規則 / 1 圖 |

---

## ⑥ F1-F5 基礎段能力盤點（5 段）

| 章節 | 核心能力 | 在 F5 用在哪 |
|---|---|---|
| F1 | OS / RAM / I/O 直覺 | `pd.read_csv` 的效能從何而來 |
| F2 | list / dict / Lambda / Comprehension | `apply(lambda x: ...)` 的 Lambda |
| F3 | class / `__init__` / self | `DataCleaner.__init__` 讀檔並存 self |
| F4 | 繼承 / 魔術方法 / 封裝 | `class DataValidationError(Exception)` |
| F5 | OOP × Pandas 整合（今天） | 把上面四段組成可鏈式工具 |

**底層越穩、上層越能長**。

---

## ⑦ S1-S6 實戰段對應（6 段，快速回顧）

| 章節 | 核心能力 | 在 F5 DataCleaner 呼應 |
|---|---|---|
| S1 | NumPy 向量化 | `numeric.columns[:4]` 選值 |
| S2 | Pandas IO / 缺失值 | `read_csv` / `dropna` / `fillna` |
| S3 | groupby / merge / pivot | （擴充方向：加聚合 method） |
| S4 | 時序 / EDA | `generate_eda_report` 的骨架 |
| S5 | matplotlib 五圖 | `plt.subplots(2,2) + hist` |
| S6 | Plotly dashboard.html | （擴充方向：把 eda 換成 html） |

**F5 + S1-S6 = 11 段完整能力地圖**。

---

## ⑧ 下一步學習路徑（5 選 1，3 個月精讀）

| 方向 | 推薦起點 | 什麼時候該選 |
|---|---|---|
| 資料庫整合 | **SQL + SQLAlchemy** | 工作要接 DB，CSV 已經不夠用 |
| 機器學習 | **scikit-learn** | 清洗好的資料想做預測 |
| 大規模資料 | **Polars / DuckDB** | Pandas 讀 GB 級檔案開始慢 |
| 自動化排程 | **Airflow / Prefect / n8n** | 手動跑管線已經煩到想自動化 |
| 雲端部署 | **AWS S3+Lambda / GCP BQ** | 管線要共享、要排程、要被其他系統呼叫 |

**Linus 忠告**：挑一條走完，比五條都碰過更值錢。

---

## ⑨ 結業三句紀律（Linus 風格）

1. **跑得起來不算數，6 個月後看得懂才算數** — type hint、docstring、好的變數名別省。
2. **最強的優化是「不要做」** — 能砍的程式比能寫的程式更值錢。
3. **OOP 不是萬靈丹** — 30 行腳本不需要 class；重用兩次以上才包。

---

## ⑩ 結業金句

> 「6 小時基礎的終點，不是『你會 OOP』——
> 是你能把 F1-F4 + Pandas 組成一條會跑的 DataCleaner。
> 下一站 —— 選一條路，3 個月後見。」
