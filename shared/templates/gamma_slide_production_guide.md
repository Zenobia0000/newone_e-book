# Gamma 投影片製作規範與控制指南

## 適用課程：2026 Python 數據分析與 AI 基礎（M0-M7）

---

## 一、為什麼需要這份規範

Gamma（gamma.app）是 AI 驅動的簡報生成工具，它的優勢是快速產出；弱點是**預設排版缺乏一致性**。如果不給明確的設計規範，生成的投影片會出現：字級跳動、字型不統一、色彩混亂、版面密度不一致。

本文件定義一套**可直接貼進 Gamma prompt 的排版規範**，確保 M0-M7 全部模組的投影片在視覺上維持專業一致。

---

## 二、品牌色彩系統（Brand Color Palette）

直接從 `book.yaml` 提取，用於所有投影片。

```
主色（背景/標題）
  Dark Navy:    #0D1B2A    ← 深色背景、模組封面
  Deep Blue:    #1B2838    ← 次要背景、程式碼區塊

強調色
  Accent Teal:  #00D4AA    ← 重點標記、圖表強調、連結
  Warm Orange:  #FF6B35    ← 警告、重要概念、CTA 按鈕

中性色
  Light Gray:   #F0F4F8    ← 淺色背景頁、表格隔行
  White:        #FFFFFF    ← 正文背景
  Text Dark:    #1A1A2E    ← 正文字色
  Text Light:   #6B7280    ← 次要說明文字
```

### Gamma Prompt 色彩指令

```
Use this exact color palette throughout all slides:
- Primary dark background: #0D1B2A
- Section headers: #1B2838
- Accent/highlight: #00D4AA (teal)
- Warning/emphasis: #FF6B35 (orange)
- Body text on light bg: #1A1A2E
- Subtle text: #6B7280
- Light background: #F0F4F8
- Code blocks: #1B2838 background with #F8F8F2 text
```

---

## 三、字型系統（Typography System）

### 指定字型

| 用途 | 字型 | 備選 | 說明 |
|------|------|------|------|
| 中文標題 | **Noto Sans TC Bold** | 思源黑體 Bold | Google Fonts 免費，繁體中文最佳選擇 |
| 中文正文 | **Noto Sans TC Regular** | 思源黑體 Regular | 同上 |
| 英文標題 | **Inter Bold** | Poppins Bold | 現代感無襯線，與 Noto Sans 搭配佳 |
| 英文正文 | **Inter Regular** | Poppins Regular | 同上 |
| 程式碼 | **Fira Code** | JetBrains Mono / Source Code Pro | 等寬字型，支援 ligatures |
| 金句/引言 | **Noto Serif TC** | 思源宋體 | 宋體增加權威感與視覺區隔 |

### Gamma Prompt 字型指令

```
Typography rules:
- Chinese text: "Noto Sans TC" (Google Fonts)
- English text: "Inter" (Google Fonts)  
- Code blocks: "Fira Code" monospace
- Quotes/citations: "Noto Serif TC" italic
- Never use default system fonts
- Never mix more than 3 font families per slide
```

---

## 四、字級系統（Font Size Hierarchy）

### 標準字級表

| 層級 | 元素 | 字級 | 字重 | 行高 | 用途 |
|------|------|------|------|------|------|
| H0 | 模組封面標題 | 48px | Bold | 1.2 | 每個模組第一張 |
| H1 | 段落大標題 | 36px | Bold | 1.3 | 每個投影片主標題 |
| H2 | 副標題 | 24px | SemiBold | 1.4 | 投影片副標題 |
| H3 | 小標題 | 20px | SemiBold | 1.4 | 表格/區塊標題 |
| Body | 正文 | 18px | Regular | 1.6 | 講師要點、說明文字 |
| Small | 次要文字 | 14px | Regular | 1.5 | 來源標注、頁腳 |
| Code | 程式碼 | 16px | Regular | 1.4 | 程式碼區塊 |
| Quote | 金句 | 22px | Italic | 1.5 | 高層視角頁引言 |
| Data | 大數字 | 64px | Bold | 1.0 | 統計數據展示 |

### Gamma Prompt 字級指令

```
Font size rules (strict):
- Module cover title: 48px bold
- Slide title (H1): 36px bold
- Subtitle (H2): 24px semibold
- Body text: 18px regular, line-height 1.6
- Code blocks: 16px monospace on dark background
- Source citations: 14px light gray (#6B7280)
- Feature numbers/stats: 64px bold accent color (#00D4AA)
- Quotes: 22px italic serif font
- Never go below 14px on any text
- Never go above 48px except for hero numbers
```

---

## 五、投影片版型系統（Slide Layout Templates）

### Template A：模組封面頁

