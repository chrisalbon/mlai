Title: Create A Sparse Matrix  
Slug: create_a_sparse_matrix     
Summary: How to create a sparse matrix in Python.     
Date: 2017-09-03 12:00  
Category: Machine Learning  
Tags: Vectors Matrices Arrays  
Authors: Chris Albon 

## Preliminaries


```python
# Load libraries
import numpy as np
from scipy import sparse
```

## Create Dense Matrix


```python
# Create a matrix
matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])
```

## Convert To Sparse Matrix


```python
# Create compressed sparse row (CSR) matrix
matrix_sparse = sparse.csr_matrix(matrix)
```

Note: There are many types of sparse matrices. In the example above we use CSR but the type we use should reflect our use case.
