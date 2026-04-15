---
title: Writing Csv Using Panda
date: 2026-04-15
author: Your Name
cell_count: 2
score: 0
---

```python
import pandas as pd

data = {
    "name": ["Alice", "Bob"],
    "age": [25, 30],
    "city": ["Paris", "London"]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
```


```python

```


---
**Score: 0**