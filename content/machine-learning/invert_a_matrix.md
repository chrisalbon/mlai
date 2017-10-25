Title: Invert A Matrix  
Slug: invert_a_matrix     
Summary: How to invert a matrix in Python.     
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
matrix = np.array([[1, 4],
                   [2, 5]])
```

## Invert Matrix


```python
# Calculate inverse of matrix
np.linalg.inv(matrix)
```




    array([[-1.66666667,  1.33333333],
           [ 0.66666667, -0.33333333]])


