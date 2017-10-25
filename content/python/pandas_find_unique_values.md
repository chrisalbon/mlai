Title: Find Unique Values In Pandas Dataframes  
Slug: pandas_find_unique_values  
Summary: Find Unique Values In Pandas Dataframes  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  


```python
import pandas as pd
import numpy as np
```


```python
raw_data = {'regiment': ['51st', '29th', '2nd', '19th', '12th', '101st', '90th', '30th', '193th', '1st', '94th', '91th'], 
            'trucks': ['MAZ-7310', np.nan, 'MAZ-7310', 'MAZ-7310', 'Tatra 810', 'Tatra 810', 'Tatra 810', 'Tatra 810', 'ZIS-150', 'Tatra 810', 'ZIS-150', 'ZIS-150'],
            'tanks': ['Merkava Mark 4', 'Merkava Mark 4', 'Merkava Mark 4', 'Leopard 2A6M', 'Leopard 2A6M', 'Leopard 2A6M', 'Arjun MBT', 'Leopard 2A6M', 'Arjun MBT', 'Arjun MBT', 'Arjun MBT', 'Arjun MBT'],
            'aircraft': ['none', 'none', 'none', 'Harbin Z-9', 'Harbin Z-9', 'none', 'Harbin Z-9', 'SH-60B Seahawk', 'SH-60B Seahawk', 'SH-60B Seahawk', 'SH-60B Seahawk', 'SH-60B Seahawk']}

df = pd.DataFrame(raw_data, columns = ['regiment', 'trucks', 'tanks', 'aircraft'])
```


```python
# View the top few rows
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>trucks</th>
      <th>tanks</th>
      <th>aircraft</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>51st</td>
      <td>MAZ-7310</td>
      <td>Merkava Mark 4</td>
      <td>none</td>
    </tr>
    <tr>
      <th>1</th>
      <td>29th</td>
      <td>NaN</td>
      <td>Merkava Mark 4</td>
      <td>none</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2nd</td>
      <td>MAZ-7310</td>
      <td>Merkava Mark 4</td>
      <td>none</td>
    </tr>
    <tr>
      <th>3</th>
      <td>19th</td>
      <td>MAZ-7310</td>
      <td>Leopard 2A6M</td>
      <td>Harbin Z-9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12th</td>
      <td>Tatra 810</td>
      <td>Leopard 2A6M</td>
      <td>Harbin Z-9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a list of unique values by turning the
# pandas column into a set
list(set(df.trucks))
```




    [nan, 'Tatra 810', 'MAZ-7310', 'ZIS-150']




```python
# Create a list of unique values in df.trucks
list(df['trucks'].unique())
```




    ['MAZ-7310', nan, 'Tatra 810', 'ZIS-150']


