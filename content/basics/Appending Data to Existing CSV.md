---
title: Appending Data To Existing Csv
date: 2026-03-03
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("users.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Charlie", 40, "Canada"])
```


```python

```


---
**Score: 0**