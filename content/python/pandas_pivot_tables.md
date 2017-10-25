Title: Pivot Tables In Pandas  
Slug: pandas_pivot_tables  
Summary: Pivot Tables In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### import modules


```python
import pandas as pd
```

### Create dataframe


```python
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'TestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3]}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'TestScore'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>TestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>31</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>24</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>31</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>2</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



### Create a pivot table of group means, by company and regiment


```python
pd.pivot_table(df, index=['regiment','company'], aggfunc='mean')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>TestScore</th>
    </tr>
    <tr>
      <th>regiment</th>
      <th>company</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Dragoons</th>
      <th>1st</th>
      <td>3.5</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>27.5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Nighthawks</th>
      <th>1st</th>
      <td>14.0</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>16.5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Scouts</th>
      <th>1st</th>
      <td>2.5</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>2.5</td>
    </tr>
  </tbody>
</table>
</div>



### Create a pivot table of group score counts, by company and regimensts


```python
df.pivot_table(index=['regiment','company'], aggfunc='count')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>TestScore</th>
    </tr>
    <tr>
      <th>regiment</th>
      <th>company</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Dragoons</th>
      <th>1st</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>2</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Nighthawks</th>
      <th>1st</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>2</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Scouts</th>
      <th>1st</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>


