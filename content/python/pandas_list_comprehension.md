Title: Using List Comprehensions With Pandas
Slug: pandas_list_comprehension
Summary: Using List Comprehensions With Pandas
Date: 2016-05-01 12:00
Category: Python
Tags: Data Wrangling
Authors: Chris Albon

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



## List Comprehensions

### As a loop


```python
# Create a variable
next_year = []

# For each row in df.years,
for row in df['year']:
    # Add 1 to the row and append it to next_year
    next_year.append(row + 1)

# Create df.next_year
df['next_year'] = next_year

# View the dataframe
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
      <th>next_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td>Jason</td>
      <td>4</td>
      <td>2012</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td>Molly</td>
      <td>24</td>
      <td>2012</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>Tina</td>
      <td>31</td>
      <td>2013</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>Jake</td>
      <td>2</td>
      <td>2014</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>Amy</td>
      <td>3</td>
      <td>2014</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>



### As list comprehension


```python
# Subtract 1 from row, for each row in df.year
df['previous_year'] = [row-1 for row in df['year']]
```


```python
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
      <th>next_year</th>
      <th>previous_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td>Jason</td>
      <td>4</td>
      <td>2012</td>
      <td>2013</td>
      <td>2011</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td>Molly</td>
      <td>24</td>
      <td>2012</td>
      <td>2013</td>
      <td>2011</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td>Tina</td>
      <td>31</td>
      <td>2013</td>
      <td>2014</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td>Jake</td>
      <td>2</td>
      <td>2014</td>
      <td>2015</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td>Amy</td>
      <td>3</td>
      <td>2014</td>
      <td>2015</td>
      <td>2013</td>
    </tr>
  </tbody>
</table>
</div>


