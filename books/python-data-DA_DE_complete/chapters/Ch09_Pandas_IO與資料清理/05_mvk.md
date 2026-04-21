# S2 · MVK 速學卡 — Pandas I/O 與資料清理

> Minimum Viable Knowledge：一張紙帶回家，覆蓋 90% 日常清理。
> 對應 teacher_notes §1 的 5 條 Learning Objectives。

---

## 🎯 五件事 SOP（對應 LO 2、Key Point 1）

拿到任何新 CSV，**先跑這五行**再做任何 query：

```python
df = pd.read_csv("orders_raw.csv", encoding="utf-8-sig")
df.shape              # 規模感
df.head()             # 長相
df.info()             # 型別 + 缺失
df.describe()         # 數值欄分佈
df.isna().sum()       # 缺值分佈
```

---

## 🧠 Pandas 三件套（LO 1）

| 概念 | 一句話 | 易錯點 |
|------|--------|--------|
| **Series** | 一維帶 Index 的陣列 | 與 NumPy array 差在 Index |
| **DataFrame** | 二維表，多 Series 共享 Index | 不是 dict 的樣子而已 |
| **Index** | 對齊與合併的「名字」 | ≠ 欄位、≠ row number |

---

## 🔑 loc vs iloc 四把鑰匙（LO 3、Key Point 3）

| 鑰匙 | 用途 | 切片行為 |
|------|------|---------|
| `df.loc[label]` | 用標籤／布林條件 | 包頭包尾（SQL 式） |
| `df.iloc[pos]` | 用整數位置 | 包頭不包尾（Python list 式） |
| `df[df.col > x]` | 布林遮罩 | 最 Pythonic |
| `df.query("col > @x")` | 字串條件 | 複雜邏輯首選 |

> ⚠️ **布林條件一定用 loc 不用 iloc**，不然直接 raise。

---

## 🛠️ 清理四大手法（LO 4、Key Point 2,4,5）

順序固定，不要亂：

1. **欄名標準化**
   `df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')`
2. **型別轉換（記得 `errors='coerce'`）**
   `df["date"] = pd.to_datetime(df["date"], errors="coerce")`
   `df["amount"] = pd.to_numeric(df["amount"].str.replace("$", "").str.replace(",", ""), errors="coerce")`
3. **缺值處理（依欄位意義）**
   - 訂單日期缺 → `dropna(subset=["date"])`
   - 金額缺 → `fillna(df["amount"].median())`
   - 類別缺 → `fillna("Unknown")`
4. **重複移除**
   `df = df.drop_duplicates(subset=["order_id"])`

---

## 📦 一次完成的 orders → orders_clean 七步（LO 5）

1. `read_csv` 指定 encoding
2. 五件事 SOP 盤點
3. 欄名標準化
4. 型別轉換（日期 / 金額）
5. 缺值處理（依欄位）
6. 去重
7. `to_csv("orders_clean.csv", index=False)`

---

## ☠️ 六個必記地雷

- `pd.to_datetime(df["date"])` 沒 `errors='coerce'` → 整批 raise
- `df["amount"].astype(float)` 碰到 `'$1,355'` 爆炸 → 先 `.str.replace`
- `df.iloc[df["age"]>18]` → IndexError，布林要用 `loc`
- `df.drop(..., inplace=True)` → 新版不建議，改賦值
- `df.append(other)` → 已 deprecated，改 `pd.concat([df, other])`
- `pd.read_csv(...)` 沒 encoding → 中文亂碼，Windows 用 `utf-8-sig`

---

## 🧪 自測三題

1. 說出『拿到新檔案的五件事』。
2. `df.loc[0:3]` 和 `df.iloc[0:3]` 在 index 被 `set_index("id")` 後差在哪？
3. 為什麼 `errors='coerce'` 是救命符、但也要小心？
