Title: Group A Time Series With pandas  
Slug: pandas_group_by_time
Summary: Group A Time Series With pandas 
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Wrangling  
Authors: Chris Albon  

### Import required modules


```python
import pandas as pd
import numpy as np
```

### Create a dataframe


```python
df = pd.DataFrame()

df['german_army'] = np.random.randint(low=20000, high=30000, size=100)
df['allied_army'] = np.random.randint(low=20000, high=40000, size=100)
df.index = pd.date_range('1/1/2014', periods=100, freq='H')

df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-01-01 00:00:00</th>
      <td>28755</td>
      <td>33938</td>
    </tr>
    <tr>
      <th>2014-01-01 01:00:00</th>
      <td>25176</td>
      <td>28631</td>
    </tr>
    <tr>
      <th>2014-01-01 02:00:00</th>
      <td>23261</td>
      <td>39685</td>
    </tr>
    <tr>
      <th>2014-01-01 03:00:00</th>
      <td>28686</td>
      <td>27756</td>
    </tr>
    <tr>
      <th>2014-01-01 04:00:00</th>
      <td>24588</td>
      <td>25681</td>
    </tr>
  </tbody>
</table>
</div>



### Truncate the dataframe


```python
df.truncate(before='1/2/2014', after='1/3/2014')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-01-02 00:00:00</th>
      <td>26401</td>
      <td>20189</td>
    </tr>
    <tr>
      <th>2014-01-02 01:00:00</th>
      <td>29958</td>
      <td>23934</td>
    </tr>
    <tr>
      <th>2014-01-02 02:00:00</th>
      <td>24492</td>
      <td>39075</td>
    </tr>
    <tr>
      <th>2014-01-02 03:00:00</th>
      <td>25707</td>
      <td>39262</td>
    </tr>
    <tr>
      <th>2014-01-02 04:00:00</th>
      <td>27129</td>
      <td>35961</td>
    </tr>
    <tr>
      <th>2014-01-02 05:00:00</th>
      <td>27903</td>
      <td>25418</td>
    </tr>
    <tr>
      <th>2014-01-02 06:00:00</th>
      <td>20409</td>
      <td>25163</td>
    </tr>
    <tr>
      <th>2014-01-02 07:00:00</th>
      <td>25736</td>
      <td>34794</td>
    </tr>
    <tr>
      <th>2014-01-02 08:00:00</th>
      <td>24057</td>
      <td>27209</td>
    </tr>
    <tr>
      <th>2014-01-02 09:00:00</th>
      <td>26875</td>
      <td>33402</td>
    </tr>
    <tr>
      <th>2014-01-02 10:00:00</th>
      <td>23963</td>
      <td>38575</td>
    </tr>
    <tr>
      <th>2014-01-02 11:00:00</th>
      <td>27506</td>
      <td>31859</td>
    </tr>
    <tr>
      <th>2014-01-02 12:00:00</th>
      <td>23564</td>
      <td>25750</td>
    </tr>
    <tr>
      <th>2014-01-02 13:00:00</th>
      <td>27958</td>
      <td>24365</td>
    </tr>
    <tr>
      <th>2014-01-02 14:00:00</th>
      <td>24915</td>
      <td>38866</td>
    </tr>
    <tr>
      <th>2014-01-02 15:00:00</th>
      <td>23538</td>
      <td>33820</td>
    </tr>
    <tr>
      <th>2014-01-02 16:00:00</th>
      <td>23361</td>
      <td>30080</td>
    </tr>
    <tr>
      <th>2014-01-02 17:00:00</th>
      <td>27284</td>
      <td>22922</td>
    </tr>
    <tr>
      <th>2014-01-02 18:00:00</th>
      <td>24176</td>
      <td>32155</td>
    </tr>
    <tr>
      <th>2014-01-02 19:00:00</th>
      <td>23924</td>
      <td>27763</td>
    </tr>
    <tr>
      <th>2014-01-02 20:00:00</th>
      <td>23111</td>
      <td>32343</td>
    </tr>
    <tr>
      <th>2014-01-02 21:00:00</th>
      <td>20348</td>
      <td>28907</td>
    </tr>
    <tr>
      <th>2014-01-02 22:00:00</th>
      <td>27136</td>
      <td>38634</td>
    </tr>
    <tr>
      <th>2014-01-02 23:00:00</th>
      <td>28649</td>
      <td>29950</td>
    </tr>
    <tr>
      <th>2014-01-03 00:00:00</th>
      <td>21292</td>
      <td>26395</td>
    </tr>
  </tbody>
</table>
</div>



### Set the dataframe's index


```python
df.index = df.index + pd.DateOffset(months=4, days=5)
```

### View the dataframe


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06 00:00:00</th>
      <td>28755</td>
      <td>33938</td>
    </tr>
    <tr>
      <th>2014-05-06 01:00:00</th>
      <td>25176</td>
      <td>28631</td>
    </tr>
    <tr>
      <th>2014-05-06 02:00:00</th>
      <td>23261</td>
      <td>39685</td>
    </tr>
    <tr>
      <th>2014-05-06 03:00:00</th>
      <td>28686</td>
      <td>27756</td>
    </tr>
    <tr>
      <th>2014-05-06 04:00:00</th>
      <td>24588</td>
      <td>25681</td>
    </tr>
  </tbody>
