Title: Getting The Diagonal Of A Matrix   
Slug: getting_the_diagonal_of_a_matrix     
Summary: How to get the diagonal of a matrix in Python.     
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

## Get The Diagonal


```python
# Return diagonal elements
matrix.diagonal()
```




    array([1, 5, 9])



## Calculate The Trace


```python
# Calculate the tracre of the matrix
matrix.diagonal().sum()
```




    15


