Title: Select Date And Time Ranges  
Slug: select_date_and_time_ranges  
Summary: How to select date and time ranges in Python.     
Date: 2017-09-11 12:00  
Category: Machine Learning  
Tags: Preprocessing Dates And Times    
Authors: Chris Albon

## Preliminaries


```python
# Load library
import pandas as pd
```

## Create pandas Series Time Data


```python
# Create data frame
df = pd.DataFrame()

# Create datetimes
df['date'] = pd.date_range('1/1/2001', periods=100000, freq='H')
```

## Select Time Range (Method 1)

Use this method if your data frame is not indexed by time.


```python
# Select observations between two datetimes
df[(df['date'] > '2002-1-1 01:00:00') & (df['date'] <= '2002-1-1 04:00:00')]
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
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8762</th>
      <td>2002-01-01 02:00:00</td>
    </tr>
    <tr>
      <th>8763</th>
      <td>2002-01-01 03:00:00</td>
    </tr>
    <tr>
      <th>8764</th>
      <td>2002-01-01 04:00:00</td>
    </tr>
  </tbody>
</table>
</div>



## Select Time Range (Method 2)

Use this method if your data frame is indexed by time.


```python
# Set index
df = df.set_index(df['date'])

# Select observations between two datetimes
df.loc['2002-1-1 01:00:00':'2002-1-1 04:00:00']
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
      <th>date</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2002-01-01 01:00:00</th>
      <td>2002-01-01 01:00:00</td>
    </tr>
    <tr>
      <th>2002-01-01 02:00:00</th>
      <td>2002-01-01 02:00:00</td>
    </tr>
    <tr>
      <th>2002-01-01 03:00:00</th>
      <td>2002-01-01 03:00:00</td>
    </tr>
    <tr>
      <th>2002-01-01 04:00:00</th>
      <td>2002-01-01 04:00:00</td>
    </tr>
  </tbody>
</table>
</div>


