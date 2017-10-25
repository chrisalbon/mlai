Title: List Unique Values In A Pandas Column  
Slug: pandas_list_unique_values_in_column  
Summary: List Unique Values In A Pandas Column  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

Special thanks to Bob Haffner for pointing out a better way of doing it.

## Preliminaries


```python
# Import modules
import pandas as pd

# Set ipython's max row display
pd.set_option('display.max_row', 1000)

# Set iPython's max column width to 50
pd.set_option('display.max_columns', 50)
```

## Create an example dataframe


```python
# Create an example dataframe
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>reports</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td>Jason</td>
      <td>4</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td>Molly</td>
      <td>24</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>Tina</td>
      <td>31</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>Jake</td>
      <td>2</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>Amy</td>
      <td>3</td>
      <td>2014</td>
    </tr>
  </tbody>
</table>
</div>



## List unique values


```python
#List unique values in the df['name'] column
df.name.unique()
```




    array(['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], dtype=object)


