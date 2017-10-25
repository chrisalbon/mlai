Title: Discretize Features  
Slug: discretize_features     
Summary: How to discretize features for machine learning in Python.   
Date: 2016-09-06 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
from sklearn.preprocessing import Binarizer
import numpy as np
```

## Create Data


```python
# Create feature
age = np.array([[6], 
                [12], 
                [20], 
                [36], 
                [65]])
```

## Option 1: Binarize Feature


```python
# Create binarizer
binarizer = Binarizer(18)

# Transform feature
binarizer.fit_transform(age)
```




    array([[0],
           [0],
           [1],
           [1],
           [1]])



## Option 2: Break Up Feature Into Bins


```python
# Bin feature
np.digitize(age, bins=[20,30,64])
```




    array([[0],
           [0],
           [1],
           [2],
           [3]])


