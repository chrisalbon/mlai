Title: Calculate The Determinant Of A Matrix   
Slug: calculate_the_determinant_of_a_matrix     
Summary: How to calculate the determinant of a matrix in Python.     
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

## Calculate Determinant


```python
# Return determinant of matrix
np.linalg.det(matrix)
```




    -9.5161973539299405e-16


