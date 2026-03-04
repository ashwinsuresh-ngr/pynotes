---
title:  Raising Custom Exceptions
date: 2026-03-04
author: Your Name
cell_count: 1
score: 0
---

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

validate_age(-5)
```


---
**Score: 0**