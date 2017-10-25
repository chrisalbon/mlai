Title: pandas Data Structures  
Slug: pandas_data_structures  
Summary: pandas Data Structures  
Date: 2016-05-01 12:00   
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### Import modules


```python
import pandas as pd
```

## Series 101

Series are one-dimensional arrays (like R's vectors)

### Create a series of the number of floodingReports


```python
floodingReports = pd.Series([5, 6, 2, 9, 12])
floodingReports
```




    0     5
    1     6
    2     2
    3     9
    4    12
    dtype: int64



Note that the first column of numbers (0 to 4) are the index.

### Set county names to be the index of the floodingReports series


```python
floodingReports = pd.Series([5, 6, 2, 9, 12], index=['Cochise County', 'Pima County', 'Santa Cruz County', 'Maricopa County', 'Yuma County'])
floodingReports
```




    Cochise County        5
    Pima County           6
    Santa Cruz County     2
    Maricopa County       9
    Yuma County          12
    dtype: int64



### View the number of floodingReports in Cochise County


```python
floodingReports['Cochise County']
```




    5



### View the counties with  more than 6 flooding reports


```python
floodingReports[floodingReports > 6]
```




    Maricopa County     9
    Yuma County        12
    dtype: int64



### Create a pandas series from a dictionary

Note: when you do this, the dict's key's will become the series's index


```python
# Create a dictionary
fireReports_dict = {'Cochise County': 12, 'Pima County': 342, 'Santa Cruz County': 13, 'Maricopa County': 42, 'Yuma County' : 52}

# Convert the dictionary into a pd.Series, and view it
fireReports = pd.Series(fireReports_dict); fireReports
```




    Cochise County        12
    Maricopa County       42
    Pima County          342
    Santa Cruz County     13
    Yuma County           52
    dtype: int64



### Change the index of a series to shorter names


```python
fireReports.index = ["Cochice", "Pima", "Santa Cruz", "Maricopa", "Yuma"]
fireReports
```




    Cochice        12
    Pima           42
    Santa Cruz    342
    Maricopa       13
    Yuma           52
    dtype: int64



## DataFrame 101

DataFrames are like R's Dataframes

### Create a dataframe from a dict of equal length lists or numpy arrays


```python
data = {'county': ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3]}
df = pd.DataFrame(data)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>county</th>
      <th>reports</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cochice</td>
      <td>4</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pima</td>
      <td>24</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Santa Cruz</td>
      <td>31</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Maricopa</td>
      <td>2</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Yuma</td>
      <td>3</td>
      <td>2014</td>
    </tr>
  </tbody>
</table>
</div>



### Set the order of the columns using the columns attribute


```python
dfColumnOrdered = pd.DataFrame(data, columns=['county', 'year', 'reports'])
dfColumnOrdered
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>county</th>
      <th>year</th>
      <th>reports</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cochice</td>
      <td>2012</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pima</td>
      <td>2012</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Santa Cruz</td>
      <td>2013</td>
      <td>31</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Maricopa</td>
      <td>2014</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Yuma</td>
      <td>2014</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



### Add a column


```python
dfColumnOrdered['newsCoverage'] = pd.Series([42.3, 92.1, 12.2, 39.3, 30.2])
dfColumnOrdered
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>county</th>
      <th>year</th>
      <th>reports</th>
      <th>newsCoverage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cochice</td>
      <td>2012</td>
      <td>4</td>
      <td>42.3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pima</td>
      <td>2012</td>
      <td>24</td>
      <td>92.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Santa Cruz</td>
      <td>2013</td>
      <td>31</td>
      <td>12.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Maricopa</td>
      <td>2014</td>
      <td>2</td>
      <td>39.3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Yuma</td>
      <td>2014</td>
      <td>3</td>
      <td>30.2</td>
    </tr>
  </tbody>
</table>
</div>



### Delete a column


```python
del dfColumnOrdered['newsCoverage']
dfColumnOrdered
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>county</th>
      <th>year</th>
      <th>reports</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cochice</td>
      <td>2012</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pima</td>
      <td>2012</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Santa Cruz</td>
      <td>2013</td>
      <td>31</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Maricopa</td>
      <td>2014</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Yuma</td>
      <td>2014</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



### Transpose the dataframe


```python
dfColumnOrdered.T
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
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>county</th>
      <td>Cochice</td>
      <td>Pima</td>
      <td>Santa Cruz</td>
      <td>Maricopa</td>
      <td>Yuma</td>
    </tr>
    <tr>
      <th>year</th>
      <td>2012</td>
      <td>2012</td>
      <td>2013</td>
      <td>2014</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>reports</th>
      <td>4</td>
      <td>24</td>
      <td>31</td>
      <td>2</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>


