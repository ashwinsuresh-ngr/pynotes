---
title: Global Variable Across Multiple Functions
date: 2026-08-10
author: Your Name
cell_count: 2
score: 10
---

```python
status = "inactive"

def activate():
    global status
    status = "active"

def show_status():
    print(status)

activate()
show_status()  # Output: active
```

    active



```python

```


---
**Score: 10**