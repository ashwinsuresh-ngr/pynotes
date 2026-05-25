# Score System

## How Scores Work

Scores are automatically calculated based on the number of code cells in each notebook:

- **Formula**: `cell_count * 5`
- **Each cell = 5 points**

### Examples:
- 0 cells → Score: 0
- 1 cell → Score: 5
- 2 cells → Score: 10
- 3 cells → Score: 15
- 5 cells → Score: 25
- 10 cells → Score: 50

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
