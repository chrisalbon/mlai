Title: Apply Operations To Elements  
Slug: apply_operations_to_elements     
Summary: How to apply operations to elements of an array in Python.    
Date: 2017-09-03 12:00  
Category: Machine Learning  
Tags: Vectors Matrices Arrays  
Authors: Chris Albon 

## Preliminaries


```python
# Load library
import numpy as np
```

## Create Matrix


```python
# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
```

## Create Vectorized Function


```python
# Create a function that adds 100 to something
add_100 = lambda i: i + 100

# Create a vectorized function
vectorized_add_100 = np.vectorize(add_100)
```

## Apply Function To Elements


```python
# Apply function to all elements in matrix
vectorized_add_100(matrix)
```




    array([[101, 102, 103],
           [104, 105, 106],
           [107, 108, 109]])


