# S6 · Minimum Viable Knowledge（MVK）

> 若只記得 10 件事，這就是 S6（也是整個 12 小時課程的收斂版）。

---

## 六個 px 函式（一行畫一張）

1. `px.line(df, x, y)` — 時間序列主力。
2. `px.bar(df, x, y)` — 類別比較。
3. `px.scatter(df, x, y, color, size, trendline)` — 雙變數關聯。
4. `px.box(df, x, y, color)` — 分群分布。
5. `px.histogram(df, x, nbins)` — 單變數次數。
6. `px.pie(df, names, values, hole)` — 占比（類別 ≤ 5 才用）。

## make_subplots 骨架（必背）

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=["月營收", "品類", "散點", "占比"],
    specs=[[{"type": "xy"},     {"type": "xy"}],
           [{"type": "xy"},     {"type": "domain"}]],
)
fig.add_trace(go.Scatter(...), row=1, col=1)
fig.add_trace(go.Bar(...),     row=1, col=2)
fig.add_trace(go.Scatter(...), row=2, col=1)
fig.add_trace(go.Pie(...),     row=2, col=2)
fig.update_layout(height=800, title="Orders Dashboard")
fig.write_html("dashboard.html", include_plotlyjs="cdn")
```

## Capstone 五站 SOP

1. `load_and_clean_orders(path)` — 讀 CSV、`to_datetime(errors='coerce')`、`dropna`、型別轉換。
2. `merge` orders × products — 取得 category 等維度欄位。
3. `groupby` 月份 / 類別 — 聚合 revenue、qty、KPIs。
4. `make_subplots(2,2)` + `add_trace(go.*)` — 組 4 張子圖。
5. `fig.write_html(out_path)` — 絕對路徑、`include_plotlyjs='cdn'`。

## 三個必背踩雷

- **specs domain vs xy**：pie/sunburst 放 subplot 時 `specs` 必須 `{'type':'domain'}`，其他 `{'type':'xy'}`。
- **px 回傳 Figure**：`add_trace(px.bar(...))` 會錯；正確是 `add_trace(go.Bar(...))` 或 `add_trace(px.bar(...).data[0])`。
- **write_html 路徑**：永遠 `Path(out).absolute()`；`hover_data` 只挑 2~3 欄最有商業意義的，不要塞十欄。

## 成果發表三問（30 秒版）

1. 這份 dashboard 最關鍵的**發現**是什麼？（1 個數字 + 1 個解讀）
2. 再給你 1 小時，你會新增哪張圖？
3. 這個流程在你未來工作會**用在哪**？

## 評分 Rubric（內化）

| 面向 | 權重 | 達標關鍵 |
|---|---|---|
| 技術完成度 | 40% | dashboard.html 能開啟、4 張子圖都有資料 |
| 洞察品質 | 30% | 至少 1 個具體數字結論 |
| 視覺呈現 | 20% | subplot_titles、hover 有商業語意 |
| 口語表達 | 10% | 30 秒內講清發現 + 行動 |

---

## 課程總結：S1-S6 能力堆疊

| 層級 | 節次 | 核心能力 |
|---|---|---|
| 1. 向量化思維 | S1 | NumPy broadcasting / ufunc |
| 2. 資料入口 | S2 | Pandas IO、缺失值、dtype |
| 3. 資料塑形 | S3 | groupby / merge / pivot |
| 4. 時序與 EDA | S4 | datetime index、resample、EDA |
| 5. 視覺化語法 | S5 | matplotlib / seaborn 五種必懂圖 |
| 6. 互動 + 整合 | S6 | Plotly + make_subplots + dashboard.html |

**底層越穩、上層越能長**。你今天能把髒 CSV 變 dashboard，是因為前五週每一層都穩了。

---

## 下一步學習路徑（5 選 1，3 個月精讀）

| 方向 | 推薦起點 | 為什麼 |
|---|---|---|
| Web App 化 | **Streamlit** | 把 notebook 變成可點擊的 Web 表單，最快上線 |
| Plotly 官方生態 | **Dash** | 真正的 production-grade 儀表板框架 |
| 資料源升級 | **SQL + SQLAlchemy** | 把 CSV 換成資料庫，才是業界現實 |
| 雲端部署 | **AWS S3+Lambda / GCP BQ** | 讓管線每天自動跑、公開連結可分享 |
| 進階分析 | **scikit-learn** | 把清洗好的資料餵給模型，從描述性走向預測性 |

**Linus 忠告**：挑一條走完，比五條都碰過更值錢。

---

## 結業金句

> 「12 小時的終點，不是你會用 Plotly；是你能獨立把一份髒 CSV，變成老闆願意轉寄的 dashboard。這，才是 DA 的商業價值。」
