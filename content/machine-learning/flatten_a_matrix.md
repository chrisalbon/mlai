Title: Flatten A Matrix   
Slug: flatten_a_matrix     
Summary: How to flatten a matrix in Python.     
Date: 2017-09-02 12:00  
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

## Flatten Matrix


```python
# Flatten matrix
matrix.flatten()
```




    array([1, 2, 3, 4, 5, 6, 7, 8, 9])


