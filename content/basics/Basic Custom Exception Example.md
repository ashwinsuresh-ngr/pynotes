---
title: Basic Custom Exception Example
date: 2026-03-03
author: Your Name
cell_count: 1
score: 0
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
**Score: 0**