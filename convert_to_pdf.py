# -*- coding: utf-8 -*-
"""Convert Markdown files to PDF with images and Chinese support."""

import os
import re
import base64
from pathlib import Path

import markdown
from xhtml2pdf import pisa


# CSS for PDF styling with Chinese font support
PDF_CSS = """
@page {
    size: A4;
    margin: 2cm;
}

body {
    font-family: SimHei;
    font-size: 11pt;
    line-height: 1.8;
    color: #333;
}

h1 {
    font-family: SimHei;
    font-size: 24pt;
    color: #1a2a3a;
    padding-bottom: 8px;
    margin-top: 30px;
}

h2 {
    font-family: SimHei;
    font-size: 18pt;
    color: #1a2a3a;
    margin-top: 25px;
    padding-left: 12px;
}

h3 {
    font-size: 14pt;
    color: #333;
    margin-top: 20px;
}

p {
    margin: 12px 0;
    text-align: justify;
}

blockquote {
    padding: 10px 15px;
    margin: 15px 0;
    background: #f8f9fa;
    font-style: italic;
    color: #555;
}

code {
    background: #f4f4f4;
    padding: 2px 5px;
    font-family: Consolas, monospace;
    font-size: 9pt;
}

pre {
    background: #2d2d2d;
    color: #f8f8f2;
    padding: 15px;
    overflow-x: auto;
    font-size: 9pt;
    line-height: 1.4;
    margin: 15px 0;
}

pre code {
    background: transparent;
    padding: 0;
    color: inherit;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 15px auto;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
    font-size: 10pt;
}

th, td {
    padding: 8px;
    text-align: left;
}

th {
    background: #1a2a3a;
    color: white;
}

tr:nth-child(even) {
    background: #f9f9f9;
}

ul, ol {
    margin: 12px 0;
    padding-left: 25px;
}

li {
    margin: 6px 0;
}

hr {
    margin: 25px 0;
    height: 1px;
    background: #ddd;
}

strong {
    color: #1a2a3a;
}

a {
    color: #4dc7af;
    text-decoration: none;
}
"""


def find_ebook_dir():
    """Find the ebook directory."""
    base_dir = Path(r"D:/python_workspace")

    for root, dirs, files in os.walk(base_dir):
        if "newone_e-book" in root and root.endswith("newone_e-book"):
            return Path(root)

    return None


def embed_images(html_content: str, base_path: Path) -> str:
    """Convert image paths to base64 embedded images."""

    def replace_img(match):
        img_tag = match.group(0)
        src_match = re.search(r'src="([^"]+)"', img_tag)

        if not src_match:
            return img_tag

        src = src_match.group(1)

        # Skip if already base64 or http
        if src.startswith('data:') or src.startswith('http'):
            return img_tag

        # Resolve image path
        img_path = base_path / src

        if not img_path.exists():
            print(f"  [WARN] Image not found: {src}")
            return img_tag

        # Read and encode image
        try:
            with open(img_path, 'rb') as f:
                img_data = base64.b64encode(f.read()).decode('utf-8')

            # Determine mime type
            ext = img_path.suffix.lower()
            mime_types = {
                '.png': 'image/png',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.gif': 'image/gif',
            }
            mime = mime_types.get(ext, 'image/png')

            # Replace src with base64
            new_src = f'data:{mime};base64,{img_data}'
            new_tag = img_tag.replace(f'src="{src}"', f'src="{new_src}"')

            print(f"  [OK] Embedded: {src}")
            return new_tag

        except Exception as e:
            print(f"  [ERR] {src}: {e}")
            return img_tag

    return re.sub(r'<img[^>]+>', replace_img, html_content)


def convert_md_to_pdf(md_path: Path, output_path: Path):
    """Convert a Markdown file to PDF."""

    print(f"\nConverting: {md_path.name}")
    print("-" * 50)

    # Read markdown content
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    md_converter = markdown.Markdown(
        extensions=['tables', 'fenced_code', 'toc']
    )
    html_body = md_converter.convert(md_content)

    # Create full HTML document
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>{md_path.stem}</title>
        <style>
            {PDF_CSS}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    # Embed images as base64
    base_path = md_path.parent
    html_content = embed_images(html_content, base_path)

    # Convert to PDF using xhtml2pdf
    print("  Generating PDF...")

    try:
        with open(output_path, 'wb') as pdf_file:
            pisa_status = pisa.CreatePDF(
                html_content.encode('utf-8'),
                dest=pdf_file,
                encoding='utf-8'
            )

        if pisa_status.err:
            print(f"  [ERROR] PDF generation had errors")
        else:
            size_mb = output_path.stat().st_size / (1024 * 1024)
            print(f"  [DONE] Saved: {output_path.name}")
            print(f"  Size: {size_mb:.2f} MB")

    except Exception as e:
        print(f"  [ERROR] {e}")


def main():
    ebook_dir = find_ebook_dir()

    if not ebook_dir:
        print("Error: Cannot find ebook directory")
        return

    print(f"Ebook directory: {ebook_dir}")

    # Files to convert
    files_to_convert = [
        ebook_dir / "小白程式入門電子書_完整版_含圖.md",
        ebook_dir / "VibeCoding全心法" / "VibeCoding全心法.md",
    ]

    # Output directory
    output_dir = ebook_dir / "PDF"
    output_dir.mkdir(exist_ok=True)

    # Convert each file
    for md_path in files_to_convert:
        if md_path.exists():
            output_path = output_dir / f"{md_path.stem}.pdf"
            convert_md_to_pdf(md_path, output_path)
        else:
            print(f"\n[SKIP] File not found: {md_path.name}")

    print("\n" + "=" * 50)
    print(f"[COMPLETE] PDFs saved to: {output_dir}")


if __name__ == "__main__":
    main()
