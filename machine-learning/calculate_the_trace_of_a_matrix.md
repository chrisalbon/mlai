Title: Calculate The Trace Of A Matrix   
Slug: calculate_the_trace_of_a_matrix     
Summary: How to calculate the trace of a matrix in Python.     
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

## Calculate The Trace


```python
# Calculate the tracre of the matrix
matrix.diagonal().sum()
```




    15


