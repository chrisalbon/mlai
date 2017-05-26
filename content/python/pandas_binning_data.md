Title: Binning Data In Pandas
Slug: pandas_binning_data
Summary: Binning Data In Pandas
Date: 2016-05-01 12:00
Category: Python
Tags: Data Wrangling
Authors: Chris Albon

Want to learn more? I recommend these Python books: [Python for Data Analysis](http://amzn.to/2ljV9wY), [Python Data Science Handbook](http://amzn.to/2m0mgMB), and [Introduction to Machine Learning with Python](http://amzn.to/2mjYiwK).

### import modules


```python
import pandas as pd
```

### Create dataframe


```python
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
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
      <th>0 </th>
      <td> Nighthawks</td>
      <td> 1st</td>
      <td>   Miller</td>
      <td>  4</td>
      <td> 25</td>
    </tr>
    <tr>
      <th>1 </th>
      <td> Nighthawks</td>
      <td> 1st</td>
      <td> Jacobson</td>
      <td> 24</td>
      <td> 94</td>
    </tr>
    <tr>
      <th>2 </th>
      <td> Nighthawks</td>
      <td> 2nd</td>
      <td>      Ali</td>
      <td> 31</td>
      <td> 57</td>
    </tr>
    <tr>
      <th>3 </th>
      <td> Nighthawks</td>
      <td> 2nd</td>
      <td>   Milner</td>
      <td>  2</td>
      <td> 62</td>
    </tr>
    <tr>
      <th>4 </th>
      <td>   Dragoons</td>
      <td> 1st</td>
      <td>    Cooze</td>
      <td>  3</td>
      <td> 70</td>
    </tr>
    <tr>
      <th>5 </th>
      <td>   Dragoons</td>
      <td> 1st</td>
      <td>    Jacon</td>
      <td>  4</td>
      <td> 25</td>
    </tr>
    <tr>
      <th>6 </th>
      <td>   Dragoons</td>
      <td> 2nd</td>
      <td>   Ryaner</td>
      <td> 24</td>
      <td> 94</td>
    </tr>
    <tr>
      <th>7 </th>
      <td>   Dragoons</td>
      <td> 2nd</td>
      <td>     Sone</td>
      <td> 31</td>
      <td> 57</td>
    </tr>
    <tr>
      <th>8 </th>
      <td>     Scouts</td>
      <td> 1st</td>
      <td>    Sloan</td>
      <td>  2</td>
      <td> 62</td>
    </tr>
    <tr>
      <th>9 </th>
      <td>     Scouts</td>
      <td> 1st</td>
      <td>    Piger</td>
      <td>  3</td>
      <td> 70</td>
    </tr>
    <tr>
      <th>10</th>
      <td>     Scouts</td>
      <td> 2nd</td>
      <td>    Riani</td>
      <td>  2</td>
      <td> 62</td>
    </tr>
    <tr>
      <th>11</th>
      <td>     Scouts</td>
      <td> 2nd</td>
      <td>      Ali</td>
      <td>  3</td>
      <td> 70</td>
    </tr>
  </tbody>
</table>
<p>12 rows × 5 columns</p>
</div>



### Define bins as 0 to 25, 25 to 50, 60 to 75, 75 to 100


```python
bins = [0, 25, 50, 75, 100]
```

### Create names for the four groups


```python
group_names = ['Low', 'Okay', 'Good', 'Great']
```

### Cut postTestScore and add scoresBinned column


```python
categories = pd.cut(df['postTestScore'], bins, labels=group_names)
df['categories'] = pd.cut(df['postTestScore'], bins, labels=group_names)
df['scoresBinned'] = pd.cut(df['postTestScore'], bins)
categories
```




       Low
     Great
      Good
      Good
      Good
       Low
     Great
      Good
      Good
      Good
      Good
      Good
    Name: postTestScore, Levels (4): Index(['Low', 'Okay', 'Good', 'Great'], dtype=object)



### Count the number of observations which each value


```python
pd.value_counts(df['categories'])
```

### View the dataframe


```python
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>regiment</th>
      <th>company</th>
      <th>name</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
      <th>scoresBinned</th>
      <th>categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0 </th>
      <td> Nighthawks</td>
      <td> 1st</td>
      <td>   Miller</td>
      <td>  4</td>
      <td> 25</td>
      <td>   (0, 25]</td>
      <td>   Low</td>
    </tr>
    <tr>
      <th>1 </th>
      <td> Nighthawks</td>
      <td> 1st</td>
      <td> Jacobson</td>
      <td> 24</td>
      <td> 94</td>
      <td> (75, 100]</td>
      <td> Great</td>
    </tr>
    <tr>
      <th>2 </th>
      <td> Nighthawks</td>
      <td> 2nd</td>
      <td>      Ali</td>
      <td> 31</td>
      <td> 57</td>
      <td>  (50, 75]</td>
      <td>  Good</td>
    </tr>
    <tr>
      <th>3 </th>
      <td> Nighthawks</td>
      <td> 2nd</td>
      <td>   Milner</td>
      <td>  2</td>
      <td> 62</td>
      <td>  (50, 75]</td>
      <td>  Good</td>
    </tr>
    <tr>
      <th>4 </th>
      <td>   Dragoons</td>
      <td> 1st</td>
      <td>    Cooze</td>
      <td>  3</td>
      <td> 70</td>
      <td>  (50, 75]</td>
      <td>  Good</td>
    </tr>
    <tr>
      <th>5 </th>
      <td>   Dragoons</td>
      <td> 1st</td>
      <td>    Jacon</td>
      <td>  4</td>
      <td> 25</td>
      <td>   (0, 25]</td>
      <td>   Low</td>
    </tr>
    <tr>
      <th>6 </th>
      <td>   Dragoons</td>
      <td> 2nd</td>
      <td>   Ryaner</td>
      <td> 24</td>
      <td> 94</td>
      <td> (75, 100]</td>
      <td> Great</td>
    </tr>
    <tr>
      <th>7 </th>
      <td>   Dragoons</td>
      <td> 2nd</td>
      <td>     Sone</td>
      <td> 31</td>
      <td> 57</td>
      <td>  (50, 75]</td>
      <td>  Good</td>
    </tr>
    <tr>
      <th>8 </th>
      <td>     Scouts</td>
      <td> 1st</td>
      <td>    Sloan</td>
      <td>  2</td>
      <td> 62</td>
      <td>  (50, 75]</td>
      <td>  Good</td>
    </tr>
    <tr>
      <th>9 </th>
      <td>     Scouts</td>
      <td> 1st</td>
      <td>    Piger</td>
      <td>  3</td>
      <td> 70</td>
      <td>  (50, 75]</td>
      <td>  Good</td>
    </tr>
    <tr>
      <th>10</th>
      <td>     Scouts</td>
      <td> 2nd</td>
      <td>    Riani</td>
      <td>  2</td>
      <td> 62</td>
      <td>  (50, 75]</td>
      <td>  Good</td>
    </tr>
    <tr>
      <th>11</th>
      <td>     Scouts</td>
      <td> 2nd</td>
      <td>      Ali</td>
      <td>  3</td>
      <td> 70</td>
      <td>  (50, 75]</td>
      <td>  Good</td>
    </tr>
  </tbody>
</table>
<p>12 rows × 7 columns</p>
</div>
