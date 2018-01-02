Title: Calculate The Average, Variance, And Standard Deviation     
Slug: calculate_average_variance_and_standard_deviation   
Summary: How to calculate the average, variance, and standard deviation of an array in Python.     
Date: 2017-09-04 12:00  
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

## Calculate Mean


```python
# Return mean
np.mean(matrix)
```




    5.0



## Calculate Variance


```python
# Return variance
np.var(matrix)
```




    6.666666666666667



## Calculate Standard Deviation


```python
# Return standard deviation
np.std(matrix)
```




    2.5819888974716112