```
用途：每個模組的第一張投影片
背景：#0D1B2A（深色全滿）
佈局：
  ┌─────────────────────────────┐
  │                             │
  │   [模組編號] M0              │  ← 14px, #00D4AA
  │                             │
  │   為什麼是 Python            │  ← 48px, White, Bold
  │   為什麼是現在               │
  │                             │
  │   3 小時 | 含工作坊 60 分鐘    │  ← 16px, #6B7280
  │                             │
  │   ─── #00D4AA 細線 ───       │
  │                             │
  │   桑尼資料科學 | Data Sunnie  │  ← 14px, White
  │                             │
  └─────────────────────────────┘
```

### Template B：內容教學頁（最常用）

```
用途：講師要點 + 視覺輔助
背景：#FFFFFF
佈局：
  ┌─────────────────────────────┐
  │ [H1] 投影片標題         M0-S02│  ← 標題左對齊，頁碼右上
  │ ─── #00D4AA 底線 ───         │
  │                             │
  │  左欄 (60%)    │  右欄 (40%) │
  │  ・要點一       │  [圖表/   │
  │  ・要點二       │   視覺化]  │
  │  ・要點三       │            │
  │  ・要點四       │            │
  │                             │
  │ 來源：XXX Survey 2024    p.2 │  ← 14px, #6B7280
  └─────────────────────────────┘

規則：
- 左欄文字不超過 4-5 個要點
- 每個要點不超過 2 行
- 右欄放圖表、流程圖或示意圖
- 底部固定放來源標注
```

### Template C：程式碼展示頁

```
用途：Python 程式碼示範
背景：#FFFFFF，程式碼區塊 #1B2838
佈局：
  ┌─────────────────────────────┐
  │ [H1] 投影片標題              │
  │ [H2] 一句話說明這段 code 做什麼│
  │                             │
  │ ┌─── #1B2838 ────────────┐  │
  │ │ # Comment in English    │  │  ← Fira Code 16px
  │ │ import pandas as pd     │  │    #F8F8F2 on dark
  │ │ df = pd.read_csv(...)   │  │
  │ │ print(df.head())        │  │
  │ └─────────────────────────┘  │
  │                             │
  │ 💡 關鍵觀念：xxx             │  ← 18px, #FF6B35 icon
  └─────────────────────────────┘

規則：
- 程式碼不超過 10 行
- 超過 10 行要拆成多張投影片
- 程式碼上方必須有一行中文說明
- 程式碼下方放一行「關鍵觀念」takeaway
```

### Template D：高層視角頁（金句頁）

```
用途：章節開場、情緒轉折、核心主張
背景：#0D1B2A 或漸層
佈局：
  ┌─────────────────────────────┐
  │                             │
  │                             │
  │   "Statistics turns         │  ← 28px, Noto Serif TC
  │    observations into        │     Italic, White
  │    confidence."             │
  │                             │
  │              ─── #00D4AA ── │
  │                             │
  │                             │
  └─────────────────────────────┘

規則：
- 整張投影片只有一句話
- 置中對齊
- 無其他元素干擾
- 每個模組至少 1 張，不超過 2 張
```

### Template E：數據展示頁

```
用途：產業調查數據、效能對比
背景：#FFFFFF
佈局：
  ┌─────────────────────────────┐
  │ [H1] 標題                   │
  │                             │
  │   ┌──────┐  ┌──────┐       │
  │   │ 60%  │  │ 43%  │       │  ← 64px, #00D4AA
  │   │時間花在│  │加速幅度│       │  ← 16px, #6B7280
  │   │資料清理│  │PyTorch│       │
  │   └──────┘  └──────┘       │
  │                             │
  │ 來源：CrowdFlower 2016      │  ← 14px, #6B7280
  │        PyTorch Official '23 │
  └─────────────────────────────┘

規則：
- 大數字用 64px Bold + 強調色
- 數字下方用 16px 說明上下文
- 底部必須標注資料來源（authority）
```

### Template F：表格頁

```
用途：比較表、清單、框架對照
背景：#FFFFFF
佈局：
  ┌─────────────────────────────┐
  │ [H1] 標題                   │
  │                             │
  │ ┌──────┬──────┬──────────┐  │
  │ │ 標頭 │ 標頭 │ 標頭     │  │  ← #0D1B2A bg, White text
  │ ├──────┼──────┼──────────┤  │
  │ │ 內容 │ 內容 │ 內容     │  │  ← 16px, #1A1A2E
  │ │ 內容 │ 內容 │ 內容     │  │     隔行 #F0F4F8
  │ │ 內容 │ 內容 │ 內容     │  │
  │ └──────┴──────┴──────────┘  │
  │                             │
  └─────────────────────────────┘

規則：
- 表頭深色背景白字
- 表格不超過 5 欄
- 行數不超過 7 行（超過要拆頁）
- 隔行用 #F0F4F8 增加可讀性
```

