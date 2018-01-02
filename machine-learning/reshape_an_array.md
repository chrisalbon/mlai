Title: Reshape An Array
Slug: reshape_an_array   
Summary: How to reshape a NumPy array.     
Date: 2017-09-04 12:00  
Category: Machine Learning  
Tags: Vectors Matrices Arrays  
Authors: Chris Albon 

## Preliminaries


```python
# Load library
import numpy as np
```

## Create Array


```python
# Create a 4x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])
```

## Reshape Array


```python
# Reshape matrix into 2x6 matrix
matrix.reshape(2, 6)
```




    array([[ 1,  2,  3,  4,  5,  6],
           [ 7,  8,  9, 10, 11, 12]])


