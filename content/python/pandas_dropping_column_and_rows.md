Title: Dropping Rows And Columns In pandas Dataframe  
Slug: pandas_dropping_column_and_rows  
Summary: Dropping Rows And Columns In pandas Dataframe  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### Import modules


```python
import pandas as pd
```

### Create a dataframe 


```python
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3]}
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



### Drop an observation (row)


```python
df.drop(['Cochice', 'Pima'])
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
      <th>year</th>
    </tr>
  </thead>
  <tbody>
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



### Drop a variable (column)

Note: axis=1 denotes that we are referring to a column, not a row


```python
df.drop('reports', axis=1)
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
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td>Jason</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td>Molly</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>Tina</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>Jake</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>Amy</td>
      <td>2014</td>
    </tr>
  </tbody>
</table>
</div>



### Drop a row if it contains a certain value (in this case, "Tina")

Specifically: Create a new dataframe called df that includes all rows where the value of a cell in the name column does not equal "Tina"


```python
df[df.name != 'Tina']
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



### Drop a row by row number (in this case, row 3)

Note that Pandas uses zero based numbering, so 0 is the first row, 1 is the second row, etc. 



```python
df.drop(df.index[2])
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



can be extended to dropping a range


```python
df.drop(df.index[[2,3]])
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
      <th>Yuma</th>
      <td>Amy</td>
      <td>3</td>
      <td>2014</td>
    </tr>
  </tbody>
</table>
</div>



or dropping relative to the end of the DF. 


```python
df.drop(df.index[-2])
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
      <th>Yuma</th>
      <td>Amy</td>
      <td>3</td>
      <td>2014</td>
    </tr>
  </tbody>
</table>
</div>



you can select ranges relative to the top or drop relative to the bottom of the DF as well.


```python
df[:3] #keep top 3
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
  </tbody>
</table>
</div>




```python
df[:-3] #drop bottom 3 
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
  </tbody>
</table>
</div>