### Template W：工作坊頁

```
用途：實作練習說明
背景：#F0F4F8（淺灰，區別於教學頁）
左邊框：4px #FF6B35 橘色邊條
佈局：
  ┌─────────────────────────────┐
  │ 🔧 工作坊 A：[練習名稱]      │  ← H2, #FF6B35
  │ ─── 時間：25 分鐘 ───        │
  │                             │
  │ 任務說明：                   │  ← Body
  │ 1. 第一步 ...                │
  │ 2. 第二步 ...                │
  │ 3. 第三步 ...                │
  │                             │
  │ 驗收標準：                   │  ← H3, #00D4AA
  │ ☑ 標準一                    │
  │ ☑ 標準二                    │
  └─────────────────────────────┘
```

---

## 六、間距與對齊規則（Spacing & Alignment）

```
投影片邊距（Slide Padding）：
  上下左右：48px（Gamma 預設偏窄，手動調大）

元素間距：
  標題 → 正文：24px
  要點 → 要點：12px
  正文 → 程式碼區塊：16px
  程式碼區塊 → 正文：16px
  圖表 → 說明文字：8px

對齊規則：
  - 標題：左對齊（永遠不要置中，除了金句頁）
  - 正文：左對齊
  - 程式碼：左對齊，等寬字型
  - 表格：左對齊，數字右對齊
  - 金句：水平垂直置中
  - 圖表：水平置中
```

---

## 七、每個模組的投影片數量估算

| 模組 | 教學頁 | 金句頁 | 程式碼頁 | 表格頁 | 工作坊頁 | 總計 |
|------|--------|--------|----------|--------|----------|------|
| M0 | 6 | 2 | 1 | 2 | 4 | ~15 |
| M1 | 8 | 1 | 2 | 2 | 3 | ~16 |
| M2 | 6 | 1 | 6 | 2 | 3 | ~18 |
| M3 | 7 | 1 | 5 | 2 | 3 | ~18 |
| M4 | 7 | 1 | 6 | 3 | 3 | ~20 |
| M5 | 8 | 1 | 4 | 3 | 2 | ~18 |
| M6 | 8 | 1 | 4 | 3 | 3 | ~19 |
| M7 | 8 | 1 | 3 | 3 | 2 | ~17 |
| **合計** | | | | | | **~141** |

---

## 八、Gamma Prompt 模板（可直接貼入）

### 初始化 Prompt（建立新簡報時使用）

以下是完整的 Gamma system prompt，建立新簡報時一次性貼入：

```
You are creating a professional course presentation for a 24-hour Python data analysis course. Follow these STRICT design rules:

=== BRAND IDENTITY ===
Course: "2026 Python 數據分析與 AI 基礎"
Author: 桑尼資料科學 | Data Sunnie
Language: Traditional Chinese (繁體中文) for all content
English only for: code, technical terms, quotes

=== COLOR PALETTE (MANDATORY) ===
- Dark background: #0D1B2A
- Section bg: #1B2838
- Accent teal: #00D4AA (highlights, links, numbers)
- Warning orange: #FF6B35 (workshops, important notes)
- Body text: #1A1A2E on white background
- Subtle text: #6B7280
- Light bg: #F0F4F8
- Code block: #1B2838 bg with #F8F8F2 text

=== TYPOGRAPHY (MANDATORY) ===
- Chinese: Noto Sans TC (Bold for titles, Regular for body)
- English: Inter (Bold for titles, Regular for body)
- Code: Fira Code monospace, 16px
- Quotes: Noto Serif TC italic

=== FONT SIZES (STRICT) ===
- Module cover title: 48px bold
- Slide title: 36px bold
- Subtitle: 24px semibold
- Body: 18px regular, line-height 1.6
- Code: 16px monospace
- Citations/footer: 14px #6B7280
- Hero numbers: 64px bold #00D4AA
- Quotes: 22px italic

=== LAYOUT RULES ===
- Slide padding: 48px all sides
- Title always left-aligned (except quote slides)
- Maximum 5 bullet points per slide
- Maximum 2 lines per bullet point
- Code blocks max 10 lines (split if longer)
- Tables max 5 columns, 7 rows
- Every data claim must show source in 14px footer

=== SLIDE TYPES ===
1. MODULE COVER: Dark bg #0D1B2A, module number in teal, title white 48px
2. CONTENT: White bg, left 60% text + right 40% visual, source footer
3. CODE: White bg, dark code block, one-line Chinese explanation above
4. QUOTE: Dark bg, single centered quote in serif italic, no other elements
5. DATA: White bg, large numbers 64px teal, source citation required
6. TABLE: White bg, dark header row, alternating row colors
7. WORKSHOP: Light gray bg #F0F4F8, orange left border, task + criteria

=== SLIDE STRUCTURE PER MODULE ===
- Slide 1: Module cover (Template A)
- Slide 2: Learning objectives (Template F, table format)
- Slides 3-N: Content slides (Templates B/C/E/F)
- 1 Quote slide per module (Template D)
- Workshop slides at 60% mark and end (Template W)
- Final slide: Module summary + next module preview
```

