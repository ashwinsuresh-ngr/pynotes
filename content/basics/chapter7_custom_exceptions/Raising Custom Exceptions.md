---
title: Raising Custom Exceptions
date: 2026-08-10
author: Your Name
cell_count: 1
score: 5
---

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

validate_age(-5)
```


---
**Score: 5**