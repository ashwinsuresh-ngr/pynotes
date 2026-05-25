---
title:  Overloading The Subtraction Operator
date: 2026-04-17
author: Your Name
cell_count: 2
score: 10
---

```python
class Balance:
    def __init__(self, amount):
        self.amount = amount

    def __sub__(self, other):
        return Balance(self.amount - other.amount)

b1 = Balance(100)
b2 = Balance(40)

result = b1 - b2
print(result.amount)  # Output: 60
```

    60



```python

```


---
**Score: 10**