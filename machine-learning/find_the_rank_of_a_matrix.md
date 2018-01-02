Title: Find The Rank Of A Matrix  
Slug: find_the_rank_of_a_matrix     
Summary: How to find the rank of a matrix in Python.     
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

## Find Rank Of Matrix


```python
# Return matrix rank
np.linalg.matrix_rank(matrix)
```




    2


