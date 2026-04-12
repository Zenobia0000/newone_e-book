# -*- coding: utf-8 -*-
"""Merge all markdown chapters into a single ebook file.

Usage:
    python merge_chapters.py <book_dir>

Example:
    python merge_chapters.py ../../books/vibe-coding-心法
"""

import sys
from pathlib import Path

import yaml


def load_book_config(book_dir: Path) -> dict:
    """Load book.yaml from the given book directory."""
    config_path = book_dir / "book.yaml"
    if not config_path.exists():
        print(f"Error: book.yaml not found in {book_dir}")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def merge_ebook(book_dir: Path) -> None:
    """Merge chapter files into a single markdown ebook."""
    book_dir = book_dir.resolve()
    config = load_book_config(book_dir)

    chapters_dir = book_dir / "chapters"
    if not chapters_dir.exists():
        print(f"Error: chapters/ not found in {book_dir}")
        sys.exit(1)

    title = config["title"]
    subtitle = config.get("subtitle", "")
    author = config.get("author", "")
    version = config.get("version", "1.0")

    # Build header
    header = f"# {title}\n\n"
    if subtitle:
        header += f"**{subtitle}**\n\n"
    header += "---\n\n"
    if author:
        header += f"**作者**：{author}\n\n"
    header += f"**版本**：{version}\n\n---\n\n"

    merged_content = [header]

    # Read and merge each chapter
    chapter_files = config.get("chapters", [])
    for i, chapter_file in enumerate(chapter_files):
        chapter_path = chapters_dir / chapter_file
        if not chapter_path.exists():
            print(f"[MISS] Missing: {chapter_file}")
            continue

        with open(chapter_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Add page break between chapters
        if i > 0:
            merged_content.append(
                '\n\n---\n\n<div style="page-break-after: always;"></div>\n\n---\n\n'
            )

        merged_content.append(content)
        print(f"[OK] Added: {chapter_file}")

    # Write merged file
    output_dir = book_dir / "output"
    output_dir.mkdir(exist_ok=True)

    # Use title for output filename, sanitize for filesystem
    safe_title = title.replace("：", "_").replace(":", "_").replace(" ", "_")
    output_path = output_dir / f"{safe_title}.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("".join(merged_content))

    total_chars = len("".join(merged_content))
    total_lines = "".join(merged_content).count("\n")
    print(f"\n[DONE] Merged ebook saved to: {output_path}")
    print(f"  Total characters: {total_chars:,}")
    print(f"  Total lines: {total_lines:,}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python merge_chapters.py <book_dir>")
        print("Example: python merge_chapters.py ../../books/vibe-coding-心法")
        sys.exit(1)

    book_dir = Path(sys.argv[1])
    if not book_dir.exists():
        print(f"Error: directory not found: {book_dir}")
        sys.exit(1)

    merge_ebook(book_dir)


if __name__ == "__main__":
    main()
