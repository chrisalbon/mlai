Title: Count Values In Pandas Dataframe  
Slug: pandas_dataframe_count_values  
Summary: Count Values In Pandas Dataframe  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### Import the pandas module


```python
import pandas as pd
```

### Create all the columns of the dataframe as series


```python
year = pd.Series([1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 
                  1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894])
guardCorps = pd.Series([0,2,2,1,0,0,1,1,0,3,0,2,1,0,0,1,0,1,0,1])
corps1 = pd.Series([0,0,0,2,0,3,0,2,0,0,0,1,1,1,0,2,0,3,1,0])
corps2 = pd.Series([0,0,0,2,0,2,0,0,1,1,0,0,2,1,1,0,0,2,0,0])
corps3 = pd.Series([0,0,0,1,1,1,2,0,2,0,0,0,1,0,1,2,1,0,0,0])
corps4 = pd.Series([0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0])
corps5 = pd.Series([0,0,0,0,2,1,0,0,1,0,0,1,0,1,1,1,1,1,1,0])
corps6 = pd.Series([0,0,1,0,2,0,0,1,2,0,1,1,3,1,1,1,0,3,0,0])
corps7 = pd.Series([1,0,1,0,0,0,1,0,1,1,0,0,2,0,0,2,1,0,2,0])
corps8 = pd.Series([1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1])
corps9 = pd.Series([0,0,0,0,0,2,1,1,1,0,2,1,1,0,1,2,0,1,0,0])
corps10 = pd.Series([0,0,1,1,0,1,0,2,0,2,0,0,0,0,2,1,3,0,1,1])
corps11 = pd.Series([0,0,0,0,2,4,0,1,3,0,1,1,1,1,2,1,3,1,3,1])
corps14 = pd.Series([ 1,1,2,1,1,3,0,4,0,1,0,3,2,1,0,2,1,1,0,0])
corps15 = pd.Series([0,1,0,0,0,0,0,1,0,1,1,0,0,0,2,2,0,0,0,0])
```

### Create a dictionary variable that assigns variable names


```python
variables = dict(guardCorps = guardCorps, corps1 = corps1, 
                 corps2 = corps2, corps3 = corps3, corps4 = corps4, 
                 corps5 = corps5, corps6 = corps6, corps7 = corps7, 
                 corps8 = corps8, corps9 = corps9, corps10 = corps10, 
                 corps11 = corps11 , corps14 = corps14, corps15 = corps15)
```

### Create a dataframe and set the order of the columns using the columns attribute


```python
horsekick = pd.DataFrame(variables, columns = ['guardCorps', 
                                                    'corps1', 'corps2', 
                                                    'corps3', 'corps4', 
                                                    'corps5', 'corps6', 
                                                    'corps7', 'corps8', 
                                                    'corps9', 'corps10', 
                                                    'corps11', 'corps14', 
                                                    'corps15'])
```

### Set the dataframe's index to be year


```python
horsekick.index = [1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 
                  1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894]
```

### View the horsekick dataframe


```python
horsekick
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>guardCorps</th>
      <th>corps1</th>
      <th>corps2</th>
      <th>corps3</th>
      <th>corps4</th>
      <th>corps5</th>
      <th>corps6</th>
      <th>corps7</th>
      <th>corps8</th>
      <th>corps9</th>
      <th>corps10</th>
      <th>corps11</th>
      <th>corps14</th>
      <th>corps15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1875</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1876</th>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1877</th>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1878</th>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1879</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1880</th>
      <td>0</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1881</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1882</th>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1883</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1884</th>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1885</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1886</th>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1887</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1888</th>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1889</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1890</th>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1891</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1892</th>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1893</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1894</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Count the number of times each number of deaths occurs in each regiment


```python
result = horsekick.apply(pd.value_counts).fillna(0); result
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>guardCorps</th>
      <th>corps1</th>
      <th>corps2</th>
      <th>corps3</th>
      <th>corps4</th>
      <th>corps5</th>
      <th>corps6</th>
      <th>corps7</th>
      <th>corps8</th>
      <th>corps9</th>
      <th>corps10</th>
      <th>corps11</th>
      <th>corps14</th>
      <th>corps15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9.0</td>
      <td>11.0</td>
      <td>12.0</td>
      <td>11.0</td>
      <td>12.0</td>
      <td>10.0</td>
      <td>9.0</td>
      <td>11.0</td>
      <td>13.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>6</td>
      <td>6</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>8</td>
      <td>8</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>2</td>
      <td>3</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>3</td>
      <td>2</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



### Count the number of times each monthly death total appears in guardCorps


```python
pd.value_counts(horsekick['guardCorps'].values, sort=False)
```




    0    9
    1    7
    2    3
    3    1
    dtype: int64



### List all the unique values in guardCorps


```python
horsekick['guardCorps'].unique()
```




    array([0, 2, 1, 3])


