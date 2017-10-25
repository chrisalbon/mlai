Title: Creating Numpy Arrays  
Slug: creating_numpy_arrays  
Summary: Creating Numpy Arrays  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  


```python
# Import Modules
import numpy as np
```


```python
# Create a list
regimentSize = [534, 5468, 6546, 542, 9856, 4125]
```


```python
# Create a ndarray from the regimentSize list
regimentSizeArray = np.array(regimentSize); regimentSizeArray
```




    array([ 534, 5468, 6546,  542, 9856, 4125])




```python
# What are the number of dimensions of the array?
regimentSizeArray.ndim
```




    1




```python
# What is the shape of the array?
regimentSizeArray.shape
```




    (6,)



## Nested Lists To Multidimensional Arrays


```python
# Create two lists
regimentSizePreWar = [534, 5468, 6546, 542, 9856, 4125]
regimentSizePostWar = [234, 255, 267, 732, 235, 723]
```


```python
# Create a ndarray from a nested list
regimentSizePrePostArray = np.array([regimentSizePreWar, regimentSizePostWar]); regimentSizePrePostArray
```




    array([[ 534, 5468, 6546,  542, 9856, 4125],
           [ 234,  255,  267,  732,  235,  723]])




```python
# What are the number of dimensions of the array?
regimentSizePrePostArray.ndim
```




    2




```python
# What is the shape of the array?
regimentSizePrePostArray.shape
```




    (2, 6)


