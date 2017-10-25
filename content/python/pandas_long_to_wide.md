Title: Pandas: Long To Wide Format  
Slug: pandas_long_to_wide  
Summary: Pandas: Long To Wide Format  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### import modules


```python
import pandas as pd
```

### Create "long" dataframe


```python
raw_data = {'patient': [1, 1, 1, 2, 2], 
        'obs': [1, 2, 3, 1, 2], 
        'treatment': [0, 1, 0, 1, 0],
        'score': [6252, 24243, 2345, 2342, 23525]} 
df = pd.DataFrame(raw_data, columns = ['patient', 'obs', 'treatment', 'score'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>patient</th>
      <th>obs</th>
      <th>treatment</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>6252</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>24243</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>2345</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2342</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>23525</td>
    </tr>
  </tbody>
</table>
</div>



### Make a "wide" data

Now we will create a "wide" dataframe with the rows by patient number, the columns being by observation number, and the cell values being the score values.


```python
df.pivot(index='patient', columns='obs', values='score')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>obs</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
    <tr>
      <th>patient</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>6252.0</td>
      <td>24243.0</td>
      <td>2345.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2342.0</td>
      <td>23525.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


