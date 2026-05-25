---
title: Reading Csv As Dictionary (Csv.Dictreader)
date: 2026-04-17
author: Your Name
cell_count: 1
score: 5
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])
```


---
**Score: 5**