Title: Apply Operations To Groups In Pandas  
Slug: pandas_apply_operations_to_groups  
Summary: Apply Operations To Groups In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

## Preliminaries


```python
# import modules
import pandas as pd
```


```python
# Create dataframe
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])
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
      <th>regiment</th>
      <th>company</th>
      <th>name</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>Miller</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>Jacobson</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>Ali</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>Milner</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>Cooze</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>Jacon</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>Ryaner</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>Sone</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>Sloan</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>Piger</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>Riani</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>Ali</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a groupby variable that groups preTestScores by regiment
groupby_regiment = df['preTestScore'].groupby(df['regiment'])
groupby_regiment
```




    <pandas.core.groupby.SeriesGroupBy object at 0x113ddb550>



"This grouped variable is now a GroupBy object. It has not actually computed anything yet except for some intermediate data about the group key df['key1']. The idea is that this object has all of the information needed to then apply some operation to each of the groups." - Python for Data Analysis

## View a grouping

Use list() to show what a grouping looks like


```python
list(df['preTestScore'].groupby(df['regiment']))
```




    [('Dragoons', 4     3
      5     4
      6    24
      7    31
      Name: preTestScore, dtype: int64), ('Nighthawks', 0     4
      1    24
      2    31
      3     2
      Name: preTestScore, dtype: int64), ('Scouts', 8     2
      9     3
      10    2
      11    3
      Name: preTestScore, dtype: int64)]



## Descriptive statistics by group


```python
df['preTestScore'].groupby(df['regiment']).describe()
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>regiment</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dragoons</th>
      <td>4.0</td>
      <td>15.50</td>
      <td>14.153916</td>
      <td>3.0</td>
      <td>3.75</td>
      <td>14.0</td>
      <td>25.75</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>Nighthawks</th>
      <td>4.0</td>
      <td>15.25</td>
      <td>14.453950</td>
      <td>2.0</td>
      <td>3.50</td>
      <td>14.0</td>
      <td>25.75</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>Scouts</th>
      <td>4.0</td>
      <td>2.50</td>
      <td>0.577350</td>
      <td>2.0</td>
      <td>2.00</td>
      <td>2.5</td>
      <td>3.00</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



### Mean of each regiment's preTestScore


```python
groupby_regiment.mean()
```




    regiment
    Dragoons      15.50
    Nighthawks    15.25
    Scouts         2.50
    Name: preTestScore, dtype: float64



### Mean preTestScores grouped by regiment and company


```python
df['preTestScore'].groupby([df['regiment'], df['company']]).mean()
```




    regiment    company
    Dragoons    1st         3.5
                2nd        27.5
    Nighthawks  1st        14.0
                2nd        16.5
    Scouts      1st         2.5
                2nd         2.5
    Name: preTestScore, dtype: float64



### Mean preTestScores grouped by regiment and company without heirarchical indexing


```python
df['preTestScore'].groupby([df['regiment'], df['company']]).mean().unstack()
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
      <th>company</th>
      <th>1st</th>
      <th>2nd</th>
    </tr>
    <tr>
      <th>regiment</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dragoons</th>
      <td>3.5</td>
      <td>27.5</td>
    </tr>
    <tr>
      <th>Nighthawks</th>
      <td>14.0</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>Scouts</th>
      <td>2.5</td>
      <td>2.5</td>
    </tr>
  </tbody>
</table>
</div>



### Group the entire dataframe by regiment and company


```python
df.groupby(['regiment', 'company']).mean()
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
      <th></th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
    <tr>
      <th>regiment</th>
      <th>company</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Dragoons</th>
      <th>1st</th>
      <td>3.5</td>
      <td>47.5</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>27.5</td>
      <td>75.5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Nighthawks</th>
      <th>1st</th>
      <td>14.0</td>
      <td>59.5</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>16.5</td>
      <td>59.5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Scouts</th>
      <th>1st</th>
      <td>2.5</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>2nd</th>
      <td>2.5</td>
      <td>66.0</td>
    </tr>
  </tbody>
</table>
</div>



### Number of observations in each regiment and company


```python
df.groupby(['regiment', 'company']).size()
```




    regiment    company
    Dragoons    1st        2
                2nd        2
    Nighthawks  1st        2
                2nd        2
    Scouts      1st        2
                2nd        2
    dtype: int64



## Iterate an operations over groups


```python
# Group the dataframe by regiment, and for each regiment,
for name, group in df.groupby('regiment'): 
    # print the name of the regiment
    print(name)
    # print the data of that regiment
    print(group)
