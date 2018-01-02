Title: Create Interaction Features  
Slug: create_interaction_features     
Summary: How to create interaction features for machine learning in Python.   
Date: 2016-09-06 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
```

## Create Feature Matrix


```python
# Create feature matrix
X = np.array([[2, 3], 
              [2, 3], 
              [2, 3]])
```

## Add Interaction Features


```python
# Create PolynomialFeatures object with interaction_only set to True
interaction = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)

# Transform feature matrix
interaction.fit_transform(X)
```




    array([[ 2.,  3.,  6.],
           [ 2.,  3.,  6.],
           [ 2.,  3.,  6.]])


