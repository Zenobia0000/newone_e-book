# -*- coding: utf-8 -*-
"""Generate QR codes with embedded logo."""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask, VerticalGradiantColorMask
from PIL import Image
from pathlib import Path


# Brand colors
LINE_GREEN = (6, 199, 85)        # #06C755
IG_PURPLE = (131, 58, 180)       # #833AB4
IG_PINK = (225, 48, 108)         # #E1306C
IG_ORANGE = (253, 175, 69)       # #FDAF45
WHITE = (255, 255, 255)


def generate_qrcode_with_logo(
    url: str,
    output_path: str,
    logo_path: str,
    logo_size_ratio: float = 0.25,
    color_mask=None
) -> None:
    """Generate a QR code with an embedded logo.

    Args:
        url: The URL to encode in the QR code
        output_path: Path to save the generated QR code
        logo_path: Path to the logo image
        logo_size_ratio: Logo size relative to QR code (default 0.25)
        color_mask: Color mask for styling the QR code
    """
    # Create QR code with high error correction for logo embedding
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Generate QR code image with rounded modules and custom colors
    make_kwargs = {
        "image_factory": StyledPilImage,
        "module_drawer": RoundedModuleDrawer(),
    }
    if color_mask:
        make_kwargs["color_mask"] = color_mask

    qr_img = qr.make_image(**make_kwargs).convert('RGBA')

    # Load and resize logo
    logo = Image.open(logo_path).convert('RGBA')

    qr_width, qr_height = qr_img.size
    logo_max_size = int(qr_width * logo_size_ratio)

    # Maintain aspect ratio
    logo_ratio = logo.width / logo.height
    if logo_ratio > 1:
        new_width = logo_max_size
        new_height = int(logo_max_size / logo_ratio)
    else:
        new_height = logo_max_size
        new_width = int(logo_max_size * logo_ratio)

    logo_resized = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Calculate position to center the logo
    pos_x = (qr_width - new_width) // 2
    pos_y = (qr_height - new_height) // 2

    # Paste logo onto QR code
    qr_img.paste(logo_resized, (pos_x, pos_y), logo_resized)

    # Save result
    qr_img.save(output_path, 'PNG')
    print(f"QR code saved: {output_path}")


def main():
    base_dir = Path(r"D:\python_workspace\電子書\newone_e-book")
    logo_path = base_dir / "logo_main.png"

    # LINE QR code - solid green
    line_color = SolidFillColorMask(
        back_color=WHITE,
        front_color=LINE_GREEN
    )

    # Instagram QR code - gradient from purple to orange
    ig_color = VerticalGradiantColorMask(
        back_color=WHITE,
        top_color=IG_PURPLE,
        bottom_color=IG_ORANGE
    )

    # QR code configurations
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
    ]

    for config in qr_configs:
        output_path = base_dir / config["filename"]
        generate_qrcode_with_logo(
            url=config["url"],
            output_path=str(output_path),
            logo_path=str(logo_path),
            logo_size_ratio=0.25,
            color_mask=config["color_mask"]
        )

    print("\nAll QR codes generated successfully!")


if __name__ == "__main__":
    main()
