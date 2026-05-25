# Score System

## How Scores Work

Scores are automatically calculated based on the number of code cells in each notebook:

- **Formula**: `(cell_count // 5) * 5`
- **Minimum**: 0 points (for notebooks with less than 5 cells)
- **Increment**: 5 points for every 5 cells

### Examples:
- 0-4 cells → Score: 0
- 5-9 cells → Score: 5
- 10-14 cells → Score: 10
- 15-19 cells → Score: 15

## Updating Scores

### Automatic (during build)
When you run `make.py`, scores are automatically calculated for newly converted notebooks.

### Manual Update
To recalculate scores for all existing markdown files:

```bash
python3 update_scores.py
```

This will:
1. Read the `cell_count` from each markdown file's metadata
2. Calculate the score using the formula above
3. Update both the metadata (`score: X`) and content (`**Score: X**`)

### After Updating
Rebuild the site to see changes:

```bash
pelican content -o docs -s pelicanconf.py
git add -A
git commit -m "Update scores"
git push
```

## Current Scores

Run this to see all non-zero scores:

```bash
grep -h "^score: [1-9]" content/**/*.md | sort | uniq -c
```

## Overall Score

The archives page (`/archives.html`) displays the total score across all articles.
