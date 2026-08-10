---
title: Optimizing Recursion With Memoization
date: 2026-08-10
author: Your Name
cell_count: 2
score: 10
---

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))  # Optimized recursion
```

    832040



```python

```


---
**Score: 10**