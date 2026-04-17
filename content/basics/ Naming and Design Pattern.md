---
title:  Naming And Design Pattern
date: 2026-04-17
author: Your Name
cell_count: 1
score: 0
---

```python
class InvalidOrderStateError(Exception):
    """Raised when an order is in an invalid processing state"""
    pass

def process_order(status):
    if status != "confirmed":
        raise InvalidOrderStateError("Order must be confirmed before processing")

process_order("draft")
```


---
**Score: 0**