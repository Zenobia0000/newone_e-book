"""Editorial-strict theme constants. Single source of truth for all decks."""
from pathlib import Path
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor

# Palette — locked per 02_slides_design.md frontmatter
PRIMARY = RGBColor(0x1B, 0x5E, 0x3F)
CHARCOAL = RGBColor(0x33, 0x33, 0x33)
GRAY_MID = RGBColor(0x80, 0x80, 0x80)
LIGHT_GRAY = RGBColor(0xD3, 0xD3, 0xD3)
TABLE_ALT = RGBColor(0xF0, 0xF0, 0xF0)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

# Hex strings for matplotlib
HEX_PRIMARY = "#1B5E3F"
HEX_CHARCOAL = "#333333"
HEX_LIGHT_GRAY = "#D3D3D3"
HEX_GRAY_MID = "#808080"

# Font sizes (pt) — aligned to design system
FONT_TITLE = Pt(28)
FONT_SUBTITLE = Pt(20)
FONT_BODY = Pt(14)
FONT_CAPTION = Pt(12)
FONT_SMALL = Pt(10)
FONT_SOURCE = Pt(8)
FONT_COVER_TITLE = Pt(36)
FONT_COVER_SUB = Pt(16)
FONT_HERO = Pt(44)  # SILENT hero statement

FONT_FAMILY = "Noto Sans CJK TC"  # fallback chain; PowerPoint will substitute
FONT_FAMILY_FALLBACK = "Microsoft JhengHei"
FONT_MONO = "Consolas"

# Slide geometry (16:9)
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN_X = Inches(0.6)
MARGIN_Y = Inches(0.4)
CONTENT_TOP = Inches(0.9)

# Logo sizing
LOGO_COVER_SIZE = Inches(2.2)
LOGO_CORNER_SIZE = Inches(0.55)

# Paths
PKG_DIR = Path(__file__).resolve().parent
BOOK_DIR = PKG_DIR.parent
LOGO_PATH = BOOK_DIR / "images" / "logo_main.png"
LOGO_DARK_PATH = BOOK_DIR / "images" / "dark.png"
CHART_CACHE = PKG_DIR / "_charts"
OUTPUT_DIR = PKG_DIR / "output"
CHART_CACHE.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# Brand
BRAND_NAME_ZH = "桑尼資料科學"
BRAND_NAME_EN = "Sunny Data Science"
COPYRIGHT_YEAR = 2026

# Copyright wording
COPYRIGHT_SHORT = f"© {COPYRIGHT_YEAR} {BRAND_NAME_ZH}"

COPYRIGHT_FULL = (
    f"© {COPYRIGHT_YEAR} {BRAND_NAME_ZH}（{BRAND_NAME_EN}）. All rights reserved.\n\n"
    "本投影片內容（包含但不限於文字、圖表、結構設計、視覺風格）為桑尼資料科學之著作財產，\n"
    "受中華民國《著作權法》及相關國際著作權公約保護。\n\n"
    "未經書面授權，任何人不得以任何形式重製、改作、散布、公開傳輸、轉載、翻印、\n"
    "或用於商業訓練、教學、授課或 AI 模型訓練資料。\n\n"
    "違反者，本公司將依法追究民事與刑事責任。\n\n"
    "授權聯絡：contact@sunny-data-science.tw"
)
