---
title: Using Custom Exceptions In Functions
date: 2026-04-15
author: Your Name
cell_count: 1
score: 0
---

```python
class FileMissingError(Exception):
    pass

def load_config(filename):
    if not filename.endswith(".json"):
        raise FileMissingError("Only JSON configuration files supported")

load_config("config.txt")
```


---
**Score: 0**