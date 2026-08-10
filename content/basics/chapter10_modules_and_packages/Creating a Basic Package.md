---
title: Creating A Basic Package
date: 2026-08-10
author: Your Name
cell_count: 2
score: 10
---

```python
# my_package/module1.py
def greet():
    return "Hello from module1"


```


```python
# main.py
import my_package.module1

print(my_package.module1.greet())
```


---
**Score: 10**