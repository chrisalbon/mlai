Title: Transpose A Vector Or Matrix    
Slug: transpose_a_vector_or_matrix   
Summary: How to transpose a vector or matrix in Python.     
Date: 2017-09-02 12:00  
Category: Machine Learning  
Tags: Vectors Matrices Arrays  
Authors: Chris Albon 

## Preliminaries


```python
# Load library
import numpy as np
```

## Create Vector


```python
# Create vector
vector = np.array([1, 2, 3, 4, 5, 6])
```

## Create Matrix


```python
# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
```

## Transpose Vector


```python
# Tranpose vector
vector.T
```




    array([1, 2, 3, 4, 5, 6])



## Transpose Matrix


```python
# Transpose matrix
matrix.T
```




    array([[1, 4, 7],
           [2, 5, 8],
           [3, 6, 9]])


