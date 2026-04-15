---
title: Writing Multiple Rows
date: 2026-04-15
author: Your Name
cell_count: 1
score: 0
---

```python
import csv

data = [
    ["Bob", 30, "London"],
    ["Emma", 28, "Berlin"],
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```


---
**Score: 0**