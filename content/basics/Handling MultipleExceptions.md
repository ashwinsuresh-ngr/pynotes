---
title: Handling Multipleexceptions
date: 2026-04-15
author: Your Name
cell_count: 2
score: 0
---

```python
try:
    value = int("10")
    result = value / 0
except ValueError:
    print("Conversion error")
except ZeroDivisionError:
    print("Division error")
```

    Division error



```python

```


---
**Score: 0**