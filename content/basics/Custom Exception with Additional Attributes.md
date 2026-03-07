---
title: Custom Exception With Additional Attributes
date: 2026-03-07
author: Your Name
cell_count: 1
score: 0
---

```python
class TransactionError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")

raise TransactionError(403, "Unauthorized action")
```


---
**Score: 0**