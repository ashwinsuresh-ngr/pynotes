---
title: Modern File Handling With Pathlib
date: 2026-03-04
author: Your Name
cell_count: 1
score: 0
---

```python
from pathlib import Path

file_path = Path("example.txt")

file_path.write_text("Using pathlib module")
print(file_path.read_text())

s(file_path.exists())
print(file_path.parent)
```

    Using pathlib module
    True
    .
    


---
**Score: 0**