Title: Select Rows With Multiple Filters  
Slug: pandas_select_rows_multiple_filters  
Summary: Select Rows With Multiple Filters  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  


```python
# import pandas as pd
import pandas as pd
```


```python
# Create an example dataframe
data = {'name': ['A', 'B', 'C', 'D', 'E'], 
        'score': [1,2,3,4,5]}
df = pd.DataFrame(data)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Select rows of the dataframe where df.score is greater than 1 and less and 5
df[(df['score'] > 1) & (df['score'] < 5)]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>


