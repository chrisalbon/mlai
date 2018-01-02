Title: Encoding Ordinal Categorical Features  
Slug: encoding_ordinal_categorical_features  
Summary: How to encode ordinal categorical features for machine learning in Python.   
Date: 2016-09-06 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon

## Preliminaries


```python
# Load library
import pandas as pd
```

## Create Feature Matrix


```python
# Create features
df = pd.DataFrame({'Score': ['Low', 
                             'Low', 
                             'Medium', 
                             'Medium', 
                             'High']})

# View data frame
df
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
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Low</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Low</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Medium</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Medium</td>
    </tr>
    <tr>
      <th>4</th>
      <td>High</td>
    </tr>
  </tbody>
</table>
</div>



## Create Scale Map


```python
# Create mapper
scale_mapper = {'Low':1, 
                'Medium':2,
                'High':3}
```

## Map Scale To Features


```python
# Map feature values to scale
df['Scale'] = df['Score'].replace(scale_mapper)

# View data frame
df
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
      <th>Score</th>
      <th>Scale</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Low</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Low</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Medium</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Medium</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>High</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>


