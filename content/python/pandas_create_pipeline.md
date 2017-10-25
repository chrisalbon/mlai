Title: Create A Pipeline In Pandas  
Slug: pandas_create_pipeline  
Summary: Create a pipeline in pandas.  
Date: 2017-01-16 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon   

Pandas' pipeline feature allows you to string together Python functions in order to build a pipeline of data processing.

## Preliminaries


```python
import pandas as pd
```

## Create Dataframe


```python
# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']
df['gender'] = ['Male', 'Male', 'Female']
df['age'] = [31, 32, 19]

# View dataframe
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>gender</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>Male</td>
      <td>31</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Steve</td>
      <td>Male</td>
      <td>32</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sarah</td>
      <td>Female</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>



## Create Functions To Process Data


```python
# Create a function that
def mean_age_by_group(dataframe, col):
    # groups the data by a column and returns the mean age per group
    return dataframe.groupby(col).mean()
```


```python
# Create a function that
def uppercase_column_name(dataframe):
    # Capitalizes all the column headers
    dataframe.columns = dataframe.columns.str.upper()
    # And returns them
    return dataframe
```

## Create A Pipeline Of Those Functions


```python
# Create a pipeline that applies the mean_age_by_group function
(df.pipe(mean_age_by_group, col='gender')
   # then applies the uppercase column name function
   .pipe(uppercase_column_name)
)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AGE</th>
    </tr>
    <tr>
      <th>gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>19.0</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>31.5</td>
    </tr>
  </tbody>
</table>
</div>


