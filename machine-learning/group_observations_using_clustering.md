Title: Group Observations Using K-Means Clustering  
Slug: group_observations_using_clustering     
Summary: How to group observations using clustering for machine learning in Python.   
Date: 2016-09-06 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import pandas as pd
```

## Create Data


```python
# Make simulated feature matrix
X, _ = make_blobs(n_samples = 50,
                  n_features = 2,
                  centers = 3,
                  random_state = 1)

# Create DataFrame
df = pd.DataFrame(X, columns=['feature_1','feature_2'])
```

## Train Clusterer


```python
# Make k-means clusterer
clusterer = KMeans(3, random_state=1)

# Fit clusterer
clusterer.fit(X)
```




    KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
        n_clusters=3, n_init=10, n_jobs=1, precompute_distances='auto',
        random_state=1, tol=0.0001, verbose=0)



## Create Feature Based On Predicted Cluster


```python
# Predict values
df['group'] = clusterer.predict(X)

# First few observations
df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>feature_1</th>
      <th>feature_2</th>
      <th>group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-9.877554</td>
      <td>-3.336145</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-7.287210</td>
      <td>-8.353986</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-6.943061</td>
      <td>-7.023744</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-7.440167</td>
      <td>-8.791959</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-6.641388</td>
      <td>-8.075888</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>


