Title: Cartesian Product  
Slug: cartesian_product  
Summary: Cartesian Product  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

## Preliminaries


```python
# import pandas as pd
import pandas as pd
```

## Create Data


```python
# Create two lists
i = [1,2,3,4,5]
j = [1,2,3,4,5]
```

## Calculate Cartesian Product (Method 1)


```python
# List every single x in i with every single y (i.e. Cartesian product)
[(x, y) for x in i for y in j]
```




    [(1, 1),
     (1, 2),
     (1, 3),
     (1, 4),
     (1, 5),
     (2, 1),
     (2, 2),
     (2, 3),
     (2, 4),
     (2, 5),
     (3, 1),
     (3, 2),
     (3, 3),
     (3, 4),
     (3, 5),
     (4, 1),
     (4, 2),
     (4, 3),
     (4, 4),
     (4, 5),
     (5, 1),
     (5, 2),
     (5, 3),
     (5, 4),
     (5, 5)]



## Calculate Cartesian Product (Method 2)


```python
# An alternative way to do the cartesian product

# import itertools
import itertools

# for two sets, find the the cartisan product
for i in itertools.product([1,2,3,4,5], [1,2,3,4,5]):
    # and print it
    print(i)
```

    (1, 1)
    (1, 2)
    (1, 3)
    (1, 4)
    (1, 5)
    (2, 1)
    (2, 2)
    (2, 3)
    (2, 4)
    (2, 5)
    (3, 1)
    (3, 2)
    (3, 3)
    (3, 4)
    (3, 5)
    (4, 1)
    (4, 2)
    (4, 3)
    (4, 4)
    (4, 5)
    (5, 1)
    (5, 2)
    (5, 3)
    (5, 4)
    (5, 5)

