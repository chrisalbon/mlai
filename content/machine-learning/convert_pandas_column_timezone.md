Title: Convert pandas Column's Time Zone  
Slug: convert_pandas_column_timezone  
Summary: How to convert the time zone of a pandas column/series in Python.     
Date: 2017-09-11 12:00  
Category: Machine Learning  
Tags: Preprocessing Dates And Times    
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
import pandas as pd
from pytz import all_timezones
```

## View Timezones


```python
# Show ten time zones
all_timezones[0:10]
```




    ['Africa/Abidjan',
     'Africa/Accra',
     'Africa/Addis_Ababa',
     'Africa/Algiers',
     'Africa/Asmara',
     'Africa/Asmera',
     'Africa/Bamako',
     'Africa/Bangui',
     'Africa/Banjul',
     'Africa/Bissau']



## Create pandas Series Of Dates


```python
# Create ten dates
dates = pd.Series(pd.date_range('2/2/2002', periods=10, freq='M'))
```

## Add Time Zone Of pandas Series


```python
# Set time zone
dates_with_abidjan_time_zone = dates.dt.tz_localize('Africa/Abidjan')

# View pandas series
dates_with_abidjan_time_zone
```




    0   2002-02-28 00:00:00+00:00
    1   2002-03-31 00:00:00+00:00
    2   2002-04-30 00:00:00+00:00
    3   2002-05-31 00:00:00+00:00
    4   2002-06-30 00:00:00+00:00
    5   2002-07-31 00:00:00+00:00
    6   2002-08-31 00:00:00+00:00
    7   2002-09-30 00:00:00+00:00
    8   2002-10-31 00:00:00+00:00
    9   2002-11-30 00:00:00+00:00
    dtype: datetime64[ns, Africa/Abidjan]



## Convert Time Zone Of pandas Series


```python
# Convert time zone
dates_with_london_time_zone = dates_with_abidjan_time_zone.dt.tz_convert('Europe/London')

# View pandas series
dates_with_london_time_zone
```




    0   2002-02-28 00:00:00+00:00
    1   2002-03-31 00:00:00+00:00
    2   2002-04-30 01:00:00+01:00
    3   2002-05-31 01:00:00+01:00
    4   2002-06-30 01:00:00+01:00
    5   2002-07-31 01:00:00+01:00
    6   2002-08-31 01:00:00+01:00
    7   2002-09-30 01:00:00+01:00
    8   2002-10-31 00:00:00+00:00
    9   2002-11-30 00:00:00+00:00
    dtype: datetime64[ns, Europe/London]


