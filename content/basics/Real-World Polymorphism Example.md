---
title: Real-World Polymorphism Example
date: 2026-04-17
author: Your Name
cell_count: 2
score: 10
---

```python
class Notification:
    def send(self):
        print("Sending notification")

class Email(Notification):
    def send(self):
        print("Sending Email")

class SMS(Notification):
    def send(self):
        print("Sending SMS")

def notify(service):
    service.send()

notify(Email())
notify(SMS())
```

    Sending Email
    Sending SMS



```python

```


---
**Score: 10**