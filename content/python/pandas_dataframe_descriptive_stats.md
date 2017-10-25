Title: Descriptive Statistics For pandas Dataframe  
Slug: pandas_dataframe_descriptive_stats  
Summary: Descriptive Statistics For pandas Dataframe  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### Import modules


```python
import pandas as pd
```

### Create dataframe


```python
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, columns = ['name', 'age', 'preTestScore', 'postTestScore'])
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> Jason</td>
      <td> 42</td>
      <td>  4</td>
      <td> 25</td>
    </tr>
    <tr>
      <th>1</th>
      <td> Molly</td>
      <td> 52</td>
      <td> 24</td>
      <td> 94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>  Tina</td>
      <td> 36</td>
      <td> 31</td>
      <td> 57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>  Jake</td>
      <td> 24</td>
      <td>  2</td>
      <td> 62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>   Amy</td>
      <td> 73</td>
      <td>  3</td>
      <td> 70</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 4 columns</p>
</div>



### The sum of all the ages


```python
df['age'].sum()
```




    227



### Mean preTestScore


```python
df['preTestScore'].mean()
```




    12.800000000000001



### Cumulative sum of preTestScores, moving from the rows from the top


```python
df['preTestScore'].cumsum()
```




    0     4
    1    28
    2    59
    3    61
    4    64
    Name: preTestScore, dtype: int64



### Summary statistics on preTestScore


```python
df['preTestScore'].describe()
```




    count     5.000000
    mean     12.800000
    std      13.663821
    min       2.000000
    25%       3.000000
    50%       4.000000
    75%      24.000000
    max      31.000000
    Name: preTestScore, dtype: float64



### Count the number of non-NA values


```python
df['preTestScore'].count()
```




    5



### Minimum value of preTestScore


```python
df['preTestScore'].min()
```




    2



### Maximum value of preTestScore


```python
df['preTestScore'].max()
```




    31



### Median value of preTestScore


```python
df['preTestScore'].median()
```




    4.0



### Sample variance of preTestScore values


```python
df['preTestScore'].var()
```




    186.69999999999999



### Sample standard deviation of preTestScore values


```python
df['preTestScore'].std()
```




    13.663820841916802



### Skewness of preTestScore values


```python
df['preTestScore'].skew()
```




    0.74334524573267591



### Kurtosis of preTestScore values


```python
df['preTestScore'].kurt()
```




    -2.4673543738411525



### Correlation Matrix Of Values


```python
df.corr()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>age</th>
      <td> 1.000000</td>
      <td>-0.105651</td>
      <td> 0.328852</td>
    </tr>
    <tr>
      <th>preTestScore</th>
      <td>-0.105651</td>
      <td> 1.000000</td>
      <td> 0.378039</td>
    </tr>
    <tr>
      <th>postTestScore</th>
      <td> 0.328852</td>
      <td> 0.378039</td>
      <td> 1.000000</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 3 columns</p>
</div>



### Covariance Matrix Of Values


```python
df.cov()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>age</th>
      <td> 340.80</td>
      <td> -26.65</td>
      <td> 151.20</td>
    </tr>
    <tr>
      <th>preTestScore</th>
      <td> -26.65</td>
      <td> 186.70</td>
      <td> 128.65</td>
    </tr>
    <tr>
      <th>postTestScore</th>
      <td> 151.20</td>
      <td> 128.65</td>
      <td> 620.30</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 3 columns</p>
</div>


