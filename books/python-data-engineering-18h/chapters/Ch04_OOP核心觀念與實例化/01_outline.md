# Chapter 4：OOP 核心觀念與實例化

**模組：** M2 物件導向程式設計  
**時數：** 1.5 小時  
**前置知識：** Ch3 函式  
**後續銜接：** Ch5（封裝/繼承/魔術方法）、Ch10（DataCleaner 整合）

---

## 一、章節定位

OOP 在資料工程中的價值不是「炫技」，而是：
- **可重用**：清洗邏輯寫一次，套到 N 個資料集
- **可測試**：小單元獨立驗證
- **降低耦合**：管線中各步驟可獨立替換

本章不講設計模式、不講多重繼承，只講「**為什麼要從腳本升級為類別**」與最基本的實例化機制。

---

## 二、學習目標

完成本章後，學生能夠：

1. 解釋 Class 與 Object 的差異（藍圖 vs 實體）
2. 寫出第一個 `class`，正確使用 `__init__` 與 `self`
3. 區分 Class Attribute 與 Instance Attribute
4. 在腳本式程式與類別式程式之間，選對使用時機

---

## 三、章節結構

### 4-1. 為什麼資料工程需要 OOP（20 分鐘）
- 對照組：「100 行寫 5 個函式管理 10 個全域變數」vs「100 行 1 個類別封裝狀態」
- 三大效益：可重用、可測試、可組合
- **反例**：什麼時候**不**該用 OOP（一次性腳本、單純函式式轉換）
- **Linus 觀點**：「If you need OOP for hello world, you've already lost.」—— 但資料管線值得

### 4-2. Class 與 Object 的本質（30 分鐘）
- **比喻**：Class 是建築藍圖，Object 是蓋出來的房子
- 最小範例：
  ```python
  class DataPipeline:
      def __init__(self, name):
          self.name = name
          self.steps = []
      
      def add_step(self, step):
          self.steps.append(step)
  
  pipe = DataPipeline("ETL_v1")
  pipe.add_step("read_csv")
  ```
- `__init__` 的角色：實例化時自動執行
- `self` 是什麼：當前物件的引用
- **記憶體模型**：兩個 `DataPipeline` 實例各自獨立的 `steps`

### 4-3. Class Attribute vs Instance Attribute（25 分鐘）
- Class Attribute：所有實例共享
- Instance Attribute：每個實例獨立
- **常見陷阱**：把可變物件（list/dict）當 Class Attribute
  ```python
  class Bad:
      data = []          # 所有實例共享同一 list！
  
  class Good:
      def __init__(self):
          self.data = []  # 每個實例獨立
  ```
- 何時刻意用 Class Attribute（常數、計數器）

### 4-4. 範例實作：DataPipeline 雛形（15 分鐘）
- 設計一個只有 `__init__` 與 `add_step` 的 `DataPipeline`
- 預告：Ch5 將加入繼承與魔術方法，Ch10 將擴充為完整 `DataCleaner`

---

## 四、課後練習

1. **觀念題**：解釋為何 `class Foo: items = []` 是常見錯誤
2. **實作題**：寫一個 `Student` 類別，包含姓名、成績 list、平均分數方法
3. **重構題**：給定一段 100 行的腳本（讀檔→清洗→輸出），重構為一個類別

---

## 五、銜接下一章

學會了「定義一個類別」，Ch5 將學習「擴充與美化類別」—— 封裝、繼承、魔術方法，並引入 Method Chaining 設計，為 Ch10 的 `cleaner.read().clean().export()` 寫法鋪路。
