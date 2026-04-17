---
title: Reading Csv With Custom Delimiter
date: 2026-04-17
author: Your Name
cell_count: 1
score: 0
---

```python
import csv

with open("data_pipe.csv", "r") as file:
    reader = csv.reader(file, delimiter="|")
    for row in reader:
        print(row)
```


---
**Score: 0**