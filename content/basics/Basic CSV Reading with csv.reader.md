---
title: Basic Csv Reading With Csv.Reader
date: 2026-04-15
author: Your Name
cell_count: 1
score: 0
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```


---
**Score: 0**