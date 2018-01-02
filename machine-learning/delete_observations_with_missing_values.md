Title: Delete Observations With Missing Values    
Slug: delete_observations_with_missing_values   
Summary: How to delete observations with missing values.     
Date: 2017-09-05 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon 

## Preliminaries


```python
# Load libraries
import numpy as np
import pandas as pd
```

## Create Feature Matrix


```python
# Create feature matrix
X = np.array([[1.1, 11.1], 
              [2.2, 22.2], 
              [3.3, 33.3], 
              [4.4, 44.4], 
              [np.nan, 55]])
```

## Delete Observations With Missing Values


```python
# Remove observations with missing values
X[~np.isnan(X).any(axis=1)]
```




    array([[  1.1,  11.1],
           [  2.2,  22.2],
           [  3.3,  33.3],
           [  4.4,  44.4]])


