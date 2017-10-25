Title: Reindexing pandas Series And Dataframes  
Slug: pandas_dataframe_reindexing  
Summary: Reindexing pandas Series And Dataframes  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

## Series


```python
# Import Modules
import pandas as pd
import numpy as np
```


```python
# Create a pandas series of the risk of fire in Southern Arizona
brushFireRisk = pd.Series([34, 23, 12, 23], index = ['Bisbee', 'Douglas', 'Sierra Vista', 'Tombstone'])
brushFireRisk
```




    Bisbee          34
    Douglas         23
    Sierra Vista    12
    Tombstone       23
    dtype: int64




```python
# Reindex the series and create a new series variable
brushFireRiskReindexed = brushFireRisk.reindex(['Tombstone', 'Douglas', 'Bisbee', 'Sierra Vista', 'Barley', 'Tucson'])
brushFireRiskReindexed
```




    Tombstone       23.0
    Douglas         23.0
    Bisbee          34.0
    Sierra Vista    12.0
    Barley           NaN
    Tucson           NaN
    dtype: float64




```python
# Reindex the series and fill in any missing indexes as 0
brushFireRiskReindexed = brushFireRisk.reindex(['Tombstone', 'Douglas', 'Bisbee', 'Sierra Vista', 'Barley', 'Tucson'], fill_value = 0)
brushFireRiskReindexed
```




    Tombstone       23
    Douglas         23
    Bisbee          34
    Sierra Vista    12
    Barley           0
    Tucson           0
    dtype: int64



## DataFrames


```python
# Create a dataframe
data = {'county': ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3]}
df = pd.DataFrame(data)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>county</th>
      <th>reports</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cochice</td>
      <td>4</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pima</td>
      <td>24</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Santa Cruz</td>
      <td>31</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Maricopa</td>
      <td>2</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Yuma</td>
      <td>3</td>
      <td>2014</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Change the order (the index) of the rows
df.reindex([4, 3, 2, 1, 0])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>county</th>
      <th>reports</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>Yuma</td>
      <td>3</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Maricopa</td>
      <td>2</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Santa Cruz</td>
      <td>31</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pima</td>
      <td>24</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Cochice</td>
      <td>4</td>
      <td>2012</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Change the order (the index) of the columns
columnsTitles = ['year', 'reports', 'county']
df.reindex(columns=columnsTitles)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>reports</th>
      <th>county</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012</td>
      <td>4</td>
      <td>Cochice</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2012</td>
      <td>24</td>
      <td>Pima</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2013</td>
      <td>31</td>
      <td>Santa Cruz</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014</td>
      <td>2</td>
      <td>Maricopa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014</td>
      <td>3</td>
      <td>Yuma</td>
    </tr>
  </tbody>
</table>
</div>


