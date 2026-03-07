---
title: Writing To A Csv File Using Csv.Writer
date: 2026-03-07
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "London"])
```


```python

```


---
**Score: 0**