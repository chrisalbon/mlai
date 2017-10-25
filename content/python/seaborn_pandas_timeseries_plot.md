Title: Creating A Time Series Plot With Seaborn And Pandas  
Slug: seaborn_pandas_timeseries_plot  
Summary: Creating A Time Series Plot With Seaborn And Pandas  
Date: 2016-05-01 12:00  
Category: Python  
Tags: Data Visualization  
Authors: Chris Albon  

## Preliminaries


```python
import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
data = {'date': ['2014-05-01 18:47:05.069722', '2014-05-01 18:47:05.119994', '2014-05-02 18:47:05.178768', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.280592', '2014-05-03 18:47:05.332662', '2014-05-03 18:47:05.385109', '2014-05-04 18:47:05.436523', '2014-05-04 18:47:05.486877'], 
        'deaths_regiment_1': [34, 43, 14, 15, 15, 14, 31, 25, 62, 41],
        'deaths_regiment_2': [52, 66, 78, 15, 15, 5, 25, 25, 86, 1],
        'deaths_regiment_3': [13, 73, 82, 58, 52, 87, 26, 5, 56, 75],
        'deaths_regiment_4': [44, 75, 26, 15, 15, 14, 54, 25, 24, 72],
        'deaths_regiment_5': [25, 24, 25, 15, 57, 68, 21, 27, 62, 5],
        'deaths_regiment_6': [84, 84, 26, 15, 15, 14, 26, 25, 62, 24],
        'deaths_regiment_7': [46, 57, 26, 15, 15, 14, 26, 25, 62, 41]}
df = pd.DataFrame(data, columns = ['date', 'battle_deaths', 'deaths_regiment_1', 'deaths_regiment_2',
                                   'deaths_regiment_3', 'deaths_regiment_4', 'deaths_regiment_5',
                                   'deaths_regiment_6', 'deaths_regiment_7'])
df = df.set_index(df.date)
```

## Time Series Plot


```python
sns.tsplot([df.deaths_regiment_1, df.deaths_regiment_2, df.deaths_regiment_3, df.deaths_regiment_4,
            df.deaths_regiment_5, df.deaths_regiment_6, df.deaths_regiment_7], color="indianred")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1140be780>




![png](seaborn_pandas_timeseries_plot_files/seaborn_pandas_timeseries_plot_5_1.png)


## Time Series Splot With Confidence Interval Lines But No Lines


```python
sns.tsplot([df.deaths_regiment_1, df.deaths_regiment_2, df.deaths_regiment_3, df.deaths_regiment_4,
            df.deaths_regiment_5, df.deaths_regiment_6, df.deaths_regiment_7], err_style="ci_bars", interpolate=False)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x116400668>




![png](seaborn_pandas_timeseries_plot_files/seaborn_pandas_timeseries_plot_7_1.png)

