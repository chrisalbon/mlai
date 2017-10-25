Title: Convert A Variable To A Time Variable In Pandas  
Slug: pandas_convert_to_datetime  
Summary: Convert A Variable To A Time Variable In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  


```python
# Import Preliminaries
import pandas as pd
```


```python
# Create a dataset with the index being a set of names
raw_data = {'date': ['2014-06-01T01:21:38.004053', '2014-06-02T01:21:38.004053', '2014-06-03T01:21:38.004053'],
        'score': [25, 94, 57]}
df = pd.DataFrame(raw_data, columns = ['date', 'score'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014-06-01T01:21:38.004053</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014-06-02T01:21:38.004053</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014-06-03T01:21:38.004053</td>
      <td>57</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Transpose the dataset, so that the index (in this case the names) are columns
df["date"] = pd.to_datetime(df["date"])
```


```python
df = df.set_index(df["date"])
```


```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>score</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-06-01 01:21:38.004053</th>
      <td>2014-06-01 01:21:38.004053</td>
      <td>25</td>
    </tr>
    <tr>
      <th>2014-06-02 01:21:38.004053</th>
      <td>2014-06-02 01:21:38.004053</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2014-06-03 01:21:38.004053</th>
      <td>2014-06-03 01:21:38.004053</td>
      <td>57</td>
    </tr>
  </tbody>
</table>
</div>


