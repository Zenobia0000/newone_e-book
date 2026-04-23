"""Uber-inspired theme constants. Black/white confident minimalism.

Design language: stark duality of jet black and pure white,
bold typography, pill-shaped accents, information-dense but clear.
Ref: .claude/ui/uber/DESIGN.md
"""
from pathlib import Path
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor

# ── Uber-inspired palette ──────────────────────────────────────
PRIMARY = RGBColor(0x00, 0x00, 0x00)       # Uber Black — brand anchor
CHARCOAL = RGBColor(0x1A, 0x1A, 0x1A)      # near-black body text
GRAY_MID = RGBColor(0x99, 0x99, 0x99)       # captions, secondary text
LIGHT_GRAY = RGBColor(0xE5, 0xE5, 0xE5)     # subtle borders, dividers
TABLE_ALT = RGBColor(0xF5, 0xF5, 0xF5)      # alternating row bg
WHITE = RGBColor(0xFF, 0xFF, 0xFF)           # pure white

# Extended palette — content accents (NOT for chrome/UI)
ACCENT = RGBColor(0x27, 0x6E, 0xF1)         # Uber blue — callouts, badges
ACCENT_WARM = RGBColor(0xFF, 0x6D, 0x00)    # warm orange — warnings, pitfall
SURFACE_DARK = RGBColor(0x0A, 0x0A, 0x0A)   # SILENT bg (near-black)
SURFACE_LIGHT = RGBColor(0xFA, 0xFA, 0xFA)  # code bg, card surfaces
CHIP_GRAY = RGBColor(0xEF, 0xEF, 0xEF)      # pill chip background

# Hex strings for matplotlib
HEX_PRIMARY = "#000000"
HEX_CHARCOAL = "#1A1A1A"
HEX_LIGHT_GRAY = "#E5E5E5"
HEX_GRAY_MID = "#999999"
HEX_ACCENT = "#276EF1"

# ── Typography ─────────────────────────────────────────────────
# Font sizes — bolder, bigger headlines for confident presence
FONT_HERO = Pt(52)          # SILENT hero statement (billboard scale)
FONT_COVER_TITLE = Pt(40)   # cover slide title
FONT_TITLE = Pt(30)         # content slide title
FONT_SUBTITLE = Pt(22)      # sub-heading
FONT_COVER_SUB = Pt(16)     # cover subtitle
FONT_BODY = Pt(15)          # standard body text
FONT_CAPTION = Pt(12)       # compact descriptions
FONT_SMALL = Pt(10)         # footer, progress markers
FONT_SOURCE = Pt(8)         # source citations

FONT_FAMILY = "Noto Sans CJK TC"
FONT_FAMILY_FALLBACK = "Microsoft JhengHei"
FONT_MONO = "Consolas"

# ── Slide geometry (16:9) ──────────────────────────────────────
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN_X = Inches(0.8)      # wider margins = more confident whitespace
MARGIN_Y = Inches(0.5)
CONTENT_TOP = Inches(1.0)

# Logo sizing
LOGO_COVER_SIZE = Inches(1.6)    # smaller on cover — text-dominant
LOGO_CORNER_SIZE = Inches(0.5)

# ── Paths ──────────────────────────────────────────────────────
PKG_DIR = Path(__file__).resolve().parent
BOOK_DIR = PKG_DIR.parent
LOGO_PATH = BOOK_DIR / "images" / "logo_main.png"
LOGO_DARK_PATH = BOOK_DIR / "images" / "dark.png"
CHART_CACHE = PKG_DIR / "_charts"
OUTPUT_DIR = PKG_DIR / "output"
CHART_CACHE.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# ── Brand ──────────────────────────────────────────────────────
BRAND_NAME_ZH = "桑尼資料科學"
BRAND_NAME_EN = "Sunny Data Science"
COPYRIGHT_YEAR = 2026

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
