Title: Split Combined Lat/Long Coordinate Variables Into Seperate Variables In Pandas  
Slug: pandas_split_lat_and_long_into_variables  
Summary: Split Combined Lat/Long Coordinate Variables Into Seperate Variables In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

## Preliminaries


```python
import pandas as pd
import numpy as np
```

## Create an example dataframe


```python
raw_data = {'geo': ['40.0024, -105.4102', '40.0068, -105.266', '39.9318, -105.2813', np.nan]}
df = pd.DataFrame(raw_data, columns = ['geo'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>geo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40.0024, -105.4102</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40.0068, -105.266</td>
    </tr>
    <tr>
      <th>2</th>
      <td>39.9318, -105.2813</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Split the geo variable into seperate lat and lon variables


```python
# Create two lists for the loop results to be placed
lat = []
lon = []

# For each row in a varible,
for row in df['geo']:
    # Try to,
    try:
        # Split the row by comma and append
        # everything before the comma to lat
        lat.append(row.split(',')[0])
        # Split the row by comma and append
        # everything after the comma to lon
        lon.append(row.split(',')[1])
    # But if you get an error
    except:
        # append a missing value to lat
        lat.append(np.NaN)
        # append a missing value to lon
        lon.append(np.NaN)

# Create two new columns from lat and lon
df['latitude'] = lat
df['longitude'] = lon
```

## View the dataframe


```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>geo</th>
      <th>latitude</th>
      <th>longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40.0024, -105.4102</td>
      <td>40.0024</td>
      <td>-105.4102</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40.0068, -105.266</td>
      <td>40.0068</td>
      <td>-105.266</td>
    </tr>
    <tr>
      <th>2</th>
      <td>39.9318, -105.2813</td>
      <td>39.9318</td>
      <td>-105.2813</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