```

    Dragoons
       regiment company    name  preTestScore  postTestScore
    4  Dragoons     1st   Cooze             3             70
    5  Dragoons     1st   Jacon             4             25
    6  Dragoons     2nd  Ryaner            24             94
    7  Dragoons     2nd    Sone            31             57
    Nighthawks
         regiment company      name  preTestScore  postTestScore
    0  Nighthawks     1st    Miller             4             25
    1  Nighthawks     1st  Jacobson            24             94
    2  Nighthawks     2nd       Ali            31             57
    3  Nighthawks     2nd    Milner             2             62
    Scouts
       regiment company   name  preTestScore  postTestScore
    8    Scouts     1st  Sloan             2             62
    9    Scouts     1st  Piger             3             70
    10   Scouts     2nd  Riani             2             62
    11   Scouts     2nd    Ali             3             70


### Group by columns

Specifically in this case: group by the data types of the columns (i.e. axis=1) and then use list() to view what that grouping looks like


```python
list(df.groupby(df.dtypes, axis=1))
```




    [(dtype('int64'),     preTestScore  postTestScore
      0              4             25
      1             24             94
      2             31             57
      3              2             62
      4              3             70
      5              4             25
      6             24             94
      7             31             57
      8              2             62
      9              3             70
      10             2             62
      11             3             70),
     (dtype('O'),       regiment company      name
      0   Nighthawks     1st    Miller
      1   Nighthawks     1st  Jacobson
      2   Nighthawks     2nd       Ali
      3   Nighthawks     2nd    Milner
      4     Dragoons     1st     Cooze
      5     Dragoons     1st     Jacon
      6     Dragoons     2nd    Ryaner
      7     Dragoons     2nd      Sone
      8       Scouts     1st     Sloan
      9       Scouts     1st     Piger
      10      Scouts     2nd     Riani
      11      Scouts     2nd       Ali)]



### In the dataframe "df", group by "regiments, take the mean values of the other variables for those groups, then display them with the prefix_mean


```python
df.groupby('regiment').mean().add_prefix('mean_')
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
      <th>mean_preTestScore</th>
      <th>mean_postTestScore</th>
    </tr>
    <tr>
      <th>regiment</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Dragoons</th>
      <td>15.50</td>
      <td>61.5</td>
    </tr>
    <tr>
      <th>Nighthawks</th>
      <td>15.25</td>
      <td>59.5</td>
    </tr>
    <tr>
      <th>Scouts</th>
      <td>2.50</td>
      <td>66.0</td>
    </tr>
  </tbody>
</table>
</div>



### Create a function to get the stats of a group


```python
def get_stats(group):
    return {'min': group.min(), 'max': group.max(), 'count': group.count(), 'mean': group.mean()}
```

### Create bins and bin up postTestScore by those pins


```python
bins = [0, 25, 50, 75, 100]
group_names = ['Low', 'Okay', 'Good', 'Great']
df['categories'] = pd.cut(df['postTestScore'], bins, labels=group_names)
```

### Apply the get_stats() function to each postTestScore bin


```python
df['postTestScore'].groupby(df['categories']).apply(get_stats).unstack()
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
      <th>count</th>
      <th>max</th>
      <th>mean</th>
      <th>min</th>
    </tr>
    <tr>
      <th>categories</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Good</th>
      <td>8.0</td>
      <td>70.0</td>
      <td>63.75</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>Great</th>
      <td>2.0</td>
      <td>94.0</td>
      <td>94.00</td>
      <td>94.0</td>
    </tr>
    <tr>
      <th>Low</th>
      <td>2.0</td>
      <td>25.0</td>
      <td>25.00</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>Okay</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


