# Chapter 5：封裝、繼承與魔術方法

**模組：** M2 物件導向程式設計  
**時數：** 1.5 小時  
**前置知識：** Ch4 OOP 基礎  
**後續銜接：** Ch6（自訂 Exception）、Ch10（DataCleaner Method Chaining）

---

## 一、章節定位

Ch4 學會「定義類別」，本章學會「擴充與美化類別」。重點放在三件事：
1. **封裝**：哪些屬性外人不該動
2. **繼承**：用一個基礎類別衍生多個變體
3. **魔術方法**：讓類別像 Python 內建型別一樣自然

---

## 二、學習目標

完成本章後，學生能夠：

1. 用單底線 / 雙底線慣例表達封裝意圖
2. 寫出單一繼承，並覆寫父類別方法
3. 為類別實作 `__str__`、`__repr__`、`__len__`、`__iter__`
4. 設計支援 Method Chaining 的 API

---

## 三、章節結構

### 5-1. 封裝：哪些屬性外人不該動（25 分鐘）
- Python 沒有 `private` 關鍵字，靠**慣例**：
  - `_name`：弱封裝，提示「請勿外部存取」
  - `__name`：強封裝，name mangling 改名為 `_Class__name`
- `@property` 裝飾器：把屬性包裝成 getter/setter
  ```python
  class Temperature:
      def __init__(self, c):
          self._celsius = c
      
      @property
      def fahrenheit(self):
          return self._celsius * 9/5 + 32
  ```
- **為何重要**：日後使用者改動內部狀態會讓清洗管線錯亂

### 5-2. 單一繼承與方法覆寫（30 分鐘）
- 繼承語法：`class Child(Parent):`
- `super().__init__(...)` 呼叫父類別建構式
- 方法覆寫（override）：子類別重新定義同名方法
- **資料工程實例**：
  ```python
  class DataReader:
      def read(self, path): ...
  
  class CSVReader(DataReader):
      def read(self, path):  # 覆寫
          import pandas as pd
          return pd.read_csv(path)
  
  class JSONReader(DataReader):
      def read(self, path):
          import pandas as pd
          return pd.read_json(path)
  ```
- **本課程不教**：多重繼承、MRO、抽象基類（屬於進階課題）

### 5-3. 魔術方法（Magic Methods）（25 分鐘）
- 定義：以 `__` 包圍的特殊方法，由 Python 機制自動呼叫
- 必學四個：

| 方法 | 何時被呼叫 | 用途 |
|------|-----------|------|
| `__str__` | `print(obj)`、`str(obj)` | 給人看的字串 |
| `__repr__` | REPL 顯示、`repr(obj)` | 給開發者看的字串（最好可重建物件） |
| `__len__` | `len(obj)` | 長度 |
| `__iter__` | `for x in obj` | 讓物件可迭代 |

- 範例：給 `DataPipeline` 加上 `__str__` 顯示步驟數
- **預告 Ch6**：自訂 Exception 也是繼承 `Exception` 的類別

### 5-4. Method Chaining 設計（10 分鐘）
- 每個方法 `return self`，就能寫成：
  ```python
  cleaner.read('data.csv').drop_na().normalize().export('out.csv')
  ```
- 為什麼這種寫法可讀性高（資料流像句子）
- **預告 Ch10**：`DataCleaner` 將完整實作

---

## 四、課後練習

1. **設計題**：建立一個 `Animal` 基類別與 `Dog`、`Cat` 子類別，覆寫 `speak` 方法
2. **實作題**：替 Ch4 的 `DataPipeline` 加上 `__str__`、`__len__`，使 `print(pipe)` 與 `len(pipe)` 都有意義
3. **重構題**：把三個獨立函式 `clean`、`transform`、`export` 重構為支援 Method Chaining 的類別

---

## 五、銜接下一章

OOP 結束。Ch6 進入 M3 數據工程，先處理「**資料從哪裡來**」—— File I/O 與例外處理，並會回頭使用 Ch5 的繼承來自訂 Exception。
