Title: Basic Operations With Numpy Array  
Slug: numpy_array_basic_operations  
Summary: Basic Operations With Numpy Array  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  


```python
# Import modules
import numpy as np
```


```python
# Create an array
civilian_deaths = np.array([4352, 233, 3245, 256, 2394])
civilian_deaths
```




    array([4352,  233, 3245,  256, 2394])




```python
# Mean value of the array
civilian_deaths.mean()
```




    2096.0




```python
# Total amount of deaths
civilian_deaths.sum()
```




    10480




```python
# Smallest value in the array
civilian_deaths.min()
```




    233




```python
# Largest value in the array
civilian_deaths.max()
```




    4352


