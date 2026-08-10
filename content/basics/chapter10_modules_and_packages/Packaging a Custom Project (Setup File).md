---
title: Packaging A Custom Project (Setup File)
date: 2026-08-10
author: Your Name
cell_count: 1
score: 5
---

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0",
    packages=find_packages()
)
```


---
**Score: 5**