Title: Create a Column Based on a Conditional in pandas  
Slug: pandas_create_column_using_conditional  
Summary: Create a Column Based on a Conditional in pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### Preliminaries


```python
# Import required modules
import pandas as pd
import numpy as np
```

### Make a dataframe


```python
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, columns = ['name', 'age', 'preTestScore', 'postTestScore'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>42</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>52</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>24</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>73</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



### Add a new column for elderly


```python
# Create a new column called df.elderly where the value is yes
# if df.age is greater than 50 and no if not
df['elderly'] = np.where(df['age']>=50, 'yes', 'no')
```


```python
# View the dataframe
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
      <th>elderly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>42</td>
      <td>4</td>
      <td>25</td>
      <td>no</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>52</td>
      <td>24</td>
      <td>94</td>
      <td>yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>36</td>
      <td>31</td>
      <td>57</td>
      <td>no</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>24</td>
      <td>2</td>
      <td>62</td>
      <td>no</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>73</td>
      <td>3</td>
      <td>70</td>
      <td>yes</td>
    </tr>
  </tbody>
</table>
</div>


