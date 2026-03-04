---
title: Basic Csv Writing With Csv.Writer
date: 2026-03-04
author: Your Name
cell_count: 1
score: 0
---

```python
import csv

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["Alice", 25, "New York"])
```


---
**Score: 0**