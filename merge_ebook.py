# -*- coding: utf-8 -*-
"""Merge all markdown chapters into a single ebook file."""

import os
from pathlib import Path


def merge_ebook():
    # Define the ebook directory
    ebook_dir = Path("/mnt/d/python_workspace/電子書/newone_e-book/VibeCoding全心法")

    if not ebook_dir.exists():
        print(f"Error: Cannot find ebook directory at {ebook_dir}")
        return

    print(f"Found ebook directory: {ebook_dir}")

    # Define chapter order
    chapter_order = [
        "00_前言.md",
        "01_典範轉移.md",
        "02_上下文工程.md",
        "03_風險控制.md",
        "04_學習路徑.md",
        "05_未來趨勢.md",
        "06_結論.md",
        "07_附錄.md",
        "08_關於作者.md",
    ]

    # Merge all chapters
    merged_content = []

    # Add ebook header
    header = """# VibeCoding全心法

**駕馭 AI 協作的開發者生存指南**

---

**作者**：桑尼資料科學 | Data Sunnie

**版本**：1.0

---

"""
    merged_content.append(header)

    # Read and merge each chapter
    for i, chapter_file in enumerate(chapter_order):
        chapter_path = ebook_dir / chapter_file

        if chapter_path.exists():
            with open(chapter_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Add page break between chapters
            if i > 0:
                merged_content.append("\n\n---\n\n<div style=\"page-break-after: always;\"></div>\n\n---\n\n")

            # Remove title from each chapter file content
            content_lines = content.split('\n')
            if content_lines and content_lines[0].startswith('# '):
                content = '\n'.join(content_lines[1:]).lstrip()


            merged_content.append(content)
            print(f"[OK] Added: {chapter_file}")
        else:
            print(f"[MISS] Missing: {chapter_file}")

    # Write merged file
    output_path = ebook_dir / "VibeCoding全心法.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("".join(merged_content))

    print(f"\n[DONE] Merged ebook saved to: {output_path}")

    # Count stats
    total_chars = len("".join(merged_content))
    total_lines = "".join(merged_content).count("\n")
    print(f"  Total characters: {total_chars:,}")
    print(f"  Total lines: {total_lines:,}")


if __name__ == "__main__":
    merge_ebook()