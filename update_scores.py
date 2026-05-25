#!/usr/bin/env python3
"""
Update scores in existing markdown files based on cell_count metadata.
Score calculation: For every 5 cells, add 5 points. Score starts at 0 if less than 5 cells.
"""

import re
from pathlib import Path


def calculate_score(cell_count):
    """
    Calculate the score based on the number of cells.
    For every 5 cells, add 5 points. Score starts at 0 if less than 5 cells.
    """
    if cell_count < 5:
        return 0
    return (cell_count // 5) * 5


def update_markdown_scores(content_dir):
    """
    Update scores in all markdown files based on their cell_count.
    """
    content_path = Path(content_dir)
    updated_count = 0
    
    for md_file in content_path.rglob("*.md"):
        # Skip hidden directories
        if any(part.startswith('.') for part in md_file.parts):
            continue
        
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Extract cell_count from metadata
        cell_count_match = re.search(r'^cell_count:\s*(\d+)', content, re.MULTILINE)
        if not cell_count_match:
            print(f"⚠️  No cell_count found in {md_file}")
            continue
        
        cell_count = int(cell_count_match.group(1))
        new_score = calculate_score(cell_count)
        
        # Update score in metadata
        content = re.sub(
            r'^score:\s*\d+',
            f'score: {new_score}',
            content,
            flags=re.MULTILINE
        )
        
        # Update score in content body (the **Score: X** line)
        content = re.sub(
            r'\*\*Score:\s*\d+\*\*',
            f'**Score: {new_score}**',
            content
        )
        
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        updated_count += 1
        print(f"✓ Updated {md_file.name}: {cell_count} cells → score {new_score}")
    
    print(f"\n✅ Updated {updated_count} markdown files")


if __name__ == "__main__":
    content_dir = "./content"
    print(f"Updating scores in {content_dir}...\n")
    update_markdown_scores(content_dir)
