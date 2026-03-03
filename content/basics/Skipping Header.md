---
title: Skipping Header
date: 2026-03-04
author: Your Name
cell_count: 1
score: 0
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)
```


---
**Score: 0**