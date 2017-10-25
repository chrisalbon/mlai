Title: Converting Strings To Datetime  
Slug: strings_to_datetime  
Summary: Converting Strings To Datetime  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Basics  
Authors: Chris Albon  

### Import modules


```python
from datetime import datetime
from dateutil.parser import parse
import pandas as pd
```

### Create a string variable with the war start time


```python
war_start = '2011-01-03'
```

### Convert the string to datetime format


```python
datetime.strptime(war_start, '%Y-%m-%d')
```




    datetime.datetime(2011, 1, 3, 0, 0)



### Create a list of strings as dates


```python
attack_dates = ['7/2/2011', '8/6/2012', '11/13/2013', '5/26/2011', '5/2/2001']
```

### Convert attack_dates strings into datetime format


```python
[datetime.strptime(x, '%m/%d/%Y') for x in attack_dates]
```




    [datetime.datetime(2011, 7, 2, 0, 0),
     datetime.datetime(2012, 8, 6, 0, 0),
     datetime.datetime(2013, 11, 13, 0, 0),
     datetime.datetime(2011, 5, 26, 0, 0),
     datetime.datetime(2001, 5, 2, 0, 0)]



### Use parse() to attempt to auto-convert common string formats


```python
parse(war_start)
```




    datetime.datetime(2011, 1, 3, 0, 0)



### Use parse() on every element of the attack_dates string


```python
[parse(x) for x in attack_dates]
```




    [datetime.datetime(2011, 7, 2, 0, 0),
     datetime.datetime(2012, 8, 6, 0, 0),
     datetime.datetime(2013, 11, 13, 0, 0),
     datetime.datetime(2011, 5, 26, 0, 0),
     datetime.datetime(2001, 5, 2, 0, 0)]



### Use parse, but designate that the day is first


```python
parse(war_start, dayfirst=True)
```




    datetime.datetime(2011, 3, 1, 0, 0)



### Create a dataframe


```python
data = {'date': ['2014-05-01 18:47:05.069722', '2014-05-01 18:47:05.119994', '2014-05-02 18:47:05.178768', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.280592', '2014-05-03 18:47:05.332662', '2014-05-03 18:47:05.385109', '2014-05-04 18:47:05.436523', '2014-05-04 18:47:05.486877'], 
        'value': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
df = pd.DataFrame(data, columns = ['date', 'value'])
print(df)
```

                             date  value
    0  2014-05-01 18:47:05.069722      1
    1  2014-05-01 18:47:05.119994      1
    2  2014-05-02 18:47:05.178768      1
    3  2014-05-02 18:47:05.230071      1
    4  2014-05-02 18:47:05.230071      1
    5  2014-05-02 18:47:05.280592      1
    6  2014-05-03 18:47:05.332662      1
    7  2014-05-03 18:47:05.385109      1
    8  2014-05-04 18:47:05.436523      1
    9  2014-05-04 18:47:05.486877      1


### Convert df['date'] from string to datetime


```python
pd.to_datetime(df['date'])
```




    0   2014-05-01 18:47:05.069722
    1   2014-05-01 18:47:05.119994
    2   2014-05-02 18:47:05.178768
    3   2014-05-02 18:47:05.230071
    4   2014-05-02 18:47:05.230071
    5   2014-05-02 18:47:05.280592
    6   2014-05-03 18:47:05.332662
    7   2014-05-03 18:47:05.385109
    8   2014-05-04 18:47:05.436523
    9   2014-05-04 18:47:05.486877
    Name: date, dtype: datetime64[ns]


