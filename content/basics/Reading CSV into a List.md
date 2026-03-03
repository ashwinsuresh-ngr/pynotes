---
title: Reading Csv Into A List
date: 2026-03-04
author: Your Name
cell_count: 1
score: 0
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

print(data)
```


---
**Score: 0**