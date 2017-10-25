Title: Applying Operations Over pandas Dataframes  
Slug: pandas_apply_operations_to_dataframes  
Summary: Applying Operations Over pandas Dataframes  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### Import Modules


```python
import pandas as pd
import numpy as np
```

### Create a dataframe


```python
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3],
        'coverage': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>coverage</th>
      <th>name</th>
      <th>reports</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td>25</td>
      <td>Jason</td>
      <td>4</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td>94</td>
      <td>Molly</td>
      <td>24</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>57</td>
      <td>Tina</td>
      <td>31</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>62</td>
      <td>Jake</td>
      <td>2</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>70</td>
      <td>Amy</td>
      <td>3</td>
      <td>2014</td>
    </tr>
  </tbody>
</table>
</div>



### Create a capitalization lambda function


```python
capitalizer = lambda x: x.upper()
```

### Apply the capitalizer function over the column 'name'

apply() can apply a function along any axis of the dataframe


```python
df['name'].apply(capitalizer)
```




    Cochice       JASON
    Pima          MOLLY
    Santa Cruz     TINA
    Maricopa       JAKE
    Yuma            AMY
    Name: name, dtype: object



### Map the capitalizer lambda function over each element in the series 'name'

map() applies an operation over each element of a series


```python
df['name'].map(capitalizer)
```




    Cochice       JASON
    Pima          MOLLY
    Santa Cruz     TINA
    Maricopa       JAKE
    Yuma            AMY
    Name: name, dtype: object



### Apply a square root function to every single cell in the whole data frame

applymap() applies a function to every single element in the entire dataframe.


```python
# Drop the string variable so that applymap() can run
df = df.drop('name', axis=1)

# Return the square root of every cell in the dataframe
df.applymap(np.sqrt)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>coverage</th>
      <th>reports</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td>5.000000</td>
      <td>2.000000</td>
      <td>44.855323</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td>9.695360</td>
      <td>4.898979</td>
      <td>44.855323</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>7.549834</td>
      <td>5.567764</td>
      <td>44.866469</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>7.874008</td>
      <td>1.414214</td>
      <td>44.877611</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>8.366600</td>
      <td>1.732051</td>
      <td>44.877611</td>
    </tr>
  </tbody>
</table>
</div>



## Applying A Function Over A Dataframe

### Create a function that multiplies all non-strings by 100


```python
# create a function called times100
def times100(x):
    # that, if x is a string,
    if type(x) is str:
        # just returns it untouched
        return x
    # but, if not, return it multiplied by 100
    elif x:
        return 100 * x
    # and leave everything else
    else:
        return
```

### Apply the times100 over every cell in the dataframe


```python
df.applymap(times100)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>coverage</th>
      <th>reports</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td>2500</td>
      <td>400</td>
      <td>201200</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td>9400</td>
      <td>2400</td>
      <td>201200</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>5700</td>
      <td>3100</td>
      <td>201300</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>6200</td>
      <td>200</td>
      <td>201400</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>7000</td>
      <td>300</td>
      <td>201400</td>
    </tr>
  </tbody>
</table>
</div>


