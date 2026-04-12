# -*- coding: utf-8 -*-
"""Generate QR codes with embedded logo.

Usage:
    python generate_qrcode.py

Generates QR codes for social media channels into shared/assets/qr_codes/.
"""

from pathlib import Path

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask, VerticalGradiantColorMask
from PIL import Image


# Brand colors
LINE_GREEN = (6, 199, 85)
IG_PURPLE = (131, 58, 180)
IG_ORANGE = (253, 175, 69)
DISCORD_BLURPLE = (88, 101, 242)
DISCORD_DARK = (64, 78, 237)
WHITE = (255, 255, 255)


def generate_qrcode_with_logo(
    url: str,
    output_path: str,
    logo_path: str,
    logo_size_ratio: float = 0.25,
    color_mask=None,
) -> None:
    """Generate a QR code with an embedded logo."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    make_kwargs = {
        "image_factory": StyledPilImage,
        "module_drawer": RoundedModuleDrawer(),
    }
    if color_mask:
        make_kwargs["color_mask"] = color_mask

    qr_img = qr.make_image(**make_kwargs).convert("RGBA")

    logo = Image.open(logo_path).convert("RGBA")
    qr_width, qr_height = qr_img.size
    logo_max_size = int(qr_width * logo_size_ratio)

    logo_ratio = logo.width / logo.height
    if logo_ratio > 1:
        new_width = logo_max_size
        new_height = int(logo_max_size / logo_ratio)
    else:
        new_height = logo_max_size
        new_width = int(logo_max_size * logo_ratio)

    logo_resized = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)

    pos_x = (qr_width - new_width) // 2
    pos_y = (qr_height - new_height) // 2

    qr_img.paste(logo_resized, (pos_x, pos_y), logo_resized)
    qr_img.save(output_path, "PNG")
    print(f"QR code saved: {output_path}")


def main():
    # Resolve paths relative to this script
    tools_dir = Path(__file__).resolve().parent
    shared_dir = tools_dir.parent
    logo_path = shared_dir / "assets" / "logo_main.png"
    output_dir = shared_dir / "assets" / "qr_codes"
    output_dir.mkdir(parents=True, exist_ok=True)

    if not logo_path.exists():
        print(f"Error: logo not found at {logo_path}")
        return

    line_color = SolidFillColorMask(back_color=WHITE, front_color=LINE_GREEN)
    ig_color = VerticalGradiantColorMask(
        back_color=WHITE, top_color=IG_PURPLE, bottom_color=IG_ORANGE
    )
    discord_color = VerticalGradiantColorMask(
        back_color=WHITE, top_color=DISCORD_BLURPLE, bottom_color=DISCORD_DARK
    )

    qr_configs = [
        {
            "filename": "qr_line.png",
            "url": "https://line.me/R/ti/p/@055zjitb",
            "color_mask": line_color,
        },
        {
            "filename": "qr_instagram.png",
            "url": "https://www.instagram.com/datasunnie",
            "color_mask": ig_color,
        },
        {
            "filename": "qr_discord.png",
            "url": "https://discord.gg/CVS6g6MbhU",
            "color_mask": discord_color,
        },
    ]

    for config in qr_configs:
        generate_qrcode_with_logo(
            url=config["url"],
            output_path=str(output_dir / config["filename"]),
            logo_path=str(logo_path),
            logo_size_ratio=0.25,
            color_mask=config["color_mask"],
        )

    print("\nAll QR codes generated successfully!")


if __name__ == "__main__":
    main()
