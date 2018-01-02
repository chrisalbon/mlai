Title: Handling Missing Values In Time Series  
Slug: handling_missing_values_in_time_series  
Summary: How to handle the missing values in time series in pandas for machine learning in Python.     
Date: 2017-09-11 12:00  
Category: Machine Learning  
Tags: Preprocessing Dates And Times    
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
import pandas as pd
import numpy as np
```

## Create Date Data With Gap In Values


```python
# Create date
time_index = pd.date_range('01/01/2010', periods=5, freq='M')

# Create data frame, set index
df = pd.DataFrame(index=time_index)

# Create feature with a gap of missing values
df['Sales'] = [1.0,2.0,np.nan,np.nan,5.0]
```

## Interpolate Missing Values


```python
# Interpolate missing values
df.interpolate()
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
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-31</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010-02-28</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2010-03-31</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2010-04-30</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2010-05-31</th>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



## Forward-fill Missing Values


```python
# Forward-fill
df.ffill()
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
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-31</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010-02-28</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2010-03-31</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2010-04-30</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2010-05-31</th>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



## Backfill Missing Values


```python
# Back-fill
df.bfill()
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
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-31</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010-02-28</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2010-03-31</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2010-04-30</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2010-05-31</th>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



## Interpolate Missing Values But Only Up One Value


```python
# Interpolate missing values
df.interpolate(limit=1, limit_direction='forward')
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
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-31</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2010-02-28</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2010-03-31</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2010-04-30</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2010-05-31</th>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>


