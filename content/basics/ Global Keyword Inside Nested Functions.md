---
title:  Global Keyword Inside Nested Functions
date: 2026-04-17
author: Your Name
cell_count: 2
score: 10
---

```python
x = 100

def outer():
    def inner():
        global x
        x = 400

    inner()

outer()
print(x)  
```

    400



```python

```


---
**Score: 10**