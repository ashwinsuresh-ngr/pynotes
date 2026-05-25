---
title: Using Super() To Call Parent Method
date: 2026-04-17
author: Your Name
cell_count: 2
score: 10
---

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

d = Dog()
d.sound()
```

    Animal makes sound
    Dog barks



```python

```


---
**Score: 10**