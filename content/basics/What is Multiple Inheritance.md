---
title: What Is Multiple Inheritance
date: 2026-03-07
author: Your Name
cell_count: 2
score: 0
---

```python
class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()
```

    Driving
    Cooking
    


```python

```


---
**Score: 0**