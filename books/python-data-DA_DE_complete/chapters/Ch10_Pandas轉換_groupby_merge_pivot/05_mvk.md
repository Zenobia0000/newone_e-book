# S3 MVK（Must-Value-Keep）｜Pandas 轉換：groupby / merge / pivot

> 下課時學員腦中只能留下這頁。
> 格式：3 把刀 × 4 條紀律 × 3 段護身符程式碼。

---

## 🗡️ 三把刀（核心心智模型）

### 1. groupby = 思考模型 · Split → Apply → Combine
- **Split**：依分組鍵把資料切成多組
- **Apply**：每組套用聚合函式
- **Combine**：把結果拼回單一表
- 所有 groupby 題都套這三步 — 卡住先問：我在 split 什麼？

### 2. merge = 多表通行證 · on + how
- `on` 決定「用哪個鍵對齊」；欄名不一致用 `left_on / right_on`
- `how` 決定「誰留誰丟」；**90% 實務用 `how='left'`**
- 預設 `how='inner'` 會默默丟資料 — 別省

### 3. pivot_table = 交叉視角 · 四件套
- `index`（列）× `columns`（欄）× `values`（儲存格）× `aggfunc`（怎麼算）
- 想「行=A 列=B 值=m」的報表就用它
- 本質 = `groupby(多鍵).agg().unstack()`

---

## 📏 四條紀律（個人 checklist）

1. **多條件篩選一定括號**：`(df.a>0) & (df.b<10)` — 或直接用 `df.query()`。
2. **groupby 後要 merge / 畫圖，一律 `.reset_index()`** — MultiIndex 是隱形坑。
3. **merge 後第一件事：`assert len(merged) == len(left)`** — 多了 = 鍵重複、少了 = 沒 left join 到。
4. **pivot_table 永遠明確寫 `aggfunc`** — 預設是 `mean` 不是 `sum`，會算錯整張報表。

---

## 🛡️ 三段護身符程式碼（直接抄走）

### A. 具名聚合（推薦寫法）
```python
report = (df.groupby("region")
            .agg(total=("amount", "sum"),
                 cnt=("order_id", "count"),
                 avg_qty=("qty", "mean"))
            .reset_index())
```

### B. merge 三行護身符
```python
# 前：驗右表 key 唯一
assert customers["customer_id"].duplicated().sum() == 0
# 中：validate 讓 pandas 自己檢查關係
merged = orders.merge(customers, on="customer_id",
                      how="left", validate="m:1")
# 後：比對前後筆數
assert len(merged) == len(orders)
```

### C. pivot_table 四件套
```python
wide.pivot_table(
    index="region",
    columns="category",
    values="amount",
    aggfunc="sum",       # 永遠明確指定
    fill_value=0,
    margins=True,        # 加總行/列
)
```

---

## 🔗 對應到 Learning Objectives

| LO | 對應 slides | 關鍵工具 |
|----|------------|--------|
| LO1 條件篩選 | S3, S4 | between / isin / query / 括號 |
| LO2 groupby + agg | S5–S10 | Split-Apply-Combine · 具名聚合 |
| LO3 merge on / how | S12–S16 | left join · validate='m:1' |
| LO4 pivot_table | S17, S18, S20 | 四件套 · margins |
| LO5 三表綜合分析 | S16, S19, S21 | 鏈式 merge → groupby → pivot |

---

## ⏭️ 下一節銜接

**S4 時間序列與 EDA 實戰** — 把 S3 的 groupby / merge / pivot 產物，
變成時間軸上的趨勢線與視覺洞察。
