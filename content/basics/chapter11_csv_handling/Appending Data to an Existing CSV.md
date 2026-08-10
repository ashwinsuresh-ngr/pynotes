---
title: Appending Data To An Existing Csv
date: 2026-08-10
author: Your Name
cell_count: 2
score: 10
---

```python
import csv

with open("users.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Charlie", 40, "USA"])
```


```python

```


---
**Score: 10**