---
title: Basic Csv Reading With Csv.Reader
date: 2026-08-10
author: Your Name
cell_count: 1
score: 5
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```


---
**Score: 5**