Title: Search A Pandas Column For A Value  
Slug: pandas_search_column_for_value  
Summary: Search A Pandas Column For A Value  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  


```python
# Import modules
import pandas as pd
```


```python
raw_data = {'first_name': ['Jason', 'Jason', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Miller', 'Ali', 'Milner', 'Cooze'], 
        'age': [42, 42, 36, 24, 73], 
        'preTestScore': [4, 4, 31, 2, 3],
        'postTestScore': [25, 25, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



## Find where a value exists in a column


```python
# View preTestscore where postTestscore is greater than 50
df['preTestScore'].where(df['postTestScore'] > 50)
```




    0     NaN
    1     NaN
    2    31.0
    3     2.0
    4     3.0
    Name: preTestScore, dtype: float64


