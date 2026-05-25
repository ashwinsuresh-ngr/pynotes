---
title:  Structured Exception Handling
date: 2026-04-17
author: Your Name
cell_count: 2
score: 10
---

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero error"
    except TypeError:
        return "Invalid input type"

print(divide(10, 0))
```

    Division by zero error



```python

```


---
**Score: 10**