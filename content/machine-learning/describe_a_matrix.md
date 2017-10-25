Title: Describe An Array  
Slug: describe_a_matrix     
Summary: How to describe an array.    
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
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
```

## View Shape


```python
# View number of rows and columns
matrix.shape
```




    (3, 4)



## View Total Elements


```python
# View number of elements (rows * columns)
matrix.size
```




    12



## View Number Of Dimensions


```python
# View number of dimensions
matrix.ndim
```




    2


