Title: Filter pandas Dataframes  
Slug: filter_dataframes  
Summary: Filter pandas Dataframes  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

## Import modules


```python
import pandas as pd
```

## Create Dataframe


```python
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3],
        'coverage': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
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



## View Column


```python
df['name']
```




    Cochice       Jason
    Pima          Molly
    Santa Cruz     Tina
    Maricopa       Jake
    Yuma            Amy
    Name: name, dtype: object



## View Two Columns


```python
df[['name', 'reports']]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>reports</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td>Jason</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td>Molly</td>
      <td>24</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>Tina</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>Jake</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>Amy</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



## View First Two Rows


```python
df[:2]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
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
  </tbody>
</table>
</div>



## View Rows Where Coverage Is Greater Than 50


```python
df[df['coverage'] > 50]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
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



## View Rows Where Coverage Is Greater Than 50 And Reports Less Than 4


```python
df[(df['coverage']  > 50) & (df['reports'] < 4)]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
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