</table>
</div>



### Lead a variable 1 hour


```python
df.shift(1).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06 00:00:00</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2014-05-06 01:00:00</th>
      <td>28755.0</td>
      <td>33938.0</td>
    </tr>
    <tr>
      <th>2014-05-06 02:00:00</th>
      <td>25176.0</td>
      <td>28631.0</td>
    </tr>
    <tr>
      <th>2014-05-06 03:00:00</th>
      <td>23261.0</td>
      <td>39685.0</td>
    </tr>
    <tr>
      <th>2014-05-06 04:00:00</th>
      <td>28686.0</td>
      <td>27756.0</td>
    </tr>
  </tbody>
</table>
</div>



### Lag a variable 1 hour


```python
df.shift(-1).tail()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-09 23:00:00</th>
      <td>26903.0</td>
      <td>39144.0</td>
    </tr>
    <tr>
      <th>2014-05-10 00:00:00</th>
      <td>27576.0</td>
      <td>39759.0</td>
    </tr>
    <tr>
      <th>2014-05-10 01:00:00</th>
      <td>25232.0</td>
      <td>35246.0</td>
    </tr>
    <tr>
      <th>2014-05-10 02:00:00</th>
      <td>23391.0</td>
      <td>21044.0</td>
    </tr>
    <tr>
      <th>2014-05-10 03:00:00</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by summing up the value of each hourly observation


```python
df.resample('D').sum()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>605161</td>
      <td>755962</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>608100</td>
      <td>740396</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>589744</td>
      <td>700297</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>607092</td>
      <td>719283</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>103102</td>
      <td>135193</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by averaging up the value of each hourly observation


```python
df.resample('D').mean()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>25215.041667</td>
      <td>31498.416667</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>25337.500000</td>
      <td>30849.833333</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>24572.666667</td>
      <td>29179.041667</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>25295.500000</td>
      <td>29970.125000</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>25775.500000</td>
      <td>33798.250000</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by taking the min value up the value of each hourly observation


```python
df.resample('D').median()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>24882.0</td>
      <td>31310.0</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>25311.0</td>
      <td>30969.5</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>24422.5</td>
      <td>28318.0</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>24941.5</td>
      <td>32082.5</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>26067.5</td>
      <td>37195.0</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by taking the median value of each day's worth of hourly observation


```python
df.resample('D').median()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>24882.0</td>
      <td>31310.0</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>25311.0</td>
      <td>30969.5</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>24422.5</td>
      <td>28318.0</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>24941.5</td>
      <td>32082.5</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>26067.5</td>
      <td>37195.0</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by taking the first value of each day's worth of hourly observation


```python
df.resample('D').first()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>28755</td>
      <td>33938</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>26401</td>
      <td>20189</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>21292</td>
      <td>26395</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>25764</td>
      <td>22613</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>26903</td>
      <td>39144</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by taking the last value of each day's worth of hourly observation


```python
df.resample('D').last()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>german_army</th>
      <th>allied_army</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>28214</td>
      <td>32110</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>28649</td>
      <td>29950</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>28379</td>
      <td>32600</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>26752</td>
      <td>22379</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>23391</td>
      <td>21044</td>
    </tr>
  </tbody>
</table>
</div>



### Aggregate into days by taking the first, last, highest, and lowest value of each day's worth of hourly observation


```python
df.resample('D').ohlc()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">german_army</th>
      <th colspan="4" halign="left">allied_army</th>
    </tr>
    <tr>
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014-05-06</th>
      <td>28755</td>
      <td>29206</td>
      <td>20037</td>
      <td>28214</td>
      <td>33938</td>
      <td>39955</td>
      <td>23417</td>
      <td>32110</td>
    </tr>
    <tr>
      <th>2014-05-07</th>
      <td>26401</td>
      <td>29958</td>
      <td>20348</td>
      <td>28649</td>
      <td>20189</td>
      <td>39262</td>
      <td>20189</td>
      <td>29950</td>
    </tr>
    <tr>
      <th>2014-05-08</th>
      <td>21292</td>
      <td>29786</td>
      <td>20296</td>
      <td>28379</td>
      <td>26395</td>
      <td>38197</td>
      <td>20404</td>
      <td>32600</td>
    </tr>
    <tr>
      <th>2014-05-09</th>
      <td>25764</td>
      <td>29952</td>
      <td>20738</td>
      <td>26752</td>
      <td>22613</td>
      <td>39695</td>
      <td>20189</td>
      <td>22379</td>
    </tr>
    <tr>
      <th>2014-05-10</th>
      <td>26903</td>
      <td>27576</td>
      <td>23391</td>
      <td>23391</td>
      <td>39144</td>
      <td>39759</td>
      <td>21044</td>
      <td>21044</td>
    </tr>
  </tbody>
</table>
</div>


