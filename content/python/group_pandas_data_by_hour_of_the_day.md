Title: Group Pandas Data By Hour Of The Day  
Slug: group_pandas_data_by_hour_of_the_day  
Summary: Group data by hour of the day using pandas.  
Date: 2016-12-21 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

## Preliminaries


```python
# Import libraries
import pandas as pd
import numpy as np
```

## Create Data


```python
# Create a time series of 2000 elements, one very five minutes starting on 1/1/2000
time = pd.date_range('1/1/2000', periods=2000, freq='5min')

# Create a pandas series with a random values between 0 and 100, using 'time' as the index
series = pd.Series(np.random.randint(100, size=2000), index=time)
```

## View Data


```python
# View the first few rows of the data
series[0:10]
```




    2000-01-01 00:00:00    40
    2000-01-01 00:05:00    13
    2000-01-01 00:10:00    99
    2000-01-01 00:15:00    72
    2000-01-01 00:20:00     4
    2000-01-01 00:25:00    36
    2000-01-01 00:30:00    24
    2000-01-01 00:35:00    20
    2000-01-01 00:40:00    83
    2000-01-01 00:45:00    44
    Freq: 5T, dtype: int64



## Group Data By Time Of The Day


```python
# Group the data by the index's hour value, then aggregate by the average
series.groupby(series.index.hour).mean()
```




    0     50.380952
    1     49.380952
    2     49.904762
    3     53.273810
    4     47.178571
    5     46.095238
    6     49.047619
    7     44.297619
    8     53.119048
    9     48.261905
    10    45.166667
    11    54.214286
    12    50.714286
    13    56.130952
    14    50.916667
    15    42.428571
    16    46.880952
    17    56.892857
    18    54.071429
    19    47.607143
    20    50.940476
    21    50.511905
    22    44.550000
    23    50.250000
    dtype: float64


