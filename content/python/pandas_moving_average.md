Title: Moving Averages In Pandas  
Slug: pandas_moving_average  
Summary: Moving Averages In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

## Import Modules


```python
# Import pandas
import pandas as pd
```

## Create Dataframe 


```python
# Create data
data = {'score': [1,1,1,2,2,2,3,3,3]}

# Create dataframe
df = pd.DataFrame(data)

# View dataframe
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
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



## Calculate Rolling Mean


```python
# Calculate the moving average. That is, take
# the first two values, average them, 
# then drop the first and add the third, etc.
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
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2.5</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>


