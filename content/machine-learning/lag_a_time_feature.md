Title: Lag A Time Feature  
Slug: lag_a_time_feature  
Summary: How to lag a dates and times feature for machine learning in Python.     
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
# Create data frame
df = pd.DataFrame()

# Create data
df['dates'] = pd.date_range('1/1/2001', periods=5, freq='D')
df['stock_price'] = [1.1,2.2,3.3,4.4,5.5]
```

## Lag Time Data By One Row


```python
# Lagged values by one row
df['previous_days_stock_price'] = df['stock_price'].shift(1)

# Show data frame
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
      <th>dates</th>
      <th>stock_price</th>
      <th>previous_days_stock_price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001-01-01</td>
      <td>1.1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001-01-02</td>
      <td>2.2</td>
      <td>1.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2001-01-03</td>
      <td>3.3</td>
      <td>2.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001-01-04</td>
      <td>4.4</td>
      <td>3.3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2001-01-05</td>
      <td>5.5</td>
      <td>4.4</td>
    </tr>
  </tbody>
</table>
</div>


