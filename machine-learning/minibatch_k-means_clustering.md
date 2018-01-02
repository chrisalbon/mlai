Title: Mini-Batch k-Means Clustering  
Slug: minibatch_k-means_clustering  
Summary: How to conduct mini-batch k-means clustering in scikit-learn.  
Date: 2017-09-22 12:00  
Category: Machine Learning  
Tags: Clustering  
Authors: Chris Albon  

Mini-batch k-means works similarly to the k-means algorithm discussed in the last recipe. Without going into too much detail, the difference is that in mini-batch k-means the most computationally costly step is conducted on only a random sample of observations as opposed to all observations. This approach can significantly reduce the time required for the algorithm to find convergence (i.e. fit the data) with only a small cost in quality.

## Preliminaries


```python
# Load libraries
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MiniBatchKMeans
```

## Load Iris Flower Dataset


```python
# Load data
iris = datasets.load_iris()
X = iris.data
```

## Standardize Features


```python
# Standarize features
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
```

## Conduct k-Means Clustering

`MiniBatchKMeans` works similarly to `KMeans`, with one significance difference: the `batch_size` parameter. `batch_size` controls the number of randomly selected observations in each batch. The larger the the size of the batch, the more computationally costly the training process.


```python
# Create k-mean object
clustering = MiniBatchKMeans(n_clusters=3, random_state=0, batch_size=100)

# Train model
model = clustering.fit(X_std)
```
