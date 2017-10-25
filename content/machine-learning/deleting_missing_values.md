Title: Deleting Missing Values    
Slug: deleting_missing_values    
Summary: How to delete missing values.     
Date: 2017-09-02 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon 

## Preliminaries


```python
# Load library
import numpy as np
import pandas as pd
```

## Create Data Frame


```python
# Create feature matrix
X = np.array([[1, 2], 
              [6, 3], 
              [8, 4], 
              [9, 5], 
              [np.nan, 4]])
```

## Drop Missing Values Using NumPy


```python
# Remove observations with missing values
X[~np.isnan(X).any(axis=1)]
```




    array([[ 1.,  2.],
           [ 6.,  3.],
           [ 8.,  4.],
           [ 9.,  5.]])



## Drop Missing Values Using pandas


```python
# Load data as a data frame
df = pd.DataFrame(X, columns=['feature_1', 'feature_2'])

# Remove observations with missing values
df.dropna()
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>


