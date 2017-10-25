Title: argmin and argmax  
Slug: argmin_and_argmax  
Summary: An explanation of argmin and argmax in Python.    
Date: 2016-01-23 12:00  
Category: Mathematics  
Tags: Basics    
Authors: Chris Albon  

`argmin` and `argmax` are the inputs, `x`'s, to a function, `f`, that creates the smallest and largest outputs, `f(x)`.

## Preliminaries


```python
import numpy as np
import pandas as pd
np.random.seed(1)
```

## Define A Function, f(x)


```python
# Define a function that,
def f(x):
    # Outputs x multiplied by a random number drawn from a normal distribution
    return x * np.random.normal(size=1)[0]
```

## Create Some Values Of x


```python
# Create some values of x
xs = [1,2,3,4,5,6]
```

## Find The Argmin Of f(x)


```python
#Define argmin that
def argmin(f, xs):
    # Applies f on all the x's
    data = [f(x) for x in xs]

    # Finds index of the smallest output of f(x)
    index_of_min = data.index(min(data))
        
    # Returns the x that produced that output
    return xs[index_of_min]
```


```python
# Run the argmin function
argmin(f, xs)
```




    6



## Check Our Results


```python
print('x','|', 'f(x)')
print('--------------')
for x in xs:
    print(x,'|', f(x))
```

    x | f(x)
    --------------
    1 | 1.74481176422
    2 | -1.52241380179
    3 | 0.957117288171
    4 | -0.99748150191
    5 | 7.31053968522
    6 | -12.360844257

