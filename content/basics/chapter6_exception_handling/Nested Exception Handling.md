---
title: Nested Exception Handling
date: 2026-08-10
author: Your Name
cell_count: 2
score: 10
---

```python
try:
    try:
        x = int("abc")
    except ValueError:
        print("Inner exception handled")
except Exception:
    print("Outer exception handler")
```

    Inner exception handled



```python

```


---
**Score: 10**