# Gamma 投影片製作規範與控制指南

## 適用課程：2026 Python 數據分析與 AI 基礎（M0-M7）
## 品牌：Sunny DataScience（色系版本 2026-03-16）

---

## 一、為什麼需要這份規範

Gamma（gamma.app）是 AI 驅動的簡報生成工具，它的優勢是快速產出；弱點是**預設排版缺乏一致性**。如果不給明確的設計規範，生成的投影片會出現：字級跳動、字型不統一、色彩混亂、版面密度不一致。

本文件定義一套**可直接貼進 Gamma prompt 的排版規範**，確保 M0-M7 全部模組的投影片在視覺上維持專業一致。

---

## 二、品牌色彩系統（Sunny DataScience Official）

### 核心品牌三色

| 角色 | HEX | RGB | 用途 |
|------|------|-----|------|
| **Primary Teal** | `#2C918C` | `44, 145, 140` | CTA 按鈕、標題重點、連結、圖表主色、大數字強調 |
| **Accent Purple** | `#A855F7` | `168, 85, 247` | 次要強調、標籤、裝飾元素、工作坊標記 |
| **Featured Red** | `#BA4D43` | `186, 77, 67` | 分隔線、精選標記、editorial 紅線 |

### 品牌延伸色

| 角色 | HEX | 用途 |
|------|------|------|
| **Navy 深藍** | `#1E3A5F` | 副品牌色、淺色簡報標題色 |
| Teal Hover | `#1A5C59` | 按鈕 hover、深色變化 |
| Teal Light | `hsl(186,94%,82%)` | badge 背景、淡色裝飾 |
| Purple Light | `#F3E8FF` | 淡紫背景、工作坊區塊 |
| Navy Light | `#DBEAFE` | 淡藍背景 |

### 背景與表面

**深色風格（科技感，推薦用於封面/金句/程式碼頁）：**

| 角色 | HEX | 用途 |
|------|------|------|
| **Background** | `#050505` | 頁面主背景、模組封面 |
| **Surface** | `#0F0F0F` | 卡片背景、程式碼區塊 |
| **Hero Teal** | `#0F2D2B` | Hero 漸層終點 |
| **Header** | `#152032` | 表頭背景 |

**淺色風格（正式場合，用於教學/表格/數據頁）：**

| 角色 | HEX | 用途 |
|------|------|------|
| **Background** | `#FFFFFF` | 正文背景 |
| **Elevated** | `#F9FAFB` | 卡片、區塊背景、工作坊頁 |
| **Muted** | `#FAFBFC` | 表格隔行 |

### 文字色

| 角色 | HEX | 用途 |
|------|------|------|
| **深底白字** | `#FFFFFF` | 深色背景上的標題與內文 |
| **淺底主文字** | `#151B28` | 淺色背景上的標題與內文 |
| **副文字** | `#6B7280` | 說明文字、日期、來源標注 |
| **淡文字** | `#9CA3AF` | placeholder、disabled |

### 狀態 / 語意色

| 語意 | HEX | 淡色背景 | 用途 |
|------|------|---------|------|
| **Success** | `#10B981` | `#ECFDF5` | 完成、成長 |
| **Warning** | `#F59E0B` | `#FFFBEB` | 警告、注意事項 |
| **Error** | `#EF4444` | `#FEF2F2` | 錯誤、風險、反模式 |
| **Info** | `#3B82F6` | `#EFF6FF` | 資訊提示、補充說明 |

### 圖表色板（依序使用）

```
#2C918C  #A855F7  #F59E0B  #3B82F6  #EF4444  #10B981  #EC4899  #8B5CF6
Teal     Purple   Amber    Blue     Red      Green    Pink     Violet
```

### 漸層

| 名稱 | 色碼 | 用途 |
|------|------|------|
| **Hero** | `#050505 -> #0A1A19 -> #0F2D2B` (135deg) | 模組封面漸層 |
| **Solutions** | `#050505 -> #0F2D2B` (180deg) | 金句頁漸層 |

### Gamma Prompt 色彩指令

