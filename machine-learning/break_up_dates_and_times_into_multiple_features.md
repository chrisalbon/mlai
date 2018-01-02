Title: Break Up Dates And Times Into Multiple Features  
Slug: break_up_dates_and_times_into_multiple_features  
Summary: How to break up dates and times into multiple features for machine learning in Python.     
Date: 2017-09-11 12:00  
Category: Machine Learning  
Tags: Preprocessing Dates And Times    
Authors: Chris Albon

## Preliminaries


```python
# Load library
import pandas as pd
```

## Create Date And Time Data


```python
# Create data frame
df = pd.DataFrame()

# Create five dates
df['date'] = pd.date_range('1/1/2001', periods=150, freq='W')
```

## Break Up Dates And Times Into Individual Features


```python
# Create features for year, month, day, hour, and minute
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute

# Show three rows
df.head(3)
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
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001-01-07</td>
      <td>2001</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001-01-14</td>
      <td>2001</td>
      <td>1</td>
      <td>14</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2001-01-21</td>
      <td>2001</td>
      <td>1</td>
      <td>21</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


