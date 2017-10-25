Title: Handling Outliers  
Slug: handling_outliers     
Summary: How to handling outliers for machine learning in Python.   
Date: 2016-09-06 12:00  
Category: Machine Learning  
Tags: Preprocessing Structured Data  
Authors: Chris Albon

<a alt="Handling outliers" href="https://machinelearningflashcards.com">
    <img src="handling_outliers/Outlier_print.png" class="flashcard center-block">
</a>

## Preliminaries


```python
# Load library
import pandas as pd
```

## Create Data


```python
# Create DataFrame
houses = pd.DataFrame()
houses['Price'] = [534433, 392333, 293222, 4322032]
houses['Bathrooms'] = [2, 3.5, 2, 116]
houses['Square_Feet'] = [1500, 2500, 1500, 48000]

houses
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
      <th>Price</th>
      <th>Bathrooms</th>
      <th>Square_Feet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>534433</td>
      <td>2.0</td>
      <td>1500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>392333</td>
      <td>3.5</td>
      <td>2500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>293222</td>
      <td>2.0</td>
      <td>1500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4322032</td>
      <td>116.0</td>
      <td>48000</td>
    </tr>
  </tbody>
</table>
</div>



## Option 1: Drop


```python
# Drop observations greater than some value
houses[houses['Bathrooms'] < 20]
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
      <th>Price</th>
      <th>Bathrooms</th>
      <th>Square_Feet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>534433</td>
      <td>2.0</td>
      <td>1500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>392333</td>
      <td>3.5</td>
      <td>2500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>293222</td>
      <td>2.0</td>
      <td>1500</td>
    </tr>
  </tbody>
</table>
</div>



## Option 2: Mark


```python
# Load library
import numpy as np

# Create feature based on boolean condition
houses['Outlier'] = np.where(houses['Bathrooms'] < 20, 0, 1)

# Show data
houses
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
      <th>Price</th>
      <th>Bathrooms</th>
      <th>Square_Feet</th>
      <th>Outlier</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>534433</td>
      <td>2.0</td>
      <td>1500</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>392333</td>
      <td>3.5</td>
      <td>2500</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>293222</td>
      <td>2.0</td>
      <td>1500</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4322032</td>
      <td>116.0</td>
      <td>48000</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Option 3: Rescale


```python
# Log feature
houses['Log_Of_Square_Feet'] = [np.log(x) for x in houses['Square_Feet']]

# Show data
houses
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
      <th>Price</th>
      <th>Bathrooms</th>
      <th>Square_Feet</th>
      <th>Outlier</th>
      <th>Log_Of_Square_Feet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>534433</td>
      <td>2.0</td>
      <td>1500</td>
      <td>0</td>
      <td>7.313220</td>
    </tr>
    <tr>
      <th>1</th>
      <td>392333</td>
      <td>3.5</td>
      <td>2500</td>
      <td>0</td>
      <td>7.824046</td>
    </tr>
    <tr>
      <th>2</th>
      <td>293222</td>
      <td>2.0</td>
      <td>1500</td>
      <td>0</td>
      <td>7.313220</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4322032</td>
      <td>116.0</td>
      <td>48000</td>
      <td>1</td>
      <td>10.778956</td>
    </tr>
  </tbody>
</table>
</div>


