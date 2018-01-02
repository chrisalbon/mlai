Title: Apply Functions By Group In Pandas  
Slug: pandas_apply_function_by_group  
Summary: Apply Functions By Group In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

## Preliminaries


```python
# import pandas as pd
import pandas as pd
```

## Create a simulated dataset


```python
# Create an example dataframe
data = {'Platoon': ['A','A','A','A','A','A','B','B','B','B','B','C','C','C','C','C'],
       'Casualties': [1,4,5,7,5,5,6,1,4,5,6,7,4,6,4,6]}
df = pd.DataFrame(data)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Casualties</th>
      <th>Platoon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>A</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>A</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>A</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>B</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>B</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4</td>
      <td>B</td>
    </tr>
    <tr>
      <th>9</th>
      <td>5</td>
      <td>B</td>
    </tr>
    <tr>
      <th>10</th>
      <td>6</td>
      <td>B</td>
    </tr>
    <tr>
      <th>11</th>
      <td>7</td>
      <td>C</td>
    </tr>
    <tr>
      <th>12</th>
      <td>4</td>
      <td>C</td>
    </tr>
    <tr>
      <th>13</th>
      <td>6</td>
      <td>C</td>
    </tr>
    <tr>
      <th>14</th>
      <td>4</td>
      <td>C</td>
    </tr>
    <tr>
      <th>15</th>
      <td>6</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>



## Apply A Function (Rolling Mean) To The DataFrame, By Group


```python
# Group df by df.platoon, then apply a rolling mean lambda function to df.casualties
df.groupby('Platoon')['Casualties'].apply(lambda x:x.rolling(center=False,window=2).mean())
```




    0     NaN
    1     2.5
    2     4.5
    3     6.0
    4     6.0
    5     5.0
    6     NaN
    7     3.5
    8     2.5
    9     4.5
    10    5.5
    11    NaN
    12    5.5
    13    5.0
    14    5.0
    15    5.0
    dtype: float64


