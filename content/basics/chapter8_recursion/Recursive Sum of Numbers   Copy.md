---
title: Recursive Sum Of Numbers   Copy
date: 2026-08-10
author: Your Name
cell_count: 2
score: 10
---

```python
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print(sum_n(5))  # Output: 15
```

    15



```python

```


---
**Score: 10**