### 逐模組 Prompt（每次生成一個模組時使用）

```
Create slides for Module [X]: [模組標題]

Source material: [貼入對應模組 .md 檔案內容]

Requirements:
1. Follow the design system established above
2. Each slide from the outline table = one Gamma slide
3. Use the "講師講解要點" as bullet points (max 4-5 per slide)
4. Use the "視覺建議" to design the right-side visual
5. Use the "轉場" text as presenter notes
6. Code examples go on dedicated code slides (Template C)
7. Every statistic must show its source in the footer
8. Workshop exercises use Template W with orange accent

Generate exactly [N] slides for this module.
```

---

## 九、品質檢查清單（QA Checklist）

每個模組的投影片生成後，逐項檢查：

### 字型與字級
- [ ] 所有中文使用 Noto Sans TC，無系統預設字型
- [ ] 標題 36px、正文 18px、程式碼 16px，無例外
- [ ] 金句頁使用 Noto Serif TC（宋體/襯線）
- [ ] 無小於 14px 的文字出現

### 色彩
- [ ] 深色背景只用 #0D1B2A 或 #1B2838
- [ ] 強調色只用 #00D4AA（teal）和 #FF6B35（orange）
- [ ] 正文字色 #1A1A2E，無純黑 #000000
- [ ] 程式碼區塊 #1B2838 背景 + #F8F8F2 文字

### 排版
- [ ] 每頁不超過 5 個要點
- [ ] 每個要點不超過 2 行
- [ ] 程式碼不超過 10 行/頁
- [ ] 表格不超過 5 欄 x 7 行
- [ ] 標題左對齊（金句頁例外）

### 內容
- [ ] 每個數據宣稱底部有來源標注（14px 灰色）
- [ ] 每個模組有 1 張金句頁
- [ ] 每個模組第一張是深色封面頁
- [ ] 工作坊頁用淺灰背景 + 橘色邊條區隔

### 一致性
- [ ] 頁碼格式統一（右上角，格式：M0-S02）
- [ ] 模組間色彩和字型完全一致
- [ ] 所有投影片邊距一致（48px）

---

## 十、Gamma 操作技巧

### 1. 如何在 Gamma 中強制字型

Gamma 的 AI 生成模式可能忽略字型指定。手動修正方式：
- 進入「Theme」設定，把 Heading font 改為 Noto Sans TC
- 把 Body font 改為 Noto Sans TC
- 在「Custom CSS」（Pro 功能）中注入：
```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;600;700&family=Inter:wght@400;600;700&family=Fira+Code:wght@400&family=Noto+Serif+TC:wght@400;700&display=swap');
```

### 2. 如何控制字級

Gamma 不直接支援 px 指定，但可以透過：
- **Heading 1** → 對應 H1（36px）
- **Heading 2** → 對應 H2（24px）
- **Heading 3** → 對應 H3（20px）
- **Normal text** → 對應 Body（18px）
- **Small text** → 對應 Small（14px）
- 在 Theme 設定中調整 base font size

### 3. 如何確保色彩一致

在 Gamma Theme 設定中：
- Primary color → #0D1B2A
- Accent color → #00D4AA
- 在生成後手動檢查，把任何偏離的色彩修正回品牌色

### 4. 建議的工作流程

```
1. 在 Gamma 中建立新 Presentation
2. 貼入「初始化 Prompt」設定設計系統
3. 進入 Theme 手動設定字型和色彩
4. 逐模組貼入「逐模組 Prompt」+ 模組 .md 內容
5. 生成後用 QA Checklist 逐項檢查
6. 手動修正不符合規範的元素
7. 匯出 PDF 前再做一次全面檢查
```

---

## 十一、附錄：課程模組金句速查

每個模組必須有至少一張金句頁，使用以下金句：

| 模組 | 金句 | 出處 |
|------|------|------|
| M0 | "Data is the raw material; Python is the operating language." | 課程原創 |
| M1 | "The goal is not to collect data. The goal is to collect the right data." | 課程原創 |
| M2 | "Code is a tool for thinking, not just for computing." | 課程原創 |
| M3 | "Don't loop. Vectorize." | NumPy 社群格言 |
| M4 | "Garbage in, garbage out." | 資料科學經典格言 |
| M5 | "The greatest value of a picture is when it forces us to notice what we never expected to see." | Tukey, 1977 |
| M6 | "Statistics turns observations into confidence." | 課程原創 |
| M7 | "Machine learning turns patterns into prediction." | 課程原創 |
