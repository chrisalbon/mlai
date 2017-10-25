Title: Breaking Up A String Into Columns Using Regex In Pandas  
Slug: pandas_regex_to_create_columns  
Summary: Breaking Up A String Into Columns Using Regex In Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

Based on [this tutorial in nbviewer](http://nbviewer.ipython.org/github/swcarpentry/notebooks/blob/master/regex-intro.ipynb).

### Import modules


```python
import re
import pandas as pd
```

### Create a dataframe of raw strings


```python
# Create a dataframe with a single column of strings
data = {'raw': ['Arizona 1 2014-12-23       3242.0',
                'Iowa 1 2010-02-23       3453.7',
                'Oregon 0 2014-06-20       2123.0',
                'Maryland 0 2014-03-14       1123.6',
                'Florida 1 2013-01-15       2134.0',
                'Georgia 0 2012-07-14       2345.6']}
df = pd.DataFrame(data, columns = ['raw'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>raw</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Arizona 1 2014-12-23       3242.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Iowa 1 2010-02-23       3453.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Oregon 0 2014-06-20       2123.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Maryland 0 2014-03-14       1123.6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Florida 1 2013-01-15       2134.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Georgia 0 2012-07-14       2345.6</td>
    </tr>
  </tbody>
</table>
</div>



### Search a column of strings for a pattern


```python
# Which rows of df['raw'] contain 'xxxx-xx-xx'?
df['raw'].str.contains('....-..-..', regex=True)
```




    0    True
    1    True
    2    True
    3    True
    4    True
    5    True
    Name: raw, dtype: bool



### Extract the column of single digits


```python
# In the column 'raw', extract single digit in the strings
df['female'] = df['raw'].str.extract('(\d)', expand=True)
df['female']
```




    0    1
    1    1
    2    0
    3    0
    4    1
    5    0
    Name: female, dtype: object



### Extract the column of dates


```python
# In the column 'raw', extract xxxx-xx-xx in the strings
df['date'] = df['raw'].str.extract('(....-..-..)', expand=True)
df['date']
```




    0    2014-12-23
    1    2010-02-23
    2    2014-06-20
    3    2014-03-14
    4    2013-01-15
    5    2012-07-14
    Name: date, dtype: object



### Extract the column of thousands


```python
# In the column 'raw', extract ####.## in the strings
df['score'] = df['raw'].str.extract('(\d\d\d\d\.\d)', expand=True)
df['score']
```




    0    3242.0
    1    3453.7
    2    2123.0
    3    1123.6
    4    2134.0
    5    2345.6
    Name: score, dtype: object



### Extract the column of words


```python
# In the column 'raw', extract the word in the strings
df['state'] = df['raw'].str.extract('([A-Z]\w{0,})', expand=True)
df['state']
```




    0     Arizona
    1        Iowa
    2      Oregon
    3    Maryland
    4     Florida
    5     Georgia
    Name: state, dtype: object



### View the final dataframe


```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>raw</th>
      <th>female</th>
      <th>date</th>
      <th>score</th>
      <th>state</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Arizona 1 2014-12-23       3242.0</td>
      <td>1</td>
      <td>2014-12-23</td>
      <td>3242.0</td>
      <td>Arizona</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Iowa 1 2010-02-23       3453.7</td>
      <td>1</td>
      <td>2010-02-23</td>
      <td>3453.7</td>
      <td>Iowa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Oregon 0 2014-06-20       2123.0</td>
      <td>0</td>
      <td>2014-06-20</td>
      <td>2123.0</td>
      <td>Oregon</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Maryland 0 2014-03-14       1123.6</td>
      <td>0</td>
      <td>2014-03-14</td>
      <td>1123.6</td>
      <td>Maryland</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Florida 1 2013-01-15       2134.0</td>
      <td>1</td>
      <td>2013-01-15</td>
      <td>2134.0</td>
      <td>Florida</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Georgia 0 2012-07-14       2345.6</td>
      <td>0</td>
      <td>2012-07-14</td>
      <td>2345.6</td>
      <td>Georgia</td>
    </tr>
  </tbody>
</table>
</div>


