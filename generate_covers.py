# -*- coding: utf-8 -*-
"""Generate ebook cover and CTA page cover."""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# Brand colors
DARK_BLUE = (26, 42, 58)
TEAL = (77, 199, 175)
LIGHT_TEAL = (130, 220, 200)
WHITE = (255, 255, 255)
GRAY = (180, 190, 200)


def get_fonts():
    """Load fonts with fallback."""
    font_paths = [
        "C:/Windows/Fonts/msjhbd.ttc",    # Microsoft JhengHei Bold
        "C:/Windows/Fonts/msjh.ttc",
        "C:/Windows/Fonts/msyh.ttc",
    ]

    for fp in font_paths:
        if os.path.exists(fp):
            return {
                "title": ImageFont.truetype(fp, 72),
                "subtitle": ImageFont.truetype(fp, 32),
                "small": ImageFont.truetype(fp, 24),
                "large": ImageFont.truetype(fp, 120),
            }

    default = ImageFont.load_default()
    return {"title": default, "subtitle": default, "small": default, "large": default}


def create_main_cover(output_path: str, logo_path: str = None):
    """Create the main ebook cover."""
    width, height = 800, 1200
    img = Image.new('RGB', (width, height), DARK_BLUE)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()

    # Draw decorative elements
    # Top gradient bar
    for i in range(20):
        alpha = int(255 * (1 - i/20))
        color = tuple(int(c * alpha/255) for c in TEAL)
        draw.rectangle([(0, i*3), (width, i*3+3)], fill=color)

    # Side accent
    draw.rectangle([(0, 100), (10, height-100)], fill=TEAL)

    # Bottom decorative bar
    draw.rectangle([(0, height-60), (width, height)], fill=TEAL)

    # Draw geometric shapes
    # Circle pattern
    for i in range(5):
        x = 650 + i * 30
        y = 200 + i * 40
        size = 80 - i * 15
        draw.ellipse([(x, y), (x+size, y+size)], outline=TEAL, width=2)

    # Code-like decorative text
    code_lines = [
        "def learn():",
        "    start()",
        "    practice()",
        "    grow()",
    ]
    y_pos = 850
    for line in code_lines:
        draw.text((550, y_pos), line, font=fonts["small"], fill=(60, 80, 100))
        y_pos += 35

    # Main title
    draw.text((50, 280), "小白程式入門", font=fonts["title"], fill=WHITE)
    draw.text((50, 380), "電子書", font=fonts["title"], fill=TEAL)

    # Subtitle
    draw.text((50, 500), "從零開始", font=fonts["subtitle"], fill=LIGHT_TEAL)
    draw.text((50, 550), "用故事帶你踏入程式世界", font=fonts["subtitle"], fill=GRAY)

    # Bullet points
    bullets = [
        "10 個章節完整學習路徑",
        "真實故事引導入門",
        "從觀念到實作一次搞懂",
    ]
    y_pos = 650
    for bullet in bullets:
        draw.ellipse([(50, y_pos+8), (62, y_pos+20)], fill=TEAL)
        draw.text((75, y_pos), bullet, font=fonts["small"], fill=WHITE)
        y_pos += 45

    # Add logo if exists
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path).convert('RGBA')
        logo = logo.resize((120, 120), Image.Resampling.LANCZOS)
        # Position at bottom right
        logo_pos = (width - 170, height - 200)
        img.paste(logo, logo_pos, logo)

    # Author info
    draw.text((50, height - 120), "桑尼資料科學", font=fonts["subtitle"], fill=WHITE)
    draw.text((50, height - 80), "Data Sunnie", font=fonts["small"], fill=GRAY)

    img.save(output_path, 'PNG')
    print(f"[OK] Main cover: {output_path}")


def create_cta_cover(output_path: str, logo_path: str = None):
    """Create the CTA page cover."""
    width, height = 800, 400
    img = Image.new('RGB', (width, height), DARK_BLUE)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()

    # Decorative top bar
    draw.rectangle([(0, 0), (width, 8)], fill=TEAL)

    # Left accent
    draw.rectangle([(0, 50), (8, height-50)], fill=TEAL)

    # Draw connecting lines pattern
    for i in range(10):
        x1 = 500 + i * 30
        y1 = 50 + i * 20
        x2 = x1 + 50
        y2 = y1 + 80
        draw.line([(x1, y1), (x2, y2)], fill=(40, 60, 80), width=2)
        draw.ellipse([(x1-4, y1-4), (x1+4, y1+4)], fill=TEAL)

    # Add logo if exists
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path).convert('RGBA')
        logo = logo.resize((80, 80), Image.Resampling.LANCZOS)
        img.paste(logo, (50, 60), logo)

    # Main text
    draw.text((50, 160), "加入學習社群", font=fonts["title"], fill=WHITE)
    draw.text((50, 260), "讓數據說故事，讓程式改變生活", font=fonts["small"], fill=GRAY)

    # Brand name
    draw.text((50, height - 60), "桑尼資料科學 | Data Sunnie", font=fonts["small"], fill=TEAL)

    # Bottom dots
    for i in range(5):
        x = width - 150 + i * 25
        draw.ellipse([(x, height-40), (x+10, height-30)], fill=TEAL if i < 2 else GRAY)

    img.save(output_path, 'PNG')
    print(f"[OK] CTA cover: {output_path}")


def find_paths():
    """Find ebook directory and logo."""
    base_dir = Path(r"D:/python_workspace")

    for root, dirs, files in os.walk(base_dir):
        if "newone_e-book" in root and root.endswith("newone_e-book"):
            ebook_dir = Path(root)

            # Find logo
            logo_path = None
            for lr, ld, lf in os.walk(ebook_dir):
                if "logo_main.png" in lf:
                    logo_path = Path(lr) / "logo_main.png"
                    break

            return ebook_dir, logo_path

    return None, None


def update_ebook_with_covers(ebook_dir: Path):
    """Update ebook to include new covers."""
    ebook_path = ebook_dir / "小白程式入門電子書_完整版_含圖.md"

    if not ebook_path.exists():
        print("Ebook not found")
        return

    with open(ebook_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add main cover at the beginning
    cover_insert = """![封面](images/cover_main.png)

---

<div style="page-break-after: always;"></div>

---

"""

    # Insert after the title
    if "# 小白程式入門電子書" in content and "![封面]" not in content:
        content = content.replace(
            "# 小白程式入門電子書\n",
            f"![封面](images/cover_main.png)\n\n# 小白程式入門電子書\n"
        )

    # Add CTA cover before the CTA section
    if "# 感謝你讀到這裡" in content and "![加入我們]" not in content:
        content = content.replace(
            "# 感謝你讀到這裡",
            "![加入我們](images/cover_cta.png)\n\n# 感謝你讀到這裡"
        )

    # Save updated file
    with open(ebook_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[OK] Updated ebook with covers")


def main():
    ebook_dir, logo_path = find_paths()

    if not ebook_dir:
        print("Error: Cannot find ebook directory")
        return

    images_dir = ebook_dir / "images"
    images_dir.mkdir(exist_ok=True)

    print(f"Ebook dir: {ebook_dir}")
    print(f"Logo path: {logo_path}")
    print()

    # Generate covers
    create_main_cover(
        str(images_dir / "cover_main.png"),
        str(logo_path) if logo_path else None
    )

    create_cta_cover(
        str(images_dir / "cover_cta.png"),
        str(logo_path) if logo_path else None
    )

    # Update ebook
    update_ebook_with_covers(ebook_dir)

    print("\n[DONE] All covers generated and inserted")


if __name__ == "__main__":
    main()