```
Use the Sunny DataScience brand color palette throughout all slides:

=== CORE BRAND COLORS ===
- Primary Teal: #2C918C (CTA, highlights, links, hero numbers, chart primary)
- Accent Purple: #A855F7 (secondary accent, tags, workshop markers)
- Featured Red: #BA4D43 (dividers, editorial lines, selected highlights)
- Navy: #1E3A5F (subtitle color on light backgrounds)

=== BACKGROUNDS ===
- Dark slide bg: #050505 (module covers, quote slides)
- Dark surface/code blocks: #0F0F0F
- Dark gradient: #050505 → #0F2D2B (hero gradient, 135deg)
- Table header bg: #152032
- Light slide bg: #FFFFFF (content slides)
- Light elevated bg: #F9FAFB (workshop slides, card backgrounds)
- Light muted: #FAFBFC (table alternating rows)

=== TEXT ===
- Text on dark bg: #FFFFFF
- Text on light bg: #151B28
- Secondary/subtle text: #6B7280
- Disabled text: #9CA3AF

=== STATUS COLORS (for callouts) ===
- Success: #10B981 on #ECFDF5
- Warning: #F59E0B on #FFFBEB
- Error: #EF4444 on #FEF2F2
- Info: #3B82F6 on #EFF6FF

=== CHART PALETTE (in order) ===
#2C918C, #A855F7, #F59E0B, #3B82F6, #EF4444, #10B981, #EC4899, #8B5CF6
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
- Code blocks: 16px monospace on dark background (#0F0F0F)
- Source citations: 14px secondary text (#6B7280)
- Feature numbers/stats: 64px bold Primary Teal (#2C918C)
- Quotes: 22px italic serif font
- Never go below 14px on any text
- Never go above 48px except for hero numbers
```

---

## 五、投影片版型系統（Slide Layout Templates）

### Template A：模組封面頁

```
用途：每個模組的第一張投影片
背景：#050505 → #0F2D2B 漸層（135deg）
佈局：
  ┌─────────────────────────────┐
  │                             │
  │   [模組編號] M0              │  ← 14px, #2C918C (Primary Teal)
  │                             │
  │   為什麼是 Python            │  ← 48px, #FFFFFF, Bold
  │   為什麼是現在               │
  │                             │
  │   3 小時 | 含工作坊 60 分鐘    │  ← 16px, #6B7280
  │                             │
  │   ─── #BA4D43 細線 ───       │  ← Featured Red 分隔線
  │                             │
  │   桑尼資料科學 | Data Sunnie  │  ← 14px, #9CA3AF
  │                             │
  └─────────────────────────────┘
```

### Template B：內容教學頁（最常用）

```
用途：講師要點 + 視覺輔助
背景：#FFFFFF
佈局：
  ┌─────────────────────────────┐
  │ [H1] 投影片標題         M0-S02│  ← #151B28 標題左對齊，頁碼右上
  │ ─── #2C918C 底線 ───         │  ← Primary Teal 底線
  │                             │
  │  左欄 (60%)    │  右欄 (40%) │
  │  ・要點一       │  [圖表/   │  ← #151B28 正文
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
背景：#FFFFFF，程式碼區塊 #0F0F0F
佈局：
  ┌─────────────────────────────┐
  │ [H1] 投影片標題              │  ← #151B28
  │ [H2] 一句話說明這段 code 做什麼│  ← #1E3A5F (Navy)
  │                             │
  │ ┌─── #0F0F0F ────────────┐  │
  │ │ # Comment in English    │  │  ← Fira Code 16px
  │ │ import pandas as pd     │  │    #F8F8F2 on dark
  │ │ df = pd.read_csv(...)   │  │    關鍵字用 #2C918C 高亮
  │ │ print(df.head())        │  │
  │ └─────────────────────────┘  │
  │                             │
  │ 💡 關鍵觀念：xxx             │  ← 18px, #A855F7 (Accent Purple)
  └─────────────────────────────┘

規則：
- 程式碼不超過 10 行
- 超過 10 行要拆成多張投影片
- 程式碼上方必須有一行中文說明
- 程式碼下方放一行「關鍵觀念」takeaway
- 程式碼區塊圓角 8px
```

### Template D：高層視角頁（金句頁）

