---
title:  Global Keyword Inside Nested Functions
date: 2026-03-03
author: Your Name
cell_count: 2
score: 0
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
**Score: 0**