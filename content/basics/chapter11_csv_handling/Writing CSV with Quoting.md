---
title: Writing Csv With Quoting
date: 2026-08-10
author: Your Name
cell_count: 2
score: 10
---

```python
import csv

with open("quotes.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["Alice", "Software Engineer", "New York"])
```


```python

```


---
**Score: 10**