```
用途：章節開場、情緒轉折、核心主張
背景：#050505 → #0F2D2B 漸層
佈局：
  ┌─────────────────────────────┐
  │                             │
  │                             │
  │   "Statistics turns         │  ← 22px, Noto Serif TC
  │    observations into        │     Italic, #FFFFFF
  │    confidence."             │
  │                             │
  │              ─── #BA4D43 ── │  ← Featured Red 底線
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
  │ [H1] 標題                   │  ← #151B28
  │                             │
  │   ┌──────┐  ┌──────┐       │
  │   │ 60%  │  │ 43%  │       │  ← 64px, Bold, #2C918C
  │   │時間花在│  │加速幅度│       │  ← 16px, #6B7280
  │   │資料清理│  │PyTorch│       │
  │   └──────┘  └──────┘       │
  │                             │
  │ 來源：CrowdFlower 2016      │  ← 14px, #6B7280
  │        PyTorch Official '23 │
  └─────────────────────────────┘

規則：
- 大數字用 64px Bold + Primary Teal (#2C918C)
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
  │ │ 標頭 │ 標頭 │ 標頭     │  │  ← #152032 bg, #FFFFFF text
  │ ├──────┼──────┼──────────┤  │
  │ │ 內容 │ 內容 │ 內容     │  │  ← 16px, #151B28
  │ │ 內容 │ 內容 │ 內容     │  │     隔行 #FAFBFC
  │ │ 內容 │ 內容 │ 內容     │  │
  │ └──────┴──────┴──────────┘  │
  │                             │
  └─────────────────────────────┘

規則：
- 表頭 #152032 背景白字
- 表格不超過 5 欄
- 行數不超過 7 行（超過要拆頁）
- 隔行用 #FAFBFC 增加可讀性
```

### Template W：工作坊頁

```
用途：實作練習說明
背景：#F9FAFB（Elevated，區別於教學頁）
左邊框：4px #A855F7（Accent Purple）邊條
佈局：
  ┌─────────────────────────────┐
  │ 🔧 工作坊 A：[練習名稱]      │  ← H2, #A855F7 (Accent Purple)
  │ ─── 時間：25 分鐘 ───        │  ← #6B7280
  │                             │
  │ 任務說明：                   │  ← Body, #151B28
  │ 1. 第一步 ...                │
  │ 2. 第二步 ...                │
  │ 3. 第三步 ...                │
  │                             │
  │ 驗收標準：                   │  ← H3, #2C918C (Primary Teal)
  │ ☑ 標準一                    │
  │ ☑ 標準二                    │
  └─────────────────────────────┘
```

### Template INFO：資訊提示卡

