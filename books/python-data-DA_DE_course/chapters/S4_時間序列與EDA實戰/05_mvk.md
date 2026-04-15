# S4 MVK — 時間序列與 EDA 速查卡

## 四大工具一句話

| 工具 | 用途 | 一句話 |
|------|------|--------|
| `.dt` accessor | 拆年月日星期 | 向量化版 Excel 日期函式 |
| `resample` | 時間粒度轉換 | 需要 DatetimeIndex；D/W/ME 三種粒度 |
| `rolling` | 移動視窗 | 平滑雜訊、看趨勢；前 N-1 列 NaN |
| `corr` | 相關係數 | 只算數值欄；>0.7 強 / 0.3–0.7 中 / <0.3 弱 |

## 時序標準開場（4 行）

```python
df = pd.read_csv("orders.csv", parse_dates=["order_date"])
df = df.set_index("order_date").sort_index()
df["month"] = df.index.month
df["weekday"] = df.index.day_name()
```

## 月度經營報表模板

```python
monthly = (df.resample("ME")["amount"]
             .agg(revenue="sum", orders="count", aov="mean"))
monthly["mom_growth"] = monthly["revenue"].pct_change()
monthly.to_csv("monthly_revenue.csv")
```

## 陷阱對照表

| 症狀 | 原因 | 修法 |
|------|------|------|
| AttributeError: Can only use .dt accessor | 沒 parse_dates | `parse_dates=["order_date"]` |
| TypeError: Only valid with DatetimeIndex | 沒 set_index | `.set_index("order_date")` |
| 資料錯亂但不噴錯 | 沒 sort_index | `.sort_index()` |
| FutureWarning 'M' deprecation | pandas ≥ 2.2 | 改 `'ME'` / `'QE'` / `'YE'` |
| 星期變字母序 | groupby 後沒 reindex | `.reindex(week_order)` |

## 相關係數口語模板

「`amount` 與 `qty` 相關係數 0.78 → **強正相關**；客人買得多、金額也高，符合直覺。」

## 下一節銜接

S5：把這些報表數字畫成圖 — 折線、長條、散點、熱圖、盒鬚。
