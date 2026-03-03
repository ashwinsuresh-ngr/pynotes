---
title: Accessing Specific Columns
date: 2026-03-03
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])
```

    Alice 25
    Bob 30
    


```python

```


---
**Score: 0**