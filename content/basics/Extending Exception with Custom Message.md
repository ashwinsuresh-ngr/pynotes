---
title: Extending Exception With Custom Message
date: 2026-04-15
author: Your Name
cell_count: 1
score: 0
---

```python
class AgeLimitError(Exception):
    def __init__(self, age):
        super().__init__(f"Age {age} is below allowed limit")

def validate_age(age):
    if age < 18:
        raise AgeLimitError(age)

validate_age(15)
```


---
**Score: 0**