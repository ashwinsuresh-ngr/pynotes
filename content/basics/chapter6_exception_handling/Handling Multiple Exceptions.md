---
title: Handling Multiple Exceptions
date: 2026-08-10
author: Your Name
cell_count: 2
score: 10
---

```python
try:
    value = int("abc")
except ValueError:
    print("Invalid conversion")
except ZeroDivisionError:
    print("Division error")
```

    Invalid conversion



```python

```


---
**Score: 10**