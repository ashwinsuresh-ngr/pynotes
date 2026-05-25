---
title: Reading A Csv File Using Csv.Reader
date: 2026-04-17
author: Your Name
cell_count: 2
score: 10
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

    ['name', 'age', 'city']
    ['Alice', '25', 'Paris']
    ['Bob', '30', 'London']



```python

```


---
**Score: 10**