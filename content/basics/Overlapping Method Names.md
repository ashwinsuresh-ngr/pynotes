---
title: Overlapping Method Names
date: 2026-04-17
author: Your Name
cell_count: 2
score: 10
---

```python
class A:
    def display(self):
        print("From A")

class B:
    def display(self):
        print("From B")

class C(A, B):
    pass

obj = C()
obj.display()
```

    From A



```python

```


---
**Score: 10**