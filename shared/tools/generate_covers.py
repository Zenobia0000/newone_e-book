# -*- coding: utf-8 -*-
"""Generate ebook cover and CTA page cover.

Usage:
    python generate_covers.py <book_dir>

Example:
    python generate_covers.py ../../books/小白程式入門
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
        "C:/Windows/Fonts/msjhbd.ttc",
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


def find_logo() -> Path | None:
    """Find the shared logo file."""
    # Resolve relative to this script's location
    tools_dir = Path(__file__).resolve().parent
    shared_dir = tools_dir.parent
    logo_path = shared_dir / "assets" / "logo_main.png"
    return logo_path if logo_path.exists() else None


def create_main_cover(
    output_path: str,
    config: dict,
    colors: dict,
    logo_path: Path | None = None,
) -> None:
    """Create the main ebook cover."""
    width, height = 800, 1200
    img = Image.new("RGB", (width, height), colors["dark_blue"])
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()

    title = config["title"]
    subtitle = config.get("subtitle", "")
    author = config.get("author", "")

    # Top gradient bar
    for i in range(20):
        alpha = int(255 * (1 - i / 20))
        color = tuple(int(c * alpha / 255) for c in colors["teal"])
        draw.rectangle([(0, i * 3), (width, i * 3 + 3)], fill=color)

    # Side accent
    draw.rectangle([(0, 100), (10, height - 100)], fill=colors["teal"])

    # Bottom bar
    draw.rectangle([(0, height - 60), (width, height)], fill=colors["teal"])

    # Geometric shapes
    for i in range(5):
        x = 650 + i * 30
        y = 200 + i * 40
        size = 80 - i * 15
        draw.ellipse([(x, y), (x + size, y + size)], outline=colors["teal"], width=2)

    # Code-like decorative text
    code_lines = ["def learn():", "    start()", "    practice()", "    grow()"]
    y_pos = 850
    for line in code_lines:
        draw.text((550, y_pos), line, font=fonts["small"], fill=(60, 80, 100))
        y_pos += 35

    # Title - split into lines if needed
    title_parts = title.split("：") if "：" in title else [title]
    y_title = 280
    for part in title_parts:
        draw.text((50, y_title), part, font=fonts["title"], fill=colors["white"])
        y_title += 100

    # Subtitle
    if subtitle:
        draw.text((50, y_title + 20), subtitle, font=fonts["subtitle"], fill=colors["light_teal"])

    # Logo
    if logo_path and logo_path.exists():
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((120, 120), Image.Resampling.LANCZOS)
        img.paste(logo, (width - 170, height - 200), logo)

    # Author
    if author:
        author_parts = author.split(" | ")
        draw.text((50, height - 120), author_parts[0], font=fonts["subtitle"], fill=colors["white"])
        if len(author_parts) > 1:
            draw.text((50, height - 80), author_parts[1], font=fonts["small"], fill=colors["gray"])

    img.save(output_path, "PNG")
    print(f"[OK] Main cover: {output_path}")


def create_cta_cover(
    output_path: str,
    colors: dict,
    logo_path: Path | None = None,
) -> None:
    """Create the CTA page cover."""
    width, height = 800, 400
    img = Image.new("RGB", (width, height), colors["dark_blue"])
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()

    draw.rectangle([(0, 0), (width, 8)], fill=colors["teal"])
    draw.rectangle([(0, 50), (8, height - 50)], fill=colors["teal"])

    # Connecting lines
    for i in range(10):
        x1 = 500 + i * 30
        y1 = 50 + i * 20
        x2 = x1 + 50
        y2 = y1 + 80
        draw.line([(x1, y1), (x2, y2)], fill=(40, 60, 80), width=2)
        draw.ellipse([(x1 - 4, y1 - 4), (x1 + 4, y1 + 4)], fill=colors["teal"])

    if logo_path and logo_path.exists():
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((80, 80), Image.Resampling.LANCZOS)
        img.paste(logo, (50, 60), logo)

    draw.text((50, 160), "加入學習社群", font=fonts["title"], fill=colors["white"])
    draw.text((50, 260), "讓數據說故事，讓程式改變生活", font=fonts["small"], fill=colors["gray"])
    draw.text((50, height - 60), "桑尼資料科學 | Data Sunnie", font=fonts["small"], fill=colors["teal"])

    for i in range(5):
        x = width - 150 + i * 25
        draw.ellipse(
            [(x, height - 40), (x + 10, height - 30)],
            fill=colors["teal"] if i < 2 else colors["gray"],
        )

    img.save(output_path, "PNG")
    print(f"[OK] CTA cover: {output_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_covers.py <book_dir>")
        sys.exit(1)

    book_dir = Path(sys.argv[1]).resolve()
    config = load_book_config(book_dir)
    colors = get_brand_colors(config)
    logo_path = find_logo()

    images_dir = book_dir / "images"
    images_dir.mkdir(exist_ok=True)

    print(f"Book: {config['title']}")
    print(f"Logo: {logo_path}")
    print()

    create_main_cover(str(images_dir / "cover_main.png"), config, colors, logo_path)
    create_cta_cover(str(images_dir / "cover_cta.png"), colors, logo_path)

    print("\n[DONE] All covers generated")


if __name__ == "__main__":
    main()
