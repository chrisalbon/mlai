Title: Create A Pandas Column With A For Loop  
Slug: pandas_create_column_with_loop  
Summary: Create A Pandas Column With A For Loop  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

## Preliminaries


```python
import pandas as pd
import numpy as np
```

## Create an example dataframe


```python
raw_data = {'student_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'test_score': [76, 88, 84, 67, 53, 96, 64, 91, 77, 73, 52, np.NaN]}
df = pd.DataFrame(raw_data, columns = ['student_name', 'test_score'])
```

## Create a function to assign letter grades


```python
# Create a list to store the data
grades = []

# For each row in the column,
for row in df['test_score']:
    # if more than a value,
    if row > 95:
        # Append a letter grade
        grades.append('A')
    # else, if more than a value,
    elif row > 90:
        # Append a letter grade
        grades.append('A-')
    # else, if more than a value,
    elif row > 85:
        # Append a letter grade
        grades.append('B')
    # else, if more than a value,
    elif row > 80:
        # Append a letter grade
        grades.append('B-')
    # else, if more than a value,
    elif row > 75:
        # Append a letter grade
        grades.append('C')
    # else, if more than a value,
    elif row > 70:
        # Append a letter grade
        grades.append('C-')
    # else, if more than a value,
    elif row > 65:
        # Append a letter grade
        grades.append('D')
    # else, if more than a value,
    elif row > 60:
        # Append a letter grade
        grades.append('D-')
    # otherwise,
    else:
        # Append a failing grade
        grades.append('Failed')
        
# Create a column from the list
df['grades'] = grades
```


```python
# View the new dataframe
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>student_name</th>
      <th>test_score</th>
      <th>grades</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Miller</td>
      <td>76.0</td>
      <td>C</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jacobson</td>
      <td>88.0</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ali</td>
      <td>84.0</td>
      <td>B-</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Milner</td>
      <td>67.0</td>
      <td>D</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cooze</td>
      <td>53.0</td>
      <td>Failed</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Jacon</td>
      <td>96.0</td>
      <td>A</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Ryaner</td>
      <td>64.0</td>
      <td>D-</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Sone</td>
      <td>91.0</td>
      <td>A-</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Sloan</td>
      <td>77.0</td>
      <td>C</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Piger</td>
      <td>73.0</td>
      <td>C-</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Riani</td>
      <td>52.0</td>
      <td>Failed</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Ali</td>
      <td>NaN</td>
      <td>Failed</td>
    </tr>
  </tbody>
</table>
</div>


