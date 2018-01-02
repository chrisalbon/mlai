Title: Ranking Rows Of Pandas Dataframes
Slug: pandas_dataframe_ranking_rows
Summary: Ranking Rows Of pandas Dataframes
Date: 2016-05-01 12:00
Category: Python
Tags: Data Wrangling
Authors: Chris Albon


```python
# import modules
import pandas as pd
```


```python
# Create dataframe
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3],
        'coverage': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
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
      <td> 25</td>
      <td> Jason</td>
      <td>  4</td>
      <td> 2012</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td> 94</td>
      <td> Molly</td>
      <td> 24</td>
      <td> 2012</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td> 57</td>
      <td>  Tina</td>
      <td> 31</td>
      <td> 2013</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td> 62</td>
      <td>  Jake</td>
      <td>  2</td>
      <td> 2014</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td> 70</td>
      <td>   Amy</td>
      <td>  3</td>
      <td> 2014</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 4 columns</p>
</div>




```python
# Create a new column that is the rank of the value of coverage in ascending order
df['coverageRanked'] = df['coverage'].rank(ascending=1)
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>coverage</th>
      <th>name</th>
      <th>reports</th>
      <th>year</th>
      <th>coverageRanked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cochice</th>
      <td> 25</td>
      <td> Jason</td>
      <td>  4</td>
      <td> 2012</td>
      <td> 1</td>
    </tr>
    <tr>
      <th>Pima</th>
      <td> 94</td>
      <td> Molly</td>
      <td> 24</td>
      <td> 2012</td>
      <td> 5</td>
    </tr>
    <tr>
      <th>Santa Cruz</th>
      <td> 57</td>
      <td>  Tina</td>
      <td> 31</td>
      <td> 2013</td>
      <td> 2</td>
    </tr>
    <tr>
      <th>Maricopa</th>
      <td> 62</td>
      <td>  Jake</td>
      <td>  2</td>
      <td> 2014</td>
      <td> 3</td>
    </tr>
    <tr>
      <th>Yuma</th>
      <td> 70</td>
      <td>   Amy</td>
      <td>  3</td>
      <td> 2014</td>
      <td> 4</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 5 columns</p>
</div>


