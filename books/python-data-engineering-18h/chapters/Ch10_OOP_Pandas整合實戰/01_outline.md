# Chapter 10：OOP × Pandas 整合實戰

**模組：** M4 視覺化與整合實戰  
**時數：** 1.5 小時  
**前置知識：** Ch4–Ch9 全數  
**後續銜接：** 結業；並導引下一階段學習路徑

---

## 一、章節定位

本章是整門課的**收斂點**。要做的不是學新語法，而是**把前 9 章學到的東西組成一個可運行、可擴充的資料管線**。

最終產出：`DataCleaner` 類別，能自動完成「讀檔 → 驗證 → 清洗 → 特徵工程 → EDA → 匯出」。

---

## 二、學習目標

完成本章後，學生能夠：

1. 從零設計一個資料管線類別，明確定義職責邊界
2. 用 Method Chaining 寫出可讀性高的工作流
3. 用自訂 Exception 處理錯誤資料
4. 整合 Matplotlib 自動產出 EDA 圖表
5. 知道下一階段該學什麼

---

## 三、章節結構

### 10-1. 需求分析與類別設計（20 分鐘）
**情境**：每月收到一份原始銷售 CSV，需要清洗成乾淨資料表 + 一份 EDA 報表。

**設計討論**：
- 哪些是「狀態」（DataFrame 本身、檔案路徑）→ Instance Attribute
- 哪些是「動作」（讀、清、轉、畫、匯出）→ Method
- 哪些動作可以鏈式呼叫 → 回傳 `self`
- 哪些情況該 raise Exception → 自訂 `DataValidationError`

**類別介面草圖**：
```python
class DataCleaner:
    def __init__(self, data_path: str): ...
    def validate(self) -> 'DataCleaner': ...
    def clean_missing_values(self, strategy: str = 'drop') -> 'DataCleaner': ...
    def apply_custom_transform(self, column: str, func) -> 'DataCleaner': ...
    def generate_eda_report(self, out_path: str) -> 'DataCleaner': ...
    def export_data(self, out_path: str) -> 'DataCleaner': ...
```

### 10-2. 完整實作 Walkthrough（45 分鐘）

教學程式碼：

```python
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

class DataValidationError(Exception):
    """資料驗證失敗時拋出"""
    def __init__(self, column, reason):
        self.column = column
        self.reason = reason
        super().__init__(f"[{column}] {reason}")

class DataCleaner:
    def __init__(self, data_path: str):
        self.path = Path(data_path)
        if not self.path.exists():
            raise FileNotFoundError(f"找不到檔案：{self.path}")
        self.df = pd.read_csv(self.path)
        print(f"已載入 {self.path.name}，shape={self.df.shape}")
    
    def validate(self):
        if self.df.empty:
            raise DataValidationError('df', '資料為空')
        if 'revenue' in self.df.columns and (self.df['revenue'] < 0).any():
            raise DataValidationError('revenue', '出現負值')
        return self
    
    def clean_missing_values(self, strategy='drop'):
        if strategy == 'drop':
            self.df = self.df.dropna()
        elif strategy == 'mean':
            self.df = self.df.fillna(self.df.mean(numeric_only=True))
        return self
    
    def apply_custom_transform(self, column, func):
        if column not in self.df.columns:
            raise DataValidationError(column, '欄位不存在')
        self.df[f'{column}_transformed'] = self.df[column].apply(func)
        return self
    
    def generate_eda_report(self, out_path='eda.png'):
        numeric = self.df.select_dtypes(include='number')
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        # 視場景填充 4 張子圖
        for ax, col in zip(axes.flat, numeric.columns[:4]):
            ax.hist(numeric[col].dropna(), bins=30)
            ax.set_title(col)
        fig.tight_layout()
        fig.savefig(out_path, dpi=150)
        plt.close(fig)
        return self
    
    def export_data(self, out_path):
        self.df.to_csv(out_path, index=False)
        print(f"匯出 {len(self.df)} 列到 {out_path}")
        return self

# 使用：
(DataCleaner('raw.csv')
    .validate()
    .clean_missing_values(strategy='mean')
    .apply_custom_transform('revenue', lambda x: x * 1.05)
    .generate_eda_report('report.png')
    .export_data('clean.csv'))
```

**講解重點**：
- 每一行都對應前面某一章學的概念，逐行回顧
- 為何 `return self` 設計、為何用自訂 Exception
- 為何 `__init__` 直接讀檔（fail fast 原則）
- **可改進方向**（給學生練習）：加入 logging、加入 from-config、加入單元測試

### 10-3. 課程總結與下一步學習路徑（25 分鐘）

**已掌握的能力盤點**
- 系統直覺：OS、RAM、I/O 三個關鍵字
- Python 進階：Generator、Lambda、Comprehension
- OOP：類別設計、繼承、Method Chaining
- 資料工程：I/O、Exception、NumPy、Pandas
- 視覺化：Matplotlib EDA 工作流

**下一階段學習路徑（5 條）**

| 方向 | 推薦起點 | 1 句話 |
|------|---------|--------|
| 資料庫整合 | SQL × Python（SQLAlchemy） | 把 CSV 換成資料庫 |
| 機器學習 | scikit-learn 入門 | 把清洗好的資料餵給模型 |
| 大規模資料 | Polars、DuckDB | 當 Pandas 變慢時的下一站 |
| 自動化排程 | Airflow / Prefect / n8n | 讓你的管線每天自動跑 |
| 雲端部署 | AWS S3 + Lambda 或 GCP BigQuery | 把腳本搬上雲 |

**結業忠告（Linus 風格）**
1. 寫的程式跑得起來不算數，能讓三個月後的自己看懂才算數
2. 最強的優化是「不要做」—— 在向量化之前，先想能不能跳過這步
3. OOP 不是萬靈丹，30 行的腳本不需要類別

---

## 四、期末專案建議

挑一個真實資料集（Kaggle、政府開放資料、自己工作的資料），完成：
1. 設計一個專屬的 `XxxCleaner` 類別
2. 至少 5 個方法，支援 Method Chaining
3. 至少 1 個自訂 Exception
4. 自動產出至少 4 圖的 EDA 報表
5. 程式碼放上 GitHub，README 說明使用方式

---

## 五、課程結束

恭喜完成 18 小時的 **Python 進階數據工程與分析**。你已經具備了：
- 看懂進階開源程式碼的基礎
- 撰寫模組化、可重用資料處理腳本的能力
- 邁向 ML 工程師、資料工程師、資料分析師三條路線的共同底盤

下一站見。
