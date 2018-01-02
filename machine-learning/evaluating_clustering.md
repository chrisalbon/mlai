Title: Evaluating Clustering  
Slug: evaluating_clustering  
Summary: How to evaluate clustering models for machine learning in Python.    
Date: 2017-09-14 12:00  
Category: Machine Learning  
Tags: Model Evaluation
Authors: Chris Albon

## Preliminaries


```python
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
```

## Create Feature Data


```python
# Generate feature matrix
X, _ = make_blobs(n_samples = 1000,
                  n_features = 10,
                  centers = 2,
                  cluster_std = 0.5,
                  shuffle = True,
                  random_state = 1)
```

## Cluster Observations


```python
# Cluster data using k-means to predict classes
model = KMeans(n_clusters=2, random_state=1).fit(X)

# Get predicted classes
y_hat = model.labels_
```

## Calculate Silhouette Coefficient

Formally, the $i$th observation's silhouette coefficient is:

$$s_{i} = \frac{b_{i} - a_{i}}{\text{max}(a_{i}, b_{i})}$$

where $s_{i}$ is the silhouette coefficient for observation $i$, a_{i} is the mean distance between $i$ and all observations of the same class and b_{i} is the mean distance between $i$ and all observations from the closest cluster of a different class. The value returned by `silhouette_score` is the mean silhouette coefficient for all observations. Silhouette coefficients range between -1 and 1, with 1 indicating dense, well separated clusters.


```python
# Evaluate model
silhouette_score(X, y_hat)
```




    0.89162655640721422


