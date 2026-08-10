---
title: Multilevel Inheritance
date: 2026-08-10
author: Your Name
cell_count: 2
score: 10
---

```python
class Grandparent:
    def feature(self):
        print("Grandparent feature")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.feature()
```

    Grandparent feature



```python

```


---
**Score: 10**