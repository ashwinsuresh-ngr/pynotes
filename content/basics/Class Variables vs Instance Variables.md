---
title: Class Variables Vs Instance Variables
date: 2026-04-17
author: Your Name
cell_count: 2
score: 0
---

```python
class Student:
    school = "Global Academy"  # Class variable

    def __init__(self, name):
        self.name = name        # Instance variable

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school)
print(s2.school)
```

    Global Academy
    Global Academy



```python

```


---
**Score: 0**