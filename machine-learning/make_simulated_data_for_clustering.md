Title: Make Simulated Data For Clustering  
Slug: make_simulated_data_for_clustering  
Summary: Make a simulated dataset for clustering.  
Date: 2017-01-16 12:00  
Category: Machine Learning  
Tags: Basics  
Authors: Chris Albon   

Inspired by [Python Machine Learning](http://amzn.to/2iyMbpA)

## Preliminaries


```python
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
```

## Make Data


```python
# Make the features (X) and output (y) with 200 samples,
X, y = make_blobs(n_samples = 200,
                  # two feature variables,
                  n_features = 2,
                  # three clusters,
                  centers = 3,
                  # with .5 cluster standard deviation,
                  cluster_std = 0.5,
                  # shuffled,
                  shuffle = True)
```

## View Data


```python
# Create a scatterplot of the first and second features
plt.scatter(X[:,0],
            X[:,1])

# Show the scatterplot
plt.show()
```


![png](make_simulated_data_for_clustering_files/make_simulated_data_for_clustering_6_0.png)

