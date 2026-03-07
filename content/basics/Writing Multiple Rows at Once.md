---
title: Writing Multiple Rows At Once
date: 2026-03-07
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

data = [
    ["John", 28, "Toronto"],
    ["Emma", 35, "Berlin"]
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```


```python

```


---
**Score: 0**