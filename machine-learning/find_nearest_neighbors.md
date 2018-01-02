Title: Find Nearest Neighbors  
Slug: find_nearest_neighbors  
Summary: Find a observation's nearest neighbors in scikit-learn.  
Date: 2017-09-19 12:00  
Category: Machine Learning  
Tags: Nearest Neighbors  
Authors: Chris Albon  

## Preliminaries


```python
# Load libraries
from sklearn.neighbors import NearestNeighbors
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np
```

## Load Iris Dataset


```python
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## Standardize Iris Data

It is important to standardize our data before we calculate any distances.


```python
# Create standardizer
standardizer = StandardScaler()

# Standardize features
X_std = standardizer.fit_transform(X)
```

## Find Each Observation's Two Nearest Neighbors


```python
# Find three nearest neighbors based on euclidean distance (including itself)
nn_euclidean = NearestNeighbors(n_neighbors=3, metric='euclidean').fit(X)

# List of lists indicating each observation's 3 nearest neighors
nearest_neighbors_with_self = nn_euclidean.kneighbors_graph(X).toarray()

# Remove 1's marking an observation is nearest to itself 
for i, x in enumerate(nearest_neighbors_with_self):
    x[i] = 0
```

## Show nearest neighbors


```python
# View first observation's two nearest neighbors
nearest_neighbors_with_self[0]
```




    array([ 0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
            0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
            0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
            0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
            0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
            0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
            0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
            0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
            0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
            0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
            0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
            0.,  0.,  0.,  0.,  0.,  0.,  0.])


