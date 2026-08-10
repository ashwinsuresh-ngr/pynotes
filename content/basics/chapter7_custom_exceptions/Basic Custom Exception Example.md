---
title: Basic Custom Exception Example
date: 2026-08-10
author: Your Name
cell_count: 1
score: 5
---

```python
class NegativeValueError(Exception):
    pass

def process_value(value):
    if value < 0:
        raise NegativeValueError("Negative values are not allowed")

process_value(-10)
```


---
**Score: 5**