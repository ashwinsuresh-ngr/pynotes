---
title: Reading Csv With Error Handling
date: 2026-04-17
author: Your Name
cell_count: 1
score: 0
---

```python
import csv

try:
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found.")
```


---
**Score: 0**