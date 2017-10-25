Title: Sorting Rows In pandas Dataframes  
Slug: pandas_sorting_rows_dataframe  
Summary: Sorting Rows In pandas Dataframes  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### import modules


```python
import pandas as pd
```

### Create dataframe


```python
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [1, 2, 1, 2, 3],
        'coverage': [2, 2, 3, 3, 3]}
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
      <td>2</td>
      <td>Jason</td>
      <td>1</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td>2</td>
      <td>Molly</td>
      <td>2</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>3</td>
      <td>Tina</td>
      <td>1</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>3</td>
      <td>Jake</td>
      <td>2</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>3</td>
      <td>Amy</td>
      <td>3</td>
      <td>2014</td>
    </tr>
  </tbody>
</table>
</div>



### Sort the dataframe's rows by reports, in descending order


```python
df.sort_values(by='reports', ascending=0)
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
      <th>Yuma</th>
      <td>3</td>
      <td>Amy</td>
      <td>3</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td>2</td>
      <td>Molly</td>
      <td>2</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>3</td>
      <td>Jake</td>
      <td>2</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>Cochice</th>
      <td>2</td>
      <td>Jason</td>
      <td>1</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>3</td>
      <td>Tina</td>
      <td>1</td>
      <td>2013</td>
    </tr>
  </tbody>
</table>
</div>



### Sort the dataframe's rows by coverage and then by reports, in ascending order


```python
df.sort_values(by=['coverage', 'reports'])
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
      <td>2</td>
      <td>Jason</td>
      <td>1</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td>2</td>
      <td>Molly</td>
      <td>2</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>3</td>
      <td>Tina</td>
      <td>1</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>3</td>
      <td>Jake</td>
      <td>2</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>3</td>
      <td>Amy</td>
      <td>3</td>
      <td>2014</td>
    </tr>
  </tbody>
</table>
</div>


