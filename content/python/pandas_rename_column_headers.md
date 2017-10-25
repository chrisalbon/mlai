Title: Rename Column Headers In Pandas  
Slug: pandas_rename_column_headers  
Summary: Rename Column Headers In Pandas  
Date: 2016-06-17 12:00  
Category: Python  
Tags: Data Wrangling 
Authors: Chris Albon  

Originally from [rgalbo](http://stackoverflow.com/users/3291077/rgalbo) on [StackOverflow](http://stackoverflow.com/questions/31328861/python-pandas-replacing-header-with-top-row).

## Preliminaries


```python
# Import required modules
import pandas as pd
```

## Create example data


```python
# Create a values as dictionary of lists
raw_data = {'0': ['first_name', 'Molly', 'Tina', 'Jake', 'Amy'], 
        '1': ['last_name', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        '2': ['age', 52, 36, 24, 73], 
        '3': ['preTestScore', 24, 31, 2, 3]}

# Create a dataframe
df = pd.DataFrame(raw_data)

# View a dataframe
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>first_name</td>
      <td>last_name</td>
      <td>age</td>
      <td>preTestScore</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>31</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



## Replace the header value with the first row's values


```python
# Create a new variable called 'header' from the first row of the dataset
header = df.iloc[0]
```




    0      first_name
    1       last_name
    2             age
    3    preTestScore
    Name: 0, dtype: object




```python
# Replace the dataframe with a new one which does not contain the first row
df = df[1:]
```


```python
# Rename the dataframe's column values with the header variable
df.rename(columns = header)
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>31</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>