```
用途：補充說明、注意事項、里程碑
佈局選項（依語意色選擇）：

  Info 類：  #EFF6FF 背景 + #3B82F6 左邊條 + 💡 圖示
  Warning 類：#FFFBEB 背景 + #F59E0B 左邊條 + ⚠️ 圖示
  Success 類：#ECFDF5 背景 + #10B981 左邊條 + ✅ 圖示
  Error 類：  #FEF2F2 背景 + #EF4444 左邊條 + ❌ 圖示
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

邊框：
  - 淺色模式邊框：#E5E7EB
  - 深色模式邊框：rgba(255,255,255, 0.1)
  - 強調邊框：#2C918C 30% alpha
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
You are creating a professional course presentation for a 24-hour Python data analysis course by Sunny DataScience. Follow these STRICT design rules:

=== BRAND IDENTITY ===
Brand: Sunny DataScience | 桑尼資料科學
Course: "2026 Python 數據分析與 AI 基礎"
Author: 桑尼資料科學 | Data Sunnie
Language: Traditional Chinese (繁體中文) for all content
English only for: code, technical terms, quotes

=== COLOR PALETTE — Sunny DataScience Official (MANDATORY) ===

Core brand colors:
- Primary Teal: #2C918C (CTA, highlights, links, hero numbers, chart primary)
- Accent Purple: #A855F7 (secondary accent, tags, workshop markers, key takeaways)
- Featured Red: #BA4D43 (divider lines, editorial accent)
- Navy: #1E3A5F (subtitles on light backgrounds)

Dark backgrounds:
- Dark bg: #050505 (module covers, quote slides)
- Surface/code blocks: #0F0F0F
- Hero gradient: #050505 → #0F2D2B (135deg)
- Table header: #152032

Light backgrounds:
- Main bg: #FFFFFF (content slides)
- Elevated: #F9FAFB (workshop slides, cards)
- Alternating rows: #FAFBFC

Text:
- On dark: #FFFFFF
- On light: #151B28
- Secondary: #6B7280
- Tertiary: #9CA3AF

Status callouts:
- Info: #3B82F6 on #EFF6FF
- Warning: #F59E0B on #FFFBEB
- Success: #10B981 on #ECFDF5
- Error: #EF4444 on #FEF2F2

Chart palette (in order): #2C918C, #A855F7, #F59E0B, #3B82F6, #EF4444, #10B981, #EC4899, #8B5CF6

=== TYPOGRAPHY (MANDATORY) ===
- Chinese: Noto Sans TC (Bold for titles, Regular for body)
- English: Inter (Bold for titles, Regular for body)
- Code: Fira Code monospace, 16px, on #0F0F0F background
- Quotes: Noto Serif TC italic

=== FONT SIZES (STRICT) ===
- Module cover title: 48px bold, white on dark gradient
- Slide title (H1): 36px bold, #151B28
- Subtitle (H2): 24px semibold, #1E3A5F (Navy)
- Body text: 18px regular, #151B28, line-height 1.6
- Code blocks: 16px Fira Code, #F8F8F2 on #0F0F0F
- Source citations/footer: 14px #6B7280
- Hero numbers/stats: 64px bold #2C918C (Primary Teal)
- Quotes: 22px Noto Serif TC italic, white on dark
- Never go below 14px on any text
- Never go above 48px except for hero numbers (64px)

=== LAYOUT RULES ===
- Slide padding: 48px all sides
- Title always left-aligned (except quote slides which are centered)
- Maximum 5 bullet points per slide
- Maximum 2 lines per bullet point
- Code blocks: max 10 lines per slide, round corners 8px
- Tables: max 5 columns, 7 rows; header #152032 with white text
- Every data claim MUST show source in 14px #6B7280 footer
- Divider lines use Featured Red #BA4D43

=== SLIDE TYPES ===
1. MODULE COVER: Dark gradient bg (#050505→#0F2D2B), module number in #2C918C, title white 48px, divider #BA4D43
2. CONTENT: White bg, left 60% text + right 40% visual, title underline #2C918C, source footer
3. CODE: White bg, dark code block #0F0F0F with round corners, key takeaway in #A855F7 below
4. QUOTE: Dark gradient bg, single centered quote in Noto Serif TC italic white, divider #BA4D43
5. DATA: White bg, large numbers 64px #2C918C, source citation required
6. TABLE: White bg, header #152032 white text, alternating rows #FAFBFC
7. WORKSHOP: Elevated bg #F9FAFB, left border 4px #A855F7, title in #A855F7, criteria in #2C918C
8. INFO CALLOUT: Colored bg + left border based on semantic type (info/warning/success/error)

=== SLIDE STRUCTURE PER MODULE ===
- Slide 1: Module cover (Template A, dark gradient)
- Slide 2: Learning objectives (Template F, table format)
- Slides 3-N: Content slides (Templates B/C/E/F)
- 1 Quote slide per module (Template D, dark gradient)
- Workshop slides at 60% mark and end (Template W, purple accent)
- Final slide: Module summary + next module preview
```

### 逐模組 Prompt（每次生成一個模組時使用）

