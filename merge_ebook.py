# -*- coding: utf-8 -*-
"""Merge all markdown chapters into a single ebook file."""

import os
from pathlib import Path


def merge_ebook():
    # Find the ebook directory
    base_dir = Path(r"D:/python_workspace")
    ebook_dir = None

    for root, dirs, files in os.walk(base_dir):
        if "newone_e-book" in root and root.endswith("newone_e-book"):
            ebook_dir = Path(root) / "小白程式入門電子書"
            break

    if not ebook_dir or not ebook_dir.exists():
        print("Error: Cannot find ebook directory")
        return

    print(f"Found ebook directory: {ebook_dir}")

    # Define chapter order
    chapter_order = [
        "00_目錄.md",
        "第1章_程式到底是什麼.md",
        "第2章_程式語言大觀園.md",
        "第3章_像電腦一樣思考.md",
        "第4章_資料與變數.md",
        "第5章_自動化你的生活.md",
        "第6章_創造你的第一個專案.md",
        "第7章_程式設計的職業道路.md",
        "第8章_學習資源與社群.md",
        "第9章_學習程式的正確心態.md",
        "第10章_從零到一的行動計畫.md",
        "11_加入我們.md",
    ]

    # Merge all chapters
    merged_content = []

    # Add ebook header
    header = """# 小白程式入門電子書

**從零開始，用故事帶你踏入程式世界**

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

            # Add page break between chapters (except for TOC)
            if i > 0:
                merged_content.append("\n\n---\n\n<div style=\"page-break-after: always;\"></div>\n\n---\n\n")

            merged_content.append(content)
            print(f"[OK] Added: {chapter_file}")
        else:
            print(f"[MISS] Missing: {chapter_file}")

    # Write merged file
    output_path = ebook_dir.parent / "小白程式入門電子書_完整版.md"

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
