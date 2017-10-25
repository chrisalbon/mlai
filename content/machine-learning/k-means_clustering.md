Title: k-Means Clustering  
Slug: k-means_clustering  
Summary: How to conduct k-means clustering in scikit-learn.  
Date: 2017-09-22 12:00  
Category: Machine Learning  
Tags: Clustering  
Authors: Chris Albon  

<a alt="k-Means Clustering" href="https://machinelearningflashcards.com">
    <img src="k-means_clustering/K-Means_Clustering_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load libraries
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
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


```python
# Create k-mean object
clt = KMeans(n_clusters=3, random_state=0, n_jobs=-1)

# Train model
model = clt.fit(X_std)
```

## Show Each Observation's Cluster Membership


```python
# View predict class
model.labels_
```




    array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2,
           2, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2,
           0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0,
           2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2], dtype=int32)



## Create New Observation


```python
# Create new observation
new_observation = [[0.8, 0.8, 0.8, 0.8]]
```

## Predict Observation's Cluster


```python
# Predict observation's cluster
model.predict(new_observation)
```




    array([0], dtype=int32)



## View Centers Of Each Cluster


```python
# View cluster centers
model.cluster_centers_
```




    array([[ 1.13597027,  0.09659843,  0.996271  ,  1.01717187],
           [-1.01457897,  0.84230679, -1.30487835, -1.25512862],
           [-0.05021989, -0.88029181,  0.34753171,  0.28206327]])


