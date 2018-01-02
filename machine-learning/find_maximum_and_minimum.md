Title: Find The Maximum And Minimum
Slug: find_maximum_and_minimum  
Summary: How to find the maximum, minimum, and average of the elements in an array.     
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

## Find Maximum Element


```python
# Return maximum element
np.max(matrix)
```




    9



## Find Minimum Element


```python
# Return minimum element
np.min(matrix)
```




    1



## Find Maximum Element By Column


```python
# Find the maximum element in each column
np.max(matrix, axis=0)
```




    array([7, 8, 9])



## Find Maximum Element By Row


```python
# Find the maximum element in each row
np.max(matrix, axis=1)
```




    array([3, 6, 9])


