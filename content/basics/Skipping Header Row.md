---
title: Skipping Header Row
date: 2026-04-17
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        print(row)
```

    ['Alice', '25', 'Paris']
    ['Bob', '30', 'London']



```python

```


---
**Score: 0**