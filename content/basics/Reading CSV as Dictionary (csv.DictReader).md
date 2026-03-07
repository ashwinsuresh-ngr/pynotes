---
title: Reading Csv As Dictionary (Csv.Dictreader)
date: 2026-03-07
author: Your Name
cell_count: 1
score: 0
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])
```


---
**Score: 0**