```
Create slides for Module [X]: [模組標題]

Source material: [貼入對應模組 .md 檔案內容]

Requirements:
1. Follow the Sunny DataScience design system established above
2. Each slide from the outline table = one Gamma slide
3. Use the "講師講解要點" as bullet points (max 4-5 per slide)
4. Use the "視覺建議" to design the right-side visual
5. Use the "轉場" text as presenter notes (not shown on slide)
6. Code examples go on dedicated code slides (Template C, #0F0F0F block)
7. Every statistic MUST show its source in 14px #6B7280 footer
8. Workshop exercises use Template W with #A855F7 purple accent
9. Module number badge uses #2C918C teal
10. Divider lines use #BA4D43 red

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

### 色彩（Sunny DataScience 品牌色）
- [ ] 深色背景只用 #050505 或 #0F0F0F，非 #000000
- [ ] 主強調色是 #2C918C（Primary Teal），非其他綠/藍色
- [ ] 次強調色是 #A855F7（Accent Purple），非橘色
- [ ] 分隔線是 #BA4D43（Featured Red），非灰色
- [ ] 淺底正文字色 #151B28，非 #000000
- [ ] 來源標注 #6B7280（Secondary），非黑色
- [ ] 程式碼區塊 #0F0F0F 背景 + #F8F8F2 文字
- [ ] 表頭 #152032 背景 + #FFFFFF 文字
- [ ] 圖表色依序使用品牌色板

### 排版
- [ ] 每頁不超過 5 個要點
- [ ] 每個要點不超過 2 行
- [ ] 程式碼不超過 10 行/頁
- [ ] 表格不超過 5 欄 x 7 行
- [ ] 標題左對齊（金句頁例外）

### 內容
- [ ] 每個數據宣稱底部有來源標注（14px #6B7280）
- [ ] 每個模組有 1 張金句頁（深色漸層背景）
- [ ] 每個模組第一張是深色漸層封面頁
- [ ] 工作坊頁用 #F9FAFB 背景 + #A855F7 紫色邊條

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
- **Heading 1** -> 對應 H1（36px）
- **Heading 2** -> 對應 H2（24px）
- **Heading 3** -> 對應 H3（20px）
- **Normal text** -> 對應 Body（18px）
- **Small text** -> 對應 Small（14px）
- 在 Theme 設定中調整 base font size

### 3. 如何確保色彩一致

在 Gamma Theme 設定中：
- Primary color -> #2C918C (Primary Teal)
- Accent color -> #A855F7 (Accent Purple)
- Background -> #050505 (Dark) 或 #FFFFFF (Light)
- 在生成後手動檢查，把任何偏離的色彩修正回品牌色

### 4. 建議的工作流程

```
1. 在 Gamma 中建立新 Presentation
2. 貼入「初始化 Prompt」設定設計系統
3. 進入 Theme 手動設定字型和色彩（優先於 prompt）
4. 逐模組貼入「逐模組 Prompt」+ 模組 .md 內容
5. 生成後用 QA Checklist 逐項檢查
6. 手動修正不符合規範的元素
7. 匯出 PDF 前再做一次全面檢查
```

### 5. 深色 vs 淺色風格快速搭配

**深色風格（科技感，推薦封面/金句/程式碼頁）：**
```
背景: #050505 | 標題: #FFFFFF | 重點: #2C918C | 強調: #A855F7 | 分隔線: #BA4D43 | 副文字: #6B7280
```

**淺色風格（正式場合，推薦教學/表格/數據頁）：**
```
背景: #FFFFFF | 標題: #151B28 | 重點: #2C918C | 強調: #1E3A5F | 分隔線: #BA4D43 | 副文字: #6B7280
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

---

## 十二、附錄：一行快速複製色碼

### 品牌核心四色
```
#2C918C  #A855F7  #BA4D43  #1E3A5F
```

### 全色板
```
#2C918C  #A855F7  #BA4D43  #1E3A5F  #050505  #FFFFFF
#151B28  #6B7280  #F59E0B  #3B82F6  #EF4444  #10B981
```

### Figma / Canva 匯入用 JSON
```json
{
  "brand": {
    "primary-teal": "#2C918C",
    "accent-purple": "#A855F7",
    "featured-red": "#BA4D43",
    "navy": "#1E3A5F"
  },
  "background": {
    "dark": "#050505",
    "dark-surface": "#0F0F0F",
    "dark-teal": "#0F2D2B",
    "dark-header": "#152032",
    "light": "#FFFFFF",
    "light-elevated": "#F9FAFB",
    "light-muted": "#FAFBFC"
  },
  "text": {
    "on-dark": "#FFFFFF",
    "on-light": "#151B28",
    "secondary": "#6B7280",
    "tertiary": "#9CA3AF"
  },
  "status": {
    "success": "#10B981",
    "warning": "#F59E0B",
    "error": "#EF4444",
    "info": "#3B82F6"
  },
  "chart": ["#2C918C", "#A855F7", "#F59E0B", "#3B82F6", "#EF4444", "#10B981", "#EC4899", "#8B5CF6"]
}
```
