Title: Rolling Time Window  
Slug: rolling_time_windows  
Summary: How to use rolling time windows in pandas for machine learning in Python.     
Date: 2017-09-11 12:00  
Category: Machine Learning  
Tags: Preprocessing Dates And Times    
Authors: Chris Albon

## Preliminaries


```python
# Load library
import pandas as pd
```

## Create Date Data


```python
# Create datetimes
time_index = pd.date_range('01/01/2010', periods=5, freq='M')

# Create data frame, set index
df = pd.DataFrame(index=time_index)

# Create feature
df['Stock_Price'] = [1,2,3,4,5]
```

## Create A Rolling Time Window Of Two Rows


```python
# Calculate rolling mean
df.rolling(window=2).mean()
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
      <th>Stock_Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-31</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2010-02-28</th>
      <td>1.5</td>
    </tr>
    <tr>
      <th>2010-03-31</th>
      <td>2.5</td>
    </tr>
    <tr>
      <th>2010-04-30</th>
      <td>3.5</td>
    </tr>
    <tr>
      <th>2010-05-31</th>
      <td>4.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Identify max value in rolling time window
df.rolling(window=2).max()
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
      <th>Stock_Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-31</th>
      <td>NaN</td>
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


