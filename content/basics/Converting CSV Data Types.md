---
title: Converting Csv Data Types
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
        age = int(row["age"])
        salary = float(row["salary"])
        print(age, salary)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[1], line 7
          5 for row in reader:
          6     age = int(row["age"])
    ----> 7     salary = float(row["salary"])
          8     print(age, salary)
    

    KeyError: 'salary'



```python

```


---
**Score: 0**