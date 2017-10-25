Title: Convert Strings To Dates  
Slug: convert_strings_to_dates  
Summary: How to convert stings to dates for machine learning in Python.     
Date: 2017-09-11 12:00  
Category: Machine Learning  
Tags: Preprocessing Dates And Times    
Authors: Chris Albon

## Preliminaries


```python
# Load libraries
import numpy as np
import pandas as pd
```

## Create Strings


```python
# Create strings
date_strings = np.array(['03-04-2005 11:35 PM',
                         '23-05-2010 12:01 AM',
                         '04-09-2009 09:09 PM'])
```

## Convert Strings To Timestamps

If `errors="coerce"` then any problem will not raise an error (the default behavior) but instead will set the value causing the error to `NaT` (i.e. a missing value).

<table>
  <tr>
    <th>Code</th>
    <th>Description</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>`%Y`</td>
    <td>Full year</td>
    <td>`2001`</td>
  </tr>
   <tr>
    <td>`%m`</td>
    <td>Month w/ zero padding</td>
    <td>`04`</td>
  </tr>
   <tr>
    <td>`%d`</td>
    <td>Day of the month w/ zero padding</td>
    <td>`09`</td>
  </tr>
  <tr>
    <td>`%I`</td>
    <td>Hour (12hr clock) w/ zero padding</td>
    <td>`02`</td>
  </tr>
  <tr>
    <td>`%p`</td>
    <td>AM or PM</td>
    <td>`AM`</td>
  </tr>
  <tr>
    <td>`%M`</td>
    <td>Minute w/ zero padding</td>
    <td>`05`</td>
  </tr>
  <tr>
    <td>`%S`</td>
    <td>Second w/ zero padding</td>
    <td>`09`</td>
  </tr>
</table>


```python
# Convert to datetimes
[pd.to_datetime(date, format="%d-%m-%Y %I:%M %p", errors="coerce") for date in date_strings]
```




    [Timestamp('2005-04-03 23:35:00'),
     Timestamp('2010-05-23 00:01:00'),
     Timestamp('2009-09-04 21:09:00')]


