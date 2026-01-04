# -*- coding: utf-8 -*-
"""Generate chapter cover images for the ebook."""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


# Brand colors (based on logo)
DARK_BLUE = (26, 42, 58)       # #1A2A3A - background
TEAL = (77, 199, 175)          # #4DC7AF - accent
LIGHT_TEAL = (130, 220, 200)   # #82DCC8 - highlight
WHITE = (255, 255, 255)
GRAY = (180, 190, 200)


# Chapter info with icons (emoji representation)
CHAPTERS = [
    {"num": "01", "title": "程式到底是什麼？", "icon": "?", "subtitle": "打破迷思，理解程式的本質"},
    {"num": "02", "title": "程式語言大觀園", "icon": "</>", "subtitle": "認識各種語言，找到適合你的"},
    {"num": "03", "title": "像電腦一樣思考", "icon": "{ }", "subtitle": "培養運算思維與邏輯能力"},
    {"num": "04", "title": "資料與變數", "icon": "x=", "subtitle": "程式如何儲存與處理資訊"},
    {"num": "05", "title": "自動化你的生活", "icon": ">>", "subtitle": "用程式解決日常問題"},
    {"num": "06", "title": "創造你的第一個專案", "icon": "*", "subtitle": "動手實作，從想法到成品"},
    {"num": "07", "title": "程式設計的職業道路", "icon": "//", "subtitle": "了解產業與職涯發展"},
    {"num": "08", "title": "學習資源與社群", "icon": "@", "subtitle": "找到持續學習的方法"},
    {"num": "09", "title": "學習程式的正確心態", "icon": "!", "subtitle": "克服挫折，建立成長思維"},
    {"num": "10", "title": "從零到一的行動計畫", "icon": "->", "subtitle": "制定你的學習路線圖"},
]


def create_chapter_image(chapter_info: dict, output_path: str, width: int = 800, height: int = 400):
    """Create a chapter cover image."""

    # Create image with dark blue background
    img = Image.new('RGB', (width, height), DARK_BLUE)
    draw = ImageDraw.Draw(img)

    # Try to load fonts, fallback to default
    try:
        # Try common Windows fonts
        font_paths = [
            "C:/Windows/Fonts/msjh.ttc",      # Microsoft JhengHei
            "C:/Windows/Fonts/msyh.ttc",      # Microsoft YaHei
            "C:/Windows/Fonts/simhei.ttf",    # SimHei
            "C:/Windows/Fonts/arial.ttf",
        ]

        title_font = None
        for fp in font_paths:
            if os.path.exists(fp):
                title_font = ImageFont.truetype(fp, 48)
                subtitle_font = ImageFont.truetype(fp, 24)
                num_font = ImageFont.truetype(fp, 120)
                icon_font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 60)
                break

        if title_font is None:
            raise Exception("No font found")

    except Exception:
        title_font = ImageFont.load_default()
        subtitle_font = title_font
        num_font = title_font
        icon_font = title_font

    # Draw decorative elements
    # Top line
    draw.rectangle([(0, 0), (width, 8)], fill=TEAL)

    # Left accent bar
    draw.rectangle([(0, 50), (8, height - 50)], fill=TEAL)

    # Draw chapter number (large, faded)
    num_text = chapter_info["num"]
    try:
        num_bbox = draw.textbbox((0, 0), num_text, font=num_font)
        num_width = num_bbox[2] - num_bbox[0]
    except:
        num_width = 150

    # Position number on the right side, slightly transparent effect
    num_x = width - num_width - 40
    num_y = height // 2 - 80

    # Draw number with gradient-like effect (multiple layers)
    for offset in range(3, 0, -1):
        alpha_color = tuple(int(c * 0.3) for c in TEAL)
        draw.text((num_x + offset, num_y + offset), num_text, font=num_font, fill=(40, 60, 80))
    draw.text((num_x, num_y), num_text, font=num_font, fill=TEAL)

    # Draw icon
    icon_text = chapter_info["icon"]
    draw.text((50, 60), icon_text, font=icon_font, fill=LIGHT_TEAL)

    # Draw "CHAPTER" label
    draw.text((50, 140), f"CHAPTER {chapter_info['num']}", font=subtitle_font, fill=GRAY)

    # Draw main title
    draw.text((50, 180), chapter_info["title"], font=title_font, fill=WHITE)

    # Draw subtitle
    draw.text((50, 260), chapter_info["subtitle"], font=subtitle_font, fill=GRAY)

    # Draw bottom decorative dots
    for i in range(5):
        x = 50 + i * 20
        draw.ellipse([(x, height - 40), (x + 8, height - 32)], fill=TEAL if i == 0 else GRAY)

    # Save image
    img.save(output_path, 'PNG')
    print(f"[OK] Created: {output_path}")


def find_ebook_dir():
    """Find the ebook directory."""
    base_dir = Path(r"D:/python_workspace")

    for root, dirs, files in os.walk(base_dir):
        if "newone_e-book" in root and root.endswith("newone_e-book"):
            return Path(root)

    return None


def main():
    ebook_dir = find_ebook_dir()

    if not ebook_dir:
        print("Error: Cannot find ebook directory")
        return

    # Create images directory
    images_dir = ebook_dir / "images"
    images_dir.mkdir(exist_ok=True)

    print(f"Output directory: {images_dir}\n")

    # Generate chapter images
    for chapter in CHAPTERS:
        filename = f"chapter_{chapter['num']}.png"
        output_path = images_dir / filename
        create_chapter_image(chapter, str(output_path))

    print(f"\n[DONE] Generated {len(CHAPTERS)} chapter images")

    # Now update the merged ebook to include images
    update_ebook_with_images(ebook_dir, images_dir)


def update_ebook_with_images(ebook_dir: Path, images_dir: Path):
    """Update the merged ebook to include chapter images."""

    ebook_path = ebook_dir / "小白程式入門電子書_完整版.md"

    if not ebook_path.exists():
        print("Ebook file not found")
        return

    with open(ebook_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert image before each chapter heading
    for chapter in CHAPTERS:
        old_heading = f"# 第{chapter['num'].lstrip('0') if chapter['num'] != '10' else '10'}章："
        if chapter['num'] == '01':
            old_heading = "# 第1章："

        img_path = f"images/chapter_{chapter['num']}.png"
        new_content = f"![Chapter {chapter['num']}]({img_path})\n\n{old_heading}"

        content = content.replace(old_heading, new_content, 1)

    # Save updated ebook
    output_path = ebook_dir / "小白程式入門電子書_完整版_含圖.md"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n[DONE] Updated ebook saved to: {output_path}")


if __name__ == "__main__":
    main()
