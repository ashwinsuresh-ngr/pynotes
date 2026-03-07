---
title:  Changing The Working Directory
date: 2026-03-07
author: Your Name
cell_count: 2
score: 0
---

```python
import os

os.chdir("C:/Projects")
print(os.getcwd())
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[1], line 3
          1 import os
    ----> 3 os.chdir("C:/Projects")
          4 print(os.getcwd())
    

    FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:/Projects'



```python

```


---
**Score: 0**