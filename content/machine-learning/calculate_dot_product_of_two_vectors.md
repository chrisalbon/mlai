Title: Calculate Dot Product Of Two Vectors    
Slug: calculate_dot_product_of_two_vectors   
Summary: How to calculate the dot product of two vectors in Python.     
Date: 2017-09-02 12:00  
Category: Machine Learning  
Tags: Vectors Matrices Arrays  
Authors: Chris Albon 

## Preliminaries


```python
# Load library
import numpy as np
```

## Create Two Vectors


```python
# Create two vectors
vector_a = np.array([1,2,3])
vector_b = np.array([4,5,6])
```

## Calculate Dot Product (Method 1)


```python
# Calculate dot product
np.dot(vector_a, vector_b)
```




    32



## Calculate Dot Product (Method 2)


```python
# Calculate dot product
vector_a @ vector_b
```




    32


