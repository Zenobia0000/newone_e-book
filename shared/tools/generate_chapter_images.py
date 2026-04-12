# -*- coding: utf-8 -*-
"""Generate chapter cover images for an ebook.

Usage:
    python generate_chapter_images.py <book_dir>

Example:
    python generate_chapter_images.py ../../books/小白程式入門
"""

import os
import sys
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert hex color string to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def load_book_config(book_dir: Path) -> dict:
    """Load book.yaml from the given book directory."""
    config_path = book_dir / "book.yaml"
    if not config_path.exists():
        print(f"Error: book.yaml not found in {book_dir}")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_brand_colors(config: dict) -> dict:
    """Extract brand colors from config, with defaults."""
    colors = config.get("brand_colors", {})
    return {
        "dark_blue": hex_to_rgb(colors.get("dark_blue", "#1A2A3A")),
        "teal": hex_to_rgb(colors.get("teal", "#4DC7AF")),
        "light_teal": hex_to_rgb(colors.get("light_teal", "#82DCC8")),
        "white": (255, 255, 255),
        "gray": (180, 190, 200),
    }


def get_fonts() -> dict:
    """Load fonts with fallback."""
    font_paths = [
        "C:/Windows/Fonts/msjh.ttc",
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
    ]

    for fp in font_paths:
        if os.path.exists(fp):
            return {
                "title": ImageFont.truetype(fp, 48),
                "subtitle": ImageFont.truetype(fp, 24),
                "num": ImageFont.truetype(fp, 120),
                "icon": ImageFont.truetype(
                    "C:/Windows/Fonts/consola.ttf", 60
                ) if os.path.exists("C:/Windows/Fonts/consola.ttf")
                else ImageFont.truetype(fp, 60),
            }

    default = ImageFont.load_default()
    return {"title": default, "subtitle": default, "num": default, "icon": default}


def create_chapter_image(
    chapter_info: dict,
    output_path: str,
    colors: dict,
    width: int = 800,
    height: int = 400,
) -> None:
    """Create a chapter cover image."""
    img = Image.new("RGB", (width, height), colors["dark_blue"])
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()

    # Decorative elements
    draw.rectangle([(0, 0), (width, 8)], fill=colors["teal"])
    draw.rectangle([(0, 50), (8, height - 50)], fill=colors["teal"])

    # Chapter number (large, on the right)
    num_text = chapter_info["num"]
    try:
        num_bbox = draw.textbbox((0, 0), num_text, font=fonts["num"])
        num_width = num_bbox[2] - num_bbox[0]
    except Exception:
        num_width = 150

    num_x = width - num_width - 40
    num_y = height // 2 - 80

    for offset in range(3, 0, -1):
        draw.text(
            (num_x + offset, num_y + offset),
            num_text,
            font=fonts["num"],
            fill=(40, 60, 80),
        )
    draw.text((num_x, num_y), num_text, font=fonts["num"], fill=colors["teal"])

    # Icon
    draw.text((50, 60), chapter_info.get("icon", ""), font=fonts["icon"], fill=colors["light_teal"])

    # Chapter label
    draw.text(
        (50, 140),
        f"CHAPTER {chapter_info['num']}",
        font=fonts["subtitle"],
        fill=colors["gray"],
    )

    # Title
    draw.text((50, 180), chapter_info["title"], font=fonts["title"], fill=colors["white"])

    # Subtitle
    draw.text(
        (50, 260),
        chapter_info.get("subtitle", ""),
        font=fonts["subtitle"],
        fill=colors["gray"],
    )

    # Bottom dots
    for i in range(5):
        x = 50 + i * 20
        draw.ellipse(
            [(x, height - 40), (x + 8, height - 32)],
            fill=colors["teal"] if i == 0 else colors["gray"],
        )

    img.save(output_path, "PNG")
    print(f"[OK] Created: {output_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_chapter_images.py <book_dir>")
        sys.exit(1)

    book_dir = Path(sys.argv[1]).resolve()
    config = load_book_config(book_dir)
    colors = get_brand_colors(config)

    images_dir = book_dir / "images"
    images_dir.mkdir(exist_ok=True)

    chapter_meta = config.get("chapter_meta", [])
    if not chapter_meta:
        print("No chapter_meta found in book.yaml, nothing to generate.")
        return

    print(f"Output directory: {images_dir}\n")

    for chapter in chapter_meta:
        filename = f"chapter_{chapter['num']}.png"
        output_path = images_dir / filename
        create_chapter_image(chapter, str(output_path), colors)

    print(f"\n[DONE] Generated {len(chapter_meta)} chapter images")


if __name__ == "__main__":
    main()
