---
title:  Structured Exception Handling
date: 2026-03-03
author: Your Name
cell_count: 2
score: 0
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
**Score: 0**