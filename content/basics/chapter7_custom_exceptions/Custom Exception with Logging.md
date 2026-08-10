---
title: Custom Exception With Logging
date: 2026-08-10
author: Your Name
cell_count: 2
score: 10
---

```python
class DataValidationError(Exception):
    pass

try:
    raise DataValidationError("Invalid CSV column format")
except DataValidationError as e:
    print("Validation Error Logged:", e)
```

    Validation Error Logged: Invalid CSV column format



```python

```


---
**Score: 10**