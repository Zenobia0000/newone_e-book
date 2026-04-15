# Ch10 · Minimum Viable Knowledge

**章節**：OOP × Pandas 整合實戰（M4 · 1.5 hr · 最終收斂章）
**Governing thought**：不是再學一個新 API，是把前九章每一項能力擰成一條可執行、可擴充、可交付的資料管線。

---

## 一、設計一個類別之前先問的四題

1. **狀態是什麼？** → instance attributes（`self.path`、`self.df`）
2. **動作是什麼？** → methods（`validate`、`clean`、`apply`、`eda`、`export`）
3. **哪些動作能串？** → 每個動作 `return self` → 開啟 Method Chaining
4. **哪些情境該炸？** → 自訂 `Exception`，錯資料不吞、不 print

---

## 二、DataCleaner 的六個方法（背得起來）

| 方法 | 職責 | 呼應章節 |
|------|------|---------|
| `__init__(path)` | 檢查檔案存在 → 讀 CSV → 存 `self.df`（fail fast） | Ch4 + Ch6 |
| `validate()` | 空表 / 負值 → raise `DataValidationError` | Ch6 |
| `clean_missing_values(strategy)` | 'drop' / 'mean' 雙策略，字串參數化 | Ch8 |
| `apply_custom_transform(col, func)` | 欄位檢查 → `df[col].apply(func)` | Ch3 + Ch8 |
| `generate_eda_report(out_path)` | `plt.subplots(2,2)` → 每欄 hist → `savefig` | Ch9 |
| `export_data(out_path)` | `to_csv` + 列數 log | Ch8 |

**全部回傳 `self`** — 這是 Method Chaining 的入場券。

---

## 三、自訂 Exception 的最小模板

```python
class DataValidationError(Exception):
    def __init__(self, column, reason):
        self.column = column
        self.reason = reason
        super().__init__(f"[{column}] {reason}")
```

- 帶 **結構化資料**（column、reason），不是只有字串
- 上游可以 `except DataValidationError as e: e.column`
- 不要 raise 泛型 `Exception` / `ValueError` — 語意含糊

---

## 四、Method Chaining 的標準寫法

```python
(DataCleaner('raw.csv')
    .validate()
    .clean_missing_values(strategy='mean')
    .apply_custom_transform('revenue', lambda x: x * 1.05)
    .generate_eda_report('report.png')
    .export_data('clean.csv'))
```

- 外層括號包住整條鏈 — 讓每個動作獨立一行
- 每行讀起來像動詞短句 — 比流程圖還清楚
- 一個方法一件事 — 不要在一個方法裡做三件事

---

## 五、18 小時能力盤點（由下而上）

1. **系統直覺** — OS / RAM / I/O 三個關鍵字（Ch1）
2. **Python 進階** — Generator / Lambda / Comprehension / 自訂函式（Ch2–Ch3）
3. **OOP** — 類別、繼承、魔術方法、Method Chaining（Ch4–Ch5）
4. **資料工程** — I/O、Exception、NumPy 向量化、Pandas 七步流水線（Ch6–Ch8）
5. **視覺化與整合** — Matplotlib EDA、OOP × Pandas 封裝（Ch9–Ch10）

---

## 六、下一站五條路線

| 方向 | 推薦起點 | 一句話 |
|------|---------|--------|
| 資料庫整合 | SQLAlchemy | 把 CSV 換成資料庫 |
| 機器學習 | scikit-learn | 把清洗好的資料餵給模型 |
| 大規模資料 | Polars、DuckDB | 當 Pandas 變慢時的下一站 |
| 自動化排程 | Airflow / Prefect / n8n | 讓你的管線每天自動跑 |
| 雲端部署 | AWS S3+Lambda、GCP BigQuery | 把腳本搬上雲 |

---

## 七、Linus 三句結業忠告

1. 跑得起來不算數，能讓三個月後的自己看懂才算數
2. 最強的優化是「不要做」—— 在向量化之前，先想能不能跳過這步
3. OOP 不是萬靈丹，30 行的腳本不需要類別

---

## 學生離開教室時應能

1. 拆出一個類別的「狀態 vs 動作」並畫介面草圖
2. 寫出帶結構化資料的自訂 Exception 並在適當時機 raise
3. 以 `return self` 設計可鏈式的 API
4. 實作一個 6 方法的 DataCleaner，並用 Method Chaining 串起完整 pipeline
5. 說出自己下一步學習路線的第一個 API 名字

## 本章刻意不深教

- Strategy Pattern 完整實作（點到為止）
- `logging` 模組細節（列為改進作業）
- `@classmethod from_config` 完整實作（列為改進作業）
- 抽象類別 `ABC` / `abstractmethod`（下一階段）

## 期末作業要點

1. 挑一份真實資料集（Kaggle / 政府開放資料 / 工作資料）
2. 自訂一個 `XxxCleaner` 類別 — 至少 5 個方法 + Method Chaining
3. 至少 1 個自訂 Exception
4. 自動產出 4 張以上的 EDA 報表
5. 程式碼上 GitHub，README 說明用法
